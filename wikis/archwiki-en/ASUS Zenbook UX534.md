# ASUS Zenbook UX534

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Webcam || ||
|-
| Card reader || ||
|-
| Bluetooth || ||
|-
| Face recognition sensor || ||
|}

ASUS UX334, UX434 and UX534 models with ScreenPad™ 2.0. These models most probably share almost the same hardware (the only difference is screen size and discrete NVidia GPU, and missing Display Port Alt-Mode on some models, even 15 inch seems to not include USB-C DP Altmode -), this article covers hardware specific configuration for all ZenBook 13 (UX334), ZenBook 14 (UX434) and ZenBook 15 (UX534).

However the first author is testing on an UX534FTC Full HD (no 4K), with NVidia GTX1650 Max-Q and a 10th generation  10510U Core I7.

## Configuration
## Secure Boot
In order to boot Arch (or any OS not supporting Secure Boot), enter the UEFI parameters by holding  (or  key and then selecting "Firmware Setup"), then navigate with the keyboard arrows to the "Security" tab and set "Secure Boot" to .

## Video
See Intel Graphics and Hardware Acceleration. For models with discrete Nvidia graphics card, also see NVIDIA Optimus.

The Screenpad works as a secondary display and is completely separate from the touchpad: you just have a (non-touch) second screen under your fingers. Therefore it can be deactivated like any other display using one's Desktop environment settings for example, thus lowering power consumption while leaving the touchpad functionality intact.

The Screenpad requires a 'Rotation Portrait Left' and is most useful with a scale factor of 200% (Wayland allows to set a different scale factor of 100% if the main screen in only the Full HD version). If you dual boot, brightness is kept from the last Windows setting.

To change the Screenpad brightness, you can install the custom kernel module asus-wmi: https://github.com/Plippo/asus-wmi-screenpad

## Touchpad
See Libinput. See Screenpad in #Video

## Facerecognition login
This computer has built-in face recognition sensor.
You can use it with the project Howdy https://github.com/boltgolt/howdy.
See the howdy page for further informations.

## Battery charge threshold
See Laptop/ASUS#Battery charge threshold.

## Troubleshooting
## Suspend
See Power management/Suspend and hibernate#Changing suspend method.

When activating suspend-to-ram, the sound is crackling (and not working for regular use) at wake-up.
An ugly fix is to reset the sound card (either inserting/removing a jack, or with the following scripts)

Create the following script (do not forget to make it executable):

Create the following service:

Enable .

## Tips and tricks
## Power saving and performance
As advertised by ASUS, these laptops are capable to last up to 9 hours on battery. In order to achieve this, see:

* BIOS update - It is generally recommended to update BIOS, as it usually brings performance, power-saving and security features.

* Power Saving - List of general recommendations to increase battery life.

* Improving performance - List of general recommendations to increase performance.

* SSD - Tips and tricks for Solid State Drives. These three laptops ship M.2 SSD by default.

* Undervolting CPU - Decrease voltage for Intel CPU (reduce battery drain, reduce heat and therefore - reduce fan speed)

* Bumblebee - If using bumbleblee and optimus, install 'bbswitch' to allow a good shutdown of NVidia Card ('nvidia-smi' return error if NVidia is power off, or information if it is in use)

UX534FT FHD perfom perfectly with Gnome 3, Bumblebee (bbswitch activated), Konkor (Gnome-extension) with Governor 'Power Save' does :

* 10h+ (more than 10 hours probably arround 12h or more) watching a video from network using VLC with bluetooth audio, low brightness (not lowest)

* 7.5h+ with brightness arround 60% watching a Youtube Video and using Firefox

* ? h (TODO) in heavy duty task (for example 'optirun' task using discrete Nvidia GPU
