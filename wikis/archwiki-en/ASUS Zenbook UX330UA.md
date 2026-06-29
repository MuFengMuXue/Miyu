# ASUS Zenbook UX330UA

This article covers configuration specific to this laptop's hardware.

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth || ||
|-
| GPU || ||
|-
| Touchpad || ||
|-
| Wi-Fi || ||
|}

This page contains instructions, tips, pointers, and links for installing and configuring Arch Linux on the Asus ZenBook UX330UA. As of this time Asus' UX330UA page is outdated. Use Amazon's page for reference till Asus updates they site info.

Hardware reference from UX330UA-AH54 (2017 variant). 2017 Model available since 24 feb 2017.

## Hardware lists
See for specific hardware information.

See [https://gist.github.com/Archerious/0efdba649f02262c7c5ed2a8c197b970 for UX330UAK (Kaby Lake) hardware information. Physically labelled with UX330UA-AH54 on laptop, but shows UX330UAK in the output of dmesg.  See and contribute to discussion tab of this page for fixes.

## Compatibility
## Touchpad
Works after installing .

If default Palm Detection does not work well, one can manually disable part of the trackpad by setting AreaEdge properties.

You can do this on the fly or add these parameters in the config file:

  $ synclient AreaLeftEdge=500
  $ synclient AreaRightEdge=2500

## Wi-Fi
Intel Dual Band Wi-Fi. See Wireless network configuration#iwlwifi for details.

## Graphics
See Intel graphics#AccelMethod.

## QHD+ Pentile Display
Some models include a 3200x1800 (faux-3200x1800 RG/BW Pentile) screen, which displays very tiny characters, and can make them difficult to read due to its incomplete subpixel matrix.

For Firefox and Thunderbird, add the below property in the about:config area

  layout.css.devPixelsPerPx=2.

## Function Keys
Kernel 4.11.2-1-ARCH FN+f5 lowers brightness, fn+f6 increases brightness, fn+f11 lowers sound, fn+f12 increases sound. Working fine with Arch and gnome without tweaking anything.
