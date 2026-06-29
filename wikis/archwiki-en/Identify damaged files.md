# Identify damaged files

This article gives details on how to find out which file owns a given disk sector. The main purpose for doing so is finding out which file was damaged in the event a storage device develops any bad sectors (that way you will know if you lost anything important).

For most of these commands you will have to be either root or a user that has direct read access to the drive you are checking (being a member of the disk group should be enough). As usual, a current backup is always a good idea, especially if imminent drive failure is suspected. S.M.A.R.T. can help determining that.

## Filesystems
## btrfs
Unlike other filesystem types, btrfs has native support for reporting on damaged files. When scrubbing a partition, btrfs reads all data and metadata blocks and verifies checksums. It automatically repairs corrupted blocks if there is a correct copy available in a RAID configuration. btrfs also reports any unreadable sector along with the affected file via system log.

## Find damaged files
First of all, scrub the damaged partition:

 # btrfs scrub start -Bd /dev/sdxy

The same partition can be scrubbed when mounted by providing its mount point:

 # btrfs scrub start -Bd /mnt/point

Scrub reports can be retrieved as many times as need with the  subcommand:

When done, search the kernel log for I/O errors:

The output above reveals that sector  could not be read and it contains data for file . The sector number can be directly used with hdparm when reallocating (see #Force the disk to reallocate bad block).

## Ext2, ext3, and ext4
## Debug the filesystem
The tune2fs command will give you access to all the low level structures within any ext2/ext3/ext4 filesystem.

The first thing we want to do is get the block size from the filesystem in question. Just run:

In this case 4096 is the block size being used (it appears to be the default).

If you did not run badblocks using the block size that your filesystem is using then you will need to convert your block number(s) to match it (remember to use the block number(s) relative to the partition they are on).

i.e. block number 100 with a block size of 1024 bytes becomes block number 25 at 4096 bytes. The formula is:

 (original block number) / ((filesystem block size) / (badblocks block size))

Now the entire point of running this program (for the purpose of this article) is to get the inode number. Before continuing to debug it, unmount the partition. Then, run the command:

 # debugfs

Then in the  console, use the  command on the ext partition containing the bad sector:

 debugfs:  open /dev/sdxy

Finally, use the  command to get information about the block in question (in this example block 1000):

 debugfs:  testb blocknumber

If the block is in use then run this command to get the inode number

 icheck blocknumber

This will return two numbers. The block number and the inode number.

## Find damaged files
Use the inode number (second number from the  command) with the  command:

 ncheck inodenumber

The  console will give you the full pathname to the file using the bad block. Now you will know what was actually damaged.

If the inode number is very small and  fails to return a path then it is probably the journal itself that is damaged. To delete the journal simply run this command on the partition:

 # tune2fs -O ^has_journal /dev/sdxy

Run the  command again from the  console on the bad block and it should be no longer marked as used if it was indeed used by the journal. To build a new journal run:

 # tune2fs -j /dev/sdxy

## JFS
## Debug the filesystem
The jfs_debugfs command will give you access to all the low level structures within any JFS filesystem. Other filesystems such as the ext3 and ext4 filesystems have similar tools. It is probably a good idea to umount any filesystem before you run this on them. To use it just run:

 # jfs_debugfs /dev/sdxy

This puts you into a command console. The first thing you should note is your aggregate block size. This is (presumably) the block size the filesystem is using. JFS seems to default to 4096 bytes.

If you did not run badblocks using the block size that your filesystem is using then you will need to convert your block number(s) to match it (remember to use the block number(s) relative to the partition they are on).

i.e. block number 100 with a block size of 1024 bytes becomes block number 25 at 4096 bytes. The formula is:

 (original block number) / ((filesystem block size) / (badblocks block size))

Now the entire point of running this program (for the purpose of this article) is to get the inode number. To do this run the command:

 d blocknumber 0 i

The syntax is the  command for display, the block number, the offset (just set it to 0), and the display format  for inode.

The decimal number that  is set to is the one we want. From here you type  to exit out of the display mode. Repeat the display command for each bad block that you have and note all of their inode numbers. For more info on the inode such as permissions and filetype type:

 i inodenumber

When you have all the inode numbers type  to quit.

## Find damaged files
Finally to find the damaged file you can simply use the gnu find utility. Mount your filesystem and run:

 # find / -inum inodenumber

Substitute  for the mountpoint of the filesystem that the inode belongs to. If you search root and have more than one filesystem mounted you can find multiple files with the same inode number on different filesystems, plus find will take significantly longer. Remember, an inode is only unique to the filesystem that it is in.

## XFS
## Debug the filesystem
The xfs_info command will give you basic information about an XFS formatted partition and the xfs_db command will give you access to all the low level structures within any XFS filesystem.

The first thing we want to do is get the block size from the filesystem in question. Just run:

In this case 4096 is the block size being used (it appears to be the default).

If you did not run badblocks using the block size that your filesystem is using then you will need to convert your block number(s) to match it (remember to use the block number(s) relative to the partition they are on).

i.e. block number 100 with a block size of 1024 bytes becomes block number 25 at 4096 bytes. The formula is:

 (original block number) / ((filesystem block size) / (badblocks block size))

Now the entire point of running this program (for the purpose of this article) is to get the inode number. Before continuing to debug it, unmount the partition. Then, run the command:

 # xfs_db -c 'blockget -b blocknumber' /dev/sdxy

You should get output similar to this:

    setting block 0/9 to data
    setting inode to 131 for block 0/9
    inode 131 block 9 at offset 0

In this example we now know the inode is 131 and can proceed to the next section

If instead you do not get an inode number in your output but do see the word free then likely this means that the bad block belongs to free space and nothing important was damaged.

## Find damaged files
Finally to find the damaged file you can simply use the gnu find utility. Mount your filesystem and run:

 # find / -inum inodenumber

Substitute  for the mountpoint of the filesystem that the inode belongs to. If you search root and have more than one filesystem mounted you can find multiple files with the same inode number on different filesystems, plus find will take significantly longer. Remember, an inode is only unique to the filesystem that it is in.

## Force the disk to reallocate bad block
First you will want to see how many badblocks the harddrive is aware of through the smartctl command:

 # smartctl -t long /dev/sdx

Wait until test completes, then:

To make the harddrive transparently map out the badblock with a spare good sector you will have to simply write zeros to the bad block using the dd command as root. Remember that with this command you have to work with the same block size as your filesystem and the block has to be relative to the partition the filesystem is on and not the harddrive as a whole:

Alternatively, hdparm provides a couple of nice and simple options to read and write a given sector (4621327, in the following example):

You can see if the harddrive did indeed map out an additional bad sector by checking with the smartctl command and seeing if the reallocated sector or event count went up:

To get  to go back to 0 you need to run a SMART long test and a selftest:

 # smartctl -t long /dev/sdx

Wait until test completes, then:

 # smartctl -l selftest /dev/sdx
