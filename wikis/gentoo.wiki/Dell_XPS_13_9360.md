**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/xps-13-9360-laptop/overview)

[[]][Specifications](https://dl.dell.com/topicspdf/xps-13-9360-laptop_setup-guide_en-us.pdf)

[[]][Hardware Maintenance Manual](https://dl.dell.com/topicspdf/xps-13-9360-laptop_service-manual_en-us.pdf)

** Note**\
This article is for the new model of the Dell XPS 13 released late 2016. For the older model released in 2015, see [Dell XPS 13 9343](https://wiki.gentoo.org/wiki/Dell_XPS_13_9343 "Dell XPS 13 9343").

The Dell XPS 13 Late 2016 (9360) is the fourth-generation model of the XPS 13 line. It comes with 7th generation Kaby Lake or 8th generation Kaby Lake R processors. Firmware is required in order to get Wi-Fi and Bluetooth operational.

-   Intel [Kaby Lake](https://en.wikipedia.org/wiki/Kaby_Lake "wikipedia:Kaby Lake") or Kaby Lake R processor.
-   13.3\" InfinityEdge display (QHD+ 3200x1800 touch display or FHD AG 1920x1080 display).
-   Intel HD Graphics 620.
-   4-16 GB LPDDR3 1866 MHz RAM (soldered in to motherboard).
-   128-512 GB NVM Express SSD.
-   2x USB 3 ports.
-   USB Type-C port.
-   SD card reader.
-   Killer 1535 802.11ac 2x2 WiFi (requires firmware) and Bluetooth 4.1 (requires firmware).

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
        -   [[2.1.1] [USB]](#USB)
        -   [[2.1.2] [NVM Express SSD]](#NVM_Express_SSD)
        -   [[2.1.3] [Wireless]](#Wireless)
        -   [[2.1.4] [SD card reader]](#SD_card_reader)
        -   [[2.1.5] [Integrated webcam]](#Integrated_webcam)
        -   [[2.1.6] [USB Type-C and Thunderbolt]](#USB_Type-C_and_Thunderbolt)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [make.conf]](#make.conf)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [No sound card detected]](#No_sound_card_detected)
    -   [[4.2] [ACPI error in syslog]](#ACPI_error_in_syslog)
    -   [[4.3] [Thermal control]](#Thermal_control)

## [Overview]

Printout of lspci:

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Device 5904 (rev 02)
    00:02.0 VGA compatible controller: Intel Corporation Device 5916 (rev 02)
    00:04.0 Signal processing controller: Intel Corporation Device 1903 (rev 02)
    00:14.0 USB controller: Intel Corporation Device 9d2f (rev 21)
    00:14.2 Signal processing controller: Intel Corporation Device 9d31 (rev 21)
    00:15.0 Signal processing controller: Intel Corporation Device 9d60 (rev 21)
    00:15.1 Signal processing controller: Intel Corporation Device 9d61 (rev 21)
    00:16.0 Communication controller: Intel Corporation Device 9d3a (rev 21)
    00:1c.0 PCI bridge: Intel Corporation Device 9d10 (rev f1)
    00:1c.4 PCI bridge: Intel Corporation Device 9d14 (rev f1)
    00:1c.5 PCI bridge: Intel Corporation Device 9d15 (rev f1)
    00:1d.0 PCI bridge: Intel Corporation Device 9d18 (rev f1)
    00:1f.0 ISA bridge: Intel Corporation Device 9d58 (rev 21)
    00:1f.2 Memory controller: Intel Corporation Device 9d21 (rev 21)
    00:1f.3 Audio device: Intel Corporation Device 9d71 (rev 21)
    00:1f.4 SMBus: Intel Corporation Device 9d23 (rev 21)
    3a:00.0 Network controller: Qualcomm Atheros QCA6174 802.11ac Wireless Network Adapter (rev 32)
    3b:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. Device 525a (rev 01)
    3c:00.0 Non-Volatile memory controller: Toshiba America Info Systems Device 0115 (rev 01)

Printout of lsusb (builtin devices, no external devices connected):

`root `[`#`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 003: ID 0bda:568b Realtek Semiconductor Corp.
    Bus 001 Device 002: ID 0cf3:e300 Atheros Communications, Inc.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Installation]

### [Kernel]

#### [USB]

USB 3.0 support needs to be enabled for the USB bus to function. USB 2.0 and USB 1.1 can be disabled. Failure to add support for the USB 3.0 bus to the kernel will prevent other hardware from functioning (Bluetooth, SD card reader etc.).

[KERNEL] **USB, 4.9.6-gentoo-r1**

    Device Drivers  --->
        [*] USB support  --->
            <*>     xHCI HCD (USB 3.0) support
            ...
            < >     EHCI HCD (USB 2.0) support
            ...
            < >     OHCI HCD (USB 1.1) support

#### [NVM Express SSD]

In the BIOS set the SATA Controller to `AHCI`. The default for models pre-loaded with Windows is `RAID` and Linux will not detect the device unless the BIOS setting is changed.

For required kernel options, see [NVMe](https://wiki.gentoo.org/wiki/NVMe "NVMe").

#### [Wireless]

See [Qualcomm Atheros QCA6174](https://wiki.gentoo.org/wiki/Qualcomm_Atheros_QCA6174 "Qualcomm Atheros QCA6174")

#### [SD card reader]

Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader.

[KERNEL] **SD Card Reader, Prior Linux 4.16**

    Device Drivers  --->
        Multifunction device drivers  --->
            <M> Realtek PCI-E card reader
        <M> MMC/SD/SDIO card support  --->
            <M>   Realtek PCI-E SD/MMC Card Interface Driver

\

[KERNEL] **SD Card Reader, Since Linux 4.16**

    Device Drivers  --->
        Misc devices  --->
            <M> Realtek PCI-E card reader
        <M> MMC/SD/SDIO card support  --->
            <M>   Realtek PCI-E SD/MMC Card Interface Driver

#### [Integrated webcam]

Enable UVC and V4L.

[KERNEL] **Webcam, 4.8.14-gentoo**

    Device Drivers  --->
        <M> Multimedia support  --->
            [*]   Cameras/video grabbers support
                <M>   USB Video Class (UVC)
            [*]   V4L platform devices  --->
            [*]   Autoselect ancillary drivers (tuners, sensors, i2c, frontends)

#### [USB Type-C and Thunderbolt]

The USB Type-C root hub is only enabled when a device is connected to the port and requires PCI-hotplug support to function. This should also allow hotplugging Thunderbolt devices.

[KERNEL] **PCI Hotplugging, 4.9.6-gentoo-r1**

    Bus options (PCI etc.)  --->
        [*] PCI support
        [*]   PCI Express Port Bus support
        [*]     PCI Express Hotplug driver
        [*] Support for PCI Hotplug  --->
            [*]   ACPI PCI Hotplug driver

## [Configuration]

### [make.conf]

[FILE] **`/etc/portage/make.conf`**

    CHOST="x86_64-pc-linux-gnu"
    CFLAGS="-O2 -pipe -march=native"
    CXXFLAGS="$"
    MAKEOPTS="-j5"
    CPU_FLAGS_X86="mmx sse sse2 sse3 ssse3 sse4_1 sse4_2 aes mmxext avx avx2 fma3 f16c"

    GRUB_PLATFORMS="efi-64"

    VIDEO_CARDS="intel i965"
    INPUT_DEVICES="evdev synaptics" # Alternatively use libinput

Most users will probably want to [enable tap-to-click](https://wiki.gentoo.org/wiki/Libinput#Touchpad_tap-to-click "Libinput") if libinput is used as the Xorg device driver.

## [Troubleshooting]

### [No sound card detected]

If the \"Audio device\" doesn\'t appear in lspci command. You may need to cold boot (no reboot, but actual cold boot) to fix it.

### [ACPI error in syslog]

If an ACPI error similar to below is logged to syslog a BIOS update might be required. An update from 1.0.7 to 1.3.2 solved the problem in at least one case.

[CODE] **syslog**

    [ 0.017217] ACPI Error: [\_SB_.PCI0.XHC_.RHUB.HS11] Namespace lookup failure, AE_NOT_FOUND (20150930/dswload-210)
    [ 0.017220] ACPI Exception: AE_NOT_FOUND, During name lookup/catalog (20150930/psobject-227)
    [ 0.017248] ACPI Exception: AE_NOT_FOUND, (SSDT:xh_rvp08) while loading table (20150930/tbxfload-193)
    [ 0.022535] ACPI Error: 1 table load failures, 7 successful (20150930/tbxfload-214)

The easiest way to perform a firmware update under Linux is by using the firmware update functionality built into the BIOS. Place the [.exe] firmware update file on the EFI boot partition, hit [F12] at boot and select **BIOS Update** from the one-time boot selection screen. When prompted select the downloaded firmware update file.

### [Thermal control]

If you are unhappy with the default thermal control (fan speed), you may use install sys-libs/libsmbios with the python USE flag and change the thermal mode with smbios-thermal-ctl.