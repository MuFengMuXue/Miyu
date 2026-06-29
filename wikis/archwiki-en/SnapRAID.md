# SnapRAID

SnapRAID is a folder-based backup tool that behaves like a software or hardware RAID5/6 disk raid, but is not a disk raid itself. There is no realtime recovery, free space between disks cannot be combined and manual execution of backup is needed.

Because of the nature of folder-based backup, SnapRAID is more flexible and simpler than software raids. Although disk raids have advantages such as realtime backup, increased complexity or reduced performance are the drawback. Not to mention a two-disk failure or a SATA URE (Unrecoverable Read Error) happening to RAID5 could damage all data, which is not the case with SnapRAID. Thus the use of SnapRAID is logical when backup is the main goal rather than preventing a system from going offline due to disk failure.

SnapRAID works by storing parity of all folders to another disk. The destination disk which the parity file is stored on should be the largest. Other disks do not have this restriction and can be of any size. Summing up, SnapRAID is suitable for media centers where files are usually large and rarely changed. SnapRAID is highly flexible and can be configured to add/remove disk at any time. Also, more than one redundant disks are supported.

## Installation
Install the  package.

## Usage
See also Manual for SnapRAID

We have four disks with data on them, and want to save a redundant just in case. These four disks are mounted at:

*
*
*
*

And an empty redundant disk mounted at:

*

Let us create a configuration file! Lines beginning with "content" designate the path to a content file that stores SnapRAID metadata.

## Backup
To begin the backup process, run:

 # snapraid sync

## Undeletion
To revert a file or folder to an earlier version (undelete):

 # snapraid fix -f FILENAME
( using complete PATH of file or dir is better. file path is relative to all root dir )

## Disk recovery
If the disk is mounted at  is dead and being replaced, edit  before doing a recovery.

Change the line

 data d1 /mnt/sda

to

 data d1 /mnt/sda_new

To begin recovery

 # snapraid -d d1 -l recovery.log fix
