Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki//etc/fstab/de "/etc/fstab (97% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki//etc/fstab/es "/etc/fstab (97% translated)")
-   [français](https://wiki.gentoo.org/wiki//etc/fstab/fr "/etc/fstab (97% translated)")
-   [italiano](https://wiki.gentoo.org/wiki//etc/fstab/it "/etc/fstab (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki//etc/fstab/hu "/etc/fstab (97% translated)")
-   [svenska](https://wiki.gentoo.org/wiki//etc/fstab/sv "Fstab (43% translated)")
-   [русский](https://wiki.gentoo.org/wiki//etc/fstab/ru "/etc/fstab (100% translated)")
-   [українська](https://wiki.gentoo.org/wiki//etc/fstab/uk "/etc/fstab (97% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki//etc/fstab/zh-cn "/etc/fstab (60% translated)")
-   [日本語](https://wiki.gentoo.org/wiki//etc/fstab/ja "/etc/fstab (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki//etc/fstab/ko "/etc/fstab/ko (10% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki//etc "wikipedia:/etc")

The **fstab** (**f**ile **s**ystem **tab**le) file ([/etc/fstab]) is a configuration file that defines how and where the main [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") are to be mounted, especially at boot time.

## Contents

-   [[1] [Syntax]](#Syntax)
-   [[2] [UUIDs and labels]](#UUIDs_and_labels)
-   [[3] [Services]](#Services)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [[] Syntax]

** Warning**\
For computers with multiple hard drives (such as two NVMe drives), using device names (e.g., [/dev/nvme0n1p1]) in fstab may cause random naming issues (for example, the previous [/dev/nvme0n1p1] may have become [/dev/nvme1n1p1] after booting), potentially leading to the ESP partition failing to mount at startup. It is recommended to use PARTUUID or UUID, which can be obtained through [blkid] command.

Each line of [/etc/fstab] contains the necessary settings to mount one partition, drive or network share. The line has six columns, separated by whitespaces or tabs. The columns are as follows:

1.  The [device file](https://wiki.gentoo.org/wiki/Device_file "Device file"), [UUID or label](https://wiki.gentoo.org/wiki//etc/fstab#UUIDs_and_labels "/etc/fstab") or other means of locating the partition or data source.
2.  The mount point, where the data is to be attached to the filesystem.
3.  The filesystem type. See [man 5 fstab] for more supported file system types.
4.  Options, including if the filesystem should be mounted at boot.
5.  Adjusts the archiving schedule for the partition (used by [[[app-arch/dump]](https://packages.gentoo.org/packages/app-arch/dump)[]] package). `0` disables, `1` enables the feature.
6.  Controls the order in which fsck checks the device/partition for errors at boot time. The root device should be `1`. Other partitions should be either `2` (to check after root) or `0` (to disable checking for that partition altogether).

An example for the root device:

[FILE] **`/etc/fstab`**

    /dev/sda1   /   ext4   defaults   0   1

Special characters can be escaped by using their octal representation from an ASCII table. For example, if the name of the mount point contains spaces or tabs these can be escaped as \\040 and \\011 respectively.

For more detailed information see [man 5 fstab].

** Tip**\
Options such as `discard` may seem useful for SSDs, though it is generally recommended to use [periodic trim jobs](https://wiki.gentoo.org/wiki/SSD#Periodic_fstrim_jobs "SSD") instead.

## [[] UUIDs and labels]

In the first column, a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier "wikipedia:Universally unique identifier") can be used instead of a device file:

[FILE] **`/etc/fstab`Using a UUID for the root partition**

    UUID=339df6e7-91a8-4cf9-a43f-7f7b3db533c6   /   ext4   defaults   0   1

Alternatively, a LABEL can be used:

[FILE] **`/etc/fstab`Using a label for the root partition**

    LABEL=Gentoo   /   ext4   defaults   0   1

Depending on the partition table (e.g. the GUID Partition Table \"GPT\"), PARTLABEL can be used:

[FILE] **`/etc/fstab`Using a label for the root partition**

    PARTLABEL=Gentoo   /   ext4   defaults   0   1

Please read [this](https://wiki.gentoo.org/wiki/Removable_media#UUIDs_and_labels "Removable media") for details on how to retrieve UUIDs and labels.

## [[] Services]

The following [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") services read the fstab to mount or manage the filesystems:

-   **localmount** - Mount disks and swap according to fstab.
-   **netmount** - Mount network shares according to fstab.
-   **fsck** - Check and repair filesystems according to fstab.
-   **root** - Mount the root filesystem read/write.

These services supplement the fstab, if the filesystems are not explicitly stated:

-   **sysfs** - Mount the [/sys] filesystem.
-   **devfs** - Mount system critical filesystems in [/dev].

Check that they are enabled to start at boot time:

`root `[`#`]`rc-update show`

## [[] See also]

-   [AutoFS](https://wiki.gentoo.org/wiki/AutoFS "AutoFS") --- a program that uses the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") automounter to automatically [mount](https://wiki.gentoo.org/wiki/Mount "Mount") [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on demand.
-   [Disk Quotas (Security Handbook)](https://wiki.gentoo.org/wiki/Security_Handbook/User_and_group_limitations#Quotas "Security Handbook/User and group limitations")
-   [fstab (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/System#About_fstab "Handbook:AMD64/Installation/System")
-   [Mounting partitions (Security Handbook)](https://wiki.gentoo.org/wiki/Security_Handbook/Mounting_partitions "Security Handbook/Mounting partitions")
-   [mount](https://wiki.gentoo.org/wiki/Mount "Mount") --- the attaching of an additional [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") to the currently accessible filesystem of a computer.
-   [removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") --- any media that is easily removed from a system.
-   [SSD](https://wiki.gentoo.org/wiki/SSD "SSD") --- provides guidelines for basic maintenance, such as enabling discard/trim support, for **SSD**s ([Solid State Drives](https://en.wikipedia.org/wiki/Solid-state_drive "wikipedia:Solid-state drive")) on Linux.

## [[] External resources]