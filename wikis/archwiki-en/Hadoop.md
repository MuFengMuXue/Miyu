# Hadoop

Apache Hadoop is a framework for running applications on large cluster built of commodity hardware. The Hadoop framework transparently provides applications both reliability and data motion. Hadoop implements a computational paradigm named Map/Reduce, where the application is divided into many small fragments of work, each of which may be executed or re-executed on any node in the cluster. In addition, it provides a distributed file system (HDFS) that stores data on the compute nodes, providing very high aggregate bandwidth across the cluster. Both MapReduce and the Hadoop Distributed File System are designed so that node failures are automatically handled by the framework.

## Installation
Install the  package.

## Configuration
By default, hadoop is already configured for pseudo-distributed operation. Some environment variables are set in  with different values than traditional hadoop.

{| class="wikitable"
|-
! Environment variable
! Value
! Description
! Permission
|-
| HADOOP_CONF_DIR
|
| Where configuration files are stored.
| Read
|-
| HADOOP_LOG_DIR
|
| Where log files are stored.
| Read and Write
|-
| HADOOP_WORKERS
|
| File naming remote worker hosts.
| Read
|-
| HADOOP_PID_DIR
|
| Where pid files are stored.
| Read and Write
|}

You also should set up the following files correctly.

 /etc/hosts
 /etc/hostname
 /etc/locale.conf

You need to tell hadoop your JAVA_HOME in  because it does not assume the location where it is installed to in Arch Linux by itself:

Check the installation with:

 $ hadoop version

The HADOOP_WORKERS option was previously called HADOOP_SLAVES. If you get warning message "WARNING: HADOOP_SLAVES has been replaced by HADOOP_WORKERS. Using value of HADOOP_SLAVES." Then replace  in  with:

 export HADOOP_WORKERS=/etc/hadoop/workers

## Single Node Setup
## Standalone Operation
By default, Hadoop is configured to run in a non-distributed mode, as a single Java process. This is useful for debugging.

The following example copies the unpacked conf directory to use as input and then finds and displays every match of the given regular expression. Output is written to the given output directory.

 $ HADOOP_CONF_DIR=/usr/lib/hadoop/orig_etc/hadoop/
 $ mkdir input
 $ cp /etc/hadoop/*.xml input
 $ hadoop jar /usr/lib/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.0.0.jar grep input output 'dfs$ cat output/*

## Pseudo-Distributed Operation
Hadoop can also be run on a single-node in a pseudo-distributed mode where each Hadoop daemon runs in a separate Java process.

By default, Hadoop will run as the user root. You can change the user in :

 HADOOP_USERNAME=""

## Set up passphraseless ssh
Make sure you have sshd enabled. Now check that you can connect to localhost without a passphrase:

 $ ssh localhost

If you cannot ssh to localhost without a passphrase, execute the following commands:

 $ ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa
 $ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
 $ chmod 0600 ~/.ssh/authorized_keys

Also make sure this line is commented in

## Execution
Format a new distributed-filesystem:
 $ hadoop namenode -format

Edit  and add below configuration:

      fs.defaultFS
      hdfs://localhost:9000

Start the hadoop namenode:
 $ hadoop namenode

You may access the web GUI via http://localhost:9870/

Start the following hadoop systemd units: , , , , .

The hadoop daemon log output is written to the {{ic|${HADOOP_LOG_DIR}}} directory (defaults to ).

Browse the web interface for the NameNode and the JobTracker; by default they are available at:

* NameNode - http://localhost:50070/
* JobTracker - http://localhost:50030/

Copy the input files into the distributed filesystem:
 $ hadoop fs -put /etc/hadoop input

Run some of the examples provided:
 $ hadoop jar /usr/lib/hadoop-2.7.3/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar grep input output 'dfs[a-z.+'

Examine the output files:

Copy the output files from the distributed filesystem to the local filesystem and examine them:
 $ hadoop fs -get output output
 $ cat output/*

or

View the output files on the distributed filesystem:
 $ hadoop fs -cat output/*

When you are done, stop the daemons , , , , .
