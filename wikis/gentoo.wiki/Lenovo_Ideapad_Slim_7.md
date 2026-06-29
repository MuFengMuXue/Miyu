\
The IdeaPad Slim 7 is a Laptop released in 2020 with a Ryzen 4700U (Renoir) APU and 8GB of dual-channel memory. The hardware is generally well-supported by open-source drivers.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [lspci]](#lspci)
    -   [[1.3] [lsusb]](#lsusb)
    -   [[1.4] [i2cdetect]](#i2cdetect)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Corrupted or Silent Audio]](#Corrupted_or_Silent_Audio)
    -   [[3.2] [System fails to correctly resume from suspen-to-RAM]](#System_fails_to_correctly_resume_from_suspen-to-RAM)

## [Hardware]

### [Standard]

  -------------------- -------------------------------------------------------------------------------------- ------------ ------------------------ ------------------------- ---------------- ----------------------------------------------------------------------------
  Device               Make/model                                                                             Status       Vendor ID / Product ID   Kernel driver(s)          Kernel version   Notes
  CPU                  AMD Ryzen 7 4700U with Radeon Graphics                                                 Works        N/A                      N/A                       5.7-rc7          8 cores, 8 threads, Integrated GPU
  GPU                  Vega                                                                                   Works        1002:1636                amdgpu                    5.7-rc7          Tested with Mesa 20.2.0-devel
  Sound                Advanced Micro Devices, Inc. \[AMD\] Family 17h (Models 10h-1fh) HD Audio Controller   Works        1022:15e3                snd_hda_intel             5.7-rc7          See the note in the \"Troubleshooting\" section when dual-booting Windows.
  Wifi and Bluetooth   Intel Corporation Wi-Fi 6 AX200                                                        Works        8086:2723                iwlwifi                   5.7-rc7
  SD Card Reader       Realtek Semiconductor Corp.                                                            Works        0bda:0177                ums-realtek               5.7-rc7
  SMBus                Advanced Micro Devices, Inc. \[AMD\] FCH SMBus Controller                              Works        1022:790b                i2c_piix4, sp5100_tco     5.7-rc7
  Touchpad             Unknown                                                                                Works        1022:790b                i2c_hid, hid_multitouch   5.7-rc7
  I2C bus              Synopsys DesignWare I2C adapter                                                        Works                                 i2c-designware-pci        5.7-rc7          Required for the touchpad to work
  Webcam               Chicony Electronics Co., Ltd                                                           Works        04f2:b6cb                uvcvideo                  5.7-rc7
  Fingerprint Sensor   Elan Microelectronics Corp.                                                            No driver    04f3:0c4d
  -------------------- -------------------------------------------------------------------------------------- ------------ ------------------------ ------------------------- ---------------- ----------------------------------------------------------------------------

### [lspci]

`user `[`$`]`lspci -nn -k`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Root Complex [1022:1630]
        Subsystem: Lenovo Renoir Root Complex [17aa:380d]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Renoir IOMMU [1022:1631]
        Subsystem: Lenovo Renoir IOMMU [17aa:380d]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:02.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge [1022:1634]
        Kernel driver in use: pcieport
    00:02.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe GPP Bridge [1022:1634]
        Kernel driver in use: pcieport
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus [1022:1635]
        Kernel driver in use: pcieport
    00:08.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus [1022:1635]
        Kernel driver in use: pcieport
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 51)
        Subsystem: Lenovo FCH SMBus Controller [17aa:380d]
        Kernel driver in use: piix4_smbus
        Kernel modules: sp5100_tco
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
        Subsystem: Lenovo FCH LPC Bridge [17aa:380d]
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 0 [1022:1448]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 1 [1022:1449]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 2 [1022:144a]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 3 [1022:144b]
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 4 [1022:144c]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 5 [1022:144d]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 6 [1022:144e]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir Device 24: Function 7 [1022:144f]
    01:00.0 Network controller [0280]: Intel Corporation Wi-Fi 6 AX200 [8086:2723] (rev 1a)
        Subsystem: Intel Corporation Wi-Fi 6 AX200 [8086:0084]
        Kernel driver in use: iwlwifi
        Kernel modules: iwlwifi
    02:00.0 Non-Volatile memory controller [0108]: Sandisk Corp Device [15b7:5006]
        Subsystem: Sandisk Corp Device [15b7:5006]
        Kernel driver in use: nvme
    03:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Renoir [1002:1636] (rev c2)
        Subsystem: Lenovo Renoir [17aa:380d]
        Kernel driver in use: amdgpu
    03:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:1637]
        Subsystem: Lenovo Device [17aa:380d]
        Kernel driver in use: snd_hda_intel
    03:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor [1022:15df]
        Subsystem: Lenovo Family 17h (Models 10h-1fh) Platform Security Processor [17aa:380d]
    03:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir USB 3.1 [1022:1639]
        Subsystem: Lenovo Renoir USB 3.1 [17aa:380d]
        Kernel driver in use: xhci_hcd
    03:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir USB 3.1 [1022:1639]
        Subsystem: Lenovo Renoir USB 3.1 [17aa:380d]
        Kernel driver in use: xhci_hcd
    03:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/FireFlight/Renoir Audio Processor [1022:15e2] (rev 01)
        Subsystem: Lenovo Raven/Raven2/FireFlight/Renoir Audio Processor [17aa:380d]
    03:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) HD Audio Controller [1022:15e3]
        Subsystem: Lenovo Family 17h (Models 10h-1fh) HD Audio Controller [17aa:380d]
        Kernel driver in use: snd_hda_intel
    03:00.7 Signal processing controller [1180]: Advanced Micro Devices, Inc. [AMD] Raven/Raven2/Renoir Sensor Fusion Hub [1022:15e4]
        Subsystem: Lenovo Raven/Raven2/Renoir Sensor Fusion Hub [17aa:380d]
    04:00.0 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 81)
        Subsystem: Lenovo FCH SATA Controller [AHCI mode] [17aa:380d]
        Kernel driver in use: ahci
    04:00.1 SATA controller [0106]: Advanced Micro Devices, Inc. [AMD] FCH SATA Controller [AHCI mode] [1022:7901] (rev 81)
        Subsystem: Lenovo FCH SATA Controller [AHCI mode] [17aa:380d]
        Kernel driver in use: ahci

### [lsusb]

`user `[`$`]`lsusb`

    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 004: ID 8087:0029 Intel Corp.
    Bus 003 Device 003: ID 04f3:0c4d Elan Microelectronics Corp.
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 003: ID 04f2:b6cb Chicony Electronics Co., Ltd
    Bus 001 Device 007: ID 0bda:0177 Realtek Semiconductor Corp.
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [i2cdetect]

`root `[`#`]`i2cdetect -l`

    i2c-3    i2c         AMDGPU DM i2c hw bus 1              I2C adapter
    i2c-1   i2c         Synopsys DesignWare I2C adapter     I2C adapter
    i2c-8   smbus       SMBus PIIX4 adapter port 2 at 0b00  SMBus adapter
    i2c-6   i2c         AMDGPU DM aux hw bus 2              I2C adapter
    i2c-4   i2c         AMDGPU DM i2c hw bus 2              I2C adapter
    i2c-2   i2c         AMDGPU DM i2c hw bus 0              I2C adapter
    i2c-0   i2c         Synopsys DesignWare I2C adapter     I2C adapter
    i2c-7   smbus       SMBus PIIX4 adapter port 0 at 0b00  SMBus adapter
    i2c-5   i2c         AMDGPU DM aux hw bus 0              I2C adapter

## [Installation]

To access the UEFI BIOS menu, hold the F2 key while powering the system on. It may be necessary to disable secure boot to boot from the installation USB drive. To access the UEFI boot menu, hold the F12 key while the system powers on. This can also be useful when dual-booting with Windows.

There was nothing unusual about the installation process for this laptop. Be sure that the correct kernel options are enabled and that the GPU and wireless firmware are included.

### [Firmware]

All of the needed firmware is available in [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]].

    amdgpu/renoir_asd.bin
    amdgpu/renoir_me.bin
    amdgpu/renoir_rlc.bin
    amdgpu/renoir_ce.bin
    amdgpu/renoir_mec.bin
    amdgpu/renoir_sdma.bin
    amdgpu/renoir_dmcub.bin
    amdgpu/renoir_mec2.bin
    amdgpu/renoir_vcn.bin
    amdgpu/renoir_gpu_info.bin
    amdgpu/renoir_pfp.bin
    amd-ucode/microcode_amd_fam17h.bin
    iwlwifi-cc-a0-46.ucode

### [Kernel]

See the above list when filling in the \"Build named firmware blobs into the kernel binary\" section.

[KERNEL] **Enable support for these hardware drivers**

    Processor type and features  --->
      [*] Symmetric multi-processing support
        [*] AMD ACPI2Platform devices support
        [*] Machine Check / overheating reporting
        [*]   AMD MCE features
        [*] CPU microcode loading support
        [*]   AMD microcode loading support
        [*] EFI runtime service support
        [*]   EFI stub support
      Power management and ACPI options  --->
        [*] Energy Model for CPUs
        [*] ACPI (Advanced Configuration and Power Interface) Support  --->
        CPU Frequency scaling  --->
          <*>   ACPI Processor P-States driver
          <*>   AMD Opteron/Athlon64 PowerNow!
          <*>   AMD frequency sensitivity feedback powersave bias
    [*] Virtualization  --->
      <*>   Kernel-based Virtual Machine (KVM) support
      <*>   KVM for AMD processors support
    [*] Networking support  --->
      Wireless  --->
        <*>   cfg80211 - wireless configuration API
          [*]     enable powersave by default
          <*>   Generic IEEE 802.11 Networking Stack (mac80211)
    Device Drivers  --->
      Generic Driver Options  --->
        Firmware loader  --->
          (SEE THE LIST ABOVE) Build named firmware blobs into the kernel binary
          (/lib/firmware) Firmware blobs root directory
      [*] PCI support  --->
        [*]   PCI Express Port Bus support
      NVME Support  --->
        <*> NVM Express block device
        [*] NVMe multipath support
        <*> NVM Express over Fabrics FC host driver
        <*> NVMe Target support
        <*>   NVMe loopback device support
        <*>   NVMe over Fabrics FC target driver
      Misc devices  --->
        <*> Realtek USB card reader
      I2C support  --->
        [*]   ACPI I2C Operation region support
        <*>   I2C device interface
        <*>   I2C bus multiplexing support
        [*]   Autoselect pertinent helper modules
        I2C Hardware Bus support  --->
          <*> Intel PIIX4 and compatible (ATI/AMD/Serverworks/Broadcom/SMSC
          <*> SMBus Control Method Interface
          <*> Synopsys DesignWare Platform
          <*> Synopsys DesignWare PCI
      <*> Multimedia support  --->
      [*]   Cameras/video grabbers support
      [*]   Media USB Adapters  --->
        <*>   USB Video Class (UVC)
        [*]     UVC input events device support
        Graphics support  --->
        <*> AMD GPU
        [*]   Always enable userptr write support
        [*]   Allow GART access through debugfs
          ACP (Audio CoProcessor) Configuration  --->
            [*] Enable AMD Audio CoProcessor IP support
          Display Engine Configuration  --->
            [*] AMD DC - Enable new display engine
            [*] Enable HDCP support in DC
        [*]   HSA kernel driver for AMD GPU devices
      <*> Sound card support  --->
      <*>   Advanced Linux Sound Architecture  --->
        HD-Audio  --->
          <*> HD Audio PCI
          [*] Support initialization patch loading for HD-audio
          <*> Build Realtek HD-audio codec support
          <*> Build HDMI/DisplayPort HD-audio codec support
        (2048) Pre-allocated buffer size for HD-audio driver
      HID support  --->
        [*]   /dev/hidraw raw HID device support
        <*>   User-space I/O driver support for HID subsystem
        <*>   Generic HID driver
          USB HID support  --->
            <*> USB HID transport layer
            [*] PID device support
            [*] /dev/hiddev raw HID device support
        I2C HID support  --->
          <*> HID over I2C transport layer
      [*] USB support  --->
      <*>   xHCI HCD (USB 3.0) support
      <*>   EHCI HCD (USB 2.0) support
      [*]     Root Hub Transaction Translators
      [*]     Improved Transaction Translator scheduling
      <*>   OHCI HCD (USB 1.1) support
      <*>     OHCI support for PCI-bus USB controllers
      <*>   USB Mass Storage support
      <*>     Realtek Card Reader support
      [*]       Realtek Card Reader autosuspend support
      <*>   USB Type-C Support  --->
        <*>   USB Type-C Port Controller Manager
        <*>     Type-C Port Controller Interface driver
        <*>   USB Type-C Connector System Software Interface driver
        <*>     UCSI ACPI Interface Driver
        USB Type-C Alternate Mode drivers  --->
          <*> DisplayPort Alternate Mode driver
      <*> EDAC (Error Detection And Correction) reporting  --->
      <*>   Decode MCEs in human-readable form (only on AMD for now)
      <*>   AMD64 (Opteron, Athlon64)
      [*] X86 Platform Specific Device Drivers  --->
      <*>   Lenovo IdeaPad Laptop Extras
      [*] IOMMU Hardware Support  --->
      [*]   AMD IOMMU support
      <*>     AMD IOMMU Version 2 driver
      [*]   Support for Interrupt Remapping

## [Troubleshooting]

### [Corrupted or Silent Audio]

The laptop can get into a state where the speakers are silent and the headphone jack outputs a very unpleasant squealing sound. This is caused by booting into Windows and then rebooting the laptop into Linux. To fix this issue, power down the laptop and wait for roughly 30 seconds before turning it on again and then booting directly to Linux.

### [System fails to correctly resume from suspen-to-RAM]

This is still being investigated.