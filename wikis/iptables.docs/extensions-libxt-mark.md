# Extensions / Libxt MARK

This target is used to set the Netfilter mark value associated with the packet. It can, for example, be used in conjunction with routing based on fwmark (needs iproute2). If you plan on doing so, note that the mark needs to be set in either the PREROUTING or the OUTPUT chain of the mangle table to affect routing. The mark field is 32 bits wide.

**--set-xmark** *value*\[**/***mask*\]
Zeroes out the bits given by *mask* and XORs *value* into the packet mark ("nfmark"). If *mask* is omitted, 0xFFFFFFFF is assumed.

**--set-mark** *value*\[**/***mask*\]
Zeroes out the bits given by *mask* and ORs *value* into the packet mark. If *mask* is omitted, 0xFFFFFFFF is assumed.

The following mnemonics are available:

**--and-mark** *bits*
Binary AND the nfmark with *bits*. (Mnemonic for **--set-xmark** 0/*invbits*, where *invbits* is the binary negation of *bits*.)

**--or-mark** *bits*
Binary OR the nfmark with *bits*. (Mnemonic for **--set-xmark** *bits***/***bits*.)

**--xor-mark** *bits*
Binary XOR the nfmark with *bits*. (Mnemonic for **--set-xmark** *bits***/0**.)
