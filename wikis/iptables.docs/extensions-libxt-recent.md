# Extensions / Libxt Recent

Allows you to dynamically create a list of IP addresses and then match against that list in a few different ways.

For example, you can create a "badguy" list out of people attempting to connect to port 139 on your firewall and then DROP all future packets from them without considering them.

**--set**, **--rcheck**, **--update** and **--remove** are mutually exclusive.

**--name** *name*
Specify the list to use for the commands. If no name is given then **DEFAULT** will be used.

\[**!**\] **--set**
This will add the source address of the packet to the list. If the source address is already in the list, this will update the existing entry. This will always return success (or failure if **!** is passed in).

**--rsource**
Match/save the source address of each packet in the recent list table. This is the default.

**--rdest**
Match/save the destination address of each packet in the recent list table.

**--mask** *netmask*
Netmask that will be applied to this recent list.

\[**!**\] **--rcheck**
Check if the source address of the packet is currently in the list.

\[**!**\] **--update**
Like **--rcheck**, except it will update the "last seen" timestamp if it matches.

\[**!**\] **--remove**
Check if the source address of the packet is currently in the list and if so that address will be removed from the list and the rule will return true. If the address is not found, false is returned.

**--seconds** *seconds*
This option must be used in conjunction with one of **--rcheck** or **--update**. When used, this will narrow the match to only happen when the address is in the list and was seen within the last given number of seconds.

**--reap**
This option can only be used in conjunction with **--seconds**. When used, this will cause entries older than the last given number of seconds to be purged.

**--hitcount** *hits*
This option must be used in conjunction with one of **--rcheck** or **--update**. When used, this will narrow the match to only happen when the address is in the list and packets had been received greater than or equal to the given value. This option may be used along with **--seconds** to create an even narrower match requiring a certain number of hits within a specific time frame.

**--rttl**
This option may only be used in conjunction with one of **--rcheck** or **--update**. When used, this will narrow the match to only happen when the address is in the list and the TTL of the current packet matches that of the packet which hit the **--set** rule. This may be useful if you have problems with people faking their source address in order to DoS you via this module by disallowing others access to your site by sending bogus packets to you.

Examples:

> iptables -A FORWARD -m recent --name badguy --rcheck --seconds 60 -j DROP

> iptables -A FORWARD -p tcp -i eth0 --dport 139 -m recent --name badguy --set -j DROP

**/proc/net/xt_recent/\*** are the current lists of addresses and information about each entry of each list.

Each file in **/proc/net/xt_recent/** can be read from to see the current list or written two using the following commands to modify the list:

**echo +***addr* **\>/proc/net/xt_recent/DEFAULT**
to add *addr* to the DEFAULT list

**echo -***addr* **\>/proc/net/xt_recent/DEFAULT**
to remove *addr* from the DEFAULT list

**echo / \>/proc/net/xt_recent/DEFAULT**
to flush the DEFAULT list (remove all entries).

The module itself accepts parameters, defaults shown:

**ip_list_tot**=*100*
Number of addresses remembered per table.

**ip_pkt_list_tot**=*0*
Number of packets per address remembered. This parameter is obsolete since kernel version 3.19 which started to calculate the table size based on given **--hitcount** parameter.

**ip_list_hash_size**=*0*
Hash table size. 0 means to calculate it based on ip_list_tot by rounding it up to the next power of two (with **ip_list_tot** defaulting to *100*, **ip_list_hash_size** will calculate to *128* by default).

**ip_list_perms**=*0644*
Permissions for /proc/net/xt_recent/\* files.

**ip_list_uid**=*0*
Numerical UID for ownership of /proc/net/xt_recent/\* files.

**ip_list_gid**=*0*
Numerical GID for ownership of /proc/net/xt_recent/\* files.
