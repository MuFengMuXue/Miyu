# ASUS Zenbook UM3402YAR

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Audio (HDMI)||  ||
|-
| Audio (Speakers)||  ||
|-
| Bluetooth ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint ||  ||
|-
| TPM ||  ||
|}

## Installation
Install per the Installation guide. The default Arch installer does not support Secure Boot so you will have to disable it before performing the installation. If you want to dual boot with Windows you will need to configure UEFI Shim or similar to allow Secure Boot to be re-enabled and Windows to boot without additional steps to unlock Bitlocker drive encryption.

## Accessibility
The ASUS firmware is accessed via  at boot. It is a graphical interface that can be navigated by mouse or keyboard. It is graphical and not text based.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
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
|  ||  ||  || Keyboard backlight cycle
|-
|  ||  ||  || Monitor select
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Screenshot
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
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function

## Numpad 2.0
See asus-numpad and follow the instructions. UM3402YAR's Numpad corresponds to  layout.

Install , configure it then enable/start the .

## Fan control
The UM3402YA laptop series do not have kernel modules to control fan profiles. EC registers are the way to control the fan level, where it also affects CPU performance and thermal throttling prevention depending on which fan pre-configured profiles the end-user writes to the registry (ASUS AIPT).

Each laptop model might have different registry and hexadecimal values. Therefore, the best way to know the fan registry and the values to the registry which represents the fan profiles, is by installing nbfc on a windows machine and using the monitor tool supplied, in a terminal with administrator permissions:

 > ec-probe monitor

While monitoring the changes using ec-probe for the fan registry, have MyASUS open and change the fan profile within it until you see a pattern change for a certain registry, in the ec-probe terminal window and the values corresponding to it. Once you found the registry, take notes of the hexadecimal values for each fan profile selected via MyASUS.

To read a registry's value:

 > ec-probe read 0x61

On a UM3402YAR laptop with the  registry related to the fan profile, and a  hexadecimal value for setting the standard profile, the following should be written to the found registry:

 > ec-probe write 0x61 0x00

You can now boot to your Linux operating system, and safely write the hexadecimal values to the registry as desired using the nbfc's EC probing tool.

The following were the fan profile hexadecimals for the  registry on a UM3402YAR laptop:

{| class="wikitable"
|-
! Fan Profile !! Hexadecimal
|-
| Silent Mode ||
|-
| Standard Mode ||
|-
| Performance Mode ||
|}
