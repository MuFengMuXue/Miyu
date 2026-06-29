[[]]This article has some todo items:\

-   Hardware Configuration
-   Software Configuration

The Samsung RV511-S04ES is a laptop manufactured by Samsung in 2010. It features an Intel Core i5 480M along with 4GB of RAM, a 500GB hard disk and a nVidia GeForce 315M with 512 MB of VRAM.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [CPU]](#CPU)
    -   [[1.2] [Video]](#Video)
    -   [[1.3] [Audio]](#Audio)
    -   [[1.4] [Input devices]](#Input_devices)
    -   [[1.5] [Ethernet]](#Ethernet)
    -   [[1.6] [Wireless]](#Wireless)
-   [[2] [Software]](#Software)
    -   [[2.1] [Samsung Tools]](#Samsung_Tools)

## [Hardware]

  --------------- ---------------------------------------
  Device          Model
  Processor       Intel® Core™ i5 480M
  Memory          4 GB DDR3 (2 SODIMM)
  Graphics        NVIDIA GeForce 315M 512MB
  Display         15.6\" LED HD (1366 x 768) 16:9 Gloss
  Hard Drive      500 GB SATA
  Optical Drive   Super Multi Dual Layer
  Sound Card      Intel/NVIDIA HD Audio (Speakers/HDMI)
  Network         Realtek RTL8111/8168B 10/100/1000
  Wireless        Broadcom BCM4313 802.11b/g/n
  --------------- ---------------------------------------

  : Hardware summary

### [CPU]

[FILE] **`/etc/portage/make.conf`CPU Flags**

    CFLAGS="-march=native -O2 -pipe"
    CXXFLAGS="$"
    MAKEOPTS="-j5"

### [Video]

[FILE] **`/etc/portage/make.conf`Video Support**

    VIDEO_CARDS="nvidia"

### [Audio]

[KERNEL] **Audio driver**

    <*> Sound card support
      <M> Advanced Linux Sound Architecture
        [*] PCI sound devices
          <M> Intel HD Audio

### [Input devices]

[FILE] **`/etc/portage/make.conf`Input Device Support**

    INPUT_DEVICES="evdev synaptics"

### [Ethernet]

Network is provided by a Realtek RTL8111/8168B Gigabit Ethernet device.

[KERNEL] **Realtek driver**

    Device Drivers
      [*] Network device support
        [*] Ethernet driver support
          [*] Realtek devices
            <M> Realtek 8169 gigabit ethernet support

\

### [Wireless]

Wireless is provided by a Broadcom BCM4313 802.11b/g/n Wireless device.

[KERNEL] **WiFi driver**

    Device Drivers
      Broadcom specific AMBA
        <M> BCMA support
      Network device support
        [*] Wireless LAN
          <M> Broadcom IEEE802.11n PCIe SoftMAC WLAN driver

You will also need linux-firmware:

`root `[`#`]`emerge --ask linux-firmware`

## [Software]

### [Samsung Tools]

TODO