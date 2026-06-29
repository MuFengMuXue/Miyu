# MSI Prestige 13 AI Evo A2VM

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
| Bluetooth ||  ||
|-
| Card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| TPM || ||
|-
| Thunderbolt 4 ||  ||
|-
| Fingerprint reader ||  ||
|}

MSI Prestige 13 AI+ Evo A2VM is an Intel Core Ultra 258V (Lunar Lake) ultraportable laptop releast in Fall 2024. (PDF Spec Sheet)

Kernel 6.13 fixes a stuttering issue.

## Firmware
"BIOS updates" (for the UEFI) are located at the MSI Support site.

## Sound
Sound requires Sound Open Firmware to be installed.

There have been reports of sporadic output corruption. If you experience this, you can try to restart your sound server, e.g. the  user unit.

## Suspend
Only s0ix/s2idle is supported (s3/deep is listed but fails to resume if used).

Using batterylog to measure suspend battery drain gives a relatively good 11-12%/day with the `6.12.0-rc6-1-mainline` kernel:

## Web camera
The MSI web camera is a MIPI camera attached to the Intel Lunar Lake IPU7. It does not currently work. The most detailed notes at the moment are here: https://gist.github.com/JeremyGrosser/dff7991668d80220b4a3429590eb59a3#camera

There is an ipu7-drivers open issue here: https://github.com/intel/ipu7-drivers/issues/17
