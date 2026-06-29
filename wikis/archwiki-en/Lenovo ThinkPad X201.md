# Lenovo ThinkPad X201

The Lenovo X201 is a subnotebook produced by Lenovo.

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || PS/2 ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Card reader ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint sensor || ||
|}

## Installation
The X201’s USB ports do not seem to work with many USB 3.x devices. A USB 2.0 install medium is recommended.

An extra kernel parameter might be necessary to enable proper CPU frequency management, see #BIOS CPU frequency limitation.

## Accessibility
The firmware is a traditional keyboard-only BIOS, navigated with arrow keys, , and some function keys. In all menus,  and  exit and return to the next-higher menu.  resets the entire firmware configuration ( to confirm), and  saves the firmware configuration and reboots (also  to confirm). In the “Boot” menu of the firmware,  can be used to move entries up, while  can be used to move entries down.

The current entry of a firmware menu appears in white text, while other entries appear in blue text. Explanatory text in black appears on the right, while keyboard shortcuts appear in white and cyan text on the bottom.

## Selecting a boot device
To interrupt startup, press the blue  button after poweron. This is the fifth button from the left in the top row. The startup interrupt menu that appears will automatically continue booting after a few seconds. This can be paused with .

Unfortunately, the  boot override does not seem to function properly at least on some models. Therefore, the following procedure utilizing the normal BIOS setup should be used:

* Enter Startup Interrupt Menu by pressing both  and  repeatedly after poweron for up to ten seconds.
*  to enter BIOS Setup.
*  and  to reset firmware configuration, such that the boot priority is in the default order.
* Navigate down three times to the fourth option “Startup” and select with .
*  for “Boot” menu. This menu contains numbered items for the boot priority.
* The default boot priority order is as follows:
*# USB FDD
*# ATAPI CD0
*# USB CD (installation medium burned to disk and connected through external drive)
*# ATA HDD0 (internal hard drive)
*# PCI LAN (network boot)
*# USB HDD (installation medium on USB mass storage device)
*# ATA HDD1
*# (empty)
** Excluded option 1: ATA HDD2
** Excluded option 2: ATAPI CD1
* Only the options “USB CD” and “USB HDD” are relevant. Note that any option below “PCI LAN” will likely never get used, as this option enters the Intel PXE ROM, which usually fails if the network is not configured for netbooting.
* To prevent PCI LAN and any existing OS on the hard drive from overwriting a USB installation medium, navigate down five times to the sixth entry in the list, which is “USB HDD”. Press  five times to move it to the first entry in the list.
*  and  to save and exit.
* The system should reboot and load an installation medium if available.

## Firmware
The X201 does not have UEFI, leaving GRUB or Limine as the only remaining maintained boot loaders.

## Function keys
{| class="wikitable"
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||  (press, or hold for >1s)
|-
|  ||  ||  ||  (lock screen)
|-
|  ||  ||  ||
|-
|  || 3 ||  ||
|-
|  ||  ||  ||  (soft-disable WiFi in rfkill)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Unknown, key code , key is marked with laptop symbol next to eject symbol
|-
|  || 3 ||  ||
|-
|  ||  ||  ||  pressed and released, followed by + pressed and released
|-
|  ||  ||  ||
|-
|  ||  ||  || +
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles keyboard light
|-
| ,  ||  ||  || Unknown, key code
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# systemd-logind handles this by default.

## Troubleshooting
## Overheating
There are some discussions concerning overheating-related shutdowns when running under full load (video encoding, etc). [https://bugs.launchpad.net/ubuntu/+source/linux/+bug/751689

Use the following  configuration can be used for frequency scaling; see CPU frequency scaling for more information. Undervolting is not possible with the Intel core iX cpu.

## No speaker output
Try pressing the mute button (next to the Escape key). See [https://www.stderr.nl/Blog/Hardware/Thinkpad/WeirdMuteButtonBehaviour.html this article for details.

## No ACPI events
See coreboot documentation: [https://www.coreboot.org/pipermail/coreboot-gerrit/2015-July/028593.html

## Display issues
See Intel graphics#AccelMethod and Intel graphics#DRI3 issues.

X201s:
If planning to use VT-d, it is also recommended to add the following kernel parameter:

 intel_iommu=igfx_off

## Hardware virtualization
If KVM claims virtualization support is disabled in BIOS, even with VT-x enabled, disable Intel TXT. === BIOS CPU frequency limitation ===

The X201 BIOS suffers from the BIOS CPU frequency limitation bug when on AC power only, which it shares with several ThinkPad models. See CPU frequency scaling#BIOS frequency limitation for how to work around this.
