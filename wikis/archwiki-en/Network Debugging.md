# Network Debugging

## Ping & Tracepath/Traceroute
The ping command can help test connectivity towards a specific host.

The first step would be verifying connectivity towards the default gateway (replace the ip address with your own default gateway):

 $ ping -c4 192.168.1.1

When erasing the "-c4" parameter, the ping will continue endlessly. It can be aborted by hitting "Control-C".

 PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
 64 bytes from 192.168.1.1: icmp_req=1 ttl=64 time=0.193 ms
 64 bytes from 192.168.1.1: icmp_req=2 ttl=64 time=0.190 ms
 64 bytes from 192.168.1.1: icmp_req=3 ttl=64 time=0.192 ms
 64 bytes from 192.168.1.1: icmp_req=4 ttl=64 time=0.189 ms

 --- 192.168.1.1 ping statistics ---
 4 packets transmitted, 4 received, 0% packet loss, time 2999ms
 rtt min/avg/max/mdev = 0.165/0.184/0.193/0.014 ms

The output above indicated the default gateway is reachable. When instead a "" message is displayed, doublecheck the ip address, netmask and default gateway config. This message can also be displayed when ICMP traffic is not permitted towards the default gateway (blocked by a firewall, router,...).

The next step is verifying connectivity towards the configured dns server(s). When no reply is received,  or  can be used to verify the routing towards said server and get an idea of where the issue lies.

 $ traceroute 8.8.4.4

Traceroute also used ICMP to determine the path and hence there can be "no reply" answers as well when ICMP traffic is blocked.

## Tcpdump
, and its underlying library , are multi-platform user space interfaces to the packets on the network. It should be emphasized they do see, they can capture, any inbound packets that reach the local NIC. No matter if the local software firewall is blocking those packets, or not. On the other hand, they can only see outbound packets the firewall passes through: A short, unintimidating introduction to tcpdump, with examples, is at: [https://wizardzines.com/zines/tcpdump/
