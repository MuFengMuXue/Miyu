**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Banana_Pi "wikipedia:Banana Pi")

The Banana Pi embedded system is very similar to the [Raspberry Pi](https://wiki.gentoo.org/wiki/Raspberry_Pi "Raspberry Pi").

## Contents

-   [[1] [Lemakers Gentoo Image]](#Lemakers_Gentoo_Image)
-   [[2] [Manual Gentoo installation on SDD]](#Manual_Gentoo_installation_on_SDD)
    -   [[2.1] [Build the Kernel for a Banana Pi]](#Build_the_Kernel_for_a_Banana_Pi)
    -   [[2.2] [Installation of U-Boot]](#Installation_of_U-Boot)
    -   [[2.3] [Install WiFi]](#Install_WiFi)
-   [[3] [See also]](#See_also)
-   [[4] [External resources]](#External_resources)

## [Lemakers Gentoo Image]

Download the compressed image file from [http://www.lemaker.org/mirror](http://www.lemaker.org/mirror) and extract it.

`user `[`$`]` tar xfzv Gentoo_For_BananaPro_v1412.tgz`

Connect a compatible SD card, or a SATA 2.5\" harddisc with your computer. Lets assume the device is named [/dev/sdx]. Write the image to the media with dd

`user `[`$`]` sudo dd if=Gentoo_For_BananaPro_v1412.img of=/dev/sdx bs=1M`

## [Manual Gentoo installation on SDD]

Boot a Gentoo system (for example the Lemaker image) from SD card. Follow to the installation procedure in the [amd64 manual](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64") but download and use an ARMv7a stage3 file from [https://www.gentoo.org/downloads/](https://www.gentoo.org/downloads/) instead of the amd64 version.

### [Build the Kernel for a Banana Pi]

[http://wiki.lemaker.org/BananaPro/Pi:Building_u-boot,\_script.bin_and_linux-kernel](http://wiki.lemaker.org/BananaPro/Pi:Building_u-boot,_script.bin_and_linux-kernel)

### [Installation of U-Boot]

See the instructions on this [Gentoo wiki page](https://wiki.gentoo.org/wiki/Banana_Pi_the_Gentoo_Way#U-Boot "Banana Pi the Gentoo Way").

### [Install WiFi]

On the Banana Pi Pro load the following module

`user `[`$`]` sudo modprobe ap6210 `

## [See also]

-   [Distcc/Cross-Compiling](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling") --- shows the reader how to set up distcc for cross-compiling across different processor architectures.
-   [Banana Pi the Gentoo Way](https://wiki.gentoo.org/wiki/Banana_Pi_the_Gentoo_Way "Banana Pi the Gentoo Way") --- provides details on how to install Gentoo with a user compiled kernel and a Gentoo stage 3 on the Banana Pi

## [External resources]

-   [Banana Pi -- Official website; LeMaker](http://www.bananapi.org)
-   [Banana Pi -- Official website; Sinovoip](http://www.banana-pi.org)