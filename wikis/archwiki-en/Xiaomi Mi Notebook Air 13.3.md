# Xiaomi Mi Notebook Air 13.3

{| class="wikitable archwiki-table-laptop"
|-
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
| Webcam || ||
|-
| Thunderbolt || ||
|-
| Fingerprint (2018) || ||
|}
The Mi Notebook Air 13.3 is an aluminium Ultrabook. It is a product by the Chinese Company Xiaomi and is currently only available in China or through import online-shops.

The 2016 and 2018 revisions share enough characteristics to be configured identically.

## Installation
Enter the UEFI menu by pressing  during Boot, then do the following:

* Security > Set Password
* Security > Disable Secure Boot
* Reset the password by setting the password again but letting the "New Password" fields blank

Installation can then proceed normally. Refer to the Installation guide for more info.

## GPU
## Intel only
If you want to completely disable the NVIDIA GPU and save battery, do the following:

* Install the  package
* Blacklist the NVIDIA and Nouveau kernel modules:

* Install  to turn off the card

## Intel/Nvidia Hybrid Configuration
You can enable hybrid GPUs by either using Bumblebee or NVIDIA Optimus. Bumblebee is generally better for battery-life and compatibility but not officially supported by NVIDIA.

Refer to the respective articles.

## Touchpad
To use the touchpad like a normal one, you have to use . If you use , your touchpad acts like a touchscreen (e.g it maps your movements directly to your screen). Synaptics usage is discourage since it is deprecated and only working sporadically. This configuration of  using Xorg configuration files enables two finger gestures, tap-to-click and 2-and 3-finger clicks (for right- and middle-click respectively).

## Function keys
On this notebook the Function keys are enabled as default (e.g. pressing  mutes the sound). If pressing the keys does nothing you are most likely using a Window manager and not a Desktop environment. Use the respective configuration files to bind the keys to their use. For example Xbindkeys or i3's .

To reverse to normal  keys just press: .

Most Fn-keys return the correct keycodes. Here is a table containing that information:

{| class="wikitable"
! Fn-F-Key
! Keycode
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|-
|
|
|}

## Display Calibration
Factory display calibration is poor. Try the ICC profiles at https://github.com/tlvince/xiaomi-mi-notebook-air-13/tree/master/display-calibration

## Troubleshooting
## Backlight
If you use a tool like  in its default configuration, nothing happens, because the path to the backlighting variable is not standard. To fix this issue, you have to use a Xorg configuration file:

## Audio Jack
If you want to use the microphone from the headset plugged in the combo jack input use  as explained in Advanced Linux Sound Architecture/Troubleshooting#Wrong model autodetection.
