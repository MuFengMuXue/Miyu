# Sysctl

sysctl is a tool for examining and changing kernel parameters at runtime. sysctl is implemented in procfs, the virtual process file system at .

## Installation
The  package should already be installed, as it is a dependency of the  meta package.

## Configuration
The sysctl preload/configuration file can be created at . For systemd,  and  are drop-in directories for kernel sysctl parameters. The naming and source directory decide the order of processing, which is important since the last parameter processed may override earlier ones. For example, parameters in a  will be overriden by equal parameters in  and any configuration file processed later from both directories.

To load all configuration files manually, execute:

 # sysctl --system

which will also output the applied hierarchy. A single parameter file can also be loaded explicitly with:

 # sysctl --load=filename.conf

See the new configuration files and more specifically  for more information.

The parameters available are those listed under . For example, the  parameter refers to the file  on the file system. The  command can be used to display all currently available values.

Settings can be changed through file manipulation or using the  utility. For example, to temporarily enable the magic SysRq key:

 # sysctl kernel.sysrq=1

or:

 # echo "1" > /proc/sys/kernel/sysrq

See Linux kernel documentation for details about .

To preserve changes between reboots, add or modify the appropriate lines in  or another applicable parameter file in .

## Security
See also Security#Kernel hardening, as well as the rest of this article.

## Networking
## Improving performance
## Increasing the size of the receive queue.
The received frames will be stored in this queue after taking them from the ring buffer on the network card.

Increasing this value for high speed cards may help prevent losing packets:

 net.core.netdev_max_backlog = 16384

## Increase the maximum connections
The upper limit on how many connections the kernel will accept (default 4096):

 net.core.somaxconn = 8192

## Increase the memory dedicated to the network interfaces
By default the Linux network stack is not configured for high speed large file transfer across WAN links (i.e. handle more network packets) and setting the correct values may save memory resources:

 net.core.rmem_default = 1048576
 net.core.rmem_max = 16777216
 net.core.wmem_default = 1048576
 net.core.wmem_max = 16777216
 net.core.optmem_max = 65536
 net.ipv4.tcp_rmem = 4096 1048576 2097152
 net.ipv4.tcp_wmem = 4096 65536 16777216

It is also possible increase the default  UDP limits:

 net.ipv4.udp_rmem_min = 8192
 net.ipv4.udp_wmem_min = 8192

See the following sources for more information and recommend values:

* http://www.nateware.com/linux-network-tuning-for-2013.html
* https://blog.cloudflare.com/the-story-of-one-latency-spike/

## Enable TCP Fast Open
TCP Fast Open is an extension to the transmission control protocol (TCP) that helps reduce network latency by enabling data to be exchanged during the sender’s initial TCP SYN Using the value  instead of the default  allows TCP Fast Open for both incoming and outgoing connections:

 net.ipv4.tcp_fastopen = 3

## Tweak the pending connection handling
 is the maximum queue length of pending connections 'Waiting Acknowledgment'.

In the event of a synflood DOS attack, this queue can fill up pretty quickly, at which point TCP SYN cookies will kick in allowing your system to continue to respond to legitimate traffic, and allowing you to gain access to block malicious IPs.

If the server suffers from overloads at peak times, you may want to increase this value a little bit:

 net.ipv4.tcp_max_syn_backlog = 8192

 is the maximum number of sockets in TIME_WAIT state.

After reaching this number the system will start destroying the socket that are in this state.

Increase this to prevent simple DOS attacks:

 net.ipv4.tcp_max_tw_buckets = 2000000

 sets whether TCP should reuse an existing connection in the TIME-WAIT state for a new outgoing connection if the new timestamp is strictly bigger than the most recent timestamp recorded for the previous connection.

The default value is , means it's enabled for loopback connections only. You can set it to  to enable for all connections, this helps avoid from running out of available network sockets:

 net.ipv4.tcp_tw_reuse = 1

Specify how many seconds to wait for a final FIN packet before the socket is forcibly closed.  This is strictly a violation  of  the TCP specification, but required to prevent denial-of-service attacks:

 net.ipv4.tcp_fin_timeout = 10

 sets whether TCP should start at the default window size only for new connections or also for existing connections that have been idle for too long.

This setting kills persistent single connection performance and could be turned off:

 net.ipv4.tcp_slow_start_after_idle = 0

## Change TCP keepalive parameters
TCP keepalive is a mechanism for TCP connections that help to determine whether the other end has stopped responding or not. TCP will send the keepalive probe that contains null data to the network peer several times after a period of idle time. If the peer does not respond, the socket will be closed automatically. By default, TCP keepalive process waits for two hours (7200 secs) for socket activity before sending the first keepalive probe, and then resend it every 75 seconds. As long as there is TCP/IP socket communications going on and active, no keepalive packets are needed.

 net.ipv4.tcp_keepalive_time = 60
 net.ipv4.tcp_keepalive_intvl = 10
 net.ipv4.tcp_keepalive_probes = 6

## Enable MTU probing
The longer the maximum transmission unit (MTU) the better for performance, but the worse for reliability.

This is because a lost packet means more data to be retransmitted and because many routers on the Internet cannot deliver very long packets:

 net.ipv4.tcp_mtu_probing = 1

See https://blog.cloudflare.com/path-mtu-discovery-in-practice/ for more information.

## TCP timestamps
Disabling timestamp generation will reduce spikes and may give a performance boost on gigabit networks:

 net.ipv4.tcp_timestamps = 0

## TCP Selective Acknowledgement
TCP Selective Acknowledgement (TCP SACK), controlled by the boolean , allows the receiving side to give the sender more detail about lost segments, reducing volume of retransmissions. This is useful on high latency networks, but disable this to improve throughput on high-speed LANs. Also disable , if you aren't sending SACK you certainly don't want to send duplicates! Forward Acknowledgement works on top of SACK and will be disabled if SACK is. [https://cromwell-intl.com/open-source/performance-tuning/tcp.html

 net.ipv4.tcp_sack = 1

## Enable BBR
The BBR congestion control algorithm can help achieve higher bandwidths and lower latencies for internet traffic. First, load the  module.

 net.core.default_qdisc = cake
 net.ipv4.tcp_congestion_control = bbr

## Increase the Ephemeral port range
The Wikipedia:Ephemeral port is typically used by the Transmission Control Protocol (TCP), User Datagram Protocol (UDP), or the Stream Control Transmission Protocol (SCTP) as the port assignment for the client end of a client–server communication.

 net.ipv4.ip_local_port_range = 30000 65535

## TCP/IP stack hardening
The following specifies a parameter set to tighten network security options of the kernel for the IPv4 protocol and related IPv6 parameters where an equivalent exists.

For some use-cases, for example using the system as a router, other parameters may be useful or required as well.

## TCP SYN cookie protection
Helps protect against SYN flood attacks. Only kicks in when  is reached. More details at, for example, As of  5.10, it is set by default.

 net.ipv4.tcp_syncookies = 1

## TCP rfc1337
Protect against tcp time-wait assassination hazards, drop RST packets for sockets in the time-wait state. Not widely supported outside of Linux,  but conforms to RFC:

 net.ipv4.tcp_rfc1337 = 1

## Reverse path filtering
By enabling reverse path filtering, the kernel will do source validation of the packets received from all the interfaces on the machine. This can protect from attackers that are using IP spoofing methods to do harm.

The kernel's default value is  (no source validation), but systemd ships  that sets  to  (loose mode)[https://github.com/systemd/systemd/pull/10971.

The following will set the reverse path filtering mechanism to value  (strict mode):

 net.ipv4.conf.default.rp_filter = 1
 net.ipv4.conf.all.rp_filter = 1

The relationship and behavior of ,  and  is explained in ip-sysctl.html.

## Log martian packets
A martian packet is an IP packet which specifies a source or destination address that is reserved for special-use by Internet Assigned Numbers Authority (IANA). See Reserved IP addresses for more details.

Often martian and unroutable packet may be used for a dangerous purpose. Logging these packets for further inspection may be useful net.ipv4.conf.default.log_martians = 1
 net.ipv4.conf.all.log_martians = 1

## Disable ICMP redirects
Background is at [https://askubuntu.com/questions/118273/what-are-icmp-redirects-and-should-they-be-blocked What are ICMP redirects? Should they be blocked?

To disable ICMP redirect acceptance:

 net.ipv4.conf.all.accept_redirects = 0
 net.ipv4.conf.default.accept_redirects = 0
 net.ipv4.conf.all.secure_redirects = 0
 net.ipv4.conf.default.secure_redirects = 0
 net.ipv6.conf.all.accept_redirects = 0
 net.ipv6.conf.default.accept_redirects = 0

To disable ICMP redirect sending when on a non router:

 net.ipv4.conf.all.send_redirects = 0
 net.ipv4.conf.default.send_redirects = 0

## Ignore ICMP echo requests
To disable ICMP echo (aka ping) requests:

 net.ipv4.icmp_echo_ignore_all = 1
 net.ipv6.icmp.echo_ignore_all = 1

## Other
## Allow unprivileged users to create IPPROTO_ICMP sockets
The IPPROTO_ICMP () socket type adds the possibility to send ICMP_ECHO messages and receive corresponding ICMP_ECHOREPLY messages without the need to open a  socket, an operation which requires the CAP_NET_RAW capability or the SUID bit with a proper privileged owner. These ICMP_ECHO messages are sent by the ping application thus making the IPPROTO_ICMP socket also known as ping socket in addition to ICMP Echo socket.

 determines the GID range of groups which their users are allowed to create IPPROTO_ICMP sockets. Additionally, the owner of the CAP_NET_RAW capability is also allowed to create IPPROTO_ICMP sockets. By default this range is  which means no one is allowed to create IPPROTO_ICMP sockets except root. To take advantage of this setting programs which currently uses raw sockets need to ported to use IPPROTO_ICMP sockets instead. For example, QEMU uses IPPROTO_ICMP for SLIRP aka User-mode networking, so allowing the user running QEMU to create IPPROTO_ICMP sockets means it is possible to ping from the guest.

To allow only users which are members of the group with GID 100 to create IPPROTO_ICMP sockets:

 net.ipv4.ping_group_range = 100 100

To allow all the users in the system to create IPPROTO_ICMP sockets:

 net.ipv4.ping_group_range = 0 65535

## Virtual memory
There are several key parameters to tune the operation of the virtual memory subsystem of the Linux kernel and the write out of dirty data to disk. See the official Linux kernel documentation for more information. For example:

*
: Contains, as a percentage of total available memory that contains free pages and reclaimable pages, the number of pages at which a process which is generating disk writes will itself start writing out dirty data.

*
: Contains, as a percentage of total available memory that contains free pages and reclaimable pages, the number of pages at which the background kernel flusher threads will start writing out dirty data.

As noted in the comments for the parameters, one needs to consider the total amount of RAM when setting these values. For example, simplifying by taking the installed system RAM instead of available memory:

* Consensus is that setting  to 10% of RAM is a sane value if RAM is say 1 GB (so 10% is  MB). But if the machine has much more RAM, say 16 GB (10% is  GB), the percentage may be out of proportion as it becomes several seconds of writeback on spinning disks. A more sane value in this case may be  (3% of 16 GB is approximately 491 MB).
* Similarly, setting  to  may be just fine for small memory values, but again, consider and adjust accordingly for the amount of RAM on a particular system.

## VFS cache
Decreasing the virtual file system (VFS) cache parameter value may improve system responsiveness:

*
: The value controls the tendency of the kernel to reclaim the memory which is used for caching of directory and inode objects (VFS cache). Lowering it from the default value of 100 makes the kernel less inclined to reclaim VFS cache (do not set it to 0, this may produce out-of-memory conditions).

## MDADM
See RAID#Change sync speed limits.

## Troubleshooting
## Small periodic system freezes
Set dirty bytes to small enough value (for example 4 MiB):

 vm.dirty_background_bytes = 4194304
 vm.dirty_bytes = 4194304
