//
// ---------- header ----------------------------------------------------------
//
// project       elle
//
// license       infinit
//
// file          /home/mycure/infinit/elle/core/Core.hh
//
// created       julien quintard   [fri jan 30 16:14:39 2009]
// updated       julien quintard   [sat mar 20 02:41:04 2010]
//

#ifndef ELLE_CORE_CORE_HH
#define ELLE_CORE_CORE_HH

namespace elle
{
  ///
  /// this namespace contains everything related to the core components
  /// such as basic types.
  ///
  namespace core
  {

//
// ---------- core -----------------------------------------------------------
//

    ///
    /// this class provides two methods for enabling the programmer to
    /// retrieve capacity properties according to a variable instead
    /// of a type.
    ///
    class Variable
    {
    public:
      //
      // methods
      //
      template <typename T>
      static T		Minimum(const T&);

      template <typename T>
      static T		Maximum(const T&);
    };

  }
}

//
// ---------- includes --------------------------------------------------------
//

#include <elle/core/Boolean.hh>
#include <elle/core/Character.hh>
#include <elle/core/Integer.hh>
#include <elle/core/Large.hh>
#include <elle/core/Meta.hh>
#include <elle/core/Natural.hh>
#include <elle/core/Null.hh>
#include <elle/core/Entity.hh>
#include <elle/core/Real.hh>
#include <elle/core/String.hh>

//
// ---------- templates -------------------------------------------------------
//

#include <elle/core/Core.hxx>

#endif
