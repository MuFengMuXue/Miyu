# GPD Pocket 4

{| class="wikitable archwiki-table-laptop"
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
| Touchscreen ||  ||
|-
| Keyboard/Pointer ||  ||
|-
| Webcam ||  ||
|-
| Fingerprint ||  ||
|-
| Accelerometer || ||
|}

The GPD Pocket 4 is a compact 8.8" convertible laptop with a 1600x2560 portrait display, touchscreen, and accelerometer for tablet mode.

## Screen orientation
The display panel is physically portrait (1600x2560) and requires rotation for normal laptop use: see Tablet PC#Screen rotation.

## Touchscreen
The touchscreen (NVTK0603) requires calibration to match the display rotation.

## Hyprland
Add a device section to your Hyprland configuration:

{{bc|1=
device {
    name = nvtk0603:00-0603:f001
    transform = 3
}
}}

## Wayland (udev)
For other Wayland compositors, create:

{{hc|/etc/udev/rules.d/99-touchscreen.conf|

ACTION=="add|change", KERNEL=="eventATTRS{name}=="NVTK0603:00 0603:F001", ENV{LIBINPUT_CALIBRATION_MATRIX}="0 1 0 -1 0 1"
}}

Then reload udev rules.

## Xorg
Install  and create :

## Automatic rotation
The GPD Pocket 4 has an accelerometer (MXC6655) that can be used for automatic screen rotation in tablet mode, see Tablet PC#Automatic rotation.

## Touchscreen gestures
For touch gestures (swipe to switch workspaces, etc.), install  from the AUR.

Create a gesture script (e.g., ):

{{bc|1=#!/bin/bash
# GPD Pocket 4 touchscreen gestures using lisgd
# Accepts orientation parameter: 0, 1, 2, 3 (matches Hyprland transform)

if [ -z "$CALLED_FROM_AUTOROTATE" ; then
    pkill -f "lisgd" 2>/dev/null
    sleep 0.3
fi

DEVICE="/dev/input/event10"  # Adjust if needed
TRANSFORM="${1:-3}"  # Default to laptop mode (transform 3)

# Commands - customize as needed
WS_PREV="hyprctl dispatch workspace e-1"
WS_NEXT="hyprctl dispatch workspace e+1"
OVERVIEW="hyprctl dispatch overview:toggle"

# Map Hyprland transform to lisgd orientation (-o flag)
case "$TRANSFORM" in
    3) LISGD_ORIENT=0 ;;  # Laptop mode
    0) LISGD_ORIENT=1 ;;  # Portrait left
    1) LISGD_ORIENT=2 ;;  # Laptop upside down
    2) LISGD_ORIENT=3 ;;  # Portrait right
esac

lisgd -d "$DEVICE" -o "$LISGD_ORIENT" \
    -g "3,LR,*,0.08,$WS_PREV" \
    -g "3,RL,*,0.08,$WS_NEXT" \
    -g "3,UD,*,0.08,$OVERVIEW" \
    -g "3,DU,*,0.08,$OVERVIEW" \
    -t 150 -r 25 &}}

Add to Hyprland startup:

To integrate with auto-rotation, modify the auto-rotation script to restart the gesture script with the new orientation when rotation changes. See the auto-rotation section for details.

## Backlight
The backlight is controlled via .

Install  for easy control:

## Function keys
{| class="wikitable"
|-
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  || Yes || Yes ||
|-
|  || Yes || Yes ||
|-
|  || Yes || Yes ||
|-
|  || Yes || Yes ||
|-
|  || Yes || Yes ||
|-
|  || No || Yes || Keyboard backlight toggle3
|-
| Fn+ || No || Yes || Fan speed cycle3
|}

# Visible to , , and similar tools.
# The key has a physical symbol describing its function.
# Controlled by keyboard/EC firmware, not configurable from the OS.

## Touchpad
The GPD Pocket 4's pointing device (HAILUCK USB KEYBOARD Mouse) is detected by libinput as a basic pointer rather than a touchpad, which means standard touchpad gesture tools like  will not work.

For swipe gestures, use the touchscreen gesture solution above instead.
