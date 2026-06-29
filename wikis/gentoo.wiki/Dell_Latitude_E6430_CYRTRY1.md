**Resources**

[[]][Official documentation](http://downloads.dell.com/manuals/all-products/esuprt_laptop/esuprt_latitude_laptop/latitude-e6430_owner%27s%20manual_en-us.pdf)

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [lspci]](#lspci)
    -   [[1.2] [lsinput]](#lsinput)
    -   [[1.3] [lshw]](#lshw)
    -   [[1.4] [lsusb]](#lsusb)
    -   [[1.5] [lscpu]](#lscpu)
    -   [[1.6] [Touchpad]](#Touchpad)
    -   [[1.7] [rfkill]](#rfkill)
    -   [[1.8] [Network interfaces]](#Network_interfaces)
    -   [[1.9] [Smartcard reader, Fingerprint reader]](#Smartcard_reader.2C_Fingerprint_reader)
-   [[2] [EFI Boot Stub quick\'n dirty]](#EFI_Boot_Stub_quick.27n_dirty)
-   [[3] [External resources]](#External_resources)

## [Hardware]

See [Linux Hardware Probe #4e38982788 of Dell Latitude E6430](https://linux-hardware.org/?probe=4e38982788)

  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------ ------------- --------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------
  Device               Make/model                                                                                                                                             Status        Vendor ID / Product ID                                                                        Kernel driver(s)                                                                                                      Notes
  CPU                  Intel [i7-3740QM](https://ark.intel.com/products/70847/Intel-Core-i7-3740QM-Processor-6M-Cache-up-to-3_70-GHz)         Works         N/A                                                                                           N/A                                                                                                                   \-
  SATA Controller      Intel Corporation 7 Series Chipset Family 6-port SATA Controller \[AHCI mode\]                                                                         Works         8086:1e03                                                                                     AHCI                                                                                                                  \-
  Video card           Intel Corporation 3rd Gen Core processor Graphics Controller                                                                                           Works         8086:0166                                                                                     [i915](https://wiki.gentoo.org/wiki/Intel "Intel")                                                                    \-
  Video card           [NVIDIA Corporation GF108GLM \[NVS 5200M\]](http://www.nvidia.com/object/nvs_techspecs.html)                           Not tested    10de:0dfc                                                                                     [nouveau](https://wiki.gentoo.org/wiki/Nouveau "Nouveau")                                                             \-
  Ethernet             Intel Corporation 82579LM Gigabit Network Connection                                                                                                   Works         [8086:1502](https://cateee.net/lkddb/web-lkddb/E1000E.html)   [e1000e](https://wiki.gentoo.org/index.php?title=E1000e&action=edit&redlink=1 "E1000e (page does not exist)")   \-
  WLAN                 [Intel Corporation Centrino Advanced-N 6205 \[Taylor Peak](https://linux-hardware.org/?id=pci:8086-0082-8086-1321)\]   Works         8086:0082                                                                                     [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")                                                             [iwldvm](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi?s%5b%5d=iwldvm#firmware)
  Touchpad             [AlpsPS/2 ALPS DualPoint TouchPad](https://wiki.gentoo.org/wiki/Alps_PS/2 "Alps PS/2")                                                                 Works         0002:0008                                                                                     MOUSE_PS2_ALPS                                                                                                        \-
  USB Controller       Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller                                                                         Works         8086:1e31                                                                                     xhci_hcd                                                                                                              \-
  USB Controller       Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2                                                                  Works         8086:1e2d                                                                                     ehci-pci                                                                                                              \-
  USB Controller       Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1                                                                  Works         8086:1e26                                                                                     ehci-pci                                                                                                              \-
  SD Host controller   O2 Micro, Inc. OZ600FJ0/OZ900FJ0/OZ600FJS SD/MMC Card Reader Controller                                                                                Works         1217:8221                                                                                     [sdhci_pci](https://cateee.net/lkddb/web-lkddb/MMC_SDHCI_PCI.html)                    \-
  WWAN                 [Dell wireless modem DW5560](https://wiki.gentoo.org/wiki/Dell_wireless_modem_DW5560 "Dell wireless modem DW5560")                       Not tested    413c:818e                                                                                     cdc_mbim                                                                                                              \-
  -------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------ ------------- --------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------

On the manufacturer\'s internet site the hardware components are listed on the [support page](http://www.dell.com/support/home/us/en/dedhs1/product-support/servicetag/CYRTRY1/configuration#subSectionB) in the Components section. Hardware detection shown below is done running the laptop under [SystemRescueCd-x86-5.0.0](https://www.system-rescue.org/Download/) in UEFI boot mode.

** Note**\
This computer\'s UEFI implementation seems to not support passing parameters from the NVRAM to an [EFI stub](https://wiki.gentoo.org/wiki/EFI_stub "EFI stub").

This computer provides a boot menu and a [configuration tool](https://philipyip.files.wordpress.com/2016/07/uefi1.png) for creating, sorting or deleting boot items. The content of the [ESP](https://wiki.gentoo.org/wiki/EFI_System_Partition "EFI System Partition") is visible to this tool and creating a boot item is like choosing the medium from a given selection, then surfing through the ESP and selecting the item, e.g `vmlinuz-4.9.16-gentoo.efi`.

Alternatively, [efibootmgr](https://wiki.gentoo.org/wiki/Efibootmgr "Efibootmgr") can be used for generating the UEFI boot items.

### [lspci]

`root `[`#`]`lspci -nnkv`

```
00:00.0 Host bridge [0600]: Intel Corporation 3rd Gen Core processor DRAM Controller [8086:0154] (rev 09)
    Subsystem: Dell 3rd Gen Core processor DRAM Controller [1028:0534]
    Flags: bus master, fast devsel, latency 0
    Capabilities: [e0] Vendor Specific Information: Len=0c <?>
    Kernel driver in use: ivb_uncore

00:01.0 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port [8086:0151] (rev 09) (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 26
    Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
    I/O behind bridge: 0000e000-0000efff
    Memory behind bridge: f5000000-f60fffff
    Prefetchable memory behind bridge: 00000000e0000000-00000000f1ffffff
    Capabilities: [88] Subsystem: Dell Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port [1028:0534]
    Capabilities: [80] Power Management version 3
    Capabilities: [90] MSI: Enable+ Count=1/1 Maskable- 64bit-
    Capabilities: [a0] Express Root Port (Slot+), MSI 00
    Capabilities: [100] Virtual Channel
    Capabilities: [140] Root Complex Link
    Capabilities: [d94] #19
    Kernel driver in use: pcieport
    Kernel modules: shpchp

00:02.0 VGA compatible controller [0300]: Intel Corporation 3rd Gen Core processor Graphics Controller [8086:0166] (rev 09) (prog-if 00 [VGA controller])
    Subsystem: Dell 3rd Gen Core processor Graphics Controller [1028:0534]
    Flags: bus master, fast devsel, latency 0, IRQ 31
    Memory at f6400000 (64-bit, non-prefetchable) [size=4M]
    Memory at d0000000 (64-bit, prefetchable) [size=256M]
    I/O ports at f000 [size=64]
    [virtual] Expansion ROM at 000c0000 [disabled] [size=128K]
    Capabilities: [90] MSI: Enable+ Count=1/1 Maskable- 64bit-
    Capabilities: [d0] Power Management version 2
    Capabilities: [a4] PCI Advanced Features
    Kernel driver in use: i915
    Kernel modules: i915

00:14.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB xHCI Host Controller [8086:1e31] (rev 04) (prog-if 30 [XHCI])
    Subsystem: Dell 7 Series/C210 Series Chipset Family USB xHCI Host Controller [1028:0534]
    Flags: bus master, medium devsel, latency 0, IRQ 28
    Memory at f7e20000 (64-bit, non-prefetchable) [size=64K]
    Capabilities: [70] Power Management version 2
    Capabilities: [80] MSI: Enable+ Count=1/8 Maskable- 64bit+
    Kernel driver in use: xhci_hcd

00:16.0 Communication controller [0780]: Intel Corporation 7 Series/C210 Series Chipset Family MEI Controller #1 [8086:1e3a] (rev 04)
    Subsystem: Dell 7 Series/C210 Series Chipset Family MEI Controller [1028:0534]
    Flags: bus master, fast devsel, latency 0, IRQ 32
    Memory at f7e3c000 (64-bit, non-prefetchable) [size=16]
    Capabilities: [50] Power Management version 3
    Capabilities: [8c] MSI: Enable+ Count=1/1 Maskable- 64bit+
    Kernel driver in use: mei_me
    Kernel modules: mei_me

00:19.0 Ethernet controller [0200]: Intel Corporation 82579LM Gigabit Network Connection [8086:1502] (rev 04)
    Subsystem: Dell 82579LM Gigabit Network Connection [1028:0534]
    Flags: bus master, fast devsel, latency 0, IRQ 29
    Memory at f7e00000 (32-bit, non-prefetchable) [size=128K]
    Memory at f7e39000 (32-bit, non-prefetchable) [size=4K]
    I/O ports at f080 [size=32]
    Capabilities: [c8] Power Management version 2
    Capabilities: [d0] MSI: Enable+ Count=1/1 Maskable- 64bit+
    Capabilities: [e0] PCI Advanced Features
    Kernel driver in use: e1000e
    Kernel modules: e1000e

00:1a.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2 [8086:1e2d] (rev 04) (prog-if 20 [EHCI])
    Subsystem: Dell 7 Series/C210 Series Chipset Family USB Enhanced Host Controller [1028:0534]
    Flags: bus master, medium devsel, latency 0, IRQ 16
    Memory at f7e38000 (32-bit, non-prefetchable) [size=1K]
    Capabilities: [50] Power Management version 2
    Capabilities: [58] Debug port: BAR=1 offset=00a0
    Capabilities: [98] PCI Advanced Features
    Kernel driver in use: ehci-pci

00:1b.0 Audio device [0403]: Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller [8086:1e20] (rev 04)
    Subsystem: Dell 7 Series/C210 Series Chipset Family High Definition Audio Controller [1028:0534]
    Flags: bus master, fast devsel, latency 0, IRQ 11
    Memory at f7e30000 (64-bit, non-prefetchable) [size=16K]
    Capabilities: [50] Power Management version 2
    Capabilities: [60] MSI: Enable- Count=1/1 Maskable- 64bit+
    Capabilities: [70] Express Root Complex Integrated Endpoint, MSI 00
    Capabilities: [100] Virtual Channel
    Capabilities: [130] Root Complex Link

00:1c.0 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 1 [8086:1e10] (rev c4) (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 16
    Bus: primary=00, secondary=02, subordinate=02, sec-latency=0
    Capabilities: [40] Express Root Port (Slot+), MSI 00
    Capabilities: [80] MSI: Enable- Count=1/1 Maskable- 64bit-
    Capabilities: [90] Subsystem: Dell 7 Series/C210 Series Chipset Family PCI Express Root Port 1 [1028:0534]
    Capabilities: [a0] Power Management version 2
    Kernel driver in use: pcieport
    Kernel modules: shpchp

00:1c.1 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 2 [8086:1e12] (rev c4) (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 17
    Bus: primary=00, secondary=03, subordinate=03, sec-latency=0
    Memory behind bridge: f7d00000-f7dfffff
    Capabilities: [40] Express Root Port (Slot+), MSI 00
    Capabilities: [80] MSI: Enable- Count=1/1 Maskable- 64bit-
    Capabilities: [90] Subsystem: Dell 7 Series/C210 Series Chipset Family PCI Express Root Port 2 [1028:0534]
    Capabilities: [a0] Power Management version 2
    Kernel driver in use: pcieport
    Kernel modules: shpchp

00:1c.2 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 3 [8086:1e14] (rev c4) (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 18
    Bus: primary=00, secondary=04, subordinate=07, sec-latency=0
    I/O behind bridge: 0000d000-0000dfff
    Memory behind bridge: f7200000-f7bfffff
    Prefetchable memory behind bridge: 00000000f2b00000-00000000f34fffff
    Capabilities: [40] Express Root Port (Slot+), MSI 00
    Capabilities: [80] MSI: Enable- Count=1/1 Maskable- 64bit-
    Capabilities: [90] Subsystem: Dell 7 Series/C210 Series Chipset Family PCI Express Root Port 3 [1028:0534]
    Capabilities: [a0] Power Management version 2
    Kernel driver in use: pcieport
    Kernel modules: shpchp

00:1c.3 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 4 [8086:1e16] (rev c4) (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 19
    Bus: primary=00, secondary=08, subordinate=0b, sec-latency=0
    I/O behind bridge: 0000c000-0000cfff
    Memory behind bridge: f6800000-f71fffff
    Prefetchable memory behind bridge: 00000000f2100000-00000000f2afffff
    Capabilities: [40] Express Root Port (Slot+), MSI 00
    Capabilities: [80] MSI: Enable- Count=1/1 Maskable- 64bit-
    Capabilities: [90] Subsystem: Dell 7 Series/C210 Series Chipset Family PCI Express Root Port 4 [1028:0534]
    Capabilities: [a0] Power Management version 2
    Kernel driver in use: pcieport
    Kernel modules: shpchp

00:1c.5 PCI bridge [0604]: Intel Corporation 7 Series/C210 Series Chipset Family PCI Express Root Port 6 [8086:1e1a] (rev c4) (prog-if 00 [Normal decode])
    Flags: bus master, fast devsel, latency 0, IRQ 17
    Bus: primary=00, secondary=0c, subordinate=0c, sec-latency=0
    Memory behind bridge: f7c00000-f7cfffff
    Capabilities: [40] Express Root Port (Slot+), MSI 00
    Capabilities: [80] MSI: Enable- Count=1/1 Maskable- 64bit-
    Capabilities: [90] Subsystem: Dell 7 Series/C210 Series Chipset Family PCI Express Root Port 6 [1028:0534]
    Capabilities: [a0] Power Management version 2
    Kernel driver in use: pcieport
    Kernel modules: shpchp

00:1d.0 USB controller [0c03]: Intel Corporation 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1 [8086:1e26] (rev 04) (prog-if 20 [EHCI])
    Subsystem: Dell 7 Series/C210 Series Chipset Family USB Enhanced Host Controller [1028:0534]
    Flags: bus master, medium devsel, latency 0, IRQ 21
    Memory at f7e37000 (32-bit, non-prefetchable) [size=1K]
    Capabilities: [50] Power Management version 2
    Capabilities: [58] Debug port: BAR=1 offset=00a0
    Capabilities: [98] PCI Advanced Features
    Kernel driver in use: ehci-pci

00:1f.0 ISA bridge [0601]: Intel Corporation QM77 Express Chipset LPC Controller [8086:1e55] (rev 04)
    Subsystem: Dell QM77 Express Chipset LPC Controller [1028:0534]
    Flags: bus master, medium devsel, latency 0
    Capabilities: [e0] Vendor Specific Information: Len=0c <?>
    Kernel driver in use: lpc_ich
    Kernel modules: lpc_ich

00:1f.2 SATA controller [0106]: Intel Corporation 7 Series Chipset Family 6-port SATA Controller [AHCI mode] [8086:1e03] (rev 04) (prog-if 01 [AHCI 1.0])
    Subsystem: Dell 7 Series Chipset Family 6-port SATA Controller [AHCI mode] [1028:0534]
    Flags: bus master, 66MHz, medium devsel, latency 0, IRQ 27
    I/O ports at f0d0 [size=8]
    I/O ports at f0c0 [size=4]
    I/O ports at f0b0 [size=8]
    I/O ports at f0a0 [size=4]
    I/O ports at f060 [size=32]
    Memory at f7e36000 (32-bit, non-prefetchable) [size=2K]
    Capabilities: [80] MSI: Enable+ Count=1/1 Maskable- 64bit-
    Capabilities: [70] Power Management version 3
    Capabilities: [a8] SATA HBA v1.0
    Capabilities: [b0] PCI Advanced Features
    Kernel driver in use: ahci

00:1f.3 SMBus [0c05]: Intel Corporation 7 Series/C210 Series Chipset Family SMBus Controller [8086:1e22] (rev 04)
    Subsystem: Dell 7 Series/C210 Series Chipset Family SMBus Controller [1028:0534]
    Flags: medium devsel, IRQ 18
    Memory at f7e35000 (64-bit, non-prefetchable) [size=256]
    I/O ports at f040 [size=32]
    Kernel driver in use: i801_smbus
    Kernel modules: i2c_i801

01:00.0 VGA compatible controller [0300]: NVIDIA Corporation GF108GLM [NVS 5200M] [10de:0dfc] (rev a1) (prog-if 00 [VGA controller])
    Subsystem: Dell GF108GLM [NVS 5200M] [1028:1534]
    Flags: bus master, fast devsel, latency 0, IRQ 30
    Memory at f5000000 (32-bit, non-prefetchable) [size=16M]
    Memory at e0000000 (64-bit, prefetchable) [size=256M]
    Memory at f0000000 (64-bit, prefetchable) [size=32M]
    I/O ports at e000 [size=128]
    Expansion ROM at f6000000 [disabled] [size=512K]
    Capabilities: [60] Power Management version 3
    Capabilities: [68] MSI: Enable+ Count=1/1 Maskable- 64bit+
    Capabilities: [78] Express Endpoint, MSI 00
    Capabilities: [b4] Vendor Specific Information: Len=14 <?>
    Capabilities: [100] Virtual Channel
    Capabilities: [128] Power Budgeting <?>
    Capabilities: [600] Vendor Specific Information: ID=0001 Rev=1 Len=024 <?>
    Kernel driver in use: nouveau
    Kernel modules: nouveau

03:00.0 Network controller [0280]: Intel Corporation Centrino Advanced-N 6205 [Taylor Peak] [8086:0082] (rev 34)
    Subsystem: Intel Corporation Centrino Advanced-N 6205 AGN [8086:1321]
    Flags: bus master, fast devsel, latency 0, IRQ 33
    Memory at f7d00000 (64-bit, non-prefetchable) [size=8K]
    Capabilities: [c8] Power Management version 3
    Capabilities: [d0] MSI: Enable+ Count=1/1 Maskable- 64bit+
    Capabilities: [e0] Express Endpoint, MSI 00
    Capabilities: [100] Advanced Error Reporting
    Capabilities: [140] Device Serial Number confidential
    Kernel driver in use: iwlwifi
    Kernel modules: iwlwifi

0c:00.0 SD Host controller [0805]: O2 Micro, Inc. OZ600FJ0/OZ900FJ0/OZ600FJS SD/MMC Card Reader Controller [1217:8221] (rev 05) (prog-if 01)
    Subsystem: Dell OZ600FJ0/OZ900FJ0/OZ600FJS SD/MMC Card Reader Controller [1028:0534]
    Flags: bus master, fast devsel, latency 0, IRQ 17
    Memory at f7c00000 (32-bit, non-prefetchable) [size=512]
    Capabilities: [a0] Power Management version 3
    Capabilities: [80] Express Endpoint, MSI 00
    Capabilities: [100] Virtual Channel
    Capabilities: [200] Advanced Error Reporting
    Kernel driver in use: sdhci-pci
    Kernel modules: sdhci_pci
```

### [lsinput]

`root `[`#`]`lsinput`

```
 0: 0000:0005 HOST   PNP0C0D/button/i Lid Switch               (null)
 1: 0000:0001 HOST   PNP0C0C/button/i Power Button             (null)
 2: 0000:0003 HOST   PNP0C0E/button/i Sleep Button             (null)
 3: 0000:0001 HOST   LNXPWRBN/button/ Power Button             (null)
 4: 0000:0006 HOST   LNXVIDEO/video/i Video Bus                (null)
 5: 0000:0006 HOST   LNXVIDEO/video/i Video Bus                (null)
 6: 0001:0001 I8042  isa0060/serio0/i AT Translated Set 2 keyb (null) (null) (null)
 7: 0000:0000 HOST                    Dell WMI hotkeys         (null) (null)
 8: 0000:0000 (null) ALSA             HDA Intel PCH Dock Mic   (null)
 9: 0000:0000 (null) ALSA             HDA Intel PCH Mic        (null)
10: 0000:0000 (null) ALSA             HDA Intel PCH Dock Line  (null)
11: 0000:0000 (null) ALSA             HDA Intel PCH Headphone  (null)
12: 062a:0001 USB    usb-0000:00:14.0 HID 062a:0001            (null) (null) (null)
13: 0002:0008 I8042  isa0060/serio1/i AlpsPS/2 ALPS DualPoint  (null) (null)
14: 0002:0008 I8042  isa0060/serio1/i AlpsPS/2 ALPS DualPoint  (null) (null)
15: 001f:0001 ISA    isa0061/input0   PC Speaker               (null)
```

### [lshw]

`root `[`#`]`lshw`

```
sysresccd
    description: Laptop
    product: Latitude E6430 (Latitude E6430)
    vendor: Dell Inc.
    version: 01
    serial: confidential
    width: 32 bits
    capabilities: smbios-2.7 dmi-2.7 smp-1.4 smp vsyscall32
    configuration: boot=normal chassis=laptop cpus=4 sku=Latitude E6430 uuid=confidential
  *-core
       description: Motherboard
       product: 0H3MT5
       vendor: Dell Inc.
       physical id: 0
       version: A00
       serial: confidential
     *-firmware
          description: BIOS
          vendor: Dell Inc.
          physical id: 0
          version: A20
          date: 01/04/2017
          size: 64KiB
          capacity: 13MiB
          capabilities: pci pnp upgrade shadowing cdboot bootselect socketedrom edd int13floppy1200 int13floppy720 int13floppy2880 int5printscreen int9keyboard int14serial int17printer acpi usb smartbattery biosbootspecification netboot uefi
     *-cpu:0
          description: CPU
          product: Intel(R) Core(TM) i7-3740QM CPU @ 2.70GHz
          vendor: Intel Corp.
          physical id: 54
          bus info: cpu@0
          version: 6.10.9
          serial: confidential
          slot: SOCKET 0
          size: 1247MHz
          capacity: 1247MHz
          width: 64 bits
          clock: 100MHz
          capabilities: x86-64 boot fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm epb tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms xsaveopt dtherm ida arat pln pts cpufreq
          configuration: cores=4 enabledcores=4 id=0 threads=8
        *-cache:0
             description: L2 cache
             physical id: 44
             slot: CPU Internal L2
             size: 1MiB
             capacity: 1MiB
             capabilities: internal write-through unified
        *-cache:1
             description: L1 cache
             physical id: 45
             slot: CPU Internal L1
             size: 256KiB
             capacity: 256KiB
             capabilities: internal write-through data
        *-cache:2
             description: L3 cache
             physical id: 46
             slot: CPU Internal L3
             size: 6MiB
             capacity: 6MiB
             capabilities: internal write-back unified
        *-logicalcpu:0
             description: Logical CPU
             physical id: 0.1
             width: 64 bits
             capabilities: logical
        *-logicalcpu:1
             description: Logical CPU
             physical id: 0.2
             width: 64 bits
             capabilities: logical
        *-logicalcpu:2
             description: Logical CPU
             physical id: 0.3
             width: 64 bits
             capabilities: logical
        *-logicalcpu:3
             description: Logical CPU
             physical id: 0.4
             width: 64 bits
             capabilities: logical
        *-logicalcpu:4
             description: Logical CPU
             physical id: 0.5
             width: 64 bits
             capabilities: logical
        *-logicalcpu:5
             description: Logical CPU
             physical id: 0.6
             width: 64 bits
             capabilities: logical
        *-logicalcpu:6
             description: Logical CPU
             physical id: 0.7
             width: 64 bits
             capabilities: logical
        *-logicalcpu:7
             description: Logical CPU
             physical id: 0.8
             width: 64 bits
             capabilities: logical
        *-logicalcpu:8
             description: Logical CPU
             physical id: 0.9
             width: 64 bits
             capabilities: logical
        *-logicalcpu:9
             description: Logical CPU
             physical id: 0.a
             width: 64 bits
             capabilities: logical
        *-logicalcpu:10
             description: Logical CPU
             physical id: 0.b
             width: 64 bits
             capabilities: logical
        *-logicalcpu:11
             description: Logical CPU
             physical id: 0.c
             width: 64 bits
             capabilities: logical
        *-logicalcpu:12
             description: Logical CPU
             physical id: 0.d
             width: 64 bits
             capabilities: logical
        *-logicalcpu:13
             description: Logical CPU
             physical id: 0.e
             width: 64 bits
             capabilities: logical
        *-logicalcpu:14
             description: Logical CPU
             physical id: 0.f
             width: 64 bits
             capabilities: logical
        *-logicalcpu:15
             description: Logical CPU
             physical id: 0.10
             width: 64 bits
             capabilities: logical
     *-memory
          description: System Memory
          physical id: 47
          slot: System board or motherboard
          size: 16GiB
        *-bank:0
             description: SODIMM DDR3 Synchronous 1600 MHz (0.6 ns)
             product: M471B1G73DB0-YK0
             vendor: Samsung
             physical id: 0
             serial: confidential
             slot: DIMM A
             size: 8GiB
             width: 64 bits
             clock: 1600MHz (0.6ns)
        *-bank:1
             description: SODIMM DDR3 Synchronous 1600 MHz (0.6 ns)
             product: M471B1G73DB0-YK0
             vendor: Samsung
             physical id: 1
             serial: confidential
             slot: DIMM B
             size: 8GiB
             width: 64 bits
             clock: 1600MHz (0.6ns)
     *-cpu:1
          physical id: 1
          bus info: cpu@1
          version: 6.10.9
          serial: confidential
          size: 1493MHz
          capacity: 1493MHz
          capabilities: vmx ht cpufreq
          configuration: id=2
        *-logicalcpu:0
             description: Logical CPU
             physical id: 2.1
             capabilities: logical
        *-logicalcpu:1
             description: Logical CPU
             physical id: 2.2
             capabilities: logical
        *-logicalcpu:2
             description: Logical CPU
             physical id: 2.3
             capabilities: logical
        *-logicalcpu:3
             description: Logical CPU
             physical id: 2.4
             capabilities: logical
        *-logicalcpu:4
             description: Logical CPU
             physical id: 2.5
             capabilities: logical
        *-logicalcpu:5
             description: Logical CPU
             physical id: 2.6
             capabilities: logical
        *-logicalcpu:6
             description: Logical CPU
             physical id: 2.7
             capabilities: logical
        *-logicalcpu:7
             description: Logical CPU
             physical id: 2.8
             capabilities: logical
        *-logicalcpu:8
             description: Logical CPU
             physical id: 2.9
             capabilities: logical
        *-logicalcpu:9
             description: Logical CPU
             physical id: 2.a
             capabilities: logical
        *-logicalcpu:10
             description: Logical CPU
             physical id: 2.b
             capabilities: logical
        *-logicalcpu:11
             description: Logical CPU
             physical id: 2.c
             capabilities: logical
        *-logicalcpu:12
             description: Logical CPU
             physical id: 2.d
             capabilities: logical
        *-logicalcpu:13
             description: Logical CPU
             physical id: 2.e
             capabilities: logical
        *-logicalcpu:14
             description: Logical CPU
             physical id: 2.f
             capabilities: logical
        *-logicalcpu:15
             description: Logical CPU
             physical id: 2.10
             capabilities: logical
     *-cpu:2
          physical id: 2
          bus info: cpu@2
          version: 6.10.9
          serial: confidential
          size: 1226MHz
          capacity: 1226MHz
          capabilities: vmx ht cpufreq
          configuration: id=4
        *-logicalcpu:0
             description: Logical CPU
             physical id: 4.1
             capabilities: logical
        *-logicalcpu:1
             description: Logical CPU
             physical id: 4.2
             capabilities: logical
        *-logicalcpu:2
             description: Logical CPU
             physical id: 4.3
             capabilities: logical
        *-logicalcpu:3
             description: Logical CPU
             physical id: 4.4
             capabilities: logical
        *-logicalcpu:4
             description: Logical CPU
             physical id: 4.5
             capabilities: logical
        *-logicalcpu:5
             description: Logical CPU
             physical id: 4.6
             capabilities: logical
        *-logicalcpu:6
             description: Logical CPU
             physical id: 4.7
             capabilities: logical
        *-logicalcpu:7
             description: Logical CPU
             physical id: 4.8
             capabilities: logical
        *-logicalcpu:8
             description: Logical CPU
             physical id: 4.9
             capabilities: logical
        *-logicalcpu:9
             description: Logical CPU
             physical id: 4.a
             capabilities: logical
        *-logicalcpu:10
             description: Logical CPU
             physical id: 4.b
             capabilities: logical
        *-logicalcpu:11
             description: Logical CPU
             physical id: 4.c
             capabilities: logical
        *-logicalcpu:12
             description: Logical CPU
             physical id: 4.d
             capabilities: logical
        *-logicalcpu:13
             description: Logical CPU
             physical id: 4.e
             capabilities: logical
        *-logicalcpu:14
             description: Logical CPU
             physical id: 4.f
             capabilities: logical
        *-logicalcpu:15
             description: Logical CPU
             physical id: 4.10
             capabilities: logical
     *-cpu:3
          physical id: 3
          bus info: cpu@3
          version: 6.10.9
          serial: confidential
          size: 1201MHz
          capacity: 1201MHz
          capabilities: vmx ht cpufreq
          configuration: id=6
        *-logicalcpu:0
             description: Logical CPU
             physical id: 6.1
             capabilities: logical
        *-logicalcpu:1
             description: Logical CPU
             physical id: 6.2
             capabilities: logical
        *-logicalcpu:2
             description: Logical CPU
             physical id: 6.3
             capabilities: logical
        *-logicalcpu:3
             description: Logical CPU
             physical id: 6.4
             capabilities: logical
        *-logicalcpu:4
             description: Logical CPU
             physical id: 6.5
             capabilities: logical
        *-logicalcpu:5
             description: Logical CPU
             physical id: 6.6
             capabilities: logical
        *-logicalcpu:6
             description: Logical CPU
             physical id: 6.7
             capabilities: logical
        *-logicalcpu:7
             description: Logical CPU
             physical id: 6.8
             capabilities: logical
        *-logicalcpu:8
             description: Logical CPU
             physical id: 6.9
             capabilities: logical
        *-logicalcpu:9
             description: Logical CPU
             physical id: 6.a
             capabilities: logical
        *-logicalcpu:10
             description: Logical CPU
             physical id: 6.b
             capabilities: logical
        *-logicalcpu:11
             description: Logical CPU
             physical id: 6.c
             capabilities: logical
        *-logicalcpu:12
             description: Logical CPU
             physical id: 6.d
             capabilities: logical
        *-logicalcpu:13
             description: Logical CPU
             physical id: 6.e
             capabilities: logical
        *-logicalcpu:14
             description: Logical CPU
             physical id: 6.f
             capabilities: logical
        *-logicalcpu:15
             description: Logical CPU
             physical id: 6.10
             capabilities: logical
     *-pci
          description: Host bridge
          product: 3rd Gen Core processor DRAM Controller
          vendor: Intel Corporation
          physical id: 100
          bus info: pci@0000:00:00.0
          version: 09
          width: 32 bits
          clock: 33MHz
          configuration: driver=ivb_uncore
          resources: irq:0
        *-pci:0
             description: PCI bridge
             product: Xeon E3-1200 v2/3rd Gen Core processor PCI Express Root Port
             vendor: Intel Corporation
             physical id: 1
             bus info: pci@0000:00:01.0
             version: 09
             width: 32 bits
             clock: 33MHz
             capabilities: pci pm msi pciexpress normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:26 ioport:e000(size=4096) memory:f5000000-f60fffff ioport:e0000000(size=301989888)
           *-display
                description: VGA compatible controller
                product: GF108GLM [NVS 5200M]
                vendor: NVIDIA Corporation
                physical id: 0
                bus info: pci@0000:01:00.0
                version: a1
                width: 64 bits
                clock: 33MHz
                capabilities: pm msi pciexpress vga_controller bus_master cap_list rom
                configuration: driver=nouveau latency=0
                resources: irq:30 memory:f5000000-f5ffffff memory:e0000000-efffffff memory:f0000000-f1ffffff ioport:e000(size=128) memory:f6000000-f607ffff
        *-display
             description: VGA compatible controller
             product: 3rd Gen Core processor Graphics Controller
             vendor: Intel Corporation
             physical id: 2
             bus info: pci@0000:00:02.0
             version: 09
             width: 64 bits
             clock: 33MHz
             capabilities: msi pm vga_controller bus_master cap_list rom
             configuration: driver=i915 latency=0
             resources: irq:31 memory:f6400000-f67fffff memory:d0000000-dfffffff ioport:f000(size=64) memory:c0000-dffff
        *-usb:0
             description: USB controller
             product: 7 Series/C210 Series Chipset Family USB xHCI Host Controller
             vendor: Intel Corporation
             physical id: 14
             bus info: pci@0000:00:14.0
             version: 04
             width: 64 bits
             clock: 33MHz
             capabilities: pm msi xhci bus_master cap_list
             configuration: driver=xhci_hcd latency=0
             resources: irq:28 memory:f7e20000-f7e2ffff
        *-communication
             description: Communication controller
             product: 7 Series/C210 Series Chipset Family MEI Controller #1
             vendor: Intel Corporation
             physical id: 16
             bus info: pci@0000:00:16.0
             version: 04
             width: 64 bits
             clock: 33MHz
             capabilities: pm msi bus_master cap_list
             configuration: driver=mei_me latency=0
             resources: irq:32 memory:f7e3c000-f7e3c00f
        *-network
             description: Ethernet interface
             product: 82579LM Gigabit Network Connection
             vendor: Intel Corporation
             physical id: 19
             bus info: pci@0000:00:19.0
             logical name: eno1
             version: 04
             serial: confidential
             capacity: 1Gbit/s
             width: 32 bits
             clock: 33MHz
             capabilities: pm msi bus_master cap_list ethernet physical tp 10bt 10bt-fd 100bt 100bt-fd 1000bt-fd autonegotiation
             configuration: autonegotiation=on broadcast=yes driver=e1000e driverversion=3.2.6-k firmware=0.13-3 latency=0 link=no multicast=yes port=twisted pair
             resources: irq:29 memory:f7e00000-f7e1ffff memory:f7e39000-f7e39fff ioport:f080(size=32)
        *-usb:1
             description: USB controller
             product: 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #2
             vendor: Intel Corporation
             physical id: 1a
             bus info: pci@0000:00:1a.0
             version: 04
             width: 32 bits
             clock: 33MHz
             capabilities: pm debug ehci bus_master cap_list
             configuration: driver=ehci-pci latency=0
             resources: irq:16 memory:f7e38000-f7e383ff
        *-multimedia UNCLAIMED
             description: Audio device
             product: 7 Series/C210 Series Chipset Family High Definition Audio Controller
             vendor: Intel Corporation
             physical id: 1b
             bus info: pci@0000:00:1b.0
             version: 04
             width: 64 bits
             clock: 33MHz
             capabilities: pm msi pciexpress bus_master cap_list
             configuration: latency=0
             resources: memory:f7e30000-f7e33fff
        *-pci:1
             description: PCI bridge
             product: 7 Series/C210 Series Chipset Family PCI Express Root Port 1
             vendor: Intel Corporation
             physical id: 1c
             bus info: pci@0000:00:1c.0
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:16 ioport:2000(size=4096) memory:cfb00000-cfcfffff ioport:cfd00000(size=2097152)
        *-pci:2
             description: PCI bridge
             product: 7 Series/C210 Series Chipset Family PCI Express Root Port 2
             vendor: Intel Corporation
             physical id: 1c.1
             bus info: pci@0000:00:1c.1
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:17 ioport:3000(size=4096) memory:f7d00000-f7dfffff ioport:f3500000(size=2097152)
           *-network
                description: Wireless interface
                product: Centrino Advanced-N 6205 [Taylor Peak]
                vendor: Intel Corporation
                physical id: 0
                bus info: pci@0000:03:00.0
                logical name: wlp3s0
                version: 34
                serial: confidential
                width: 64 bits
                clock: 33MHz
                capabilities: pm msi pciexpress bus_master cap_list ethernet physical wireless
                configuration: broadcast=yes driver=iwlwifi driverversion=4.9.24-std500-amd64 firmware=18.168.6.1 latency=0 link=no multicast=yes wireless=IEEE 802.11
                resources: irq:33 memory:f7d00000-f7d01fff
        *-pci:3
             description: PCI bridge
             product: 7 Series/C210 Series Chipset Family PCI Express Root Port 3
             vendor: Intel Corporation
             physical id: 1c.2
             bus info: pci@0000:00:1c.2
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:18 ioport:d000(size=4096) memory:f7200000-f7bfffff ioport:f2b00000(size=10485760)
        *-pci:4
             description: PCI bridge
             product: 7 Series/C210 Series Chipset Family PCI Express Root Port 4
             vendor: Intel Corporation
             physical id: 1c.3
             bus info: pci@0000:00:1c.3
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:19 ioport:c000(size=4096) memory:f6800000-f71fffff ioport:f2100000(size=10485760)
        *-pci:5
             description: PCI bridge
             product: 7 Series/C210 Series Chipset Family PCI Express Root Port 6
             vendor: Intel Corporation
             physical id: 1c.5
             bus info: pci@0000:00:1c.5
             version: c4
             width: 32 bits
             clock: 33MHz
             capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
             configuration: driver=pcieport
             resources: irq:17 ioport:4000(size=4096) memory:f7c00000-f7cfffff ioport:f3700000(size=2097152)
           *-generic
                description: SD Host controller
                product: OZ600FJ0/OZ900FJ0/OZ600FJS SD/MMC Card Reader Controller
                vendor: O2 Micro, Inc.
                physical id: 0
                bus info: pci@0000:0c:00.0
                version: 05
                width: 32 bits
                clock: 33MHz
                capabilities: pm pciexpress bus_master cap_list
                configuration: driver=sdhci-pci latency=0
                resources: irq:17 memory:f7c00000-f7c001ff
        *-usb:2
             description: USB controller
             product: 7 Series/C210 Series Chipset Family USB Enhanced Host Controller #1
             vendor: Intel Corporation
             physical id: 1d
             bus info: pci@0000:00:1d.0
             version: 04
             width: 32 bits
             clock: 33MHz
             capabilities: pm debug ehci bus_master cap_list
             configuration: driver=ehci-pci latency=0
             resources: irq:21 memory:f7e37000-f7e373ff
        *-isa
             description: ISA bridge
             product: QM77 Express Chipset LPC Controller
             vendor: Intel Corporation
             physical id: 1f
             bus info: pci@0000:00:1f.0
             version: 04
             width: 32 bits
             clock: 33MHz
             capabilities: isa bus_master cap_list
             configuration: driver=lpc_ich latency=0
             resources: irq:0
        *-storage
             description: SATA controller
             product: 7 Series Chipset Family 6-port SATA Controller [AHCI mode]
             vendor: Intel Corporation
             physical id: 1f.2
             bus info: pci@0000:00:1f.2
             version: 04
             width: 32 bits
             clock: 66MHz
             capabilities: storage msi pm ahci_1.0 bus_master cap_list
             configuration: driver=ahci latency=0
             resources: irq:27 ioport:f0d0(size=8) ioport:f0c0(size=4) ioport:f0b0(size=8) ioport:f0a0(size=4) ioport:f060(size=32) memory:f7e36000-f7e367ff
        *-serial
             description: SMBus
             product: 7 Series/C210 Series Chipset Family SMBus Controller
             vendor: Intel Corporation
             physical id: 1f.3
             bus info: pci@0000:00:1f.3
             version: 04
             width: 64 bits
             clock: 33MHz
             configuration: driver=i801_smbus latency=0
             resources: irq:18 memory:f7e35000-f7e350ff ioport:f040(size=32)
     *-scsi:0
          physical id: 4
          logical name: scsi0
          capabilities: emulated
        *-disk
             description: ATA Disk
             product: SAMSUNG SSD SM84
             physical id: 0.0.0
             bus info: scsi@0:0.0.0
             logical name: /dev/sda
             version: 1D0Q
             serial: confidential
             size: 238GiB (256GB)
             capabilities: gpt-1.00 partitioned partitioned:gpt
             configuration: ansiversion=5 guid=1b59c2c8-8795-4625-9718-4d636b005ac1 sectorsize=512
           *-volume:0
                description: EFI partition
                vendor: Linux
                physical id: 1
                bus info: scsi@0:0.0.0,1
                logical name: /dev/sda1
                logical name: /mnt/floppy
                version: 1.0
                serial: confidential
                size: 94MiB
                capabilities: extended_attributes large_files ext2 initialized
                configuration: filesystem=ext2 modified=2017-05-15 16:24:20 mount.fstype=ext2 mount.options=rw,relatime,errors=continue,user_xattr,acl name=Linux boot state=mounted
           *-volume:1
                description: EFI partition
                physical id: 2
                bus info: scsi@0:0.0.0,2
                logical name: /dev/sda2
                serial: confidential
                size: 119GiB
                capabilities: lvm2
                configuration: name=LVM Linux
           *-volume:2
                description: Windows FAT volume
                vendor: MSDOS5.0
                physical id: 3
                bus info: scsi@0:0.0.0,3
                logical name: /dev/sda3
                version: FAT32
                serial: confidential
                size: 77MiB
                capacity: 99MiB
                capabilities: boot fat initialized
                configuration: FATs=2 filesystem=fat name=EFI system partition
           *-volume:3
                description: reserved partition
                vendor: Windows
                physical id: 4
                bus info: scsi@0:0.0.0,4
                logical name: /dev/sda4
                serial: confidential
                capacity: 127MiB
                capabilities: nofs
                configuration: name=Microsoft reserved partition
           *-volume:4
                description: Windows NTFS volume
                vendor: Windows
                physical id: 5
                bus info: scsi@0:0.0.0,5
                logical name: /dev/sda5
                version: 3.1
                serial: confidential
                size: 118GiB
                capacity: 119GiB
                capabilities: ntfs initialized
                configuration: clustersize=4096 created=2017-05-16 00:03:06 filesystem=ntfs name=Basic data partition state=clean
     *-scsi:1
          physical id: 5
          logical name: scsi1
          capabilities: emulated
        *-cdrom
             description: DVD-RAM writer
             product: DVD+-RW GU70N
             vendor: HL-DT-ST
             physical id: 0.0.0
             bus info: scsi@1:0.0.0
             logical name: /dev/cdrom
             logical name: /dev/scd0
             logical name: /dev/sr0
             version: A104
             capabilities: removable audio cd-r cd-rw dvd dvd-r dvd-ram
             configuration: ansiversion=5 status=nodisc
  *-battery
       product: DELL NY38W38
       vendor: Sanyo
       physical id: 1
       version: 08/09/2013
       serial: confidential
       slot: Sys. Battery Bay
       capacity: 99900mWh
       configuration: voltage=11.1V
  *-power UNCLAIMED
       description: To Be Filled By O.E.M.
       product: To Be Filled By O.E.M.
       vendor: To Be Filled By O.E.M.
       physical id: 2
       version: To Be Filled By O.E.M.
       serial: confidential
       capacity: 130mWh
  *-network DISABLED
       description: Ethernet interface
       physical id: 3
       logical name: wwp0s29u1u6i6
       serial: confidential
       capabilities: ethernet physical
       configuration: broadcast=yes driver=cdc_mbim driverversion=22-Aug-2005 firmware=CDC MBIM link=no multicast=yes
```

### [lsusb]

`user `[`$`]`lsusb`

    Bus 002 Device 004: ID 0a5c:5801 Broadcom Corp. BCM5880 Secure Applications Processor with fingerprint swipe sensor
    Bus 002 Device 006: ID 413c:818e Dell Computer Corp. DW5560 miniPCIe HSPA+ Mobile Broadband Modem
    Bus 002 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 002 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 004: ID 0c45:643f Microdia Dell Integrated HD Webcam
    Bus 001 Device 003: ID 413c:8197 Dell Computer Corp. BCM20702A0 Bluetooth Module
    Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

### [lscpu]

`user `[`$`]`lscpu`

    Architecture:          x86_64
    CPU op-mode(s):        32-bit, 64-bit
    Byte Order:            Little Endian
    CPU(s):                8
    On-line CPU(s) list:   0-7
    Thread(s) per core:    2
    Core(s) per socket:    4
    Socket(s):             1
    NUMA node(s):          1
    Vendor ID:             GenuineIntel
    CPU family:            6
    Model:                 58
    Model name:            Intel(R) Core(TM) i7-3740QM CPU @ 2.70GHz
    Stepping:              9
    CPU MHz:               1282.104
    CPU max MHz:           3700.0000
    CPU min MHz:           1200.0000
    BogoMIPS:              5382.39
    Virtualization:        VT-x
    L1d cache:             32K
    L1i cache:             32K
    L2 cache:              256K
    L3 cache:              6144K
    NUMA node0 CPU(s):     0-7
    Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc aperfmperf eagerfpu pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm epb tpr_shadow vnmi flexpriority ept vpid fsgsbase smep erms xsaveopt dtherm ida arat pln pts

### [Touchpad]

See the [Alps PS/2](https://wiki.gentoo.org/wiki/Alps_PS/2 "Alps PS/2") article.

### [rfkill]

`user `[`$`]`rfkill list all`

    1: hci0: Bluetooth
        Soft blocked: no
        Hard blocked: no
    2: dell-wifi: Wireless LAN
        Soft blocked: no
        Hard blocked: no
    3: dell-bluetooth: Bluetooth
        Soft blocked: no
        Hard blocked: no
    4: dell-wwan: Wireless WAN
        Soft blocked: no
        Hard blocked: no
    5: phy0: Wireless LAN
        Soft blocked: no
        Hard blocked: no

Needs Dell Laptop Extras `( CONFIG_DELL_LAPTOP )` enabled in the kernel.

### [Network interfaces]

`user `[`$`]`tree /sys/class/net`

    /sys/class/net
    ├── eno1 -> ../../devices/pci0000:00/0000:00:19.0/net/eno1
    ├── lo -> ../../devices/virtual/net/lo
    ├── wlp3s0 -> ../../devices/pci0000:00/0000:00:1c.1/0000:03:00.0/net/wlp3s0
    └── wwp0s29u1u6i6 -> ../../devices/pci0000:00/0000:00:1d.0/usb2/2-1/2-1.6/2-1.6:1.6/net/wwp0s29u1u6i6

### [][Smartcard reader, Fingerprint reader]

For information regarding the fingerprint reader and smartcard reader see

-   [https://forums.gentoo.org/viewtopic-t-1070136.html](https://forums.gentoo.org/viewtopic-t-1070136.html)
-   [https://www.dell.com/support/home/en/us/dedhs1/Drivers/DriversDetails?driverId=HGX2G](https://www.dell.com/support/home/en/us/dedhs1/Drivers/DriversDetails?driverId=HGX2G)
-   [https://blog.g3rt.nl/enable-dell-nfc-contactless-reader.html#broadcom-ush-diagnostics-tool](https://blog.g3rt.nl/enable-dell-nfc-contactless-reader.html#broadcom-ush-diagnostics-tool)

## [][EFI Boot Stub quick\'n dirty]

This computer\'s UEFI allows to ignore the [EFI directory structure](https://wiki.gentoo.org/wiki/EFI_System_Partition#Standard_layout "EFI System Partition") and naming conventions. Running the [[make install]](https://wiki.gentoo.org/wiki/Kernel/Rebuild "Kernel/Rebuild") command for the [stub kernel](https://wiki.gentoo.org/wiki/EFI_stub_kernel#Installation "EFI stub kernel") produces directory content like:

[CODE] **/boot**

    /boot
     ├── config-4.9.16-gentoo
     ├── EFI
     ├── System.map-4.9.16-gentoo
     └── vmlinuz-4.9.16-gentoo

The [vmlinuz-4.9.16-gentoo] file can be used for an [EFI boot entry](https://wiki.gentoo.org/wiki/EFI_System_Partition#UEFI_boot_items "EFI System Partition") without further copying, moving or renaming. Even if it were renamed `foobar`, the UEFI would start it.

## [External resources]

-   [https://linux-hardware.org/index.php?view=computers&type=notebook&vendor=Dell&model=Latitude+E6430](https://linux-hardware.org/index.php?view=computers&type=notebook&vendor=Dell&model=Latitude+E6430)
-   [https://www.techinferno.com/index.php?/forums/topic/7574-14-dell-latitude-e6430-performance-upgrades-and-system-mods/](https://www.techinferno.com/index.php?/forums/topic/7574-14-dell-latitude-e6430-performance-upgrades-and-system-mods/)
-   [Gentoo Forums: i7-3740QM, pstate, powersave and overheating](https://forums.gentoo.org/viewtopic-t-1083460-highlight-.html)