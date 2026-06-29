This article details the process of enabling support for USB to serial (RS-232, RS-422, RS-485 etc) adapters in the Linux kernel.

Most modern, user facing hardware devices do not come with serial ports accessible from the exterior casing of the device. This becomes an issue when attempting to configure or troubleshoot certain devices that implement a console port with serial communication for data input/output. Most modern hardware devices *do* include at least one USB port that is accessible from the device casing.

The Linux kernel has support for USB to serial adapters. These devices can be also known as USB serial converters. Support can be enabled in the kernel, udev will configure the device, and an engineer can obtain success communicating with serial input/output via the console port.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Additional software]](#Additional_software)
-   [[2] [See also]](#See_also)

## [Installation]

### [Kernel]

Enable support for USB to serial by selecting the following symbols in the [kernel\'s configuration](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration"): `CONFIG_USB_SERIAL`, `CONFIG_USB_SERIAL_CONSOLE`, `CONFIG_USB_SERIAL_GENERIC`, and `CONFIG_USB_SERIAL_SIMPLE`:

[KERNEL] **USB to serial support**

    Device Drivers  --->
       [*] USB support  --->
          <*>   USB Serial Converter support  --->
             --- USB Serial Converter support
             [*]   USB Serial Console device support
             [*]   USB Generic Serial Driver
             <*>   USB Serial Simple Driver

From this point, specific drivers for each hardware device can be enabled as necessary. To reduce kernel size it is wise to build support for additional adapters as modules.

After the above options have been enabled do not forget to recompile the kernel, update the bootloader, and re-execute the new kernel. Instructions for how to do these steps can be found in related articles.

### [Additional software]

Useful software for accessing the serial interface:

-   [Picocom](https://wiki.gentoo.org/wiki/Picocom "Picocom")
-   [Minicom](https://wiki.gentoo.org/wiki/Minicom "Minicom")
-   [Screen](https://wiki.gentoo.org/wiki/Screen "Screen")

\

## [See also]

-   [Kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") --- a central part of the Gentoo [operating system (OS)](https://en.wikipedia.org/wiki/operating_system "wikipedia:operating system")
-   [Kernel/Configuration](https://wiki.gentoo.org/wiki/Kernel/Configuration "Kernel/Configuration")