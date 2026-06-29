# Extensions / Libxt NETMAP

This target allows you to statically map a whole network of addresses onto another network of addresses. It can only be used from rules in the **nat** table.

**--to** *address*\[**/***mask*\]
Network address to map to. The resulting address will be constructed in the following way: All 'one' bits in the mask are filled in from the new \`address'. All bits that are zero in the mask are filled in from the original address.

IPv6 support available since Linux kernels \>= 3.7.
