Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Broadcom_Bluetooth/hu "Broadcom Bluetooth (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Broadcom_Bluetooth/ru "Broadcom Bluetooth (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Broadcom_Bluetooth/ja "Broadcom Bluetooth (100% translated)")

**Resources**

[[]][broadcom-bt-firmware homepage](https://github.com/winterheart/broadcom-bt-firmware)

This article details setup for Broadcom Bluetooth 4.x devices mostly based on BCM20702, BCM4354, and BCM4356 chipsets. These bluetooth chipsets are also used in various devices including USB-dongles, hybrid WIFI+Bluetooth embedded chipsets, etc.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Security considerations]](#Security_considerations)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [Kernel]](#Kernel)
    -   [[3.2] [Firmware]](#Firmware)
-   [[4] [Configuration]](#Configuration)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Kernel requires BCM.hcd or BCM\<CHIPSET\>.hcd]](#Kernel_requires_BCM.hcd_or_BCM.3CCHIPSET.3E.hcd)
    -   [[5.2] [After installing firmware device still won\'t work]](#After_installing_firmware_device_still_won.27t_work)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Hardware]

Mostly complete list of supported devices can be [found upstream](https://github.com/winterheart/broadcom-bt-firmware/blob/master/DEVICES.md).

  ------------ ----------------- -------- ------------------------ ------------------ ---------------- --------------------------------------------------------------------------------------------------------------------------------------
  Device       Make/model        Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  USB Dongle   Asus BT-400 USB   Works    `0b05:17cb`              btbcm              4.2              Requires firmware
  USB Dongle   Targus ACB75AU    Works    `0a5c:21e8`              btbcm              3.4+             Requires firmware [brcm/BCM20702A1-0a5c-21e8.hcd]
  ------------ ----------------- -------- ------------------------ ------------------ ---------------- --------------------------------------------------------------------------------------------------------------------------------------

## [Security considerations]

Recently several vulnerabilities have been discovered in the Bluetooth stack such as [CVE-2018-5383](https://www.kb.cert.org/vuls/id/304725/), [CVE-2019-9506](https://www.kb.cert.org/vuls/id/918987/) (KNOB), [CVE-2020-10135](https://www.kb.cert.org/vuls/id/647177/) (BIAS) and others. Since Broadcom has stopped active support for its consumer devices, systems utilizing this software may be subject to security risks. It is wise to assess the risk before moving forward, since the repository maintainer cannot provide security fixes.

## [Installation]

### [Kernel]

Broadcom Bluetooth devices require the `btbcm` kernel module, which can be built with these kernel options:

[KERNEL] **Broadcom Bluetooth support**

    [*] Networking support  --->
        <M>   Bluetooth subsystem support  --->
            Bluetooth device drivers  --->
                <M> HCI USB driver
                [*]   Broadcom protocol support
                [*] Broadcom protocol support

### [Firmware]

Mostly Broadcom Bluetooth stack requires external firmware, supplied with Windows drivers. This can be verified by using following commands:

`user `[`$`]`dmesg | grep -i bluetooth`

    Bluetooth: hci1: BCM: chip id 63
    Bluetooth: hci1: BCM20702A
    Bluetooth: hci1: BCM20702A1 (001.002.014) build 0000
    bluetooth hci1: Direct firmware load for brcm/BCM20702A1-0b05-17cb.hcd failed with error -2
    Bluetooth: hci1: BCM: Patch brcm/BCM20702A1-0b05-17cb.hcd not found

Luckily, the [[[sys-firmware/broadcom-bt-firmware]](https://packages.gentoo.org/packages/sys-firmware/broadcom-bt-firmware)[]] package can be used to install the most recent firmware files for Broadcom Bluetooth:

`root `[`#`]`emerge --ask sys-firmware/broadcom-bt-firmware`

After installation, reinsert Bluetooth device or reboot system for applying firmware. After the reboot the output should look something like the following:

`user `[`$`]`dmesg | grep -i bluetooth`

    Bluetooth: hci1: BCM: chip id 63
    Bluetooth: hci1: BCM20702A
    Bluetooth: hci1: BCM20702A1 (001.002.014) build 0000
    Bluetooth: hci1: BCM20702A1 (001.002.014) build 1467
    Bluetooth: hci1: Broadcom Bluetooth Device

## [Configuration]

After enabling the kernel options and installing firmware, proceed to the [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") article.

## [Troubleshooting]

### [][Kernel requires BCM.hcd or BCM\<CHIPSET\>.hcd]

Some VID/PIDs not yet defined in kernel driver so btbcm cannot properly identify the device:

`user `[`$`]`dmesg | grep -i bluetooth`

    Bluetooth: hci1: BCM: chip id 63
    Bluetooth: hci1: BCM20702A
    Bluetooth: hci1: BCM20702A1 (001.002.014) build 0000
    bluetooth hci1: Direct firmware load for brcm/BCM.hcd failed with error -2
    Bluetooth: hci1: BCM: Patch brcm/BCM.hcd not found

In this case VID/PID will be manually retrieved via the [lspci] or [lsusb] commands:

`user `[`$`]`lsusb`

    ...
    Bus 003 Device 005: ID 0b05:17cb ASUSTek Computer, Inc. Broadcom BCM20702A0 Bluetooth
    ...

Here the VID/PID - `0b05:17cb`. Next, check the [Devices list](https://github.com/winterheart/broadcom-bt-firmware/blob/master/DEVICES.md) and choose firmware as appropriate. After that just copy firmware file into name that requires kernel:

`root `[`#`]`cd /lib/firmware/brcm `

`root `[`#`]`cp BCM20702A1-0b05-17cb.hcd BCM.hcd `

After that reinsert device or reboot system.

### [][After installing firmware device still won\'t work]

Some Bluetooth controller (for example, BCM4354 and BCM4356) are integrated to WiFi chipset (this can be BCM43XX 802.11ac Wireless Network Adapter or just simple generic Broadcom PCIE Wireless). These devices requires two kinds of firmware - first for WiFi, and second for Bluetooth. Without WiFi firmware Bluetooth will not initialize and will not work properly. Firmware for WiFi already included to kernel, but some additional work may be necessary to [place correct NVRAM](https://wireless.wiki.kernel.org/en/users/drivers/brcm80211#broadcom_brcmfmac_driver).

Here example how it can looks (note about [brcm/brcmfmac4356-pcie.txt] loading - this is the customized NVRAM):

`user `[`$`]`dmesg`

    usbcore: registered new interface driver brcmfmac
    brcmfmac 0000:02:00.0: firmware: direct-loading firmware brcm/brcmfmac4356-pcie.bin
    brcmfmac 0000:02:00.0: firmware: direct-loading firmware brcm/brcmfmac4356-pcie.txt
    Bluetooth: hci0: BCM: chip id 101
    Bluetooth: hci0: N360-11
    Bluetooth: hci0: BCM4354A2 (001.003.015) build 0000
    bluetooth hci0: firmware: direct-loading firmware brcm/BCM4354A2-13d3-3485.hcd

## [See also]

-   [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") --- describes the configuration and usage of Bluetooth controllers and devices.

## [References]