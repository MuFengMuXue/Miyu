This page contains [[changes](https://wiki.gentoo.org/index.php?title=Bluetooth_input_devices&oldid=1021029&diff=1329014)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Bluetooth_input_devices/hu "Bluetooth beviteli eszközök (100% translated)")
-   [தமிழ்](https://wiki.gentoo.org/wiki/Bluetooth_input_devices/ta "ஊடலை உள்ளீடு சாதனங்கள் (95% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Bluetooth_input_devices/ja "Bluetooh 入力デバイス (100% translated)")

This article describes the setup of [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") input devices, for example a bluetooth mouse, on a Linux system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [BlueZ settings]](#BlueZ_settings)
-   [[2] [Configuration]](#Configuration)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel]

Both [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") and [evdev](https://wiki.gentoo.org/wiki/Evdev "Evdev") support is necessary in the kernel. The following options are also required.

** Important**\
It is important to note that some hardware may require a special driver for the input device. Look under [Special HID devices] as necessary.

[KERNEL]

    Device Drivers  --->
        [*] HID bus support  --->
            Special HID drivers  --->
                <*> ...

    [*] Networking support  --->
        <*>   Bluetooth subsystem support  --->
            [*] Bluetooth Classic (BR/EDR) features
                <*> HIDP Protocol support
            [*] Bluetooth Low Energy (LE) features
                <*>   Bluetooth L2CAP Enhanced Credit Flow Control

### [BlueZ settings]

Change the value of `UserspaceHID` to `true` in [/etc/bluetooth/input.conf] to enable user-space HID support:

[FILE] **`/etc/bluetooth/input.conf`**

    # Enable HID protocol handling in userspace input profile
    # Defaults to false (HIDP handled in HIDP kernel module)
    UserspaceHID=true

User-space HID support also requires the User-space I/O driver for HID input devices (`CONFIG_UHID`) to be enabled:

[KERNEL] **Enabling user-space-hid support**

    Device Drivers --->
        HID support --->
            <*>   User-space I/O driver support for HID subsystem

## [Configuration]

To configure the input devices use the specialized desktop management tools:

-   [[[net-wireless/gnome-bluetooth]](https://packages.gentoo.org/packages/net-wireless/gnome-bluetooth)[]] for [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME")
-   [[[kde-plasma/bluedevil]](https://packages.gentoo.org/packages/kde-plasma/bluedevil)[]] for [KDE](https://wiki.gentoo.org/wiki/KDE "KDE")
-   [[[net-wireless/blueman]](https://packages.gentoo.org/packages/net-wireless/blueman)[]] is a generic GTK client (i.e. for use with Openbox/i3, etc)

Some Bluetooth input devices are initially not in HID mode, but in HCI mode. This is handled by udev in [/lib/udev/rules.d/97-hid2hci.rules]. Additional devices can be added in a custom rule file which needs to be placed in [/etc/udev/rules.d]. Refer to the [udev](https://wiki.gentoo.org/wiki/Udev#Rules "Udev") article for more details.

## [See also]

-   [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") --- describes the configuration and usage of Bluetooth controllers and devices.