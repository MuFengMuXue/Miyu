# Extensions / Libxt CONNMARK

This module sets the netfilter mark value associated with a connection. The mark is 32 bits wide.

**--set-xmark** *value*\[**/***mask*\]
Zero out the bits given by *mask* and XOR *value* into the ctmark.

**--save-mark** \[**--nfmask** *nfmask*\] \[**--ctmask** *ctmask*\]
Copy the packet mark (nfmark) to the connection mark (ctmark) using the given masks. The new nfmark value is determined as follows:

ctmark = (ctmark & ~ctmask) ^ (nfmark & nfmask)

i.e. *ctmask* defines what bits to clear and *nfmask* what bits of the nfmark to XOR into the ctmark. *ctmask* and *nfmask* default to 0xFFFFFFFF.

**--restore-mark** \[**--nfmask** *nfmask*\] \[**--ctmask** *ctmask*\]
Copy the connection mark (ctmark) to the packet mark (nfmark) using the given masks. The new ctmark value is determined as follows:

nfmark = (nfmark & ~*nfmask*) ^ (ctmark & *ctmask*);

i.e. *nfmask* defines what bits to clear and *ctmask* what bits of the ctmark to XOR into the nfmark. *ctmask* and *nfmask* default to 0xFFFFFFFF.

**--restore-mark** is only valid in the **mangle** table.

The following mnemonics are available for **--set-xmark**:

**--and-mark** *bits*
Binary AND the ctmark with *bits*. (Mnemonic for **--set-xmark** 0/*invbits*, where *invbits* is the binary negation of *bits*.)

**--or-mark** *bits*
Binary OR the ctmark with *bits*. (Mnemonic for **--set-xmark** *bits***/***bits*.)

**--xor-mark** *bits*
Binary XOR the ctmark with *bits*. (Mnemonic for **--set-xmark** *bits***/0**.)

**--set-mark** *value*\[**/***mask*\]
Set the connection mark. If a mask is specified then only those bits set in the mask are modified.

**--save-mark** \[**--mask** *mask*\]
Copy the nfmark to the ctmark. If a mask is specified, only those bits are copied.

**--restore-mark** \[**--mask** *mask*\]
Copy the ctmark to the nfmark. If a mask is specified, only those bits are copied. This is only valid in the **mangle** table.
