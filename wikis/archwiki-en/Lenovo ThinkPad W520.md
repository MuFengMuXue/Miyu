# Lenovo ThinkPad W520

## GPT / MBR Partition Table
I was unable to get the most recent version of the BIOS to boot from a GPT partition table. Everything worked fine once I tried an MBR ("msdos" in gparted) partition table.

## Wi-Fi issues
* Random Disconnection
** The output from running  as root will include "wlan0: deauthenticating from MAC by local choice (reason=3)"
** Disable power management of pci-express in BIOS

## Nvidia Optimus Setup
## Bumblebee
nVidia Optimus works nicely with a standard bumblebee setup, using the proprietary NVIDIA drivers. For further information refer to the NVIDIA Optimus article.

## Multimonitor
The digital and analog video outputs are hardwired to the nVidia chip and are thus unvailable in a standard bumblebee setup, since the X Server is run by the Intel GPU. Unlike earlier Thinkpad W Models, the VGA-Output is not connected to the integrated chip. There are several workarounds available.

Using  works really well with little tweaking necessary
 $ intel-virtual-output -f

It is needed to enable virtual outputs for intel graphic card  .

see also Stackexchange for troubleshooting with virtual outputs

{{hc|multiscreen_term.sh|
#!/bin/bash
# Initializes Bumblebee for multi-screen functionality.
xrandr --output VIRTUAL8 --off
xorg_process=$(ps aux | grep 'Xorg :8' | awk '{print $2}')
kill -15 $xorg_process
sleep 1
rmmod nvidia_modeset
sleep 1
rmmod nvidia
}}

For the nvidia card to recognize external monitors, some lines have to be commented out of the default config file at .

see also: Phoronix Nvidia Forums

## Ultranav - Trackpoint and Touchpad
Trackpoint and Touchpad will work out of the box, but some tweaking is required for further configuration.
* Set up trackpoint scrolling by adding a new config in .

* Trackpoint sensitivity and speed can be set up using an udev rule in  (the add-rule will work around the configuration not being applied when the trackpoint hasn't been loaded, alternatively a wait-for can be used, which comes with the added drawback of added unresponsiveness of the trackpoint some time after boot)
{{hc|82-trackpoint.rules|# Set the trackpoint speed and sensitivity
ACTION=="add",SUBSYSTEM=="input",ATTR{name}=="TPPS/2 IBM TrackPoint",ATTR{device/sensitivity}="240"}}
* Touchpad can be used after installing

## Other
## Boot up issue with UDEV timeout
Similar issue at .

## System beep
See PC speaker#Disabling the PC speaker.

## Screen brightness
 is enabled by default, unfortunately this setting does not work well for the W520, disabling it should solve the issue:

 video.use_native_backlight=0

The following kernel parameters may also be necessary to get backlight control working in X sessions with NVIDIA drivers:

 acpi_backlight=video

and create the file:

## FAN Settings with Thinkfan
Default temperature management allows only a limited fan speed. This inherently leads to overheating since the laptop is designed to run with unregulated fan speed under full load.

Thinkfan.conf:
