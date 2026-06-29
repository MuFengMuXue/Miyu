**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/iBook "wikipedia:iBook")

[[]][[#mac](ircs://irc.libera.chat/#mac)] ([[webchat](https://web.libera.chat/#mac)])

[[]][[#gentoo-powerpc](ircs://irc.libera.chat/#gentoo-powerpc)] ([[webchat](https://web.libera.chat/#gentoo-powerpc)])

[[]][[comp.sys.mac.vintage](news:comp.sys.mac.vintage) ([weblink](https://www.novabbs.com/devel/thread.php?group=comp.sys.mac.vintage))]

[[]][r/PowerPC](https://reddit.com/r/PowerPC)

The Apple Macintosh **PowerBook4,1**, also known as the iBook [G3](https://en.wikipedia.org/wiki/PowerPC_7xx "wikipedia:PowerPC 7xx") Snow M6497, is an Apple laptop computer with a single core 32-bit [PowerPC](https://wiki.gentoo.org/wiki/PPC "PPC") 750cx (G3) CPU. It shipped with either [Mac OS 9.2.1](https://en.wikipedia.org/wiki/Mac_OS_9 "wikipedia:Mac OS 9") or [Mac OS X 10.1 - Puma](https://en.wikipedia.org/wiki/Mac_OS_X_10.1 "wikipedia:Mac OS X 10.1") preinstalled. The last version of OS X that can be installed on the device is [Mac OS X 10.4 - Tiger](https://en.wikipedia.org/wiki/Mac_OS_X_Tiger "wikipedia:Mac OS X Tiger"), as it is the last version of Mac OS X to support 32-bit PowerPC processors.

This system is not compatible with the unofficial Mac OS X build [Mac OS X 10.5.9 - Sorbet Leopard](https://apple.fandom.com/wiki/Sorbet_Leopard), as that requires a G4 or G5 PowerPC CPU.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Portage make.conf]](#Portage_make.conf)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Why is USB so slow?]](#Why_is_USB_so_slow.3F)
    -   [[4.2] [How do I boot from a USB device?]](#How_do_I_boot_from_a_USB_device.3F)
    -   [[4.3] [X doesn\'t start; segfaults at address 0x48]](#X_doesn.27t_start.3B_segfaults_at_address_0x48)
    -   [[4.4] [Display loses synchronization when starting X]](#Display_loses_synchronization_when_starting_X)
    -   [[4.5] [Graphical artifacts in more complex applications; desktop wallpaper doesn\'t render]](#Graphical_artifacts_in_more_complex_applications.3B_desktop_wallpaper_doesn.27t_render)
    -   [[4.6] [Why can\'t I have an internal hard disk \> 137 GB?]](#Why_can.27t_I_have_an_internal_hard_disk_.3E_137_GB.3F)
    -   [[4.7] [How do I increase system disk or swap device performance?]](#How_do_I_increase_system_disk_or_swap_device_performance.3F)
    -   [[4.8] [Known GCC 15 build failures]](#Known_GCC_15_build_failures)
-   [[5] [See Also]](#See_Also)
-   [[6] [External resources]](#External_resources)

## [Hardware]

The PowerBook4,1 M6947 is a 12\" laptop from 2001-2002. It came in a few variants, with differences in preinstalled RAM, CPU clock speed, disk size, and the optional inclusion of an AirPort wireless card.

  --------------- ------------------------------------------- ----------- ------------------------ --------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device          Make/model                                  Status      Vendor ID / Product ID   Kernel driver   Notes
  CPU             PowerPC 750cx (G3) (500 or 600 MHz)         Works       ---                      ---             Not upgradable
  RAM             PC100 SDRAM (64-640MB)                      Works       ---                      ---             1× 144-pin slot. Early models offered 64 MB built-in, while later ones were minimum 128 MB. The slot will take up to a 512 MB module, for a maximum of 576/640 MB.
  Graphics        ATI Rage Mobility 128 AGP 2X                Works       `1002:4c46`              `aty128fb`      8MB VRAM. The DRI1 DRM driver was removed from the kernel in 6.3. Support was removed from Mesa 11 years earlier in 8.0. The [fbdev](https://wiki.gentoo.org/wiki/Framebuffer "Framebuffer") driver sticks around, though.
  Hard Drive      10, 15, or 20 GB 2.5\" PATA/100             Works       ---                      ---             137 GB max drive capacity.
  Optical Drive   TOSHIBA DVD-ROM SD-R2002                    Works       ---                      `sr-mod`        ---
  WiFi            802.11b                                     Untested    ---                      `orinoco`       No WPA2 support. A USB WiFi dongle should work, but it will be limited by USB 1.1\'s maximum of 12Mbps.
  Ethernet        Apple Inc. UniNorth/Pangea GMAC (Sun GEM)   Works       `106b:0024`              `sungem`        ---
  USB 1.1         2× Apple Inc. KeyLargo/Pangea USB           Works       `106b:0026`              `ohci-pci`      2× USB-A ports
  Firewire 400    Apple Inc. UniNorth/Pangea FireWire         Untested    `106b:0030`              ---             1× 6-pin port
  --------------- ------------------------------------------- ----------- ------------------------ --------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Installation]

The PowerBook4,1 does not support booting from USB, but it will detect and boot the Gentoo LiveCD from the built-in optical drive with no workarounds. The built-in boot menu can be accessed by holding [⌥ Option] on power-up, just like on Intel x86-based Macs. After booting, install the system as usual, following the [PPC Handbook](https://wiki.gentoo.org/wiki/Handbook:PPC "Handbook:PPC").

It is a good idea to max out the RAM, and allocate a sufficiently sized [swap](https://wiki.gentoo.org/wiki/Swap "Swap") file or partition. It is possible to compile with a 4GB swap, however as this is slow it is recommended to follow the *Building for other Architectures* section of the [Binary package guide](https://wiki.gentoo.org/wiki/Binary_package_guide#Building_for_other_architectures "Binary package guide") instead.

## [Configuration]

### [Portage make.conf]

The `-mcpu` flag for the PowerPC 750cx is `-mcpu=750`. No additional flags are added by setting it to `native`, so this is enough for compiling on another system:

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="-mcpu=750 -O2 -pipe"
    CFLAGS="$"
    CXXFLAGS="$"

## [Troubleshooting]

### [][Why is USB so slow?]

Welcome to USB 1.1.

Maximum *theoretical* data rate of USB 1.1 is 12 Mbit/s (1.5MB/s). In practice this figure will be lower. Firewire is faster at 400 Mbit/s (50MB/s), but still less than half the speed of USB 2.0 and far slower than the 5 Gbit/s of USB 3.0.

### [][How do I boot from a USB device?]

You can\'t.

The Open Firmware version that ships with the device is 3.*x*. Open Firmware added support for booting from USB in Open Firmware 4.8. There is no technical reason why it shouldn\'t be possible to either backport USB boot support from 4.8 to the 3.*x* branch or make 4.8 bootable from the device. Either option would presumably require a significant reverse engineering and development effort.

### [][X doesn\'t start; segfaults at address 0x48]

If you attempt to invoke [startx] or autostart the X11 environment on boot and encounter an error that looks something like this:

    [  1247.492] (EE) Segmentation fault at address 0x48
    [  1247.492] (EE)
    Fatal server error:
    [  1247.492] (EE) Caught signal 11 (Segmentation fault). Server aborting

And/or a [dmesg] entry that looks something like this:

    [24775.983164] aty128fb 0000:00:10.0: Invalid PCI ROM header signature: expecting 0xaa55, got 0x8181

You have encountered a known bug in the [[[x11-drivers/xf86-video-r128]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-r128)[]] DDX driver caused by it expecting to find a VGA BIOS ROM that does not exist on non-x86 systems. ([patch](https://raw.githubusercontent.com/void-linux/void-packages/refs/heads/master/srcpkgs/xf86-video-r128/patches/fix-non-x86.patch)). See: [[[bug #956651]](https://bugs.gentoo.org/show_bug.cgi?id=956651)[]].

### [Display loses synchronization when starting X]

This is a known issue in the [[[x11-drivers/xf86-video-r128]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-r128)[]] DDX driver. From [[[r128(4)]](https://man.archlinux.org/man/r128.4.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")]:

> Dualhead Note: The video BIOS on some laptops interacts strangely with dualhead. This can result in flickering and problems changing modes on crtc2. If you experience these problems try toggling your laptop\'s video output switch (*e.g.,* [fn]-[F7], etc.) prior to starting X, or switch to another VT and back.

This is a long standing issue and there is no patch for this. Anyone desiring to take a deep look into the problem is encouraged to share any patches they create with the [upstream project](https://www.x.org/).

### [][Graphical artifacts in more complex applications; desktop wallpaper doesn\'t render]

This is due to bugs in the [[[x11-drivers/xf86-video-r128]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-r128)[]] driver. The solution is to to use [[[x11-drivers/xf86-video-fbdev]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-fbdev)[]] instead. Despite being a generic software rendering driver, it tends to perform faster and use less CPU time than [[[x11-drivers/xf86-video-r128]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-r128)[]] when dealing with applications and toolkits that submit buffers to the server rather than making X drawing calls, such as GTK3.

### [][Why can\'t I have an internal hard disk \> 137 GB?]

This is a limitation of 28-bit LBA addressing. This is a limit imposed by the system\'s disk controller. There is no way around it. Keep in mind this is a limit for the *entire disk* not merely [partitions](https://wiki.gentoo.org/wiki/Partition "Partition") on the disk. Modern SATA devices attached to the USB or Firewire ports will not have this limitation.

### [][How do I increase system disk or swap device performance?]

The PATA/100 disk bus is limited to 100 MB/s, but a spinning disk will not get this performance outside of the drive cache. Opting for an SSD will likely result in disk operations at or near the maximum speed. That said, there is more than one factor to consider here.

Depending on the system workload, it may help to migrate the swap partition to a FireWire device, even though its bus speed is half that of the main IDE bus. Such a configuration may eliminate resource contention on the IDE bus and improve overall performance.

### [Known GCC 15 build failures]

[GCC 15](https://wiki.gentoo.org/wiki/GCC "GCC") follows the [C23](https://en.wikipedia.org/wiki/C23_(C_standard_revision) "wikipedia:C23 (C standard revision)") standard by default. This causes a number of changes to default compiler behavior. Unforunately, this breaks some packages. See [Modern C porting](https://wiki.gentoo.org/wiki/Modern_C_porting "Modern C porting").

The following packages are known to fail to build but have patches in the works:

-   [[[app-laptop/pbbuttonsd]](https://packages.gentoo.org/packages/app-laptop/pbbuttonsd)[]], required for LCD backlight control with the keyboard outside of X. ([patch](https://raw.githubusercontent.com/gentoo/gentoo/d4eb54937b0cd4ff01ef2cc47aced7f01214c45d/app-laptop/pbbuttonsd/files/pbbuttonsd-0.8.1a-fix-build-with-gcc-15.patch)) Also see ([patch](https://raw.githubusercontent.com/gentoo/gentoo/e9b9571b2f0f823b302d59e2c355ee903d3b85f3/app-laptop/pbbuttonsd/files/pbbuttonsd-0.8.1a-fix-build-with-dash.patch)) if using [[[app-shells/dash]](https://packages.gentoo.org/packages/app-shells/dash)[]] as [/bin/sh]; see [Project:Base/Alternatives](https://wiki.gentoo.org/wiki/Project:Base/Alternatives "Project:Base/Alternatives").
    -   [[[bug #948138]](https://bugs.gentoo.org/show_bug.cgi?id=948138)[]]
    -   [[[bug #947851]](https://bugs.gentoo.org/show_bug.cgi?id=947851)[]]
    -   [[[bug #946207]](https://bugs.gentoo.org/show_bug.cgi?id=946207)[]]
    -   [[[bug #944303]](https://bugs.gentoo.org/show_bug.cgi?id=944303)[]]
    -   [[[bug #941868]](https://bugs.gentoo.org/show_bug.cgi?id=941868)[]]
    -   [[[bug #927480]](https://bugs.gentoo.org/show_bug.cgi?id=927480)[]]
    -   [[[bug #886071]](https://bugs.gentoo.org/show_bug.cgi?id=886071)[]]
    -   [[[bug #881503]](https://bugs.gentoo.org/show_bug.cgi?id=881503)[]]
    -   [[[bug #771864]](https://bugs.gentoo.org/show_bug.cgi?id=771864)[]]
-   [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]], Linux kernel built with Gentoo patches. Fixed ≥6.16.0. (pre-6.16.0 [patch](https:////github.com/torvalds/linux/commit/5a821e2d69e26b51b7f3740b6b0c3462b8cacaff.patch))
    -   Fixed upstream as of kernel version 6.16.0, no corresponding Gentoo bug.
-   [[[sys-apps/ibm-powerpc-utils]](https://packages.gentoo.org/packages/sys-apps/ibm-powerpc-utils)[]], Utilities for the maintenance of the IBM and Apple PowerPC platforms. ([patch](https://github.com/ibm-power-utilities/powerpc-utils/commit/f61fb364d92b2e0f425c89bf9c2d7c1ca75d8fa3.patch))
    -   [[[bug #955092]](https://bugs.gentoo.org/show_bug.cgi?id=955092)[]]

## [See Also]

-   [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") --- a heavily stack-oriented self-compiling procedural programming language that is only slightly more abstract than [assembly](https://wiki.gentoo.org/wiki/Assembly_language "Assembly language").
-   [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware") --- an [IEEE 1275-1994](https://ieeexplore.ieee.org/document/763383) standard for hardware independent firmware built on top of a [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") machine.

## [External resources]

-   [Mac OS X 10.5.9 - Sorbet Leopard](https://apple.fandom.com/wiki/Sorbet_Leopard) --- a community build of OS X for G4/G5 Macs.
-   [Forth Lessons](https://wiki.laptop.org/go/Forth_Lessons) --- a in-depth series of progressive lessons on the [Forth](https://wiki.gentoo.org/wiki/Forth "Forth") programming language, useful for understanding [Open Firmware](https://wiki.gentoo.org/wiki/Open_Firmware "Open Firmware").