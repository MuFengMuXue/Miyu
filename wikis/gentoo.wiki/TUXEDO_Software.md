[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=TUXEDO_Software&action=edit).

**Resources**

[[]][Home](https://github.com/tuxedocomputers)

[![](/images/thumb/b/bf/Screenshot_20220423-191112.png/300px-Screenshot_20220423-191112.png)](https://wiki.gentoo.org/wiki/File:Screenshot_20220423-191112.png)

[](https://wiki.gentoo.org/wiki/File:Screenshot_20220423-191112.png "Enlarge")

TUXEDO Control Center UI

This article is a guide about installing TUXEDO\'s Linux drivers and Control Center on Gentoo Linux - software for vendor-specific TUXEDO hardware.

## Contents

-   [[1] [Kernel]](#Kernel)
-   [[2] [Drivers]](#Drivers)
-   [[3] [Control Center]](#Control_Center)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Kernel]

First enable these Kernel options^[\[1\]](#cite_note-1)^ to make the compiling of [[[app-laptop/tuxedo-keyboard]](https://packages.gentoo.org/packages/app-laptop/tuxedo-keyboard)[]] and [[[sys-power/tuxedo-cc-wmi]](https://packages.gentoo.org/packages/sys-power/tuxedo-cc-wmi)[]] packages possible.

[KERNEL] **Enable ACPI WMI in 6.1.31-gentoo**

    [*] Networking Support  --->
      <*> RF switch subsystem support
    Device Drivers  --->
      Input device support  --->
        [*] Generic input layer (needed for keyboard, mouse, ...)
       Hardware Monitoring support
      Graphics support  --->
        Backlight & LCD device support  --->
          [*] Lowlevel Backlight controls
      [*] X86 Platform Specific Device Drivers  --->
         WMI

## [Drivers]

`root `[`#`]`emerge --ask app-laptop/tuxedo-keyboard`

These modules should be automatically loaded when booting:^[\[2\]](#cite_note-2)^

[FILE] **`/etc/modules-load.d/tuxedo.conf`Load custom modules at boot**

    tuxedo_keyboard
    tuxedo_io
    clevo_acpi
    clevo_wmi

To configure the backlighting of the laptop\'s keyboard, edit [/etc/modprobe.d/tuxedo_keyboard.conf]. For other configuration options, see the [tuxedo-keyboard README](https://github.com/tuxedocomputers/tuxedo-keyboard#sysfs-).

[FILE] **`/etc/modprobe.d/tuxedo_keyboard.conf`Static white backlighting**

    options tuxedo_keyboard mode=0 color_left=0xFFFFFF color_center=0xFFFFFF color_right=0xFFFFFF

It is also possible to configure the keyboard via the [TUXEDO Control Center](https://wiki.gentoo.org/wiki/TUXEDO_Software#Control_Center "TUXEDO Software"). But effects, e. g. "Wave", are not configurable in the UI yet.

Before rebooting, add this service:

`root `[`#`]`rc-update add tccd default`

## [Control Center]

TUXEDO Computers provides an application to control various hardware components. A binary package exists in the Gentoo tree.

`root `[`#`]`emerge --ask app-laptop/tuxedo-control-center-bin`

## [See also]

-   [TUXEDO Aura 15 (Gen2)](https://wiki.gentoo.org/wiki/TUXEDO_Aura_15_(Gen2) "TUXEDO Aura 15 (Gen2)") --- a configurable Linux notebook from 2022.
-   [TUXEDO InfinityBook Pro 15 (Gen10)](https://wiki.gentoo.org/wiki/TUXEDO_InfinityBook_Pro_15_(Gen10) "TUXEDO InfinityBook Pro 15 (Gen10)") --- a configurable Linux notebook from 2025.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://forums.gentoo.org/viewtopic-t-926426-start-0.html](https://forums.gentoo.org/viewtopic-t-926426-start-0.html)]]
2.  [[[↑](#cite_ref-2)] [[https://github.com/tuxedocomputers/tuxedo-keyboard#description-](https://github.com/tuxedocomputers/tuxedo-keyboard#description-)]]