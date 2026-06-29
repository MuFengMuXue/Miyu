** Tip**\
Also works on a Pi5

## Contents

-   [[1] [Motivation]](#Motivation)
-   [[2] [Overview]](#Overview)
    -   [[2.1] [The Pi4]](#The_Pi4)
    -   [[2.2] [The Pi5]](#The_Pi5)
-   [[3] [Hardware Requirements]](#Hardware_Requirements)
-   [[4] [Setting Up]](#Setting_Up)
    -   [[4.1] [How it works IPv4 Only]](#How_it_works_IPv4_Only)
    -   [[4.2] [Required packages]](#Required_packages)
    -   [[4.3] [Optional extra packages]](#Optional_extra_packages)
    -   [[4.4] [Debugging packages]](#Debugging_packages)
    -   [[4.5] [How it works Additions for IPv6 Only]](#How_it_works_Additions_for_IPv6_Only)
    -   [[4.6] [Voice over IP - Coming Soon]](#Voice_over_IP_-_Coming_Soon)
    -   [[4.7] [How It Works IPv6 Only]](#How_It_Works_IPv6_Only)
-   [[5] [Installing]](#Installing)
    -   [[5.1] [net-misc/dhcpcd]](#net-misc.2Fdhcpcd)
    -   [[5.2] [net-misc/dhcp]](#net-misc.2Fdhcp)
    -   [[5.3] [net-firewall/shorewall]](#net-firewall.2Fshorewall)
    -   [[5.4] [net-dns/unbound]](#net-dns.2Funbound)
    -   [[5.5] [net-dialup/ppp]](#net-dialup.2Fppp)
    -   [[5.6] [net-misc/radvd]](#net-misc.2Fradvd)
    -   [[5.7] [Kernel Options]](#Kernel_Options)
-   [[6] [Putting the Pieces Together - IPv4]](#Putting_the_Pieces_Together_-_IPv4)
    -   [[6.1] [/etc/dhcpcd.conf]](#.2Fetc.2Fdhcpcd.conf)
    -   [[6.2] [/etc/conf.d/net]](#.2Fetc.2Fconf.d.2Fnet)
    -   [[6.3] [/etc/dhcp/dhcpd.conf]](#.2Fetc.2Fdhcp.2Fdhcpd.conf)
    -   [[6.4] [Shorewall - Overview and Planning - IPv4]](#Shorewall_-_Overview_and_Planning_-_IPv4)
    -   [[6.5] [/etc/shorewall/\* - Implementation]](#.2Fetc.2Fshorewall.2F.2A_-_Implementation)
        -   [[6.5.1] [zones]](#zones)
        -   [[6.5.2] [interfaces]](#interfaces)
        -   [[6.5.3] [policy]](#policy)
        -   [[6.5.4] [params]](#params)
        -   [[6.5.5] [snat]](#snat)
        -   [[6.5.6] [rules]](#rules)
        -   [[6.5.7] [shorewall.conf]](#shorewall.conf)
        -   [[6.5.8] [/etc/sysctl.d/router.conf]](#.2Fetc.2Fsysctl.d.2Frouter.conf)
-   [[7] [Putting the Pieces Together - IPv6]](#Putting_the_Pieces_Together_-_IPv6)
    -   [[7.1] [/etc/dhcpcd.conf]](#.2Fetc.2Fdhcpcd.conf_2)
    -   [[7.2] [/etc/radvd.conf]](#.2Fetc.2Fradvd.conf)
    -   [[7.3] [/etc/shorewall6/\* - Implementation]](#.2Fetc.2Fshorewall6.2F.2A_-_Implementation)
        -   [[7.3.1] [zones]](#zones_2)
        -   [[7.3.2] [interfaces]](#interfaces_2)
        -   [[7.3.3] [policy]](#policy_2)
        -   [[7.3.4] [params]](#params_2)
        -   [[7.3.5] [snat]](#snat_2)
        -   [[7.3.6] [rules]](#rules_2)
        -   [[7.3.7] [/etc/sysctl.d/router.conf]](#.2Fetc.2Fsysctl.d.2Frouter.conf_2)
-   [[8] [Starting]](#Starting)
-   [[9] [Debugging]](#Debugging)

## [Motivation]

The price of electricity in the UK has gone up by a factor of four in the last six months (August, 2022).

I have been running a HP Gen 7 Microserver, hosting various KVMs. I\'m just left with my router KVM now. A HP Gen 7 Microserver, with 4x4TB conventional hard drives is overkill to support a single small KVM

Consolidating the router into the [Pi4 Stratum 1 Time Server](https://wiki.gentoo.org/wiki/Pi4_Stratum_1_Time_Server "Pi4 Stratum 1 Time Server") I can switch off the Microserver, saving about 60W on my base load, or about 1.5kW/h per day, or £22.50/month.

## [Overview]

The Raspberry Pi4 is the first Pi with sufficient IO bandwith for a domestic router. Earlier Pis have the USB and Ethernet ports on a single USB2 root hub as thats all the Broadcom CPUs provide. Keep in mind that they were designed as mobile phone chips.

### [The Pi4]

-   SDIO 0 - The mmc card
-   SDIO 1 - WiFi
-   1Gb Ethernet Phy
-   Single lane PCIe - USB Ports (2 x USB3, 2 x USB2)
-   All the usual GPIO

\
By using the on board Ethernet and the USB3 ports, we can have three 1G ethernet ports. All operating at 1G full duplex concurrently may not go too well.

### [The Pi5]

-   SDIO 0 - The mmc card
-   SDIO 1 - WiFi
-   1Gb Ethernet Phy (From the RP1)
-   Four lane PCIe to the RP1 - USB Ports (2 x USB3, 2 x USB2)
-   All the usual GPIO

This is much more suited to three 1Gbit/sec interfaces, as you may need if your ISP provides fibre.

** Tip**\
The method will work on any system with sufficient Ethernet ports

** Important**\
In the UK POTS is going away soon, to be replaced by VoIP. VoIP and QoS will be added real soon now

## [Hardware Requirements]

-   A Pi 4 or Pi 5
-   Two or more USB3 to 1Gb adaptors

** Warning**\
There are a lot of USB2 to 100Mb adaptors advertised as USB3 to 1Gb. Caveat Emptor

[![](/images/thumb/c/c3/Pi4_Router.jpg/300px-Pi4_Router.jpg)](https://wiki.gentoo.org/wiki/File:Pi4_Router.jpg)

[](https://wiki.gentoo.org/wiki/File:Pi4_Router.jpg "Enlarge")

A Pi4 fitted with 3 USB3 to 1GB Ethernet Adaptors

[![](/images/thumb/f/f1/Pi5-router.jpg/300px-Pi5-router.jpg)](https://wiki.gentoo.org/wiki/File:Pi5-router.jpg)

[](https://wiki.gentoo.org/wiki/File:Pi5-router.jpg "Enlarge")

A Pi5 fitted with passive cooling and 3 USB3 to 1GB Ethernet Adaptors

** Tip**\
the coloured tape and binding interface names to MAC addresses allows the adapters to be moved around

Observant readers will notice the GPS hat in the image. These Pis are doing both routing and [GPS time](https://wiki.gentoo.org/wiki/Pi4_Stratum_1_Time_Server "Pi4 Stratum 1 Time Server").

** Note**\
The Pi does not have enough USB3 ports for SSD over USB3 and three USB3 to 1G Ethernet ports. A powered USB3 hub (not shown) is required

## [Setting Up]

Carry out a basic install. Follow the [Raspberry_Pi_Install_Guide](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide "Raspberry Pi Install Guide"). Use the `default/linux/arm64/23.0` profile as the router will be headless. This will be a merged-usr install.

The same userland will work on the Pi4 and Pi5 if its built with Pi4 CFLAGS.

The Pi5 kernel will work on both sets of hardware too.

** Warning**\
The Pi4 normally uses a 4k block size and the Pi5 uses 16k, so swap spaces are not interchangeable.

** Tip**\
The kernel needs to support the RP1 chip for use on a Pi5

### [How it works IPv4 Only]

Traditionally, routers have used an all static setup but domestic internet providers are moving more and more to dynamic set up only, even if the setup never changes.

A router is two loosely coupled interacting systems.

The first system is the internet facing client. It uses [[[net-misc/dhcp]](https://packages.gentoo.org/packages/net-misc/dhcp)[]], to aquire its internet facing settings. This may require PPP support.

The second system is the internal network facing side. This uses [[[net-misc/dhcp]](https://packages.gentoo.org/packages/net-misc/dhcp)[]] to hand out settings to internal systems, [[[net-dns/unbound]](https://packages.gentoo.org/packages/net-dns/unbound)[]] to keep a cache of domain names lookups and a firewall, here [[[net-firewall/shorewall]](https://packages.gentoo.org/packages/net-firewall/shorewall)[]] to control what goes in and out.

### [Required packages]

-   [[[net-dns/unbound]](https://packages.gentoo.org/packages/net-dns/unbound)[]] A caching DNS resolver,
-   [[[net-firewall/shorewall]](https://packages.gentoo.org/packages/net-firewall/shorewall)[]] To generate Netfilter rules without having to do it all the hard way.
-   [[[net-misc/dhcp]](https://packages.gentoo.org/packages/net-misc/dhcp)[]] A DHCP server
-   [[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]] A DHCP client

### [Optional extra packages]

-   [[[net-analyzer/snort]](https://packages.gentoo.org/packages/net-analyzer/snort)[]] For intrusion detection
-   [[[net-dialup/ppp]](https://packages.gentoo.org/packages/net-dialup/ppp)[]] Point-to-Point Protocol support. Required if your ISP delivers your internet using PPP or PPPoE
-   [[[net-misc/radvd]](https://packages.gentoo.org/packages/net-misc/radvd)[]] IPv6 Router Advertisement Daemon. Required for automated IPv6 support
-   [[[net-vpn/wireguard-tools]](https://packages.gentoo.org/packages/net-vpn/wireguard-tools)[]] To support wireguard VPN. If you ever use public WiFi, you need a VPN of some sort.
-   [[[net-wireless/hostapd]](https://packages.gentoo.org/packages/net-wireless/hostapd)[]] The Pi 4 can be a 2.4GHz band WiF Access Point

### [Debugging packages]

Hopefully, these will not be needed, as it will just work.

-   [[[sys-apps/ethtool]](https://packages.gentoo.org/packages/sys-apps/ethtool)[]] Reads and writes Ethernet port hardware options.
-   [[[net-analyzer/tcpdump]](https://packages.gentoo.org/packages/net-analyzer/tcpdump)[]] Ethernet packet capture
-   [[[net-analyzer/traceroute]](https://packages.gentoo.org/packages/net-analyzer/traceroute)[]] Trace the path along a network.

### [How it works Additions for IPv6 Only]

[[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]] aquires some allocations from your delegated prefix for your internal subnets and allocates the first address in each delegated /64 to the router interfaces. [[[net-misc/radvd]](https://packages.gentoo.org/packages/net-misc/radvd)[]] then advertises the router IPv6 address and hosts perform IPv6 auto configuration.

This does mean that until you do something about it all your internal systems, behind NAT on IPv4, are on the big bad public internet on IPv6.

** Warning**\
All IPv6 addresses starting with the digits 2 or 3 are public

### [Voice over IP - Coming Soon]

Full fibre is coming to a street cabinet near me. Openreach say March 2023, so the POTS service is going away, to be replaced by a voice service over the fibre. No more pulse dialling, so our real finger in the hole dialling, 1960s phone won\'t work any more. On the upside, my ISP is offering up to 1Gb downlink over fibre \... for a price.

Its still early days but my Pi router will need to cope with the telephone service too. Somehow I\'ll need IP to DECT. IP to pulse dialling and real ringing would be nice to keep the old phone alive but that needs 48v DC on the line and 50v AC for the ringer.

Voice over IP to DECT is on the TODO list \... unless its already been done and someone would care to add it.

### [How It Works IPv6 Only]

Think of a router as two systems, a client and a server, with a bridge between them. The client faces the outside world. The ISP. It uses [[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]] to aquire the upstream settings automatically for both IPv4 and IPv6. This may also require [[[net-dialup/ppp]](https://packages.gentoo.org/packages/net-dialup/ppp)[]].

With those things in place, [[[net-firewall/shorewall]](https://packages.gentoo.org/packages/net-firewall/shorewall)[]] is the gate keeper on the bridge, determining which packets that are allowed to cross the bridge.

Static configuration of LAN members is still possible for both IPv4 and IPv6. Static configuration of the ISP facing interface is ISP dependent.

## [Installing]

### [][[[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]]]

To aquire our setup from our ISP. No special USE settings are required.

### [][[[[net-misc/dhcp]](https://packages.gentoo.org/packages/net-misc/dhcp)[]]]

To pass out settings to our clients. No special USE settings are required.

### [][[[[net-firewall/shorewall]](https://packages.gentoo.org/packages/net-firewall/shorewall)[]]]

Shorewall is not yet keyworded for arm64. Add `<net-firewall/shorewall-9999 **` to [/etc/portage/package.accept_keywords/shorewall]

**TODO:** After further testing, fix the ::gentoo repo.

### [][[[[net-dns/unbound]](https://packages.gentoo.org/packages/net-dns/unbound)[]]]

Cut down on DNS lookups. No special USE settings are required.

### [][[[[net-dialup/ppp]](https://packages.gentoo.org/packages/net-dialup/ppp)[]]]

Required if your ISP demands it or you use PPP for other reasons. No special USE settings are required.

### [][[[[net-misc/radvd]](https://packages.gentoo.org/packages/net-misc/radvd)[]]]

Required for IPv6 only, to advertise that we are a IPv6 router to enable clients to auto configure for IPv6.

### [Kernel Options]

Choose IPv6 support if its required. The `default/linux/arm64/17.0` profile already provides USE=ipv6 by defaut, so IPv6 support will be included everywhere that its optional.

Add IPv4 Netfilter support.

Add IPv6 Netfilter support.

## [Putting the Pieces Together - IPv4]

The documentation reserved subnets are used for the illustrations that follow.

2001:DB8::/32 Document Prefix

The blocks 192.0.2.0/24 (TEST-NET-1), 198.51.100.0/24 (TEST-NET-2), and 203.0.113.0/24 (TEST-NET-3) are provided for use in documentation.

### [][/etc/dhcpcd.conf]

To be added by others - the authors IPv4 setup is static.

### [][/etc/conf.d/net]

The setup for connecting to the ISP uses PPPoE in the example below.

    modules="iproute2"

    # TODO Map private address ranges to documentation ranges.

    config_green="192.168.100.252/24"

    config_dmz="192.168.10.252/24"

    config_blue="192.168.54.252/24"

    ## Only if your ISP uses PPPoE ##
    # PPPoE will go here
    config_red="null"

    config_ppp0="ppp"
    link_ppp0="red"

    # Roaring Penguin pppoe but its in the kernel now
    plugins_ppp0="pppoe"

    dns_servers_ppp0="xxx.xxx.xxx.xxx
                      xxx.xxx.yyy.xxx"

    # There may be other settings you want, see /usr/share/doc/openrc-*/net.example.bz2

    # for IPv6 only
    config_ppp0="dhcp"

    username_ppp0='Your ISP Username'
    password_ppp0='Your Secret ISP Pass phrase'

    postup()  == "ppp0" ]] && echo 2 > /proc/sys/net/ipv6/conf/ppp0/accept_ra
    # Should not be needed as its done in /etc/sysctl.d/router.conf

    }

** Important**\
There is no default route defined. Shorewall will control what can go where

### [][/etc/dhcp/dhcpd.conf]

IPv4 automatic host configuration server. IPv6 operates differently

    # Set our domain name, if we have one.
    option domain-name "example.com";

    # The upstream Domain Nawe Servers
    option domain-name-servers 203.0.113.100,203.0.113.200;

    authoritative;

    # No service on theses networks
    # IMPORTANT our ISP must be excluded.
    subnet 203.0.113.0/24 netmask 255.255.255.248

    # Our DMZ for our servers. Servers need static IPv4
    subnet 198.51.100.0/24 netmask 255.255.255.0

    # Make addresses in the range 192.0.2.0.120 to 192.0.2.139
    # avaiable via DHCP, with a lease time of 3600 to 14400 sec.
    # Thats a good time for WiFi where things come and go.

    subnet 192.0.2.0/24 netmask 255.255.255.0

    # Tell clients where the router is.
    # Set the Maximum Transmission Unit size to 1492
    # Autodiscovery does not always work.
    # The default is 1500 but PPPoE needs 8 bytes
    # which makes 1492 a good number.

    # Rinse and repeat for other private subnets

Users that have a TFTP server to support PXE booting, for example, for diskless hosts, configure it here.

### [Shorewall - Overview and Planning - IPv4]

Shorewall is big, you just won\'t believe how vastly, hugely, mind-bogglingly big it is. I mean, you may think it\'s a long way down the road to the chemist\'s, but that\'s just peanuts to Shorewall. Shorewall is a \'short cut\' too.

As IPv4 and IPv6 are completely separate network stacks, Shorewall is twice as big as that. It has two separate directories for its configuration files. [/etc/shorewall] and [/etc/shorewall6]

Setting up a firewall is like installing Gentoo. Design decisions are required before you start writing rules.

There are essentially two sorts of firewalls, half open and paranoid.

With half open, everything is allowed out but only responses and things specifically requested are allowed in. That\'s your typical domestic router. It means that if the bad guys get in, they can phone home.

With a paranoid firewall, nothing is allowed in and nothing is allowed out unless its expressly permitted.

Its not possible to cover the configuration that suits your install, so only a few key points will be covered. The zone and interface naming convention has been borrowed from [Smoothwall](https://www.smoothwall.org/about.html#collapse1_10) as that was the first firewall I used.

It helps to draw a diagram to show what is allowed to connect to where.

    # Table below shows firewall setup.  Symbols are
    #       From - To       may not initiate connections
    #       From ? To       connection initiation determined by rules
    #       From / To       its in the same zone - no restrictions

    #-------------------------------------------------------------------------------
    #       fw IP           |       From    |                   To                  |
    #-------------------------------------------------------------------------------
    #                                       |  net  | Green |  Blue |  DMZ  |   fw  |
    #-------------------------------------------------------------------------------
    # 203.0.113.26/29       |  Net          |   /   |   -   |   -   |   ?   |   ?   |
    #-------------------------------------------------------------------------------
    # 198.51.100.0/28       |  Green        |   ?   |   /   |   ?   |   ?   |   ?   |
    #-------------------------------------------------------------------------------
    # 198.51.100.128/28     |  Blue         |   ?   |   -   |   /   |   ?   |   -   |
    #-------------------------------------------------------------------------------
    # 10.10.0.0/16          |  DMZ          |   ?   |   -   |   -   |   /   |   -   |
    #-------------------------------------------------------------------------------
    # All of the Above      |  fw           |   ?   |   -   |   -   |   ?   |   /   |
    #-------------------------------------------------------------------------------

### [][/etc/shorewall/\* - Implementation]

** Important**\
Headings below are file name in [/etc/shorewall/]

Firstly, most of the files can be left untouched. The following is a get-you-going list for IPv4.

#### [zones]

Describe your network zones to Shorewall. The firewall itself is its own zone and is required here.

    ###############################################################################

    #ZONE           TYPE            OPTIONS         IN_OPTIONS      OUT_OPTIONS

    fw              firewall
    green           ipv4
    dmz             ipv4
    blue            ipv4
    net             ipv4

-   green the wired fully protected network. No uninvited inbound connections from anywhere are permitted.
-   blue the protected but untrusted network. e.g. WiFi devices, smart TVs. If You don\'t know what\'s in it, it goes here.
-   dmz for servers. Inbound connections may be permitted here but only if a service is provided on the requested port.
-   net sometimes known as red, is the big bad internet from the ISP.

\
The names are case sensitive and will be used in other files.

\

#### [interfaces]

Tell Shorewall how the zones, defined above, map to interfaces.

    #ZONE   INTERFACE       OPTIONS
    net     ppp0
    dmz     dmz             logmartians=1,nosmurfs
    blue    blue            dhcp,logmartians=1,nosmurfs
    green   green           dhcp,logmartians=1,nosmurfs

** Tip**\
Write udev rules to rename interfaces by MAC Address

\

#### [policy]

The policy is applied when there are no more rules left to test. The default for packets from the net is to DROP them on the floor and log them.

Green is allowed connect to the firewall. This matters if the rules are not correct. Its a headless system that will be administered over ssh. As long an the rules permit it. You can lock yourself out.

Everything else is REJECTed, which gives the sender a nice error message.

The first four LOGLEVEL entries for unwanted packets from the net can be removed once correct operation has been tested. The IPv4 address range has been full for several years so the logs will grow very quickly.

    #SOURCE         DEST            POLICY          LOGLEVEL        RATE

    net             dmz             DROP            $LOG
    net             blue            DROP            $LOG
    net             green           DROP            $LOG
    net             $FW             DROP            $LOG

    green           fw              ACCEPT          $LOG

    # Reject everything else
    # everything that is not explictly allowed is denied
    # locally, we use REJECT as it helps debug

    all             all     REJECT          $LOG

It would be more secure to use REJECT for green to the firewall then to open a port for ssh from a single system in the rules file.

** Tip**\
One system in the green LAN needs to be configured statically so that when dhcpd gets into a mess it can be fixed remotely

#### [params]

Map names to static IP addresses and the like, so that names can be used in rules.

    ### IP addresses where we run particular services
    ### This avoids using name resolution in rules
    ### and at the same time, lets us use names for IP addresses
    # Convention is initial capital letters for parameters

    # Raspberry Pi Timeserver
    Ntp=10.10.10.10

#### [snat]

Source NAT is better known as masquerading as it\'s the magic that makes Network Address Translation work.

    #ACTION                 SOURCE                  DEST            PROTO   PORT    IPSEC   MARK    USER    SWITCH  ORIGDEST        PROBABILITY

    MASQUERADE  198.51.100.0/28   ppp0
    MASQUERADE  198.51.100.128/28 ppp0
    MASQUERADE  10.10.0.0/16 ppp0

#### [rules]

The authors rules file is over 20k, so its not shared here. This is the hard bit. The following snippet is for the green zone only. Rinse and repeat for your other zones.

    ####################################################################################################################################################################
    #ACTION         SOURCE          DEST                    PROTO   DPORT   SPORT           ORIGDEST        RATE            USER    MARK    CONNLIMIT       TIME         HEADERS

    #############################################################
    #### WARNING - Required for remote control of shorewall maybe make this port 222
    ACCEPT          green   fw                      tcp     ssh

    ACCEPT          green   net                     tcp     www
    ACCEPT          green   net                     tcp     https
    ACCEPT          green   net                     udp     domain
    ACCEPT          green   net                     udp     ntp
    ACCEPT          green   net                     tcp     ftp
    ACCEPT          green   net                     tcp     smtp
    ACCEPT          green   net                     tcp     submission
    ACCEPT          green   net                     tcp     514
    ACCEPT          green   net                     tcp     svn
    ACCEPT          green   net                     tcp     hkp
    ACCEPT          green   net                     tcp     pop3s
    ACCEPT          green   net                     udp     imaps
    ACCEPT          green   net                     tcp     imaps
    ACCEPT          green   net                     udp     https
    ACCEPT          green   net                     tcp     64738
    ACCEPT          green   net                     udp     64738
    ACCEPT          green   net                     tcp     8880
    ACCEPT          green   net                     tcp     4242
    ACCEPT          green   net                     udp     9987
    ACCEPT          green   net                     tcp     nicname
    ACCEPT          green   net                     tcp     ircd
    ACCEPT          green   net                     tcp     urd
    ACCEPT          green   net                     tcp     git
    ACCEPT          green   net                     tcp     rsync
    ACCEPT          green   net                     tcp     git

For every outgoing rule here, by default, shorewall creates a rule to allow the response back in. The service names are taken from [/etc/services].

There is no reason to allow a whole zone out. green:IPaddr only allows tho one host at IPaddr to use the rule.

If you run your own servers, some Destination NAT rules are required

    DNAT            net             dmz:$Mail               tcp     smtp
    DNAT            net             dmz:$Shell              tcp     ssh
    DNAT            net             dmz:$Shell              tcp     https
    DNAT            net             dmz:$Web                tcp     http

Notice the use of Mail, Shell and Web for IP addresses in the DMZ.

#### [shorewall.conf]

TODO

#### [][/etc/sysctl.d/router.conf]

Turn on some kernel options that are off by default, even when support is built into the kernel.

    # In order for this file to work properly, you must first
    # enable 'Sysctl support' in the kernel.
    #
    # Look in /proc/sys/ for all the things you can setup.
    #
    # Enable packet forwarding
    net.ipv4.ip_forward = 1

    # Enables source route verification
    net.ipv4.conf.default.rp_filter = 1
    # Enable reverse path
    net.ipv4.conf.all.rp_filter = 1

    # Enable SYN cookies (yum!) Helps defend against syn flooding
    # http://cr.yp.to/syncookies.html
    net.ipv4.tcp_syncookies = 1

## [Putting the Pieces Together - IPv6]

Shorewall6 is completely separate from Shorewall. A long time ago, they were separate packages but the separation idea remains. One day, IPv4 will be switched off but most of the world is not ready for that yet. Feel free to test by blocking IPv4 totally.

### [][/etc/dhcpcd.conf]

** Important**\
ipv6only means what it says. Do nothing for IPv4

    # Use the hardware address of the interface for the Client ID.
    #clientid
    # or
    # Use the same DUID + IAID as set in DHCPv6 for DHCPv4 ClientID as per RFC4361.
    # Some non-RFC compliant DHCP servers do not reply with this set.
    # In this case, comment out duid and enable clientid above.
    duid

    # Persist interface configuration when dhcpcd exits.
    persistent

    # vendorclassid is set to blank to avoid sending the default of
    # dhcpcd-<version>:<os>:<machine>:
    vendorclassid

    # A list of options to request from the DHCP server.
    option domain_name_servers, domain_name, domain_search
    option classless_static_routes

    # Respect the network MTU. This is applied to DHCP routes.
    option interface_mtu

    # Request a hostname from the network
    option host_name

    # Most distributions have NTP support.
    option ntp_servers

    # Rapid commit support.
    # Safe to enable by default because it requires the equivalent option set
    # on the server to actually work.
    option rapid_commit

    # A ServerID is required by RFC2131.
    require dhcp_server_identifier

    # Generate SLAAC address using the Hardware Address of the interface
    #slaac hwaddr
    # OR generate Stable Private IPv6 Addresses based from the DUID
    slaac private

    # Respect the network MTU. This is applied to DHCP routes.
    option interface_mtu

    ipv6only

    allowinterfaces ppp0

    interface ppp0
            IAID 0
            iaid 100

    # Request a DHCPv6 Delegated Prefix for iaid.

    #ia_pd 3 blue green
    # The /64 to define the requested prefix size is the default and should not be required.
    # However some horrible routers get a single bigger prefix and allocate it everywhere.

    ia_pd 3 blue/1/64 green/2/64

The author has a /64 for the IPv6 uplink and a delegated /48 prefix. The `ia_pd 3 blue green` entry causes the ISP to assign two /64 subnets from the /48 delegated prefix to the blue and green interfaces. The other 65534 subnets are not used and dropped by the ISP at their boundary router.

As always, your ISP facing interface my not be ppp0. Modify to suit.

### [][/etc/radvd.conf]

    interface green
    # green - wired

    ;
    };

### [][/etc/shorewall6/\* - Implementation]

** Important**\
Headings below are file name in [/etc/shorewall6/]

#### [zones]

     # a copy of /etc/shorewall/zones with the type changed to ipv6

    ###############################################################################
    #ZONE           TYPE            OPTIONS         IN_OPTIONS         OUT_OPTIONS
    fw              firewall
    green           ipv6
    dmz             ipv6
    blue            ipv6
    net             ipv6

#### [interfaces]

This similar to its IPv4 namesake

    ###############################################################################
    #ZONE           INTERFACE               OPTIONS

    net               ppp0                  tcpflags
    dmz               dmz                   nosmurfs
    blue              blue                  dhcp,nosmurfs
    green             green                 tcpflags

#### [policy]

This similar to its IPv4 namesake too.

    ###############################################################################
    #SOURCE DEST    POLICY      LOGLEVEL  RATE    CONNLIMIT

    net     dmz     DROP            $LOG
    net     blue    DROP            $LOG
    net     green   DROP            $LOG
    net     $FW     DROP            $LOG
    all     all     REJECT          $LOG

Again, once everything works all of the \$LOG levels except the last can be removed. There is not nearly as much log spam on IPv6 as the address space is almost empty.

#### [params]

If you need parameters to help keep your rules file easy to read, define them here.

#### [snat]

NAT is not used with IPv6. NAT on IPv4 was designed to delay the exhaustion of the IPv4 address range.

#### [rules]

This is almost but not quite a copy of its IPv4 counterpart.

    ##############################################################################################################################################################
    #ACTION         SOURCE          DEST            PROTO   DPORT   SPORT   ORIGDEST        RATE    USER    MARK    CONNLIMIT       TIME    HEADERS SWITCH  HELPER

    # All ipv6-icmp to/from anywhere
    ACCEPT          any             any       ipv6-icmp

    # We get our subnets via dhcpcd over pppoe
    ACCEPT      fw      net     udp dhcpv6-server
    ACCEPT      net     fw      udp dhcpv6-client
    ACCEPT          fw              net             tcp     dhcpv6-server
    ACCEPT          net             fw              tcp     dhcpv6-client

When the firewall asks for its IPv6 setup, it uses dhcpv6-server messages. So these must be allowed out. The server responds with dhcpv6-client messages, which are on a different port, so these must be explicitly permitted.

#### [][/etc/sysctl.d/router.conf]

In addition to the IPv4 entries IPv6 requires

    # A very trendy value for a binary flag!
    net.ipv6.conf.ppp0.accept_ra = 2

** Important**\
Change the .ppp0. above to whatever your ISP facing interface name is

## [Starting]

** Tip**\
Build on what you know works - Start things a bit at a time

Set services to start as follows.

                   dhcpcd |      default
                    dhcpd |      default
                 net.blue |      default
                  net.dmz |      default
                net.green |      default
                 net.ppp0 |      default
                  net.red |      default
                    radvd |      default
                shorewall |      default
           shorewall-init | boot
               shorewall6 |      default

shorewall-init makes sure that the firewall is closed when the network interfaces start, to avoid being open to the world between the network interfaces starting and Shorewall starting.

## [Debugging]

There are lots of logs in /var/log. dmesg will be flooded with DROPs due to all the logging.

`shorewall show ...` and `shorewall6 show ...` will be useful too.