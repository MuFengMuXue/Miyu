# Lenovo ThinkPad P15 Gen 1

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Trackpoint || ||
|-
| Keyboard || ||
|-
| GPU (NVIDIA) ||  ||
|-
| GPU (Intel) ||  ||
|-
| Webcam
|

|
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader ||  ||
|}

## Discrete GPU
This model uses PRIME for combining the integrated and the dedicated GPU. As the external graphic ports are wired to the discrete GPU, drivers for the discrete GPU need to be present in order to use them. However, no special X.org configuration should be necessary, as xrandr should detect the ports automatically. If not, follow the instructions in PRIME#Reverse PRIME.

## Disabling discrete GPU
The built in GPU can be disabled and re-enabled on the fly. This can significantly reduce power consumption and increase battery life up to a factor of 5.

## Using bbswitch
Note that with this method, nouveau module must be completely unloaded to use bbswitch to disable the GPU. So it does not really allow for on the fly enable/disable when using a GUI.

First, in the UEFI settings, ensure the iGPU is enabled, in case you have disabled it earlier.

Then, boot Linux. Uninstall the nvidia and nvidia-open drivers. Reboot into nouveau. Next, if you have setup kms hook in mkinitcpio, remove that so that nouveau module isn't loaded early. Then, blacklist nouveau, and reboot the laptop. Then use bbswitch to disable the dGPU.

## Using acpi_call
This method is not recommended since it results in a hard freeze of the system which needs to be forcefully powered off using the power button. Use bbswitch method instead which does work reliably.

See Hybrid graphics#Using acpi_call, the specific ACPI call for this device is .

## GPU power consumption
With the nvidia proprietary drivers, the laptop's idle power consumption is pretty high at 16-17W.

With the nouveau drivers, the laptop idle power consumption drops all the way to 5W, or even less, resulting in significantly better battery life.

If you don't need to use the NVIDIA dGPU, using nouveau may be the better option.

Note that the HDMI port and Thunderbolt port display output will only work through the NVIDIA dGPU.

## Fan control
The default operation of fans is noisy, as they are basically at medium power all the time. The  program can be used to create a quieter operation, while retaining reasonable temperatures.

Here is an example  configuration:

## Enabling Turbo boost
By default, the CPU power governor does not allow CPU frequencies to reach turbo boost speeds. This can be fixed via, for instance, .

This can be changed by modifying the file :

Then start/enable .

## Firmware
This Device has fwupd support.

## Problems with s2idle/S0ix sleep mode
While s2idle/S0ix is supported by the hardware, it seems to assume that the laptop is only suspended by closing the lid. If you suspend using "systemctl suspend" or through a GUI menu, the laptop can't be woken up again using the keyboard, power button etc. and only closing and opening the lid wakes it up.

It is unclear if this is a Linux kernel/userspace bug, or a bug in the laptop firmware. Either way, it is buggy behaviour. It's recommended to use S3 suspend for now for more predictable behaviour.
