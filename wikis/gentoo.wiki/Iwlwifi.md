Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Iwlwifi/de "Iwlwifi/de (14% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Iwlwifi/es "Iwlwifi (20% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Iwlwifi/hu "iwlwifi (100% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Iwlwifi/pl "Iwlwifi/pl (3% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Iwlwifi/ru "Iwlwifi (59% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Iwlwifi/zh-cn "Iwlwifi (33% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Iwlwifi/ja "iwlwifi (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Iwlwifi/ko "Iwlwifi (14% translated)")

**Resources**

[[]][Home](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi)

[[]][gitweb Driver](https://git.kernel.org/cgit/linux/kernel/git/stable/linux-stable.git/tree/drivers/net/wireless/intel/iwlwifi/Kconfig)

**iwlwifi** is the wireless driver for [Intel\'s current wireless chips](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi#introduction). Correct operation requires support from the kernel\'s wifi stack and card specific firmware loaded at run time.

## Contents

-   [[1] [Kernel]](#Kernel)
    -   [[1.1] [IEEE 802.11]](#IEEE_802.11)
    -   [[1.2] [Device driver iwlwifi]](#Device_driver_iwlwifi)
-   [[2] [Firmware]](#Firmware)
    -   [[2.1] [When using built-in configuration]](#When_using_built-in_configuration)
    -   [[2.2] [Optional: savedconfig]](#Optional:_savedconfig)
    -   [[2.3] [Latest firmware version supporting device]](#Latest_firmware_version_supporting_device)
-   [[3] [Testing]](#Testing)
    -   [[3.1] [/sys file system]](#.2Fsys_file_system)
    -   [[3.2] [ip command]](#ip_command)
    -   [[3.3] [ifconfig command]](#ifconfig_command)
    -   [[3.4] [iw command]](#iw_command)
    -   [[3.5] [modprobe and modinfo]](#modprobe_and_modinfo)
    -   [[3.6] [lspci]](#lspci)
    -   [[3.7] [dmesg]](#dmesg)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Kernel not loaded]](#Kernel_not_loaded)
    -   [[4.2] [Firmware issues]](#Firmware_issues)
    -   [[4.3] [Wireless not working]](#Wireless_not_working)
    -   [[4.4] [No internet connection]](#No_internet_connection)
    -   [[4.5] [Network crashes under heavy load]](#Network_crashes_under_heavy_load)
    -   [[4.6] [\"Microcode SW error detected. Restarting 0x0\" message in kernel logs]](#.22Microcode_SW_error_detected._Restarting_0x0.22_message_in_kernel_logs)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [[] Kernel]

To make it work some kernel configuration is needed. The driver supports 802.11a/b/g/n/ac (depending on the device), so IEEE 802.11 should be enabled.

### [[] IEEE 802.11]

Activate at least [cfg80211](https://wireless.wiki.kernel.org/en/developers/documentation/cfg80211) (`CONFIG_CFG80211`) and [mac80211](https://wireless.wiki.kernel.org/en/developers/documentation/mac80211) (`CONFIG_MAC80211`). For details see [IEEE 802.11 section of Wi-Fi artice](https://wiki.gentoo.org/wiki/Wi-Fi#IEEE_802.11 "Wi-Fi").

### [[] Device driver iwlwifi]

Use this driver for Intel\'s [current wireless chips](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi#supported_devices). Set it as a module `<M>` as shown here. Also the correct *DVM* or *MVM* firmware option according to the **Module** column of the [firmware table](https://web.archive.org/web/20190305085430/https://wireless.wiki.kernel.org/en/users/Drivers/iwlwifi) is needed.

[KERNEL] **Options for Linux Kernel 4.19**

    Device Drivers  --->
        [*] Network device support  --->
            [*]   Wireless LAN  --->
                [*]     Intel devices
                <M>       Intel Wireless WiFi Next Gen AGN - Wireless-N/Advanced-N/Ultimate-N (iwlwifi)
                <M>         Intel Wireless WiFi DVM Firmware support
                <M>         Intel Wireless WiFi MVM Firmware support

** Important**\
In case the driver is built into the kernel (`<*>`) instead as a module (`<M>`), also the firmware needs to be built [into the kernel](https://wiki.gentoo.org/wiki/Kernel_Modules#About_loadable_kernel_modules "Kernel Modules"). See the section [When using built-in configuration](https://wiki.gentoo.org/wiki/Iwlwifi#When_using_built-in_configuration "Iwlwifi").\
After changes on kernel configuration do not forget to [rebuild the kernel](https://wiki.gentoo.org/wiki/Kernel/Rebuild "Kernel/Rebuild").

After rebuilding the kernel and rebooting with this kernel, the selected options can be verified as follows:

`user `[`$`]`zgrep 'IWLWIFI\|IWLDVM\|IWLMVM' /proc/config.gz`

** Note**\
Support for the [/proc/config.gz] file can be enabled through the [Kernel/IKCONFIG support](https://wiki.gentoo.org/wiki/Kernel/IKCONFIG_support "Kernel/IKCONFIG support") feature.

## [[] Firmware]

Additional [firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") for the individual device is needed as listed in [this table](https://www.intel.com/content/www/us/en/support/articles/000005511/wireless.html). Contemporary firmware is always available in the [[[sys-kernel/linux-firmware]](https://packages.gentoo.org/packages/sys-kernel/linux-firmware)[]] package. In case it is not in linux-firmware it might be found in device-specific [sys-firmware/iwlxxxx-\*ucode](https://packages.gentoo.org/packages/search?q=sys-firmware%2Fiwl) packages.

Upstream Intel instructions recommend^[\[1\]](#cite_note-1)^ adding all iwlwifi ucode to the kernel image. This is recommended for convenience, however it will bloat the kernel slightly.

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

### [[] When using built-in configuration]

In case the driver is built into the kernel (`<*>`) instead as a module (`<M>`), also the firmware needs to be built [into the kernel](https://wiki.gentoo.org/wiki/Kernel_Modules#About_loadable_kernel_modules "Kernel Modules").

[KERNEL] **linux-4.19**

    Device Drivers  --->
                Generic Driver Options  --->
                    Firmware loader --->

                        -*- Firmware loading facility
                        (iwlwifi-xxxx.ucode) Build named firmware blobs into the kernel binary
                        (/lib/firmware) Firmware blobs root directory
                        [ ] Enable the firmware sysfs fallback mechanism

In this case replace `iwlwifi-xxxx.ucode` with the exact firmware name. Some attention seems to be needed for `FW_LOADER_USER_HELPER_FALLBACK`.

### [[] Optional: savedconfig]

The [`savedconfig`](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") USE flag could be set for [Linux firmware](https://wiki.gentoo.org/wiki/Linux_firmware "Linux firmware") in order to avoid unneeded stuff in [/lib/firmware/].

As for example the [Intel® Centrino® Advanced-N 6205](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi?s%5b%5d=N%206205#firmware) needs **iwlwifi-6000g2a-ucode** while anything else may be commented out or deleted.

[FILE] **`/etc/portage/savedconfig/sys-kernel/linux-firmware`Take care that version number is removed**

    iwlwifi-6000g2a-5.ucode
    iwlwifi-6000g2a-6.ucode

In order to not lose these settings on next firmware update the version number needs to be removed:

`user `[`$`]`cd /etc/portage/savedconfig/sys-kernel`

`root `[`#`]`mv linux-firmware `

### [Latest firmware version supporting device]

Below is an incomplete list of the latest known firmware blob supporting a given chipset. Device names are retrieved using [lspci].

  ------------------------------------------ ------------------------------------------------------------------------------------------------------------- ------------------
  Device name                                Firmware blob filename                                                                                        Firmware version
  Intel Corporation Wi-Fi 6 AX200 (rev 1a)   [iwlwifi-cc-a0-77.ucode]   `77.ad46c98b.0`
  ------------------------------------------ ------------------------------------------------------------------------------------------------------------- ------------------

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

### [[] modprobe and modinfo]

[modprobe] should return nothing:

`root `[`#`]`modprobe iwlwifi`

Most information about the driver module can be obtained by [modinfo iwlwifi]:

`user `[`$`]`modinfo iwlwifi`

### [[] lspci]

[lspci] should display `iwlwifi` for both `Kernel driver in use:` and `Kernel modules:`.

`root `[`#`]`lspci -nnkv | sed -n '/Network/,/^$/p'`

    03:00.0 Network controller [0280]: Intel Corporation Centrino Advanced-N 6205 [Taylor Peak] [8086:0082] (rev 34)
            Subsystem: Intel Corporation Centrino Advanced-N 6205 AGN [8086:1321]
            Flags: bus master, fast devsel, latency 0, IRQ 33
            Memory at f7d00000 (64-bit, non-prefetchable) [size=8K]
            Capabilities: [c8] Power Management version 3
            Capabilities: [d0] MSI: Enable+ Count=1/1 Maskable- 64bit+
            Capabilities: [e0] Express Endpoint, MSI 00
            Capabilities: [100] Advanced Error Reporting
            Capabilities: [140] Device Serial Number confidential
            Kernel driver in use: iwlwifi
            Kernel modules: iwlwifi

The `xx:xx.x` identifier will be useful for grepping specific information from dmesg.

### [[] dmesg]

Check the output of dmesg. Replace `03:00.0` with the identifier from [lspci](https://wiki.gentoo.org/wiki/Iwlwifi#lspci "Iwlwifi") and `wlp` with the [network interface name](https://wiki.gentoo.org/wiki/Iwlwifi#Network_device_names "Iwlwifi").

`user `[`$`]`dmesg | grep -i -E '03:00.0|wlp|iwl|80211'`

    [    0.251986] pci 0000:03:00.0: [8086:0082] type 00 class 0x028000
    [    0.252146] pci 0000:03:00.0: reg 0x10: [mem 0xf7d00000-0xf7d01fff 64bit]
    [    0.252863] pci 0000:03:00.0: PME# supported from D0 D3hot D3cold
    [    3.621978] cfg80211: Loading compiled-in X.509 certificates for regulatory database
    [    3.629362] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
    [    3.634986] iwlwifi 0000:03:00.0: enabling device (0100 -> 0102)
    [    3.635111] iwlwifi 0000:03:00.0: can't disable ASPM; OS doesn't have ASPM control
    [    3.644480] iwlwifi 0000:03:00.0: loaded firmware version 18.168.6.1 op_mode iwldvm
    [    3.659269] iwlwifi 0000:03:00.0: CONFIG_IWLWIFI_DEBUG disabled
    [    3.659270] iwlwifi 0000:03:00.0: CONFIG_IWLWIFI_DEBUGFS disabled
    [    3.659271] iwlwifi 0000:03:00.0: CONFIG_IWLWIFI_DEVICE_TRACING enabled
    [    3.659273] iwlwifi 0000:03:00.0: Detected Intel(R) Centrino(R) Advanced-N 6205 AGN, REV=0xB0
    [    3.694543] ieee80211 phy0: Selected rate control algorithm 'iwl-agn-rs'
    [    3.695812] iwlwifi 0000:03:00.0 wlp3s0: renamed from wlan0
    [    5.060307] iwlwifi 0000:03:00.0: Radio type=0x1-0x2-0x0
    [    5.352853] iwlwifi 0000:03:00.0: Radio type=0x1-0x2-0x0
    [    5.431804] IPv6: ADDRCONF(NETDEV_UP): wlp3s0: link is not ready
    [    8.908518] wlp3s0: authenticate with <my WLAN AP>
    [    8.912238] wlp3s0: send auth to <my WLAN AP> (try 1/3)
    [    9.016437] wlp3s0: send auth to <my WLAN AP> (try 2/3)
    [    9.120455] wlp3s0: send auth to <my WLAN AP> (try 3/3)
    [    9.125773] wlp3s0: authenticated
    [    9.126019] wlp3s0: waiting for beacon from <my WLAN AP>
    [    9.148418] wlp3s0: associate with <my WLAN AP> (try 1/3)
    [    9.191232] wlp3s0: RX AssocResp from <my WLAN AP> (capab=0x1431 status=0 aid=2)
    [    9.211860] wlp3s0: associated
    [    9.242532] IPv6: ADDRCONF(NETDEV_CHANGE): wlp3s0: link becomes ready
    [    9.249856] wlp3s0: Limiting TX power to 20 (20 - 0) dBm as advertised by <my WLAN AP>

## [[] Troubleshooting]

### [[] Kernel not loaded]

Check if the correct kernel is loaded. This can be accomplished as follows (depends on the [IKCONFIG feature](https://wiki.gentoo.org/wiki/Kernel/IKCONFIG_support "Kernel/IKCONFIG support")):

`user `[`$`]`zgrep CONFIG_IWL /proc/config.gz`

### [[] Firmware issues]

-   For systems using udev or systemd, it is imperative to configure the kernel to load binary blobs. In this case the wireless card\'s firmware is the firmware that needs loaded. More information on configuring the kernel in this manner can be found in the following thread on the Gentoo forums: [FW_LOADER_USER_HELPER_FALLBACK](https://forums.gentoo.org/viewtopic-t-1001638.html).

<!-- -->

-   [Linux firmware for iwlwifi ucode failed with error -2](https://z-issue.com/wp/linux-firmware-for-iwlwifi-ucode-failed-with-error-2/) from [https://z-issue.com/wp/](https://z-issue.com/wp/)

### [[] Wireless not working]

-   Intel Corporation Wireless 8260 (rev 3a) [can\'t access the RSA semaphore it is write protected](https://forums.gentoo.org/viewtopic-t-1040894-highlight-.html)
-   [Intel Wireless-AC 9560 iwlwifi not working kernel 5.4.0](https://forums.gentoo.org/viewtopic-t-1104736.html)
-   [Linux kernel 5.6.0 iwlwifi bug](https://www.mpagano.com/blog/?p=291)
-   Intel Corporation Wi-Fi 6 AX200 (rev 1a). If getting dmesg message **pci_enable_msi failed - -38** and the card shows **Input/output** error in spite of the correct firmware being loaded, then try enabling the *Message Signaled Interrupts (MSI and MSI-X)* kernel option (*CONFIG_PCI_MSI*)

[KERNEL]

    Device Drivers  --->
        [*] PCI support  --->
            [*]   Message Signaled Interrupts (MSI and MSI-X)

### [[] No internet connection]

If it is possible to connect to an access point, but not possible to connect to any server or get any connection to the Internet, it may be worth trying to disable 802.11n and/or enable software encryption. To do so, it is necessary to pass the parameter `iwlwifi.11n_disable=1` or `iwlwifi.11n_disable=8` and/or `iwlwifi.swcrypto=1` to the kernel. In order to pass the parameter automatically on module load, the following file should be created:

[FILE] **`/etc/modprobe.d/iwlwifi.conf`Disabling 802.11n, enabling software crypto**

    options iwlwifi 11n_disable=1 swcrypto=1

** Note**\
In newer kernels, inspected as of 5.3.7, setting 11n_disable=1 (or masked with 0x01) will result in 802.11ac being disabled. This will limit the device to a maximum of 54Mbit throughput.

### [[] Network crashes under heavy load]

On some wireless cards (e.g. Intel® Wi-Fi 6 AX201), under heavy load, the network crashes with a similar error:

`root `[`#`]`dmesg`

    [  367.411551] iwlwifi 0000:00:14.3: reached 20 old SN frames from 77:77:77:77:77:77 on queue 2, stopping BA session on TID 3

As a workaround, RX aggregation should be disabled using the kernel parameter `iwlwifi.11n_disable=4`:

[FILE] **`/etc/modprobe.d/iwlwifi.conf`Disabling RX aggregation**

    options iwlwifi 11n_disable=4

### [][[] \"Microcode SW error detected. Restarting 0x0\" message in kernel logs]

`root `[`#`]`dmesg | grep iwlwifi`

    (... redacted ...)
    [ 5711.326985] iwlwifi 0000:28:00.0: Microcode SW error detected. Restarting 0x0.
    [ 5711.326987] iwlwifi 0000:28:00.0: Start IWL Error Log Dump:
    [ 5711.326990] iwlwifi 0000:28:00.0: Transport status: 0x0000004A, valid: 6
    [ 5711.326992] iwlwifi 0000:28:00.0: Loaded firmware version: 71.058653f6.0 ty-a0-gf-a0-71.ucode
    [ 5711.326993] iwlwifi 0000:28:00.0: 0x00000071 | NMI_INTERRUPT_UMAC_FATAL
    [ 5711.326995] iwlwifi 0000:28:00.0: 0x00008210 | trm_hw_status0
    [ 5711.326998] iwlwifi 0000:28:00.0: 0x00000000 | trm_hw_status1
    [ 5711.327001] iwlwifi 0000:28:00.0: 0x004DAEA2 | branchlink2
    [ 5711.327003] iwlwifi 0000:28:00.0: 0x004D9974 | interruptlink1
    [ 5711.327004] iwlwifi 0000:28:00.0: 0x004D9974 | interruptlink2
    [ 5711.327006] iwlwifi 0000:28:00.0: 0x0000C314 | data1
    [ 5711.327008] iwlwifi 0000:28:00.0: 0x00000010 | data2
    [ 5711.327009] iwlwifi 0000:28:00.0: 0x00000000 | data3
    (... redacted ...)
    [ 5711.329587] iwlwifi 0000:28:00.0: ieee80211 phy0: Hardware restart was requested

This indicates that a severe error has been encountered by the WiFi adapter\'s micro-controller which led it to be reset. Consequences might be network drop outs and/and severe slow downs even after the connection to the AP has been restored. The root cause might be difficult to point out (platform own radio noise/buggy firmware/etc) however one of the very first things to try, even if the power management has been disabled for the iwlwifi module, is to prevent the WiFi adapter PCIe link to go in power save mode. This is accomplished by changing the `power_scheme` value used by the iwlmvm module to **1** (active):

[FILE] **`/etc/modprobe.d/iwlmvm.conf`Changing power_scheme to \'active\'**

    options iwlmvm power_scheme=1

Amongst additional countermeasures suggested on [https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi) disabling 40 MHz channels usage on the 2.4GHz band might also help:

[FILE] **`/etc/modprobe.d/cfg80211.conf`Turning off 40 MHz channels usage (2.4 Ghz band)**

    options cfg80211 cfg80211_disable_40mhz_24ghz=Y

## [[] See also]

-   [Handbook:AMD64/Networking/Wireless](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Wireless "Handbook:AMD64/Networking/Wireless")
-   [Wifi](https://wiki.gentoo.org/wiki/Wifi "Wifi") --- describes the setup of a [Wi-Fi](https://en.wikipedia.org/wiki/Wi-Fi "wikipedia:Wi-Fi") (wireless) network device.
-   [Wpa_supplicant](https://wiki.gentoo.org/wiki/Wpa_supplicant "Wpa supplicant") --- an app for [Wi-Fi](https://wiki.gentoo.org/wiki/Wi-Fi "Wi-Fi") authentication
-   [Network management using DHCPCD](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD "Network management using DHCPCD") --- explains how to use dhcpcd for complete network stack management.
-   [Netifrc](https://wiki.gentoo.org/wiki/Netifrc "Netifrc") --- Gentoo\'s default framework for configuring and [managing network](https://wiki.gentoo.org/wiki/Network_management "Network management") interfaces on systems running [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC").
-   [Troubleshooting](https://wiki.gentoo.org/wiki/Troubleshooting "Troubleshooting") --- provide users with a set of techniques and tools to troubleshoot and fix problems with their Gentoo setups.

## [[] External resources]

-   [https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi)
-   [https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git](https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git)
-   [https://cateee.net/lkddb/web-lkddb/IWLWIFI.html](https://cateee.net/lkddb/web-lkddb/IWLWIFI.html)
-   [https://wiki.archlinux.org/index.php/Wireless_network_configuration#iwlwifi](https://wiki.archlinux.org/index.php/Wireless_network_configuration#iwlwifi)
-   [Fixing Intel Wi-Fi 6 AX200 latency and ping spikes in Linux](https://z-issue.com/wp/fixing-intel-wi-fi-6-ax200-latency-and-ping-spikes-in-linux/)

## [[] References]

1.  [[[↑](#cite_ref-1)] [[https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi#firmware](https://wireless.wiki.kernel.org/en/users/drivers/iwlwifi#firmware)]]