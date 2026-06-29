# Man / Avahi Resolve

avahi-resolve --name  host-name ...
       avahi-resolve-host-name  host-name ...
       avahi-resolve --address  address ...
       avahi-resolve-address  address ...


       Resolve one or more mDNS/DNS host name(s) to IP address(es) (and vice versa) using the Avahi daemon.


       When passing -n, specify one or more fully qualified mDNS/DNS host name(s)
      (e.g. "foo.local") to resolve into IP addresses on the command line.

       When passing -a, specify one or more IP addresses
      to resolve into host names. When  enable-wide-area  is
      set to yes in  ,
      reverse lookups will go over unicast DNS first and fallback to mDNS.

       avahi-resolve-host-name is equivalent to avahi-resolve --name.

       avahi-resolve-address is equivalent to avahi-resolve --address.


		  -n | --name
		  Translate one or more fully qualified host names into addresses.


		  -a | --address
		  Translate one or more addresses into fully qualified host names.


          -v | --verbose
          Enable verbose mode.


          -6
          When resolving a host name, look for IPv6 addresses exclusively.


          -4
          When resolving a host name, look for IPv4 addresses exclusively.


		  -h | --help
		  Show help.


		  -V | --version
		  Show version information.


	   The Avahi Developers  ; Avahi is
	  available from


         ,


	   This man page was written using   by Oliver Kurth.
