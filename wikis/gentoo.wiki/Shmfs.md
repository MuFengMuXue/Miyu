Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Tmpfs/de "Tmpfs/de (2% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Tmpfs/hu "tmpfs (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Tmpfs/ru "Tmpfs (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Tmpfs/ja "tmpfs (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tmpfs "wikipedia:Tmpfs")

**tmpfs** (**t**e**mp**orary **f**ile **s**ystem) (formerly known as shmfs) is a virtual [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") created to store files in dynamic (volatile) memory. tmpfs is typically created on RAM.

** Warning**\
The volatile memory (such as RAM) cannot keep the files after system shutdown, reboot, or crash. It should be apparent by the name: tmpfs is meant only for ephemeral files. Best practice is to only store *recoverable/regeneratable* files in tmpfs.

In Linux ramfs (**r**andom **a**ccess **m**emory **f**ile **s**ystem) has been replaced by tmpfs as the old ramfs did not handle well when the system run out of memory. tmpfs allows the filesystem to grow dynamically when it needs more space until it hits the pre-set maximum value it has been allocated; after that it will use swap space if it is available.

There are many cases for using temporary file systems in Linux, one being the [/tmp] directory which does not need to physically store non-volatile data.

** Important**\
When using systemd, the [/tmp] directory is mounted by default as tmpfs. See [this section](https://wiki.gentoo.org/wiki/Tmpfs#systemd "Tmpfs") to disable this behavior and mount it manually in [/etc/fstab].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [systemd]](#systemd)
    -   [[2.2] [OpenRC]](#OpenRC)
-   [[3] [Conclusion]](#Conclusion)
-   [[4] [Advancements in technology]](#Advancements_in_technology)
-   [[5] [See also]](#See_also)

## [Installation]

### [Kernel]

Users need to activate the following kernel options:

[KERNEL] **Enable tmpfs support**

    File systems  --->
         Pseudo filesystems  --->
              [*] Tmpfs virtual memory file system support (former shm fs)
              [ ] Optional drivers

  ---------------------------------- --------------------------------------------------------------------------------------------------------------------------------------
  Option                             Description
  Tmpfs POSIX Access Control Lists   Enable [ACL](https://en.wikipedia.org/wiki/Access_control_list#Filesystem_ACLs "wikipedia:Access control list") permissions.
  Tmpfs extended attributes          Enable metadata support.
  ---------------------------------- --------------------------------------------------------------------------------------------------------------------------------------

  : Optional drivers

## [Usage]

Generate and mount tmpfs in one step:

`root `[`#`]`mount -t tmpfs tmpfs /MOUNTPOINT`

Users can specify the mount option *size* to control the maximum size of the filesystem (default: half of system RAM). Note that tmpfs doesn\'t reserve this memory, but allocates only the needed memory.

### [[] systemd]

When using systemd the [/tmp] directory is mounted by default as tmpfs and given a default size which is deemed big enough without chewing up too much RAM.

Users can view mounted temporary filesystems using the following command:

`root `[`#`]`findmnt --target /tmp`

This will show if the [/tmp] mount point is a tmpfs filesystem and the size of such filesystem.

In order to disable this behavior and take back control of the directory by using [/etc/fstab] the user needs to run the following command:

`root `[`#`]`systemctl mask tmp.mount`

This command will now not mount [/tmp] as a tmpfs and will automatically switch back to a block device.

Users should now add a new line in [/etc/fstab] which will create a tmpfs for [/tmp] manually.

[FILE] **`/etc/fstab`tmpfs fstab example**

    tmpfs /tmp tmpfs rw,nosuid,nodev,size=4G,mode=1777 0 0

### [OpenRC]

OpenRC users should simply add the mount point into [/etc/fstab]:

[FILE] **`/etc/fstab`tmpfs fstab example**

    tmpfs /tmp tmpfs rw,nosuid,nodev,size=4G,mode=1777 0 0

\

** Note**\
If the user is interested in mounting other directories besides [/tmp], be sure to first check if they already use tmpfs with the [findmnt] command:

`root `[`#`]`findmnt --target /<directory-to-check>`

## [Conclusion]

The outcome of using a temporary filesystem for non volatile files such as the [/tmp] directory is that the system has a very fast and very responsive access to caching files and stored session media. This also helps when using a browser to surf the web as cookies can be stored on this volatile media speeding up the application; on every reboot they are scrubbed or wiped from RAM. If users need to keep temporary files for analytics then they should avoid using the tmpfs filesystem for [/tmp] and other directories. All data stored in the tmpfs mount point will be lost when the system is rebooted or powered down.

## [Advancements in technology]

Some hardware manufactures provide devices that are slower than RAM but faster than SSD to be used as cache drives. These devices are usually incorporated on a PCIe add-in card and have either an adapter from PCIe to M.2 slot or the entire memory device is embedded into the PCIe card.

If users need a non-volatile high speed versatile solution faster than SSD/SAS/SATA then these high speed solutions should be considered. Of course users should not mount these devices with tmpfs but instead use a conventional partitioning filesystem.

Technology such as the Intel 3Dx Optane memory cache can be used too, but this technology, although more versatile than SSD, is still subject to wearing out. It does however provide a brilliant midway point that will only get better as the technology progresses in the future and provides us with a much faster computing experience when setup correctly.

## [See also]

-   [Portage TMPDIR on tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs") --- It is unlikely that tmpfs will provide any performance gain for modern systems
-   [Zram](https://wiki.gentoo.org/wiki/Zram "Zram") --- a [Linux kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") feature and set of userspace tools for creating compressible RAM-based block devices.