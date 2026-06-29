# HP ZBook Studio G5

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| Webcam ||  ||
|-
| Backlight ||  ||
|-
| Bluetooth ||  ||
|-
| SD-Card slot ||  ||
|-
| Audio ||  ||
|-
| HDMI audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|}

The HP Zbook Studio G5 is a workstation replacement laptop.

## Configuration
## Thunderbolt
Since the Zbook does not allow a no security option for Thunderbolt in the BIOS, a Thunderbolt manager has
to be installed see .

## Graphics
## Nouveau
This laptop works out of the box with nouveau graphics from the latest kernel, including HDMI audio. The performance is worse than with Nvidia drivers, which is especially noticeable in video decoding. Frames might get dropped when trying to stream 1080p videos, depending on the bitrate. The biggest issue, though, is that when the laptop has been connected to an external monitor, the shutdown does not complete and you have to force shutdown.

## Nvidia drivers
The proprietary Nvidia drivers work flawlessly on this laptop. This driver also has better performance than the nouveau driver, but for Wayland users using this driver is not an option (yet).

## BIOS settings
In the BIOS you can choose between three different modes: "Discrete", "Hybrid" and "UMA graphics" (Intel Graphics), referring to which GPU('s) to turn on. The option "Hybrid" works well, but if you are experiencing issues with graphics performance you can try setting the "Discrete" option to disable the integrated GPU. This does come at the expense of the battery life.

## External monitors
The HDMI port is routed to the Nvidia GPU and the internal display is routed to the internal Intel GPU. To use the HDMI output the Nvidia driver or nouveau has to be installed.
There are two ways to use the USB-C ports as display outputs:
* Disable the Nvidia graphics in the BIOS setup (Advanced > Built-in device options > Graphics > UMA graphics). This allows the user to use the USB-C port as display output without the Nvidia graphics and without additional configuration. The HDMI port will be disabled in this mode.
* Use the "Hybrid" setting in the BIOS and configure Bumblebee as described below. This method allows the user to either use the HDMI port or the USB-C ports for display output purposes.

## Bumblebee
To make use of both the onboard graphics and the Nvidia GPU, install  (and add user to bumblebee user group and start ).
For an output on the ports connected to the Nvidia chip, the chip always needs to be powered on. To do this change the following options:

This prevents the NVIDIA chip from powering off after turning on.
Next edit the following:

Next a virtual output needs to be added to the Intel GPU.
Edit or create an entry for the Intel GPU:

That is all the configuration, now to enable external monitor:

  $ optirun true
  $ intel-virtual-output

It is recommended to put this in a script and create a desktop entry or similar to quickly enable the external display(s).

## Troubleshooting
## CPU throttling down under load
If your CPU throttles down under high load without reaching critical temperatures (e.g. >95°C) and you are absolutely sure the laptop is not overheating, install the  package by erpalma on GitHub. Start/enable .

This service overrides the package power limit every 5 seconds (30 on battery) by overriding default values in MSR and MCHBAR. A static fix for this problem has not been tested thoroughly. The default configuration works fine, refer to the GitHub page for more information.

## Framerate drops to 1 fps on discrete graphics
Refer to the Bumblebee troubleshooting page.

## Framerate drops to 1 fps when using external display
In certain applications, eg. Discord, Zoom and Steam, the fps drops to an unusable level when connected to an external display. This is an issue with vsync not working correctly. Try to disable vsync on the intgrated GPU. If that does not work you can try to disable vsync on the dGPU.

## Microphone not detected
If your internal microphone is not detected on boot you can force PulseAudio to detect it. See PulseAudio/Troubleshooting#Microphone not detected by PulseAudio.

## Brightness keys do not work
On some BIOS versions some of your functions keys, namely the brightness up, down and microphone mute keys, produce identical scan codes. You can try to update your BIOS to fix this. See for the bug report. If this does not work you can try to perform a [https://support.hp.com/document/ish_1997208-1551050-16 power reset (see This problem seems to be related to the HP Hotkey Service in Windows, that changes how the keys are handled (see [https://h30434.www3.hp.com/t5/Notebook-Operating-System-and-Recovery/Brightness-keys-not-working-in-Linux/td-p/7549927), so after you boot to Windows it might reappear.

## No sound output from two front speakers
Out of the box there is no sound output from the two front speakers. To solve this, use hdajackretask and change the following:

* Under codec > Conexant CX11970, press Show unconnected pins, and change for pin  the status to Override and set Internal speaker (LFE).
* Then press Install boot override and reboot.
* After this, specify Analog Surround 4.0 Output in sound settings.
