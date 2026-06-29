# HP EliteBook x360 1030 G8

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Audio ||  ||
|-
| Bluetooth ||  ||
|-
| Wi-Fi ||  ||
|-
| WWAN ||  ||
|-
| Webcam ||  ||
|-
| Fingerprint reader ||  ||
|-
| NFC || I2C via  ||
|}

## Accessibility
HP T93 firmware has a bright white background and black/blue font. All settings can be accessed using the keyboard. System LED is integrated into the power button on the backlit keyboard.

## Firmware
Only the main system firmware (HP T93) is currently supported by fwupd.

## Touchpad
Touchpad behaves weird sometimes (ghost clicks, locked in scroll mode). Doesn't seem to be a hardware or software issue, but rather a very sensitive lower area that also recognizes a finger if you only place it on the front edge of the case (not the touchpad itself). Be very careful where you place your "unused" fingers when using the touchpad.

## WWAN
Device (Intel XMM7360) is being detected by recent kernels, but they only contain support for devices in USB mode. On the x360 G8 it is only connected via PCI, so it is missing a stable, working driver. There is an alpha-stage driver with no recent development (Xmm7360-pci) with which several people got the same module to work (including ModemManager) and establish a connection, see upstream for the latest instructions.

## Fingerprint reader
Device (Synaptics FS7600) is being detected by the kernel and supported by  >= v1.94.10.

## NFC
Device (NXP NPC300) is being detected by the kernel, but not recognized by userspace tools. See here for some discussion.

## Function keys
{| class="wikitable"
! Key
! Visible?
! Marked?
! Effect
|-
|  ||  ||  || toggles Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  || unused
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
|  ||  ||  || keyboard backlight bright/dim/off
|-
|  ||  ||  || regular  key
|-
|  ||  ||  ||
|-
|  ||  ||  || unknown purpose
|-
|}
