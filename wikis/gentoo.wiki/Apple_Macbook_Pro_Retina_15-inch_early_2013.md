[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

These instructions cover the Macbook Pro with Retina Display, 15\" model. This model has both an [Intel](https://wiki.gentoo.org/wiki/Intel "Intel") and an NVIDIA graphics card. It has the model code 10,1.

You must use rEFInd with this setup.

## Contents

-   [[1] [lspci and lsusb]](#lspci_and_lsusb)
-   [[2] [Driver settings]](#Driver_settings)
-   [[3] [Intel and Nouveau graphic drivers]](#Intel_and_Nouveau_graphic_drivers)
    -   [[3.1] [Intel graphics card use cases]](#Intel_graphics_card_use_cases)
-   [[4] [Proprietary NVIDIA graphic drivers]](#Proprietary_NVIDIA_graphic_drivers)
    -   [[4.1] [NVIDIA graphics card use cases]](#NVIDIA_graphics_card_use_cases)

## [lspci and lsusb]

The output from the [lspci -nn] command:

`root `[`#`]`lspci -nn`

     00:00.0 Host bridge [0600]: Intel Corporation 3rd Gen Core processor DRAM Controller [8086:0154] (rev 09)
     00:01.0 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port [8086:0151] (rev 09)
     00:01.1 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port [8086:0155] (rev 09)
     00:01.2 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port [8086:0159] (rev 09)
     00:02.0 VGA compatible controller [0300]: Intel Corporation 3rd Gen Core processor Graphics Controller [8086:0166] (rev 09)
     00:14.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller [8086:1e31] (rev 04)
     00:16.0 Communication controller [0780]: Intel Corporation 7 Series/C210 Series Chipset Family MEI Controller #1 [8086:1e3a] (rev 04)
     00:1a.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2 [8086:1e2d] (rev 04)
     00:1b.0 Audio device [0403]: Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller [8086:1e20] (rev 04)
     00:1c.0 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 1 [8086:1e10] (rev c4)
     00:1c.1 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 2 [8086:1e12] (rev c4)
     00:1d.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1 [8086:1e26] (rev 04)
     00:1f.0 ISA bridge [0601]: Intel Corporation HM77 Express Chipset LPC Controller [8086:1e57] (rev 04)
     00:1f.2 SATA controller [0106]: Intel Corporation 7 Series Chipset Family 6-port SATA Controller [AHCI mode] [8086:1e03] (rev 04)
     00:1f.3 SMBus [0c05]: Intel Corporation 7 Series/C210 Series Chipset Family SMBus Controller [8086:1e22] (rev 04)
     01:00.0 VGA compatible controller [0300]: NVIDIA Corporation Device [10de:0fd5] (rev a1)
     01:00.1 Audio device [0403]: NVIDIA Corporation GK107 HDMI Audio Controller [10de:0e1b] (rev a1)
     03:00.0 Ethernet controller [0200]: Broadcom Corporation Device [14e4:16a3] (rev 10)
     03:00.1 SD Host controller [0805]: Broadcom Corporation NetXtreme BCM57765 Memory Card Reader [14e4:16bc] (rev 10)
     04:00.0 Network controller [0280]: Broadcom Corporation BCM4331 802.11a/b/g/n [14e4:4331] (rev 02)

The output from the [lsusb] command:

`root `[`#`]`lsusb`

     Bus 002 Device 005: ID 05ac:0262 Apple, Inc.
     Bus 002 Device 008: ID 05ac:8286 Apple, Inc.
     Bus 002 Device 004: ID 0a5c:4500 Broadcom Corp. BCM2046B1 USB 2.0 Hub (part of BCM2046 Bluetooth)
     Bus 002 Device 003: ID 0424:2512 Standard Microsystems Corp. USB 2.0 Hub
     Bus 001 Device 003: ID 05ac:8510 Apple, Inc.
     Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
     Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
     Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
     Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
     Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
     Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Driver settings]

First, while using Mac OSX, download GfxCardStatus version 2.2.1 (not 2.1 or 2.3+, it need to be 2.2.1) and select integrated graphics. This step is very important as it will allow you disable the NVIDIA card, allowing the Intel one to work. This is the only way to get the Intel card to work until vga_switcheroo fixes this.

You have can either use the open source graphic drivers (Intel 915 or [Nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau")) OR the NVIDIA proprietary graphic drivers.

## [Intel and Nouveau graphic drivers]

If you are going open source, it is strongly advised that you configure both drivers, even if you only plan on using one. This is because installing both into the kernel allows you to use vga_switcheroo. This will, at the very least, allow you to turn the one you are not using off to save power.

If you had previously used the proprietary NVIDIA driver you will need to uninstall it complete in order for everything to work as intended.

Follow the setup for both Intel and Nouveau on the wiki, compiling both directly into the kernel. Also, set up [vga_switcheroo](https://archive.is/ofeBp).

You can use [Hprofile](https://wiki.gentoo.org/wiki/Hprofile "Hprofile") to swap between Intel and Nouveau configurations seamlessly. Note however that it does not appear possible (at the moment) to switch from NVIDIA to Intel without rebooting into OSX using the latest 3.14 kernel.

TO DO: add hprofile settings.

### [Intel graphics card use cases]

Use the Intel graphics card when you are going for long durations without AC power. You\'ll have to boot into OSX and use gfxCardStatus to force Intel graphics, then use vga_switcheroo to power off the NVIDIA card.

Unfortunately, the Intel card does not support multiple displays. If you don\'t need multiple displays (you don\'t have a docking station) the Intel card is recommended as it provides better battery life.

## [Proprietary NVIDIA graphic drivers]

Setup here is a lot simpler, but the driver support is really sketchy. If you use this, you can\'t control the built in display\'s backlight; stopping the x server will result in a black screen requiring a reboot. You will also not be able to suspend/resume your system until after the reboot.

Use kernel 3.9 with nvidia-drivers-319.17. Later kernel versions or graphics card versions don\'t seem to work. You must add \"nomodeset\" to your kernel command line.

Basically, just follow the normal instructions for setting up NVIDIA graphics [drivers](https://wiki.gentoo.org/wiki/NVIDIA/nvidia-drivers "NVIDIA/nvidia-drivers"), and make sure all the open source drivers are disabled.

### [NVIDIA graphics card use cases]

Use the NVIDIA card if you need to use multiple displays. The ZaphodHeads feature can be used, or you can simply use [xrandr].