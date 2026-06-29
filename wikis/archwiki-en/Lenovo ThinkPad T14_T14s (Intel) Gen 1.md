# Lenovo ThinkPad T14/T14s (Intel) Gen 1

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| TrackPoint || ||
|-
| Touchscreen || ||
|-
| GPU || ||
|-
| Webcam || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Wireless || ||
|-
| Mobile broadband || ||
|-
| Fingerprint reader || ||
|-
| Smartcard reader || ||
|}

This article covers the installation and configuration of Arch Linux on a Lenovo ThinkPad T14/T14s (Intel) Gen 1 laptop.

## Firmware
## Secure Boot
Deleting Secure Boot keys and installing your own keys (for example by using KeyTool) can brick the device on older firmware. This is a problem that is similar to one which has been reported on some other Lenovo laptops and is likely due to a faulty firmware. This has since been fixed. You must update your device firmware if you plan on enrolling secure boot keys through automated tools or you risk bricking your device. The only way to repair it is by replacing the mainboard of the device.

## Power modes
Lenovo Vantage software manages 3 power modes in Windows with Intel DPTF, they are managed through acpi calls:

* economy
* balanced
* performance

This can be managed graphically or in the command line with .

If you do not enable the performance mode, the GPU will throttle at 57 C and the CPU Mhz will be throttled too. Which makes applications stutter. So far, in a desk, using the performance mode while connected to the power supply was not a problem.

You may wish to set ACPI calls manually, for the ThinkPad T14 Intel, the ACPI calls are as follows:

{| class="wikitable"
| economy || \_SB.PCI0.LPCB.EC._Q6F
|-
| balanced || \_SB.PCI0.LPCB.EC._Q6E
|-
| performance || \_SB.PCI0.LPCB.EC._Q6D
|}

To enable ACPI method calls through , install the  kernel module. Install  if you are using .

Then call one of the ACPI methods above to enable a power mode. For example, run the following command to enable performance mode:

 # echo '\_SB.PCI0.LPCB.EC._Q6D' > /proc/acpi/call

The result of the call can be determined by examining the contents of . A successful call for the previous method is indicated by the following output:

You can check what is the throttling temperature in Celsius for the NVIDIA GPU if you want to make sure, note that you need the  package installed:

 $ nvidia-settings -q GPUMaxOperatingTempThreshold

An output of  or  means it is in performance mode.

## Intel Turbo Boost
Check that Intel® Turbo Boost Technology 2.0 is enabled using

 $ cat /sys/devices/system/cpu/intel_pstate/no_turbo

An output of 1 means it is not enabled, so you will have to reset your BIOS to defaults. After doing that, running the command again should print 0.
You should be able to see your CPU boosting way higher.

## Suspend
S3 suspend works, optionally you can set the Config > Power > Sleep to Linux in bios.

## Smartcard reader
Tested and confirmed to work with integrated Smart card reader Alcor Micro AU9540. Follow Lenovo ThinkPad T14s (AMD) Gen 1#Smartcard reader. Smart card must be inserted with the chip facing upwards.

## Audio
This laptop requires Sound Open Firmware in order for the soundcard to work.

## T14 links
* Product Specifications Reference (PSREF)
* Hardware maintenance manual
* User guide
* https://ubuntu.com/certified/202005-27918

## T14s links
* Product Specifications Reference (PSREF)
* Hardware maintenance manual
* User guide
* https://ubuntu.com/certified/202004-27845
