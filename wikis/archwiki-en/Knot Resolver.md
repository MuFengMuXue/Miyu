# Knot Resolver

Knot Resolver (a.k.a. kresd) is a full (recursive), caching DNS resolver. It is designed to scale from small home-office networks to providing DNS servers at the scale of ISPs. Knot Resolver supports DNSSEC validation, which is enabled by default.

## Installation
Install the  package.

## Configuration
Start/enable .

To use Knot Resolver as the local resolver, configure  and  as your nameservers in . For example:

By default, the resolver will listen on  and , ports  and  (DNS over TLS). If the resolver should be accessible from other hosts, configure other network interfaces in  with . Refer to Knot Resolver documentation for more information.

If the resolver should respect entries from the  file, add a  line to .

## Knot Resolver and dnsmasq
If dnsmasq is used for managing DHCP, then advertising a kresd instance works like any other external DNS server would: By adding an  line to the dnsmasq configuration file.

Note that a default configuration of dnsmasq will clash with the default configuration of kresd, since both will attempt to use port . Disable the dnsmasq DNS functionality (), or assign a different port to either service.
