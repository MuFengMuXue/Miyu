[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Android_USB_tethering&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Tethering "wikipedia:Tethering")

[[]]This article has some todo items:\

-   make section USB tethering more generic
-   do NOT add Bluetooth tethering
-   verify HW list

**Tethering**, or phone-as-modem (PAM) is the sharing of a mobile device\'s Internet connection with other connected computers. Connection of a mobile device with other devices can be done over wireless LAN ([Wi-Fi](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi")), over [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") or by physical connection using a cable, for example through USB. The focus of this article is **USB tethering** with **Android** devices.

Android mobile phones can behave as an external network interface usbN, connected via the USB infrastructure. The usbN interface is in turn connected to the mobile phone LAN, providing DHCP server, DNS server, and a gateway.

That is how a mobile phone can provide an Internet connection to another device.

Android phones are already equipped to provide this functionality. Simply connect the USB cable and go to [Settings -\> Wireless settings -\> Tethering -\> Tethering USB].

What you need is some kernel and network configuration on the other side (e.g. a laptop).

## Contents

-   [[1] [Kernel]](#Kernel)
-   [[2] [Testing]](#Testing)
-   [[3] [Connecting]](#Connecting)
    -   [[3.1] [Manually]](#Manually)
    -   [[3.2] [Permanent configuration]](#Permanent_configuration)
    -   [[3.3] [Checks]](#Checks)
-   [[4] [Advanced network settings]](#Advanced_network_settings)
-   [[5] [Tested devices]](#Tested_devices)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Kernel]

Selected kernel modules can either be built-in build as loadable linux kernel modules.

[KERNEL] **Required kernel options**

     Device Drivers --->
       [*] Network device support Search for <code>CONFIG_NETDEVICES</code> to find this item. --->
           <M> USB Network Adapters Search for <code>CONFIG_USB_NET_DRIVERS</code> to find this item. --->
               <M> Multi-purpose USB Networking Framework Search for <code>CONFIG_USB_USBNET</code> to find this item.
                   <M>  CDC Ethernet support (smart devices such as cable modems) Search for <code>CONFIG_USB_NET_CDCETHER</code> to find this item.
                   <M>  CDC EEM support Search for <code>CONFIG_USB_NET_CDC_EEM</code> to find this item.
                   <M>  CDC NCM support Search for <code>CONFIG_USB_NET_CDC_NCM</code> to find this item.
                   <M>  Host for RNDIS and ActiveSync devices Search for <code>CONFIG_USB_NET_RNDIS_HOST</code> to find this item.
                   <M>  Simple USB Network Links (CDC Ethernet subset) Search for <code>CONFIG_USB_NET_CDC_SUBSET</code> to find this item.
                        [*] Embedded ARM Linux links (iPaq, ...) Search for <code>CONFIG_USB_ARMLINUX</code> to find this item.
       [*] USB support Search for <code>CONFIG_USB_SUPPORT</code> to find this item.  --->
           <M> USB Modem (CDC ACM) support Search for <code>CONFIG_USB_ACM</code> to find this item.
           <M> USB Wireless Device Management support Search for <code>CONFIG_USB_WDM</code> to find this item.
           <M> USB Gadget Support Search for <code>CONFIG_USB_GADGET</code> to find this item.  ---->
                   USB Gadget precomposed configurations --->
                       <M> Ethernet Gadget (with CDC Ethernet support) Search for <code>CONFIG_USB_ETH</code> to find this item.
                       [*]   RNDIS support Search for <code>CONFIG_USB_ETH_RNDIS</code> to find this item.
                       [*]   Ethernet Emulation Model (EEM) support Search for <code>CONFIG_USB_ETH_EEM</code> to find this item.
                       <M> Network Control Model (NCM) support Search for <code>CONFIG_USB_G_NCM</code> to find this item.

\

** Important**\
RNDIS linux module is being deprecated and will be removed from the Linux Kernel in favor Network Control Model (NCM), but it is used by majority of devices nowadays (2023) and up to now the only way to configure working USB tethering for old Android devices.^[\[1\]](#cite_note-1)^ For more recent devices (Android 14 era) try to use \"Network Control Model (NCM) support\" module first.

For configuration check [this thread](https://forums.gentoo.org/viewtopic-t-843255.html) and [here](https://forums.gentoo.org/viewtopic-t-1095940.html).

## [Testing]

After connecting an Android device following events appear in the dmesg:

`user `[`$`]`dmesg`

    usb 1-7: New USB device found, idVendor=18d1, idProduct=4e13
    usb 1-7: New USB device strings: Mfr=1, Product=2, SerialNumber=3
    usb 1-7: Product: Nexus One
    usb 1-7: Manufacturer: Google, Inc.
    usb 1-7: SerialNumber: HT9CSP803294
    usb 1-7: usb_probe_device
    usb 1-7: configuration #1 chosen from 1 choice
    usb 1-7: adding 1-7:1.0 (config #1, interface 0)
    rndis_host 1-7:1.0: usb_probe_interface
    rndis_host 1-7:1.0: usb_probe_interface - got id
    rndis_host 1-7:1.0: usb0: register 'rndis_host' at usb-0000:00:1d.7-7, RNDIS device, ea:61:37:88:a2:e5
    usb 1-7: adding 1-7:1.1 (config #1, interface 1)
    drivers/usb/core/inode.c: creating file '004'
    hub 1-0:1.0: state 7 ports 8 chg 0000 evt fe80
    uhci_hcd 0000:00:1d.0: reserve dev 2 ep81-INT, period 8, phase 4, 93 us
    usb 1-7: link qh32-0001/ffff88021aa4bc80 start 1 [1/0 us]
    usb0: no IPv6 routers present

`user `[`$`]`ip link`

If you see `usbN` interface (N may be a different number) you are all set.

## [Connecting]

Since the mobile phone LAN changes its addresses, you need a DHCP client to configure the usbN device.

If you are on a laptop, you probably have a DHCP client. If not, emerge [[[net-misc/dhcpcd]](https://packages.gentoo.org/packages/net-misc/dhcpcd)[]]:

`root `[`#`]`emerge --ask net-misc/dhcpcd`

### [Manually]

Simply run [dhcpcd] after plug/mobile activation:

`root `[`#`]`dhcpcd usb0`

### [Permanent configuration]

Edit your [/etc/conf.d/net] to have a permanent, automatic activation of the interface.

[FILE] **`/etc/conf.d/net`**

    # ...
    config_usb0="dhcp"
    # ...

Once plugged in and activated on the mobile phone side, the usb0 will be up and configured.

### [Checks]

Run the usual checks to verify the connection:

`root `[`#`]`ip link show usb0 `

`root `[`#`]`ip route `

`root `[`#`]`cat /etc/resolv.conf `

## [Advanced network settings]

DHCP is very quick, but the default settings don\'t give you as much freedom as you may want.

A possible scenario is that you are in a corporate, protected LAN context that doesn\'t provide Internet connection but you need to stay connected to have access to some Intranet resource or you have a free but limited connection (a public WiFi network allowing HTTP only, an evil firewall, etc.). Since mobile connections could be expensive, you could want to save money by tethering only when needed.

Here is a handful of examples pertaining to DHCP usage.

If you want to limit the information set by DHCP, you can fine-tune its behavior:

`root `[`#`]`dhcpcd --nogateway --nohook resolv.conf --nohook hostname usb0`

This will let your default gateway, [resolv.conf] and hostname as they are, letting you provide extra info by hand:

`root `[`#`]`ip route add my_sshd_remote_host_IP scope host dev usb0`

Finally, you can permanently configure your USB network interface:

[FILE] **`/etc/conf.d/net`**

    config_usb0="dhcp"
    dhcpcd_usb0="--nogateway --nohook resolv.conf --nohook hostname"
    # Special hosts
    postup()
     ]]; then
            ip route add my_sshd_remote_host_IP scope host dev usb0
        fi
    }

Generally, you can avoid every DHCP setting but gather them with:

`root `[`#`]`dhcpcd -U usb0`

Then you can set what you want in the `postup` hook.

## [Tested devices]

Tested devices list.

  ----------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------
  Device                              OS                                                                                                                                                                                                                                                                                                                                           Notes
  Fairphone 2                         Fairphone OS Android 6.0.1, build no FP2-gms-18.04.1                                                                                                                                                                                                                                                                                         `rndis_host` required
  Google Nexus One                    Android 2.3.6 build GRK39F
  Google Nexus 4                      Android 4.3 build JWR66Y                                                                                                                                                                                                                                                                                                                     `rndis_host` required
  Google Pixel 3                      Android 12                                                                                                                                                                                                                                                                                                                                   `rndis_host` required
  Google Pixel 6                      Android 16                                                                                                                                                                                                                                                                                                                                   `cdc_ncm` required (instead of `rndis_host`)
  Google Pixel 8 Pro                  Android 16                                                                                                                                                                                                                                                                                                                                   `cdc_ncm` required
  HTC Desire HD                       Android 2.3.6 Stock Rom build and Android 4.4.4 (unofficial CyanogenMod 11)                                                                                                                                                                                                                                                                  `rndis_host` required
  HTC One M7                          Sense 5.5, Android 4.3, Software number 3.62.401.1,HTC SDK API level 5.65                                                                                                                                                                                                                                                                    rndis_host, cdc_ether and usbnet modules ONLY to get it to work
  Huawei Honor 4x                     unofficial CyanogenMod 11 / Android 4.4.4                                                                                                                                                                                                                                                                                                    `rndis_host` required
  Huawei Honor View 10 Lite           Model JSN-10L, Android 10                                                                                                                                                                                                                                                                                                                    autoloads rndis_host, cdc_ether and usbnet modules; it works flawlessly
  Huawei P10                          Android 8.0.0 stock
  LG P350                             Android 2.2.1 build FRG83
  LG E400                             Android 2.3.6 build GRK39F
  LG L7 P705                          Android 4.1.2 build JZO54K
  Motorola Defy                       Android 2.3.7 Cyanogenmod 7
  Motorola Moto G 4G 2013 (1st Gen)   Android 5.1                                                                                                                                                                                                                                                                                                                                  `rndis_host` required
  OnePlus One                                                                                                                                                                                                                                                                                                                                                                      `rndis_host` required
  OnePlus 3T                                                                                                                                                                                                                                                                                                                                                                       `rndis_host` required
  PINE64                              [PinePhone](https://wiki.pine64.org/wiki/PinePhone) **([pine64-pinephone](https://wiki.postmarketos.org/wiki/PINE64_PinePhone_(pine64-pinephone)) [postmarketOS](https://postmarketos.org/) GNU/Linux 5.17.0-rc8 non Android based phone**   `rndis_host` required
  Samsung Galaxy Grand Neo+ Duos      GT-I9060I / Android 4.4.4                                                                                                                                                                                                                                                                                                                    only needed rndis_host - cdc_ether - usbnet modules
  Samsung Galaxy Nexus i9250          Android 4.0.1 ITL41D, Android 6.0.1 (CyanogenMod 13)                                                                                                                                                                                                                                                                                         `rndis_host` required
  Samsung Galaxy S i9000
  Samsung Galaxy S2
  Samsung Galaxy S3                   GT-I9300 Android 4.3 Stock Rom
  Samsung Galaxy S4 Mini Duos         GT-I9192, unofficial CyanogenMod 12.1 / Android 5.1                                                                                                                                                                                                                                                                                          `rndis_host` required
  Samsung Galaxy S5                   Android 6.0.1                                                                                                                                                                                                                                                                                                                                `rndis_host` required
  Samsung Galaxy S6                   Android 7.0                                                                                                                                                                                                                                                                                                                                  `rndis_host` required
  Samsung Galaxy S7                                                                                                                                                                                                                                                                                                                                                                `rndis_host` required
  Samsung Galaxy Tab 2 7.0            Android 4.1.2
  Sony Xperia Go                      St27i Android 4.1.2 Stock Rom build no 6.2.A.1.100                                                                                                                                                                                                                                                                                           `rndis_host` required
  Sony Xperia X Compact               Android 8.0.0, build no 34.4.A.2.118                                                                                                                                                                                                                                                                                                         needed rndis_host module and \"Embedded ARM Linux links\" (CONFIG_USB_ARMLINUX) on kernel 4.16.18
  Sony Xperia XZ Premium              G8142 Stock Android 8.0, build no 47.1.A.8.49                                                                                                                                                                                                                                                                                                `rndis_host` required
  Wileyfox Storm                      CyanogenOS 13.1.5 - Android 6.0.1
  Xiaomi Redmi 5                      MIUI 9, 10 and 11
  Xiaomi Pad 5 Pro 5G                 Xiaomi Hyper OS 1.0.3.0 (Android 13)
  ----------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------

## [See also]

-   Ethernet over IP crossreferece [https://en.wikipedia.org/wiki/Ethernet_over_USB](https://en.wikipedia.org/wiki/Ethernet_over_USB)
-   [Project:Android](https://wiki.gentoo.org/wiki/Project:Android "Project:Android")
-   Reverse tethering approach workstation server- android client [https://groups.google.com/g/linux.gentoo.user/c/v8zfJmoJT5c](https://groups.google.com/g/linux.gentoo.user/c/v8zfJmoJT5c)
-   really old gentoo reference using RNDIS [http://hcx-security.org/blog/?p=328](http://hcx-security.org/blog/?p=328)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://lkml.org/lkml/2022/11/23/1502](https://lkml.org/lkml/2022/11/23/1502)]]