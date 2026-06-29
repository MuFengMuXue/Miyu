# Lenovo Yoga Duet 7 13IML05

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Touchpad ||  ||
|-
| Webcam front ||  ||
|-
| Webcam rear ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchscreen || ||
|-
| MicroSD card reader ||  ||
|-
| Sensors ||  ||
|}

The Lenovo Yoga Duet 7 13IML05 is a 2-in-1 convertible laptop introduced in late 2019. It features a 13" 16:10 2160x1350 WQHD multi-touch touchscreen, Intel 10th-gen Comet Lake Core processors and integrated Intel UHD 620 graphics. Its detachable keyboard/touchpad unit features Bluetooth connectivity and may be used detached from the main tablet unit.

To ensure you have this version, install the package  and run:

Note: Lenovo Yoga Duet 7i is a different laptop, with much worse support.

## Firmware
The BIOS is accessed by repeatedly pressing the  key during system boot when the display powers up and before the Lenovo logo is displayed on the screen.

The boot menu to choose the boot device is accessed by repeatedly pressing the  key during system boot when the display powers up and before the Lenovo logo is displayed on the screen.

## Accessibility
The BIOS user interface is graphical. An option to switch to a text-based GUI is not provided. However, the options may be selected with the arrow keys and the values changed with the  and  keys.

## Suspend / Standby
See Power management/Suspend and hibernate#Changing suspend method.

## Audio
The speakers, the headphones connector and the microphones work once Sound Open Firmware is installed.

## Enabling automatic screen rotation under GNOME and Wayland
Install the  package. The screen will now automatically rotate and keyboard/touchpad input will be disabled when the keyboard/touchpad unit is folded back in tablet mode. If the screen does not rotate automatically, try running

 $ gsettings set org.gnome.settings-daemon.peripherals.touchscreen orientation-lock false

Alternatively, use  to toggle lock state.

## Function keys
{| class="wikitable"
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Enables Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || , toggles soft-block Wi-Fi and Bluetooth
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  ||
|-
|   ||  ||  || Toggle Keyboard Backlight
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default
