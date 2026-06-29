**Resources**

[[]][Manufacturer](https://www.hardkernel.com)

[[]][Official ODROID-M1S wiki](https://wiki.odroid.com/odroid-m1s/odroid-m1s)

[[]][ODROID](https://en.wikipedia.org/wiki/ODROID "wikipedia:ODROID")

This article is a supplementary guide for the nuances of installing Gentoo on the M1S system. This guide assumes the user can boot the system via a drive that is not the installation destination(SD card or onboard MMC). It will begin with assuming the user has done nothing to the XU4 and assuming that the M1S has internet access to it. The guide will walk through steps that are outside the standard Gentoo handbook, and will refer back to the handbook for standard installation sections. This guide will cover, getting a boot-able image usable for installation, minor U-boot configuration, and lastly kernel requirements to make a boot-able system. This guide is based off the [ODROID-XU4](https://wiki.gentoo.org/wiki/Hardkernel_ODROID-XU4 "Hardkernel ODROID-XU4") and [ODROID-N2](https://wiki.gentoo.org/wiki/Hardkernel_ODROID-N2 "Hardkernel ODROID-N2") Wiki articles.

** Note**\
This guide does not cover any of the GPIO interface equipment

## Contents

-   [[1] [Prerequisites]](#Prerequisites)
-   [[2] [Booting installation media]](#Booting_installation_media)
    -   [[2.1] [Getting an image]](#Getting_an_image)
    -   [[2.2] [Micro SD-Card preparation Option 1]](#Micro_SD-Card_preparation_Option_1)
    -   [[2.3] [OTG mmc writing]](#OTG_mmc_writing)
    -   [[2.4] [Place image on SD card]](#Place_image_on_SD_card)
    -   [[2.5] [Boot and installation]](#Boot_and_installation)
-   [[3] [Gentoo installation]](#Gentoo_installation)
-   [[4] [Kernel building]](#Kernel_building)
-   [[5] [Making initramfs]](#Making_initramfs)
    -   [[5.1] [Install packages]](#Install_packages)
    -   [[5.2] [Modify Dracut configuraiton]](#Modify_Dracut_configuraiton)
-   [[6] [Kernel install and initramfs install]](#Kernel_install_and_initramfs_install)
-   [[7] [Boot loader configuration]](#Boot_loader_configuration)
    -   [[7.1] [Kernel Device tree DTS and DTB]](#Kernel_Device_tree_DTS_and_DTB)
    -   [[7.2] [Creating boot.scr]](#Creating_boot.scr)
-   [[8] [Finalizing]](#Finalizing)
-   [[9] [External resources]](#External_resources)

## [Prerequisites]

-   Computer running linux or unix based OS
-   Access to read/write to an SD-Card from this computer

## [Booting installation media]

### [Getting an image]

The official documentation is here and it points to images the user can download. [Odroid M1S OS images](https://wiki.odroid.com/odroid-m1s/os_images/os_images) Although this link uses an older image, for the purpose of this document the new version of Ubuntu 22 for the m1s was used. Available from here [Ubuntu M1S images](http://ppa.linuxfactory.or.kr/images/raw/arm64/jammy/) At the time of this writing this is the image that was used.

`user `[`$`]`wget `[`http://ppa.linuxfactory.or.kr/images/raw/arm64/jammy/ubuntu-22.04-server-odroidm1s-20231114.img.xz`](http://ppa.linuxfactory.or.kr/images/raw/arm64/jammy/ubuntu-22.04-server-odroidm1s-20231114.img.xz)

### [Micro SD-Card preparation Option 1]

The boot process of the M1s is described in the [ODROID-M1S wiki](https://wiki.odroid.com/odroid-m1s/board_support/boot_sequence) First the boot software loads U-Boot, which as to be a specific location, which then loads the actual kernel from the boot partition. Boot order is the SD card first then the eMMC

** Note**\
According to postings on the Odroid forms there are options to change the version of Uboot or running a special binary which is said to allow booting the system differently for example via the NVMe drive.

### [OTG mmc writing]

This has not been tested during the writing of this document, but according to the odroid wiki you can use OTG and their SDK to write to the eMMC drive.

### [Place image on SD card]

Once the image file has been downloaded, write it to the SD card. Please be careful of your system and drive lettering. Many people also use something like etcher to write images for windows or other operating systems.

`root `[`#`]`xz -dc ubuntu-22.04-server-odroidm1s-20231114.img.xz | dd of=/dev/sdY status=progress`

### [Boot and installation]

Place the SD card in the system and power the system on. A USB keyboard and HDMI compatible monitor or a Serial adapter compatible with the interface on the board will be required if access to the system is needed(EG: network is not working). SSH into the system using username odroid and password is the same.

** Note**\
According to this guide [\[1\]](https://www.famera.cz/blog/computers/gentoo-minimal-odroid-m1-upstream-kernel-lvm-luks.html) it is recommended to create two partitions for Bootloader use in the future. Although the MMC in the system comes partitioned with 2 partitions. 1 for boot and 2 for the OS.

## [Gentoo installation]

Installation from this point the user can follow the standard handbook. Come back here when the kernel is ready to be configured.

** Note**\
Please be mindful of x86/amd64 speicifc steps from the handbook, Generally this is going to be CFLAG optimizations etc. It is safe to skip those steps and just have a standard system

## [Kernel building]

The user can build the kernel manually or with genkernel. Below is a list of options that will need to be enabled. At the time of this writing only the 6.1.x kernel was able to boot and operate properly. 6.6.x and 5.10 were attempted, but did not work.

Edit kernel options:

[KERNEL]

    Platform selection --->
      [*] Rockchip Platforms
    Device Drivers --->
      [*] PCI support --->
         PCI controller drivers --->
           <*> Rockchip PCIe host controller
           [*] Rockchip PCIe endpoint controller
             DesignWare PCI Core Support --->
               [*] Rockchip DesignWare PCIe controller
      <*> Memory Technology Device (MTD) suport --->
        <M> SPI NOR device support
      -*- Device Tree and Open Firmware support --->
        [*] Device Tree overlays
       NVME Support --->
        <*> NVME Exporess block device
      [*] Network device support --->
        [*] Ethernet driver support  --->
          [*] STMicroelectronics devices
            <*> STMicroelectronics Multi-Gigabit Ethernet driver
              <*> STMMAC Platform bus support
                <*> Generic driver for DWMAC
                <*> Rockchip dwmac support
         PHY Device support and infrastructure --->
           <*> Rockchip Ethernet PHYs
      Character devices  --->
        <*> Serial device bus  --->
          [*]   Serial device TTY port controller
        Serial drivers  --->
          <*> 8250/16550 and compatible serial support
          [*]   Console on 8250/16550 and compatible serial port
          [*]   DMA support for 16550 compatible UART controllers
          <*>   8250/16550 PCI device support
          <*> Support for Synopsys DesignWare 8250 quirks
          <*> Devicetree based probing for 8250 ports
          [*] Early console using ARM semihosting
      I2C support --->
        I2c Hardware Bus support --->
          <M> Rockchip RK3xxx I2C adapter
      PTP Clock support --->
        <M> PTP clock support
      Pin controllers --->
        <*> Pinctrl and GPIO driver for RK805 PMIC
        <*> Rockchip gpio and pinctrl driver
      [*] Voltage and Current Regulator Support --->
        <*>   PWM voltage regulator
        <*>   Rockchip RK805/RK808/RK809/RK817/RK818 Power regulators
      Graphics support  --->
        <*> Direct Rendering Manager (XFree86 4.1.0 and higher DRI support)
        <*> DRM Support for Rockchip
        <M> Panfrost (DRM support for ARM Mali Midgard/Bifrost GPUs)
      USB support --->
        <*>   xHCI HCD (USB 3.0) support
      <*> MMC/SD/SDIO card support  --->
         <*>   MMC block device drive
         <*>   Synopsys DesignWare Memory Card Interface
         <*>     Rockchip specific extensions for Synopsys DW Memory Card Interface
      IOMMU Hardware support --->
         [*]   Rockchip IOMMU Support
      SOC (System On Chip) specific Drivers  --->
         <*> Rockchip IO domain support
         [*] Rockchip generic power domain

** Note**\
All of these may not be required. The user can decide if they want to do built in vs module as well.

## [Making initramfs]

For this build Dracut is used for building the initramfs. This is done for the user when running make install in the kernel source tree. Before doing the dracut configuration needs to be modified. You will also need u-boot-tools installed.

### [Install packages]

`root `[`#`]`emerge --ask sys-kernel/dracut dev-embedded/u-boot-tools`

### [Modify Dracut configuraiton]

Then create the needed configuration file, this is needed to make it include the video card driver.

`root `[`#`]`mkdir -p /etc/dracut.conf.d/`

`root `[`#`]`echo 'add_dracutmodules+=" drm "' > /etc/dracut.conf.d/odroid.conf`

Edit the system dracut DRM script, the section that needs to be modified look like this. It is near the top of the file.

[FILE] **`/usr/lib/dracut/modules.d/50drm/module-setup.sh`**

    if [[ $ == arm* || $ == aarch64 ]]; then
            # arm/aarch64 specific modules needed by drm
            instmods \
                "=drivers/gpu/drm/i2c" \
                "=drivers/gpu/drm/panel" \
                "=drivers/gpu/drm/rockchip" \
                "=drivers/gpu/drm/panfrost" \
                "=drivers/gpu/drm/bridge" \
                "=drivers/video/backlight"
        fi

The rockchip and panfrost directories were added to this list.

## [Kernel install and initramfs install]

Lastly from the kernel source tree run the modules_install and install. This will execute dracut and place the kernel and initramfs in the /boot directory.

`root `[`#`]`make modules_install`

`root `[`#`]`make install`

The make install script also handles formatting the kernel and initramfs properly for boot with uboot. There is no need to use the mkImage script from uboot.

** Note**\
The user will need to make sure the /boot filesystem is mounted.

** Note**\
Uboot supports various file systems, but for this article ext4 was used.

## [Boot loader configuration]

** Note**\
The writer of this article is not very familiar with uboot and the ARM booting process, below is just a way that was found that made the system work correctly.

The boot file system now should just have your kernel along with the supporting files. The version of uboot currently with the M1S uses a boot.scr file to handle its configuration. We will create a boot.txt file to use as the source to build the .scr file. We will also require a DTB file from the boot medium for the system.

### [Kernel Device tree DTS and DTB]

** Note**\
This is a step the writer does not understand why it needs to be done. So if someone can share more information here it would be appreciated

First we will get the Device tree files. As of this writing the kernel source does not include the needed DTS file for the M1S hardware, thus we will use the one from the install medium. Create a new session into the running installation source OS(ubuntu). Go to the [/boot] directory and copy the dtb-6.1.0-odroid-arm64 or which ever one is available to your boot partition.

`root `[`#`]`cp /boot/dtb-6.1.0-odroid-arm64 /mnt/gentoo/boot`

Back inside the gentoo install, we will use the dtc \"compiler\" that comes with the kernel to \"re-compile\" the file.

`root `[`#`]`/usr/src/linux/scripts/dtc/dtc -I dtb -O dts -o /boot/source.dts /boot/dtb-6.1.0-odroid-arm64`

Then re-compile

`root `[`#`]`/usr/src/linux/scripts/dtc/dtc -I dts -O dtb -o /boot/dtb-6.1.74-gentoo-arm64 /boot/source.dts`

Cleanup the dtb file copied from the installation media

`root `[`#`]`rm /boot/dtb-6.1.0-odroid-arm64`

** Note**\
Once the DTS is in the kernel source tree, instead of the above the user would run make dtbs from the kernel source tree then copy the correct DTB file for your hardware to the [/boot] filesystem.

### [Creating boot.scr]

Now we create a boot.txt file

** Warning**\
While the boot.scr looks like a normal text file there is some binary data that mkImage adds to it so do not directly edit this file

[FILE] **`/boot/boot.txt`**

    #
    # flash-kernel: bootscr.odroid-rk3566
    #

    # Bootscript using the new unified bootcmd handling
    #
    # Expects to be called with the following environment variables set:
    #
    #  devtype              e.g. mmc/scsi etc
    #  devnum               The device number of the given type
    #  bootpart             The partition containing the boot files
    #                       (introduced in u-boot mainline 2016.01)
    #  prefix               Prefix within the boot partiion to the boot files
    #  kernel_addr_r        Address to load the kernel to
    #  fdt_addr_r           Address to load the FDT to
    #  ramdisk_addr_r       Address to load the initrd to.
    #
    # The uboot must support the booti and generic filesystem load commands.

    if test -z "$"; then
        setenv variant m1s
    fi
    setenv board odroid$

    setenv bootargs " $ root=YOUR_ROOT"
    setenv bootargs "$ rootwait pcie_aspm=off"
    setenv overlay_resize 8192

    setenv bootlabel "Gentoo"

    # Default TTY console
    setenv bootargs "$ console=tty1 console=ttyS2,1500000"

    # MISC
    #
    setenv bootargs "$ pci=nomsi"
    setenv bootargs "$ net.ifnames=0"

    load $ $:$ $ $config.ini \
        &&  ini generic $
    if test -n "$"; then
        ini overlay_$ $
    fi

    if test -n "$"; then
      setenv bootargs "$ console=$"
    fi

    if test -n "$"; then
      setenv bootargs "$ console=$"
    fi

    # kernel version string to append to filenames.
    if test -z "$"; then
       setenv fk_kvers "6.1.74-gentoo-arm64"
    fi

    if test -z "$"; then
       setenv fdtfile "rk3566-odroid-$.dtb"
    fi

    if test -z "$"; then
      setenv partition $
    else
      setenv partition $
    fi

    load $ $:$ $ $dtb-$ \
    fdt addr $

    if test "x" != "x"; then
        for overlay in $; do
            fdt resize $
            load $ $:$ $ $dtbs/$/rockchip/overlays/$/$
        done
    fi

    load $ $:$ $ $vmlinuz-$ \
    && unzip $ $ \
    && load $ $:$ $ $initramfs-$.img \
    && echo "Booting Gentoo $ from $ $:$..." \
    && booti $ $:$ $

    load $ $:$ $ $vmlinuz-$ \
    && load $ $:$ $ $initramfs-$.img \
    && echo "Booting Gentoo $ from $ $:$..." \
    && booti $ $:$ $

\
In this file the user will need to modify their kernel arguments and kernel version string. Kernel version is set on the line that looks like this **setenv fk_kvers \"6.1.74-gentoo-arm64\"** Kernel boot line arguments are built using lines like this **setenv bootargs \" \$ root=YOUR_ROOT\"** Some lines are configured for the user like Console etc. The user is required to put the correct root string for their system.(this is the kernel cmdline)

** Note**\
File naming standard will have to follow how this script is configured or the user will have to make their own modifications.

Once modifications have been made the file must be \"compiled\".

`root `[`#`]`mkimage -A arm64 -T script -O linux -n 'boot script' -C none -d /boot/boot.txt /boot/boot.scr`

This will properly format the boot.scr file for uboot.

## [Finalizing]

From here it is back to the handbook to complete the installation.

** Note**\
Remember to take out the SD card for the reboot into Gentoo, as it is the first boot priority

## [External resources]

-   [ODROID Forum » Post where questions were asked](https://forum.odroid.com/viewtopic.php?f=216&t=47989&p=382253#p382253)
-   [ODROID Forum » Switching to newer version of uboot](https://forum.odroid.com/viewtopic.php?p=381207#p381207)
-   [ODROID Forum » Booting to NVMe discussion](https://forum.odroid.com/viewtopic.php?f=211&t=47615)
-   [ODROID Wiki » building kernel](https://wiki.odroid.com/odroid-m1s/board_support/building_kernel)
-   [GitHub » tobetter\'s kernel repository for ODROID](https://github.com/tobetter/linux/tree/odroid-6.6.y)
-   [Linux Factory repository » Images that work with ODROID equipment](https://ppa.linuxfactory.or.kr/images/raw/arm64/jammy/)
-   [Ondrej Famera » Gentoo on Odroid-M1 (aarch64) with upstream 6.1.x kernel, LVM and LUKS](https://www.famera.cz/blog/computers/gentoo-minimal-odroid-m1-upstream-kernel-lvm-luks.html)
-   [Ondrej Famera » Gentoo on Odroid-M1 (aarch64)](https://www.famera.cz/blog/computers/gentoo-minimal-odroid-m1.html)