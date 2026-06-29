# Extensions / Libxt Tcpmss

This matches the TCP MSS (maximum segment size) field of the TCP header. You can only use this on TCP SYN or SYN/ACK packets, since the MSS is only negotiated during the TCP handshake at connection startup time.

\[**!**\] **--mss** *value*\[**:***value*\]
Match a given TCP MSS value or range. If a range is given, the second *value* must be greater than or equal to the first *value*.
