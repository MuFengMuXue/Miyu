\
The Samsung Chromebook Plus is a Rockchip RK3399 (ARMv8-A, Cortex-A72/A53) based 2 in 1 touchscreen laptop.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [SoC]](#SoC)
    -   [[1.2] [Peripherals]](#Peripherals)
-   [[2] [GCC Optimization]](#GCC_Optimization)
-   [[3] [Creating installation media]](#Creating_installation_media)
-   [[4] [Installing Gentoo]](#Installing_Gentoo)
-   [[5] [Built-in wifi]](#Built-in_wifi)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Hardware]

  ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------
               Make/model                                                                                                                                                                                                               Notes
  Board        gru-kevin                                                                                                                                                                                                                filename of device tree binary: [rk3399-gru-kevin.dtb]
  SoC          Rockchip RK3399                                                                                                                                                                                                          Branded as the \"OP1\" by Google
  RAM          4GB                                                                                                                                                                                                                      LPDDR3
  Firmware     [Coreboot](https://coreboot.org/) with [depthcharge](https://chromium.googlesource.com/chromiumos/platform/depthcharge) payload^[\[1\]](#cite_note-1)^   physical write protection (need to remove battery to disable as there is no cr50)
  Boot media   Internal eMMC, USB or microSD
  ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------

### [SoC]

+-----------+------------------------------+-----------+------------------+----------------+------------+
| Component | Make/model                   | Status    | Kernel driver(s) | Kernel version | Notes      |
+-----------+------------------------------+-----------+------------------+----------------+------------+
| CPU       | 2 x ARM Cortex-A72 (ARMv8-A) | Works     |                  | 5.12           |            |
|           |                              |           |                  |                |            |
|           | 4 x ARM Cortex-A53 (ARMv8-A) |           |                  |                |            |
+-----------+------------------------------+-----------+------------------+----------------+------------+
| GPU       | 4 x Mali-T860MP4             |  ?        | panfrost         | 5.12           |            |
+-----------+------------------------------+-----------+------------------+----------------+------------+
| USB 3.0   |                              | Works     |                  | 5.12           | 2 \* USB-C |
+-----------+------------------------------+-----------+------------------+----------------+------------+

### [Peripherals]

  ----------- -------------------- -------- ------------------ ---------------- ------------------------------------------------
  Component   Make/model           Status   Kernel driver(s)   Kernel version   Notes
  Display     12.3\" @ 2400x1600   Works                       5.12
  WiFi        Marvell 88W8997      Works    mwifiex            5.12             works with [proprietary blobs](#Built-in_wifi)
  Touchpad                         Works                       5.12
  Bluetooth                         ?
  ----------- -------------------- -------- ------------------ ---------------- ------------------------------------------------

## [GCC Optimization]

[FILE] **`/etc/portage/make.conf`RK3399 example**

    COMMON_FLAGS="-march=armv8-a+crc+crypto -mtune=cortex-a72.cortex-a53 -mfix-cortex-a53-835769 -mfix-cortex-a53-843419"
    CFLAGS="$"
    CXXFLAGS="$"

** Note**\
For a hardened system consider appending `-fstack-protector-all`

## [Creating installation media]

[Create the installation media](https://wiki.gentoo.org/wiki/Creating_bootable_media_for_depthcharge_based_devices "Creating bootable media for depthcharge based devices") manually.

## [Installing Gentoo]

Consult [Samsung Chromebook Plus/Installing Gentoo](https://wiki.gentoo.org/index.php?title=Samsung_Chromebook_Plus/Installing_Gentoo&action=edit&redlink=1 "Samsung Chromebook Plus/Installing Gentoo (page does not exist)") for instructions on how to install Gentoo on the Samsung Chromebook Plus.

## [Built-in wifi]

Built-in wifi requires the proprietary binary firmware blob [88W8997.bin], provided by [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware `

## [External resources]

-   [https://github.com/SolidHal/PrawnOS](https://github.com/SolidHal/PrawnOS)
-   [https://archlinuxarm.org/platforms/armv8/rockchip/samsung-chromebook-plus](https://archlinuxarm.org/platforms/armv8/rockchip/samsung-chromebook-plus)

## [References]

1.  [[[↑](#cite_ref-1)] [[Depthcharge](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/custom-firmware#TOC-Depthcharge), [Developer Information for Chrome OS Devices](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices). Retrieved on June 21st, 2019]]