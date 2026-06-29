**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Power_management "wikipedia:Power management")

[[]][Guide](https://wiki.gentoo.org/wiki/Power_management/Guide "Power management/Guide")

This article describes methods to save energy for longer battery runtimes, a quieter computer, lower power bills, and an environmentally friendly impact.

## Contents

-   [[1] [Configuration]](#Configuration)
    -   [[1.1] [UEFI]](#UEFI)
    -   [[1.2] [Kernel and Userspace]](#Kernel_and_Userspace)
    -   [[1.3] [Power modes]](#Power_modes)
-   [[2] [See also]](#See_also)
-   [[3] [External resources]](#External_resources)

## [Configuration]

### [UEFI]

The [UEFI](https://wiki.gentoo.org/wiki/UEFI "UEFI") or [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") might provide settings to save power, however, the machine must reboot to apply changes this way. It\'s better to make changes to the kernel and/or make use of userspace utilities as (most) changes in the machine\'s firmware can be overridden and done without rebooting.

Changes include, but not limited to enabling/disabling:

-   Processor cores
-   [USB](https://wiki.gentoo.org/wiki/USB "USB") ports
-   [Ethernet](https://wiki.gentoo.org/wiki/Ethernet "Ethernet") network devices
-   [Wireless](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi") network devices
-   [Sound cards](https://wiki.gentoo.org/wiki/Category:Sound_devices "Category:Sound devices")
-   [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") controllers
-   Serial ports
-   Parallel ports

### [Kernel and Userspace]

Below are links to sub-articles that explain what changes to make to increase power savings; they include changes to the kernel and use userspace utilities.

-   [CPU / Processor](https://wiki.gentoo.org/wiki/Power_management/Processor "Power management/Processor")
-   Display
-   [PCI](https://wiki.gentoo.org/wiki/Power_management/PCI "Power management/PCI")
-   [USB](https://wiki.gentoo.org/wiki/Power_management/USB "Power management/USB")
-   [Disk](https://wiki.gentoo.org/wiki/Power_management/Disk "Power management/Disk")
-   [Ethernet](https://wiki.gentoo.org/wiki/Power_management/Ethernet "Power management/Ethernet")
-   [Wi-Fi](https://wiki.gentoo.org/wiki/Power_management/Wi-Fi "Power management/Wi-Fi")
-   [Bluetooth](https://wiki.gentoo.org/wiki/Power_management/Bluetooth "Power management/Bluetooth")
-   [Soundcard](https://wiki.gentoo.org/wiki/Power_management/Soundcard "Power management/Soundcard")
-   [Hardware Acceleration](https://wiki.gentoo.org/wiki/Power_management/Hardware_Acceleration "Power management/Hardware Acceleration")

### [Power modes]

-   [Suspend and hibernate](https://wiki.gentoo.org/wiki/Suspend_and_hibernate "Suspend and hibernate")
-   [Laptop](https://wiki.gentoo.org/wiki/Power_management/Guide "Power management/Guide")

## [See also]

-   [PowerTOP](https://wiki.gentoo.org/wiki/PowerTOP "PowerTOP") --- a Linux utility that can monitor and display a system\'s electrical power usage.

## [External resources]

-   [https://www.linux.com/news/power-saving-linux](https://www.linux.com/news/power-saving-linux) - An article that provides generic explanations and advice for power saving on Linux.