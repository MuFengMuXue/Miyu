**evdev** is

-   The open source input driver ([[[x11-drivers/xf86-input-evdev]](https://packages.gentoo.org/packages/x11-drivers/xf86-input-evdev)[]]) for many input devices like keyboards, mice, joysticks and more.
-   The short name of the Linux kernel\'s event interface (CONFIG_INPUT_EVDEV), needed for [libinput](https://wiki.gentoo.org/wiki/Libinput#Kernel "Libinput").
-   The [`input_devices_evdev`](https://packages.gentoo.org/useflags/input_devices_evdev) USE flag.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Driver]](#Driver)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Keyboard layout]](#Keyboard_layout)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel]

You need [USB](https://wiki.gentoo.org/wiki/USB "USB") support, if you have an USB input device. Also you need to activate the following kernel options:

[KERNEL] **PS/2 keyboard/mouse support**

    Device Drivers  --->
        Input device support  --->
            <*>   Event interface
            [*]   Mice  --->
                  <*>   PS/2 mouse
            -*-   Keyboards  --->
                  <*>   AT keyboard

[KERNEL] **USB input device support**

    Device Drivers  --->
        HID support  --->
            <*> HID bus support
            <*> Generic HID driver
                USB HID support  --->
                    <*> USB HID transport layer

Some USB mice (e.g. Logitech G5 and Razer Naga 2014) additionally need the following option:

[KERNEL] **Improved transaction support**

    Device Drivers  --->
        [*] USB support  --->
            [*]   Improved Transaction Translator scheduling

### [Driver]

[FILE] **`/etc/portage/make.conf`Set `INPUT_DEVICES`**

    INPUT_DEVICES="evdev"

After setting the `INPUT_DEVICES` variable remember to update the system using the following command so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

\

## [Configuration]

### [Keyboard layout]

To set the default layout copy the file [10-evdev.conf] to [/etc/X11/xorg.conf.d] and edit the keyboard section, e.g. for a German layout:

`root `[`#`]`cp /usr/share/X11/xorg.conf.d/10-evdev.conf /etc/X11/xorg.conf.d/`

[FILE] **`/etc/X11/xorg.conf.d/10-evdev.conf`**

    Section "InputClass"
            Identifier "evdev keyboard catchall"
            ...
            Driver "evdev"
            Option "xkb_layout" "de"
    EndSection

For more info please read the [Configuring the keyboard](https://wiki.gentoo.org/wiki/Xorg/Guide#Configuring_the_keyboard "Xorg/Guide").

## [See also]

-   [Libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") --- an input device driver for [Wayland compositors](https://wiki.gentoo.org/wiki/Wayland_Desktop_Landscape#Compositors "Wayland Desktop Landscape") and [X.org](https://wiki.gentoo.org/wiki/Xorg "Xorg") window system.