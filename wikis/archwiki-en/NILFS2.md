# NILFS2

NILFS2 (New Implementation of a Log-structured File System) is a log-structured file system supporting versioning of the entire file system and continuous snapshotting, which allows users to even restore files mistakenly overwritten or destroyed just a few seconds ago.

It was developed by Nippon Telegraph and Telephone Corporation (NTT) CyberSpace Laboratories and a community from all over the world. NILFS was released under the terms of the GNU General Public License (GPL).

NILFS2 is continously snapshoted, as such it can be considered versioning file system where file system automatically keeps past versions of every file.

## Creating a NILFS2 file system
This article assumes the device has partitions already setup.  Install .  Use  to format the target partition referred to as :

 # mkfs.nilfs2 -L mylabel /dev/sdxY

See  for all available options.

## Changing label
Nilfs-tune command should be used only for unmounted file systems.

 # nilfs-tune -L newlabel /dev/sdxY

## Mounting
The file system can then be mounted manually or via other mechanisms:

 # mount /dev/sdxY /mnt/foo

## Mount options
## Error handling
 /  /
Specifies what NILFS2 should do on file system error. Continue Ignores error, remount-ro remounts file system read-only and panic halts the system.

## Discard
 /
Enable/disable TRIM

See  for all available options.

## Snapshots
NILFS2 has two types of snapshots, checkpoints and snapshots. They are often written as  and  respectively.

NILFS2 creates checkpoints on every write automatically. Checkpoint is snapshot that can be automatically deleted by NILFS2 garbage collector to free up space when file system is filled up or when user manually prompts it for cleaning.

Snapshots have to be manually converted from checkpoints and are never deleted automatically. They can be mounted to recover data from them.

## Listing snapshots
Checkpoints and snapshots can be listed with:

To list only snapshots(ss) use  flag with lscp. See  for all available options.

## Converting checkpoints to snapshots
In order to recover data from checkpoint it first has to be converted into snapshot. To do that use  utility:

 # chcp ss /dev/sdxY checkpoint-number

 is number of the checkpoint listed in  in the CNO column.

 will now show line like:
     4  2025-04-14 22:28:56   ss    -     10181423     554012
#

To convert snapshot back to checkpoint use:

 # chcp cp /dev/sdxY checkpoint-number

## Creating snapshots
Use following to create a checkpoint:

 # mkcp /dev/sdxY

Or to create a snapshot directly:

 # mkcp --snapshot /dev/sdxY

## Mounting snapshots
Following command will mount snapshot  read-only into :
 # mount -t nilfs2 -r -o cp=checkpoint-number /dev/sdxY /mnt/snapshot

## Deleting snapshots
To delete a singular checkpoint use:
 # rmcp /dev/sdxY checkpoint-number

To delete a range of checkpoints you can use:
 # rmcp /dev/sdxY start..end
Where start is number of starting checkpoint and end the number of ending checkpoint.

To delete all checkpoints older than a checkpoint use:
 # rmcp /dev/sdxY ..checkpoint-number

To delete all checkpoints newer than a checkpoint use:
 # rmcp /dev/sdxY checkpoint-number..

See  for further details.

## Cleaning file system
To clear obsolete checkpoints from a mounted NILFS2 file system run:
 # nilfs-clean /dev/sdxY

See  and  for further details on garbage collector.

## Resizing file system
 tool resizes online NILFS2 file system.

Mounted NILFS2 filesystem can be resized with following command:

 # nilfs-resize /dev/sdxY desired-size

Where  can be suffixed by unit letter , , , , or , for 512 byte sectors, kilobytes, megabytes, gigabytes, or terabytes, respectively. If  is not specified, it will default to the size of partition.

 does not change size of paritions themselves, they either have to be shrink afterwards when shrinking the filesystem or grown beforehand when enlarging it. This can be done with fdisk for example.

See  for further details.
