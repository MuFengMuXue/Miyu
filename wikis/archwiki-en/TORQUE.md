# TORQUE

TORQUE is a resource manager providing control over batch jobs and distributed compute nodes. Basically, one can setup a home or small office Linux cluster and queue jobs with this software. A cluster consists of one head node and many compute nodes. The head node runs the torque-server daemon and the compute nodes run the torque-client daemon. The head node also runs a scheduler daemon.

## Installation
Install the  package.

## Must haves
## /etc/hosts
Make sure that  on all of the boxes in the cluster contains the hostnames of every PC in the cluster. Example, cluster consists of 3 PCs, mars, phobos, and deimos.

 192.168.0.20   mars
 192.168.0.21   phobos
 192.168.0.22   deimos

## Firewall configuration (if installed)
Be sure to open TCP for all machines using TORQUE.

The pbs_server (server) and pbs_mom (client) by default use TCP and UDP ports 15001-15004.
pbs_mom (client) also uses UDP ports 1023 and below if privileged ports are configured (the default).

## NFS
Technically, one does not need to use NFS but doing so simplifies the whole process. An NFS share either on the server or another machine is highly recommended to simplify the process of sharing common build disk space.

## Configuration
## Server (head node) configuration
Follow these steps on the head node/scheduler.

Edit  to name the head node. It is recommended to match the hostname in  for simplicity's sake.

Create and configure the torque server:

Then start trqauthd by running

A minimal set of options are provided here. Adjust the first line substituting "mars" with the hostname entered in :

 qmgr -c "set server acl_hosts = mars"
 qmgr -c "set server scheduling=true"
 qmgr -c "create queue batch queue_type=execution"
 qmgr -c "set queue batch started=true"
 qmgr -c "set queue batch enabled=true"
 qmgr -c "set queue batch resources_default.nodes=1"
 qmgr -c "set queue batch resources_default.walltime=3600"
 qmgr -c "set server default_queue=batch"

It may be of interest to keep finished jobs in the queue for a period of time.

 qmgr -c "set server keep_completed = 86400"

Here, 86400 sec = 24 h after which point, the job will be auto removed from the queue. One can see the full log of jobs removed from the queue with the  switch on qstat:

 qstat -f

Verify the server configuration with this command:
 # qmgr -c 'p s'

Edit  adding all compute nodes. Again, it is recommended to match the hostname(s) of the machines on the LAN. The syntax is HOSTNAME np=x gpus=y properties

* HOSTNAME=the hostname of the machine
* np=number of processors
* gpus=number of gpus
* properties=comments

Only the hostname is required, all other fields are optional.

Example:

 mars np=4
 phobos np=2
 deimos np=2

Restart the server and the new options are sourced.

## Client (compute node) configuration
Follow these steps on each compute node in the cluster.

Edit  to contain some basic info identifying the server:

 $pbsserver      mars          # note: this is the hostname of the headnode
 $logevent       255           # bitmap of which events to log

## Restart the server
That should be it. Now restart the server so the settings can take effect.

## Starting the client(s)
In order to start the clients run the following on each of the clients, including the server if it is also a client:

## Verifying cluster status
To check the status of the cluster, issue the following:
 $ pbsnodes -a

Each node if up should indicate that it is ready to receive jobs echoing a state of free.  If a node is not working, it will report a state of down.

Example output:

## Queuing jobs
Queuing to the cluster is accomplished via the qsub command.

A trivial test is to simply run sleep:
 $ echo "sleep 30" | qsub

Check the status of the queue via the qstat command described below. At this point, the work will have a status of "Q" which means queued. To start it, run the scheduler:

 # pbs_sched

One can modify the torque-server  systemd daemon to activate pbs_sched at boot.

Another usage of qsub is to name a job and queue a script:

 $ qsub -N x264 /home/facade/bin/x264_HQ.sh

Another example can use a wrapper script to make and queue work en mass automatically.

## Checking job status
 is used to check work status.

Append the  switch to see which nodes are doing which jobs.
