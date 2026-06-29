# Bridge with netctl

Make sure netctl is installed.

Copy  to .

In this example, we create a bridge called  which has real Ethernet adapter  and (optionally) a tap device  connected to it. Of course, edit ,  and  to your needs.

This example creates a statically assigned bridge called  which has real Ethernet adapter  connected to it. Edit , , , , and  according to your needs.

You can bridge any combination of network devices editing  option.

If any of the bridged devices (e.g. , ) had dhcpcd enabled, stop and disable the  daemon. Or set  to the netctl profiles.

Finally, start and enable your .
