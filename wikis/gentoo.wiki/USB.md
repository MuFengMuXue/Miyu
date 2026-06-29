**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/USB "wikipedia:USB")

[[]][Guide](https://wiki.gentoo.org/wiki/USB/Guide "USB/Guide")

This article describes the setup of **USB** (Universal Serial Bus) controllers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Hardware detection]](#Hardware_detection)
    -   [[1.2] [Kernel]](#Kernel)
    -   [[1.3] [Portage]](#Portage)
    -   [[1.4] [Emerge]](#Emerge)
-   [[2] [External resources]](#External_resources)

## [Installation]

### [Hardware detection]

To choose the right driver, first detect the used USB controllers. The [[lspci](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection")] utility works nicely for this task:

`root `[`#`]`lspci | grep --color -i usb`

### [Kernel]

See the kernel section of the [USB guide](https://wiki.gentoo.org/wiki/USB/Guide#Config_options_for_the_kernel "USB/Guide") and the USB host controllers section of the [Kernel configuration guide](https://wiki.gentoo.org/wiki/Kernel/Gentoo_Kernel_Configuration_Guide#USB_host_controllers "Kernel/Gentoo Kernel Configuration Guide").

### [Portage]

Portage knows the [`usb` USE flag](https://packages.gentoo.org/useflags/usb). Some packages include or exclude support for USB based on this flag. As with all [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), can be set as a value of the `USE` variable in [[/etc/portage/make.conf](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE "/etc/portage/make.conf")] or in [[/etc/portage/package.use](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use")].

### [Emerge]

Install the [[[sys-apps/usbutils]](https://packages.gentoo.org/packages/sys-apps/usbutils)[]] package, if it is not already installed by adding the [`usb` USE flag](https://packages.gentoo.org/useflags/usb) and re-running emerge with `--changed-use`:

`root `[`#`]`emerge --ask sys-apps/usbutils`

## [External resources]

-   [Universal Serial Bus Device Class Definition for Audio Devices](https://www.usb.org/sites/default/files/Audio2_with_Errata_and_ECN_through_Apr_2_2025.pdf) \[PDF, 2025-04-02\]