# Lenovo IdeaPad Flex 5 14ARE05

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| Wi-Fi ||  ||
|-
| GPU ||  ||
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Fingerprint reader(Egis) || ||
|-
| Fingerprint reader(Goodix) ||  ||
|-
| Fingerprint reader(Synaptics) ||  ||
|-
| SD card reader ||  ||
|-
| Audio ||  ||
|-
| Accelerometer || ||
|}

The Lenovo IdeaPad Flex 5 14ARE05 is a convertible 2-in-1 laptop computer with a 14" screen, AMD Ryzen™ 3/5/7 4000 U-Series Processor, 4GB/8GB/16GB of memory, webcam, microphone, stereo speakers, headphone / microphone combo jack, 802.11ac wireless card with Bluetooth 5.0, 1 x USB-C 3.2 Gen 1 Type-C(supports charging), 2 x USB 3.2 Gen 1 Type-A, 1 x SD card reader, 1 x HDMI 1.4b, 1 x power connector, and a fingerprint reader.

## Installation
Before installing, disable Secure Boot in the BIOS. You can access the BIOS by pressing  during boot. The boot menu can also be accessed by pressing .

## Accessibility
## Issues
* HDMI sound suffers from the PulseAudio limitation described in PulseAudio/Examples#Simultaneous output to multiple HDMI / DisplayPort outputs. The workaround described there works (manually setting the  in ).
* Errors with pointer devices when flipping/rotating the screen manually with randr.
* In kernel 5.12 keyboard backlight support was added to the  kernel module but it does not seem to properly support the multiple keyboard backlight brightnesses provided by the keyboad (off|dim|bright). This can cause problems setting keyboard brightness with software.
* Occasionally the touchscreen and touchpad do not work after boot. The workaround for this a reboot. The cause and fix is unknown. The dmesg log is below:

* The  fingerprint sensor is not supported out of the box by libfprint. To work around this, you can use  along with , to get this fingerprint reader working.

## Touch screen setup
The touchscreen and pen is recognized by the input-wacom driver. For setup information look at Wacom.

## Tablet/Laptop mode
Install  to get device recognition for the lid switch. This creates the device , on which  or  can act.

## Power management options
## Rapid charge
First install  (or  for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' > /proc/acpi/call

Turn off:
 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' > /proc/acpi/call

## Battery conservation mode
This device supports battery conservation mode.

## Kernel method
Turn on:

 # echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

Turn off:

 # echo 0 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

## ACPI method
First install  (or  for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x03' > /proc/acpi/call

To verify your setting run the command below, you should get 1:

 $ cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

Turn off:
 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x05' > /proc/acpi/call

To verify your setting run the command below, you should get 0:

 $ cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

## System performance mode
There are 3 modes available: Intelligent Cooling, Extreme Performance and Battery Saving.

## Kernel method
To list available options run the command below:

Set it to Intelligent Cooling mode:

 # echo 'balanced' > /sys/firmware/acpi/platform_profile

Set it to Extreme Performance mode:

 # echo 'performance' > /sys/firmware/acpi/platform_profile

Set it to Battery Saving mode:

 # echo 'low-power' > /sys/firmware/acpi/platform_profile

## ACPI method
First install  (or  for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

Set it to Intelligent Cooling mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x000FB001' > /proc/acpi/call

Set it to Extreme Performance mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0012B001' > /proc/acpi/call

Set it to Battery Saving mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0013B001' > /proc/acpi/call

## Firmware
fwupd does not officially support this device but it can still be used to apply uefi firmware updates.=== Updating bios ===

## Pre update
* Install the ,  and  packages.
* Download bios update exe file.[https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/flex-series/flex-5-14are05/downloads/driver-list/component?name=BIOS%2FUEFI

## Procedure
Run the following commands:
* Extract the bios  file:
 $ innoextract file.exe
* Get the GUID number of your system firmware for the next step. You should get something that looks like example below:
{{hc|# fwupdmgr get-devices|
system-firmware type, {e20bafd3-9914-4f4f-9537-3129e090eb3c} version 22315982 can be updated to any version above 22315981
device-firmware type, {e3be8073-66a6-4bf6-966a-c0d58b486c40} version 1 can be updated to any version above 0
device-firmware type, {c85ba1bc-54a7-4aab-9337-eed4746bf09f} version 0 can be updated to any version above 4294967295
}}
* Schedule the update for the next system reboot, using extracted  file:
 # fwupdtool install-blob /path/to/file.cap e20bafd3-9914-4f4f-9537-3129e090eb3c

* Reboot if there are no errors.
* Enter the bios settings and move  to the first option in the Boot Priority Order menu.
* Save and exit and the update should begin.

* When the update completes it will boot into the boot menu. At this point it is safe to interact with the device again.

## Post update
* Disable secure boot in the settings to be able to boot into Linux.
* If your boot loader is not detected, boot into a usb with Arch and use  to reinstall your boot loader or use  to create a boot entry.

## Secure boot
This device supports custom importing keys using ().

## Lenovo diagnostics
The Lenovo diagnostics can be accessed by pressing  during boot. The Diagnostics contains tests for the motherboard and memory. Results of the tests can be stored onto a USB stick.

## Firmware settings
## AMD PSP
The AMD Platform Security Processor setting in the firmware can be used to disable or enable TPM functionality.

## Disable built-in battery
This option temporarily disables the battery for servicing(e.g. changing ssd). To enable the battery again, connect the charger to the device.

## Accessing the bios
The firmware settings and boot menu can be accessed by pressing the novo button(located on the right side of the headphone jack) with a pin or paperclip when the device powered off.

## Power management in firmware
The System Performance Mode Option can be set to Extreme Performance, Intelligent Cooling, Battery Conservation. These settings can also be controlled from the OS, see #System performance mode.

## Issues
## OneKeyBattery bug
There is a bug with the OneKeyBattery setting which can cause problems powering on the device. It effects bios versions older than eecn25ww. To fix this, disable the OneKeyBattery setting in the bios or update the bios to version eecn25ww or newer.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Enables Fn lock
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || 3 ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Opens Lenovo Vantage on Windows wich is not usable on Linux, even that, it does weird things.
|-
|  ||  ||  ||
|-
|  ||  ||  || Changes keyboard backlight brightness
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}
# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# systemd-logind handles this by default.
