# Extensions / Libxt SET

This module adds and/or deletes entries from IP sets which can be defined by ipset(8).

**--add-set** *setname* *flag*\[**,***flag*...\]
add the address(es)/port(s) of the packet to the set

**--del-set** *setname* *flag*\[**,***flag*...\]
delete the address(es)/port(s) of the packet from the set

**--map-set** *setname* *flag*\[**,***flag*...\]
\[--map-mark\] \[--map-prio\] \[--map-queue\] map packet properties (firewall mark, tc priority, hardware queue)

where *flag*(s) are **src** and/or **dst** specifications and there can be no more than six of them.

**--timeout** *value*
when adding an entry, the timeout value to use instead of the default one from the set definition

**--exist**
when adding an entry if it already exists, reset the timeout value to the specified one or to the default from the set definition

**--map-set** *set-name*
the set-name should be created with --skbinfo option **--map-mark** map firewall mark to packet by lookup of value in the set **--map-prio** map traffic control priority to packet by lookup of value in the set **--map-queue** map hardware NIC queue to packet by lookup of value in the set

The **--map-set** option can be used from the mangle table only. The **--map-prio** and **--map-queue** flags can be used in the OUTPUT, FORWARD and POSTROUTING chains.

Use of -j SET requires that ipset kernel support is provided, which, for standard kernels, is the case since Linux 2.6.39.
