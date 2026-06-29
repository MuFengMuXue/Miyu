# BeeGFS

BeeGFS is a scalable network-storage platform with a focus on being distributed, resilient, highly configurable and having good performance and high reliability. BeeGFS is extremely configurable, with administrators being able to control virtually all aspects of the system. A command line interface is used to monitor and control the cluster.

From Wikipedia:
:BeeGFS (formerly FhGFS) is a parallel file system, developed and optimized for high-performance computing. BeeGFS includes a distributed metadata architecture for scalability and flexibility reasons. Its most important aspect is data throughput. BeeGFS was originally developed at the Fraunhofer Center for High Performance Computing in Germany by a team around Sven Breuner, who later became the CEO of ThinkParQ, the spin-off company that was founded in 2014 to maintain BeeGFS and offer professional services.

From BeeGFS.io:
:BeeGFS is the leading parallel cluster file system, developed with a strong focus on performance and designed for very easy installation and management. If I/O intensive workloads are your problem, BeeGFS is the solution.

## Terminology
{| class="wikitable"
!Node Type and Description
!Packages
|-
|Management Server (one node)
* Manages configuration and group membership
* Hostname or IP address must be known by other nodes at service start time
|
|-
|Metadata Server (at least one node)
* Stores directory information and allocates file space on storage servers
|
|-
|Storage Server (at least one node)
* Stores raw file contents
|
|-
|InfluxDB / Grafana based Monitoring Server (optional)
* Continuous monitoring of servers
* Live statistics
* beegfs-admon (Java based administration and monitoring GUI), must not be installed on the same server
|
|-
|BeeGFS utilities for administrators
*  tool for command-line administration
*  tool for file system checking
* Several small helper scripts such logging and DNS lookup functionality
|
|-
|BeeGFS Common
* Common files for all packages
* Enables support for remote direct memory access  based on the OpenFabrics IBVerbs API, through .
|
|-
|Client
* Kernel module to mount the file system
* Requires userspace helper daemon for logging and hostname resolution
|
|}

In addition to the free and open-source packages described here, BeeGFS also offers a number of Enterprise Features and Professional Support, which include:
* High Availability
* Quota Enforcement
* Access Control Lists (ACLs)
* Storage Pools
* Burst buffer function with BeeOND

## Installation
## Example cluster deployment
The following hardware configuration will be used in this example:
{| class="wikitable"
!Hostname
!IP Address
!Description
|-
|node01
|
|Management Server and Monitoring (optional) Server
|-
|node02
|
|Metadata Server
|-
|node03
|
|Storage Server
|-
|node04
|
|Client
|}

## NTP client
Install and run a time synchronization client on all the nodes. See Time synchronization for details.

## Management server
Install it with the package  on the management node .

The management service needs to know where it can store its data. It will only store some node information like connectivity data, so it will not require much storage space and its data access is not performance critical. Thus, this service is typically not running on a dedicated machine.

Start/enable the  on the management node.

## Monitoring server
Install the package   on the management/monitoring node , which collects statistics from the system and provides them to the user using a time series database InfluxDB. For visualization of the data  provides predefined Grafana panels that can be used out of the box.

Before running , you need to edit the configuration file . If you have everything installed on the same host, you only need to specify the management host:

Start/enable the  on the management/monitoring node.

## Configuration of default Grafana panels
You can use the provided installation script for default InfluxDB and Grafana deployments on the same host.

 # cd /etc/beegfs/grafana
 # ./import-dashboards default

## Accessing Grafana panels
Access the application on localhost, e.g.: http://127.0.0.1:3000 . Refer to Custom Grafana Panel Configuration for non-default installations and for the Reference to All Metrics monitored.

## Metadata server
Install the package  on the metadata server(s), i.e. .

The metadata service needs to know where it can store its data and where the management service is running. Typically, one will have multiple metadata services running on different machines.

Start/enable the  on the metadata node.

## Storage server
Install the package  on the storage server(s), i.e. .

The storage service needs to know where it can store its data and how to reach the management server. Typically, one will have multiple storage services running on different machines and/or multiple storage targets (e.g. multiple RAID volumes) per storage service.

Start/enable the  on the storage node.

## Client
Install the package  on the client node, which will build the client Kernel module.

The client service needs to know where it can reach the management server.

The client service needs to know where it can mount the cluster storage, as well as the location of the client configuration file.

Load the Kernel module and its dependencies.

 # modprobe beegfs

Start/enable the  on the client node.

Start/enable the  on the client node.

## Utilities
Install the package .

## Check connectivity
Check the detected network interfaces and transport protocols from a client node with the following commands:

 # beegfs-ctl --listnodes --nodetype=mgmt --nicdetails
   node01 1
     Ports: UDP: 8008; TCP: 8008
     Interfaces:
     + enp0s31f6addr: 192.168.0.1; type: TCP

 # beegfs-ctl --listnodes --nodetype=meta --nicdetails
   node02 2
     Ports: UDP: 8005; TCP: 8005
     Interfaces:
     + eno1addr: 192.168.0.2; type: TCP

 # beegfs-ctl --listnodes --nodetype=storage --nicdetails
   node03 3
     Ports: UDP: 8003; TCP: 8003
     Interfaces:
     + eno1addr: 192.168.0.3; type: TCP

 # beegfs-ctl --listnodes --nodetype=client --nicdetails
   4E451-5DAEDCBF-node04 4
     Ports: UDP: 8004; TCP: 0
     Interfaces:
     + wlo1addr: 192.168.0.4; type: TCP

## Server tuning and advanced features
## InfiniBand Support
* Explicitly Install , which will provide  shared object libraries.
* Enable support for RDMA-capable network hardware.
* Rebuild the client kernel module.

## ACLs
## Storage Pools
## Quota Enforcement
## High Availability
