Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Ceph/de "Ceph (100% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Ceph/hu "Ceph (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Ceph/ru "Ceph/ru (10% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Ceph/ja "Ceph (90% translated)")

**Resources**

[[]][Home](https://www.ceph.com/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ceph_(software) "wikipedia:Ceph (software)")

**Ceph** is a distributed object store and filesystem designed to provide excellent performance, reliability, and scalability. It is designed to have no single point of failure, and scale towards thousands of nodes participating in the distributed object store cluster.

## [[] Use cases]

Ceph provides three main storage features:

1.  Within a Ceph cluster, pools are made available in which objects can be stored and retrieved. Gateways (such as the Rados Gateway) and other applications can use this to keep their data in a highly available manner.
2.  A pool can be exposed as a file system. Each Ceph cluster can currently hold one file system which can be made accessible by Linux clients. This file system is POSIX compliant and can be used to build highly available NFS services (or directly use the mounted file system).
3.  Rados block devices are stored in the Ceph cluster and can be used to build highly available virtualized infrastructure (for instance virtual guest images on a highly available cluster).

## [[] Resources]

In order to support a Ceph cluster, some insights in how Ceph operates as well as its various components is necessary. An [introductory guide to Ceph](https://wiki.gentoo.org/wiki/Ceph/Guide "Ceph/Guide") is available on the wiki which not only explains how Ceph operates, but also introduces an example 3-host setup for Ceph.

For more in-depth information, please refer to the following resources.

  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------
  Concepts
  [Cluster](https://wiki.gentoo.org/wiki/Ceph/Cluster "Ceph/Cluster")                                             A Ceph cluster is the basic setup for any Ceph deployment.
  [Object Store Device (OSD)](https://wiki.gentoo.org/wiki/Ceph/Object_Store_Device "Ceph/Object Store Device")   A representation of a storage area in which Ceph uses to store objects.
  [Monitor (MON)](https://wiki.gentoo.org/wiki/Ceph/Monitor "Ceph/Monitor")                                       A quorum-supporting monitor to enable highly available operations even when some resources are unavailable.
  [Metadata Server (MDS)](https://wiki.gentoo.org/wiki/Ceph/Metadata_Server "Ceph/Metadata Server")               Metadata handling server used as the entrypoint for mounting Ceph\'s POSIX file system.
  [Rados Block Device](https://wiki.gentoo.org/wiki/Ceph/Rados_Block_Device "Ceph/Rados Block Device")            A Ceph-supported block device.
  User guides
  [Installation](https://wiki.gentoo.org/wiki/Ceph/Installation "Ceph/Installation")                              Installing Ceph on a Gentoo Linux environment.
  [Administration](https://wiki.gentoo.org/wiki/Ceph/Administration "Ceph/Administration")                        Administering a Ceph cluster.
  --------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------