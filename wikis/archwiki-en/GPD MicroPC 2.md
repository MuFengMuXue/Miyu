# GPD MicroPC 2

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (N250) ||  ||
|-
| GPU (N300) ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Display || ||
|-
| Touchpad ||  ||
|-
| Touchscreen ||  ||
|-
| Fingerprint sensor || ||
|-
| SD card reader ||  ||
|}

This page provides information for the GPD MicroPC 2.

## Specifications
Only two variants exist so far; N250 and N300. Other specifications should be identical.

## N250/N300
* Display: 7" 1920x1080
* CPU: Intel N250 or N300
* RAM: 16GB LPDDR5 4800 MT/s
* Storage: 512GB NVMe SSD PCIe Gen 3 2280
* Network: 2.5Gbps Ethernet, Intel AX201 802.11ax (2.4/5Ghz), Bluetooth 5.2

## Firmware
 is not supported on the GPD MicroPC 2. GPD provides firmware updates via Windows executables.

See https://www.gpd.hk/gpdmicropc2firmwaredriver for firmware, primarily the BIOS is all we need and includes a method to update via USB; refer to the instructions provided within the zip.

## Recommendations
It is highly recommended to use Wayland for this laptop and not X11, as Wayland will give a better end result and need less tweaking.

For the most like-for-like functionality and experience to Windows on the GPD MicroPC 2, KDE would be the most appropriate desktop environment; especially for overall on-screen keyboard functionality when using the touchscreen.

If the section does not exist it either works, or no issue has been found.

## Display
The MicroPC 2 display is designed for portrait devices and is rotated by 90 degrees counter-clockwise by default. This can be solved as explained in Tablet PC#Screen rotation.

## Automatic screen rotation
See Tablet PC#Automatic rotation.

## X11 screen tearing
Due to the display being designed for portrait devices, the device experiences vertical screen tearing.
This can be solved by ensuring  is installed and following the instructions in Intel graphics#Tearing.

A user mentioned a possible fix with Intel driver set: Enable fractional scaling and set to 150, then disable it - this should prevent the mouse cursor from disappearing at the bottom of the screen.

## Touchscreen
The touchscreen is an Ilitek ILTP7807.

## X11
Touchscreen controls are very limited for X11.

Then logout or restart for changes to apply.

## On-Screen Keyboard
In Windows, when you use the touchscreen and tap an input field an on-screen keyboard will show but not with left click of mouse/touchpad.

KDE: It's recommended to use  and enable it in Settings under "Virtual Keyboards" to get the same behaviour as Windows.

GNOME: With testing there is unfortunately no simple way to get the same functionality as presented in Windows. One solution is you may set the on-screen keyboard to be available only while in portrait mode with the extension mentioned before.

## Touchpad and mouse buttons
## Middle Mouse Scrolling
The script found on GitHub essentially unifies the touchpad and mouse - which are separate and mouse input only uses middle mouse which can be temperamental - and allows for middle mouse scrolling.

## Wayland
## X11
Install .

Then re-log.

## Fingerprint sensor
A Microarray MAFP8800 is used in the MicroPC 2. A fingerprint driver was released on a GPD Discord (gpd_devices) so far and seems to work.

## Additional features
## Charging control
The MicroPC 2 features threshold charging to limit max charging to preserve the batteries health. You can set this in the BIOS under Main > OEM System Configuration.

It also has a bypass feature, allowing it to run from the mains without stressing the battery.

## BIOS reset
There is a pinhole BIOS reset button on the left hand side of the device.

## TPD and Quiet Fan Mode
While the original MicroPC had a physical fan toggle, the MicroPC 2 does not. You may however set the TDP to either 6W or 8W within the BIOS and enable a quiet fan mode - which will only allow the fan to turn on when a certain temperature (~65c) is met.

Additionally, you can adjust the TDP manually which is effective until reboot. This is handy if you have set a quiet fan mode, as it will stay that way when you change to a higher TDP.

The following example sets 15W (+3W for turbo):

 # echo 15000000 > /sys/class/powercap/intel-rapl:0/constraint_0_power_limit_uw
 # echo 18000000 > /sys/class/powercap/intel-rapl:0/constraint_1_power_limit_uw

If you wish to set 5W, 5000000 would be your first value and the second would be 8000000. Keep in mind the zeroes. There is a script with safe limits on the community Discord.
