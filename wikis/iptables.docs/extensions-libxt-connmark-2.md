# Extensions / Libxt Connmark

This module matches the netfilter mark field associated with a connection (which can be set using the **CONNMARK** target below).

\[**!**\] **--mark** *value*\[**/***mask*\]
Matches packets in connections with the given mark value (if a mask is specified, this is logically ANDed with the mark before the comparison).
