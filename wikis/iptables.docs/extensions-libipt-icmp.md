# Extensions / Libipt Icmp

This extension can be used if \`--protocol icmp' is specified. It provides the following option:

\[**!**\] **--icmp-type** {*type*\[**/***code*\]\|*typename*}
This allows specification of the ICMP type, which can be a numeric ICMP type, type/code pair, or one of the ICMP type names shown by the command


     iptables -p icmp -h
