**Resources**

[[]][Home](https://pcsclite.apdu.fr/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/PC/SC "wikipedia:PC/SC")

PCSC-Lite implements the PC/SC international standard for PC to smartcard reader communication.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [SystemD]](#SystemD)
        -   [[2.1.2] [OpenRC]](#OpenRC)
-   [[3] [Testing]](#Testing)
-   [[4] [See also]](#See_also)

## [Installation]

### [Kernel]

The kernel configuration depends on how the card reader is connected:

-   For USB card reader see the [USB](https://wiki.gentoo.org/wiki/USB "USB") article.
-   For PC-Card card reader see the [PC-Card](https://wiki.gentoo.org/wiki/PC-Card "PC-Card") article.
-   For serial card reader enable serial support.

### [USE flags]

Some packages are aware of the [[[pcsc-lite]](https://packages.gentoo.org/useflags/pcsc-lite)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag").

### [USE flags for] [sys-apps/pcsc-lite](https://packages.gentoo.org/packages/sys-apps/pcsc-lite) [[]] [PC/SC Architecture smartcard middleware library]

  ----------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+udev`](https://packages.gentoo.org/useflags/+udev)             Use virtual/libudev rules to handle devices\' permissions and hotplug support. Unless you know what you\'re doing do not disable this flag on Linux kernels. This is provided as an option for completeness.
  [`embedded`](https://packages.gentoo.org/useflags/embedded)       limit RAM and CPU ressources by disabling features
  [`libusb`](https://packages.gentoo.org/useflags/libusb)           Use dev-libs/libusb detection to hotplug new smartcard readers. This flag should only be enabled if you\'re running a non-Linux kernel or you don\'t want to use udev.
  [`policykit`](https://packages.gentoo.org/useflags/policykit)     Uses sys-auth/polkit to restrict access to smartcard readers or smartcards to given users.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)         Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-15 08:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Update the system so the changes can take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

Install PCSC-Lite:

`root `[`#`]`emerge --ask --noreplace sys-apps/pcsc-lite`

### [Additional software]

Install one or more of the following driver packages:

-   [[[app-crypt/asedriveiiie-serial]](https://packages.gentoo.org/packages/app-crypt/asedriveiiie-serial)[]] - ASEDriveIIIe serial card reader
-   [[[app-crypt/asedriveiiie-usb]](https://packages.gentoo.org/packages/app-crypt/asedriveiiie-usb)[]] - ASEDriveIIIe USB card reader
-   [[[app-crypt/asekey]](https://packages.gentoo.org/packages/app-crypt/asekey)[]] - ASEKey USB SIM card reader
-   [[[app-crypt/ccid]](https://packages.gentoo.org/packages/app-crypt/ccid)[]] - compatible CCID card reader
-   [[[app-crypt/coolkey]](https://packages.gentoo.org/packages/app-crypt/coolkey)[]] - CoolKey and CAC card reader
-   [[[dev-libs/cyberjack]](https://packages.gentoo.org/packages/dev-libs/cyberjack)[]] - REINER SCT cyberJack pinpad/e-com card reader
-   [[[sys-apps/ifd-gempc]](https://packages.gentoo.org/packages/sys-apps/ifd-gempc)[]] - GemCore based card reader
-   [[[sys-apps/pcsc-slb-rf72-drv]](https://packages.gentoo.org/packages/sys-apps/pcsc-slb-rf72-drv)[]] - Schlumberger Reflex 72 serial card reader

## [Configuration]

USB card readers are detected automatically and work out of the box. For PC-Card and serial card readers, [/etc/reader.conf.d/reader.conf] will need to be adjusted. See [man reader.conf] for more information.

### [Service]

#### [SystemD]

`root `[`#`]`systemctl start pcscd.service`

To enable PCSC-Lite at boottime:

`root `[`#`]`systemctl enable pcscd.service`

#### [OpenRC]

With hotplug enabled, pcscd will start on plugging the card reader. It wil also start at boot time with the card reader already plugged.

    * Hotplug support is provided by udev rules.
    * When using OpenRC you additionally need to tell it to hotplug
    * pcscd by setting this variable in /etc/rc.conf:
    *
    *     rc_hotplug="pcscd"

With hotplug **not** enabled, pcscd needs to be started manually:

`root `[`#`]`rc-service pcscd start`

To start PCSC-Lite at boot time but without hotplug support, add it to the default runlevel:

`root `[`#`]`rc-update add pcscd default`

** Note**\
The PCSC-Lite daemon blocks all detected card readers for every other software.

## [Testing]

Start the daemon in debug mode manually:

OpenRC:

`root `[`#`]`/etc/init.d/pcscd stop`

System-d:

`root `[`#`]`systemctl stop cscd.service `

`root `[`#`]`systemctl stop cscd.socket `

then on both run:

`root `[`#`]`pcscd -a -d -f`

The daemon will now output all detected card readers. If a card reader is not detected, the correct driver may not have been installed. If there is a detected card reader, insert a smartcard. The daemon should inform about this event and among other things output the [ATR](https://en.wikipedia.org/wiki/Answer_to_reset "wikipedia:Answer to reset"), e.g.:

[CODE] **ATR**

    00000028 Card ATR: 3B 75 94 00 00 62 02 02 03 01

If everything works the daemon can be killed with [Ctrl]+[C].

## [See also]

-   [OpenCT](https://wiki.gentoo.org/wiki/OpenCT "OpenCT") --- a German standard for PC to smartcard reader communication, which is implemented by OpenCT.