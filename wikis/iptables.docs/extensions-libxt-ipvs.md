# Extensions / Libxt Ipvs

Match IPVS connection properties.

\[**!**\] **--ipvs**
packet belongs to an IPVS connection

Any of the following options implies --ipvs (even negated)
\[**!**\] **--vproto** *protocol*
VIP protocol to match; by number or name, e.g. "tcp"

\[**!**\] **--vaddr** *address*\[**/***mask*\]
VIP address to match

\[**!**\] **--vport** *port*
VIP port to match; by number or name, e.g. "http"

**--vdir** {**ORIGINAL**\|**REPLY**}
flow direction of packet

\[**!**\] **--vmethod** {**GATE**\|**IPIP**\|**MASQ**}
IPVS forwarding method used

\[**!**\] **--vportctl** *port*
VIP port of the controlling connection to match, e.g. 21 for FTP
