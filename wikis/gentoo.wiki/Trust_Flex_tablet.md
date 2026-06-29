This is a guide on how to configure and install the Trust Flex graphics tablet using the Wizardpen driver provided by a portage overlay. This guide may also be modified to work with other non-Wacom graphics tablets compatible with the Wizardpen driver however this article is only about the Trust Flex graphics tablet.

Some of these steps may not be necessary however they are all of the steps which the original author of this article took in order to get the tablet working.

## Contents

-   [[1] [Kernel options]](#Kernel_options)
-   [[2] [Modifying xorg.conf]](#Modifying_xorg.conf)
-   [[3] [Adding udev rules]](#Adding_udev_rules)
-   [[4] [Compiling the Wizardpen driver]](#Compiling_the_Wizardpen_driver)

## [Kernel options]

In order for the Trust Flex graphics tablet to work, the following options specific to the Trust Flex tablet need to be selected during the kernel configuration:

[KERNEL] **Example output after searching for WALTOP**

    Symbol: HID_WALTOP [=y]
    Type  : tristate
    Prompt: Waltop
      Location:
        -> Device Drivers
          -> HID support
            -> HID bus support (HID [=y])
    (1)       -> Special HID drivers
      Defined at drivers/hid/Kconfig:319
      Depends on: INPUT [=y] && HID [=y]

After this the kernel must be recompiled and booted into.

** Note**\
It is sufficient to enable HID_WALTOP as a module, build it, and plug the tablet in to make it work. The Wizardpen driver is not required.

## [Modifying xorg.conf]

Next it is important to add a section in [/etc/X11/xorg.conf] that defines the tablet as an input device. This can be accomplished by editing or creating (if it does not exist yet) [/etc/X11/xorg.conf] to contain the following:

[FILE] **`/etc/X11/xorg.conf`**

    Section "InputDevice"
       Identifier  "tablet"
       Driver  "wizardpen"
       Option  "Device"  "/dev/tablet"
    EndSection

## [Adding udev rules]

As udev is the device manager and handles all user space actions when adding or removing devices, udev rules for the tablet must be created so that it functions properly. The following file must be created and edited as shown:

[FILE] **`/etc/udev/rules.d/67-xorg-wizardpen.rules`**

    ENV=="172f", ENV=="0038", ENV="wizardpen"
    ENV=="wizardpen", KERNEL=="event*" ENV="wizardpen"
    ENV=="wizardpen", KERNEL=="event*", ENV="1"

\

## [Compiling the Wizardpen driver]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=Trust_Flex_tablet&action=edit).

** Warning**\
This repository has been removed from the official listing and is in need of updating.

The Wizardpen driver necessary for the functioning of this and other Wizardpen compatible tablets will be installed from the *wavilen* portage overlay. After installing and configuring [eselect repository], the overlay can be installed using the following commands:

`root `[`#`]`eselect repository enable wavilen`

Then sync the repos:

`root `[`#`]`emerge --sync`

and finally compile the wizardpen driver itself:

`root `[`#`]`emerge -av wizardpen`

Finally reboot and plug in your Trust Flex graphics tablet. The tablet should now be functioning in software that supports it such as GIMP and mypaint.