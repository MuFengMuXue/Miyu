\
The Dell Inspiron 11 3000 (3195) is an 11\" 2-in-1 laptop (keyboard and touchscreen).

## [Hardware]

  ------------------ ------------------------------------------------------------ -------- -----------
  Device             Make/model                                                   Status   PCI IDs
  CPU (APU)          AMD A9-9420e Processor with Radeon(TM) R5 Graphics           Works
  SMBus Controller   FCH SMBus Controller                                         Works    1022:790b
  SATA               FCH SATA Controller \[AHCI mode\]                            Works    1022:7901
  Video / GPU        AMD/ATI Stoney Radeon R2/R3/R4/R5 Graphics                   Works    1002:98e4
  Touchscreen        ELAN Touchscreen                                             Works
  Touchpad           ?                                                            Works
  Audio              AMD Audio                                                    Works    1002:15b3
  Audio              AMD Family 15h (Models 60h-6fh) Audio Controller             Works    1022:157a
  Wireless           Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter   Works    168c:0036
  Bluetooth          0x0cf3 0xe005 Qualcomm Atheros Communications                Works
  Webcam             Vendor CNFHH46P34343016D440                                  Works
  Microphone                                                                      Works
  ------------------ ------------------------------------------------------------ -------- -----------

**Notes**:

-   The touchscreen works like a basic mouse, but does not seem to support multitouch (e.g. two-finger scrolling) in KDE. The touchpad has full multitouch functionality, though.
-   [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] is needed for Bluetooth functionality. Include the ar3k/\* firmwares. See [Linux_firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware"). See also [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") and [Bluetooth_headset](https://wiki.gentoo.org/wiki/Bluetooth_headset "Bluetooth headset").
-   Keyboard and touchpad are disabled (as expected) when screen is folded behind keyboard (to avoid unintended inputs when used in tablet form).

## [Extra hardware information]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 15h (Models 60h-6fh) Processor Root Complex [1022:1576]                         [6/19]
            Subsystem: Dell Family 15h (Models 60h-6fh) Processor Root Complex [1028:0944]
    lspci: Unable to load libkmod resources: error -12
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Family 15h (Models 60h-6fh) I/O Memory Management Unit [1022:1577]
            Subsystem: Dell Family 15h (Models 60h-6fh) I/O Memory Management Unit [1028:0944]
    00:01.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Stoney [Radeon R2/R3/R4/R5 Graphics] [1002:98e4] (rev ca)
            Subsystem: Dell Stoney [Radeon R2/R3/R4/R5 Graphics] [1028:0944]
    00:01.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:15b3]
            Subsystem: Dell Device [1028:0944]
            Kernel driver in use: snd_hda_intel
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 15h (Models 60h-6fh) Host Bridge [1022:157b]
    00:02.4 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 15h (Models 60h-6fh) Processor Root Port [1022:157c]
            Kernel driver in use: pcieport
    00:02.5 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Family 15h (Models 60h-6fh) Processor Root Port [1022:157c]
            Kernel driver in use: pcieport
    00:03.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Family 15h (Models 60h-6fh) Host Bridge [1022:157b]
    00:08.0 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Carrizo Platform Security Processor [1022:1578]
            Subsystem: Dell Carrizo Platform Security Processor [1028:0944]
    00:09.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Carrizo Audio Dummy Host Bridge [1022:157d]
    00:09.2 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 15h (Models 60h-6fh) Audio Controller [1022:157a]
            Subsystem: Dell Family 15h (Models 60h-6fh) Audio Controller [1028:0944]
            Kernel driver in use: snd_hda_intel
    00:10.0 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] FCH USB XHCI Controller [1022:7914] (rev 20)
            Subsystem: Dell FCH USB XHCI Controller [1028:0944]
            Kernel driver in use: xhci_hcd
    00:11.0 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 4b)
            Subsystem: Dell FCH SATA Controller [AHCI mode] [1028:0944]
            Kernel driver in use: ahci
    00:12.0 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] FCH USB EHCI Controller [1022:7908] (rev 49)
            Subsystem: Dell FCH USB EHCI Controller [1028:0944]
            Kernel driver in use: ehci-pci
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 4b)
            Subsystem: Dell FCH SMBus Controller [1028:0944]
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 11)
            Subsystem: Dell FCH LPC Bridge [1028:0944]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Stoney HT Configuration [1022:15b0]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Stoney Address Maps [1022:15b1]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Stoney DRAM Configuration [1022:15b2]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Stoney Miscellaneous Configuration [1022:15b3]
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Stoney PM Configuration [1022:15b4]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Stoney NB Performance Monitor [1022:15b5]
    01:00.0 SD Host controller [0805]: O2 Micro, Inc. Device [1217:8620] (rev 01)
            Subsystem: Dell Device [1028:0944]
            Kernel driver in use: sdhci-pci
    04:00.0 Network controller [0280]: Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter [168c:0036] (rev 01)
            Subsystem: Dell QCA9565 / AR9565 Wireless Network Adapter [1028:020e]
            Kernel driver in use: ath9k

## [Installation]

Follow [Handbook:AMD64](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") and [AMDGPU](https://wiki.gentoo.org/wiki/AMDGPU "AMDGPU").

The initramfs step in the Handbook is marked optional, but for this laptop, it is required, or the main disk (/dev/mmcblk0) will not be visible at boot time, and the VFS will die, unable to read the root partition.