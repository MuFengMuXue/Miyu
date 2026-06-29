[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=ASUS_Eee_PC_1201PN&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

## Contents

-   [[1] [Hardware Status]](#Hardware_Status)
-   [[2] [Hardware]](#Hardware)
-   [[3] [CPU]](#CPU)
-   [[4] [Video]](#Video)
    -   [[4.1] [Kernel]](#Kernel)
    -   [[4.2] [Install driver]](#Install_driver)
    -   [[4.3] [Xorg]](#Xorg)
-   [[5] [Sound]](#Sound)
-   [[6] [Ethernet]](#Ethernet)
-   [[7] [Wireless]](#Wireless)
-   [[8] [Bluetooth]](#Bluetooth)
-   [[9] [Fn Keys]](#Fn_Keys)
-   [[10] [Camera]](#Camera)
-   [[11] [Sleep]](#Sleep)

## [Hardware Status]

  ------------------------- ------- -------
  Device                    Works   Notes
  Intel Atom N450           Yes
  Nvidia ION                Yes
  Intel HDA                 Yes
  Ethernet Atheros AR8132   Yes
  Wireless Atheros AR9285   Yes
  Bluetooth                 Yes
  Camera                    Yes
  Card Reader               Yes
  ------------------------- ------- -------

## [Hardware]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Intel Corporation N10 Family DMI Bridge [8086:a010]
    00:1b.0 Audio device [0403]: Intel Corporation N10/ICH 7 Family High Definition Audio Controller [8086:27d8] (rev 02)
    00:1c.0 PCI bridge [0604]: Intel Corporation N10/ICH 7 Family PCI Express Port 1 [8086:27d0] (rev 02)
    00:1c.1 PCI bridge [0604]: Intel Corporation N10/ICH 7 Family PCI Express Port 2 [8086:27d2] (rev 02)
    00:1c.3 PCI bridge [0604]: Intel Corporation N10/ICH 7 Family PCI Express Port 4 [8086:27d6] (rev 02)
    00:1d.0 USB controller [0c03]: Intel Corporation N10/ICH 7 Family USB UHCI Controller #1 [8086:27c8] (rev 02)
    00:1d.1 USB controller [0c03]: Intel Corporation N10/ICH 7 Family USB UHCI Controller #2 [8086:27c9] (rev 02)
    00:1d.2 USB controller [0c03]: Intel Corporation N10/ICH 7 Family USB UHCI Controller #3 [8086:27ca] (rev 02)
    00:1d.3 USB controller [0c03]: Intel Corporation N10/ICH 7 Family USB UHCI Controller #4 [8086:27cb] (rev 02)
    00:1d.7 USB controller [0c03]: Intel Corporation N10/ICH 7 Family USB2 EHCI Controller [8086:27cc] (rev 02)
    00:1e.0 PCI bridge [0604]: Intel Corporation 82801 Mobile PCI Bridge [8086:2448] (rev e2)
    00:1f.0 ISA bridge [0601]: Intel Corporation NM10 Family LPC Controller [8086:27bc] (rev 02)
    00:1f.2 SATA controller [0106]: Intel Corporation N10/ICH7 Family SATA Controller [AHCI mode] [8086:27c1] (rev 02)
    01:00.0 Ethernet controller [0200]: Atheros Communications Inc. AR8132 Fast Ethernet [1969:1062] (rev c0)
    02:00.0 Network controller [0280]: Atheros Communications Inc. AR9285 Wireless Network Adapter (PCI-Express) [168c:002b] (rev 01)
    04:00.0 VGA compatible controller [0300]: NVIDIA Corporation Device [10de:0a76] (rev a2)
    04:00.1 Audio device [0403]: NVIDIA Corporation High Definition Audio Controller [10de:0be3] (rev a1)

`user `[`$`]`lsusb`

    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 001 Device 002: ID 13d3:5111 IMC Networks Integrated Webcam
    Bus 004 Device 002: ID 0b05:1789 ASUSTek Computer, Inc.

## [CPU]

[FILE] **`/etc/portage/make.conf`**

    CHOST="i686-pc-linux-gnu"
    CFLAGS="-march=atom -O2 -fomit-frame-pointer -pipe -mfpmath=sse"
    CXXFLAGS="$"

## [Video]

### [Kernel]

[KERNEL] **nVidia**

    General setup --->
     [*] System V IPC
    Loadable Module Support --->
     [*] Enable Loadable Module Support
    Processor Type and Features --->
     [*] MTRR (Memory Type Range Register) Support

    Device Drivers --->
     Graphics support --->
      [*] /dev/agpgart (AGP Support)

    Device Drivers --->
     Graphics Support --->
       Support for frame buffer devices --->
      < >   nVidia Framebuffer Support
      < >   nVidia Riva support

### [Install driver]

`root `[`#`]`emerge --ask x11-drivers/nvidia-drivers`

### [Xorg]

[FILE] **`/etc/X11/xorg.conf`**

    Section "Files"
     ModulePath   "/usr/lib/xorg/modules"
     FontPath     "/usr/share/fonts/misc/"
     FontPath     "/usr/share/fonts/TTF/"
     FontPath     "/usr/share/fonts/OTF/"
     FontPath     "/usr/share/fonts/Type1/"
     FontPath     "/usr/share/fonts/100dpi/"
     FontPath     "/usr/share/fonts/75dpi/"
    EndSection

    Section "Module"
     Load    "record"
     Load    "glx"
     Load    "dbe"
     Load    "extmod"
    EndSection

    Section "Monitor"
     Identifier "Monitor0"
     ModelName  "Asus 1201NL"
     Option "DPI" "96x96"
    EndSection

    Section "Device"
     Identifier "Card0"
     Driver     "nvidia"
     BusID      "PCI:2:0:0"
     Option     "NoLogo"                "True"
     Option     "AllowGLXwithComposite" "True"
     Option     "TripleBuffer"          "True"
     Option     "AddARGBGLXVisuals"     "True"
    EndSection

    Section "Screen"
     Identifier "Screen0"
     Device     "Card0"
     Monitor    "Monitor0"
     SubSection "Display"
      Viewport   0 0
      Depth     24
     EndSubSection
    EndSection

    Section "ServerFlags"
        Option      "AllowEmptyInput" "on"
        Option      "AutoAddDevices" "on"
        Option      "AutoEnableDevices" "on"
    EndSection

    Section "ServerLayout"
        Identifier  "Asus 1201NL"
        Screen 0    "Screen0" 0 0
    EndSection

## [Sound]

[KERNEL] **Intel HDA**

    Device Drivers  --->
       Sound --->
       <*> Sound card support
       <*>   Advanced Linux Sound Architecture --->
       [*]     PCI devices --->
       <*>       Inetl HD Audio --->
       [*]         Build Realtek HD-audio codec support
       [*]         Build NVIDIA HDMI HD-audio codec support

## [Ethernet]

[KERNEL] **AR8132**

      Device Drivers --->
         [*] Network device support --->
         [*]   Ethernet (1000 Mbit) --->
         <*>     Atheros L1C Gigabite Ethernet support

** Note**\
To avoid system hang at high Ethernet activity, set `MTU=750`

## [Wireless]

[KERNEL] **AR9285**

    [*] Networking support --->
         <*>   Wireless --->
         <*>    cfg80211 - wireless configuration API
         <*>    Generic IEEE 802.11 Networking Stack (mac80211)

    Device Drivers --->
         [*]   Network device support --->
         [*]    Wireless LAN --->
         <*>     Atheros Wireless Cards --->
         <*>      Atheros 802.11n wireless cards support

## [Bluetooth]

[KERNEL] **Bluetooth**

    [*] Networking support --->
         <*>   Bluetooth subsystem support --->
         <*>     L2CAP protocol support
         <*>     SCO links support
         <*>     RFCOMM protocol support
         [*]       RFCOMM tty support
         <*>     BNEP protocol support
         [*]       Multicast filter support
         [*]       Protocol filter support
         <*>     HIDP protocol support
                 Bluetooth device drivers --->
         <*>       HCI USB driver

## [Fn Keys]

[KERNEL]

    Bus options (PCI etc.)  --->
        <*> Support for PCI Hotplug  --->
    Device Drivers  --->
        [*] X86 Platform Specific Device Drivers  --->
            <*> ASUS WMI Driver
            <*>    Eee PC WMI Driver
            <*> WMI

## [Camera]

[KERNEL]

    Device Drivers --->
         Multimedia devices --->
         [*]   Video capture adapters --->
         [*]     V4L USB device --->
         <*>       USB Video Class (UVC)
         [*]         UVC input events device support

`user `[`$`]`dmesg | grep EasyCamera`

    uvcvideo: Found UVC 1.00 device USB2.0 UVC VGA WebCam (13d3:5111)

**Test Camera**

`user `[`$`]`mplayer -tv driver=v4l2:device=/dev/video0 tv://`

** Note**\
Need mplayer build with `v4l2` USE flag

**Bug** On new kernel (3.3.8) camera hangs the system, to avoid this, build driver as module.

[KERNEL]

         Multimedia devices --->
         <M>       USB Video Class (UVC)
         [*]         UVC input events device support

And put below options to the module.

`root `[`#`]`echo "options uvcvideo nodrop=1" > /etc/modprobe.d/uvcvideo.conf`

## [Sleep]

If after Fn-F2 laptop goes to suspend and wakes up immediately, run as root code below and try again.

`root `[`#`]`echo US15 > /proc/acpi/wakeup`

If the problem was fixed, add this code to autostart. For example:

`root `[`#`]`echo "echo US15 > /proc/acpi/wakeup" > /etc/local.d/suspend_fix.start `

`root `[`#`]`chmod +x /etc/local.d/suspend_fix.start`

** Note**\
Tested on gentoo-sources-3.3.8