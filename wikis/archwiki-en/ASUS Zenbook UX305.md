# ASUS Zenbook UX305

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Audio ||  ||
|-
| Touchpad || PS/2 ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| SD card reader ||  ||
|-
|}

This page contains instructions, tips, pointers, and links for installing and configuring Arch Linux on the ASUS Zenbook UX305.

Hardware reference from UX305-FB041H. Model available since 12 feb 2015.

## Hardware lists
See for specific hardware information.

See [https://gist.github.com/precurse/6dc1990cd000551c8f11 for UX305CA (Skylake) hardware information. Physically labelled with UX305C on laptop, but UX305CA shows in dmesg.  See and contribute to discussion tab of this page for fixes.

## Touchpad
Works after installing .

## Palm detection
If default Palm Detection does not work well, one can manually disable part of the trackpad by setting AreaEdge properties.

You can do this on the fly or add these parameters in the config file:

 $ /usr/bin/synclient AreaLeftEdge=500 AreaRightEdge=2500

## Middle click
Three finger tap should work with libinput.

If you are still using the  driver, you can enable three finger tapping by running:

 $ /usr/bin/synclient TapButton1=1 TapButton2=3 TapButton3=2

## Graphics
UEFI results with memory changes for the Intel graphics card:

* With 32-256MB memory assignment in bios: Works.
* With 512MB memory assignment: X11 breaks. 1/3th upper-part of screen semi works (swapped and mis-alligned), rest is noise/snow.

Bug: https://bugzilla.redhat.com/show_bug.cgi?id=1151757

## QHD+ Pentile Display
Some models include a 3200x1800 (faux-3200x1800 RG/BW Pentile) QHD+ screen, which displays very tiny characters, and can make them difficult to read due to its incomplete subpixel matrix.

Desktop Environments that have native Hi-DPI support such as GNOME 3 should automatically scale text and applications to the appropriate factor of 200% (x2.0).

If you experience scaling issues (specifically with text) in Firefox and Thunderbird, add the below property in the about:config area

  layout.css.devPixelsPerPx=2.

## Function Keys
The  (blank display) does not work.

The ambient light sensor button () returns:

  PNP0C14:00 000000ff 00000000
