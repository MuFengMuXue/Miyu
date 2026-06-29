# TUXEDO InfinityBook Pro 15v4

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Card Reader || ||
|-
| Webcam || ||
|-
| IR Camera || ||
|-
| Thunderbolt 3 || ||
|-
| Fingerprint sensor || ||
|}

## Configuration
## Video
## Drivers
See Intel graphics#Installation and Hardware video acceleration

## Function keys
The most  function keys work out of the box. For the  function keys ,  and  the following must be set as kernel parameter. If  is installed this is not necessary.

 acpi_os_name=Linux acpi_osi=

## Keyboard backlight
TUXEDO Computers provides a driver for their models with RGB keyboard. TUXEDO Keyboard can be installed manually from source or you use

## TUXEDO Control Center
TUXEDO Computers provides their own control center, TUXEDO Control Center (TCC), "to help you control performance, energy, fan and comfort settings". Install the  package.

## Power management
## Suspend
See Power management/Suspend and hibernate#Changing suspend method.

Read more at the help page from TUXEDO === Undervolting ===

With the TUXEDO Premium BIOS you can undervolt the CPU over the BIOS. You can switch between  and . The selectable values are not dangerous, but test it in small steps. So try , if it is stable you can try  and so on You also can use . Read Undervolting CPU for more Informations.

By default  is pre-selected. You can change the value over the BIOS under Setup Utility > Advanced > Advanced Chipset Control > BIOS-controlled Undervolting.

## BIOS Performance Profiles
With the TUXEDO Premium BIOS you can select one of four Performance Profiles. By default Entertainment is pre-selected.

* Quiet
* Power Saving
* Entertainment
* Performance

You can change the Profile over the BIOS under Setup Utility > Advanced > Advanced Chipset Control > Performance Profile Select.

More informations can found at the help page from TUXEDO [https://www.tuxedocomputers.com/en/Infos/Help-Support/Instructions/Premium-BIOS-BIOS-Performance-Profiles.tuxedo

## Thunderbolt
The integrated Thunderbolt Controller will only shown up when a Thunderbolt device is connected or if you manually force Thunderbolt power.
