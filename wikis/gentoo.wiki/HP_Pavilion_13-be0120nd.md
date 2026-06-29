**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-pavilion-aero-13.3-inch-laptop-pc-13-be0000/model/2100683886?sku=468Q4EA)

[[]][Specifications](https://support.hp.com/th-en/document/c07618032)

[[]][Hardware Maintenance Manual](https://kaas.hpcloud.hp.com/pdf-public/pdf_3641731_en-US-1.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c07636741.pdf)

[[]][HP Pavilion](https://en.wikipedia.org/wiki/HP_Pavilion "wikipedia:HP Pavilion")

The HP Pavalion 13-be0120nd is a 13 inch lightweight laptop with aluminum casing. It sports a third generation six core AMD Ryzen 5 5600U CPU, capable of hyperthreading and with AMD Vega2 integrated graphics. Some models have a backlit keyboard, controllable with the FN-4 key.

## Contents

-   [[1] [Connectors]](#Connectors)
-   [[2] [Hardware]](#Hardware)
    -   [[2.1] [lspci]](#lspci)
    -   [[2.2] [lsusb]](#lsusb)
-   [[3] [Devices]](#Devices)
    -   [[3.1] [Audio]](#Audio)
    -   [[3.2] [Wireless network]](#Wireless_network)
    -   [[3.3] [Bluetooth]](#Bluetooth)
    -   [[3.4] [Display]](#Display)
    -   [[3.5] [Keyboard]](#Keyboard)
    -   [[3.6] [Touchpad]](#Touchpad)
-   [[4] [External resources]](#External_resources)

## [Connectors]

-   one laptop power supply connector
-   one USB-C connector, can also be used for power supply
-   two USB-A connectors
-   one HDMI connector
-   an audio headset jack

There is no ethernet or sd card reader available.

## [Hardware]

### [lspci]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Root Complex [1022:1630]
            Subsystem: Hewlett-Packard Company Renoir Root Complex [103c:8919]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Renoir IOMMU [1022:1631]
            Subsystem: Hewlett-Packard Company Renoir IOMMU [103c:8919]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:02.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge [1022:1634]
            Kernel driver in use: pcieport
    00:02.4 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge [1022:1634]
            Kernel driver in use: pcieport
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus [1022:1635]
            Kernel driver in use: pcieport
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 51)
            Subsystem: Hewlett-Packard Company FCH SMBus Controller [103c:8919]
            Kernel driver in use: piix4_smbus
            Kernel modules: sp5100_tco
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
            Subsystem: Hewlett-Packard Company FCH LPC Bridge [103c:8919]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:166a]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:166b]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:166c]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:166d]
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:166e]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:166f]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:1670]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Device [1022:1671]
    01:00.0 Network controller [0280]: Realtek Semiconductor Co., Ltd. Device [10ec:a85a]
            Subsystem: Hewlett-Packard Company Device [103c:88e2]
            Kernel driver in use: rtw89_pci
    02:00.0 Non-Volatile memory controller [0108]: Micron Technology Inc Device [1344:5404] (rev 03)
            Subsystem: Micron Technology Inc Device [1344:1100]
            Kernel driver in use: nvme
    03:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:1638] (rev c2)
            Subsystem: Hewlett-Packard Company Device [103c:8919]
            Kernel driver in use: amdgpu
            Kernel modules: amdgpu
    03:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:1637]
            Subsystem: Hewlett-Packard Company Device [103c:8919]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    03:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor [1022:15df]
            Subsystem: Hewlett-Packard Company Family 17h (Models 10h-1fh) Platform Security Processor [103c:8919]
            Kernel driver in use: ccp
    03:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir USB 3.1 [1022:1639]
            Subsystem: Hewlett-Packard Company Renoir USB 3.1 [103c:8919]
            Kernel driver in use: xhci_hcd
    03:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir USB 3.1 [1022:1639]
            Subsystem: Hewlett-Packard Company Renoir USB 3.1 [103c:8919]
            Kernel driver in use: xhci_hcd
    03:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/FireFlight/Renoir Audio Processor [1022:15e2] (rev 01)
            Subsystem: Hewlett-Packard Company Raven/Raven2/FireFlight/Renoir Audio Processor [103c:8919]
            Kernel modules: snd_pci_acp3x
    03:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller [1022:15e3]
            DeviceName: HD Audio Controller
            Subsystem: Hewlett-Packard Company Family 17h (Models 10h-1fh) HD Audio Controller [103c:8919]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    03:00.7 Signal processing controller [1180]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/Renoir Sensor Fusion Hub [1022:15e4]
            Subsystem: Hewlett-Packard Company Raven/Raven2/Renoir Sensor Fusion Hub [103c:891

### [lsusb]

`user `[`$`]`lsusb`

    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 002: ID 0bda:385a Realtek Semiconductor Corp. Bluetooth Radio
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 003: ID 0bda:8153 Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
    Bus 002 Device 002: ID 2109:0210 VIA Labs, Inc. Hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 005: ID 04f3:0c00 Elan Microelectronics Corp. ELAN:ARM-M4
    Bus 001 Device 003: ID 04f2:b6bb Chicony Electronics Co., Ltd HP Wide Vision HD Camera
    Bus 001 Device 004: ID 2109:0100 VIA Labs, Inc. USB 2.0 BILLBOARD
    Bus 001 Device 002: ID 2109:2210 VIA Labs, Inc. Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Devices]

### [Audio]

There are two audio cards:

`user `[`$`]`aplay -l`

    **** List of PLAYBACK Hardware Devices ****
    card 0: Generic [HD-Audio Generic], device 3: HDMI 0 [HDMI 0]
      Subdevices: 1/1
      Subdevice #0: subdevice #0
    card 1: Generic_1 [HD-Audio Generic], device 0: ALC287 Analog [ALC287 Analog]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

If the the default card should be the on-board audio, not the HDMI card, then create [\~/.asoundrc] as follows:

[FILE] **`~/.asoundrc`**

    defaults.pcm.!card Generic_1
    defaults.pcm.!device 0
    defaults.ctl.!card Generic_1

Alternatively put the same content in [/etc/asound.conf] for a system wide configuration.

### [Wireless network]

This laptop has Realtek 8852AE WiFi card, for which there are no drivers yet in Linux 5.10.61, the current stable version at the time of writing this document. To make it work follow the instructions in [this git repository](https://github.com/lwfinger/rtw89) to build a rtw89 module.

Note that this needs to be repeated whenever the kernel is rebuilt.

\

### [Bluetooth]

Bluetooth should be provided using the same Realtek 8852AE chip. There is [an issue for this](https://github.com/lwfinger/rtw89/issues/77) in the rtw89 github repository. It is not fixed, it is not working.

### [Display]

The display brightness can be set using [[[app-misc/brightnessctl]](https://packages.gentoo.org/packages/app-misc/brightnessctl)[]], available on [Project:GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU"), on a hardware level. Alternatively, [[[x11-apps/xrandr]](https://packages.gentoo.org/packages/x11-apps/xrandr)[]] can be used to set the brightness software level.

### [Keyboard]

The keyboard works out of the box. Function keys are not caught by the acpi deamon, but are silently passed to the desktop environment. Follow the instructions for your desktop environment if it needs tweaking, see the [i3 configuration settings](https://wiki.gentoo.org/wiki/I3#Enabling_multimedia_keys "I3") for an example. Note that if [[[app-misc/brightnessctl]](https://packages.gentoo.org/packages/app-misc/brightnessctl)[]] is used, it needs to have its suid set when called from an normal non-root user session.

### [Touchpad]

The Elan:ARM-M4 touchpad is finicky. It works most of the time using [[[sys-kernel/gentoo-kernel]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel)[]] without issues. It may be needed to reboot once or twice before it works.

## [External resources]

-   [Review on ultrabook.com](https://www.ultrabookreview.com/49926-hp-pavilion-aero-13-review)
-   [Review on The Verge](https://www.theverge.com/22632318/hp-pavilion-aero-13-2021-amd-review)