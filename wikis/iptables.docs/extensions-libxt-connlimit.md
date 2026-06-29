# Extensions / Libxt Connlimit

Allows you to restrict the number of parallel connections to a server per client IP address (or client address block).

**--connlimit-upto** *n*
Match if the number of existing connections is below or equal *n*.

**--connlimit-above** *n*
Match if the number of existing connections is above *n*.

**--connlimit-mask** *prefix_length*
Group hosts using the prefix length. For IPv4, this must be a number between (including) 0 and 32. For IPv6, between 0 and 128. If not specified, the maximum prefix length for the applicable protocol is used.

**--connlimit-saddr**
Apply the limit onto the source group. This is the default if --connlimit-daddr is not specified.

**--connlimit-daddr**
Apply the limit onto the destination group.

Examples:

- allow 2 telnet connections per client host:
  iptables -A INPUT -p tcp --syn --dport 23 -m connlimit --connlimit-above 2 -j REJECT

- you can also match the other way around:
  iptables -A INPUT -p tcp --syn --dport 23 -m connlimit --connlimit-upto 2 -j ACCEPT

- limit the number of parallel HTTP requests to 16 per class C sized source network (24 bit netmask):
  iptables -p tcp --syn --dport 80 -m connlimit --connlimit-above 16 --connlimit-mask 24 -j REJECT

- limit the number of parallel HTTP requests to 16 for the link local network (IPv6):
  ip6tables -p tcp --syn --dport 80 -s fe80::/64 -m connlimit --connlimit-above 16 --connlimit-mask 64 -j REJECT

- Limit the number of connections to a particular host:
  ip6tables -p tcp --syn --dport 49152:65535 -d 2001:db8::1 -m connlimit --connlimit-above 100 -j REJECT
