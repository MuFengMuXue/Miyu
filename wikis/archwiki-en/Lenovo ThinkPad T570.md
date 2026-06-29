# Lenovo ThinkPad T570

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| TrackPoint || ||
|-
| Keyboard || ||
|-
| Video ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Wi-Fi ||  ||
|-
| I219-LM ||  ||
|-
| Audio ||  ||
|-
| SD card reader ||  ||
|-
| Fingerprint reader ||  ||
|-
| Mobile broadband ||  ||
|-
|}

## Installation
Make sure that Secure Boot is disabled in BIOS Setup.

## Configuration
## BIOS Update
Install this BIOS update (or a newer one) to fix a serious bug concerning hyperthreading and issues with thunderbolt
[https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1708043/
, which can affect you even if you do not use thunderbolt.
See Flashing BIOS from Linux for details on how to install the BIOS without an optical drive; the  method is known to work on the T570.

Note: before flashing, you have to disable the Intel BIOS guard or risk bricking your laptop. In the BIOS, set Security - Intel (R) SGX - Intel (R) SGX Control to Disabled. Do the same for Device guard, if needed. If you corrupt your BIOS, you can fix it by flashing a working ROM directly into the EEPROM chip either with [https://web.archive.org/web/20200318130144/http://posts.nadim.computer/2018/10/26/repairing-a-thinkpad.html a Raspberry Pi or a specialized programming device.

## Healing a corrupted BIOS
If you got bitten by the Intel BIOS (Boot) Guard, you can follow these instructions to reverse the damage.

# Open the bottom cover (see video)
# Locate the chip containing the BIOS. It is under a black sticker (see photo). The model of the chip is MXIC MX25L12873F M2I-10G (see datasheet).
# Connect your programming device to the chip using a SOIC8 clip. You should probably support the clip and its cable somehow, so it remains completely still.
# Read the old BIOS image from the chip using Flashrom or the software that came with your programming device
# Open the old BIOS image with
# In UEFITool, do File - Search - String and systematically input BIOS IDs that are found in the VERSION INFORMATION section of the Lenovo BIOS readme file found on the Lenovo BIOS download page
# When you hit the corresponding ID, you will see something like this in the Message section of UEFITool: "Unicode text "N1VET31W" found in PE32 image section at offset 31B0h"
# Download the BIOS with the matching ID from Lenovo's site (it has to be the same, because Boot Guard is looking at the specific cryptographic signature)
# Install
# Extract the boot image with a command like
# Create a loop device
# Mount the partition found in the loop device
# In the mounted partition, navigate into the directory named something like Flash/N1VET31W/
# Copy the file with the extension FL1 into your project directory
# Unmount
# In your old corrupted BIOS, the section with the corruption is pinpointed by UEFITool with a message like "parseSection: GUID defined section can not be processed". Double-clicking the message will show you the volume it belongs to. In the BIOS region, you will replace the corrupted volume and all the preceding ones with healthy volumes extracted from the downloaded BIOS image. This type of minimal replacement is needed instead of replacing every volume, because UEFITool is not yet smart enough to preserve all the required Boot Guard data. UEFITool_NE (New Engine) is able to display the Boot Guard keys and signatures, but, as of the writing of this, is not yet able to do volume replacing. It is probably a good idea to use the NE version to do the extraction.
# Open the FL1 file in UEFITool NE
# Do Right-click - Extract as is... or Ctrl-E for each of the needed volumes (save them with names that preserve the order they appear in)
# Open the corrupted BIOS in UEFITool (old engine version) and do Right-click - Replace as is... or Ctrl-R for the respective volumes
# File - Save image file... under some different name
# Flash the healed image back into the chip

If you find your boot loader is gone, install it using a live USB.

## Bumblebee
Until bbswitch is updated to support the new power management method, add  to your kernel parameters.

## Bluetooth
If you have a very weak Bluetooth signal when using Wi-Fi, make sure you have a recent . See https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1721271 for more information.
