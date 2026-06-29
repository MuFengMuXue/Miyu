# Ceph

Ceph is a storage platform with a focus on being distributed, resilient, and having good performance and high reliability. Ceph can also be used as a block storage solution for virtual machines or through the use of FUSE, a conventional filesystem. Ceph is extremely configurable, with administrators being able to control virtually all aspects of the system. A command line interface is used to monitor and control the cluster. The platform also contains authentication & authorization features, and various gateways to make it compatible with systems such as OpenStack Swift and Amazon S3.

From Wikipedia: Ceph (software):
:Ceph is a free software storage platform designed to present object, block, and file storage from a single distributed computer cluster. Ceph's main goals are to be completely distributed without a single point of failure, scalable to the exabyte level, and freely-available. The data is replicated, making it fault tolerant.

From Ceph.com:
:Ceph is a distributed object store and file system designed to provide excellent performance, reliability and scalability.

## Terminology
* Client : Something which connects to a Ceph cluster to access data but is not part of the Ceph cluster itself.
* MONs : Also known as monitors, these store cluster state and maps containing information about the cluster such as running services and data locations.
* MDSs : Also known as metadata servers, these store metadata for the Ceph filesystem to reduce load on the storage cluster (e.g. information for commands such as ).
* Node : A machine which is running Ceph services, such as OSDs or MONs.
* OSDs : Also known as OSD daemons, these are responsible for the storage of data within the cluster and also conduct various related operations such as replication, recovery, and rebalancing.
* Storage cluster : The core set of software responsible for storing data (OSDs+MONs).

## Installation
## Packages
Install it with the package .

Install  on all nodes that will be in the cluster.

## NTP Client
Install and run a time synchronisation client on the node. See Time synchronization for details.

## Bootstrapping a storage cluster
Before a storage cluster can operate, the monitors for that cluster must be bootstrapped with several identifiers and keyrings.

The upstream Ceph documentation is well-written and kept updated with the latest releases.

To boostrap a storage cluster, follow the steps documented in the official manual deployment guide.

## Starting a monitor
Since your system most likely uses systemd, you can enable a monitor as a systemd unit.

As an example, for a monitor named  start and enable .
