# Open-iSCSI

This article describes how to access an iSCSI target with the Open-iSCSI initiator.

## Installation
Install the  package.

## Overview
The following diagram shows how the Components work together:

From the Open-iSCSI README:

Persistent configuration is implemented as a tree of files and directories, which are contained in two directories:

* Discovery directory  which has directories named after target addresses.
* Node directory  which has directories named after IQN (ISCSI Unique Name) of particular device.

## Configuration
## Start the Service
 is managed by a systemd Unit.

Start  or .

## ISCSI Qualified Name (IQN)
IQN is used for identifying every device.

Open-ISCSI stores its initiator IQN in the  file with a format

During installation the initial IQN will be generated. If you wish to generate new IQN the  utility can be used which prints out new IQN.

## Authentication
If the ISCSI target requires authentication by the initiator, the configuration file  may need to be updated.

The following parameters are used for authenticating a login session of an initiator to a target:

 node.session.auth.authmethod = CHAP
 node.session.auth.username = initiators_username
 node.session.auth.password = initiators_password

If your target has two-way authentication enabled then those lines also need to be edited:

 node.session.auth.username_in = targets_username
 node.session.auth.password_in = targets_password

If your target requires authentication to get the list of its nodes (most will not) then following lines should be edited:

 discovery.sendtargets.auth.authmethod = CHAP
 discovery.sendtargets.auth.username = initiators_username
 discovery.sendtargets.auth.password = initiators_password

If your target has two-way authentication enabled then those lines also need to be edited:

 discovery.sendtargets.auth.username_in = targets_username
 discovery.sendtargets.auth.password_in = targets_password

## Target discovery
Request the target its nodes.

 # iscsiadm --mode discovery --portal target_ip --type sendtargets

On success information about nodes and target will be saved on your initiator.

## Add target manually
 # iscsiadm -m node --target targetname --portal target_ip -o new

A possible scenario to use this is when server does not allow discovery.

## Delete obsolete targets
 # iscsiadm -m discovery -p target_ip -o delete

## Login to available targets
 # iscsiadm -m node -L all

or login to specific target

 # iscsiadm -m node --targetname=targetname --login

logout:

 # iscsiadm -m node -U all

## Info
For running session

 # iscsiadm -m session -P 3

The last line of the above command will show the name of the attached device e.g

 Attached scsi disk sdd State: running

For the known nodes

 # iscsiadm -m node

## Online resize of volumes
If the iscsi blockdevice contains a partitiontable, you will not be able to do an online resize. In this case you have to unmount the filesystem and alter the size of the affected partition.

# Rescan active nodes in current session
# If you use multipath, you also have to rescan multipath volume information.
# Finally resize the filesystem.

## Tips and tricks
## Check for attached iSCSI devices
You can also check where the attached iSCSI devices are located in the  tree with:

 $ ls -l /dev/disk/by-path/ip-*

## Login to targets on boot
To log in to a target during boot, enable  and make sure the nodes have  in their configuration ().

## Troubleshooting
## Client IQN
At the server (target) you might need to include the client IQN from  in the account configuration.

## Debugging the iSCSI daemon
To run the iSCSI daemon in debug mode (make sure you stopped  before)

 # iscsid -d 8 -c /etc/iscsi/iscsid.conf -i /etc/iscsi/initiatorname.iscsi -f
