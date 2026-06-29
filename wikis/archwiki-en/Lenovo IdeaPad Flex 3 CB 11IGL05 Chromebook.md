# Lenovo IdeaPad Flex 3 CB 11IGL05 Chromebook

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| MicroSD card reader ||||
|-
| Keyboard ||||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad ||  ||
|-
| Touchscreen ||||
|-
| Webcam ||  ||
|}

## Firmware
This device is not supported by fwupd. To change or update the firmware, follow the instructions in Chrome OS devices/Custom firmware.

This Chromebook does not support Legacy Boot Mode. Even if you try to invoke it by pressing  on the Developer Mode boot screen, it will show two options without a choice. Therefore it is necessary to flash a custom firmware before the installation.

# Disable Firmware Write Protection by booting without battery (use original power supply) or using SuzyQable.
# Enable Developer Mode.
# Use MrChromebox's Firmware Utility Script.

## Accessibility
The appearance of the SeaBIOS is pretty simple and not very colorful, so it might work well with OCR software because it is completely in text mode.

## Installation
Use  to suppress audit messages that appear every second:

 # auditctl -e0

Follow the Installation guide.

## Audio
Install the following packages:

*  — sound driver
*  — contains ALSA configuration profile for  device
*  — PulseAudio
*  — required to connect ALSA with PulseAudio
*  — required to correctly respond to headset plug in
*  — optional, required for Bluetooth headsets
*  — optional, can be used to control the sound from a terminal (e.g. )

Create the following script to switch sinks with acpid when plugging in a 3.5mm jack headset:

Make the script executable.

Register the script as a listener:

Enable , the sound should work after reboot.

## Function keys
## Default assignment
This Chromebook model  has many of the Chromebook special keys and they are mostly assigned correctly.
The  key is assigned to  by default.

{| class="wikitable"
|-
! Key
! Visible?
! Marked?
! Effect
|-
|  ||  ||  || Previous/Back
|-
|  ||  ||  || Next
|-
|  ||  ||  || Refresh/Reload
|-
|  ||  1 ||  || No default action -> adjust to
|-
|  ||  ||  || "Scale" action --> adjust to
|-
|  ||  ||  || Decrease Brightness
|-
|  ||  ||  || Increase Brightness
|-
|  ||  ||  || Mute toggle
|-
|  ||  ||  || Decrease Volume
|-
|  ||  ||  || Increase Volume
|-
|  ||  ||  || Sleep
|-
|  ||  ||  || Assigned "Left Meta" =
|}

# This key is visible to kernel/udev but not within X11.

The following table gives an overview of the underlying default keycodes. This information is needed to change the configuration.

See Keyboard input for more information

{| class="wikitable"
|-
! Chromebook special key
! Scancode
! Keycode
! Keysym
|-
|  || ea || 158 || KEY_BACK
|-
|  || e9 || 159 || KEY_FORWARD
|-
|  || e7 || 173 || KEY_REFRESH
|-
|  || 91 || 372 || KEY_ZOOM
|-
|  || 92 || 120 || KEY_SCALE
|-
|  || 94 || 224 || KEY_BRIGHTNESSDOWN
|-
|  || 95 || 225 || KEY_BRIGHTNESSUP
|-
|  || ea0 || 113 || KEY_MUTE
|-
|  || ae || 114 || KEY_VOLUMEDOWN
|-
|  || b0 || 115 || KEY_VOLUMEUP
|-
|  || 5d || 142 || KEY_SLEEP
|}

## Adjust non-responsive keys for Xorg
There is only one key that is completely unresponsive in Xorg, because the keycode is above 255:  has a keycode of 371.
By changing this key to an unused key with a lower keycode we can resolve this issue.

Create the following file as root:

and update the hardware database index.

After reboot you will see this change in the table above:

{| class="wikitable"
|-
! Chromebook special key
! Scancode
! Keycode
! Keysym
|-
|  || 91 || 152 || KEY_SCREENLOCK
|}

## Create additional key bindings
To also have function keys, Chromebook shortcuts (page-up, home, delete, ...) by using a combination of the Search key (that is assigned meta or  by default) as an overlay, there are many options:

xbindkeys, sxhkd, desktop environments keyboard shortcuts,...

A good option is , because this way all the bindings work in console, Xorg and Wayland without any delay.

After installing, create the following file:

Enable/start .

This makes it possible to go to a console tty by holding  (which is translated to )
And also to come back to graphical mode by holding (which is translated to )
