# Extensions / Libxt Dscp

This module matches the 6 bit DSCP field within the TOS field in the IP header. DSCP has superseded TOS within the IETF.

\[**!**\] **--dscp** *value*
Match against a numeric (decimal or hex) value in the range 0–63.

\[**!**\] **--dscp-class** *class*
Match the DiffServ class. This value may be any of the BE, EF, AFxx or CSx classes. It will then be converted into its according numeric value.
