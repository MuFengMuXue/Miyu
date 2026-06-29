# Extensions / Libxt Comment

Allows you to add comments (up to 256 characters) to any rule.

**--comment** *comment*
Example:
iptables -A INPUT -i eth1 -m comment --comment "my local LAN"
