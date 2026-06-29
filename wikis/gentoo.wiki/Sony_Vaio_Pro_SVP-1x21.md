\
How to setup Gentoo Linux on the Sony Vaio Pro Haswell based ultrabooks.

## Contents

-   [[1] [Preparation]](#Preparation)
-   [[2] [Kernel configuration]](#Kernel_configuration)
    -   [[2.1] [CPU]](#CPU)
    -   [[2.2] [SATA]](#SATA)
    -   [[2.3] [Network]](#Network)
    -   [[2.4] [I2C support]](#I2C_support)
    -   [[2.5] [Webcam]](#Webcam)
    -   [[2.6] [Graphics]](#Graphics)
    -   [[2.7] [Sound]](#Sound)
    -   [[2.8] [SD card reader]](#SD_card_reader)

## [Preparation]

It\'s recommended you back up your disk so that you can keep the windows recovery partition in-case you ever need it.

Since most live usb sticks do not support the WiFi card (Intel(R) Dual Band Wireless N 7260) of these laptops, you will likely be without Internet while setting up the laptop until you can compile a kernel which contains the support (3.11.x or newer). The easiest way to bootstrap the laptop into a WiFi capable kernel is to use USB tethering with an internet capable phone. Alternatively if you do not own a tethering capable phone, you can download the following (or newer) packages from a [Gentoo Mirror](http://www.gentoo.org/main/en/mirrors2.xml). Or, if you have a working Gentoo machine already, simply copying them from that machine\'s [/usr/portage/distfiles]. Be sure also to get the latest firmware for the Intel 7260 WiFi card [\[1\]](http://intellinuxwireless.org).

`root `[`#`]` cd /usr/portage/distfiles `

`root `[`#`]` cp autogen* bc* busybox* cpio* dmraid* efibootmgr* fuse* gcc-*-specs* gcc-*-patches* gcc-*-piepatches* gcc-* gcc-*-uclibc-patches* genkernel* genpatches-*.base* genpatches-*.extras* gnupg* grub* guile* hwids* libnl* linux* LVM2* mdadm* open-iscsi* pciutils* unifont* unionfs-fuse* wireless_tools* wpa_supplicant* /mnt/usbkey `

These are all the source packages required to install efibootmgr, gentoo-sources, grub, wireless-tools, and wpa_supplicant. With all this in hand you should be able to install Gentoo, build the newest kernel with support for the Intel 7260, and all the wireless tools necessary to connect to a wireless access point.

You will also need an appropriate stage3 tarball and the portage-latest tarball, so get those from your favourite mirror: [Gentoo Mirrors](http://www.gentoo.org/main/en/mirrors2.xml).

Another alternative is preparing your own live usb stick that has the necessary support for the Intel 7260.

## [Kernel configuration]

It\'s highly recommended you start from a kernel seed from [Pappy\'s Kernel Seeds](http://kernel-seeds.org/). Follow the guide for [Working with Kernel Seeds](http://kernel-seeds.org/working.html). The guide will take you through all the important steps of preparing your kernel. In the following sections, recommended configurations for **most** the Vaio Pro\'s hardware are included, as well as tips for getting some things working correctly. For those remaining pieces of hardware not listed, just follow the Working with Kernel Seeds guide.

### [CPU]

[KERNEL]

    Processor type and features --->
      Processor family (Core 2/newer Xeon)  --->
      [ ] IBM Calgary IOMMU support
      [ ] Enable Maximum number of SMP Processors and NUMA Nodes
      (8) Maximum number of CPUs

### [SATA]

Works with the generic ahci driver.

[KERNEL]

    Device Drivers --->
    <*> Serial ATA and Parallel ATA Drivers --->
    <*>  AHCI SATA Support

### [Network]

Be sure to place the appropriate firmware retrieved from [\[2\]](http://intellinuxwireless.org) in [/lib/firmware] or create an ebuild to do so.

[KERNEL]

    Networking Support --->
    -*- Wireless --->
    <M>   cfg80211 - wireless configuration API
    [*]     enable powersave by default
    [*]     cfg80211 DebugFS entries
    [*]     cfg80211 wireless extensions compatibility
    <M>   Generic IEEE 802.11 Networking Stack (mac80211)
          Default rate control algorithm (Minstrel)  --->
    -*-   Enable LED triggers
    [*]   Export mac80211 internals in DebugFS

[KERNEL]

    Device Drivers  --->
    [*] Network device support  --->
    [*]  Wireless LAN  --->
    <M>  Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
    < >     Intel Wireless WiFi DVM Firmware support
    <M>     Intel Wireless WiFi MVM Firmware support

### [I2C support]

[KERNEL]

    Device Drivers --->
     I2C Support --->
    I2C Hardware Bus support --->
    <M> Intel 82801 (ICH/PCH)

### [Webcam]

[KERNEL]

    Device Drivers --->
    <M> Multimedia support --->
    [*]   Cameras/video grabbers support
    [*]   Media USB Adapters  --->
    <M>   USB Video Class (UVC)
    [*]     UVC input events device support

### [Graphics]

[KERNEL]

    Device Drivers --->
    Graphics support --->
    <M> /dev/agpgart (AGP Support)  --->
    <M>   Intel 440LX/BX/GX, I8xx and E7x05 chipset support
    -*- VGA Arbitration
    (2)   Maximum number of GPUs
    <M> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)  --->
    <M> Intel 8xx/9xx/G3x/G4x/HD Graphics
    [*]   Enable modesetting on intel by default

### [Sound]

Using ALSA alone doesn\'t produce very good sound. It\'s recommended that you use [PulseAudio](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") with this laptop. Using plain alsa produces with this laptop produces poor sound quality at this time.

[KERNEL]

    Device Drivers --->
    <M> Sound card support --->
    <M>   Advanced Linux Sound Architecture --->
    [*]   Dynamic device file minor numbers
    [*]   Support old ALSA API
    [*]   Verbose procfs contents
    [ ]   Verbose printk
    [ ]     Enable PCM ring buffer overrun/underrun debugging
    [*]   PCI sound devices  --->
    <M>   Intel HD Audio  --->
    (4096) Pre-allocated buffer size for HD-audio driver
    [*]   Support initialization patch loading for HD-audio
    [*]   Build Realtek HD-audio codec support
    [*]   Build Analog Device HD-audio codec support
    [*]   Build HDMI/DisplayPort HD-audio codec support
    [*]   Build Display HD-audio controller/codec power well support for i915 cards
    (0)   Default time-out for HD-audio power-save mode

### [SD card reader]

Since kernel version 3.11.0, the SD card reader in the Sony Vaio Pro 13 (Realtek Semiconductor Co., Ltd. RTS5209 PCI Express Card Reader) does not work unless an SD card is inserted before booting. This unfortunately renders the SD Card reader mostly useless. Other than this major bug, the card reader works fine with the following config, and with the use of the rts_pstor package.

`root `[`#`]`emerge --ask rts_pstor`

[KERNEL]

    Device Drivers  --->
    <M> MMC/SD/SDIO card support  --->
    [*]   MMC debugging
    <M>   MMC block device driver
    (8)     Number of minors per block device
    [*]     Use bounce buffer for simple hosts
    <M>   Secure Digital Host Controller Interface support
    <M>   SDHCI support on PCI bus