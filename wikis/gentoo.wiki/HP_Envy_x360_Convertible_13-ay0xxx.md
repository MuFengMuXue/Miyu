**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-envy-13-ay0000-x360-convertible-laptop-pc-series/32552483)

[[]][Specifications (by model)](https://support.hp.com/us-en/product/product-specs/hp-envy-13-ay0000-x360-convertible-laptop-pc-series/32552483)

[[]][Interactive Part Locator](https://h10032.www1.hp.com/ctg/Manual/c06584270.pdf)

[[]][Interactive LED Diagnostic](https://h10032.www1.hp.com/ctg/Manual/c06584271.pdf)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c06618429.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c06620975.pdf)

[[]][HP Envy](https://en.wikipedia.org/wiki/HP_Envy "wikipedia:HP Envy")

HP Envy x360 Convertible 13-ay0xxx is a series of 2-in-1 laptop devices released by Hewlett-Packard in 2020. The product line is equipped with AMD Ryzen 4000 series (codename \"Renoir\") mobile APU, which has been continuously receiving improvements on Linux hardware support from AMD.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Tested Hardware]](#Tested_Hardware)
    -   [[1.2] [Hardware Details]](#Hardware_Details)
    -   [[1.3] [Firmware]](#Firmware)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Portage settings]](#Portage_settings)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Laptop does not wake up from suspend when lid is opened]](#Laptop_does_not_wake_up_from_suspend_when_lid_is_opened)
    -   [[3.2] [GRUB boot entry in UEFI firmware disappears]](#GRUB_boot_entry_in_UEFI_firmware_disappears)
-   [[4] [References]](#References)

## [Hardware]

### [Tested Hardware]

+--------------------+-------------------------------------------------------+--------+--------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| Device             | Make/model                                            | Status | Vendor ID / Product ID                     | Kernel driver(s) | Kernel version                                                                                                                                                                           | Notes                                                                                                                                                                                                                                                                                                                                                                                                                       |        |
+--------------------+-------------------------------------------------------+--------+--------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| APU                | AMD Ryzen 3 4300U with Radeon Graphics *or*\          | Works  | 1002:1636 for the integrated graphics card | amdgpu           | 5.16.11, 5.15.25^[\[1\]](#cite_note-AMD_C3_Optimizations_for_5.15-1)^ or newer recommended; tested working optimally in 5.13, mostly working in 5.10-5.12, 5.14-5.15.24, 5.16-5.16.10^A^ | Firmware from [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] recommended |        |
|                    | AMD Ryzen 5 4500U with Radeon Graphics *or*\          |        |                                            |                  |                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                             |        |
|                    | AMD Ryzen 7 4700U with Radeon Graphics                |        |                                            |                  |                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                             |        |
+--------------------+-------------------------------------------------------+--------+--------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| Webcam             | Chicony Electronics Co., Ltd HP Wide Vision HD Camera | Works  | 04f2:b6b6                                  | uvcvideo         | unknown, tested working in 5.10+                                                                                                                                                         | Hardware lens cap button on keyboard works                                                                                                                                                                                                                                                                                                                                                                                  |        |
+--------------------+-------------------------------------------------------+--------+--------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| Wireless           | Intel Corporation Wi-Fi 6 AX200                       | Works  | 8086:2723                                  | iwlwifi          | unknown, tested working in 5.10+                                                                                                                                                         | Requires firmware from [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]    |        |
+--------------------+-------------------------------------------------------+--------+--------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| Touch screen       | ELAN2514:00                                           | Works  | 04f3:2af1                                  | hid_multitouch   | unknown, tested working in 5.10+                                                                                                                                                         | Multi-touch and stylus both work                                                                                                                                                                                                                                                                                                                                                                                            |        |
+--------------------+-------------------------------------------------------+--------+--------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| Fingerprint reader | Synaptics, Inc                                        | No     | 06cb:00e7                                  | N/A              | N/A                                                                                                                                                                                      | Support in libfprint reverted at request of Synaptics^[\[2\]](#cite_note-libfprint_unsupported_device_wiki-2)^                                                                                                                                                                                                                                                                                                              |        |
+--------------------+-------------------------------------------------------+--------+--------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

^A^ This model supports *only* the [s2idle](https://www.kernel.org/doc/Documentation/power/states.txt) state (a.k.a. s0ix, [Modern Standby](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/modern-standby)) for system suspend. Prior to Linux 5.13, the kernel could not correctly enter or exit from s2idle, and the suspend functionality was mostly broken on this model^[\[3\]](#cite_note-3)^. In Linux 5.13, the issue was fixed, and the suspend functionality worked without any significant issues. Linux 5.14 introduced a regression in the suspend functionality where the laptop would not resume from suspend after the lid had been opened^[\[4\]](#cite_note-4)^. In Linux 5.16.11 and 5.15.25, the regression was eventually fixed^[\[5\]](#cite_note-lid-wakeup-fix-5.16-5)[\[6\]](#cite_note-lid-wakeup-fix-5.15-6)^.

### [Hardware Details]

`root `[`#`]`lspci`

    00:00.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne Root Complex
    00:00.2 IOMMU: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne IOMMU
    00:01.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:01.3 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
    00:02.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:02.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
    00:02.3 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge
    00:08.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge
    00:08.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus
    00:14.0 SMBus: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller (rev 51)
    00:14.3 ISA bridge: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge (rev 51)
    00:18.0 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 0
    00:18.1 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 1
    00:18.2 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 2
    00:18.3 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 3
    00:18.4 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 4
    00:18.5 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 5
    00:18.6 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 6
    00:18.7 Host bridge: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 7
    01:00.0 Network controller: Intel Corporation Wi-Fi 6 AX200 (rev 1a)
    02:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader (rev 01)
    03:00.0 Non-Volatile memory controller: KIOXIA Corporation Device 0001
    04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir (rev c2)
    04:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller
    04:00.2 Encryption controller: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor
    04:00.3 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
    04:00.4 USB controller: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1
    04:00.5 Multimedia controller: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/FireFlight/Renoir Audio Processor (rev 01)
    04:00.6 Audio device: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller
    04:00.7 Signal processing controller: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/Renoir Sensor Fusion Hub

`root `[`#`]`lsusb`

    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 002: ID 8087:0029 Intel Corp. AX200 Bluetooth
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 04f2:b6b6 Chicony Electronics Co., Ltd HP Wide Vision HD Camera
    Bus 001 Device 002: ID 06cb:00e7 Synaptics, Inc.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [Firmware]

Tested with firmware version F.20.

## [Configuration]

### [Portage settings]

[FILE] **`/etc/portage/make.conf`Suggested Portage settings**

    VIDEO_CARDS="amdgpu radeonsi"
    CPU_FLAGS_X86="aes avx avx2 f16c fma3 mmx mmxext pclmul popcnt rdrand sha sse sse2 sse3 sse4_1 sse4_2 sse4a ssse3"
    ALSA_CARDS="hda-intel"

## [Troubleshooting]

### [Laptop does not wake up from suspend when lid is opened]

This was an issue in the Linux kernel that has been fixed in 5.16.11^[\[5\]](#cite_note-lid-wakeup-fix-5.16-5)^ and 5.15.25^[\[6\]](#cite_note-lid-wakeup-fix-5.15-6)^. To resolve the problem, please upgrade to one of those patched versions, which include Linux 5.16.11, 5.15.25, and above.

Alternatively, apply the [patch](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/patch/?id=0c430ff95116c4a635e651d9be9e4e8e1163bc5d) containing the fix to the sources of an older kernel. If a kernel sources package like [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] or a [distribution kernel](https://wiki.gentoo.org/wiki/Project:Distribution_Kernel "Project:Distribution Kernel") package that *builds a kernel from source* is being used, the patch can be added to [[/etc/portage/patches]](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches"), so it can be applied automatically.

** Important**\
[[[sys-kernel/gentoo-kernel-bin]](https://packages.gentoo.org/packages/sys-kernel/gentoo-kernel-bin)[]] users must either upgrade to one of those patched versions to install a kernel that incorporates the patch or switch to another non-binary kernel package for the ability to build an older kernel with the patch applied locally.

** Important**\
When the kernel is being upgraded to one of those patched versions later, the patch under [/etc/portage/patches] must be removed to avoid patch failure.

### [GRUB boot entry in UEFI firmware disappears]

If GRUB is installed (e.g. via [grub-install]) to the laptop\'s internal disk when the disk contains a Microsoft Windows installation, then after the laptop has been rebooted a few times (typically three times), the UEFI firmware may remove GRUB\'s boot entry of its own accord.

This problem seems to be caused by some hardcoded, non-configurable logic in the UEFI firmware that automatically recreates a boot entry for any detected Windows installation on the internal disk. Such logic has a side effect of removing non-Windows boot entries.

To fix this problem, please follow these steps:

1.  Boot into Windows, then start Windows PowerShell or Command Prompt as administrator.
2.  Run this command:

    :::: cmd-box


    `>``bcdedit /set '' path \EFI\Boot\bootx64.efi`


    ::::
3.  Disconnect all external bootable storage devices from the laptop.
4.  Restart the laptop, and keep pressing [F9] until the screen displays \"F9\...Change Boot Device Order\" on the bottom-left corner.
5.  Start GRUB from the displayed menu.
    1.  Select \"Boot from EFI File\".
    2.  Select the only option on the next screen, which corresponds to the internal disk\'s EFI system partition.
    3.  Navigate to the GRUB EFI file ([grubx64.efi]) on the EFI system partition. By default, the file\'s path is [EFI/gentoo/grubx64.efi].
    4.  Select this file to start GRUB.
6.  Boot into Gentoo from GRUB.
7.  Reinstall GRUB under Gentoo: [GRUB#Installing_GRUB_for_EFI](https://wiki.gentoo.org/wiki/GRUB#Installing_GRUB_for_EFI "GRUB").
8.  Restart the laptop three times. If GRUB\'s boot entry does not disappear after the restarts, then the problem has been fixed successfully.

## [References]

1.  [[[↑](#cite_ref-AMD_C3_Optimizations_for_5.15_1-0)] [[https://www.phoronix.com/scan.php?page=news_item&px=AMD-C3-Optimize-Linux-5.15](https://www.phoronix.com/scan.php?page=news_item&px=AMD-C3-Optimize-Linux-5.15)]]
2.  [[[↑](#cite_ref-libfprint_unsupported_device_wiki_2-0)] [[https://gitlab.freedesktop.org/libfprint/wiki/-/wikis/Unsupported-Devices](https://gitlab.freedesktop.org/libfprint/wiki/-/wikis/Unsupported-Devices)]]
3.  [[[↑](#cite_ref-3)] [[https://gitlab.freedesktop.org/drm/amd/-/issues/1230#note_638991](https://gitlab.freedesktop.org/drm/amd/-/issues/1230#note_638991)]]
4.  [[[↑](#cite_ref-4)] [[https://gitlab.freedesktop.org/drm/amd/-/issues/1691#note_1042077](https://gitlab.freedesktop.org/drm/amd/-/issues/1691#note_1042077)]]
5.  [[↑ ^[5.0](#cite_ref-lid-wakeup-fix-5.16_5-0)^ ^[5.1](#cite_ref-lid-wakeup-fix-5.16_5-1)^] [[https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?h=v5.16.11&id=0c430ff95116c4a635e651d9be9e4e8e1163bc5d](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?h=v5.16.11&id=0c430ff95116c4a635e651d9be9e4e8e1163bc5d)]]
6.  [[↑ ^[6.0](#cite_ref-lid-wakeup-fix-5.15_6-0)^ ^[6.1](#cite_ref-lid-wakeup-fix-5.15_6-1)^] [[https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?h=v5.15.25&id=0044583276952621822022b6ff8f5dc54c246f9a](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/commit/?h=v5.15.25&id=0044583276952621822022b6ff8f5dc54c246f9a)]]