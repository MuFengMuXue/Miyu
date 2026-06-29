**Resources**

[[]][Official Support Page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/yoga-series/yoga-2-11-notebook-lenovo)

[[]][Specifications](https://psref.lenovo.com/syspool/Sys/PDF/Lenovo_Laptops/Lenovo_Yoga_2_11/Lenovo_Yoga_2_11_Spec.PDF)

[[]][Specifications (by region)](https://psref.lenovo.com/Product/Yoga/Lenovo_Yoga_2_11)

[[]][Hardware Maintenance Manual](https://download.lenovo.com/consumer/mobiles_pub/lenovo_yoga_2_11_hmm.pdf)

[[]][User Guide](https://download.lenovo.com/consumer/mobiles_pub/lenovo_yoga_2_11_ug_english.pdf)

[[]][Lenovo Yoga](https://en.wikipedia.org/wiki/Lenovo_Yoga#Lenovo_Yoga_2_11 "wikipedia:Lenovo Yoga")

Information contained herein was acquired from model no. 20332, but may work with variants.

## Contents

-   [[1] [Hardware]](#Hardware)
    -   [[1.1] [Laptop Specifications]](#Laptop_Specifications)
        -   [[1.1.1] [Hardware]](#Hardware_2)
-   [[2] [Configuration details]](#Configuration_details)
    -   [[2.1] [Graphics]](#Graphics)
    -   [[2.2] [Touchpad]](#Touchpad)
    -   [[2.3] [make.conf]](#make.conf)
-   [[3] [External resources]](#External_resources)

## [Hardware]

### [Laptop Specifications]

  ----------------------------- ----------------------------------- ------------- ---------------------------------------------------------
             Device                            Model                    Works                               Notes
         Intel® Pentium™         N3520, 2.42GHz, 4T, 2M (BayTrail)       Yes
       Intel® HD Graphics                      4200                      Yes                         i915 kernel driver
   11.6\" 1366x768 IPS TFT LCD                                           Yes
            Wireless                 Qualcomm Atheros QCA9565            Yes                         ath9k kernel driver
            Bluetooth                                                Not tested
             Camera                                                  Not tested                           uvcvideo
           Card Reader                                                   Yes
        ELantech Touchpad                     ETPS/2                     Yes       PS/2 Mouse as module + Elantech PS/2 protocol extension
         Intel HD Audio                                                  Yes                    HD Audio PCI (snd-hda-intel)
            Digitizer                     Atmel maXTouch                 Yes
  ----------------------------- ----------------------------------- ------------- ---------------------------------------------------------

#### [Hardware]

`root `[`#`]`lspci -k`

    00:00.0 Host bridge: Intel Corporation Atom Processor Z36xxx/Z37xxx Series SoC Transaction Register (rev 0e)
        Subsystem: Lenovo Atom Processor Z36xxx/Z37xxx Series SoC Transaction Register
        Kernel driver in use: iosf_mbi_pci
    00:02.0 VGA compatible controller: Intel Corporation Atom Processor Z36xxx/Z37xxx Series Graphics & Display (rev 0e)
        Subsystem: Lenovo Atom Processor Z36xxx/Z37xxx Series Graphics & Display
        Kernel driver in use: i915
        Kernel modules: i915
    00:13.0 SATA controller: Intel Corporation Atom Processor E3800 Series SATA AHCI Controller (rev 0e)
        Subsystem: Lenovo Atom Processor E3800 Series SATA AHCI Controller
        Kernel driver in use: ahci
    00:14.0 USB controller: Intel Corporation Atom Processor Z36xxx/Z37xxx, Celeron N2000 Series USB xHCI (rev 0e)
        Subsystem: Lenovo Atom Processor Z36xxx/Z37xxx, Celeron N2000 Series USB xHCI
        Kernel driver in use: xhci_hcd
    00:1a.0 Encryption controller: Intel Corporation Atom Processor Z36xxx/Z37xxx Series Trusted Execution Engine (rev 0e)
        Subsystem: Lenovo Atom Processor Z36xxx/Z37xxx Series Trusted Execution Engine
        Kernel driver in use: mei_txe
        Kernel modules: mei_txe
    00:1b.0 Audio device: Intel Corporation Atom Processor Z36xxx/Z37xxx Series High Definition Audio Controller (rev 0e)
        Subsystem: Lenovo Atom Processor Z36xxx/Z37xxx Series High Definition Audio Controller
    00:1c.0 PCI bridge: Intel Corporation Atom Processor E3800 Series PCI Express Root Port 1 (rev 0e)
        Kernel driver in use: pcieport
        Kernel modules: shpchp
    00:1f.0 ISA bridge: Intel Corporation Atom Processor Z36xxx/Z37xxx Series Power Control Unit (rev 0e)
        Subsystem: Lenovo Atom Processor Z36xxx/Z37xxx Series Power Control Unit
        Kernel driver in use: lpc_ich
        Kernel modules: lpc_ich
    00:1f.3 SMBus: Intel Corporation Atom Processor E3800 Series SMBus Controller (rev 0e)
        Subsystem: Lenovo Atom Processor E3800 Series SMBus Controller
        Kernel driver in use: i801_smbus
        Kernel modules: i2c_i801
    01:00.0 Network controller: Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter (rev 01)
        Subsystem: Lenovo QCA9565 / AR9565 Wireless Network Adapter
        Kernel driver in use: ath9k
        Kernel modules: ath9k

`root `[`#`]`lsusb`

    Bus 001 Device 005: ID 048d:8386 Integrated Technology Express, Inc.
    Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
    Bus 001 Device 006: ID 1bcf:2c66 Sunplus Innovation Technology Inc.
    Bus 001 Device 008: ID 0cf3:3004 Qualcomm Atheros Communications AR3012 Bluetooth 4.0
    Bus 001 Device 003: ID 03eb:8c1d Atmel Corp.
    Bus 001 Device 004: ID 0781:5581 SanDisk Corp. Ultra
    Bus 001 Device 002: ID 05e3:0608 Genesys Logic, Inc. Hub
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

## [Configuration details]

** Tip**\
[[[sys-kernel/kergen]](https://packages.gentoo.org/packages/sys-kernel/kergen)[]] works well with this model.

### [Graphics]

See [Intel](https://wiki.gentoo.org/wiki/Intel "Intel").

### [Touchpad]

This laptop has an Elantech PS/2 touchpad:

[KERNEL]

    --- Mice
    <*>   PS/2 mouse
    [*]     Elantech PS/2 protocol extension

### [make.conf]

It is recommended to add or replace the following lines

[FILE] **`/etc/portage/make.conf`**

    VIDEO_CARDS="intel i965"
    CPU_FLAGS_X86="mmx mmxext popcnt sse sse2 sse3 sse4_1 sse4_2 ssse3"
    INPUT_DEVICES="evdev synaptics"

## [External resources]

-   [Detailed Hardware Info](http://pdadb.net/index.php?m=device&id=5805&c=lenovo_yoga_2_11_20332__ideapad_yoga_2_11_80cx).
-   [Pappy\'s preconfigs](//forums.gentoo.org/viewtopic-t-1051430.html)
-   [Unofficial forum thread](http://forums.gentoo.org/viewtopic-t-1066726.html)
-   [User made kernel config](https://bitbucket.org/experimentfailed/gentoo-kernel-configs)
-   [https://wiki.archlinux.org/title/Lenovo_Yoga_2_11](https://wiki.archlinux.org/title/Lenovo_Yoga_2_11)