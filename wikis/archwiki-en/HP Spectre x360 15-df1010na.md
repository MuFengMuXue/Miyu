# HP Spectre x360 15-df1010na

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| GPU Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader || ||
|-
| TPM || ||
|-
| Thunderbolt ||  ||
|}

## Installation
Secure Boot must be disabled in the BIOS.
The BIOS can be accessed by holding down  while booting, then pressing  when the options screen is shown.  can be used to select the boot device.

## Firmware
fwupd supports this device.

## Biometrics
## Fingerprint Scanner
Tested using Fprint, fprintd-enroll reports that the device cannot be found.

## Windows Hello
Facial recognition works using Howdy.

## Audio
If audio does not work initially, create the file
with the following line.

 options snd-hda-intel

The audio mute button works by default but with no led indicator to show its state.
Suggested fixes including adding  after
but this does not appear to work for this model.

## Power management
For general battery improvements,  and  seem to help,
although battery life is still poor.

Unfortunately HP do not support s3 sleep (see Power management/Suspend and hibernate) for this laptop,
which leads to extreme battery drain when left in 'suspend' mode (s2idle).

This can be fixed by modifying the DSDT, but resuming from suspend with deep sleep is unreliable, rendering this method pointless.
An alternative solution to saving power would be using hibernation and then focusing on improving the boot time to bring wakeup from hibernation closer to wakeup from suspend times.

## ACPI override to support S3 sleep
See Power management/Suspend and hibernate#Changing suspend method for the general context in which this workaround fits.

Extract and disassemble the DSDT tables. You then need to modify the  file.

Find the section which begins with
and increment the final number (remember to increment it as hex).

For example:

 DefinitionBlock ("", "DSDT", 2, "HPQOEM", "863E    ", 0x01072009)

Should be changed to

 DefinitionBlock ("", "DSDT", 2, "HPQOEM", "863E    ", 0x0107200a)

Then the definition for  needs to be added between the sections for
 and .
This should end up as follows:

{{bc|    Name (_S0, Package (0x04)  // _S0_: S0 System State
    {
        Zero,
        Zero,
        Zero,
        Zero
    })
    Name (_S3, Package(0x04) //  _S3_: S3 System State
    {
        0x03,
        0x03,
        Zero,
        Zero
    })
    Name (_S4, Package (0x04)  // _S4_: S4 System State
    {
        0x06,
        Zero,
        Zero,
        Zero
    })
}}

You then need to recompile the DSDT tables and create a cpio override archive, as explained in DSDT#Using modified code.
