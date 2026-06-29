**Resources**

[[]][Home](http://support.hp.com/us-en/product/HP-ENVY-17-Notebook-PC-series/4149943/model/4229804)

## [Hardware]

### [lspci]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor DRAM Controller [8086:0c04] (rev 06)
            Subsystem: Hewlett-Packard Company Xeon E3-1200 v3/4th Gen Core Processor DRAM Controller [103c:1966]
    00:01.0 PCI bridge [0604]: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor PCI Express x16 Controller [8086:0c01] (rev 06)
            Kernel driver in use: pcieport
    00:02.0 VGA compatible controller [0300]: Intel Corporation 4th Gen Core Processor Integrated Graphics Controller [8086:0416] (rev 06)
            Subsystem: Hewlett-Packard Company 4th Gen Core Processor Integrated Graphics Controller [103c:1966]
            Kernel driver in use: i915
            Kernel modules: i915
    00:03.0 Audio device [0403]: Intel Corporation Xeon E3-1200 v3/4th Gen Core Processor HD Audio Controller [8086:0c0c] (rev 06)
            Subsystem: Hewlett-Packard Company Xeon E3-1200 v3/4th Gen Core Processor HD Audio Controller [103c:1966]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    00:14.0 USB controller [0c03]: Intel Corporation 8 Series/C220 Series Chipset Family USB xHCI [8086:8c31] (rev 05)
            Subsystem: Hewlett-Packard Company 8 Series/C220 Series Chipset Family USB xHCI [103c:1966]
            Kernel driver in use: xhci_hcd
            Kernel modules: xhci_pci
    00:16.0 Communication controller [0780]: Intel Corporation 8 Series/C220 Series Chipset Family MEI Controller #1 [8086:8c3a] (rev 04)
            Subsystem: Hewlett-Packard Company 8 Series/C220 Series Chipset Family MEI Controller [103c:1966]
    00:1a.0 USB controller [0c03]: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #2 [8086:8c2d] (rev 05)
            Subsystem: Hewlett-Packard Company 8 Series/C220 Series Chipset Family USB EHCI [103c:1966]
            Kernel driver in use: ehci-pci
            Kernel modules: ehci_pci
    00:1b.0 Audio device [0403]: Intel Corporation 8 Series/C220 Series Chipset High Definition Audio Controller [8086:8c20] (rev 05)
            Subsystem: Hewlett-Packard Company 8 Series/C220 Series Chipset High Definition Audio Controller [103c:1966]
            Kernel driver in use: snd_hda_intel
            Kernel modules: snd_hda_intel
    00:1c.0 PCI bridge [0604]: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #3 [8086:8c14] (rev d5)
            Kernel driver in use: pcieport
    00:1c.2 PCI bridge [0604]: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #1 [8086:8c10] (rev d5)
            Kernel driver in use: pcieport
    00:1c.3 PCI bridge [0604]: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #4 [8086:8c16] (rev d5)
            Kernel driver in use: pcieport
    00:1c.6 PCI bridge [0604]: Intel Corporation 8 Series/C220 Series Chipset Family PCI Express Root Port #7 [8086:8c1c] (rev d5)
            Kernel driver in use: pcieport
    00:1d.0 USB controller [0c03]: Intel Corporation 8 Series/C220 Series Chipset Family USB EHCI #1 [8086:8c26] (rev 05)
            Subsystem: Hewlett-Packard Company 8 Series/C220 Series Chipset Family USB EHCI [103c:1966]
            Kernel driver in use: ehci-pci
            Kernel modules: ehci_pci
    00:1f.0 ISA bridge [0601]: Intel Corporation HM87 Express LPC Controller [8086:8c4b] (rev 05)
            Subsystem: Hewlett-Packard Company HM87 Express LPC Controller [103c:1966]
    00:1f.2 SATA controller [0106]: Intel Corporation 8 Series/C220 Series Chipset Family 6-port SATA Controller 1 [AHCI mode] [8086:8c03] (rev 05)
            Subsystem: Hewlett-Packard Company 8 Series/C220 Series Chipset Family 6-port SATA Controller 1 [AHCI mode] [103c:1966]
            Kernel driver in use: ahci
            Kernel modules: ahci
    00:1f.3 SMBus [0c05]: Intel Corporation 8 Series/C220 Series Chipset Family SMBus Controller [8086:8c22] (rev 05)
            Subsystem: Hewlett-Packard Company 8 Series/C220 Series Chipset Family SMBus Controller [103c:1966]
            Kernel driver in use: i801_smbus
            Kernel modules: i2c_i801
    01:00.0 3D controller [0302]: NVIDIA Corporation GK208M [GeForce GT 740M] [10de:1292] (rev ff)
            Kernel modules: nvidia_drm, nvidia
    07:00.0 Network controller [0280]: Broadcom Limited BCM4352 802.11ac Wireless Network Adapter [14e4:43b1] (rev 03)
            Subsystem: Hewlett-Packard Company BCM4352 802.11ac Wireless Network Adapter [103c:2154]
            Kernel driver in use: wl
            Kernel modules: wl
    09:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader [10ec:5227] (rev 01)
            Subsystem: Hewlett-Packard Company RTS5227 PCI Express Card Reader [103c:1966]
    0f:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [10ec:8168] (rev 0c)
            Subsystem: Hewlett-Packard Company RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller [103c:1966]
            Kernel driver in use: r8169
            Kernel modules: r8169

## [lsusb]

`user `[`$`]`lsusb`

    Bus 004 Device 002: ID 8087:8000 Intel Corp.
    Bus 004 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 003 Device 002: ID 8087:8008 Intel Corp.
    Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 064e:9301 Suyin Corp.
    Bus 001 Device 003: ID 0a5c:21fb Broadcom Corp.
    Bus 001 Device 002: ID 046d:c52f Logitech, Inc. Unifying Receiver
    Bus 001 Device 005: ID 138a:0050 Validity Sensors, Inc. Swipe Fingerprint Sensor
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub