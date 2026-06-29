# Extensions / libip6t Rt

Match on IPv6 routing header

\[**!**\] **--rt-type** *type*
Match the type (numeric).

\[**!**\] **--rt-segsleft** *num*\[**:***num*\]
Match the \`segments left' field (range).

\[**!**\] **--rt-len** *length*
Match the length of this header.

**--rt-0-res**
Match the reserved field, too (type=0)

**--rt-0-addrs** *addr*\[**,***addr*...\]
Match type=0 addresses (list).

**--rt-0-not-strict**
List of type=0 addresses is not a strict list.
