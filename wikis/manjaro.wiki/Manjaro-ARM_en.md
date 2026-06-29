[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Manjaro-ARM&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Manjaro-ARM "Manjaro-ARM (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Manjaro-ARM/ru "Manjaro-ARM (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Manjaro-ARM/fa "مانجارو-آرم (ARM) (33% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Manjaro-ARM/zh-cn "Manjaro-ARM (33% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Preparing the SPI (optional)]](#Preparing_the_SPI_.28optional.29)
    -   [[2.2] [Downloading]](#Downloading)
    -   [[2.3] [Writing the Installation Media]](#Writing_the_Installation_Media)
    -   [[2.4] [Cleanup and First Boot]](#Cleanup_and_First_Boot)
    -   [[2.5] [Resizing the partitions]](#Resizing_the_partitions)
    -   [[2.6] [Login]](#Login)
-   [[3] [Supported Devices]](#Supported_Devices)
    -   [[3.1] [Device List]](#Device_List)
        -   [[3.1.1] [Hardkernel]](#Hardkernel)
        -   [[3.1.2] [Khadas]](#Khadas)
        -   [[3.1.3] [Orange Pi]](#Orange_Pi)
        -   [[3.1.4] [Pine64]](#Pine64)
        -   [[3.1.5] [Radxa]](#Radxa)
        -   [[3.1.6] [RaspberryPi]](#RaspberryPi)
        -   [[3.1.7] [Ugoos]](#Ugoos)
    -   [[3.2] [Android TV boxes]](#Android_TV_boxes)
-   [[4] [Raspberry Pi Tips]](#Raspberry_Pi_Tips)
    -   [[4.1] [Sensors]](#Sensors)
    -   [[4.2] [Overclocking]](#Overclocking)
-   [[5] [Raspberry Pi Troubleshooting]](#Raspberry_Pi_Troubleshooting)
    -   [[5.1] [Pi 400 Power Button]](#Pi_400_Power_Button)
    -   [[5.2] [Blocked Update]](#Blocked_Update)
    -   [[5.3] [Missing Bluetooth after raspberrypi-bootloader/-x update 20210208-1]](#Missing_Bluetooth_after_raspberrypi-bootloader.2F-x_update_20210208-1)
-   [[6] [Unsupported Devices]](#Unsupported_Devices)
-   [[7] [See also]](#See_also)

# [Overview]

The Manjaro distribution, but for ARM devices.

Based on Arch Linux ARM, combined with Manjaro tools, themes and infrastructure to make install images for your ARM device, like the Pinebook and Raspberry Pi.

# [Installation]

### [][Preparing the SPI (optional)]

Some boards have an SPI storage chip. This is a small storage device, usually 4-16 MB in size, that the board checks for firmware before proceeding to other devices. So we can utilize this chip, by preparing the board specific firmware on it, making it able to boot our [generic image](https://github.com/manjaro-arm/generic-images/releases) and our [generic EFI image](https://github.com/manjaro-arm/generic-efi-images/releases).\
We have currently tested [Tow-Boot](https://github.com/Tow-Boot/Tow-Boot), so that\'s what this guide will use.

1.  Go to the [latest release section](https://github.com/Tow-Boot/Tow-Boot/releases) of Tow-Boot and download the file that matches your board. This is important.
2.
3.  Unpack it and flash the \`spi.installer.img\` file to a spare SD card. If the archive does not contain any spi.installer.img file for your board, you should use one of our pre-built OS images instead, which has the Shared Storage version of U-boot installed.
4.
5.  Insert the SD card into your device and boot from it. You will be presented with a short menu. One entry is \"Flash Tow-Boot to SPI\", second entry is \"Erase SPI Flash\" and the last option is \"Reboot\".
6.
7.  Select the \"Flash Tow-Boot to SPI\" option and wait until it finishes successfully. It can take a couple of minutes as SPI storage is rather slow.
8.
9.  When it\'s done, power off the device and take out the SD card. Now your device has the Tow-Boot board firmware in place and should now be capable of booting any generic (EFI) aarch64 image that supports your board.

Our Generic Aarch64 image supports the Extlinux booting scheme, while our Generic EFI Aarch64 uses EFI enabled firmware (which tow-boot has).

### [Downloading]

You can find installation images in the downloads section of the [Manjaro Website](https://manjaro.org/download/#ARM).\
Find the image that matches your target device and desired edition.\
Or if you have Board Firmware on your SPI, you can try our new [Generic Aarch64 images](https://github.com/manjaro-arm/generic-images/releases).

### [Writing the Installation Media]

The images are in a .xz file. These files can be burned directly to an SD card with Etcher or with dd directly.\
To manually install to your SD card with dd:

Extract the image.

    unxz Manjaro-ARM-[Edition]-[Device]-[Version].xz

Get it on the SD card

    sudo dd if=Manjaro-ARM-[Edition]-[Device]-[Version].img of=/dev/[device] bs=4M

Where *\[device\]* is your SD card\'s device, as seen by lsblk. Usually mmcblk0 or sdb.

\

### [Cleanup and First Boot]

Once you have the image on the SDCard, you should be able to put the card into your device and plug it in. If everything worked correctly, it should boot to the OEM setup. Here you define your username, passwords locales etc. Once that is done, the script will clean up after itself, resize the partition and reboot the device. After that reboot, it should boot to the Operating System. Depending on the edition you have installed, this could be a simple TTY login or a graphical desktop environment.

### [Resizing the partitions]

Since 18.09 this is now done automatically. The device will boot to OEM setup, which will handle the resizing, and then reboot before the login screen would appear. When it\'s booted to the login screen, the filesystem has been resized to fill out the remaining space on the SD card.

\

### [Login]

Login depends on what you set up during the OEM setup. There are 1 users by default on the image. root. And by default it has no password and autologin enabled. This gets changed when the OEM script is run, to disable the autologin and set the password defined during the setup.

# [Supported Devices]

Devices listed here are either supported by having device specific images, runs from the Generic images with board firmware on SPI or is still installable via the [Manjaro ARM Installer](https://gitlab.manjaro.org/manjaro-arm/applications/manjaro-arm-installer) script.

## [Device List]

### [Hardkernel]

  ---------------- -------------- ------------------ ------------- ---------- ----------------- --------------- ------------------ --------------- -----------------------
  Model            Release Year   SoC Manufacturer   Lithography   CPU        CPU Topology      CPU Frequency   GPU                Memory          Generic Image Support

  **Odroid C2**    2016           Amlogic            28nm          S905       Quad-core:\       4 x 1.5GHz      Mali-450 MP3       2GB DDR3        No
                                                                              4 x Cortex-A53

  **Odroid C4**    2020           Amlogic            12nm          S905X3     Quad-core:\       4 x 2.0GHz      Mali-G31 MP2       4GB DDR4        No
                                                                              4 x Cortex-A55

  **Odroid N2**    2019           Amlogic            12nm          S922X      Hexa-core:\       4 x 2.0GHz\     Mali-G52 MP4       2-4GB DDR4      Yes
                                                                              4 x Cortex-A73\   2 x 1.8GHz
                                                                              2 x Cortex-A53

  **Odroid N2+**   2020           Amlogic            12nm          S922X      Hexa-core:\       4 x 2.4GHz\     Mali-G52 MP4       2-4GB DDR4      Yes
                                                                              4 x Cortex-A73\   2 x 1.9GHz
                                                                              2 x Cortex-A53

  **Odroid M1**    2021           Rockchip           22nm          RK3568B2   Quad-core:\       4 x 2.0GHz      Mali-G52 2EE MC2   4--8GB LPDDR4   No
                                                                              4 x Cortex-A55
  ---------------- -------------- ------------------ ------------- ---------- ----------------- --------------- ------------------ --------------- -----------------------

### [Khadas]

  ------------ -------------- ------------------ ------------- -------- ----------------- --------------- --------------- -------------- -----------------------
  Model        Release Year   SoC Manufacturer   Lithography   CPU      CPU Topology      CPU Frequency   GPU             Memory         Generic Image Support

  **Edge-V**   2018           Rockchip           28nm          RK3399   Hexa-core:\       2 x 1.8GHz\     Mali-T860 MP4   2-4GB LPDDR4   No
                                                                        2 x Cortex-A72\   4 x 1.5GHz
                                                                        4 x Cortex-A53

  **Vim 1**    2016           Amlogic            28nm          S905X    Quad-core:\       4 x 1.5GHz      Mali-450 MP3    2GB DDR3       No
                                                                        4 x Cortex-A53

  **Vim 2**    2017           Amlogic            28nm          S912     Octa-core:\       8 x 1.5GHz      Mali-T820 MP3   2-3GB LPDDR4   No
                                                                        8 x Cortex-A53

  **Vim 3**    2019           Amlogic            12nm          A311D    Hexa-core:\       4 x 2.2GHz\     Mali-G52 MP4    2-4GB LPDDR4   No
                                                                        4 x Cortex-A73\   2 x 1.8GHz
                                                                        2 x Cortex-A53
  ------------ -------------- ------------------ ------------- -------- ----------------- --------------- --------------- -------------- -----------------------

### [Orange Pi]

  --------------------- -------------- ------------------ ------------- -------- ----------------- --------------- --------------- -------------- -----------------------
  Model                 Release Year   SoC Manufacturer   Lithography   CPU      CPU Topology      CPU Frequency   GPU             Memory         Generic Image Support

  **Orange Pi 3 LTS**   2019           Allwinner          28nm          H6       Quad-core:\       4 x 1.8GHz      Mali-T720 MP2   1-2GB LPDDR3   No
                                                                                 4 x Cortex-A53

  **Orange Pi 4 LTS**   2021           Rockchip           28nm          RK3399   Hexa-core:\       2 x 2.0GHz\     Mali-T860 MP4   2-4GB LPDDR4   No
                                                                                 4 x Cortex-A73\   4 x 1.5GHz
                                                                                 2 x Cortex-A53

  **Orange Pi 800**     2022           Rockchip           28nm          RK3399   Hexa-core:\       2 x 2.0GHz\     Mali-T860 MP4   2-4GB LPDDR4   No
                                                                                 4 x Cortex-A73\   4 x 1.5GHz
                                                                                 2 x Cortex-A53
  --------------------- -------------- ------------------ ------------- -------- ----------------- --------------- --------------- -------------- -----------------------

### [Pine64]

  ------------------- -------------- ------------------ ------------- -------- ----------------- --------------- --------------- ---------------------- -----------------------
  Model               Release Year   SoC Manufacturer   Lithography   CPU      CPU Topology      CPU Frequency   GPU             Memory                 Generic Image Support

  **Rock64**          2017           Rockchip           28nm          RK3328   Quad-core:\       4 x 1.5GHz      Mali-450 MP2    1-4GB LPDDR3           No
                                                                               4 x Cortex-A53

  **RockPro64**       2017           Rockchip           28nm          RK3399   Hexa-core:\       2 x 2.0GHz\     Mali-T860 MP4   2-4GB LPDDR4           Yes
                                                                               4 x Cortex-A73\   4 x 1.5GHz
                                                                               2 x Cortex-A53

  **Pine H64**        2019           Allwinner          28nm          H6       Quad-core:\       4 x 1.8GHz      Mali-T720 MP2   2-4GB LPDDR3           Yes
                                                                               4 x Cortex-A53

  **Pinebook**        2017           Allwinner          40nm          A64      Quad-core:\       4 x 1.152GHz    Mali-400 MP2    2GB LPDDR3             Yes
                                                                               4 x Cortex-A53

  **Pinebook Pro**    2019           Rockchip           28nm          RK3399   Hexa-core:\       2 x 2.0GHz\     Mali-T860 MP4   4GB LPDDR4             Yes
                                                                               2 x Cortex-A72\   4 x 1.5GHz
                                                                               4 x Cortex-A53

  **Pinephone**       2019           Allwinner          40nm          A64      Quad-core:\       4 x 1.2GHz      Mali-400 MP2    2-3GB LPDDR3           No
                                                                               4 x Cortex-A53

  **Pinephone Pro**   2022           Rockchip           28nm          RK3399   Hexa-core:\       2 x 1.5GHz\     Mali-T860 MP4   4GB LPDDR4 \@800 MHz   No
                                                                               2 x Cortex-A72\   4 x 1.5GHz
                                                                               4 x Cortex-A53
  ------------------- -------------- ------------------ ------------- -------- ----------------- --------------- --------------- ---------------------- -----------------------

### [Radxa]

  --------------------- -------------- ------------------ ------------- -------- ----------------- --------------- --------------- --------------- -----------------------
  Model                 Release Year   SoC Manufacturer   Lithography   CPU      CPU Topology      CPU Frequency   GPU             Memory          Generic Image Support

  **Rock Pi 4B & 4C**   2019           Rockchip           28nm          RK3399   Hexa-core:\       2 x 2.0GHz\     Mali-T860 MP4   1--4GB LPDDR4   Yes
                                                                                 2 x Cortex-A72\   4 x 1.5GHz
                                                                                 4 x Cortex-A53

  **Radxa Zero**        2021           Amlogic            12nm          S905Y2   Quad-core:\       4 x 1.8GHz      Mali-G31 MP2    1-4GB LPDDR4    No
                                                                                 4 x Cortex-A53

  **Rock 3A**           2022           Rockchip           22nm          RK3568   Quad-core:\       4 x 2.0GHz      Mali-G52 2EE    2-8GB LPDDR4    No
                                                                                 4 x Cortex-A55
  --------------------- -------------- ------------------ ------------- -------- ----------------- --------------- --------------- --------------- -----------------------

### [RaspberryPi]

  ------------ -------------- ------------------ ------------- ----------- ---------------- --------------- -------------- -------------- -----------------------
  Model        Release Year   SoC Manufacturer   Lithography   CPU         CPU Topology     CPU Frequency   GPU            Memory         Generic Image Support

  **Pi 3B**    2016           Broadcom           28nm          BCM2837     Quad-core:\      4 x 1.2GHz      VideoCore IV   1GB LPDDR2     No
                                                                           4 x Cortex-A53

  **Pi 3B+**   2018           Broadcom           28nm          BCM2837B0   Quad-core:\      4 x 1.4GHz      VideoCore IV   1GB LPDDR2     No
                                                                           4 x Cortex-A53

  **Pi 400**   2020           Broadcom           28nm          BCM2711     Quad-core:\      4 x 1.5GHz      VideoCore VI   4GB LPDDR4     No
                                                                           4 x Cortex-A72

  **Pi 4B**    2019           Broadcom           28nm          BCM2711     Quad-core:\      4 x 1.5GHz      VideoCore VI   1-8GB LPDDR4   No
                                                                           4 x Cortex-A72
  ------------ -------------- ------------------ ------------- ----------- ---------------- --------------- -------------- -------------- -----------------------

### [Ugoos]

  -------------- -------------- ------------------ ------------- -------- ----------------- --------------- -------------- ------------ -----------------------
  Model          Release Year   SoC Manufacturer   Lithography   CPU      CPU Topology      CPU Frequency   GPU            Memory       Generic Image Support

  **AM6 Plus**   2019?          Amlogic            12nm          S922XJ   Hexa-core:\       4 x 2.2GHz\     Mali-G52 MP6   4GB LPDDR4   No
                                                                          4 x Cortex-A73\   2 x 1.9GHZ
                                                                          2 x Cortex-A53
  -------------- -------------- ------------------ ------------- -------- ----------------- --------------- -------------- ------------ -----------------------

## [Android TV boxes]

With a couple of small tweaks it is possible to boot and install the vim3 builds of Manjaro on some [Amlogic TV boxes](//wiki.manjaro.org/index.php?title=Amlogic_TV_boxes "Amlogic TV boxes"). Running Manjaro on TV boxes is not recommended for less experienced users of Linux nor serious production use.

# [Raspberry Pi Tips]

## [Sensors]

For temperature and humidity sensor see this tutorial on the forums: [https://forum.manjaro.org/t/howto-raspberry-pi-temperature-and-humidity-sensor-dht22-dht11-am2302/34685](https://forum.manjaro.org/t/howto-raspberry-pi-temperature-and-humidity-sensor-dht22-dht11-am2302/34685)

## [Overclocking]

You can manage voltage and frequency settings in your `/boot/config.txt`. The following are the most common values for the Raspberry Pi:

     over_voltage=6
     arm_freq=2100
     gpu_freq=650

# [Raspberry Pi Troubleshooting]

## [Pi 400 Power Button]

If you have trouble using the power button on your Pi 400 with the XFCE desktop (or xfce4-power-manager) then make sure logind is handling button events:

    xfconf-query -c xfce4-power-manager -p /xfce4-power-manager/logind-handle-power-key -n -t bool -s true

## [Blocked Update]

There are device-dependent workarounds if you experience an error similar to:

    error: failed to prepare transaction (conflicting dependencies)
    :: brcm-patchram-plus and pi-bluetooth are in conflict

For the **Pi 3B**:

    sudo systemctl disable brcm43438.service
    sudo pacman -S -dd  brcm-patchram-plus-pi3b firmware-raspberrypi
    sudo systemctl enable attach-bluetooth-pi3.service

For the **Pi 3B+**:

    sudo systemctl disable brcm43438.service
    sudo pacman -S -dd  brcm-patchram-plus firmware-raspberrypi
    sudo systemctl enable attach-bluetooth.service

For the **Pi 4B**:

    sudo systemctl disable brcm43438.service
    sudo pacman -S -dd  brcm-patchram-plus firmware-raspberrypi
    sudo systemctl enable attach-bluetooth.service

For the **Pi 400**:

sudo systemctl disable brcm43438.service

    sudo pacman -S -dd  brcm-patchram-plus-pi400 firmware-raspberrypi
    sudo systemctl enable attach-bluetooth-pi400.service

## [][Missing Bluetooth after raspberrypi-bootloader/-x update 20210208-1]

First, check whether the bootloader has been updated:

    pacman -Ss raspberrypi-bootloader

Possible results:

    core/raspberrypi-bootloader 20210208-1 [installed]
       Bootloader files for Raspberry Pi
    core/raspberrypi-bootloader-x 20210208-1 [installed]
       Bootloader with extra codecs for Raspberry Pi

If it is the case, changing the occurrences of **ttyAMA0** in /boot/cmdline.txt to **serial0** may fix missing Bluetooth ([Source](https://forum.manjaro.org/t/new-raspberry-pi-kernels-related-packages/4721/344)).

# [Unsupported Devices]

In general, any device that does not have a device specific image or works with the Generic image, is considered unsupported. We may drop support for a device when the manufacturer no longer sells the device. The device is then considered EOL (End-Of-Life). Such a device might still work by updating and old image or running the Generic image, but we no longer work to keep it working.

# [See also]

[https://wiki.archlinux.org/index.php/Category:ARM_architecture](https://wiki.archlinux.org/index.php/Category:ARM_architecture)\
[https://archlinuxarm.org/wiki](https://archlinuxarm.org/wiki)\
[https://osdn.net/projects/manjaro-arm/](https://osdn.net/projects/manjaro-arm/)\
\