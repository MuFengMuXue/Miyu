**Resources**

[[]][Home](https://www.mysn.de/xmg-advanced-gaming-laptops/xmg-a507)

This laptop is based on Clevo N850HJ(?), available with different configurations.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Firmware]](#Firmware)
    -   [[2.2] [Kernel]](#Kernel)
        -   [[2.2.1] [Keyboard backlight]](#Keyboard_backlight)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [NVIDIA GPU]](#NVIDIA_GPU)
    -   [[3.1] [nouveau]](#nouveau)
    -   [[3.2] [nvidia-drivers (proprietary)]](#nvidia-drivers_.28proprietary.29)
    -   [[3.3] [Freezes when starting Xorg, or when switching to tty from Xorg]](#Freezes_when_starting_Xorg.2C_or_when_switching_to_tty_from_Xorg)

## [Hardware]

  ------------------- ------------------------------------------------------- --------------------------------- ------------------------ ------------------ ---------------- ----------------------------------- --
  Device              Make/model                                              Status                            Vendor ID / Product ID   Kernel driver(s)   Kernel version   Notes
  CPU                 Intel(R) Core(TM) i7-7700HQ                             Works                             N/A                      N/A                4.13.13
  Video card          NVIDIA Corporation GP107M \[GeForce GTX 1050 Mobile\]   See [#NVIDIA GPU](#NVIDIA_GPU)                             nouveau            4.17.3
  WiFi                Intel(R) Dual Band Wireless AC 3168                     Works                                                      iwlwifi            4.13.13          Firmware required
  Integrated webcam   Chicony USB 2.0 Camera: Chicony                         Works                                                      uvcvideo           4.13.16          Only photos tested, not video yet
  ------------------- ------------------------------------------------------- --------------------------------- ------------------------ ------------------ ---------------- ----------------------------------- --

## [Installation]

Installed in non-UEFI mode. Recommend Live-Distributions that do not boot into X11, since they will freeze most certainly. Use Gentoo\'s DVD.

### [Firmware]

Required for WiFi.

### [Kernel]

Latest (stable) kernel is recommended.

#### [Keyboard backlight]

[clevo-xsm-wmi moddule](https://bitbucket.org/tuxedocomputers/clevo-xsm-wmi/overview) required to get control over keyboard backlight. After building and loading this module, you can turn the backlight off or change colours etc.

This module may not work with kernel version 4.14 at this time, see the [bug report](https://bitbucket.org/tuxedocomputers/clevo-xsm-wmi/issues/32/module-does-not-work-with-kernel-version).

### [Emerge]

`root `[`#`]`emerge --ask sys-kernel/linux-firmware`

## [NVIDIA GPU]

### [nouveau]

It might be required to add `acpi_rev_override=1` to the kernel boot cmdline.

Additionally:

[FILE] **`/etc/modprobe.d/nouveau.conf`**

    options nouveau runpm=0

Given however that this disables runtime power management, you probably want to blacklist the module instead and use bbswitch to disable it. If nouveau is not loaded and GPU is off Xorg may also freeze. Hence, disable it only after you have successfully opened Xorg.

In the times you need it, do the following:

`root `[`#`]`echo ON > /proc/acpi/bbswitch `

`root `[`#`]`rmmod bbswitch `

`root `[`#`]`modprobe nouveau runpm=0 `

An already running Xorg server might crash, thus it\'s better to stop Xorg, then run these commands before starting Xorg again.

### [][nvidia-drivers (proprietary)]

It might be required to add `acpi_rev_override=1` to the kernel boot cmdline. No additional laptop-specified instructions were used, see [NVIDIA](https://wiki.gentoo.org/wiki/NVIDIA "NVIDIA").

This driver appears to be working at this point, external displays weren\'t tried though.

### [][Freezes when starting Xorg, or when switching to tty from Xorg]

Please see [#NVIDIA GPU](#NVIDIA_GPU)