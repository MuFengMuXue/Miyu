# Extensions / libip6t icmp6

This extension can be used if \`--protocol ipv6-icmp' or \`--protocol icmpv6' is specified. It provides the following option:

\[**!**\] **--icmpv6-type** *type*\[**/***code*\]\|*typename*
This allows specification of the ICMPv6 type, which can be a numeric ICMPv6 *type*, *type* and *code*, or one of the ICMPv6 type names shown by the command


     ip6tables -p ipv6-icmp -h
