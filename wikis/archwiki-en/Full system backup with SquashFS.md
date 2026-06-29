# Full system backup with SquashFS

Compressed backup archives of whole filesystems can be made in the SquashFS format. Backup and retrieval takes relatively less time with its random access capability, but any kind of modification other than appending is not yet possible.

{| class="wikitable"
|-
! Device File
! Description
|-
| /dev/sdB
| Backup Drive
|-
| /dev/sdL
| Live Medium
|-
| /dev/sdSRC
| Drive to Be Backed Up
|}

## Pros and cons
Pros:

* No partitioning, no guessing how much size is required
* Should be supported by most rescue disks running at least Linux 2.6.29 (released in 2009)
* Random accessneeded, with a plain
* Duplicate files are removed by default (unless  flag is on)

Cons:

* Access Control Lists are not yet supported, and therefore not backed up
* Not accessible from Windows1
* Appendable but impossible to remove things from it
* To use the disk for some other purposes, you have to destroy the backup2

## Prepare the backup drive
# Wipe out all partitions , then the partition table , with wipefs.
# Synchronize all write caches
# Inform the OS of partition table changes
# Check for bad blocks:
#* If the backup drive is an SSD, use S.M.A.R.T..
#* If the backup drive is an HDD, use badblocks.

## Prepare a live medium
Installation guide#Prepare an installation medium or archiso to /dev/sdL

## Back up
Installation guide#Boot the live environment

Mount filesystems you would like to backup. (e.g. /dev/sdSRC to /mnt)

Back up (example script)

; -not-reproducible: Slightly increase backup speed
; -noappend: Overwrite
; -mem: RAM granted to mksquashfs
; -e: List of exclude dirs/files

## (Optional) Test backup in QEMU
Grant permission

 $ sudo chown $USER:$USER /dev/sdB

Launch QEMU

## (Optional) Inspect backup
Get backup date

 # date --date=@"$(unsquashfs -mkfs-time /dev/sdB)"

More superblock information

 # unsquashfs -stat /dev/sdB

Checksum

## Retrieve file from backup
 # mount /dev/sdB /mnt
 # cp /mnt/path/to/file /path/to/destination

## Restore backup
