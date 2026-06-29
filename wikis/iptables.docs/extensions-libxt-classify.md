# Extensions / Libxt CLASSIFY

This module allows you to set the skb-\>priority value (and thus classify the packet into a specific CBQ class).

**--set-class** *major***:***minor*
Set the major and minor class value. The values are always interpreted as hexadecimal even if no 0x prefix is given.
