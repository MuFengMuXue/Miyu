[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Dell_XPS_13_9343&action=edit).

**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/xps-13-9343-laptop/overview)

[[]][Specifications](https://dl.dell.com/manuals/all-products/esuprt_laptop/esuprt_xps_laptop/xps-13-9343-laptop_reference%20guide_en-us.pdf)

[[]][Hardware Maintenance Manual](https://dl.dell.com/manuals/all-products/esuprt_laptop/esuprt_xps_laptop/xps-13-9343-laptop_service%20manual_en-us.pdf)

** Note**\
This article is for the model of the Dell XPS 13 released in 2015. For the 2012 model, see [Dell XPS 13-L321X Ultrabook](https://wiki.gentoo.org/wiki/Dell_XPS_13-L321X_Ultrabook "Dell XPS 13-L321X Ultrabook"). For the 2016 model, see [Dell XPS 13 9360](https://wiki.gentoo.org/wiki/Dell_XPS_13_9360 "Dell XPS 13 9360").

** Important**\
Installing the [latest BIOS patch](https://www.dell.com/support/home/us/en/19/Drivers/DriversDetails?driverId=133FN) fixes many issues on this laptop. It is recommended that you do this before continuing.

** Important**\
\

-   Due to the lack of CD-ROM or DVD drive on this laptop, it is generally necessary to install Gentoo using a removable drive. However, at the time of this writing, Gentoo\'s official [LiveUSB](https://wiki.gentoo.org/wiki/LiveUSB "LiveUSB") lacks drivers needed to install using the instructions in the [Gentoo handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64"):
    -   USB 3 drivers - needed to boot to the live medium due to all ports being USB 3
    -   Proprietary Broadcom wireless drivers - needed to set up the network
-   **For these reasons, it is recommended to use a different installation medium.** Some possible alternatives include:
    -   [Arch Linux USB](https://wiki.archlinux.org/index.php/USB_flash_installation_media)
    -   [Kali Linux USB](https://docs.kali.org/downloading/kali-linux-live-usb-install)
    -   [SystemRescueCd USB](https://www.system-rescue.org/Installing-SystemRescue-on-a-USB-memory-stick/)
-   After successfully booting any of these mediums, you can pick the handbook back up at [Configuring the network](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Networking "Handbook:AMD64/Installation/Networking"). *Results may vary.*

## Contents

-   [[1] [Hardware specs]](#Hardware_specs)
-   [[2] [make.conf]](#make.conf)
-   [[3] [Hardware Config]](#Hardware_Config)
    -   [[3.1] [USB]](#USB)
    -   [[3.2] [Wireless]](#Wireless)
    -   [[3.3] [Bluetooth]](#Bluetooth)
    -   [[3.4] [ALSA sound]](#ALSA_sound)
    -   [[3.5] [Synaptics Touchpad]](#Synaptics_Touchpad)
    -   [[3.6] [MMC/SD Card Reader]](#MMC.2FSD_Card_Reader)
-   [[4] [Issues]](#Issues)
    -   [[4.1] [Loss of horizontal sync when switching TTYs]](#Loss_of_horizontal_sync_when_switching_TTYs)
    -   [[4.2] [GPU hang/freeze4 with external display]](#GPU_hang.2Ffreeze4_with_external_display)
    -   [[4.3] [Display Blanking randomly]](#Display_Blanking_randomly)
-   [[5] [See also]](#See_also)

## [Hardware specs]

All variants of this model come with 5th-gen Intel processors and have an option of a touchscreen with HD+ display.

-   [i3-5010U](https://ark.intel.com/products/84697/Intel-Core-i3-5010U-Processor-3M-Cache-2_10-GHz), [i5-5200U](https://ark.intel.com/products/85212/Intel-Core-i5-5200U-Processor-3M-Cache-up-to-2_70-GHz), [i7-5500U](https://ark.intel.com/products/85214/Intel-Core-i7-5500U-Processor-4M-Cache-up-to-3_00-GHz) or [i7-5600U](https://ark.intel.com/de/products/85215/Intel-Core-i7-5600U-Processor-4M-Cache-up-to-3_20-GHz) processor
-   13.3\" LCD screen (3200x1800 touchscreen display or 1920x1080without touchscreen)
-   Broadwell-U Integrated Graphics
-   4-8 GB DDR3 1600MHz RAM
-   128-512 GB Samsung SSD
-   2x USB 3 ports
-   mini-DisplayPort output
-   Broadcom DW1560 802.11a/b/g/n/ac + Bluetooth 4.0 *or* Intel Dual Band Wireless-AC 7265 802.11a/b/g/n/ac + Bluetooth 4.0

## [make.conf]

[FILE] **`/etc/portage/make.conf`**

    CFLAGS="-O2 -pipe -march=core-avx2 -mabm -madx -mavx256-split-unaligned-load -mavx256-split-unaligned-store -mprfchw -mrdseed"
    CXXFLAGS="$"
    MAKEOPTS="-j4"

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel i96

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptics

[FILE] **`/etc/portage/package.use/00cpu-flags`**

    */* CPU_FLAGS_X86: aes avx avx2 fma3 mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3

## [Hardware Config]

### [USB]

The two USB 3 ports require the xHCI driver to function with USB 3 devices and the EHCI driver to function with non-USB 3 devices. Any removable USB drive will also require USB Mass storage support.

[KERNEL] **USB configuration, 4.0.5-gentoo**

    Device Drivers  --->
        [*] USB Support  --->
            <M> Support for Host-side USB
                <M> xHCI HCD (USB 3.0) support
                <M> EHCI HCD (USB 2.0) support
                <M> USB Mass Storage support

### [Wireless]

** Note**\
*The Dell XPS 13 9343 does not come with a built-in NIC other than the Broadcom or Intel wireless adapter*

\

-   It may be impossible to fetch the distfiles needed by the **[[[net-wireless/broadcom-sta]](https://packages.gentoo.org/packages/net-wireless/broadcom-sta)[]]** package or **[[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]** (for the Intel Wireless variant) while the wireless is offline. It is recommended that you emerge the broadcom-sta or linux-firmware package during Gentoo\'s installation, after compiling the kernel, but before rebooting.

<!-- -->

-   If you end up running a kernel without wireless support and still need to download the distfiles, you can transfer the files using a removable drive and copy them to [/var/cache/distfiles]. To find the URLs for the needed files, run the following:

    :::: cmd-box


    `root `[`#`]`emerge --fetchonly --pretend net-wireless/broadcom-sta `


    ::::

The Broadcom BCM4352 wireless adapter requires the use of the official Broadcom driver. This driver is proprietary and requires that several kernel options be (un)set before installation:

[KERNEL] **Configuration for broadcom-sta, 4.0.5-gentoo**

    Processor type and features  --->
        Preemption Model  --->
            Voluntary Kernel Preemption (Desktop)
    [*] Networking support  --->
        [*] Wireless  --->
            <M> cfg80211 - wireless configuration API
            < > Generic IEEE 802.11 Networking Stack (mac80211)
    Device Drivers  --->
        [*] Network device support  --->
            [*] Wireless LAN  --->
                < > Broadcom 43xx wireless support (mac80211 stack)
                <M> IEEE 802.11 for Host AP (Prism2/2.5/3 and WEP/TKIP/CCMP)
        Sonics Silicon Backplane  --->
            < > Sonics Silicon Backplane support
        Broadcom Specific AMBA  --->
            < > BCMA support

After compiling the new kernel, emerge broadcom-sta:

`root `[`#`]`emerge --ask net-wireless/broadcom-sta`

Reboot to the new kernel and make sure the new Broadcom module is loaded

`root `[`#`]`modprobe wl`

If all goes well, you should have a working wireless interface

`root `[`#`]`iw list`

    Wiphy phy0
            max # scan SSIDs: 1
            max scan IEs length: 0 bytes
            Retry short limit: 7
            Retry long limit: 4
            Coverage class: 0 (up to 0m)
            Supported Ciphers:
                    * WEP40 (00-0f-ac:1)
                    * WEP104 (00-0f-ac:5)
                    * TKIP (00-0f-ac:2)
                    * CCMP (00-0f-ac:4)
                    * CMAC (00-0f-ac:6)
            Available Antennas: TX 0 RX 0
            Supported interface modes:
                     * IBSS
                     * managed

The configuration for the [Intel adapter](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") is similar, but no other package than linux-firmware needs to be installed:

[KERNEL] **Configuration for Intel, 4.2.0-gentoo-r1**

    [*] Networking support  --->
        [*] Wireless  --->
            <M> cfg80211 - wireless configuration API
            <M> Generic IEEE 802.11 Networking Stack (mac80211)
    Device Drivers  --->
        [*] Network device support  --->
            [*] Wireless LAN  --->
                <M> Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                < >   Intel Wireless WiFi DVM Firmware support
                <M>   Intel Wireless WiFi MVM Firmware support

### [Bluetooth]

Much like the Broadcom wireless chipset, the Broadcom BCM2045A0 Bluetooth chipset also requires proprietary firmware. If you are booting the kernel using [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub"), you will need to compile the kernel bluetooth options as modules:

[KERNEL] **Configuration for Intel, 4.5.3-gentoo**

    [*] Networking support  --->
        <M> Bluetooth subsystem support  --->
            <M> RFCOMM protocol support
            <M> BNEP protocol support
            <M> HIDP protocol support
                Bluetooth device drivers  --->
                      <M> HCI USB driver
                      [*] Broadcom protocol support
                      <M> HCI SDIO driver
                      <M> HCI UART driver
                      [*] Broadcom protocol support

If you compile the Bluetooth components into the kernel, the firmware is not available at the time the kernel loads, the firmware is not loaded and the Bluetooth system is not initialized. Compiling as a module ensures that the firmware is available at module autoload, and the system is initialized successfully. See [Broadcom Bluetooth](https://wiki.gentoo.org/wiki/Broadcom_Bluetooth "Broadcom Bluetooth") for additional info.

Remember to set the appropriate Bluetooth USE flags.

### [ALSA sound]

The built-in sound card has two different components: Standard audio output and audio output using the HDMI port. It is necessary to configure ALSA so that these are loaded in the proper order.

[KERNEL] **Intel HD Audio, 4.0.5-gentoo**

    Device Drivers  --->
        <M> Sound card support  --->
            <M> Advanced Linux Sound Architecture  --->
                HD-Audio  --->
                    <M> HD Audio PCI
                    (2048) Pre-allocated buffer size for HD-audio driver
                    [*] Support jack plugging notification via input layer
                    <M> Build Realtek HD-audio codec support
                    <M> Build Analog Device HD-audio codec support
                    <M> Build HDMI/DisplayPort HD-audio codec support

[FILE] **`/etc/modprobe.d/alsa.conf`**

    options snd cards_limit=2

    # These options force the audio-out port to be the primary card, and sound over the HDMI port to be secondary
    options snd-hda-intel id=PCH  index=0
    options snd-hda-intel id=HDMI index=1

    options snd-hda-intel model=dell-headset-multi

### [Synaptics Touchpad]

The touchpad runs off of an I2C bus and needs some special kernel drivers to be installed:

[KERNEL] **i2c touchpad, 4.0.5-gentoo**

    Device Drivers  --->
        Input device support  --->
            [*] Generic input layer (needed for keyboard, mouse, ...)
        I2C Support  --->
            <*> I2C Support
                [*] Autoselect pertinent helper modules
                I2C Hardware Bus Support  --->
                    <M> Synopsys DesignWare Platform
        HID Support  --->
            <M> HID bus support
                Special HID drivers  --->
                    <M> HID Multitouch panels
                I2C HID support  --->
                    <M> HID over I2C transport layer

### [][MMC/SD Card Reader]

The MMC/SD slot is located on the right side of the laptop, next to the right USB port. It is relatively easy to use with the proper kernel config.

[KERNEL] **Realtek PCI-E SD/MMC card interface, 4.0.5-gentoo**

    Device Drivers  --->
        <M> MMC/SD/SDIO card support  --->
            <M> MMC block device driver
                [*] Use bounce buffer for simple hosts
            <M> Realtek PCI-E SD/MMC Card Interface Driver
        <M> Sony MemoryStick card support  --->
            <M> MemoryStick Pro block device driver
            <M> MemoryStick Standard device driver
            <M> Realtek PCI-E Memstick Card Interface Driver

[KERNEL] **Realtek PCI-E SD/MMC card interface, 4.5.3-gentoo**

    Device Drivers  --->
        <M> MMC/SD/SDIO card support  --->
            <M> MMC block device driver
                [*] Use bounce buffer for simple hosts
        <M> Sony MemoryStick card support  --->
            <M> MemoryStick Pro block device driver
            <M> MemoryStick Standard device driver
            <M> Realtek PCI-E Memstick Card Interface Driver
            Multifunction device drivers  --->
                <M> Realtek PCI-E card reader

## [Issues]

### [Loss of horizontal sync when switching TTYs]

A bug is present in current kernel versions that results in horizontal sync loss on Broadwell machines when switching TTYs. [\[1\]](https://bugzilla.kernel.org/show_bug.cgi?id=95741) To fix it, you can add `i915.enable_ips=0` to your kernel command-line as a workaround.

### [][GPU hang/freeze4 with external display]

An issue appears present on QHD display models that may result in GPU hangs/freezing when manipulating the displays with xrandr on kernels 4.0 and up. Ensure i915.preliminary_hw_support=0 is set as this appears to alleviate this issue.

### [Display Blanking randomly]

This issue appears to be related to high resolutions on both the internal display as well as 4k external displays. Preliminary testing indicates that the i915.preliminary_hw_support=0 option being set significantly reduces or removes the issue.

## [See also]

-   [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") - For configuring the Intel integrated graphics card