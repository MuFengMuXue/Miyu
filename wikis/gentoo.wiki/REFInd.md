Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/REFInd/fr "REFInd (32% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/REFInd/hu "rEFInd (76% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/REFInd/ja "rEFInd (83% translated)")

\

**Resources**

[[]][Home](http://www.rodsbooks.com/refind/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/REFInd "wikipedia:REFInd")

[[]][Package information](https://packages.gentoo.org/packages/sys-boot/refind)

[[]][GitWeb](https://sourceforge.net/p/refind/code/ci/master/tree/)

**rEFInd** is a boot manager for UEFI platforms. It provides a graphical interface for launching EFI-based operating systems and accessing EFI-based utilities.

rEFInd can boot traditional Linux kernels, but also any compatible EFI bootloader. Examples include [unified kernel images](https://wiki.gentoo.org/wiki/Unified_kernel_image "Unified kernel image") (see [below](https://wiki.gentoo.org/wiki/REFInd#Unified_kernel_image "REFInd")), aside from additional operating systems such as BSD Unix (like FreeBSD), macOS and Windows.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [ESP installation]](#ESP_installation)
    -   [[2.1] [File system layout]](#File_system_layout)
    -   [[2.2] [Installation with NVRAM modification]](#Installation_with_NVRAM_modification)
    -   [[2.3] [Installation to the EFI Default/Fallback path]](#Installation_to_the_EFI_Default.2FFallback_path)
    -   [[2.4] [Upgrading rEFInd]](#Upgrading_rEFInd)
-   [[3] [Kernel management]](#Kernel_management)
    -   [[3.1] [Unified kernel image]](#Unified_kernel_image)
-   [[4] [Linux command line options]](#Linux_command_line_options)
    -   [[4.1] [Initial RAM filesystem (initramfs)]](#Initial_RAM_filesystem_.28initramfs.29)
-   [[5] [Icons]](#Icons)
    -   [[5.1] [Icons and kernel image on the ESP]](#Icons_and_kernel_image_on_the_ESP)
-   [[6] [ISO images]](#ISO_images)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)

## [[] Installation]

### [[] Kernel]

For a kernel to be bootable from rEFInd, its EFI stub support (`CONFIG_EFI_STUB`) has to be enabled:

[KERNEL] **Enable EFI stub support for Kernels 6.1+**

    Processor type and features  --->
        [*] EFI runtime service support
        [*]     EFI stub support

EFI framebuffer support (`CONFIG_FB_EFI`) or a vendor specific [Framebuffer](https://wiki.gentoo.org/wiki/Framebuffer "Framebuffer") is required to display video when launching the kernel from an EFI such as rEFInd:

[KERNEL] **Enable EFI framebuffer support**

    Device Drivers --->
       Graphics support --->
          Frame buffer Devices --->
             <*> Support for frame buffer devices --->
                [*] EFI-based Framebuffer Support

### [[] USE flags]

rEFInd has optional support for scanning several filesystems for EFI executables before loading the operating system. This allows to keep the kernels outside of the [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") (ESP) but needs the rEFInd built with the respective [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") enabled.

### [USE flags for] [sys-boot/refind](https://packages.gentoo.org/packages/sys-boot/refind) [[]] [The UEFI Boot Manager by Rod Smith]

  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`+ext2`](https://packages.gentoo.org/useflags/+ext2)             Builds the EFI binary ext2 filesystem driver
  [`+ext4`](https://packages.gentoo.org/useflags/+ext4)             Builds the EFI binary ext4 filesystem driver
  [`+iso9660`](https://packages.gentoo.org/useflags/+iso9660)       Builds the EFI binary iso9660 filesystem driver
  [`btrfs`](https://packages.gentoo.org/useflags/btrfs)             Builds the EFI binary btrfs filesystem driver
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`hfs`](https://packages.gentoo.org/useflags/hfs)                 Builds the EFI binary hfs filesystem driver
  [`ntfs`](https://packages.gentoo.org/useflags/ntfs)               Builds the EFI binary ntfs filesystem driver
  [`reiserfs`](https://packages.gentoo.org/useflags/reiserfs)       Builds the EFI binary reiserfs filesystem driver
  [`secureboot`](https://packages.gentoo.org/useflags/secureboot)   Automatically sign efi executables using user specified key
  ----------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-14 09:04] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

`root `[`#`]`emerge --ask sys-boot/refind`

    rEFInd has been built and installed into $/usr/share/$
    You will need to use the command 'refind-install' to install
    the binaries into your EFI System Partition

## [[] ESP installation]

Once the rEFInd package has been emerged, a second step is needed to install the binaries to the ESP. If an ESP does not exist, one needs to be created. See [EFI System Partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition").

### [[] File system layout]

For kernel storage there are multiple options.

During boot, rEFInd can automatically find EFI boot images and Linux kernels. It looks for files ending in [.efi] or beginning with [vmlinuz], [bzImage] or [kernel]. On the filesystems it can read (based on above USE flags), it scans in the following locations[\[1\]](https://www.rodsbooks.com/refind/configfile.html#hiding):

-   File system root ([/]).
-   [/boot] directory.
-   Most of the sub-directories of [/EFI]. (See example in the [Kernel image at ESP](https://wiki.gentoo.org/wiki/REFInd#Kernel_image_at_ESP "REFInd") section).

Boot partition configuration is quite flexible. For example, choose one of:

-   Separate boot, ESP and root partitions
-   Separate ESP partition with [/boot] part of the root filesystem. (Provided it is a non-encrypted, non-LVM and one of the above supported filesystems).
-   Only ESP partition mounted at [/boot], or unified kernel images living in [/EFI/Linux/].

### [[] Installation with NVRAM modification]

The rEFInd package comes with the [refind-install] command. Running it will:

1.  Looks if the ESP is already mounted. If not, automount the ESP according to [[/etc/fstab]](https://wiki.gentoo.org/wiki/EFI_System_Partition#Mount_point "EFI System Partition")
2.  Install its [refind_x64.efi] application and other stuff into the ESP
3.  Call [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") to set itself as the default boot manager.

`root `[`#`]`refind-install`

    ShimSource is none
    Installing rEFInd on Linux....
    ESP was found at /boot using vfat
    Copied rEFInd binary files

    Copying sample configuration file as refind.conf; edit this file to configure
    rEFInd.

    Installing it!
    rEFInd has been set as the default boot manager.
    Creating //boot/refind_linux.conf; edit it to adjust kernel options.

    Installation has completed successfully.

`user `[`$`]`tree -L 3 /boot`

    /boot
    ├── EFI
    │   ├── refind
    │   │   ├── icons
    │   │   ├── keys
    │   │   ├── refind.conf
    │   │   └── refind_x64.efi
    │   └── tools
    └── refind_linux.conf

`user `[`$`]`efibootmgr -v`

    Boot000x* rEFInd Boot Manager   HD(1,GPT,1729a003-cf0d-4bd4-88c9-cc24d8d418c4,0x800,0x2f000)/File(\EFI\refind\refind_x64.efi)

Boot000x\* can vary depending on existing entries.

** Warning**\
If [/boot] cannot be found in [[/etc/fstab]](https://wiki.gentoo.org/wiki/EFI_System_Partition#Mount_point "EFI System Partition"), [refind-install] will default to using [/boot/efi/EFI] and even move an existing [/boot/EFI] to [/boot/efi/EFI].

** Warning**\
It is important to manually [remount the efivarfs](https://wiki.gentoo.org/wiki/Efibootmgr#EFI_vars "Efibootmgr") with `rw` option or rEFInd won\'t be able to set itself as the default boot manager, issuing an error message.

In order to do this, use the following command:

`root `[`#`]`mount -o remount,rw -t efivarfs efivarfs /sys/firmware/efi/efivars`

### [][[] Installation to the EFI Default/Fallback path]

rEFInd can be installed to a disk using the default/fallback filename of [EFI/BOOT/bootx64.efi]. The computer\'s NVRAM entries will not be modified when installing in this way. Most EFI and UEFI firmware support a fallback EFI image to boot from if the configured EFI file cannot be found, and some will also override the configured boot selection if the fallback boot image is found. This can be used to boot into EFI mode when doing so otherwise is difficult.

`root `[`#`]`refind-install --usedefault /dev/sda1 `

Where [/dev/sda1] is the ESP. This installation method can be used as either a permanent setup to create a bootable USB flash drive or install rEFInd on a computer that tends to \"forget\" its NVRAM settings or as a temporary bootstrap to get the system to boot in EFI mode.

### [[] Upgrading rEFInd]

Before upgrading rEFInd, it is possible to check it and see if it works correctly. The existing rEFInd is able to start a new rEFInd. This can be accomplished by copying [/usr/lib64/refind/refind] to the ESP (for example [EFI/refind]).

## [Kernel management]

Regardless if [/boot] is a separate partition or part of the root file system, rEFInd should be able to find a kernel if standard naming convention is used. This makes it compatible with (semi-) automatic kernel installation methods such as [genkernel \--install] or [make install] **without further configuration**.

### [Unified kernel image]

rEFInd can boot [unified kernel images](https://wiki.gentoo.org/wiki/Unified_kernel_image "Unified kernel image") (UKI) too. For UKI kernels [refind_linux.conf] is not refereed to. So even for rEFInd users, UKI simplifies the things, and with rEFInd, UKIs can be stored in a Linux partition, instead of the ESP.

** Note**\
When UKIs are there, rEFInd can take \>5 seconds to boot. Do not panic.

## [[] Linux command line options]

[refind_linux.conf] should live in the same directory as the kernels. It is automatically generated in [/boot] during [refind_install] or with [[mkrlconf]](https://www.rodsbooks.com/refind/mkrlconf.html). Each entry will show up as an option for each kernel.

The default entry is based on the current [/proc/cmdline]. Single is the same as default, but with [single] added. And [minimal] is contains only the current root device, with the [ro] argument. None of the entries contain the initramfs, as it is established automatically at boot.

This file usually works out of the box when it is generated from the same boot session as it is supposed to start. For instance, when replacing the bootloader for rEFInd. However, when generated from another OS, for instance during installation of Gentoo, care must be taken and the entries must be corrected manually.

Simple example configuration:

[FILE] **`/boot/refind_linux.conf`**

    "Default" "root=/dev/sda2 rootfstype=xfs ro quiet"
    "Console" "root=/dev/sda2 rootfstype=xfs ro quiet nox nogui"
    "Emergency"   "root=/dev/sda2 rootfstype=xfs ro 1"

In simple cases, users do not have specify initramfs, because rEFInd automatically passes the appropriate initramfs. See [below](https://wiki.gentoo.org/wiki/REFInd#Initial_RAM_filesystem_.28initramfs.29 "REFInd") for the details.

Custom (static) initramfs and [microcode](https://wiki.gentoo.org/wiki/Intel_microcode#rEFInd "Intel microcode") loading:

[FILE] **`/boot/refind_linux.conf`**

    "Standard boot"       "root=LABEL=root initrd=intel-ucode.img initrd=initramfs-custom.img quiet"
    "Single-user mode"    "root=LABEL=root initrd=intel-ucode.img initrd=initramfs-custom.img single"
    "Minimal options"     "ro root=LABEL=root initrd=initramfs-custom.img"

The main selection screen for rEFInd will use the first option as the default option, however alternate boot entries can be accessed by highlighting the kernel and pressing [F2]. Also cmdline can be modified on-the-fly by pressing [F2] on a menu item to open it in an editor. When ready, press [Enter] to boot the kernel.

** Note**\
The kernel cmdline options above are for example only - The user will need to have its own options that allow the kernel to boot for the system.

### [][Initial RAM filesystem (initramfs)]

rEFInd can automatically pass the appropriate initramfs to the kernel without configuration. More precisely at boot, rEFInd looks for an initial RAM disk (initramfs) that starts with [init] and ends in a kernel version string. For example [initramfs-5.4.66-gentoo.img] matches with [vmlinuz-5.4.66-gentoo]. Provided that [refind_linux.conf] does not specify an [initrd], it is automatically appended to the kernel command line.

When using tools like [Genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") or [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut"), no additional configuration is required. However, if a [Custom Initramfs](https://wiki.gentoo.org/wiki/Custom_Initramfs "Custom Initramfs") is used some care is required. Either, the initramfs should be named using the same convention, or its name should be specified in [[refind_linux.conf]](https://wiki.gentoo.org/wiki/REFInd#Linux_command_line_options "REFInd").

## [[] Icons]

rEFInd comes with a collection of icons for different Linux distributions. In order to [set an icon](https://www.rodsbooks.com/refind/configfile.html#icons) on the menu entry, it needs to know the OS name. For that it looks in the following places, in this order:

1.  An icon base name matches the kernel base name. For instance [vmlinuz-5.4.66-gentoo.png]
2.  The kernel is in an ESP sub-directory, named after the OS. For instance the kernel is at [/EFI/Gentoo/vmlinuz-5.4.66-gentoo.png] See \"[Kernel image at ESP](https://wiki.gentoo.org/wiki/REFInd#Kernel_image_at_ESP "REFInd")\" for more info.
3.  Filesystem label contains a space, underscore or dash delimited OS name. For instance with [tunetfs -L Gentoo-boot /dev/sdaX].
4.  GPT partition name, following the same convention as filesystem labels.
5.  From the [/etc/os-release] file on the same partition. For instance, when [/boot] is part of the root partition.
6.  Hard coded rules based on words kernel names. For instance, [vmlinux] and [bzImage] default to the Linux \"Tux\" icon.

** Tip**\
To automatically install a custom icon alongside the (unified) kernel image, enable the [[[refind]](https://packages.gentoo.org/useflags/refind)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]] and set `REFIND_ICON` to the desired icon in the environment. If this variable is unset, the Gentoo logo is installed by default.

### [[] Icons and kernel image on the ESP]

It is possible to store the kernels and initial RAM disks on the ESP by mounting it at [/boot]. Because the kernel is on a separate partition refind can not automatically determine which distribution the kernel belongs to and will therefore fall back to the default Tux logo. To automatically install a Gentoo icon file for refind to pickup alongside the kernel image, enable the [[[refind]](https://packages.gentoo.org/useflags/refind)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]].

A similar problem occurs when using [Unified Kernel Images](https://wiki.gentoo.org/wiki/Unified_Kernel_Image "Unified Kernel Image"), these will be installed in the [EFI/Linux] directory on the ESP. Refind is then unable to get any information on which distribution this unified kernel image belongs to. To automatically install a Gentoo icon file for refind to pickup alongside the unified kernel image, enable the [[[refind]](https://packages.gentoo.org/useflags/refind)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag on [[[sys-kernel/installkernel]](https://packages.gentoo.org/packages/sys-kernel/installkernel)[]].

** Tip**\
Which icon file is installed may be overridden by setting `REFIND_ICON` in the environment.

## [ISO images]

rEFInd can find and boot iso images. For that purpose, each iso image has to be burnt to one partition using tools like [dd](https://wiki.gentoo.org/wiki/Dd "Dd"). It also requires the USE flag iso9660.

## [See also]

-   [Kernel/Configuration](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration")
-   [Dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") --- an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") infrastructure and aims to have as little as possible hard-coded into the initramfs.
-   [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") --- a multiboot secondary [bootloader](https://wiki.gentoo.org/wiki/Bootloader "Bootloader") capable of loading kernels from a variety of [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") on most system architectures.
-   [Syslinux](https://wiki.gentoo.org/wiki/Syslinux "Syslinux") --- a package that contains a family of [bootloaders](https://wiki.gentoo.org/wiki/Bootloader "Bootloader").
-   [UEFI Dual boot with Windows 7/8](https://wiki.gentoo.org/wiki/UEFI_Dual_boot_with_Windows_7/8 "UEFI Dual boot with Windows 7/8") --- describes how to dual boot Microsoft Windows on a UEFI computer.

## [External resources]

-   [rEFInd SourceForge repository](http://sourceforge.net/p/refind/code/ci/master/tree/)
-   [Upstream installation instructions](http://www.rodsbooks.com/refind/installing.html)