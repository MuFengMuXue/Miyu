# NTFS-3G

NTFS-3G is an open source implementation of Microsoft NTFS that includes read and write support. NTFS-3G developers use the FUSE file system to facilitate development and to help with portability.

## Installation
Install the following packages:

*  — the FUSE driver to mount NTFS partitions.
*  — userspace utilities to perform actions like #Formatting.

## Manual mounting
Two options exist when manually mounting NTFS partitions. The traditional:

 # mount /dev/your_NTFS_partition /mount/point

The mount type  does not need to be explicitly specified in Arch. The mount command by default will use  which is symlinked to  after the ntfs-3g package is installed.

The second option is to call  directly:

 # ntfs-3g /dev/your_NTFS_partition /mount/point

See  for the available options.

## Formatting
 # mkfs.ntfs -Q -L diskLabel /dev/sdXY

## Configuring
Your NTFS partition(s) can be set up to mount automatically, or pre-configured to be able to mount in a certain way when you would like them to be mounted. This configuration can be done in the static filesystem configuration (fstab) or by the use of udev rules.

## Default settings
Using the default settings will mount the NTFS partition(s) at boot. With this method, if the parent folder that it is mounted upon has the proper user or group permissions (e.g. ), then that user or group will be able to read and write on that partition(s).

## Linux compatible permissions
Permissions on a Linux system are normally set to 755 for folders and 644 for files. It is recommended to keep these permissions in use for the NTFS partition as well if you use the partition on a regular basis. The following example assigns the above permissions to a normal user:

 # Mount internal Windows partition with linux compatible permissions, i.e. 755 for directories (dmask=022) and 644 for files (fmask=133)
 /dev/NTFS-partition  /mnt/windows  ntfs-3g uid=userid,gid=groupid,dmask=022,fmask=133 0 0

Alternatively, if the Windows permissions do matter to you, you can use the  command to map Windows users to Linux ones. ntfs-3g will handle the translation of these permissions.

## Allowing group/user
In  you can also specify other options like those who are allowed to access (read) the partition. For example, for you to allow people in the  group to have access:

 /dev/NTFS-partition  /mnt/windows  ntfs-3g   gid=groupid,umask=0022    0       0

By default, the above line will enable write support for root only. To enable user writing, you have to specify the user who should be granted write permissions. Use the  parameter together with your user id to enable user writing:

 /dev/NTFS-partition  /mnt/windows  ntfs-3g   uid=userid,gid=groupid,umask=0022    0       0

If you are running on a single user machine, you may like to own the file system yourself and grant all possible permissions:
 /dev/NTFS-partition  /mnt/windows  ntfs-3g   uid=userid,gid=groupid    0       0

## Basic NTFS-3G options
For most, the above settings should suffice. Here are a few other options that are general common options for various Linux filesystems. For a complete list, see .

;umask: umask is a built-in shell command which automatically sets file permissions on newly created files. For Arch Linux, the default umask for root and user is 0022. With 0022 new folders have the directory permissions of 755 and new files have permissions of 644. You can read more about umask permissions here.
;fmask and dmask: Like  but defining file and directory respectively individually.
;noauto: If  is set, NTFS entries in  do not get mounted automatically at boot.
;uid: The user id. This allows a specific user to have full access to the partition. Your uid can be found with the  command.

The following option is specific to ntfs-3g only:

;windows_names: prevents files, directories and extended attributes to be created with a name not allowed by windows.

## Allowing user to mount
By default, ntfs-3g requires root rights to mount the filesystem if it is a block device, even with the  option in . See ntfs-3g-faq for details. The  option in the fstab is still required.

For non-blockfiles like normal images, ntfs-3g on the command-line should work out-of-the-box with normal user privileges as the underlying FUSE calls are redirected to the setuid-root fusermount when direct kernel interaction is unavailable.

## Resizing NTFS partition
Most systems that are purchased already have Windows installed on it, and some people would prefer not wipe it off completely when doing an Arch Linux installation. For this reason, among others, it is useful to resize the existing Windows partition to make room for a Linux partition or two. This is often accomplished with a Live CD or bootable USB thumb drive.

For Live CDs the typical procedure is to download an ISO file, burn it to a CD, and then boot from it. InfraRecorder is a free (as in GPL3) CD/DVD burning application for Windows which fits the bill nicely. If you would rather use a bootable USB media instead, see USB flash installation media for methods to create bootable USB stick.

There are a number of bootable CD/USB images available. This list is not exhaustive, but is a good place to start:

*
*

Note that the important programs for resizing NTFS partitions include ntfs-3g and a utility like (G)parted or fdisk, provided by the  package. Unless you are an "advanced" user it is advisable to use a tool like GParted to perform any resize operations to minimize the chance of data loss due to user error.

If you already have Arch Linux installed on your system and simply want to resize an existing NTFS partition, you can use the parted and ntfs-3g packages to do it. Optionally, you can use the GParted GUI after installing the GParted package. At the core of the resizing is the  command.

## Troubleshooting
## Unsupported reparse point
When mounting an NTFS filesystem for Windows 10, and reading files or directories, you may

# see broken symbolic links to 'unsupported reparse point', or
# see the error message  (in this case you see  in the journal).

The reason for this are NTFS reparse points, used by Microsoft to extend the file system. NTFS-3G does not support some types of reparse points by default. NTFS-3G plugins may be used to provide compatibility with a part of the features defined by the following reparse points:

* System compression: also known as "Compact OS", this feature provides a stronger, executable-optimized type of conversion than NTFS's old LZ77. Use the  plugin for read-only support, or run  in Windows to disable.
* Deduplicated files: this is a Windows Server 2012 feature providing block-level offline deduplication. Not yet packaged in AUR.
* OneDrive files: OneDrive files are stored as a special volume on Windows. The  plugin gives read-write access only for files marked "available locally".

See this page for further details, and archive.org for downloads.

## Damaged NTFS filesystems
If an NTFS filesystem has errors on it, NTFS-3G will mount it as read-only. To fix an NTFS filesystem, load Windows and run its disk checking program, chkdsk.

Note that ntfsfix can only repair some errors. If it fails, chkdsk will probably succeed.

To fix the NTFS file system, the device must already be unmounted. For example, to fix an NTFS partition residing in :

 # umount /dev/sda2
 # ntfsfix /dev/sda2
 Mounting volume... OK
 Processing of $MFT and $MFTMirr completed successfully.
 NTFS volume version is 3.1.
 NTFS partition /dev/sda2 was processed successfully.
 # mount /dev/sda2

If all went well, the volume will now be writable.

## Garbled Chinese file name under Windows partition
See Character encoding#Incorrect mount encoding.

## Metadata kept in Windows cache, refused to mount
When dual booting with Windows 8 or 10, trying to mount a partition that is visible to Windows may yield the following error:

 The disk contains an unclean file system (0, 0).
 Metadata kept in Windows cache, refused to mount.
 Failed to mount '/dev/sdc1': Operation not permitted
 The NTFS partition is in an unsafe state. Please resume and shutdown
 Windows fully (no hibernation or fast restarting), or mount the volume
 read-only with the 'ro' mount option.

The problem is due to a feature introduced in Windows 8 called "fast startup". When fast startup is enabled, part of the metadata of all mounted partitions are restored to the state they were at the previous closing down. As a consequence, changes made on Linux may be lost. This can happen to any NTFS partition when selecting "Shut down" or "Hibernate" under Windows 8 or 10. Leaving Windows by selecting "Restart", however, is apparently safe.

To enable writing to the partitions on other operating systems, be sure fast startup is disabled. This can be achieved by issuing as an administrator the command:

 powercfg /h off

You can check the current settings on Control Panel > Hardware and Sound > Power Options > System Setting > Choose what the power buttons do. The box Turn on fast startup should either be disabled or missing.

## Deleting Windows hibernate metadata
As an alternative to above clean shutdown method, there is a way to completely destroy NTFS metadata that was saved after hibernating. This method is only feasible if you are not able or unwilling to boot into Windows and shut it down completely. This is by running ntfsfix provided by .

 # ntfsfix /dev/your_NTFS_partition

## Mount failure
If you cannot mount your NTFS partition even when following this guide, try using the UUID instead of device name in  for all NTFS partitions. See fstab#File system UUIDs for an example.

## Windows mount failure
Windows will not recognize a NTFS partition that does not have a corresponding partition type. A common pitfall when creating an NTFS partition to work with Windows is forgetting to set the partition type as NTFS. See fdisk or one of the partitioning tools.
