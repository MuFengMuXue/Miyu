# Lenovo Legion 7i

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Backlight || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Webcam ||  ||
|-
| Bluetooth || ||
|-
| Thunderbolt || ||
|-
| Keyboard || ||
|-
| Touchpad || ||
|}

For a general overview of laptop-related articles and recommendations, see Laptop.

## BIOS
At bootup, the BIOS settings page is entered via the  key.

In the BIOS settings, the model name can be seen in the Main tab, Secure Boot can be disabled from the Security tab and boot mode can optionally be switched between UEFI and legacy.

Advanced BIOS options can be accessed by going into more settings, hold down  and press each key horizontally from  to ,  to , then  to , let go of  and press . Click save changes and reboot into BIOS. Advanced settings will now be available.

There is no known option to disable the discrete NVIDIA GPU using the BIOS, there may be one present after unlocking the advanced options.

## NVMe Detection
You must manually change storage type from RST to AHCI in BIOS settings for Linux to be able to detect the NVMe drive.

## Undervolt
Undervolting is possible. Enter advanced bios, go to overclocking section, and enable XTU settings.  can be used now.

Undervolting levels vary between chips, the 10875H has been known to be stable around -100mV for CPU, -25mV for GPU, and -100mV for CPU Cache.

## Video
## Backlight
Backlight does not work with default kernel parameters. This problem may be solved by adding  to the list of kernel parameters.

if the above solution does NOT work then you can try this:

The only solution for now is to do it through the terminal
using the following commands:

to get the display Identifier so that you can send the brightness adjustment command:

 $ xrandr --output 0x43 --brightness 0.8

Where you can specify the brightness value between 1 and 0 using decimals(0.1, 0.2, 0.3, 0.5, 0.8, etc)

For example to place the brightness at 50% you can apply the following command:

 $ xrandr --output 0x43 --brightness 0.5

## Power Down Nvidia Card
Blacklist nouveau drivers, reboot, and run:

 # echo 'auto' >> /sys/bus/pci/devices/0000:01:00.0/power/control

## Multihead
External displays using the USB-C ports only seem to function using the proprietary NVIDIA driver.

## Power Management
Battery conservation mode is available. It will charge the device to 60% when charge falls below 50%, extending the life of the battery. It can be activated by running the following command:

 # echo 1 >/sys/bus/platform/drivers/ideapad_acpi/VPC2004:00/conservation_mode

## Keyboard
## Lights
Per-RGB keyboard lighting cannot be configured under Linux.  &  do not work to control the keyboard lighting.

## Touchpad
Single tap and double finger scrolling work. Multi gestures must be configured, they are detected with .

## Fan Control
Fan control only works with  or LenovoLegionLinux.

## Troubleshooting
## System hangs with BBSwitch
System hang occurs if bbswitch is used to shutdown the discrete Nvidia card. Do not use bbswitch, instead blacklist nouveau and use powertop or run:

 # echo 'auto' >> /sys/bus/pci/devices/0000:01:00.0/power/control

## Screen flickering
Screen flickers on a part of the screen. This problem may be solved by adding  to the list of kernel parameters, see NVIDIA for more information.

## EXT4-fs error after resume
If you get a error like EXT4-fs error (device nvme0n1p2): __ext4_find_entry:1532: inode #2102576: ... when suspending and resuming the system it seems the NVME cant be accessed. Hard-reboot and deactivate any hardware passwords/protections for this device in the BIOS settings.

## Known Issues
## Hinge Defects
Widespread issues with hinges breaking have been reported, especially the right side. There is no metal backing on the LCD side of the hinge, it is held in with glue causing it to become de-bonded over time. Extreme care is advised, warranty will not cover hinge issues.
