# ASUS N550JV

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Intel || ||
|-
| Nvidia || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Camera || ||
|-
| Card Reader || ||
|-
| Bluetooth || ||
|}

ASUS N550JV - this article covers hardware specific configuration. All topics covered can be performed after an installation of Arch Linux has been finished and the machine rebooted into it.

For a general overview of laptop-related articles and recommendations, see Laptop.

## Configuration
## Video
## Drivers
See Intel Graphics,  Hardware Acceleration and NVIDIA Optimus.

## Brightness
In order to be able to adjust the screen brightness using  and  you need to set the kernel parameter  (the space is required).

## Audio
Install PulseAudio.

After installation, reboot the laptop to ensure all modules are loaded. Check if the fallback device is correctly set to Built-in Audio Analog Stereo with . See PulseAudio/Troubleshooting#Fallback device is not respected for more information. Also check for muted devices:

 $ alsamixer -c PCH

## Keyboard
## Brightness
Key mappings  and  should work with most desktop environments out of the box. If not, install , load the kernel module  to control hotkeys, then start/enable the .

## Incorrectly mapped buttons
 and  buttons are not mapped correctly. It is not necessary to remap  shortcut, because it works without any additional configuration.

Install , which provides app . Generate a xmodmap config file if you have not done it already:

 $ xmodmap -pke > ~/.Xmodmap
Then open it and locate keycode 234:

Now move  text on the empty keycode 248 and leave keycode 234 empty:

Optionally, for  give some value on keycode 253.

The next step is apply changes:

 $ xmodmap ~/.Xmodmap

Test with  or try to bind something on media button.  should be controlled by hardware and switch display without any additional configuration. Also, if you are satisfied, put the command above to Xinitrc.
{{hc|~/.xinitrc|
{ sleep 10; xmodmap ~/.Xmodmap; } &
}}

## Touchpad
Install libinput. If there are any problems, try Touchpad Synaptics.

## Troubleshooting
## Audio
## Dual boot
If you boot your laptop right after Windows to Linux, sound might only work through headphones jack, but not through speakers and subwoofer. The quick fix is to suspend your laptop and resume it back.

## Bug
The internal speakers seems not to play any sound until volume is being increased significantly. This also occurs on Windows operation system as well as on Linux.

## Sound pops twice during shutdown and sleep
Create and enable the following two services:

## Crackling sound
Add  to PulseAudio config file as per instructions at PulseAudio/Troubleshooting#Troubleshooting buffer underruns (glitches, skips, crackling).

## Failed to initialize the NVIDIA GPU
If you receive error similar to this , see here.

## Messages during console login
After booting up, when Linux asks you to enter your login and password, some messages might appear similar to these:

 Nouveau E[    PBUS]MIMO write of 0x00000002 FAULT at 0x4188ac [ IBUS
 Nouveau E[    DRM] Pointer to TMDS table invalid
 Nouveau E[    DRM] Pointer to flat panel table invalid

To resolve, refer to #Drivers.

## USB devices and sleep
Hibernate via systemd works out of the box when the swap space or file is correctly identified in the resume kernel parameter. However, even though the system suspends properly it will lock up when resuming. This is due to the USB controller not properly turning off on its own. Create two the following files as shown:

Then enable  and  as root.

## Battery charging issues
This battery in this laptop can only be accessed by removing the bottom of the entire laptop, which requires removing 10 TORX-5 screws. That there appears to be a power issue related to the recharging USB port (the USB port with a lightning bolt) under Linux. When an externally powered device is plugged into the charging USB port and the system is power cycled, the battery indicator will begin flashing orange and the system no longer recognizes or charges the battery. One way to reset the charging circuit is to force shutdown by holding the power button for a few seconds. See this thread at the Ubuntu forums for other possible solutions.

## Card reader does not detect cards
Due to unknown reasons, card reader does not detect cards. To resolve this, quickly pull out the card and insert it back for several times (leave inserted afterwards) and after few seconds card will be detected in your system.

## Tips and tricks
## Fan control
See Fan speed control.

Here is a configuration file, which was tested on Asus N550JV and was used with  kernel module. It however might need some tweaking:

Here is a configuration file, which was tested on Asus N550JV and was used with  kernel module. It however might need some tweaking:

## Enable full performance of GPU
If you have BIOS 208 or 207 installed and tried to play something heavy, you noticed that for a few seconds game runs for 60fps, but most of the time - 20-40fps. This is strange behaviour, which happens on Windows as well as on Linux. Even if the temperature limit is set to 90c, GPU throttling occurs at 75c or even all the time (with a feeling that GPU only runs at 60-70% of its full potential).

To fix this, flash bios 206. If your BIOS version is newer than this, you must follow this guide, which requires you to have Windows installed on this laptop.

## Special keys for window managers
If you prefer using a Window manager rather than a Desktop environment, most settings will not work out of the box, so you might need to manually bind every single  button combination. How to bind, see Extra keyboard keys in Xorg.

{| class="wikitable"
! Buttons !! Output
|-
| Media Button ||  (xmodmap)
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||  (xmodmap)
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|}
