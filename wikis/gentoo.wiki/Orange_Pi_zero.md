This guide covers a basic bootstrapping for the Orange Pi Zero.

## Contents

-   [[1] [Orange pi zero quick install]](#Orange_pi_zero_quick_install)
    -   [[1.1] [Download]](#Download)
    -   [[1.2] [Backup modules firmware]](#Backup_modules_firmware)
    -   [[1.3] [Mount orangpi zero sd to mnt]](#Mount_orangpi_zero_sd_to_mnt)
    -   [[1.4] [Down and install armv7a stage3 and portage]](#Down_and_install_armv7a_stage3_and_portage)
    -   [[1.5] [Copy modules firmware to Gentoo]](#Copy_modules_firmware_to_Gentoo)
    -   [[1.6] [Edit fstab]](#Edit_fstab)
    -   [[1.7] [Change root passwd]](#Change_root_passwd)
    -   [[1.8] [Start wifi insmod wifi driver]](#Start_wifi_insmod_wifi_driver)

## [Orange pi zero quick install]

### [Download]

[orangpizero](http://www.orangepi.cn/) product choice Orange Pi Zero (because cn page new than en).

Download the Ubuntu_Desktop 2018-02-01 for orange pi zero img.

dd the ubuntu image file to an SD card.

### [Backup modules firmware]

`root `[`#`]`mount /dev/mmcblk0p2 /mnt `

`root `[`#`]`cp -r /mnt/lib/firmware /home/username `

`root `[`#`]`cp -r /mnt/lib/modules /home/username `

`root `[`#`]`mkdir etc `

`root `[`#`]`cp -r /mnt/etc/firmware /home/username/etc ##this firmware for wifi bin file `

`root `[`#`]`umount /dev/mmcblk0p2 `

`root `[`#`]`fdisk /dev/mmcblk0 `

d del 2 disk partition n add 2 partition

`root `[`#`]`resize2fs /dev/mmcblk0p2 `

`root `[`#`]`mkfs.ext4 /dev/mmcblk0p2 `

### [Mount orangpi zero sd to mnt]

`root `[`#`]`mkdir /mnt/gentoo `

`root `[`#`]`mount /dev/mmcblk0p2 /mnt/gentoo `

`root `[`#`]`mkdir /mnt/gentoo/boot `

`root `[`#`]`mount /dev/mmcblk0p1 /mnt/gentoo/boot `

### [Down and install armv7a stage3 and portage]

`root `[`#`]`cd /mnt/gentoo `

`root `[`#`]`wget -c `[`http://distfiles.gentoo.org/releases/arm/autobuilds/20161129/stage3-armv7a-20161129.tar.bz2`](http://distfiles.gentoo.org/releases/arm/autobuilds/20161129/stage3-armv7a-20161129.tar.bz2)` `

`root `[`#`]`tar xvpf stage3-armv7a-20161129.tar.bz2 -C /mnt/gentoo `

`root `[`#`]`wget `[`http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2`](http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2)` `

`root `[`#`]`tar xjf portage-latest.tar.bz2 -C /mnt/gentoo/usr `

### [Copy modules firmware to Gentoo]

`root `[`#`]`cp /home/username/firmware /mnt/gentoo/lib `

`root `[`#`]`cp /home/username/modules /mnt/gentoo/lib `

`root `[`#`]`cp /home/username/etc/firmware /mnt/gentoo/etc `

### [Edit fstab]

`root `[`#`]`nano /mnt/gentoo/etc/fstab `

[FILE] **`/etc/fstab`Example**

    /dev/mmcblk0p1          /boot           vfat            umask=033       1 2
    /dev/mmcblk0p2          /               ext4            defaults        0 1

### [Change root passwd]

`root `[`#`]`sed -i 's/^root:.*/root::::::::/' /mnt/gentoo/etc/shadow `

### [Start wifi insmod wifi driver]

`root `[`#`]`cd /etc/init.d/ `

`root `[`#`]`cp net.lo net.eth0 `

`root `[`#`]`cp net.lo net.wlan0 `

`root `[`#`]`nano /etc/local.d/insmod.start `

[FILE] **`/etc/local.d/insmod.start`**

    insmod  /lib/modules/3.4.39_zero/xradio_wlan.ko #insmod modules

See the [Wireless section](https://wiki.gentoo.org/wiki/Handbook:AMD64/Networking/Wireless "Handbook:AMD64/Networking/Wireless") of the Gentoo Handbook for more information.

Now put the SD card in the Orange PI Zero. Power requirements are 2 Amps. Wifi requires 3.3v.