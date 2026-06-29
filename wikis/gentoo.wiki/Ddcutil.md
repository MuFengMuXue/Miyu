\

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ddcutil&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://www.ddcutil.com/)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/ddcutil)

[[]][GitHub](https://github.com/rockowitz/ddcutil)

ddcutil is a Linux program for managing monitor settings, such as brightness, color levels, and input source. Generally speaking, any setting that can be changed by pressing buttons on the monitor can be modified by ddcutil.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Configuration]](#Configuration)
        -   [[1.3.1] [I2C]](#I2C)
        -   [[1.3.2] [Permissions]](#Permissions)
            -   [[1.3.2.1] [Granting I2C Device Permissions on Versions Prior to 1.4.0]](#Granting_I2C_Device_Permissions_on_Versions_Prior_to_1.4.0)

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/ddcutil](https://packages.gentoo.org/packages/app-misc/ddcutil) [[]] [Program for querying and changing monitor settings]

  ----------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                                 Add support for X11
  [`drm`](https://packages.gentoo.org/useflags/drm)                             Use x11-libs/libdrm for more verbose diagnostics.
  [`usb-monitor`](https://packages.gentoo.org/useflags/usb-monitor)             Adds support for monitors attached via USB.
  [`user-permissions`](https://packages.gentoo.org/useflags/user-permissions)   Adds a udev rules to allow non-root users in the i2c group to access the /dev/i2c-\* devices. If usb-monitor is selected, users will need to be added to the video group to access the USB monitor. Otherwise, only root will be able to use ddcutil.
  ----------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-21 15:48] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/ddcutil`

### [Configuration]

#### [I2C]

Module [i2c_dev](https://wiki.gentoo.org/wiki/I2C "I2C") should be loaded to allow ddcutil to work. The package should automatically enable this via [/usr/lib/modules-load.d/ddcutil.conf]. If not:

`root `[`#`]`echo "i2c_dev" > /etc/modules-load.d/i2c_dev.conf`

`root `[`#`]`modprobe i2c_dev`

#### [Permissions]

On recent versions (2.2.0 at time of writing, early 2026), [/usr/lib/udev/rules.d/60-ddcutil-i2c.rules] is installed when [[[user-permissions]](https://packages.gentoo.org/useflags/user-permissions)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] is activated. However, 2.2.2 and beyond (currently in testing) contain a fixed udev rule for some hardware, which the user can override locally with

[FILE] **`/etc/udev/rules.d/60-ddcutil-i2c.rules`**

    # fix from ddcutil-2.2.2: 0x03* (see https://github.com/rockowitz/ddcutil/issues/530)
    SUBSYSTEM=="i2c-dev", KERNEL=="i2c-[0-9]*", ATTRS=="0x03*", TAG+="uaccess"
    SUBSYSTEM=="dri", KERNEL=="card[0-9]*", TAG+="uaccess"

\

##### [Granting I2C Device Permissions on Versions Prior to 1.4.0]

It is necessary is to add users who will use ddcutil to group `i2c`

`root `[`#`]`groupadd --system i2c`

`root `[`#`]`modprobe i2c_dev`

Create udev rule for giving group i2c RW permission on the /dev/i2c devices

`root `[`#`]`cp -v /usr/share/ddcutil/data/45-ddcutil-i2c.rules /etc/udev/rules.d`