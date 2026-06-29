# Extensions / Libipt ULOG

This is the deprecated IPv4-only predecessor of the NFLOG target. It provides userspace logging of matching packets. When this target is set for a rule, the Linux kernel will multicast this packet through a *netlink* socket. One or more userspace processes may then subscribe to various multicast groups and receive the packets. Like LOG, this is a "non-terminating target", i.e. rule traversal continues at the next rule.

**--ulog-nlgroup** *nlgroup*
This specifies the netlink group (1–32) to which the packet is sent. Default value is 1.

**--ulog-prefix** *prefix*
Prefix log messages with the specified prefix; up to 32 characters long, and useful for distinguishing messages in the logs.

**--ulog-cprange** *size*
Number of bytes to be copied to userspace. A value of 0 always copies the entire packet, regardless of its size. Default is 0.

**--ulog-qthreshold** *size*
Number of packet to queue inside kernel. Setting this value to, e.g. 10 accumulates ten packets inside the kernel and transmits them as one netlink multipart message to userspace. Default is 1 (for backwards compatibility).
