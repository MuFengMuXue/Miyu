# ASUS Zenbook Prime UX31A

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||  *
|-
| SD Card Reader ||  ||
|-
| colspan="3" | *Usage can impair Wi-Fi quality
|}

This page contains instructions, tips, pointers, and links for installing and configuring Arch Linux on the ASUS Zenbook UX31A and UX21A Ultrabooks. Most of it should also hold for UX32VD.

See previous generation ASUS Zenbook UX31E page that has mostly orthogonal information to those here (may be only partially applicable to UX31A)

## Installation
To install Arch Linux on UX31A, you can follow the official Installation guide. Since the UX31A uses UEFI and GPT, make sure to also read the UEFI, GPT and Arch boot process#Boot loader pages.

## Boot from USB medium
Press  to get into the boot menu. If the USB bootable device is not listed, enter the configuration menu and directly press  to save. Press  again on reboot: this time the USB bootable device should appear in the menu.

Make sure to boot the USB in UEFI mode, to easily install the boot loader later.

## Function keys
{| class="wikitable"
|-
! Keys
! Visible?1
! Marked?2
! Effect
|-
|
| 3
|
|
|-
|
|
|
|  &
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
| Turn off LCD
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|
|-
|
|
|
|  - Ambient light sensors
|-
|
|
|
|  - Switch display profile
|-
|
|
|
|
|-
|
|
|
|  - Switch power profiles
|}
# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# systemd-logind handles this by default.

## Screen backlight
The brightness is managed via hardware, so it should work across all DE's.
In case it is not working directly, you need to set the kernel parameter  (the space is required).

## Keyboard backlight
Keyboard backlight should work automatically with any recent kernel. Desktop environments that use UPower, like GNOME or KDE, work out the box and do not need any tool or script to register the keys and change the keyboard brightness.

## Manually setting the brightness
See Keyboard backlight.

## Using asus-kbd-backlight
 is a convenient way to manage the backlight brightness, if one does not want to use UPower. To allow users to change the brightness, write:

 # asus-kbd-backlight allowusers

Now you can easily change keyboard backlight in terminal:

 $ asus-kbd-backlight up
 $ asus-kbd-backlight down
 $ asus-kbd-backlight max
 $ asus-kbd-backlight off
 $ asus-kbd-backlight night
 $ asus-kbd-backlight 2
 $ asus-kbd-backlight show

You can then bind the  and  keys to the above functions.

## Solid state drive
See Solid state drive and Power management#SATA Active Link Power Management

## Graphics
See Intel graphics. For hardware accelerated video read Hardware video acceleration.

## Touchpad
Instructions to activate the right button.
(As an alternative you cant try This).

Multifinger taps work out of the box.

## Multitouch gestures
To enable multitouch gestures like those under Windows, one can install . Using  will require disabling some input-handling that is done by the synaptics input driver. Edit your

 Section "InputClass"
         Identifier "touchpad catchall"
         Driver "synaptics"
         MatchIsTouchpad "on"
         MatchDevicePath "/dev/input/event*"
         Option "TapButton1" "1"
         Option "TapButton2" "0"
         Option "TapButton3" "0"
         Option "ClickFinger2" "0"
         Option "ClickFinger3" "0"
         Option "HorizTwoFingerScroll" "0"
         Option "VertTwoFingerScroll" "0"
         Option "ClickPad" "true"
         Option "EmulateMidButtonTime" "0"
         Option "SoftButtonAreas" "50% 0 82% 0 0 0 0 0"
 EndSection

An alternative to X.org configuration files is to use the  command within the  script. This method will limit changes to your desktop environment.

  synclient TapButton2=0 TapButton3=0 ClickFinger2=0 ClickFinger3=0 HorizTwoFingerScroll=0 VertTwoFingerScroll=0

 will need to be autostarted for multitouch gestures to be activated. This can be done with  in your , or using the autostart/startup applications functionality of your desktop environment.  can then be configured as necessary.

## Multitouch gestures in GNOME
GNOME 3's gnome-shell does its own mouse-handling, which can interfere with synaptics and touchegg settings unless the appropriate plugin is disabled.

 $ gsettings set org.gnome.settings-daemon.plugins.mouse active false

Note that disabling this plugin will cause the current settings within the Mouse & Touchpad section of System Settings to be ignored.

## Disable Touchpad While Typing
One of the criticisms this laptop gets (see reviews at Amazon) is that the placement of the touchpad results in frequent touchpad brushing during typing. You should use whatever touchpad disabling method you prefer. See Touchpad Synaptics#Disable touchpad while typing.

## HDMI plugged at boot
There seems to be a problem whereby having an HDMI device plugged in at boot results in the screens being switched and also the laptop screen not coming on. To make this more bearable you can automate switching HDMI on with the following udev rule and script:

Add the following script as root:

then make it executable.

Add the following udev rule:

Suspending, unplugging the HDMI cable, and resuming is a way to enable the Zenbook's screen without rebooting if it was booted with the cable plugged in.

## Powersave management
To configure some power saving options and tools, see Power saving.

## Other Devices and Drivers
## MEI
If you know what you are doing and want to use the i7 MEI, you need the Intel Local Manageability Service. You can find it as .

## Additional resources
* https://help.ubuntu.com/community/AsusZenbookPrime
* https://ubuntuforums.org/showthread.php?t=2005999
* Wikipedia:Zenbook#UX32.2C UX42 and UX52
