# Extensions / Libxt Policy

This module matches the policy used by IPsec for handling a packet.

**--dir** {**in**\|**out**}
Used to select whether to match the policy used for decapsulation or the policy that will be used for encapsulation. **in** is valid in the **PREROUTING, INPUT and FORWARD** chains, **out** is valid in the **POSTROUTING, OUTPUT and FORWARD** chains.

**--pol** {**none**\|**ipsec**}
Matches if the packet is subject to IPsec processing. **--pol none** cannot be combined with **--strict**.

**--strict**
Selects whether to match the exact policy or match if any rule of the policy matches the given policy.

For each policy element that is to be described, one can use one or more of the following options. When **--strict** is in effect, at least one must be used per element.

\[**!**\] **--reqid** *id*
Matches the reqid of the policy rule. The reqid can be specified with **setkey(8)** using **unique:id** as level.

\[**!**\] **--spi** *spi*
Matches the SPI of the SA.

\[**!**\] **--proto** {**ah**\|**esp**\|**ipcomp**}
Matches the encapsulation protocol.

\[**!**\] **--mode** {**tunnel**\|**transport**}
Matches the encapsulation mode.

\[**!**\] **--tunnel-src** *addr*\[**/***mask*\]
Matches the source end-point address of a tunnel mode SA. Only valid with **--mode tunnel**.

\[**!**\] **--tunnel-dst** *addr*\[**/***mask*\]
Matches the destination end-point address of a tunnel mode SA. Only valid with **--mode tunnel**.

**--next**
Start the next element in the policy specification. Can only be used with **--strict**.
