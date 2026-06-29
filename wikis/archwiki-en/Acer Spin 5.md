# Acer Spin 5

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad || PS/2 ||
|-
| TouchScreen ||  ||
|-
| Camera ||  ||
|-
| Fingerprint scanner ||  ||
|}

General info about the Acer Spin 5 SP513-52N laptop.

## Installation
To disable Secure Boot, set the supervisor password in the UEFI settings. Then you should be able to disable Secure Boot and boot Arch.

Even with Secure Boot disabled, if the Windows Boot Manager is not the *first* EFI entry, it then becomes impossible to access the UEFI settings and the only known method that works for regaining such access is temporarily placing the Windows Boot Manager as the first option again. The cause for this behavior is unknown and it is therefore strongly recommended that you select your preferred settings prior to installing Arch, especially enabling the  Boot Menu in order to allow booting from external devices.

If the  Boot Menu is not enabled and you need to boot from an external device, your only option will be opening the chassis and temporarily removing the SSD to prevent it from being used as the boot device. Also note that the Spin 5 comes with a battery protection measure which causes battery power to be supplied only when the case is completely closed with all screws, as explained in an Acer community answer. Any loose screw may prevent the computer from turning on except when the power cord is plugged in, or else cause unexpected shutdowns while on battery power, as reported in Acer forums.

Another quirk is that apparently the UEFI "function keys" setting will either enable special keys such as sleep and Wi-Fi as default (thus making the  prefix necessary for using  through ), OR it will enable the opposite behavior but completely disabling the  key as a side effect. This is not specific to Linux and there is no known solution to this problem.

## Touchscreen and active stylus
The touchscreen should work perfectly out of the box, including pinching gestures - except for applications which do not implement such support (for example, ).

When in tablet mode, the keyboard and touchpad are disabled, but the screen does not rotate automatically. For manual or automatic screen rotation, see Tablet PC#Rotation and Tablet PC#Automatic rotation.

The Acer Spin 5 has MPP (Microsoft Pen Protocol) support. To improve the functionality of an active stylus in Arch Linux, follow the instructions on Microsoft Surface Pro 3#Tuning the Pen. This post might also have useful information on the subject.

## Touchpad
The touchpad works perfectly with libinput. Some commonly reviewed settings are Tapping (tap-to-click) and Natural Scrolling. The default middle button emulation may also present undesired behavior due to the fact that the button pressing area is divided in three equal parts, which causes frequent accidental middle clicks: for example, when trying to select a web browser tab, if the default region for the middle button is pressed down, the tab will be closed instead of selected.

To disable middle button emulation and enable Tapping and Natural Scrolling, create/edit the following configuration file:

For more details refer to libinput#Tapping button re-mapping.

To use touch gestures such as pinching in a window manager or desktop environment that does not implement it, fusuma is recommended.

## Temperature management
The laptop has been observed to overheat while the power cord is connected. This can be fixed by simply installing thermald and starting/enabling the respective service. For more information, see CPU frequency scaling.
