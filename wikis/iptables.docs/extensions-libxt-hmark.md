# Extensions / Libxt HMARK

Like MARK, i.e. set the fwmark, but the mark is calculated from hashing packet selector at choice. You have also to specify the mark range and, optionally, the offset to start from. ICMP error messages are inspected and used to calculate the hashing.

Existing options are:

**--hmark-tuple** tuple
Possible tuple members are: **src** meaning source address (IPv4, IPv6 address), **dst** meaning destination address (IPv4, IPv6 address), **sport** meaning source port (TCP, UDP, UDPlite, SCTP, DCCP), **dport** meaning destination port (TCP, UDP, UDPlite, SCTP, DCCP), **spi** meaning Security Parameter Index (AH, ESP), and **ct** meaning the usage of the conntrack tuple instead of the packet selectors.

**--hmark-mod** *value (must be \> 0)*
Modulus for hash calculation (to limit the range of possible marks)

**--hmark-offset** *value*
Offset to start marks from.

For advanced usage, instead of using --hmark-tuple, you can specify custom
prefixes and masks:

**--hmark-src-prefix** *cidr*
The source address mask in CIDR notation.

**--hmark-dst-prefix** *cidr*
The destination address mask in CIDR notation.

**--hmark-sport-mask** *value*
A 16 bit source port mask in hexadecimal.

**--hmark-dport-mask** *value*
A 16 bit destination port mask in hexadecimal.

**--hmark-spi-mask** *value*
A 32 bit field with spi mask.

**--hmark-proto-mask** *value*
An 8 bit field with layer 4 protocol number.

**--hmark-rnd** *value*
A 32 bit random custom value to feed hash calculation.

*Examples:*

iptables -t mangle -A PREROUTING -m conntrack --ctstate NEW -j HMARK --hmark-tuple ct,src,dst,proto --hmark-offset 10000 --hmark-mod 10 --hmark-rnd 0xfeedcafe

iptables -t mangle -A PREROUTING -j HMARK --hmark-offset 10000 --hmark-tuple src,dst,proto --hmark-mod 10 --hmark-rnd 0xdeafbeef
