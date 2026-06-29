# ASUS X421IA

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Fingerprint sensor || ||
|-
| Camera || ||
|-
| Card Reader || ||
|-
| Bluetooth || ||
|-
|}

This article contains information about running Linux on the laptop ASUS X421IA which are known as ASUS Vivobook S14 M433 in Malaysia. The laptop are almost fully functional on Linux out of the box, requiring a few tweaks to meet a user's basic needs.

## Booting into Linux
## Secure boot
In order to boot Arch (or any OS not supporting Secure Boot), enter the UEFI parameters by holding  (or  key and then selecting "Firmware Setup"), then navigate with the keyboard arrows to the "Security" tab and set "Secure Boot" to Off.

## Fast startup
If you are planning to dual boot with Windows, it is advisable to disable Fast Startup in the UEFI menu at the "Boot" tab. For more information, see Fast Startup.

## Hardware
## Battery charge threshold
See Laptop/ASUS#Battery charge threshold.

## Limitation
## Suspend and Hibernation
Unfortunately, Suspend to RAM is not available in this model. The supported suspension methods are suspend to idle and hibernate. To wake from suspend, simply press any keyboard keys other than the power button. Note that suspend may not work consistently. See #Freezing issue.

## Fingerprint sensor
The fingerprint sensor (available to some models) are too small to be able to be enrolled and used successfully.

## Fan speed control
Full fan speed control is not supported in this laptop. Only  is available for the  driver which can be set to 2 for automatic and 0 for maximum fan speed (6000 RPM). See Fan speed control#ASUS laptops.

## Troubleshooting
## Freezing issue
Under certain circumstances (such as gaming or resuming from suspend), the screen may freeze and the user are not able to do anything except doing a force reboot. Before proceeding, make sure that the kernel, AMDGPU, AMD microcode and BIOS is updated.

## Gaming
 kernel: amdgpu *ERROR* Waiting for fences timed out!
 kernel: amdgpu *ERROR* ring gfx timeout, but soft recovered

If you encounter freezing and the above error log while gaming, try adding  to the kernel parameters. See freedesktop issue.

## Resuming from suspend
 kernel: amdgpu 0000:03:00.0: amdgpu *ERROR* IB test failed on gfx
 kernel: *ERROR* ib ring test failed

If you encounter freezing and the above error log while resuming from suspend (particularly when suspend time is longer), try adding  to the kernel parameters. See [https://bugzilla.kernel.org/show_bug.cgi?id=204241 kernel issue.

## Backlight brightness cannot be restored at boot
 Failed to start Load/Save Screen Backlight Brightness of backlight:amdgpu_bl0

If the backlight brightness cannot be restored at boot and is therefore always set to a value of 100% or (close to) 0%, you can add  as a workaround to the kernel parameters. See kernel issue.

## Tips and tricks
There are a few ways that can be done to improve the battery life and performance of laptop. In order to achieve this, see:

* BIOS update - It is generally recommended to update BIOS, as it usually brings performance, power-saving and security features.
* Power Saving - List of general recommendations to increase battery life.
* Improving performance - List of general recommendations to increase performance.
* SSD - Tips and tricks for Solid State Drives.
