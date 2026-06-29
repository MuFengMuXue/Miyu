[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Easynote_TE69BM&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Official Support Page](https://www.acer.com/gb-en/support/product-support/EN_TE69BM)

[[]][Manufacturer Packard Bell](https://en.wikipedia.org/wiki/Packard_Bell "wikipedia:Packard Bell")

The **Acer (Packard Bell) EasyNote TE69BM** is a laptop.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Standard]](#Standard)
    -   [[1.2] [Detailed information]](#Detailed_information)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Screen tearing]](#Screen_tearing)
        -   [[3.1.1] [Xorg]](#Xorg)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Hardware]

** Note**\
There is [a video](https://www.youtube.com/watch?v=xmyoAKnMqME) of Gentoo + [LXQt](https://wiki.gentoo.org/wiki/LXQt "LXQt") running on this laptop.

### [Standard]

  ---------- ----------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------
  Device     Make/model                                                  Status   Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU        Intel® Celeron® Processor N2920                             Works    N/A                      N/A                5.4.92
  GPU        Atom Processor Z36xxx/Z37xxx Series Graphics & Display      Works    N/A                      i915               5.4.92
  Ethernet   RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller   Works    N/A                      r8169              5.4.92
  Wi-Fi      QCA9565 / AR9565 Wireless Network Adapter                   Works    N/A                      ath9k              5.4.92
  ---------- ----------------------------------------------------------- -------- ------------------------ ------------------ ---------------- -------

-   ::::::
    ::::
    :::
    [![](/images/thumb/5/5a/Laptop-from-packard-bell--easynote-te69bm.jpg/90px-Laptop-from-packard-bell--easynote-te69bm.jpg)](https://wiki.gentoo.org/wiki/File:Laptop-from-packard-bell--easynote-te69bm.jpg)
    :::
    ::::

    ::: gallerytext
    Photo of the laptop
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/a/af/Easynote-bios-information.jpg/120px-Easynote-bios-information.jpg)](https://wiki.gentoo.org/wiki/File:Easynote-bios-information.jpg)
    :::
    ::::

    ::: gallerytext
    Easynote BIOS information
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/7/73/Easynote-bios-main.jpg/120px-Easynote-bios-main.jpg)](https://wiki.gentoo.org/wiki/File:Easynote-bios-main.jpg)
    :::
    ::::

    ::: gallerytext
    Easynote BIOS: Main
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/a/a8/Easynote-bios-security.jpg/120px-Easynote-bios-security.jpg)](https://wiki.gentoo.org/wiki/File:Easynote-bios-security.jpg)
    :::
    ::::

    ::: gallerytext
    Easynote BIOS: Security
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/6/67/Easynote-bios-boot.jpg/120px-Easynote-bios-boot.jpg)](https://wiki.gentoo.org/wiki/File:Easynote-bios-boot.jpg)
    :::
    ::::

    ::: gallerytext
    Easynote BIOS: Boot
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/e/e6/Easynote-bios-boot-mode.jpg/120px-Easynote-bios-boot-mode.jpg)](https://wiki.gentoo.org/wiki/File:Easynote-bios-boot-mode.jpg)
    :::
    ::::

    ::: gallerytext
    Easynote BIOS: Boot mode
    :::
    ::::::

-   ::::::
    ::::
    :::
    [![](/images/thumb/d/d7/Easynote-bios-exit.jpg/120px-Easynote-bios-exit.jpg)](https://wiki.gentoo.org/wiki/File:Easynote-bios-exit.jpg)
    :::
    ::::

    ::: gallerytext
    Easynote BIOS: Exit
    :::
    ::::::

### [Detailed information]

`root `[`#`]`lshw`

    gentoo
        description: Notebook
        product: Easynote TE69BM (Easynote TE69BM_0845_V2.11)
        vendor: Packard Bell
        version: V2.11
        serial: NXC39ES0104171C5B43400
        width: 64 bits
        capabilities: smbios-2.7 dmi-2.7 smp vsyscall32
        configuration: chassis=notebook family=Bay Trail-M System sku=Easynote TE69BM_0845_V2.11 uuid=1CB9C0E3-CAC1-11E3-AFF4-F8A9636946E8
      *-core
           description: Motherboard
           product: Easynote TE69BM
           vendor: Packard Bell
           physical id: 0
           version: V2.11
           serial: NXC39ES0104171C5B43400
           slot: Type2 - Board Chassis Location
         *-firmware
              description: BIOS
              vendor: Packard Bell
              physical id: 0
              version: V2.11
              date: 04/07/2014
              size: 64KiB
              capacity: 3MiB
              capabilities: pci upgrade shadowing cdboot bootselect edd int9keyboard int14serial int17printer int10video acpi usb zipboot biosbootspecification netboot
         *-cpu
              description: CPU
              product: Intel(R) Celeron(R) CPU  N2920  @ 1.86GHz
              vendor: Intel Corp.
              physical id: 4
              bus info: cpu@0
              version: Intel(R) Celeron(R) CPU  N2920  @ 1.86GHz
              slot: CPU 1
              size: 1484MHz
              capacity: 1999MHz
              width: 64 bits
              clock: 133MHz
              capabilities: lm fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx rdtscp x86-64 constant_tsc arch_perfmon pebs bts rep_good nopl xtopology tsc_reliable nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq dtes64 monitor ds_cpl vmx est tm2 ssse3 cx16 xtpr pdcm sse4_1 sse4_2 movbe popcnt tsc_deadline_timer rdrand lahf_lm 3dnowprefetch epb pti tpr_shadow vnmi flexpriority ept vpid tsc_adjust smep erms dtherm ida arat cpufreq
              configuration: cores=4 enabledcores=4 threads=1
            *-cache:0
                 description: L1 cache
                 physical id: 8
                 slot: Unknown
                 size: 32KiB
                 capacity: 32KiB
                 capabilities: synchronous internal write-back instruction
                 configuration: level=1
            *-cache:1
                 description: L2 cache
                 physical id: 9
                 slot: Unknown
                 size: 1MiB
                 capacity: 1MiB
                 capabilities: synchronous internal write-back unified
                 configuration: level=2
         *-cache
              description: L1 cache
              physical id: 7
              slot: Unknown
              size: 24KiB
              capacity: 24KiB
              capabilities: synchronous internal write-back data
              configuration: level=1
         *-memory
              description: System Memory
              physical id: f
              slot: System board or motherboard
              size: 4GiB
            *-bank:0
                 description: SODIMM DDR3 Synchronous 1066 MHz (0.9 ns)
                 product: M471B5173DB0-YK0
                 vendor: Samsung
                 physical id: 0
                 serial: 55142522
                 slot: DIMM0
                 size: 4GiB
                 width: 64 bits
                 clock: 1066MHz (0.9ns)
            *-bank:1
                 description: SODIMM [empty]
                 physical id: 1
                 slot: DIMM1
         *-pci
              description: Host bridge
              product: Atom Processor Z36xxx/Z37xxx Series SoC Transaction Register
              vendor: Intel Corporation
              physical id: 100
              bus info: pci@0000:00:00.0
              version: 0c
              width: 32 bits
              clock: 33MHz
              configuration: driver=iosf_mbi_pci
              resources: irq:0
            *-display
                 description: VGA compatible controller
                 product: Atom Processor Z36xxx/Z37xxx Series Graphics & Display
                 vendor: Intel Corporation
                 physical id: 2
                 bus info: pci@0000:00:02.0
                 version: 0c
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pm msi vga_controller bus_master cap_list rom
                 configuration: driver=i915 latency=0
                 resources: irq:93 memory:90000000-903fffff memory:80000000-8fffffff ioport:2050(size=8) memory:c0000-dffff
            *-sata
                 description: SATA controller
                 product: Atom Processor E3800 Series SATA AHCI Controller
                 vendor: Intel Corporation
                 physical id: 13
                 bus info: pci@0000:00:13.0
                 logical name: scsi0
                 logical name: scsi1
                 version: 0c
                 width: 32 bits
                 clock: 66MHz
                 capabilities: sata msi pm ahci_1.0 bus_master cap_list emulated
                 configuration: driver=ahci latency=0
                 resources: irq:92 ioport:2048(size=8) ioport:205c(size=4) ioport:2040(size=8) ioport:2058(size=4) ioport:2020(size=32) memory:90914000-909147ff
               *-disk
                    description: ATA Disk
                    product: ST500LT012-1DG14
                    physical id: 0
                    bus info: scsi@0:0.0.0
                    logical name: /dev/sda
                    version: SDM1
                    serial: S3P6HW70
                    size: 465GiB (500GB)
                    capabilities: partitioned partitioned:dos
                    configuration: ansiversion=5 logicalsectorsize=512 sectorsize=4096 signature=584c5a6e
                  *-volume:0
                       description: Linux swap volume
                       physical id: 1
                       bus info: scsi@0:0.0.0,1
                       logical name: /dev/sda1
                       version: 1
                       serial: 90487e0c-aaf6-4bd4-a9db-ec048f1c9fcb
                       size: 3815MiB
                       capacity: 3815MiB
                       capabilities: primary nofs swap initialized
                       configuration: filesystem=swap label=swap pagesize=4096
                  *-volume:1
                       description: EXT4 volume
                       vendor: Linux
                       physical id: 2
                       bus info: scsi@0:0.0.0,2
                       logical name: /dev/sda2
                       logical name: /mnt
                       version: 1.0
                       serial: be4de9ac-2889-413a-936c-219d2c1a11ed
                       size: 462GiB
                       capacity: 462GiB
                       capabilities: primary journaled extended_attributes large_files huge_files dir_nlink recover 64bit extents ext4 ext2 initialized
                       configuration: created=2021-01-30 18:23:03 filesystem=ext4 lastmountpoint=/ modified=2021-02-01 20:58:07 mount.fstype=ext4 mount.options=rw,relatime mounted=2021-02-01 20:58:07 state=mounted
               *-cdrom
                    description: DVD-RAM writer
                    product: DVD-RAM UJ8E2Q
                    vendor: MATSHITA
                    physical id: 1
                    bus info: scsi@1:0.0.0
                    logical name: /dev/cdrom
                    logical name: /dev/cdrw
                    logical name: /dev/dvd
                    logical name: /dev/dvdrw
                    logical name: /dev/sr0
                    version: 1.00
                    capabilities: removable audio cd-r cd-rw dvd dvd-r dvd-ram
                    configuration: ansiversion=5 status=nodisc
            *-usb
                 description: USB controller
                 product: Atom Processor Z36xxx/Z37xxx, Celeron N2000 Series USB xHCI
                 vendor: Intel Corporation
                 physical id: 14
                 bus info: pci@0000:00:14.0
                 version: 0c
                 width: 64 bits
                 clock: 33MHz
                 capabilities: pm msi xhci bus_master cap_list
                 configuration: driver=xhci_hcd latency=0
                 resources: irq:89 memory:90900000-9090ffff
               *-usbhost:0
                    product: xHCI Host Controller
                    vendor: Linux 5.4.0-42-generic xhci-hcd
                    physical id: 0
                    bus info: usb@1
                    logical name: usb1
                    version: 5.04
                    capabilities: usb-2.00
                    configuration: driver=hub slots=6 speed=480Mbit/s
                  *-usb:0
                       description: USB hub
                       product: USB 2.0 Hub
                       vendor: Terminus Technology Inc.
                       physical id: 2
                       bus info: usb@1:2
                       version: 1.11
                       capabilities: usb-2.00
                       configuration: driver=hub maxpower=100mA slots=4 speed=480Mbit/s
                     *-usb:0
                          description: Bluetooth wireless interface
                          product: Atheros AR3012 Bluetooth
                          vendor: Lite-On Technology Corp.
                          physical id: 1
                          bus info: usb@1:2.1
                          version: 0.02
                          capabilities: bluetooth usb-1.10
                          configuration: driver=btusb maxpower=100mA speed=12Mbit/s
                     *-usb:1
                          description: Mass storage device
                          product: Mass Storage
                          vendor: Generic
                          physical id: 2
                          bus info: usb@1:2.2
                          logical name: scsi2
                          version: 1.00
                          serial: 78C97DC8
                          capabilities: usb-2.00 scsi emulated scsi-host
                          configuration: driver=usb-storage maxpower=200mA speed=480Mbit/s
                        *-disk
                             description: SCSI Disk
                             product: Flash Disk
                             vendor: Generic
                             physical id: 0.0.0
                             bus info: scsi@2:0.0.0
                             logical name: /dev/sdb
                             version: 8.07
                             serial: 7
                             size: 14GiB (15GB)
                             capabilities: removable
                             configuration: ansiversion=4 logicalsectorsize=512 sectorsize=512
                           *-medium
                                physical id: 0
                                logical name: /dev/sdb
                                size: 14GiB (15GB)
                                capabilities: partitioned partitioned:dos
                                configuration: signature=56f48570
                              *-volume:0
                                   description: Windows FAT volume
                                   vendor: mkfs.fat
                                   physical id: 2
                                   logical name: /dev/sdb2
                                   version: FAT12
                                   serial: c26e-047e
                                   size: 15EiB
                                   capabilities: primary boot fat initialized
                                   configuration: FATs=2 filesystem=fat
                              *-volume:1
                                   description: EXT4 volume
                                   vendor: Linux
                                   physical id: 3
                                   logical name: /dev/sdb3
                                   logical name: /var/log
                                   logical name: /var/crash
                                   version: 1.0
                                   serial: 29983dcb-9843-48ae-b6d5-bf72aec37448
                                   size: 12GiB
                                   capacity: 12GiB
                                   capabilities: primary journaled extended_attributes large_files huge_files dir_nlink recover 64bit extents ext4 ext2 initialized
                                   configuration: created=2021-01-16 00:26:01 filesystem=ext4 label=writable lastmountpoint=/root/var/crash modified=2021-02-01 20:51:25 mount.fstype=ext4 mount.options=rw,relatime mounted=2021-02-01 20:51:25 state=mounted
                  *-usb:1
                       description: Video
                       product: HD WebCam
                       vendor: SuYin
                       physical id: 4
                       bus info: usb@1:4
                       version: 1.01
                       capabilities: usb-2.00
                       configuration: driver=uvcvideo maxpower=500mA speed=480Mbit/s
               *-usbhost:1
                    product: xHCI Host Controller
                    vendor: Linux 5.4.0-42-generic xhci-hcd
                    physical id: 1
                    bus info: usb@2
                    logical name: usb2
                    version: 5.04
                    capabilities: usb-3.00
                    configuration: driver=hub slots=1 speed=5000Mbit/s
            *-generic
                 description: Encryption controller
                 product: Atom Processor Z36xxx/Z37xxx Series Trusted Execution Engine
                 vendor: Intel Corporation
                 physical id: 1a
                 bus info: pci@0000:00:1a.0
                 version: 0c
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pm msi bus_master cap_list
                 configuration: driver=mei_txe latency=0
                 resources: irq:94 memory:90800000-908fffff memory:90700000-907fffff
            *-multimedia
                 description: Audio device
                 product: Atom Processor Z36xxx/Z37xxx Series High Definition Audio Controller
                 vendor: Intel Corporation
                 physical id: 1b
                 bus info: pci@0000:00:1b.0
                 version: 0c
                 width: 64 bits
                 clock: 33MHz
                 capabilities: pm msi bus_master cap_list
                 configuration: driver=snd_hda_intel latency=0
                 resources: irq:95 memory:90910000-90913fff
            *-pci:0
                 description: PCI bridge
                 product: Atom Processor E3800 Series PCI Express Root Port 1
                 vendor: Intel Corporation
                 physical id: 1c
                 bus info: pci@0000:00:1c.0
                 version: 0c
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
                 configuration: driver=pcieport
                 resources: irq:87 ioport:1000(size=4096) memory:90600000-906fffff ioport:90400000(size=1048576)
               *-generic
                    description: Unassigned class
                    product: RTL8411 PCI Express Card Reader
                    vendor: Realtek Semiconductor Co., Ltd.
                    physical id: 0
                    bus info: pci@0000:01:00.0
                    version: 01
                    width: 32 bits
                    clock: 33MHz
                    capabilities: pm msi pciexpress msix vpd bus_master cap_list
                    configuration: driver=rtsx_pci latency=0
                    resources: irq:90 memory:90600000-9060ffff
               *-network
                    description: Ethernet interface
                    product: RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
                    vendor: Realtek Semiconductor Co., Ltd.
                    physical id: 0.2
                    bus info: pci@0000:01:00.2
                    logical name: enp1s0f2
                    version: 0a
                    serial: f8:a9:63:69:46:e8
                    capacity: 1Gbit/s
                    width: 64 bits
                    clock: 33MHz
                    capabilities: pm msi pciexpress msix vpd bus_master cap_list ethernet physical tp mii 10bt 10bt-fd 100bt 100bt-fd 1000bt-fd autonegotiation
                    configuration: autonegotiation=on broadcast=yes driver=r8169 firmware=rtl8411-1_0.0.3 06/18/12 latency=0 link=no multicast=yes port=MII
                    resources: irq:16 ioport:1000(size=256) memory:90610000-90610fff memory:90400000-90403fff
            *-pci:1
                 description: PCI bridge
                 product: Atom Processor E3800 Series PCI Express Root Port 2
                 vendor: Intel Corporation
                 physical id: 1c.1
                 bus info: pci@0000:00:1c.1
                 version: 0c
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pci pciexpress msi pm normal_decode bus_master cap_list
                 configuration: driver=pcieport
                 resources: irq:88 ioport:3000(size=4096) memory:90500000-905fffff
               *-network
                    description: Wireless interface
                    product: QCA9565 / AR9565 Wireless Network Adapter
                    vendor: Qualcomm Atheros
                    physical id: 0
                    bus info: pci@0000:02:00.0
                    logical name: wlp2s0
                    version: 01
                    serial: b8:ee:65:60:0c:0c
                    width: 64 bits
                    clock: 33MHz
                    capabilities: pm msi pciexpress bus_master cap_list rom ethernet physical wireless
                    configuration: broadcast=yes driver=ath9k driverversion=5.4.0-42-generic firmware=N/A ip=192.168.100.97 latency=0 link=yes multicast=yes wireless=IEEE 802.11
                    resources: irq:17 memory:90500000-9057ffff memory:90580000-9058ffff
            *-isa
                 description: ISA bridge
                 product: Atom Processor Z36xxx/Z37xxx Series Power Control Unit
                 vendor: Intel Corporation
                 physical id: 1f
                 bus info: pci@0000:00:1f.0
                 version: 0c
                 width: 32 bits
                 clock: 33MHz
                 capabilities: isa bus_master cap_list
                 configuration: driver=lpc_ich latency=0
                 resources: irq:0
            *-serial
                 description: SMBus
                 product: Atom Processor E3800 Series SMBus Controller
                 vendor: Intel Corporation
                 physical id: 1f.3
                 bus info: pci@0000:00:1f.3
                 version: 0c
                 width: 32 bits
                 clock: 33MHz
                 capabilities: pm cap_list
                 configuration: driver=i801_smbus latency=0
                 resources: irq:18 memory:90916000-9091601f ioport:2000(size=32)
         *-pnp00:00
              product: PnP device PNP0b00
              physical id: 1
              capabilities: pnp
              configuration: driver=rtc_cmos
         *-pnp00:01
              product: PnP device PNP0c02
              physical id: 2
              capabilities: pnp
              configuration: driver=system
         *-pnp00:02
              product: PnP device MSF0001
              physical id: 3
              capabilities: pnp
              configuration: driver=i8042 kbd
         *-pnp00:03
              product: PnP device ETD0509
              physical id: 5
              capabilities: pnp
              configuration: driver=i8042 aux
         *-pnp00:04
              product: PnP device PNP0c02
              physical id: 6
              capabilities: pnp
              configuration: driver=system

## [Installation]

** Tip**\
Press [F2] to enter the BIOS.

### [Kernel]

A third-party [kernel configuration file](https://gitlab.com/vitaly-zdanevich-configs/linux-kernel-easynote-te69bm/-/blob/master/.config) can be used as a template.

## [Troubleshooting]

### [Screen tearing]

** Note**\
This issue does not affect [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") compositors (e.g. [Sway](https://wiki.gentoo.org/wiki/Sway "Sway")).

#### [Xorg]

To fix the [screen tearing](https://en.wikipedia.org/wiki/Screen_tearing "wikipedia:Screen tearing"), the following [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") configuration file should be created ^[\[1\]](#cite_note-1)^:

[FILE] **`/etc/X11/xorg.conf.d/20-intel.conf`**

    Section "Device"
       Identifier  "Intel Graphics"
       Driver      "intel"
       Option      "TearFree"    "true"
    EndSection

The configuration file requires [[[x11-drivers/xf86-video-intel]](https://packages.gentoo.org/packages/x11-drivers/xf86-video-intel)[]] to be installed ^[\[2\]](#cite_note-2)^, as the fix has not yet been implemented ^[\[3\]](#cite_note-3)^ in **xf86-video-modesetting** (part of [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]]):

`root `[`#`]`emerge --ask x11-drivers/xf86-video-intel`

The new configuration requires a reboot.

## [External resources]

-   [Benchmark and components](https://www.userbenchmark.com/System/Packard-Easynote-TE69BM/7843)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://learnubuntumate.weebly.com/screen-tearing-on-intel-graphics.html](https://learnubuntumate.weebly.com/screen-tearing-on-intel-graphics.html)]]
2.  [[[↑](#cite_ref-2)] [[https://manpages.debian.org/buster/xserver-xorg-video-intel/intel.4.en.html](https://manpages.debian.org/buster/xserver-xorg-video-intel/intel.4.en.html)]]
3.  [[[↑](#cite_ref-3)] [[https://gitlab.freedesktop.org/xorg/xserver/-/issues/244](https://gitlab.freedesktop.org/xorg/xserver/-/issues/244)]]