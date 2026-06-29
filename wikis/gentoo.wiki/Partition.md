Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Partition/hu "Partíció (88% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Partition/ja "パーティション (100% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Disk_partitioning "wikipedia:Disk partitioning")

A **partition** is a means of splitting a block device up to sub-regions. It allows creating a more manageable and adaptive \"logical\" structure visible to the system. The PARTUUID (partition UUID) can be seen using [blkid].

** See also**\
See the [Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks "Handbook:AMD64/Installation/Disks") for more information on partitioning for Gentoo.

** Note**\
The software presented in the following sections sometimes supports more partition table types than listed. For example, [fdisk] also supports Sun, SGI and BSD partition tables.

## Contents

-   [[1] [Master Boot Record (MBR)]](#Master_Boot_Record_.28MBR.29)
    -   [[1.1] [Kernel configuration]](#Kernel_configuration)
    -   [[1.2] [Available software]](#Available_software)
    -   [[1.3] [Supported operating systems]](#Supported_operating_systems)
-   [[2] [GUID Partition Table (GPT)]](#GUID_Partition_Table_.28GPT.29)
    -   [[2.1] [Kernel configuration]](#Kernel_configuration_2)
    -   [[2.2] [Available software]](#Available_software_2)
    -   [[2.3] [Supported operating systems]](#Supported_operating_systems_2)
-   [[3] [Logical Volume Manager (LVM)]](#Logical_Volume_Manager_.28LVM.29)
    -   [[3.1] [Kernel configuration]](#Kernel_configuration_3)
    -   [[3.2] [Available software]](#Available_software_3)
    -   [[3.3] [Supported operating systems]](#Supported_operating_systems_3)
-   [[4] [ZFS]](#ZFS)
    -   [[4.1] [Available software]](#Available_software_4)
    -   [[4.2] [Supported operating systems]](#Supported_operating_systems_4)
-   [[5] [Other software]](#Other_software)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [][Master Boot Record (MBR)]

** See also**\
See [Master Boot Record](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record") article for more information.

Used for a long time to organize data, also called DOS-Partitions. Partition information is stored in the first 512 bytes of the device.

-   Widespread and supported in nearly all operating systems.
-   Very well documented.
-   Maximum of 4 primary partitions per device.
-   Maximum size of the device 2 TiB.
-   Using one primary partition as an extended partition, it is possible to create additional logical partitions to work around the problem of only 4 primary partitions.

### [Kernel configuration]

[KERNEL] **Enable MBR support (CONFIG_MSDOS_PARTITION)**

    -*- Enable the block layer
        Partition Types  --->
          [*] Advanced partition selection
          [*]   PC BIOS (MSDOS partition tables) support

### [Available software]

The following programs can be used to create, alter, and remove MBR partitions:

  ----------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------- ----------------------------------------------------------------------------
  Program                                                                 Package                                                                                                                                                                                                                                                                                                                                                                                                GUI        Function
  [cfdisk](https://wiki.gentoo.org/wiki/Util-linux#cfdisk "Util-linux")   [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]                        ncurses    Create, alter, and remove partitions. More intuitive interface than fdisk.
  [fdisk](https://wiki.gentoo.org/wiki/Util-linux "Util-linux")           [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]                        No         Create, alter, and remove partitions.
  gparted                                                                 [[[sys-block/gparted]](https://packages.gentoo.org/packages/sys-block/gparted)[]]                              GTK3       GNOME Partition Editor; create, alter, and remove partitions.
  parted                                                                  [[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]]                                 No         Create, alter, remove, check, copy partitions and file systems.
  partitionmanager                                                        [[[sys-block/partitionmanager]](https://packages.gentoo.org/packages/sys-block/partitionmanager)[]]   Qt5        KDE Partition Manager; create, alter, and remove partitions.
  [sfdisk](https://wiki.gentoo.org/wiki/Util-linux "Util-linux")          [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]                        No         Non-interactive version of fdisk.
  ----------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------- ----------------------------------------------------------------------------

### [Supported operating systems]

-   BSD (Mac OS X) - full support.
-   DOS - full support.
-   Linux - full support.
-   Solaris - full support.
-   Windows - full support.

## [][GUID Partition Table (GPT)]

** See also**\
See [GPT](https://wiki.gentoo.org/wiki/GPT "GPT") article for more information.

In GUID (**G**lobal **U**nique **ID**entifier) partition system, a small amount of disk space at the beginning of the device is used to store the partition information. Its main advantage is the supported size of storage devices and the creation of a backup of the partition table at the end of the device.

-   Widespread and supported in most modern operating systems.
-   Maximum of 128 primary partitions per device.
-   Maximum size of the device 8 ZiB.

### [Kernel configuration]

[KERNEL] **Enable GPT support (CONFIG_EFI_PARTITION)**

    -*- Enable the block layer
        Partition Types  --->
          [*]   EFI GUID Partition support

### [Available software]

The following programs can be used to create, alter, and remove **[GPT](https://en.wikipedia.org/wiki/GUID_Partition_Table "wikipedia:GUID Partition Table")** partitions:

  ---------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------- ---------------------------------------------------------------------------------------
  Program                                                          Package                                                                                                                                                                                                                                                                                                                                                                                                   GUI     Function
  [cfdisk](https://wiki.gentoo.org/wiki/Util-linux "Util-linux")   [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]                           No      Create, alter, and remove partitions. More intuitive interface than fdisk.
  [fdisk](https://wiki.gentoo.org/wiki/Util-linux "Util-linux")    [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]                           No      Create, alter, and remove partitions.
  GNOME Disks                                                      [[[sys-apps/gnome-disk-utility]](https://packages.gentoo.org/packages/sys-apps/gnome-disk-utility)[]]   GTK3    GNOME partition manager.
  gparted                                                          [[[sys-block/gparted]](https://packages.gentoo.org/packages/sys-block/gparted)[]]                                 GTK3    GNOME Partition Editor; create, alter, and remove partitions.
  gptfdisk                                                         [[[sys-apps/gptfdisk]](https://packages.gentoo.org/packages/sys-apps/gptfdisk)[]]                                 No      Create, alter, remove, convert MBR to GPT, and recreate partition tables from backup.
  parted                                                           [[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]]                                    No      Create, alter, remove, check, copy partitions and file systems.
  partitionmanager                                                 [[[sys-block/partitionmanager]](https://packages.gentoo.org/packages/sys-block/partitionmanager)[]]      Qt5     KDE Partition Manager; create, alter, and remove partitions.
  [sfdisk](https://wiki.gentoo.org/wiki/Util-linux "Util-linux")   [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]                           No      Non-interactive version of fdisk.
  ---------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------- ---------------------------------------------------------------------------------------

### [Supported operating systems]

-   BSD (Mac OS X) - full support.
-   Linux - full support.
-   Windows - Installs into the [/boot/EFI/Microsoft/] subdirectory of the [ESP](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition").

## [][Logical Volume Manager (LVM)]

** See also**\
See [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") article for more information.

LVM is a complete suite to dynamically manage partitions, storage devices or other underlying systems as volumes.

-   Widespread and supported in most modern operating systems.
-   Maximum size of the device depends on the underlying systems limitations.
-   Maximum size of Logical Volumes is 8 EiB on 64-bit Linux and 16 TiB on 32-bit Linux.
-   Storage devices, RAID system, network storage (e.g. [iSCSI](https://wiki.gentoo.org/wiki/ISCSI "ISCSI")) can be used as Physical Volumes (no need of partitioning).
-   Provides basic forms of data redundancy (RAID 1, RAID 5) or stripset (RAID 0) for performance.

** Note**\
To use features like dynamic resizing, the used filesystem should be resizable as well.

### [Kernel configuration]

[KERNEL] **Enabling LVM**

    Device Drivers  --->
       Multiple devices driver support (RAID and LVM)  --->
           <*> Device mapper support
               <*> Crypt target support
               <*> Snapshot target
               <*> Thin provisioning target
               <*> Mirror target
               <*> Multipath target
                   <*> I/O Path Selector based on the number of in-flight I/Os
                   <*> I/O Path Selector based on the service time

### [Available software]

The following programs come with [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]]

  ---------- ----- ---------------------------------------------------------------
  Program    GUI   Function
  lvcreate   No    Create, alter, and remove volumes.
  pvcreate   No    Create or remove Physical Volumes of storage devices/systems.
  vgcreate   No    Groups PV as Volume Group.
  ---------- ----- ---------------------------------------------------------------

The following programs can be used to create, alter, and remove LVM partitions:

  ------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------ ---------------------------------------------------------------------
  Program            Package                                                                                                                                                                                                                                                                                                                                                                                                GUI    Function
  partitionmanager   [[[sys-block/partitionmanager]](https://packages.gentoo.org/packages/sys-block/partitionmanager)[]]   Qt5    KDE Partition Manager; create, alter, and remove LVM PVs, VGs, LVs.
  ------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------ ---------------------------------------------------------------------

### [Supported operating systems]

-   BSD - cannot boot itself, needs Linux [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") with dual boot.
-   Linux - full support.

** Note**\
This is the Linux specific LVM implementation, other OS have their own systems, see [Logical volume management](https://en.wikipedia.org/wiki/Logical_volume_management#Implementations "wikipedia:Logical volume management").

## [ZFS]

** See also**\
See [ZFS](https://wiki.gentoo.org/wiki/ZFS "ZFS") article for more information.

ZFS is a complete suite to dynamically manage storage and [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem").

-   Support in Linux (via ZFSOnLinux^[\[1\]](#cite_note-1)^), Solaris, FreeBSD.
-   Needs [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") bootloader.
-   Maximum size of a single zpool is 256 ZiB
-   Storage devices can be used complete as vdev (no need of partitioning)
-   Zpools are created once and cannot be resized afterwards. Every volume has access to the full capacity of the zpool, this can be reduced via quota.
-   It provides forms of redundancy like RAID 1 (mirroring), and RAID 0 (striping) for performance. Also supports RAID 5, RAID 6, etc.
-   Has its own filesystem with features like compression, copy-on-write, and deduplication.

### [Available software]

The following programs come with [[[sys-fs/zfs]](https://packages.gentoo.org/packages/sys-fs/zfs)[]]:

  --------- ----- ---------------------------------------------
  Program   GUI   Function
  zfs       No    Create, alter (resize), and remove volumes.
  zpool     No    Manage and organize vdevs in zpools.
  --------- ----- ---------------------------------------------

### [Supported operating systems]

-   BSD - full support.
-   Linux - built as external module because of the CDDL and GPL license conflict - mostly supported.
-   Solaris - full support.

## [Other software]

[Busybox](https://wiki.gentoo.org/wiki/Busybox "Busybox") also contains a version of fdisk.

There are some special versions of fdisk for specific system types in the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), such as: [[[sys-fs/arm-fdisk]](https://packages.gentoo.org/packages/sys-fs/arm-fdisk)[]], [[[sys-fs/mac-fdisk]](https://packages.gentoo.org/packages/sys-fs/mac-fdisk)[]], or [[[sys-fs/atari-fdisk]](https://packages.gentoo.org/packages/sys-fs/atari-fdisk)[]].

See [sys-fs](https://packages.gentoo.org/categories/sys-fs) category for even more tools.

## [See also]

-   [Complete Handbook/Putting the minimal environment in place](https://wiki.gentoo.org/wiki/Complete_Handbook/Putting_the_minimal_environment_in_place "Complete Handbook/Putting the minimal environment in place")
-   [Filesystem/Security](https://wiki.gentoo.org/wiki/Filesystem/Security "Filesystem/Security") --- one of the basic means to harden a system.
-   [Handbook:AMD64/Installation/Disks](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks "Handbook:AMD64/Installation/Disks")

## [References]

1.  [[[↑](#cite_ref-1)] [[OpenZFS on Linux](https://zfsonlinux.org/)]]