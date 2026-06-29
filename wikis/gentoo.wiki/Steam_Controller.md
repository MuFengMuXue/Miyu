**Resources**

[[]][Home](https://store.steampowered.com/app/353370/Steam_Controller/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Steam_Controller "wikipedia:Steam Controller")

The [Steam](https://wiki.gentoo.org/wiki/Steam "Steam") Controller is a game controller developed by [Valve](https://en.wikipedia.org/wiki/Valve_Corporation "wikipedia:Valve Corporation"). It features two trackpads (in place of thumbsticks) with [haptic](https://en.wikipedia.org/wiki/Haptic_technology "wikipedia:Haptic technology") feedback and sixteen buttons. The Steam controller is designed not only for games supporting traditional controllers, but also for games that support keyboard and mouse.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Permissions]](#Permissions)
        -   [[1.2.1] [systemd]](#systemd)
        -   [[1.2.2] [Manual udev]](#Manual_udev)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Pairing]](#Pairing)
-   [[3] [See also]](#See_also)

## [Installation]

### [Kernel]

The Steam Controller is fully supported by Linux via the Steam client, however it does require [USB](https://wiki.gentoo.org/wiki/USB "USB") and user level driver (`CONFIG_INPUT_UINPUT`) support.

[KERNEL] **Enabling user level driver support (`CONFIG_INPUT`, `CONFIG_INPUT_MISC`, `CONFIG_INPUT_UINPUT`)**

    Device Drivers --->
       Input device support --->
          [*] Generic input layer (needed for keyboard, mouse,...)
          [*]   Miscellaneous devices --->
             <*>   User level driver support

To have kernel support for the Steam controller (which makes it possible to use the Steam controller when not running the Steam client), enable the driver support in the kernel (`CONFIG_HID_STEAM`). Steam Controller support was added in kernel version 4.3 and above.

[KERNEL] **Enabling Steam Controller driver support (`CONFIG_HID_STEAM`)**

    Device Drivers --->
       HID support  --->
          Special HID drivers  --->
             <*> Steam Controller support

### [Permissions]

#### [systemd]

If Steam was installed manually and systemd/elogind ***are*** being used, create the following udev rules file:

[FILE] **`/etc/udev/rules.d/99-steam-controller-perms.rules`**

    # Valve USB devices
    SUBSYSTEM=="usb", ATTRS=="28de", MODE="0666"

    # Steam Controller udev write access
    KERNEL=="uinput", SUBSYSTEM=="misc", TAG+="uaccess", TAG+="udev-acl"

    # Valve HID devices over USB hidraw
    KERNEL=="hidraw*", ATTRS=="28de", MODE="0666"

    # Valve HID devices over bluetooth hidraw
    KERNEL=="hidraw*", KERNELS=="*28DE:*", MODE="0666"

The above udev rules file will grant access to the Steam Controller by automatically setting an [ACL](https://wiki.gentoo.org/wiki/Filesystem/Access_Control_List_Guide "Filesystem/Access Control List Guide") entry for the logged-in user.

If Steam was installed from anyc\'s Steam [external repository](https://wiki.gentoo.org/wiki/Steam#External_repositories "Steam"), a udev rules file that supports systemd/elogind should already be installed with the [\>=steam-launcher-1.0.0.51-r1] ebuild.

** Note**\
If systemd/elogind are being used, set the `USE` variable to `acl` to have the ACL entry set for the logged-in user.

Next, reload the udev rules files and trigger a device event for the new rule:

`root `[`#`]`udevadm control --reload `

`root `[`#`]`udevadm trigger `

Once the udev rules files are reloaded, the user using the Steam Controller will need to log out/in for the correct permissions to be set.

#### [Manual udev]

If Steam was installed [manually](https://wiki.gentoo.org/wiki/Steam#Manual "Steam") or from an [external repository](https://wiki.gentoo.org/wiki/Steam#External_repositories "Steam"), and [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd")/[elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") ***are not*** being used, create the following [udev](https://wiki.gentoo.org/wiki/Udev "Udev") rules file:

[FILE] **`/etc/udev/rules.d/99-steam-controller-perms.rules`**

    # Valve USB devices
    SUBSYSTEM=="usb", ATTRS=="28de", MODE="0666"

    # Steam Controller udev write access
    KERNEL=="uinput", SUBSYSTEM=="misc", MODE="0660", GROUP="input", OPTIONS+="static_node=uinput"

    # Valve HID devices over USB hidraw
    KERNEL=="hidraw*", ATTRS=="28de", MODE="0666"

    # Valve HID devices over bluetooth hidraw
    KERNEL=="hidraw*", KERNELS=="*28DE:*", MODE="0666"

The above udev rules file will grant access to the Steam Controller for users in the [input] group:

`root `[`#`]`gpasswd -a <user> input`

## [Usage]

### [Pairing]

[B]+[Steam] puts the controller into Bluetooth Low Energy mode, whereas [A]+[Steam] puts the controller into wireless mode (requires the WiFi dongle).^[\[1\]](#cite_note-1)^

Press the [Steam]+[Y] key to enter pairing mode. Once paired successfully, the Steam button will glow white.

See the [Bluetooth](https://wiki.gentoo.org/wiki/Bluetooth "Bluetooth") article for more information on pairing.

## [See also]

-   [Sony DualShock](https://wiki.gentoo.org/wiki/Sony_DualShock "Sony DualShock") --- describes the use of Sony DualShock 3 / [Sixaxis](https://en.wikipedia.org/wiki/Sixaxis "wikipedia:Sixaxis"), DualShock 4, and [DualSense](https://en.wikipedia.org/wiki/DualShock#DualSense "wikipedia:DualShock") [PlayStation](https://en.wikipedia.org/wiki/PlayStation "wikipedia:PlayStation") controllers via USB and Bluetooth.

1.  [[[↑](#cite_ref-1)] [[https://store.steampowered.com/news/app/353370/view/3931035846865617357](https://store.steampowered.com/news/app/353370/view/3931035846865617357)]]