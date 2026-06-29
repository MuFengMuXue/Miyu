[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Btrfs&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Btrfs "Btrfs (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Btrfs/tr "Btrfs (1% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Btrfs/ru "Btrfs (69% translated)")

## Contents

-   [[1] [Btrfs is a modern CoW file system]](#Btrfs_is_a_modern_CoW_file_system)
    -   [[1.1] [Familiar with btrfs-slang ?]](#Familiar_with_btrfs-slang_.3F)
-   [[2] [Volume management ⇒]](#Volume_management_.E2.87.92)
    -   [[2.1] [Extend a volume]](#Extend_a_volume)
    -   [[2.2] [Move a volume (to another disk)]](#Move_a_volume_.28to_another_disk.29)
    -   [[2.3] [Subvolume ⇒]](#Subvolume_.E2.87.92)
        -   [[2.3.1] [Subvolume **@**]](#Subvolume_.40)
        -   [[2.3.2] [Subvolume **\@home**]](#Subvolume_.40home)
        -   [[2.3.3] [Subvolume **\@snapshots**, **\@home.snapshots**]](#Subvolume_.40snapshots.2C_.40home.snapshots)
        -   [[2.3.4] [Subvolume **@\...**]](#Subvolume_.40...)
    -   [[2.4] [Snapshot]](#Snapshot)
        -   [[2.4.1] [Taking snapshots]](#Taking_snapshots)
        -   [[2.4.2] [Releasing snapshots]](#Releasing_snapshots)
        -   [[2.4.3] [Rollback to a snapshot]](#Rollback_to_a_snapshot)
-   [[3] [Btrfs RAID]](#Btrfs_RAID)
    -   [[3.1] [RAID 0 (not Just a Bunch of Disks)]](#RAID_0_.28not_Just_a_Bunch_of_Disks.29)
        -   [[3.1.1] [1 device]](#1_device)
        -   [[3.1.2] [2 or more devices]](#2_or_more_devices)
    -   [[3.2] [RAID 1 (mirrored), 1C3, 1C4]](#RAID_1_.28mirrored.29.2C_1C3.2C_1C4)
        -   [[3.2.1] [Automatic repair]](#Automatic_repair)
        -   [[3.2.2] [RAID 10 (automatic)]](#RAID_10_.28automatic.29)
    -   [[3.3] [RAID 5]](#RAID_5)
    -   [[3.4] [RAID 6]](#RAID_6)
-   [[4] [Btrfs maintenance]](#Btrfs_maintenance)
    -   [[4.1] [Fragmentation]](#Fragmentation)
        -   [[4.1.1] [Databases]](#Databases)
        -   [[4.1.2] [Logfiles]](#Logfiles)
    -   [[4.2] [Balance ⇒]](#Balance_.E2.87.92)
        -   [[4.2.1] [Filters]](#Filters)
        -   [[4.2.2] [Merging chunks]](#Merging_chunks)
        -   [[4.2.3] [After removing a device]](#After_removing_a_device)
        -   [[4.2.4] [After adding a device]](#After_adding_a_device)
        -   [[4.2.5] [After changing RAID-level]](#After_changing_RAID-level)
        -   [[4.2.6] [Metadata]](#Metadata)
    -   [[4.3] [Scrub ⇒]](#Scrub_.E2.87.92)
        -   [[4.3.1] [Check & repair on the fly]](#Check_.26_repair_on_the_fly)
        -   [[4.3.2] [Full check]](#Full_check)
-   [[5] [Solving Problems]](#Solving_Problems)
    -   [[5.1] [Out of space]](#Out_of_space)
        -   [[5.1.1] [Avoid to get out of space with btrfs!]](#Avoid_to_get_out_of_space_with_btrfs.21)
        -   [[5.1.2] [Get out of jail]](#Get_out_of_jail)
        -   [[5.1.3] [Stay out of jail]](#Stay_out_of_jail)
    -   [[5.2] [Corrupted checksums]](#Corrupted_checksums)
    -   [[5.3] [Tips]](#Tips)
        -   [[5.3.1] [Move a volume]](#Move_a_volume)
        -   [[5.3.2] [Resize a btrfs filesystem/device]](#Resize_a_btrfs_filesystem.2Fdevice)
            -   [[5.3.2.1] [shrink]](#shrink)
            -   [[5.3.2.2] [expand]](#expand)
        -   [[5.3.3] [Mount options]](#Mount_options)
-   [[6] [Btrfs options]](#Btrfs_options)
    -   [[6.1] [Compression ⇒]](#Compression_.E2.87.92)
    -   [[6.2] [Encryption]](#Encryption)
    -   [[6.3] [Send + receive = backup ⇒]](#Send_.2B_receive_.3D_backup_.E2.87.92)
    -   [[6.4] [Quota groups ⇒]](#Quota_groups_.E2.87.92)
    -   [[6.5] [Zoned mode ⇒]](#Zoned_mode_.E2.87.92)
-   [[7] [Btrfs Tools]](#Btrfs_Tools)
    -   [[7.1] [btrfs (the command) ⇒]](#btrfs_.28the_command.29_.E2.87.92)
        -   [[7.1.1] [help, version]](#help.2C_version)
        -   [[7.1.2] [device]](#device)
        -   [[7.1.3] [btrfs filesystem df /]](#btrfs_filesystem_df_.2F)
        -   [[7.1.4] [btrfs filesystem du]](#btrfs_filesystem_du)
        -   [[7.1.5] [btrfs filesystem show]](#btrfs_filesystem_show)
        -   [[7.1.6] [btrfs filesystem usage]](#btrfs_filesystem_usage)
        -   [[7.1.7] [btrfs scrub status]](#btrfs_scrub_status)
    -   [[7.2] [btrfsck]](#btrfsck)
    -   [[7.3] [Recomendations]](#Recomendations)
-   [[8] [Additional Information]](#Additional_Information)
    -   [[8.1] [Why not btrfs ?]](#Why_not_btrfs_.3F)
        -   [[8.1.1] [Not stable ?]](#Not_stable_.3F)
        -   [[8.1.2] [Experimental ?]](#Experimental_.3F)
        -   [[8.1.3] [Not usable for production ?]](#Not_usable_for_production_.3F)
        -   [[8.1.4] [Difficult to repair ?]](#Difficult_to_repair_.3F)
    -   [[8.2] [What\'s this \"Copy on Write\"]](#What.27s_this_.22Copy_on_Write.22)
        -   [[8.2.1] [Write in place (FAT32)]](#Write_in_place_.28FAT32.29)
        -   [[8.2.2] [Write to a metadata-log (Ext4)]](#Write_to_a_metadata-log_.28Ext4.29)
        -   [[8.2.3] [Copy on Write! (Btrfs)]](#Copy_on_Write.21_.28Btrfs.29)
            -   [[8.2.3.1] [Downsides]](#Downsides)
            -   [[8.2.3.2] [Advantages]](#Advantages)
-   [[9] [Use the Forum!]](#Use_the_Forum.21)
-   [[10] [Btrfs is fast moving! See Also:]](#Btrfs_is_fast_moving.21_See_Also:)

# [Btrfs is a modern CoW [file system](//wiki.manjaro.org/index.php?title=File_Systems "File Systems")]

A modern **C**opy **o**n **W**rite file system for Linux aimed at implementing advanced features while also focusing on **fault tolerance**, **repair** and **easy administration**. Btrfs not only is a file system, but also is partly a volume manager, software-raid, backup-tool, and it is flash-friendly.

Because Btrfs is different, some things seem unfamiliar and strange. If you want to learn the details and the newest stuff, then [btrfs.wiki.kernel.org](https://btrfs.wiki.kernel.org/index.php/Main_Page) is the place to go or [btrfs.readthedocs.io](https://btrfs.readthedocs.io/en/latest/index.html). Development of Btrfs started in 2007. Since that time, Btrfs is a part of the Linux kernel and is under active development. The Btrfs code base and filesystem-layout is **[stable](https://btrfs.wiki.kernel.org/index.php/Status) .** However, new features are still under development. Its main features and benefits are:

-   **Snapshots** which do not make a full copy of files
-   **Volume Manager** join partitions, split into subvolumes
-   **RAID** - support for software-based RAID 0, RAID 1, RAID 10
-   **Auto-repair** - checksums for data and metadata, automatic detection of silent data corruption

(see [btrfs@kernel.org](https://btrfs.wiki.kernel.org/index.php/Main_Page), [btrfs.readthedocs.io](https://btrfs.readthedocs.io/en/latest/), [Btrfs@ARC-wiki](https://wiki.archlinux.org/title/Btrfs), [Btrfs@wikipedia](https://de.wikipedia.org/wiki/Btrfs))

\

### [][Familiar with btrfs-slang ?]

Because Btrfs is different, you will find some words that do have a special meaning when used for btrfs. This may be a source of confusion.

▶ Btrfs **volume**

A **[volume](//wiki.manjaro.org/index.php?title=Btrfs#Btrfs_Volume "Btrfs")** is a pool of raw storage and consists of one or more **device**s. The size of the volume will be the addition of all devices that are part of this volume. In most cases you will only use **one** volume. You are able to add/remove devices at any time. *Usually you do **not** mount a Btrfs volume.*

▶ **chunk**

A **chunk** is simply a piece of storage that Btrfs can use to put data on. Think of a chunk (usually 1GiB) as of a page in a book. The book is the **[volume](//wiki.manjaro.org/index.php?title=Btrfs#Btrfs_Volume "Btrfs")**, and the chunk is one page of it. When you start, all pages are empty. When you write data to the volume, one page (=\"chunk\") after the other is written to.

▶ **device**

A **device** is some linux device. It may be **a partition** like **/dev/sdz1** or /dev/sdz2. Or it may be a raw disk device like /dev/sdz without any partitioning. A Btrfs **[volume](//wiki.manjaro.org/index.php?title=Btrfs#Btrfs_Volume "Btrfs")** consists of **at least one device**.

▶ **subvolume**

A Btrfs **[subvolume](//wiki.manjaro.org/index.php?title=Btrfs#subvolume "Btrfs")** is an independently mountable POSIX file-tree and **not a block device**. It is the part of a **[volume](//wiki.manjaro.org/index.php?title=Btrfs#Btrfs_Volume "Btrfs")** that will be **mounted writeable** into your Linux system. By convention the names of subvolumes start with @ (**@**, **\@home**, **\@snapshots** \...). All subvolumes share the space of the Btrfs volume. You may create subvolumes at will. (You may think of subvolumes *as sort of \"dynamic partitions\" inside a Btrfs volume*)

▶ **default subvolume**

The default subvolume of a Btrfs **[volume](//wiki.manjaro.org/index.php?title=Btrfs#Btrfs_Volume "Btrfs")** is special. When you mount, you normally have to name a **[subvolume](//wiki.manjaro.org/index.php?title=Btrfs#subvolume "Btrfs")** to mount. When you don\'t name a subvolume, the default subvolume will be used. The default subvolume can be changed to any subvolume. It is advisable to set that subvolume as default, that is used for mounting linux **\"/\"** this is often the subvolume with the name **\"@\"**

▶ Btrfs **volume-root** \"/\", Btrfs **layout**

A **[volume](//wiki.manjaro.org/index.php?title=Btrfs#Btrfs_Volume "Btrfs")** contains one ore more **[subvolumes](//wiki.manjaro.org/index.php?title=Btrfs#subvolume "Btrfs")**. But they are not stored in form of a simple list. These subvolumes are stored in a tree-like structure like in a filesystem. Sometimes called the \"top-level subvolume\" or \"root of the volume\". But be careful this is **not linux-root \"/\"**, but Btrfs **volume-root \"/\"**. There are several basic schemas to **layout** subvolumes in a volume

▶ **snapshot**

A **[snapshot](//wiki.manjaro.org/index.php?title=Btrfs#snapshot "Btrfs")** looks nearly the same as a **[subvolumes](//wiki.manjaro.org/index.php?title=Btrfs#subvolume "Btrfs")**. But don´t get confused. When we talk about snapshots we usually mean a \"**Read-Only (ro) photograph** of a subvolume\". While the subvolume changes with time. A snapshot stays in the state of the subvolume at the time we made it. You can mount snapshots into your linux system, but you only can read the content. And the content will never change while this snapshot exists. When creating **snapshots** you have to watch out for the Btrfs-**layout** in use.

It is possible to make a writeable(rw) subvolume out of a ro-snapshot. This is the way **[roll back](//wiki.manjaro.org/index.php?title=Btrfs#Rollback_to_a_snapshot "Btrfs")** does work. It is also possible to send a ro-snapshot to another btrfs volume as **[backup](//wiki.manjaro.org/index.php?title=Btrfs#Send_.2B_receive_.3D_backup_.E2.87.92 "Btrfs")**

▶ Self-healing

**This is no magic.** Because of the nature of Btrfs as **[CopyOnWrite](//wiki.manjaro.org/index.php?title=Btrfs#What.27s_this_.22Copy_on_Write.22 "Btrfs")** filesystem and because of the checksums, it is possible to check the filesystem and repair some errors. This does happen silently.

-   [Without RAID](//wiki.manjaro.org/index.php?title=Btrfs#RAID_0_.28not_Just_a_Bunch_of_Disks.29 "Btrfs") it is possible to correct some small faults that happen because of power outage. (This is done when the filesystem is mounted again)
-   [With RAID1](//wiki.manjaro.org/index.php?title=Btrfs#RAID_1_.28mirrored.29.2C_1C3.2C_1C4 "Btrfs") it is possible to repair some parts of files that where damaged by faults on one device. (This is done when the file is read the next time)

▶ **scrub**

A **[scrub](//wiki.manjaro.org/index.php?title=Btrfs#scrub "Btrfs")** is like an inspection of your car. The mechanic will look at all parts, and will tell you if something is amiss. If he finds very small problems, he will repair this automatically without asking for permission, and with minimal extra cost.

▶ **balance**

A **[balance](//wiki.manjaro.org/index.php?title=Btrfs#balance "Btrfs")** is like renovating your home. Sometimes it is necessary to renovate a room, sometimes you will renovate your home completely. But you don\'t do it once in every week ;-) With balance, the furniture will be transported around and rearranged. **You need to do this when changing RAID-levels.**

You may also have a look at [Btrfs Glossary](https://btrfs.readthedocs.io/en/latest/Glossary.html)

# [][Volume management [⇒](https://btrfs.readthedocs.io/en/latest/Volume-management.html)]

A volume is a pool of raw storage. Consists of one or more devices. The size of the volume will be the addition of all included devices, unless you use RAID.

If you do use more then one device, please also read the section about RAID. You are able to add/remove devices at any time to increase/decrease the size of the volume. With adding/removing devices it is also possible to move a volume from one device to another (without changing the UUID).

Usually you do not mount the Btrfs volume itself, but you mount subvolumes. There may be times when it is practical to mount the Btrfs volume-root itself. Then you are able to change the volume layout. All (writeable) subvolumes inside a volume are movable inside the volume with mv. Moving subvolumes will not touch the data, but change the volume layout in an instant.

When not otherwise specified, additional devices are handled as **J**ust a **B**unch **o**f **D**isks (JBOD)

**Tip**

------------------------------------------------------------------------

In most cases it is advisable to use **only one volume**

### [Extend a volume]

This is very easy because btrfs incorporates a volume manager. You only have to look for a free device. You may use a partition like */dev/sdz4* or you may use a raw device like */dev/sdz*. Then add this device to your existing volume with **btrfs device add**. You may need to do a **balance** afterwards to redistribute some chunks.

[root \# ][ btrfs device add \[/dev/sdz4\] / [COPY TO CLIPBOARD]]

\

**Dont´t format the partition!**

------------------------------------------------------------------------

To add a device it should have **NO filesystem** on it. The btrfs volume manager will include the free storage of the device **into the existing filesystem**.

### [][Move a volume (to another disk)]

There are a lot of ways you can move a \"normal\" filesystem from one disk to another. But there are dangers with moving btrfs volumes that do not exist with other filesystems! **Don´t ever move a btrfs volume with a tool that does not say it is 100% btrfs-proof.** When at any time there are 2 partitions in one computer that have the same filesystem UUID, one ore both filesystems **may be destroyed**. Under the topic **tips** you will find an easy way to do move a volume without any danger

**Do NOT**

------------------------------------------------------------------------

-   make a block-level copy of a Btrfs filesystem to another block device
-   use LVM snapshots, or any other kind of block level snapshots
-   turn a copy of a filesystem that is stored in a file into a block device with the loopback driver
-   try to mount either the original or the copy while both are visible to the same kernel

See why at [Block-level copies of devices@btrfs.wiki.kernel.org](https://btrfs.wiki.kernel.org/index.php/Gotchas)

**Tip: move a volume**

------------------------------------------------------------------------

There is an easy and secure way to move a volume to another disk/device. If you use Btrfs itself to move the volume, there will be no danger. You even can do this while the volume is in use. [See how to in \"tips\"](//wiki.manjaro.org/index.php?title=Btrfs#move_a_volume "Btrfs")

## [][Subvolume [⇒](https://btrfs.readthedocs.io/en/latest/Subvolumes.html)]

A subvolume is an independent mountable POSIX file-tree and **not a block device**. It is the part of a volume that will be **mounted writeable** into your Linux system. If you dont´t care about snapshots, and you don´t care about backups, it would be possible to use only one subvolume for everything. But then you would not be able to use the powers of Btrfs. *Lets assume you do care.*

All subvolumes share the space of the Btrfs volume. You may create subvolumes at will. (You may think of subvolumes as sort of \"dynamic partitions\" inside a Btrfs volume)

When making snapshots (or send/receive) every subvolume will be handled separately. For example when you have 2 subvolumes(@, \@home), and make a snapshot of one of them(@), this snapshot will contain every bit of data of all files in this subvolume(@), but none of the data from the other subvolume(@home). So if you make a few subvolumes, you are able to **follow different strategies for snapshots** of them. And you can **restore** each of them **separately**.

By convention the names of subvolumes start with **@ (@home, \@snapshots** \...).

\

### [][Subvolume **@**]

This is the subvolume where your **complete manjaro system** will reside. It is mounted at \"/\" in your filesystem. You may take snapshots of this subvolume to secure a running manjaro system. When something bad happens, you are able to rollback to one of the snapshots, (or to restore one of the external backups of a snapshot) **without changing your data** at /home.

\

**In order to make a rollback possible**

------------------------------------------------------------------------

The snapshot has to contain all and every data that is needed for your manjaro to work properly! This includes:

-   **config** of your bootloader (/boot/brub/grub.cfg)
-   **initramdisk** (/boot/initramfs-6.xx-x86_64.img)
-   **kernel** (/boot/vmlinuz-6.xx-x86_64)
-   **kernel-modules** (/usr/lib/modules/6.xx.xx-x-MANJARO/\*)
-   programs (/usr/bin/\*)
-   configs (/etc/\*)
-   libraries (/usr/lib/\*)
-   your root account (/root/\*)
-   rest of system files (/usr/\*)

### [][Subvolume **\@home**]

This is the subvolume where all **user data** ist stored. When you rollback your \"@\", this will not change at all. You may take snapshots of /home at a different rate and for different reasons. While snapshots of \"@\" are good for rollback, snapshots of \@home are good for **undeleting** accidentally by users deleted (or overwritten) files.

### [][Subvolume **\@snapshots**, **\@home.snapshots**]

It is wise to \"store\" snapshots **NOT inside** the subvolume they where taken from. So this may be the right place to store your snapshots of **@** or **\@home**.

### [][Subvolume **@\...**]

Sometimes it is desired to have other **special snapshot strategies** (or no snapshots at all) for some parts of the filesystem. If you need this, make another subvolume.

To have access to the root(/) of your volume, you need to mount this separately. (Please do not confuse this with \"/\" of the file system)

[root \# ][ mount -t btrfs -o subvol=/,defaults \[/dev/sdz2\] /mnt [COPY TO CLIPBOARD]]

\

Now you are able to create a new subvolume in a flat layout.

[root \# ][ btrfs subvolume create \[/mnt/@tests\] [COPY TO CLIPBOARD]]

\

This will be shown by

[root \# ][ ls -lA /mnt [COPY TO CLIPBOARD]]

\

[root \# ][ btrfs subvolume list /mnt [COPY TO CLIPBOARD]]

\

This subvolume **tests** is empty. And it is not mounted by default. So if you want to use it, you have to mount it by *fstab* or other means. **Now lets delete it again.**

[root \# ][ btrfs subvolume delete \[/mnt/@tests\] [COPY TO CLIPBOARD]]

\

[root \# ][ umount /mnt [COPY TO CLIPBOARD]]

\

## [Snapshot]

A snapshot looks nearly the same as a subvolume. But snapshots really are \"read-only photographs of a subvolume\". While the subvolume changes with time. The snapshot is frozen in the state of the subvolume at the time you made it. A snapshot is **read-only**. Therefore it is guaranteed not to change. In a snapshot you will find all files of the subvolume frozen in time. A snapshot is not a substitute for a backup!

**Where to place snapshots**

------------------------------------------------------------------------

When creating snapshots you have to watch out for the volume layout in use. [see@wiki.archlinux](https://github.com/jrabinow/snapper-rollback)

Snapshots (if regularly made) may be used for:

-   Comparing config files from different \"times\"
-   Merging config files
-   Recovering accidentally deleted/overwritten files
-   Rollback your system
-   Anchor for a backup with send/receive
-   Basis for a seed
-   *What do you use snapshots for ?*

Making and deleting snapshots is best done automatically:

-   snapper [snapper@wiki.archlinux](https://wiki.archlinux.org/title/snapper) [snapper@github](https://github.com/openSUSE/snapper) [snapper.io](http://snapper.io/)
-   timeshift [timeshift@wiki.archlinux](https://wiki.archlinux.org/title/Synchronization_and_backup_programs) [timeshift@github](https://github.com/teejee2008/timeshift)

### [Taking snapshots]

Taking a snapshot is **very fast**, and **nearly priceless**. After the snapshot is taken, all future writes will go as in CoW usual. But none of the space occupied by files in the snapshot will be reusable. As you write more and more new files, the filesystem will grow because it can not reuse the files in the snapshot. A new snapshot will freeze additionally all created or modified files since the last snapshot and so on. **If you don´t release**(delete) any snapshot **you will** eventually **run [out of space](//wiki.manjaro.org/index.php?title=Btrfs#Out_of_space "Btrfs")** soon.

### [Releasing snapshots]

Deleting a snapshot does not delete any files that are actually in use by other snapshots or the subvolume they where taken from. To free some space, Btrfs has to test for every file in the snapshot, whether it is in use, or it is not. If it is not, the space of this file/version will become free.(This is greatly simplified) Therefore it is **costly to remove snapshots**. And Btrfs will do this work in the background. You may notice this, because when you delete a snapshot there will be **no immediate gain in free space**. After a while you will notice that some space has become free.

It\'s best to delete snapshots using the tool that created them.

-   If you used Snapper to create them, delete them using Snapper.
-   If you used Timeshift to create them, delete them using Timeshift.
-   If you created them manually, delete them manually.

Don\'t forget to delete snapshots, or you\'ll soon run into **[out of space](//wiki.manjaro.org/index.php?title=Btrfs#Out_of_space "Btrfs") problems**. Btrfs needs free space (at least 5 GB) to do its work. If your volume is more than 90% full, you\'ll need to figure out what to do (quickly). Even a Manjaro update can be more than 10 GB in size, so you\'ll always need some free space.

-   ++++ **[Add](//wiki.manjaro.org/index.php?title=Btrfs#Extend_a_volume "Btrfs")** some partition/device to the volume
-   +++ **Remove** some snapshots you don\'t need (starting with the oldest one!)
-   ++ [Compress](//wiki.manjaro.org/index.php?title=Btrfs#Compression_.E2.87.92 "Btrfs") your volume
-   \+ **Delete** some files (This does only help if they are not part of **any** snapshot)

### [Rollback to a snapshot]

If you need to roll back into a snapshot you have to **replace** the actual subvolume by the chosen snapshot.

1.  **Make a snapshot(ro)** of the actual subvolume (for later reference)
2.  **Delete the subvolume** out of its actual place
3.  **Create a new subvolume(rw)** out of the snapshot chosen for rollback
4.  Make this new subvolume the default (optional)
5.  **Don\'t forget** to remove the snapshot you made in a few days

see in forum: [manual Rollback with btrfs](https://forum.manjaro.org/t/how-to-manual-rollback-with-btrfs/80230)

Please also have a look at [snapper-rollback@github](https://github.com/jrabinow/snapper-rollback) and at [snapshot-layout@wiki.archlinux](https://wiki.archlinux.org/title/Snapper#Suggested_filesystem_layout) for the suggested flat layout and the reasoning. ([Rollback example](https://forum.manjaro.org/t/how-to-manual-rollback-with-btrfs/80230) )

**Don\'t forget to delete snapshots before you run out of space**

------------------------------------------------------------------------

Each time you create a snapshot, you only use the **rest of the volume** to save all changes. Eventually, you\'ll need to free the snapshot. Don\'t overuse the space. Btrfs needs **breathing room.** Don\'t use more than **95%** and leave at least **5 GB free**, or you\'ll be in big trouble.

**NO Snapshots together with quotas**

------------------------------------------------------------------------

There are reports about massive problems when using **quotas** together with snapshots (snapper, timeshift). Please have a look at: [Known_issues@btrfs.kernel.org](https://btrfs.wiki.kernel.org/index.php/Quota_support#Known_issues)

# [Btrfs RAID]

With Btrfs you no longer need to use *mdadm* to create mirrored volumes or to create RAIDs. This is already included in btrfs, and very easy to use. There are even advanced features bult in:

-   Add devices to the volume This will integrate a device into the mounted volume

    :::
    [root \# ][ btrfs device add \[/dev/sdz7\] / [COPY TO CLIPBOARD]]
    :::

\

-   Remove devices from the volume. This will not delete any data, but remove the device from the volume. Bevorehand all data will be copied to the remaining devices of the volume.

    :::
    [root \# ][ btrfs device delete \[/dev/sdz8\] / [COPY TO CLIPBOARD]]
    :::

\

-   Use devices with different sizes in one volume
-   Switch the volume between RAID levels
-   Convert data to different RAID levels
-   Do this while the volume is mounted and being used

**Raid Levels**

------------------------------------------------------------------------

There's some similarity with traditional RAID levels, but this could be confusing to users familiar with the traditional meaning. Due to the similarity, the RAID terminology is widely used in the documentation (of btrfs). See [RAID@wikipedia](https://en.wikipedia.org/wiki/RAID),[RAID profiles@btrfs.readthedocs](https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html#profiles)

## [][[RAID 0](https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html#raid0) (not Just a Bunch of Disks)]

Using one or more devices to build a volume. This volume has the **capacity of all the used devices together(1+2+3+4\...)**. This is an very easy way to expand your volume when you need more space. You even can add 2 or 3 devices at a time. When you want to replace a device, you can add the new device, then remove the old device. Btrfs will move all data as necessary. *To distribute all data to all devices you may want to **balance** the volume.* Btrfs will stripe the data to all devices.

**If one device fails, everything is lost**

------------------------------------------------------------------------

Be aware that when one of the devices fails your complete volume may be lost if you use RAID 0

### [1 device]

In most setups you will start a volume with 1 device. If only one device is present, **metadata will be duplicated** on that device. Even with this simple setup you benefit from most features of Btrfs.

### [2 or more devices]

By default, **metadata will be mirrored** across two devices and **data will be striped** across all of the devices present. But if you have 2 or more devices in your volume you should consider using RAID 1.

## [][[RAID 1](https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html#raid1) (mirrored), [1C3](https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html#raid1c3), [1C4](https://btrfs.readthedocs.io/en/stable/mkfs.btrfs.html#man-mkfs-profiles)]

When using RAID 1 btrfs mirrors **data and metadata**. This way it is possible to repair data when one copy gets damaged. This could happen when one device fails, when power was lost while writing, \... **After enabling RAID1** all new data and metadata is automatically mirrored. To mirror your existing data and metadata, **you have to balance your complete volume**.

### [Automatic repair]

In order to preserve the integrity of the volume, Btrfs does separate CRC-checksums of metadata blocks and of data blocks. Every time a data block is read, the checksum is verified. When the checksum shows that the data is not good, Btrfs tries to get a good copy from the mirrored block. Then the bad block is written again with the good data from the mirrored block. This happens in background. The filesystem has been repaired, and this is logged into syslog.

With btrfs scrub, you can force btrfs to repair all corrupted blocks. This can take a long time because all blocks containing data must be read to verify the checksums.

### [][[RAID 10](https://btrfs.readthedocs.io/en/stable/mkfs.btrfs.html#man-mkfs-profiles) (automatic)]

When using enough devices(4\...) with RAID 1, Btrfs will distribute all data, so that it not only is mirrored but also striped.

**Bulletproof your system**

------------------------------------------------------------------------

If you have enough storage space and it is spread across 2 devices, it is really advisable to use btrfs RAID1/10. This will cover a whole range of risks that would be impossible to manage without RAID. At the same time, RAID in BTRFS is as straightforward as it gets.

## [RAID 5]

**Not save yet**

------------------------------------------------------------------------

This is not recommended [see Parity RAID@btrfs.wiki.kernel.org](https://btrfs.wiki.kernel.org/index.php/Gotchas)

## [RAID 6]

**Not save yet**

------------------------------------------------------------------------

This is not recommended [see Parity RAID@btrfs.wiki.kernel.org](https://btrfs.wiki.kernel.org/index.php/Gotchas)

# [Btrfs maintenance]

Btrfs needs maintenace like every filesystem. The more you use advanced features of btrfs, the more you have to watch for the right maintenance. Please also have a look at [Btrfs_Maintenance](//wiki.manjaro.org/index.php?title=Btrfs_Maintenance "Btrfs Maintenance")

### [Fragmentation]

Files on btrfs tend to get somewhat fragmented, when they are appended or changed often. If you use a mechanical disk with slow seeks, it may be advisable to defragment some heavy used files from time to time (like once in a month).

When the files are only written to, or are only read seldom, **don\'t worry**.

#### [Databases]

It may be good to defragment a database if there is a *noticeable* slowdown when using it.

#### [Logfiles]

It may be good to defragment a logfile, if there is a *noticeable* slowdown when booting your system.

## [][Balance [⇒](https://btrfs.readthedocs.io/en/latest/Balance.html)]

When adding devices or changing the RAID-level of your volume, it may be necessary to balance your volume. While balancing, btrfs will read ALL (or a subset of all) **chunks** in, and write them out again using the actual RAID-level. It will stripe these files over all available devices equally. While this happens, the volume will keep being usable, but you may see some **heavy load** on it. Also **this may take a very long time** because **ALL data must be** read AND **written** again. Don´t worry about shutdown. When you shutdown your computer while the balance is running, the balance will pause. After you restart the computer the balance will restart and continue until it is finished.

**Possible bug when using a swap file:**

------------------------------------------------------------------------

Never use a full-balance on a machine with a swapfile, since it will ignore +C Attributes. You may also have a look at [\[1\]](https://forum.manjaro.org/t/howto-enable-and-configure-hibernation-with-btrfs/51253/36)

### [Filters]

Because a complete balance may take **a long time**, there is the possibility of filters in balance. When using a filter only those chunks will be balanced, that are named by the filter.

-   **balance** all chunks that are less than 50% full. This **will** take some time !

[root \# ][ btrfs balance start -dusage=50 / [COPY TO CLIPBOARD]]

\

-   **balance** all chunks that are less than 90% full. This **will** take some time !

[root \# ][ btrfs balance start -dusage=90 / [COPY TO CLIPBOARD]]

\

**Don\'t use filters higher than 95%**

------------------------------------------------------------------------

This is unnecessary on an SSD drive. On a hard drive, this will put a lot of strain on the disk. Even with today\'s hard drives (\>2TB), it may take a very long time. (e.g. 24 hours or more)

### [Merging chunks]

As you use your volume, you will be creating some files, deleting some, modifying some. Then some parts of the chunks are empty. But this is not a coherent space that can be easily reused. Usually this is not a problem for btrfs and will be cleaned up automatically over time. However, if space is scarce (\> 85% full), it is advisable to merge free areas together. This can be done by using balance with a filter.

### [After removing a device]

When you remove a device from a volume, btrfs will automatically balance all \"chunks\" that where on the removed device. These chunks are placed on another device of the volume. So you don\'t need to balance by yourself after removing a device.

### [After adding a device]

When you add a device there will be no automatic balance. Only when further using the volume, btrfs will use the additional free space according to the actual RAID-level.

### [After changing RAID-level]

When you changed RAID-levels (for example from RAID 0 to RAID 1) there is no automatic duplication of the chunks. Only when writing further, btrfs will respect the changed RAID-level. This may not be what you intended. To complete the conversion to another RAID-level you need to tell btrfs to rewrite chunks where needed. You do this with a manual balance:

### [Metadata]

It is rarely recommended to include blocks with metadata in a balance. It is advantageous, in exceptional cases, if the following conditions are currently met: You can check with:

[root \# ][ sudo btrfs fi us / [COPY TO CLIPBOARD]]

\

`Metadata,RAID1: Size:9.00GiB, Used:6.58GiB (73.09%)`

-   Several GB of metadata are present in your filesystem (*6.6 GB present, 9 GB used*)
-   This metadata is poorly distributed (*73%*)
-   Significantly more than one full GB could become free (9 GB - 6.6 GB ==\> *2.4 GB could become free*)

The command is then:

[root \# ][ btrfs balance start -musage=95 / [COPY TO CLIPBOARD]]

\

Btrfs had to move 9 GB of metadata to free up 1 GB ! `Metadata,RAID1: Size:8.00GiB, Used:6.58GiB (82.20%)`

\
see: [btrfs filesystem balance](https://btrfs.readthedocs.io/en/latest/Balance.html)

## [][Scrub [⇒](https://btrfs.readthedocs.io/en/latest/Scrub.html)]

A scrub of a btrfs volume is like inspecting your home. Does the light work in every room? Is the battery of a smoke alarm empty? Does the fire extinguisher need to be replaced? Is any faucet dripping? Every now and then it is advisable to look for such things. And fix it right away!

#### [][Check & repair on the fly]

Every time btrfs reads a file, it checks the corresponding checksums. When btrfs is in RAID 0 and detects a \'damaged\' file, it only can tell you that the file is damaged. You may delete it, or replace it from your backup. When running in RAID 1 btrfs has 2 copies of every file. So if one file seems to be damaged, btrfs will read the other copy. If this other copy is ok, btrfs will automatically create another good copy of the file, and then afterwards delete the defect copy. You won\'t even notice this \'**automatic\' repair.**

#### [Full check]

Sometimes you may want to check ALL files, and to get a report of defects, because:

-   Some files are read very seldom, and you don\'t want \"bitrott\"
-   You want to check your data completely for any faults
-   Once in a while you want to make sure all is well
-   You want to force your disk/device to verify all data
-   \...

This is when you use btrfs scrub. Scrub will read ALL data of your complete volume. While this is done, all files and metadata will be checked by the checksums and all problems will be reportet. Because this will read and verify your complete volume (eventually a few Terra-byte), it may take some time. Scrub will not waste time in checking unused chunks. While checking you can enable automatic repair for RAID 1 or disable it. If you disable automatic repair, scrub will work completely readonly, and will change nothing on your volume.

Scrub can be done automatically (for example every month), or manually.

\

**Notice**

------------------------------------------------------------------------

Be aware, that Scrub does not structurally check the filesystem, but only checksums data and tree blocks. You may also have a look at [tree checker](https://btrfs.readthedocs.io/en/latest/Tree-checker.html)

A manual scrub is done by:

[root \# ][ btrfs scrub start -Bd / [COPY TO CLIPBOARD]]

\

# [Solving Problems]

## [Out of space]

#### [][Avoid to get out of space with btrfs!]

Don\'t skimp on storage space when creating a Btrfs volume. A Btrfs volume should normally be less than 90% full. Then it\'s recommended to adjust the volume. In an emergency, 95% (plus at least 5 GB free) is fine. However, this isn\'t beneficial for neither the Btrfs volume nor an SSD.

**Don\'t forget to include the snapshots in the bill**

------------------------------------------------------------------------

Manjaro is a rolling release distribution. There will be a lot of changes over time.

**Tip: Check how close you are to \"out of space\".**

------------------------------------------------------------------------

Look at **Device unallocated:** (not at *Free (estimated):*) [1](https://forum.manjaro.org/t/could-not-boot-due-to-brfs-no-space-condition-how-should-i-keep-using-btrfs/92922/7)

[root \# ][ btrfs filesystem usage / [COPY TO CLIPBOARD]]

\

### [Get out of jail]

This said, there is an **easy way out**: Give btrfs more space ;-)

-   **add a (unformatted) partition** (for example a fast extern USB-Stick with 8GB) to the btrfs-volume with

    :::
    [root \# ][ btrfs device add /dev/\[sdz4\] / [COPY TO CLIPBOARD]]
    :::

\

**Do NOT remove this USB-Stick**

------------------------------------------------------------------------

From now on this partition belongs to your volume! **Do not boot without it**. If possible do not reboot at all in this stage! This USB-stick has to stay until **btrfs device remove** has **completed**.

-   look for old snapshots you don´t need, remove them **now** (starting with the oldest one)
-   **or delete some files** you do not need
-   Do this until your disk will be not more then 95% full (plus 5 GB free space)

Do not get confused if btrfs does not immediately display the vacant space. After the next step (balance) it will become visible.

-   **balance** your volume with a filter(50%) This **will** take some time !

    :::
    [root \# ][ btrfs balance start -dusage=50 / [COPY TO CLIPBOARD]]
    :::

\

**Tip: Want to watch the volume clean up ?**

------------------------------------------------------------------------

[user \$ ][ pamac install procps-ng [COPY TO CLIPBOARD]]

\

------------------------------------------------------------------------

After that inside a terminal:

[root \# ][ watch -n 60 btrfs filesystem usage -h / [COPY TO CLIPBOARD]]

\

-   If neccesary **balance** your volume with a filter(90-95 %) This **will** take some more time !

    :::
    [root \# ][ btrfs balance start -dusage=95 / [COPY TO CLIPBOARD]]
    :::

\

-   **remove the added partition** from the volume with

    :::
    [root \# ][ btrfs device remove /dev/\[sdz4\] / [COPY TO CLIPBOARD]]
    :::

\

-   This **will** take some time ! **Do not reboot until this step is complete**.
-   After \"btrfs remove\" has finished successfully, you can remove the USB stick.

### [Stay out of jail]

-   Think about how to extend the btrfs volume to **double size**
-   seek if there is a program filling your disk
-   look for snapshots !
-   don't forget to remove old snapshots (best done automatically)
-   [use compression](//wiki.manjaro.org/index.php?title=Btrfs#Compression_.E2.87.92 "Btrfs") on this volume

## [Corrupted checksums]

    [ 9364.354241] BTRFS error (device nvme0n1p3): block=58469742080 write time tree block corruption detected

This ERROR or similar may lead to Messages like:

    Configuration file "/home/user/.config/dolphinrc" not writable. Please contact your system administrator.

because btrfs does mount this partition **readonly** when it detects corrupted blocks.

Now you have to investigate WHY a checksum of a btrfs block says it is corrupted.

-   In some cases the underlying device may beginn to fail ! =\> replace it (consider using RAID10)
-   In other cases a corruption may have happened even before the block had been written to disk
    -   corruption in RAM
    -   some software-bug ???
    -   ssd gone bad ??? [example](https://forum.manjaro.org/t/update-ended-in-readonly-filesystem/154442/34)

[What the Btrfs developers say:](https://btrfs.readthedocs.io/en/latest/Hardware.html) If you use unreliable hardware and don't know about that, don't blame the filesystem when it tells you.

Also see: [Tree-ckecker](https://btrfs.readthedocs.io/en/latest/Tree-checker.html)

## [Tips]

### [Move a volume]

There is an **easy and secure way** to move a volume to another disk/device. If you use Btrfs itself to move the volume, there will be no danger. You even can do this **while the volume is in use**.

-   Create the partition you want to use as *destination* **without formatting** it. Or remove the filesystem when one is present
-   Add the *destination* device to your volume by

    :::
    [root \# ][ btrfs device add /dev/\[destination\] \[path to filesystem\] [COPY TO CLIPBOARD]]
    :::

\

-   Remove the *source* device from your volume by

    :::
    [root \# ][ btrfs device remove /dev/\[source\] \[path to filesystem\] [COPY TO CLIPBOARD]]
    :::

\

Btrfs will notice, that it is necessary for this setup to move all data from the source device to the destination device. And it will start immediately to move data in the background. Meanwhile you can use your PC as you want.

-   Empty Blocks will not be moved
-   Compressed data will remain compressed
-   All Snapshots will remain
-   **The UUID of the filesystem will remain the same**, but btrfs will be aware of this
-   If you used the UUID to identify your volume, you even wont´t need to edit **/boot/grub/grub.cfg** and **/etc/fstab**
-   Only, **don\'t shutdown while the move of the volume is not complete**.

If you want to watch the volume move, inside a terminal:

[user \$ ][ pamac install procps-ng [COPY TO CLIPBOARD]]

\

[root \# ][ watch -n 60 btrfs filesystem show / [COPY TO CLIPBOARD]]

\

### [][Resize a btrfs filesystem/device]

When you resize a file system, you also need to resize the partition (device) it resides on. You cannot resize a mounted partition using **gparted**! So you need to unmount it beforehand or use a live manjaro from USB to resize the partition and file system.

When resizing existing file systems, it is strongly advisable to have current backups. However, resizing is possible without any problems when using **gparted**.

#### [shrink]

What you need to understand is that you can only safely shrink a file system if it is *not too full*. Shrinking a file system can take a **long time** because BTRFS may need to move data that was in the area to be freed to the remaining area.

Using **gparted** you can safely shrink a BTRFS file system. All necessary steps are taken such as:

-   Mount file system
-   Shrink file system
-   Unmount file system
-   Shrink partition

see@ [https://forum.manjaro.org/t/howto-resize-a-btrfs-filesystem/152999](https://forum.manjaro.org/t/howto-resize-a-btrfs-filesystem/152999)

#### [expand]

A BTRFS file system can also be safely expanded with **gparted**. All necessary steps are taken such as:

-   Extend partition
-   Mount file system
-   Expand file system
-   Unmount file system

### [Mount options]

The default mount settings chosen by btrfs are really optimal in most cases! There are only a few options to think about. Current and accurate information can also be found at: [https://btrfs.readthedocs.io/en/latest/Administration.html](https://btrfs.readthedocs.io/en/latest/Administration.html)

**,noatime**

------------------------------------------------------------------------

Under read intensive work-loads, specifying noatime significantly improves performance because no new access time information needs to be written. Default is *relatime*. ( ***,lazytime* [may not help, however](https://github.com/kdave/btrfs-progs/issues/377)**)

**,compress=zstd:7**

------------------------------------------------------------------------

Enables automatic and transparent compression. If compression is enabled, *nodatacow* and *nodatasum* are disabled. The compression level is adjustable, with higher levels trading off speed and memory for higher compression rates. ZLIB accepts the range \[1, 9\] and ZSTD accepts \[1, 15\]. **Default is 3** each

-   *,ssd* (**automatic !)**
-   *,discard* (**automatic !)**
-   *,space_cache* (**automatic !)**

You can always test what btrfs uses with:

[user \$ ][ mount -t btrfs [COPY TO CLIPBOARD]]

\

# [Btrfs options]

## [][Compression [⇒](https://btrfs.readthedocs.io/en/latest/Compression.html)]

You can turn on compression at any time by changing the mount options in the fstab. After the next reboot, all newly written data from then on will be automatically compressed. Compression factors of 2:1 on average are not uncommon. [\@see mount-options](//wiki.manjaro.org/index.php?title=Btrfs#Mount_options "Btrfs")

    UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx / btrfs rw,noatime,compress=zstd,subvol=@ 0 0

  -------- ---------------- ----------------
  CPU      rotating disk    SSD
  slow     zstd:1 \... 4    zstd:1 \... 3
  medium   zstd:4 \... 7    zstd:3 \... 5
  fast     zstd:7 \... 10   zstd:5 \... 10
  -------- ---------------- ----------------

  : Which compression suits me best?

Compression can only be set **per volume**. So if you set different \"levels\" of compression for different mounts in the fstab, only the first \"level\" will be applied. [see@btrfs.readthedocs.io](https://btrfs.readthedocs.io/en/latest/Compression.html#how-to-enable-compression)

**Grub needs to load the kernel and initrd**

------------------------------------------------------------------------

When you use compression on kernel, initrd, or grub config files, **grub** needs to decompress these files. Otherwise you will **not be able to boot**. GRUB introduced **zstd** support in **2.04.** Maybe you need to update grub **and** reinstall it

## [Encryption]

May be in the future.

## [][Send + receive = backup [⇒](https://btrfs.readthedocs.io/en/latest/Send-receive.html)]

Some wiki-posts in the forum:

-   [move a subvolume to another volume](https://forum.manjaro.org/t/howto-copy-move-a-subvolume-from-one-partition-to-another/135166)
-   [backup snapshots](https://forum.manjaro.org/t/howto-use-btrfs-send-receive/135808)

## [][Quota groups [⇒](https://btrfs.readthedocs.io/en/latest/Qgroups.html)]

Quota support in Btrfs is implemented at the subvolume level.

For more info see [Quota_support@btrfs.kernel.org](https://btrfs.wiki.kernel.org/index.php/Quota_support)

**Reports about problems**

------------------------------------------------------------------------

There are reports about massive problems when using quotas (especially together with snapshots, snapper, timeshift). Please have a look at: [Known_issues@btrfs.kernel.org](https://btrfs.wiki.kernel.org/index.php/Quota_support#Known_issues)

-   [freeze-issues-with-btrfs-and-timeshift 2021](https://forum.manjaro.org/t/freeze-issues-with-btrfs-and-timeshift/22005/10)
-   [cannot-clone-btrfs-boot-drive-with-clonezilla 2021](https://forum.manjaro.org/t/cannot-clone-btrfs-boot-drive-with-clonezilla/78836/10)
-   [btrfs-qgroups-warning-error 2021](https://forum.manjaro.org/t/btrfs-qgroups-warning-error/64029)
-   [files-disappearing-in-btrfs-and-ssd 2020](https://forum.manjaro.org/t/files-disappearing-in-btrfs-and-ssd/28991)

## [][Zoned mode [⇒](https://btrfs.readthedocs.io/en/latest/Zoned-mode.html)]

Beginning with version 5.12

# [Btrfs Tools]

For complete info an all tools for btrfs please do an actual search at the arch wiki and at the manjaro forum for \"btrfs\". In the following section only a few commands are described. Especially those commands that are often misinterpreted. Commands described earlier are omitted.

## [][btrfs (the command) [⇒](https://btrfs.readthedocs.io/en/latest/man-index.html)]

Be aware that some sub-commands of btrfs will not work as normal user. Other sub-commands do work but will give only partial info. So best use them as *root* or with *sudo*.

#### [][help, version]

**help** together with **man btrfs** or **info btrfs** will get you an overview over the usable options on your install.

[user \$ ][ btrfs help [COPY TO CLIPBOARD]]

\
With the **version** of btrfs given here you can look at [changelog](https://btrfs.wiki.kernel.org/index.php/Changelog).

[user \$ ][ btrfs version [COPY TO CLIPBOARD]]

\

#### [device]

**scan** will give no visible results 😜

[root \# ][ btrfs device scan [COPY TO CLIPBOARD]]

\

**stats** will give a list of errors detected in the past. This all should be 0, or you may be in trouble.

[root \# ][ btrfs device stats / [COPY TO CLIPBOARD]]

\

What to look for in device **usage**:

-   RAID-level of Data, Metadata and System
-   Unalocated:

Don\'t ever let *Unalocated:* get below 5% of your volume (or double the size you need for your next update)! If this goes too low, you will get into \"out of space\" trouble

[root \# ][ btrfs device usage / [COPY TO CLIPBOARD]]

\

Without sudo this will give very wrong results for everything displayed. **Dont´t use this without sudo !**

\

### [][btrfs filesystem df /]

### [btrfs filesystem du]

Here the full scope of btrfs\' difference becomes visible. When btrfs takes snapshots, many files are contained unchanged in several snapshots, but only take up space in the file system once. At the same time, there can be the same(!) file with different content and size in different snapshots.

It is therefore not enough to simply add up the size of all files in a path to determine the **space consumption** in the file system.

For each file, it must be determined how large it is and whether all or part of it is shared with other subvolumes. Since btrfs has to read a lot of metadata for this, it can take a **long time** to display the results:

[root \# ][ btrfs filesystem du -s /home [COPY TO CLIPBOARD]]

\

        Total   Exclusive  Set shared  Filename
      8.11TiB     6.23GiB   215.76GiB  /home

**Total**

------------------------------------------------------------------------

The sum of all files, as \"du\" would display them in a conventional file system. This is how much space a conventional file system would use to store these files (and all the necessary copies).

**Exclusive**

------------------------------------------------------------------------

The sum of the files that \"only\" occur in one of the subvolumes and are not shared with other subvolumes

**Set shared**

------------------------------------------------------------------------

The sum of files shared with other subvolumes

**Exclusive + Set shared**

------------------------------------------------------------------------

This is the actual space used in the file system

### [btrfs filesystem show]

### [btrfs filesystem usage]

### [btrfs scrub status]

## [btrfsck]

This is not what you may think it is 😜

## [Recomendations]

  ----------- -------------------------------------------------------------------------------------------------- ------------------------------ ---------------------------
  Partition   Filesystem                                                                                         Size                           Partition type
  /dev/sda1   Fat32                                                                                              1GiB                           EFI system partition
  /dev/sda2   Btrfs                                                                                              1Gib - 8EiB                    Btrfs Volume
  /dev/sda3   swap [⇒](https://btrfs.readthedocs.io/en/latest/Subvolumes.html)   4GiB, at least your RAM-size   Swap partition (optional)
  ----------- -------------------------------------------------------------------------------------------------- ------------------------------ ---------------------------

  : We recommend using Btrfs with UEFI and GPT

  ----------- -------------------------------------------------------------------------------------------------- ------------------------------ ---------------------------
  Partition   Filesystem                                                                                         Size                           Partition type
  /dev/sda1   (bootloader)                                                                                       4MiB                           BIOS boot partition
  /dev/sda2   Btrfs                                                                                              1Gib - 8EiB                    Btrfs Volume
  /dev/sda3   swap [⇒](https://btrfs.readthedocs.io/en/latest/Subvolumes.html)   4GiB, at least your RAM-size   Swap partition (optional)
  ----------- -------------------------------------------------------------------------------------------------- ------------------------------ ---------------------------

  : IF you don\'t have UEFI, you may use Btrfs with BIOS and GPT

\
[Please be aware that the information on this page is a simplified version of the reality. Is is written to make the reader understand a little of these complex things. To get an in depth understanding it will be neccesary to read further at btrfs.wiki.kernel.org or other places.]

# [Additional Information]

### [][Why not btrfs ?]

A lot of people say: \"**I don\'t use btrfs because** it is experimental and is **not stable**. You can´t use it in production. It is not safe!\".

#### [][Not stable ?]

The status of btrfs was experimental for a long time, but the core functionality is considered **good enough for daily use**. [(from kernel.org)]

If you see statements declaring Btrfs as not stable, please look for the date of them. Some seem to date from 10 years ago. So if you want to give Btrfs a chance, you have to look for newer statements. Maybe even look at [Btrfs Kernel Wiki](https://btrfs.wiki.kernel.org) as that sure is the best information regarding Btrfs

#### [][Experimental ?]

Btrfs is feature-rich! There are new features being implemented and these should be considered experimental for a few releases when the bugs get ironed out when number of brave users help stabilizing it.[(from kernel.org)]

Some features are **not implemented yet**. Others are only **partly implemented**. Some are **experimental** and not suggested for production use. As is always the case in Linux-land *you* decide what to use, and so you are responsible for your own decisions.

#### [][Not usable for production ?]

-   [Distro support](https://btrfs.wiki.kernel.org/index.php/Getting_started#Distro_support) for Btrfs as main filesystem
-   Some companies do use Btrfs in production@wiki.btrfs.kernel.org
-   Some manufacturers do deploy devices where Btrfs is installed by default.

#### [][Difficult to repair ?]

Indeed, when you search for the usual ways to repair a file system like FAT or Ext4 then you don\'t find good information about repairing btrfs. This is not because it is difficult to repair Btrfs, but because repairing Btrfs **does work very differently**.

## [][What\'s this \"Copy on Write\"]

When you want to get the most out of using Btrfs you do need to know some things about this file system. Then you are able to use it properly and to your advantage. Btrfs is not difficult, but different to some extend.

### [][Write in place (FAT32)]

Most older file systems do write \"in place\". This means that some data or metadata will be written \"over\" the previous data at the same place.

For example this is the case for FAT32 file systems. The **F**ile **A**llocation **T**able is at a fixed place on this file system. When the \"FAT\" changes (because a file got bigger and needs more blocks), this new FAT must be written with the new data to the same place as before. When the disk is ejected before (or while) this data is written, the file system will be corrupted. And the FAT does change a lot.

The danger of corruption is especially big while metadata (like filename, permission, usage of disk space \...) is being written.

### [][Write to a metadata-log (Ext4)]

There is a solution to this with newer file systems like Ext4. Instead of writing metadata \"in place\", metadata is written into an \"endless\" log. Then it is not possible to be corrupted while overwritten. This is possible because metadata is only a very small part of the data in a file system.

There has to be an additional mechanism to make this safe. Sometimes this is called \"barriers\", and there have to be checksums that tell when a part of the log is corrupted.

This does protect the file system itself, but not the files in it. Because a file may be overwritten in place, and then the old file is lost, and the new one may not have been written completely.

### [][Copy on Write! (Btrfs)]

Copy on Write is a \"new\" concept. It means the file system will try to **never** write over existing data. **How is this even possible?**

-   Files are appended at the end of a \"data page\"
-   Metadata is appended at a \"metadata page\"
-   Inside a page **nothing is ever overwritten**
-   When a page is full the file system will use the next free page
-   Deleting a file does not write/clean its data, but writes metadata, that marks this file as deleted
-   Overwriting a file does first append the new file to the actual \"data page\", then appends the metadata for this file to the \"metadata page\".
-   Changing small parts of a file will write only the new parts, then *link* the rest to the old file
-   there are checksums for data and metadata

#### [Downsides]

-   Management of space is complex
-   There are 2 sorts of pages (data / metadata)
-   There has to be a clean-up-process who makes the space of deleted files reusable, so that the disk does not run out of free pages
-   It must be avoided to write data unnecessarily, because then the clean-up would also be very expensive

#### [Advantages]

-   It is possible to **detect** nearly any **corruption** because of the checksums
-   When the power is lost, or the disk is disconnected, all old data is save. WHY?
    -   Every bit of \"old\" data from before the power loss or the disconnection is present because it is **NOT overwritten**
    -   Only the newly written data may be partly damaged
    -   The metadata may also be partly damaged
    -   When mounting the volume it is possible by analyzing checksums and metadata to find the point in the filesystem where all was good
    -   Btrfs will **automatically roll back** to this point, then it can mount the file system writable

<!-- -->

-   CoW is a sound foundation to build upon
    -   Snapshots
    -   RAID
    -   Volume management
    -   Compression
    -   Encryption (maybe some time in the future)

\

**Don´t disable CoW in Btrfs**

------------------------------------------------------------------------

It is possible to disable CoW in Btrfs. But then you **loose all benefits** of Btrfs. It won´t even make checksums. If you don\'t like CoW, then you better use another filesystem

# [][Use the Forum!]

It is a good Idea to [search the forum](https://forum.manjaro.org/search?q=btrfs) for posts related to btrfs.

# [][Btrfs is fast moving! See Also:]

-   [btrfs.readthedocs.io](https://btrfs.readthedocs.io/en/latest/index.html)
-   [btrfs@ARCH-wiki](https://wiki.archlinux.org/title/btrfs)