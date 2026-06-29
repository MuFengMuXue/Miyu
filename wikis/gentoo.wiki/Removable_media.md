Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Removable_media/hu "Cserélhető adathordozó (57% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Removable_media/ja "リムーバブルメディア (72% translated)")

**Removable media** are simply any media that is easily removed from a system. Typically this includes [CDs](https://wiki.gentoo.org/wiki/CDROM "CDROM"), DVDs, [USB](https://wiki.gentoo.org/wiki/USB "USB") drives, or memory cards of all form factors.

These types of media require special handling if an unprivileged user desires to [[mount](https://wiki.gentoo.org/wiki/Mount "Mount")] an unknown device.

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [UUIDs and labels]](#UUIDs_and_labels)
-   [[3] [Mounting removable media]](#Mounting_removable_media)
-   [[4] [MTP]](#MTP)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Prerequisites]

-   [Kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") support for the storage device.
-   Kernel support for the [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") used by the device.

## [[] UUIDs and labels]

Even though storage devices are identified by their [device file](https://wiki.gentoo.org/wiki/Device_file "Device file") in many cases, e.g. [/dev/sd\*], their **UUID** ([/dev/disk/by-uuid/\*]) or **label** ([/dev/disk/by-label/\*]) can be used as a more convenient alternative. In comparison to device files, UUIDs and labels are persistent and will never change because of asynchronous detection. The UUID is generated automatically during [partition](https://wiki.gentoo.org/wiki/Partition "Partition") (in case of [GPT](https://wiki.gentoo.org/wiki/GUID_Partition_Table "GUID Partition Table")) and [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") creation. The optional label can be specified at time of creation or changed afterwards.

UUIDs are considered unique. Especially when removable media is used, labels may *not* be unique. While device file names may change every time an external storage device is connected, filesystem UUIDs may be used as a stable means of identification, as may filesystem labels. Alternatively, partition UUIDs and labels can be used, but are less common and not always available.

** Warning**\
When a drive is cloned using a 1:1 copy method, the UUIDs will be non-unique when both drives are connected at the same time. Professional cloning software may change cloned partition and filesystem UUIDs so they become unique again, but may not support all filesystems.

**U**niversally **U**nique **Id**entifiers, UUIDs in short, are used in many places for partitions, filesystems and other (logical) volumes. It is paramount to understand which UUID is used to identify a specific entity.

[CODE]

    +-----------------------------------------------------------------+  +------------------------------------+
    |                  Disk /dev/sdX (Physical Drive)                 |  |   Disk /dev/sdY (physical drive)   |
    |     GPT Disk UUID      (lsblk: PTUUID)    entire disk GUID      |  | GPT Disk UUID (PTUUID) entire disk |
    +-----------------------------------------------------------------+  +------------------------------------+
    |                                                                 |  |                                    |
    | +---------------------------------------------+ +-------------+ |  | +-------------+ +----------------+ |
    | |         Partition (/dev/sdXn)               | | /dev/sdXn+1 | |  | | /dev/sdYn   | | /dev/sdYn+1    | |
    | |  Partition UUID         (lsblk: PARTUUID)   | |  PARTUUID   | |  | |  PARTUUID   | |  PARTUUID      | |
    | |  Partition Label        (lsblk: PARTLABEL)  | |  PARTLABEL  | |  | |  PARTLABEL  | |  PARTLABEL     | |
    | |  Filesystem Type UUID   (lsblk: PARTTYPE)   | |  PARTTYPE   | |  | |  PARTTYPE   | |  PARTTYPE      | |
    | |  +-- corresponding name (lsblk: FSTYPE)     | |   |         | |  | |   |         | |  +-- FSTYPE    | |
    | |                                             | |  LVM PV     | |  | |  LVM PV     | |                | |
    | |  +---------------------------------------+  | | +------------------------------+ | | +-----------+  | |
    | |  |   Filesystem (e.g. ext4, xfs)         |  | | |  LVM volume group (VG)       | | | | e.g. swap |  | |
    | |  |   +-- UUID       (lsblk: UUID)        |  | | |                              | | | | +-- UUID  |  | |
    | |  |   +-- Label      (lsblk: LABEL)       |  | | |                              | | | | +-- LABEL |  | |
    | |  +---------------------------------------+  | | +------------------------------+ | | +-----------+  | |
    | +---------------------------------------------+ +-------------+ |  | +-------------+ +----------------+ |
    |                                                                 |  |                                    |
    +-----------------------------------------------------------------+  +------------------------------------+

On many systems UUIDs are used for:

1.  a partition table in case [lsblk] `PTTYPE` is `gpt` (short for [GUID Partition Table](https://wiki.gentoo.org/wiki/GUID_Partition_Table "GUID Partition Table"))
    -   a GUID Partition Table unique UUID ([lsblk]: `PTUUID`); this will differ for each drive, e.g. [/dev/nvme0n0] will have a different `PTUUID` than [/dev/nvme0n1], [/dev/sda] or [/dev/sdb].
2.  a partition of that partition table
    -   each partition of a GPT has a unique UUID ([lsblk]: `PARTUUID`)
    -   each partition can have a (non-unique) label ([lsblk]: `PARTLABEL`)
    -   each partition has a non-unique filesystem type UUID ([lsblk]: `PARTTYPE`)\
        (Note that `FSTYPE` will give each filesystem type UUID a name, i.e. `0657FD6D-A4AB-43C4-84E5-0933C84B4F4F` stands for `FSTYPE` `swap`, a Linux swap partition; the `PARTTYPE` UUIDs for the specified type are automatically assigned by partition tools such as [gdisk].)
3.  a filesystem, e.g. in a partition or [LVM](https://wiki.gentoo.org/wiki/LVM "LVM")
    -   unique UUIDs are filesystem-dependent or assigned by Linux, see [/dev/disk/by-uuid] ([lsblk]: `UUID`)\
        Unix i.e. Linux, \*BSD and macOS filesystems are typically in the form `faaf358f-bead-4e26-bd1d-c673af6b636d`, whereas filesystems from other operating systems may be different, e.g. for VFAT the volume serial number is used as UUID, like `1234-ABCD`, and NTFS uses 64-bit wide UUIDs (16 characters) `0123456789ABCDEF`. On UEFI-based systems the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP) is VFAT.
    -   a filesystem-dependent non-unique volume label may be present ([lsblk]: `LABEL`)

** Note**\
Logical block layers, such as [dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt")-based LUKS and [LVM](https://wiki.gentoo.org/wiki/LVM "LVM"), internally also use UUIDs which are **not** usable by [mount] or in [/etc/fstab].

** Note**\
Other partition tables, such as [MBR](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record"), neither support partition UUIDs nor labels. While [APM](https://en.wikipedia.org/wiki/Apple_Partition_Map "wikipedia:Apple Partition Map") doesn\'t support UUIDs either, it does feature partition names, but they are not treated as labels by the kernel.

For the most part, the filesystem UUID ([lsblk]: `UUID`) should be used (it is the most unique identifier for a volume), followed by a volume label ([lsblk]: `LABEL`), which may not be unique since it is possible to give two or more partitions the same volume label. This will also work in cases such as LUKS encrypted partitions and LVMs. Since a partition UUID ([lsblk]: `PARTUUID`) will normally also be unique, it can alternatively be used if the filesystem is in that partition, whereas two or more partitions may be given the same label ([lsblk]: `PARTLABEL`).

All UUIDs (except the partition table UUID itself, `PTUUID`) and labels (if unique) are usable to identify a volume (i.e. filesystem) for the use in [/etc/fstab] and with [mount].

  ----------------------------------- --------------------------------------------------------------------------------------------------------
                                      use in\
                                      [/etc/fstab]\
                                      and [mount]

  Partition UUID                      `PARTUUID=`

  Partition label                     `PARTLABEL=`

  Filesystem UUID                     `UUID=`

  Filesystem label                    `LABEL=`
  ----------------------------------- --------------------------------------------------------------------------------------------------------

The partition UUIDs and labels can only be used if the mountable filesystem is directly installed on the partition. If an additional logical layer is used on top of partitions (on Linux mostly [dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt")-based), such as encrypted partitions (e.g. [LUKS](https://wiki.gentoo.org/wiki/LUKS "LUKS")) or logical volumes ([LVM LV](https://wiki.gentoo.org/wiki/LVM#LV_.28Logical_Volume.29 "LVM")), only the filesystem UUIDs or labels can be used for mounting---after they\'ve been made available logically.

Use [tree /dev/disk/] or [lsblk] (part of [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]) to show all storage devices and their UUIDs and labels:

`user `[`$`]`tree /dev/disk/`

`user `[`$`]`lsblk -o +fstype,label,uuid,partuuid`

    NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT FSTYPE   LABEL           UUID                                 PARTUUID
    sda      8:0    0 111.8G  0 disk
    ├─sda1   8:1    0    96M  0 part            ext2                     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-01
    ├─sda2   8:2    0     1K  0 part                                                                          xxxxxxxx-02
    ├─sda3   8:3    0   100M  0 part            ntfs     System Reserved XXXXXXXXXXXXXXXX                     xxxxxxxx-03
    ├─sda4   8:4    0  29.6G  0 part            ntfs                     XXXXXXXXXXXXXXXX                     xxxxxxxx-04
    ├─sda5   8:5    0   2.8G  0 part [SWAP]     swap                     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-05
    └─sda6   8:6    0  79.2G  0 part /          ext4                     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-06
    sr0     11:0    1  1024M  0 rom

## [Mounting removable media]

For [mounting](https://wiki.gentoo.org/wiki/Mount "Mount") as a normal user without root privileges the device needs an entry with the [user] option in [[/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab#UUIDs_and_labels "/etc/fstab")].

Plug removable media to the computer then run [tree /dev/disk/] or [lsblk].

`user `[`$`]`lsblk -o +fstype,label,uuid,partuuid`

    NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT FSTYPE   LABEL           UUID                                 PARTUUID
    sda      8:0    0 111.8G  0 disk
    ├─sda1   8:1    0    96M  0 part            ext2                     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-01
    ├─sda2   8:2    0     1K  0 part                                                                          xxxxxxxx-02
    ├─sda3   8:3    0   100M  0 part            ntfs     System Reserved XXXXXXXXXXXXXXXX                     xxxxxxxx-03
    ├─sda4   8:4    0  29.6G  0 part            ntfs                     XXXXXXXXXXXXXXXX                     xxxxxxxx-04
    ├─sda5   8:5    0   2.8G  0 part [SWAP]     swap                     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-05
    └─sda6   8:6    0  79.2G  0 part /          ext4                     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-06
    sdb      8:16   1   3.8G  0 disk
    └─sdb1   8:17   1   3.8G  0 part            vfat                     QWER-1234
    sdc      8:32   1   1.9G  0 disk
    └─sdc1   8:33   1   1.9G  0 part            vfat     QWERTZ12345     4321-REWQ                            qwer1234-01
    sr0     11:0    1  1024M  0 rom

The [sdb1] and [sdc1] lines display the [UUIDs](https://wiki.gentoo.org/wiki/Removable_media#UUIDs_and_labels "Removable media") [QWER-1234] and [4321-REWQ] to be added to [/etc/fstab] for two media just plugged-in. [sdc1] also has the label [QWERTZ12345] which could be used alternatively. Let\'s create their mountpoints [larry1] and [larry2]:

`root `[`#`]`mkdir /mnt/ `

`root `[`#`]`chmod 777 /mnt/ `

And add them in [/etc/fstab].

[FILE] **`/etc/fstab`**

    # <fs>            <mountpoint> <type> <opts>         <dump/pass>
    ...
    UUID=QWER-1234    /mnt/larry1  vfat   noauto,rw,user     0 0
    LABEL=QWERTZ12345 /mnt/larry2  vfat   noauto,rw,user     0 0

With the [user] option in these entries, they can be mounted / unmounted by normal users.

`user `[`$`]`mount /mnt/larry1`

`user `[`$`]`mount /mnt/larry2`

To see what is mounted, run [mount] without arguments or [lsblk] again and find the [MOUNTPOINT] column populated for sdb1 and sdc1:

`user `[`$`]`lsblk -o +fstype,label,uuid,partuuid`

    NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT  FSTYPE   LABEL           UUID                                 PARTUUID
    sda      8:0    0 111.8G  0 disk
    ├─sda1   8:1    0    96M  0 part             ext2                     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-01
    ├─sda2   8:2    0     1K  0 part                                                                           xxxxxxxx-02
    ├─sda3   8:3    0   100M  0 part             ntfs     System Reserved XXXXXXXXXXXXXXXX                     xxxxxxxx-03
    ├─sda4   8:4    0  29.6G  0 part             ntfs                     XXXXXXXXXXXXXXXX                     xxxxxxxx-04
    ├─sda5   8:5    0   2.8G  0 part [SWAP]      swap                     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-05
    └─sda6   8:6    0  79.2G  0 part /           ext4                     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-06
    sdb      8:16   1   3.8G  0 disk
    └─sdb1   8:17   1   3.8G  0 part /mnt/larry1 vfat                     QWER-1234
    sdc      8:32   1   1.9G  0 disk
    └─sdc1   8:33   1   1.9G  0 part /mnt/larry2 vfat     QWERTZ12345     4321-REWQ                            qwer1234-01
    sr0     11:0    1  1024M  0 rom

Once a device is mounted it can be accessed like a normal hard disk. Usual operations like [cp], [mv], [rm], etc. work fine.

For unmounting the usage of mountpoint, label or UUID is equivalent as is for mounting. Any of them will do it.

`user `[`$`]`umount /mnt/larry2`

`user `[`$`]`umount LABEL=QWERTZ12345`

`user `[`$`]`umount UUID=4321-REWQ`

Mounting without the [/etc/fstab] entry can be done by root only.

`root `[`#`]`mount UUID=QWER-1234 /mnt/larry1`

`user `[`$`]`mount`

    /dev/sdb1 on /mnt/larry1 type vfat (rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=iso8859-1,shortname=mixed,errors=remount-ro)

For further details see [[[mount(8)]](https://man.archlinux.org/man/mount.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.

Another alternative is to edit [/usr/share/polkit-1/actions/org.freedesktop.UDisks2.policy], under action id `org.freedesktop.udisks2.filesystem-mount`, for `allow_any` change the value from `auth_admin` to `yes`. This will allow a disk to be mounted by remote and local users.

** Warning**\
Consider this change a potential security risk.

[FILE] **`/usr/share/polkit-1/actions/org.freedesktop.UDisks2.policy`**

        <action id="org.freedesktop.udisks2.filesystem-mount">
          <description>Mount a filesystem</description>
          <message>Authentication is required to mount the filesystem</message>
          <defaults>
            <allow_any>yes</allow_any>
            <allow_inactive>auth_admin</allow_inactive>
            <allow_active>yes</allow_active>
          </defaults>
        </action>

## [MTP]

For handling media using the **MTP** (**M**edia **T**ransfer **P**rotocol) protocol see the [MTP](https://wiki.gentoo.org/wiki/MTP "MTP") article.

## [See also]

-   [Mount](https://wiki.gentoo.org/wiki/Mount "Mount") --- the attaching of an additional [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") to the currently accessible filesystem of a computer.
-   [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") --- a configuration file that defines how and where the main [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") are to be mounted, especially at boot time.
-   [CurlFtpFS](https://wiki.gentoo.org/wiki/CurlFtpFS "CurlFtpFS") --- allows for [mounting](https://wiki.gentoo.org/wiki/Mount "Mount") an FTP folder as a regular directory to the local directory tree.
-   [AutoFS](https://wiki.gentoo.org/wiki/AutoFS "AutoFS") --- a program that uses the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") automounter to automatically [mount](https://wiki.gentoo.org/wiki/Mount "Mount") [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on demand.
-   [Udisks](https://wiki.gentoo.org/wiki/Udisks "Udisks") --- a [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") daemon offering storage related services.
-   [Silk Guardian](https://wiki.gentoo.org/wiki/Silk_Guardian "Silk Guardian") --- a Linux kernel module kill switch that upon detecting changes to USB ports, wipes the RAM, securely deletes user specified files, and then shuts down the system.

## [External resources]

-   [https://wiki.debian.org/Part-UUID](https://wiki.debian.org/Part-UUID)
-   [https://en.wikipedia.org/wiki/Universally_unique_identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier)