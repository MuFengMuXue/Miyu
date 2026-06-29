# Extensions / Libxt REDIRECT

This target is only valid in the **nat** table, in the **PREROUTING** and **OUTPUT** chains, and user-defined chains which are only called from those chains. It redirects the packet to the machine itself by changing the destination IP to the primary address of the incoming interface (locally-generated packets are mapped to the localhost address, 127.0.0.1 for IPv4 and ::1 for IPv6, and packets arriving on interfaces that don't have an IP address configured are dropped).

**--to-ports** *port*\[**-***port*\]
This specifies a destination port or range of ports to use: without this, the destination port is never altered. This is only valid if the rule also specifies one of the following protocols: **tcp**, **udp**, **dccp** or **sctp**. For a single port, a service name as listed in **/etc/services** may be used.

**--random**
Randomize source port mapping (kernel \>= 2.6.22).

IPv6 support available starting Linux kernels \>= 3.7.
