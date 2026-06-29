**Resources**

[[]][Home](https://www.dell.com/support/home/en-us/product-support/product/latitude-d630/overview)

[[]][Wikipedia](https://en.wikipedia.org/wiki/https://en.wikipedia.org/wiki/Dell_Latitude#Latitude_D630 "wikipedia:https://en.wikipedia.org/wiki/Dell Latitude")

This article describes the hardware and the respective drivers on Dell Latitude D630/D830 laptops.

## Contents

-   [[1] [Hardware and Drivers]](#Hardware_and_Drivers)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Accessories]](#Accessories)
-   [[2] [See also]](#See_also)

## [Hardware and Drivers]

### [Standard]

  -------------------- ----------------------------------------- -------- ------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------ --
  Device               Make/model                                Status   Vendor ID / Product ID   Kernel driver(s)                                                                                                                                         Kernel version   Notes
  CPU                  Intel Core Duo                            Works                             [Intel Core 2](https://wiki.gentoo.org/wiki/Intel_Core_2 "Intel Core 2")
  Hard disk drive      Hitachi Travelstar                        Works                             [ahci](https://wiki.gentoo.org/wiki/HDD "HDD")
  Optical drive        TSSTcorp DVD+-RW TS-L632D                 Works                             [ata_piix](https://wiki.gentoo.org/wiki/CDROM "CDROM")
  Graphic card         Intel GMA X3100M                          Works                             [intel](https://wiki.gentoo.org/wiki/Intel "Intel")
  Graphic card         NVIDIA Quadro NVS 135M                    Works                             [nvidia-drivers](https://wiki.gentoo.org/wiki/Nvidia-drivers "Nvidia-drivers")/[Nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau")
  Keyboard                                                       Works                             [evdev](https://wiki.gentoo.org/wiki/Evdev "Evdev")
  Touchpad             ALPS GlidePoint                           Works                             [synaptics](https://wiki.gentoo.org/wiki/Synaptics "Synaptics")
  Ethernet             Broadcom NetXtreme BCM5755M               Works                             [tg3](https://wiki.gentoo.org/wiki/Ethernet "Ethernet")
  WiFi                 Intel PRO/Wireless 3945ABG / 4965AGN      Works                             [iwl3945 / iwl4965](https://wiki.gentoo.org/wiki/Wifi "Wifi")                                                                                               See [Intel Corporation PRO/Wireless 3945ABG](https://wiki.gentoo.org/wiki/Intel_Corporation_PRO/Wireless_3945ABG "Intel Corporation PRO/Wireless 3945ABG")
  WiFi                 Dell Wireless 1390 / 1490 / 1505          Works                             [b43](https://wiki.gentoo.org/wiki/Wifi "Wifi")
  Modem                Connexant HSF                                                                                                                                                                                                                                         Proprietary software, full version with costs
  UMTS modem           Dell Wireless 5520 HSDPA
  CDMA modem           Dell Wireless 5720 EVDO
  Sound card           Intel HD Audio, SigmaTel STAC9205 Codec   Works                             [snd_intel_hda](https://wiki.gentoo.org/wiki/ALSA "ALSA")
  USB                  USB 1.1                                   Works                             [uhci](https://wiki.gentoo.org/wiki/USB "USB")
  USB                  USB 2.0                                   Works                             [ehci](https://wiki.gentoo.org/wiki/USB "USB")
  Bluetooth            Dell Wireless 360 Bluetooth               Works                             [btusb](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth")
  Firewire             02 Micro FireWire                         Works                             [FireWire](https://wiki.gentoo.org/wiki/FireWire "FireWire")
  PC-card              O2 Micro OZ601/6912/711E0                 Works                             [yenta_socket](https://wiki.gentoo.org/wiki/PC-Card "PC-Card")
  Serial port                                                    Works                             serial
  ACPI                                                           Works                             [ACPI](https://wiki.gentoo.org/wiki/ACPI "ACPI")
  Fingerprint reader   SG5 Thomson Microelectronics              Works                             [fprint](https://wiki.gentoo.org/wiki/Fingerprint_Reader "Fingerprint Reader")
  Sensors                                                        Works                             [coretemp](https://wiki.gentoo.org/wiki/Lm_sensors "Lm sensors"), [i8k](https://wiki.gentoo.org/wiki/I8k "I8k")
  Onboard              O2 Micro OZ776CCID                        Works                             [ccid](https://wiki.gentoo.org/wiki/PCSC-Lite "PCSC-Lite")
  -------------------- ----------------------------------------- -------- ------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------ --

### [Accessories]

  ----------------- ------------------------ -------- -------- ----------------------------------------------------------------- ---------------- -------
  Device            Make/model               Status   Bus ID   Kernel driver(s)                                                  Kernel version   Notes
  Docking station   Dell Latitude D Models   Works             [acpi_dock](https://wiki.gentoo.org/wiki/Acpi_dock "Acpi dock")
  ----------------- ------------------------ -------- -------- ----------------------------------------------------------------- ---------------- -------

## [See also]

-   [Power management](https://wiki.gentoo.org/wiki/Power_management "Power management") --- describes methods to save energy for longer battery runtimes, a quieter computer, lower power bills, and an environmentally friendly impact.