The **Pinephone** is a cheap, generic, arm64 smartphone produced with the goal of supporting user-modifiable operating systems and hardware. It uses an Allwinner \"sunxi\" A64 processor, a Quectel EG-25G Modem, and can boot from either microSD (removable storage) or eMMC (internal storage). It comes in a couple variants that don\'t really affect the installation process.

** Note**\
Due to hardware differences, The user should not expect to run desktop programs normally. Consider using less computer-intensive and keyboard-dependent alternatives to common programs.

## Contents

-   [[1] [Initial chroot and disk setup]](#Initial_chroot_and_disk_setup)
    -   [[1.1] [Option 1: Using another operating system as installation medium]](#Option_1:_Using_another_operating_system_as_installation_medium)
    -   [[1.2] [Option 2: cross-compilation from another Gentoo system]](#Option_2:_cross-compilation_from_another_Gentoo_system)
-   [[2] [Compiling the kernel]](#Compiling_the_kernel)
-   [[3] [Installing the bootloader]](#Installing_the_bootloader)
    -   [[3.1] [Option 1: p-boot]](#Option_1:_p-boot)
        -   [[3.1.1] [Building from source]](#Building_from_source)
    -   [[3.2] [Option 2: U-boot]](#Option_2:_U-boot)
-   [[4] [Installing the user interface]](#Installing_the_user_interface)
    -   [[4.1] [Option 1: sway with custom configuration]](#Option_1:_sway_with_custom_configuration)
    -   [[4.2] [Option 2: Phosh]](#Option_2:_Phosh)
    -   [[4.3] [Option 3: KDE mobile]](#Option_3:_KDE_mobile)
-   [[5] [Wifi/Bluetooth]](#Wifi.2FBluetooth)
-   [[6] [GPU]](#GPU)
-   [[7] [Modem]](#Modem)
-   [[8] [See also]](#See_also)
-   [[9] [References]](#References)

## [Initial chroot and disk setup]

** Note**\
The disk setup depends a lot on the bootloader choice. if p-boot is used, a MBR partition table is needed, and /boot stays on the / filesystem.

### [Option 1: Using another operating system as installation medium]

This seems like the easiest option for installing on eMMC, although it takes a long time to compile.

This method works by installing another OS on the PinePhone that the user can ssh into, then using that to partition the flash, unpack stage3, and chroot, etc. Gentoo could be either installed on eMMC by installing the other operating system on microSD, or installed on the microSD, by first installing another OS on the eMMC ([https://wiki.pine64.org/index.php/PinePhone#Flashing_eMMC_using_Jumpdrive](https://wiki.pine64.org/index.php/PinePhone#Flashing_eMMC_using_Jumpdrive)).

The author currently have problems with mounting and formatting eMMC with postmarketOS (seems it has to do with the way that filesystems are mounted by it\'s initramfs), but the unofficial fedora Linux port works fine. postmarketOS has a nice ssh-over-USB feature ([https://wiki.postmarketos.org/wiki/SSH](https://wiki.postmarketos.org/wiki/SSH)).

### [Option 2: cross-compilation from another Gentoo system]

** Note**\
TODO: write and test something similar to [Raspberry_Pi_3_64_bit_Install](https://wiki.gentoo.org/wiki/Raspberry_Pi_3_64_bit_Install "Raspberry Pi 3 64 bit Install").

This is the easiest option for installing on microSD.

The eMMC can be exposed via USB by installing jumpdrive on a microSD ([https://wiki.pine64.org/index.php/PinePhone#Flashing_eMMC_using_Jumpdrive](https://wiki.pine64.org/index.php/PinePhone#Flashing_eMMC_using_Jumpdrive)).

** Note**\
TODO: see if the filesystem could be mounted directly with jumpdrive and not just flash ISOs.

## [Compiling the kernel]

The new mainline kernels include the sun50i-a64-pinephone-1.X.dtb file (where 1.X is the hardware version), which is needed for the phone\'s bootloader. As of December 2020, the latest stable gentoo-sources doesn\'t have it yet so add \"sys-kernel/gentoo-sources \~arm64\" to [/etc/portage/package.accept_keywords] to get a kernel that supports it.

`root `[`#`]`emerge gentoo-sources `

`root `[`#`]`cd /usr/src/linux `

`root `[`#`]`make menuconfig # (or some pinephone_defconfig) `

`root `[`#`]`make -j4 `

`root `[`#`]`make modules_install `

`root `[`#`]`make install `

`root `[`#`]`make dtbs `

`root `[`#`]`make dtbs_install `

** Note**\
TODO: test kernel configurations, write defconfig and config guide

## [Installing the bootloader]

### [Option 1: p-boot]

p-boot is a bootloader designed specifically for the pinephone^[\[1\]](#cite_note-1)^. it has a menu that lets the user select different kernels at boot time, like grub does. It also allows booting into FEL mode^[\[2\]](#cite_note-2)^.

** Note**\
TODO: figure this out and get back with an ebuild.

#### [Building from source]

To compile p-boot, the ninja build system and a second compiler (arm-none-eabi-gcc) is needed , which could be acquired with crossdev as so:

`root `[`#`]`emerge -av git ninja crossdev`

`root `[`#`]`crossdev --target arm-none-eabi`

`root `[`#`]`git clone `[`https://megous.com/git/p-boot/`](https://megous.com/git/p-boot/)

`root `[`#`]`cd p-boot/build`

`root `[`#`]`ninja`

then the firmware has to be built, which requires aarch64-linux-musl-gcc and or1k-linux-musl-gcc compilers.

`root `[`#`]`crossdev --target aarch64-linux-musl`

`root `[`#`]`crossdev --target or1k-linux-musl`

`root `[`#`]`cd ../fw`

** Important**\
Default gold linker with lto should be disabled for cross-or1k-linux-musl/musl in portage environment *before* running crossdev for the or1k-linux-musl target.

### [Option 2: U-boot]

u-boot is a a bootloader for embedded devices. it\'s supported by the SoC manufacturer, and works on the pine64 which has the same processor.

** Note**\
TODO: figure this out and get back.

## [Installing the user interface]

** Note**\
TODO: make a separate page for (each?) mobile WM?

### [Option 1: sway with custom configuration]

Sway is a wayland compositor. Unlike window managers such as i3, the user can use the mouse, therefore it would work well on a touchscreen. The user could increase the border size to make windows easier to drag and use window scaling to make things larger. The user just needs to replace dmenu with a touchscreen alternative, make an on-screen keyboard for wayland, could set those to the volume buttons respectively and then set swaylock to [Power]. A way to drag windows between virtual workspaces with the touchscreen is needed. This is slowed down by the phone\'s processor and the lack of touchscreen controls. it takes too long to scroll with the volume buttons for a good user experience.

The user can use [wf-osk](https://github.com/WayfireWM/wf-osk) as an on screen keyboard.

[Volume Up], [Volume Down], and [Power] buttons could be bindsym with XF86XK_AudioRaiseVolume, XF86XK_AudioLowerVolume, and XF86XK_PowerOff repectively.

** Note**\
TODO: include an example \~/.config/sway/config

### [Option 2: Phosh]

Phosh can be installed from the official guru repository.

Enable the repository and sync:

`root `[`#`]`eselect repository enable guru`

`root `[`#`]`emerge --sync`

Install phosh:

`root `[`#`]`emerge phosh-base/phosh-shell`

** Note**\
The user might want to also install a login manager which is capable of functioning under a touchscreen environment

### [Option 3: KDE mobile]

Plasma mobile is available in the [KDE ebuild repository](https://wiki.gentoo.org/wiki/KDE/Ebuild_repository "KDE/Ebuild repository").

## [][Wifi/Bluetooth]

uses RTL8723BS/RTL8723CS

## [GPU]

the Allwinner A64 has a mali 400 GPU, which is supported by the lima driver^[\[3\]](#cite_note-3)^. To enable support for lima, add `VIDEO_CARDS: -* lima` to [/etc/portage/package.use].

The main way programs can take advantage the GPU on this hardware is through OpenGL. Specifically, it supports OpenGL ES 2, so consider using \"gles2\" and \"gles2-only\" alongside other already configured useflags. Don\'t enable the \"opengl\" useflag, as this seems to override the \"gles2-only\" useflag on packages like media-libs/mesa.

[FILE] **`/etc/portage/make.conf`Recommended graphics options**

    USE="gles2 gles2-only"

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* lima

The GPU frequency could also be adjusted. ^[\[4\]](#cite_note-4)^

## [Modem]

The current user needs to be in the plugdev group in order to manipulate texts

## [See also]

-   [PINE64 ROCKPro64](https://wiki.gentoo.org/wiki/PINE64_ROCKPro64 "PINE64 ROCKPro64") --- a Rockchip RK3399 (ARMv8-A, Cortex-A72/A53 big.LITTLE) based, exceptionally libre software friendly SBC.

## [References]

1.  [[[↑](#cite_ref-1)] [[p-boot](https://xnux.eu/p-boot/)]]
2.  [[[↑](#cite_ref-2)] [[FEL mode](https://linux-sunxi.org/FEL)]]
3.  [[[↑](#cite_ref-3)] [[Sunxi wiki on the Allwinner A64](https://linux-sunxi.org/A64)]]
4.  [[[↑](#cite_ref-4)] [[gpu overclocking](https://wiki.pine64.org/wiki/Overclocking#GPU)]]

1.  [U-boot manual](http://www.denx.de/wiki/DULG/Manual)
2.  [sunxi wiki page on the PinePhone](https://linux-sunxi.org/PinePhone)
3.  [building the kernel](https://linux-sunxi.org/Manual_build_howto)
4.  [board support packages](https://linux-sunxi.org/BSP)
5.  [hope](https://linux-sunxi.org/Gentoo)
6.  [hardware/firmware information](https://wiki.pine64.org/index.php/PinePhone)
7.  [modem information](https://wiki.pine64.org/wiki/PineModems)
8.  [\[1\]](https://wiki.pine64.org/index.php/Pine_A64_Software_Release#Gentoo) working image for a similar SBC
9.  [someone\'s pinephone overlay, use with caution](https://gitlab.com/bingch/gentoo-overlay/-/blob/master/README.md)
10. [cpu overclocking](https://linux-sunxi.org/Cpufreq)