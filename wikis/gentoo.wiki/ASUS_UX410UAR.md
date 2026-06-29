\
This page editing is **in progress**, please let me know if I need to share something asap.

## Contents

-   [[1] [Gentoo Sources]](#Gentoo_Sources)
-   [[2] [What is working]](#What_is_working)
-   [[3] [lspci]](#lspci)
-   [[4] [Touchpad]](#Touchpad)
    -   [[4.1] [Kernel]](#Kernel)
        -   [[4.1.1] [Finding the good modules names]](#Finding_the_good_modules_names)
            -   [[4.1.1.1] [Step 1: Find the needed modules names]](#Step_1:_Find_the_needed_modules_names)
            -   [[4.1.1.2] [Step 2: Find the modules that are using those modules]](#Step_2:_Find_the_modules_that_are_using_those_modules)

## [Gentoo Sources]

You can find the .config file for the latest version in this [git repo](https://gitlab.com/elacheche/gentoo-asus-ux410uar)

## [What is working]

-   Built-in WiFi
-   Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter (check [commit #ed0a51998](https://gitlab.com/elacheche/gentoo-asus-ux410uar/-/commit/ed0a51998732943b970d36da52c5d79d7e90238e))
-   Webcam
-   Sound
-   Touchpad (see below)
-   Docker

\

## [lspci]

`user `[`$`]`lpci`

    00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v6/7th Gen Core Processor Host Bridge/DRAM Registers (rev 08)
    00:02.0 VGA compatible controller: Intel Corporation UHD Graphics 620 (rev 07)
    00:04.0 Signal processing controller: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Thermal Subsystem (rev 08)
    00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
    00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
    00:15.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #0 (rev 21)
    00:15.1 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #1 (rev 21)
    00:15.2 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO I2C Controller #2 (rev 21)
    00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
    00:17.0 SATA controller: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] (rev 21)
    00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #1 (rev f1)
    00:1c.7 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #8 (rev f1)
    00:1f.0 ISA bridge: Intel Corporation Sunrise Point LPC Controller/eSPI Controller (rev 21)
    00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
    00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
    00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
    02:00.0 Network controller: Intel Corporation Wireless 8265 / 8275 (rev 78)

\

## [Touchpad]

### [Kernel]

#### [Finding the good modules names]

A Devuan Live Session was used to debug the issue,because the Touchpad was perfectly working on that session.

##### [Step 1: Find the needed modules names]

To find the used module names, a trial and error way was used, the idea is to find all loaded modules and unload them one by one to see if the Touchpad behavior changes. Because we can\'t unload the modules used by other modules we\'ll only unload the unused ones.

[CODE]

    #!/usr/bin/env bash
    for  MOD in $(lsmod | awk '$3 ~ 0 ' | sort -h);
     do echo "$MOD";
     sudo modprobe -r "$MOD"; echo "Reload $MOD?";
     read -r ANS;
     test "$ANS" = "y" && sudo modprobe "$MOD";
     done

Based on this method, the needed modules are:

[CODE]

    hid_multitouch
    i2c_designware_platform
    i2c_hid
    intel_lpss_pci

##### [Step 2: Find the modules that are using those modules]

To find the other used modules by the Touchpad we can use the below commands:

`user `[`$`]`lsmod | grep -E "hid_multitouch|i2c_designware_platform|i2c_hid|intel_lpss_pci"`

     intel_lpss_pci
     intel_lpss
     i2c_hid
     i2c_designware_platform
     i2c_designware_core
     hid_multitouch
     hid

\