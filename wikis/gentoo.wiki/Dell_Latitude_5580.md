**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/latitude-15-5580-laptop/overview)

[[]][Hardware Maintenance Manual](https://dl.dell.com/topicspdf/latitude-15-5580-laptop_owners-manual_en-us.pdf)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
        -   [[2.2.1] [Touchpad]](#Touchpad)
        -   [[2.2.2] [Nvidia dGPU and freeze on starting X with dGPU switched off by bbswitch]](#Nvidia_dGPU_and_freeze_on_starting_X_with_dGPU_switched_off_by_bbswitch)
        -   [[2.2.3] [SD card reader]](#SD_card_reader)
        -   [[2.2.4] [Webcam]](#Webcam)
-   [[3] [See also]](#See_also)

## [Hardware]

### [Standard]

+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Device         | Make/model                                                                                                                                   | Status      | Vendor ID / Product ID | Kernel driver(s)                                          | Kernel version | Notes                                                              |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| CPU            | [Intel i5-7300U](https://ark.intel.com/products/97472/Intel-Core-i5-7300U-Processor-3M-Cache-up-to-3_50-GHz) | Works       | N/A                    | N/A                                                       | 4.12.12        |                                                                    |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Controller     | Intel Sunrise Point-LP Serial IO I2C Controller                                                                                              | Works       |                        | mfd_intel_lpss\_                                | 4.12.12        | required for touchpad                                              |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Controller     | Intel Sunrise Point-LP Thermal subsystem                                                                                                     | Works       |                        | intel_pch_thermal                                         | 4.12.12        |                                                                    |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Video          | Intel Device 5916                                                                                                                            | Works       |                        | i915                                                      | 4.12.12        |                                                                    |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Audio          | Intel Device 9d71                                                                                                                            | Works       |                        | snd_hda_intel                                             | 4.12.12        |                                                                    |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Ethernet       | [Intel I219-LM](https://ark.intel.com/products/82185/Intel-Ethernet-Connection-I219-LM)                      | Works       |                        | e1000e                                                    | 4.12.12        |                                                                    |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Wireless       | Intel Wireless 8265 / 8275                                                                                                                   | Works       |                        | [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") | 4.12.12        | linux-firmware-2017 wifi-8265-27.ucode                             |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Touchpad       | DLL07A8:01 044E:120B                                                                                                                         | Works       |                        | i2c_designware\_                           | 4.12.12        | with alps/synaptics                                                |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| SD Card reader | Realtek RTS525A PCI Express Card Reader                                                                                                      | Works       |                        | mfd_rtsx_pci, mmc_realtek_pci                             | 4.12.12        |                                                                    |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Bluetooth      | Intel Bluetooth controller                                                                                                                   | Works       | 8087:0a2b              | intel/ibt-12-16.sfi                                       | 4.19.97        | with regulatory.db regulatory.db.p7s, all in CONFIG_EXTRA_FIRMWARE |
|                |                                                                                                                                              |             |                        |                                                           |                |                                                                    |
|                |                                                                                                                                              |             |                        | intel/ibt-12-16.ddc                                       | 5.4.80         |                                                                    |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Webcam         | Realtek Integrated Webcam HD                                                                                                                 | Works       | 0bda:568c              | uvcvideo (usb_video_class)                                | 4.12.12        |                                                                    |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+
| Smartcard      | Broadcom 5880                                                                                                                                | Not tested  | 0a5c:5832              |                                                           |                |                                                                    |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------+-------------+------------------------+-----------------------------------------------------------+----------------+--------------------------------------------------------------------+

## [Installation]

### [Firmware]

You will need some firmware from the Linux firmware package:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

-   iwlwifi-8265-27.ucode
-   i915/kbl_dmc_ver1_01.bin (be sure to follow the [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") manual)

And add them space-separated in the kernel firmware selection:

[KERNEL] **Enable firmware**

    Device Drivers  --->
        Generic Driver Options  --->
            (iwlwifi-8265-27.ucode i915/kbl_dmc_ver1_01.bin) External firmware blobs to build into the kernel binary
            (/lib/firmware) Firmware blobs root directory

### [Kernel]

#### [Touchpad]

To set the touchpad (and keyboard knob) in the kernel, do the following.

[KERNEL] **Enable support for touchpad and knob**

    Device Drivers  --->
         I2C support  --->
             I2C Hardware Bus support  --->
                  <*> Synopsys DesignWare Platform
         Multifunction device drivers  --->
                  <*> Intel Low Power Subsystem support in PCI mode
         HID support  --->
             Special HID drivers  --->
                 <*> Alps HID device support
             I2C HID support  --->
                 <*> HID over I2C transport layer

After that, the [Synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics") article can be followed.

NOTE! Altering acpi_osi parameter may result in touchpad being not detected and as such, not working.

#### [Nvidia dGPU and freeze on starting X with dGPU switched off by bbswitch]

It may occour that Xorg freezes on start if prior to that dGPU was disabled using the bbswitch kernel module. The system may also randomely freeze after waking out of s2ram. Soluton to that is to enable CONFIG_ACPI_REV_OVERRIDE_POSSIBLE and add acpi_rev_override=5 to boot params. [https://github.com/Bumblebee-Project/Bumblebee/issues/764#issuecomment-395869314](https://github.com/Bumblebee-Project/Bumblebee/issues/764#issuecomment-395869314)

#### [SD card reader]

[KERNEL] **Enable support for the SD card reader**

    Device Drivers  --->
         Multifunction device drivers  --->
             <*> Realtek PCI-E card reader
         <*> MMC/SD/SDIO card support  --->
             <*>   Realtek PCI-E SD/MMC Card Interface Driver

#### [Webcam]

[KERNEL] **Enable support for the webcam**

    Device Drivers  --->
        <*> Multimedia support  --->
            [*]   Media USB Adapters  --->.
                <*>   USB Video Class (UVC)

And add a user to the video group to access the [/dev/video0].

`root `[`#`]`gpassword -a <user> video`

## [See also]

-   [Intel](https://wiki.gentoo.org/wiki/Intel "Intel")