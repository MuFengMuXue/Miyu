# Lenovo ThinkPad X13 Gen 3

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|}

The Lenovo ThinkPad X13 Gen 3 laptop was released in 2022. It is available with an Intel or AMD Ryzen CPU. Some models include a fingerprint reader, a Smartcard reader, and a WWAN card.

To figure out which model you are using, run  as root: the  field starts with 21BN or 21BQ on Intel models and with 21CM or 21CN on AMD models.

## Accessibility
The BIOS offers two modes of operation, GUI and Simple Text.

The GUI can be navigated to some degree via the keyboard. Use the arrow keys to move the selection and  to activate.

Switching to Simple Text can be accomplished by:

* Pressing  to select the sidebar, then  to select Config, then  to activate it
* Holding  for two seconds to select the drop-down menu at the very bottom
* Pressing  to change it from Graphical to Simple Text
* Pressing , then  to save and exit

## Firmware
Firmware can be updated using fwupd. The UEFI BIOS can also be updated manually: download the ISO from Lenovo's support page for Intel or AMD models and use  to flash the BIOS from Linux. To check the BIOS version, run
 $ cat /sys/class/dmi/id/bios_version

## Sound
This laptop requires Sound Open Firmware in order for the sound card to work.

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
|  ||  ||  || 3
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Enables/disables keyboard backlight
|-
|  ||  ||  || 3
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
|  ||  ||  || Set power profile to "low-power" (low)4
|-
|  ||  ||  || Set power profile to "balanced" (medium)4
|-
|  ||  ||  || Set power profile to "performance" (high)4
|}

# The key is visible via  and similar tools
# The physical key has a symbol on it, which describes its function
# systemd-logind handles this by default
# To see which profile is active run
