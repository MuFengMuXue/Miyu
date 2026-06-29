# Apache Cassandra

Apache Cassandra is a NoSQL multi-master database with linear scalability and no single point of failure.

## Installation
Install the  package.

## Configuration
## systemd unit
## Logging to journald
The package logs to  by default. To instead log to journald you will need to edit the unit and set the service to run in the foreground by adding  to the  line, and set Type to  as the process will no longer fork.

This can be also done using a systemd drop-in file:

If Cassandra was running, you will need to drain, and then restart Cassandra.

 $ nodetool drain

## cassandra.yaml
There is copious amounts of documentation in the default . When installed via the  package, it is located in

## Basic configuration items to change
Setting the name of the cluster. This needs to be consistent for all nodes that you intend to have in this cluster.

 cluster_name: 'Test Cluster'

Set the directory where cassandra will write too, below is the default that will be used if unset. If possible set this to a disk used only for storing cassandra data

 data_file_directories:
     - /var/lib/cassandra/data

For the first node (the seed node) make sure to include its IP address in the seeds, and atleast 1 other node. for all other nodes, try and set a broad range of nodes in the cluster. If a node cannot connect to one of the seeds listed in this configuration at startup - it will fail to start.

 seed_provider:
     - class_name: org.apache.cassandra.locator.SimpleSeedProvider
       parameters:
           - seeds: "192.168.1.53, 192.168.1.52"

set this based on what type of disk cassandra is using to store data on  or

 disk_optimization_strategy: ssd|spinning

This is the address Cassandra will listen for client connections on

 listen_address: 192.168.1.51

This is the address this node will advertise itself as, ensure both your clients and nodes can reach this node on this address

 broadcast_address: 192.168.1.51

This is the address used for thrift connections, set to  it will listen on all interfaces, which is fine as long as its firewalled for security

 rpc_address: 0.0.0.0

## Troubleshooting
If Cassandra fails to run as a service, try running Cassandra

 $ cassandra

If you receive the following error:

 Improperly specified VM option 'ThreadPriorityPolicy=42'
 Error: Could not create the Java Virtual Machine.
 Error: A fatal exception has occurred. Program will exit.

Cassandra runs on Java 8 and starting with Cassandra 4.0.2, also on Java 11.  You will need to install the proper Java and override the default JVM with a systemd drop-in file:

If this file already exists, simply add the Environment line into the Service block.
