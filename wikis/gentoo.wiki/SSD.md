**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Solid-state_drive "wikipedia:Solid-state drive")

This article provides guidelines for basic maintenance, such as enabling discard/trim support, for **SSD**s ([Solid State Drives](https://en.wikipedia.org/wiki/Solid-state_drive "wikipedia:Solid-state drive")) on Linux. It presumes the user has a basic understanding of partitioning and formatting disk drives.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Dealing with empty blocks]](#Dealing_with_empty_blocks)
    -   [[1.2] [Slowing wear out]](#Slowing_wear_out)
-   [[2] [Considerations]](#Considerations)
    -   [[2.1] [Discard (trim) support]](#Discard_.28trim.29_support)
-   [[3] [Initial setup]](#Initial_setup)
    -   [[3.1] [Partitioning]](#Partitioning)
        -   [[3.1.1] [blkdiscard]](#blkdiscard)
        -   [[3.1.2] [LVM]](#LVM)
        -   [[3.1.3] [LUKS]](#LUKS)
            -   [[3.1.3.1] [LUKS1]](#LUKS1)
    -   [[3.2] [Formatting]](#Formatting)
        -   [[3.2.1] [Configuring for erase block size]](#Configuring_for_erase_block_size)
            -   [[3.2.1.1] [List of devices with known erase block sizes]](#List_of_devices_with_known_erase_block_sizes)
    -   [[3.3] [Mounting]](#Mounting)
-   [[4] [Additional configuration]](#Additional_configuration)
    -   [[4.1] [Periodic fstrim jobs]](#Periodic_fstrim_jobs)
        -   [[4.1.1] [cron]](#cron)
        -   [[4.1.2] [SSDcronTRIM]](#SSDcronTRIM)
        -   [[4.1.3] [SSDcronTRIM-LUKS]](#SSDcronTRIM-LUKS)
        -   [[4.1.4] [systemd timer]](#systemd_timer)
        -   [[4.1.5] [Without cron, on system shutdown (with OpenRC)]](#Without_cron.2C_on_system_shutdown_.28with_OpenRC.29)
    -   [[4.2] [Reducing amount of writes]](#Reducing_amount_of_writes)
        -   [[4.2.1] [Portage TMPDIR on tmpfs]](#Portage_TMPDIR_on_tmpfs)
        -   [[4.2.2] [Temporal files on tmpfs]](#Temporal_files_on_tmpfs)
        -   [[4.2.3] [XDG cache on tmpfs]](#XDG_cache_on_tmpfs)
        -   [[4.2.4] [Web browser profile(s) and cache on tmpfs]](#Web_browser_profile.28s.29_and_cache_on_tmpfs)
            -   [[4.2.4.1] [systemd]](#systemd)
            -   [[4.2.4.2] [OpenRC]](#OpenRC)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Introduction]

The term Solid State Drive is commonly used for flash-based block devices. Compared to conventional [HDD](https://wiki.gentoo.org/wiki/HDD "HDD"), flash-based technology offers a much faster access time, lower latency, silent operation, power savings (no moving parts), and more. However, the flash-based technology brings a few issues which require some special system attention and care.

### [Dealing with empty blocks]

Generally, traditional [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") do not erase deleted data blocks but only flags them as such. Due to nature of flash memory cells any write operation has to be done to empty cells only. Thus writing to physically non-empty cells, flagged as deleted by a filesystem, requires their erasure which makes the operation slower than writing to empty cells. This problem is further amplified by hardware limitations. Futhermore, the data still remains on the storage media, even when it is flagged as deleted, which is a non-issue on conventional storage media such as HDD. On SDD on the other hand, storing unused (deleted) data severely limits the availability of empty cells.

For modern [kernels](https://wiki.gentoo.org/wiki/Kernel "Kernel") it is possible to hint the deleted (not-used) data blocks to SSD. The described mechanism is called **discard**. Names of implementations differ --- **TRIM** for [ATAPI](https://en.wikipedia.org/wiki/ATA_Packet_Interface "wikipedia:ATA Packet Interface"), **UNMAP** for [SCSI](https://en.wikipedia.org/wiki/SCSI "wikipedia:SCSI"), **Deallocate** for [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe"); [MMC](https://en.wikipedia.org/wiki/MultiMediaCard "wikipedia:MultiMediaCard") and [SD cards](https://wiki.gentoo.org/wiki/SDCard "SDCard") (although not contained in the term \"SSD\" technically sharing the same technology: non-volatile [flash memory](https://en.wikipedia.org/wiki/flash_memory "wikipedia:flash memory")) distinguish between TRIM and **ERASE**. Filesystem support is required in order to use discard. Majority of modern filesystems (like [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4")^[\[1\]](#cite_note-1)^, [XFS](https://wiki.gentoo.org/wiki/XFS "XFS")^[\[2\]](#cite_note-2)^, [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs")^[\[3\]](#cite_note-3)^, or [bcachefs](https://wiki.gentoo.org/wiki/Bcachefs "Bcachefs")) support discard, and it has been implemented for traditional (existing, \"old\") filesystems as well (e.g. [FAT](https://wiki.gentoo.org/wiki/FAT "FAT"), or [NTFS](https://wiki.gentoo.org/wiki/NTFS "NTFS")). Also there are filesystems developed primarily for flash-based devices, such as [F2FS](https://wiki.gentoo.org/wiki/F2FS "F2FS").

There are two basic approaches to issue the discard command --- using [mount] `discard` option (`-o discard`) for continuous discard^[\[4\]](#cite_note-4)^ or periodic calls of [fstrim] utility^[\[5\]](#cite_note-fstrim-5)^. Not all filesystems support both methods.

### [Slowing wear out]

Each write operation performed on a [NAND](https://en.wikipedia.org/wiki/Nand_memory "wikipedia:Nand memory") flash cell causes its wear. This fact limits the SSD lifespan. The cell endurance varies with used technology^[\[6\]](#cite_note-lifetime-6)^. On the other hand, read operations are straightforward and do not cause cell wear.

A basic method increasing SSD lifespan is to uniformly distribute writes across all the blocks. This method is called *wear leveling* and is deployed via SSD firmware.

From the system point of view, it is appropriate to generally reduce amount of writes.

## [Considerations]

### [][Discard (trim) support]

Device support for discard (sometimes referred to as trim) should be verified before performing any form of discarding on the drive.

It is possible to use [lsblk] utility from [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]]:

`user `[`$`]`lsblk --discard`

    NAME   DISC-ALN DISC-GRAN DISC-MAX DISC-ZERO
    sda           0      512B       2G         0
    ├─sda1        0      512B       2G         0
    ├─sda2        0      512B       2G         0
    └─sda3        0      512B       2G         0
    sdb           0        0B       0B         0
    └─sdb1        0        0B       0B         0

A device supporting discard has non-zero values in the columns of `DISC-GRAN` (discard granularity) and `DISC-MAX` (discard max bytes). In the example listing above, the [/dev/sda] device supports discard while [/dev/sdb] does not.

** Warning**\
Performing discard on a device that does not support it is potentially unsafe.

## [Initial setup]

### [Partitioning]

Sizes of SSD internal data structures (blocks and pages) varies across different devices. Filesystems operates on data structures of different sizes. For optimal performance filesystem data structures should aim not to cross boundaries of underlying SSD internal data structures. Thus effectively minimizing the number of required internal SSD operations. This can be achieved by aligning start of each partition --- the common alignment is to 1 MiB.

Both [parted] and [fdisk] partitioning utilities support partition alignment. For [parted], there is `-a optimal` option. Recent versions of [fdisk] should use optimal alignment by default^[\[7\]](#cite_note-7)^.

It is possible to easily check the alignment for given partition using [parted]:

`root `[`#`]`parted /dev/sda`

    (parted) align-check optimal 1
    1 aligned

For further details about the partitioning, follow dedicated [handbook chapter](https://wiki.gentoo.org/wiki/Handbook:AMD64/Blocks/Disks "Handbook:AMD64/Blocks/Disks").

#### [blkdiscard]

[blkdiscard] utility from [[[sys-apps/util-linux-2.23]](https://packages.gentoo.org/packages/sys-apps/util-linux-2.23)[]] (or later) discards all data blocks on given device.

** Warning**\
All data on the discarded device will be lost!

#### [LVM]

[LVM](https://wiki.gentoo.org/wiki/LVM "LVM") aligns to MiB boundaries and passes discards to underlying devices by default. No additional configuration is required.

In order to discard all unused space in a [Volume Group](https://wiki.gentoo.org/wiki/LVM#VG_.28Volume_Group.29 "LVM") ([VG](https://wiki.gentoo.org/wiki/LVM#VG_.28Volume_Group.29 "LVM")) use the [[blkdiscard]](https://wiki.gentoo.org/wiki/SSD#blkdiscard "SSD") utility:

`root `[`#`]`lvcreate -l100%FREE -n trim yourvg `

`root `[`#`]`blkdiscard /dev/yourvg/trim `

`root `[`#`]`lvremove yourvg/trim `

Alternatively, there is a discard option in [lvm.conf] which makes LVM discard entire [Logical Volume](https://wiki.gentoo.org/wiki/LVM#LV_.28Logical_Volume.29 "LVM") ([LV](https://wiki.gentoo.org/wiki/LVM#LV_.28Logical_Volume.29 "LVM")) on [lvremove], [lvreduce], [pvmove] and other actions that free Physical Extents (PE) in a VG.

** Warning**\
Enabling it will immediately render the system unable to recover any lost data from changes to the LV layout.

[FILE] **`/etc/lvm/lvm.conf`**

    devices

#### [LUKS]

For discards to pass through [fully encrypted devices](https://wiki.gentoo.org/wiki/Full_Disk_Encryption_From_Scratch "Full Disk Encryption From Scratch") ([LUKS](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt")), they have to be opened with the `--allow-discards` option.

`root `[`#`]`cryptsetup luksOpen --allow-discards /dev/thing <name>`

This can be applied permanently in LUKS2 by adding it to the header.

`root `[`#`]`cryptsetup refresh --persistent --allow-discards <name>`

To check if discard is enabled for the current session, see if `flags: discards` is listed in:

`root `[`#`]`cryptsetup status <name>`

To check if discard is permamently enabled, see if `Flags: allow-discards` is listed in:

`root `[`#`]`cryptsetup luksDump /dev/thing`

##### [LUKS1]

When the root-device is encrypted with LUKS1, discards must be enabled by the [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs"). When using [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") for creating your initramfs, pass the following kernel option:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="root_trim=yes"

When using [dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") for creating the initramfs, pass the following kernel option:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="rd.luks.allow-discards"

To evaluate if discard is enabled on a LUKS device, check if the output of the following command contains the string `allow_discards`:

`root `[`#`]`dmsetup table /dev/mapper/crypt_dev --showkeys`

### [Formatting]

Similarly to [partitions](https://wiki.gentoo.org/wiki/SSD#Partitioning "SSD"), performance can be improved if a filesystem is configured the way it can align its data structures with device\'s internal structures sizes --- namely its erase block size.

This configuration gets important in case of a software RAID, when one really should know the erase block size^[\[8\]](#cite_note-8)^. Consider this information when making a purchase.

#### [Configuring for erase block size]

When device\'s erase block size is known, it can be used when creating a filesystem.

For example for [ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4") using [mkfs.ext4] on an average-sized partition, it will apply 4KiB blocks^[\[9\]](#cite_note-9)^. Using `-E stride` and `-E stripe-width` options, it is possible to set the alignment to erase block size. Both options should be set as *erase block size* / *block size*.

For a drive with 512KiB erase block size, it makes 512KiB / 4KiB = 128:

`root `[`#`]`mkfs.ext4 -E stride=128,stripe-width=128 /dev/sda3`

##### [List of devices with known erase block sizes]

-   *OCZ* drives; stride an stripe-width are 128

** Note**\
Erase block size is 512KiB^[\[10\]](#cite_note-10)^

-   *Crucial M500 240GB*; stride and stripe-width are 2048

** Note**\
Page size is 16KiB, there are 512 pages per block^[\[11\]](#cite_note-11)^. 16KiB \* 512 = 8192KiB for erase block size. 8192KiB / 4KiB = 2048 for stride and stripe-width size.

-   *SanDisk z400s*; stride an stripe-width are 4096

** Note**\
According to Dutch customer care service from SanDisk the erase block size = 16KiB.

### [Mounting]

For rootfs it is usually recommended to periodically use [fstrim] utility. Using the `discard` mount option results in continuous discard that could potentially cause degradation of older or poor-quality SSDs^[\[5\]](#cite_note-fstrim-5)^.

The following command can be used manually or be setup as a [periodic job](https://wiki.gentoo.org/wiki/SSD#Periodic_fstrim_jobs "SSD") to run once a week^[\[12\]](#cite_note-freq-12)^:

`root `[`#`]`fstrim -v /`

** Note**\
Not every filesystem driver supports [fstrim]. Examples are [ntfs3](https://wiki.gentoo.org/wiki/NTFS#Native_support "NTFS") and [bcachefs](https://wiki.gentoo.org/wiki/Bcachefs "Bcachefs"), which only support the `discard` mount option. On a [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") system, running the [fstrim] command on any mounted subvolume will perform the discard command on the device.

For mount points with a low amount of disk writes occurring on a SSD it should be safe to use the `discard` mount option in [[/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab")]. Also it is recommended to use the [mount] option when maintaining performance is required^[\[13\]](#cite_note-13)^.

Given the considerations above, a discard-enabled [/etc/fstab] could look like this:

[FILE] **`/etc/fstab`fstab with discard enabled**

    /dev/sda3          /mnt/archive          ext4          defaults,relatime,discard          0 1

Once the [/etc/fstab] has been modified, remount all filesystems mentioned there via:

`root `[`#`]`mount -a`

** Note**\
Not every filesystem driver supports the `discard` mount option, although the majority do. As an example, [ntfs-3g](https://wiki.gentoo.org/wiki/NTFS#NTFS-3G_.28FUSE_implementation.29 "NTFS") can only be trimmed with [fstrim].

## [Additional configuration]

### [Periodic fstrim jobs]

There are multiple ways how to setup a periodic block discarding process. As of 2018, the default recommended frequency is once a week^[\[12\]](#cite_note-freq-12)^.

#### [cron]

Run [fstrim] on all mounted devices that support discard on a weekly basis:

[FILE] **`/etc/crontab`Run fstrim once per week**

    # Mins  Hours  Days   Months  Day of the week   Command
      15    13     *      *       1                 /sbin/fstrim --all

Similarly, it is possible to run [fstrim] only for a selected mount point:

[FILE] **`/etc/crontab`Run fstrim once per week on rootfs**

    # Mins  Hours  Days   Months  Day of the week   Command
      15    13     *      *       1                 /sbin/fstrim -v /

#### [SSDcronTRIM]

There is also a semi-automatic cron job available on GitHub called [SSDcronTRIM](http://chmatse.github.io/SSDcronTRIM/) which has the following features:

-   Distribution independent script (developed on a Gentoo system).
-   The script decides every time depending on the disk usage how often (monthly, weekly, daily, hourly) each partition has to be trimmed.
-   Recognizes if it should install itself into [/etc/cron.], [/etc/cron.d] or any other defined directory and if it should make an entry into [crontab].
-   Checks if the kernel meets the requirements, the filesystem is able to and if the SSD supports trimming.

#### [SSDcronTRIM-LUKS]

There is also a semi-automatic cron job available on GitHub called [SSDcronTRIM-LUKS](https://github.com/spai-phoenix/SSDcronTRIM-L/) with dm-crypt/LUKS support.

#### [systemd timer]

** Tip**\
The timer only operates on filesystems listed in [/etc/fstab]. This means that Discoverable Partition Specification setups won\'t be trimmed out of the box.

[[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] on systemd-enabled systems comes with a timer unit executing a weekly fstrim. Enable it with:

`root `[`#`]`systemctl enable fstrim.timer`

#### [][Without cron, on system shutdown (with OpenRC)]

A [/etc/local.d](https://wiki.gentoo.org/wiki//etc/local.d "/etc/local.d") script may be used to trim on poweroff on Fridays:

[FILE] **`/etc/local.d/date.stop`**

    # From
    # https://fitzcarraldoblog.wordpress.com/2018/01/13/running-a-shell-script-at-shutdown-only-not-at-reboot-a-comparison-between-openrc-and-systemd/
    if [ `who -r | awk ''` = "0" ] && [ "$(date +%a)" = "Fri" ]; then
        echo /etc/local.d/trim.stop: run SSD trim
        fstrim / --verbose
        sleep 5
    fi

### [Reducing amount of writes]

** Tip**\
While the advice below is technically valid, modern flash-based internal storage devices typically have sufficient write endurance that no special action is required, even on a system where all packages are rebuilt regularly. **Buying additional, relatively expensive, RAM to use as a tmpfs to save on writes to relatively cheap storage media is not an effective use of resources**.

The flash-based SSDs have a limited write lifetime - the number of writes performed^[\[6\]](#cite_note-lifetime-6)^. Thus when using a SSD, administrators generally want to reduce the amount of writes.

#### [Portage `TMPDIR` on tmpfs]

When building packages via [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") it is possible to perform the operations in RAM by using a [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs") or [zram](https://wiki.gentoo.org/wiki/Zram "Zram") mount. This has the theoretical benefit of reducing writes to the SSD. See [Portage `TMPDIR` on tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs") (or zram) guide.

#### [Temporal files on tmpfs]

** Warning**\
Remember that all data in [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs") reside in volatile memory. So data on tmpfs will be lost after system reboot, shutdown or crash!

It is possible to mount desired mount points as [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs"). Since tmpfs stores files in volatile memory all the I/O operations directed to the given mount points are not performed on the solid state disk. This reduces the amount of writes and also improves performance.

This is an example of both [/tmp] and [/var/tmp] being mounted as tmpfs:

[FILE] **[`/etc/fstab`](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab")**

    # temporal mountpoints on tmpfs
    tmpfs           /tmp            tmpfs           size=16G,noatime        0 0
    tmpfs           /var/tmp        tmpfs           size=1G,noatime         0 0

** Tip**\
[Systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")-based systems mount [/tmp] as tmpfs by default. Therefore an explicit [/etc/fstab] entry is required only for changing the default mount options. Currently used options can be reviewed by:

`user `[`$`]`findmnt | grep '/tmp'`

** Warning**\
[/var/tmp] will typically also be used by [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") (under the [/var/tmp/portage] directory). If its size is too small, it will lead to build errors. Refer to [Portage TMPDIR on tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs") for appropriately sizing [/var/tmp].

** Tip**\
On modern (fast) systems, [zram](https://wiki.gentoo.org/wiki/Zram "Zram") is an alternative to [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs").

#### [XDG cache on tmpfs]

When running a Gentoo desktop, many programs, using [X Window System](https://wiki.gentoo.org/wiki/Xorg "Xorg") ([Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium"), [Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox") etc.) make frequent disk I/O every few seconds to cache^[\[14\]](#cite_note-14)^.

The cache directory location usually complies to *XDG Base Directory Specification*^[\[15\]](#cite_note-15)^, namely to the `XDG_CACHE_HOME` environment variable. The default cache location is [\~/.cache], which is usually mounted on a hard drive and could be moved to [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs").

To remap the cache directory location create a script that exports to directory under [/run]:

[FILE] **`/etc/profile.d/xdg_cache_home.sh`**

    if [ $ ]; then
      export XDG_CACHE_HOME="/run/user/$/cache"
    fi

#### [][Web browser profile(s) and cache on tmpfs]

The web browser profile/s, cache, etc. can be relocated to [tmpfs](https://wiki.gentoo.org/wiki/Tmpfs "Tmpfs"). The corresponding I/O associated with using the browser gets redirected from the SSD drive to tmpfs\' volatile memory, resulting in reduced wear to the physical drive and also improving browser speed and responsiveness.

It is possible to relocate the browser components mentioned above with the utility [[[www-misc/profile-sync-daemon]](https://packages.gentoo.org/packages/www-misc/profile-sync-daemon)[]]:

`root `[`#`]`emerge --ask www-misc/profile-sync-daemon`

** Note**\
Note [[[www-misc/profile-sync-daemon]](https://packages.gentoo.org/packages/www-misc/profile-sync-daemon)[]] version 6 or greater requires [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd").

##### [systemd]

Close all the browsers, start and enable the daemon:

`user `[`$`]`systemctl --user enable --now psd`

Now it is possible to view all symlinks by printing the status of the started daemon:

`user `[`$`]`psd p`

##### [OpenRC]

Next add the users whose browser(s) profile(s) will get symlinked to a tmpfs or another mountpoint in the variable `USERS`:

[FILE] **`/etc/psd.conf`**

    USERS="user user2 root"

Finally, close all the browsers, start and enable the daemon:

`root `[`#`]`rc-update add psd default `

`root `[`#`]`rc-service psd start `

Now it is possible to view all symlinks by printing the status of the started daemon:

`user `[`$`]`psd p`

## [See also]

-   [HDD](https://wiki.gentoo.org/wiki/HDD "HDD") --- describes the setup of an internal SATA or PATA (IDE) rotational **hard disk drive**.
-   [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe") --- flash memory chips connected to a system via the PCI-E bus (use four-lane max).

## [External resources]

-   [Aligning an SSD on Linux](http://blog.nuclex-games.com/2009/12/aligning-an-ssd-on-linux/) --- Drives internal structures explained.
-   [Aligning filesystems to an SSD's erase block size](https://tytso.livejournal.com/2009/02/20/) --- Aligning explained by Ted T\'so.
-   [Magic soup: ext4 with SSD, stripes and strides](https://thelastmaimou.wordpress.com/2013/05/04/magic-soup-ext4-with-ssd-stripes-and-strides/) --- ext4 aligning discussion
-   [Arch Linux Profile-Sync-Daemon](https://wiki.archlinux.org/index.php/profile-sync-daemon)

## [References]

1.  [[[↑](#cite_ref-1)] [[Performance of TRIM command on ext4 filesystem](https://people.redhat.com/lczerner/discard/ext4_discard.html), people.redhat.com. Retrieved on October 29, 2018]]
2.  [[[↑](#cite_ref-2)] [[FITRIM/discard](http://xfs.org/index.php/FITRIM/discard), XFS.org. Retrieved on October 29, 2018]]
3.  [[[↑](#cite_ref-3)] [[FAQ - btrfs Wiki](https://btrfs.wiki.kernel.org/index.php/FAQ#Does_Btrfs_support_TRIM.2Fdiscard.3F), btrfs.wiki.kernel.org. Retrieved on October 29, 2018]]
4.  [[[↑](#cite_ref-4)] [[mount(8) - Linux manual page](http://man7.org/linux/man-pages/man8/mount.8.html), man7.org. Retrieved on October 29, 2018]]
5.  [[↑ ^[5.0](#cite_ref-fstrim_5-0)^ ^[5.1](#cite_ref-fstrim_5-1)^] [[fstrim(8) - Linux manual page](http://man7.org/linux/man-pages/man8/fstrim.8.html), man7.org. Retrieved on October 29, 2018]]
6.  [[↑ ^[6.0](#cite_ref-lifetime_6-0)^ ^[6.1](#cite_ref-lifetime_6-1)^] [[Hard Drive - Why Do Solid State Devices (SSD) Wear Out](https://www.dell.com/support/article/cz/cs/czdhs1/sln156899/hard-drive-why-do-solid-state-devices-ssd-wear-out?lang=en), Dell. Retrieved on October 29, 2018]]
7.  [[[↑](#cite_ref-7)] [[fdisk(8) - Linux manual page](http://man7.org/linux/man-pages/man8/fdisk.8.html), man7.org. Retrieved on October 31, 2018]]
8.  [[[↑](#cite_ref-8)] [[RAID setup - Linux Raid Wiki](https://raid.wiki.kernel.org/index.php/RAID_setup#Performance), wiki.kernel.org. Retrieved on November 1, 2018]]
9.  [[[↑](#cite_ref-9)] [[mke2fs(8) - Linux manual page](http://man7.org/linux/man-pages/man8/mke2fs.8.html), man7.org. Retrieved on November 1, 2018]]
10. [[[↑](#cite_ref-10)] [[Partition Alignment Spreadsheet](https://www.techpowerup.com/forums/threads/partition-alignment-spreadsheet.107126/), techpowerup.com. Retrieved on November 1, 2018]]
11. [[[↑](#cite_ref-11)] [[The Crucial/Micron M500 Review (960GB, 480GB, 240GB, 120GB)](http://www.anandtech.com/show/6884/crucial-micron-m500-review-960gb-480gb-240gb-120gb)]]
12. [[↑ ^[12.0](#cite_ref-freq_12-0)^ ^[12.1](#cite_ref-freq_12-1)^] [[fstrim.timer\\sys-utils - util-linux/util-linux.git - The util-linux code repository](https://git.kernel.org/pub/scm/utils/util-linux/util-linux.git/tree/sys-utils/fstrim.timer), kernel.org. Retrieved on October 30, 2018]]
13. [[[↑](#cite_ref-13)] [[2.4. Discard unused blocks](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Storage_Administration_Guide/ch02s04.html), Red Hat. Retrieved on October 30, 2018]]
14. [[[↑](#cite_ref-14)] [[Firefox is eating your SSD - here is how to fix it](https://www.servethehome.com/firefox-is-eating-your-ssd-here-is-how-to-fix-it/), Loyolan Ventures. Retrieved on October 28, 2018]]
15. [[[↑](#cite_ref-15)] [[XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html), freedesktop.org. Retrieved on October 28, 2018]]