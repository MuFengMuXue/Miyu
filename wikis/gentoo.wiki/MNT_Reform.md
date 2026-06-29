**Resources**

[[]][Home](https://mntre.com/media/reform_md/2020-05-08-the-much-more-personal-computer.html)

MNT Reform is an ARM Cortex-A53 powered open hardware laptop.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [u-boot]](#u-boot)
        -   [[2.1.1] [boot script]](#boot_script)
        -   [[2.1.2] [Install to SD-card]](#Install_to_SD-card)
        -   [[2.1.3] [Install to internal storage]](#Install_to_internal_storage)
    -   [[2.2] [initrd]](#initrd)
    -   [[2.3] [Kernel]](#Kernel)
-   [[3] [Installing A Gentoo Stage3 on top the the Debian kernel and boot loader]](#Installing_A_Gentoo_Stage3_on_top_the_the_Debian_kernel_and_boot_loader)
    -   [[3.1] [Preserve Required directories]](#Preserve_Required_directories)
    -   [[3.2] [Delete other things]](#Delete_other_things)
    -   [[3.3] [Adding Gentoo]](#Adding_Gentoo)
    -   [[3.4] [Tidy up and run in qemu]](#Tidy_up_and_run_in_qemu)
-   [[4] [TODO Add the ::gentoo repo and test emerge]](#TODO_Add_the_::gentoo_repo_and_test_emerge)
-   [[5] [f0 respawning]](#f0_respawning)
-   [[6] [Clock loses time on reboot]](#Clock_loses_time_on_reboot)
-   [[7] [Build the out-off-tree LPC kernel module]](#Build_the_out-off-tree_LPC_kernel_module)

## [Hardware]

`root `[`#`]`lspci`

    0000:00:00.0 PCI bridge: Synopsys, Inc. DWC_usb3 / PCIe bridge (rev 01)
    0000:01:00.0 Network controller: Qualcomm Atheros AR928X Wireless Network Adapter (PCI-Express) (rev 01)
    0001:00:00.0 PCI bridge: Synopsys, Inc. DWC_usb3 / PCIe bridge (rev 01)
    0001:01:00.0 Non-Volatile memory controller: Silicon Motion, Inc. Device 2263 (rev 03)

`root `[`#`]`lsusb`

    Bus 001 Device 006: ID 03eb:2042 Atmel Corp. LUFA Keyboard Demo Application
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 005: ID 03eb:2041 Atmel Corp. LUFA Mouse Demo Application
    Bus 001 Device 002: ID 0451:8142 Texas Instruments, Inc. TUSB8041 4-Port Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 002: ID 0451:8140 Texas Instruments, Inc. TUSB8041 4-Port Hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

`root `[`#`]`cat /proc/cpuinfo`

    processor   : 0
    BogoMIPS    : 16.66
    Features    : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
    CPU implementer : 0x41
    CPU architecture: 8
    CPU variant : 0x0
    CPU part    : 0xd03
    CPU revision    : 4

    processor   : 1
    BogoMIPS    : 16.66
    Features    : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
    CPU implementer : 0x41
    CPU architecture: 8
    CPU variant : 0x0
    CPU part    : 0xd03
    CPU revision    : 4

    processor   : 2
    BogoMIPS    : 16.66
    Features    : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
    CPU implementer : 0x41
    CPU architecture: 8
    CPU variant : 0x0
    CPU part    : 0xd03
    CPU revision    : 4

    processor   : 3
    BogoMIPS    : 16.66
    Features    : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
    CPU implementer : 0x41
    CPU architecture: 8
    CPU variant : 0x0
    CPU part    : 0xd03
    CPU revision    : 4

## [Installation]

Installing Gentoo on the **MNT Reform** is very similar to how one installs Gentoo on just about any desktop / laptop system. The only parts that need special attention are the bootloader and the kernel.

### [u-boot]

The **MNT Reform** boots using the u-boot bootloader. There is a patched version available in [a separate repository](https://source.mnt.re/reform/reform-boundary-uboot). This bootloader can be used on either an SD-card or on the internal storage, or on both of them.

Unmodified, the bootloader will first attempt to find an OS on the SD card when one is present. For that purpose, it will search the SD-cards first partition for a file [/boot.scr] and if it can\'t find that file, for [/boot/boot.scr] with [boot.scr] being a u-boot script. If no SD-card is present or none of the above files can be found on the SD-card, the bootloader will then proceed to search for the same files on the first partition of the internal storage.

The exact behavior can be studied and / or modified in the file [board/boundary/nitrogen8m_som/nitrogen8m_som.c] of the above-mentioned repository.

To build the bootloader, run these commands:

`root `[`#`]` cd /usr/src `

`root `[`#`]` git clone `[`https://source.mnt.re/reform/reform-boundary-uboot`](https://source.mnt.re/reform/reform-boundary-uboot)` u-boot `

`root `[`#`]` cd u-boot `

`root `[`#`]` cp mntreform-config .config `

`root `[`#`]` make flash.bin `

** Tip**\
gcc-newer than gcc-13 may require KCFLAGS=-fpermissive make flash.bin to get a successful build

To install the bootloader to a device, run this command:

`root `[`#`]`dd if=./flash.bin of=/dev/mmcblk1 conv=notrunc bs=1k seek=33`

With [/dev/mmcblk1] being the SD-card to install it to.

** Warning**\
Don\'t do this yet. Its covered after partitioning the SD card.

#### [boot script]

The bootloader, as prepared above, will load a boot script. This boot script contains the further details on how to load the kernel, device tree, initrd and pass the kernel command line parameters.

The official images for the **MNT Reform** use a Debian tool called [flash-kernel] to generate the boot script. But it can pretty easily be done by hand.

First, install the u-boot utilities:

`root `[`#`]`emerge --ask dev-embedded/u-boot-tools `

Now, a boot script is needed in human-readable text form. Start out with the same template as used by Debian\'s [flash-kernel]. The file is located at: [https://salsa.debian.org/installer-team/flash-kernel/-/blob/master/bootscript/arm64/bootscr.uboot-generic](https://salsa.debian.org/installer-team/flash-kernel/-/blob/master/bootscript/arm64/bootscr.uboot-generic)

Place that in a file [boot.txt], then edit it. Primarily, replace the `@@LINUX_KERNEL_CMDLINE_DEFAULTS@@` and `@@LINUX_KERNEL_CMDLINE@@` values. The values used in the official Image (as of v3) are `ro no_console_suspend cma=512M pci=nomsi` and `console=ttymxc1,115200 console=tty1` respectively.

Replace `@@KERNEL_VERSION@@` with the kernel version information and remove the `@@UBOOT_ENV_EXTRA@@` part.

Once satisfied, compile it by running:

`root `[`#`]`mkimage -A arm -O linux -T script -C none -a 0x0 -e 0x0 -n "boot script" -d boot.txt boot.scr `

The while compiling, the file\'s header information will be printed. To show that information later, run:

`root `[`#`]`dumpimage -l boot.scr `

The output is supposed to look a bit like this:

    Image Name:   boot script
    Created:      Mon Mar 14 15:31:46 2022
    Image Type:   ARM Linux Script (uncompressed)
    Data Size:    2441 Bytes = 2.38 KiB = 0.00 MiB
    Load Address: 00000000
    Entry Point:  00000000
    Contents:
       Image 0: 2433 Bytes = 2.38 KiB = 0.00 MiB

Here is the complete boot script used when creating this tutorial:

`root `[`#`]`cat boot.txt`

    # sh-kernel: bootscr.uboot-generic
    #

    # Bootscript using the new unified bootcmd handling
    #
    # Expects to be called with the following environment variables set:
    #
    #  devtype              e.g. mmc/scsi etc
    #  devnum               The device number of the given type
    #  bootpart             The partition containing the boot files
    #  distro_bootpart      The partition containing the boot files
    #                       (introduced in u-boot mainline 2016.01)
    #  prefix               Prefix within the boot partiion to the boot files
    #  kernel_addr_r        Address to load the kernel to
    #  fdt_addr_r           Address to load the FDT to
    #  ramdisk_addr_r       Address to load the initrd to.
    #
    # The uboot must support the booti and generic filesystem load commands.

    if test -n "$"; then
      setenv bootargs "$ console=$"
    fi

    setenv bootargs ro no_console_suspend cma=512M pci=nomsi $ console=ttymxc1,115200 console=tty1 root=UUID=8709fad5-63c9-48db-83f3-5bf64ac2873b rd.luks.uuid=03741e41-0882-4327-8805-bb4c5b3be2da rd.luks.allow-discards root_trim=yes

    # setenv bootpart "1"
    # setenv prefix "/"
    # setenv kernel_addr_r "0x40480000"
    # setenv fdt_addr_r "0x50000000"
    # setenv ramdisk_addr_r "0x51000000"

    if test -z "$"; then
       setenv fk_kvers '6.1.8-mnt-reform2'
    fi

    # These two blocks should be the same apart from the use of
    # $ in the first, the syntax supported by u-boot does not
    # lend itself to removing this duplication.

    setenv fdtpath dtb-$

    if test -z "$"; then
      setenv partition $
    else
      setenv partition $
    fi

    # place here any u-boot commands to be executed before boot

    load $ $:$ $ $vmlinuz-$ \
    && load $ $:$ $ $$ \
    && load $ $:$ $ $initramfs-$.img \
    && echo "Booting Debian $ from $ $:$..." \
    && booti $ $:$ $

    load $ $:$ $ $vmlinuz \
    && load $ $:$ $ $dtb \
    && load $ $:$ $ $initrd.img \
    && echo "Booting Debian from $ $:$..." \
    && booti $ $:$ $

#### [Install to SD-card]

Having u-boot and the boot script, install them to an SD-card. Since the SD-card will only hold the kernel and initrd, it can be relatively small.

First, prepare the partition table:

`root `[`#`]` parted --script /dev/mmcblk1 "mklabel msdos" `

`root `[`#`]` parted --script /dev/mmcblk1 "mkpart primary ext4 4MiB -1" `

`root `[`#`]` mkfs.ext4 /dev/mmcblk1p1 `

Next, write the bootloader to the exact location it needs to be at:

`root `[`#`]`dd if=./flash.bin of=/dev/mmcblk1 conv=notrunc bs=1k seek=33`

Now, mount the SD-card\'s first partition, and place the files in a structure like so (using kernel version 5.12.0 in the below example):

    ├── boot.scr             # The boot script
    ├── dtb-5.12.0           # The device tree
    ├── initrd.img-5.12.0    # The initramfs
    └── vmlinuz-5.12.0       # The kernel

#### [Install to internal storage]

To boot from the internal storage instead of the SD-card, first partition the storage at `mmcblk0`:

`root `[`#`]` parted --script /dev/mmcblk0 "mklabel msdos" `

`root `[`#`]` parted --script /dev/mmcblk0 "mkpart primary ext4 4MiB -1" `

`root `[`#`]` mkfs.ext4 /dev/mmcblk0p1 `

Now, before we can write the bootloader to the internal storage, we have to make it writeable:

`root `[`#`]` echo 0 > /sys/class/block/mmcblk0boot0/force_ro `

Now, we can write the bootloader:

`root `[`#`]`dd if=./flash.bin of=/dev/mmcblk0boot0 conv=notrunc bs=1k seek=33`

Now, mount the partition created above and place the files in a structure like so (using kernel version 5.12.0 in the below example):

    ├── boot.scr             # The boot script
    ├── dtb-5.12.0           # The device tree
    ├── initrd.img-5.12.0    # The initramfs
    └── vmlinuz-5.12.0       # The kernel

Depending on when you received your MNT Reform, you might have to toggle the DIP switch on the SOM to enable booting from the internal storage.

### [initrd]

When generating an initrd make sure the following kernel modules are included and loaded early, to ensure the display output is working:

-   reset_imx7
-   mux_mmio
-   fixed
-   i2c-imx
-   fan53555
-   i2c_mux_pca954x
-   pwm_imx27
-   pwm_bl
-   panel_edp
-   ti_sn65dsi86
-   imx-dcss
-   phy-fsl-imx8-mipi-dphy
-   nwl-dsi
-   mxsfb
-   usbhid
-   imx8mq-interconnect
-   nvme

The above list is based off [this script from the reference image](https://source.mnt.re/reform/reform-tools/-/blob/main/initramfs-tools/reform). Depending on which tool you use to generate the initrd, all or some of those might be included automatically.

When using [dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut") to build the initrd, add a configuration file that looks like this:

[FILE] **`/etc/dracut.conf.d/20_mnt-reform-2.conf`**

    force_drivers+=" reset_imx7 mux_mmio fixed i2c-imx fan53555 i2c_mux_pca954x pwm_imx27 pwm_bl panel_edp ti_sn65dsi86 imx-dcss phy-fsl-imx8-mipi-dphy nwl-dsi mxsfb usbhid imx8mq-interconnect nvme "

### [Kernel]

I have created an ebuild for a patched kernel.

This ebuild is based on the [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] and thus includes the usual Gentoo-specific kernel patches and is based on the same configuration as the Gentoo kernel. Additionally, it also incorporates the patches and configuration [used in building the reference kernel](https://source.mnt.re/reform/reform-debian-packages/-/tree/main/linux).

Note that the author of this ebuild is not associated with MNT and this kernel is not officially supported by MNT.

First, add the necessary repository:

`root `[`#`]`eselect repository enable mnt-reform `

`root `[`#`]`emerge --sync mnt-reform`

Optionally updated eix:

`root `[`#`]`eix-update --repo-name mnt-reform2`

Now, install the kernel. Note that this will take about 8 hours on the MNT Reform itself:

`root `[`#`]`emerge --ask sys-kernel/mnt-reform2-kernel`

By default, this will also trigger initramfs generation through dracut. Make sure to end up with a working initramfs as in the [the previous chapter](https://wiki.gentoo.org/wiki/MNT_Reform#initrd "MNT Reform").

As of now, the resulting image is gzip compressed, but u-boot expects an uncompressed kernel image. Manually unpack the image and place it in the correct location for the system to successfully boot:

`root `[`#`]`mv /boot/vmlinuz-$-mnt-reform2 `

`root `[`#`]`gunzip /boot/vmlinuz-$-mnt-reform2.gz`

Check the format of the resulting file:

`root `[`#`]`file /boot/vmlinuz-$-mnt-reform2`

    /boot/vmlinuz-6.1.8-mnt-reform2: Linux kernel ARM64 boot executable Image, little-endian, 4K pages

Before rebooting the system, please make sure all files are named correctly. In particular, the u-boot boot script expects the kernel to be named [vmlinuz-\<VERSION\>] whereas the file installed by this ebuild is called [vmlinuz-\<VERSION\>-mnt-reform2].

The same goes for the initrd which is expected by the boot script to be named [initrd.img-\<VERSION\>] whereas the file generated by dracut will be called [initramfs-\<VERSION\>-mnt-reform2.img].

So either rename the files or modify the boot script to make this work.

## [Installing A Gentoo Stage3 on top the the Debian kernel and boot loader]

** Warning**\
This has not beet tested on real hardware and uboot has not been tested by the author at all.

Fetch pocket-reform-system-imx8mp.img. Its a disk image with a partition table and two partitions

loop mount it, read only to start with.

`root `[`#`]`losetup -f -P pocket-reform-system-imx8mp.img`

so we see the partitions

`root `[`#`]`mount -o loop,ro /dev/loopXp2 /mnt/gentoo`

`root `[`#`]`mount -o loop,ro /dev/loopXp1 /mnt/gentoo/boot`

to look around.

`root `[`#`]`ls -l /mnt/gentoo `

    total 76
    lrwxrwxrwx   1 root root     7 May 12 20:25 bin -> usr/bin
    drwxr-xr-x   2 root root  4096 Jul  6 15:49 boot
    drwxr-xr-x   4 root root  4096 Jul  6 15:49 dev
    drwxr-xr-x 122 root root  4096 Sep  4 20:14 etc
    drwxr-xr-x   2 root root  4096 May 12 20:25 home
    lrwxrwxrwx   1 root root    39 Jul  6 15:49 initrd.img -> boot/initrd.img-6.15.4-mnt-reform-arm64
    lrwxrwxrwx   1 root root    39 Jul  6 15:49 initrd.img.old -> boot/initrd.img-6.15.4-mnt-reform-arm64
    lrwxrwxrwx   1 root root     7 May 12 20:25 lib -> usr/lib
    drwx------   2 root root 16384 Jul  6 15:49 lost+found
    drwxr-xr-x   2 root root  4096 Jul  6 15:49 media
    drwxr-xr-x   2 root root  4096 Jul  6 15:49 mnt
    drwxr-xr-x   3 root root  4096 Jul  6 15:49 opt
    drwxr-xr-x   2 root root  4096 May 12 20:25 proc
    drwxr-x--x  12 root root  4096 Sep  4 19:52 root
    drwxr-xr-x   3 root root  4096 Jul  6 15:49 run
    lrwxrwxrwx   1 root root     8 May 12 20:25 sbin -> usr/sbin
    drwxr-xr-x   2 root root  4096 Jul  6 15:49 srv
    drwxr-xr-x   2 root root  4096 May 12 20:25 sys
    drwxrwxrwt   2 root root  4096 Jul  6 15:49 tmp
    drwxr-xr-x  11 root root  4096 Jul  6 15:49 usr
    drwxr-xr-x  11 root root  4096 Sep  4 16:35 var
    lrwxrwxrwx   1 root root    36 Jul  6 15:49 vmlinuz -> boot/vmlinuz-6.15.4-mnt-reform-arm64
    lrwxrwxrwx   1 root root    36 Jul  6 15:49 vmlinuz.old -> boot/vmlinuz-6.15.4-mnt-reform-arm64

### [Preserve Required directories]

** Warning**\
Looking is harmless. Getting the path names wrong now will destroy your host install.

Do not make a new fs so that the UUID and LABEL are preserved.

`root `[`#`]`mount -o rw,remount /dev/loopXp2 /mnt/gentoo`

`root `[`#`]` cd /mnt/gentoo`

Keep etc for reference, in case we need it later.

`/mnt/gentoo``mv etc pocket_etc `

Presorve modules and firmware

`/mnt/gentoo``mv ./usr/lib/firmware/ ./firmware`

`/mnt/gentoo``mv ./usr/lib/modules/ ./modules`

### [Delete other things]

`/mnt/gentoo``rmdir ./boot ./home ./media ./mnt ./srv ./sys ./tmp`

`/mnt/gentoo``rm -rf ./dev ./run`

`/mnt/gentoo``rm -rf ./opt ./proc ./root ./usr/ ./var`

This leaves

`/mnt/gentoo``ls -al `

    total 40
    drwxr-xr-x   6 root root  4096 Sep  5 17:17 .
    drwxr-xr-x   8 root root  4096 Oct 24  2022 ..
    lrwxrwxrwx   1 root root     7 May 12 20:25 bin -> usr/bin
    drwxr-xr-x  48 root root  8192 Jul  6 15:49 firmware
    lrwxrwxrwx   1 root root    39 Jul  6 15:49 initrd.img -> boot/initrd.img-6.15.4-mnt-reform-arm64
    lrwxrwxrwx   1 root root    39 Jul  6 15:49 initrd.img.old -> boot/initrd.img-6.15.4-mnt-reform-arm64
    lrwxrwxrwx   1 root root     7 May 12 20:25 lib -> usr/lib
    drwx------   2 root root 16384 Jul  6 15:49 lost+found
    drwxr-xr-x   3 root root  4096 Jul  6 15:49 modules
    drwxr-xr-x 122 root root  4096 Sep  4 20:14 pocket_etc
    lrwxrwxrwx   1 root root     8 May 12 20:25 sbin -> usr/sbin
    lrwxrwxrwx   1 root root    36 Jul  6 15:49 vmlinuz -> boot/vmlinuz-6.15.4-mnt-reform-arm64
    lrwxrwxrwx   1 root root    36 Jul  6 15:49 vmlinuz.old -> boot/vmlinuz-6.15.4-mnt-reform-arm64

from the original filesystem, leaving 9.0G for a stage3

`/mnt/gentoo``df -h `

    Filesystem                      Size  Used Avail Use% Mounted on
    /dev/loop0p2                    9.8G  338M  9.0G   4% /mnt/gentoo

### [Adding Gentoo]

The Debian kernel expects a systemd usrland, OpenRC is untested.

Untar a systemd arm64 stage3 to /mnt/gentoo, as per the amd64 handbook.

`/mnt/gentoo``wget `[`https://distfiles.gentoo.org/releases/arm64/autobuilds/20250831T234929Z/stage3-arm64-desktop-systemd-20250831T234929Z.tar.xz`](https://distfiles.gentoo.org/releases/arm64/autobuilds/20250831T234929Z/stage3-arm64-desktop-systemd-20250831T234929Z.tar.xz)

because Debian uses systemd. Desktop because most users want a desktop

`/mnt/gentoo``tar xpf stage3-*.tar.xz --xattrs-include='*.*' --numeric-owner -C /mnt/gentoo`

Nervous readers can use `tar xpvf`

Restore modules and firmware

`/mnt/gentoo``mv ./firmware ./usr/lib/`

`/mnt/gentoo``mv ./modules ./usr/lib/`

Trust but verify

`/mnt/gentoo``ls -l ./usr/lib/ `

    total 108
    drwxr-xr-x  2 root root 4096 Sep  1 03:32 binfmt.d
    lrwxrwxrwx  1 root root   38 Sep  1 04:13 cpp -> /usr/bin/aarch64-unknown-linux-gnu-cpp
    drwxr-xr-x  2 root root 4096 Sep  1 04:17 environment.d
    drwxr-xr-x 48 root root 8192 Jul  6 15:49 firmware
    drwxr-xr-x  3 root root 4096 Sep  1 03:29 gcc
    drwxr-xr-x  2 root root 4096 Sep  1 03:28 gentoo
    drwxr-xr-x  3 root root 4096 Sep  1 04:17 kernel
    lrwxrwxrwx  1 root root   30 Sep  1 04:05 ld-linux-aarch64.so.1 -> ../lib64/ld-linux-aarch64.so.1
    drwxr-xr-x  2 root root 4096 Sep  1 03:28 lessfilter.d
    drwxr-xr-x  3 root root 4096 Sep  1 04:25 llvm
    drwxr-xr-x  2 root root 4096 Sep  1 04:07 locale
    drwxr-xr-x  2 root root 4096 Sep  1 03:32 modprobe.d
    drwxr-xr-x  3 root root 4096 Jul  6 15:49 modules
    drwxr-xr-x  2 root root 4096 Sep  1 03:32 modules-load.d
    -rw-r--r--  1 root root  208 Mar 24 00:52 os-release
    drwxr-xr-x  2 root root 4096 Sep  1 04:17 pam.d
    drwxr-xr-x  2 root root 4096 Sep  1 04:17 polkit-1
    drwxr-xr-x  3 root root 4096 Sep  1 03:32 portage
    drwxr-xr-x  3 root root 4096 Sep  1 04:20 python
    drwxr-xr-x 38 root root 4096 Sep  1 04:20 python3.13
    drwxr-xr-x  3 root root 4096 Sep  1 03:32 python-exec
    drwxr-xr-x  3 root root 4096 Sep  1 03:32 rpm
    drwxr-xr-x  2 root root 4096 Sep  1 04:16 rust
    lrwxrwxrwx  1 root root   18 Sep  1 04:16 rustlib -> rustlib-bin-1.88.0
    lrwxrwxrwx  1 root root   37 Sep  1 04:16 rustlib-bin-1.88.0 -> ../../opt/rust-bin-1.88.0/lib/rustlib
    drwxr-xr-x  2 root root 4096 Sep  1 03:32 sysctl.d
    drwxr-xr-x 20 root root 4096 Sep  1 04:17 systemd
    drwxr-xr-x  2 root root 4096 Sep  1 04:04 sysusers.d
    drwxr-xr-x  2 root root 4096 Sep  1 04:19 tmpfiles.d
    drwxr-xr-x  4 root root 4096 Sep  1 04:19 udev

As this will be booted in QEMU, set a root password the hard way

`/mnt/gentoo``nano ./etc/shadow`

    root:$6$xxPVR/Td5iP$/7Asdgq0ux2sgNkklnndcG4g3493kUYfrrdenBXjxBxEsoLneJpDAwOyX/kkpFB4pU5dlhHEyN0SK4eh/WpmO0::0:99999:7:::
    halt:*:9797:0:::::

This sets the root password to **raspberry**. Don\'t leave it like that.

### [Tidy up and run in qemu]

Reboot to test \...

cd out of the filesystems to be unmounted.

`/mnt/gentoo``cd`

`root `[`#`]`umount /dev/loop0p1`

`root `[`#`]`umount /dev/loop0p2`

** Warning**\
Do not run qemu as root

`user `[`$`]`cd pocket-reform`

`~/pocket-reform $``qemu-system-aarch64 `

                   -machine virt -cpu neoverse-v1 -m 8G -smp 4 \
                   -kernel vmlinuz-6.15.4-mnt-reform-arm64 \
                   -initrd initrd.img-6.15.4-mnt-reform-arm64 -drive \
                    file=pocket-reform-system-imx8mp.img,format=raw

`Ctrl-Alt-2` to see the kernel console in qemu. Boots and allows root logins.

** Note**\
There is no networking as none was defined in the qemu-system-aarch64 command.

## [TODO Add the ::gentoo repo and test emerge]

With the binhost too

## [f0 respawning]

With a default arm64 system, error messages like this will appear both on the default `TTY` in the system log:

    Id "f0" respawning too fast: disabled for 5 minutes

To get rid of those, edit the `inittab` at [/etc/inittab] and remove or comment out the last line, that looks something like this:

[FILE] **`/etc/inittab`**

    # Architecture specific features
    f0:12345:respawn:/sbin/agetty 9600 ttyAMA0 vt100

Then, restart the system.

## [Clock loses time on reboot]

The Reform has two Real-time clocks installed in the system - a battery backed up `PCF8523` and an on-CPU `SNVS`. The `SNVS` clock is powered by the same rail as the `i.MX8M` CPU and will reset together with the system.

By default, the `hwclock` is using [/dev/rtc0], which might be the wrong clock.

To fix this issue, either remove the `rtc-snvs` kernel driver, or edit the following line in the [/etc/conf.d/hwclock] file:

[FILE] **`/etc/conf.d/hwclock`**

    clock_args="--rtc /dev/rtc1"

Check which RTC has been assigned to which device by looking at the kernel ring buffer:

`user `[`$`]` dmesg | grep --ignore-case rtc`

    [    3.556883] rtc-pcf8523 2-0068: registered as rtc0
    [    3.563641] rtc-pcf8523 2-0068: setting system clock to 2020-07-13T17:27:26 UTC (1594661246)

In the above example, the `PCF8523` is the only RTC and it is assigned to [/dev/rtc0].

## [Build the out-off-tree LPC kernel module]

An out of tree kernel module exists that allows the OS to interact with the LPC System controller. Foremost, it makes battery / charge information available in Linux.

The GCC used to compile the module must be the exact same that was used to build the kernel, otherwise, the build will abort with an error.

`root `[`#`]` cd /usr/src/ `

`root `[`#`]` git clone `[`https://source.mnt.re/reform/reform-tools.git`](https://source.mnt.re/reform/reform-tools.git)` `

`root `[`#`]` cd reform-tools/lpc/ `

Once compiled, you can now load the module like so:

`root `[`#`]` insmod /usr/src/reform-tools/lpc/reform2_lpc.ko `

Details about the laptop\'s power supply is now available through [/sys/class/power_supply/8xlifepo4/].

To install the module into a path where it can be handled more easily, run these commands:

`root `[`#`]` mkdir --parents /lib/modules/$(uname --kernel-release)/kernel/drivers/other/reform2_lpc `

`root `[`#`]` cp /usr/src/reform-tools/lpc/reform2_lpc.ko /lib/modules/$(uname --kernel-release)/kernel/drivers/other/reform2_lpc/ `

`root `[`#`]` depmod `

You should now be able to load the module lik so:

`root `[`#`]` modprobe reform2_lpc `