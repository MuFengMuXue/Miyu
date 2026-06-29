# Glusterfs

Glusterfs is a scalable network filesystem.

## Installation
Install the package .

## Configuration
Glusterfs can be setup to run in many different configurations depending operating needs, including distributed and replicated.  For the example below, a two node replicated server is being created, with nodes gluster1 and gluster2 each have two disks, one containing the OS (), the other to be shared by glusterfs ().  Unless stated, all setup is carried on gluster1:

*Start/enable  on both servers.

*Connect the servers
  # gluster peer probe gluster2

*Partition and format the glusterfs drive on both servers
**The upstream advises creating a single partition and formatting this as XFS

*On both servers automount the drives by appending  to include the following line, where  is the appropriate device (e.g., ).

*On both servers mount the drives. Then create a brick:
  # mkdir -p /export/sdXY/brick

*Enable replication on primary server
  # gluster volume create gv0 replica 2 gluster1.mydomain.net:/export/sdb1/brick gluster2.mydomain.net:/export/sdb1/brick

*Ensure volume is created correctly
  # gluster volume info

*Start volume
  # gluster volume start gv0

*Mount the volume
  # mkdir -p /mnt/glusterClientMount
  # mount -t glusterfs gluster1:/gv0 /mnt/glusterClientMount

## Automount gluster volume on boot
To mount a gluster volume on boot, systemd needs to wait for both the network, and the  service to be started. You can specify the following fstab options to do this:
