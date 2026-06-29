# Extensions / Libxt Tcp

These extensions can be used if \`--protocol tcp' is specified. It provides the following options:

\[**!**\] **--source-port**,**--sport** *port*\[**:***port*\]
Source port or port range specification. This can either be a service name or a port number. An inclusive range can also be specified, using the format *first***:***last*. If the first port is omitted, "0" is assumed; if the last is omitted, "65535" is assumed. The flag **--sport** is a convenient alias for this option.

\[**!**\] **--destination-port**,**--dport** *port*\[**:***port*\]
Destination port or port range specification. The flag **--dport** is a convenient alias for this option.

\[**!**\] **--tcp-flags** *mask* *comp*
Match when the TCP flags are as specified. The first argument *mask* is the flags which we should examine, written as a comma-separated list, and the second argument *comp* is a comma-separated list of flags which must be set. Flags are: **SYN ACK FIN RST URG PSH ALL NONE**. Hence the command


     iptables -A FORWARD -p tcp --tcp-flags SYN,ACK,FIN,RST SYN

will only match packets with the SYN flag set, and the ACK, FIN and RST flags unset.

\[**!**\] **--syn**
Only match TCP packets with the SYN bit set and the ACK,RST and FIN bits cleared. Such packets are used to request TCP connection initiation; for example, blocking such packets coming in an interface will prevent incoming TCP connections, but outgoing TCP connections will be unaffected. It is equivalent to **--tcp-flags SYN,RST,ACK,FIN SYN**. If the "!" flag precedes the "--syn", the sense of the option is inverted.

\[**!**\] **--tcp-option** *number*
Match if TCP option set.
