# Extensions / libip6t HL

This is used to modify the Hop Limit field in IPv6 header. The Hop Limit field is similar to what is known as TTL value in IPv4. Setting or incrementing the Hop Limit field can potentially be very dangerous, so it should be avoided at any cost. This target is only valid in **mangle** table.

**Don't ever set or increment the value on packets that leave your local network!**

**--hl-set** *value*
Set the Hop Limit to \`value'.

**--hl-dec** *value*
Decrement the Hop Limit \`value' times.

**--hl-inc** *value*
Increment the Hop Limit \`value' times.
