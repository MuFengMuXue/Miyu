# Extensions / Libxt Socket

This matches if an open TCP/UDP socket can be found by doing a socket lookup on the packet. It matches if there is an established or non-zero bound listening socket (possibly with a non-local address). The lookup is performed using the **packet** tuple of TCP/UDP packets, or the original TCP/UDP header **embedded** in an ICMP/ICPMv6 error packet.

**--transparent**
Ignore non-transparent sockets.

**--nowildcard**
Do not ignore sockets bound to 'any' address. The socket match won't accept zero-bound listeners by default, since then local services could intercept traffic that would otherwise be forwarded. This option therefore has security implications when used to match traffic being forwarded to redirect such packets to local machine with policy routing. When using the socket match to implement fully transparent proxies bound to non-local addresses it is recommended to use the --transparent option instead.

Example (assuming packets with mark 1 are delivered locally):

> -t mangle -A PREROUTING -m socket --transparent -j MARK --set-mark 1

**--restore-skmark**
Set the packet mark to the matching socket's mark. Can be combined with the **--transparent** and **--nowildcard** options to restrict the sockets to be matched when restoring the packet mark.

Example: An application opens 2 transparent (**IP_TRANSPARENT**) sockets and sets a mark on them with **SO_MARK** socket option. We can filter matching packets:

> -t mangle -I PREROUTING -m socket --transparent --restore-skmark -j action

> -t mangle -A action -m mark --mark 10 -j action2

> -t mangle -A action -m mark --mark 11 -j action3
