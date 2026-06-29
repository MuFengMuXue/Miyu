# Lenovo ThinkPad P14s (Intel) Gen 6

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Ethernet ||  ||
|-
| Audio ||  ||
|-
| TrackPoint || ||
|-
| Touchpad || ||
|-
| Touchscreen || || Untested
|-
| Webcam ||  ||
|-
| TPM || ||
|-
| Fingerprint reader ||  ||
|-
| Smartcard reader ||  ||
|-
| NFC || || Untested
|}

Model Number:

This article covers the installation and configuration of Arch Linux on the Lenovo ThinkPad P14s (Intel) Gen 6 laptop.

For a general overview of ThinkPad-related articles and recommendations, see Laptop/Lenovo.

## Firmware
This model is fully compatible with fwupd.

Run the following command to detect system components:

This will detect:
* System Firmware
* UEFI BIOS
* Webcam
* Fingerprint sensor
* CPU/GPU
* TPM
* NVMe controller

## CPU
The laptop features an Intel Arrow Lake-H processor with a hybrid architecture (Performance-cores and Efficient-cores).

The  package should be installed for microcode updates.

Frequency scaling is handled by the  driver in active mode by default.

## GPU
This laptop uses a hybrid graphics solution: see NVIDIA Optimus for configuration options (e.g., PRIME).

## Touchpad
To disable sleep wake-up from touchpad, see Lenovo ThinkPad T14s (AMD) Gen 3#Disable wakeup from sleep on touchpad activity (applicable to most ThinkPads).

## Audio
It requires  and  for proper functionality. The microphone and speakers should work out of the box with PipeWire or PulseAudio.

## Smartcard reader
See Smartcards for configuration.

## Fingerprint reader
The Goodix reader is supported by fprintd.

## Power management
## Sleep modes
S3 () sleep is typically not supported on Intel Arrow Lake mobile CPUs.

 (S0ix) is the default and works out of the box.

## Charge thresholds
Battery charge thresholds (also called Battery conservation mode) can be set using: TLP, KDE and GNOME power management.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
! Note
|-
|  ||  ||  ||  || Can be swapped with left Ctrl in BIOS
|-
|  ||  ||  ||  ||
|-
|  ||  ||  || Toggles Fn lock || Has status led
|-
|  ||  ||  ||  || Has status led
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  || Has status led
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  || Marked with airplane mode
|-
|  ||  ||  ||  || Marked with message box
|-
|  ||  ||  ||  || Marked with phone answer call
|-
|  ||  ||  ||  || Marked with phone end call
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  || Change keyboard backlight level ||
|}

# The key is visible to xev or  and similar tools.
# The physical key has a symbol on it, which describes its function.
