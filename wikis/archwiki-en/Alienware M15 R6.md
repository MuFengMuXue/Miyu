# Alienware M15 R6

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Wi-Fi || ||
|-
| Bluetooth || ||
|-
| Touchpad || ||
|-
| Audio || ||
|-
| GPU (Intel) || ||
|-
| GPU (NVIDIA) || ||
|-
| Webcam || ||
|-
|}

While Arch Linux works out of the box on this laptop, this page contains recommendations for running it on the Alienware M16 R6 (2021). With some configuration almost all the hardware is well supported. Exceptions are the lighting, S3 state of suspend and anything above 60Hz on supported built-in panels.

## Firmware
The BIOS settings can be accessed by repeatedly pressing the F2 at boot. In here, the SATA Mode is, by default, at "AHCI" and hence needless to modify. If at all you have tinkered with this option, reverting back to "AHCI" is a must for installing Arch.
* If dual booting with an existing Windows installation, Windows may not boot after the change but this can be fixed without a reinstallation before changing the mode
* Change Fastboot to "Thorough" as it prevents intermittent boot failures
* Disable secure boot to allow Linux to boot

Installation of Arch Linux can proceed normally. Refer to the installation guide for more information.  detects the NIC without any workaround; Wi-Fi and LAN work out of the box.

## Suspend and Hibernate
## Suspend
The popular S3 state of suspend is not supported as, unfortunately, Dell has excluded it at a BIOS level on the newer notebooks.

See Power management/Suspend and hibernate#Changing suspend method.

## Hibernate
Hibernation is the best alternative to combat the absence of S3 state of suspend and can be achieved by simply setting up and configuring a swap file. The major advantage here is the 0% power drain over time.

## Input
While the trackpad works perfectly out of the box with the libinput driver, the keyboard has a few quirks.

## Keyboard
* Windows key lock (Fn+Super) and function lock (Fn+Esc) work perfectly
* F1 for performance mode works perfectly; fans max out
* F12 for disabling the trackpad is nonfunctional but it can be assigned a shortcut
* Hardware mic mute is nonfunctional as the kernel does not, as yet (), recognize its scancode but then again can be remapped to another key

## Audio
The audio card requires Sound Open Firmware.

## Video
Though the Intel and Nvidia GPUs Optimus#Available methods can work independently, they are fully functional through Optimus despite the BIOS indicating no support for hybrid mode.

## DisplayPort and HDMI
The DisplayPort, accessible via the type-C port at the back, is wired directly to the Intel GPU and hence can output video even with a completely disabled Nvidia GPU. This is the default configuration and works out of the box.

The HDMI port  is wired directly to the Nvidia GPU and hence requires an NVIDIA driver. Nonetheless, the power drain will be prodigious and disabling the Nvidia card altogether is also not an option, in which case there will be no video out through HDMI.

There is no way to get output from the Nvidia GPU through the type-C port and from the Intel GPU through the HDMI port even with Optimus configured perfectly.

## Lighting
Presently, there is no third party support for the lights although there is a good issue to track on the akbl repository.
