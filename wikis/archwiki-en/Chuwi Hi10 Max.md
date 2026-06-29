# Chuwi Hi10 Max

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Touchscreen || ||
|-
| Keyboard ||  ||
|-
| GPU ||  ||
|-
| Webcam || ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|}

## Accessibility
The appearance of the BIOS Setup Utility is simple and uses contrasting colours, so it may work well with OCR software. A legend of keyboard navigation shortcuts is also clearly listed at the bottom right of the screen.

{| class="wikitable"
! Key !! Effect
|-
|  || May be needed to be pressed together with the  keys.
|-
|  || Start the BIOS Setup Utility
|-
|  || Bring up the Boot Menu window
|}

## Installation
To enter the firmware set-up, press  (or maybe only ) repeatedly at boot.
For the boot menu, use .

Disable Secure Boot in the security section before installing, then save and restart to the boot menu and select your installation device.

## Pen and tablet mode
The Hi10 Max stylus conflicts with the  touchscreen driver.
By default, when the driver is loaded, tablet mode detection works, but the stylus does not.

To enable stylus support, blacklist the module:

However, this disables tablet-mode detection. To restore it, install the  package, which provides keyboard-based mode switching.

It hard-codes the id of the keyboard. If you happen to have a different id, open a bug report in https://github.com/aligator/tablet-mode

## Screen rotation
In tablet mode, the accelerometer reports an incorrect orientation.

To fix it, create the file:

Then update the hardware database index.

## libwacom configuration
When the screen is rotated, the stylus may not apply the rotation, to fix this, create a custom device description:

After that, reboot.

It may be needed to calibrate the pen again in your desktop environment settings.

For gnome this may be the correct calibration:

 $ dconf write /org/gnome/desktop/peripherals/tablets/222a:0001/area "-0.060763880610466003, -1.4901161193847656e-08, -7.4505805969238281e-08"

## Secure Boot
Follow Secure Boot set-up using .

If you have installed the custom module from the  tablet mode workaround, you have to enable automatic DKMS module signing with sbctl keys.

Rebuild the module (e.g. by reinstalling it) to sign automatically.

## USB-C charging
Note that the tablet does not charge with all chargers as it seems to require 12V and does not work with for example 20V chargers.

Also note that the delivered charger may be dangerous with other devices https://www.reddit.com/r/Chuwi/comments/1fjb2xx/fire_hazard_charger_hi10max_eu/

## Function keys
{| class="wikitable"
! Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  || (un)lock  3
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
|  ||  ||  || Del
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# The Fn key is locked by default. There is no option in the BIOS to disable this.
