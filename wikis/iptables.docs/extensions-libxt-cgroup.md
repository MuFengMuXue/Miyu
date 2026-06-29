# Extensions / Libxt Cgroup

\[**!**\] **--path** *path*
Match cgroup2 membership.

Each socket is associated with the v2 cgroup of the creating process. This matches packets coming from or going to all sockets in the sub-hierarchy of the specified path. The path should be relative to the root of the cgroup2 hierarchy.

\[**!**\] **--cgroup** *classid*
Match cgroup net_cls classid.

classid is the marker set through the cgroup net_cls controller. This option and --path can't be used together.

Example:

> iptables -A OUTPUT -p tcp --sport 80 -m cgroup ! --path service/http-server -j DROP

> iptables -A OUTPUT -p tcp --sport 80 -m cgroup ! --cgroup 1 -j DROP

**IMPORTANT**: when being used in the INPUT chain, the cgroup matcher is currently only of limited functionality, meaning it will only match on packets that are processed for local sockets through early socket demuxing. Therefore, general usage on the INPUT chain is not advised unless the implications are well understood.

Available since Linux 3.14.
