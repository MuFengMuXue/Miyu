# Acer Predator Helios 300

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU || ||
|-
| Webcam || ||
|-
| Ethernet || ||
|-
| Bluetooth || ||
|-
| SD-card reader || ||
|-
| Audio || ||
|-
| Wireless || ||
|-
| TPM || ||
|}

## Installation
RAID mode is enabled by default. AHCI mode must be used, otherwise the disks will be invisible. Secure boot and fast startup must be disabled as well for Arch to boot if Windows is present on the system.

Changing the storage mode from RAID into AHCI may be challenging as the BIOS does not list the options to do so by default. Going into the main tab in the BIOS menu, and pressing () should bring up the relevant options.

## Accessibility
The appearance of the BIOS is simple and not too colorful.

This device has a diagnostic LED which may visualize beep codes in some cases. See the "Diagnostic LED" section in the service manual for more details.
The service manual also contains shortcuts which are needed to trigger certain features, such as the boot menu and settings ().

## Firmware
fwupd does not support this device.

## Secure Boot
The BIOS does not accept .auth files.

## Bluetooth
Bluetooth works out of the box.

After suspending, Bluetooth may stop working. Restart  to fix it.

## Power buttons
This device has two detected power buttons and one sleep button.

In this case,  () is the "real", physical power button. You can verify this by inhibiting the handling of the power button
 # systemd-inhibit --what=handle-power-key sleep 1h
and recording the events:
 # stdbuf -o0 evemu-record /dev/input/event3 > event3

Pressing the power button should log an event.

The other detected power button seems to be a virtual, firmware-handled button. This power button will be triggered when your device runs out of battery.
The firmware will send many power button presses, so your machine will most likely only take a few seconds to power off because systemd kills the process/unit it is waiting for when the power button is pressed.

Holding the physical shutdown button for more than three seconds will force the system to shutdown.

See  for more information on handling specific keys.

## Sleep button
There is also a sleep button/suspend key. It is a virtual, firmware-handled key and will be triggered when using an unmarked keybind, which would suspend your device.
Use this to inhibit the handling of the suspend key.

## Kernel
Appending  to the kernel parameters is recommended if you are planning to use the installation for penetration-testing as the wireless adapter names will be quite long by default.

## Wireless
The integrated wireless chip works fine under normal conditions, monitor mode is supported out of the box, although injection is not.

## GPU
Rendering of the windows can be handled by the integrated Intel-graphics, and it is recommended to not install Nvidia drivers if unnecessary as functions such as; booting up, connecting a second monitor, battery life and overall system-stability will greatly suffer.
