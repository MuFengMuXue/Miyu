# Extensions / Libxt State

The "state" extension is a subset of the "conntrack" module. "state" allows access to the connection tracking state for this packet.

\[**!**\] **--state** *state*
Where state is a comma separated list of the connection states to match. Only a subset of the states unterstood by "conntrack" are recognized: **INVALID**, **ESTABLISHED**, **NEW**, **RELATED** or **UNTRACKED**. For their description, see the "conntrack" heading in this manpage.
