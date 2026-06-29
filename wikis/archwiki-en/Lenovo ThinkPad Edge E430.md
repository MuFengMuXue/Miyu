# Lenovo ThinkPad Edge E430

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU || ||
|-
| Ethernet || ||
|-
| Wi-Fi || ||
|-
| Bluetooth || ||
|-
| Audio || ||
|-
| Webcam || ||
|-
| Fingerprint reader ||  ||
|-
| Card Reader || ||
|}

The following is regarding the Lenovo Thinkpad Edge E430 with 3rd Generation Ivy Bridge Intel processor, released in mid 2012. The E430 is intended to be an affordable, yet still entirely capable business machine. This article is meant to suppliment the current Installation guide.

## Ethernet
The Realtek RTL8111/8168B ethernet controller may be relatively unreliable with the r8169 module. Better Ethernet connectivity can be achieved with the  module. See Network configuration/Ethernet#Realtek RTL8111/8168B for instructions.

## Wireless
If the Thinkpad in question has the Thinkpad branded Wi-Fi adapter, it semi-works out of the box. There may be a delay preceding any attempted network activity, which can be resolved by disabling the power saving feature. The usual

 # ip link interface power off

is not a feature of this particular card. Instead, the over aggressive power saving feature may be turned off upon loading the module on boot.

This may be achieved with the following kernel module parameter:

 rtl8192ce.fwlps=0

This will turn off the firmware lowpowerstate or fwlps.

Because Lenovo is one of a few companies that whitelist wireless cards, replacing/upgarding can be challenging, costly, or just downright impossible. To find what FRU (Field Replaceable Unit) this machine accepts, go to the Lenovo support site where you should be able to find the necessary documentation.

If you failed to realize that the wireless card was a horribly supported Realtek, and you are now kicking yourself because of the above mentioned whitelist, you do have an option to change it without ordering a Lenovo specific card. Some kind souls are willing to help others modify their BIOS' in various ways, one of which is removal of the whitelist. See thread where Serg008 was able to remove the whitelist for the E430. If you go this route, proceed with caution, as upgrading the BIOS (and messing up) can render your machine a brick. Also, there are legitimate warranty concerns with unauthorized BIOS modifications.

## Fingerprint reader
Typically with older hardware, one can get the fingerprint reader to function by using one of two open-source fingerprint reader projects. They are ThinkFinger and fprint. Alternatively, Ubuntu has put together a system that includes drivers included in these previous projects, as well as including proprietary drivers for the newest models. In typical Ubuntu fashion, it is gui driven and appropriately named .

The fingerprint reader included on the newest generation of Thinkpad E430 is a Upek. To verify the model of the device in a given machine, one may use lsusb.

## Trackpoint
See TrackPoint.

## Fans
Thinkfan may be used to control the fan speed. This is probably not necessary as the BIOS seems to typically handle the fan speed just fine.

The  kernel module needs to be configured so user space programs can control the fan speed.

The thinkfan configuration file also needs to know how to set the fan speed. Replace the default sensor settings with the following.

Direct fan control can be achieved by using "echo" to apply the desired level. Set the speed as shown in the following examples:

 # echo engage > /proc/acpi/ibm/fan
 # echo level auto > /proc/acpi/ibm/fan
 # echo level 1 > /proc/etc/ibm/fan

Once thinkpad_acpi has been loaded with , available settings can be displayed like so:

 $ cat /proc/acpi/ibm/fan
