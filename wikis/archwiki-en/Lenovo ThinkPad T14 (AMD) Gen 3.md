# Lenovo ThinkPad T14 (AMD) Gen 3

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| TrackPoint || ||
|-
| Touchpad ||  ||
|-
| Fingerprint reader || ||
|-
| Smartcard reader ||  ||
|-
| Mobile broadband ||  ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo Thinkpad T14 (AMD) Gen 3 21CFCT01WW laptop. Everything works, except the keyboard does not feel the same as the first generation and the battery life is not great.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Firmware
## fwupd
fwupd supports the UEFI BIOS, the webcam, the touchpad, the CPU/GPU, TPM and the NVMe controller.

## Sleep to idle (s2idle, S0ix)
According to Lenovo staff the CPU generation in this device only supports s2idle and not S3 sleep.

See Power management/Suspend and hibernate#Changing suspend method.

## Suspend/Hibernate
There is a known bug in the  kernel module that could block the resume process, freeze the graphics interface and cause loss of wireless card interface. A manual fix is to disable the  module before hibernate and re-enable it after resume.

This also seems to fix an intermittent issue causing the laptop to immediately wake up after suspend.

See Dell XPS 13 (9310)#Wi-Fi for a systemd service to automate this procedure.

This can be automated via sleep hooks - if the module is unloaded before hibernating or suspending it unloads immediately with no delay, and the resume kernel bug does not happen:

You need to enable  and .

## Disable wakeup from sleep on touchpad activity
Use the following to disable wake-up events caused by the touchpad. Note that this only applies to the touchpad itself and the integrated buttons for left/right click at its bottom, not the 3 buttons at its top or any other input.

{{hc|/etc/udev/rules.d/99-disable-touchpad-wakeup.rules|2=
KERNEL=="i2c-ELAN0678:00", SUBSYSTEM=="i2c", ATTR{power/wakeup}="disabled"
}}

## Quectel EM05-G 4G LTE Modem
The integrated modem is supported by default, but you need a custom FCC unlock script for ModemManager. This script should be located at  and has to be linked from

{{hc|/usr/share/ModemManager/fcc-unlock.available.d/2c7c|
 #!/bin/bash

# SPDX-License-Identifier: CC0-1.0
# 2022 Leah Oswald
#
# Queltec EM05-G FCC unlock mechanism
#

# require program name and at least 2 arguments
[ $# -lt 2 ] && exit 1

# first argument is DBus path, not needed here
shift

# second and next arguments are control port names
for PORT in "$@"; do
  # match port name
  echo "$PORT" | grep -q cdc-wdm && {
    CDC_WDM_PORT=$PORT
    break
  }
done

# fail if no cdc-wdm port exposed
[ -n "$CDC_WDM_PORT" ] || exit 2

# run mbimcli operation
mbimcli --device-open-proxy --device="/dev/$CDC_WDM_PORT" --quectel-set-radio-state=on
exit $?

}}

Then link them:

 # ln -s /usr/share/ModemManager/fcc-unlock.available.d/2c7c /etc/ModemManager/fcc-unlock.d/2c7c:030a

After that everything should work normal.

There is an issue at the ModemManager Gitlab to add this script to make this obsolete in the future.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles the Fn lock
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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles the PrivacyGuard feature
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Controls the keyboard backlight
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function

## Mute Mic LED always on
There is an issue where the LED light on the mic button is always on.

Using  from :

* Select the Realtek ALCXXX sound card (with ). The card label may be HD-Audio Generic (it should have 5 channels).
* Disable Auto-Mute Mode.
* Use  to test the mute/unmute functionality for your microphone. The LED should now properly toggle on and off as expected. If it doesn’t work, try rebooting.
* Keep the state of Auto-Mute Mode disabled, do not re-enable it.

## Audio
Install .
