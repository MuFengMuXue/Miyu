# Extensions / Libxt Addrtype

This module matches packets based on their **address type.** Address types are used within the kernel networking stack and categorize addresses into various groups. The exact definition of that group depends on the specific layer three protocol.

The following address types are possible:

**UNSPEC**
an unspecified address (i.e. 0.0.0.0)

**UNICAST**
an unicast address

**LOCAL**
a local address

**BROADCAST**
a broadcast address

**ANYCAST**
an anycast packet

**MULTICAST**
a multicast address

**BLACKHOLE**
a blackhole address

**UNREACHABLE**
an unreachable address

**PROHIBIT**
a prohibited address

**THROW**
FIXME

**NAT**
FIXME

**XRESOLVE**
\[**!**\] **--src-type** *type*
Matches if the source address is of given type

\[**!**\] **--dst-type** *type*
Matches if the destination address is of given type

**--limit-iface-in**
The address type checking can be limited to the interface the packet is coming in. This option is only valid in the **PREROUTING**, **INPUT** and **FORWARD** chains. It cannot be specified with the **--limit-iface-out** option.

**--limit-iface-out**
The address type checking can be limited to the interface the packet is going out. This option is only valid in the **POSTROUTING**, **OUTPUT** and **FORWARD** chains. It cannot be specified with the **--limit-iface-in** option.
