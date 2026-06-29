# Extensions / Libxt Dccp

\[**!**\] **--source-port**,**--sport** *port*\[**:***port*\]
\[**!**\] **--destination-port**,**--dport** *port*\[**:***port*\]
\[**!**\] **--dccp-types** *mask*
Match when the DCCP packet type is one of 'mask'. 'mask' is a comma-separated list of packet types. Packet types are: **REQUEST RESPONSE DATA ACK DATAACK CLOSEREQ CLOSE RESET SYNC SYNCACK INVALID**.

\[**!**\] **--dccp-option** *number*
Match if DCCP option set.
