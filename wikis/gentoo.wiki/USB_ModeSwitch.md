**Resources**

[[]][Home](http://www.draisberghof.de/usb_modeswitch/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Virtual_CD-ROM_switching_utility "wikipedia:Virtual CD-ROM switching utility")

**USB_ModeSwitch** is a tool for controlling \"flip flop\" (multiple devices) USB gear like UMTS sticks.

## Contents

-   [[1] [Hardware detection]](#Hardware_detection)
-   [[2] [Installation]](#Installation)
-   [[3] [Configuration]](#Configuration)
-   [[4] [Result checking]](#Result_checking)
-   [[5] [Troubleshooting]](#Troubleshooting)

## [Hardware detection]

Run **dmesg** in monitor mode:

`user `[`$`]`dmesg -w`

Plug in the device and check if it gets detected as a new CD-ROM drive. If so, then you have a \"flip flop\" device and you need USB_ModeSwitch.

## [Installation]

Install [[[sys-apps/usb_modeswitch]](https://packages.gentoo.org/packages/sys-apps/usb_modeswitch)[]]:

`root `[`#`]`emerge --ask usb_modeswitch`

## [Configuration]

** Note**\
USB_ModeSwitch is designed to work out-of-the-box. Plug in the device and let [udev](https://wiki.gentoo.org/wiki/Udev "Udev") do the work.

If USB_ModeSwitch doesn\'t work out-of-the-box, search the internet for a matching config. Use [lsusb](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") to detect the device\'s vendor and product IDs. If you find a config, create a new configuration file using the device\'s vendor and product IDs, e.g.:

[FILE] **`/etc/usb_modeswitch.d/12d1:1446`**

    TargetVendor=0x12d1
    TargetProductList="1001,1406,140b,140c,1412,141b,1432,1433,1436,14ac,1506,1511"

    MessageContent="55534243123456780000000000000011062000000100000000000000000000"

If you don\'t use [udev](https://wiki.gentoo.org/wiki/Udev "Udev"), you have to run **usb_modeswitch** manually:

`root `[`#`]`usb_modeswitch -c /etc/usb_modeswitch.conf`

## [Result checking]

After switching [lsusb](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection") should detect a different product ID.

If the right drivers are loaded, the proper device files appear. E.g. in the case of the [option](https://wiki.gentoo.org/wiki/USB_mobile_broadband_modem "USB mobile broadband modem") driver the [/dev/ttyUSB\*] files.

## [Troubleshooting]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=usb_modeswitch&order=bug_id%20DESC)[]]
-   See upstream [troubleshooting guide](http://www.draisberghof.de/usb_modeswitch/#trouble)