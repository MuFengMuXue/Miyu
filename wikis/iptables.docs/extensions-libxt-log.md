# Extensions / Libxt LOG

Turn on kernel logging of matching packets. When this option is set for a rule, the Linux kernel will print some information on all matching packets (like most IP/IPv6 header fields) via the kernel log (where it can be read with *dmesg(1)* or read in the syslog).

This is a "non-terminating target", i.e. rule traversal continues at the next rule. So if you want to LOG the packets you refuse, use two separate rules with the same matching criteria, first using target LOG then DROP (or REJECT).

**--log-level** *level*
Level of logging, which can be (system-specific) numeric or a mnemonic. Possible values are (in decreasing order of priority): **emerg**, **alert**, **crit**, **error**, **warning**, **notice**, **info** or **debug**.

**--log-prefix** *prefix*
Prefix log messages with the specified prefix; up to 29 letters long, and useful for distinguishing messages in the logs.

**--log-tcp-sequence**
Log TCP sequence numbers. This is a security risk if the log is readable by users.

**--log-tcp-options**
Log options from the TCP packet header.

**--log-ip-options**
Log options from the IP/IPv6 packet header.

**--log-uid**
Log the userid of the process which generated the packet.

**--log-macdecode**
Log MAC addresses and protocol.
