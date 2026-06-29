# Extensions / Libxt Ecn

This allows you to match the ECN bits of the IPv4/IPv6 and TCP header. ECN is the Explicit Congestion Notification mechanism as specified in RFC3168

\[**!**\] **--ecn-tcp-cwr**
This matches if the TCP ECN CWR (Congestion Window Received) bit is set.

\[**!**\] **--ecn-tcp-ece**
This matches if the TCP ECN ECE (ECN Echo) bit is set.

\[**!**\] **--ecn-ip-ect** *num*
This matches a particular IPv4/IPv6 ECT (ECN-Capable Transport). You have to specify a number between \`0' and \`3'.
