# Extensions / Libipt REJECT

This is used to send back an error packet in response to the matched packet: otherwise it is equivalent to **DROP** so it is a terminating TARGET, ending rule traversal. This target is only valid in the **INPUT**, **FORWARD** and **OUTPUT** chains, and user-defined chains which are only called from those chains. The following option controls the nature of the error packet returned:

**--reject-with** *type*
The type given can be **icmp-net-unreachable**, **icmp-host-unreachable**, **icmp-port-unreachable**, **icmp-proto-unreachable**, **icmp-net-prohibited**, **icmp-host-prohibited**, or **icmp-admin-prohibited**, which return the appropriate ICMP error message (**icmp-port-unreachable** is the default). The option **tcp-reset** can be used on rules which only match the TCP protocol: this causes a TCP RST packet to be sent back. This is mainly useful for blocking *ident* (113/tcp) probes which frequently occur when sending mail to broken mail hosts (which won't accept your mail otherwise).

*Warning:* You should not indiscriminately apply the REJECT target to packets whose connection state is classified as INVALID; instead, you should only DROP these.

Consider a source host transmitting a packet P, with P experiencing so much delay along its path that the source host issues a retransmission, P_2, with P_2 being successful in reaching its destination and advancing the connection state normally. It is conceivable that the late-arriving P may be considered not to be associated with any connection tracking entry. Generating a reject response for a packet so classed would then terminate the healthy connection.

So, instead of:

-A INPUT ... -j REJECT

do consider using:

-A INPUT ... -m conntrack --ctstate INVALID -j DROP
-A INPUT ... -j REJECT
