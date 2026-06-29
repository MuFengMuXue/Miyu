# TUXEDO InfinityBook S 14 v5

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
| Card Reader || ||
|-
| Webcam || ||
|-
| IR Camera || ||
|}

## Video
See Intel Graphics and Hardware Acceleration

## Audio
If the Headphone Jack Audio not working it can be fixed by create the following file:

## Function keys
The most  function keys work out of the box. For the  function keys ,  and  the following must be set as kernel parameter. If  is installed this is not necessary.

 acpi_os_name=Linux acpi_osi=

## TUXEDO Control Center
See TUXEDO InfinityBook Pro 15v4#TUXEDO Control Center.

## Power Management
## Suspend
See Power management/Suspend and hibernate#Changing suspend method.

Read more at the help page from TUXEDO: https://www.tuxedocomputers.com/en/Infos/Help-Support/Instructions/Fine-tuning-of-power-management-with-suspend-standby.tuxedo.

## Undervolting
With the TUXEDO Premium BIOS you can undervolt the CPU over the BIOS. You can switch between  and . The selectable values are not dangerous, but test it in small steps. So try , if it is stable you can try  and so on You also can use . Read Undervolting CPU for more Informations.
As default  is pre-selected. You can change the value over the BIOS under ''Setup Utility > Advanced > Advanced Chipset Control > BIOS-controlled Undervolting''.

## BIOS Performance Profiles
With the TUXEDO Premium BIOS you can select one of four Performance Profiles. As default the  is pre-selected.
* Quiet
* Power Saving
* Entertainment
* Performance
You can change the Profile over the BIOS under ''Setup Utility > Advanced > Advanced Chipset Control > Performance Profile Select''.
More informations can found at the help page from TUXEDO https://www.tuxedocomputers.com/en/Infos/Help-Support/Instructions/Premium-BIOS-BIOS-Performance-Profiles.tuxedo
