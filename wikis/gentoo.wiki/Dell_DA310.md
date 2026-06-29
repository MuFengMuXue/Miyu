**Resources**

[[]][Home](https://www.dell.com/support/product-details/en-us/product/usb-c-mobile-adapter-da310/overview)

**Resources**

[[]][Official documentation](https://dl.dell.com/content/manual84584788-dell-pro-7-in-1-usb-c-mobile-adapter-da310-user-s-guide.pdf)

The DA310 is a compact 7-port USB-C to USB-C, HDMI, DisplayPort, VGA, Ethernet and USB 3.2 adapter by Dell. It is fully compatible with the latest Linux kernels.

## Contents

-   [[1] [Status]](#Status)
    -   [[1.1] [Standard]](#Standard)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)
-   [[5] [References]](#References)

## [Status]

  ------------------------ ------------
  **Port/Functionality**   **Status**
  Male USB Type-C          Works
  USB Type-C               Works
  Thunderbolt 3 Hotplug    Works
  USB 3.2                  Works
  Ethernet                 Works
  HDMI                     Works
  DisplayPort              Works
  VGA                      Works
  ------------------------ ------------

### [Standard]

  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------ ------------------ ------------ ---------------- --------------------------------------------------------------
  Device                     Make/model                                                                                                                         Status   Vendor ID / Product ID                                                                                 Kernel driver(s)   Firmware     Kernel version   Notes
  Gigabit Ethernet Adapter   [`Realtek RTL8153`](https://www.realtek.com/en/products/communications-network-ics/item/rtl8153)   Works    [`0bda:8153`](https://cateee.net/lkddb/web-lkddb/USB_RTL8152.html)     RTL8152            rtl8153b-2   6.16.12          Enable kernel option `USB_RTL8152` in the kernel.
  USB 2.0 Hub                Fresco Logic Frescologic                                                                                                           Works    [`1d5c:5510`](https://linux-hardware.org/index.php?id=usb:1d5c-5510)   HUB (usbcore)      N/A          6.16.12
  USB 3.1 Gen. 2 Hub         Fresco Logic Frescologic                                                                                                           Works    [`1d5c:5500`](https://linux-hardware.org/index.php?id=usb:1d5c-5500)   HUB (usbcore)      N/A          6.16.12
  Dell DA310                 Dell Computer Corp.                                                                                                                Works    [`413c:c010`](https://linux-hardware.org/?id=usb:413c-c010)            usbhid             N/A          6.16.12          Enable kernel option `USB_HID` in the kernel.
  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------- -------- ------------------------------------------------------------------------------------------------------ ------------------ ------------ ---------------- --------------------------------------------------------------

## [Installation]

### [Kernel]

[KERNEL]

    Device Drivers --->
      Generic Driver Options  --->
        Firmware loader --->
          -*- Firmware loading facility
          () Build named firmware blobs into the kernel binary
          (/lib/firmware) Firmware blobs root directory
      [*] HID support  --->
          HID support  --->
          <*>   USB HID transport layer
      [*] PCI support  --->
        [*]   PCI Express Port Bus support
        [*]     PCI Express Hotplug driver
        [*] Support for PCI Hotplug  --->
            [*]   ACPI PCI Hotplug driver
      [*] USB support  --->
        <*>   USB Type-C Support  --->
          <*>   USB Type-C Port Controller Manager
          <*>     Type-C Port Controller Interface driver
          <*>   USB Type-C Connector System Software Interface driver
          <*>     UCSI ACPI Interface Driver
                USB Type-C Alternate Mode drivers  --->
            <*> DisplayPort Alternate Mode driver
            <*> Thunderbolt3 Alternate Mode driver
      [*] Network device support --->
        <*> USB Network Adapters --->
          <*>   Realtek RTL8152/RTL8153 Based USB Ethernet Adapters

### [Emerge]

In order to enable the security levels for Thunderbolt 3, [[[sys-apps/bolt]](https://packages.gentoo.org/packages/sys-apps/bolt)[]] needs to be installed:

`root `[`#`]`emerge --ask sys-apps/bolt`

## [See also]

-   [USB/Guide#USB_Type-C_and_Thunderbolt](https://wiki.gentoo.org/wiki/USB/Guide#USB_Type-C_and_Thunderbolt "USB/Guide")
-   [USB to Ethernet Adapter](https://wiki.gentoo.org/wiki/USB_to_Ethernet_Adapter "USB to Ethernet Adapter")

## [External resources]

-   [https://gitlab.freedesktop.org/bolt/bolt](https://gitlab.freedesktop.org/bolt/bolt)

## [References]