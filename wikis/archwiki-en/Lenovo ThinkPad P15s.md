# Lenovo ThinkPad P15s

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
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
| Card reader || ||
|-
| Bluetooth || ||
|-
| Thunderbolt || ||
|-
| Fingerprint reader || ||
|}

The Thinkpad P15s is a thin-and-light 15.6" workstation laptop from Lenovo's 2020 ThinkPad P lineup.

This page specifically concerns the specifics of running Arch Linux on this laptop. See Laptop for generic laptop-related information, or ThinkPad for other ThinkPad laptops.

## Hardware
## Thunderbolt 3
To use Thunderbolt 3:

1. Go into BIOS

2. Enable BIOS Assist mode: (Thunderbolt 3 -> Enable BIOS assist mode)

## NVIDIA
## Prime features
The NVIDIA driver now supports PRIME Offloading. Following this guide you can try out this new mode.

## Power management
To get the best power options the graphics card may be configured to use low power mode by following the guide here

## Optimus manager
Currently, one of the easiest solutions for this laptop is to use optimus-manager with the hybrid backend. This requires the most up to date nvidia and xorg-server packages.

This allows easy switching between the PRIME offloading feature above, and a mode where external display ports (HDMI and USB-C) work.

Steps to setup after a fresh install:

* Install nvidia proprietary driver 'prime', not bumblebee.
* Reboot.
* Install .
* Reboot.
*  # this will restart your X session, but not make the change persistent.
*  should say: .
*  should list HDMI output - try to configure screen, should work.
*  should work.
*  makes it persistent.
* Check: reboot, external display should still work.

## Audio
This laptop requires Sound Open Firmware in order for the soundcard to work.

## Fingerprint
The 1.90.1 version of fprint supports this device.

## Webcam
The webcam in this laptop is capable of "Windows Hello" which has a Linux version called Howdy. The device you should use to configure howdy on this laptop is . It is possible that Howdy will only use the RGB camera, in this case some additional configuration and software is required. Follow the Reddit guide for the X1 Extreme Gen2 on installing chicony-ir-toggle and setting it up as a service. Or you can just install , which automatically helps you enable the IR camera after booting the system and waking up from sleep. Before installing , make sure you change the local variables in  in PKGBUILD to match your own IR camera. In this case try changing the video device to  in the howdy config ( as root), if everything has worked correctly when running  as root the IR Camera should have a very faint red light. This will indicate that the camera is functioning and Howdy is using the IR camera correctly.

## Keyboard
## Backlight
If you would like to enable the keyboard backlight, run:

 # echo 2 > /sys/class/leds/tpacpi::kbd_backlight/brightness

The "2" represents the brightness and can be any value between 0 and 2 (inclusive) for the laptop. For example, to turn off the keyboard backlight, you would run:

 # echo 0 > /sys/class/leds/tpacpi::kbd_backlight/brightness

## Touchpad
The touchpad works out-of-the-box with libinput. However, it will be very insensitive.

Make sure to not install  - this driver is deprecated, lacks all features mentioned below, but is still installed by default with the  group.

You can check which input driver Xorg is using for your touchpad with:

You can explicitly choose an input driver by placing an Xorg configuration snippet like the following in

## Acceleration
You can adjust acceleration using the command:

 $ xinput set-prop 'SynPS/2 Synaptics TouchPad' 'libinput Accel Speed' 0.5

## Two-finger right click
Additionally, if you wish to disable right-clicking so that you use two finger click as your right click, run:

 $ xinput set-prop 'SynPS/2 Synaptics TouchPad' 'libinput Click Method Enabled' 0 1

## Tap clicking
If you would like for a tap on the touchpad to be registered as a click, use:

 $ xinput set-prop 'SynPS/2 Synaptics TouchPad' 'libinput Tapping Enabled' 1

## Software
## Throttling fix
CPU throttling on the P15s is a known issue but can be easily fixed with undervolting by 100mV.

There are a few ways to fix this. You should only use one of the following as they both attempt to undervolt.

## Throttled
To fix this install , then start/enable .

Note that on kernels 5.9 and newer, the  kernel parameter is required to prevent error messages, for example:

## CPU undervolting
Undervolting the CPU/Intel GPU works well with intel-undervolt.
