Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/GRUB/de "GRUB (45% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/GRUB/es "GRUB2 (32% translated)")
-   [français](https://wiki.gentoo.org/wiki/GRUB/fr "GRUB2 (0% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/GRUB/it "GRUB (40% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/GRUB/hu "GRUB (70% translated)")
-   [polski](https://wiki.gentoo.org/wiki/GRUB/pl "GRUB2 (2% translated)")
-   [português do Brasil](https://wiki.gentoo.org/wiki/GRUB/pt-br "GRUB2 (3% translated)")
-   [русский](https://wiki.gentoo.org/wiki/GRUB/ru "GRUB (73% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/GRUB/zh-cn "GRUB (51% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/GRUB/ja "GRUB (98% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/GRUB/ko "GRUB2/ko (24% translated)")

**Resources**

[[]][Home](https://gnu.org/software/grub/)

[[]][Official documentation](https://gnu.org/software/grub/grub-documentation.html)

[[]][Package information](https://packages.gentoo.org/packages/sys-boot/grub)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GNU_GRUB "wikipedia:GNU GRUB")

[[]][GitWeb](https://git.savannah.gnu.org/cgit/grub.git/)

[[]][[#grub](ircs://irc.libera.chat/#grub)] ([[webchat](https://web.libera.chat/#grub)])

**GRUB** is a multiboot secondary [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") capable of loading kernels from a variety of [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on most system architectures. GRUB supports PC BIOS, PC EFI, IEEE 1275 (Open Firmware), SPARC, and MIPS Lemote Yeeloong.

GRUB, or more formally **GRUB 2**, replaces the original \"GRUB Legacy\" (or \"GRUB 1\") with an entirely separate code base featuring a new shell-like syntax for advanced scripting capabilities.

Since GRUB 2 superseded GRUB legacy long ago, today it is commonly called simply \"GRUB\".

** See also**\
For a quick setup approach, see [GRUB2 Quick Start](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start "GRUB2 Quick Start").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Prerequisites]](#Prerequisites)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Additional software]](#Additional_software)
        -   [[1.4.1] [os-prober to automatically detect available operating systems]](#os-prober_to_automatically_detect_available_operating_systems)
        -   [[1.4.2] [libisoburn for rescue image creation with grub-mkrescue]](#libisoburn_for_rescue_image_creation_with_grub-mkrescue)
        -   [[1.4.3] [Boot from ISOs from your main storage - without USB]](#Boot_from_ISOs_from_your_main_storage_-_without_USB)
        -   [[1.4.4] [sys-fs/mdadm for RAID device detection]](#sys-fs.2Fmdadm_for_RAID_device_detection)
-   [[2] [GRUB Bootloader Installation]](#GRUB_Bootloader_Installation)
    -   [[2.1] [UEFI with GPT]](#UEFI_with_GPT)
        -   [[2.1.1] [Partitioning for UEFI with GPT]](#Partitioning_for_UEFI_with_GPT)
            -   [[2.1.1.1] [Partitioning with fdisk]](#Partitioning_with_fdisk)
        -   [[2.1.2] [Installing GRUB for EFI]](#Installing_GRUB_for_EFI)
    -   [[2.2] [BIOS with MBR]](#BIOS_with_MBR)
        -   [[2.2.1] [Partitioning for BIOS with MBR]](#Partitioning_for_BIOS_with_MBR)
    -   [[2.3] [BIOS with GPT]](#BIOS_with_GPT)
        -   [[2.3.1] [Dual-boot with Windows]](#Dual-boot_with_Windows)
        -   [[2.3.2] [Partitioning for BIOS with GPT]](#Partitioning_for_BIOS_with_GPT)
    -   [[2.4] [Open Firmware (IEEE 1275) on PowerPC]](#Open_Firmware_.28IEEE_1275.29_on_PowerPC)
    -   [[2.5] [Install on encrypted partition]](#Install_on_encrypted_partition)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Main configuration file]](#Main_configuration_file)
    -   [[3.2] [Setting configuration parameters]](#Setting_configuration_parameters)
    -   [[3.3] [Enabling or disabling configuration scripts]](#Enabling_or_disabling_configuration_scripts)
    -   [[3.4] [Manipulating configuration scripts]](#Manipulating_configuration_scripts)
-   [[4] [Extended features]](#Extended_features)
    -   [[4.1] [Chainloading]](#Chainloading)
    -   [[4.2] [Password protection of GRUB menu]](#Password_protection_of_GRUB_menu)
    -   [[4.3] [Using framebuffer display]](#Using_framebuffer_display)
        -   [[4.3.1] [HiDPI displays]](#HiDPI_displays)
-   [[5] [Installing a new kernel]](#Installing_a_new_kernel)
    -   [[5.1] [Automatic GRUB reconfiguration]](#Automatic_GRUB_reconfiguration)
-   [[6] [After updating sys-boot/grub]](#After_updating_sys-boot.2Fgrub)
-   [[7] [Troubleshooting]](#Troubleshooting)
    -   [[7.1] [os-prober not running]](#os-prober_not_running)
    -   [[7.2] [Motherboard firmware not finding the .EFI file]](#Motherboard_firmware_not_finding_the_.EFI_file)
    -   [[7.3] [os-prober and UEFI in chroot]](#os-prober_and_UEFI_in_chroot)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)
-   [[10] [References]](#References)

## [Installation]

### [Prerequisites]

The `GRUB_PLATFORMS` variable in [make.conf] controls what **target** GRUB will use with [grub-install]. The **[amd64]** architecture includes a profile default which works for most systems.

[FILE] **`/etc/portage/make.conf`Example of setting the `GRUB_PLATFORMS` variable for EMU, EFI, and PC platforms**

    GRUB_PLATFORMS="emu efi-32 efi-64 pc"

The following platforms are supported depending on the target CPU:

  --------------------------- -------- ------ ------ -------- --------- --------- ---------
           Platform            Target
                                i386    ia64   mips   mipsel   powerpc   sparc64   x86_64
              ARC                No      No     No     Yes       No        No        No
           Coreboot             Yes      No     No      No       No        No      32-bit
              EFI               Yes     Yes     No      No       No        No        Yes
              EMU               Yes     Yes    Yes     Yes       Yes       Yes       Yes
   IEEE 1275 (Open Firmware)    Yes      No     No      No       Yes       Yes     32-bit
           Loongson              No      No     No     Yes       No        No        No
           Multiboot            Yes      No     No      No       No        No      32-bit
             QEMU               Yes      No     No      No       No        No      32-bit
           QEMU-MIPS             No      No    Yes      No       No        No        No
              PC                Yes      No     No      No       No        No      32-bit
  --------------------------- -------- ------ ------ -------- --------- --------- ---------

** Note**\
Whenever the values in the `GRUB_PLATFORMS` variable are adjusted GRUB will need to be re-emerged in order to build the changed binary. Be sure to use the `--newuse --deep` options as shown in the [emerge section](https://wiki.gentoo.org/wiki/GRUB#Emerge "GRUB") below.

The **[amd64]** profiles enable support for (U)EFI functionality by default. When using a BIOS-based system, set `GRUB_PLATFORMS` variable to `pc` to avoid unneeded dependencies.

### [USE flags]

### [USE flags for] [sys-boot/grub](https://packages.gentoo.org/packages/sys-boot/grub) [[]] [GNU GRUB boot loader]

  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+branding`](https://packages.gentoo.org/useflags/+branding)             Enable Gentoo specific branding
  [`+device-mapper`](https://packages.gentoo.org/useflags/+device-mapper)   Enable support for devmapper; required for LUKS or LVM volume detection
  [`+fonts`](https://packages.gentoo.org/useflags/+fonts)                   Build and install fonts for the gfxterm module
  [`+themes`](https://packages.gentoo.org/useflags/+themes)                 Build and install GRUB themes (starfield)
  [`doc`](https://packages.gentoo.org/useflags/doc)                         Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`efiemu`](https://packages.gentoo.org/useflags/efiemu)                   Build and install the efiemu runtimes
  [`libzfs`](https://packages.gentoo.org/useflags/libzfs)                   Enable support for sys-fs/zfs
  [`mount`](https://packages.gentoo.org/useflags/mount)                     Build and install the grub-mount utility
  [`nls`](https://packages.gentoo.org/useflags/nls)                         Add Native Language Support (using gettext - GNU locale utilities)
  [`protect`](https://packages.gentoo.org/useflags/protect)                 Build and install the grub-protect utility
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                         Add support for Simple Direct Layer (media library)
  [`secureboot`](https://packages.gentoo.org/useflags/secureboot)           Automatically sign efi executables using user specified key
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`truetype`](https://packages.gentoo.org/useflags/truetype)               Build and install grub-mkfont conversion utility
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)           Verify upstream signatures on distfiles
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-07 17:58] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

** Important**\
Installing GRUB with [emerge](https://wiki.gentoo.org/wiki/Emerge "Emerge") does not *enable* the boot loader\'s operation. This only installs the \"GRUB system and utilities\" to the appropriate subdirectories of the Gentoo root filesystem. To install GRUB from there so that it will be used when booting the system, additional steps need to be taken. These steps are covered in the [Configuration](https://wiki.gentoo.org/wiki/GRUB#Configuration "GRUB") section.

To install GRUB use the following [emerge] syntax:

`root `[`#`]`emerge --ask --newuse --deep sys-boot/grub`

** Tip**\
On Gentoo, *os-prober* is neither installed nor enabled when installing GRUB, because of security concerns. If this is needed, see the [additional software](#additional_software_os-prober) section for more information.

### [Additional software]

#### [[] os-prober to automatically detect available operating systems]

Optionally, the [os-prober] utility (provided through the [[[sys-boot/os-prober]](https://packages.gentoo.org/packages/sys-boot/os-prober)[]] package) can be installed to let GRUB probe and generate boot entries for other operating systems when running the [grub-mkconfig] command. In most instances, this will enable GRUB to automatically detect other operating systems including Windows 7, 8.1, 10, other distributions of Linux, etc.

`root `[`#`]`emerge --ask --newuse sys-boot/os-prober`

** Tip**\
Due to security concerns, os-prober is disabled by default. Set `GRUB_DISABLE_OS_PROBER=false`` in `[`/etc/default/grub`]` to enable it. See `[`corresponding troubleshooting section`](#os-prober_not_running)`.`

#### [libisoburn for rescue image creation with grub-mkrescue]

[[[dev-libs/libisoburn]](https://packages.gentoo.org/packages/dev-libs/libisoburn)[]] may be installed to allow creation of rescue images with the [grub-mkrescue] utility:

`root `[`#`]`emerge --ask dev-libs/libisoburn`

#### [Boot from ISOs from your main storage - without USB]

[https://wiki.grml.org/doku.php?id=rescueboot](https://wiki.grml.org/doku.php?id=rescueboot)

From Guru:

`root `[`#`]`emerge --ask sys-boot/grml-rescueboot`

Or manually launch discs with GRUB\'s loopback device:

[FILE] **`/etc/grub.d/40_custom`**

    menuentry "systemrescue-11.02-amd64.iso"

After saving the entry, to update GRUB:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

#### [][sys-fs/mdadm for RAID device detection]

[[[sys-fs/mdadm]](https://packages.gentoo.org/packages/sys-fs/mdadm)[]] may be installed to enable RAID device detection:

`root `[`#`]`emerge --ask sys-fs/mdadm`

## [[]GRUB Bootloader Installation]

Installing GRUB as the system\'s boot loader depends on how the system is meant to boot (through which type of firmware, e.g. on PCs either the legacy [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") or its successor [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI")) and how the disk on which the boot loader should be installed is partitioned (e.g. on a PC, whether it is using the [MBR](https://wiki.gentoo.org/wiki/Master_Boot_Record "Master Boot Record") or the [GPT](https://wiki.gentoo.org/wiki/GPT "GPT") [partition](https://wiki.gentoo.org/wiki/Partition "Partition") layout).

This article covers the following situations:

-   [BIOS with MBR](https://wiki.gentoo.org/wiki/GRUB#BIOS_with_MBR "GRUB") or (U)EFI using the CSM (often called \'BIOS mode\' or \'legacy/compatibility mode\')
-   [BIOS with GPT](https://wiki.gentoo.org/wiki/GRUB#BIOS_with_GPT "GRUB")
-   [UEFI with GPT](https://wiki.gentoo.org/wiki/GRUB#UEFI_with_GPT "GRUB"), the native (U)EFI boot mode
-   [Open Firmware (IEEE 1275) on PowerPC](https://wiki.gentoo.org/wiki/GRUB#Open_Firmware_.28IEEE_1275.29_on_PowerPC "GRUB")

Select the installation instructions appropriate for the system.

### [[] UEFI with GPT]

** Warning**\
Even though 64-bit processors of Intel/AMD architecture (\"x86_64\", for which Gentoo uses the **[amd64]** notation) support running 32-bit software, it is not possible for an EFI implementation to do the same. A 64-bit EFI will not be able to run 32-bit [.efi] loaders! It should be noted that some early 64-bit-capable systems, used a 32-bit implementation of EFI, like some early MacBooks (Intel Core 2) and some pre-2010 Windows computers. In such cases, even though the processor is 64-bit, (U)EFI is implemented as 32-bit software, so `efi-32` would be the correct GRUB platform.

** Note**\
If the CSM is used, refer to [BIOS with MBR](https://wiki.gentoo.org/wiki/GRUB#BIOS_with_MBR "GRUB") or [BIOS with GPT](https://wiki.gentoo.org/wiki/GRUB#BIOS_with_GPT "GRUB") instead. CSM stands for \"Compatibility Support Module\" and is a BIOS emulation, making the UEFI behave like a BIOS. In the firmware setup user interface it is often called \"Legacy Mode\" or \"Compatibility Mode\". CSM has always been optional and was phased out on mainstream systems (such as PCs) in 2020.

#### [Partitioning for UEFI with GPT]

UEFI systems boot from executable files ([.efi] files) in a variant of Microsoft\'s Portable Executable format ---PE32+, specifically---, on their [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP). The EFI System Partition can be just about any size, [with implementation considerations in mind](https://www.ctrl.blog/entry/esp-size-guide.html).

** Important**\
For UEFI GPT boot, the system *must* have a dedicated ESP containing a [FAT](https://wiki.gentoo.org/wiki/FAT "FAT") filesystem.

Only the bootloader\'s [.efi] file is *required* to be in EFI System Partition. Typically, [/boot] contains the kernels, [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") if needed, and GRUB\'s configuration file and support files.

** Note**\
The EFI System Partition is usually mounted at [/boot], [/boot/efi] or [/efi]. Using [/efi] allows files like the kernel, initramfs and bootloader support files to be stored on a separate partition and filesystem, or on the root filesystem itself; the later requires that GRUB can access the root filesystem and read the required files, which may not always be possible or very hard to set up (like with root filesystem encryption).

A size of 128MB for the EFI System Partition is reasonable, this allows multiple PE32+ [.efi] files to be stored. There is little harm in keeping backups of working PE32+ files, which could still be booted if a new one is installed.

Create the partition using the partitioning [tool of choice](https://wiki.gentoo.org/wiki/Partition#GUID_Partition_Table_.28GPT.29 "Partition").

##### [Partitioning with fdisk]

** Note**\
In the example contained in [Preparing the disks](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Disks "Handbook:AMD64/Installation/Disks"), an EFI System Partition with a FAT32 filesystem mounted at [/efi] is shown. Depending on the preferred system configuration, a separate partition for [/boot] may be desirable, e.g. in the case of filesystem encryption.

If using [fdisk] to do the partitioning, start by opening the disk for modification, [/dev/sda] in this example:

`root `[`#`]`fdisk /dev/sda`

    Welcome to fdisk (util-linux 2.38.1).
    Changes will remain in memory only, until you decide to write them.
    Be careful before using the write command.

A new partition table can be created using **g**:

`Command (m for help):``g`

    Created a new GPT disklabel (GUID: 4AB36B49-BAAD-D544-AC45-E3154565018D).

A new partition can be created using **n**:

`Command (m for help):``n`

    Partition number (1-128, default 1): 1
    First sector (2048-121012190, default 2048):
    Last sector, +/-sectors or +/-size (2048-121012190, default 121010175): +128M

    Created a new partition 1 of type 'Linux filesystem' and of size 128 MiB.

Once the partition is created, its Partition Type GUID must be set to that of the EFI System Partition; this can be accomplished with the **t** option, to change the *partition type*, and then selecting **1** to set it to \"EFI System Partition\":

`Command (m for help):``t`

    Selected partition 1
    Partition type or alias (type L to list all): 1
    Changed type of partition 'Linux filesystem' to 'EFI System'.

Finally, the changes can be saved by running **w**:

`Command (m for help):``w`

    The partition table has been altered.
    Calling ioctl() to re-read partition table.
    Syncing disks.

Now, the partition can be formatted to use the FAT32 filesystem with:

`root `[`#`]`mkfs.fat -F 32 -n efi-boot /dev/sda1 `

`root `[`#`]`mount /dev/sda1 /efi `

`root `[`#`]`mkdir -p /efi/EFI`

To determine the *partition UUID* (PARTUUID) of the new partition, the following command can be used:

`user `[`$`]`lsblk -o name,partuuid`

    NAME   PARTUUID
    sda
    └─sda1 20f3d6cc-9781-3640-9232-0f5a8c662a60

To create a [fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab") entry for this partition:

[FILE] **`/etc/fstab`Adding the ESP\'s mountpoint**

    PARTUUID=20f3d6cc-9781-3640-9232-0f5a8c662a60       /efi      vfat    noauto,noatime  1 2

#### [Installing GRUB for EFI]

** Note**\
Gentoo\'s **[amd64]** profiles set a reasonable default for the `GRUB_PLATFORMS` variable, and [grub-install] can usually figure out whether to install GRUB for EFI, for BIOS with MBR or for BIOS with GPT, so setting `GRUB_PLATFORMS` in [/etc/portage/make.conf] is usually not necessary. Users might want to set it so that it matches their computer\'s platform, to make [emerge sys-boot/grub] install fewer files. As mentioned before, 32-bit UEFI systems need `efi-32` set in `GRUB_PLATFORMS`.

Before installing GRUB, the EFI System Partition must be mounted. If there is an entry for it in the [fstab](https://wiki.gentoo.org/wiki//etc/fstab "/etc/fstab"), it can be mounted just by specifying the corresponding mountpoint. Assuming it is [/efi], like in the example from the Handbook:

`root `[`#`]`mount /efi`

[grub-install] copies GRUB\'s support files to [/boot/grub], GRUB\'s PE32+ executable to the [\\EFI\\gentoo] directory of the ESP with name [grubx64.efi] (making its full pathname [/efi/EFI/gentoo/grubx64.efi] if the ESP is mounted at [/efi]), and calls [[efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr")] to add a boot entry.

** Important**\
In order for [grub-install]\'s call to [efibootmgr] to succeed, the [efivarfs] pseudo-filesystem must be mounted read-write, before using the [grub-install] command. If support for this pseudo-filesystem was built as a module, the [efivarfs] kernel module must be loaded.

If the ESP is mounted at [/boot/efi]:

`root `[`#`]`grub-install`

    Installation finished. No error reported.

If the ESP is mounted elsewhere, an `--efi-directory` option specifying its mountpoint\'s pathname must be used. So, if the ESP is mounted at [/efi], like in the example from the Handbook:

`root `[`#`]`grub-install --efi-directory=/efi`

    Installation finished. No error reported.

** Note**\
By default, GRUB installs targeting the platform of system which the command is executed on. If another system platform is used (e. g. if the computer was booted in CSM mode, making the platform BIOS with GPT), the `--target=x86_64-efi` option (or `--target=i386-efi` for a 32-bit UEFI target) can be used to target an EFI platform.

** Note**\
The `--removable` option can be used to install GRUB\'s PE32+ executable to the [\\EFI\\BOOT] directory of the ESP with name [BOOTX64.efi] (making its full pathname [/efi/EFI/BOOT/BOOTX64.efi] if the ESP is mounted at [/efi]). This is only recommended when installing to a removable medium, or when installing on a computer with limited UEFI firmware that does not support boot entries with arbitrary pathnames very well. See also [EFI System Partition #Removable media](https://wiki.gentoo.org/wiki/EFI_System_Partition#Removable_media "EFI System Partition").

### [[] BIOS with MBR]

** Note**\
When the system is meant to dual-boot with another (pre-installed) operating system, such as Microsoft Windows, make sure that the Linux bootloader can coexist or dual-boot both operating systems. On PCs it is recommended to use the same boot method as the pre-installed system, e.g. when Windows is using the legacy MBR partitioning, it is also booted in \'legacy BIOS\' mode (UEFI calls it CSM, short for Compatibility Support Module, in essence a BIOS emulation). If the mode is changed, e.g. from EFI-CSM (BIOS mode) to native (U)EFI mode, the pre-installed system will most certainly no longer be bootable.

Make sure that the [/boot] location is available - if this uses a separate partition, make sure that it is mounted:

`root `[`#`]`mount /boot`

Run the [grub-install] command to copy the relevant files to [/boot/grub]. On the PC platform, this also installs a boot image to the Master Boot Record (MBR) or a partition\'s boot sector. If all goes well, after running [grub-install] an output such as the one below is to be expected:

`root `[`#`]`grub-install /dev/sda`

    Installation finished. No error reported.

[grub-install] accepts a `--target` option to set the CPU architecture and system platform. If unspecified, [grub-install] will attempt to guess the proper values; on an **[amd64]**/**[x86]** system it will use `i386-pc` by default. [grub-install] also accepts a `--boot-directory` option to tell the GRUB installer which directory to look for the boot files. This defaults to the current [/boot] but is useful when trying to move a root partition.

#### [Partitioning for BIOS with MBR]

Be sure to leave enough free space before the first partition. Starting the first partition at sector 2048 leaves at least 1 MiB of disk space for the master boot record. It is recommended (but not mandatory) to create an additional partition for GRUB called the *BIOS boot partition*. This partition just needs to be defined, but not formatted. It is only needed if the system is later migrated to the GPT partition layout. When sticking with MBR, this is not needed.

If the [Gentoo installation instructions](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") were followed, this BIOS boot partition will already be available.

### [[] BIOS with GPT]

** Warning**\
Although GPT was not designed for legacy BIOS systems, it defines a [protective MBR](https://en.wikipedia.org/wiki/GUID_Partition_Table#Protective_MBR_(LBA_0)) to maintain compatibility and prevent MBR-based utilities from misinterpreting GPT disks. In dual-boot setups with legacy OSes that rely on MBR (common in BIOS-based systems), partitions must be accessed via the MBR. This is achievable using hybrid GPT/MBR partitions, which combine a standard GPT layout with a modified MBR to bridge compatibility. However, this approach comes with some limitations.

On a BIOS system with GPT partitioning, GRUB relies on a partition called \"BIOS boot partition\". This partition is not formatted with a file system, instead [grub-install] will copy parts of the boot loader to it. The \"BIOS boot partition\" is not the same partition as a /boot partition.

** Note**\
See also [What is the BIOS boot partition?](https://wiki.gentoo.org/wiki/Handbook:X86/Blocks/Disks#What_is_the_BIOS_boot_partition.3F "Handbook:X86/Blocks/Disks") in the **[x86]** Handbook.

If a [/boot] partition is needed, start by mounting the [/boot] partition:

`root `[`#`]`mount /boot`

If all goes well, after running the [grub-install] command an output such as the one below is to be expected:

`root `[`#`]`grub-install /dev/sda`

    Installation finished. No error reported.

[grub-install] accepts a `--target` option to set the CPU architecture and system platform. If unspecified, [grub-install] will attempt to guess the correct values; on an **[amd64]**/**[x86]** system in BIOS mode it will use `i386-pc` by default and in conjunction with a GUID partition table (GPT) a \"BIOS boot partition\" will be automatically used when present.

[grub-install] also accepts a `--boot-directory` option to tell the GRUB installer which directory to look in for the boot files. This defaults to the current [/boot] but is useful when trying to move a root partition.

#### [Dual-boot with Windows]

When the system is meant to dual-boot with Microsoft Windows installed in BIOS mode, full and native GPT partitioning isn\'t possible. Windows only allows to be booted from an MBR partition when in BIOS mode, which includes the BIOS emulation mode of (U)EFI called \'CSM\'. For Linux however it is still possible to use a GPT partitioning scheme even from BIOS (or EFI-CSM) mode, but for the dual-boot with Windows this requires hybrid partitioning: up to four partitions can be defined in both the GPT and the MBR partition tables simultainiously.

** Note**\
Traditionally x86-PCs used a BIOS as firmware. After the switch to (U)EFI on PCs (around 2005) there used to be a BIOS emulation called \'Compatibility Support Module\' (CSM), PCs were therefore still compatible with existing operating systems. On mainstream PCs the EFI-CSM has been phased out since 2020. Even before 2020 some (U)EFI implementations, such as servers, lacked the CSM completely. \'Legacy BIOS mode\' is therefore no longer available on modern UEFI systems. UEFI in its native boot mode demands the GUID Partition Table (GPT), a pre-installed operating system will therefore already be using a GPT partitioning scheme.

An already installed Windows will refuse to boot when the boot mode or the partitioning scheme is changed. Also, older Windows systems don\'t support GPT (or EFI) at all, demanding that a BIOS or the EFI-CSM along with an MBR must be used. If Windows supports EFI it can be re-installed in the native UEFI mode and the GPT partitioning scheme, as well as Linux; see section [UEFI with GPT](https://wiki.gentoo.org/wiki/GRUB#UEFI_with_GPT "GRUB").

[Hybrid partitioning](https://wiki.gentoo.org/wiki/Hybrid_partition_table "Hybrid partition table") between GPT and MBR creates both a valid GPT partition table and a valid MBR partition table at the same time, but limits the total number of hybrid partitions to four because of the four primary partition limit of the MBR. Since the ESP (the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") holding the EFI bootloaders) takes up one partition this leaves only three shared partitions between MBR and GPT. When one partition is used for Windows and one for Linux, there is only one additional hybrid partition possible, like a separate Linux [/boot] partition or a shared data partition between the two operating systems.

** Warning**\
Normally, a GPT partition table will always also create an MBR partition table which holds only one partition spanning over the whole disk. This will ensure that older software doesn\'t mistake the disk as \'empty\'. The MBR with its protective partition is therefore called a \'protecive MBR\' and is part of the GPT specification. By defining hybrid partitions, this protective feature of the GPT is sacrificed! Legacy software will no longer see used space when analyzing the hybrid MBR. Software that is unaware of the GPT and only sees the MBR may mistake undefined disk space as unused and empty space. Data written outside the defined MBR partitions may cause data loss to the underlying GPT partitions!

If there are two physical disks available to the system, a great solution is to have one disk use the GPT and the other the MBR partitioning scheme. Normally, the Windows installation uses only one partition as \'system partition\' and \'boot partition\', called \'drive C:\'. When in BIOS mode the initial partition for booting, the \'system partition\', must be an MBR partition. This applies to every Windows version since Windows XP and includes Windows 10. Since Windows Vista (actually Windows XP x64 Edition) the Microsoft operating system supports accessing GPT partitions. The solution is to relocate the \'system partition\' part of an installation to the MBR partitioned disk, and convert the \'boot partition\' (the one containing \\WINDOWS) into a GPT partitioned disk. Windows can thereafter access all the GPT partitions on the one disk, and will continue to use the MBR partitions (or hybrid partitions) on the disk containing the \'system partition\'. The Windows installation (containing \\WINDOWS) would be a GPT partition, even when booted in BIOS mode. Windows 11 no longer supports BIOS/CSM/MBR mode.

#### [Partitioning for BIOS with GPT]

When a GPT partition table is present on the system, a small *BIOS boot partition* with type `EF02` (which is different from the *EFI System Partition (ESP)* which has type `EF00`) will need to be available. 1 MiB will be enough to work, but 2-4 MiB is a safer option. This BIOS boot partition will hold the stage 2 of the bootloader. BIOS boot partitions do not need to be formatted with a filesystem; the [grub-install] command will overwrite any existing filesystem with one of its own.

** Important**\
The BIOS boot partition is *not* the same partition that is commonly mounted at [/boot]. The [/boot] and BIOS boot are different partitions and should be handled separately. The BIOS boot partition should *not* be regularly mounted on the system (i.e., it should *not* be defined in [/etc/fstab]). The [/boot] partition *can* be regularly mounted with no issues and therefore can be present in the [/etc/fstab] file.

To set a partition as a BIOS partition use the command-line tool [parted] ([[[sys-block/parted]](https://packages.gentoo.org/packages/sys-block/parted)[]]) by typing (change `1` to the number of the partition to mark as a BIOS boot partition!):

`(parted)``set 1 bios_grub on`

With [[[sys-apps/gptfdisk]](https://packages.gentoo.org/packages/sys-apps/gptfdisk)[]]\'s [cgdisk] utility, this is accomplished by setting the partition type to `0xEF02` and giving it a label of `gptbios`.

An EFI System Partition is not required, but it would be sensible to make sure that the BIOS boot partition is large enough to be converted to one, should the system motherboard later be upgraded to an UEFI board.

The following is the output of pressing the [p] key using the [gdisk] utility on a GPT-partitioned disk with both a BIOS boot \[0xEF02\] partition and an EFI \[0xEF00\] partition:

`root `[`#`]`gdisk /dev/sdc`

    GPT fdisk (gdisk) version 0.8.1

    Partition table scan:
      MBR: protective
      BSD: not present
      APM: not present
      GPT: present

    Found valid GPT with protective MBR; using GPT.

    Command (? for help): p
    Disk /dev/sdc: 976773168 sectors, 465.8 GiB
    Logical sector size: 512 bytes
    Disk identifier (GUID): AA369F4D-37A4-4C0D-A357-DC24B99A6337
    Partition table holds up to 128 entries
    First usable sector is 34, last usable sector is 976773134
    Partitions will be aligned on 2048-sector boundaries
    Total free space is 2014 sectors (1007.0 KiB)

    Number  Start (sector)    End (sector)  Size       Code  Name
       1            2048       828377087   395.0 GiB   8E00  Linux LVM
       2       828377088       891291647   30.0 GiB    0700  Microsoft basic data
       3       891291648       975177727   40.0 GiB    0700  Microsoft basic data
       4       975177728       976754687   770.0 MiB   8300  Linux filesystem
       5       976754688       976756735   1024.0 KiB  EF02  BIOS boot partition
       6       976756736       976773134   8.0 MiB     EF00  EFI System

    Command (? for help):

** Note**\
The `0x` hexadecimal prefix does not need to be entered for GPT when using [fdisk].

Using the same setup, the [parted] utility gives output with slightly different syntax:

`root `[`#`]`parted /dev/sdc`

    GNU Parted 3.0
    Using /dev/sdc
    (parted) print
    ...
    Sector size (logical/physical): 512B/512B
    Partition Table: gpt

    Number  Start   End    Size    File system  Name                  Flags
     1      1049kB  424GB  424GB                Linux LVM             lvm
     2      424GB   456GB  32.2GB               Microsoft basic data
     3      456GB   499GB  42.9GB               Microsoft basic data
     4      499GB   500GB  807MB   ext2         Linux filesystem
     5      500GB   500GB  1049kB               BIOS boot partition   bios_grub
     6      500GB   500GB  8396kB               EFI System            boot

    (parted)

Creating partitions in [gdisk] is straightforward for users familiar with the [fdisk] partitioning utility. After starting [gdisk], type [n] (for new) in the main menu, provide beginning and end sectors (if needed), and set the partition type to `EF00` for an EFI system partition.

Users who have followed the [Gentoo installation instructions](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") will already have the proper partitioning layout set up.

### [][[] Open Firmware (IEEE 1275) on PowerPC]

See [GRUB on Open Firmware (PowerPC)](https://wiki.gentoo.org/wiki/GRUB_on_Open_Firmware_(PowerPC) "GRUB on Open Firmware (PowerPC)").

### [Install on encrypted partition]

If the whole disk is encrypted, including [/boot], extra steps need to be taken, to allow GRUB to decrypt and mount the device.

The [device-mapper](https://www.gentoo.org/support/use-flags/) [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") needs to be set when emerging the GRUB package. Then the [[[sys-fs/cryptsetup]](https://packages.gentoo.org/packages/sys-fs/cryptsetup)[]] package needs to be installed. The partition needs to be encrypted as [luks1](https://wiki.gentoo.org/wiki/Dm-crypt#Full_disk_encryption_booting "Dm-crypt") partition type.

After installing GRUB on the device, depending on the way the kernel is setup, [initramfs](https://wiki.gentoo.org/wiki/Dm-crypt_full_disk_encryption#Generating_an_initramfs "Dm-crypt full disk encryption") might need to be modified in order for the system to boot completely. If a [distribution kernel](https://wiki.gentoo.org/wiki/Kernel#Distribution_kernels "Kernel") is installed, [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") will be installed on the system as well and can be used to finish the configuration.

## [[] Configuration]

Once GRUB has been installed, it can be configured to suit the specific system. In most cases, no additional configuration is required.

### [Main configuration file]

The [grub-mkconfig] script is used to generate a grub configuration. It uses the scripts under [/etc/grub.d/\*] together with the [/etc/default/grub] configuration file to generate the final [/boot/grub/grub.cfg] - the only configuration file used by GRUB itself.

  -------------------------------------------------------------------------------------------------------------- --------------------- -------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  File                                                                                                           Format                Edits recommended?   Description
  [/usr/sbin/grub-mkconfig]   POSIX shell script    No                   Installed as part of the [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]]:2 package. Run this script to generate [/boot/grub/grub.cfg] after configuring the files described below.
  [/boot/grub/grub.cfg]       GRUB shell script     No                   The file generated by [grub-mkconfig]. This file is evaluated by GRUB\'s built-in script interpreter and doesn\'t necessarily support all POSIX commands or syntax. See the [scripting reference](https://www.gnu.org/software/grub/manual/grub.html#Shell_002dlike-scripting) in the GRUB manual for supported features. Be aware that modifications to this file won\'t persist to the next time [grub-mkconfig] is run.
  [/etc/grub.d/\*]            POSIX shell scripts   Maybe                Each script under [/etc/grub.d/\*] that has its execute bit set is evaluated in sequence, and the stdout is concatenated to form the final [/boot/grub/grub.cfg] (or whatever file is given to the [grub-mkconfig] `-o` option). These scripts use the current system shell and therefore can use any supported syntax. Ideally they should be POSIX-compatible scripts, and the output script must be compatible with the GRUB interpreter. It may be necessary to disable or add scripts. For instance, to add menu items that couldn\'t be automatically generated.
  [/boot/grub/custom.cfg]     GRUB shell script     Maybe                The /etc/grub.d/41_custom script will reference this file to be read in at boot time if it exists. This file provides a place to add additional entries or commands and does not require regeneration of the main grub.cfg file.
  [/etc/default/grub]         POSIX shell script    Yes                  In most cases this is the only file that should be modified directly. It is mainly used to assign variables used by the scripts in [/etc/grub.d] to generate a working configuration file. See [GRUB configuration variables](https://wiki.gentoo.org/wiki/GRUB/Configuration_variables "GRUB/Configuration variables") or the [official reference](https://www.gnu.org/software/grub/manual/grub.html#Simple-configuration) for supported variables.
  -------------------------------------------------------------------------------------------------------------- --------------------- -------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

GRUB does not require the administrator to manually maintain a boot option configuration (as is the case with boot loaders such as GRUB Legacy and [LILO](https://wiki.gentoo.org/wiki/LILO "LILO")). Instead it can generate its configuration file ([/boot/grub/grub.cfg]) using the [grub-mkconfig] command. This utility will use the scripts in [/etc/grub.d/] and the settings in [/etc/default/grub].

** Warning**\
The [grub-mkconfig] utility does not work properly when using software RAID. Manual configuration of the scripts in [/etc/grub.d/] is necessary, as otherwise after installation the system will be left in a non-bootable state.

After modifying one or more settings, run the [grub-mkconfig] utility with the `-o` option pointing to the output file located at [/boot/grub/grub.cfg] (this is GRUB\'s default output location):

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub.cfg ...
    Found linux image: /boot/vmlinuz-3.3.0-gentoo
    done

Each time the [grub-mkconfig] utility is called a new configuration will be generated.

** Warning**\
If [grub-mkconfig] does not report any found entries then no entries were found. In this case GRUB will offer no boot selections when upon system restart which may be a tricky, time consuming situation to resolve. Make sure the output is satisfactory before restarting the system.

### [Setting configuration parameters]

The following variables in [/etc/default/grub] are the most common ones to set to control how GRUB will function:

  ----------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------
  Variable                                  Explanation                                                                                                                                                                                                                                                                                                                                          Default value
  `GRUB_DEFAULT`                 Defines the default menu entry selected on boot. May be a numeric index (starts from 0), a menu title, or \"saved\". Accessing menus requires the value to be put in double quotes and seperated by a bigger than symbol, for example, `"1>3"` will open the second submenu and the fourth option in it.                                             Defaults to first detected entry.
  `GRUB_TIMEOUT`                 Delay (in seconds) before booting default menu entry. Set to `0` to boot immediately or `-1` to wait indefinitely.                                                                                                                                                                                                                                   The default is 5 seconds.
  `GRUB_CMDLINE_LINUX`           Parameters to be passed on the kernel command line for all Linux menu entries. For instance, to support hibernation, users will need to add `GRUB_CMDLINE_LINUX="resume=/dev/sdXY"` with [/dev/sdXY] being the swap partition.
  `GRUB_CMDLINE_LINUX_DEFAULT`   Parameters to be passed on the kernel command line for non-recovery Linux menu entries.
  `GRUB_DEVICE`                  The initial root device (i.e. the kernel\'s `root=` parameter). Set this to override the [grub-mkconfig] command\'s root device auto-detection. For example, `GRUB_DEVICE=/dev/ram0` will force `root=/dev/ram0` to be used in the kernel command line.
  ----------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------

For a more complete list, please refer to the [configuration variables](https://wiki.gentoo.org/wiki/GRUB/Configuration_variables "GRUB/Configuration variables") sub-page and as the [info] page of [grub-mkconfig].

After modifying the parameters, regenerate the GRUB configuration file with [grub-mkconfig].

### [Enabling or disabling configuration scripts]

The directory [/etc/grub.d/] contains the scripts that [grub-mkconfig] uses to generate a [grub.cfg] file. By default the contents of this directory should be similar to the following:

`user `[`$`]`ls /etc/grub.d/`

    00_header  10_linux  20_linux_xen  30_os-prober  40_custom  41_custom README

GRUB will use all installed scripts that are marked as executable (which by default, they all are). To disable any of the scripts simply remove the executable bit from the script\'s file permissions using the [chmod] command. In the following example every script but [00_header] and [10_linux] are disabled:

`root `[`#`]`chmod -x /etc/grub.d/`

After modifying the scripts (or removing the executable bit), regenerate the configuration file using [grub-mkconfig].

### [Manipulating configuration scripts]

Some features or functionalities are only possible to be exploited by modifying the configuration scripts. For instance, to support dual-booting with FreeBSD, the following manipulation needs to be done.

Change the [/etc/grub.d/40_custom] script to:

[FILE] **`/etc/grub.d/40_custom`Adding an entry for dual booting**

    menuentry "FreeBSD" --class freebsd --class bsd --class os

[/dev/sda1] or `(hd0,1)` is the partition in which FreeBSD resides. If the normal UFS install was used for the FreeBSD partition then [/dev/sda1] is a container (something like a logical partition). It consists of the swap and root partition. Verify the [40_custom] script is executable by running [ls -la /etc/grub.d/40_custom]. If the executable bit is not set then set it using the [chmod u+x 40_custom] command.

** Note**\
Users familiar with how GRUB Legacy numbered partitions should note partitions starting from 1, not 0, with GRUB.

Next install GRUB and update the configuration file:

`root `[`#`]`grub-install /dev/sda `

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

## [Extended features]

GRUB 2 has many features that make it a very powerful boot loader. It supports:

-   Booting from UEFI platforms.
-   Booting from GPT partitioned drives without needing a hybrid MBR (hybrid MBR can enabled as needed for compatibility or portability).
-   Booting from a [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") formatted [/boot] partition.
-   Booting from a [ZFS](https://wiki.gentoo.org/wiki/ZFS "ZFS") pool.
-   Booting directly from a [btrfs](https://wiki.gentoo.org/wiki/Btrfs "Btrfs") RAID set without needing an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") for early mount setup.
-   Booting directly from logical volume management (such as [LVM2](https://wiki.gentoo.org/wiki/LVM "LVM")).
-   Booting with support for DM-RAID (RAID 0, 1, 4, 5, 6, 9 and 10).
-   Booting from encrypted devices (LUKS).

Some specific features are explained in more detail next.

### [Chainloading]

GRUB 2 was built with a truly improved chainload mode when compared to GRUB Legacy. To chainload another boot loader, use the `chainloader` option.

[FILE] **`/etc/grub.d/40_custom`Chainloading another bootloader**

    menuentry "Custom Super-bootloader example"

For more information on chainloading, please see the [Chainloading](https://wiki.gentoo.org/wiki/GRUB/Chainloading "GRUB/Chainloading") sub-page.

### [Password protection of GRUB menu]

To secure GRUB so it is not possible for anyone to change boot parameters or use the command line, add a user/password combination to GRUB\'s configuration files. The program grub-mkpasswd-pbkdf2 generates password hashes for GRUBː

`user `[`$`]`grub-mkpasswd-pbkdf2`

    Password:
    Reenter password:

    PBKDF2 hash of your password is grub.pbkdf2.sha512.10000.9CA4611006FE96BC77A...

Then, add the following toː

[FILE] **`/etc/grub.d/35_auth:`**

    # Grub user
    echo 'set superusers="<username>"'
    # Grub password
    echo 'password_pbkdf2 <username> '

The above may lock all Grub menu entries, even the default entry. In that case, to allow users to boot some menu entries without a password, see [Securing the grub boot loader](https://daniel-lange.com/archives/75-Securing-the-grub-boot-loader.html).

The permissions for the file need to be properly set before doing grub-mkconfig:

`root `[`#`]`chmod 755 /etc/grub.d/35_auth`

### [Using framebuffer display]

To have GRUB use a [framebuffer](https://wiki.gentoo.org/wiki/Framebuffer "Framebuffer") graphical display, re-emerge GRUB with the `truetype` USE flag enabled. This will install a default True Type font as well as a font conversion utility.

`root `[`#`]`emerge --ask --newuse sys-boot/grub:2`

Proceed to configure the default configuration file located at [/etc/default/grub]. For example:

[FILE] **`/etc/default/grub`Framebuffer related settings**

    # Set resolution and color depth
    GRUB_GFXMODE=1366x768x32

    # Keep resolution when loading the kernel
    GRUB_GFXPAYLOAD_LINUX=keep

    # Set a background image
    GRUB_BACKGROUND="/boot/grub/bg.png"

    # Use a custom font, converted using grub-mkfont utility
    GRUB_FONT="/boot/grub/fonts/roboto.pf2"

    # Set the menu colors
    GRUB_COLOR_NORMAL="light-blue/black"
    GRUB_COLOR_HIGHLIGHT="light-cyan/blue"

#### [HiDPI displays]

On modern displays with high DPI (\"HiDPI\"), e.g. UHD (3840x2160), the standard font will look very small. If you like to have the same font as the kernel, Terminus can be used, which resembles a BIOS built-in textmode font.

To select this font in-kernel, `CONFIG_FONT_TER16x32` has to be enabled.

[KERNEL] **Kernel compiled-in fonts**

    Library routines  --->
          [*] Select compiled-in fonts
          [*] Terminus 16x32 font (not supported by all drivers)

The same font is available as [[[media-fonts/terminus-font]](https://packages.gentoo.org/packages/media-fonts/terminus-font)[]], which can then be used for GRUB as well.

`root `[`#`]`emerge --ask media-fonts/terminus-font`

`root `[`#`]`grub-mkfont -s 32 -o /boot/grub/fonts/terminus32b.pf2 /usr/share/fonts/terminus/ter-u32b.otb`

In the above example the filename chosen for `grub-mkfont` output is `terminus32b.pf2`. The font\'s path has to be accessible to GRUB during boot, so it should reside in the same mount point as GRUB does; this example uses `/boot/grub/fonts`. The font then has to be set as `GRUB_FONT` in `/etc/default/grub` in order to be used.

[FILE] **`/etc/default/grub`Framebuffer related settings**

    # Use a custom font, converted using grub-mkfont utility
    GRUB_FONT="/boot/grub/fonts/terminus32b.pf2"

Updating the GRUB configuration file `grub.cfg` will then activate the configuration with the new font.

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

## [Installing a new kernel]

Whenever a new kernel is installed, GRUB must be reconfigured to recognize it. This can be done using [grub-mkconfig], as shown below, or can be [done manually](https://wiki.gentoo.org/wiki/GRUB2_Quick_Start#Manual_configuration "GRUB2 Quick Start").

** Note**\
Make sure the [/boot] partition is mounted for this step.

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub.cfg ...
    Found linux image: /boot/kernel-3.3.8-gentoo
    Found initrd image: /boot/initramfs-genkernel-x86_64-3.3.8-gentoo
    Found linux image: /boot/kernel-3.2.12-gentoo
    Found initrd image: /boot/initramfs-genkernel-x86_64-3.2.12-gentoo
    done

Note that GRUB only needs to be reconfigured, not *reinstalled* to the boot drive\'s Master Boot Record (MBR). On the other hand, when GRUB itself has been upgraded it does need to be reinstalled on the boot drive, but usually does not need to be reconfigured.

### [Automatic GRUB reconfiguration]

If the package [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] is installed and the [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") [grub] is set, then on every installation of a kernel, [grub-mkconfig] will run automatically.

## [][After updating sys-boot/grub]

After [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]] is updated (either explicitly or via a [world update](https://wiki.gentoo.org/wiki/Upgrading_Gentoo "Upgrading Gentoo")), the core boot files and modules should be reinstalled. This is mentioned in the following post-install message:

[CODE]

    * Re-run grub-install to update installed boot code!
    * Re-run grub-mkconfig to update grub.cfg!

To re-install these files, follow the steps in the relevant sections:

-   [Installing GRUB for EFI](#Installing_GRUB_for_EFI)
-   [BIOS with MBR](#BIOS_with_MBR)
-   [BIOS with GPT](#BIOS_with_GPT)
-   [Open Firmware (IEEE 1275) on PowerPC](#Open_Firmware_.28IEEE_1275.29_on_PowerPC)
-   [Install on encrypted partition](#Install_on_encrypted_partition)

## [Troubleshooting]

** See also**\
For more troubleshooting, please refer to the **[Troubleshooting](https://wiki.gentoo.org/wiki/GRUB/Troubleshooting "GRUB/Troubleshooting")** sub-article.

Most of the issues can be resolved by ensuring that the partition layout is correct. Make sure enough space is available before the first partition of the disk, or optionally make sure that a *BIOS boot partition* is available. Also verify that [/boot/grub/grub.cfg] was correctly generated with [grub-mkconfig], or generate one with a custom menu entry.

### [[] os-prober not running]

When running the [grub-mkconfig] command, [os-prober] is not running as expected, even though it is installed:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub configuration file ...
    Found linux image: /boot/vmlinuz-5.11.14-gentoo-x86_64
    Found initrd image: /boot/amd-uc.img /boot/initramfs-5.11.14-gentoo-x86_64.img
    Warning: os-prober will not be executed to detect other bootable partitions.
    Systems on them will not be added to the GRUB boot configuration.
    Check GRUB_DISABLE_OS_PROBER documentation entry.
    Adding boot menu entry for UEFI Firmware Settings ...
    done

This can be corrected by setting the `GRUB_DISABLE_OS_PROBER` variable to `false` in [/etc/default/grub] file.

[FILE] **`/etc/default/grub`**

    GRUB_DISABLE_OS_PROBER=false

Upon the next run, [grub-mkconfig] should find additional bootable partitions:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

    Generating grub configuration file ...
    Found linux image: /boot/vmlinuz-5.11.14-gentoo-x86_64
    Found initrd image: /boot/amd-uc.img /boot/initramfs-5.11.14-gentoo-x86_64.img
    Warning: os-prober will be executed to detect other bootable partitions.
    It's output will be used to detect bootable binaries on them and create new boot entries.
    Found Windows Boot Manager on /dev/nvme0n1p2@/efi/Microsoft/Boot/bootmgfw.efi
    Adding boot menu entry for UEFI Firmware Settings ...
    done

### [Motherboard firmware not finding the .EFI file]

Some especially older (pre-2020) motherboards from certain manufacturers seem to only support one location for PE32+ files in the EFI System Partition (ESP): the [fallback or removable media path](https://wiki.gentoo.org/wiki/EFI_System_Partition#Removable_media "EFI System Partition"). If this seems to be the case, GRUB\'s [] file can be renamed and moved to the [\\EFI\\BOOT] directory of the ESP. First, make sure the ESP is mounted. Presuming it is mounted at [/efi], as suggested in the Handbook, execute:

`root `[`#`]`mkdir -p /efi/EFI/BOOT `

`root `[`#`]`cp /efi/EFI/gentoo/grubx64.efi /efi/EFI/BOOT/BOOTX64.efi `

On a 32-bit EFI implementation use name `BOOTIA32.efi` instead:

`root `[`#`]`cp /efi/EFI/gentoo/grubia32.efi /efi/EFI/BOOT/BOOTIA32.efi `

Alternatively, the `--removable` option of [grub-install] can be used to generate this file automatically:

`root `[`#`]`grub-install --efi-directory=/efi --removable`

    Installation finished. No error reported.

This should aid the motherboard firmware in loading GRUB\'s executable. Reboot the system to see if the firmware now correctly loads GRUB.

### [os-prober and UEFI in chroot]

The [[[sys-boot/os-prober]](https://packages.gentoo.org/packages/sys-boot/os-prober)[]] utility is used to discover alternate installs, such as Microsoft Windows. To function properly, it needs to have access to information from the live environment\'s udev to test for the EFI System Partition.

Run these commands in the host environment to provide the required files (example shows Gentoo mounted on [/mnt/gentoo] like in the Handbook):

`root `[`#`]`mkdir -p /mnt/gentoo/run/udev `

`root `[`#`]`mount -o bind /run/udev /mnt/gentoo/run/udev `

`root `[`#`]`mount --make-rslave /mnt/gentoo/run/udev `

## [See also]

-   [Secure Boot/GRUB](https://wiki.gentoo.org/wiki/Secure_Boot/GRUB "Secure Boot/GRUB") --- This article explains how to set up [GRUB] to work with [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot").
-   [GRUB2 Migration](https://wiki.gentoo.org/wiki/GRUB2_Migration "GRUB2 Migration") --- provides instructions for smooth migration from [GRUB Legacy](https://wiki.gentoo.org/wiki/GRUB_Legacy "GRUB Legacy") to [GRUB].
-   [Advanced storage subarticle](https://wiki.gentoo.org/wiki/GRUB/Advanced_storage "GRUB/Advanced storage") the necessary steps are documented on how to install and use GRUB on more advanced storage situations, such as software RAID, logical volumes or encrypted file systems.
-   [Chainloading subarticle](https://wiki.gentoo.org/wiki/GRUB/Chainloading "GRUB/Chainloading") the use of GRUB to boot other boot loaders is described. This is important to read when dual-booting systems, or when GRUB needs to be configured to boot ISO files.
-   [Configuration variables subarticle](https://wiki.gentoo.org/wiki/GRUB/Configuration_variables "GRUB/Configuration variables") an exhaustive list of GRUB configuration variables, as used by [/etc/default/grub], is documented.
-   [Hybrid partition table](https://wiki.gentoo.org/wiki/Hybrid_partition_table "Hybrid partition table") the use of a mixed MBR/GPT setup is documented, as well as how to use such hybrid partition layout with GRUB.
-   In [Troubleshooting subarticle](https://wiki.gentoo.org/wiki/GRUB/Troubleshooting "GRUB/Troubleshooting") a list of common GRUB errors (with their solutions) is presented.

## [External resources]

For more information, please see:

-   [GNU GRUB 2 manual page](https://www.gnu.org/software/grub/manual/grub.html)
    -   [Network (PXE) section of GRUB](https://www.gnu.org/software/grub/manual/grub.html#Network)
-   [Legacy BIOS issues with GPT article](https://www.rodsbooks.com/gdisk/bios.html)
-   [GPT and Hybrid MBR article](https://www.rodsbooks.com/gdisk/hybrid.html)
-   [GPT fdisk utility page](https://www.rodsbooks.com/gdisk/)
-   [Arch Linux GRUB 2 wiki article](https://wiki.archlinux.org/index.php/GRUB2)
-   [Fedora GRUB2 wiki article : Encountering the dreaded GRUB2 boot prompt](https://fedoraproject.org/wiki/GRUB_2?rd=Grub2#Encountering_the_dreaded_GRUB_2_boot_prompt)
-   [ubuntu UEFI booting help](https://help.ubuntu.com/community/UEFIBooting)
-   [https://unix.stackexchange.com/questions/109272/dualboot-freebsd-gentoo-with-grub2-mbr](https://unix.stackexchange.com/questions/109272/dualboot-freebsd-gentoo-with-grub2-mbr)
-   [A blog post entry on locking specific GRUB2 boot entries with a password](https://daniel-lange.com/archives/75-Securing-the-grub-boot-loader.html)

## [References]