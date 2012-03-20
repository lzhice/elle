//
// ---------- header ----------------------------------------------------------
//
// project       nucleus
//
// license       infinit
//
// author        julien quintard   [tue aug  4 06:54:28 2009]
//

#ifndef NUCLEUS_NEUTRON_DATA_HH
#define NUCLEUS_NEUTRON_DATA_HH

//
// ---------- includes --------------------------------------------------------
//

#include <elle/Elle.hh>

#include <nucleus/proton/Contents.hh>
#include <nucleus/proton/State.hh>

#include <nucleus/neutron/Offset.hh>

namespace nucleus
{
  namespace neutron
  {

//
// ---------- classes ---------------------------------------------------------
//

    ///
    /// this class represents a file's content.
    ///
    /// note that the Data does not derive the Block class. indeed, the
    /// Contents class represents the container for genre-specific content:
    /// Catalog for directories, Data for files etc.
    ///
    class Data:
      public elle::Object
    {
    public:
      //
      // constructors & destructors
      //

      // XXX
      proton::Contents<Data>& contents;
      Data(proton::Contents<Data>& contents): contents(contents) {}

      //
      // methods
      //

      // XXX[to remove]
      elle::Status Create() { elle::StatusOk; }

      elle::Status      Write(const Offset&,
                              const elle::Region&);
      elle::Status      Read(const Offset&,
                             const Size&,
                             elle::Region&) const;
      elle::Status      Adjust(const Size&);

      elle::Status      Capacity(Size&) const;

      //
      // interfaces
      //

      // dumpable
      elle::Status      Dump(const elle::Natural32 = 0) const;

      // archivable
      elle::Status      Serialize(elle::Archive&) const;
      elle::Status      Extract(elle::Archive&);

      //
      // attributes
      //
      proton::State     state;
      elle::Region      region;
    };

  }
}

#endif
