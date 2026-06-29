# Man / Avahi Autoipd.action

@pkgsysconfdir@/avahi-autoipd.action


        avahi-autoipd.action  is the action script that
      is called whenever an IP address has been acquired by
      avahi-autoipd or when it detected an IP address conflict. The
      script should add or remove the specified address from the
      specified network interface.


          argv[1]  An event string: one of BIND, CONFLICT,
        UNBIND or STOP. If BIND is passed an IP address has been
        successfully acquired and the script shall add it to the
        network interface. If CONFLICT is passed avahi-autopid
        detected a IP address on the local network, the action script
        should remove the configured IP address. If UNBIND is passed
        the IP address should be removed from the interface, too,
        because a routable address has been configured to the
        interface by some other program. If STOP is passed the
        avahi-autoipd is being shutdown and the action script should
        remove the IP address. In short: on BIND the address should be
        added to the interface, on CONFLICT, UNBIND or STOP it should
        be removed.


          argv[2]  The network interface name.


          argv[3]  An IP address from the IPv4LL range.


	   The Avahi Developers  ; Avahi is
	  available from


         ,  ,  ,


	   This man page was written using   by Oliver Kurth.
