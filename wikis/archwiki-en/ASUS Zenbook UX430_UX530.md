# ASUS Zenbook UX430/UX530

{| class="wikitable archwiki-table-laptop"
! Device !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (NVIDIA) || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Webcam || ||
|-
| SD-card reader || ||
|-
| Bluetooth || ||
|-
| Fingerprint reader || ||
|-
| Ambient light sensor || ||
|}
ASUS announced UX430 and UX530 models. Since these models share almost the same hardware (the only difference is screen size and discrete NVIDIA GPU), this article covers hardware specific configuration for all UX430UA, UX430UQ, UX530UQ and UX530UX models.

## Configuration
## Secure Boot (option)
In order to boot any Linux operating system, navigate to BIOS, then hit  or click on Advanced Menu, then the Security tab and set Secure Boot to .

If the aforementioned Secure Boot option is a menu rather than an on-or-off option, click on Secure Boot, Key Management, then Reset to Setup Mode and confirm in the dialog.

## Video
See Intel graphics and hardware video acceleration. For models with discrete NVIDIA graphics card, also see NVIDIA Optimus.

## Audio
See PulseAudio.

## Touchpad
See Libinput.

## Fingerprint sensor
The fingerprint sensor is supported since Fprint v0.99.0, even through it is supported it does not work reliably. This is due to the fingerprint small sensor=== Ambient Light Sensor ===

The Ambient Light Sensor should work on UX430UQ[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=db2582afa7444a0ce6bb1ebf1431715969a10b06 and UX430UNR=== Battery charge threshold ===

See Laptop/ASUS#Battery charge threshold.

## Troubleshooting
## Microcode
During boot you might get the message . See Microcode to resolve it.

## NVIDIA issues with Bumblebee
It is likely that it is one of these issues:

* You used a power management application (especially Powertop). See bumblebee#Broken power management with kernel 4.8 for more information.
* You suspended your laptop and resumed, and are now unable to start your GPU, see Bumblebee#Failed to initialize the NVIDIA GPU at PCI:1:0:0 (Bumblebee daemon reported: error: %5BXORG%5D (EE) NVIDIA(GPU-0)).

## Headset Microphone
You may encounter an issue where your headset microphone is not being detected. To fix this, use  as explained in Advanced Linux Sound Architecture/Troubleshooting#Wrong model autodetection.

## No sound after Windows reboot
There seems to be a bug in the firmware that prevents the embedded sound card from working in Arch after Windows has been restarted. The sound system works, and you can hear sounds from, say, wireless headphones, but the embedded sound card either plays no sounds at all, or plays sounds for a couple seconds before quickly "fading out" to silence.

Unlike some other models, suspending and resuming makes no difference. Instead, following are the known workarounds:

* If you have not exited Windows yet and plan to boot into Arch next, do a Windows shutdown instead of restart, and then boot into Arch.
* If you are already booted into Arch, do an Arch shutdown/poweroff and then boot back into it (an Arch reboot will not work).

As a general rule of thumb, if the sound card is not working, boot into Arch via a complete shutdown (as opposed to a restart) to fix it.

## Suspend
See Power management/Suspend and hibernate#Changing suspend method.

## Fan always active
See Fan speed control#NBFC.

## Tips and tricks
## Power saving and performance
As advertised by ASUS, both laptops are capable to last up to 9 hours on battery. In order to achieve this, see:

* BIOS update - It is generally recommended to update BIOS, as it usually brings performance, power-saving and security features.
* Power Saving - List of general recommendations to increase battery life.
* Improving performance - List of general recommendations to increase performance.
* SSD - Tips and tricks for Solid State Drives. Both laptops ship M.2 SSD by default.
* Undervolting CPU - Decrease voltage for Intel CPU (reduce battery drain, reduce heat and therefore - reduce fan speed)

## Extract Windows 10 license key
The laptop comes with Windows 10 preinstalled and the activation key is hardcoded into the firmware. If you replace Windows with Linux, then hardcoded activation key is useless. You might want to extract it and use somewhere else (e.g. virtualized Windows 10):
 # grep -aPo '\w{5}-[\w]{5}-[\w]{5}-[\w]{5}-[\w{5}' /sys/firmware/acpi/tables/MSDM
