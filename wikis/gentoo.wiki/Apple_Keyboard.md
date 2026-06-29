**Resources**

[[]][Wikipedia](https://en.wikipedia.org/wiki/Apple_Keyboard "wikipedia:Apple Keyboard")

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Behavior]](#Behavior)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [Kernel]

** Important**\
When using Linux 4.0 or lower, the Apple HID driver is enabled by default as a built-in module, and is only visible when the kernel is configured in expert mode.

[KERNEL] **Enabling the Apple HID driver for Linux 4.1 or higher**

        Device Drivers --->
              HID support --->
                      Special HID drivers --->
                        <*> Apple Books

## [Configuration]

### [Behavior]

The behavior of the function keys ([F1]-[F12]) defaults to their special functions (screen brightness, volume control, etc.). To change the behavior of the function keys to their traditional functions ([F5] - page refresh, [F11] - full screen, etc.), set the [fn] key mode to function keys first:

`root `[`#`]`echo 2 > /sys/module/hid_apple/parameters/fnmode`

When using a non-English layout, the [\<] and [\>] keys may be mapped to the [\^] and [°] keys. To correct this, disable the hard-coded ISO layout of the keyboard:

`root `[`#`]`echo 0 > /sys/module/hid_apple/parameters/iso_layout`

If the Apple HID driver is built into the kernel, create the following [local.d](https://wiki.gentoo.org/wiki/Local.d "Local.d") script to have the module parameters set at boot:

[FILE] **`/etc/local.d/hid_apple.start`**

    #!/bin/sh

    # set fn key mode to function keys first
    echo 2 > /sys/module/hid_apple/parameters/fnmode

    # disable iso layout
    echo 0 > /sys/module/hid_apple/parameters/iso_layout

Set the local.d script as executable:

`root `[`#`]`chmod +x /etc/local.d/hid_apple.start`

If the Apple HID driver is built as a module, add the following to [/etc/modprobe.d/keyboard.conf] to have the module parameters set at boot:

[FILE] **`/etc/modprobe.d/keyboard.conf`**

    options hid_apple fnmode=2 iso_layout=0

## [External resources]

-   [Ubuntu - Apple Keyboard](https://help.ubuntu.com/community/AppleKeyboard)
-   [Arch Linux - Apple Keyboard](https://wiki.archlinux.org/index.php/Apple_Keyboard)