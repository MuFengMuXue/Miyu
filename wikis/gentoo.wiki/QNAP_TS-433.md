**Resources**

[[]][Home](https://www.qnap.com/en/product/ts-433)

The QNAP TS-433-4G is a Rockchip RK3568 (ARMv8-A, Cortex-A55) based NAS. Because of the great work of [Heiko Stübner](https://github.com/mmind), there is from kernel version 6.14 upstream support for this SoC. Makes for a great NAS with 4x 3.5\" HDD slots.

Easiest way to install Gentoo on the system, is to prepare a USB device you can boot from, and then use that to install Gentoo on the eMMC itself. You should have a serial cable and confirm that it works before beginning. See the instructions on [u-boot](https://docs.u-boot.org/en/latest/board/qnap/ts433.html)

With the serial cable working, you can gain access to the preinstalled Linux image provided by QNAP. I suggest using this to make a full image backup of the whole eMMC by doing `dd if=/dev/mmcblk0 bs=1M | ssh somewhere dd of=backup.img bs=1M`

## [Installing the bootloader]

Rockchip uses GPT as its partition scheme, and embeds u-boot before the first partition. So remember to leave some room at the beginning when creating your partitions.

Follow the guide from [u-boot](https://docs.u-boot.org/en/latest/board/qnap/ts433.html) to build and install u-boot for the device.

Do note that this board does not like all 5V to TTL 3.3V-adapters out there. If you want to make sure you will get a working serial console, try this cable: [https://ftdichip.com/products/ttl-232r-3v3/](https://ftdichip.com/products/ttl-232r-3v3/) (don\'t connect VCC).

## [Installing Gentoo]

After installing your own u-boot at the beginning on the eMMC, you should know that u-boot looks after /boot/extlinux/extlinux.conf or /extlinux/extlinux.conf on the first partition it sees (formatted with ext4). This will work both from USB and from eMMC. The system will not boot QNAP OS when you update u-boot, so the easiest way is just providing a usb drive with a working boot and root partition.

Example partition layout:

`root `[`#`]`# gdisk -l /dev/mmcblk0 `

GPT fdisk (gdisk) version 1.0.10

Partition table scan:

     MBR: protective
     BSD: not present
     APM: not present
     GPT: present

Found valid GPT with protective MBR; using GPT. Disk /dev/mmcblk0: 7733248 sectors, 3.7 GiB Sector size (logical/physical): 512/512 bytes Disk identifier (GUID): B0ABD73E-F302-449B-88FF-C4A53275B1F1 Partition table holds up to 128 entries Main partition table begins at sector 2 and ends at sector 33 First usable sector is 34, last usable sector is 7733214 Partitions will be aligned on 2048-sector boundaries Total free space is 34749 sectors (17.0 MiB)

Number Start (sector) End (sector) Size Code Name

      1           32768          573439   264.0 MiB   8300  uboot
      2          573440         7731199   3.4 GiB     8305  Linux ARM64 root (/)

Kernel sources with patches for TS-433 (from 6.14 you can use upstream): [https://github.com/mmind/linux-rockchip/commits/dev/qnap-ts433/mainline/](https://github.com/mmind/linux-rockchip/commits/dev/qnap-ts433/mainline/)

With an arm64 compiler chain, do: `make qnap-ts433_defconfig` and `make -j4 && make modules_install` (and get the modules to the target filesystem, of course.)

/boot (mmcblk0p1 (GPT) or USB partition 1 (GPT), ext4) should contain these files:

`rk3568-qnap-ts433.dtb` (from arch/arm64/boot/dts)\
`Image` (from arch/arm64/boot)\
`extlinux/extlinux.conf`\
and a boot -\> . symlink (`ln -s boot .` in /boot)

[FILE] **`/boot/extlinux/extlinux.conf`extlinux.conf example**

    label gentoo
        kernel /boot/Image
        fdt /boot/rk3568-qnap-ts433.dtb
        append earlycon=uart8250,mmio32,0xfe660000 console=tty1 console=ttyS2,115200n8 rw root=/dev/mmcblk0p2 rootwait init=/sbin/init

Partition 2 could be a normal stage3 arm64, works just fine out of the box.