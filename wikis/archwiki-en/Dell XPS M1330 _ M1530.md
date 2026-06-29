# Dell XPS M1330 / M1530

Dell XPS M1330 and the larger M1530 are laptops sold from 2007 to 2009. They work quite well out of the box with Arch and GNU/Linux in general.

## CPU
The CPU is either Intel Merom or Penryn. Despite their age, they are both x86_64 and thus supported by Arch. Remember to install  for full stability.

## BIOS
The last BIOS revision for this product was A15. You can see which version is in use on the startup screen. The best way to update to the last version is through Windows Update (on a still-supported version of Windows).

Alternatively, the BIOS can be updated in Arch using FreeDOS. Download the Dell image (M1330A15.EXE or M1530_A12.EXE) and follow the instructions given here.

## Network
## Ethernet
The ethernet interface is made by Broadcom. The  kernel module should load automatically. To use it, install and enable your preferred network manager (see Network configuration).

## Wireless
Make sure the wireless interfaces are unblocked.

Wi-Fi and/or Bluetooth can be turned on/off with a hardware switch located on the right-hand side of the laptop. The functionality can be changed in the BIOS settings.

## Wi-Fi
See Wireless network configuration for details.

M1330 and M1530 were shipped with many different Wi-Fi chipsets. Check which one you have with .

* Intel chipset: 3945abg or 4965agn
The correct kernel module should load automatically.

* Broadcom chipset: bcm43xx'
You may try installing the broadcom-wl driver first. The  module should load on boot.

If this fails, your only option is to use the b43 driver and associated firmware. The  module loads automatically but the  module needs to be enabled manually. Performance will not be great.

## Bluetooth
Some units include a Bluetooth card. The correct kernel module should load automatically. To use it, install the  package (if not already present) along with additional packages mentioned in relevant articles. Then enable .

## Graphics
Most units were shipped with an Nvidia 8400M-GS card (G86M). It is no longer properly supported by the proprietary NVIDIA driver. You have two options:

* Use kernel mode setting (works out of the box)

* Install  (small improvement)

Performance will not be great. Expect frequent freezes under moderate loads.

## Sound
Sound works very well with PulseAudio. Simply install the necessary packages if not already present.

If you prefer pure ALSA, be sure to unmute all channels. To get the microphone working, you may have to change the digital input source.

## Touchpad
The Synaptics-made touchpad works well with libinput which is included with most desktop environments.

## Extra media keys
The media buttons are detected automatically by udev. The MediaDirect (house) button can be reassigned for any purpose.

## Fingerprint reader
Some units include a fingerprint reader made by SGS Thomson Microelectronics. It should work with the generic fprint driver. If not try the manufacturer-supplied ThinkFinger driver.

## SD Card Reader
The device is recognized by the kernel. The adapter module is .

The card will be available for mounting under the device

## Webcam
See Webcam setup for details.

Most units are equipped with a webcam, If it is not working, run the built-in diagnostics (available by pushing 'F12' during the POST screen, then selecting 'Diagnostics').

## Sensors / Hardware info
Install i8k packages: .

This will provide many useful information (temperature, fan speed, BIOS...) and utilities (fan monitor, BIOS update...). For CPU temps, use lm_sensors.

## Hard Drive
If the hard drive clicks regularly, it may be suffering from this problem.
