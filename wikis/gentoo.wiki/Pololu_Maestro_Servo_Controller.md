**Resources**

[[]][Home](https://www.pololu.com/docs/0J40)

This document describes how to install Pololu Maestro Servo Controller board software on Gentoo.

## Contents

-   [[1] [Install needed packages]](#Install_needed_packages)
-   [[2] [Download software]](#Download_software)
-   [[3] [Troubleshooting]](#Troubleshooting)
-   [[4] [External resources]](#External_resources)

## [Install needed packages]

Install [[[dev-lang/mono]](https://packages.gentoo.org/packages/dev-lang/mono)[]] and [[[dev-libs/libusb]](https://packages.gentoo.org/packages/dev-libs/libusb)[]]:

`root `[`#`]`emerge dev-lang/mono dev-libs/libusb`

## [Download software]

Download Maestro Control Center [\[1\]](http://www.pololu.com/file/download/maestro-linux-100507.tar.gz?file_id=0J315) and USB Software Development Kit [\[2\]](https://www.pololu.com/file/download/pololu-usb-sdk-140604.zip?file_id=0J765).

It is necessary to run MaestroControlCenter and UscCmd programs with \"mono\"

`user `[`$`]`mono MaestroControlCenter`

`user `[`$`]`mono UscCmd`

Read README.txt files there for more information how to use and compile software.

## [Troubleshooting]

Create link to libusb-1.0.so.0.1.0 if Maestro Control Center or other program got error \"Library not found: libusb-1.0\"

`root `[`#`]`cd /lib`

`root `[`#`]`ln -s libusb-1.0.so.0.1.0 libusb-1.0.so`

Edit Makefile if USB Software Development Kit couldn\'t build with error \"make: gmcs: Command not found\".

[FILE] **`Makefile`USB Software Development Kit**

    Change line:
    CSC:=gmcs
    to
    CSC:=mcs

## [External resources]

-   [Maestro Control Center](https://www.pololu.com/docs/0J40/3.b)
-   [USB Software Development Kit](https://www.pololu.com/docs/0J41)