**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/latitude-14-5491-laptop/overview)

[[]][Specifications](https://dl.dell.com/content/manual53353521-latitude-5491-setup-and-specifications-guide.pdf)

[[]][Hardware Maintenance Manual](https://dl.dell.com/topicspdf/latitude-14-5491-laptop_service-manual_en-us.pdf)

The Dell Latitude 5491 is a 14\" laptop with 8th generation Intel Core i5/i7 CPU and a dedicated NVidia GeForce MX130 GPU.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Microcode]](#Microcode)
    -   [[2.3] [Kernel]](#Kernel)
        -   [[2.3.1] [Touchpad]](#Touchpad)
        -   [[2.3.2] [SD card reader]](#SD_card_reader)
        -   [[2.3.3] [Webcam]](#Webcam)

## [Hardware]

### [Standard]

  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------- -------------- ------------------------ ----------------------------------------------------------- ---------------- -------------------------------------------------------------------------------------------------------------------------------------------
  Device               Make/model                                                                                                                                  Status         Vendor ID / Product ID   Kernel driver(s)                                            Kernel version   Notes
  CPU                  Intel Core i5/i7 8th gen.                                                                                                                   Works                                                                                               5.4.38
  PCIe controller      Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor PCIe Controller                                                         Works                                   pcieport                                                    5.4.38           Twice
  PCIe controller      Intel Corporation Cannon Lake PCH PCI Express Root Port                                                                                     Works                                   pcieport                                                    5.4.38           Twice, once used for the Alps synaptics
  Video                Intel Corporation UHD Graphics 630                                                                                                          Works                                   i915                                                        5.4.38
  Video                NVidia GeForce MX130 (GM108M)                                                                                                               Works                                   nouveau or nvidia                                           5.4.38           Tested with proprietary drivers
  Audio                Intel Corporation Cannon Lake PCH cAVS                                                                                                      Works                                   snd_hda_intel                                               5.4.38
  Ethernet             Intel Corporation Ethernet Connection I219-LM                                                                                               Works                                   e1000e                                                      5.4.38
  WiFi                 Intel Corporation Wireless-AC 9560 \[Jefferson Peak\]                                                                                       Works                                   [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")   5.4.38           [Requires firmware](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi?s%5b%5d=AC%209560#firmware)
  WWAN                 Sierra Wireless, Inc. [DW5811e](https://linux-hardware.org/index.php?id=usb:413c-81b6) Snapdragon™ X7 LTE   Not tested     413c:81b6
  Bluetooth            Bluetooth                                                                                                                                   Works          8087:0aaa                btusb                                                       5.4.38
  USB controller       Intel Corporation Cannon Lake PCH USB 3.1 xHCI Host Controller                                                                              Works                                   xhci_hcd                                                    5.4.38
  Sata controller      Intel Corporation 82801 Mobile SATA Controller                                                                                              Works                                   ahci                                                        5.4.38
  SD card reader       Realtek Semiconductor Co., Ltd. RTS525A PCI Express Card Reader                                                                             Works                                   rtsx_pci                                                    5.4.38           Does not detect the insertion & removal of the SD card straight away
  Webcam               Sunplus Innovation Technology Inc.                                                                                                          Works          1bcf:2b96                uvcvideo                                                    5.4.38
  Fingerprint reader   Broadcom Corp 5880                                                                                                                          Not tested     0a5c:5834
  Thermal              Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem                                                       Works                                   proc_thermal                                                5.4.38
  Thermal              Intel Corporation Cannon Lake PCH Thermal Controller                                                                                        Works                                   intel_pch_thermal                                           5.4.38
                       Intel Corporation Xeon E3-1200 v5/v6 / E3-1500 v5 / 6th/7th/8th Gen Core Processor Gaussian Mixture Model                                   Not working                                                                                         5.7.38           [Linux hardware status](https://linux-hardware.org/index.php?id=pci:8086-1911-8086-2064)
  I2C controllers      Intel Corporation Cannon Lake PCH Serial IO I2C Controller                                                                                  Works                                   intel-lpss                                                  5.4.38           Twice
  SMBus                Intel Corporation Cannon Lake PCH SMBus Controller                                                                                          Works                                   i801_smbus                                                  5.4.38
  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------- -------------- ------------------------ ----------------------------------------------------------- ---------------- -------------------------------------------------------------------------------------------------------------------------------------------

For [hardware probes](https://wiki.gentoo.org/wiki/Hardware_probe "Hardware probe") see [https://linux-hardware.org/index.php?view=computers&vendor=Dell&model=Latitude+5491](https://linux-hardware.org/index.php?view=computers&vendor=Dell&model=Latitude+5491)

## [Installation]

### [Firmware]

The [Linux firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") package will have to be installed, for certain components to work properly

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

-   iwlwifi-9000-pu-b0-jf-b0-34.ucode
-   i915/skl_dmc_ver1_27.bin

\
And add them space-separated in the kernel firmware selection:

[KERNEL] **Enable firmware**

    Device Drivers  --->
        Generic Driver Options  --->
            (iwlwifi-9000-pu-b0-jf-b0-34.ucode i915/skl_dmc_ver1_27.bin) External firmware blobs to build into the kernel binary
            (/lib/firmware) Firmware blobs root directory

### [Microcode]

Be sure to follow the Wiki page on how to load the [Intel microcode](https://wiki.gentoo.org/wiki/Intel_microcode "Intel microcode")

### [Kernel]

#### [Touchpad]

To set the touchpad and keyboard knob in the kernel, do the following.

[KERNEL] **Enable support for touchpad and knob**

    Device Drivers  --->
         I2C support  --->
             I2C Hardware Bus support  --->
                  <*> Synopsys DesignWare Platform
         Multifunction device drivers  --->
                  <*> Intel Low Power Subsystem support in PCI mode
         HID support  --->
             I2C HID support  --->
                 <*> HID over I2C transport layer

Do not forget to add the `libinput` in the `INPUT_DEVICE` variable of the [/etc/portage/package.use] file:

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput

Here is what is excpected:

`user `[`$`]`dmesg`

    [    2.075357] mousedev: PS/2 mouse device common for all mice
    [    2.190180] input: DELL0818:00 044E:121F Mouse as /devices/pci0000:00/0000:00:15.1/i2c_designware.1/i2c-9/i2c-DELL0818:00/0018:044E:121F.0001/input/input7
    [    2.190347] hid-multitouch 0018:044E:121F.0001: input,hidraw0: I2C HID v1.00 Mouse [DELL0818:00 044E:121F] on i2c-DELL0818:00

#### [SD card reader]

[KERNEL] **Enable support for the SD card reader**

    Device Drivers  --->
         Multifunction device drivers  --->
             <*> Realtek PCI-E card reader
         <*> MMC/SD/SDIO card support  --->
             <*> Realtek PCI-E SD/MMC Card Interface Driver

#### [Webcam]

[KERNEL] **Enable support for the webcam**

    Device Drivers  --->
        <*> Multimedia support  --->
            [*] Media USB Adapters  --->
                <*> USB Video Class (UVC)

And add a user to the video group to access the [/dev/video0].

`root `[`#`]`gpassword -a <user> video`