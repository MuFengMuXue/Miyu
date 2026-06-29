# Extensions / Libxt Conntrack

This module, when combined with connection tracking, allows access to the connection tracking state for this packet/connection.

\[**!**\] **--ctstate** *statelist*
*statelist* is a comma separated list of the connection states to match. Possible states are listed below.

\[**!**\] **--ctproto** *l4proto*
Layer-4 protocol to match (by number or name)

\[**!**\] **--ctorigsrc** *address*\[**/***mask*\]
\[**!**\] **--ctorigdst** *address*\[**/***mask*\]
\[**!**\] **--ctreplsrc** *address*\[**/***mask*\]
\[**!**\] **--ctrepldst** *address*\[**/***mask*\]
Match against original/reply source/destination address

\[**!**\] **--ctorigsrcport** *port*\[**:***port*\]
\[**!**\] **--ctorigdstport** *port*\[**:***port*\]
\[**!**\] **--ctreplsrcport** *port*\[**:***port*\]
\[**!**\] **--ctrepldstport** *port*\[**:***port*\]
Match against original/reply source/destination port (TCP/UDP/etc.) or GRE key. Matching against port ranges is only supported in kernel versions above 2.6.38.

\[**!**\] **--ctstatus** *statelist*
*statuslist* is a comma separated list of the connection statuses to match. Possible statuses are listed below.

\[**!**\] **--ctexpire** *time*\[**:***time*\]
Match remaining lifetime in seconds against given value or range of values (inclusive)

**--ctdir** {**ORIGINAL**\|**REPLY**}
Match packets that are flowing in the specified direction. If this flag is not specified at all, matches packets in both directions.

States for **--ctstate**:

**INVALID**
The packet is associated with no known connection.

**NEW**
The packet has started a new connection or otherwise associated with a connection which has not seen packets in both directions.

**ESTABLISHED**
The packet is associated with a connection which has seen packets in both directions.

**RELATED**
The packet is starting a new connection, but is associated with an existing connection, such as an FTP data transfer or an ICMP error.

**UNTRACKED**
The packet is not tracked at all, which happens if you explicitly untrack it by using -j CT --notrack in the raw table.

**SNAT**
A virtual state, matching if the original source address differs from the reply destination.

**DNAT**
A virtual state, matching if the original destination differs from the reply source.

Statuses for **--ctstatus**:

**NONE**
None of the below.

**EXPECTED**
This is an expected connection (i.e. a conntrack helper set it up).

**SEEN_REPLY**
Conntrack has seen packets in both directions.

**ASSURED**
Conntrack entry should never be early-expired.

**CONFIRMED**
Connection is confirmed: originating packet has left box.
