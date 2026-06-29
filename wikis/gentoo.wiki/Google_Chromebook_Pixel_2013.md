[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Google_Chromebook_Pixel_(2013)&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://support.google.com/pixelbook/topic/9807729)

[[]][Specifications](https://support.google.com/pixelbook/answer/2762037)

[[]][Developer information](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/chromebook-pixel)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Chromebook_Pixel "wikipedia:Chromebook Pixel")

This Chromebook went on sale in 2013 in two versions. The first version has a 32 GB SSD. The second version has a 64 GB SSD and a removable LTE modem. The SSD in both versions is soldered into the motherboard, so it is not upgradeable. Both versions have the same motherboard, so the first version also has the slot for the modem, but not the modem itself.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)

## [Hardware]

** Tip**\
The storage memory can be increased by installing a Mini PCI-E to SD adapter in the slot designed for LTE modem. [\[1\]](https://reddit.com/r/GalliumOS/comments/cv0v1w/enable_mini_pcie_port_on_pixel_2013_on_galliumos) [\[2\]](https://reddit.com/r/GalliumOS/comments/7og7ah/chromebook_pixel_2013_wwan_slot_storage_experiment)

### [Standard]

  ------------- ----------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device        Make/model                                Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU           Intel Core i5-3427U (dual-core 1.8 GHz)   Works    N/A                      N/A                N/A
  GPU           Intel HD Graphics 4000                    Works    N/A                      N/A                N/A
  SSD           SanDisk SSD i100 (soldered on-board)      Works    N/A                      N/A                N/A
  WiFi          Atheros AR5BMD22                          Works    N/A                      N/A                N/A
  Touchpad      N/A                                       Works    N/A                      N/A                N/A
  Touchscreen   Atmel mXT224SL                            Works    N/A                      N/A                N/A
  ------------- ----------------------------------------- -------- ------------------------ ------------------ ---------------- -------

### [Accessories]

  ----------- ------------ ------------- ------------------------ ------------------ ---------------- -------
  Device      Make/model   Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  LTE Modem   N/A          Not tested    N/A                      N/A                N/A
  ----------- ------------ ------------- ------------------------ ------------------ ---------------- -------

## [Installation]

### [Firmware]

** Warning**\
Installing the operating system on this Chromebook requires flashing custom firmware, as the stock firmware reached **EOL**. If for some reason it is still necessary to use stock firmware, there are two articles that may help: [David S. Miller\'s article](http://vger.kernel.org/~davem/chromebook_pixel_linux.txt) and [Brock M. Tice\'s article](https://blog.brocktice.com/2013/03/09/running-debian-wheezy-7-0-on-the-chromebook-pixel). But it is highly **not recommended** to use the stock firmware because of **bugs** and lack of **security** updates. Proceed at your own risk.

** Tip**\
You can follow [this video](https://www.youtube.com/watch?v=r3Sj54dpbf8) to install the UEFI firmware provided by MrChromebox. The video also shows how to remove the screw.

To install the UEFI firmware, the hardware write protection must first be disabled. To do this, it is necessary to open the case and remove the special screw according to [the manual](https://www.chromium.org/chromium-os/developer-information-for-chrome-os-devices/chromebook-pixel). After that, the [remaining steps](https://wiki.gentoo.org/wiki/Chromebook#Installation "Chromebook") must be performed.

### [Kernel]

[KERNEL]

    Device Drivers  --->
      [*] Network device support  --->
        [*]   Wireless LAN  --->
          <*>   Atheros Wireless Cards  --->
            <*>   Atheros 802.11n wireless cards support
      Input device support  --->
        [*]   Touchscreens  --->
          <*>   Atmel mXT I2C Touchscreen
      [*] Platform support for Chrome hardware  --->
        <*>   Chrome OS Laptop

### [Emerge]

[FILE] **`/etc/portage/make.conf`**

    VIDEO_CARDS="intel i965"
    INPUT_DEVICES="evdev synaptics"