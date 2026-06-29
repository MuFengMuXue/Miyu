\
The Asus Chromebook C201 is a Rockchip RK3288-C (ARMv7-A, Cortex-A17) based, exceptionally free (libre) software friendly portable computer. It\'s a lightweight (ca. 980g) and, thanks to the Rockchip RK3288-C system on chip (SoC), pretty fast device. Besides supporting hardware 3D acceleration without proprietary software its most distinguishing feature is, however, that it is one of only a few devices supported by Libreboot^[\[1\]](#cite_note-1)^. Thus the factory firmware can optionally be replaced with entirely libre firmware. Instructions on how to do this can be found on the [Libreboot website](https://libreboot.org/docs/install/c201.html).

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [SoC]](#SoC)
    -   [[1.2] [Peripherals]](#Peripherals)
-   [[2] [GCC Optimization]](#GCC_Optimization)
-   [[3] [Creating installation media]](#Creating_installation_media)
-   [[4] [Installing Gentoo]](#Installing_Gentoo)
-   [[5] [Built-in wifi]](#Built-in_wifi)
-   [[6] [Issues]](#Issues)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

## [Hardware]

  ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               Make/model                                                                                                                                                                                                               Notes
  Board        Veyron-Speedy, veyron-minnie                                                                                                                                                                                             filename of device tree binary: [rk3288-veyron-speedy.dtb,rk3288-veyron-minnie.dtb]
  SoC          Rockchip RK3288-C
  RAM          4GB                                                                                                                                                                                                                      2GB version available, DDR3
  Firmware     [Coreboot](https://coreboot.org/) with [depthcharge](https://chromium.googlesource.com/chromiumos/platform/depthcharge) payload^[\[2\]](#cite_note-2)^   [physical write-protection](https://libreboot.org/docs/install/c201.html#removing-the-write-protect-screw) (screw), [Libreboot](https://libreboot.org) supported
  Boot media   eMMC, SDXC or USB
  ------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [SoC]

  -------------- ------------------------------------ -------- ------------------- ---------------- -----------------------------------------
  Component      Make/model                           Status   Kernel driver(s)    Kernel version   Notes
  CPU            4 x ARM Cortex-A17                   Works                        4.15             max \@1,8GHz
  GPU            Mali-T764                            Works    Panfrost            5.3              OpenGL ES \<2.0^[\[3\]](#cite_note-3)^
  USB 2.0                                             Works                        4.15             2 \* USB-A
  HDMI                                                 ?       dwhdmi
  Analog Audio   Rockchip I2S                         Works    rockchip_i2s        5.2              Required codecs: es8328_i2c, es8328_spi
  HDMI Audio     Synopsis Designware HDMI I2S Audio    ?       dw_hdmi_i2s_audio   5.15             Required codecs: hdmi_codec
  -------------- ------------------------------------ -------- ------------------- ---------------- -----------------------------------------

### [Peripherals]

  --------------------- ------------------- -------- ------------------ ---------------- ------------------------------------------------
  Component             Make/model          Status   Kernel driver(s)   Kernel version   Notes
  Display               11.6\" @ 1366x768   Works                       4.15             xorg-server via fbdev works
  WiFi                  Broadcom            Works    brcmfmac           4.15             works with [proprietary blobs](#Built-in_wifi)
  Touchpad              Elan I2C            Works    elan_i2c           4.15
  Bluetooth                                  ?
  Embedded controller   Google              Works    cros_ec            4.15
  --------------------- ------------------- -------- ------------------ ---------------- ------------------------------------------------

## [GCC Optimization]

[FILE] **`/etc/portage/make.conf`RK3288 example**

    COMMON_FLAGS="-march=armv7-a -mtune=cortex-a17 -mfpu=neon -mfloat-abi=hard"
    CFLAGS="$"
    CXXFLAGS="$"

** Note**\
For a hardened system consider appending `-fstack-protector-all`

## [Creating installation media]

[Create the installation media](https://wiki.gentoo.org/wiki/Creating_bootable_media_for_depthcharge_based_devices "Creating bootable media for depthcharge based devices") manually.

## [Installing Gentoo]

Consult [Asus Chromebook C201/Installing Gentoo](https://wiki.gentoo.org/wiki/Asus_Chromebook_C201/Installing_Gentoo "Asus Chromebook C201/Installing Gentoo") for instructions on how to install Gentoo on the Asus Chromebook C201.

## [Built-in wifi]

Built-in wifi requires the proprietary binary firmware blob [brcmfmac4354-sdio.bin], provided by [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware `

Furthermore the aforementioned binary expects a nvram, [/lib/firmware/brcm/brcmfmac4354-sdio.txt]. Create it with the content provided by the ChromiumOS project: [https://chromium.googlesource.com/chromiumos/overlays/board-overlays/+/master/overlay-veyron/chromeos-base/chromeos-bsp-veyron/files/firmware/brcmfmac4354-sdio.txt](https://chromium.googlesource.com/chromiumos/overlays/board-overlays/+/master/overlay-veyron/chromeos-base/chromeos-bsp-veyron/files/firmware/brcmfmac4354-sdio.txt)

The ChromiumOS project considers this file belonging to the BSP (Board Support Package) and considers upstreaming the file to [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] as being pointless.^[\[4\]](#cite_note-4)^

For additional background information regarding this nvram, consult the [Linux Wireless wiki](https://wireless.wiki.kernel.org/en/users/drivers/brcm80211#firmware_installation1).

## [Issues]

If the bluetooth module is loaded at any time and the system is suspended, both the bluetooth and wireless driver will stop working. A temporary fix is to blacklist the btsdio module:

`root `[`#`]`echo "blacklist btsdio" > /etc/modprobe.d/blacklist-btsdio.conf`

## [External resources]

-   [https://notabug.org/dimkr/devsus](https://notabug.org/dimkr/devsus)
-   [https://github.com/Miouyouyou/RockMyy](https://github.com/Miouyouyou/RockMyy)
-   [http://www.synkhronix.com/journal/gentoo-chromebook](http://www.synkhronix.com/journal/gentoo-chromebook)
-   [http://www.galexander.org/chromebook](http://www.galexander.org/chromebook)
-   [https://wiki.debian.org/InstallingDebianOn/Asus/C201](https://wiki.debian.org/InstallingDebianOn/Asus/C201)
-   [https://libreboot.org/docs/hardware/c201.html](https://libreboot.org/docs/hardware/c201.html)

## [References]

1.  [[[↑](#cite_ref-1)] [[List of supported hardware](https://libreboot.org/docs/hardware/#list-of-supported-hardware), [Libreboot](https://libreboot.org). Retrieved on June 21st, 2019]]
2.  [[[↑](#cite_ref-2)] [[Depthcharge](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/custom-firmware#TOC-Depthcharge), [Developer Information for Chrome OS Devices](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices). Retrieved on June 21st, 2019]]
3.  [[[↑](#cite_ref-3)] [[GNOME Meets Panfrost](https://rosenzweig.io/blog/gnome-meets-panfrost.html), [blog of Panfrost\'s main developer Alyssa Rosenzweig](https://rosenzweig.io/blog). Retrieved on November 16th, 2019]]
4.  [[[↑](#cite_ref-4)] [[ChromiumOS Git at Google](https://chromium.googlesource.com/chromiumos/third_party/linux-firmware/+/08b6ec4d1cac8dbac24addd2c6b36e5cf4f13923). Retrieved on February 25th, 2019]]