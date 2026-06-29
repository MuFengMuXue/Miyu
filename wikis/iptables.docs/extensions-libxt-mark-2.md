# Extensions / Libxt Mark

This module matches the netfilter mark field associated with a packet (which can be set using the **MARK** target below).

\[**!**\] **--mark** *value*\[**/***mask*\]
Matches packets with the given unsigned mark value (if a *mask* is specified, this is logically ANDed with the *mask* before the comparison).
