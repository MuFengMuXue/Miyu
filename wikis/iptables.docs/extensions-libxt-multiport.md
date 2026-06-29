# Extensions / Libxt Multiport

This module matches a set of source or destination ports. Up to 15 ports can be specified. A port range (port:port) counts as two ports. It can only be used in conjunction with one of the following protocols: **tcp**, **udp**, **udplite**, **dccp** and **sctp**.

\[**!**\] **--source-ports**,**--sports** *port*\[**,***port*\|**,***port***:***port*\]...
Match if the source port is one of the given ports. The flag **--sports** is a convenient alias for this option. Multiple ports or port ranges are separated using a comma, and a port range is specified using a colon. **53,1024:65535** would therefore match ports 53 and all from 1024 through 65535.

\[**!**\] **--destination-ports**,**--dports** *port*\[**,***port*\|**,***port***:***port*\]...
Match if the destination port is one of the given ports. The flag **--dports** is a convenient alias for this option.

\[**!**\] **--ports** *port*\[**,***port*\|**,***port***:***port*\]...
Match if either the source or destination ports are equal to one of the given ports.
