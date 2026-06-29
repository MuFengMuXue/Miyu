# Extensions / Libipt ECN

This target selectively works around known ECN blackholes. It can only be used in the mangle table.

**--ecn-tcp-remove**
Remove all ECN bits from the TCP header. Of course, it can only be used in conjunction with **-p tcp**.
