# Extensions / libip6t Frag

This module matches the parameters in Fragment header.

\[**!**\] **--fragid** *id*\[**:***id*\]
Matches the given Identification or range of it.

\[**!**\] **--fraglen** *length*
This option cannot be used with kernel version 2.6.10 or later. The length of Fragment header is static and this option doesn't make sense.

**--fragres**
Matches if the reserved fields are filled with zero.

**--fragfirst**
Matches on the first fragment.

**--fragmore**
Matches if there are more fragments.

**--fraglast**
Matches if this is the last fragment.
