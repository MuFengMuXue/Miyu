# Extensions / libip6t Mh

This extension is loaded if \`--protocol ipv6-mh' or \`--protocol mh' is specified. It provides the following option:

\[**!**\] **--mh-type** *type*\[**:***type*\]
This allows specification of the Mobility Header(MH) type, which can be a numeric MH *type*, *type* or one of the MH type names shown by the command


     ip6tables -p mh -h
