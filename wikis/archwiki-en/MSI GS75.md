# MSI GS75

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Thunderbolt ||  ||
|-
| Audio ||  ||
|-
| SD Card Reader ||  ||
|}

The MSI GS75 Stealth (9SF) is an Intel architecture American Megatrends Inc. notebook with an Intel i7-9750H CPU and an NVIDIA Turing 20XX Q GPU.

* HDMI ports are directly wired to the dedicated GPU, Thunderbolt Type-C is not.
* The Intel integrated GPU (iGPU) is directly wired to the notebooks screen (EDP-1).
* The NVIDIA GPU (dGPU) is directly wired to the external HDMI port.
* Thunderbolt is wired to its own controller, but is somehow attached to the power state of the NVIDIA GPU.
* Thunderbolt firmware can be updated via BIOS, but the process is dangerous and can brick the machine.
* Native Microphone comprises two mono microphones that need to be managed for stereo-input and noise reduction.

## Installation
It is best to to enable factory default settings in the UEFI before installing. This will disable Secure Boot and provide sane settings for the CPU/GPU/PCH/EC. Resetting is not required, but this suggestion exists due to the complexity of advanced options and the configuration of PCIe on this model.

## Firmware
* Enter UEFI configuration:
* Select BOOT Device:

This laptop has advanced UEFI settings if desired.

## fwupdate
MSI provides firmware binaries for both the UEFI and Embedded Controller (EC). These files can be found at https://www.msi.com/Laptop/GS75-Stealth-9SF/support .

System firmware (EC) can be updated via , but the UEFI cannot.

## Keyboard
## Backlight
Keyboard brightness works out of the box with .

The lights on the keyboard cannot be configured with , because this tool only works with region-based RGB lighting. For this laptop model, the tool  provides partial control.

## Function keys
The airplane mode key combination () is disabled by default. Adding the following kernel parameters activates airplane mode key combination:

 acpi_osi=! acpi_osi="Windows 2009"

## Touchpad
Multi gestures do not work out the box, but are detected with .

## Thermals
Control the fans with . It will only work after enabling  by adding the following to your kernel command line:

 ec_sys.write_support=1

## Microphone
This notebook has a microphone array which provides stereo input. Noise reduction, echo cancellation, noise suppression can all be done via beamforming. To get the best of it add:
