**Resources**

[[]][Home](http://www.gpd.hk/pocket.asp)

[] This article is a **work in progress**; treat its contents with caution - [Drcrane](https://wiki.gentoo.org/index.php?title=User:Drcrane&action=edit&redlink=1 "User:Drcrane (page does not exist)") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:Drcrane&action=edit&redlink=1 "User talk:Drcrane (page does not exist)") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/Drcrane "Special:Contributions/Drcrane")).

This article provides instructions on getting Gentoo operational on the GPD Pocket.

The GPD Pocket is a 7\" UMPC manufactured by Game Park Digital running an Intel Atom x7-Z8750 and 8 GB RAM. Lots of work has already been done on getting the kernel to work out of the box by [Hans de Goede](https://github.com/jwrdegoede).

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Creating an EFI-capable bootable USB drive]](#Creating_an_EFI-capable_bootable_USB_drive)
    -   [[2.3] [Installing a bootloader]](#Installing_a_bootloader)
    -   [[2.4] [Kernel and Initial RAM Disk]](#Kernel_and_Initial_RAM_Disk)
    -   [[2.5] [Booting to the USB drive]](#Booting_to_the_USB_drive)
-   [[3] [Creating a GPD Userspace]](#Creating_a_GPD_Userspace)
    -   [[3.1] [Configure Package Build Host]](#Configure_Package_Build_Host)
    -   [[3.2] [From Stage3 to boot]](#From_Stage3_to_boot)
    -   [[3.3] [Configuring the Goodix Capacitive TouchScreen]](#Configuring_the_Goodix_Capacitive_TouchScreen)
    -   [[3.4] [Configuring the UEFI Boot Menu]](#Configuring_the_UEFI_Boot_Menu)
    -   [[3.5] [Setting up the GPD Pocket Fan]](#Setting_up_the_GPD_Pocket_Fan)

## [Hardware]

The GPD Pocket contains the following hardware, the kernel should be configured to include drivers for all these items:

  ------------------------------- ------------------------------------------------------------------------------
  Hardware                        Kernel Configuration Key
  USB Keyboard                    USB Options Enabled (xHCI also)
  MAX17047 Fuel Gauge             `BATTERY_MAX17042`
  BQ24190 Charger                 `CHARGER_BQ24190`
  GPIO for Fan Control            `GPD_POCKET_FAN`
  Intel Graphics                  `CONFIG_DRM_I915`
  UEFI Framebuffer                `CONFIG_FB_EFI`
  ALSA Sound Card Support         `CONFIG_SND_SST_ATOM_HIFI2_PLATFORM_ACPI`
  eMMC Block Device (ACPI SDIO)   `CONFIG_MMC_SDHCI` `CONFIG_MMC_SDHCI_ACPI`
  Wireless                        `CONFIG_B43` `CONFIG_BRCMFMAC` `CONFIG_BRCMFMAC_SDIO` `CONFIG_BRCMFMAC_PCIE`
  .
  ------------------------------- ------------------------------------------------------------------------------

I recommend compiling all these as modules they can then be tested in the normal way. Be careful of the Keyboard support though!

## [Installation]

### [Kernel]

** Note**\
Knowledge of configuring the kernel is required here although it is quite simple.

This is the most complex step but you can avoid the pain by downloading the pre-built kernel from [https://github.com/joshskidmore/gpd-pocket-arch-guide](https://github.com/joshskidmore/gpd-pocket-arch-guide). A kernel can be compiled from gentoo-sources in portage, a working configuration can be found on [Hans de Goede\'s github linux-sunxi config](https://github.com/jwrdegoede/linux-sunxi) (I can confirm that gentoo-sources-4.16.0 works). Also, gentoo-sources-4.16.0 contains the [GPD Pocket fan driver](https://github.com/jwrdegoede/linux-sunxi/commit/cf59a9b05feb95999a1a2c095e52398267e55db6).

`root `[`#`]`emerge =gentoo-sources-4.16.0`

Copy the [.config] file from Hans de Goede\'s GitHub repository [https://github.com/jwrdegoede/linux-sunxi](https://github.com/jwrdegoede/linux-sunxi) into the [/usr/src/linux-4.16.0-gentoo/.config] directory.

This change to the linux-sunxi [.config] file should help with a funny sound driver problem:

[KERNEL]

    CONFIG_INTEL_ATOMISP=n

`root `[`#`]`make menuconfig `

`root `[`#`]`make -j4 `

`root `[`#`]`mkdir /usr/src/modules-4.16.0-gentoo `

`root `[`#`]`make INSTALL_MOD_STRIP=1 INSTALL_MOD_PATH=/usr/src/modules-4.16.0-gentoo modules_install `

The new kernel is available under [/usr/src/linux-4.16.0-gentoo/arch/x86_64/boot/bzImage] and the new modules in [/usr/src/modules-4.16.0-gentoo]

### [Creating an EFI-capable bootable USB drive]

** Warning**\
This will make all the data on the USB Stick inaccessible.

Use [fdisk] to create a new GPT partition table on the USB Stick. It is important that the partition table is GPT for a UEFI enabled machine to detect the UEFI partition.

`root `[`#`]`fdisk /dev/sdc`

    Command (m for help): g
    Created a new GPT disklabel (GUID: C799490C-B64C-4DF0-8466-7EDAB65294B3).

    Command (m for help): n
    Partition number (1-128, default 1): 1
    First sector (2048-60547342, default 2048): 4096
    Last sector, +sectors or +size (4096-60547342, default 60547342): +256M

    Created a new partition 1 of type 'Linux filesystem' and of size 256 MiB.

    Command (m for help): t
    Selected partition 1
    Partition type (type L to list all types): 1
    Changed type of partition 'Linux filesystem' to 'EFI System'.

    Command (m for help): n
    Partition number (2-128, default 2): 2
    First sector (528384-60547342, default 528384):
    Last sector, +sectors or +size (528384-60547342, default 60547342):

    Created a new partition 2 of type 'Linux filesystem' and of size 28.6 GiB.

    Command (m for help): w

An [EFI System partition](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") is just a FAT32 partition, to set up the partition you may need to install [[[sys-fs/dosfstools]](https://packages.gentoo.org/packages/sys-fs/dosfstools)[]]:

`root `[`#`]`emerge --ask sys-fs/dosfsutils`

`root `[`#`]`mkfs.vfat -F32 /dev/sdc1`

Mount the drive and make the UEFI boot directories:

`root `[`#`]`mount /dev/sdc1 /mnt/sdc1 `

`root `[`#`]`mkdir -p /mnt/sdc1/EFI/BOOT `

Create a Linux root file system on [/dev/sdc2]:

`root `[`#`]`mkfs.ext2 /dev/sdc2`

Download and extract a stage 3 onto [/dev/sdc2] (alter the mirror and date to flavor):

`root `[`#`]`mount /dev/sdc2 /mnt/sdc2 `

`root `[`#`]`wget `[`http://gentoomirror/.../stage3-amd64-nomultilib-YYYYMMDD.tar.bz2`](http://gentoomirror/.../stage3-amd64-nomultilib-YYYYMMDD.tar.bz2)` `

`root `[`#`]`cd /mnt/sdc2 `

`root `[`#`]`tar -xf stage3-amd64-nomultilib-YYYYMMDD.tar.bz2 `

Edit the [etc/passwd] and [etc/shadow] files so that you can login.

### [Installing a bootloader]

SYSLINUX will be used to boot the kernel, if syslinux is not installed on the system, do it now:

`root `[`#`]`emerge --ask sys-boot/syslinux`

Copy the required binaries to the USB drive:

`root `[`#`]`cp /usr/share/syslinux/efi64/syslinux.efi /mnt/sdc1/EFI/BOOT/bootx64.efi `

`root `[`#`]`cp /usr/share/syslinux/efi64/ldlinux.e64 /mnt/sdc1/EFI/BOOT/ldlinux.e64 `

Create the syslinux configuration file:

[FILE] **`/mnt/sdc1/EFI/BOOT/syslinux.cfg`**

    PROMPT 1
    TIMEOUT 50
    DEFAULT gentoo

    LABEL gentoo
        LINUX ../vmlinuz-4.16.0-gentoo
        APPEND root=/dev/ram0 fbcon=rotate:1
        INITRD ../initramfs-4.16.0-gentoo.cpio.gz

The kernel and the RAM disk will be created next

### [Kernel and Initial RAM Disk]

Creating a custom `initramfs` is [explained here](https://wiki.gentoo.org/wiki/Custom_Initramfs "Custom Initramfs") to allow access to the GPD Pocket internal eMMC flash and access to the USB stick that the root fs is installed on some modules must be available in the initramfs:

`root `[`#`]`find lib/ -type f`

    lib/modules/4.16.0-gentoo/kernel/drivers/usb/storage/usb-storage.ko
    lib/modules/4.16.0-gentoo/kernel/drivers/mmc/core/mmc_block.ko
    lib/modules/4.16.0-gentoo/kernel/drivers/mmc/core/mmc_core.ko
    lib/modules/4.16.0-gentoo/kernel/drivers/mmc/host/sdhci.ko
    lib/modules/4.16.0-gentoo/kernel/drivers/mmc/host/sdhci-acpi.ko

These files can be copied from the kernel modules directory when a kernel is compiled with the Hans de Goede (or Fedora) settings.

The newly created initramfs and kernel should be copied to the EFI partition:

`root `[`#`]`cp /usr/src/linux-4.16.0-gentoo/arch/x86_64/boot/bzImage /mnt/sdc1/EFI/vmlinuz-4.16.0-gentoo `

`root `[`#`]`cp /usr/src/initramfs-4.16.0-gentoo.cpio.gz /mnt/sdc1/EFI `

### [Booting to the USB drive]

To boot to the USB drive insert the drive into the GPD Pocket\'s USB socket and press [F7] when the GPD Pocket is starting up (that means hold down the [Fn] key and press [7] a few times when you power up).

You should be presented with a list of startup options, one of which should be the name of your USB drive, select that one and syslinux should start and then boot the kernel and execute the initramfs.

## [Creating a GPD Userspace]

I recommend creating a Virtual Machine or a Docker Container using a stage3 tarball, the VM or Container will be where all the applications are compiled and then installed on the GPD Pocket using portage\'s binary package support.

### [Configure Package Build Host]

To begin, create and configure a clean Gentoo VM / Docker Container with the same configuration that will be used on the GPD Pocket:

[FILE] **`/etc/portage/make.conf`**

    FEATURES="buildpkg"
    USE="-bindist"
    CPU_FLAGS_X86="mmx mmxext sse sse2 sse3 ssse3 sse4_1 sse4_2 avx aes"
    VIDEO_CARDS="intel"
    PORTDIR="/var/db/repos/gentoo"
    DISTDIR="/mnt/portage/distfiles"
    PKGDIR="/mnt/portage/packages"

Alter the PORTDIR, DISTDIR and PKGDIR to taste, this configuration is for a [Portage Tree in SquashFS](https://www.brunsware.de/blog/gentoo/portage-tree-squashfs-overlayfs.html) configuration.

The configuration for the GPD Pocket would look something like this, also be aware that the files in [/etc/portage/package.use] and [/etc/portage/package.accept_keywords] on both machines (the VM and your GPD Pocket) should match.

[FILE] **`/etc/portage/make.conf`**

    FEATURES="getbinpkg"
    PORTAGE_BINHOST="ssh://user@hostname:port/mnt/portage/packages"
    USE="-bindist"
    CPU_FLAGS_X86="mmx mmxext sse sse2 sse3 ssse3 sse4_1 sse4_2 avx aes"
    VIDEO_CARDS="intel"
    PORTDIR="/var/db/repos/gentoo"
    DISTDIR="/mnt/portage/distfiles"
    PKGDIR="/mnt/portage/packages"

** Warning**\
Although not strictly necessary it is probably better that the portage tree is the same on the VM and GPD Pocket, using SquashFS makes this easy and SquashFS images are provided on Gentoo mirrors!

### [From Stage3 to boot]

OpenSSL and OpenSSH when compiled with the `bindist` use flag will not support wpa_supplicant which is required for the GPD Pocket to connect to a WiFi network. Emerge these on your VM.

`root `[`#`]`emerge --oneshot openssl openssh `

`root `[`#`]`emerge linux-firmware `

`root `[`#`]`emerge wpa_supplicant `

The [brcmfmac] driver (which is required for WiFi, see earlier) will not work properly with [linux-firmware-20181026]. The driver cannot find the file [brcm/brcmfmac4356-pcie.txt], this file can be obtained from Google (and probably Broadcom). Fix is documented in this [bug](https://bugzilla.kernel.org/show_bug.cgi?id=185661) and by [joshskidmore](https://github.com/joshskidmore/gpd-pocket-arch-guide) in his GPD Pocket guide for Arch Linux.

`root `[`#`]`mv brcmfmac4356-pcie.txt /lib/firmware/brcm/brcmfmac4356-pcie.txt `

Of course it will be difficult to install these packages without a network connection so install them from a chroot environment.

### [Configuring the Goodix Capacitive TouchScreen]

The GPD Pocket orientation is incorrect (it is obvious when the device is booting). For the frame buffer terminal the kernel command line argument above [}}] but for Wayland and X11 udev must be configured through the rules. This works if the X server is using libinput but if not different configuration specific to [xorg-X11] may be required.

[FILE] **`/etc/udev/rules.d/99-goodix-touch.rules`**

    ACTION=="add|change", KERNEL=="event[0-9]*", ATTRS=="Goodix Capacitive TouchScreen", ENV="0 1 0 -1 0 1"

The character between [add] and [change] is a pipe ([\|]).

[Found here (it works)](http://daniel-lnx.blogspot.com/2017/07/gpd-pocker-touchscreen-rotation-with.html)

### [Configuring the UEFI Boot Menu]

[This is probably a good reference](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr").

### [Setting up the GPD Pocket Fan]

Newer kernels have a module for fan control on the GPD Pocket but annoyingly when the GPD Pocket is connected to AC supply the module defaults to switching the fan on. To modify this behaviour the module can be reloaded, first unload the module:

`gpdpocket `[`~ #`]`modprobe -r gpd-pocket-fan `

Then, reload the module:

`gpdpocket `[`~ #`]`modprobe gpd-pocket-fan speed_on_ac=0 `

Fan on and off levels can be altered in a similar way for the fan to turn on at 40 degrees:

`gpdpocket `[`~ #`]`modprobe gpd-pocket-fan temp_limits=40000,40001,40002 `

[Arch Linux Wiki](https://wiki.archlinux.org/index.php/GPD_Pocket)