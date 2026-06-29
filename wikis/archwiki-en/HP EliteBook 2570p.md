# HP EliteBook 2570p

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Pointstick || ||
|-
| Keyboard || ||
|-
| Video || ||
|-
| Webcam || ||
|-
| Ethernet || ||
|-
| Bluetooth ||  ||
|-
| Card reader || ||
|-
| Audio || ||
|-
| Wireless || ||
|-
| Mobile broadband ||  ||
|-
| GPS || ||
|-
| Fingerprint reader || ||
|}

## Bluetooth
The integrated Bluetooth device seems a bit buggy as a few random disconnects were observed in combination with some BT4.0 devices. One possible way to circumvent this is to replace the integrated Wi-Fi card with Wi-Fi+BT combo one such as Intel® Centrino® Advanced-N 6235 or similar (later 2570p BIOS-es should have WLAN whitelisting removed) and then connecting the Bluetooth interface of the card to the pins used by the docking connector. This is necessary as this laptop has no USB pins connected on the WLAN miniPCIe interface and the user also benefits from the Intel® Centrino® Advanced-N 6235's improved power efficiency over 6205.

## Power management
The following kernel parameters can be enabled to provide additional power management for Intel graphics. However, some of them are experimental on Ivy Bridge hardware and can lead to problems.

 i915.i915_enable_fbc=1
 drm.vblankoffdelay=1

This laptop has ASPM disabled by default and even later versions of BIOS do not provide any options for enabling it. As this feature improves battery life for around 25%, it is a very useful one to have. It is possible to forcibly enable ASPM by using GRUB to write the proper bits to the configuration registers before the kernel is executed. The easiest way is to add the following to the :

{{hc|/etc/grub.d/01_enable-aspm|
#! /bin/sh
set -e

prefix="/usr"
exec_prefix="/usr"
datarootdir="/usr/share"

. "${datarootdir}/grub/grub-mkconfig_lib"

export TEXTDOMAIN=grub
export TEXTDOMAINDIR="${datarootdir}/locale"

# HP EliteBook 2570p ASPM hardware enable
echo "write_byte 0xB9CF506D 0x03" # Enable in ACPI FADT/FACP (BIOS F.40-)
echo "write_byte 0xB9FFC06D 0x03" # Enable in ACPI FADT/FACP (BIOS F.40+)
echo "write_byte 0xB9FFC019 0x10" # Correct checksum
}}

If ASPM has been successfully enabled, there will be no complaints from running  as root. Forcing ASPM in software with  kernel parameter is not needed, however ASPM still needs to be enabled for every PCI device after the kernel is booted. This can be done by a startup script and its contents should be:

Some of the lines are commented out because ASPM does not work properly with some WLAN cards (Intel® Centrino® Advanced-N 6235 for example), causing the kernel to not detect the card after some time (a reboot is needed). The final check if everything is set up correctly can be performed after a reboot by running  (as root).
