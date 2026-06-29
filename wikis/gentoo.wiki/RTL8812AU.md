**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/IEEE_802.11ac "wikipedia:IEEE 802.11ac")

## Contents

-   [[1] [Finding an adapter]](#Finding_an_adapter)
-   [[2] [Finding a driver]](#Finding_a_driver)
-   [[3] [Working devices]](#Working_devices)
    -   [[3.1] [PCI]](#PCI)
    -   [[3.2] [USB]](#USB)
-   [[4] [Notes]](#Notes)
-   [[5] [Realtek RTL8812AU]](#Realtek_RTL8812AU)
    -   [[5.1] [Kernel configuration]](#Kernel_configuration)
    -   [[5.2] [Scripted installation]](#Scripted_installation)
    -   [[5.3] [Manual installation]](#Manual_installation)
-   [[6] [External resources]](#External_resources)

## [Finding an adapter]

1.  Browse to the [WikiDev](https://wikidevi.com/wiki/Main_Page) wireless adapter [query](https://wikidevi.com/wiki/Special:RunQuery/Wireless_adapter_query) page.
2.  Enter \"abgn+ac\" in the `Supported 802dot11 protocols` field.
3.  Select \"linux_support\" for the `Table query type` option.
4.  Click `Run query`.
5.  Scroll down to find a table of known abgn+ac wireless adapters with chipset, device ID, and probable Linux driver. The AC1200 adapters listed in the table will have Realtek RTL8812AU or Broadcom BCM43526 chipsets. The remaining adapters support data rates other than AC1200.

## [Finding a driver]

-   Realtek 8723/8812/8821 PCIe drivers are in Linux 3.17.8 and later.
-   Intel\'s AC7260 PCIe driver is builtin the kernel. After reported problems with kernel 4.0.x, it is working well with kernel 4.1.x.
-   The Realtek 8812au USB driver (kernel 3.10) is available from [https://github.com/gnab/rtl8812au](https://github.com/gnab/rtl8812au).
-   The rtltek 8812au USB driver (kernel 4.3.14) is available from [https://github.com/abperiasamy/rtl8812AU_8821AU_linux](https://github.com/abperiasamy/rtl8812AU_8821AU_linux).
-   Broadcom drivers are provided by the [[[net-wireless/broadcom-sta]](https://packages.gentoo.org/packages/net-wireless/broadcom-sta)[]] package, but support of BCM4352 and BCM43526 devices is very unlikely. BCM43526 is not listed under \"SUPPORTED DEVICES\" in the driver [readme](http://www.broadcom.com/docs/linux_sta/README_6.30.223.248.txt) file. Using [[[net-wireless/ndiswrapper]](https://packages.gentoo.org/packages/net-wireless/ndiswrapper)[]] and 32-bit Windows files *may* work, while 64-bit Windows files *will not*.

## [Working devices]

### [PCI]

The table below lists AC1200 PCIe adapters tested and working with Linux 4.1.3 and later on **[amd64]** multilib.

  ------------------- ------------------------ ------------------- --------------- --------- -----------------------------------------------------------
  Device              Vendor ID / Product ID   Vendor Name         Product Name    Chipset   Driver
  Intel 7260HMWDTX1   `8086:08b1`              Intel Corporation   Wireless 7260   Unknown   [iwlwifi](https://wiki.gentoo.org/wiki/Iwlwifi "Iwlwifi")
  ------------------- ------------------------ ------------------- --------------- --------- -----------------------------------------------------------

### [USB]

The table below lists AC1200 USB 3.0 adapters tested and working with Linux 3.18.5 and later on **[amd64]** multilib.

  -------------------------- ------------------------ ----------------------------- ------------------------------------------------------------------ ------------------- --------
  Device                     Vendor ID / Product ID   Vendor Name                   Product Name                                                       Chipset             Driver
  Alfa Network AWUS036AC     `0bda:8812`              Realtek Semiconductor Corp.   RTL8812AU 802.11a/b/g/n/ac WLAN Adapter                            Realtek RTL8812AU   8812au
  Alfa Network AWUS036ACH    `0bda:8812`              Realtek Semiconductor Corp.   RTL8812AU 802.11a/b/g/n/ac WLAN Adapter                            Realtek RTL8812AU   8812au
  D-Link DWA-182 (Rev. C1)   `2001:3315`              D-Link Corp.                                                                                     Realtek RTL8812AU   8812au
  Edimax EW-7822UAC          `7392:a822`              Edimax Technology Co., Ltd                                                                       Realtek RTL8812AU   8812au
  Linksys WUSB6300           `13b1:003f`              Linksys                       WUSB6300 802.11a/b/g/n/ac Wireless Adapter \[Realtek RTL8812AU\]   Realtek RTL8812AU   8812au
  Rosewill RNX-AC1200UBE     `0bda:8812`              Realtek Semiconductor Corp.   RTL8812AU 802.11a/b/g/n/ac WLAN Adapter                            Realtek RTL8812AU   8812au
  TRENDnet TEW-805UB         `20f4:805b`              TRENDnet                                                                                         Realtek RTL8812AU   8812au
  -------------------------- ------------------------ ----------------------------- ------------------------------------------------------------------ ------------------- --------

## [Notes]

-   The RTL8812AU driver will not install correctly if the USB adapter is plugged-in before the driver is installed.
-   The RTL8812AU driver may not install correctly unless the kernel configuration enables some of the built-in Realtek wireless drivers (including those in staging) as modules.
-   The RTL8812AU driver must be re-installed after every kernel update, even if the kernel version has not changed.
-   The RTL8812AU driver requires the Linux wireless extensions (wext) driver.
-   The RTL8812AU adapters listed in [working devices](#Working_devices) support hot-plugging.
-   BCM43526 adapters are USB 2.0 and have a 480 Mbit/s maximum data rate, therefore they cannot support the theoretical 867 Mbit/s data rate of 5 GHz channels.
-   Depending on which driver is used, the following install script may have to be edited.

## [Realtek RTL8812AU]

### [Kernel configuration]

[KERNEL]

    [*] Networking support --->
          <*>   Wireless --->
                  <*>   cfg80211 - wireless configuration API
                  <*>   Generic IEEE 802.11 Networking Stack (mac80211)
          <*>   RF switch subsystem support --->
        Device Drivers --->
          [*] Network device support --->
                [*]   Wireless LAN --->
                        <M>   Realtek rtlwifi family of devices --->
                                <M>   Realtek RTL8821AE/RTL8812AE Wireless Network Adapter
                                <M>   Realtek RTL8192CU/RTL8188CU USB Wireless Network Adapter
          [*] Staging drivers --->
                <M>   Support for rtllib wireless devices
                <M>     Support for rtllib CCMP crypto
                <M>     Support for rtllib TKIP crypto
                <M>     Support for rtllib WEP crypto
                <M>   Realtek RTL8723AU Wireless LAN NIC driver
                [*]     Realtek RTL8723AU AP mode
                [*]     Realtek RTL8723AU BlueTooth Coexistence

### [Scripted installation]

Create the following installation script which performs the actions from the manual installation below:

[FILE] **`/root/rtlscript.sh`**

    #!/bin/bash
    if [ "$(id -u)" != "0" ]; then
        echo "Please login as root, then try again" 1>&2
        exit 1
    fi
    eselected=$(eselect kernel list | awk '/\*/ ' | awk 'gsub("linux-", "")')
    running=$(uname -r)
    if [ "$running" != "$eselected" ]; then
        echo "Please ensure the eselected kernel source and running kernel are the same version, then try again." 1>&2;
        exit 1
    fi
    WGET="/usr/bin/wget"
    $WGET -q --tries=1 --timeout=1 http://www.google.com -O /tmp/google.idx &> /dev/null
    if [ -s /tmp/google.idx ]; then
        version=$
        required_version="4"
        if [ "$version" = "$required_version" ]; then
            wget -N https://github.com/csssuf/rtl8812au/archive/master.zip
        else
            wget -N https://github.com/gnab/rtl8812au/archive/master.zip
        fi
        if [ -d "rtl8812au-master" ]; then
            rm -rf rtl8812au-master
        fi
    fi
    if [ -s /root/master.zip ]; then
        unzip master.zip
    fi
    if [ -d "rtl8812au-master" ]; then
        cd rtl8812au-master
        sed 's/CONFIG_POWER_SAVING = y/CONFIG_POWER_SAVING = n/g' Makefile > OUT
        mv OUT Makefile
        make
        insmod 8812au.ko
            if [ ! -d "/lib64/modules/$(uname -r)/kernel/drivers/net/wireless/rtlwifi/rtl8812au" ]; then
                mkdir /lib64/modules/$(uname -r)/kernel/drivers/net/wireless/rtlwifi/rtl8812au
                echo "rtl8812au directory created."; 1>&2;
            else
                echo "rtl8812au directory existed." 1>&2;
            fi
        cp -f 8812au.ko /lib64/modules/$(uname -r)/kernel/drivers/net/wireless/rtlwifi/rtl8812au
        depmod -a
        echo "Connect the wireless usb device and reboot";
    else
        echo "Unable to find or create /root/rtl8812au-master -> no internet connection, no master.zip file, no rtl8812au-master file.";
        exit 1
    fi

Install the script dependencies:

`root `[`#`]`emerge --ask --noreplace app-arch/unzip`

Run the installation script:

`root `[`#`]`chmod o+x /root/rtlscript.sh `

`root `[`#`]`/root/rtlscript.sh `

### [Manual installation]

    After booting the kernel configured as above:
    Use eselect kernel list and uname -r  and ensure the eselected kernel source and running kernel are the same version.
    Download
    https://github.com/gnab/rtl8812au/archive/master.zip# (incompatible with 4.x.x and >5.15.x kernels, pending pull approval of the change below)
    OR
    1) https://github.com/csssuf/rtl8812au/archive/master.zip (kernel 4.0.0 compatible pull)
    2) https://github.com/fsantini/rtl8812au/archive/refs/heads/fix_kernel_5.15.zip (kernel 5.15 compatibility fix)
    to a directory you can find again. cd into the directory containing master.zip .
    If an "rtl8812au-master" subdirectory exists, remove it.
    unzip master.zip to create a fresh "rtl8812au-master" subdirectory.
    cd rtl8812au-master .
    Edit rtl8812au-master/Makefile to replace CONFIG_POWER_SAVING = y with CONFIG_POWER_SAVING = n .
    Run make .
    Run insmod 8812au.ko .
    Make directory /lib64/modules/$(uname -r)/kernel/drivers/net/wireless/rtlwifi/rtl8812au if not present.
    Copy 8812au.ko into the directory /lib64/modules/$(uname -r)/kernel/drivers/net/wireless/rtlwifi/rtl8812au .
    Run depmod -a .
    Connect the wireless usb device and reboot.

## [External resources]

-   [https://gpo.zugaina.org/net-wireless/rtl8812au](https://gpo.zugaina.org/net-wireless/rtl8812au)