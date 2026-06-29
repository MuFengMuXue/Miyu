# Extensions / Libxt DSCP

This target alters the value of the DSCP bits within the TOS header of the IPv4 packet. As this manipulates a packet, it can only be used in the mangle table.

**--set-dscp** *value*
Set the DSCP field to a numerical value (can be decimal or hex)

**--set-dscp-class** *class*
Set the DSCP field to a DiffServ class.
