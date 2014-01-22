#ifndef INFINIT_REACTOR_NETWORK_SOCKET_HH
# define INFINIT_REACTOR_NETWORK_SOCKET_HH

# include <elle/Buffer.hh>
# include <elle/IOStream.hh>
# include <elle/attribute.hh>
# include <elle/network/Locus.hh>

# include <reactor/asio.hh>
# include <reactor/duration.hh>
# include <reactor/mutex.hh>
# include <reactor/network/fwd.hh>
# include <reactor/network/Protocol.hh>

namespace reactor
{
  namespace network
  {
    template <typename AsioSocket>
    class SocketOperation;

    class Socket:
      public elle::IOStream
    {
      /*---------.
      | Typedefs |
      `---------*/
      public:
        /// Self type.
        typedef Socket Self;

      /*----------.
      | Constants |
      `----------*/
      public:
        static size_t const buffer_size;

      /*-------------.
      | Construction |
      `-------------*/
      public:
        /// Create an unbound socket.
        Socket();
        /// Destroy a socket.
        virtual
        ~Socket();
        /** Create a socket for the given protocol.
         *  @param protocol The transport protocl to use.
         */
        static
        std::unique_ptr<Socket>
        create(Protocol protocol,
               const std::string& hostname,
               int port,
               DurationOpt connection_timeout);
        void
        _pacify_streambuffer();

      /*-----------.
      | Properties |
      `-----------*/
      public:
        virtual
        boost::asio::ip::tcp::endpoint
        peer() const = 0;

        virtual
        boost::asio::ip::tcp::endpoint
        local_endpoint() const = 0;

      /*------.
      | Write |
      `------*/
      public:
        virtual
        void
        write(elle::ConstWeakBuffer buffer) = 0;

    /*-----.
    | Read |
    `-----*/
    public:
      virtual
      void
      read(Buffer buffer, DurationOpt timeout = DurationOpt());

      virtual
      Size
      read_some(Buffer buffer, DurationOpt timeout = DurationOpt()) = 0;

      elle::Buffer
      read(Size size, DurationOpt timeout = DurationOpt());

      elle::Buffer
      read_some(Size size, DurationOpt timeout = DurationOpt());

     /*----------------.
     | Pretty printing |
     `----------------*/
      public:
        virtual
        void
        print(std::ostream& s) const = 0;
    };
    std::ostream& operator << (std::ostream& s, const Socket& socket);

    template <typename AsioSocket_,
              typename EndPoint_ = typename AsioSocket_::endpoint_type>
    class PlainSocket:
      public Socket
    {
    /*---------.
    | Typedefs |
    `---------*/
    public:
      /// Self type.
      typedef PlainSocket<AsioSocket_, EndPoint_> Self;
      /// Super type.
      typedef Socket Super;
      /// Underlying asio socket type.
      typedef AsioSocket_ AsioSocket;
      /// End point type for the asio socket type.
      typedef EndPoint_ EndPoint;

    /*-------------.
    | Construction |
    `-------------*/
    protected:
      /// Create and connect socket.
      PlainSocket(std::unique_ptr<AsioSocket> socket,
                  EndPoint const& peer,
                  DurationOpt timeout);
      /// Create wrapping socket.
      PlainSocket(std::unique_ptr<AsioSocket> socket,
                  EndPoint const& peer);
      /// Destroy a socket.
      virtual
      ~PlainSocket();

    /*-----------.
    | Connection |
    `-----------*/
    public:
      void
      close();
    private:
      void
      _connect(EndPoint const& peer, DurationOpt timeout);
      void
      _disconnect();

    /*-----------.
    | Properties |
    `-----------*/
    public:
      EndPoint
      peer() const;

      EndPoint
      local_endpoint() const;

    /*----------------.
    | Pretty printing |
    `----------------*/
    public:
      virtual
      void
      print(std::ostream& s) const;

    /*------------.
    | Asio socket |
    `------------*/
    protected:
      friend class FingerprintedSocket;
      friend class SSLSocket;
      friend class SSLServer;
      friend class TCPServer;
      friend class TCPSocket;
      template <typename AsioSocket>
      friend class SocketOperation;
      ELLE_ATTRIBUTE_R(std::unique_ptr<AsioSocket>, socket);
      EndPoint _peer;
    };

    template <typename AsioSocket,
              typename EndPoint = typename AsioSocket::endpoint_type>
    class StreamSocket:
      public PlainSocket<AsioSocket, EndPoint>
    {
    /*---------.
    | Typedefs |
    `---------*/
    public:
      /// Self type.
      typedef StreamSocket<AsioSocket, EndPoint> Self;
      /// Super type.
      typedef PlainSocket<AsioSocket, EndPoint> Super;

    /*-------------.
    | Construction |
    `-------------*/
    public:
      // XXX: gcc 4.7 can't use parent's constructor.
      StreamSocket(std::unique_ptr<AsioSocket> socket,
                   EndPoint const& peer,
                   DurationOpt timeout):
        Super(std::move(socket), peer, timeout)
      {}

      // XXX: gcc 4.7 can't use parent's constructor.
      StreamSocket(std::unique_ptr<AsioSocket> socket,
                   EndPoint const& peer):
        Super(std::move(socket), peer)
      {}

      virtual
      ~StreamSocket();

    /*-----.
    | Read |
    `-----*/
    public:
      using Super::read;
      virtual
      void
      read(Buffer buffer, DurationOpt timeout = DurationOpt());
      using Super::read_some;
      virtual
      Size
      read_some(Buffer buffer, DurationOpt timeout = DurationOpt());

      elle::Buffer
      read_until(std::string const& delimiter, DurationOpt opt = DurationOpt());

    private:
      virtual
      Size
      _read(Buffer buffer, DurationOpt timeout, bool some);

      ELLE_ATTRIBUTE(boost::asio::streambuf, streambuffer);

    /*------.
    | Write |
    `------*/
    public:
      virtual
      void
      write(elle::ConstWeakBuffer buffer);

    private:
      ELLE_ATTRIBUTE(Mutex, write_mutex);

    /*-----------------.
    | Concrete sockets |
    `-----------------*/
    protected:
      friend class TCPServer;
      friend class TCPSocket;
      // friend class UDPServer;
      // friend class UDPSocket;
    };
  }
}

#endif
