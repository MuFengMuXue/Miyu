**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Computer_cluster "wikipedia:Computer cluster")

A **cluster\'** is a set of computers that cooperate together to provide some service or perform some action.

Clusters-based designs are often adopted in preference to traditional network designs in order to achieve increased scalability, manageability or availability (sometimes referred to as *High Availability*, or *HA* for short).

## Contents

-   [[1] [Types of clusters]](#Types_of_clusters)
-   [[2] [Cluster architecture]](#Cluster_architecture)
    -   [[2.1] [Messaging layer]](#Messaging_layer)
    -   [[2.2] [Resource management layer]](#Resource_management_layer)
-   [[3] [Clusters on Gentoo]](#Clusters_on_Gentoo)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Types of clusters]

-   **Dense clusters** are those in which nodes are typically tightly connected with low latency, high bandwidth links (typically LANs). Such clusters are often vulnerable to site failures.
-   **Sparse clusters** are those in which nodes are spread across relatively higher latency, low bandwidth links such as long distance internet connectivity.
-   **HAC** High Availability Computing
-   **HPC** High Performance Computing
-   **HTC** High Throughput Computing
-   **HEC** High Efficiency Computing
-   Grid

## [Cluster architecture]

### [Messaging layer]

Clusters typically employ a *messaging layer* such as [Corosync](https://wiki.gentoo.org/wiki/Corosync "Corosync") (or the older [Heartbeat](https://wiki.gentoo.org/wiki/Heartbeat "Heartbeat")) to distribute information regarding cluster state changes between the participating nodes.

### [Resource management layer]

Cluster-based services are often managed by a *resource management* layer.

This layer may in turn be divided in to two components, the *cluster resource management* layer (typically taking in to account its view of the overall state of the cluster and all of its participants, and helping the cluster to maintain or transition towards some predefined, desirable state) and a *local resource management* layer (that might perform a similar function but within a single participating node).

## [Clusters on Gentoo]

Gentoo is well suited to building clusters due to its configurability (see also: *[Benefits of Gentoo](https://wiki.gentoo.org/wiki/Benefits_of_Gentoo "Benefits of Gentoo")*) and has been used to build a variety of clusters. Gentoo\'s cluster-related software is grouped under the *sys-cluster* section of [portage](https://wiki.gentoo.org/wiki/Portage "Portage").

Many modern Gentoo-based clusters make use of the [Corosync](https://wiki.gentoo.org/wiki/Corosync "Corosync") messaging layer and the [Pacemaker](https://wiki.gentoo.org/wiki/Pacemaker "Pacemaker") cluster resource manager (provided by the [Linux-HA Project](http://linux-ha.org/)).

## [See also]

-   [NFS](https://wiki.gentoo.org/wiki/NFS "NFS") --- a file system protocol that allows client machines to access network attached filesystems (called exports) from a host system.
-   [Syslinux](https://wiki.gentoo.org/wiki/Syslinux "Syslinux") --- a package that contains a family of [bootloaders](https://wiki.gentoo.org/wiki/Bootloader "Bootloader").
-   [Dnsmasq](https://wiki.gentoo.org/wiki/Dnsmasq "Dnsmasq") --- a simple DHCP/DNS server which can be used in a local network of up to a 1000 clients.

## [External resources]

-   [Linux-HA Project](http://linux-ha.org/)
-   [Linux Cluster HOWTO](http://www.tldp.org/HOWTO/pdf/Cluster-HOWTO.pdf)