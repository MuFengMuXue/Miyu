# ASUS Zenbook UX390

## Volume increments do not work
Because of the "surround sound" audio hardware on the UX390, you have to tweak a Pulse configuration file to get volume incrementing to work. Otherwise, the volume will either be full or muted, despite appearing to increment.

Edit the analog output path config and add the  and  parts below.

Then, restart PulseAudio and changing the volume should work.

## Headphone jack audio is always muted
See Advanced Linux Sound Architecture#Unmuting the channels.

## Keyboard and Touchpad unusable in X and Wayland
Since kernel version v5.8, the  driver gained the ability to detect "tablet mode" on convertible devices. However, at least on UX390UAK the  driver believes that the device is always in tablet mode, although it is not a convertible (see https://bugzilla.kernel.org/show_bug.cgi?id=209011 for a kernel bug report). Libinput automatically disables touchpad and keyboard when kernel reports tablet mode, so they only work in tty but not in X or wayland.

To workaround this, add a quirk file for libinput:
