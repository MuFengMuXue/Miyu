# Man / Avahi Dnsconfd.action

@pkgsysconfdir@/avahi-dnsconfd.action


        avahi-dnsconfd.action  is the action script that
      is called whenever a new unicast DNS server is found or
       removed by avahi-dnsconfd. The default script as shipped
      with avahi patches  /etc/resolv.conf  to reflect the
      changed unicast DNS server configuration.


          argv[1]  Contains the character "+" if the DNS server is new, "-" when it shall be removed from the DNS server list.


          argv[2]  The IP address of the DNS server.


          argv[3]  Numerical network interface number this DNS server was found on.


          argv[4]  Numerical protocol number this DNS server was found on. (usually 2 for IPv4 and 10 for IPv6)


          AVAHI_INTERFACE  Contains the textual interface name the corresponds with argv[3]. (e.g. "eth0")


         AVAHI_INTERFACE_DNS_SERVERS  Contains a
      list of all DNS servers that avahi-dnsconfd found on the
      interface  $AVAHI_INTERFACE , separated by
      spaces.

         AVAHI_DNS_SERVERS  Contains a list of all
      DNS server that avahi-dnsconfd found on all interfaces,
      separated by spaces.


	   The Avahi Developers  ; Avahi is
	  available from


         ,


	   This man page was written using   by Oliver Kurth.
