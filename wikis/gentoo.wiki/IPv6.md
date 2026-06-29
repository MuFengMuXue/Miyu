**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/IPv6 "wikipedia:IPv6")

[IPv6] is the most recent version of the [Internet Protocol](https://en.wikipedia.org/wiki/Internet_Protocol "wikipedia:Internet Protocol") (IP). A first draft was issued in December 1998, and IPv6 was ratified as an Internet Standard in July 2017.

This page is a general introduction to IPv6. For information about:

-   configuring IPv6 on Gentoo, refer to the [IPv6/Configuration](https://wiki.gentoo.org/wiki/IPv6/Configuration "IPv6/Configuration") page.
-   creating an IPv6 tunnel over IPv4, refer to the [IPv6/IPv6 tunnels](https://wiki.gentoo.org/wiki/IPv6/IPv6_tunnels "IPv6/IPv6 tunnels") page.
-   using Gentoo as an IPv6 router, refer to the [IPv6 router guide](https://wiki.gentoo.org/wiki/IPv6_router_guide "IPv6 router guide") page.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [IPv6 address format]](#IPv6_address_format)
-   [[3] [Link-local addresses]](#Link-local_addresses)
-   [[4] [Neighbor Discovery]](#Neighbor_Discovery)
-   [[5] [IPv6 address blocks]](#IPv6_address_blocks)
-   [[6] [IPv6 multicast addresses]](#IPv6_multicast_addresses)
-   [[7] [RFCs]](#RFCs)
-   [[8] [Transition mechanisms]](#Transition_mechanisms)
    -   [[8.1] [6to4]](#6to4)
    -   [[8.2] [6rd]](#6rd)
    -   [[8.3] [6over4]](#6over4)
    -   [[8.4] [6in4]](#6in4)
    -   [[8.5] [Teredo]](#Teredo)
-   [[9] [External resources]](#External_resources)
-   [[10] [References]](#References)

## [Introduction]

Compared to IPv4, IPv6 provides a significantly larger number of available addresses: IPv4 uses 32-bit addresses, allowing for a total of 2\^32 = 4,294,967,296 addresses, whereas IPv6 uses 128-bit addresses, allowing for a total of 2\^128 = 340,282,366,920,938,463,463,374,607,431,768,211,456 addresses. The IPv4 address space has now been exhausted:

> All RIRs \[Regional Internet Registries\] have exhausted their address pools, except those reserved for IPv6 transition; this occurred on 15 April 2011 for the Asia-Pacific (APNIC), on 10 June 2014 for Latin America and the Caribbean (LACNIC), on 24 September 2015 for North America (ARIN), on 21 April 2017 for Africa (AfriNIC), and on 25 November 2019 for Europe, Middle East and Central Asia (RIPE NCC). These RIRs still allocate recovered addresses or addresses reserved for a special purpose. Individual ISPs still have pools of unassigned IP addresses, and could recycle addresses no longer needed by subscribers.^[\[1\]](#cite_note-1)^

[Carrier-Grade Network Address Translation](https://en.wikipedia.org/wiki/CGNAT "wikipedia:CGNAT") (CGNAT), the [HTTP `Host` header](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields), and [TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security "wikipedia:Transport Layer Security") [Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication "wikipedia:Server Name Indication") have reduced the pressure to move to IPv6^[\[2\]](#cite_note-2)[\[3\]](#cite_note-3)^. However, there are other advantages to IPv6 compared to IPv4, such as:

-   [Multicasting](https://en.wikipedia.org/wiki/IPv6#Multicasting), via which a single send operation can transmit data to multiple destinations, is part of the base specification of IPv6. It\'s only optional in IPv4 ([RFC 1112](https://datatracker.ietf.org/doc/html/rfc1112)), and therefore not guaranteed to be supported.
-   [Stateless address autoconfiguration](https://en.wikipedia.org/wiki/IPv6#Stateless_address_autoconfiguration_(SLAAC)), via which hosts configure their IP address automatically.
-   [Mobile IPv6](https://en.wikipedia.org/wiki/IPv6#Mobility), which avoids the triangular routing required by Mobile IPv4.

There was never an \'IPv5\'. A streaming protocol known as the [Internet Streaming Protocol](https://en.wikipedia.org/wiki/Internet_Streaming_Protocol "wikipedia:Internet Streaming Protocol"), abbreviated as \'ST\', used the IP version 5 ID, but it used the same limited address space as IPv4, and never made it past the draft stage.

## [IPv6 address format]

An individual IPv6 address has the format nnnn:nnnn:nnnn:nnnn:nnnn:nnnn:nnnn:nnnn, where each `n` is a hexadecimal digit. Leading zeroes in each inter-colon group can be removed; thus, a group \'0021\' can be reduced to simply \'21\'. Additionally, a single sequence of inter-colon groups only containing zeroes can be abbreviated to \'::\'. Thus, fe80:0000:0000:0000:0000:0000:000:0001 can be abbreviated to fe80::0001, and even further to fe80::1. Note that the \'::\' abbreviation can only be used once in an address: thus, fe80:0000:0000:1111:0000:0000:0000:0001 can be abbreviated to fe80::1111:0000:0000:0000:0001, fe80::1111:0000:0000:0000:1, fe80:0000:0000:1111::0001 or fe80:0000:0000:1111::1, but *not* fe80::1111::0001.

IPv6 address ranges/blocks are represented using standard [CIDR](https://en.wikipedia.org/wiki/CIDR "wikipedia:CIDR") (Classless Inter-Domain Routing) notation, e.g. fe80::/48; the number after the \'/\' indicates how many bits are allocated to the prefix designating a specific subnetwork.

## [Link-local addresses]

All IPv6 interfaces require a [[link-local] address](https://en.wikipedia.org/wiki/Link-local_address "wikipedia:Link-local address"), i.e. an address only valid on the local network to which a host is connected. IPv6 link-local addresses have the prefix fe80::/10; the first 54 bits after the prefix can be used for subnetting. Bringing an IPv6 interface up will result in a link-local address automatically being generated via [Stateless address autoconfiguration](https://en.wikipedia.org/wiki/IPv6#Stateless_address_autoconfiguration_(SLAAC)) (SLAAC); how this address is generated is implementation-dependent. However, globally routable addresses can also be assigned manually, or by using [DHCPv6](https://en.wikipedia.org/wiki/DHCPv6 "wikipedia:DHCPv6") (cf. [RFC 8415](https://www.rfc-editor.org/info/rfc8415)).

## [Neighbor Discovery]

The [Neighbor Discovery Protocol](https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol "wikipedia:Neighbor Discovery Protocol") (NDP), specified by [RFC 4861](https://datatracker.ietf.org/doc/html/rfc4861). uses five [ICMPv6](https://en.wikipedia.org/wiki/ICMPv6 "wikipedia:ICMPv6") packet types to gather information required for configuring of local connections, domain name servers, and gateways. These packet types provide functionality similar to the IPv4 [Address Resolution Protocol](https://en.wikipedia.org/wiki/Address_Resolution_Protocol "wikipedia:Address Resolution Protocol") (ARP) and [ICMP](https://en.wikipedia.org/wiki/IMCP "wikipedia:IMCP") redirect and router discovery message types.

NDP also includes Neighbor Unreachability Detection (NUD), improving packet delivery in the presence of failing routers, links, or mobile nodes.

## [IPv6 address blocks]

A selection of standard IPv6 address blocks/ranges.

  ----------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Address block     Description                                                                                                                                                                                      RFC(s)
  ::/128            The \'unspecified\' address                                                                                                                                                                      [RFC 4291](https://www.rfc-editor.org/info/rfc4291)
  ::1/128           Loopback address / \'localhost\'                                                                                                                                                                 [RFC 4291](https://www.rfc-editor.org/info/rfc4291)
  ::ffff:0:0/96     IPv4-mapped addresses: an IPv4 address in the form of an IPv6 address                                                                                                                            [RFC 4291](https://www.rfc-editor.org/info/rfc4291)
  ::ffff:0:0:0/96   IPv4 translated addresses, via the Stateless IP/ICMP Translation (SIIT) algorithm                                                                                                                [RFC 2765](https://www.rfc-editor.org/info/rfc2765)
  64:ff9b::/96      IPv4/IPv6 translation                                                                                                                                                                            [RFC 6052](https://datatracker.ietf.org/doc/html/rfc6052), updating [RFC 4291](https://www.rfc-editor.org/info/rfc4291)
  64:ff9b:1::/48    IPv4/IPv6 translation for private networks                                                                                                                                                       [RFC 8215](https://www.rfc-editor.org/info/rfc8215)
  0100::/64         Discard-Only Prefix, for black hole routing                                                                                                                                                      [RFC 6666](https://www.rfc-editor.org/info/rfc6666)
  2000::/3          Global Unicast Address Space ([current allocations](https://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xhtml))   [RFC 4291](https://www.rfc-editor.org/info/rfc4291)
  2001::/32         Teredo tunneling                                                                                                                                                                                 [RFC 4380](https://www.rfc-editor.org/info/rfc4380)
  2001:db8::/32     Addresses for use in examples (e.g. in documentation and code examples)                                                                                                                          [RFC 3849](https://www.rfc-editor.org/info/rfc3849)
  3fff::/20         Addresses for use in examples (e.g. in documentation and code examples); updates RFC 3849                                                                                                        [RFC 9637](https://www.rfc-editor.org/info/rfc9637)
  2002::/16         The deprecated 6to4 addressing scheme                                                                                                                                                            [RFC 7526](https://www.rfc-editor.org/info/rfc7256)
  fc00::/7          [Unique local addresses](https://en.wikipedia.org/wiki/Unique_local_address "wikipedia:Unique local address") (ULAs) for private networks                                                [RFC 4193](https://www.rfc-editor.org/info/rfc4193)
  fe80::/64         Link-local addresses                                                                                                                                                                             [RFC 4291](https://www.rfc-editor.org/info/rfc4291)
  ff00::/8          Multicast addresses                                                                                                                                                                              [RFC 4291](https://www.rfc-editor.org/info/rfc4291)
  ----------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [IPv6 multicast addresses]

The following is a list of *well-known* IPv6 multicast addresses^[\[4\]](#cite_note-4)^.

  ----------------------------- ---------------------------------------------------------------------------------------------------------------
  Address                       Description
  ff02::1                       All nodes
  ff02::2                       All routers
  ff02::5                       All OSPF (Open Shortest Path First) routers
  ff02::6                       All OSPF Designated Routers
  ff02::9                       All RIP (Routing Information Protocol) routers
  ff02::a                       All EIGRP (Enhanced Interior Gateway Routing Protocol) routers
  ff02::d                       All PIM (Protocol Independent Multicast) routers
  ff02::f                       UPNP (Universal Plug and Play) devices
  ff02::11                      All homenet nodes
  ff02::12                      VRRP (Virtual Router Redundancy Protocol)
  ff02::16                      All MLD (Multicast Listener Discovery) v2-capable routers
  ff02::1a                      All RPL (Routing Protocol for Low-Power and Lossy Networks) routers, used in IoT (Internet of Things) devices
  ff02::fb                      Multicast DNS (Domain Name System) IPv6
  ff02::101                     NTP (Network Time Protocol)
  ff02::1:2                     All DHCP (Dynamic Host Configuration Protocol) agents
  ff02::1:3                     LLMNR (Link-Local Multicast Name Resolution)
  ff02:0:0:0:0:1:ff00::/104     Solicited node address
  ff02:0:0:0:0:1-2:ff00::/104   Node information query
  ff05::1:3                     All DHCP servers for site
  ff05::101                     All NTP servers for site
  ----------------------------- ---------------------------------------------------------------------------------------------------------------

## [RFCs]

A selection of current [IETF](https://en.wikipedia.org/wiki/IETF "wikipedia:IETF") [RFCs](https://en.wikipedia.org/wiki/Request_for_Comments "wikipedia:Request for Comments") describing IPv6 standards.

  ------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------
  RFC                                                                                         Title
  [RFC 4291](https://datatracker.ietf.org/doc/html/rfc4291)   IP Version 6 Addressing Architecture
  [RFC 4862](https://datatracker.ietf.org/doc/html/rfc4291)   IPv6 Stateless Address Autoconfiguration
  [RFC 4861](https://datatracker.ietf.org/doc/html/rfc4861)   Neighbor Discovery for IP version 6 (IPv6)
  [RFC 4193](https://datatracker.ietf.org/doc/html/rfc4193)   Unique Local IPv6 Unicast Addresses
  [RFC 4213](https://datatracker.ietf.org/doc/html/rfc4213)   Basic Transition Mechanisms for IPv6 Hosts and Routers
  [RFC 3053](https://datatracker.ietf.org/doc/html/rfc3053)   IPv6 Tunnel Broker
  [RFC 8415](https://datatracker.ietf.org/doc/html/rfc8415)   Dynamic Host Configuration Protocol for IPv6 (DHCPv6)
  [RFC 7943](https://datatracker.ietf.org/doc/html/rfc7943)   A Method for Generating Semantically Opaque Interface Identifiers (IIDs) with the Dynamic Host Configuration Protocol for IPv6 (DHCPv6)
  ------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------

## [Transition mechanisms]

### [6to4]

[6to4](https://en.wikipedia.org/wiki/6to4 "wikipedia:6to4") generates a globally-routable IPv6 address by appending the IPv4 address to 2002::/16. For example, an IPv4 address of 203.0.113.1 has a hexadecimal representation of cb007101, so the 6to4 IPv6 address would be 2002:0000:0000:0000:0000:0000:cb00:7101 (which can be abbreviated to 2002::cb00:7101). It cannot used behind NAT devices (e.g. home routers), should not be used for connecting IPv4-only hosts with IPv6-only hosts (which should be done with [NAT64](https://en.wikipedia.org/wiki/NAT64 "wikipedia:NAT64")), and is often misconfigured.

### [6rd]

[6rd](https://en.wikipedia.org/wiki/IPv6_rapid_deployment "wikipedia:IPv6 rapid deployment"), IPv6 rapid deployment, is derived from 6to4; it operates entirely within the network of an end-user\'s ISP. Each ISP uses one of its own IPv6 prefixes instead of the 6to4 2002::/16 prefix, allowing all its 6rd hosts to be reachable by all IPv6 hosts that can reach the ISP\'s IPv6 network.

### [6over4]

[6over4](https://en.wikipedia.org/wiki/6over4 "wikipedia:6over4") generates a link-local IPv6 address from an IPv4 address, and provide a mechanism to perform Neighbor Discovery on top of IPv4, via IPv4 multicast. The link-local IPv6 address is obtained by appending the IPv4 address to fe80::/96. For example, an IPv4 address of 203.0.113.1 has a hexadecimal representation of cb007101, so the 6over4 IPv6 address would be fe80:0000:0000:0000:0000:0000:cb00:7101 (which can be abbreviated to fe80::cb00:7101).

### [6in4]

[6in4](https://en.wikipedia.org/wiki/6in4 "wikipedia:6in4") is a tunneling protocol which transfers IPv6 packets via specially configured IPv4 links: the endpoints are configured statically.

### [Teredo]

[Teredo](https://en.wikipedia.org/wiki/Teredo_tunnelling "wikipedia:Teredo tunnelling") is a tunneling protocol providing IPv6 connectivity to IPv6-capable hosts which are only on the IPv4 Internet; unlike 6to4, it works even behind NAT devices (e.g. home routers).

## [External resources]

-   [\'IPv6\' article on Wikipedia](https://en.wikipedia.org/wiki/Ipv6)
-   [Introduction to IPv4/IPv6 Translation](https://www.jool.mx/en/intro-xlat.html)

## [References]

1.  [[[↑](#cite_ref-1)] [[Wikipedia:IPv4 address exhaustion](https://en.wikipedia.org/wiki/IPv4_address_exhaustion "wikipedia:IPv4 address exhaustion"). Retrieved on 2024-04-15.]]
2.  [[[↑](#cite_ref-2)] [[The IPv6 Transition](https://www.potaroo.net/ispcol/2024-10/ipv6-transition.html). Retrieved on 2024-10-21.]]
3.  [[[↑](#cite_ref-3)] [[The importance of name-based virtual hosts (websites)](https://utcc.utoronto.ca/~cks/space/blog/web/NameBasedVirtualHostsImportance). Retrieved on 2024-10-28.]]
4.  [[[↑](#cite_ref-4)] [[IPv6 cheat-sheet, part 3: IPv6 multicast](https://www.menandmice.com/blog/ipv6-reference-multicast). Retrieved on 2024-11-18.]]