# Slurm

Slurm (also referred as Slurm Workload Manager or slurm-llnl) is an open-source workload manager designed for Linux clusters of all sizes, used by many of the world's supercomputers and computer clusters. It provides three key functions. First it allocates exclusive and/or non-exclusive access to resources (computer nodes) to users for some duration of time so they can perform work. Second, it provides a framework for starting, executing, and monitoring work (typically a parallel job) on a set of allocated nodes. Finally, it arbitrates contention for resources by managing a queue of pending work.

## Installation
Install the  package. It pulls in  (an authentication service, as a dependency. It is started as a requirement through slurmd's systemd service and encrypts the connection between the various hosts. Therefore make sure that all nodes in your cluster have the same key in . Then start and enable .

The package itself has many more optional dependencies, though Slurm has to be recompiled to make use of them, after they have been installed.

## Configuration
The configuration files for slurm-llnl reside under . Prior to starting any slurm-services, it has to be configured properly by creating a configuration file at . Client and server may use the same configuration file, which can either be generated at [https://slurm.schedmd.com/configurator.html the official website or by copying  to  and adapting it to ones liking.

By default the Slurm user, which was introduced to your system in the installation process, has  as UID and GID, this simplifies the setup on multiple systems. UID and GID matches the one used in Debian, therefore they may be used side-by-side, but remember that binaries are not in the same directories on each and every distribution.

## Client (compute node) configuration
On the client-side one may now safely start/enable .

## Server (head node) configuration
Start/enable .

Additionally you may want to start/enable , which handles a SQL database for easier management thereby logging somewhat essential process information.

## Troubleshooting
## Services fail to start on boot
If  or  fail to start at boot but work fine when manually started, then the service may be trying to start before a network connection has been established. To verify this, add the lines associated with the failing service from below to the  file:

Then, check the associated log file. If you notice the fatal exception mentions , then you may want to extend the unit so that it waits for a valid network connection via network-online.target.

## Running RHEL based nodes side-by-side
On RedHat based distributions, slurm is running as root by default. To add these nodes to the cluster, first create  user with  and  equal  to match the one used in Arch Linux, then change slurm user with command .
