**Resources**

[[]][Home](https://limine-bootloader.org)

[[]][GitHub](https://github.com/limine-bootloader/limine)

Limine is a modern, advanced, portable, multiprotocol [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") and boot manager which also provides the reference implementation of the Limine boot protocol.

This guide is designed to be followed alongside [the installation Handbook](https://wiki.gentoo.org/wiki/Handbook:Main_Page "Handbook:Main Page") and [the ZFS root guide](https://wiki.gentoo.org/wiki/ZFS/rootfs "ZFS/rootfs") if so desired, though the config file examples are of course universal to all.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Unmasking the Package]](#Unmasking_the_Package)
    -   [[1.2] [Optional: USE flags]](#Optional:_USE_flags)
    -   [[1.3] [Emerging the Package]](#Emerging_the_Package)
-   [[2] [Setting up the Bootloader]](#Setting_up_the_Bootloader)
    -   [[2.1] [Copying the Bootloader Files]](#Copying_the_Bootloader_Files)
        -   [[2.1.1] [For UEFI]](#For_UEFI)
            -   [[2.1.1.1] [Using efibootmgr (optional)]](#Using_efibootmgr_.28optional.29)
        -   [[2.1.2] [For BIOS]](#For_BIOS)
    -   [[2.2] [Writing the Config File]](#Writing_the_Config_File)
        -   [[2.2.1] [Generic Config Example]](#Generic_Config_Example)
        -   [[2.2.2] [Using Limine With ZFS Root]](#Using_Limine_With_ZFS_Root)
        -   [[2.2.3] [Dual-booting with Windows in Limine (UEFI)]](#Dual-booting_with_Windows_in_Limine_.28UEFI.29)
        -   [[2.2.4] [Dual-booting with Windows in Limine (BIOS)]](#Dual-booting_with_Windows_in_Limine_.28BIOS.29)
-   [[3] [Finalising]](#Finalising)

## [Installation]

### [Unmasking the Package]

Limine is now available in the main tree, but it is not currently unmasked. Unmasking the package is a relatively simple process, to do so, the allowed keywords variable needs to be edited, in which the following needs to be appended utilising a preferred editor:

[FILE] **`/etc/portage/package.accept_keywords/limine`Unmasking Limine for install**

    sys-boot/limine ~amd64

### [Optional: USE flags]

It is possible to configure Limine for only the target system\'s method, it may be done so by specifying USE flags, assuming the target is an AMD64 UEFI system, the required USE flags would be:

[FILE] **`/etc/portage/package.use/limine`Specifying USE flags to exclusively build UEFI AMD64 files**

    sys-boot/limine -bios -bios-cd -bios-pxe -uefi-aarch64 -uefi-cd -uefi-ia32 -uefi-loongarch64 -uefi-riscv64 uefi-x86-64

The other USE flags may be viewed with the following command:

`user `[`$`]`emerge --pretend --verbose sys-boot/limine`

### [Emerging the Package]

Once all the above steps are completed, [[[sys-boot/limine]](https://packages.gentoo.org/packages/sys-boot/limine)[]] can be installed to the target:

`root `[`#`]`emerge --ask --verbose sys-boot/limine`

## [Setting up the Bootloader]

Now that Limine is installed on the target system, configuring the bootloader can begin.

To configure the bootloader, differing files will be utilised depending on target architecture and whether the target is using BIOS or UEFI.

### [Copying the Bootloader Files]

In order for Limine to boot, Limine requires there to be a mounted vfat partition as [/boot], which will be your ESP on UEFI systems, and simply a normal extra partition formatted as vfat on BIOS systems.

** Note**\
~~With Limine ver 8.x, there is experimental support for ext2/3/4 - this can be useful for those on MBR systems who do not want to use vfat, however issues may occur with the nature of brand new and experimental features. Use at your own risk!~~ With Limine 9.x, the addition of ext2/3/4 support has been reverted and is no longer usable. If the target systems\' 8.x Limine files are on an ext2/3/4 partition, it is best to either [mask newer versions](https://wiki.gentoo.org/wiki//etc/portage/package.mask "/etc/portage/package.mask") or change the location to a vfat partition alongside updating to version 9.x.

The bootloader files are stored in [/usr/share/limine] and are named after their respective architectures, excluding the BIOS file, which is universal for both x86 and amd64 BIOS systems.

It is a good idea initially to check if [/boot] is mounted, this can be done by simply running the [lsblk] command:

`user `[`$`]`lsblk`

    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
    zram0       252:0    0     2G  0 disk [SWAP]
    zram1       252:1    0     2G  0 disk /tmp
    nvme0n1     259:0    0 238.5G  0 disk
    ├─nvme0n1p1 259:1    0   400M  0 part /boot
    └─nvme0n1p2 259:2    0 238.1G  0 part /

After confirming [/boot] is mounted, the architecture files can be copied across.

#### [For UEFI]

For UEFI, there is no need for [[[sys-boot/efibootmgr]](https://packages.gentoo.org/packages/sys-boot/efibootmgr)[]] 99% of the time, using the default directory structure will get picked up by the firmware.

`root `[`#`]`mkdir -p /boot/EFI/BOOT/`

After creating this directory, the respective .EFI firmware file can be copied across, assuming the target is an AMD64 UEFI system, the correct command would be:

`root `[`#`]`cp -v /usr/share/limine/BOOTX64.EFI /boot/EFI/BOOT/`

If the target is not AMD64 EFI, and rather RISCV, AARCH64 or x86, their respective files can be located by listing the contents of [/usr/share/limine]:

`user `[`$`]`ls /usr/share/limine`

** Important**\
If USE flags were specified as demonstrated in [section 1.3](https://wiki.gentoo.org/wiki/Limine#Optional:_USE_flags "Limine"), the other files will not exist! If in doubt, always use default USE flags.

##### [][Using efibootmgr (optional)]

If the target systems UEFI firmware is unable to find the ESP, or for peace of mind, [[[sys-boot/efibootmgr]](https://packages.gentoo.org/packages/sys-boot/efibootmgr)[]] can be utilized in order to create an entry pointing towards Limine in the EFI Firmware.

[[[sys-boot/efibootmgr]](https://packages.gentoo.org/packages/sys-boot/efibootmgr)[]] can be installed with the following command:

`root `[`#`]`emerge --ask --verbose sys-boot/efibootmgr`

Following it\'s install and assuming the target is an amd64 system, creating an entry will look like this:

`root `[`#`]`efibootmgr \ `

         --create \
         --disk /dev/sdX \
         --part Y \
         --label "Gentoo Linux Limine Bootloader" \
         --loader '\EFI\limine\BOOTX64.EFI' \
         --unicode \
         --verbose

** Warning**\
Remember to note that [/dev/sdX] is the disk itself, and [\--part] afterwards defines the partition, and that the arguments to [\--loader] must be back slashes, like Windows\' directory structure, not like that of Linux or other Unix-like systems.

** Note**\
For additional information on creating, deleting or editing EFI Firmware entries, please read the [efibootmgr wiki page](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") or its manual pages.

#### [For BIOS]

For BIOS systems, the bootloader file can be copied to the root of the [/boot] partition:

`root `[`#`]`cp -v /usr/share/limine/limine-bios.sys /boot`

Now the BIOS file is in place, Limine can be installed to the MBR of the drive, so that BIOS firmware can pick up and boot Limine on the next boot:

`root `[`#`]`limine bios-install /dev/sdX`

    Physical block size of 512 bytes.
    Installing to MBR.
    Stage 2 to be located at 0x200 and 0x2600.
    Reminder: Remember to copy the limine-bios.sys file in either
              the root, /boot, /limine, or /boot/limine directories of
              one of the partitions on the device, or boot will fail!
    Limine BIOS stages installed successfully!

** Note**\
Don\'t forget to replace sdX with the drive you\'re installing to! NVMe, SATA and eMMC devices are all supported by this command, as long as they have a DOS partition table.

### [Writing the Config File]

** Warning**\
Since Limine 9.x was released, the legacy config syntax has been retired and will no longer be parsed. Please update it to the newer syntax if you are upgrading from 7.x or 8.x. If this is a new install, this warning can be safely ignored.

Limine\'s configuration file to find kernels, initramfs\' and microcode is entirely manually written. There\'s a lot of customisation that can be done within the config file, but for simplicity\'s sake, only the basics will be covered here. Limine\'s config file needs to be called [limine.conf], and can be [/boot/limine.conf], [/boot/limine/limine.conf] or [/boot/EFI/BOOT/limine.conf]. For a more detailed explanation of Limine\'s config, [Limine\'s official CONFIG.md file can be viewed](https://github.com/Limine-Bootloader/Limine/blob/v12.x/CONFIG.md).

The config has a pretty simple syntax to follow, with [boot():/] being the root of the partition all the boot files are inside of. The cmdline variable is a standard command line to be parsed to the kernel when it loads, this is required, so the kernel knows what to mount as the root, and can also be used to pre-load modules that might be needed very early on.

#### [Generic Config Example]

The following config example will likely fit most users, it assumes the target system is running the [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] or [[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] distribution kernel, and are on BtrFS, but can be easily edited to specific needs.

[FILE] **`/boot/limine.conf`Generic Config Example**

    # Designates 5 seconds until Limine will automatically boot the first entry if nothing is pressed
    timeout: 5

    /Linux
    //Gentoo Example
            protocol: linux
            kernel_path: boot():/vmlinuz-6.6.62-gentoo-dist
            # Replace with amd-uc.img if the target has an AMD CPU
            module_path: boot():/intel-uc.img
            module_path: boot():/initramfs-6.6.62-gentoo-dist.img
            # Replace $UUID with the UUID blkid echoes for the root partition.
            cmdline: root=UUID=$UUID rw rootfstype=btrfs
            comment: Boot Gentoo Linux!

#### [Using Limine With ZFS Root]

If [ZFS/rootfs](https://wiki.gentoo.org/wiki/ZFS/rootfs "ZFS/rootfs") is being followed, Limine can also be utilised by editing the config slightly, as showcased:

[FILE] **`/boot/limine.conf`ZFS Config Example**

    # Designates 5 seconds until Limine will automatically boot the first selected entry if nothing is pressed.
    timeout: 5

    /Gentoo Example
            protocol: linux
            kernel_path: boot():/vmlinuz-6.6.62-gentoo-dist
            # Replace with amd-uc.img if the target has an AMD CPU.
            module_path: boot():/intel-uc.img
            module_path: boot():/initramfs-6.6.62-gentoo-dist.img
            cmdline: root=ZFS=tank/os/gentoo rw modules=zfs rootfstype=zfs
            comment: Boot Gentoo Linux!

In this config, the root filesystem variable has been changed to tell the kernel to look for a ZFS root partition, and the modules argument tells the kernel to preload the ZFS module, so there is not any issues with the rootfs support not being built into the kernel, as ZFS modules have to be side-loaded with the [[[sys-fs/zfs-kmod]](https://packages.gentoo.org/packages/sys-fs/zfs-kmod)[]] package.

#### [][Dual-booting with Windows in Limine (UEFI)]

Unlike [[[sys-boot/grub]](https://packages.gentoo.org/packages/sys-boot/grub)[]], Limine does not require [[[sys-boot/os-prober]](https://packages.gentoo.org/packages/sys-boot/os-prober)[]] to find other operating systems, Limine can find other EFI files, and has the ability to chainload them when manually pointed to the other EFI file.

[FILE] **`/boot/limine.conf`Dual-Boot Config Example (EFI)**

    # Designates 5 seconds until Limine will automatically boot the first entry if nothing is pressed
    timeout: 5

    /Linux
    //Gentoo Example
            protocol: linux
            kernel_path: boot():/vmlinuz-6.6.62-gentoo-dist
            # Replace with amd-uc.img if the target has an AMD CPU
            module_path: boot():/intel-uc.img
            module_path: boot():/initramfs-6.6.62-gentoo-dist.img
            # Replace $UUID with the UUID blkid echoes for the root partition.
            cmdline: root=UUID=$UUID rw rootfstype=btrfs
            comment: Boot Gentoo Linux!

    /Windows
    //Windows Example
            protocol: efi
            # This tells the efi protocol to call the specified EFI file and load it.
            path: boot():/EFI/Microsoft/boot/bootmgfw.efi
            comment: Boot Microsoft Windows!

This example shows off entries and sub-entries, where as one slash deeper identifies contents of a directory, being able to group and nest entries together for neatness\'s sake. It may be needed to double-check the location of the Windows\' EFI file to make sure Limine is pointing to the right location.

#### [][Dual-booting with Windows in Limine (BIOS)]

Limine can also be pointed to other partitions of OSes installed in MBR configs. The config isn\'t changed too much compared to EFI chainloading, as detailed below, however it may require more trial and error than EFI chainloading to ensure you have specified the right drive and partition.

[FILE] **`/boot/limine.conf`Dual-Boot Config Example (MBR)**

    # Designates 5 seconds until Limine will automatically boot the first entry if nothing is pressed
    timeout: 5

    /Linux
    //Gentoo Example
            protocol: linux
            kernel_path: boot():/vmlinuz-6.6.62-gentoo-dist
            # Replace with amd-uc.img if the target has an AMD CPU
            module_path: boot():/intel-uc.img
            module_path: boot():/initramfs-6.6.62-gentoo-dist.img
            # Replace $UUID with the UUID blkid echoes for the root partition.
            cmdline: root=UUID=$UUID rw rootfstype=btrfs
            comment: Boot Gentoo Linux!

    /Windows
    //Windows Example
            protocol: bios
            drive: 1
            partition: 1
            # This tells the bios protocol to call the specified partition on the specified drive.
            comment: Boot Microsoft Windows!

## [Finalising]

Now, Limine is entirely setup and ready to boot to. Extra eye-candy can be found and applied by revising [the official configuration file documentation](https://github.com/limine-bootloader/limine/blob/v8.x/CONFIG.md). Any issues can be reported on the official GitHub, and the official Limine discord, both of which can be found on their website linked [at the top of the page.](https://wiki.gentoo.org/wiki/Limine#Contents "Limine")