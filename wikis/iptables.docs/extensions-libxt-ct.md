# Extensions / Libxt CT

The CT target sets parameters for a packet or its associated connection. The target attaches a "template" connection tracking entry to the packet, which is then used by the conntrack core when initializing a new ct entry. This target is thus only valid in the "raw" table.

**--notrack**
Disables connection tracking for this packet.

**--helper** *name*
Use the helper identified by *name* for the connection. This is more flexible than loading the conntrack helper modules with preset ports.

**--ctevents** *event*\[**,**...\]
Only generate the specified conntrack events for this connection. Possible event types are: **new**, **related**, **destroy**, **reply**, **assured**, **protoinfo**, **helper**, **mark** (this refers to the ctmark, not nfmark), **natseqinfo**, **secmark** (ctsecmark).

**--expevents** *event*\[**,**...\]
Only generate the specified expectation events for this connection. Possible event types are: **new**.

**--zone-orig** {*id*\|**mark**}
For traffic coming from ORIGINAL direction, assign this packet to zone *id* and only have lookups done in that zone. If **mark** is used instead of *id*, the zone is derived from the packet nfmark.

**--zone-reply** {*id*\|**mark**}
For traffic coming from REPLY direction, assign this packet to zone *id* and only have lookups done in that zone. If **mark** is used instead of *id*, the zone is derived from the packet nfmark.

**--zone** {*id*\|**mark**}
Assign this packet to zone *id* and only have lookups done in that zone. If **mark** is used instead of *id*, the zone is derived from the packet nfmark. By default, packets have zone 0. This option applies to both directions.

**--timeout** *name*
Use the timeout policy identified by *name* for the connection. This is provides more flexible timeout policy definition than global timeout values available at /proc/sys/net/netfilter/nf_conntrack\_\*\_timeout\_\*.
