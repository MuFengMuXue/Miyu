# Panasonic CF-SZ5

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || PS/2 ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Infrared Camera || ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader || ||
|-
| TPM || ||
|-
| Light sensor || ||
|}

## Accessibility
The BIOS setup and battery calibration utility have a standard text based UI, only the keyboard is required to interact with both programs. The menus should be easy to OCR. The  or  key can be used to enter BIOS setup, and  can be used to enter the built-in battery calibration utility.

* To restore factory default settings, press  in BIOS setup.
* To save changes and reboot, press  in BIOS setup.

## Firmware
fwupd detects the device, but fails to provide any firmware updates. Firmware updates for BIOS, ME and EC can be downloaded from Panasonic's official website.

## Battery
Battery can be swapped while the system is connected to external power and in sleep state without causing the system to lose power. ECO mode state (80% Charging restriction to preserve battery life) will persist across reboots and in Linux if toggled on in the Panasonic PC Settings Utility under Windows.

## Touchpad
See Panasonic CF-SV9#Touchpad.

## TPM
CF-SZ5 has a  TPM 1.2 onboard, which can be unofficially upgraded to support TPM 2.0 for better integrations with systemd. BIOS version V3xxL25 and later have built in TPM 2.0 support and is able to interact with the TPM upon upgrade. A firmware upgrade tool from Supermicro can be used to perform the upgrade. A detailed blog post provides instructions to perform an Infineon TPM upgrade.
