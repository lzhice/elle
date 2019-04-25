# Copyright (C) 2011-2019, Quentin "mefyl" Hocquet
#
# This software is provided "as is" without warranty of any kind,
# either expressed or implied, including but not limited to the
# implied warranties of fitness for a particular purpose.
#
# See the LICENSE file for more information.

import drake

class SDK(drake.Configuration):

  """Configuration for the Air SDK."""

  def __init__(self, prefix = None):
    """Find and create a configuration for the Air SDK.

    prefix -- Where to find the Air SDK, should contain bin/adl.
    """
    # Compute the search path.
    if prefix is None:
      test = [drake.Path('/usr'), drake.Path('/usr/local')]
    else:
      test = [drake.Path(prefix)]
    self.__prefix = self._search_all('bin/adl', test)[0]

  def adl(self):
    return self.__prefix / 'bin/adl'

  def prefix(self):
    return self.__prefix

  def __repr__(self):
    return 'Air(prefix = %s)' % repr(self.__prefix)

  def runtime_nodes(self):
    res = []
    res.append('bin/adl')
    res.append('bin/adt')
    res.append('lib/nai/bin/naip')
    res.append('lib/smali.jar')
    res.append('lib/adt.jar')
    res.append('lib/android/bin/adb')
    res.append('lib/baksmali.jar')
#    res.append('samples/badge/red_badge.html')
#    res.append('samples/badge/AIRBadge.as')
#    res.append('samples/badge/test.jpg')
#    res.append('samples/badge/readme.txt')
#    res.append('samples/badge/default_badge.html')
#    res.append('samples/badge/AC_RunActiveContent.js')
#    res.append('samples/badge/badge.fla')
#    res.append('samples/badge/badge.swf')
#    res.append('samples/icons/AIRApp_16.png')
#    res.append('samples/icons/AIRApp_32.png')
#    res.append('samples/icons/AIRApp_48.png')
#    res.append('samples/icons/AIRApp_128.png')
#    res.append('samples/descriptor-sample.xml')
    res.append('frameworks/libs/air/AIRLocalizer.js')
    res.append('frameworks/libs/air/AIRMenuBuilder.js')
    res.append('frameworks/libs/air/AIRAliases.js')
    res.append('frameworks/libs/air/AIRSourceViewer.js')
    res.append('frameworks/libs/air/aircore.swc')
    res.append('frameworks/libs/air/aircore.swf')
    res.append('frameworks/libs/air/applicationupdater_ui.swc')
    res.append('frameworks/libs/air/applicationupdater_ui.swf')
    res.append('frameworks/libs/air/AIRIntrospector.js')
    res.append('frameworks/libs/air/servicemonitor.swc')
    res.append('frameworks/libs/air/servicemonitor.swf')
    res.append('frameworks/libs/air/applicationupdater.swc')
    res.append('frameworks/libs/air/applicationupdater.swf')
    res.append('frameworks/libs/air/airglobal.abc')
    res.append('frameworks/libs/air/airglobal.swc')
    res.append('frameworks/projects/air/Core/src/air/net/ServiceMonitor.as')
    res.append('frameworks/projects/air/Core/src/air/net/URLMonitor.as')
    res.append('frameworks/projects/air/Core/src/air/net/SocketMonitor.as')
    res.append('frameworks/projects/air/Core/src/air/net/SecureSocketMonitor.as')
    res.append('frameworks/projects/air/Core/src/air/desktop/URLFilePromise.as')
    res.append('frameworks/projects/air/Core/manifest-servicemonitor.xml')
    res.append('frameworks/projects/air/Core/manifest.xml')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/ui/ResourceManagerReflection.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/ui/EmbeddedUILoader.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/ui/UpdaterUI.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/net/FileDownloader.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/core/AIRUnpackager.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/core/UpdaterConfiguration.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/core/UpdaterHSM.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/core/UCFUnpackager.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/core/UpdaterState.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/ApplicationUpdaterUI.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/utils/FileUtils.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/utils/VersionUtils.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/utils/NetUtils.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/utils/Constants.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/utils/StringUtils.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/logging/Level.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/logging/Logger.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/descriptors/ApplicationDescriptor.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/descriptors/ConfigurationDescriptor.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/descriptors/StateDescriptor.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/descriptors/UpdateDescriptor.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/events/StatusFileUpdateEvent.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/events/DownloadErrorEvent.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/events/UpdateEvent.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/events/StatusUpdateErrorEvent.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/events/StatusFileUpdateErrorEvent.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/events/StatusUpdateEvent.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/ApplicationUpdater.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/states/HSMEvent.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/states/HSM.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdater/air/update/states/UpdateState.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/air/update/locale/UpdaterResourceManager.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/com/adobe/utils/LocaleRegistry.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/com/adobe/utils/LocaleId.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/com/adobe/utils/LocaleUtil.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/com/adobe/utils/LocaleParserState.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/skins/SimpleScrollArrowSkin.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/skins/SimpleScrollTrackSkin.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/skins/SimpleScrollThumbSkin.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/skins/SimpleProgressTrackSkin.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterHRule.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterImage.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterLabel.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterCanvas.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/TruncatedLabel.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterSpacer.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterFormItem.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterProgressBar.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterHBox.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterVBox.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterButton.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterTextArea.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterApplication.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterText.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterForm.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/ApplicationUpdaterLinkButton.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/components/OSButtonBarHBox.as')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/Button_Default_overSkin.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/styles4.css')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/Button_Default_upSkin.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/Button_downSkin.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/Button_overSkin.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/Button_upSkin.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/UpdateIcon.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/Button_Default_DisabledSkin.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/Button_disabledSkin.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/button.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/scroll_thumb.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/down_arrow.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/styles.css')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/Button_Default_downSkin.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/assets/right_arrow.png')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/ApplicationUpdaterDialogs.mxml')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/de/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/cs/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/es/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/fr/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/ja/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/it/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/ko/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/nl/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/pl/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/pt/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/ru/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/sv/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/tr/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/en_US/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/zh_Hans/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/src/ApplicationUpdaterDialogs/locale/zh_Hant/ApplicationUpdaterDialogs.properties')
    res.append('frameworks/projects/air/ApplicationUpdater/manifest.xml')
    res.append('frameworks/projects/air/sample-frameworks-build.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/libCore.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/pl.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/libadobecp15.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/application.desktop')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/zh_Hans.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/cs.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/appinstall.spec')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/pt.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/application.directory')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/sv.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/tr.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/zh_Hant.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/libadobecertstore.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/installCertificate')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/appinstall/control')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/appinstall/prerm')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/appinstall/postinst')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/appinstall/copyright')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/ko.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/es.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/appentry')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/Adobe AIR.vch')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/Thawte Root Certificate.cer')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/libaddkey.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/setup.deb')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/ru.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/libWebKit.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/libeggtray.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/en.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/libflashplayer.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/Adobe Root Certificate.cer')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/curl-ca-bundle.crt')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/nl.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/de.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/ja.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/libcurl.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/fr.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/rpmbuilder')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-screensaver')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-mime')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-open')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-autostart')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-user-dir-lookup')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-su')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-icon-resource')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-desktop-icon')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-desktop-menu')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-email')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/xdg-utils/xdg-user-dirs-update')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/libadobecp.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/it.lproj/ContentUIText.xml')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/libpacparser.so')
    res.append('runtimes/air/linux/Adobe AIR/Versions/1.0/Resources/adobecp.vch')
    res.append('runtimes/air/android/device/Runtime.apk')
    res.append('runtimes/air/android/emulator/Runtime.apk')
    res.append('templates/air/Descriptor.1.5.1.xsd')
    res.append('templates/air/Descriptor.1.5.2.xsd')
    res.append('templates/air/Descriptor.1.5.3.xsd')
    res.append('templates/air/descriptor-template.xml')
    res.append('templates/air/Descriptor.1.1.xsd')
    res.append('templates/air/Descriptor.1.5.xsd')
    res.append('templates/air/Descriptor.2.0.xsd')
    res.append('templates/air/Descriptor.2.5.xsd')
    res.append('templates/air/Descriptor.2.6.xsd')
    return list(map(lambda p: drake.Node('%s/%s' % (self.prefix(), p)), res))
