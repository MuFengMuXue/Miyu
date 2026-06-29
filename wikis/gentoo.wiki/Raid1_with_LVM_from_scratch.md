[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

In this manual, a RAID 1 volume will be created with LVM. In this tutorial, disk are mounted in system as [/dev/sdX] and [/dev/sdY]

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Software]](#Software)
-   [[3] [Disk partitions create]](#Disk_partitions_create)
-   [[4] [LVM]](#LVM)
    -   [[4.1] [Physical volume]](#Physical_volume)
    -   [[4.2] [Volume group]](#Volume_group)
    -   [[4.3] [Logical Volume]](#Logical_Volume)
-   [[5] [Ext4 Filesystem (non encrypted)]](#Ext4_Filesystem_.28non_encrypted.29)
    -   [[5.1] [Mount filesystem on boot]](#Mount_filesystem_on_boot)
-   [[6] [Ext4 Filesystem (encrypted with LUKS)]](#Ext4_Filesystem_.28encrypted_with_LUKS.29)
    -   [[6.1] [Mount LUKS encrypted device on boot from LVM RAID 1]](#Mount_LUKS_encrypted_device_on_boot_from_LVM_RAID_1)
-   [[7] [Check LVM RAID 1 status]](#Check_LVM_RAID_1_status)
-   [[8] [Performance tunnig]](#Performance_tunnig)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)

## [Prerequisites]

-   2 empty HDDs with same capacity
-   Kernel with device mapper and RAID target support
-   [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]]
-   [[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]]

## [Software]

Make sure to enable the [[[lvm]](https://packages.gentoo.org/useflags/lvm)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") for [[[sys-fs/lvm2]](https://packages.gentoo.org/packages/sys-fs/lvm2)[]]:

[FILE] **`/etc/portage/package.use`**

    # Enable support for the LVM daemon and related tools
    sys-fs/lvm2 lvm

Install the LVM package:

`root `[`#`]`emerge sys-fs/lvm2`

Install GNU parted:

`(parted)``emerge sys-block/parted`

## [Disk partitions create]

** Warning**\
Data on /dev/sdX and /dev/sdY will be lost. Be careful with disk names!

Create partitions on both disks with parted.

Start [parted] for [/dev/sdX] disk

`root `[`#`]`parted -a optimal /dev/sdX`

Set units to mib:

`(parted)``unit mib`

Create GPT table on disk:

`(parted)``mklabel gpt`

Create primary partition, use all available space:

`(parted)``mkpart primary 1 -1`

Set partition name to raiddata0:

`(parted)``name 1 raiddata0`

Add lvm flag to new partition:

`(parted)``set 1 lvm on`

Result should be:

`(parted)``print`

    Model: ATA ST6000VN0033-2EE (scsi)
    Disk /dev/sdc: 6001GB
    Sector size (logical/physical): 512B/4096B
    Partition Table: gpt
    Disk Flags:

    Number  Start   End     Size    File system  Name       Flags
     1      1049kB  6001GB  6001GB               raiddata0  lvm

Execute same parted commands for [/dev/sdY].

## [LVM]

Next steps will be to create physical volumes on both disks, add both physical volumes to a volume group, and create a logical volume with RAID 1 logic.

### [Physical volume]

Create physical LVM volumes on the first disk\'s first partition:

`root `[`#`]`lvm pvcreate /dev/sdX1`

Create physical LVM volumes on the second disk\'s first partition:

`root `[`#`]`lvm pvcreate /dev/sdY1`

### [Volume group]

Include both physical volumes to one volume group with name *raid0vg0*:

`root `[`#`]`vgcreate raid0vg0 /dev/sdX1 /dev/sdY1`

Now both disks are in the same volume group.

### [Logical Volume]

Create logical volume with name *raid0lv0* on volume group *raid0vg0* with RAID 1 logic, using all available space. \--nosync means skip the initial synchronization for RAID 1 (because this is a new RAID without any data on it):

`root `[`#`]`lvcreate --mirrors 1 --type raid1 -l 100%FREE --nosync -n raid0lv0 raid0vg0 `

Now RAID 1 is created on both disks [/dev/sdX] and [/dev/sdY].

The final step is to create the filesystem and mount it on boot. See sections below.

## [][Ext4 Filesystem (non encrypted)]

Create filesystem on the logical volume *raid0lv0* on volume group *raid0vg0*:

`root `[`#`]`mkfs.ext4 /dev/raid0vg0/raid0lv0`

** Important**\
Do not forget to add lvm2 service at boot: [rc-update add lvm2 boot]

** Important**\
Your kernel should include LVM modules in initrd or compiled into kernel.

### [Mount filesystem on boot]

Run [blkid] to find UUID of the ext4 filesystem on *raid0lv0*:

`root `[`#`]`blkid`

    ...
    /dev/mapper/raid0vg0-raid0lv0_rimage_0: UUID="10092fa9-43f5-421e-a0a1-ca96323c6388" TYPE="ext4"
    /dev/mapper/raid0vg0-raid0lv0_rimage_1: UUID="10092fa9-43f5-421e-a0a1-ca96323c6388" TYPE="ext4"
    /dev/mapper/raid0vg0-raid0lv0: UUID="10092fa9-43f5-421e-a0a1-ca96323c6388" TYPE="ext4"
    ...

\"10092fa9-43f5-421e-a0a1-ca96323c6388\" is UUID of the ext4 filesystem on RAID 1.

Create mountpoint [/mnt/data]:

`root `[`#`]`mkdir /mnt/data`

Add an entry to [/etc/fstab]:

[FILE] **`/etc/fstab`**

    ...
    UUID=10092fa9-43f5-421e-a0a1-ca96323c6388  /mnt/data        ext4        defaults        0 2
    ...

## [][Ext4 Filesystem (encrypted with LUKS)]

** Important**\
Please, see [Full Disk Encryption From Scratch Simplified](https://wiki.gentoo.org/wiki/Full_Disk_Encryption_From_Scratch_Simplified "Full Disk Encryption From Scratch Simplified") --- a guide which covers the process of configuring a drive to be encrypted using LUKS and btrfs.

Create LUKS AES encrypted partition on top of logical volume *raid0lv0* in volume group *raid0vg0* (RAID 1):

`root `[`#`]`cryptsetup luksFormat -c aes-xts-plain64:sha256 -s 256 /dev/raid0vg0/raid0lv0`

Map encrypted LUKS partition as *raid0lv0encripted*:

`root `[`#`]`cryptsetup luksOpen /dev/raid0vg0/raid0lv0 raid0lv0encripted`

Create ext4 filesystem on LUKS partition:

`root `[`#`]`mkfs.ext4 /dev/mapped/raid0lv0encripted`

### [Mount LUKS encrypted device on boot from LVM RAID 1]

First, create directrory, that will contain keys for encrypting/decryption devices:

`root `[`#`]`mkdir /etc/keyfiles `

`root `[`#`]`chmod 0400 /etc/keyfiles `

Create 4k keyfile with name *main*:

`root `[`#`]`dd if=/dev/urandom of=/etc/keyfiles/main bs=1024 count=4`

`root `[`#`]`chmod 0400 /etc/keyfiles/main`

Add main keyfile to list of keys that can decrypt the disk (technically: add keyfile to LUKS slot)

`root `[`#`]`cryptsetup luksAddKey /dev/raid0vg0/raid0lv0 /etc/keyfiles/main`

Find UUID of LUKS device (should be same as logical volume raid0lv0)

`root `[`#`]`blkid`

    /dev/sdc1: UUID="OxJaqA-yMAP-sOjE-T5BR-H9Lp-rtPN-pl7rFC" TYPE="LVM2_member" PARTLABEL="raiddata1" PARTUUID="9c794e91-22a8-4b58-bedd-c3f656d82bd9"
    /dev/sdb1: UUID="gNcHvg-Rocv-pFFc-VzvF-49tX-D1d3-odSe2h" TYPE="LVM2_member" PARTLABEL="raiddata0" PARTUUID="70121885-4a45-4a2b-8d3e-49edd8fffd34"
    /dev/mapper/raid0vg0-raid0lv0_rimage_0: UUID="10092fa9-43f5-421e-a0a1-ca96323c6388" TYPE="ext4"
    /dev/mapper/raid0vg0-raid0lv0_rimage_1: UUID="10092fa9-43f5-421e-a0a1-ca96323c6388" TYPE="ext4"
    /dev/mapper/raid0vg0-raid0lv0: UUID="cd5740a1-b642-4359-a0b9-af84a8f01092" TYPE="crypto_LUKS"
    /dev/mapper/raid0lv0encripted: UUID="fc7ec587-35e4-4726-815d-e1693cd89b70" TYPE="ext4"

In this case it is **UUID=\"cd5740a1-b642-4359-a0b9-af84a8f01092\"**

Add to file /etc/conf.d/dmcrypt

[FILE] **`/etc/conf.d/dmcrypt`**

    target='raid0lv0encripted'
    source=UUID='cd5740a1-b642-4359-a0b9-af84a8f01092'
    key='/etc/keyfiles/main'

Add dmcrypt to be started at boot:

`root `[`#`]`rc-update add dmcrypt boot `

Create mountpoint [/mnt/data]:

`root `[`#`]`mkdir /mnt/data`

Find EXT4 filesystem UUID

`root `[`#`]`blkid`

    /dev/sdc1: UUID="OxJaqA-yMAP-sOjE-T5BR-H9Lp-rtPN-pl7rFC" TYPE="LVM2_member" PARTLABEL="raiddata1" PARTUUID="9c794e91-22a8-4b58-bedd-c3f656d82bd9"
    /dev/sdb1: UUID="gNcHvg-Rocv-pFFc-VzvF-49tX-D1d3-odSe2h" TYPE="LVM2_member" PARTLABEL="raiddata0" PARTUUID="70121885-4a45-4a2b-8d3e-49edd8fffd34"
    /dev/mapper/raid0vg0-raid0lv0_rimage_0: UUID="10092fa9-43f5-421e-a0a1-ca96323c6388" TYPE="ext4"
    /dev/mapper/raid0vg0-raid0lv0_rimage_1: UUID="10092fa9-43f5-421e-a0a1-ca96323c6388" TYPE="ext4"
    /dev/mapper/raid0vg0-raid0lv0: UUID="cd5740a1-b642-4359-a0b9-af84a8f01092" TYPE="crypto_LUKS"
    /dev/mapper/raid0lv0encripted: UUID="fc7ec587-35e4-4726-815d-e1693cd89b70" TYPE="ext4"

In our case it is **UUID=\"fc7ec587-35e4-4726-815d-e1693cd89b70\"**

Add an entry to [/etc/fstab]:

[FILE] **`/etc/fstab`**

    ...
    UUID=fc7ec587-35e4-4726-815d-e1693cd89b70  /mnt/data        ext4        defaults        0 2
    ...

## [Check LVM RAID 1 status]

To check LVM RAID status for volume group *raid0vg0*:

`root `[`#`]`lvs -a -o name,copy_percent,devices raid0vg0`

      LV                  Cpy%Sync Devices
      raid0lv0            100.00   raid0lv0_rimage_0(0),raid0lv0_rimage_1(0)
      [raid0lv0_rimage_0]          /dev/sdc1(1)
      [raid0lv0_rimage_1]          /dev/sdb1(1)
      [raid0lv0_rmeta_0]           /dev/sdc1(0)
      [raid0lv0_rmeta_1]           /dev/sdb1(0)

## [Performance tunnig]

By default, in RAID 1, all disk are used for reading and writing. If one of disks is much slower then the other, it possible to improve write performance (with a small penalty to read performance) by disabling reading from the slowest drive.

In such scenario, the slowest drive will only write data (without reading), while the faster drive will read/write data.

`root `[`#`]`lvchange --raidwritemostly /dev/sdb1 raid0vg0`

    Logical volume raid0vg0/raid0lv0 changed.

Where /dev/sdb1 is the physical volume in vg0 (slowest drive) and raid0vg0 is the volume group.

## [See also]

-   [LVM](https://wiki.gentoo.org/wiki/LVM "LVM") --- allows administrators to create meta devices that provide an abstraction layer between a file system and the physical storage that is used underneath.
-   [Full Disk Encryption From Scratch Simplified](https://wiki.gentoo.org/wiki/Full_Disk_Encryption_From_Scratch_Simplified "Full Disk Encryption From Scratch Simplified") --- a guide which covers the process of configuring a drive to be encrypted using LUKS and btrfs.

## [External resources]

-   [https://blog.programster.org/create-raid-with-lvm](https://blog.programster.org/create-raid-with-lvm) --- Another example of creating RAID 1 with LVM