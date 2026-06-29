**Resources**

[[]][Home](https://www.raspberrypi.com)

[[]][Official documentation](https://www.raspberrypi.com/documentation/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Raspberry_Pi "wikipedia:Raspberry Pi")

[[]][GitHub](https://github.com/raspberrypi/linux)

[[]][[#raspberrypi](ircs://irc.libera.chat/#raspberrypi)] ([[webchat](https://web.libera.chat/#raspberrypi)])

[[]][Blog](https://www.raspberrypi.com/news/)

The **Raspberry Pi** is a series of small single-board computers.

These machines are well supported by Gentoo. There are two main ways of installing Gentoo on them:

-   cross-compiling
-   using Raspberry Pi OS, or the gentoo \"Minimal Installation CD\", as a system to provide a chroot. - Note: This method is more complex and less supported.

\

## Contents

-   [[1] [Installation Instructions]](#Installation_Instructions)
-   [[2] [RPi usage guides]](#RPi_usage_guides)
-   [[3] [Old deprecated guides]](#Old_deprecated_guides)
    -   [[3.1] [32-bit]](#32-bit)
    -   [[3.2] [64-bit]](#64-bit)
-   [[4] [Hardware]](#Hardware)
    -   [[4.1] [WiFi 5Ghz DFS Channels]](#WiFi_5Ghz_DFS_Channels)
-   [[5] [See also]](#See_also)

## [Installation Instructions]

There is no Gentoo ARM(64) Handbook in general since the hardware and therefore the installation process differs much more than installation for e.g. x86 hardware.

The below guide is the recommended for both 32and 64bit Raspberry Pis:

-   [Raspberry Pi Install](https://wiki.gentoo.org/wiki/Raspberry_Pi_Install_Guide "Raspberry Pi Install Guide")

## [RPi usage guides]

A collection of guides of interesting projects to run on a Raspberry Pi:

-   [Pi router](https://wiki.gentoo.org/wiki/Pi_Router "Pi Router")
-   [NTP server](https://wiki.gentoo.org/wiki/Raspberry_Pi_Stratum_1_Time_Server "Raspberry Pi Stratum 1 Time Server")

## [Old deprecated guides]

** Important**\
Users looking for a certain usage case might find the follow archived guides useful for reference, however do note these are likely very out of date:

### [32-bit]

-   [Installation](https://wiki.gentoo.org/wiki/Raspberry_Pi/Installation "Raspberry Pi/Installation") (previously on this page)
-   [Quick Install Guide](https://wiki.gentoo.org/wiki/Raspberry_Pi/Quick_Install_Guide "Raspberry Pi/Quick Install Guide")
-   [Minimal musl and busybox cross building](https://wiki.gentoo.org/wiki/Raspberry_Pi/Minimal_musl%2Bbusybox_cross_building "Raspberry Pi/Minimal musl+busybox cross building")
-   [Cross building](https://wiki.gentoo.org/wiki/Raspberry_Pi/Cross_building "Raspberry Pi/Cross building")

### [64-bit]

-   [Pi 3 64 bit install](https://wiki.gentoo.org/wiki/Raspberry_Pi_3_64_bit_Install "Raspberry Pi 3 64 bit Install")
-   [Pi 4 64 bit install](https://wiki.gentoo.org/wiki/Raspberry_Pi4_64_Bit_Install "Raspberry Pi4 64 Bit Install")
-   [In place installation](https://wiki.gentoo.org/wiki/Raspberry_Pi/ARM64_in_place_installation "Raspberry Pi/ARM64 in place installation") (this will largely work for 32-bit too)

## [Hardware]

  -------------------------------- --------- -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Model                            CPU       Architecture   Stage3
  Raspberry PI Zero                BCM2708   ARM            [ARMv6j stage 3](//gentoo.org/downloads/#arm)
  Raspberry PI (Original)          BCM2708   ARM            [ARMv6j stage 3](//gentoo.org/downloads/#arm)
  Raspberry PI Zero w              BCM2708   ARM            [ARMv6j stage 3](//gentoo.org/downloads/#arm)
  Raspberry PI 2b Before Ver 1.2   BCM2709   ARM            [ARMv7a stage 3](//gentoo.org/downloads/#arm)
  Raspberry PI 2b Ver 1.2          BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 3b                  BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 3b+                 BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI Zero 2              BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI Zero 2 w            BCM2710   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 4b                  BCM2711   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI CM4                 BCM2711   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 5                   BCM2712   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI CM5                 BCM2712   ARM/ARM64      [ARMv7a stage 3](//gentoo.org/downloads/#arm) or [arm64 stage3](//gentoo.org/downloads/#arm64)
  Raspberry PI 6                   TBD       TBD
  -------------------------------- --------- -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------

There are some ARM SoCs that support 64-bit but no 32-bit. Those weren\'t used in the Pis.

### [WiFi 5Ghz DFS Channels]

On the Raspberry Pi you may have issues being able to see your WiFi 5Ghz networks. You should be able to advise the chip which region you are in and be able to enable the DFS channels, but that does not seem to work. It is unknown if this is a hardware or driver issue at this time. The workaround for this issue is to set your access point/router to not use the DFS channels and then you should be able to see your networks in the list. This only applies to the Raspberry Pi systems that have a WiFi 5Ghz capable chip, PI3 and above.

An [extensive table of Pi hardware](https://en.wikipedia.org/wiki/Raspberry_Pi#Specifications "wikipedia:Raspberry Pi") is available in the English Wikipedia.

## [See also]

-   [Project:ARM](https://wiki.gentoo.org/wiki/Project:ARM "Project:ARM")
-   [Project:ARM64](https://wiki.gentoo.org/wiki/Project:ARM64 "Project:ARM64")