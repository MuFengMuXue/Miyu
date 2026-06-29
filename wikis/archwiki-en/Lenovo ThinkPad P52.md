# Lenovo ThinkPad P52

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Wireless || ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad || ||
|-
| Webcam ||  ||
|-
| Card reader ||  ||
|-
| Fingerprint reader ||  ||
|}

The Lenovo P52 is a quad or hex core Intel 8th generation Laptop.

## Installation
Make sure to update your BIOS to V1.17 or later (current is v1.24 as of March 2019). Earlier versions of the BIOS may become inoperable if you select certain settings:

# Hybrid vs discrete graphics - https://forums.lenovo.com/t5/ThinkPad-P-and-W-Series-Mobile/P52-won-t-start-after-change-to-only-discrete-graphic-card/m-p/4265065
# Thunderbolt 3 Support - https://forums.lenovo.com/t5/ThinkPad-P-and-W-Series-Mobile/Lenovo-P52-bricked-by-selecting-BIOS-thunderbolt-support-for/td-p/4207538?page=12

## Graphics
This laptop has its external display ports directly wired to the NVIDIA chip. In loose terms this means that the dedicated GPU must be enabled in order for external displays to be used. Luckily, it is possible to do dynamic switching between the integrated and dedicated graphics, but this is only possible by using the Intel DDX driver  as opposed to modesetting.

The laptop can be used in one of two modes: Hybrid Graphics, or Dedicated Graphics only.

In order to use the integrated Intel UHD 630 GPU (as part of Hybrid Graphics) you need to add the  module to your  by adding it as a module in your mkinitcpio. This is done by setting the following on :

Failure to add the above will leave you stuck when trying to load the  and your system will not be able to boot.

It might be possible to make do without the module above by using the  only (this can be done by changing the setting in UEFI).

## Proprietary driver with bumblebee
With this setup the integrated GPU is used by default but some applications can be rendered on the discrete GPU with the  or  launchers. See Bumblebee for detailed instructions. The lack of proper v-sync support means that with this method applications rendered on the discrete GPU exhibit tearing. There is also some overhead introduced as a result of moving data inefficiently between the discrete and integrated GPUs, but the Nvidia GPU performs much better than it does with Nouveau.

To get this working you will need , ,  and .

Then set the following configuration files.

(you probably already have one of these so adjust/add as needed - the dummy device at the end is essential!!):

At this stage, restart your machine. Then you should be able to run applications on the GPU as you normally would with , e.g., . If you want to use the external displays you need to keep your GPU on by running a task on  and then running  (this will stay running and binds the external display ports to virtual outputs that you can use). At this stage you should be able to see and use the external ports.

## Fingerprint reader
See Lenovo ThinkPad T480s - it works with  but not with libfprint.

## Touchpad
Every once in a while Linux kernel upgrades will cause issues where the Touchpad and Trackpoint stop working. Booting with kernel parameter  seems to fix it.
