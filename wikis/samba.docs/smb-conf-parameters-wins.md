# smb.conf Parameters / wins

### `dns proxy`

Section: wins; Context: G; Type: boolean; Default: `yes`

Specifies that nmbd 8 when acting as a WINS server and finding that a NetBIOS name has not been registered, should treat the NetBIOS name word-for-word as a DNS name and do a lookup with the DNS server for that name on behalf of the name-querying client. Note that the maximum length for a NetBIOS name is 15 characters, so the DNS name (or DNS alias) can likewise only be 15 characters, maximum. nmbd spawns a second copy of itself to do the DNS name lookup requests, as doing a name lookup is a blocking action.

### `max wins ttl`

Section: wins; Context: G; Type: integer; Default: `518400`

This option tells smbd 8 when acting as a WINS server ( yes ) what the maximum 'time to live' of NetBIOS names that nmbd will grant will be (in seconds). You should never need to change this parameter. The default is 6 days (518400 seconds).

### `min wins ttl`

Section: wins; Context: G; Type: integer; Default: `21600`

This option tells nmbd 8 when acting as a WINS server ( yes ) what the minimum 'time to live' of NetBIOS names that nmbd will grant will be (in seconds). You should never need to change this parameter. The default is 6 hours (21600 seconds).

### `nbtd:wins_prepend1Bto1Cqueries`

Section: wins; Context: G; Type: string; Default: `yes`

Normally queries for 0x1C names (all logon servers for a domain) will return the first address of the 0x1B names (domain master browser and PDC) as first address in the result list. As many client only use the first address in the list by default, all clients will use the same server (the PDC). Windows servers have an option to disable this behavior (since Windows 2000 Service Pack 2).

### `nbtd:wins_wins_randomize1Clist`

Section: wins; Context: G; Type: string; Default: `no`

Normally queries for 0x1C names will return the addresses in the same order as they're stored in the database, that means first all addresses which have been directly registered at the local wins server and then all addresses registered at other servers. Windows servers have an option to change this behavior and randomize the returned addresses. Set this parameter to "yes" and Samba will sort the address list depending on the client address and the matching bits of the addresses, the first address is randomized based on depending on the "nbtd:wins_randomize1Clist_mask" parameter.

### `nbtd:wins_randomize1Clist_mask`

Section: wins; Context: G; Type: string; Default: `255.255.255.0`

If the "nbtd:wins_randomize1Clist" parameter is set to "yes", then randomizing of the first returned address is based on the specified netmask. If there are addresses which are in the same subnet as the client address, the first returned address is randomly chosen out them. Otherwise the first returned address is randomly chosen out of all addresses.

### `winsdb:local_owner`

Section: wins; Context: G; Type: string

This specifies the address that is stored in the winsOwner attribute, of locally registered winsRecord-objects. The default is to use the ip-address of the first network interface.

### `winsdb:dbnosync`

Section: wins; Context: G; Type: string; Default: `no`

This parameter disables fsync() after changes of the WINS database.

### `wins hook`

Section: wins; Context: G; Type: string

When Samba is running as a WINS server this allows you to call an external program for all changes to the WINS database. The primary use for this option is to allow the dynamic update of external name resolution databases such as dynamic DNS. The wins hook parameter specifies the name of a script or executable that will be called as follows: wins_hook operation name nametype ttl IP_list The first argument is the operation and is one of "add", "delete", or "refresh". In most cases the operation can be ignored as the rest of the parameters provide sufficient information. Note that "refresh" may sometimes be called when the name has not previously been added, in that case it should be treated as an add. The second argument is the NetBIOS name. If the name is not a legal name then the wins hook is not called. Legal names contain only letters, digits, hyphens, underscores and periods. The third argument is the NetBIOS name type as a 2 digit hexadecimal number. The fourth argument is the TTL (time to live) for the name in seconds. The fifth and subsequent arguments are the IP addresses currently registered for that name. If this list is empty then the name should be deleted. An example script that calls the BIND dynamic DNS update program nsupdate is provided in the examples directory of the Samba source code.

### `wins proxy`

Section: wins; Context: G; Type: boolean; Default: `no`

This is a boolean that controls if nmbd 8 will respond to broadcast name queries on behalf of other hosts. You may need to set this to yes for some older clients.

### `wins server`

Section: wins; Context: G; Type: cmdlist

This specifies the IP address (or DNS name: IP address for preference) of the WINS server that nmbd 8 should register with. If you have a WINS server on your network then you should set this to the WINS server's IP. You should point this at your WINS server if you have a multi-subnetted network. If you want to work in multiple namespaces, you can give every wins server a 'tag'. For each tag, only one (working) server will be queried for a name. The tag should be separated from the ip address by a colon. You need to set up Samba to point to a WINS server if you have multiple subnets and wish cross-subnet browsing to work correctly. See the chapter in the Samba3-HOWTO on Network Browsing.

### `wins support`

Section: wins; Context: G; Type: boolean; Default: `no`

This boolean controls if the nmbd 8 process in Samba will act as a WINS server. You should not set this to yes unless you have a multi-subnetted network and you wish a particular nmbd to be your WINS server. Note that you should NEVER set this to yes on more than one machine in your network.

### `wreplsrv:periodic_interval`

Section: wins; Context: G; Type: string; Default: `15`

This maximum interval in seconds between 2 periodically scheduled runs where we check for wins.ldb changes and do push notifications to our push partners. Also wins_config.ldb changes are checked in that interval and partner configuration reloads are done.

### `wreplsrv:propagate name releases`

Section: wins; Context: G; Type: string; Default: `no`

If this parameter is enabled, then explicit (from the client) and implicit (via the scavenging) name releases are propagated to the other servers directly, even if there are still other addresses active, this applies to SPECIAL GROUP (2) and MULTIHOMED (3) entries. Also the replication conflict merge algorithm for SPECIAL GROUP (2) entries discards replica addresses where the address owner is the local server, if the address was not stored locally before. The merge result is propagated directly in case an address was discarded. A Windows servers doesn't propagate name releases of SPECIAL GROUP (2) and MULTIHOMED (3) entries directly, which means that Windows servers may return different results to name queries for SPECIAL GROUP (2) and MULTIHOMED (3) names. The option doesn't have much negative impact if Windows servers are around, but be aware that they might return unexpected results.

### `wreplsrv:scavenging_interval`

Section: wins; Context: G; Type: string

This is the interval in s between 2 scavenging runs which clean up the WINS database and changes the states of expired name records. Defaults to half of the value of wreplsrv:renew_interval.

### `wreplsrv:tombstone_extra_timeout`

Section: wins; Context: G; Type: string; Default: `259200`

This is the time in s the server needs to be up till we'll remove tombstone records from our database. Defaults to 3 days.

### `wreplsrv:tombstone_interval`

Section: wins; Context: G; Type: string; Default: `518400`

This is the interval in s till released records of the WINS server become tombstone. Defaults to 6 days.

### `wreplsrv:tombstone_timeout`

Section: wins; Context: G; Type: string; Default: `86400`

This is the interval in s till tombstone records are deleted from the WINS database. Defaults to 1 day.

### `wreplsrv:verify_interval`

Section: wins; Context: G; Type: string; Default: `2073600`

This is the interval in s till we verify active replica records with the owning WINS server. Unfortunately not implemented yet. Defaults to 24 days.
