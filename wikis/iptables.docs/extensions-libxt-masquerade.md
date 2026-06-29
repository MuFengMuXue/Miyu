# Extensions / Libxt MASQUERADE

This target is only valid in the **nat** table, in the **POSTROUTING** chain. It should only be used with dynamically assigned IP (dialup) connections: if you have a static IP address, you should use the SNAT target. Masquerading is equivalent to specifying a mapping to the IP address of the interface the packet is going out, but also has the effect that connections are *forgotten* when the interface goes down. This is the correct behavior when the next dialup is unlikely to have the same interface address (and hence any established connections are lost anyway).

**--to-ports** *port*\[**-***port*\]
This specifies a range of source ports to use, overriding the default **SNAT** source port selection heuristics (see above). This is only valid if the rule also specifies one of the following protocols: **tcp**, **udp**, **dccp** or **sctp**.

**--random**
Randomize source port mapping (kernel \>= 2.6.21). Since kernel 5.0, **--random** is identical to **--random-fully**.

**--random-fully**
Fully randomize source port mapping (kernel \>= 3.13).

IPv6 support available since Linux kernels \>= 3.7.
