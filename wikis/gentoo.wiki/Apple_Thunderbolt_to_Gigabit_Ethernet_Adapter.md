## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
-   [[3] [References]](#References)

## [Hardware]

The Apple Thunderbolt to Gigabit Ethernet Adapter carries the model number: `A1433 EMC 2590`

`root `[`#`]`lspci -nnk`

    Ethernet controller [0200]: Broadcom Corporation NetXtreme BCM57762 Gigabit Ethernet PCIe [14e4:1682]
    Subsystem: Apple Inc. Device [106b:00f6]
    Kernel driver in use: tg3

## [Installation]

### [Kernel]

The recommended minimum version of Linux to use is 4.3. This release fixes an issue that prevented the hot-plugging of Thunderbolt Ethernet devices on Apple hardware^[\[1\]](#cite_note-1)^.

[KERNEL] **Enabling Apple Thunderbolt to Gigabit Ethernet Adapter support**

        Device Drivers --->
          [*] Network device support --->
                [*]   Ethernet driver support --->
                        [*]   Broadcom devices
                        <*>     Broadcom Tigon3 support
                <*>   PHY Device support and infrastructure --->
                        <*>   Broadcom PHYs

[KERNEL] **Enabling Thunderbolt hot-plugging support**

        Bus options (PCI etc.) --->
          [*] PCI support
          [*]   PCI Express Port Bus support
          [*]     PCI Express Hotplug driver
          [*] Support for PCI Hotplug --->
                [*]   ACPI PCI Hotplug driver
        Device Drivers --->
          <*> Thunderbolt support

## [References]

1.  [[[↑](#cite_ref-1)] [Knuth Posern. [\[PATCH\] thunderbolt: Allow loading of module on recent Apple MacBooks with thunderbolt 2 controller](https://lkml.org/lkml/2015/9/20/150), [LKML](https://lkml.org/), September 20th, 2015. Retrieved on December 3rd, 2015.]]