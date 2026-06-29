# Extensions / Libxt Cluster

Allows you to deploy gateway and back-end load-sharing clusters without the need of load-balancers.

This match requires that all the nodes see the same packets. Thus, the cluster match decides if this node has to handle a packet given the following options:

**--cluster-total-nodes** *num*
Set number of total nodes in cluster.

\[**!**\] **--cluster-local-node** *num*
Set the local node number ID.

\[**!**\] **--cluster-local-nodemask** *mask*
Set the local node number ID mask. You can use this option instead of **--cluster-local-node**.

**--cluster-hash-seed** *value*
Set seed value of the Jenkins hash.

Example:

> iptables -A PREROUTING -t mangle -i eth1 -m cluster --cluster-total-nodes 2 --cluster-local-node 1 --cluster-hash-seed 0xdeadbeef -j MARK --set-mark 0xffff

> iptables -A PREROUTING -t mangle -i eth2 -m cluster --cluster-total-nodes 2 --cluster-local-node 1 --cluster-hash-seed 0xdeadbeef -j MARK --set-mark 0xffff

> iptables -A PREROUTING -t mangle -i eth1 -m mark ! --mark 0xffff -j DROP

> iptables -A PREROUTING -t mangle -i eth2 -m mark ! --mark 0xffff -j DROP

And the following commands to make all nodes see the same packets:

> ip maddr add 01:00:5e:00:01:01 dev eth1

> ip maddr add 01:00:5e:00:01:02 dev eth2

> arptables -A OUTPUT -o eth1 --h-length 6 -j mangle --mangle-mac-s 01:00:5e:00:01:01

> arptables -A INPUT -i eth1 --h-length 6 --destination-mac 01:00:5e:00:01:01 -j mangle --mangle-mac-d 00:zz:yy:xx:5a:27

> arptables -A OUTPUT -o eth2 --h-length 6 -j mangle --mangle-mac-s 01:00:5e:00:01:02

> arptables -A INPUT -i eth2 --h-length 6 --destination-mac 01:00:5e:00:01:02 -j mangle --mangle-mac-d 00:zz:yy:xx:5a:27

**NOTE**: the arptables commands above use mainstream syntax. If you are using arptables-jf included in some RedHat, CentOS and Fedora versions, you will hit syntax errors. Therefore, you'll have to adapt these to the arptables-jf syntax to get them working.

In the case of TCP connections, pickup facility has to be disabled to avoid marking TCP ACK packets coming in the reply direction as valid.

> echo 0 \> /proc/sys/net/netfilter/nf_conntrack_tcp_loose
