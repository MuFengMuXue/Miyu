[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Compaq_Presario_CQ5109DE&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](http://support.hp.com/us-en/product/Compaq-Presario-CQ5100-Desktop-PC-series/3942817/model/3975092/product-info)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Compaq_Presario "wikipedia:Compaq Presario")

All available pages on the Wayback Machine about CQ5100 series is at [this](https://web.archive.org/web/*/http://support.hp.com/us-en/product/Compaq-Presario-CQ5100-Desktop-PC-series/*) link. Unfortunately, original product pages (including the homepage link in the infobox) on hp.com have not been not archived. [Here](https://www.manualslib.com/c/cq5100.html) is a link to manuals.

There is also [this](https://web.archive.org/web/20160601044505/http://support.hp.com/us-en/product/compaq-presario-cq5000-desktop-pc-series/3884644/product-info) for information about the CQ5000 series.

## [Hardware detection]

`root `[`#`]`lspci -nnkv`

    00:00.0 Host bridge [0600]: Intel Corporation 82G33/G31/P35/P31 Express DRAM Controller [8086:29c0] (rev 10)
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, fast devsel, latency 0
        Capabilities: [e0] Vendor Specific Information: Len=0b <?>
        Kernel driver in use: agpgart-intel

    00:02.0 VGA compatible controller [0300]: Intel Corporation 82G33/G31 Express Integrated Graphics Controller [8086:29c2] (rev 10) (prog-if 00 [VGA controller])
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, fast devsel, latency 0, IRQ 42
        Memory at fdf00000 (32-bit, non-prefetchable) [size=512K]
        I/O ports at f400 [size=8]
        Memory at d0000000 (32-bit, prefetchable) [size=256M]
        Memory at fda00000 (32-bit, non-prefetchable) [size=1M]
        Expansion ROM at <unassigned> [disabled]
        Capabilities: [90] MSI: Enable+ Count=1/1 Maskable- 64bit-
        Capabilities: [d0] Power Management version 2
        Kernel driver in use: i915
        Kernel modules: i915

    00:1b.0 Audio device [0403]: Intel Corporation NM10/ICH7 Family High Definition Audio Controller [8086:27d8] (rev 01)
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, fast devsel, latency 0, IRQ 10
        Memory at fdff8000 (64-bit, non-prefetchable) [size=16K]
        Capabilities: [50] Power Management version 2
        Capabilities: [60] MSI: Enable- Count=1/1 Maskable- 64bit+
        Capabilities: [70] Express Root Complex Integrated Endpoint, MSI 00
        Capabilities: [100] Virtual Channel
        Capabilities: [130] Root Complex Link

    00:1c.0 PCI bridge [0604]: Intel Corporation NM10/ICH7 Family PCI Express Port 1 [8086:27d0] (rev 01) (prog-if 00 [Normal decode])
        Flags: bus master, fast devsel, latency 0
        Bus: primary=00, secondary=01, subordinate=01, sec-latency=0
        I/O behind bridge: 0000d000-0000dfff
        Memory behind bridge: fdb00000-fdbfffff
        Prefetchable memory behind bridge: 00000000fdc00000-00000000fdcfffff
        Capabilities: [40] Express Root Port (Slot+), MSI 00
        Capabilities: [80] MSI: Enable+ Count=1/1 Maskable- 64bit-
        Capabilities: [90] Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Capabilities: [a0] Power Management version 2
        Capabilities: [100] Virtual Channel
        Capabilities: [180] Root Complex Link
        Kernel driver in use: pcieport
        Kernel modules: shpchp

    00:1d.0 USB controller [0c03]: Intel Corporation NM10/ICH7 Family USB UHCI Controller #1 [8086:27c8] (rev 01) (prog-if 00 [UHCI])
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, medium devsel, latency 0, IRQ 23
        I/O ports at f500 [size=32]
        Kernel driver in use: uhci_hcd

    00:1d.1 USB controller [0c03]: Intel Corporation NM10/ICH7 Family USB UHCI Controller #2 [8086:27c9] (rev 01) (prog-if 00 [UHCI])
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, medium devsel, latency 0, IRQ 19
        I/O ports at f600 [size=32]
        Kernel driver in use: uhci_hcd

    00:1d.2 USB controller [0c03]: Intel Corporation NM10/ICH7 Family USB UHCI Controller #3 [8086:27ca] (rev 01) (prog-if 00 [UHCI])
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, medium devsel, latency 0, IRQ 18
        I/O ports at f700 [size=32]
        Kernel driver in use: uhci_hcd

    00:1d.3 USB controller [0c03]: Intel Corporation NM10/ICH7 Family USB UHCI Controller #4 [8086:27cb] (rev 01) (prog-if 00 [UHCI])
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, medium devsel, latency 0, IRQ 16
        I/O ports at f800 [size=32]
        Kernel driver in use: uhci_hcd

    00:1d.7 USB controller [0c03]: Intel Corporation NM10/ICH7 Family USB2 EHCI Controller [8086:27cc] (rev 01) (prog-if 20 [EHCI])
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, medium devsel, latency 0, IRQ 23
        Memory at fdfff000 (32-bit, non-prefetchable) [size=1K]
        Capabilities: [50] Power Management version 2
        Capabilities: [58] Debug port: BAR=1 offset=00a0
        Kernel driver in use: ehci-pci

    00:1e.0 PCI bridge [0604]: Intel Corporation 82801 PCI Bridge [8086:244e] (rev e1) (prog-if 01 [Subtractive decode])
        Flags: bus master, fast devsel, latency 0
        Bus: primary=00, secondary=05, subordinate=05, sec-latency=32
        I/O behind bridge: 0000e000-0000efff
        Memory behind bridge: fdd00000-fddfffff
        Prefetchable memory behind bridge: 00000000fde00000-00000000fdefffff
        Capabilities: [50] Subsystem: Hewlett-Packard Company Device [103c:2a78]

    00:1f.0 ISA bridge [0601]: Intel Corporation 82801GB/GR (ICH7 Family) LPC Interface Bridge [8086:27b8] (rev 01)
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, medium devsel, latency 0
        Capabilities: [e0] Vendor Specific Information: Len=0c <?>
        Kernel driver in use: lpc_ich
        Kernel modules: intel_rng, lpc_ich, leds_ss4200

    00:1f.2 IDE interface [0101]: Intel Corporation NM10/ICH7 Family SATA Controller [IDE mode] [8086:27c0] (rev 01) (prog-if 8a [Master SecP PriP])
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, 66MHz, medium devsel, latency 0, IRQ 19
        I/O ports at 01f0 [size=8]
        I/O ports at 03f4
        I/O ports at 0170 [size=8]
        I/O ports at 0374
        I/O ports at f900 [size=16]
        Capabilities: [70] Power Management version 2
        Kernel driver in use: ata_piix
        Kernel modules: pata_acpi, ata_generic

    00:1f.3 SMBus [0c05]: Intel Corporation NM10/ICH7 Family SMBus Controller [8086:27da] (rev 01)
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: medium devsel, IRQ 19
        I/O ports at 0500 [size=32]
        Kernel driver in use: i801_smbus
        Kernel modules: i2c_i801

    01:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8101E/RTL8102E PCI Express Fast Ethernet controller [10ec:8136] (rev 01)
        Subsystem: Hewlett-Packard Company Device [103c:2a78]
        Flags: bus master, fast devsel, latency 0, IRQ 41
        I/O ports at de00 [size=256]
        Memory at fdbff000 (64-bit, non-prefetchable) [size=4K]
        [virtual] Expansion ROM at fdc00000 [disabled] [size=128K]
        Capabilities: [40] Power Management version 2
        Capabilities: [48] Vital Product Data
        Capabilities: [50] MSI: Enable+ Count=1/2 Maskable- 64bit+
        Capabilities: [60] Express Endpoint, MSI 00
        Capabilities: [84] Vendor Specific Information: Len=4c <?>
        Capabilities: [100] Advanced Error Reporting
        Capabilities: [12c] Virtual Channel
        Capabilities: [148] Device Serial Number 05-00-00-00-36-4c-e0-00
        Capabilities: [154] Power Budgeting <?>
        Kernel driver in use: r8169
        Kernel modules: r8169

`root `[`#`]`lshw`

    sysresccd
        description: Desktop Computer
        product: VC774AA-ABD CQ5109DE (VC774AA#ABD)
        vendor: Compaq-Presario
        serial: CNX92902FT
        width: 32 bits
        capabilities: smbios-2.5 dmi-2.5 smp-1.4 smp vsyscall32
        configuration: boot=normal chassis=desktop cpus=2 family=103C_53316J sku=VC774AA#ABD uuid=70B7F5A1-83A5-2734-32A5-43A34AB47AB3
      *-core
           description: Motherboard
           product: Boston
           vendor: MSI
           physical id: 0
           version: 1.0
         *-firmware
              description: BIOS
              vendor: Phoenix Technologies, LTD
              physical id: 0
              version: 5.24
              date: 06/19/2009
              size: 128KiB
              capacity: 960KiB
              capabilities: isa pci pnp apm upgrade shadowing cdboot bootselect socketedrom edd int13floppy360 int13floppy1200 int13floppy720 int13floppy2880 int5printscreen int9keyboard int14serial int17printer int10video acpi usb ls120boot zipboot
         *-cpu:0
              description: CPU
              product: Pentium(R) Dual-Core  CPU      E5200  @ 2.50GHz
              vendor: Intel Corp.
              physical id: 4
              bus info: cpu@0
              version: 6.7.10
              serial: 0001-067A-0000-0000-0000-0000
              slot: Socket 775
              size: 2500MHz
              capacity: 4GHz
              width: 64 bits
              clock: 800MHz
              capabilities: x86-64 boot fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx constant_tsc arch_perfmon pebs bts rep_good nopl aperfmperf pni dtes64 monitor ds_cpl est tm2 ssse3 cx16 xtpr pdcm xsave lahf_lm dtherm cpufreq
              configuration: cores=2 enabledcores=2 id=0 threads=2
            *-cache:0
                 description: L1 cache
                 physical id: 8
                 slot: Internal Cache
                 size: 32KiB
                 capacity: 32KiB
                 capabilities: synchronous internal write-back data
            *-cache:1
                 description: L2 cache
                 physical id: 9
                 slot: External Cache
                 size: 2MiB
                 capacity: 2MiB
                 capabilities: synchronous external write-back unified
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
         *-memory
              description: System Memory
              physical id: 12
              slot: System board or motherboard
              size: 6GiB
            *-bank:0
                 description: DIMM DDR2 Synchronous 800 MHz (1.2 ns)
                 product: M3 78T5663EH3-CF7
                 vendor: Samsung
                 physical id: 0
                 serial: 649DE9B7
                 slot: A0
                 size: 2GiB
                 width: 64 bits
                 clock: 800MHz (1.2ns)
            *-bank:1
                 description: DIMM DDR2 Synchronous 800 MHz (1.2 ns)
                 product: 99P5471-013.A00LF
                 vendor: Kingston
                 physical id: 1
                 serial: 16EE28EF
                 slot: A1
                 size: 4GiB
                 width: 64 bits
                 clock: 800MHz (1.2ns)
         *-cpu:1
              physical id: 1
              bus info: cpu@1
              version: 6.7.10
              serial: 0001-067A-0000-0000-0000-0000
              size: 2500MHz
              capacity: 2500MHz
              capabilities: ht cpufreq
              configuration: id=1
            *-logicalcpu:0
                 description: Logical CPU
                 physical id: 1.1
                 capabilities: logical
            *-logicalcpu:1
                 description: Logical CPU
                 physical id: 1.2
                 capabilities: logical
         *-pci
              description: Host bridge
              product: 82G33/G31/P35/P31 Express DRAM Controller
              vendor: Intel Corporation
              physical id: 100
              bus info: pci@0000:00:00.0
              version: 10
              width: 32 bits
              clock: 33MHz
              configuration: driver=agpgart-intel
              resources: irq:0
            *-display
                 description: VGA compatible controller
                 product: 82G33/G31 Express Integrated Graphics Controller
                 vendor: Intel Corporation
                 physical id: 2
                 bus info: pci@0000:00:02.0
                 version: 10
                 width: 32 bits
                 clock: 33MHz
                 capabilities: msi pm vga_controller bus_master cap_list rom
                 configuration: driver=i915 latency=0
                 resources: irq:42 memory:fdf00000-fdf7ffff ioport:f400(size=8) memory:d0000000-dfffffff memory:fda00000-fdafffff
            *-multimedia UNCLAIMED
                 description: Audio device
                 product: NM10/ICH7 Family High Definition Audio Controller
                 vendor: Intel Corporation
                 physical id: 1b
                 bus info: pci@0000:00:1b.0
                 version: 01
                 width: 64 bits
                 clock: 33MHz
                 capabilities: pm msi pciexpress bus_master cap_list
                 configuration: latency=0
                 resources: memory:fdff8000-fdffbfff
            *-pci:0
                 description: PCI bridge
                 product: NM10/ICH7 Family PCI Express Port 1
                 vendor: Intel Corporation
                 physical id: 1c
                 bus info: pci@0000:00:1c.0
                 version: 01
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
                 configuration: driver=pcieport
                 resources: irq:40 ioport:d000(size=4096) memory:fdb00000-fdbfffff ioport:fdc00000(size=1048576)
               *-network
                    description: Ethernet interface
                    product: RTL8101E/RTL8102E PCI Express Fast Ethernet controller
                    vendor: Realtek Semiconductor Co., Ltd.
                    physical id: 0
                    bus info: pci@0000:01:00.0
                    logical name: enp1s0
                    version: 01
                    serial: 00:24:21:ad:74:83
                    size: 10Mbit/s
                    capacity: 100Mbit/s
                    width: 64 bits
                    clock: 33MHz
                    capabilities: pm vpd msi pciexpress bus_master cap_list rom ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd autonegotiation
                    configuration: autonegotiation=on broadcast=yes driver=r8169 driverversion=2.3LK-NAPI duplex=half latency=0 link=no multicast=yes port=MII speed=10Mbit/s
                    resources: irq:41 ioport:de00(size=256) memory:fdbff000-fdbfffff memory:fdc00000-fdc1ffff
            *-usb:0
                 description: USB controller
                 product: NM10/ICH7 Family USB UHCI Controller #1
                 vendor: Intel Corporation
                 physical id: 1d
                 bus info: pci@0000:00:1d.0
                 version: 01
                 width: 32 bits
                 clock: 33MHz
                 capabilities: uhci bus_master
                 configuration: driver=uhci_hcd latency=0
                 resources: irq:23 ioport:f500(size=32)
            *-usb:1
                 description: USB controller
                 product: NM10/ICH7 Family USB UHCI Controller #2
                 vendor: Intel Corporation
                 physical id: 1d.1
                 bus info: pci@0000:00:1d.1
                 version: 01
                 width: 32 bits
                 clock: 33MHz
                 capabilities: uhci bus_master
                 configuration: driver=uhci_hcd latency=0
                 resources: irq:19 ioport:f600(size=32)
            *-usb:2
                 description: USB controller
                 product: NM10/ICH7 Family USB UHCI Controller #3
                 vendor: Intel Corporation
                 physical id: 1d.2
                 bus info: pci@0000:00:1d.2
                 version: 01
                 width: 32 bits
                 clock: 33MHz
                 capabilities: uhci bus_master
                 configuration: driver=uhci_hcd latency=0
                 resources: irq:18 ioport:f700(size=32)
            *-usb:3
                 description: USB controller
                 product: NM10/ICH7 Family USB UHCI Controller #4
                 vendor: Intel Corporation
                 physical id: 1d.3
                 bus info: pci@0000:00:1d.3
                 version: 01
                 width: 32 bits
                 clock: 33MHz
                 capabilities: uhci bus_master
                 configuration: driver=uhci_hcd latency=0
                 resources: irq:16 ioport:f800(size=32)
            *-usb:4
                 description: USB controller
                 product: NM10/ICH7 Family USB2 EHCI Controller
                 vendor: Intel Corporation
                 physical id: 1d.7
                 bus info: pci@0000:00:1d.7
                 version: 01
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pm debug ehci bus_master cap_list
                 configuration: driver=ehci-pci latency=0
                 resources: irq:23 memory:fdfff000-fdfff3ff
            *-pci:1
                 description: PCI bridge
                 product: 82801 PCI Bridge
                 vendor: Intel Corporation
                 physical id: 1e
                 bus info: pci@0000:00:1e.0
                 version: e1
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci subtractive_decode bus_master cap_list
                 resources: ioport:e000(size=4096) memory:fdd00000-fddfffff ioport:fde00000(size=1048576)
            *-isa
                 description: ISA bridge
                 product: 82801GB/GR (ICH7 Family) LPC Interface Bridge
                 vendor: Intel Corporation
                 physical id: 1f
                 bus info: pci@0000:00:1f.0
                 version: 01
                 width: 32 bits
                 clock: 33MHz
                 capabilities: isa bus_master cap_list
                 configuration: driver=lpc_ich latency=0
                 resources: irq:0
            *-ide
                 description: IDE interface
                 product: NM10/ICH7 Family SATA Controller [IDE mode]
                 vendor: Intel Corporation
                 physical id: 1f.2
                 bus info: pci@0000:00:1f.2
                 version: 01
                 width: 32 bits
                 clock: 66MHz
                 capabilities: ide pm bus_master cap_list
                 configuration: driver=ata_piix latency=0
                 resources: irq:19 ioport:1f0(size=8) ioport:3f6 ioport:170(size=8) ioport:376 ioport:f900(size=16)
            *-serial
                 description: SMBus
                 product: NM10/ICH7 Family SMBus Controller
                 vendor: Intel Corporation
                 physical id: 1f.3
                 bus info: pci@0000:00:1f.3
                 version: 01
                 width: 32 bits
                 clock: 33MHz
                 configuration: driver=i801_smbus latency=0
                 resources: irq:19 ioport:500(size=32)
         *-scsi:0
              physical id: 2
              logical name: scsi0
              capabilities: emulated
            *-disk
                 description: ATA Disk
                 product: WDC WD6400AAKS-6
                 vendor: Western Digital
                 physical id: 0.0.0
                 bus info: scsi@0:0.0.0
                 logical name: /dev/sda
                 version: 01.0
                 serial: WD-WCASY5647150
                 size: 596GiB (640GB)
                 capabilities: partitioned partitioned:dos
                 configuration: ansiversion=5 sectorsize=512 signature=1549f232
               *-volume:0
                    description: Windows NTFS volume
                    physical id: 1
                    bus info: scsi@0:0.0.0,1
                    logical name: /dev/sda1
                    version: 3.1
                    serial: 463f-1486
                    size: 98MiB
                    capacity: 100MiB
                    capabilities: primary bootable ntfs initialized
                    configuration: clustersize=4096 created=2015-11-20 02:50:42 filesystem=ntfs label=System-reserviert state=clean
               *-volume:1
                    description: Windows NTFS volume
                    physical id: 2
                    bus info: scsi@0:0.0.0,2
                    logical name: /dev/sda2
                    version: 3.1
                    serial: c02affa8-9bdc-554b-98ce-dfebca93461e
                    size: 465GiB
                    capacity: 465GiB
                    capabilities: primary ntfs initialized
                    configuration: clustersize=4096 created=2015-11-20 02:51:23 filesystem=ntfs state=clean
            *-cdrom
                 description: DVD-RAM writer
                 product: DVD-RAM GH40L
                 vendor: HL-DT-ST
                 physical id: 0.1.0
                 bus info: scsi@0:0.1.0
                 logical name: /dev/cdrom
                 logical name: /dev/scd0
                 logical name: /dev/sr0
                 logical name: /livemnt/boot
                 version: 1.04
                 capabilities: removable audio cd-r cd-rw dvd dvd-r dvd-ram
                 configuration: ansiversion=5 mount.fstype=iso9660 mount.options=ro,relatime,mode=0644 state=mounted status=ready
               *-medium
                    physical id: 0
                    logical name: /dev/cdrom
                    logical name: /livemnt/boot
                    configuration: mount.fstype=iso9660 mount.options=ro,relatime,mode=0644 state=mounted
         *-scsi:1
              physical id: 3
              bus info: usb@1:8
              logical name: scsi2
              capabilities: emulated scsi-host
              configuration: driver=usb-storage
            *-disk
                 description: SCSI Disk
                 physical id: 0.0.0
                 bus info: scsi@2:0.0.0
                 logical name: /dev/sdb
                 size: 58GiB (62GB)
                 capabilities: partitioned partitioned:dos
                 configuration: sectorsize=512
               *-volume
                    description: Windows NTFS volume
                    physical id: 1
                    bus info: scsi@2:0.0.0,1
                    logical name: /dev/sdb1
                    version: 3.1
                    serial: 0246-9ff7
                    size: 58GiB
                    capacity: 58GiB
                    capabilities: primary ntfs initialized
                    configuration: clustersize=4096 filesystem=ntfs label=Willis state=clean
         *-scsi:2
              physical id: 5
              bus info: usb@1:5
              logical name: scsi3
              capabilities: emulated scsi-host
              configuration: driver=usb-storage
            *-disk
                 description: SCSI Disk
                 physical id: 0.0.0
                 bus info: scsi@3:0.0.0
                 logical name: /dev/sdc
                 size: 3916MiB (4106MB)
                 capabilities: partitioned partitioned:dos
                 configuration: sectorsize=512
               *-volume
                    description: Windows FAT volume
                    vendor: MSDOS5.0
                    physical id: 1
                    bus info: scsi@3:0.0.0,1
                    logical name: /dev/sdc1
                    logical name: /mnt/custom
                    version: FAT32
                    serial: b0b3-fac4
                    size: 3915MiB
                    capacity: 3915MiB
                    capabilities: primary fat initialized
                    configuration: FATs=2 filesystem=fat mount.fstype=vfat mount.options=rw,relatime,fmask=0022,dmask=0022,codepage=437,iocharset=ascii,shortname=mixed,errors=remount-ro state=mounted

## [References]