[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Intel_Edison&action=edit).

**Resources**

[[]][Product Information](https://www.intel.com/content/www/us/en/products/sku/84572/intel-edison-compute-module-iot/specifications.html)

[[]][Intel Edison](https://en.wikipedia.org/wiki/Intel_Edison "wikipedia:Intel Edison")

The **Intel Edison** is a tiny computer-on-module offered by Intel as a development system for wearable devices and Internet of Things devices.

[![Intel-Edison.png](/images/thumb/8/88/Intel-Edison.png/200px-Intel-Edison.png)](https://wiki.gentoo.org/wiki/File:Intel-Edison.png)

[](https://wiki.gentoo.org/wiki/File:Intel-Edison.png "Enlarge")

## Contents

-   [[1] [Gentoo for Edison]](#Gentoo_for_Edison)
    -   [[1.1] [License]](#License)
    -   [[1.2] [Pre-made image]](#Pre-made_image)
    -   [[1.3] [Image password]](#Image_password)
    -   [[1.4] [Features list]](#Features_list)
    -   [[1.5] [Image install]](#Image_install)
        -   [[1.5.1] [Configure Wifi]](#Configure_Wifi)
    -   [[1.6] [Features]](#Features)
        -   [[1.6.1] [Cross compile preparation]](#Cross_compile_preparation)
        -   [[1.6.2] [Squashfs Gentoo repository]](#Squashfs_Gentoo_repository)
        -   [[1.6.3] [Kernel multi-boot]](#Kernel_multi-boot)
        -   [[1.6.4] [Performance]](#Performance)
    -   [[1.7] [Install from source]](#Install_from_source)
-   [[2] [Support]](#Support)
-   [[3] [External resources]](#External_resources)

## [Gentoo for Edison]

### [License]

U-boot: GPL-2+ [https://github.com/01org/edison-u-boot](https://github.com/01org/edison-u-boot)

### [Pre-made image]

[Gentoo-edison-170104.tar.gz](http://public.aliceinwire.net/edison/Gentoo-edison-170104.tar.gz) md5sum: 3f956280ba52de26fe95705e884e83c4

### [Image password]

User: root

Password: edison

### [Features list]

-   Working WiFi
-   Portage
-   Squashfs Gentoo repository
-   [specification](https://wiki.gentoo.org/wiki/Intel_Edison/specs "Intel Edison/specs")
-   [Performance](#Performance)

### [Image install]

Download the Gentoo image on your local PC:

`root `[`#`]`wget `[`http://public.aliceinwire.net/edison/Gentoo-edison-170104.tar.gz`](http://public.aliceinwire.net/edison/Gentoo-edison-170104.tar.gz)` `

`root `[`#`]`tar -xvzf Gentoo-edison-*.tar.gz `

`root `[`#`]`cd GentootoFlash `

Connect and flash the Intel Edison.

This will delete all your previous data:

`root `[`#`]`./flashall.sh `

[CODE] **flashall.sh output example**

    Using U-Boot target: edison-blankcdc
    Now waiting for dfu device 8087:0a99
    Please plug and reboot the board
    Flashing IFWI
    Download        [=========================] 100%      4194304 bytes
    Download        [=========================] 100%      4194304 bytes
    Flashing U-Boot
    Download        [=========================] 100%       245760 bytes
    Flashing U-Boot Environment
    Download        [=========================] 100%        65536 bytes
    Flashing U-Boot Environment Backup
    Download        [=========================] 100%        65536 bytes
    Rebooting to apply partition changes
    Now waiting for dfu device 8087:0a99
    Flashing boot partition (kernel)
    Download        [=========================] 100%      5980160 bytes
    Flashing rootfs, (it can take up to 10 minutes... Please be patient)
    Download        [=========================] 100%   1610612736 bytes
    Rebooting
    U-boot & Kernel System Flash Success...
    Your board needs to reboot to complete the flashing procedure, please do not unplug it for 2 minutes.

#### [Configure Wifi]

symlink wlan0

`root `[`#`]`cd /etc/init.d/ `

`root `[`#`]`ln -s net.lo net.wlan0 `

`root `[`#`]`rc-config add net.wlan0 default `

Create [/etc/conf.d/net] file:

[FILE] **`/etc/conf.d/net`**

    # Set the dns_domain_lo variable to the selected domain name
    dns_domain_lo="homenetwork"
    modules_wlan0="wpa_supplicant"
    wpa_supplicant_wlan0="-Dnl80211"
    config_wlan0="dhcp"

### [Features]

#### [Cross compile preparation]

Setup:

`root `[`#`]`emerge --ask crossdev`

`root `[`#`]`crossdev i686-pc-linux-gnu`

Copy package to Intel Edison:

`root `[`#`]`scp -r /usr/i686-pc-linux-gnu/packages root@192.168.0.102:/var/cache/packages/`

Install in Intel Edison:

`root `[`#`]`emerge --ask --oneshot --usepkgonly  `

#### [Squashfs Gentoo repository]

Mount squashfs or use sd-card:

`root `[`#`]`mount /portage.squash /var/db/repos/gentoo/ `

#### [Kernel multi-boot]

Increase the Edison boot partition:

`root `[`#`]`mount /dev/mmcblk0p7 /mnt/boot/ `

`root `[`#`]`mkdir /tmp/boot `

`root `[`#`]`mv /mnt/boot/* /tmp/boot `

`root `[`#`]`umount /mnt/boot `

`root `[`#`]`mkfs.vfat /dev/mmcblk0p7 `

`root `[`#`]`mount /mnt/boot `

`root `[`#`]`cp /tmp/boot/* /boot `

Add a new kernel in the /mnt/boot directory. For example vmlinuz_01 and vmlinuz_02:

multi boot with u-boot for start vmlinuz_01

`boot > setenv load_kernel fatload mmc 0:7 $ vmlinuz_01 `

`boot > boot `

#### [Performance]

-   [Intel Edison Board Software Package v2.2](https://wiki.gentoo.org/wiki/User:Alicef/Gentoo_Edison/Performance/IntelBoard "User:Alicef/Gentoo Edison/Performance/IntelBoard")
-   [Gentoo for Edison 170104](https://wiki.gentoo.org/wiki/User:Alicef/Gentoo_Edison/Performance/Gentoo4Edison "User:Alicef/Gentoo Edison/Performance/Gentoo4Edison")

### [Install from source]

[Repository](https://github.com/aliceinwire/Gentoo_for_Edison)

## [Support]

For support contact: [Arisu Tachibana (Alicef) ](https://wiki.gentoo.org/wiki/User:Alicef "User:Alicef")

## [External resources]

-   [homepage](https://software.intel.com/en-us/iot/hardware/edison)
-   [wikipedia](https://www.wikiwand.com/en/Intel_Edison)
-   [github](https://github.com/01org/edison-linux)
-   [Community wiki](https://edison.internet-share.com/wiki/Main_Page)