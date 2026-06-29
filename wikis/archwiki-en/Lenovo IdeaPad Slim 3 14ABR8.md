# Lenovo IdeaPad Slim 3 14ABR8

The following page was adapted from the Lenovo IdeaPad Slim 3 16ABR8

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Audio ||  ||
|-
| GPU (Integrated) ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
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
You can use the native wireless driver with  and  Kernel module parameter  in the  Kernel module is required in order for Wi-Fi to work.

For Bluetooth use  with  kernel parameter.

## Function keys
No dedicated keys. The  functions on the keyboard are recognized and should work.

## Fingerprint
You may use  or . The laptop can enroll but not verify fingerprints.

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

With that patch no other keyboard-related workarounds should be necessary (except maybe updating the BIOS), but if you want to avoid using that kernel module, there are other workarounds that at least partly fix the problems:

Adding the  kernel parameter, see keeps most of the keyboard functional after suspend, but the Fn/Multimedia keys and also the lid switch may continue to be broken.

If that does not work, make a script:

Remember to make it executable.[https://discussion.fedoraproject.org/t/keyboard-not-working-after-sleep-and-some-bluetooth-problems/161174/6
Note that the script likely will not fix the Fn-key and lid switch issues, but should at least make the rest of the keyboard usable after suspend.

Updating the bios is generally a good idea, see https://bbs.archlinux.org/viewtopic.php?pid=2251998#p2251998][https://bbs.archlinux.org/viewtopic.php?id=279102.
The patched kernel module has been tested with the latest BIOS (KYCN41WW), it's unclear/untested if it works with (all) older BIOS versions.

## EFI Boot Manager fills up
The EFI Boot Manager fills itself with old boot entries which need to be manually deleted after changing the OS. For that you can use .
