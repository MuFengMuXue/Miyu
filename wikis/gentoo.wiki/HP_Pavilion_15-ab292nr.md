**Resources**

[[]][Official Support Page](http://support.hp.com/us-en/product/HP-Pavilion-15-Notebook-PC-series/8502667/model/9193004)

[[]][Specifications](https://support.hp.com/us-en/document/c04923026)

[[]][Hardware Maintenance Manual](https://h10032.www1.hp.com/ctg/Manual/c04642845.pdf)

[[]][User Guide](https://h10032.www1.hp.com/ctg/Manual/c04774324.pdf)

[[]][HP Pavilion](https://en.wikipedia.org/wiki/HP_Pavilion "wikipedia:HP Pavilion")

## [Hardware]

### [Standard]

  ----------- ------------------------------------------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- -------
  Device      Make/model                                                                                  Status        Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU         Intel® Core™ i7-6700HQ                                                                      Works         N/A                      N/A                N/A
  GPU         Intel® HD Graphics 530                                                                      Works         8086:191b                i915               N/A
  Sound       Intel Corporation Sunrise Point-H HD Audio                                                  Works         8086:a170                snd_hda_intel      N/A
  Ethernet    Realtek Semiconductor Co., Ltd. RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller   Works         10ec:8136                r8169              N/A
  Wi-Fi       Intel Corporation Wireless 3165                                                             Works         8086:3165                iwlwifi            N/A
  Bluetooth   N/A                                                                                         Not tested    N/A                      N/A                N/A
  ----------- ------------------------------------------------------------------------------------------- ------------- ------------------------ ------------------ ---------------- -------

### [Detailed information]

`root `[`#`]`lspci -nnk`

    00:00.0 Host bridge [0600]: Intel Corporation Skylake Host Bridge/DRAM Registers [8086:1910] (rev 07)
        Subsystem: Hewlett-Packard Company Skylake Host Bridge/DRAM Registers [103c:8119]
        Kernel driver in use: skl_uncore
    00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 530 [8086:191b] (rev 06)
        Subsystem: Hewlett-Packard Company HD Graphics 530 [103c:8119]
        Kernel driver in use: i915
    00:04.0 Signal processing controller [1180]: Intel Corporation Skylake Processor Thermal Subsystem [8086:1903] (rev 07)
        Subsystem: Hewlett-Packard Company Skylake Processor Thermal Subsystem [103c:8119]
    00:14.0 USB controller [0c03]: Intel Corporation Sunrise Point-H USB 3.0 xHCI Controller [8086:a12f] (rev 31)
        Subsystem: Hewlett-Packard Company Sunrise Point-H USB 3.0 xHCI Controller [103c:8119]
        Kernel driver in use: xhci_hcd
    00:14.2 Signal processing controller [1180]: Intel Corporation Sunrise Point-H Thermal subsystem [8086:a131] (rev 31)
        Subsystem: Hewlett-Packard Company Sunrise Point-H Thermal subsystem [103c:8119]
    00:16.0 Communication controller [0780]: Intel Corporation Sunrise Point-H CSME HECI #1 [8086:a13a] (rev 31)
        Subsystem: Hewlett-Packard Company Sunrise Point-H CSME HECI [103c:8119]
        Kernel driver in use: mei_me
    00:17.0 SATA controller [0106]: Intel Corporation Sunrise Point-H SATA Controller [AHCI mode] [8086:a103] (rev 31)
        Subsystem: Hewlett-Packard Company Sunrise Point-H SATA Controller [AHCI mode] [103c:8119]
        Kernel driver in use: ahci
    00:1c.0 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #5 [8086:a114] (rev f1)
        Kernel driver in use: pcieport
    00:1c.5 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #6 [8086:a115] (rev f1)
        Kernel driver in use: pcieport
    00:1c.6 PCI bridge [0604]: Intel Corporation Sunrise Point-H PCI Express Root Port #7 [8086:a116] (rev f1)
        Kernel driver in use: pcieport
    00:1f.0 ISA bridge [0601]: Intel Corporation Sunrise Point-H LPC Controller [8086:a14e] (rev 31)
        Subsystem: Hewlett-Packard Company Sunrise Point-H LPC Controller [103c:8119]
    00:1f.2 Memory controller [0580]: Intel Corporation Sunrise Point-H PMC [8086:a121] (rev 31)
        Subsystem: Hewlett-Packard Company Sunrise Point-H PMC [103c:8119]
    00:1f.3 Audio device [0403]: Intel Corporation Sunrise Point-H HD Audio [8086:a170] (rev 31)
        Subsystem: Hewlett-Packard Company Sunrise Point-H HD Audio [103c:8119]
        Kernel driver in use: snd_hda_intel
    00:1f.4 SMBus [0c05]: Intel Corporation Sunrise Point-H SMBus [8086:a123] (rev 31)
        Subsystem: Hewlett-Packard Company Sunrise Point-H SMBus [103c:8119]
        Kernel driver in use: i801_smbus
    01:00.0 Unassigned class [ff00]: Realtek Semiconductor Co., Ltd. RTS522A PCI Express Card Reader [10ec:522a] (rev 01)
        Subsystem: Hewlett-Packard Company RTS522A PCI Express Card Reader [103c:8119]
        Kernel driver in use: rtsx_pci
    02:00.0 Network controller [0280]: Intel Corporation Wireless 3165 [8086:3165] (rev 81)
        Subsystem: Intel Corporation Dual Band Wireless AC 3165 [8086:4010]
        Kernel driver in use: iwlwifi
    03:00.0 Ethernet controller [0200]: Realtek Semiconductor Co., Ltd. RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller [10ec:8136] (rev 0a)
        Subsystem: Hewlett-Packard Company RTL8101/2/6E PCI Express Fast/Gigabit Ethernet controller [103c:8119]
        Kernel driver in use: r8169

`user `[`$`]`lsusb`

    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 004: ID 04f3:20cf Elan Microelectronics Corp.
    Bus 001 Device 003: ID 8087:0a2a Intel Corp.
    Bus 001 Device 002: ID 05c8:0379 Cheng Uei Precision Industry Co., Ltd (Foxlink)
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub