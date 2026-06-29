# Extensions / libip6t REJECT

This is used to send back an error packet in response to the matched packet: otherwise it is equivalent to **DROP** so it is a terminating TARGET, ending rule traversal. This target is only valid in the **INPUT**, **FORWARD** and **OUTPUT** chains, and user-defined chains which are only called from those chains. The following option controls the nature of the error packet returned:

**--reject-with** *type*
The type given can be **icmp6-no-route**, **no-route**, **icmp6-adm-prohibited**, **adm-prohibited**, **icmp6-addr-unreachable**, **addr-unreach**, or **icmp6-port-unreachable**, which return the appropriate ICMPv6 error message (**icmp6-port-unreachable** is the default). Finally, the option **tcp-reset** can be used on rules which only match the TCP protocol: this causes a TCP RST packet to be sent back. This is mainly useful for blocking *ident* (113/tcp) probes which frequently occur when sending mail to broken mail hosts (which won't accept your mail otherwise). **tcp-reset** can only be used with kernel versions 2.6.14 or later.

*Warning:* You should not indiscriminately apply the REJECT target to packets whose connection state is classified as INVALID; instead, you should only DROP these.

Consider a source host transmitting a packet P, with P experiencing so much delay along its path that the source host issues a retransmission, P_2, with P_2 being successful in reaching its destination and advancing the connection state normally. It is conceivable that the late-arriving P may be considered not to be associated with any connection tracking entry. Generating a reject response for a packet so classed would then terminate the healthy connection.

So, instead of:

-A INPUT ... -j REJECT

do consider using:

-A INPUT ... -m conntrack --ctstate INVALID -j DROP
-A INPUT ... -j REJECT
