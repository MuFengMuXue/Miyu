# Extensions / Libxt SNAT

This target is only valid in the **nat** table, in the **POSTROUTING** and **INPUT** chains, and user-defined chains which are only called from those chains. It specifies that the source address of the packet should be modified (and all future packets in this connection will also be mangled), and rules should cease being examined. It takes the following options:

**--to-source** \[*ipaddr*\[**-***ipaddr*\]\]\[**:***port*\[**-***port*\]\]
which can specify a single new source IP address, an inclusive range of IP addresses. Optionally a port range, if the rule also specifies one of the following protocols: **tcp**, **udp**, **dccp** or **sctp**. If no port range is specified, then source ports below 512 will be mapped to other ports below 512: those between 512 and 1023 inclusive will be mapped to ports below 1024, and other ports will be mapped to 1024 or above. Where possible, no port alteration will occur.

**--random**
Randomize source port mapping through a hash-based algorithm (kernel \>= 2.6.21).

**--random-fully**
Fully randomize source port mapping through a PRNG (kernel \>= 3.14).

**--persistent**
Gives a client the same source-/destination-address for each connection. This supersedes the SAME target. Support for persistent mappings is available from 2.6.29-rc2.

Kernels prior to 2.6.36-rc1 don't have the ability to **SNAT** in the **INPUT** chain.

IPv6 support available since Linux kernels \>= 3.7.
