# Lenovo ThinkPad X230

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| TrackPoint || ||
|-
| Keyboard || ||
|-
| Video ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader ||  || , no boot option
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Mobile broadband ||  ||
|-
| Fingerprint Reader ||  ||
|}

## Firmware
fwupd does not support this device yet.

To update the firmware on the device, get the latest bootable CD and follow the steps in Flashing BIOS from Linux#Bootable optical disk emulation.

## Display
If you experience that your brightness setting is not restored on resume from suspend, then create config:

HD Graphics 4000 supports external 4K display and audio via display port to HDMI adapter, but requires to add 4K mode manually == Input devices ==

## Sound control buttons
The red LED mute indicators light up automatically, if the corresponding channel is muted in alsamixer. The easiest way to make buttons work is to install PulseAudio and its plugin for your desktop environment.

* GNOME - works out of the box
* Xfce - install , , add plugin to panel and reboot. Additionally  uses  as mixer and  for sound level popups
* Handle ACPI events with acpid the [https://makandracards.com/makandra/47162-how-to-enable-the-thinkpad-microphone-mute-key-on-ubuntu-16-04 hard way. Some functions like  are implemented in .

## X230T (tablet version)
## Wacom tablet input
Works out of the box with . See Wacom tablet.

## Multitouch screen for the X230t
Some X230t models have a multitouch screen in addition to the Wacom tablet. Works out of the box with .

## Touchpad
Under certain circumstances, the touchpad may behave very jumpily. Ubuntu Bugtracker offers a solution for this issue. Install Touchpad Synaptics and create the following file:

## OpenCL
Thinkpad X230 based on Intel Ivy Bridge (3rd generation) platform which meets OpenCL 1.2 specification. Unfortunately GPU support in Linux is broken, so  and  will not work. Use CPU-only  instead.

OpenCL computation performance differ between CPU and GPU, depending on task. In many cases GPU is preferable. For Core(TM) i5-3210M CPU, which incorporates HD Graphics 4000 GPU:

* GPU  reports 3095 H/s (checked in Windows)
* CPU  reports only 2660 H/s, which is the same as no-OpenCL

In this example OpenCL does not give any advantage, and it is better to look for other options such as building native binaries for your system.

## Power saving
Main article: Power saving

## TLP
Users of TLP need to pay attention to a hardware bug according to which it is recommended to only use either the upper or lower charging threshold. The following configuration is recommended by the developer of TLP.== UEFI ==

Laptop incorporates InsydeH2O® UEFI BIOS with classic text interface. It supports UEFI with Secure Boot, UEFI-CSM and Legacy BIOS modes.

## Boot configuration
UEFI boot options can be safely (no bricking) set with  or UEFI Shell v2 (checked with BIOS 2.77 (G2ETB7WW) EC 1.15). Though you can delete any boot variable, so be careful!

An EFI boot stub on SSD boots into a display manager in less than 25 seconds in non-CSM mode. Small ESP (100 MiB fat32) also supported.

## USB UEFI update
All official updates, including Windows utility, Bootable CD and documentation can be found [https://pcsupport.lenovo.com/gb/en/downloads/ds029187 here. You can use  to create bootable USB images from the Bootable CD:

 $ geteltorito.pl g2uj24us.iso > update.img
 # dd bs=512K if=update.img of=/dev/sdX

Insert USB stick, reboot and press , choose your USB. Follow the instructions.

## Trusted Platform Module
Laptop has dedicated TPM 1.2 chip onboardIt does not looks like it can be upgraded to TPM 2.0. Chip itself disabled by default sometimes, also owner clearing will not appear without Supervisor password set:

# Enter Thinkpad UEFI Setup by pressing
# Set Security > Password > Supervisor password
# Set Security > Security Chip > Security Chip [Active
# Save settings by pressing  and reboot
# Turn laptop off, turn on and UEFI option Security > Security Chip > Clear Security Chip eventually will appear.

Process described in "ThinkPad X230 and X230i User Guide", Chapter 4. Security > Setting the security chip.

## Known issues
* There is a BIOS bug that gets in the way of the boot process with LUKS and full-disk encryption. The user is stuck at the "Loading initial ramdisk" step, and does not see a password prompt to unlock the encrypted device. You can actually enter your password at this step, and boot-up will continue. However, updating the BIOS will resolve this completely. If you are using coreboot as a BIOS replacement, you can fix this issue by adding  to the  list in  and rebuilding your initrams with .
* UEFI option to clear TPM not working. STM chip datasheet describes physical presence pin, which, probably, can be used as workaround.
