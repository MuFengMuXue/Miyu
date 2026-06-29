# HP EliteBook 745 G2

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Pointing Stick || ||
|-
| Keyboard || ||
|-
| Video || ||
|-
| Webcam || 04f2:b477 ||
|-
| Ethernet || ||
|-
| Bluetooth || 0a5c:21fb ||
|-
| SD-Card slot || ||
|-
| Audio || ||
|-
| Wi-Fi || 0a5c:21fb ||
|-
| Fingerprint reader || ||
|-
| Smart Card Reader || ||
|-
|}

## Installation
Even if UEFI, Arch Linux and (e.g.) GRUB are correctly configured and with the correct UEFI NVRAM variables set, the system will not boot from the HDD/SSD. The problem is that HP hard coded the paths for the OS boot manager in their UEFI boot manager to  to boot Microsoft Windows, regardless of how the UEFI NVRAM variables are changed. There are two workarounds:

## Using the "Customized Boot" path option (recommended)
The latest HP firmware allows defining a “Customized Boot” path in the UEFI pre-boot graphical environment.
Select the “Customized Boot” option in the UEFI pre-boot graphical environment under “Boot Options” and set the path to your OS boot loader on the EFI system partition e.g.:

Always verify the correct path to the .efi file. Also, adjust the device boot order (also in the UEFI pre-boot graphical environment) to boot this entry first.

## Change the OS boot loader path to match the hard coded path
Change the UEFI application path of the OS boot loader to that hard coded path.
On your EFI system partition; e.g. with  being the EFI system partition mountpoint:

 # mkdir -p esp/EFI/Microsoft/Boot
 # cp esp/EFI/grub/grubx64.efi esp/EFI/Microsoft/Boot/bootmgfw.efi

or

 # mkdir -p esp/EFI/BOOT
 # cp esp/EFI/grub/grubx64.efi esp/EFI/BOOT/BOOTx64.EFI

## Firmware
This notebook supports HDD FDE (SED). The HDD/SSD can be locked by setting a password in the UEFI pre-boot graphical environment under the option "DriveLock" (this requires setting a password for the UEFI pre-boot graphical environment first). If you replace the HDD/SSD, make sure to get a compatible one to make use of this feature.

## Bluetooth
The default driver seems to work but cannot discover other devices. You need to either:

# Download the  file from broadcom-bt-firmware and place it to the  directory. This is preferred.
# Use  but you will need to figure out conflicts with already installed firmware - beware that Bluetooth and WLAN are the on the same chip and you might easily break your existing setup.

## Card reader
Use .

## Function keys
The function key controlling the microphone does not work.

## Power management
Resume on lid open feature needs to be enabled in the bios / uefi setup: Advanced > Built-in device options > Wake unit from sleep when lid is opened.
