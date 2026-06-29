# Systemd-resolved

systemd-resolved is a systemd service that provides network name resolution to local applications via a D-Bus interface, the  NSS service (), and a local DNS stub listener on . See  for the usage.

## Installation
systemd-resolved is a part of the  package that is installed by default.

## Configuration
systemd-resolved provides resolver services for Domain Name System (DNS) (including DNSSEC and DNS over TLS), Multicast DNS (mDNS) and Link-Local Multicast Name Resolution (LLMNR).

The resolver can be configured by editing  and/or drop-in .conf files in . See .

To use systemd-resolved start and enable .

## DNS
Software that relies on glibc's  (or similar) will work out of the box, since, by default,  is configured to use  if it is available.

To provide domain name resolution for software that reads  directly, such as web browsers, Go, GnuPG and QEMU when using user networking, systemd-resolved has four different modes for handling the file—stub, static, uplink and foreign. They are described in . We will focus here only on the recommended mode, i.e. the stub mode which uses .

 contains the local stub  as the only DNS server and a list of search domains. This is the recommended mode of operation that propagates the systemd-resolved managed configuration to all clients. To use it, replace  with a symbolic link to it:

 # ln -sf ../run/systemd/resolve/stub-resolv.conf /etc/resolv.conf

## Setting DNS servers
## Automatically
systemd-resolved will work out of the box with a network manager using . No particular configuration is required since systemd-resolved will be detected by following the  symlink. This is going to be the case with systemd-networkd, NetworkManager, and iwd.

However, if the DHCP and VPN clients use the resolvconf program to set name servers and search domains (see openresolv#Users for a list of software that use resolvconf), the additional package  is needed to provide the  symlink.

## Manually
In stub and static modes, custom DNS server(s) can be set in the  file:

## Fallback
If systemd-resolved does not receive DNS server addresses from the network manager and no DNS servers are configured manually then systemd-resolved falls back to the fallback DNS addresses to ensure that DNS resolution always works.

The addresses can be changed by setting  in . E.g.:

To disable the fallback DNS functionality set the  option without specifying any addresses:

## DNSSEC
The  package is built with DNSSEC validation disabled by default. This can be changed with the  setting in .

* Set  (the default) to disable DNSSEC validation.
* Set  to validate DNSSEC only if the upstream DNS server supports it. If your DNS server does not support DNSSEC and you experience problems with this mode (e.g.: systemd issue 21107, systemd issue 36681), you may need to explicitly disable DNSSEC validation instead.
* Set  to always validate DNSSEC, thus breaking DNS resolution with name servers that do not support it. For example:

Test DNSSEC validation by querying a domain name with no signature:

Now test a domain with valid signature:

## DNS over TLS
## Global DNS over TLS
DNS over TLS is disabled by default. To enable it change the  setting in the  section in . To enable validation of your DNS provider's server certificate, include their hostname in the  setting in the format . For example:

 can be used to test if DNS over TLS is working since DNS over TLS always uses port 853 and never port 53. The command  should produce no output when a hostname is resolved with DNS over TLS and  should produce encrypted output.

Wireshark can be used for more detailed packet inspection of DNS over TLS queries.

## Per-link DNS over TLS
Enabling DNS over TLS for specific connections depends on the network manager:

* For systemd-networkd, set the  setting in the  section of a .network file. If necessary, configure custom DNS servers with the  setting. See .
* For NetworkManager, set  in the  section of a .nmconnection file (e.g. by running ); see . To set custom DNS servers, see NetworkManager#Setting custom DNS servers in a connection.

## Additional listening interfaces
systemd-resolved answers DNS requests to local applications via loopback interface per default. To make systemd-resolved answer DNS requests on additional interfaces or addresses than the default one, set the option  for every additional interface in . For example:

## mDNS
systemd-resolved is capable of working as a multicast DNS resolver and responder.

The resolver provides hostname resolution using a "hostname.local" naming scheme.

mDNS will only be activated for a connection if both systemd-resolved's mDNS support is enabled, and if the configuration for the currently active network manager enables mDNS for the connection.

systemd-resolveds mDNS support is enabled by default. It can be disabled by its  setting (see ).

Enabling per-connection mDNS support depends on the network manager:

* For systemd-networkd, set the  setting in the  section of a per-connection settings file. You may also have to set  in the  section. See .
* For NetworkManager, set  in the  section of the connection's settings file. Running {{ic|nmcli connection modify interface_name connection.mdns {yesnoresolve}}} will do that for you. See .

## LLMNR
Link-Local Multicast Name Resolution is a hostname resolution protocol created by Microsoft.

LLMNR will only be activated for the connection if both the systemd-resolved's global setting ( in ) and the network manager's per-connection setting is enabled. By default systemd-resolved enables LLMNR responder; systemd-networkd and NetworkManagerenable it for connections.

* For systemd-networkd the setting is  in the  section. See .
* For NetworkManager the setting is  in the  section. See .

If you plan to use LLMNR and use a firewall, make sure to open UDP and TCP ports .

## Lookup
To query DNS records, mDNS or LLMNR hosts you can use the resolvectl utility.

For example, to query a DNS record:

## Troubleshooting
## systemd-resolved not searching the local domain
systemd-resolved may not search the local domain when given just the hostname, even when  or  is present in the appropriate systemd-networkd's .network file, and that file produces the expected  in . You can run  or  to check if the search domains are actually being picked up.

Possible workarounds:

* Disable #Global DNS over TLS on the local link by setting  in the .network file of the link in question. It should still be using TLS on non-local DNS queries, even if they're leaving through the same interface.
* Disable LLMNR to let systemd-resolved immediately continue with appending the DNS suffixes
* Trim 's  database (e.g., by removing  option after  service)
* Switch to using fully-qualified domain names
* Use  to resolve hostnames
* Fall back to using glibc's  instead of using systemd's

## systemd-resolved does not resolve hostnames without suffix
To make systemd-resolved resolve hostnames that are not fully qualified domain names, add  to .

This only seems to work with LLMNR disabled ().

If you are using systemd-networkd, you might want the domain supplied by the DHCP server or IPv6 Router Advertisement to be used as a search domain. This is disabled by default, to enable it add to the interface's .network file:

You can check what systemd-resolved has for each interface with:

 $ resolvectl domain
