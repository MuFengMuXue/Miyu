This page contains [[changes](https://wiki.gentoo.org/index.php?title=Wi-Fi&oldid=1402109&diff=1430156)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Wi-Fi/de "Wi-Fi/de (1% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Wi-Fi/es "Wifi (32% translated)")
-   [français](https://wiki.gentoo.org/wiki/Wi-Fi/fr "Wi-Fi (97% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Wi-Fi/hu "Wi-Fi (100% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/Wi-Fi/cs "Wi-Fi/cs (1% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Wi-Fi/ru "Wi-Fi (99% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Wi-Fi/zh-cn "Wi-Fi (53% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Wi-Fi/ja "Wi-Fi (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Wi-Fi/ko "Wifi/ko (28% translated)")

**Resources**

[[]][Home](https://wireless.wiki.kernel.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Wi-Fi "wikipedia:Wi-Fi")

This article describes the setup of a [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi "wikipedia:Wi-Fi") (wireless) network device.

## Contents

-   [[1] [Wi-Fi during installation]](#Wi-Fi_during_installation)
-   [[2] [Hardware detection]](#Hardware_detection)
-   [[3] [Kernel]](#Kernel)
    -   [[3.1] [IEEE 802.11]](#IEEE_802.11)
    -   [[3.2] [WEXT]](#WEXT)
    -   [[3.3] [Device drivers]](#Device_drivers)
    -   [[3.4] [LED support]](#LED_support)
-   [[4] [Firmware]](#Firmware)
-   [[5] [Wireless supplicant]](#Wireless_supplicant)
-   [[6] [Testing]](#Testing)
    -   [[6.1] [/sys file system]](#.2Fsys_file_system)
    -   [[6.2] [ip command]](#ip_command)
    -   [[6.3] [ifconfig command]](#ifconfig_command)
    -   [[6.4] [iw command]](#iw_command)
    -   [[6.5] [dmesg]](#dmesg)
-   [[7] [Troubleshooting]](#Troubleshooting)
    -   [[7.1] [Finding missing firmware]](#Finding_missing_firmware)
    -   [[7.2] [Wi-Fi adapter cannot find and connect to a 5 GHz network]](#Wi-Fi_adapter_cannot_find_and_connect_to_a_5_GHz_network)
    -   [[7.3] [Forum threads]](#Forum_threads)
-   [[8] [See also]](#See_also)

## [Wi-Fi during installation]

If a Wi-Fi connection is needed while installing Gentoo, then it is recommended to use [NetworkManager](https://wiki.gentoo.org/wiki/NetworkManager "NetworkManager") which can be configured on the LiveGUI from the system tray, or from the minimal install CD, by running the [nmtui] and following the on-screen instructions.

## [[] Hardware detection]

First detect the Wi-Fi controllers. [[lspci](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection")] or [[lsusb](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection")] are command-line tools that can be used for this task.

If a Linux (LiveCD/USB) is booted that makes a Wi-Fi connection:

`root `[`#`]`lspci -k`

The driver will be identified on one of the lines starting with `Kernel driver in use:`.

If the booted system does not make a Wi-Fi connection, then obtain a full list of hardware identifiers from the current system. This list can be used to identify the proper driver later:

`root `[`#`]`lspci -n`

Copy the list of PCIID\'s that the command produces.

For USB devices, a similar approach can be taken. First obtain the list of detected USB devices on the system:

`user `[`$`]`lsusb`

This command produces the PCI ID, manufacturer, make, model, and/or chipset of every USB device attached to the system. Of these, the chipset may be the most useful information. Searching the web for *linuxwireless.org \<chipset\>* is often the shortest way to find a USB NIC driver and firmware name.

Alternatively, [lshw] can be used to obtain the necessary information:

`root `[`#`]`lshw | grep -i driver | perl -pe 's/^.*driver=(\S+).*$/$1/g;' | sort -u`

This command produces a list of all drivers, regardless of the device being PCI or USB based.

## [Kernel]

With the drivers identified, it is time to configure the Linux kernel.

### [[] IEEE 802.11]

Activate at least [cfg80211](https://wireless.wiki.kernel.org/en/developers/documentation/cfg80211) (`CONFIG_CFG80211`) and [mac80211](https://wireless.wiki.kernel.org/en/developers/documentation/mac80211) (`CONFIG_MAC80211`).

[KERNEL] **linux-4.19 example**

    [*] Networking support  --->
        [*] Wireless  --->
            <M>   cfg80211 - wireless configuration API
            [ ]     nl80211 testmode command
            [ ]     enable developer warnings
            [ ]     cfg80211 certification onus
            [*]     enable powersave by default
            [ ]     cfg80211 DebugFS entries
            [ ]     support CRDA
            [ ]     cfg80211 wireless extensions compatibility
            <M>   Generic IEEE 802.11 Networking Stack (mac80211)
            [*]   Minstrel
            [*]     Minstrel 802.11n support
            [ ]       Minstrel 802.11ac support
                  Default rate control algorithm (Minstrel)  --->
            [ ]   Enable mac80211 mesh networking (pre-802.11s) support
            -*-   Enable LED triggers
            [ ]   Export mac80211 internals in DebugFS
            [ ]   Trace all mac80211 debug messages
            [ ]   Select mac80211 debugging features  ----

Minstrel and its 802.11n support is a [rate control algorithm](https://wireless.wiki.kernel.org/en/developers/Documentation/mac80211/RateControl/minstrel). Some wireless drivers might require it enabled.

** Important**\
In case the **wireless configuration API** (`CONFIG_CFG80211`) is built into the kernel (`<*>`) instead as a module (`<M>`), the driver won\'t be able to load [regulatory.db] from [/lib/firmware] resulting in broken regulatory domain support. Please set `CONFIG_CFG80211=m` or add [regulatory.db] and [regulatory.db.p7s] (from [[[net-wireless/wireless-regdb]](https://packages.gentoo.org/packages/net-wireless/wireless-regdb)[]]) to `CONFIG_EXTRA_FIRMWARE`.

### [WEXT]

The \"cfg80211 wireless extensions compatibility\" option aka WEXT will support old [wireless-tools](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Wireless#Wireless_tools "Handbook:AMD64/Networking/Wireless") and [iwconfig].

[KERNEL]

    [*] Networking support  --->
        [*] Wireless  --->
            [*]     cfg80211 wireless extensions compatibility

### [Device drivers]

Next the right set of corresponding kernel options need to be enabled, based on the drivers and hardware detected previously. The [recommendation](https://forums.gentoo.org/viewtopic-p-7640140.html#7640140) is to build [drivers as modules](https://wiki.gentoo.org/wiki/Kernel_Modules#Compile-in-kernel_modules_vs_Loadable_kernel_modules_.28LKMs.29 "Kernel Modules"). Also be sure to enable AES cipher support in the kernel if the wireless network uses WPA or WPA2 encryption.

[KERNEL]

    Device Drivers  --->
        [*] Network device support  --->
            [*] Wireless LAN  --->

                Select the driver for your Wifi network device, e.g.:
                <M> Broadcom 43xx wireless support (mac80211 stack) (b43)
                [M]    Support for 802.11n (N-PHY) devices
                [M]    Support for low-power (LP-PHY) devices
                [M]    Support for HT-PHY (high throughput) devices
                <M> Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                <M>    Intel Wireless WiFi DVM Firmware support
                <M>    Intel Wireless WiFi MVM Firmware support
                <M> Intel Wireless WiFi 4965AGN (iwl4965)
                <M> Intel PRO/Wireless 3945ABG/BG Network Connection (iwl3945)
                <M> Ralink driver support  --->
                    <M>   Ralink rt27xx/rt28xx/rt30xx (USB) support (rt2800usb)

    -*- Cryptographic API --->
        Accelerated Cryptographic Algorithms for CPU (x86)  --->
           <*> Ciphers: AES, modes: ECB, CBC, CTS, CTR, XTR, XTS, GCM (AES-NI)

** Important**\
In case the driver is built into the kernel (`<*>`) instead of as a module (`<M>`), then the firmware needs to be built [into the kernel](https://wiki.gentoo.org/wiki/Kernel_Modules#Compile-in-kernel_modules_vs_Loadable_kernel_modules_.28LKMs.29 "Kernel Modules") as well.\
Do not forget to [rebuild the kernel](https://wiki.gentoo.org/wiki/Kernel/Rebuild "Kernel/Rebuild") after changing its configuration.

### [LED support]

To enable LED triggers for different packet receive/transmit events, compile the kernel with the following options:

[KERNEL]

    Device Drivers  --->
        [*] LED Support  --->
            <*>   LED Class Support

    [*] Networking support  --->
        [*] Wireless  --->
            [*] Enable LED triggers

## [Firmware]

In addition to the kernel driver, some chipsets (especially modern ones) also require firmware. If required, locate it on the following list and install it:

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

  ----------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Wi-Fi device                                                                                                                                    Driver                                                                                                                                                                                                                                                Firmware                                                                                                                                                                                                                                                                                                                                                                                                        Note
  Atheros AR9271 & AR7010                                                                                                                         ath9k_htc                                                                                                                                                                                                                                             [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]
  Broadcom 43xx wireless support                                                                                                                  b43 / b43legacy                                                                                                                                                                                                                                       [[[sys-firmware/b43-firmware]](https://packages.gentoo.org/packages/sys-firmware/b43-firmware)[]]               Aircrack-ng ready, most probably the best choice [when a bcm43xx device is supported](https://wireless.wiki.kernel.org/en/users/drivers/b43#Supported_devices)
  Broadcom PCIe and SDIO/USB devices                                                                                                              [brcmsmac](https://wireless.wiki.kernel.org/en/users/drivers/brcm80211?s%5b%5d=brcmsmac) / [brcmfmac](https://wireless.wiki.kernel.org/en/users/drivers/brcm80211?s%5b%5d=brcmfmac)   [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]               Lacks powersaving, LED support and [other features](https://wireless.wiki.kernel.org/en/users/drivers/brcm80211#To_be_done_for_softmac_driver)
  Broadcom 43xx wireless support                                                                                                                  wl                                                                                                                                                                                                                                                    [[[net-wireless/broadcom-sta]](https://packages.gentoo.org/packages/net-wireless/broadcom-sta)[]]               Proprietary, no AP or Monitor modes, [Comparison of bcm43xx drivers](https://wireless.wiki.kernel.org/en/users/drivers/b43#Comparison_of_recent_drivers)
  Intel PRO/Wireless 2200BG                                                                                                                       ipw2200                                                                                                                                                                                                                                               [[[sys-firmware/ipw2200-firmware]](https://packages.gentoo.org/packages/sys-firmware/ipw2200-firmware)[]]
  [Intel PRO/Wireless 3945ABG/BG](https://wiki.gentoo.org/wiki/Intel_Corporation_PRO/Wireless_3945ABG "Intel Corporation PRO/Wireless 3945ABG")   [iwlegacy](https://wiki.gentoo.org/wiki/Intel_Corporation_PRO/Wireless_3945ABG#Device_driver_iwl3945 "Intel Corporation PRO/Wireless 3945ABG")                                                                                                        [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]
  Intel Wireless WiFi 4965AGN                                                                                                                     iwl4965                                                                                                                                                                                                                                               [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]
  All other Intel Wireless devices                                                                                                                [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")                                                                                                                                                                                             [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]               See the [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") article for detailed instructions.
  [Qualcomm Atheros QCA6174](https://wiki.gentoo.org/wiki/Qualcomm_Atheros_QCA6174 "Qualcomm Atheros QCA6174")                                    ath10k_pci                                                                                                                                                                                                                                            ath10k-firmware                                                                                                                                                                                                                                                                                                                                                                                                 See [Qualcomm Atheros QCA6174](https://wiki.gentoo.org/wiki/Qualcomm_Atheros_QCA6174#Firmware "Qualcomm Atheros QCA6174")
  Ralink/MediaTek USB devices                                                                                                                     e.g. [rt2800usb](https://wireless.wiki.kernel.org/en/users/drivers/rt2800usb?s%5b%5d=rt2800usb)                                                                                                                       [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]
  Realtek RTL8191SE & RTL8192SE                                                                                                                   rtl8192se                                                                                                                                                                                                                                             [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]
  Realtek 8723AU/8723BU/8191EU/8192EU/8188EU/8188RU                                                                                               rtl8xxxu                                                                                                                                                                                                                                              [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]]               May need the `CONFIG_RTL8XXXU_UNTESTED` kernel option to find all devices. Only those verified by kernel developers are enabled by default.
  ----------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If the driver requires firmware but does not appear on the list, it will be necessary to download it manually and place it in [/lib/firmware].

## [Wireless supplicant]

If the wireless network is set up with WPA or WPA2, then a [wireless supplicant](https://en.wikipedia.org/wiki/Wireless_supplicant "wikipedia:Wireless supplicant") like [wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") or [iwd](https://wiki.gentoo.org/wiki/Iwd "Iwd") needs to be used. For more information on configuring wireless networking in Gentoo Linux, please read the [Wireless networking chapter](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Wireless "Handbook:AMD64/Networking/Wireless") in the Gentoo Handbook.

\

## [Testing]

After a reboot with the new kernel or after loading the modules, the device can be checked for availability by using following methods:

-   Using the [[/sys] file system](https://wiki.gentoo.org/wiki/Wifi/Testing#.2Fsys_file_system "Wifi/Testing")
-   Using the [[ip] command](https://wiki.gentoo.org/wiki/Wifi/Testing#ip_command "Wifi/Testing")
-   Using the [[ifconfig] command](https://wiki.gentoo.org/wiki/Wifi/Testing#ifconfig_command "Wifi/Testing")
-   Using the [[iw] command](https://wiki.gentoo.org/wiki/Wifi/Testing#iw_command "Wifi/Testing")

### [][[] /sys file system]

Get the device name by listing the [/sys/class/net] directory contents using [ls -al] or the [tree] command (provided by the [[[app-text/tree]](https://packages.gentoo.org/packages/app-text/tree)[]] package):

`user `[`$`]`tree /sys/class/net`

    /sys/class/net/
    ├── enp2s14 -> ../../devices/pci0000:00/0000:00:1e.0/0000:02:0e.0/net/enp2s14
    ├── lo -> ../../devices/virtual/net/lo
    ├── sit0 -> ../../devices/virtual/net/sit0
    └── wlp8s0 -> ../../devices/pci0000:00/0000:00:1c.0/0000:08:00.0/net/wlp8s0

### [[] ip command]

To obtain the device name and verify that the wireless card is detected, execute the following [[ip] command](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2"):

`user `[`$`]`ip addr`

    3: wlan0:   ...

A network card can be activated as follows:

`root `[`#`]`ip link set wlan0 up`

### [[] ifconfig command]

The [ifconfig] command is provided through the [[[sys-apps/net-tools]](https://packages.gentoo.org/packages/sys-apps/net-tools)[]] package. Use [ifconfig -a] to list all detected network cards, even those that are not enabled/active yet:

`user `[`$`]`ifconfig -a`

    wlan0     ...

A network card can be activated as follows:

`root `[`#`]`ifconfig -v wlan0 up`

    SIOCSIFFLAGS: Operation not possible due to RF-kill
    WARNING: at least one error occurred. (-1)

In this example, enabling the wireless card failed as a radio frequency kill state is set (usually to reduce power consumption and not connect by accident to a wireless network).

### [[] iw command]

If the wireless network card driver supports the nl80211 stack, then the [iw] command as offered by the [[[net-wireless/iw]](https://packages.gentoo.org/packages/net-wireless/iw)[]] package can show the detected wireless cards:

`root `[`#`]`iw dev`

       phy#0
        Interface wlan0
            ifindex 4
            type managed

### [dmesg]

Check the output of [dmesg].

`user `[`$`]`dmesg | grep -i -E 'xx:xx.x|wlan|iwl|80211'`

Be sure to replace

-   `xx:xx.x` with the identifier (PCIID) from [lspci](https://wiki.gentoo.org/wiki/Wi-Fi#Hardware_detection "Wi-Fi"),
-   `wlan` with the [network interface name](https://wiki.gentoo.org/wiki/Wi-Fi#Network_device_names "Wi-Fi") and
-   `iwl` with the name of the [Kernel driver in use](https://wiki.gentoo.org/wiki/Wi-Fi#Hardware_detection "Wi-Fi").

## [Troubleshooting]

** Note**\
When facing connectivity problems, enabling verbose/debug output from the relevant Wi-Fi software, combined with a [list of 802.11 Association Status codes and 802.11 Deauth Reason codes](https://community.cisco.com/t5/wireless-mobility-knowledge-base/802-11-association-status-802-11-deauth-reason-codes/ta-p/3148055), might provide relevant information.

### [Finding missing firmware]

At system boot, the kernel will attempt to probe firmware as appropriate for each card. This can be discovered by searching [dmesg] or [journalctl]\'s (systemd) output from the current boot.

`user `[`$`]`journalctl -b 0 --dmesg | grep -i firmware`

    Oct 05 14:51:09 maffbook kernel: Spectre V2 : Enabling Restricted Speculation for firmware calls
    Oct 05 14:51:09 maffbook kernel: ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
    Oct 05 14:51:09 maffbook kernel: sgx: [Firmware Bug]: Unable to map EPC section to online node. Fallback to the NUMA node 0.
    Oct 05 14:51:09 maffbook kernel: i915 0000:00:02.0: [drm] Finished loading DMC firmware i915/kbl_dmc_ver1_04.bin (v1.4)
    Oct 05 14:51:09 maffbook kernel: ACPI: video: [Firmware Bug]: ACPI(PEGP) defines _DOD but not _DOS
    Oct 05 14:51:09 maffbook kernel: iwlwifi 0000:00:14.3: loaded firmware version 46.6b541b68.0 9000-pu-b0-jf-b0-46.ucode op_mode iwlmvm
    Oct 05 14:51:09 maffbook kernel: psmouse serio1: elantech: assuming hardware version 4 (with firmware version 0x5f2001)
    Oct 05 14:51:09 maffbook kernel: Bluetooth: hci0: Firmware revision 0.1 build 6 week 12 2021
    Oct 06 17:26:26 maffbook kernel: Bluetooth: hci0: Minimum firmware build 1 week 10 2014
    Oct 06 17:26:26 maffbook kernel: Bluetooth: hci0: Found device firmware: intel/ibt-17-16-1.sfi
    Oct 06 17:26:28 maffbook kernel: Bluetooth: hci0: Waiting for firmware download to complete
    Oct 06 17:26:28 maffbook kernel: Bluetooth: hci0: Firmware loaded in 1484394 usecs
    Oct 06 17:26:28 maffbook kernel: Bluetooth: hci0: Firmware revision 0.1 build 6 week 12 2021

### [Wi-Fi adapter cannot find and connect to a 5 GHz network]

Networks with WPA or WPA2 use the legacy TKIP protocol instead of AES to connect. Install [[[net-wireless/wpa_supplicant]](https://packages.gentoo.org/packages/net-wireless/wpa_supplicant)[]] with the [[[tkip]](https://packages.gentoo.org/useflags/tkip)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") and reboot your system.

### [Forum threads]

-   [Forum thread: wireless lan can\'t get ip from access point](https://forums.gentoo.org/viewtopic-p-7888312.html#7888312) which explains about 169.254.x.x ([link local address](https://en.wikipedia.org/wiki/Link-local_address "wikipedia:Link-local address")) being a wrong IP address

## [See also]

-   [Handbook:AMD64/Networking/Wireless](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Wireless "Handbook:AMD64/Networking/Wireless")
-   [AC1200 Wireless Adapters](https://wiki.gentoo.org/wiki/AC1200_Wireless_Adapters "AC1200 Wireless Adapters")
-   [Iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2") --- a tool developed to unify network interface configuration, routing, and tunneling for Linux systems.
-   [Iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi") --- the wireless driver for [Intel\'s current wireless chips](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi#introduction).
-   [Qualcomm Atheros QCA6174](https://wiki.gentoo.org/wiki/Qualcomm_Atheros_QCA6174 "Qualcomm Atheros QCA6174") --- a [802.11ac](https://en.wikipedia.org/wiki/IEEE_802.11ac "wikipedia:IEEE 802.11ac") Wireless Network Adapter which is used in some laptops.