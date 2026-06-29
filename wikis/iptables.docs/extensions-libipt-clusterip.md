# Extensions / Libipt CLUSTERIP

This module allows you to configure a simple cluster of nodes that share a certain IP and MAC address without an explicit load balancer in front of them. Connections are statically distributed between the nodes in this cluster.

Please note that CLUSTERIP target is considered deprecated in favour of cluster match which is more flexible and not limited to IPv4.

**--new**
Create a new ClusterIP. You always have to set this on the first rule for a given ClusterIP.

**--hashmode** *mode*
Specify the hashing mode. Has to be one of **sourceip**, **sourceip-sourceport**, **sourceip-sourceport-destport**.

**--clustermac** *mac*
Specify the ClusterIP MAC address. Has to be a link-layer multicast address

**--total-nodes** *num*
Number of total nodes within this cluster.

**--local-node** *num*
Local node number within this cluster.

**--hash-init** *rnd*
Specify the random seed used for hash initialization.
