[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Lenovo_Thinkpad_R500&action=edit).

**Resources**

[[]][Specifications](https://support.lenovo.com/us/en/solutions/pd005118-detailed-specifications-thinkpad-r500)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/pccbbs/mobiles_pdf/r500_hmm_en_43y6631_03.pdf)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Trackpoint]](#Trackpoint)
    -   [[3.2] [Power saving]](#Power_saving)
-   [[4] [External resources]](#External_resources)

## [Hardware]

### [Standard]

** Note**\
Everything works except the fingerprint reader.

  -------------------- -------------------------------------------------------------------------- --------- ------------------------ ------------------ ---------------- -------
  Device               Make/model                                                                 Status    Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                  N/A                                                                        Works     N/A                      N/A                N/A
  GPU                  Intel Corporation Mobile 4 Series Chipset Integrated Graphics Controller   Works     N/A                      N/A                N/A
  Ethernet             Broadcom Corporation NetLink BCM5787M Gigabit Ethernet PCI Express         Works     N/A                      N/A                N/A
  Wi-Fi                Intel Corporation PRO/Wireless 5100 AGN \[Shiloh\] Network Connection      Works     N/A                      N/A                N/A
  SD Card Reader       Ricoh Co Ltd R5C822 SD/SDIO/MMC/MS/MSPro Host Adapter                      Works     N/A                      N/A                N/A
  Webcam               N/A                                                                        Works     N/A                      N/A                N/A
  Fingerprint reader   N/A                                                                        Borked    N/A                      N/A                N/A
  -------------------- -------------------------------------------------------------------------- --------- ------------------------ ------------------ ---------------- -------

`root `[`#`]`lspci`

    00:00.0 Host bridge: Intel Corporation Mobile 4 Series Chipset Memory Controller Hub (rev 07)
    00:02.0 VGA compatible controller: Intel Corporation Mobile 4 Series Chipset Integrated Graphics Controller (rev 07)
    00:02.1 Display controller: Intel Corporation Mobile 4 Series Chipset Integrated Graphics Controller (rev 07)
    00:03.0 Communication controller: Intel Corporation Mobile 4 Series Chipset MEI Controller (rev 07)
    00:1a.0 USB controller: Intel Corporation 82801I (ICH9 Family) USB UHCI Controller #4 (rev 03)
    00:1a.1 USB controller: Intel Corporation 82801I (ICH9 Family) USB UHCI Controller #5 (rev 03)
    00:1a.2 USB controller: Intel Corporation 82801I (ICH9 Family) USB UHCI Controller #6 (rev 03)
    00:1a.7 USB controller: Intel Corporation 82801I (ICH9 Family) USB2 EHCI Controller #2 (rev 03)
    00:1b.0 Audio device: Intel Corporation 82801I (ICH9 Family) HD Audio Controller (rev 03)
    00:1c.0 PCI bridge: Intel Corporation 82801I (ICH9 Family) PCI Express Port 1 (rev 03)
    00:1c.1 PCI bridge: Intel Corporation 82801I (ICH9 Family) PCI Express Port 2 (rev 03)
    00:1c.3 PCI bridge: Intel Corporation 82801I (ICH9 Family) PCI Express Port 4 (rev 03)
    00:1c.4 PCI bridge: Intel Corporation 82801I (ICH9 Family) PCI Express Port 5 (rev 03)
    00:1c.5 PCI bridge: Intel Corporation 82801I (ICH9 Family) PCI Express Port 6 (rev 03)
    00:1d.0 USB controller: Intel Corporation 82801I (ICH9 Family) USB UHCI Controller #1 (rev 03)
    00:1d.1 USB controller: Intel Corporation 82801I (ICH9 Family) USB UHCI Controller #2 (rev 03)
    00:1d.2 USB controller: Intel Corporation 82801I (ICH9 Family) USB UHCI Controller #3 (rev 03)
    00:1d.7 USB controller: Intel Corporation 82801I (ICH9 Family) USB2 EHCI Controller #1 (rev 03)
    00:1e.0 PCI bridge: Intel Corporation 82801 Mobile PCI Bridge (rev 93)
    00:1f.0 ISA bridge: Intel Corporation ICH9M LPC Interface Controller (rev 03)
    00:1f.2 SATA controller: Intel Corporation 82801IBM/IEM (ICH9M/ICH9M-E) 4 port SATA Controller [AHCI mode] (rev 03)
    00:1f.3 SMBus: Intel Corporation 82801I (ICH9 Family) SMBus Controller (rev 03)
    03:00.0 Network controller: Intel Corporation PRO/Wireless 5100 AGN [Shiloh] Network Connection
    04:00.0 Ethernet controller: Broadcom Corporation NetLink BCM5787M Gigabit Ethernet PCI Express (rev 02)
    15:00.0 CardBus bridge: Ricoh Co Ltd RL5c476 II (rev ba)
    15:00.1 FireWire (IEEE 1394): Ricoh Co Ltd R5C832 IEEE 1394 Controller (rev 04)
    15:00.2 SD Host controller: Ricoh Co Ltd R5C822 SD/SDIO/MMC/MS/MSPro Host Adapter (rev 21)
    15:00.3 System peripheral: Ricoh Co Ltd R5C843 MMC Host Controller (rev 11)
    15:00.4 System peripheral: Ricoh Co Ltd R5C592 Memory Stick Bus Host Adapter (rev 11)
    15:00.5 System peripheral: Ricoh Co Ltd xD-Picture Card Controller (rev 11)

## [Installation]

### [Firmware]

Install the firmware for Wi-Fi:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [Kernel]

[KERNEL] **Ethernet and Wi-Fi**

    Device Drivers  --->
    [*] Network device support  --->
    [*]   Ethernet driver support  --->
    [*]   Broadcom devices
    <M>     Broadcom Tigon3 support

    [*]   Wireless LAN  --->
    <M>   Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
    -M-     Intel Wireless WiFi

[KERNEL] **Sensors**

    Device Drivers  --->
    -*- I2C support  --->
    I2C Hardware Bus support  --->
    <*> Intel 82801 (ICH/PCH)

    -*- Hardware Monitoring support  --->
    <M>   Intel Core/Core2/Atom temperature sensor

    [*] X86 Platform Specific Device Drivers  --->
    <M>   ThinkPad ACPI Laptop Extras
    [*]     Console audio control ALSA interface

[KERNEL] **Watchdog**

    Device Drivers  --->
    [*] Watchdog Timer Support  --->
    <M>   Intel TCO Timer/Watchdog
    [*]     Intel TCO Timer/Watchdog Specific Vendor Support

[KERNEL] **Random number generator**

    Device Drivers  --->
    Character devices  --->
    [*]   Intel HW Random Number Generator support

[KERNEL] **Memory card reader**

    Bus options (PCI etc.)  --->
    [*] PCCard (PCMCIA/CardBus) support  --->
    [*]   CardBus yenta-compatible bridge support

    Device Drivers  --->
    [*] Memory Technology Device (MTD) support  --->
    [*]   NAND SSFDC (SmartMedia) read only translation layer
    [*]   NAND Device Support  --->
    [*]   Ricoh xD card reader

    [*] MMC/SD/SDIO card support  --->
    [*]   Secure Digital Host Controller Interface support
    [*]   SDHCI support on PCI bus

    [*] Sony MemoryStick card support  --->
    [*]   Ricoh R5C592 MemoryStick interface support

[KERNEL] **Webcam**

    Device Drivers  --->
    [*] Multimedia support  --->
      Media device types --->
        [*]   Cameras/video grabbers support
      Media drivers  --->
        [*]   Media USB Adapters  --->
          [*]   USB Video Class (UVC)

### [Emerge]

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput evdev synaptics

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* intel # or "radeon" in case of AMD/ATi integrated graphics

Install the sensor monitoring program:

`root `[`#`]`emerge --ask sys-apps/lm-sensors`

## [Configuration]

### [Trackpoint]

Enable 3-button scroll:

[FILE] **`/usr/share/X11/xorg.conf.d/11-evdev-trackpoint.conf`**

    Section "InputClass"
            Identifier      "Trackpoint Wheel Emulation"
            MatchProduct    "TPPS/2 IBM TrackPoint|DualPoint Stick|Synaptics Inc. Composite TouchPad / TrackPoint|ThinkPad USB Keyboard with TrackPoint|USB Trackpoint pointing device"
            MatchDevicePath "/dev/input/event*"
            Option  "EmulateWheel"          "true"
            Option  "EmulateWheelButton"    "2"
            Option  "Emulate3Buttons"       "false"
            Option  "XAxisMapping"          "6 7"
            Option  "YAxisMapping"          "4 5"
    EndSection

### [Power saving]

The following configuration enables aggressive power saving:

[FILE] **`/etc/udev/rules.d/10-local-powersave.rules`**

    # PCI runtime power management
    ACTION=="add", SUBSYSTEM=="pci", ATTR="auto"

    # USB autosuspend
    ACTION=="add", SUBSYSTEM=="usb", ATTR="auto"
    ACTION=="add", SUBSYSTEM=="usb", TEST=="power/autosuspend" ATTR="60"

    # SATA active link power management
    SUBSYSTEM=="scsi_host", KERNEL=="host*", ATTR="min_power"

    # Wlan power save
    ACTION=="add", SUBSYSTEM=="net", KERNEL=="wlan*" RUN+="/usr/sbin/iw dev %k set power_save on"

    # Disable bluetooth
    SUBSYSTEM=="rfkill", ATTR=="bluetooth", ATTR="0"

    # Disable wake-on-LAN
    ACTION=="add", SUBSYSTEM=="net", KERNEL=="eth*" RUN+="/usr/sbin/ethtool -s %k wol d"

## [External resources]

-   [https://www.thinkwiki.org/wiki/Category:R500](https://www.thinkwiki.org/wiki/Category:R500)