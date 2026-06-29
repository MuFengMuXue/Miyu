# Extensions / Libxt Physdev

This module matches on the bridge port input and output devices enslaved to a bridge device. This module is a part of the infrastructure that enables a transparent bridging IP firewall and is only useful for kernel versions above version 2.5.44.

\[**!**\] **--physdev-in** *name*
Name of a bridge port via which a packet is received (only for packets entering the **INPUT**, **FORWARD** and **PREROUTING** chains). If the interface name ends in a "+", then any interface which begins with this name will match. If the packet didn't arrive through a bridge device, this packet won't match this option, unless '!' is used.

\[**!**\] **--physdev-out** *name*
Name of a bridge port via which a packet is going to be sent (for bridged packets entering the **FORWARD** and **POSTROUTING** chains). If the interface name ends in a "+", then any interface which begins with this name will match.

\[**!**\] **--physdev-is-in**
Matches if the packet has entered through a bridge interface.

\[**!**\] **--physdev-is-out**
Matches if the packet will leave through a bridge interface.

\[**!**\] **--physdev-is-bridged**
Matches if the packet is being bridged and therefore is not being routed. This is only useful in the FORWARD and POSTROUTING chains.
