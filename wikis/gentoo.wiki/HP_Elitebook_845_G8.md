[] This article is a **work in progress**; treat its contents with caution - [KrissN](https://wiki.gentoo.org/index.php?title=User:KrissN&action=edit&redlink=1 "User:KrissN (page does not exist)") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:KrissN&action=edit&redlink=1 "User talk:KrissN (page does not exist)") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/KrissN "Special:Contributions/KrissN")).

**Resources**

[[]][Official Support Page](https://support.hp.com/us-en/product/details/hp-elitebook-845-g8-notebook-pc/38492638)

[[]][Specifications](https://support.hp.com/us-en/document/c07120411)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c07067671.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c06719950.pdf)

[[]][HP EliteBook](https://en.wikipedia.org/wiki/HP_EliteBook "wikipedia:HP EliteBook")

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Using M.2 SSD in WWAN NGFF slot]](#Using_M.2_SSD_in_WWAN_NGFF_slot)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [X11/Wayland graphics freezes]](#X11.2FWayland_graphics_freezes)
    -   [[3.2] [RTL8822CE Bluetooth adapter crashes]](#RTL8822CE_Bluetooth_adapter_crashes)
    -   [[3.3] [RTL8822CE Bluetooth refuses to pair devices]](#RTL8822CE_Bluetooth_refuses_to_pair_devices)
    -   [[3.4] [Suspend does not work]](#Suspend_does_not_work)

## [Hardware]

`root `[`#`]`lspci -nn`

    00:00.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne Root Complex [1022:1630]
    00:00.2 IOMMU [0806]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne IOMMU [1022:1631]
    00:01.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:01.3 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge [1022:1634]
    00:02.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:02.2 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge [1022:1634]
    00:02.4 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne PCIe GPP Bridge [1022:1634]
    00:08.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Renoir PCIe Dummy Host Bridge [1022:1632]
    00:08.1 PCI bridge [0604]: Advanced Micro Devices, Inc. [AMD] Renoir Internal PCIe GPP Bridge to Bus [1022:1635]
    00:14.0 SMBus [0c05]: Advanced Micro Devices, Inc. [AMD] FCH SMBus Controller [1022:790b] (rev 51)
    00:14.3 ISA bridge [0601]: Advanced Micro Devices, Inc. [AMD] FCH LPC Bridge [1022:790e] (rev 51)
    00:18.0 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 0 [1022:166a]
    00:18.1 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 1 [1022:166b]
    00:18.2 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 2 [1022:166c]
    00:18.3 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 3 [1022:166d]
    00:18.4 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 4 [1022:166e]
    00:18.5 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 5 [1022:166f]
    00:18.6 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 6 [1022:1670]
    00:18.7 Host bridge [0600]: Advanced Micro Devices, Inc. [AMD] Cezanne Data Fabric; Function 7 [1022:1671]
    01:00.0 Network controller [0280]: Realtek Semiconductor Co., Ltd. RTL8822CE 802.11ac PCIe Wireless Network Adapter [10ec:c822]
    02:00.0 USB controller [0c03]: Renesas Technology Corp. uPD720202 USB 3.0 Host Controller [1912:0015] (rev 02)
    03:00.0 Non-Volatile memory controller [0108]: Samsung Electronics Co Ltd NVMe SSD Controller PM9A1/PM9A3/980PRO [144d:a80a]
    04:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne [1002:1638] (rev d2)
    04:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Renoir Radeon High Definition Audio Controller [1002:1637]
    04:00.2 Encryption controller [1080]: Advanced Micro Devices, Inc. [AMD] Family 17h (Models 10h-1fh) Platform Security Processor [1022:15df]
    04:00.3 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1 [1022:1639]
    04:00.4 USB controller [0c03]: Advanced Micro Devices, Inc. [AMD] Renoir/Cezanne USB 3.1 [1022:1639]
    04:00.5 Multimedia controller [0480]: Advanced Micro Devices, Inc. [AMD] ACP/ACP3X/ACP6x Audio Coprocessor [1022:15e2] (rev 01)
    04:00.6 Audio device [0403]: Advanced Micro Devices, Inc. [AMD] Family 17h/19h HD Audio Controller [1022:15e3]

`root `[`#`]`lsusb`

    Bus 006 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 005 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 004: ID 0bda:0411 Realtek Semiconductor Corp. Hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 004: ID 06cb:00f0 Synaptics, Inc.
    Bus 003 Device 003: ID 0bda:b00c Realtek Semiconductor Corp. 802.11ac WLAN Adapter
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 002: ID 0408:5347 Quanta Computer, Inc. HP HD Camera
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [Standard]

  ----------------------------- ---------------------------------------------------------------------------------- -------------- ------------------------ ------------------ ---------------- ------------------------------------------------------------------------------
  Device                        Make/model                                                                         Status         Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  Video card                    Advanced Micro Devices, Inc. \[AMD/ATI\] Cezanne (rev d2)                          Works          \[1002:1638\]            amdgpu             ---              ---
  Wireless network controller   Realtek Semiconductor Co., Ltd. RTL8822CE 802.11ac PCIe Wireless Network Adapter   Works          \[10ec:c822\]            rtw_8822ce         ---              ---
  Bluetooth                     Realtek Semiconductor Corp. 802.11ac WLAN Adapter                                  Partial        \[0bda:b00c\]            btusb              ---              ---
  Web Camera                    Quanta Computer, Inc. HP HD Camera                                                 Works          \[0408:5347\]            uvcvideo           ---              ---
  Fingerprint Reader                                                                                               Not tested                              ---                ---              ---
  Touchpad                                                                                                         Not working                             ---                ---              Device not detected - probably missing some I2C bus driver in kernel config.
  ----------------------------- ---------------------------------------------------------------------------------- -------------- ------------------------ ------------------ ---------------- ------------------------------------------------------------------------------

### [Using M.2 SSD in WWAN NGFF slot]

Although some laptops provide official or unofficial support for using a M.2 2242 B+E keyed SSD in the WWAN slot, this is not the case for this model according to both official HP statement and actual tests.

## [Installation]

[FILE] **`/etc/portage/make.conf`**

    COMMON_FLAGS="-march=znver3 -O2 -pipe"

[FILE] **`/etc/portage/package.use/00input`**

    */* INPUT_DEVICES: libinput synaptics

[FILE] **`/etc/portage/package.use/00video`**

    */* VIDEO_CARDS: -* amdgpu radeonsi

### [Firmware]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

  ----------------------------- -----------------------------------------------------
  Device                        Firmware files
  Video card                    amdgpu/green_sardine\_\*.bin
  Wireless network controller   rtw88/rtw8822c_fw.bin rtw88/rtw8822c_wow_fw.bin
  Bluetooth                     rtl_bt/rtl8822cu_fw.bin rtl_bt/rtl8822cu_config.bin
  ----------------------------- -----------------------------------------------------

### [Kernel]

[KERNEL] **General**

    Processor type and features  --->
       Processor family (AMD Zen 3)  --->
       [*] CPU microcode loading support
       [*]   AMD microcode loading support
       [*] AMD Secure Memory Encryption (SME) support
       [ ]   Activate AMD Secure Memory Encryption (SME) by default
       [*] EFI runtime service support

[KERNEL] **NVME block device**

    Device Drivers  --->
           NVME Support  --->
          <*> NVM Express block device

Building the following device driver as module may be appropriate as it requires firmware during initialization.

[KERNEL] **Wireless network controller**

    Generic Driver Options  --->
       [*] Network device support  ---
          [*]   Wireless LAN  --->
             [*]   Realtek devices
             <*>     Realtek 802.11ac wireless chips support  --->
                <*>   Realtek 8822CE PCI wireless network adapter

Building the following device driver as module may be appropriate as it requires firmware during initialization.

[KERNEL] **Bluetooth device**

    Networking Support  --->
       <*> Bluetooth subsystem support  --->
          <*>   Bluetooth device drivers  --->
             <M>   HCI USB driver  --->
             [*]   Realtek protocol support

[KERNEL] **Audio device**

    Device Drivers  --->
       <*> Sound card support  --->
          <*>   Advanced Linux Sound Architecture  --->
             [*]   PCI sound devices  --->
                   HD-Audio  --->
                      <*> HD Audio PCI
                      <*> Build Realtek HD-audio codec support

[KERNEL] **Web camera**

    Device Drivers  --->
       <*> Multimedia support  --->
                Media Device Types  --->
             [*] Cameras and video grabbers
                Media drivers  -->
             [*] Media USB Adapters  --->
                   <*>   USB Video Class (UVC)

## [Troubleshooting]

### [][X11/Wayland graphics freezes]

AMDGPU driver is known not to work correctly with AMD Secure Memory Encryption (SME). Until proper support is implemented SME needs to be disabled either:

-   by enabling the CONFIG_AMD_MEM_ENCRYPT kernel option and
    -   making sure CONFIG_AMD_MEM_ENCRYPT_ACTIVE_BY_DEFAULT is not selected, or
    -   setting mem_encrypt=off in the kernel command line
-   by disabling SME in BIOS Setup

### [RTL8822CE Bluetooth adapter crashes]

The RTL8822CE is a WiFi/Bluetooth combo adapter. The Bluetooth part is available on the USB bus of the NGFF interface and is visible as a USB Bluetooth adapter.

Unfortunately the error handling inside the adapter hardware is not very resilient. In case when some communication error between the hardware and kernel driver occurs (e.g. a timeout or state machine lockup) the Bluetooth adapter is know to crash and as a result the device is kicked out of the USB bus. There is no way to recover from this situation other than a reboot. The WiFi part of the RTL8822CE works fine.

This is especially visible with kernel 5.17, which has a known bug in the Bluetooth stack, but on newer kernels it is also possible to get this to occur, although much less frequently. While such communication issues are known to also occur with adapters from other vendors, their HW is designed in a way that the Bluetooth part is able to reset itself and recover.

If you require stable Bluetooth operation it is best to avoid the RTL8822CE adapter and switch to using an Intel adapter, which also works fine (I have personally successfully tested the Intel WiFi 8265).

### [RTL8822CE Bluetooth refuses to pair devices]

In case the Bluetooth adapter detects devices, but refuses to pair them, it may indicate that the adapter is missing firmware. Strangely enough the adapter is detected by the system and kernel driver and appears as if it was working fine, while actually not being able to function properly.

To fix the problem make sure the necessary firmware files are installed:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

When using an initrd it may be also necessary to copy them to the ramdisk.

### [Suspend does not work]

This laptop lacks support for classic S3 suspend and exclusively uses the newer S2idle state (a.k.a. modern suspend). Unfortunately this mode is poorly supported by the Linux kernel as of this time (kernel 5.18), especially for AMD hardware.

This means that the laptop either fails to enter suspend or has problems resuming from it.