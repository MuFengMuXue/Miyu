# Lenovo IdeaPad 5 Pro 14ACN6

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth (Intel AX200) ||  ||
|-
| Bluetooth (Foxconn) ||  ||
|-
| Wireless (Intel AX200) ||  ||
|-
| Wireless (MediaTek) ||  ||
|-
| Webcam ||  ||
|-
| GPU ||  ||
|-
| Touchpad || ||
|-
| SD card reader ||  ||
|-
| Audio ||  ||
|}

The Lenovo IdeaPad 5 Pro 14ACN6 is a laptop computer with a 14" screen, AMD Ryzen™ 5/7 5000 U-Series Processor, 8GB/16GB of memory, webcam (with IR), dual-array microphone, stereo speakers, Bluetooth 5.1 and WiFi 5 or 6. It can be configured with a 2.2K matte or touchscreen display at 60Hz and 300 nits of brightness, or a 2.8K matte screen at 90Hz and 400 nits of brightness.

The available ports are:
* 1x USB 3.2 Gen 1 Type-A
* 1x USB 3.2 Gen 1 Type-A (Always On)
* 1x USB 3.2 Gen 1 Type-C (data transfer and Power Delivery 3.0)
* 1x USB 3.2 Gen 1 Type-C (data transfer, Power Delivery 3.0, and DisplayPort 1.4)
* HDMI 1.4b
* Headphones / microphone combo jack
* SD-card reader (SD, SDHC, SDXC, MMC)

All hardware works out of the box as tested with kernel 5.17.

## Installation
The device comes preloaded with Windows. It can be used to update the BIOS through the Lenovo Vantage app before installing Arch. Disable Secure Boot in the BIOS.

## Issues
## Suspend issues (S3 sleep fix)
Suspending works once the necessary BIOS settings are adjusted.

## About issue
By default the laptop comes configured for "Modern Standby", a Windows feature that is similar to modern smartphones deep sleep (allowing the devices to remain connected to the network and pull for information like new emails etc).

This does not work properly on Linux and will manifest as the device immediately exiting stand-by after you try to suspend it. You can also see it based on the power LED on the right hand side, it will be on instead of blinking.

## Solution: Enabling S3 sleep on advanced BIOS
* Turn off OneKeyBattery mode in BIOS setup, if it is enabled, and save the BIOS settings, and power down the device.
* Follow the instructions to enter the hidden/advanced BIOS

You will find the Modern Standby feature in the AMD PBS menu, about 3/4 of the way down. Change this setting to S3 Enabled, save and exit.

## Internal Microphone
If the internal digital microphone is not detected out of the box, adding  to the kernel parameter does the trick after rebooting.

## Power management options
## Rapid charge
First install  (or  for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' > /proc/acpi/call

You can also use ideapad-perf to control both the System Performance and the Battery Conservation mode through the CLI or with the provided tray applet.

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
fwupd does not officially support this device. It cannot be used to apply UEFI firmware updates.

## Accessing the BIOS
The BIOS can be accessed by pressing the  or  key while turning on the device.

## Hidden BIOS menus
A number of advanced BIOS menus are available that allow for significant tweaking of the device. Do not touch these setting unless you know what you are doing.

* Boot the laptop with  pressed to get into BIOS.
* Under Configuration menu, disable "HotKey Mode" and "OneKeyBattery".
* Switch language to Chinese.
* Save settings and power down the laptop.
* Type, with the laptop powered off:      .
* Get into BIOS as usual, you will get into the BIOS but with a few options more unlocked.
If you do not get a number of extra menus in the sidebar, you either mistyped the combination or did it too slowly. Power off the device and try again.

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
|  || 4 ||  || Opens Lenovo Vantage on Windows, broken on Linux
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggle keyboard backlight
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
# Emits  alongside  if Fn is not held, regardless of Fn lock state. If Fn is held, only emits .
