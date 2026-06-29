# Extensions / Libxt Owner

This module attempts to match various characteristics of the packet creator, for locally generated packets. This match is only valid in the OUTPUT and POSTROUTING chains. Forwarded packets do not have any socket associated with them. Packets from kernel threads do have a socket, but usually no owner.

\[**!**\] **--uid-owner** *username*
\[**!**\] **--uid-owner** *userid*\[**-***userid*\]
Matches if the packet socket's file structure (if it has one) is owned by the given user. You may also specify a numerical UID, or an UID range.

\[**!**\] **--gid-owner** *groupname*
\[**!**\] **--gid-owner** *groupid*\[**-***groupid*\]
Matches if the packet socket's file structure is owned by the given group. You may also specify a numerical GID, or a GID range.

**--suppl-groups**
Causes group(s) specified with **--gid-owner** to be also checked in the supplementary groups of a process.

\[**!**\] **--socket-exists**
Matches if the packet is associated with a socket.
