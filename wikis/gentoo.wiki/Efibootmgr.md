Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Efibootmgr/de "Efibootmgr (89% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Efibootmgr/es "Efibootmgr (25% translated)")
-   [français](https://wiki.gentoo.org/wiki/Efibootmgr/fr "Efibootmgr (100% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Efibootmgr/it "Efibootmgr (23% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Efibootmgr/hu "efibootmgr (100% translated)")
-   [svenska](https://wiki.gentoo.org/wiki/Efibootmgr/sv "Efibootmgr (2% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Efibootmgr/ru "Efibootmgr (85% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Efibootmgr/zh-cn "Efibootmgr (2% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Efibootmgr/ja "efibootmgr (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Efibootmgr/ko "Efibootmgr (17% translated)")

**Resources**

[[]][GitHub](https://github.com/rhinstaller/efibootmgr)

[[]][Package information](https://packages.gentoo.org/packages/sys-boot/efibootmgr)

[[]][README](https://github.com/rhboot/efibootmgr/blob/master/README.md)

[[]][EFIBOOTMGR(8)](https://linux.die.net/man/8/efibootmgr)

[efibootmgr] is a tool for managing [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") boot entries.

It is *not* a [bootloader](https://wiki.gentoo.org/wiki/Category:Bootloaders "Category:Bootloaders"). It is a tool that interacts with the EFI firmware of the system, which itself is acting as a boot manager. Using [efibootmgr] boot entries can be created, reshuffled and removed.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [EFI vars]](#EFI_vars)
-   [[3] [Preconditions]](#Preconditions)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Listing boot entries]](#Listing_boot_entries)
    -   [[4.2] [Creating a boot entry]](#Creating_a_boot_entry)
    -   [[4.3] [Deleting a boot entry]](#Deleting_a_boot_entry)
    -   [[4.4] [Removable media]](#Removable_media)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [[] Installation]

### [[] Kernel]

[`CONFIG_EFIVAR_FS`](https://wiki.gentoo.org/wiki/Efivarfs "Efivarfs") support needs to be enabled.

** Note**\
It is not possible to use [efivarfs] without the EFI runtime services, which (in case they have been disabled by default, i.e. `CONFIG_EFI_DISABLE_RUNTIME=y`) can also be enabled by the [kernel command-line option](https://wiki.gentoo.org/wiki/Kernel#Kernel_command-line_parameters "Kernel") [efi=runtime].

### [[] Emerge]

The [[[sys-boot/efibootmgr]](https://packages.gentoo.org/packages/sys-boot/efibootmgr)[]] package does not have any USE flags. All that is needed is to install it:

`root `[`#`]`emerge --ask sys-boot/efibootmgr`

## [[] Configuration]

### [[] EFI vars]

In order to successfully use [efibootmgr] the EFI variables filesystem must be accessible. This requires that the system has been booted in EFI mode (and not through the firmware\'s MBR mode) as otherwise the EFI variables themselves cannot be accessed. If the system is in MBR mode, reboot and do what is necessary in order to tell the system firmware to boot in EFI mode. Usually this involved either changing an option in the firmware\'s settings or selecting an EFI boot entry in the system\'s boot menu.

When the system is in EFI mode, run the following command to check for the existence of a mounted [efivarfs](https://wiki.gentoo.org/wiki/Efivarfs "Efivarfs"):

`root `[`#`]`mount | grep efivars`

    efivarfs on /sys/firmware/efi/efivars type efivarfs (ro,relatime)

It is mounted read-only (ro) through the [sysfs] init script), so it needs to be remounted read-write (rw) manually using the following command:

`root `[`#`]`mount -o remount,rw -t efivarfs efivarfs /sys/firmware/efi/efivars`

## [[] Preconditions]

If an EFI System Partition (ESP) does not exist, one needs to be created, see [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition").

## [[] Usage]

### [[] Listing boot entries]

When using an older version of [efibootmgr] the option `--verbose` or `-v` is needed:

`root `[`#`]`efibootmgr`

    BootCurrent: 0002
    Timeout: 3 seconds
    BootOrder: 0003,0003,0002,0000,0004
    Boot0000* CD/DVD Drive  BIOS(3,0,00)
    Boot0001* Hard Drive    BIOS(2,0,00)
    Boot0002* Gentoo        HD(1,800,61800,6d98f360-cb3e-4727-8fed-5ce0c040365d)File(\EFI\boot\bootx64.efi)
    Boot0003* Hard Drive    BIOS(2,0,00)P0: ST1500DM003-9YN16G

### [[] Creating a boot entry]

To create an EFI boot entry, a couple of arguments are passed to [efibootmgr]:

-   `--create` or `-c` to create a new entry;
-   `--part` or `-p` followed by the partition number on which the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") is hosted;
-   `--disk` or `-d` followed by the disk on which the EFI System Partition is hosted;
-   `--label` or `-L` followed by the label to use as the boot entry;
-   `--loader` or `-l` followed by the path of the EFI image to boot

** Important**\
The path of the EFI image to boot *must* use [\\] (backslash) instead of [/] (forward slash) as path separator.

** Important**\
Additionally, if the ESP was already created by another OS, it might be named differently than [/efi/**EFI**]. If an ESP was created by another OS, begin the EFI Boot entry using this directory name, which immediately follows [/efi].

Below are some examples of how a UEFI entry can be created. If this is the folder structure:

`root `[`#`]`tree /efi/ -L 3`

    /efi/
    └── EFI
        ├── Grub
        │   └── grubx64.efi
        └── Gentoo
            └── bzImage.efi

then the loader paths will be:

`root `[`#`]`efibootmgr -c -L "Grub" -l '\EFI\Grub\grubx64.efi' `

`root `[`#`]`efibootmgr -c -L "Gentoo" -l '\EFI\Gentoo\bzImage.efi'`

For instance:

`root `[`#`]`efibootmgr -c -d /dev/sda -p 2 -L "Gentoo" -l '\efi\boot\bootx64.efi'`

While [not supported](https://wiki.gentoo.org/wiki/Dell_Latitude_E6430_(CYRTRY1)#Hardware "Dell Latitude E6430 (CYRTRY1)") by all UEFI implementations^[\[1\]](#cite_note-1)^, to add `--unicode` or `-u` kernel command-line parameters issue:

`root `[`#`]`efibootmgr -c -d /dev/sda -p 2 -L "Gentoo" -l '\efi\boot\bootx64.efi' -u 'root=/dev/sda3 initrd=\efi\boot\initramfs.img quiet'`

For a dm-crypt module initrd example, refer to [efibootmgr](https://wiki.gentoo.org/wiki/Rootfs_encryption#efibootmgr "Rootfs encryption").

Refer to [Why make your own](https://wiki.gentoo.org/wiki/Initramfs_-_make_your_own#Why_make_your_own "Initramfs - make your own") for initial ramdisk systems.

Optionally, additional kernels can be installed and made known to the UEFI firmware. This is especially useful when wanting to test more kernels or to dual-boot with another operating system. These will be shown in the boot selection prompt, normally after a keyboard hotkey is pressed at the right time during system initialization. The latest added entry always gets highest boot priority, so it will be default. If the hotkey combination is unknown, search for official documentation from the computer manufacturer. This information is usually not difficult to find.

### [[] Deleting a boot entry]

Before deleting an entry, first figure out what ID the entry has.

To delete the Gentoo entry as shown above (which has *Boot0002* as the identifier), ask [efibootmgr] to delete the entry with id 2, passing the arguments `--bootnum` or `-b` with the identifier, and `--delete-bootnum` or `-B` to delete the entry:

`root `[`#`]`efibootmgr -b 2 -B`

### [[] Removable media]

EFI bootloaders on removable media are not configured as boot entries, neither are bootloaders using the removable media boot path on the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") or ESP, i.e. for both [efibootmgr] is not required. See [removable media boot path](https://wiki.gentoo.org/wiki/EFI_System_Partition#Removable_media "EFI System Partition") for details.

## [[] Removal]

### [[] Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose sys-boot/efibootmgr`

## [[] See also]

-   [Alternative 2: efibootmgr](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Bootloader#Alternative_2:_efibootmgr "Handbook:AMD64/Installation/Bootloader") in the Gentoo Handbook
-   [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub")
-   [Efivarfs](https://wiki.gentoo.org/wiki/Efivarfs "Efivarfs") --- a filesystem in the Linux [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") that enables users to create, delete, and modify [(U)EFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") variables
-   [Initramfs - make your own](https://wiki.gentoo.org/wiki/Initramfs_-_make_your_own "Initramfs - make your own") --- build an initramfs which does not contain kernel modules.
-   [REFInd](https://wiki.gentoo.org/wiki/REFInd "REFInd") --- a boot manager for UEFI platforms.

## [[] References]

1.  [[[↑](#cite_ref-1)] [At least for Dell EFI firmware, a workaround was implemented in kernel 5.10: [https://lkml.org/lkml/2020/9/18/228](https://lkml.org/lkml/2020/9/18/228)]]