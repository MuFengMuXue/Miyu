This page lists common USB to Ethernet network adapters and provides details for enabling Linux kernel support.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel configuration]](#Kernel_configuration)
-   [[2] [Working devices]](#Working_devices)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel configuration]

[KERNEL] **`CONFIG_USB_USBNET`**

    Device Drivers --->
      [*] Network device support --->
        <*> USB Network Adapters --->
          <M> Multi-purpose USB Networking Framework
            <M> (Module from table)

If there is an USB HUB inside the adapter, this should work directly if your USB Controller is configured correctly (see the [USB Guide](https://wiki.gentoo.org/wiki/USB/Guide "USB/Guide") article).

** Note**\
For more complete Ethernet kernel configuration see the [Ethernet](https://wiki.gentoo.org/wiki/Ethernet "Ethernet") article.

## [Working devices]

The table below lists USB Fast Ethernet adapters working with kernel-modules:

  ----------- ---------------------------------------------------- --------------------------------------------------------------------------------------------------------- ------------------ -----------------------------
  ID          Product Name                                         [lsusb] Name   Chipset            Module
  0fe6:9700   1 Port USB Network with 3 Port USB HUB               Kontron DM9601 Fast Ethernet Adapter                                                                      Davicom DM9601     USB_NET_DM9601
  2357:0602   TP-Link UE200 USB 2.0 to 100Mbps adapter             TP-Link                                                                                                   Realtek RTL8152B   CONFIG_USB_RTL8152
  0bda:8153   Anker 3-Port USB 3.0 Hub with Ethernet               Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter                                              Realtek RTL8153    CONFIG_USB_RTL8152
  0b95:1790   TP-Link UE300C USB Type-C to RJ45 Gigabit Ethernet   ASIX Electronics Corp. AX88179 Gigabit Ethernet                                                           Realtek RTL8153    CONFIG_USB_NET_AX88179_178A
  ----------- ---------------------------------------------------- --------------------------------------------------------------------------------------------------------- ------------------ -----------------------------

## [See also]

-   [USB Audio](https://wiki.gentoo.org/wiki/USB_Audio "USB Audio") --- details the necessary system configuration to support **speakers** and **microphones** connected to the system via USB.