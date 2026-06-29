Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Nouveau/es "Nouveau (58% translated)")
-   [français](https://wiki.gentoo.org/wiki/Nouveau/fr "Nouveau (62% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Nouveau/hu "nouveau (85% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Nouveau/pl "Nouveau/pl (2% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Nouveau/ru "nouveau (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Nouveau/ja "nouveau (73% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Nouveau/ko "nouveau/ko (47% translated)")

**Resources**

[[]][Home](https://nouveau.freedesktop.org/wiki/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/nouveau_(software) "wikipedia:nouveau (software)")

[[]][[#nouveau](ircs://irc.libera.chat/#nouveau)] ([[webchat](https://web.libera.chat/#nouveau)])

**nouveau** is an open source driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards. It is maintained under the umbrella of the FreeDesktop project. Nouveau shouldn\'t be confused with the open source components on the official [Nvidia drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers#Open_source_kernel_modules "NVIDIA/nvidia-drivers").

## Contents

-   [[1] [Limitations]](#Limitations)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Firmware]](#Firmware)
    -   [[2.3] [Driver]](#Driver)
    -   [[2.4] [Udev]](#Udev)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Permissions]](#Permissions)
    -   [[3.2] [xorg.conf]](#xorg.conf)
-   [[4] [Enabling the Mesa NVK Vulkan driver]](#Enabling_the_Mesa_NVK_Vulkan_driver)
-   [[5] [Switching between Intel GPU and Nouveau]](#Switching_between_Intel_GPU_and_Nouveau)
-   [[6] [Limitations]](#Limitations_2)
-   [[7] [Troubleshooting]](#Troubleshooting)
    -   [[7.1] [Multi-monitor problems]](#Multi-monitor_problems)
    -   [[7.2] [Nouveau loads but lacks 3D acceleration]](#Nouveau_loads_but_lacks_3D_acceleration)
-   [[8] [See also]](#See_also)
-   [[9] [External resources]](#External_resources)

## [Limitations]

Being an open source project running on what is largely proprietary hardware, there are some limitations inherent to Nouveau that are not applicable to the closed-source [nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers"). That said, Nouveau is constantly evolving, so these limitations are subject to change over time.

Those interested in using this driver should verify support has been added for the card (and features) in question by referencing [upstream\'s feature matrix](https://nouveau.freedesktop.org/wiki/FeatureMatrix/). Upstream also keeps a [list of card code names](https://nouveau.freedesktop.org/wiki/CodeNames) to cross reference from the feature matrix.

## [Installation]

### [Kernel]

Activate the following kernel options:

[KERNEL] **Enabling nouveau**

    Device Drivers  --->
       Graphics support  --->
          <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support) Search for <code>CONFIG_DRM</code> to find this item.  --->
              [*] Enable legacy fbdev support for your modesetting driver Search for <code>CONFIG_DRM_FBDEV_EMULATION</code> to find this item.
              <M/*> Nouveau (NVIDIA) cards Search for <code>CONFIG_DRM_NOUVEAU</code> to find this item.

### [Firmware]

Beginning with the Kepler series (GeForce 600 and above), some cards may need to load firmware at boot time in order to operate correctly. It is recommended to build firmware that is needed into the kernel. This is the default for systems running the systemd init system. See the [Linux firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") article for more information on building firmware into the kernel.

See upstream\'s [list of codenames](https://nouveau.freedesktop.org/wiki/CodeNames/) to determine what firmware is necessary.

Firmware for nouveau cards are distributed in the [[[sys-firmware/nvidia-firmware]](https://packages.gentoo.org/packages/sys-firmware/nvidia-firmware)[]] package. Be sure it has been installed before defining firmware in the kernel:

`root `[`#`]`emerge --ask sys-firmware/nvidia-firmware`

### [Driver]

[FILE] **`/etc/portage/package.use/00video`Set `VIDEO_CARDS` to nouveau**

    */* VIDEO_CARDS: -* nouveau

After setting or altering `VIDEO_CARDS` values remember to update the system using the following command so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

### [Udev]

If NVIDIA\'s proprietary driver has been installed, it will have installed a udev rules file in [/lib/udev/rules.d/99-nvidia.rules]. When attempting to use the nouveau driver without disabling that rule file, the X11 log file fill up with a block of messages like this repeating every 10ms:

[FILE] **`/var/log/Xorg.0.log`Results of obsolete udev rule for nvidia-drivers**

     [   180.669] (II) NOUVEAU(0): EDID vendor "SAM", prod id 430
     [   180.669] (II) NOUVEAU(0): Using hsync ranges from config file
     [   180.669] (II) NOUVEAU(0): Using vrefresh ranges from config file
     [   180.669] (II) NOUVEAU(0): Printing DDC gathered Modelines:
     [   180.669] (II) NOUVEAU(0): Modeline "1600x1200"x0.0  162.00  1600 1664 1856 2160  1200 1201 1204 1250 +hsync +vsync (75.0 kHz eP)
     [   180.669] (II) NOUVEAU(0): Modeline "800x600"x0.0   40.00  800 840 968 1056  600 601 605 628 +hsync +vsync (37.9 kHz e)
     [   180.669] (II) NOUVEAU(0): Modeline "800x600"x0.0   36.00  800 824 896 1024  600 601 603 625 +hsync +vsync (35.2 kHz e)
     [...]
     [   180.669] (II) NOUVEAU(0): Modeline "1152x864"x0.0  108.00  1152 1216 1344 1600  864 865 868 900 +hsync +vsync (67.5 kHz e)
     [   180.669] (II) NOUVEAU(0): Modeline "1280x1024"x0.0  108.00  1280 1328 1440 1688  1024 1025 1028 1066 +hsync +vsync (64.0 kHz e)
     [   180.669] (II) NOUVEAU(0): Modeline "1280x960"x0.0  108.00  1280 1376 1488 1800  960 961 964 1000 +hsync +vsync (60.0 kHz e)
     [   180.669] removing GPU device /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0/drm/card2 /dev/dri/card2

To prevent this (without uninstalling the [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package), simply remove/move/rename the udev file [/lib/udev/rules.d/99-nvidia.rules] so that is no longer taken up by udev (see [Advanced Configuration of udev](https://wiki.gentoo.org/wiki/Udev#Advanced_Configuration "Udev")). Note that the next time nvidia-drivers is updated, that file will be re-installed, so consider unmerging nvidia-drivers.

## [Configuration]

### [Permissions]

If the [`acl`](https://packages.gentoo.org/useflags/acl) USE flag is enabled globally and [`elogind`](https://packages.gentoo.org/useflags/elogind) is being used (default for desktop profiles) permissions to video cards will be handled automatically. It is possible to check the permissions using [getfacl]:

`user `[`$`]`getfacl /dev/dri/card0 | grep larry`

`user:`**`larry`**`:rw-`

A broader solution is to add the user(s) needing access the video card to the [video] group:

`root `[`#`]`gpasswd -a larry video`

Note that users will be able to run X without permission to the DRI subsystem, but hardware acceleration will be disabled.

### [xorg.conf]

The [X server](https://wiki.gentoo.org/wiki/X_server "X server") is designed to work out-of-the-box, with no need to manually edit X.Org\'s configuration files. It should detect and configure devices such as displays, keyboards, and mice.

However, the main configuration file of the X server is the [[xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf")] file.

## [Enabling the Mesa NVK Vulkan driver]

NVK is an open-source Vulkan driver based on Nouveau for Kepler and newer NVIDIA cards. Support for it can be enabled via adding `nvk` to the [VIDEO_CARDS](https://wiki.gentoo.org/wiki//etc/portage/make.conf#VIDEO_CARDS "/etc/portage/make.conf") variable, as explained in the [Vulkan](https://wiki.gentoo.org/wiki/Vulkan "Vulkan") article.

[FILE] **`/etc/portage/package.use/00video`Set `VIDEO_CARDS` to nouveau+nvk**

    */* VIDEO_CARDS: -* nouveau nvk

Again, to apply changes, remember to update the system:

`root `[`#`]`emerge --ask --changed-use --deep @world`

## [Switching between Intel GPU and Nouveau]

Sometimes users may want to switch between two drivers. One way this matter is handled is through [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") and early [Kernel Mode Setting](https://nouveau.freedesktop.org/KernelModeSetting.html).

For example, if [initramfs](https://wiki.gentoo.org/wiki/Initramfs "Initramfs") is built using [dracut](https://wiki.gentoo.org/wiki/Dracut "Dracut"), and nouveau is meant to be used, the following adjustments must take place:

[FILE] **`/etc/dracut.conf`**

    #add_drivers+=" i915 " # Note leading and trailing spaces
    add_drivers+=" nouveau " # Note leading and trailing spaces
    #force_drivers+=" i915 " # Note leading and trailing spaces
    force_drivers+=" nouveau " # Note leading and trailing spaces

In kernel mode setting method using [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"), the variable `GRUB_CMDLINE_LINUX_DEFAULT` in [/etc/default/grub] can be changed to enable or disable either of GPUs by taking the right values.

For instance, to disable i915 and enable nouveau, we will add the following to `GRUB_CMDLINE_LINUX_DEFAULT` variable: `i915.modeset=0 nouveau.modeset=1`.

## [Limitations]

Some of the current issues or draw-backs compared to the closed-source [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] are stated below:

-   Performance (especially 3D performance) on the same card/chipset may be significantly worse than using nvidia-drivers.
-   Attempts to run at higher refresh rates (i.e. above 60 Hz) may fail.
-   Using advanced features from various NVIDIA cards (e.g. multiple-display capabilities of Quadro cards without SLI) may not function correctly.

## [Troubleshooting]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=xf86-video-nouveau&order=bug_id%20DESC)[]]
-   [[[Freedesktop.org bugtracker: known bugs]](https://bugs.freedesktop.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=CONFIRMED&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=NEEDINFO&bug_status=PLEASETEST&bug_status=IN_PROGRESS&product=xorg&component=Driver%2Fnouveau&order=bug_id%20DESC)[]]

### [Multi-monitor problems]

When the screen freezes often with possible EDID probes while using dual monitors/displays, try adding `video=VGA-1:e` or `video=VGA-1:d` (enable or disable respectively) to the `GRUB_CMDLINE_LINUX_DEFAULT` variable in the [/etc/default/grub] file for [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB") or the respective kernel command-line option for other loaders. Make sure to substitute the name of the monitor listed within [dmesg] or [/var/log/Xorg.0.log] (i.e. CRT-1, VGA-1, LVDS-1, DVI-1, \...)

For instance, on a Dell Inspiron 8100 laptop with a connected external display connected via the laptop\'s external VGA port, a possible command line is: `video=LVDS-1:1280x1024@60 video=VGA-1:1280x1024@60`. The EDID (DRM) probe on the external VGA connected display is still causing freezing during nouveau/DRM load for the author, but at least it\'s usable if the display is connected after GRUB is loaded and prior to the nouveau/DRM modules loading. And with the prior mentioned command line LVDS/VGA resolutions, the displays are cloned and centred with somewhat correct resolutions for cloned displays.

### [Nouveau loads but lacks 3D acceleration]

If the desktop environment or window manager seems to run slow, check that [[[x11-drivers/xf86-video-nouveau]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-nouveau)[]] is installed on the system. If not, it can be emerged manually:

`root `[`#`]`emerge --ask x11-drivers/xf86-video-nouveau`

## [See also]

-   [NVIDIA/nvidia-drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") --- The [[[x11-drivers/nvidia-drivers]](https://packages.gentoo.org/packages/x11-drivers/nvidia-drivers)[]] package contains the *proprietary* graphics driver for [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA") graphic cards.
-   [Nouveau & nvidia-drivers switching](https://wiki.gentoo.org/wiki/Nouveau_%26_nvidia-drivers_switching "Nouveau & nvidia-drivers switching") --- describes how to switch between [NVIDIA\'s binary driver](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers") and the open source [nouveau] driver.
-   [Hprofile](https://wiki.gentoo.org/wiki/Hprofile "Hprofile") --- an application that can be used to manage multiple profiles be it hardware or software.

## [External resources]

-   [https://nouveau.freedesktop.org/wiki/VideoAcceleration/](https://nouveau.freedesktop.org/wiki/VideoAcceleration/) - This wiki page provides an overview of NVIDIA cards that support hardware acceleration by VDPAU.
-   [https://nouveau.freedesktop.org/wiki/KernelModuleParameters/](https://nouveau.freedesktop.org/wiki/KernelModuleParameters/) - Provides a list of possible parameters to pass to the nouveau kernel module.