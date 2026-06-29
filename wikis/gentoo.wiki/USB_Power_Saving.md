[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Power_management/USB&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This article describes the Linux\'s ability to power off USB devices and to let USB devices request to wake them up again.

It is important to note many optical mice do not support power saving. Once they lose power they cannot detect motion and cannot power back on when motion is invoked. With this being stated, it is possible to use specific driver calls or the sysfs [/sys/bus/usb/devices/usb\*/power/control] file to enable or disable auto-suspend for individual USB peripherals.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Set Default USB Autosuspend Delay Value]](#Set_Default_USB_Autosuspend_Delay_Value)
        -   [[1.2.1] [Via Kernel]](#Via_Kernel)
        -   [[1.2.2] [Via Command Line]](#Via_Command_Line)
        -   [[1.2.3] [Via Modprobe]](#Via_Modprobe)
    -   [[1.3] [Udev]](#Udev)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Set autosuspend]](#Set_autosuspend)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Configuration]

### [Kernel]

[KERNEL]

    Device Drivers --->
      [*] USB support ---> Search for <code>CONFIG_USB_SUPPORT</code> to find this item.
        <M> Support for Host-side USB Search for <code>CONFIG_USB</code> to find this item.
        (2) Default autosuspend delay Search for <code>CONFIG_USB_AUTOSUSPEND_DELAY</code> to find this item.

### [Set Default USB Autosuspend Delay Value]

#### [Via Kernel]

The default USB autosuspend delay value can be set in the kernel at compile time. The kernel `CONFIG_` option, `CONFIG_USB_AUTOSUSPEND_DELAY`, can be set to `2`.

#### [Via Command Line]

The default USB autosuspend delay value can be set in the kernel command line. This implementation uses GRUB as an example:

Add `usbcore.autosuspend=2` to the `GRUB_CMDLINE_LINUX_DEFAULT` variable inside the config file found in [/etc/default/grub]. Regenerate the [grub.cfg] config via the [grub2-mkconfig] command and reboot in order for the changes to take effect.

`root `[`#`]`grub2-mkconfig -o /path/to/grub.cfg`

#### [Via Modprobe]

The default USB autosuspend delay value can be set as an option when the USB module loads.

** Important**\
`CONFIG_USB` must be set to `M` for this to work!

[FILE] **`/etc/modprobe.d/usb.conf`**

    options usbcore autosuspend=2

### [Udev]

Make the following [udev](https://wiki.gentoo.org/wiki/Udev "Udev") rule file to automate power management:

[FILE] **`/etc/udev/rules.d/10-my-usb-power.rules`**

    # USB autosuspend
    ACTION=="add", SUBSYSTEM=="usb", ATTR="auto"
    ACTION=="add", SUBSYSTEM=="usb", TEST=="power/autosuspend" ATTR="60"

**[ Proposed changes ]** [- Please make edits here until a final revision is agreed upon.]\
\
[ **Todo:**]

-   I don\'t know enough about udev to know if this information is correct and/or redundant to the existing udev rules.
-   Delete this proposal?

\

Enforce for every device:

[FILE] **`/etc/udev/rules.d/60-power.rules`**

    SUBSYSTEM!="usb", GOTO="power_usb_rules_end"
    ACTION!="add", GOTO="power_usb_rules_end"

    KERNEL=="[0-9]*:*", WAIT_FOR_SYSFS="bInterfaceProtocol"
    PROGRAM="/bin/sleep 0.1"

    ATTR=="*", ATTR="auto"

    LABEL="power_usb_rules_end"

## [Usage]

### [Set autosuspend]

We can set an autosuspend time for a specific USB device using a local.d service. There are many ways to do this besides using a local.d service, but the method is the same: write a value to the file, [/sys/bus/usb/devices/\*-\*/power/control]. The value can be a number (representing the number of seconds to delay the suspension) or \"`auto`\" (to use the default value set in the kernel).

Run [lsusb] to list all USB devices with their bus and device numbers:

`root `[`#`]`lsusb`

    Bus 007 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 006 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 002: ID 05af:1012 Jing-Mold Enterprise Co., Ltd
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 003 Device 002: ID 09da:9090 A4Tech Co., Ltd. XL-730K / XL-750BK / XL-755BK Mice
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub

As an example, we want a USB device (such as the **A4Tech** mouse listed above) to autosuspend after being in the idle state for 45 minutes.

**[ Proposed changes ]** [- Please make edits here until a final revision is agreed upon.]\
\
[ **Todo:**]

-   The following information is false; a `Bus-Device` directory doesn\'t always exist for a specific USB device.
-   Fix the instructions to correctly identify and configure specific devices.

\

Add the following file into the local.d services:

[FILE] **`/etc/local.d/mouse_auto_sleep.start`**

    echo "<value>" > /sys/bus/usb/devices/3-3/power/control

As we see here, the bus number of the mouse is 3 and the device number of 2 is auto-increased by 1 by the kernel into 3 (its usual behavior). `<value>` can be a number (representing the number of seconds the delay is) or \"auto\" (use the kernel default value). If the kernel\'s default value is already set to `2700` (60 \* 45 = 2700), then we can use `auto`; otherwise, we can use `2700`.

Don\'t forget to make the local.d file executable:

`root `[`#`]`chmod +x /etc/local.d/mouse_auto_sleep.start`

If we reboot, the **A4Tech** mouse should autosuspend after being in the idle state for 45 minutes.

Read [/usr/src/linux/Documentation/usb/power-management.txt] for more information on power management in Linux.

## [See also]

-   [USB](https://wiki.gentoo.org/wiki/USB "USB") --- the setup of **USB** (Universal Serial Bus) controllers

## [External resources]

-   [https://github.com/mvp/uhubctl](https://github.com/mvp/uhubctl) - USB hub per-port power control