**Resources**

[[]][Official Support Page](https://www.dell.com/support/home/en-us/product-support/product/latitude-d810/overview)

[[]][Hardware Maintenance Manual](https://downloads.dell.com/manuals/all-products/esuprt_laptop/esuprt_latitude_laptop/latitude-d810_service%20manual_en-us.pdf)

[[]][User Guide](https://dl.dell.com/manuals/all-products/esuprt_laptop/esuprt_latitude_laptop/latitude-d810_users-guide_en-us.pdf)

## Contents

-   [[1] [Dell Latitude D810]](#Dell_Latitude_D810)
    -   [[1.1] [Hardware]](#Hardware)
    -   [[1.2] [Choosing the right install medium]](#Choosing_the_right_install_medium)
    -   [[1.3] [CPU]](#CPU)
    -   [[1.4] [Video]](#Video)
    -   [[1.5] [Drive Controller]](#Drive_Controller)
    -   [[1.6] [Audio]](#Audio)
    -   [[1.7] [USB]](#USB)
    -   [[1.8] [Ethernet]](#Ethernet)
    -   [[1.9] [Wireless]](#Wireless)

## [Dell Latitude D810]

This article will describe configuration and kernel options to make make the hardware work in Gentoo.

**Work in progress.**

### [Hardware]

*The below list is based on the machine this configuration was done one. There might be some variance.*

-   CPU: Intel Pentium M 2.0 GHz
-   Video: Radeon X600 Graphics
-   Display: 15.4\" 1920x1200 display
-   Audio: 82801FB/FBM/FR/FW/FRW (ICH6 Family) AC\'97 Audio Controller
-   USB: Intel Corporation 82801FB/FBM/FR/FW/FRW (ICH6 Family) USB UHCI
-   USB: Intel Corporation 82801FB/FBM/FR/FW/FRW (ICH6 Family) USB2 EHCI Controller
-   Wired network: Broadcom Corporation NetXtreme BCM5751 Gigabit Ethernet PCI Express
-   Wireless network: Intel Corporation PRO/Wireless 2915ABG \[Calexico2\] Network Connection

### [Choosing the right install medium]

The D810 has a modular bay that could contain a DVD/CD drive, floppy drive or less useful to the install, a battery. Using a CD or DVD is fine, but the machine also supports booting from USB.

If your boot order is not already accommodating, tap [F2] ([F12]?) at the POST screen to get a menu of available choices and boot the install media.

### [CPU]

The CPU is an Intel Pentium M.

[KERNEL] **Processor Support**

    Processor type and features --->
        Process family (Pentium M)

### [Video]

Video device is either an ATI (AMD) Radeon X300 or X600. The [R300_cp.bin] firmware is used for both.

[KERNEL] **Video Device Support**

    Device Drivers --->
        Generic Driver Options --->
            (radeon/R300_cp.bin) External firmware blobs to build into the kernel binary
        Graphics support --->
            <*> ATI Radeon

### [Drive Controller]

[KERNEL] **Drive Controller Support**

    Device Drivers --->
        <*> Serial ATA and Parallel ATA drivers --->
            <*> Intel ESB, ICH, PIIX3, PIIX4 PATA/SATA support

\

### [Audio]

[KERNEL] **Audio Support**

    Device Drivers --->
        <*> Sound card support --->
            <*> Advanced Linux Sound Architecture --->
                [*] PCI sound devices --->
                    <*> Intel/SiS/nVidia/AMD/ALi AC97 Controller

### [USB]

[KERNEL] **USB Support**

    Device Drivers --->
        [*] USB support
            <*> EHCI HCD (USB 2.0) support
            <*> UHCI HDC (most Intel and VIA) support

### [Ethernet]

[KERNEL] **Ethernet Support**

    Device Drivers --->
        [*] Network devices support --->
            [*] Ethernet driver support --->
                [*] Broadcom devices
                    <*> Broadcom Tigon3 support

### [Wireless]

[KERNEL] **Wireless Networking Support**

    Device Drivers --->
        [*] Network devices support --->
            [*] Wireless LAN --->
                <*> Intel PRO/Wireless 2200BG and 2915ABG Network Connection