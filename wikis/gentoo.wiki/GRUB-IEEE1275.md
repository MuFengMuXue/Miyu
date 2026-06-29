This article covers installation of the [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") bootloader on PowerPC machines with [Open Firmware](https://en.wikipedia.org/wiki/Open_Firmware "wikipedia:Open Firmware"). This corresponds to `GRUB_PLATFORMS`=`ieee1275` for **[ppc]** and **[ppc64]** architectures, and to the `--target=powerpc-ieee1275` option of [grub-install]. IEEE standard 1275 was the official standard for Open Firmware, sometimes abbreviated as **OFW** or **OF**.

** Note**\
Linux PowerPC [profiles](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") ([default/linux/powerpc/\*]) set [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") `grub_platforms_ieee1275` by default for [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]], so no special setting of `GRUB_PLATFORMS` is needed in [/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf "/etc/portage/make.conf").

## Contents

-   [[1] [Installing the bootloader]](#Installing_the_bootloader)
    -   [[1.1] [Apple NewWorld Macs (PowerPC)]](#Apple_NewWorld_Macs_.28PowerPC.29)
        -   [[1.1.1] [NewWorld Bootblock partition]](#NewWorld_Bootblock_partition)
        -   [[1.1.2] [CHRP boot script]](#CHRP_boot_script)
        -   [[1.1.3] [Test and set as default boot-device]](#Test_and_set_as_default_boot-device)
-   [[2] [External resources]](#External_resources)

## [Installing the bootloader]

### [][Apple NewWorld Macs (PowerPC)]

NewWorld Macs are Macs with Open Firmware version 3 (OF3) or later (OF3+). NewWorld Macs will show a graphical boot selection when holding the [⌥/Option/Alt] key right after the chime, until a startup selection is shown on the screen. This will only work well when a CHRP script that includes an `os-badge` is blessed (attribute `:tbxi`) on a [HFS](https://wiki.gentoo.org/wiki/HFS "HFS") volume.

** Important**\
The precondition for this example is that [/boot] is a separate [ext2](https://wiki.gentoo.org/wiki/Ext2 "Ext2") partition. Other filesystems are possible when the list of GRUB modules is adapted accordingly. If [/boot] is on the root partition, the example has to be adapted accordingly as well.

-   NewWorld Apple Mac computer (1999---2006).
-   [/boot] is a separate [ext2](https://wiki.gentoo.org/wiki/Ext2 "Ext2") partition.
-   Apple Partition Map (APM) consisting of:
    -   NewWorld Bootblock as `Apple_Boot`
    -   Filesystem [HFS](https://wiki.gentoo.org/wiki/HFS "HFS").
    -   As any partition number (at the beginning of the disk is preferred, but not required).
-   Apple specific `os-badge`.

#### [NewWorld Bootblock partition]

** Note**\
The use of [[[sys-fs/mac-fdisk]](https://packages.gentoo.org/packages/sys-fs/mac-fdisk)[]] is highly recommended. Even though package [[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]] can also create Apple Partition Map (APM) style partitions it is not as verbose about partition types.

First, a NewWorld Bootblock has to be created using [mac-fdisk]:

`root `[`#`]`emerge --ask sys-fs/mac-fdisk`

`root `[`#`]`mac-fdisk /dev/sda`

At the interactive command prompt this partition can either be created manually e.g. by using the [C] command for \"create new partition, specifying the partition type\", or semi-automatic by using the [b] command for \"create new 800k Apple_Bootstrap partition (used by yaboot)\". Either way you should get a bootable HFS partition of either the type `Apple_Boot` or `Apple_Bootstrap`. The partition name is optional but helps when listing the partitions. All values are entered by hand without automatism of any kind.

The following example uses the free space (type Apple_Free) right after the partition table. If this wasn\'t taken care of e.g. when installing Mac OS X, per default only 128 MB will be free here, which should barely be enough for this purpose. Older versions of Mac OS X don\'t add free space between partitions, so the NewWorld Bootblock will have to be added behind the already existing partitions.

Normally 800 KB is used but any size big enough for a HFS filesystem and the GRUB core files will do. In this example, the *hole* between the partition table and the first partition (Mac OS X Tiger) is 1.1 GB. It starts at block 64 (base column) and is 2359232 blocks long (length column). Since this is enough to add 128 MB \"holes\" before and after, the partition will add two more Apple_Free holes. The block numbers to enter have to be calculated first: 128 MB Apple_Free \"holes\" are 262144 blocks in size, so the first block will have to be `64` (base) + `262144` (Apple_Free) = `262208`. Since the original Apple_Free \"hole\" in this specific example ([/dev/sda2]) has 2359232 blocks, another hole is left at the end if the size of the bootstrap partition is `2359232 - (2 * 262144) = 1834944`.

To get this done, the key sequence [p] (print partition table), [C] (create partition with type also specified; type uppercase C!), `262208` (first block), `1834944` (length), `"NewWorld Bootblock"` (name of partition; use quotes!) and `Apple_Boot` (type of partition). To check if this worked, use [p] again to list the new partition table. Note that two more partitions were added and the numbers behind those partitions have been shifted accordingly (\"Linux Boot\" was /dev/sda9 and got shifted to /dev/sda11). All modifications are done in memory and will be saved with [w] (write the partition table), followed by [y] (to confirm). To restart if something got messed up simply quit without writing the modifications. Type [q] for quit.

** Important**\
For strings use quotation marks `"` if they contain whitespace(s)! Since partition types use underlines `_` only, this is mainly important for (optional) partition names. However, for a better understanding of what is what it is recommended to use partition names. Partition names can also be used for referring to partitions using the `PARTLABEL=` directive, e.g. in [/etc/fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab").

`root `[`#`]`mac-fdisk /dev/sda `

    /dev/sda
    Command (? for help): p
            #                    type name                  length   base      ( size )  system
    /dev/sda1     Apple_partition_map Apple                     63 @ 1         ( 31.5k)  Partition map
    /dev/sda2              Apple_Free Extra                2359232 @ 64        (  1.1G)  Free space
    /dev/sda3               Apple_HFS Tiger              209715200 @ 2359296   (100.0G)  HFS
    /dev/sda4              Apple_Free Extra                 262144 @ 212074496 (128.0M)  Free space
    /dev/sda5               Apple_HFS Leopard            314572800 @ 212336640 (150.0G)  HFS
    /dev/sda6              Apple_Free Extra                 262144 @ 526909440 (128.0M)  Free space
    /dev/sda7              Apple_Boot Apple Hardware Test    100898 @ 527171584 ( 49.3M)  Unknown
    /dev/sda8              Apple_Free Extra                 262144 @ 527272482 (128.0M)  Free space
    /dev/sda9         Apple_UNIX_SVR2 Linux Boot           2097152 @ 527534626 (  1.0G)  Linux native
    /dev/sda10             Apple_Free Extra                 262144 @ 529631778 (128.0M)  Free space
    /dev/sda11        Apple_UNIX_SVR2 Gentoo Linux       134217728 @ 529893922 ( 64.0G)  Linux native
    /dev/sda12             Apple_Free Extra                 262144 @ 664111650 (128.0M)  Free space
    /dev/sda13        Apple_UNIX_SVR2 Debian Linux       134217728 @ 664373794 ( 64.0G)  Linux native
    /dev/sda14             Apple_Free Extra                 262144 @ 798591522 (128.0M)  Free space
    /dev/sda15        Apple_UNIX_SVR2 Linux Local         71216270 @ 798853666 ( 34.0G)  Linux native
    /dev/sda16             Apple_Free Extra                 262144 @ 870069936 (128.0M)  Free space
    /dev/sda17        Apple_UNIX_SVR2 Linux swap          67108864 @ 870332080 ( 32.0G)  Linux native
    /dev/sda18             Apple_Free Extra                 262144 @ 937440944 (128.0M)  Free space

    Block size=512, Number of Blocks=937703088
    DeviceType=0x0, DeviceId=0x0

    Command (? for help): C
    First block: 262208
    Length (in blocks, kB (k), MB (M) or GB (G)): 1834944
    Name of partition: "NewWorld Bootblock"
    Type of partition: Apple_Boot
    Command (? for help): w
    IMPORTANT: You are about to write a changed partition map to disk.
    For any partition you changed the start or size of, writing out
    the map causes all data on that partition to be LOST FOREVER.
    Make sure you have a backup of any data on such partitions you
    want to keep before answering 'yes' to the question below!

    Write partition map? [n/y]: y
    The partition map has been saved successfully!

    Syncing disks.

    Partition map written to disk. If any partitions on this disk
    were still in use by the system (see messages above), you will need
    to reboot in order to utilize the new partition map.

    Command (? for help): q

The final partition layout of this example looks like this, using [mac-fdisk] and [parted]:

`root `[`#`]`mac-fdisk -l /dev/sda `

    /dev/sda
            #                    type name                  length   base      ( size )  system
    /dev/sda1     Apple_partition_map Apple                     63 @ 1         ( 31.5k)  Partition map
    /dev/sda2              Apple_Free Extra                 262144 @ 64        (128.0M)  Free space
    /dev/sda3              Apple_Boot NewWorld Bootblock   1834944 @ 262208    (896.0M)  Unknown
    /dev/sda4              Apple_Free Extra                 262144 @ 2097152   (128.0M)  Free space
    /dev/sda5               Apple_HFS Tiger              209715200 @ 2359296   (100.0G)  HFS
    /dev/sda6              Apple_Free Extra                 262144 @ 212074496 (128.0M)  Free space
    /dev/sda7               Apple_HFS Leopard            314572800 @ 212336640 (150.0G)  HFS
    /dev/sda8              Apple_Free Extra                 262144 @ 526909440 (128.0M)  Free space
    /dev/sda9              Apple_Boot Apple Hardware Test    100898 @ 527171584 ( 49.3M)  Unknown
    /dev/sda10             Apple_Free Extra                 262144 @ 527272482 (128.0M)  Free space
    /dev/sda11        Apple_UNIX_SVR2 Linux Boot           2097152 @ 527534626 (  1.0G)  Linux native
    /dev/sda12             Apple_Free Extra                 262144 @ 529631778 (128.0M)  Free space
    /dev/sda13        Apple_UNIX_SVR2 Gentoo Linux       134217728 @ 529893922 ( 64.0G)  Linux native
    /dev/sda14             Apple_Free Extra                 262144 @ 664111650 (128.0M)  Free space
    /dev/sda15        Apple_UNIX_SVR2 Debian Linux       134217728 @ 664373794 ( 64.0G)  Linux native
    /dev/sda16             Apple_Free Extra                 262144 @ 798591522 (128.0M)  Free space
    /dev/sda17        Apple_UNIX_SVR2 Linux Local         71216270 @ 798853666 ( 34.0G)  Linux native
    /dev/sda18             Apple_Free Extra                 262144 @ 870069936 (128.0M)  Free space
    /dev/sda19        Apple_UNIX_SVR2 Linux swap          67108864 @ 870332080 ( 32.0G)  Linux native
    /dev/sda20             Apple_Free Extra                 262144 @ 937440944 (128.0M)  Free space

    Block size=512, Number of Blocks=937703088
    DeviceType=0x0, DeviceId=0x0

`root `[`#`]`parted /dev/sda print `

    Model: ATA TOSHIBA-TR200 (scsi)
    Disk /dev/sda: 480GB
    Sector size (logical/physical): 512B/512B
    Partition Table: mac
    Disk Flags:

    Number  Start   End     Size    File system     Name                 Flags
     1      512B    32.8kB  32.3kB                  Apple
     3      134MB   1074MB  939MB   hfs             NewWorld Bootblock   boot
     5      1208MB  109GB   107GB   hfs+            Tiger
     7      109GB   270GB   161GB   hfs+            Leopard
     9      270GB   270GB   51.7MB  hfs+            Apple Hardware Test  boot
    11      270GB   271GB   1074MB  ext2            Linux Boot
    13      271GB   340GB   68.7GB  btrfs           Gentoo Linux
    15      340GB   409GB   68.7GB  btrfs           Debian Linux
    17      409GB   445GB   36.5GB  ext4            Linux Local
    19      446GB   480GB   34.4GB  linux-swap(v1)  Linux swap

To make the Linux kernel recognize the new partitions a restart is required. But to get access to devices that were not in use, [partprobe] (from the [[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]] package) can force the kernel to re-read the partition table, with the exception of partitions already in use:

`root `[`#`]`partprobe /dev/sda`

    Error: Partition(s) 11, 13, 17, 19 on /dev/sda have been written, but we have been unable to inform the kernel of the change, probably because it/they are in use.  As a result, the old partition(s) will remain in use.  You should reboot now before making further changes.

Notice that partition 11 is now [/boot] \"Linux Boot\" (ext2), but it was mounted as [/dev/sda9] before the change to [/dev/sda11]. The former partition numbers and the listet new partition numbers from the [partprobe] error message should not be used for anything else than to keep them mounted as they were, but it should be safe to access the newly created NewWorld Bootblock as [/dev/sda3] now to setup GRUB as the bootloader -- before a restart.

#### [CHRP boot script]

Install the required tools:

`root `[`#`]`emerge --ask sys-boot/grub sys-fs/hfsutils sys-apps/ibm-powerpc-utils`

In this example, a CHRP boot script will load the GRUB image, which will use an initial [grub.cfg] to find and load the actual [grub.cfg] configuration from the [/boot/grub] directory on the `Linux Boot` [/boot] partition.

Make sure that [/boot] is mounted and create a new directory [/boot/NWBB] (for NewWorld BootBlock):

`root `[`#`]`mount /boot `

`root `[`#`]`mkdir /boot/NWBB`

Find out the UUID of the [/boot] partition:

`root `[`#`]`cat /etc/fstab | grep /boot`

    UUID=be0188a5-1fd3-46fa-a82a-34cdea8ff194 /boot ext2 noauto,noatime,nodiratime,errors=remount-ro 1 2

Alternative:

`root `[`#`]`cat /etc/fstab | grep /boot`

    /dev/sda11 /boot ext2 noauto,noatime,nodiratime,errors=remount-ro 1 2

`root `[`#`]`blkid /dev/sda11`

    /dev/sda11: LABEL="Linux Boot" UUID="be0188a5-1fd3-46fa-a82a-34cdea8ff194" TYPE="ext2" PARTLABEL="Linux Boot"

Create file [/boot/NWBB/grub-initial.cfg] and use the UUID from above to let GRUB find the correct [/boot] partition. Although it would also be possible to specify an absolute path, using the UUID will compensate automatically for small changes, like switching drives or adding/deleting partitions.

[FILE] **`/boot/NWBB/grub-initial.cfg`**

    search --no-floppy --fs-uuid --set=root be0188a5-1fd3-46fa-a82a-34cdea8ff194
    set prefix=($root)/grub
    configfile /grub/grub.cfg

** Note**\
The UUID set via `--set=root UUID` is the UUID of the ext2 boot partition, not the root partition of the Linux base system. The real [grub.cfg] in [/boot/grub/grub.cfg] created by [grub-mkconfig] takes care of supplying the kernel cmdline with the real root UUID for booting Linux correctly.

Install GRUB to [/boot/grub] (the default path). Option `--no-nvram` prevents GRUB from setting the Open Firmware `boot-device` nvram variable. Since GRUB doesn\'t know about the CHRP script on the NewWorld Bootblock, it would set the wrong value anyway.

`root `[`#`]`grub-install --target=powerpc-ieee1275 --no-nvram`

With this setup, the initial [grub.cfg] ([/boot/NWBB/grub-initial.cfg]), GRUB will then look for [/grub/grub.cfg] on the actual [/boot] partition (i.e. [/boot/grub/grub.cfg] on the live system, since the boot partition is mounted) found via its UUID. Further updates to [grub.cfg] therefore go via the real [grub.cfg] the usual way, without the need to touch the NewWorld Bootblock anymore:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

Now create a list of modules to be included in the GRUB image.

[FILE] **`/boot/NWBB/grub_mod-minimal.list`**

    search_fs_uuid.mod search_fs_file.mod search_label.mod search.mod
    part_apple.mod
    fshelp.mod ext2.mod
    halt.mod reboot.mod echo.mod

The command [grub-mkimage] will create a minimal grub bootimage that includes these modules and the initial [grub.cfg]:

`root `[`#`]`` grub-mkimage --prefix=/boot/grub --format=powerpc-ieee1275 --config=/boot/NWBB/grub-initial.cfg --output=/boot/NWBB/grub.img `cat /boot/NWBB/grub_mod-minimal.list` ``

If `--config` with [grub-initial.cfg] is ommited, it will be looked up as [grub.cfg] in the same directory where the [grub.img] will later be loaded on the NewWorld Bootblock HFS partition.

This [/grub/grub.img] bootloader can then be called from a CHRP boot script, which will enable easy selection. When turning on (or rebooting) the Power Mac, holding the [⌥/Option/Alt] key right after the chime until the graphical boot selection appears, Open Firmware will show a list of all found operating systems with a compatible `os-badge` icon. Standard filenames for such a CHRP boot script are [ofboot.b], which is used here, or [bootinfo.txt]. In reality the file name for the CHRP boot script does not matter as long as it is in XML format and the only blessed file on the partition. It may contain the following:

[FILE] **`/boot/NWBB/ofboot.b`CHRP boot script**

    <CHRP-BOOT>
    <COMPATIBLE>
    MacRISC MacRISC3 MacRISC4
    </COMPATIBLE>
    <DESCRIPTION>
    GRand Unified Bootloader
    </DESCRIPTION>
    <OS-NAME>
    Linux
    </OS-NAME>
    <OS-BADGE-ICONS>
    3434
    00000000000000F781FB8181818181FBFAF500000000000000000000000000000000000000F6FAFAFAFA81F9F600000000000000
    0000000000F8FBF9F500F95656FCFB5656FBF800000000000000000000000000000000F5FAF9F5F7F600F6F6F9FAF70000000000
    000000F5FBFA0056FDFEFEFDFDFAAC81FB56568181560000000000000000000000F9F9F9F7FCFDFEFEFEFFFC81F656FA00000000
    0000F5AC2BF7FBFEFEFD2BF6568181F9F7F6F6F8FBF50000000000000000000000FAF700F600F5F7F7F6F7FEFFACF82BFB000000
    0000FC2BF5FEFFFFF5F7FC81F70000F7F9FAFAF8000000000000000000000000000056F9F9FAF9F7F7FA812BF7FFFF56F7FA0000
    005656F5FEFFAC2BF9FA000000000000000000000000000000000000000000000000000000000000000000FA56FAFEFEF8F9F700
    00FB00F7FFFF56F9F800000000000000000000F656FAFA56F50000000000F5F8F9F8F5000000000000000000F9F7FCFFFB00FB00
    F8F800ACFFACF6FA000000000000000000F6FA562BF5F5F781FA000000F9FA2B00F556F9F5000000000000000081F8FFFEF6562B
    810000FFFFF9FAF500000000000000002B8100F5F9FCACFBF82BFBF6FCFAF6FAFC81F600FA2B000000000000002BF8FEFFF8F5FA
    FA00F5FEFFFA8100000000000000002B8100F9FEFFFFFFFFFFFBF6FDFEACFDFEFFFFFFFBF581F600000000000000F9FEFFF700FA
    FA00FBFFFEF6F900000000000000F6FB00FCFFFFFFFFFFFFFFFFFCF600FCF7ACFEFFFFFFFDF6810000000000000056F9FFAC00FA
    FA00F6FFFFF856000000000000F5FBF5ACFFFFFFFFFFFFFFFFFFFF2B002BF8F5ACFFFFFFFFFDF6FA000000000000F9FCFF560081
    FA0081FFFFF8F9000000000000FBF6FBFFFFFFFFFFFFFFFFFFFFFFF800F55600FCFFFFFFFFFF81F8F80000000000F981FFAC0081
    FA0000FEFEF8FB0000000000812BFAFFFFFFFFFFFFFEFFFFFDF92BFA0000F6F981ACFEFFFFFFFF56F9F600000000F9FDFF2B0081
    FA00FAFFFF81812B000000FAF8F9FFFFFEACFBF80000F500000000F9F900562B0000FCF7F9ACFFFF2BF9F50000F9F6FEFFFB0081
    810000FCFFFBF6FB56F7FBF8F9FFFE5600000000F5FAAC000000F82BF6FAFBF800F556F80000F9FFFE2BFAFAFAF8FAFFFEF60081
    FAF6F5ACFFFFAC00F856F7ACFFFCF500000000FAFCFFFC00000056AC00F581F92BFEF9FAF6000081FFFFFBF6F62BFFFFACF6F6FA
    F6FA00FAFFFFFFACFA56FFFFAC0000000000F6FD2BFEF6F5565600F5F800F60081FEF7F656000000FDFFFFFDFDFFFFFFAC0081F5
    0081F52BFDFFFFFFFFFFFFFFF60000000000FBF6F6F5F656F52BF900FA000000FCFAF5F656000000F7FFFFFFFFFFFFFDF7F68100
    00F6FB00F8FDFFFFFFFFFF810000000000F6F5000000F52B56F9FC00F7F70000FCF881FCF500000000FEFFFFFFFFAC5600FBF500
    000056F900F8ACFDFFFFFFF5000000000000002B0000FDFEFFFE560000F60000F9ACFFFE810000000081FFFEFDFAF800FAF70000
    000000FAF9002B56FAFDFC0000000000000000F80000FBF5FEFEF5000000000000ACFFFA2B0000000000FEFB2BF5008156000000
    00000000F9FBF600F6FBF800000000000000F7F8000000F9F9F9F82B0000000000F6ACACF70000000000F7FD2BFA812B00000000
    0000000000F681FCFBFD0000000000000000FBF6000000000000F52B000000000000F92B810000000000008181F6000000000000
    0000000000000000F6FC00000000000000F6FF0000000000000000000000000000000081FBFB2B00000000F7F900000000000000
    000000000000000000FC00000000000000FCFAF600000000000000000000000000000056ACF581FBF700000081FB000000000000
    0000000000000000FAF90000000000008156F5F8000000000000002BFBFCFBF800000000FD2B000056FB8181FBF8000000000000
    0000000000000000AC0000000000F5FBF90000F6000000000000F5AC56F6005681F50000F6ACFCFBF70000000000000000000000
    00000000000000F881000000F5FAFDFD00000000000000000000F7FEFA2B0000F581F70000000000810000000000000000000000
    000000000000F9FCF500FAFDACFAF5FD00000000000000000000F5ACF5FDFEFA0000F82B00000000810000000000000000000000
    000000000000FCF8F9AC81FD000000FD000000000000FAF7000000F50081F9FAF800000000000000FB0000000000000000000000
    000000000000FC81F956F5FD000000FD0000000000000000F800F5000000000056000000000000F7FB0000000000000000000000
    00000000000000000000F5AC000000ACF800000000000000F5FAF80000000000F50000000000F8ACF50000000000000000000000
    00000000000000000000F5AC000000F5AC000000000000000056F9000000000000000000F7ACFCF5000000000000000000000000
    00000000000000000000F5FD00000000AC000000000000000000FB0000000000000000F5F6F5FCF6000000000000000000000000
    0000000000000000000000FD00000000FBFDF600000000000000F8F900000000000000000000F5FB000000000000000000000000
    0000000000000000000000FDF500000000F9ACF800000000000000815600000000F656818181AC56000000000000000000000000
    000000000000000000000081F80000000000F9FC0000000000000000F9ACACACFCFBFAFA81FD2B00000000000000000000000000
    0000000000000000000000F7FB0000000000FBF70000000000000000000000000000000000FB0000000000000000000000000000
    000000000000000000000000ACF500000000F9FD56F5000000000000000000000000000000FB0000000000000000000000000000
    000000000000000000000000F8FA0000000000F6FEFEF5000000000000F55681FCACFDACFC560000000000000000000000000000
    00000000000000000000000000FBF600000000002BFCFA00F700000000F9FDFDFAFEF90000000000000000000000000000000000
    00000000000000000000000000F5FB0000000000F5FEF7ACAC0000000000000000FCF50000000000000000000000000000000000
    0000000000000000000000000000F6FA000000002BFF2BFFFFAC00000000000000F7FA0000000000000000000000000000000000
    000000000000000000000000000000F65600000000FAFEFFFFAC0000000000F800F6810000000000000000000000000000000000
    00000000000000000000000000000000F52B00000000F8FEFBFF5600000000FCFAACF60000000000000000000000000000000000
    0000000000000000000000000000000000000000000000F9FCFCFFFB00F8FEFFFDF5000000000000000000000000000000000000
    00000000000000000000000000000000000000000000F9FDF7F5FFFD56FFFFFFFD00000000000000000000000000000000000000
    00000000000000000000000000000000000000000000810000FBFFFFFBFFFFFFFFACF9F5F5000000000000000000000000000000
    0000000000000000000000000000000000000000000000F600FC81FFFEFFFFFFFFFFFE8100000000000000000000000000000000
    00000000000000000000000000000000000000000000000000F7F6FDFFFFFFFEFFFFACF500000000000000000000000000000000
    000000000000000000000000000000000000000000000000000000F5FC81FC81FAFBF9F500000000000000000000000000000000

    00000000000000F781FB8181818181FBFAF500000000000000000000000000000000000000F6FAFAFAFA81F9F600000000000000
    0000000000F8FBF9F500F95656FCFB5656FBF800000000000000000000000000000000F5FAF9F5F7F600F6F6F9FAF70000000000
    000000F5FBFA0056FDFEFEFDFDFAAC81FB56568181560000000000000000000000F9F9F9F7FCFDFEFEFEFFFC81F656FA00000000
    0000F5AC2BF7FBFEFEFD2BF6568181F9F7F6F6F8FBF50000000000000000000000FAF700F600F5F7F7F6F7FEFFACF82BFB000000
    0000FC2BF5FEFFFFF5F7FC81F70000F7F9FAFAF8000000000000000000000000000056F9F9FAF9F7F7FA812BF7FFFF56F7FA0000
    005656F5FEFFAC2BF9FA000000000000000000000000000000000000000000000000000000000000000000FA56FAFEFEF8F9F700
    00FB00F7FFFF56F9F800000000000000000000F656FAFA56F50000000000F5F8F9F8F5000000000000000000F9F7FCFFFB00FB00
    F8F800ACFFACF6FA000000000000000000F6FA562BF5F5F781FA000000F9FA2B00F556F9F5000000000000000081F8FFFEF6562B
    810000FFFFF9FAF500000000000000002B8100F5F9FCACFBF82BFBF6FCFAF6FAFC81F600FA2B000000000000002BF8FEFFF8F5FA
    FA00F5FEFFFA8100000000000000002B8100F9FEFFFFFFFFFFFBF6FDFEACFDFEFFFFFFFBF581F600000000000000F9FEFFF700FA
    FA00FBFFFEF6F900000000000000F6FB00FCFFFFFFFFFFFFFFFFFCF600FCF7ACFEFFFFFFFDF6810000000000000056F9FFAC00FA
    FA00F6FFFFF856000000000000F5FBF5ACFFFFFFFFFFFFFFFFFFFF2B002BF8F5ACFFFFFFFFFDF6FA000000000000F9FCFF560081
    FA0081FFFFF8F9000000000000FBF6FBFFFFFFFFFFFFFFFFFFFFFFF800F55600FCFFFFFFFFFF81F8F80000000000F981FFAC0081
    FA0000FEFEF8FB0000000000812BFAFFFFFFFFFFFFFEFFFFFDF92BFA0000F6F981ACFEFFFFFFFF56F9F600000000F9FDFF2B0081
    FA00FAFFFF81812B000000FAF8F9FFFFFEACFBF80000F500000000F9F900562B0000FCF7F9ACFFFF2BF9F50000F9F6FEFFFB0081
    810000FCFFFBF6FB56F7FBF8F9FFFE5600000000F5FAAC000000F82BF6FAFBF800F556F80000F9FFFE2BFAFAFAF8FAFFFEF60081
    FAF6F5ACFFFFAC00F856F7ACFFFCF500000000FAFCFFFC00000056AC00F581F92BFEF9FAF6000081FFFFFBF6F62BFFFFACF6F6FA
    F6FA00FAFFFFFFACFA56FFFFAC0000000000F6FD2BFEF6F5565600F5F800F60081FEF7F656000000FDFFFFFDFDFFFFFFAC0081F5
    0081F52BFDFFFFFFFFFFFFFFF60000000000FBF6F6F5F656F52BF900FA000000FCFAF5F656000000F7FFFFFFFFFFFFFDF7F68100
    00F6FB00F8FDFFFFFFFFFF810000000000F6F5000000F52B56F9FC00F7F70000FCF881FCF500000000FEFFFFFFFFAC5600FBF500
    000056F900F8ACFDFFFFFFF5000000000000002B0000FDFEFFFE560000F60000F9ACFFFE810000000081FFFEFDFAF800FAF70000
    000000FAF9002B56FAFDFC0000000000000000F80000FBF5FEFEF5000000000000ACFFFA2B0000000000FEFB2BF5008156000000
    00000000F9FBF600F6FBF800000000000000F7F8000000F9F9F9F82B0000000000F6ACACF70000000000F7FD2BFA812B00000000
    0000000000F681FCFBFD0000000000000000FBF6000000000000F52B000000000000F92B810000000000008181F6000000000000
    0000000000000000F6FC00000000000000F6FF0000000000000000000000000000000081FBFB2B00000000F7F900000000000000
    000000000000000000FC00000000000000FCFAF600000000000000000000000000000056ACF581FBF700000081FB000000000000
    0000000000000000FAF90000000000008156F5F8000000000000002BFBFCFBF800000000FD2B000056FB8181FBF8000000000000
    0000000000000000AC0000000000F5FBF90000F6000000000000F5AC56F6005681F50000F6ACFCFBF70000000000000000000000
    00000000000000F881000000F5FAFDFD00000000000000000000F7FEFA2B0000F581F70000000000810000000000000000000000
    000000000000F9FCF500FAFDACFAF5FD00000000000000000000F5ACF5FDFEFA0000F82B00000000810000000000000000000000
    000000000000FCF8F9AC81FD000000FD000000000000FAF7000000F50081F9FAF800000000000000FB0000000000000000000000
    000000000000FC81F956F5FD000000FD0000000000000000F800F5000000000056000000000000F7FB0000000000000000000000
    00000000000000000000F5AC000000ACF800000000000000F5FAF80000000000F50000000000F8ACF50000000000000000000000
    00000000000000000000F5AC000000F5AC000000000000000056F9000000000000000000F7ACFCF5000000000000000000000000
    00000000000000000000F5FD00000000AC000000000000000000FB0000000000000000F5F6F5FCF6000000000000000000000000
    0000000000000000000000FD00000000FBFDF600000000000000F8F900000000000000000000F5FB000000000000000000000000
    0000000000000000000000FDF500000000F9ACF800000000000000815600000000F656818181AC56000000000000000000000000
    000000000000000000000081F80000000000F9FC0000000000000000F9ACACACFCFBFAFA81FD2B00000000000000000000000000
    0000000000000000000000F7FB0000000000FBF70000000000000000000000000000000000FB0000000000000000000000000000
    000000000000000000000000ACF500000000F9FD56F5000000000000000000000000000000FB0000000000000000000000000000
    000000000000000000000000F8FA0000000000F6FEFEF5000000000000F55681FCACFDACFC560000000000000000000000000000
    00000000000000000000000000FBF600000000002BFCFA00F700000000F9FDFDFAFEF90000000000000000000000000000000000
    00000000000000000000000000F5FB0000000000F5FEF7ACAC0000000000000000FCF50000000000000000000000000000000000
    0000000000000000000000000000F6FA000000002BFF2BFFFFAC00000000000000F7FA0000000000000000000000000000000000
    000000000000000000000000000000F65600000000FAFEFFFFAC0000000000F800F6810000000000000000000000000000000000
    00000000000000000000000000000000F52B00000000F8FEFBFF5600000000FCFAACF60000000000000000000000000000000000
    0000000000000000000000000000000000000000000000F9FCFCFFFB00F8FEFFFDF5000000000000000000000000000000000000
    00000000000000000000000000000000000000000000F9FDF7F5FFFD56FFFFFFFD00000000000000000000000000000000000000
    00000000000000000000000000000000000000000000810000FBFFFFFBFFFFFFFFACF9F5F5000000000000000000000000000000
    0000000000000000000000000000000000000000000000F600FC81FFFEFFFFFFFFFFFE8100000000000000000000000000000000
    00000000000000000000000000000000000000000000000000F7F6FDFFFFFFFEFFFFACF500000000000000000000000000000000
    000000000000000000000000000000000000000000000000000000F5FC81FC81FAFBF9F500000000000000000000000000000000

    00000000000000FFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000000000FFFFFFFFFFFFFFFF00000000000000
    0000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF0000000000
    000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000
    0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000
    0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000
    00FFFFFFFFFFFFFFFFFF000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFF00
    00FFFFFFFFFFFFFFFF00000000000000000000FFFFFFFFFFFF0000000000FFFFFFFFFF000000000000000000FFFFFFFFFFFFFF00
    FFFFFFFFFFFFFFFF000000000000000000FFFFFFFFFFFFFFFFFF000000FFFFFFFFFFFFFFFF0000000000000000FFFFFFFFFFFFFF
    FFFFFFFFFFFFFFFF0000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000FFFFFFFFFFFFFF
    FFFFFFFFFFFFFF0000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000FFFFFFFFFFFF
    FFFFFFFFFFFFFF00000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000FFFFFFFFFFFF
    FFFFFFFFFFFFFF000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000FFFFFFFFFFFF
    FFFFFFFFFFFFFF000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000FFFFFFFFFFFF
    FFFFFFFFFFFFFF0000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000FFFFFFFFFFFF
    FFFFFFFFFFFFFFFF000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000FFFFFFFFFFFFFF
    FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    00FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00
    00FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00
    0000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000
    000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000
    00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB00000000
    0000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000
    0000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000
    000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000
    0000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000
    0000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000
    00000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000
    000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000
    000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000
    000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000
    00000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000
    00000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000000000000000
    00000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000000000000000
    0000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000000000000000
    0000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000000000000000
    0000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000
    0000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000
    000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000
    000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000
    00000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000
    00000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000
    0000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000
    000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000
    00000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000
    0000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000000000000000000000000000
    000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000000000
    0000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF000000000000000000000000000000
    00000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000
    000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000
    0000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000
    </OS-BADGE-ICONS>
    <BOOT-SCRIPT>
    " screen" output
    load-base release-load-area
    boot &device;:&partition;,\grub\grub.img
    </BOOT-SCRIPT>
    </CHRP-BOOT>

If, for some reason, the `boot` instruction in the `<BOOT-SCRIPT>` section does not work, it is always possible to specify the boot partition directly.

** Note**\
The `<BOOT-SCRIPT>` section of the CHRP boot script needs to be in Open Firmware syntax. For the `boot` command this is a *device-specifier* and *arguments*. The syntax is **`/`**` component `**`/`**` component `**`/`**` ... name `**`@`**` address `**`:`**` arguments`. Arguments cannot contain `/` or `@`, hence the use of backslashes `\` in the path. In order to use the current device, the `&device;` variable can be used, likewise `&partition;` for the current partition. The resulting `&device;:&partition;` contains the path where the CHRP script is loaded from. If the *device-specifier* doesn\'t start with a slash it is an *alias*, e.g. `hd` stands for the first internal disk drive. All available aliases are listed by the `devalias` command on the Open Firmware command prompt, which is loaded by holding [⌘ Cmd] + [⌥ Option] + [O] + [F] keys at the chime.

To find the partition number of the NewWorld Bootblock, simply translate the known Linux device path, e.g. [/dev/sda3] is partition `3`. In Open Firmware notation the command for the absolute path in the CHRP script would be `boot hd:3,\grub\grub.img` when the GRUB image is in [/grub/grub.img] and the HFS NewWorld Bootblock is the third partition on `hd:`, an alias for the first disk drive.

** Note**\
The use of an absolute path has the disadvantage that it has to be changed in case the drive or the partition number changes for some reason. This would be the case if, for example, a second drive is installed and (due to the Open Firmware device lookup order) gets assigned the `hd:` alias, or if a partition is inserted before the NewWorld Bootblock and its partition number changes, resulting in a wrong path in the CHRP boot script. Booting GRUB would no longer work from the Open Firmware boot selection until the `boot` statement is changed to the new absolute path in the CHRP boot script. In such a case, GRUB can still be booted from the Open Firmware command prompt manually: should typing `boot hd:3,\grub\grub.img` instead of loading GRUB print an error message or load a different system, replacing the drive number and/or partition number could lead to a successful boot. For a second disk drive `hd:` may be replaced with `hd1:`, likewise the partition number after the colon.

[FILE] **`ofboot.b`example for using an absolute path in the CHRP boot script**

    <BOOT-SCRIPT>
    boot hd:3,\grub\grub.img
    </BOOT-SCRIPT>

Now copy all files to the NewWorld Bootblock HFS filesystem into [/grub] and bless (attribute `:tbxi`) the CHRP boot script [ofboot.b] and the [/grub] subdirectory:

`root `[`#`]`hformat -l "NewWorld Bootblock" /dev/sda3 `

`root `[`#`]`hmount /dev/sda3 `

`root `[`#`]`hmkdir :grub `

`root `[`#`]`hcopy -r /boot/NWBB/grub-initial.cfg :grub:grub.cfg `

`root `[`#`]`hcopy -r /boot/NWBB/grub.img :grub:grub.img `

`root `[`#`]`hcopy -r /boot/NWBB/ofboot.b :grub:ofboot.b `

`root `[`#`]`hattrib -c UNIX -t tbxi :grub:ofboot.b `

`root `[`#`]`hattrib -b :grub `

`root `[`#`]`humount`

#### [Test and set as default boot-device]

After a reboot, when holding the [⌥/Option/Alt] key right after the chime, a startup selection for the partition with GRUB should now be visible. If everything worked, [nvram] from the [[[sys-apps/ibm-powerpc-utils]](https://packages.gentoo.org/packages/sys-apps/ibm-powerpc-utils)[]] package may be used to set the default startup volume:

`root `[`#`]`nvram --print-config | grep ^boot-device `

    boot-device=first-boot/@0:5,\\:tbxi

`root `[`#`]`nvram --update-config boot-device='first-boot/@0:3,\\:tbxi'`

In the above commands the default startup volume was [/dev/sda5] (in the example APM partition layout from above this is Tiger i.e. Mac OS X Tiger 10.4) and it is then set to [/dev/sda3], the GRUB CHRP boot script in this example.

** Note**\
Use the command [nvram \--print-config \| grep \^boot-device] to see how the default was set before. This information should be used to set the startup partition to the NewWorld Bootblock since most of the times only the partition number has to be changed. The above example is from a Power Mac G5, it may be different on other Macs. `boot-device=hd:3,\\:tbxi` should also work, as should `boot-device=hd:3,\grub\ofboot.b` and `boot-device=hd:3,\grub\grub.img`\...

## [External resources]

-   [Open Firmware Quick Reference](http://firmworks.com/QuickRef.html) from FirmWorks
-   [NetBSD/macppc port FAQ](https://www.netbsd.org/ports/macppc/faq.html#ofw), containing useful information about Open Firmware