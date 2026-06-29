# MSI GS63VR

{| class="wikitable archwiki-table-laptop"
|| Device || GS63-6RF (2016) || GS63 (2017) || GS63-8RE (2018)
|-
| CPU ||  i7-6700HQ ||  i7-7700HQ ||  i7-8750H
|-
| Display || -- || Full HD 120Hz/3ms || Full HD 120Hz/3ms
|-
| Intel IGU ||  Intel HD Graphics 530 ||  HD Graphics 630 (i915) ||   Intel HD Graphics 630
|-
| Nvidia GPU ||  GTX 1060 ||  GTX 1070 ||  GTX 1060
|-
| Network ||  ||  ||
|-
| Atheros Wireless ||  ||  ||
|-
| ALSA ||  ||  ||
|-
| Touchpad ||  ||  ||
|-
| Webcam ||  ||  ||
|-
| Card Reader ||  ||  ||
|-
| Power management ||  ||  ||
|}
The GS series of MSI laptops is considered to be a thin gaming laptop. Although it is not thin as ultrabooks, it is still very thin for a gaming laptop. As of October 5th 2017, the 2016 model works fine with the latest kernel. The 2017 model has a bug concerning the eDP LCD display. There is a fix from intel here: https://github.com/freedesktop/drm-tip/commit/0501a3b0eb01ac2209ef6fce76153e5d6b07034e.patch

This issue was discussed in this thread: https://bbs.archlinux.org/viewtopic.php?id=230541

## Installation
Standard installation works flawlessly per the Installation guide.

## Drivers
## Nvidia/Optimus
It is possible to use Bumblebee to make the Nvidia GPU in this laptop usable.  In order to avoid issues caused by the BIOS in the GS63VR when using bbswitch, add  to the kernel options at boot (per NVIDIA Optimus#Lockup issue (lspci hangs)).

For HDMI/DP ouput: Bumblebee#Output wired to the NVIDIA chip.

As alternative, you can use Optimus Manager. You can change between Intel and Nvidia  restarting the X server and use external screen use nouveau driver.

## Touchpad
This laptop uses an Elantech touchpad, and as such libinput works well.
Two finger scrolling works out of the box (tested on GS63-6RF and GS63-8RE).
Install  for more multitouch actions.

## Networking
## Wireless
NetworkManager works out of the box for Wi-Fi on both 2.4GHz and 5GHz networks.

## Audio
The headphone jack always acts as SPDIF out and subsequently has no volume control and does not mute the speakers when a device is plugged in.  Link to a description of the issue on the ALSA mailing list.

As a workaround it is possible to reassign a microphone input jack using hdajackretask to behave as an audio output.

## SteelSeries keyboard
To set color to Steel Series keyboard use MSIKLM

## GS63-8RE
Use the instructions on MSI GS65#Keyboard backlight to install .

## Sleep
If the laptop does not fully enter sleep mode, bluetooth and mobile light stay on and sleep light does not come on. Then try reinstalling TLP.

## Web camera
## GS63-8RE
 will toggle disable/ enable the web camera.

## Power management
## GS63-8RE
After installing NVIDIA, bumblebee, and  bbswitch while running KDE power usage is down to ~7W or 9 hours according to powertop.

## Misc
## BIOS
To access the BIOS, from a cold shutdown, repeatedly press the  key immediately after pressing the power button.
To access the Boot Device Menu, from a cold shutdown, repeatedly press the  key immediately after pressing the power button.
