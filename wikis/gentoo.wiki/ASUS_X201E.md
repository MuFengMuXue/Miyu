[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=ASUS_X201E&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

Asus x201e is ultra-slim and light notebook manufactured by Asus. It has Intel Core i3, Pentium or Celeron processors with integrated graphics with up to 4GB of RAM. This article can help you to install Gentoo Linux on Asus X201E and point to typical problems during installation and setting the system.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [General Configuration]](#General_Configuration)
    -   [[1.2] [Hard Disks and DVD Drives]](#Hard_Disks_and_DVD_Drives)
    -   [[1.3] [Memory Card Reader]](#Memory_Card_Reader)
    -   [[1.4] [Video Chipset]](#Video_Chipset)
    -   [[1.5] [Input Devices]](#Input_Devices)
    -   [[1.6] [Ethernet]](#Ethernet)
    -   [[1.7] [802.11 Wifi]](#802.11_Wifi)
    -   [[1.8] [Bluetooth]](#Bluetooth)
    -   [[1.9] [Sound]](#Sound)
    -   [[1.10] [USB/USB3.0]](#USB.2FUSB3.0)
    -   [[1.11] [Webcam]](#Webcam)

## [Hardware]

### [General Configuration]

There is no need for any specific configuration except drivers and one GRUB hack to make function keys work.

### [Hard Disks and DVD Drives]

The only hard drive is connected via SATA. There is no empty space to place another hard drive or cd/dvd drive. Driver in use for hard drive is ahci:

[KERNEL] **SATA Hard Drive Support**

    Device Drivers  --->
        <*> Serial ATA and Parallel ATA drivers  --->
            <*>   AHCI SATA support

### [Memory Card Reader]

TODO

### [Video Chipset]

Integrated Intel HD Graphics uses I915 driver:

[KERNEL] **Video Support**

    Device Drivers  --->
            Graphics support  --->
            <*> Intel 8xx/9xx/G3x/G4x/HD Graphics

### [Input Devices]

The keyboard support for X11 is provided by evdev.

To make [Fn] + [F5] (brightness down) and [Fn] + [F6] (brightness up) function keys work it is needed to unspecify acpi_osi in GRUB.

[FILE] **`/etc/default/grub`Brightness Keys Support**

    GRUB_CMDLINE_LINUX_DEFAULT='quiet splash acpi_osi='

Nevertheless brightness set with keyboard will not synchronize with brightness set with KDE.

Touchpad support is provided through synaptics.

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: evdev synaptics

\
Also you must enable CONFIG_MOUSE_PS2_ELANTECH in kernel.

[KERNEL] **Touchpad Support**

    Device Drivers  --->
        [*] Input device support  --->
            [*] Generic input layer (needed for keyboard, mouse, ...)  --->
                [*] Mice  --->
                    [*] PS/2 mouse  --->
                        [*] Elantech PS/2 protocol extension

Double- and triple- tapping and scroll will work, although 4- and 5- finger tap will not be recognized (driver issue?).

### [Ethernet]

Networking is provided by Qualcomm Atheros AR8162 Fast Ethernet. Alx driver is needed:

[KERNEL] **Ethernet Support**

    Device Drivers  --->
        [*] Network device support  --->
            [*] Ethernet driver support  --->
                [*] Atheros devices  --->
                    [*] Qualcomm Atheros AR816x/AR817x support

### [802.11 Wifi]

Wifi is provided by Qualcomm Atheros AR9485 Wireless Network Adapter. ath9k driver is needed:

[KERNEL] **Wifi Support**

    Device Drivers  --->
        [*] Network device support  --->
            [*] Wireless LAN  --->
                [*] Atheros Wireless Cards  --->
                    [*] Atheros 802.11n wireless cards support  --->
                        [*] Atheros ath9k PCI/PCIe bus support

### [Bluetooth]

Though Atheros AR9485 has integrated bluetooth, ath9k driver doesn\'t support it.

### [Sound]

Sound system is based on Intel HD Audio and could be easily brought up by snd_hda_intel driver:

[KERNEL] **Audio Support**

    Device Drivers  --->
        <*> Sound card support  --->
            <*> Advanced Linux Sound Architecture  --->
                [*] PCI sound devices  --->
                    <*> Intel HD Audio

### [][USB/USB3.0]

TODO (not tested)

### [Webcam]

Webcam is supported with standart UVC:

[KERNEL] **Webcam Support**

    Device Drivers  --->
        <*> Multimedia support  --->
            [*] Media USB Adapters  --->
                <*> USB Video Class (UVC)