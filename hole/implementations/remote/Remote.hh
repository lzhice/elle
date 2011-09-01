//
// ---------- header ----------------------------------------------------------
//
// project       hole
//
// license       infinit
//
// file          /home/mycure/infinit/hole/implementations/remote/Remote.hh
//
// created       julien quintard   [fri may 20 19:31:08 2011]
// updated       julien quintard   [wed aug 31 14:32:45 2011]
//

#ifndef HOLE_IMPLEMENTATIONS_REMOTE_REMOTE_HH
#define HOLE_IMPLEMENTATIONS_REMOTE_REMOTE_HH

//
// ---------- includes --------------------------------------------------------
//

#include <elle/Elle.hh>

#include <hole/implementations/remote/Client.hh>
#include <hole/implementations/remote/Server.hh>
#include <hole/implementations/remote/Machine.hh>

namespace hole
{
  namespace implementations
  {
    ///
    /// this namespace contains the remote hole implementation.
    ///
    /// note that for this implementation, hole can be run alone so as to
    /// join a network at startup.
    ///
    /// if this network relies on a remote model, the implementation starts
    /// by trying to connect to the server. should this step fail, a server
    /// is spawn in order to wait for connections.
    ///
    /// this way a single implementation emulates both the client and server.
    ///
    namespace remote
    {

//
// ---------- classes ---------------------------------------------------------
//

      ///
      /// the remote hole implementation stores data on a remote host's
      /// storage.
      ///
      class Remote
      {
      public:
	//
	// static attributes
	//
	static Machine*		Computer;
      };

    }
  }
}

//
// ---------- includes --------------------------------------------------------
//

#include <hole/implementations/remote/Customer.hh>
#include <hole/implementations/remote/Implementation.hh>
#include <hole/implementations/remote/Manifest.hh>

#endif
