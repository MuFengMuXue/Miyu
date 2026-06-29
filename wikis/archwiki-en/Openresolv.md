# Openresolv

openresolv is a resolvconf implementation, i.e. a resolv.conf management framework.

Although openresolv is most known for allowing multiple applications to modify , it is currently the only standard way to implement:
* dynamic control of a DNS resolver (other than glibc),
* dynamic conditional forwarding.

## Installation
Install the   package.

## Usage
openresolv provides  and is configured in . See  for supported options.

Running  will generate .

## Users
DHCP clients:

* dhcpcd has a hook which uses resolvconf if it is installed.
* iwd#Enable built-in network configuration

Network managers:

* netctl (used by default)
* NetworkManager#Use openresolv (limited to a single interface)

VPN clients:

* OpenConnect
* OpenVPN#DNS
* strongSwan
* WireGuard

## Subscribers
openresolv can be configured to pass name servers and search domains to DNS resolvers. The supported resolvers are:

* BIND
* dnsmasq#openresolv
* pdnsd
*
* Unbound

See the official documentation for instructions.

## Tips and tricks
## Defining multiple values for options
The man page does not mention it, but to define multiple values, for options that support it (e.g. ,  etc.) in , you need to write them space separated inside quotes. E.g.:
