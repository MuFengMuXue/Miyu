**Resources**

[[]][Home](https://www.logitech.com/en-us/products/mice/logi-bolt-usb-receiver.956-000007.html)

The Logitech Bolt is an encrypted wireless receiver dongle for Bolt enabled devices.

To quote Logitech:

> It's Logitech's next-gen wireless technology --- delivering a high-performance, secure wireless connection when compatible mice and keyboards are connected via Logi Bolt USB receiver.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Install]](#Install)
    -   [[1.3] [Udev Rules]](#Udev_Rules)
    -   [[1.4] [Hardware list]](#Hardware_list)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [Disconnects]](#Disconnects)

## [Installation]

### [Kernel]

[KERNEL] **Enable Logitech hid++**

    Device Drivers --->
      [*] HID Devices  --->
         Special HID drivers --->
         <*>   Logitech receivers full support
         <*>   Logitech HID++ devices support

### [Install]

[Solaar](https://pwr-solaar.github.io/Solaar/) is a replacement for the OEM Logitech software. It allows pairing of bolt devices to their bolt receiver and configuring bolt and unify receiver enabled devices.

`root `[`#`]`emerge --ask app-misc/solaar`

### [Udev Rules]

[FILE] **`/etc/udev/rules.d/42-logitech-unify-permissions.rules`**

    # This rule was added by Solaar.
    #
    # Allows non-root users to have raw access to Logitech devices.
    # Allowing users to write to the device is potentially dangerous
    # because they could perform firmware updates.

    ACTION != "add", GOTO="solaar_end"
    SUBSYSTEM != "hidraw", GOTO="solaar_end"

    # USB-connected Logitech receivers and devices
    ATTRS=="046d", GOTO="solaar_apply"

    # Lenovo nano receiver
    ATTRS=="17ef", ATTRS=="6042", GOTO="solaar_apply"

    # Bluetooth-connected Logitech devices
    KERNELS == "0005:046D:*", GOTO="solaar_apply"

    GOTO="solaar_end"

    LABEL="solaar_apply"

    # Allow any seated user to access the receiver.
    # uaccess: modern ACL-enabled udev
    # udev-acl: for Ubuntu 12.10 and older
    TAG+="uaccess", TAG+="udev-acl"

    # Grant members of the "plugdev" group access to receiver (useful for SSH users)
    #MODE="0660", GROUP="plugdev"

    LABEL="solaar_end"
    # vim: ft=udevrules

`root `[`#`]`udevadm control --reload-rules`

### [Hardware list]

  -------------- --------- --------------- -------- --------------------------------------------------------------------------------- ------------------
  Device         Version   Solaar Compat   Works?   Reported by                                                                       Notes
  MX Keys Mini   V1        Yes             Yes      [nathanlkoch](https://wiki.gentoo.org/wiki/User:Nathanlkoch "User:Nathanlkoch")   Everything works
  -------------- --------- --------------- -------- --------------------------------------------------------------------------------- ------------------

Logitech bolt receivers can pair up to six keyboards and mice each. Logitech bolt receivers are fully HID complaint and work in the bios and are paired on a hardware level. Great for people who multi boot and do not require to be repaired.

## [Troubleshooting]

### [Disconnects]

If you are experiencing disconnects on either the Bolt or Unify receiver after enabling hid++ in the kernel, it could be because you are using an unpowered USB hub. Adding the kernel extension appear to either draw more power or cause conflicts when operating though a hub. Try connecting directly to your computer.