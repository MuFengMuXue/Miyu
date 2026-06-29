[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Wacom&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

This article provides instructions for enabling touchscreen support for [Wacom](https://www.wacom.com/) devices such as laptops, tablets, and ultrabooks, and the like.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Userspace driver]](#Userspace_driver)
        -   [[1.2.1] [Xinput2 multitouch]](#Xinput2_multitouch)
-   [[2] [Configuration]](#Configuration)

## [Installation]

### [Kernel]

The following option is likely necessary for proper tablet functionality, even if the device is not an Intuos/Graphire tablet as it says in the description.

[KERNEL] **Kernel config**

    Device drivers --->
       HID support --->
          HID bus support --->
             Special HID drivers --->
                <*> Wacom Intuos/Graphire tablet support (USB)

Recent touchscreen models may need other options like I2C_HID_ACPI (for a Lenovo IdeaPad Flex 5 16ALC7 82RA):

[KERNEL] **Kernel config**

    Device drivers --->
       I2C support --->
          <M> I2C support
          I2C Hardware Bus support --->
          <M> Intel PIIX4 and compatible (ATI/AMD/Serverworks/Broadcom/SMSC) (I2C_PIIX4)
       HID support --->
          I2C HID support --->
             <M> HID over I2C transport layer ACPI driver (I2C_HID_ACPI)

Some tablet models may also require these options:

[KERNEL] **Additional config**

    Device drivers --->
       Input device support --->
          [*] Tablets --->
             <*> Wacom protocol 4 serial tablet support--->
          [*] Touchscreens --->
             <*> Wacom W8001 penabled serial touchscreen
             <*> Wacom Tablet support (I2C)

### [Userspace driver]

After kernel is configured, update the `INPUT_DEVICES` Portage variable using the wacom driver:

[FILE] **`/etc/portage/make.conf`Set `INPUT_DEVICES`**

    INPUT_DEVICES="wacom libinput"

After setting the `INPUT_DEVICES` variable remember to update the system using the following command so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

\
You should also create Xorg config file so that Xorg knows which driver should be used for the tablet. Example:

[FILE] **`/etc/X11/xorg.conf.d/42-libinput.conf`**

    Section "InputClass"
            Identifier "Tablet"
            Driver "wacom"
            MatchIsTablet "on"
    EndSection

#### [Xinput2 multitouch]

The default setting of the `wacom` xinput driver has \"gesture emulation\".

When *disabled*, **true multitouch events** will be emitted instead and it can be used with [Firefox multitouch](https://wiki.gentoo.org/wiki/Firefox#Enabling_multitouch "Firefox").

[FILE] **[`/etc/X11/xorg.conf.d/50-wacom.conf`](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf")**

    Section "InputClass"
        Identifier "Wacom class"
        MatchProduct "Wacom|WACOM|Hanwang|PTK-540WL|ISDv4|ISD-V4|ISDV4"
        MatchDevicePath "/dev/input/event*"

        Driver "wacom"
        Option "Gesture" "off"
    EndSection

## [Configuration]

To list detected devices in the terminal, try `xsetwacom`. This command also allows tweaking things such as stylus buttons and draw space, but keep in mind that more work is necessary to make the changes persist after exiting an X session (see [this discussion](https://askubuntu.com/questions/9242/how-do-i-change-xsetwacom-and-make-the-settings-stay-on-startup)).

`user `[`$`]`xsetwacom --list devices`

    Wacom One by Wacom S Pen stylus         id: 15  type: STYLUS
    Wacom One by Wacom S Pen eraser         id: 16  type: ERASER