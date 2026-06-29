# Disk cloning

Disk cloning is the process of making an image of a partition or of an entire hard drive. This can be useful for copying the drive to other computers or for backup and recovery purposes.

## Block-level cloning
## Using dd
See dd#Disk cloning and restore and Core utilities#dd alternatives.

## Using ddrescue
If possible, data recovery from disks should be performed using their native interface: SATA or, for older drives, IDE. Results may vary while using USB adapters.

GNU  is a data recovery tool capable of ignoring read errors. ddrescue is not related to dd in any way except that both can be used for copying data from one device to another. The key difference is that ddrescue uses a sophisticated algorithm to copy data from failing drives causing them as little additional damage as possible. See the ddrescue manual for details.

## First round
To clone a faulty or dying drive, run ddrescue twice. For the first round, copy every block without read error and map the errors to .

 # ddrescue --force --no-scrape /dev/sdX /dev/sdY rescue.map

; : This option is used when writing directly to a device (like a disk or partition). Without this flag, ddrescue will refuse to overwrite an existing device to avoid accidental data loss. Using  allows you to bypass this safety check, so be cautious when using it.
; : This option tells ddrescue to skip the "retrying" phase and focus on copying the easily readable data first (the first pass). It avoids retrying failed sectors, which is useful when you want to quickly recover as much data as possible without getting stuck on bad areas.
; : This represents the source device you want to recover data from. Replace  with the actual device name (e.g., ). where  is the partition letter of the source and  of the target block device.
; : This is the destination device or file where the recovered data will be written. In this case, it's another device (e.g., ). Be very careful when specifying this, as the command will overwrite this device. Alternatively, you can create image, just typing path/to/file/image.img
; : This is the log file used by ddrescue to track recovery progress. The log file is critical because it records which sectors have been successfully recovered and which need further attention. If the recovery process is interrupted, you can resume it later using this log file without starting from scratch.

This command copies data from one device () to another device () while prioritizing speed (by skipping retry attempts).

* The  option is needed because you are writing directly to a device ().
* The  file keeps track of progress, allowing you to resume the recovery if it stops.

## Second round
For the second round, copy only the bad blocks and try 3 times to read from the source before giving up.

 # ddrescue --force --idirect --retry-passes=3 --no-scrape /dev/sdX /dev/sdY rescue.map

; : Direct disk access, which can bypass some issues. If mapfile positions and sizes are multiples of the sector size, the kernel may be caching disk accesses. To bypass this and recover more data, consider using direct disc access or reading from a raw device, ensuring the correct sector size is set with . Direct disc access can copy arbitrary domains by reading entire sectors and writing only the necessary parts. Start by trying the  option, or use raw devices if direct access is unavailable. Depending on your OS and hardware, direct access may be slower or faster than normal cached reading.
; : Retry bad sectors up to 3 times.

This command attempts to read problematic sectors more aggressively.

if you encounter issue like this:

 ddrescue: /dev/sdX: Unaligned read error. Is sector size correct?

check sector size of the device:

 # blockdev --getss /dev/sdX

This will display the sector size in bytes. For example, most CD/DVD drives, the correct sector size is 2048 bytes. and specify sector size manually:

 # ddrescue --sector-size=2048 --force --idirect --retry-passes=3 --no-scrape /dev/sdX /dev/sdY rescue.map

## Third round (optional)
 # ddrescue --force --idirect --retry-passes=3 --reverse /dev/sdX /dev/sdY rescue.map

 reads the drive in reverse, which can sometimes bypass issues that prevent forward reads.

## Fourth round
For the fourth round, use scraping mode for fine-grained recovery:

 # ddrescue --force --idirect --retry-passes=3 /dev/sdX /dev/sdY rescue.map

 will scrape over the problematic sectors multiple times. It tries to rescue data from the most damaged sectors.

When to stop: If the drive continues to have read speeds near 0 B/s with no further improvement, the likelihood of recovering more data diminishes. In such cases, professional data recovery services might be the best option. Ultimately, if the process continues to stall without rescuing more data, the drive might be physically failing, and further attempts may yield minimal results..

In some circumstances the disk controller or a USB adapter may lock, while attempting to read a particular sector. The  option may be used to instruct ddrescue to start reading after that position.

Now you can check the file system for corruption and mount the new drive.

 # fsck -f /dev/sdY
## Fifth round (optional)
Once the copy is complete, run a final pass in read-only mode to verify integrity of the rescued image:

 # ddrescue --force --verify /dev/sdX /dev/sdY rescue.map

or mounting the image, if it's CD/DVD/BD:

 # mount -o loop cd_rescue.iso /mnt/test

Or run a checksum if you have a reference file.

## File system cloning
## Using e2image
e2image is a tool included in  for debugging purposes. It can be used to copy ext2, ext3, and ext4 partitions efficiently by only copying the used blocks. Note that this only works for ext2, ext3, and ext4 filesystems, and the unused blocks are not copied so this may not be a useful tool if one is hoping to recover deleted files.

To clone a partition from physical disk , partition 1, to physical disk , partition 1 with e2image, run

 # e2image -ra -p /dev/sda1 /dev/sdb1

## Using xfs_copy
 from  can be used to copy an XFS file system to one or more block devices in parallel.

For example, to clone the file system on  to , run:

 # xfs_copy /dev/sda1 /dev/sdb1

## Versatile cloning solutions
These applications allow easy backup of entire file systems and recovery in case of failure, usually in the form of a Live CD or USB drive. They contain complete system images from one or more specific points in time and are frequently used to record known good configurations. See Wikipedia:Comparison of disk cloning software for their comparison.

See also Synchronization and backup programs for other applications that can take full system snapshots, among other functionality.

*
*
*
*
*
