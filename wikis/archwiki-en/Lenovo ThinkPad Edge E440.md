# Lenovo ThinkPad Edge E440

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Graphics || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Camera || ||
|-
| Card Reader || ||
|-
| Bluetooth || ||
|-
| Fingerprint scanner || ||
|}

## ClickPad
The only tweak you may want is to resize active area. With default config, you can cosily use as pointer only top 1/3 of ClickPad. See Touchpad Synaptics#Buttonless touchpads (aka ClickPads) for instructions.

## Keyboard
 and  keys can be swapped in BIOS.

 lock can be switched with .

## Backlight
Backlight control works with multimedia keys (/).
To configure brightness level on startup see Backlight#Udev rule.

## Audio
Default configuration could point to non-existent device because numbering of HDMI devices does not start with 0. Suggested solution is to set PCH device to default by placing a configuration file into . The following thread contains alternative solutions and detailed
instructions: Fixing ALSA device selection.

## Troubleshooting
## With Fn and Ctrl_L keys swapped, Ctrl_L+s hotkey is mapped to Alt_L
Lenovo Forums topic

Issue is present on notebooks with BIOS versions older than v2.16.
Problem can be solved with a BIOS update up to v2.16 or newer. See the BIOS v2.16 update changelog.

## Blinking power LED after resume from suspend
This is not a real problem, but can be annoying and has a very simple solution:

 # echo "0 on" > /proc/acpi/ibm/led

For automation, create a script depending on the used power management tool.

## BIOS Update
Steps below were tested by contributors of this page and work perfectly. However, do the following procedure at your own risk!

To update the BIOS from a USB drive, follow these steps (alternatively, you can download the ISO, burn it to a CD, and then boot from the CD):

# Download the latest firmware from the official E440 Downloads page (search for "BIOS Update (Bootable CD) for Windows").
# Install the  utility.
# Convert ISO image:
# Write the image to the USB drive. Suppose, your drive is . Warning: all information on USB stick will be lost!
## Unmount all partitions associated to the drive (perform for every existing 'X'):
## Write image:
# Reboot you PC and boot from your USB drive.
# FOLLOW ALL INSTRUCTIONS written in the update utility!
