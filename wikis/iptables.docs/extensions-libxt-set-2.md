# Extensions / Libxt Set

This module matches IP sets which can be defined by ipset(8).

\[**!**\] **--match-set** *setname* *flag*\[**,***flag*\]...
where flags are the comma separated list of **src** and/or **dst** specifications and there can be no more than six of them. Hence the command

iptables -A FORWARD -m set --match-set test src,dst

will match packets, for which (if the set type is ipportmap) the source address and destination port pair can be found in the specified set. If the set type of the specified set is single dimension (for example ipmap), then the command will match packets for which the source address can be found in the specified set.

**--return-nomatch**
If the **--return-nomatch** option is specified and the set type supports the **nomatch** flag, then the matching is reversed: a match with an element flagged with **nomatch** returns **true**, while a match with a plain element returns **false**.

**!** **--update-counters**
If the **--update-counters** flag is negated, then the packet and byte counters of the matching element in the set won't be updated. Default the packet and byte counters are updated.

**!** **--update-subcounters**
If the **--update-subcounters** flag is negated, then the packet and byte counters of the matching element in the member set of a list type of set won't be updated. Default the packet and byte counters are updated.

\[**!**\] **--packets-eq** *value*
If the packet is matched an element in the set, match only if the packet counter of the element matches the given value too.

**--packets-lt** *value*
If the packet is matched an element in the set, match only if the packet counter of the element is less than the given value as well.

**--packets-gt** *value*
If the packet is matched an element in the set, match only if the packet counter of the element is greater than the given value as well.

\[**!**\] **--bytes-eq** *value*
If the packet is matched an element in the set, match only if the byte counter of the element matches the given value too.

**--bytes-lt** *value*
If the packet is matched an element in the set, match only if the byte counter of the element is less than the given value as well.

**--bytes-gt** *value*
If the packet is matched an element in the set, match only if the byte counter of the element is greater than the given value as well.

The packet and byte counters related options and flags are ignored when the set was defined without counter support.

The option **--match-set** can be replaced by **--set** if that does not clash with an option of other extensions.

Use of -m set requires that ipset kernel support is provided, which, for standard kernels, is the case since Linux 2.6.39.
