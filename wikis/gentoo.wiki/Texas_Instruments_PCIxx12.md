This page contains [[changes](https://wiki.gentoo.org/index.php?title=Texas_Instruments_PCIxx12&diff=1291829)] which are not marked for translation.

\

[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Texas_Instruments_PCIxx12&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

\

## Contents

-   [[1] [Hardware detection]](#Hardware_detection)
-   [[2] [Device drivers]](#Device_drivers)
    -   [[2.1] [pcmcia - PCIxx12 Cardbus Controller]](#pcmcia_-_PCIxx12_Cardbus_Controller)
    -   [[2.2] [firewire - PCIxx12 OHCI Compliant IEEE 1394 Host Controller]](#firewire_-_PCIxx12_OHCI_Compliant_IEEE_1394_Host_Controller)
    -   [[2.3] [storage - 5-in-1 Multimedia Card Reader (SD/MMC/MS/MS PRO/xD)]](#storage_-_5-in-1_Multimedia_Card_Reader_.28SD.2FMMC.2FMS.2FMS_PRO.2FxD.29)
    -   [[2.4] [generic - PCIxx12 SDA Standard Compliant SD Host Controller]](#generic_-_PCIxx12_SDA_Standard_Compliant_SD_Host_Controller)
-   [[3] [Card detection]](#Card_detection)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Hardware detection]

`root `[`#`]`lspci -nnkv`

    02:06.0 CardBus bridge [0607]: Texas Instruments PCIxx12 Cardbus Controller [104c:8039]
            Subsystem: Hewlett-Packard Company PCIxx12 Cardbus Controller [103c:30aa]
            Flags: bus master, medium devsel, latency 168, IRQ 18
            Memory at e8100000 (32-bit, non-prefetchable) [size=4K]
            Bus: primary=02, secondary=03, subordinate=06, sec-latency=176
            Memory window 0: ec000000-efffffff (prefetchable)
            Memory window 1: f0000000-f3ffffff
            I/O window 0: 00008000-000080ff
            I/O window 1: 00008400-000084ff
            16-bit legacy interface ports at 0001
            Capabilities: [a0] Power Management version 2
            Kernel driver in use: yenta_cardbus

    02:06.1 FireWire (IEEE 1394) [0c00]: Texas Instruments PCIxx12 OHCI Compliant IEEE 1394 Host Controller [104c:803a] (prog-if 10 [OHCI])
            Subsystem: Hewlett-Packard Company PCIxx12 OHCI Compliant IEEE 1394 Host Controller [103c:30aa]
            Flags: bus master, medium devsel, latency 64, IRQ 19
            Memory at e8101000 (32-bit, non-prefetchable) [size=2K]
            Memory at e8104000 (32-bit, non-prefetchable) [size=16K]
            Capabilities: [44] Power Management version 2
            Kernel driver in use: firewire_ohci
            Kernel modules: firewire_ohci

    02:06.2 Mass storage controller [0180]: Texas Instruments 5-in-1 Multimedia Card Reader (SD/MMC/MS/MS PRO/xD) [104c:803b]
            Subsystem: Hewlett-Packard Company 5-in-1 Multimedia Card Reader (SD/MMC/MS/MS PRO/xD) [103c:30aa]
            Flags: bus master, medium devsel, latency 64, IRQ 19
            Memory at e8108000 (32-bit, non-prefetchable) [size=4K]
            Capabilities: [44] Power Management version 2
            Kernel driver in use: tifm_7xx1

    02:06.3 SD Host controller [0805]: Texas Instruments PCIxx12 SDA Standard Compliant SD Host Controller [104c:803c]
            Subsystem: Hewlett-Packard Company PCIxx12 SDA Standard Compliant SD Host Controller [103c:30aa]
            Flags: bus master, medium devsel, latency 64, IRQ 22
            Memory at e8109000 (32-bit, non-prefetchable) [size=256]
            Capabilities: [80] Power Management version 2
            Kernel driver in use: sdhci-pci

    02:06.4 Communication controller [0780]: Texas Instruments PCIxx12 GemCore based SmartCard controller [104c:803d]
            Subsystem: Hewlett-Packard Company nc6310 [103c:30aa]
            Flags: medium devsel, IRQ 10
            Memory at e810a000 (32-bit, non-prefetchable) [size=4K]
            Memory at e810b000 (32-bit, non-prefetchable) [size=4K]
            Capabilities: [44] Power Management version 2

`root `[`#`]`lshw`

      *-core
         *-pci
            *-pci:3
                 description: PCI bridge
                 product: 82801 Mobile PCI Bridge
                 vendor: Intel Corporation
                 physical id: 1e
                 bus info: pci@0000:00:1e.0
                 version: e1
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci subtractive_decode bus_master cap_list
                 resources: ioport:8000(size=4096) memory:e8100000-e83fffff
               *-pcmcia
                    description: CardBus bridge
                    product: PCIxx12 Cardbus Controller
                    vendor: Texas Instruments
                    physical id: 6
                    bus info: pci@0000:02:06.0
                    version: 00
                    width: 32 bits
                    clock: 33MHz
                    capabilities: pcmcia bus_master cap_list
                    configuration: driver=yenta_cardbus latency=176 maxlatency=5 mingnt=192
                    resources: irq:18 memory:e8100000-e8100fff ioport:8000(size=256) ioport:8400(size=256) memory:ec000000-efffffff memory:f0000000-f3ffffff
               *-firewire
                    description: FireWire (IEEE 1394)
                    product: PCIxx12 OHCI Compliant IEEE 1394 Host Controller
                    vendor: Texas Instruments
                    physical id: 6.1
                    bus info: pci@0000:02:06.1
                    version: 00
                    width: 32 bits
                    clock: 33MHz
                    capabilities: pm ohci bus_master cap_list
                    configuration: driver=firewire_ohci latency=64 maxlatency=4 mingnt=2
                    resources: irq:19 memory:e8101000-e81017ff memory:e8104000-e8107fff
               *-storage
                    description: Mass storage controller
                    product: 5-in-1 Multimedia Card Reader (SD/MMC/MS/MS PRO/xD)
                    vendor: Texas Instruments
                    physical id: 6.2
                    bus info: pci@0000:02:06.2
                    version: 00
                    width: 32 bits
                    clock: 33MHz
                    capabilities: storage pm bus_master cap_list
                    configuration: driver=tifm_7xx1 latency=64 maxlatency=4 mingnt=7
                    resources: irq:19 memory:e8108000-e8108fff
               *-generic
                    description: SD Host controller
                    product: PCIxx12 SDA Standard Compliant SD Host Controller
                    vendor: Texas Instruments
                    physical id: 6.3
                    bus info: pci@0000:02:06.3
                    version: 00
                    width: 32 bits
                    clock: 33MHz
                    capabilities: pm bus_master cap_list
                    configuration: driver=sdhci-pci latency=64 maxlatency=4 mingnt=7
                    resources: irq:22 memory:e8109000-e81090ff
               *-communication UNCLAIMED
                    description: Communication controller
                    product: PCIxx12 GemCore based SmartCard controller
                    vendor: Texas Instruments
                    physical id: 6.4
                    bus info: pci@0000:02:06.4
                    version: 00
                    width: 32 bits
                    clock: 33MHz
                    capabilities: pm cap_list
                    configuration: latency=0
                    resources: memory:e810a000-e810afff memory:e810b000-e810bfff

## [Device drivers]

** Note**\
After changes on kernel configuration do not forget to [rebuild the kernel](https://wiki.gentoo.org/wiki/Kernel/Rebuild "Kernel/Rebuild").

### [pcmcia - PCIxx12 Cardbus Controller]

[KERNEL] **linux-4.1.8 - PCIxx12 Cardbus Controller**

    Bus options (PCI etc.)  --->

                [*] PCI support
                [ ]   Support mmconfig PCI config space access
                [ ]   Read CNB20LE Host Bridge Windows
                [*]   PCI Express Port Bus support
                [ ]     Root Port Advanced Error Reporting support
                [*]     PCI Express ASPM control
                [ ]   Message Signaled Interrupts (MSI and MSI-X)
                [ ]   PCI Debugging
                [ ]   Enable PCI resource re-allocation detection
                < >   PCI Stub driver
                [ ]   Interrupts on hypertransport devices
                [ ] PCI IOV support
                [ ] PCI PRI support
                [ ] PCI PASID support
                    PCI host controller drivers  ----
                [*] ISA-style DMA support
                <*> PCCard (PCMCIA/CardBus) support  --->

                    --- PCCard (PCMCIA/CardBus) support
                    < >   16-bit PCMCIA support
                    [*]   32-bit CardBus support
                    *** PC-card bridges ***
                    <*>   CardBus yenta-compatible bridge support
                    [*]     Special initialization for O2Micro bridges
                    [*]     Special initialization for Ricoh bridges
                    [*]     Special initialization for TI and EnE bridges
                    [*]       Auto-tune EnE bridges for CB cards
                    [*]     Special initialization for Toshiba ToPIC bridges

See also the [PC-Card](https://wiki.gentoo.org/wiki/PC-Card "PC-Card") article and [Handbook: Get PCMCIA working](https://wiki.gentoo.org/wiki/Handbook:Parts/Installation/System#Optional:_Get_PCMCIA_working "Handbook:Parts/Installation/System").

### [firewire - PCIxx12 OHCI Compliant IEEE 1394 Host Controller]

For kernel config and more details see the [FireWire](https://wiki.gentoo.org/wiki/FireWire "FireWire") article.

### [][storage - 5-in-1 Multimedia Card Reader (SD/MMC/MS/MS PRO/xD)]

[KERNEL] **linux-4.1.8 - 5-in-1 Multimedia Card Reader (SD/MMC/MS/MS PRO/xD)**

    Device Drivers  --->

                Misc devices  --->

                    < > Analog Devices Digital Potentiometers
                    < > Dummy IRQ handler
                    < > Device driver for IBM RSA service processor
                    < > Sensable PHANToM (PCI)
                    < > SGI IOC4 Base IO support
                    -*- TI Flash Media interface support
                    <*>   TI Flash Media PCI74xx/PCI76xx host adapter support
                    < > Integrated Circuits ICS932S401

### [generic - PCIxx12 SDA Standard Compliant SD Host Controller]

[KERNEL] **linux-4.1.8 - PCIxx12 SDA Standard Compliant SD Host Controller**

    Device Drivers  --->

                <*> MMC/SD/SDIO card support  --->

                    --- MMC/SD/SDIO card support
                    [ ]   MMC debugging
                    [ ]   MMC host clock gating
                    *** MMC/SD/SDIO Card Drivers ***
                    <*>   MMC block device driver
                    (8)     Number of minors per block device
                    [ ]     Use bounce buffer for simple hosts
                    <*>   SDIO UART/GPS class support
                    < >   MMC host test driver
                    *** MMC/SD/SDIO Host Controller Drivers ***
                    <*>   Secure Digital Host Controller Interface support
                    <*>     SDHCI support on PCI bus
                    [ ]       Ricoh MMC Controller Disabler
                    < >     SDHCI support for ACPI enumerated SDHCI controllers
                    < >     SDHCI platform and OF driver helper
                    < >   Winbond W83L51xD SD/MMC Card Interface support
                    <*>   TI Flash Media MMC/SD Interface support
                    < >   ENE CB710 MMC/SD Interface support
                    < >   VIA SD/MMC Card Reader Driver
                    < >   VUB300 USB to SDIO/SD/MMC Host Controller support
                    < >   USB SD Host Controller (USHC) support
                    < >   Renesas USDHI6ROL0 SD/SDIO Host Controller support
                    < >   Toshiba Type A SD/MMC Card Interface Driver

                <*> Sony MemoryStick card support  --->

                    --- Sony MemoryStick card support
                    [ ]   MemoryStick debugging
                    *** MemoryStick drivers ***
                    [ ]   Allow unsafe resume (DANGEROUS)
                    <M>   MemoryStick Pro block device driver
                    < >   MemoryStick Standard device driver
                    *** MemoryStick Host Controller Drivers ***
                    <M>   TI Flash Media MemoryStick Interface support
                    < >   JMicron JMB38X MemoryStick interface support
                    < >   Ricoh R5C592 MemoryStick interface support

## [Card detection]

Media inserted in the card reader do not go in [/dev/disk/] but will be presented as [mspblk0p1] in case of [MemoryStick](https://en.wikipedia.org/wiki/Memory_Stick):

`user `[`$`]` dmesg`

    [ 4344.728058] tifm_core: MemoryStick card detected in socket 0:0
    [ 4344.884195] memstick0: switching to 4-bit parallel mode
    [ 4344.886722]  mspblk0: p1

`user `[`$`]`lsblk -o +fstype,label,uuid,partuuid`

    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT FSTYPE   LABEL           UUID                                 PARTUUID

    mspblk0     254:0    0 958.5M  0 tape
    └─mspblk0p1 254:1    0   957M  0 part            vfat     1WD67HU8N6F

And as [mmcblk0p1] in case of SDHC Card:

`user `[`$`]` dmesg`

    [ 5427.236057] tifm_core: MMC/SD card detected in socket 0:1
    [ 5427.501725] mmc1: new SDHC card at address e624
    [ 5427.502529] mmcblk0: mmc1:e624 SU16G 14.8 GiB
    [ 5427.509956]  mmcblk0: p1

`user `[`$`]`lsblk -o +fstype,label,uuid,partuuid`

    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT FSTYPE   LABEL           UUID                                 PARTUUID

    mmcblk0     179:0    0  14.9G  0 disk
    └─mmcblk0p1 179:1    0  14.9G  0 part            vfat                     30CB-DBD7

For handling of inserted media, see also the [Removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") article.

## [See also]

-   [FireWire](https://wiki.gentoo.org/wiki/FireWire "FireWire")
-   [Removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media")
-   [PC-Card](https://wiki.gentoo.org/wiki/PC-Card "PC-Card")
-   [Handbook:Parts/Installation/System#Optional:\_Get_PCMCIA_working](https://wiki.gentoo.org/wiki/Handbook:Parts/Installation/System#Optional:_Get_PCMCIA_working "Handbook:Parts/Installation/System")

## [External resources]

## [References]