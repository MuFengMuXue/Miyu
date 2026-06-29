# NTFS

From Wikipedia:
:NTFS (New Technology File System) is a proprietary journaling file system developed by Microsoft. Starting with Windows NT 3.1, it is the default file system of the Windows NT family.

The ntfs3 kernel driver provides read and write support for the file system.

There are no userspace utilities alongside the kernel driver. To format partitions and perform maintenance, you can install the  package from NTFS-3G or use a Windows machine.

## Tips and tricks
## Improving performance
You can enable the   option to decrease fragmentation in case of parallel write operations (most useful for HDD).

## Prevent creation of names not allowed by Windows
NTFS itself does not have restrictions for characters and names used, but Windows does.

ntfs3 supports   option. Use it to strictly maintain compatibility.

## Known issues
## Explicit file system type required to mount
 may require the file system type to mount, or may otherwise mount read-only, see #File system mounts read-only.

To be able to mount the file system, specify its type as . For example, using 's / option:

 # mount -t ntfs3 /dev/sdxY /mnt

Or using fstab:

## Troubleshooting
## File system mounts read-only
The kernel from  package has enabled  compatibility option It mimics the legacy driver behavior and mounts the file system read-only when  type is used for mount.

To mount the file system read-write, use  type. See #Explicit file system type required to mount.

## unknown filesystem type 'ntfs'
When mounting NTFS, you can encounter an error such as:

 mount: /mnt: unknown filesystem type 'ntfs'

See #Explicit file system type required to mount.

If you want to use  as the default driver for  partitions, such udev rule does the trick:

{{hc|/etc/udev/rules.d/ntfs3_by_default.rules|2=SUBSYSTEM=="block", ENV{ID_FS_TYPE}=="ntfs", ENV{ID_FS_TYPE}="ntfs3"}}

Although, this method is not recommended and can confuse some 3rd party tools.

## Unable to mount with ntfs3 with partition marked dirty
When trying to mount a good NTFS partition (i.e. which successfully mounts with NTFS-3G and for which  does not report any error), you may get the following error:

 mount: /mnt: wrong fs type, bad option, bad superblock on /dev/sdb1, missing codepage or helper program, or other error.
        dmesg(1) may have more information after failed mount system call.

ntfs3 will not mount a partition where the volume is marked dirty without the force option.  explicitly helps recognizing the situation, saying:

 sdb1: volume is dirty and "force" flag is not set!

You can try passing the  argument to  to clean it. [https://bbs.archlinux.org/viewtopic.php?id=271650
