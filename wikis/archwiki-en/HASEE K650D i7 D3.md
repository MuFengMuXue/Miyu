# HASEE K650D i7 D3

The HASEE K650D-i7-D3 is a powerful laptop, on which Arch Linux runs fine. For a lightweight window manager, some additional configuration should be setup.

## Touchpad synaptics
 should be installed for a lightweight window manager (but not Gnome or KDE). In some cases, addition configuration is necessary for single-click, double-click and middle-click:

For details, see Touchpad Synaptics.

## Backlight
Hot keys for backlight might not work after installation of Arch Linux, so  is necessary for backlight configuration. See Backlight#xbacklight.

## Video cards
Install bumblebee along with Nvidia and Intel drivers.  is recommended for auto configuration after kernel updates.

Acceleration mode of the Intel video card should be changed to "uxa", according to Intel graphics#AccelMethod, so that firefox will not fail to scroll smoothly, and 3D games will run normally.

## Audio
After regular sound check, additional configuration should be conducted. Run  to find default build-in Audio Analog Stereo. In current machine, you can find the card ID with 1 and the device ID with 0. Then following configuration file can be created as following:

After that, run  to unmute.

## Webcam
The webcam works out of the box. In order to test the device, see Webcam setup#Applications.

## Software access point
A Wi-Fi access point can be created in this computer following Software access point. However, WPA/WPA2 will not work properly in channel 1 ~ 9, so channel must be set at 10 or more in the configuration:
