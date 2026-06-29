# Acer Aspire E5-575

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Audio || ||
|-
| Wireless || ||
|-
| Ethernet || ||
|-
| Card Reader || ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|}

## Installation
In order to boot from the Arch Linux ISO, hit  to enter UEFI settings (InsydeH20 Setup Utility rev. 5.0). Then set the supervisor password. From there you can disable Secure Boot and boot from any media.

## Configuration
## Add entries to UEFI menu
UEFI will not boot from menu entries created by efibootmgr. Instead, use bcfg in the UEFI Shell (v.2) to add an entry.

## Use Secure Boot with trusted EFI executables
You can use Secure Boot and mark EFI executables as trusted through the UEFI settings. The executables must end with . For example, if you use an EFI boot stub, you must copy  to  and then mark that file as trusted in the UEFI settings.

Whenever the executable is updated, it might have to be removed from the trusted list and then re-added as trusted in the UEFI settings. It is only possible to remove all trusted entries at once, not individually.

See Secure Boot for other options.

## Function keys
Many function keys work without any need for changing settings. Suspend (), blanking the screen (), touchpad disable/enable (), and keyboard backlight disable/enable () all work. Additionally  is mapped to  correctly, as well as  to .

To add functionality for brightness keys,  and , append the following kernel parameters:

 acpi_osi=Linux

Other function keys are exposed as media keys and can be added as keyboard shortcuts for the desired operation.

{| class="wikitable"
! Function Key ()
! Media Key
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|}

## Known issues
## Trusted Platform Module
You may have the following entries in your journal:

 Feb 17 09:58:29 kernel: platform MSFT0101:00: failed to claim resource 1: 0xfed40000-0xfed40fff
 Feb 17 09:58:29 kernel: acpi MSFT0101:00: platform device creation failed: -16

These are related to the Trusted Platform Module (TPM), which can be safely disabled in the UEFI settings if you do not use TPM.

## Not a Dell system error
You may get the following error in your journal:

 dell_smbios: Unable to run on non-Dell system

To remove this error, blacklist the  kernel module.
