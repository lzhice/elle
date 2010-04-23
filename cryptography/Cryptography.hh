//
// ---------- header ----------------------------------------------------------
//
// project       elle
//
// license       infinit
//
// file          /home/mycure/infinit/elle/cryptography/Cryptography.hh
//
// created       julien quintard   [tue oct 30 12:15:12 2007]
// updated       julien quintard   [sat mar 20 01:30:51 2010]
//

#ifndef ELLE_CRYPTOGRAPHY_CRYPTOGRAPHYGRAPHY_HH
#define ELLE_CRYPTOGRAPHY_CRYPTOGRAPHYGRAPHY_HH

//
// ---------- includes --------------------------------------------------------
//

#include <elle/miscellaneous/Status.hh>

#include <elle/cryptography/Cipher.hh>
#include <elle/cryptography/Clear.hh>
#include <elle/cryptography/Code.hh>
#include <elle/cryptography/Digest.hh>
#include <elle/cryptography/KeyPair.hh>
#include <elle/cryptography/OneWay.hh>
#include <elle/cryptography/Plain.hh>
#include <elle/cryptography/PrivateKey.hh>
#include <elle/cryptography/PublicKey.hh>
#include <elle/cryptography/SecretKey.hh>
#include <elle/cryptography/Signature.hh>

#include <elle/idiom/Close.hh>
# include <openssl/engine.h>
# include <openssl/err.h>
# include <openssl/rand.h>
#include <elle/idiom/Open.hh>

namespace elle
{
  using namespace core;
  using namespace miscellaneous;

  ///
  /// this namespace contains everything necessary for performing
  /// cryptographic operations.
  ///
  namespace cryptography
  {

//
// ---------- classes ---------------------------------------------------------
//

    ///
    /// this class represents the cryptography package and provides a
    /// Initialise() method for initialising the package's components.
    ///
    /// this class also provides a general interface for cryptographic
    /// operations.
    ///
    /// note that both Initialize() and Clean() should be called in an
    /// upper sccope to any other cryptographic operations. indeed, otherwise,
    /// the Clean() would release every resource and would prevents live
    /// cryptograhic object from being properly deleted since destructors
    /// usually call _free() functions and those will no longer work after
    /// Clean() has been called.
    ///
    /// the same is true for static objects. since those objects will be
    /// deleted when the application stops and since Clean() will probably
    /// have been called, hence before, these static objects will never be
    /// properly deleted. one should therefore avoid using such static
    /// objects or use static pointers with initialization and cleaning
    /// methods.
    ///
    /// note that Initialize() and Clean() should be called from a single
    /// thread as, obviously, these method are *not* thread-safe.
    ///
    class Cryptography
    {
    public:
      //
      // static methods
      //
      static Status		Initialize();
      static Status		Clean();
    };

  }
}

#endif
