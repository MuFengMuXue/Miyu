This page contains [[changes](https://wiki.gentoo.org/index.php?title=Synaptics&oldid=1242116&diff=1267346)] which are not marked for translation.

Other languages:

-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/Synaptics/hu "Synaptics (100% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Synaptics/ja "synaptics (100% translated)")

**synaptics** is the open source input driver for Synaptics and [ALPS](https://wiki.gentoo.org/wiki/Alps_PS/2 "Alps PS/2") touchpads.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Driver]](#Driver)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Fixed configuration]](#Fixed_configuration)
    -   [[2.2] [Configuration at runtime]](#Configuration_at_runtime)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Touchpad is not recognized]](#Touchpad_is_not_recognized)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

## [Installation]

### [Kernel]

Activate the following kernel options:

[KERNEL]

    Device Drivers  --->
       Input device support  --->
          <*>   Event interface
          [*]   Mice  --->
             <*>   PS/2 mouse

** Note**\
Additional drivers may be necessary under the Mice menu to support the touchpad. e.g. \"Synaptics PS/2 mouse protocol extension\". The touchpad may also be USB, not PS/2. When in doubt, select multiple drivers and check what the kernel uses later with [lspci -k].

[KERNEL]

    Device Drivers  --->
       HID bus support  --->
          <M>   I2C HID support  --->
              <M>   HID over I2C transport layer ACPI driver

### [Driver]

[FILE] **`/etc/portage/make.conf`Set `INPUT_DEVICES`**

    INPUT_DEVICES="synaptics libinput"

After setting the `INPUT_DEVICES` variable remember to update the system using the following command so the changes take effect:

`root `[`#`]`emerge --ask --changed-use --deep @world`

\

## [Configuration]

The driver has a lot options for tuning. See the [[[synaptics(5)]](https://man.archlinux.org/man/synaptics.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for more information.

### [Fixed configuration]

Referring to [xorg.conf](https://wiki.gentoo.org/wiki/Xorg.conf "Xorg.conf") there should have a [/etc/X11/xorg.conf.d] directory on the system. If there is none create one:

`root `[`#`]`mkdir /etc/X11/xorg.conf.d`

Configure file [/etc/X11/xorg.conf.d/50-synaptics.conf] as in the example below:

[FILE] **`/etc/X11/xorg.conf.d/50-synaptics.conf`**

    Section "InputClass"
            Identifier "touchpad catchall"
            Driver "synaptics"
            MatchIsTouchpad "on"
            Option "VertEdgeScroll" "on"
            Option      "CircularScrolling"         "on"
            Option      "VertScrollDelta"          "-111"
            Option      "HorizScrollDelta"         "-111"
            Option      "TapButton1"                    "1"
    EndSection

### [Configuration at runtime]

Enable the above option to be able to configure the driver also at runtime. Changes at runtime will be lost with the next start of the X server. Add changes to the above config file to persist desired settings.

Configure the driver with the program [synclient]. Some examples:

List all parameters:

`user `[`$`]`synclient -l`

Cut the right side of the touch area to expand the vertical scroll area:

`user `[`$`]`synclient RightEdge=5000`

Finding the right edge parameter:

`user `[`$`]`synclient -m 50`

Disable the mouse click function:

`user `[`$`]`synclient MaxTapTime=0`

Finally, dump the handpicked configuration to the [99-synaptics] file pasting output of the following command inside the `InputClass` section:

`user `[`$`]`synclient -l | sed -e '1d' -e 's/^ \+/Option\t"/g' -e 's/ \+= /"\t"/g' -e 's/$/"/g'`

Alternatively there is the [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") systemsettings module [[[kde-misc/synaptiks]](https://packages.gentoo.org/packages/kde-misc/synaptiks)[]]:

`root `[`#`]`emerge --ask kde-misc/synaptiks`

## [Troubleshooting]

### [Touchpad is not recognized]

If the touchpad does not show in either [lsusb] nor [lspci], that might be due to the PS/2 controller and how it is handled by the kernel^[\[1\]](#cite_note-1)^. One indication is if [dmesg] returns sometings along the lines of:

`user `[`$`]`dmesg | grep i8042`

    i8042: PNP: PS/2 appears to have AUX port disabled, if this is incorrect please boot with i8042.nopnp

That AUX port is where the touchpad is connected^[\[2\]](#cite_note-2)^. Try adding the following to the kernel command line, e.g. in [/etc/default/grub]:

[FILE] **`/etc/default/grub`**

    GRUB_CMDLINE_LINUX_DEFAULT="... i8042.noloop i8042.nomux i8042.nopnp i8042.reset ..."

Now, update your grub.cfg:

`root `[`#`]`grub-mkconfig -o /boot/grub/grub.cfg`

If, after rebooting with these parameters, a generic `Logitech PS/2 mouse` input device is detected, the appropriate PS/2 extension driver may be necessary in the Kernel config:

[KERNEL]

    Device Drivers  --->
       Input device support  --->
          <*>   Event interface
          [*]   Mice  --->
             <*>   PS/2 mouse
                [ /*]   Elantech PS/2 protocol extension
                [ /*]   Sentelic Finger Sensing Pad PS/2 protocol extension
                [ /*]   eGalax TouchKit PS/2 protocol extension

After rebooting, the touchpad should be recognized correctly.

## [See also]

-   [libinput](https://wiki.gentoo.org/wiki/Libinput "Libinput") --- an input device driver for [Wayland compositors](https://wiki.gentoo.org/wiki/Wayland_Desktop_Landscape#Compositors "Wayland Desktop Landscape") and [X.org](https://wiki.gentoo.org/wiki/Xorg "Xorg") window system.
-   [Xorg/Using the numeric keyboard keys as mouse](https://wiki.gentoo.org/wiki/Xorg/Using_the_numeric_keyboard_keys_as_mouse "Xorg/Using the numeric keyboard keys as mouse") --- XOrg comes with built-in mouse emulation using the keyboards numeric keypad.

## [References]

1.  [[[↑](#cite_ref-1)] [[Trackpad on Acer laptop not working](https://www.linuxquestions.org/questions/linux-hardware-18/trackpad-on-acer-laptop-not-working-4175621311/)]]
2.  [[[↑](#cite_ref-2)] [[Explanation on PS/2 Controllers](https://unix.stackexchange.com/a/28810)]]