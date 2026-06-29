# Extensions / libip6t ipv6header

This module matches IPv6 extension headers and/or upper layer header.

**--soft**
Matches if the packet includes **any** of the headers specified with **--header**.

\[**!**\] **--header** *header*\[**,***header*...\]
Matches the packet which EXACTLY includes all specified headers. The headers encapsulated with ESP header are out of scope. Possible *header* types can be:

**hop**\|**hop-by-hop**
Hop-by-Hop Options header

**dst**
Destination Options header

**route**
Routing header

**frag**
Fragment header

**auth**
Authentication header

**esp**
Encapsulating Security Payload header

**none**
No Next header which matches 59 in the 'Next Header field' of IPv6 header or any IPv6 extension headers

**prot**
which matches any upper layer protocol header. A protocol name from /etc/protocols and numeric value also allowed. The number 255 is equivalent to **prot**.
