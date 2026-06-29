# Fstab

The  file can be used to define how disk partitions, various other block devices, or remote file systems should be mounted into the file system.

Each file system is described in a separate line. These definitions will be converted into systemd mount units dynamically at boot, and when the configuration of the system manager is reloaded. The default setup will automatically fsck and mount file systems before starting services that need them to be mounted. For example, systemd automatically makes sure that remote file system mounts like NFS or Samba are only started after the network has been set up. Therefore, local and remote file system mounts specified in  should work out-of-the-box. See  for details.

The  command will use fstab, if just one of either directory or device is given, to fill in the value for the other parameter. When doing so, mount options which are listed in fstab will also be used.

## Usage
A simple , using file system UUIDs:

*  describes the block special device or remote file system to be mounted; see #Identifying file systems.
*  is the directory where the file system will be mounted to, a.k.a. the mountpoint. The directory must be created beforehand.
*  is the file system type.
*  are the file system mount options; see  and .
*  is checked by the  utility. This field is usually set to , which disables the check.
*  sets the order for file system checks at boot time; see . For the root device it should be . For other partitions it should be , or  to disable checking.

All specified devices within  will be automatically mounted on startup and when the  flag is used with  unless the  option is specified. Devices that are listed and not present will result in an error unless the  option is used.

See  for details.

## Identifying file systems
There are different ways to identify file systems that will be mounted in : kernel name descriptor, file system label and UUID, and GPT partition label and UUID for GPT disks. Kernel name descriptors should not be used, while UUIDs or PARTUUIDs should be preferred over labels. See Persistent block device naming for more explanations. It is recommended to read that article first before continuing with this article.

In this section, we will describe how to mount file systems using all the mount methods available via examples. The output of the commands  and  used in the following examples are available in the article Persistent block device naming.

## Kernel name descriptors
Run  to list the partitions and prefix the values in the NAME column with .

## File system labels
Run  to list the partitions, and prefix the values in the LABEL column with  or alternatively run  and use the LABEL values without the quotes:

## File system UUIDs
Run  to list the partitions, and prefix the values in the UUID column with  or alternatively run  and use the UUID values without the quotes:

## GPT partition labels
Run  to list the partitions, and use the PARTLABEL values without the quotes:

## GPT partition UUIDs
Run  to list the partitions, and use the PARTUUID values without the quotes:

## Tips and tricks
## Automount with systemd
See  for all systemd mount options.

## Local partition
In case of a large partition, it may be more efficient to allow services that do not depend on it to start while it is checked by fsck. This can be achieved by adding the following options to the  entry of the partition:

 x-systemd.automount

This will fsck and mount the partition only when it is first accessed, and the kernel will buffer all file access to it until it is ready.
This method can be relevant if one has, for example, a significantly large  partition.

## Remote file system
The same applies to remote file system mounts. If you want them to be mounted only upon access, you will need to use the  parameters. In addition, you can use the  option to specify how long systemd should wait for the mount command to finish. Also, the  option ensures systemd understands that the mount is network dependent and order it after the network is online.

 x-systemd.automount,x-systemd.mount-timeout=30,_netdev

Instruct systemd to reload  and create the  unit by doing a daemon-reload then restarting the .

## Encrypted file system
If you have secondary encrypted file systems with keyfiles, you can also add the  parameter to the corresponding entries in  and . systemd will not wait for the cryptsetup service to finish unlocking and mounting the filesystem on boot, but instead may finish mounting this after reaching default.target. This will avoid any boot delay caused by unlocking secondary partitions that are not required immediately after boot. See dm-crypt/System configuration#Non blocking mounting for cryptsetup configuration

Since mount services will by default only wait for 90 seconds for the partition to be available, any delay in making the keyfile available may cause the mount to fail. To avoid this, add the option  to fstab in order to make sure that the mount service waits indefinitely for the partition to be unlocked.

## Automatic unmount
You may also specify an idle timeout for a mount with the  flag.  For example:

 x-systemd.automount,x-systemd.idle-timeout=1min

This will make systemd unmount the mount after it has been idle for 1 minute.

## External devices
External devices that are to be mounted when present but ignored if absent may require the  option. This prevents errors being reported at boot. For example:

The  option is best combined with the  option. This is because the default device timeout is 90 seconds, so a disconnected external device with only  will make your boot take 90 seconds longer, unless you reconfigure the timeout as shown. Make sure not to set the timeout to 0, as this translates to infinite timeout.

## Filepath spaces
Since spaces are used in  to delimit fields, if any field (PARTLABEL, LABEL or the mount point) contains spaces, these spaces must be replaced by escape characters  followed by the 3 digit octal code :

## atime options
Below atime options can impact drive performance.

* The  option updates the access time of the files every time they are accessed. This is more purposeful when Linux is used for servers; it does not have much value for desktop use. The drawback about the  option is that even reading a file from the page cache (reading from memory instead of the drive) will still result in a write.
* The  option fully disables writing file access times to the drive every time you read a file. This works well for almost all applications, except for those that need to know if a file has been read since the last time it was modified. The write time information to a file will continue to be updated anytime the file is written to with this option enabled.
* The  option disables the writing of file access times only for directories while other files still get access times written.
*  updates the access time only if the previous access time was earlier than the current modify or change time. In addition, since Linux 2.6.30, the access time is always updated if the previous access time was more than 24 hours old. This option is used when the  option,  option (which means to use the kernel default, which is ; see  and Once upon atime) or no options at all are specified.

When using Mutt or other applications that need to know if a file has been read since the last time it was modified, the  option should not be used; using the  option is acceptable and still provides a performance improvement.

Since kernel 4.0 there is another related option:

*  reduces writes to disk by maintaining changes to inode timestamps (access, modification and creation times) only in memory. The on-disk timestamps are updated only when either (1) the file inode needs to be updated for some change unrelated to file timestamps, (2) a sync to disk occurs, (3) an undeleted inode is evicted from memory or (4) if more than 24 hours passed since the last time the in-memory copy was written to disk.
:

Note that the  option works in combination with the aforementioned  options, not as an alternative. That is  by default, but can be even  with the same or less cost of disk writes as the plain  option.

## Remounting the root partition
If for some reason the root partition has been improperly mounted read only, remount the root partition with read-write access with the following command:

 # mount -o remount,rw /

## GPT partition automounting
When using UEFI/GPT, it is possible to omit certain partitions from  by partitioning according to the Discoverable Partitions Specification and have  mount the partitions. See systemd#GPT partition automounting.

To specify custom mount options for these volumes, use a by-designator identifier as the device name:

## Bind mount
You can link directories with the  option:

See  for details.

## Automatically generate an fstab using genfstab
You can use the genfstab tool to create an fstab file. See genfstab for details.

## GUI utilities
Here is a list of programs that can be used to modify mount points. They might not have all the features possible for editing fstab, but have all of the most used ones and might make your workflow much easier:

*
*

## Modifying user permissions and ownership
If you want to allow any user to mount the drive, consider adding these mount options to add onto your fstab entries.

*  - Allow any user to mount and to unmount the filesystem, even when some other ordinary user mounted it. This option implies the options noexec, nosuid, and nodev (unless overridden by subsequent options, as in the option line users,exec,dev,suid). Simply add  to the mount options to enable this.
*  - Allow an ordinary user to mount the filesystem. Only allows the same user to unmount. This option implies the options noexec, nosuid, and nodev (unless overridden by subsequent options, as in the option line user,exec,dev,suid). Simply add  to the mount options to enable this.

For filesystems that do not have file permissions built in such as FAT and exFAT, you can explicitly set the user or group for the entire drive and its files. You can view the ID of a specific user in . The uid is the third number in the entry, and the group id is the fourth.

*  - Set the owner ID of the drive
*  - Set the group ID of the drive

For ext4, btrfs, and other filesystems that have permission abilities, other users might not be permitted to see the drive. Be sure to double check the permissions of  and modify them for what you need.

## Verify changes
Use  to check for syntax errors and invalid options in fstab.
