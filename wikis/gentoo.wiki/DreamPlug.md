## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Disk partitions]](#Disk_partitions)
-   [[3] [U-boot]](#U-boot)
-   [[4] [Kernel]](#Kernel)
    -   [[4.1] [Roll your own]](#Roll_your_own)
        -   [[4.1.1] [Manually appending the device tree]](#Manually_appending_the_device_tree)
        -   [[4.1.2] [Cross-compiling]](#Cross-compiling)
        -   [[4.1.3] [Built-in vs modular drivers]](#Built-in_vs_modular_drivers)
        -   [[4.1.4] [Kernel configuration]](#Kernel_configuration)
    -   [[4.2] [Pre-built images]](#Pre-built_images)
-   [[5] [External resources]](#External_resources)

## [Hardware]

+-------------------------------------------+---------------------------------------------------------------------+
| System on Chip                            | Kirkwood MV88F6281-A1                                               |
+-------------------------------------------+---------------------------------------------------------------------+
| CPU                                       | Feroceon 88FR131 rev 1 (v5l) a.k.a. Marvel Sheeva 1.2 GHz (ARMv5TE) |
+-------------------------------------------+---------------------------------------------------------------------+
| RAM                                       | 512 MiB 16bit DDR2-800 MHz                                          |
+-------------------------------------------+---------------------------------------------------------------------+
| Internal storage                          | 4 GiB on board micro-SD                                             |
+-------------------------------------------+---------------------------------------------------------------------+
| Internet connectivity                     | -   2 x Gigabit Ethernet 10/100/1000 Mbps                           |
|                                           | -   WiFi 802.11 b/g                                                 |
|                                           | -   Bluetooth BT2.1 + EDR                                           |
|                                           | -   JTAG and UART connections for external module                   |
+-------------------------------------------+---------------------------------------------------------------------+
| External storage and connectivity         | -   2 x USB 2.0 ports (Host)                                        |
|                                           | -   1 x eSATA 2.0 port -3Gbps SATAII                                |
|                                           | -   1 x SD socket for user expansion/application                    |
+-------------------------------------------+---------------------------------------------------------------------+
| Audio interfaces Headphone (analogue) out | -   Mic In                                                          |
|                                           | -   Fiber Optics (SP/DIF) out                                       |
+-------------------------------------------+---------------------------------------------------------------------+
| Power suppy                               | 5V3A DC power supply (yes, it consumes \<5 W!)                      |
+-------------------------------------------+---------------------------------------------------------------------+
| Physical dimensions                       | 120mm (L) x 90mm (W) x 30mm (H)                                     |
+-------------------------------------------+---------------------------------------------------------------------+

## [Disk partitions]

While unless you have a good reason you should be mounting partitions using UUID or Label, the existing disk partitions are as follows:

-   [/dev/sda] is the internal SD card and separated so sda1 is a \~100 MiB FAT16 partition with kernel uImages and sda2 is a \~4 GiB ext3 partition carrying the stock (in my case Debian) OS.
-   [/dev/sdb] is the external SD card slot
-   [/dev/sdc] is the first external disk via USB or eSATA
-   The rest follows in the same logic.

## [U-boot]

A clean u-boot environment that first boots from the external USB and has an option to boot from the internal SD (check yours with printenv).

To switch just change the bootcmd to include either gentoo_bootcmd (for USB) or stock_bootcmd (for internal SD).

    bootdelay=3
    baudrate=115200
    ethact=egiga0
    ethaddr=F0:AD:4E:00:B0:8E
    eth1addr=F0:AD:4E:00:B0:8F
    clear_kernel_in_mem=echo Purging kernel in memory; mw 0x6400000 0x0 0x300000
    ipaddr=192.168.1.103
    serverip=192.168.1.111
    x_bootcmd_usb=usb start
    x_bootcmd_ethernet=192.168.1.1
    stock_bootargs=root=/dev/sda2 rootdelay=10 console=ttyS0,115200
    gentoo_bootargs=root=/dev/sdc2 rootdelay=10 console=ttyS0,115200
    stock_load_kernel=fatload usb 0 0x6400000 uImage
    stock_bootcmd=usb start; fatload usb 0 0x6400000 uImage; setenv bootargs root=/dev/sda2 rootdelay=10 console=ttyS0,115200; bootm 0x6400000;
    gentoo_bootcmd=usb start; fatload usb 0 0x6400000 uImage; setenv bootargs root=/dev/sdc2 rootdelay=10 console=ttyS0,115200; bootm 0x6400000;
    bootcmd=clear_kernel_in_mem; run gentoo_bootcmd
    stdin=serial
    stdout=serial
    stderr=serial

    Environment size: 838/4092 bytes

Don't forget to \`saveenv\` if you want to keep the environment after the reboot.

** Note**\
You have to escape ; with \\ if you want to use it in setenv.

** Note**\
If you want to remove a setenv line, just call setenv with the variable, but no definition (e.g. \`setenv x_boot_lala\` will delete the line that defines x_boot_lala).

## [Kernel]

### [Roll your own]

The stock version of U-Boot that ships with the DreamPlug does not pass a device tree as required by newer kernels. Flashing a newer version of U-Boot is an option but due to the way the hardware initializes, this is extremely tedious to do, if not almost impossible. On [Freedombox wiki](http://www.freedomboxfoundation.org/ubootUpgradeInstructions/index.en.html) there are probably the most up-to-date uBoot images for DreamPlug and instructions. [This poor user](https://wiki.gentoo.org/wiki/User:Chewi "User:Chewi") tried unsuccessfully for two days. Alternatively, newer kernels (3.2+) support appending the device tree to the kernel image manually. Give yourself an easy life with the following steps.

#### [Manually appending the device tree]

This method is tested to work on 3.6 kernels. [This other poor user](https://wiki.gentoo.org/index.php?title=User:Hook&action=edit&redlink=1 "User:Hook (page does not exist)") failed at getting it to work on 3.5, 3.6 worked as a charm though.

1.  `emerge dev-embedded/u-boot-tools`
2.  Configure and build the kernel as usual with CONFIG_ARM_APPENDED_DTB enabled.
    1.  `make kirkwood-dreamplug.dtb`
    2.  `cat $dtb_file_from_the_output_of_previous_command >> arch/arm/boot/zImage`
    3.  `make uImage`
3.  Copy [arch/arm/boot/uImage] to the device. Don\'t forget the modules!

#### [Cross-compiling]

The DreamPlug is not very fast. Save some time and build the kernel on another machine. Only a stage 1 toolchain is required for building a kernel.

1.  `emerge sys-devel/crossdev`
2.  `crossdev -s1 -t arm-none-eabi`
3.  Append **ARCH=arm CROSS_COMPILE=arm-none-eabi-** to all invocations of make.

#### [Built-in vs modular drivers]

Be aware that building the SATA driver (sata_mv) into the kernel will result in any drives attached to the DreamPlug at boot time taking priority over any SD cards. In other words, [/dev/sda] will be a SATA drive, not an SD card. This will most likely cause a boot failure. The simplest option is to build the driver as a module. Another option is to use an initrd. If neither of these appeal, there is a third option as of 3.7. You can now specify the root device in the form **root=PARTUUID=XXXXXXXX-XX** with an NT disk signature and partition number. This has been verified to work on the DreamPlug.

#### [Kernel configuration]

A minimal(ish) kernel configuration for 3.6.5 can be found [here](http://dev.gentooexperimental.org/~chewi/dreamplug-kernel-config.txt). Only DreamPlug hardware drivers have been enabled, except for wireless and Bluetooth, which have been left disabled for security reasons.

### [Pre-built images]

You can still use a pre-built kernel image, like the ones available on [PlugComputer Forums](http://www.plugcomputer.org/plugforum/index.php?board=2.0) ...but where\'s the fun in that? ;)

## [External resources]

-   [armin76's (un)official SheevaPlug howto](http://dev.gentoo.org/~armin76/arm/sheevaplug/install.xml)
-   [richardgroux' blog post on dual-booting Gentoo and Debian on a DreamPlug](https://sites.google.com/site/richardgroux/tools/dreamplug)