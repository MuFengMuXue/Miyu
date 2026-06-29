# Domain name resolution

In general, a domain name represents an IP address and is associated to it in the Domain Name System (DNS).
This article explains how to configure domain name resolution and resolve domain names.

## Name Service Switch
The Name Service Switch (NSS) facility is part of the GNU C Library () and backs the  API, used to resolve domain names. NSS allows system databases to be provided by separate services, whose search order can be configured by the administrator in . The database responsible for domain name resolution is the hosts database, for which glibc offers the following services:

* files: reads the  file, see
* dns: the glibc resolver which reads , see

systemd provides three NSS services for hostname resolution:

*  — a caching DNS stub resolver, described in systemd-resolved
*  — provides local hostname resolution without having to edit
*  — provides hostname resolution for the names of local  containers

## Resolve a domain name using NSS
NSS databases can be queried with . A domain name can be resolved through NSS using:

 $ getent ahosts domain_name

## Glibc resolver
The glibc resolver reads  for every resolution to determine the nameservers and options to use.

 lists nameservers together with some configuration options.
Nameservers listed first are tried first, up to three nameservers may be listed. Lines starting with a number sign () are ignored.

## Overwriting of /etc/resolv.conf
Network managers tend to overwrite , for specifics see the corresponding section:

* dhcpcd#/etc/resolv.conf
* Netctl#/etc/resolv.conf
* NetworkManager#/etc/resolv.conf
* ConnMan#/etc/resolv.conf

To prevent programs from overwriting , it is also possible to write-protect it by setting the immutable file attribute:

 # chattr +i /etc/resolv.conf

## Alternative using nmcli
If you use NetworkManager,  can be used to set persistent options for . Change "Wired" to the name of your connection. Example:

 # nmcli con mod Wired +ipv4.dns-options 'rotate,single-request,timeout:1'

For more options have a look at the man pages of ,  and .

## Limit lookup time
If you are confronted with a very long hostname lookup (may it be in pacman or while browsing), it often helps to define a small timeout after which an alternative nameserver is used. To do so, put the following in .

## Hostname lookup delayed with IPv6
If you experience a 5 second delay when resolving hostnames it might be due to a DNS-server/Firewall misbehaving and only giving one reply to a parallel A and AAAA request.You can fix that by setting the following option in :

## Local domain names
To be able to use the hostname of local machine names without the fully qualified domain name, add a line to  with the local domain such as:

That way you can refer to local hosts such as  as simply  when using the ssh command, but the drill command still requires the fully qualified domain names in order to perform lookups.

## Lookup utilities
To query specific DNS servers and DNS/DNSSEC records you can use dedicated DNS lookup utilities or those shipped with DNS servers. These tools implement DNS themselves and do not use NSS.

*
:For example, to query a specific nameserver with drill for the TXT records of a domain:
:Unless a DNS server is specified, drill will use the nameservers defined in .
*
*
*
*
*
*

Some DNS server packages ship with DNS lookup utilities that can be used without running the DNS server:

*  provides  and .
*  provides .
*  provides ,  and .
*  provides .

## Resolver performance
The Glibc resolver does not cache queries. To implement local caching, use systemd-resolved or set up a local caching DNS server and use it as the name server by setting  and  as the name servers in  or in  if using openresolv.

## Privacy and security
The DNS protocol (Do53) is unencrypted and does not account for confidentiality, integrity or authentication, so if you use an untrusted network or a malicious ISP, your DNS queries can be eavesdropped and the responses manipulated. Furthermore, DNS servers can conduct DNS hijacking.

You need to trust your DNS server to treat your queries confidentially. DNS servers are provided by ISPs and third-parties. Alternatively you can run your own recursive name server (a.k.a. recursive resolver, a.k.a. DNS recursor), which however takes more effort. If you use a DHCP client in untrusted networks, be sure to set static name servers to avoid using and being subject to arbitrary DNS servers, or alternatively, use a VPN to connect to a secure network and use its DNS servers. To secure your communication with a remote DNS server you can use an encrypted protocol, provided that both the upstream server and your local resolver support the protocol. Common encrypted DNS protocols are:

* DNS over TLS (DoT)—RFC 7858,
* DNS over HTTPS (DoH)—RFC 8484,
* DNS over QUIC (DoQ)—RFC 9250,
* DNSCrypt.

To verify that responses are actually from authoritative name servers, you can validate DNSSEC, provided that both the upstream server(s) and your local resolver support it.

## TLS Server Name Indication
Although one may use an encrypted DNS resolver, a TLS connection still leaks the domain names in the Server Name Indication (SNI) when requesting the domain certificate. This leak can be checked using the Wireshark filter , or using the following tshark command:

 # tshark -p -Tfields -e tls.handshake.extensions_server_name -Y 'tls.handshake.extensions_server_name_len>0'

A proposed solution is to use the Encrypted Client Hello (ECH), a TLS 1.3 protocol extension.

## Application-level DNS
Be aware that some client software, such as major web browsers[https://support.mozilla.org/en-US/kb/firefox-dns-over-httpsare starting to implement DNS over HTTPS. While the encryption of queries may often be seen as a bonus, it also means the software sidetracks queries around the system resolver configuration.[https://blog.powerdns.com/2019/09/25/centralised-doh-is-bad-for-privacy-in-2019-and-beyond/

Firefox provides configuration options to enable or disable DNS over HTTPS and select a DNS server. Mozilla has setup a Trusted Recursive Resolver (TRR) programme with transparency information on their default providers. It is notable that Firefox supports and automatically enables the Encrypted Client Hello (ECH) for TRR providers, see Firefox/Privacy#Encrypted Client Hello.

Chromium will examine the user's system resolver and enable DNS over HTTPS if the system resolver addresses are known to also provide DNS over HTTPS. See this blog post for more information and how DNS over HTTPS can be disabled.

Mozilla has proposed universally disabling application-level DNS if the system resolver cannot resolve the domain . Currently, this is only implemented in Firefox.

## Oblivious DNS over HTTPS
Oblivious DNS over HTTPS (ODoH)—RFC 9230—is a system which addresses a number of DNS privacy concerns. See Cloudflare's article for more information. It added DNS over HTTPS to the academic Oblivious DNS design. See the Improving the privacy of DNS and DoH with oblivion article for a discussion of the differences.

## Recursive resolver
Communication between recursive resolvers and root servers is not encrypted and the root server operators are against implementing it. For encrypted communication with authoritative servers there is the experimental RFC 9539 which allows the opportunistic use of DNS over TLS and DNS over QUIC.

## Third-party DNS services
There are various third-party DNS services. Wikipedia has a list of "notable" public DNS service operators while the curl project's wiki has a more extensive list of publicly available DNS over HTTPS servers (a lot of which also support DNS over TLS). The  package configures fallback DNS for systemd-resolved when no DNS servers are configured (manually or via DHCP/RA).

You can use dnsperftest to test the performance of the most popular DNS resolvers from your location. dnsperf.com provides global benchmarks between providers.

## Third-party DNS client software
Some DNS services also provide dedicated software:

*
*

## DNS servers
DNS servers can be authoritative and recursive. If they are neither, they are called stub resolvers and simply forward all queries to another recursive name server. Stub resolvers are typically used to introduce DNS caching on the local host or network. Note that the same can also be achieved with a fully-fledged name server. This section compares the available DNS servers, for a more detailed comparison, refer to Wikipedia:Comparison of DNS server software.

{| class="wikitable sortable" style="text-align:center"
! rowspan=2 | Name !! rowspan=2 | Package !! colspan=4 | Capabilities !! rowspan=2 | resolvconf !! colspan=5 | Supported protocols
|-
! Authoritative !! Recursive !! Cache !!  ValidatesDNSSEC  !! DNS !! DNSCrypt !! DNSover TLS !! DNSover HTTPS !! DNSover QUIC
|-
! BIND
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! CoreDNS
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! DNS-over-HTTPS
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! Deadwood (MaraDNS recursor)
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! dnscrypt-proxy
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! dnsmasq
|  || 1 ||  ||  || 2 ||  ||  ||  ||  ||  ||
|-
! dnsproxy
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! Knot Resolver
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! pdnsd
|  || 1 ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! PowerDNS Recursor
|  ||  ||  ||  || 2 ||  ||  ||  ||  ||  ||
|-
! Rescached
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! RouteDNS
|  ||  ||  || 3 ||  ||  ||  ||  ||  ||  ||
|-
! SmartDNS
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! Stubby
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
!style="white-space: nowrap;"| systemd-resolved
|  ||  ||  ||  ||  ||  ||  ||  ||  ||  ||
|-
! Unbound
|  ||  ||  || 3 ||  ||  ||  ||  ||  ||  ||
|}

# From Wikipedia: limited authoritative support, intended for internal network use rather than public Internet use.
# DNSSEC validation is disabled by default and must be enabled in the configuration file.
# Supports persistent cache using the Redis backend.

## Authoritative-only servers
{| class="wikitable sortable" style="text-align:center"
! Name !! Package !!  DNSSECsigning !! Geographicbalancing
|-
! gdnsd
|  ||  ||
|-
! Knot DNS
|  ||  ||
|-
! MaraDNS
|  ||  ||
|-
! NSD
|  ||  ||
|-
! PowerDNS
|  ||  ||
|}

## Conditional forwarding
It is possible to use specific DNS resolvers when querying specific domain names. This is particularly useful when connecting to a VPN, so that queries to the VPN network are resolved by the VPN's DNS, while queries to the internet will still be resolved by your standard DNS resolver. It can also be used on local networks.

To implement it, you need to use a local resolver because glibc does not support it.

In a dynamic environment (laptops and to some extents desktops), you need to configure your resolver based on the network(s) you are connected to. The best way to do that is to use openresolv because it supports multiple subscribers. Some network managers support it, either through openresolv, or by configuring the resolver directly. NetworkManager supports conditional forwarding without openresolv.
