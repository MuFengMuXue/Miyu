# Man / Avahi Bookmarks

avahi-bookmarks


       A web service for listing HTTP services that are announced
      via mDNS/DNS-SD using the Avahi daemon. avahi-bookmarks opens a
      TCP socket on port 8080 and waits for incoming HTTP connections
      returning a dynamic web site containing links to all services of
      type _http._tcp on the LAN. Point your browser to
      http://localhost:8080/ to make use of avahi-bookmarks.


          -p | --port=   PORT
          Specify a TCP port number to listen on. If omitted defaults to 8080.


          -a | --address=   address
          Specify an IP address to listen on. If omitted defaults to 127.0.0.1. Specify 0.0.0.0 if you want to allow remote access.


          -H | --host-names
          Create links pointing to mDNS host names instead
        of resolved IP addresses. This is only compatible with your
        browser if you run some kind of local NSS module to resolve
        mDNS host names (e.g. nss-mdns). If both -A and -H are omitted
        avahi-bookmarks detects whether NSS support is available
        locally. This option conflicts with -A.


          -A | --addresses
          Create links pointing to numeric IP addresses
        instead of mDNS host names. This will break access to hosts
        running virtual servers. If both -A and -H are omitted
        avahi-bookmarks detects whether NSS support is available
        locally. This option conflicts with -H.


          -d | --domain = DOMAIN
          The domain to browse for services in.


		  -h | --help
		  Show help


	   The Avahi Developers  ; Avahi is
	  available from


         ,


	   This man page was written using   by Oliver Kurth.
