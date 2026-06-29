# MongoDB

MongoDB (from humongous) is a source-available document-oriented database system developed and supported by MongoDB Inc. (formerly 10gen). It is part of the NoSQL family of database systems. Instead of storing data in tables as is done in a "classical" relational database, MongoDB stores structured data as JSON-like documents with dynamic schemas (MongoDB calls the format BSON), making the integration of data in certain types of applications easier and faster.

## Installation
MongoDB has been removed from the official repositories due to its re-licensing issues Install one of the following for the latest version available:

*  - builds from source.
*  - prebuilt MongoDB binary extracted from [https://repo.mongodb.org/apt/ubuntu/ official MongoDB Ubuntu repository packages. Compilation options used are unknown.

Alternatively, there are older versions of MongoDB available:

* ,
* ,
*
*
*
*
*

## Tools
Other MongoDB tools can be found packaged as well:

*
*
*
*

## Usage
Start/Enable the  daemon.

To access the MongoDB shell $ mongosh

Or, if authentication is configured:

 $ mongosh -u userName

## Configuration
## File Format
MongoDB uses a YAML-based configuration file format. See https://docs.mongodb.com/manual/reference/configuration-options/ for available configuration options.

## Requiring Authentication
To create a MongoDB user account with administrator access [https://docs.mongodb.com/manual/tutorial/enable-authentication/:

{{hc|$ mongosh|
use admin
db.createUser(
  {
    user: "myUserAdmin",
    pwd: "abc123",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
)}}

Append the following to your .

Restart .

## NUMA
Running MongoDB with Non-Uniform Memory Access (NUMA) can significantly impact performance.  To see if your system uses NUMA:

 # dmesg | grep -i numa

Also,  will show warnings if NUMA is in use and MongoDB is not started through .  (The  shell will also show this, but only if you do not have authentication enabled.)

If your system uses NUMA, to improve performance, you should make MongoDB start through .

Edit  according to the package you installed.

If using , change it from:

 ExecStart=/usr/bin/mongod $OPTIONS

To:

 ExecStart=/usr/bin/numactl --interleave=all /usr/bin/mongod $OPTIONS

If using , change it from:

 ExecStart=/usr/bin/mongod --quiet --config /etc/mongodb.conf

To:

 ExecStart=/usr/bin/numactl --interleave=all /usr/bin/mongod --quiet --config /etc/mongodb.conf

Zone claim also needs to be disabled, but on arch,  defaults to .

Reenable and Restart  as needed.

## Clean Start and Stop
By default, systemd immediately kills anything after asking it to start or stop, if it has not finished doing so within 90 seconds.

 makes systemd wait as long as it takes for MongoDB to start, but  does not.  Both packages allow systemd to kill MongoDB after it is asked to stop, if it has not finished within 90 seconds.

Large MongoDB databases can take a considerable amount of time to cleanly shut down, especially if swap is being used.  (An active 450GB database on a top of the line NVMe with 64GB RAM and 16GB swap can take an hour to shut down.)

By default, MongoDB uses journaling. [https://docs.mongodb.com/manual/reference/configuration-options/#storage-options  With journaling, an unclean shutdown should not pose a risk of data loss.  But, if not shutdown cleanly, large MongoDB databases can take a considerable amount of time to start back up.  In this case, choosing whether to require a clean shutdown is a choice of a slower shutdown versus a slower startup. To prevent systemd from killing MongoDB after 90 seconds, edit .

To allow MongoDB to cleanly shutdown, append to the  section: (On large databases, this may substantially slow down your system shutdown time, but speeds up your next MongoDB start time)

 TimeoutStopSec=infinity

If MongoDB needs a long time to start back up, it can be very problematic for systemd to keep killing and restarting it every 90 seconds [https://jira.mongodb.org/browse/SERVER-38086, so  prevents this.  If using , to make systemd wait as long as it takes for MongoDB to start, append to the  section:

 TimeoutStartSec=infinity

## Troubleshooting
## MongoDB will not start
If MongoDB will not start, and you just upgraded to  4.0.6-2+, you probably have a custom .  When MongoDB was in the Official repositories, it used an Arch-specific configuration file that used the systemd service type of simple.  It now supplies upstream's systemd service and configuration files, which instead use a systemd service type of forking.  Pacman will automatically upgrade your systemd service file, but will only automatically upgrade your  if you never modified it.  In that case, systemd will be expecting  to fork, but its configuration file will tell it not to.  You need to: switch to the new configuration file installed at , and duplicate changes you made to the old one that you still need, considering the new one is now in the YAML format, and the old one is probably in the MongoDB 2.4 format; or modify your existing one to enable forking.  (To continue using the old 2.4 file format instead of YAML, adding  should be what is needed.)

Check that  is configured to use the correct database location.

Add  to the  line:

 ExecStart=/usr/bin/numactl --interleave=all mongod --quiet --config /etc/mongodb.conf --dbpath /var/lib/mongodb

Check that there is at least 3GB space available for its journal files, otherwise mongodb can fail to start (without issuing a message to the user):

 $ df -h /var/lib/mongodb/

Check if the  lock file is empty or not:

 # ls  -lisa /var/lib/mongodb

If it is, stop . Run a repair on the database, specifying the dbpath ( is the default  in Arch Linux):

 # mongod --dbpath /var/lib/mongodb/ --repair

Upon completion, the dbpath should contain the repaired data files and an empty  file.

After running the repair as root, the files will be owned by the root user, whilst Arch Linux runs it under a different user. You will need to use chown to change the ownership of the files back to the correct user. See following link for further details: Further reference

 # chown -R mongodb: /var/{log,lib}/mongodb/

## Switching to a different version / Clean install
After removing a version of MongoDB and installing a different version, MongoDB might not start. In that case, try removing and recreating these folders (note that these will delete your database):
 $ rm -r /var/{lib,log}/mongodb
 $ mkdir /var/{lib,log}/mongodb
 $ chown -R mongodb:mongodb /var/{log,lib}/mongodb/

## Some computer just cannot run MongoDB
Some computers simply will not run MongoDB because their CPU architecture does not have the instruction set needed to run it. For instance, MongoDB was able to be installed on a GPD MicroPC which has an Intel "Gemini Lake Refresh"/Goldmount Plus microarchitecture, but running the MongoDB Shell returned the following:

Furthermore,  reported a signal  meaning that an illegal instruction execution was attempted. In other words, the computer did not have the instruction set to run this program, at least not locally.

It was able to connect to MongoDB Atlas where the server is hosted remotely on a machine that can run MongoDB, no  required.

## Warning about Transparent Huge Pages (THP)
One may want to permanently disable this feature by using a tmpfile:

Use sysctl to disable THP at runtime:

 # echo never > /sys/kernel/mm/transparent_hugepage/enabled
 # echo never > /sys/kernel/mm/transparent_hugepage/defrag

## Warning about Soft rlimits too low
If you are using systemd service, then edit the unit file:

 # Other directives omitted
 # (file size)
 LimitFSIZE=infinity
 # (cpu time)
 LimitCPU=infinity
 # (virtual memory size)
 LimitAS=infinity
 # (locked-in-memory size)
 LimitMEMLOCK=infinity
 # (open files)
 LimitNOFILE=64000
 # (processes/threads)
 LimitNPROC=64000

See following link for further details: [https://docs.mongodb.com/manual/reference/ulimit/#review-and-set-resource-limits Further reference
