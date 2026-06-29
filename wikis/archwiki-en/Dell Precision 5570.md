# Dell Precision 5570

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||||
|-
| Webcam ||  ||
|-
| Bluetooth || ||
|-
| SD Card reader || ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|-
| TPM || ||
|}

## Installation
You can enter the bios menu with , disable Secure Boot or you will not be able to boot the Arch Linux image.

You can enter the bios one-time boot menu with .

With both disk inserted, boot to any of them individually with the firmware storage mode set to RAID (default setting) remains possible. One may consider setting the mode to AHCI.

See the following forum post for more information on storage modes.

## Accessibility
The appearance of the UEFI is pretty simple and not very colorful, so it might work well with OCR software. However, it requires the user to use a mouse.

## Firmware
fwupd is supported on this device and it is advised to upgrade the firmware version before configure it as new options will likely be added.
If using two disk with an EFI system partition on both, fwupd will need your help to figure out your current EFI system partition.

## Secure Boot
The UEFI accepts .auth files.

## Firmware data path
The UEFI stores logs, telemetry and recovery images in .
Recovery images are stored in . It appears that there will only be two images at the same time,  and .
Those files will be created when the UEFI was updated.
The firmware also expose some telemetry (metrics) that you could use in . It seems to have file for previous boots, formatted in json.

## Logs
 contains XML files which contain diagnostics data (SupportAssist).
It appears that there will only be two logs at the same time,  and .
Those files will be created when an error happened and are really useful to troubleshoot any issue you may have with the laptop or when plugged with external devices.

## LFE Speakers
By default only the front speakers are enable. To enable the LFE speakers, install .

With hdajackretask:

* Choose Realtek ALC289 in codec menu,
* Check Show unconnected pins,
* Enable Pin ID  and select Internal Speaker (LFE),
* Enable Pin ID  ans select Internal Speaker,
* Click Apply Now,
* Click Install boot override.

## Fingerprint reader
Fingerprint authentication works flawlessly. The sensor is located under the power button on the top right corner of the keyboard. Just follow the steps in fprint. This amounts to installing  and configuring PAM appropriately. Then registering (or in fprint lingo: enrolling) your fingerprint with .

## Battery charge limit
In order to extend the lifetime of the laptop battery, charge limits can be set. There is a Dell utility to do this called Dell Command Configure, but it only supports old versions of Ubuntu, and does not work with Arch due to dependencies on old system libraries.

But there is a better solution. Install . Then, to limit the charge level to 80%:

 # smbios-battery-ctl --set-custom-charge-interval 75 80
 # smbios-battery-ctl --set-charging-mode=custom

To revert to the default settings:

 # smbios-battery-ctl --set-charging-mode=adaptive

Source: https://askubuntu.com/a/1351481
