Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/Rootfs_encryption/fr "Chiffrement de la partition racine (''Rootfs encryption'') (15% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Rootfs_encryption/hu "Rootfs titkosítása (21% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Rootfs_encryption/ru "Rootfs encryption/ru (1% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Rootfs_encryption/ja "Rootfs の暗号化 (95% translated)")

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Disk_encryption "wikipedia:Disk encryption")

[[]][Package information](https://packages.gentoo.org/packages/sys-fs/cryptsetup)

Encrypting the root [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") can enhance privacy, and prevent unauthorized access.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [System preparation]](#System_preparation)
-   [[3] [Disk preparation]](#Disk_preparation)
    -   [[3.1] [Simple EFI System Partition Layout]](#Simple_EFI_System_Partition_Layout)
        -   [[3.1.1] [Configure GPT label]](#Configure_GPT_label)
        -   [[3.1.2] [Create the ESP]](#Create_the_ESP)
        -   [[3.1.3] [Create the Root partition]](#Create_the_Root_partition)
        -   [[3.1.4] [Apply changes]](#Apply_changes)
    -   [[3.2] [Split EFI/BOOTx Grub layout]](#Split_EFI.2FBOOTx_Grub_layout)
        -   [[3.2.1] [Configure GPT label]](#Configure_GPT_label_2)
        -   [[3.2.2] [Create the ESP]](#Create_the_ESP_2)
        -   [[3.2.3] [Create the Extended Boot partition]](#Create_the_Extended_Boot_partition)
        -   [[3.2.4] [Create the Root partition]](#Create_the_Root_partition_2)
        -   [[3.2.5] [Apply changes]](#Apply_changes_2)
-   [[4] [LUKS setup]](#LUKS_setup)
    -   [[4.1] [Create the LUKS encrypted partition]](#Create_the_LUKS_encrypted_partition)
        -   [[4.1.1] [LUKS Header Backup]](#LUKS_Header_Backup)
    -   [[4.2] [Open the LUKS volume]](#Open_the_LUKS_volume)
    -   [[4.3] [Set LUKS flags]](#Set_LUKS_flags)
-   [[5] [Filesystems Preparation]](#Filesystems_Preparation)
    -   [[5.1] [ESP]](#ESP)
    -   [[5.2] [Root filesystem]](#Root_filesystem)
    -   [[5.3] [Optional: Extended boot formatting]](#Optional:_Extended_boot_formatting)
-   [[6] [Gentoo installation]](#Gentoo_installation)
-   [[7] [Initramfs configuration]](#Initramfs_configuration)
    -   [[7.1] [UGRD]](#UGRD)
    -   [[7.2] [Dracut]](#Dracut)
        -   [[7.2.1] [Module configuration]](#Module_configuration)
        -   [[7.2.2] [LUKS target configuration]](#LUKS_target_configuration)
        -   [[7.2.3] [Systemd]](#Systemd)
        -   [[7.2.4] [Building the image]](#Building_the_image)
-   [[8] [Booting with the initramfs]](#Booting_with_the_initramfs)
    -   [[8.1] [efibootmgr]](#efibootmgr)
        -   [[8.1.1] [systemd]](#systemd_2)
            -   [[8.1.1.1] [UGRD]](#UGRD_2)
    -   [[8.2] [GRUB]](#GRUB)
-   [[9] [See also]](#See_also)

## [Installation]

### [Emerge]

** Note**\
[cryptsetup] is included in the [Gentoo Minimal installation CD](https://www.gentoo.org/downloads/).

`root `[`#`]`emerge --ask sys-fs/cryptsetup`

## [System preparation]

** Important**\
The [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") must be configured according to: [Dm-crypt: Kernel Configuration](https://wiki.gentoo.org/wiki/Dm-crypt#Kernel_Configuration "Dm-crypt").

This guide is designed to be followed as part of a fresh Gentoo install, the install procedure can be followed until the following step: [AMD64 Handbook: Designing a partition scheme](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Designing_a_partition_scheme "Handbook:AMD64/Full/Installation")

## [Disk preparation]

** Important**\
Partitioning typically does not involve modification of any of the data in partitions. If a drive is re-partitioned then encrypted, old data may remain in an unencrypted form until it is overwritten.

** Note**\
Modern storage devices **may not** be securely erased with something like [dd if=/dev/urandom of=/dev/sdX]. See [Secure wipe](https://wiki.gentoo.org/wiki/Secure_wipe "Secure wipe") for more information.

This example will use [GPT](https://wiki.gentoo.org/wiki/GPT "GPT") as disk partition schema. [[fdisk]](https://wiki.gentoo.org/wiki/Fdisk "Fdisk") will be used as the partitioning tool though any partitioning utility will work.

** See also**\
For more information about GPT and [EFI](https://wiki.gentoo.org/wiki/UEFI "UEFI"), see [Disks (AMD64 Handbook)](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks "Handbook:AMD64/Installation/Disks").

### [Simple EFI System Partition Layout]

In most cases, only an ESP is required, to create one on the same disk as the encrypted root:

[CODE] **Partition layout with a single EFI system partition**

    /dev/nvme0n1
     ├── /dev/nvme0n1p1 [EFI]       /efi       1 GB         fat32       Bootloader + support files, kernel, initramfs
     └── /dev/nvme0n1p2 [ROOT]      (root)     ->END        luks        encrypted root partition
          └──  rootfs               /          ->END        btrfs       root filesystem

** Important**\
Some Installkernel layouts (mainly for systems using GRUB) install files to /boot. If such a layout is used, the ESP (/dev/nvme0n1p1 on that example) should be mounted on [/boot]. Check [possible layouts](https://wiki.gentoo.org/wiki/Installkernel "Installkernel") for more information.

#### [Configure GPT label]

First, a fresh partition table is created on [/dev/nvme0n1] with:

`root `[`#`]`fdisk /dev/nvme0n1`

    Welcome to fdisk (util-linux 2.38.1).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

    Device does not contain a recognized partition table.
    Created a new DOS disklabel with disk identifier 0x81391dbc.

`Command (m for help):``g`

    Created a new GPT disklabel (GUID: 8D91A3C1-8661-2940-9076-65B815B36906).

#### [Create the ESP]

With a GPT partition table created, the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP) can be added using **n**:

`Command (m for help):``n`

    Partition number (1-128, default 1):
    First sector (2048-134217694, default 2048):
    Last sector, +/-sectors or +/-size (2048-134217694, default 134215679): +1G

    Created a new partition 1 of type 'Linux filesystem' and of size 1 GiB.

The **ESP** property can be set using **t**:

`Command (m for help):``t`

    Selected partition 1
    Partition type or alias (type L to list all): 1
    Changed type of partition 'Linux filesystem' to 'EFI System'.

#### [Create the Root partition]

The root partition can be created with:

`Command (m for help):``n`

    Partition number (2-128, default 2):
    First sector (2099200-134217694, default 2099200):
    Last sector, +/-sectors or +/-size (2099200-134217694, default 134215679):

    Created a new partition 2 of type 'Linux filesystem' and of size 62 GiB.

The **Linux Root (x86-64)** property can be set using **t**:

`Command (m for help):``t`

    Partition number (1-2, default 2):
    Partition type or alias (type L to list all): 23
    Changed type of partition 'Linux filesystem' to 'Linux Root (x86-64)'.

#### [Apply changes]

Finally, the changes can be written with **w**:

`Command (m for help):``w`

    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.

### [][Split EFI/BOOTx Grub layout]

If an additional boot partition is needed, it can be created in addition to an ESP.

** Note**\
Use of an extended boot partition requires bootloader support.

[CODE] **Partition layout with boot partition**

    /dev/nvme0n1
     ├── /dev/nvme0n1p1 [EFI]       /efi       1 GB         fat32       Bootloader
     ├── /dev/nvme0n1p2 [BOOTX]     /boot      1 GB         ext4        Bootloader support files, kernel, initramfs
     └── /dev/nvme0n1p3 [ROOT]      (root)     ->END        luks        encrypted root partition
          └──  rootfs               /          ->END        btrfs       root filesystem

#### [Configure GPT label]

To create a partition layout using [fdisk], start by creating a fresh partition table on the root disk:

`root `[`#`]`fdisk /dev/nvme0n1`

    Welcome to fdisk (util-linux 2.38.1).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

    Device does not contain a recognized partition table.
    Created a new DOS disklabel with disk identifier 0x81391dbc.

`Command (m for help):``g`

    Created a new GPT disklabel (GUID: 8D91A3C1-8661-2940-9076-65B815B36906).

#### [Create the ESP]

With a GPT partition table created, the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP) can be added using **n**:

`Command (m for help):``n`

    Partition number (1-128, default 1):
    First sector (2048-134217694, default 2048):
    Last sector, +/-sectors or +/-size (2048-134217694, default 134215679): +1G

    Created a new partition 1 of type 'Linux filesystem' and of size 1 GiB.

The **ESP** property can be set using **t**:

`Command (m for help):``t`

    Selected partition 1
    Partition type or alias (type L to list all): 1
    Changed type of partition 'Linux filesystem' to 'EFI System'.

#### [Create the Extended Boot partition]

The boot partition can be created with:

`Command (m for help):``n`

    Partition number (2-128, default 2):
    First sector (2099200-134217694, default 2099200):
    Last sector, +/-sectors or +/-size (2099200-134217694, default 134215679): +1G

    Created a new partition 2 of type 'Linux filesystem' and of size 1 GiB.

The **Linux Extended Boot** property can be set using **t**:

** Note**\
Setting this property is optional, but if set, should match the architecture of the system.

`Command (m for help):``t`

    Partition number (1-2, default 2):
    Partition type or alias (type L to list all): 142
    Changed type of partition 'Linux filesystem' to 'Linux Extended Boot'.

#### [Create the Root partition]

The root partition can be created with:

`Command (m for help):``n`

    Partition number (3-128, default 3):
    First sector (4196352-134217694, default 4196352):
    Last sector, +/-sectors or +/-size (4196352-134217694, default 134215679):

    Created a new partition 3 of type 'Linux filesystem' and of size 62 GiB.

The **Linux Root (x86-64)** property can be set using **t**:

`Command (m for help):``t`

    Partition number (1-3, default 3):
    Partition type or alias (type L to list all): 23
    Changed type of partition 'Linux filesystem' to 'Linux Root (x86-64)'.

#### [Apply changes]

Finally, the changes can be written with **w**:

`Command (m for help):``w`

    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.

## [LUKS setup]

Once partitions have been created, [cryptsetup] can be used to format the LUKS volumes.

### [Create the LUKS encrypted partition]

To prepare the encrypted filesystem, [dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") can be used:

** Note**\
To ensure the **dm_crypt** module is loaded, the following command can be used:

`root `[`#`]`modprobe dm_crypt`

The status of the module can be checked with:

`user `[`$`]`lsmod | grep dm_crypt`

To format the root partition ([/dev/nvme0n1p2]) using LUKS, secured with a passphrase:

`root `[`#`]`cryptsetup luksFormat /dev/nvme0n1p2`

    WARNING!
    ========
    This will overwrite data on /dev/nvme0n1p2 irrevocably.

    Are you sure? (Type 'yes' in capital letters):
    YES
    Enter passphrase for /dev/nvme0n1p2:

#### [LUKS Header Backup]

** Important**\
Do not forget this step, keys/passwords are used to decrypt the LUKS header, if it is destroyed for some reason, the remaining data will only be recoverable with the header file.

The headers can be backed up with:

`root `[`#`]`cryptsetup luksHeaderBackup /dev/nvme0n1p2 --header-backup-file root_headers.img`

### [Open the LUKS volume]

The encrypted device must be opened and mapped before it can be used, this can be done with:

`root `[`#`]`cryptsetup luksOpen /dev/nvme0n1p2 `[`root`]

** Note**\
In this example, the volume is opened and mapped to [/dev/mapper/[root]], as suggested by the [Discoverable Partitions Specification](https://uapi-group.org/specifications/specs/discoverable_partitions_specification/).

### [Set LUKS flags]

On [SSDs](https://wiki.gentoo.org/wiki/SSD "SSD"), allow discard instructions to pass through from the file system by setting the `allow-discards` flag:

`root `[`#`]`cryptsetup refresh --persistent --allow-discards `[`root`]

For more info see [SSD LUKS](https://wiki.gentoo.org/wiki/SSD#LUKS "SSD").

## [Filesystems Preparation]

Once partitions are formatted, and LUKS volumes are unlocked, they must be formatted before they can be mounted and used.

### [ESP]

The [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") on most motherboards can only read [FAT32](https://wiki.gentoo.org/wiki/FAT "FAT") filesystems. To format the ESP:

`root `[`#`]`mkfs.vfat -F32 /dev/nvme0n1p1`

### [Root filesystem]

To format the root filesystem with [Btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs"):

`root `[`#`]`mkfs.btrfs -L rootfs /dev/mapper/`[`root`]

### [Optional: Extended boot formatting]

If used, the extended boot partition must be formatted. Any filesystem which the bootloader supports can be used.

To format the BOOTx partition at [/dev/nvme0n1p2] with [Ext4](https://wiki.gentoo.org/wiki/Ext4 "Ext4"):

`root `[`#`]`mkfs.ext4 -L boot /dev/nvme0n1p2`

## [Gentoo installation]

If this procedure is being followed during a Gentoo install (in place of [Designing a partition scheme](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Designing_a_partition_scheme "Handbook:AMD64/Full/Installation") through [Mounting the root partition](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Mounting_the_root_partition "Handbook:AMD64/Full/Installation")), the install can be completed using the handbook with a few important considerations:

** Important**\
\* [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]] and [[[sys-fs/btrfs-progs]](https://packages.gentoo.org/packages/sys-fs/btrfs-progs)[]] must be installed within the [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot"), before the initramfs is created.

-   An initial RAM filesystem must be built with support for decrypting and mounting the root partition.
-   If a [bootloader](https://wiki.gentoo.org/wiki/Category:Bootloaders "Category:Bootloaders") is being used, it must be configured and installed on unencrypted volumes.

The root file system can be mounted at [/mnt/gentoo] to continue the install with:

`root `[`#`]`mount --label rootfs /mnt/gentoo`

At this point, the Gentoo install can be continued: [Installing a stage tarball](https://wiki.gentoo.org/wiki/Handbook:AMD64/Full/Installation#Installing_a_stage_tarball "Handbook:AMD64/Full/Installation").

## [Initramfs configuration]

** See also**\
For additional configuration including GPG keys, refer to [Full_Disk_Encryption_From_Scratch](https://wiki.gentoo.org/wiki/Full_Disk_Encryption_From_Scratch "Full Disk Encryption From Scratch").

An [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") must be used to decrypt and mount the root partition. This can be accomplished using an image generated by a tool such as [UgRD](https://wiki.gentoo.org/wiki/UgRD "UgRD") or [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut").

** Important**\
This configuration should be done while chrooted, or in the system which the initramfs is being built for.

### [UGRD]

** Tip**\
UGRD (µgRD for Microgram Ramdisk) should automatically detect most LUKS configurations, requiring no additional configuration.

[ugrd] can be installed directly, but is best installed by adding it as a USE flag for installkernel:

[FILE] **`/etc/portage/package.use/ugrd`**

    sys-kernel/installkernel -dracut ugrd

Once configured, installkernel can be re-emerged and will pull UGRD:

`root `[`#`]`emerge -1 sys-kernel/installkernel`

To force an initramfs rebuild, [emerge \--config] can be used on dist-kernel packages:

`root `[`#`]`emerge --config gentoo-kernel-bin`

### [Dracut]

In order to properly decrypt LUKS volumes, Dracut must be configured to use the `crypt` module, and cmdline parameters specifying the LUKS information must be configured:

The following modules must be added to the `add_dracutmodules` directive in [/etc/dracut.conf.d/luks.conf]:

#### [Module configuration]

[FILE] **`/etc/dracut.conf.d/luks.conf`Minimum required component to decrypt LUKS volumes using dracut**

    add_dracutmodules+=" crypt "

** Important**\
The spacing for [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") configuration directives is very important. Ensure there are no spaces between `add_dracutmodules` and *+=\"*, parameters in `add_dracutmodules` must be padded with spaces.

#### [LUKS target configuration]

Dracut can be configured to build with configuration for LUKS hardcoded, first disk information must be obtained:

`root `[`#`]`lsblk -o name,uuid`

    NAME        UUID
    sdb
    ├─nvme0n1p1 BDF2-0139
    ├─nvme0n1p2 b0e86bef-30f8-4e3b-ae35-3fa2c6ae705b
    └─nvme0n1p3 4bb45bd6-9ed9-44b3-b547-b411079f043b
      └─root    cb070f9e-da0e-4bc5-825c-b01bb2707704

[FILE] **`/etc/dracut.conf.d/luks.conf`Embed cmdline parameters for rootfs decryption**

    kernel_cmdline+=" root=UUID=cb070f9e-da0e-4bc5-825c-b01bb2707704 rd.luks.uuid=4bb45bd6-9ed9-44b3-b547-b411079f043b "

** Warning**\
If using GRUB, the `root=` parameter, \"*root=*\" included, should be added to the `GRUB_CMDLINE_LINUX_DEFAULT` option in [/etc/default/grub].

** Note**\
On some setups it may be necessary to specify the `rd.luks.uuid` parameters in `GRUB_CMDLINE_LINUX_DEFAULT` and use `rd.luks.name=UUID=root` for the encrypted root partition.

** Important**\
Embedding the `root=` option into the kernel commandline is required when using [[[sys-boot/systemd-boot]](https://packages.gentoo.org/packages/sys-boot/systemd-boot)[]], but redundant when using [GRUB\'s](https://wiki.gentoo.org/wiki/Grub "Grub") [grub-mkconfig], which will automatically add that parameter.

#### [Systemd]

When using [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"), rebuild it with the USE-flag `cryptsetup`:

[FILE] **`/etc/portage/package.use/systemd`**

    sys-apps/systemd cryptsetup

`root `[`#`]`emerge --ask sys-apps/systemd`

** Note**\
When using [systemd], `rd.luks.uuid` parameters in [dracut.conf] should be moved to cmdline of the bootloader

[FILE] **`/etc/dracut.conf.d/luks.conf`Embed cmdline parameters for rootfs decryption**

    kernel_cmdline+=" root=UUID=cb070f9e-da0e-4bc5-825c-b01bb2707704 "

** Note**\
If you are having trouble booting, consider rebuild [dracut] with the USE-flag [dracut-cpio].

#### [Building the image]

** Important**\
By default, Dracut writes to [/boot] which must be mounted.

** Warning**\
Dracut uses the running kernel version by default, which will likely differ from the installed kernel.

Once Dracut is configured, the new initramfs is generated by:

`root `[`#`]`dracut --kver 6.1.28-gentoo`

** Tip**\
Find possible kernel versions using:

`user `[`$`]`ls /lib/modules`

## [Booting with the initramfs]

### [efibootmgr]

Extensible Firmware Interface systems may boot an EFI stub kernel with initramfs using [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr"). A page relevant example is provided:

`root `[`#`]`efibootmgr --create --disk /dev/nvme0n1 --label "Gentoo" --loader "vmlinuz-6.1.28-gentoo" --unicode "initrd=initramfs-6.1.28-gentoo"`

** Tip**\
If the ESP is on any partition but the first partition, the `--part` number must be specified.

#### [systemd]

If using dracut with systemd, the rd.luks.uuid parameter should be passed in the cmdline, not embedded:

`root `[`#`]`efibootmgr --create --disk /dev/nvme0n1 --label "Gentoo" --loader "vmlinuz-6.1.28-gentoo" --unicode "initrd=initramfs-6.1.28-gentoo rd.luks.uuid=4bb45bd6-9ed9-44b3-b547-b411079f043b"`

##### [UGRD]

UGRD versions \< 2.0 need the \"ugrd.fs.fakeudev\" module enabled in order to prevent boot stalls when using systemd.

### [GRUB]

If [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") is used with the simple disk layout it should be installed with:

`root `[`#`]`grub-install --efi-directory=/boot`

With the split boot layout:

`root `[`#`]`grub-install --efi-directory=/efi`

** Tip**\
In both cases, the current mountpoint of the *EFI System Partition* is used, but the location differs based on the chosen disk layout.

## [See also]

-   [Dm-crypt](https://wiki.gentoo.org/wiki/Dm-crypt "Dm-crypt") --- a disk encryption system using the kernels crypto API framework and device mapper subsystem.
-   [Efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") --- a tool for managing [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot entries.
-   [Full Disk Encryption From Scratch](https://wiki.gentoo.org/wiki/Full_Disk_Encryption_From_Scratch "Full Disk Encryption From Scratch") --- a guide which covers the process of configuring a drive to be encrypted using LUKS and btrfs.
-   [Unlocking Rootfs encryption over SSH](https://wiki.gentoo.org/wiki/Unlocking_Rootfs_encryption_over_SSH "Unlocking Rootfs encryption over SSH")