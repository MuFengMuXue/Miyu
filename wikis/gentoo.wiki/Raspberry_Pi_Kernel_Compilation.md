The [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi") cannot run a vanilla Linux kernel. A patched version of the kernel is maintained by the Raspberry Pi Foundation and is available from their [GitHub page](https://github.com/raspberrypi).

** Note**\
The official Raspberry Pi Foundation kernels are built 32-bit, which is appropriate for Raspberry Pi 1, 2, and 3 (running in 32-bit mode; recommended). This guide does not cover building a 64-bit kernel for the Raspberry Pi 3 (issues / unstable / not recommended).

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Get the kernel source]](#Get_the_kernel_source)
-   [[3] [Compile and install the kernel with genkernel]](#Compile_and_install_the_kernel_with_genkernel)
    -   [[3.1] [Default kernel]](#Default_kernel)
    -   [[3.2] [Kernel with initramfs]](#Kernel_with_initramfs)
-   [[4] [Compile and install the kernel without genkernel]](#Compile_and_install_the_kernel_without_genkernel)
-   [[5] [Adding new kernel to the bootloader]](#Adding_new_kernel_to_the_bootloader)
-   [[6] [Detailed step-by-step guide]](#Detailed_step-by-step_guide)

## [Prerequisites]

To compile a kernel, [[[dev-vcs/git]](https://packages.gentoo.org/packages/dev-vcs/git)[]] is required to download the source code when not using [[[sys-kernel/raspberrypi-sources]](https://packages.gentoo.org/packages/sys-kernel/raspberrypi-sources)[]] and also (optional) [genkernel](https://wiki.gentoo.org/wiki/Genkernel "Genkernel") to manage the build process.

`root `[`#`]`emerge --ask dev-vcs/git sys-kernel/genkernel`

## [Get the kernel source]

`root `[`#`]`emerge --ask sys-kernel/raspberrypi-sources`

or manually:

`root `[`#`]`cd /opt `

`root `[`#`]`git clone --depth 1 https://github.com/raspberrypi/linux.git `

`root `[`#`]`ln -s /opt/linux /usr/src/linux `

## [Compile and install the kernel with genkernel]

** Note**\
Compiling the kernel will take about 6 hours.

genkernel can build a Linux kernel with support for many different features. Follow one of the examples below that has the required features.

### [Default kernel]

In this example, the configuration options from the running kernel are used to compile the new kernel.

`root `[`#`]`genkernel --kernel-config=/proc/config.gz kernel`

After the kernel has compiled, it will be installed into the [/boot] folder.

### [Kernel with initramfs]

This example will run menuconfig before compiling the kernel to enable any extra modules needed. Using a kernel with an [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") allows loading modules, decrypt partitions and other more complex task that maybe require early in the boot process.

`root `[`#`]`genkernel --kernname=rpi --menuconfig all`

To support initramfs, the following options need to be enabled in menuconfig:

[KERNEL]

    General setup  --->
        [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
            ()    Initramfs source file(s) (NEW)
            [*]   Support initial ramdisks compressed using gzip (NEW)
            [ ]   Support initial ramdisks compressed using bzip2 (NEW)

After the kernel has compiled, it and the initramfs be installed into the [/boot] folder, add it to bootloader (skip to **[Adding new kernel to the bootloader](#Adding_new_kernel_to_the_bootloader)**)

## [Compile and install the kernel without genkernel]

The first time configuring the kernel sources, create a default .config file (for Raspberry Pi2 use bcm2709_defconfig):

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make bcm2835_defconfig `

After that, modify this default configuration (a good idea is to add .config support):

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make menuconfig `

An example config can be found at [https://github.com/modulix/raspggen/blob/master/kernel.conf](https://github.com/modulix/raspggen/blob/master/kernel.conf)

Then, try to compile/install it:

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`mount /boot `

`root `[`#`]`mkdir /boot/overlays `

`root `[`#`]`make -j4 Image modules dtbs `

`root `[`#`]`make modules_install dtbs_install `

for 32-bit kernels:

`root `[`#`]`gzip -9cf arch/arm/boot/Image > /boot/kernel7.img `

for 64-bit kernels:

`root `[`#`]`gzip -9cf arch/arm64/boot/Image > /boot/kernel8.img `

** Note**\
If this kernel is called kernel7.img / kernel8.img, adding it in [/boot/config.txt] file is not necessary. See: [config.txt on raspberrypi.com](https://www.raspberrypi.com/documentation/computers/config_txt.html#kernel)

\
For now, to have [WiFi](https://wiki.gentoo.org/wiki/Wifi "Wifi") work, download firmware:

`root `[`#`]`wget https://github.com/RPi-Distro/firmware-nonfree/blob/master/brcm80211/brcm/brcmfmac43430-sdio.bin -O /lib/firmware/brcm/brcmfmac43430-sdio.bin `

`root `[`#`]`wget https://github.com/RPi-Distro/firmware-nonfree/blob/master/brcm80211/brcm/brcmfmac43430-sdio.txt -O /lib/firmware/brcm/brcmfmac43430-sdio.txt `

## [Adding new kernel to the bootloader]

By default, the Raspberry Pi looks for a kernel in [/boot/kernel.img]. This is changed in the configuration file [/boot/config.txt] to load the new kernel.

[FILE] **`/boot/config.txt`Example config.txt**

    kernel=kernel-genkernel-arm-3.2.27+

If using an initramfs, add that to the [config.txt] as well:

[FILE] **`/boot/config.txt`Example config.txt with an initramfs**

    kernel=kernel-rpi-arm-3.2.27+
    initramfs initramfs-rpi-arm-3.2.27+

Now, the Raspberry Pi can be rebooted and should make use of the new kernel. If for some reason the new kernel does not load or gives errors, the kernel entry in the [/boot/config.txt] can be removed. Then, on the next reboot, the default [kernel.img] will be loaded.

## [Detailed step-by-step guide]

Upon encountering problems building or deploying the kernel, try following the [detailed kernel building guide](http://visualkernel.com/tutorials/raspberry/buildkernel/) for clues on resolving the problems. Additionally The Raspberry Pi foundation provides these [build guides](https://www.raspberrypi.org/documentation/linux/kernel/building.md) to assist in Kernel compilation.