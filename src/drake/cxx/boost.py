# Copyright (C) 2009-2011, Quentin "mefyl" Hocquet
#
# This software is provided "as is" without warranty of any kind,
# either expressed or implied, including but not limited to the
# implied warranties of fitness for a particular purpose.
#
# See the LICENSE file for more information.

import drake
import drake.cxx
import itertools
import sys

from .. import Exception, Path, Version
from .  import Config, StaticLib

def find(prefix = None,
         cxx_toolkit = None,
         version = Version(),
         prefer_shared = True):
  if isinstance(prefix, Boost):
    if prefix.version not in version:
      raise Exception('given Boost %s does not fit '
                      'the requested version %s' %
                      (prefix.version, version))
    return prefix
  else:
    return Boost(prefix = prefix,
                 cxx_toolkit = cxx_toolkit,
                 version = version,
                 prefix_shared = prefer_shared)

class Boost(drake.Configuration):

  """Configuration for the Boost C++ library collection"""

  __libraries = {
    'test': 'unit_test_framework',
    'thread': 'thread',
    'system': 'system',
    'filesystem': 'filesystem',
    'signals': 'signals',
    'date_time': 'date_time',
    'regex': 'regex',
    'program_options': 'program_options',
    'chrono': 'chrono',
    'iostreams': 'iostreams',
    'python': ('python3', 'python-3.2')
    }

  def __init__(self,
               cxx_toolkit = None,
               prefix = None,
               version = Version(),
               prefer_shared = True):
    """Find and create a configuration for Boost.

    prefix -- Where to find Boost, should contain
              include/boost/version.hpp among others. /usr and
              /usr/local are searched by default. If relative, it
              is rooted in the source tree.
    version -- Requested version.
    prefer_shared -- Check dynamic libraries first.
    """
    # Fix arguments
    cxx_toolkit = cxx_toolkit or drake.cxx.Toolkit()
    self.__cxx_toolkit = cxx_toolkit
    self.__prefer_shared = prefer_shared
    # Compute the search path.
    if prefix is None:
      if cxx_toolkit.os == drake.os.windows:
        test = [Path('C:\\Boost')]
      else:
        test = [Path('/usr'), Path('/usr/local')]
    else:
      test = [Path(prefix)]
    for i in range(len(test)):
      if not test[i].absolute():
        test[i] = drake.path_source() / test[i]
    token = drake.Path('boost/version.hpp')
    include_subdirs = {drake.Path('include')}
    for prefix in test:
      for subdir in include_subdirs:
        if not (prefix / subdir).exists():
          continue
        include_subdirs = include_subdirs.union(
          (subdir / p for p in (prefix / subdir).list()
           if p.startswith('boost-')))
    tokens = map(lambda p: p / token, include_subdirs)
    prefixes = self._search_many_all(list(tokens), test)
    miss = []
    # Try every search path
    for path, include_subdir in prefixes:
      include_subdir = include_subdir.without_suffix(token)
      # Create basic configuration for version checking.
      cfg = Config()
      cfg.add_system_include_path(path / include_subdir)
      self.__lib_path = path / 'lib'
      cfg.lib_path(self.__lib_path)
      # Check the version.
      version_eff = cxx_toolkit.preprocess(
          '#include <boost/version.hpp>\nBOOST_VERSION',
          config = cfg)
      version_eff = int(version_eff.split('\n')[-2].strip())
      version_eff = Version(version_eff // 100000,
                            version_eff // 100 % 1000,
                            version_eff % 100)
      if version_eff not in version:
        miss.append(version_eff)
        continue
      # Fill configuration
      self.__prefix = path
      self.__cfg = cfg
      for prop in self.__libraries:
        setattr(self, '_Boost__config_%s_dynamic' % prop, None)
        setattr(self, '_Boost__config_%s_static' % prop, None)
        setattr(self, '_Boost__config_%s_dynamic_header' % prop, None)
        setattr(self, '_Boost__config_%s_static_header' % prop, None)
        setattr(self, '_Boost__%s_dynamic' % prop, None)
        setattr(self, '_Boost__%s_static' % prop, None)
      self.__version = version_eff
      return

    raise Exception('no matching boost for the requested version '
                    '(%s) in %s. Found versions: %s.' % \
                    (version, self._format_search([path for path, include_subdir in prefixes]),
                     ', '.join(map(str, miss))))

  def __find_lib(self, lib, lib_path, cxx_toolkit, static):
    # Suffixes
    suffixes = ['-mt', '']
    if static:
      suffixes.append('-mt-s')
      suffixes.append('-s')
    if isinstance(cxx_toolkit, drake.cxx.VisualToolkit):
      suffix = '-vc%s0-mt-%s_%s' % (cxx_toolkit.version,
                                    self.version.major,
                                    self.version.minor)
      suffixes = [suffix] + suffixes
    mgw = '-mgw-mt-%s_%s' % (self.version.major, self.version.minor)
    suffixes += [mgw]
    # Variants
    variants = ['']
    if lib == 'thread' and cxx_toolkit.os is drake.os.windows:
      variants.append('_win32')
    if isinstance(lib, str):
      lib = (lib,)
    for lib, suffix, variant in itertools.product(lib, suffixes, variants):
      libname = 'boost_%s%s%s' % (lib, variant, suffix)
      tests = []
      if static:
        filename = cxx_toolkit.libname_static(self.__cfg, libname)
        tests.append(lib_path / filename)
      else:
        filename = cxx_toolkit.libname_dyn(self.__cfg, libname)
        tests.append(lib_path / filename)
        tests.append(lib_path / ('%s.%s' % (filename, self.__version)))
      for test in  tests:
        if test.exists():
          return test
    raise Exception(
      'Unable to find %s Boost %s library in %s' % \
      ('static' if static else 'dynamic', lib, lib_path))

  def config(self):
      return self.__cfg

  def __repr__(self):
    return 'Boost(prefix = %s)' % repr(self.__prefix)

  @property
  def version(self):
    return self.__version


for prop, library in Boost._Boost__libraries.items():
  def unclosure(prop, library):
    def library_getter(self, static):
      name = '_Boost__%s_%s' % (prop,
                                'static' if static else 'dynamic')
      if getattr(self, name) is None:
        lib = self._Boost__find_lib(library,
                                    self._Boost__lib_path,
                                    self._Boost__cxx_toolkit,
                                    static = static)
        setattr(self, name, drake.node(lib))
      return getattr(self, name)
    setattr(Boost, '%s_dynamic' % prop,
            property(lambda self: library_getter(self, False)))
    setattr(Boost, '%s_static' % prop,
            property(lambda self: library_getter(self, True)))
    def config_getter(self, static = None, link = True):
      if static is None:
        static = not self._Boost__prefer_shared
      name = '_Boost__config_%s_%s' % \
             (prop, 'static' if static else 'dynamic')
      if getattr(self, name) is None:
        lib = library_getter(self, static)
        c = Config()
        macro = prop.upper()
        macro += static and '_STATIC' or '_DYN'
        c.define('BOOST_%s_LINK' % macro, 1)
        setattr(self, name + '_header', Config(c))
        c.library_add(lib)
        setattr(self, name, Config(c))
      return getattr(self, name + ('_header' if not link else ''))
    setattr(Boost, 'config_%s' % prop, config_getter)
  unclosure(prop, library)
