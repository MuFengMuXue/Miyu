\
Apple\'s Mid 2010 13\" MacBook Pro (model code 7,1) is capable of installing and running Gentoo Linux. Installation and configuration is decently easy, especially when these types of guides are available!

## Contents

-   [[1] [Installation media]](#Installation_media)
-   [[2] [Hardware]](#Hardware)
    -   [[2.1] [lspci]](#lspci)
    -   [[2.2] [lsusb]](#lsusb)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Kernel]](#Kernel)
    -   [[3.2] [Wireless drivers]](#Wireless_drivers)
-   [[4] [Tips]](#Tips)
    -   [[4.1] [Detection tools]](#Detection_tools)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation media]

This computer is capable of an EFI only install. This is made possible via booting from EFI media. Some users have reported rEFInd was needed to get EFI working properly, however this did not appear to be the case for this system. It should be able to boot off of any EFI enabled media.

To boot to a LiveCD or LiveDVD put the disk into the DVD drive and reboot the system. Press and hold the [option] ([alt]) key at the beginning of the boot process (before the sound plays). Continue holding the key until a mouse pointer appears. The DVD drive should be making some noises. Eventually (around a minute) two boot options should appear. Select the DVD drive.

** Note**\
When using SystemRescueCD, if a black GRUB2 screen appears then the system is booting via EFI firmware. If a blue screen appears SysLinux screen appears, then it is not booting via EFI and the system will be unable to load `efivars` into the kernel.

For further installation instructions see the [AMD64 Handbook](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64"). Refer to some of the configuration instructions in the lower sections of this article for help with specific device setup and kernel configuration.

## [Hardware]

### [lspci]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: NVIDIA Corporation MCP89 HOST Bridge [10de:0d60] (rev a1)
    00:00.1 RAM memory [0500]: NVIDIA Corporation MCP89 Memory Controller [10de:0d68] (rev a1)
    00:01.0 RAM memory [0500]: NVIDIA Corporation Device [10de:0d6d] (rev a1)
    00:01.1 RAM memory [0500]: NVIDIA Corporation Device [10de:0d6e] (rev a1)
    00:01.2 RAM memory [0500]: NVIDIA Corporation Device [10de:0d6f] (rev a1)
    00:01.3 RAM memory [0500]: NVIDIA Corporation Device [10de:0d70] (rev a1)
    00:02.0 RAM memory [0500]: NVIDIA Corporation Device [10de:0d71] (rev a1)
    00:02.1 RAM memory [0500]: NVIDIA Corporation Device [10de:0d72] (rev a1)
    00:03.0 ISA bridge [0601]: NVIDIA Corporation MCP89 LPC Bridge [10de:0d80] (rev a2)
            Subsystem: Apple Inc. MCP89 LPC Bridge [106b:cb89]
    00:03.1 RAM memory [0500]: NVIDIA Corporation MCP89 Memory Controller [10de:0d7b] (rev a1)
    00:03.2 SMBus [0c05]: NVIDIA Corporation MCP89 SMBus [10de:0d79] (rev a1)
            Subsystem: NVIDIA Corporation MCP89 SMBus [10de:cb89]
    00:03.3 RAM memory [0500]: NVIDIA Corporation MCP89 Memory Controller [10de:0d69] (rev a1)
    00:03.4 Co-processor [0b40]: NVIDIA Corporation MCP89 Co-Processor [10de:0d7a] (rev a1)
            Subsystem: NVIDIA Corporation MCP89 Co-Processor [10de:cb89]
    00:04.0 USB controller [0c03]: NVIDIA Corporation MCP89 OHCI USB 1.1 Controller [10de:0d9c] (rev a1)
            Subsystem: NVIDIA Corporation MCP89 OHCI USB 1.1 Controller [10de:cb89]
            Kernel driver in use: ohci-pci
    00:04.1 USB controller [0c03]: NVIDIA Corporation MCP89 EHCI USB 2.0 Controller [10de:0d9d] (rev a2)
            Subsystem: NVIDIA Corporation MCP89 EHCI USB 2.0 Controller [10de:cb89]
            Kernel driver in use: ehci-pci
    00:06.0 USB controller [0c03]: NVIDIA Corporation MCP89 OHCI USB 1.1 Controller [10de:0d9c] (rev a1)
            Subsystem: NVIDIA Corporation MCP89 OHCI USB 1.1 Controller [10de:cb89]
            Kernel driver in use: ohci-pci
    00:06.1 USB controller [0c03]: NVIDIA Corporation MCP89 EHCI USB 2.0 Controller [10de:0d9d] (rev a2)
            Subsystem: NVIDIA Corporation MCP89 EHCI USB 2.0 Controller [10de:cb89]
            Kernel driver in use: ehci-pci
    00:08.0 Audio device [0403]: NVIDIA Corporation MCP89 High Definition Audio [10de:0d94] (rev a2)
            Subsystem: NVIDIA Corporation MCP89 High Definition Audio [10de:cb89]
            Kernel driver in use: snd_hda_intel
    00:0a.0 SATA controller [0106]: NVIDIA Corporation MCP89 SATA Controller (AHCI mode) [10de:0d88] (rev a2)
            Subsystem: Apple Inc. MCP89 SATA Controller (AHCI mode) [106b:cb89]
            Kernel driver in use: ahci
    00:0b.0 RAM memory [0500]: NVIDIA Corporation Device [10de:0d75] (rev a1)
    00:0e.0 PCI bridge [0604]: NVIDIA Corporation Device [10de:0d9a] (rev a1)
            Kernel driver in use: pcieport
    00:15.0 PCI bridge [0604]: NVIDIA Corporation Device [10de:0d9b] (rev a1)
            Kernel driver in use: pcieport
    00:16.0 PCI bridge [0604]: NVIDIA Corporation Device [10de:0d9b] (rev a1)
            Kernel driver in use: pcieport
    00:17.0 PCI bridge [0604]: NVIDIA Corporation MCP89 PCI Express Bridge [10de:0d76] (rev a1)
    01:00.0 FireWire (IEEE 1394) [0c00]: LSI Corporation FW643 [TrueFire] PCIe 1394b Controller [11c1:5901] (rev 08)
            Subsystem: LSI Corporation FW643 [TrueFire] PCIe 1394b Controller [11c1:5900]
            Kernel driver in use: firewire_ohci
    02:00.0 Network controller [0280]: Broadcom Corporation BCM4322 802.11a/b/g/n Wireless LAN Controller [14e4:432b] (rev 01)
            Subsystem: Apple Inc. AirPort Extreme [106b:008d]
            Kernel driver in use: wl
            Kernel modules: wl
    03:00.0 Ethernet controller [0200]: Broadcom Corporation NetXtreme BCM5764M Gigabit Ethernet PCIe [14e4:1684] (rev 10)
            Subsystem: Broadcom Corporation NetXtreme BCM5764M Gigabit Ethernet PCIe [14e4:1684]
            Kernel driver in use: tg3
    04:00.0 VGA compatible controller [0300]: NVIDIA Corporation MCP89 [GeForce 320M] [10de:08a0] (rev a2)
            Subsystem: Apple Inc. MCP89 [GeForce 320M] [106b:00c2]
            Kernel driver in use: nouveau

### [lsusb]

`root `[`#`]`lsusb`

    Bus 002 Device 002: ID 05ac:8403 Apple, Inc. Internal Memory Card Reader
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 007: ID 05ac:820b Apple, Inc. Bluetooth HID Mouse
    Bus 004 Device 006: ID 05ac:820a Apple, Inc. Bluetooth HID Keyboard
    Bus 004 Device 005: ID 05ac:8213 Apple, Inc. Bluetooth Host Controller
    Bus 004 Device 004: ID 0a5c:4500 Broadcom Corp. BCM2046B1 USB 2.0 Hub (part of BCM2046 Bluetooth)
    Bus 004 Device 003: ID 05ac:8242 Apple, Inc. Built-in IR Receiver
    Bus 004 Device 002: ID 05ac:0236 Apple, Inc. Internal Keyboard/Trackpad (ANSI)
    Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
    Bus 001 Device 002: ID 05ac:8507 Apple, Inc. Built-in iSight
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub

## [Configuration]

### [Kernel]

Configuring the kernel for most recent MacBook systems is relatively simple. Specific kernel options can be viewed on the MacBook Pro Retina [Kernel Configuration](https://wiki.gentoo.org/wiki/Apple_Macbook_Pro_Retina#Kernel_Configuration "Apple Macbook Pro Retina") article. The writer of *this* article has verified the kernel options listed there will work for the 13-inch, Mid 2010 MacBook Pro with the exception of the iSight microphone driver which can be seen below:

[KERNEL] **iSight driver (`CONFIG_SND_ISIGHT`)**

    Device Drivers  --->
       <*> Sound card support  --->
          <*>   Advanced Linux Sound Architecture  --->
             [*]   FireWire sound devices  --->
                <*>   Apple iSight microphone

### [Wireless drivers]

See the [wireless driver section](https://wiki.gentoo.org/wiki/Apple_Macbook_Pro_Retina#Wireless "Apple Macbook Pro Retina") from the MacBook Pro Retina article for proper wireless driver configuration. The writer of *this* article has verified the kernel options listed there will work for the 13-inch, Mid 2010 MacBook Pro. There is no need to repeat them here.

## [Tips]

### [Detection tools]

Many [software tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") and [hardware detection utilities](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") are available in order to help administer and troubleshoot a new Gentoo installation. Users who are new to Gentoo have many options to choose from. Quite a few of the packages available in the Gentoo repository are utilities available on other Linux distributions.

## [See also]

-   [Apple Macbook Pro Retina (early 2013)](https://wiki.gentoo.org/wiki/Apple_Macbook_Pro_Retina_(early_2013) "Apple Macbook Pro Retina (early 2013)") - Instructions on how to install Gentoo on Apple\'s the 2013 line of MacBooks.
-   [Portage TMPDIR on tmpfs](https://wiki.gentoo.org/wiki/Portage_TMPDIR_on_tmpfs "Portage TMPDIR on tmpfs") - Instructions on how to build packages entirely in memory (RAM). This is useful for preserving read/write operations to a disk.
-   [Gentoo Cheat Sheet](https://wiki.gentoo.org/wiki/Gentoo_Cheat_Sheet "Gentoo Cheat Sheet") - A reference article for basic package management, USE flags, log file, and administration management.

## [External resources]

-   [https://support.apple.com/kb/sp583?locale=en_US](https://support.apple.com/kb/sp583?locale=en_US) - Apple\'s technical specifications page for this laptop.
-   [https://www.gentoo.org/downloads/](https://www.gentoo.org/downloads/) - Obtain a Minimal Installation CD from a Gentoo mirror.