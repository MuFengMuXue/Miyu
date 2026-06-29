# Macvtap

A macvtap device is a newer device driver that enables Network bridge-like networking, but with a much simpler set up process. This is most useful for virtualization. For most purposes, the only disadvantage compared to a network bridge is that the host will not be able to communicate with the guests via this network.

## Setting up a macvtap network
Create a macvtap interface  that is bridged to  with these commands:

 # ip link add link eth0 name macvtap0 type macvtap
 # ip link set macvtap0 up

## Troubleshooting
## Guest virtual machine can reach outside network, but cannot reach host
See for solution.
