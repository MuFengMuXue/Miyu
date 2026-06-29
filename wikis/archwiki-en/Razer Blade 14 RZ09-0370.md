# Razer Blade 14 RZ09-0370

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard ||  ||
|-
| GPU (AMD) ||  ||
|-
| GPU (Nvidia) ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|}

This page contains information about the Razer Blade 14 RZ09-0370 (mid 2021) the first Razer Blade notebook to have an AMD Ryzen processor. Currently the information on this page corresponds to the RTX 3070 and RTX 3080 QHD 165 Hz display versions, but should apply to other versions.

## Installation
In order to boot into the installation it is important to disable modesetting by adding  to the kernel flags. Disabling only the nouveau modset using  can work but is unstable.

You can also opt to install while running the proprietary nvidia drivers.

## EFI system partition
The computer comes with an EFI system partition from the factory that is used by Windows. The partition is only 100 MiB in size and can cause problems holding both a boot loader and Arch kernels. Resize this partition, create a new EFI system partition, or reformat the disk before installing.

## Accessibility
The appearance of the BIOS is pretty simple and not very colorful, so it might work well with OCR software.

The BIOS can be navigated via the keyboard.  and  to select the screen,  and  to select an item.  can be used to enter a menu or change an option.  and  can be used to change options directly without open a dialog.  can be used to load defaults.  save and exit.

The keyboard layout defaults to QWERTY in the BIOS even if the computer itself has a different keyboard layout. For example with the AZERTY version, keys such as  must be accessed using  instead of the regular  key.

## Firmware
fwupd does not support this device.

Razer statement on the LVFS website: Updating firmware is only supported on Windows

## Secure Boot
The BIOS does not seem to support custom keys.

## Battery Life
## nVidia+AMD Hybrid Graphics Battery Drain
If you experience very poor battery life compared to Windows, even after implementing Powertop (which sometimes misidentifies dGPU power use as iwlwifi, bluetooth or webcam power use), TPL and cpupower-gui recommendations, try reverting back to the nvidia525 drivers instead of the nvidia535 drivers; the 535xx series have a known bug which does not properly power down the dGPU even when the iGPU is set to integrated.

## Webcam power drain
The webcam is consuming power regardless of whether it is in use or not as seen in powertop. The recommended methods for disabling the webcam work to disable the webcam but power drain remains constant. Those methods include added blacklist uvcvideo to /etc/modprobe.d/blocklist.conf and echo usb-id > /sys/bus/usb/drivers/unbind.

## Bluetooth
Bluetooth works out of the box, however Bluetooth mice experience lagging and hangs when the laptop is running on battery power and/or under load.

## Audio
The integrated speakers work perfectly. The microphone array works perfectly. The headphone jack produces a muffled (only high frequencies), low volume and apparently mono output. Tested with the 5.12 kernel.

As of Kernel 6.4, the headphone jack still does not work. It produces very low-quality, low-volume unusable sound. Speakers and Bluetooth headsets do work fine, however.

## Backlight
The backlight controls do not work after installation and is caused by a bug in amdgpu driver. As suggested in the OpenSUSE forum, adding the  kernel parameter would solve the issue.

To make systemd save and load brightness settings after restarts, one may need to enable

## HDMI Port
The external HDMI is bound to the discrete NVIDIA GPU. Reverse PRIME can be used to allow for using the iGPU for rendering.

## RGB
The keyboard RGB lights can be controlled using . The logo illumination can be controlled using  logo-control.
