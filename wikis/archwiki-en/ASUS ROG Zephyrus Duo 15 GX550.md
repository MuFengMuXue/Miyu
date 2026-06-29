# ASUS ROG Zephyrus Duo 15 GX550

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Trackpad || PS/2 ||
|-
| Keyboard ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|}

## Installation
GX550 comes with a couple of different configurations, so please pay attention to your specific hardware while trying to install it.It comes with dual PCIe-SSDs configured with intel Rapid Storage Technology; i.e. RAID level 0 (Striping). Default operating system is Windows 10 installed in UEFI. Installing Arch will require a complete format / re-partitioning of the disks.

The NVIDIA graphics cards in this model currently does not seem to work with `nouveau` at all, which means there may be boot freeze's while trying to boot from the default ArchISO, which uses nouveau. best workaround for this would be to completely diable the nvidia gpu and use only intel graphics until installation is complete; or to build a custom archiso with nvidia binary drivers bundled instead off nouveau.

Once you have obtained a bootable copy of Arch, Start the installation with the following steps.

# Disable Intel Rapid Storage Technology and change SATA configuration to AHCI from the Asus UEFI BIOS.
# Boot from a "Bootable Arch USB Device" in UEFI mode.
# Format/Partition both SSDs on the device.
# Reboot to the "Bootable Arch USB Device".

Now, proceed with the standard Installation guide.

## Firmware
fwupd does not support this device yet.

## Hardware
See for a hardware probe of this device.

## Screenpad
The Asus Screenpad gets recognized as a second monitor (with touch-enabled) by default. The Touch functionality will be uncalibrated by default and the touch-input is mapped to both the main monitor and screen pad. The Special Screenpad button on the keyboard does not work. Cannot adjust the brightness of Screenpad (Which is controlled via Software in Windows). Optionally try the instructions in [https://askubuntu.com/questions/51445/how-do-i-calibrate-a-touchscreen-on-a-dual-monitor-system this page for calibrating the Screenpad-touch.

## Keyboard
Like many other Asus Laptop, this model features an Asus N-Key Custom RGB USB Keyboard.

For a better experience, use ≥5.13.

With asusctl installed, most features and keys of the keyboard do work. However, The CPU-Fan-Profile RGB-Auro-Profiles Switching needs to be manually set up via hotkey scripts or it needs to be operated via command-line using the command . Try the command  for details.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || (Marked as Built-in Microphone ON-OFF Toggle for Windows)
|-
|  ||  ||  || CPU Fanspeed Control
|-
|  ||  ||  || Screencapture
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || KDE Switches to External screen
|-
|  ||  ||  || Enables/disables Touchpad
|-
|  ||  ||  ||  Sleep / Screens Off
|-
|  ||  ||  ||  Marked as Airplay Mode ON-OFF Toggle
|-
|  ||  ||  || Keyboard RGB Brightness (Increase / ON)
|-
|  ||  ||  || Keyboard RGB Brightness (Decrease / OFF)
|-
|  ||  ||  ||  Key is detected(KEY_PROG1:149) but no action assigned. (Marked Prev Keyboard RGB mode for Windows)
|-
|  ||  ||  || Key is detected(KEY_PROG1:202) but no action assigned. (Marked Next Keyboard RGB mode for Windows)
|}

## Asus/ROG Special keys
Being an ROG series gaming laptop, this model also features some non-standard special keys on the keyboard, which are partially or fully incompatible as listed below.

{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Key is detected(KEY_PROG1:148) but no action assigned. (Opens Armorycrate App in Windows)
|-
|  ||  ||  || Key is not detected. Toggles PageUp/PageDown mode and Arrow Keys mode
|-
|  ||  ||  || Key is not detected. Turns on Software/RGB Based NumPad on Trackpad in Windows.
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function

## Known Issues
* Earphone / Microphone ports do not work.
* Keyboard: Keyboard/Power-button might not wake up the system if the device goes to sleep. Keep pressing the Power button for a while(~20 seconds) to turn off the system in this case.
* USB-C/Thunderbolt: The port is detected and works in USB 3 mode.
* On startup there is an error message while systemd fails to start .
