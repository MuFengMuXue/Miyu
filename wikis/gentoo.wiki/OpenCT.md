*Not to be confused with [OpenCL](https://wiki.gentoo.org/wiki/OpenCL "OpenCL").*

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/CT-API "wikipedia:CT-API")

**CTAPI** is a German standard for PC to smartcard reader communication, which is implemented by OpenCT. The international standard is in contrast [PC/SC](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Permissions]](#Permissions)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [OpenRC]](#OpenRC)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Listing readers]](#Listing_readers)

## [Installation]

### [Kernel]

You have to enable kernel support depending on how your cardreader is connected:

-   For USB cardreader see the [USB](https://wiki.gentoo.org/wiki/USB "USB") article.
-   For PC-Card cardreader see the [PC-Card](https://wiki.gentoo.org/wiki/PC-Card "PC-Card") article.
-   For serial cardreader enable serial support.

### [USE flags]

Portage knows the global `openct` USE flag for enabling support for OpenCT in other packages. Enabling this USE flag will pull in [[[dev-libs/openct]](https://packages.gentoo.org/packages/dev-libs/openct)[]] automatically:

[FILE] **`/etc/portage/make.conf`**

    USE="openct"

Other USE flags of openct include:

### [USE flags for] [dev-libs/openct](https://packages.gentoo.org/packages/dev-libs/openct) [[]] [library for accessing smart card terminals]

  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)           Add debug output to the driver library for pcsc-lite.
  [`doc`](https://packages.gentoo.org/useflags/doc)               Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`pcsc-lite`](https://packages.gentoo.org/useflags/pcsc-lite)   Build a driver library for sys-apps/pcsc-lite, providing PC/SC API access to devices supported by OpenCT.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)       !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`usb`](https://packages.gentoo.org/useflags/usb)               Add USB support to applications that have optional USB support (e.g. cups)
  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After setting this you want to update your system so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

## [Configuration]

### [Permissions]

Add your user to the *openct* group to be able to access the cardreader:

`root `[`#`]`gpasswd -a larry openct`

### [Services]

#### [OpenRC]

To tart OpenCT:

`root `[`#`]`/etc/init.d/openct start`

To start OpenCT at boot time, add it the default runlevel:

`root `[`#`]`rc-update add openct default`

** Note**\
The OpenCT daemon blocks all detected cardreaders for every other software. An exception is, if you use the ifdhandler for PCSC-Lite.

## [Usage]

### [Listing readers]

List all detected cardreaders:

`user `[`$`]`openct-tool list`

If there is a detected cardreader, insert a smartcard. Test the access by checking the [ATR](https://en.wikipedia.org/wiki/Answer_to_reset "wikipedia:Answer to reset"):

`user `[`$`]`openct-tool atr`

    Detected CCID Compatible
    Card present, status changed
    ATR: 3B 75 94 00 00 62 02 02 03 01