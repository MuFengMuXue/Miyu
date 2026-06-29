# Dell XPS 15z

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Bluetooth || ||
|-
| Touchpad || ||
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Webcam || ||
|-
| Card reader || ||
|}

## Hangs on boot
Sometimes when booting the laptop with the default kernel it would hang at uevent detection. To prevent this from happening, append the following to the kernel parameters:

 nox2apic

## Graphics
Dell XPS 15z has two graphics processors installed, Intel integrated graphics and NVIDIA GeForce GT 525M. The NVIDIA card is using Optimus technology.

See Intel for details on using the Intel GPU.

## Using Bumblebee
Another way, which allows to use Optimus technology is Bumblebee.

## Video Performance
Using the Intel card without any modifications can result in poor video performance. A quick fix is to edit boot options of your boot loader and append the following to the kernel parameters:

 i915.semaphores=1

## Boot time errors
If you encounter boot time errors with Intel graphics, add the  and  modules to  in :

Then regenerate the initramfs.

## Touchpad and keyboard
The touchpad is fully supported in kernels 3.9 and later. Make sure to install  as well as a program such as synaptiks so that you can customize all of the features.

## Keyboard is not working
In case your keyboard is not working after installing Arch, or after upgrading older installation append the following to your kernel parameters:

 acpi=noirq

As mentioned above, this problem should not occur in new installations, although may in some cases of customized installs.

## Card Reader
To make the card reader function enter the following command:

 # echo 1 > /sys/bus/pci/rescan

This will allow it to auto mount cards until the next reboot.
