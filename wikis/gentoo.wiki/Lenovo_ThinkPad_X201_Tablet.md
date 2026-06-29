**Resources**

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/withdrawnbook/ltwbook_2013.pdf#%5B%7B%22num%22%3A69709%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22Fit%22%7D%5D)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/ibmdl/pub/pc/pccbbs/mobiles_pdf/45n3683_04.pdf)

[[]][ThinkPad X series](https://en.wikipedia.org/wiki/ThinkPad_X_series "wikipedia:ThinkPad X series")

This article was written using 0831CTO model of the Lenovo ThinkPad X201 Tablet.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [package.use]](#package.use)
        -   [[2.1.1] [X200 Tablet]](#X200_Tablet)
        -   [[2.1.2] [X201 Tablet]](#X201_Tablet)
    -   [[2.2] [Firmware]](#Firmware)
    -   [[2.3] [Kernel]](#Kernel)
    -   [[2.4] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Screen Buttons]](#Screen_Buttons)
    -   [[3.2] [Finger/Pen Input]](#Finger.2FPen_Input)
        -   [[3.2.1] [Attach Serial Interface]](#Attach_Serial_Interface)
        -   [[3.2.2] [X11]](#X11)
-   [[4] [External resources]](#External_resources)

## [Hardware]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation Core Processor DRAM Controller [8086:0044] (rev 02)
    00:02.0 VGA compatible controller [0300]: Intel Corporation Core Processor Integrated Graphics Controller [8086:0046] (rev 02)
    00:16.0 Communication controller [0780]: Intel Corporation 5 Series/3400 Series Chipset HECI Controller [8086:3b64] (rev 06)
    00:19.0 Ethernet controller [0200]: Intel Corporation 82577LM Gigabit Network Connection [8086:10ea] (rev 06)
    00:1a.0 USB controller [0c03]: Intel Corporation 5 Series/3400 Series Chipset USB2 Enhanced Host Controller [8086:3b3c] (rev 06)
    00:1b.0 Audio device [0403]: Intel Corporation 5 Series/3400 Series Chipset High Definition Audio [8086:3b56] (rev 06)
    00:1c.0 PCI bridge [0604]: Intel Corporation 5 Series/3400 Series Chipset PCI Express Root Port 1 [8086:3b42] (rev 06)
    00:1c.3 PCI bridge [0604]: Intel Corporation 5 Series/3400 Series Chipset PCI Express Root Port 4 [8086:3b48] (rev 06)
    00:1c.4 PCI bridge [0604]: Intel Corporation 5 Series/3400 Series Chipset PCI Express Root Port 5 [8086:3b4a] (rev 06)
    00:1d.0 USB controller [0c03]: Intel Corporation 5 Series/3400 Series Chipset USB2 Enhanced Host Controller [8086:3b34] (rev 06)
    00:1e.0 PCI bridge [0604]: Intel Corporation 82801 Mobile PCI Bridge [8086:2448] (rev a6)
    00:1f.0 ISA bridge [0601]: Intel Corporation QM57 Chipset LPC Interface Controller [8086:3b07] (rev 06)
    00:1f.2 SATA controller [0106]: Intel Corporation 5 Series/3400 Series Chipset 6 port SATA AHCI Controller [8086:3b2f] (rev 06)
    00:1f.3 SMBus [0c05]: Intel Corporation 5 Series/3400 Series Chipset SMBus Controller [8086:3b30] (rev 06)
    00:1f.6 Signal processing controller [1180]: Intel Corporation 5 Series/3400 Series Chipset Thermal Subsystem [8086:3b32] (rev 06)
    02:00.0 Network controller [0280]: Intel Corporation Centrino Advanced-N 6200 [8086:4239] (rev 35)
    ff:00.0 Host bridge [0600]: Intel Corporation Core Processor QuickPath Architecture Generic Non-core Registers [8086:2c62] (rev 02)
    ff:00.1 Host bridge [0600]: Intel Corporation Core Processor QuickPath Architecture System Address Decoder [8086:2d01] (rev 02)
    ff:02.0 Host bridge [0600]: Intel Corporation Core Processor QPI Link 0 [8086:2d10] (rev 02)
    ff:02.1 Host bridge [0600]: Intel Corporation 1st Generation Core i3/5/7 Processor QPI Physical 0 [8086:2d11] (rev 02)
    ff:02.2 Host bridge [0600]: Intel Corporation 1st Generation Core i3/5/7 Processor Reserved [8086:2d12] (rev 02)
    ff:02.3 Host bridge [0600]: Intel Corporation 1st Generation Core i3/5/7 Processor Reserved [8086:2d13] (rev 02)

`root `[`#`]`lsusb`

    Bus 002 Device 005: ID 05c6:9204 Qualcomm, Inc.
    Bus 002 Device 003: ID 0bda:0159 Realtek Semiconductor Corp. RTS5159 Card Reader Controller
    Bus 002 Device 002: ID 8087:0020 Intel Corp. Integrated Rate Matching Hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 007: ID 17ef:4816 Lenovo Integrated Webcam
    Bus 001 Device 008: ID 17ef:1005 Lenovo
    Bus 001 Device 005: ID 147e:2016 Upek Biometric Touchchip/Touchstrip Fingerprint Sensor
    Bus 001 Device 004: ID 0a5c:217f Broadcom Corp. BCM2045B (BDC-2.1)
    Bus 001 Device 002: ID 8087:0020 Intel Corp. Integrated Rate Matching Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [Standard]

  ----------------------------- -------------------------------------------------------- ------------- ----------- ------------------ ---------------- -------
  Device                        Make/model                                               Status        Bus ID      Kernel driver(s)   Kernel version   Notes
  Wireless network controller   Intel Corporation Centrino Advanced-N 6200 (rev 35)      Works         8086:4239   iwlwifi            4.9.16-gentoo    ---
  Bluetooth                     Broadcom Corp. BCM2045B (BDC-2.1)                        Works         0a5c:217f   bcm203x            4.9.16-gentoo    ---
  Touchscreen                   Wacom Serial Penabled 2FG Touchscreen                    Works         ---         wacom_w8001        4.9.16-gentoo    ---
  Fingerprint reader            Upek Biometric Touchchip/Touchstrip Fingerprint Sensor   Works         147e:2016   ---                4.9.16-gentoo    ---
  WWAN & GPS                    Qualcomm Gobi 2000                                       Not tested    \-          \-                 \-               \-
  ----------------------------- -------------------------------------------------------- ------------- ----------- ------------------ ---------------- -------

### [Accessories]

(Optional section. Describe any accessories that may be possible in this section. Anything from external plug-and-play LCD screens to computer docks.)

  -------- ------------------------- ------------- -------- ------------------ ---------------- -------
  Device   Make/model                Status        Bus ID   Kernel driver(s)   Kernel version   Notes
  Dock     ThinkPad X200 Ultrabase   Not tested    \-       \-                 \-               \-
  -------- ------------------------- ------------- -------- ------------------ ---------------- -------

## [Installation]

(Write the necessary steps to get Gentoo onto this system. Try to document any special step that each user will need to reproduce on their system. Includes getting special drivers or firmware from a manufacturer website, etc.)

### [package.use]

[FILE] **`/etc/portage/package.use/00grub`**

    */* GRUB_PLATFORMS: pc

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput wacom

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* i965 intel

#### [X200 Tablet]

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: mmx mmxext sse sse2 sse3 sse4_1 ssse3

#### [X201 Tablet]

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

### [Firmware]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **ACPI**

    Generic Driver Options  --->
       [*] X86 Platform Specific Device Drivers  --->
          <*>   ThinkPad ACPI Laptop Extras
          [*]     Console audio control ALSA interface
          [ ]     Maintainer debug facilities
          [ ]     Verbose debug mode
          [ ]     Allow control of important LEDs (unsafe)
          [*]     Video output control support
          [*]     Support NVRAM polling for hot keys

[KERNEL] **Ethernet controller**

    Generic Driver Options  --->
       [*] Network device support  ---
          [*]   Ethernet driver support  --->
             [*]   Intel devices
             <*>     Intel(R) PRO/1000 PCI-Express Gigabit Ethernet support

\
Building the following device driver as module may be appropriate as it requires firmware during initialization.

[KERNEL] **Wireless network controller**

    Generic Driver Options  --->
       [*] Network device support  ---
          [*]   Wireless LAN  --->
             [*]   Intel devices
             <M>     Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
             <M>       Intel Wireless WiFi DVM Firmware support

[KERNEL] **Audio device**

    Generic Driver Options  --->
       <*> Sound card support  --->
          <*>   Advanced Linux Sound Architecture  --->
             [*]   PCI sound devices  --->
                   HD-Audio  --->
                      <*> HD Audio PCI
                      <*> Build Conexant HD-audio codec support

[KERNEL] **Bluetooth**

    -*- Networking support  --->
       <*>   Bluetooth subsystem support  --->
                Bluetooth device drivers  --->
                   <*> HCI USB driver
                   [*]   Broadcom protocol support
                   <*> HCI BCM203x USB driver

[KERNEL] **Touchscreen**

    Generic Driver Options  --->
       -*- Generic input layer (needed for keyboard, mouse, ...)
          [*]   Touchscreens  --->
             <*>   Wacom W8001 penabled serial touchscreen

[KERNEL] **Card reader**

    Generic Driver Options  --->
       [*] USB support  --->
          <*>   Support for Host-side USB
          <*>     USB Mass Storage support
          <*>       Realtek Card Reader support
          [*]         Realtek Card Reader autosuspend support

### [Emerge]

Touchscreen requires [inputtattach](#Finger.2FPen_Input) program from the following package.

`root `[`#`]`emerge --ask games-util/joystick`

Fingerprint reader is recognized by the following library.

`root `[`#`]`emerge --ask sys-auth/libfprint`

## [Configuration]

### [Screen Buttons]

Both the ThinkPad X200T and X201T have 4 buttons underneath their swivel screen intended to be used when the device is in tablet mode. These buttons send events to the laptop keyboard and work out of the box; however, libinput will disable the laptop keyboard (and therefore the front buttons) when it detects the device switching to tablet mode. It does this to prevent accidental input on other 2-in-1 laptops (like the ThinkPad Yoga) that have their keyboards exposed while in tablet mode.

To reverse this behaviour for our X200T or X201T and keep the front buttons enabled in tablet mode, a libinput quirk needs to be added.

[FILE] **`/usr/share/libinput/50-system-x200.quirks`**

    # The Lenovo X200 Tablet (and X201 Tablet) are 360 convertible laptops
    # that have 4 physical buttons below the screen.
    # These buttons are mapped to the same device as the laptop keyboard.
    # The keyboard is physically impossible to accidentally touch in tablet mode.
    # When these devices are in tablet mode, the keyboard should remain enabled
    # so that the front buttons continue to work.
    [Lenovo X200T]
    MatchName=AT Translated Set 2 keyboard
    MatchDMIModalias="dmi:*:svnLenovo:fnThinkPadX20?T:*"
    ModelTabletModeNoSuspend=1

### [][Finger/Pen Input]

#### [Attach Serial Interface]

For models with pen and touch support, the following command must be running for touchscreen inputs to work.

`root `[`#`]`inputattach -w8001 /dev/ttyS0`

For models with pen only support, the baud rate of 19200 must be specified. The command is otherwise the same.

`root `[`#`]`inputattach -w8001 --baud 19200 /dev/ttyS0`

#### [X11]

For [X11](https://wiki.gentoo.org/wiki/X11 "X11") to work with finger/pen input, pull in [[[x11-drivers/xf86-input-wacom]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-wacom)[]] by inserting `wacom` argument into the indicated variable in the file shown below and run the following command for the configuration to emerge.

[FILE] **`/etc/portage/package.use`**

    INPUT_DEVICES="... wacom"

`root `[`#`]`emerge --ask --deep --newuse @world`

## [External resources]

-   [http://www.thinkwiki.org/wiki/Category:X201_Tablet](http://www.thinkwiki.org/wiki/Category:X201_Tablet)
-   [https://wiki.archlinux.org/title/Lenovo_ThinkPad_X201_Tablet](https://wiki.archlinux.org/title/Lenovo_ThinkPad_X201_Tablet)