# Acer Swift 5

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| TouchScreen || ||
|-
| Camera || ||
|-
| Fingerprint scanner || ||
|}

General info about the Acer Swift 5 SF515-51T laptop. Everything pretty much works out of the box, follow standard documentation for details.

## Disabling UEFI Secure Boot
To disable Secure Boot, set the supervisor password in the BIOS settings. Then you should be able to disable Secure Boot and boot Arch.

## Changing SATA mode to AHCI
To change SATA mode to AHCI, in BIOS settings navigate to the Main tab. If you do not see  settings press  and navigate tabs forwards and backward.  option should now appear.

## Configuration
## Kernel boot parameters
The following parameters can be added to boot arguments as explained in Kernel parameters:

*  to enable backlight setting from keyboard function keys
*  to enable multimedia special function keys
*  to discard pci ACPI informations, may fix boot problems
*  to enable framebuffer compression (power saving)
*  to enable internal microphones
*  to enable touchscreen ( is the ID for the touchscreen from )

## Kernel modules parameters
In kernels after linux-5.10, audio with SOF (Sound Open Firmware) from Intel is fully working (speakers, jack, internal and external mics) with the following setup:
