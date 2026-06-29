# Man / Avahi Dnsconfd

avahi-dnsconfd [ options ]
       avahi-dnsconfd  --kill
       avahi-dnsconfd  --refresh
       avahi-dnsconfd  --check


       avahi-dnsconfd connects to a running avahi-daemon and runs
      the script  @pkgsysconfdir@/avahi-dnsconfd.action  for each unicast DNS
      server that is announced on the local LAN. This is useful for
      configuring unicast DNS servers in a DHCP-like fashion with
      mDNS.


		  -D | --daemonize
		  Daemonize after startup and redirect log messages to syslog.


          -s | --syslog
          Log to syslog instead of STDERR. Implied by  --daemonize .


		  -k | --kill
		  Kill an already running avahi-dnsconfd. (equivalent to sending a SIGTERM)


		  -r | --refresh
		  Tell an already running avahi-dnsconfd to refresh the DNS server data. (equivalent to sending a SIGHUP)


		  -c | --check
		  Return 0 as return code when avahi-dnsconfd is already running.


		  -h | --help
		  Show help


		  -v | --version
		  Show version information


        @pkgsysconfdir@/avahi-dnsconfd.action : the script to run when a DNS server is found or removed.


        SIGINT, SIGTERM : avahi-dnsconfd will shutdown. This is issued by passing --kill to avahi-daemon.
        SIGHUP : avahi-dnsconfd will refresh the DNS server data.


	   The Avahi Developers  ; Avahi is
	  available from


         ,


	   This man page was written using   by Oliver Kurth.
