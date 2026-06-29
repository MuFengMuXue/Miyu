# Lenovo ThinkPad P14s (AMD) Gen 6

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
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
| Touchpad ||  ||
|-
| Touchscreen ||  ||
|-
| Webcam ||  ||
|-
| TPM || ||
|-
| Fingerprint reader ||  ||
|-
| Smartcard reader || || Untested
|-
| NFC || || Untested
|}

Model Number:

This article covers the installation and configuration of Arch Linux on the Lenovo ThinkPad P14s (AMD) Gen 6 laptop.

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
Since kernel 6.5, the AMD P-State EPP driver with "Active" profile is applied by default, no additional configuration is needed.
Just ensure  was properly added during installation.

## GPU
If you experience occasional split-second screen flickering or massive lags when using the terminal, add the  kernel parameter=== GPU Resets ===

If experiencing GPU resets (black screen), refer to Lenovo ThinkPad T14s (AMD) Gen 3#CPU.

## Input Devices
## Touchpad
To disable sleep wake-up from touchpad, see Lenovo ThinkPad T14s (AMD) Gen 3#Disable wakeup from sleep on touchpad activity.

## Touchscreen
For variants that include a touchscreen, it should work out of the box.

See Touchscreen for additional information.

## Audio
## Speakers
Speakers work out of the box, but default sound quality is poor due to missing Dolby Atmos Convolver.

Improve sound quality using EasyEffects with a convolver effect. Refer to [https://github.com/kikislater/thinkpad-p14s-g5-linux/#sound these presets.

## Microphone
## Recognized but Silent
If the internal mic is recognized by ALSA but the recorded input is silent, see this Arch Linux forum thread and adapt according to your model number.

## Microphone LED
If the Mic LED seems to stay always on, see Lenovo ThinkPad T14 (AMD) Gen 3#Mute Mic LED always on.

## Networking
## Wi-Fi
Wi-Fi works out of the box with modern kernels (such as 6.17 and newer).

The MediaTek Wi-Fi card  is soldered onto the mainboard.

## Peripherals
## Smartcard Reader
Untested. Follow instructions from smartcards.

## Fingerprint Reader
Works as expected. Follow fprintd documentation.

## NFC
Uses an NXP NPC300 connected via I2C. To use, load the modules  and .

For more information, see NFC.

## Power Management
## Sleep Modes
## S3 vs s2idle Sleep
S3 () sleep not supported by this CPU, and as such there is no BIOS parameter for sleep mode selection.

, a.k.a.  works out of the box with kernel 6.17.1. In some older firmware version of this machine, the ACPI will repeatedly wake the device if Wake-on-LAN is disabled. This issue is not present on updated firmware versions.

Sleep power consumption varies based on OS and peripheral sleep management.
 power consumption on this CPU can be debugged with one of AMD's Linux debug tools.

## Hibernation
Not tested.
If experiencing Wi-Fi issues after hibernation, see #Wi-Fi

## Battery Management
## Charge Thresholds
Battery charge thresholds can be set using:

* TLP
* KDE power management
* GNOME power management

## Power Profiles
## Important notice
TLP, especially with  has seamless integration, easy and reliable configuration.
, on the other hand, whereas integrated in Gnome and KDE, does not offer (yet) as many options as tlp.

## TLP
Install
Start/enable the  service
Optional: Install  for configuration
Optional: Apply tlp configuration for P14s Gen5 (put in `/etc/tlp.d`): Link to TLP conf for Ryzen 7

## Power Profiles Daemon
Install
Start/enable the  service.

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
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  ||  ||
|-
|  ||  ||  || Change keyboard backlight level ||
|}

# The key is visible to xev or  and similar tools.
# The physical key has a symbol on it, which describes its function.
