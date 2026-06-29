# Lenovo IdeaPad Slim 3 16ABR8

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Audio ||  ||
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Wi-Fi, alt. ||  ||
|-
| Bluetooth, alt. ||  ||
|-
| Webcam ||  ||
|-
| Touchpad ||  ||
|-
| Fingerprint ||  ||
|-
| TPM ||  ||
|-
| SD-card reader ||  ||
|}

## Installation
Before installing, disable Secure Boot in the BIOS. You can access the BIOS by pressing  at the Splash screen. The boot menu can also be accessed by pressing .

## Video
X works natively with a current  and .

If you are having video issues with only the  installed, also install the AMD PRO package . See AMDGPU.

## Wireless
Apparently there are 16ABR8 models with different Wireless solutions.

## Realtek 10ec:b852
You can use the native wireless driver with  and  Kernel module parameter  in the  Kernel module is required in order for Wi-Fi to work.

For Bluetooth use  with  kernel parameter.

## Mediatek MT7921 (14c3:7961)
With this one, WiFi works out-of-the-box on recent kernels.

(Bluetooth hasn't really been tested yet, but is available and uses the  driver)

## Function keys
No dedicated keys. The  functions on the keyboard are recognized and should work.

## Fingerprint
It seems that there are inconsistencies within the Fingerprint devices. This means, that either the official Lenovo Driver  or  should work.

For installation see fprintd.

## Power management
The following section was adapted from Lenovo IdeaPad 5 15are05.

Battery Conservation Mode is a feature that limits battery charging to 55-60% of its capacity to improve battery life, being most useful when the laptop tends to run on external power much of the time. It can be controlled with . With  or  it is possible to control both Battery Conservation and System performance modes.

## Kernel method
Set the  kernel module parameter.

To use without reboot:

 # rmmod ideapad_laptop
 # modprobe ideapad_laptop allow_v4_dytc=1

Restart . Now power-profiles-daemon can do everything below.

## System Performance Mode
There are 3 modes available: Intelligent Cooling, Extreme Performance and Battery Saving. To toggle it, you need to call some ACPI methods.

First install  (or  for LTS kernel,  for other kernels) and load the kernel module:

 # modprobe acpi_call

Set it to Intelligent Cooling mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x000FB001' > /proc/acpi/call

Set it to Extreme Performance mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0012B001' > /proc/acpi/call

Set it to Battery Saving mode:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.DYTC 0x0013B001' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.SPMO' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

As a result you get the value for the bit SPMO (either ,  or ).

 # echo '\_SB.PCI0.LPC0.EC0.FCMO' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

As a result you get the value for the bit FCMO (either ,  or ). To interpret the results the following table can be used:

{| class="wikitable"
! SPMO !! FCMO !! Mode
|-
| 0x0 || 0x0 || Intelligent Cooling
|-
| 0x1 || 0x1 || Extreme Performance
|-
| 0x2 || 0x2 || Battery Saving
|}

## Rapid Charge
Make sure you have set up .

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x07' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x08' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.QCHO' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for off and  stands for on.

## Battery Conservation
Similarly to the #Rapid Charge, make sure you have set up .

Turn on:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x03' > /proc/acpi/call

Turn off:

 # echo '\_SB.PCI0.LPC0.EC0.VPC0.SBMC 0x05' > /proc/acpi/call

To verify your setting:

 # echo '\_SB.PCI0.LPC0.EC0.BTSM' > /proc/acpi/call
 # cat /proc/acpi/call; printf '\n'

where  stands for off and  stands for on.

There is also an alternative way to control the conservation mode of the battery.

## Known issues
## Keyboard
The Keyboard and Lid Switch will be non-functional after waking up from suspend, this bug fixes itself after an reboot.

A kernel patch that seems to reliably work around this problem is waiting to be merged into the kerneluntil then you can build the patched  module out-of-tree, and install it with DKMS, get it and instructions at the [https://github.com/DanielGibson/amd_pmc-ideapad amd_pmc-ideapad repository

Even with that patch the problem might still occur when using timed resume ("wakealarm", like with rtcwake) - but normal suspend (via closing lid or suspending in a menu or  will work fine.

To work around issues with wakealarm, it makes sense to still set the  so you still have at least basic keyboard functionality after resume from a timed suspend (this will not impair keyboard functionality after a "normal" suspend+resume).

## Workarounds without patching the Kernel
Adding the  kernel parameter, see keeps most of the keyboard functional after suspend, but the Fn/Multimedia keys and also the lid switch may continue to be broken.

If that does not work, make a script:

Remember to make it executable.[https://discussion.fedoraproject.org/t/keyboard-not-working-after-sleep-and-some-bluetooth-problems/161174/6
Note that the script likely will not fix the Fn-key and lid switch issues, but should at least make the rest of the keyboard usable after suspend.

Updating the bios is generally a good idea, see The patched kernel module has been tested with the latest BIOS (KYCN41WW), it's unclear/untested if it works with (all) older BIOS versions.

## Battery
The battery level may be capped above 100% (e.g. with ) which can lead to confusion.

## Bluetooth
It seems pairing does not work correctly with . Try to connect to the Bluetooth device directly to pair with the device.

## Onboard devices
Sometimes one or more onboard devices get soft locked, although it rarely occurs. To solve this, use rfkill (from ):

 # rfkill unblock your_device

## Network Adapters not working
It seems external network adapters over the USB-C port do not work even if they did work on other Linux devices[citation needed.

It's unclear which devices exactly failed and/or if those issues have been resolved since, at least now several devices just work.

## EFI Boot Manager fills up
The EFI Boot Manager fills itself with old boot entries which need to be manually deleted after changing the OS. For that you can use .
