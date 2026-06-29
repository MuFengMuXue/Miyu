# Microsoft Surface Pro 3

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam (front) ||  ||
|-
| Webcam (rear) ||  ||
|}

This page aims to document all relevant information on getting Arch Linux working on the Microsoft Surface Pro 3 tablet.

## Booting into the installer
To boot from USB, you will need to instruct the tablet to boot from USB or SD Card. Also, you may want to avoid disabling Secure Boot as this will cause each boot to display an ugly bright red background intentionally clashing with the "Surface" splash logo.

There are three types of boots in the Surface Pro 3 explained here:
# Normal mode
## Just leave the computer go. You can change it from "Alternate Boot order" in the UEFI Setup
# Boot into the UEFI Setup
## With the device powered off (or rebooting, but better play safe)
## Press & hold Volume up
## Press power button
## Wait until the surface logo appears
## Release Volume up
## You will be presented with the UEFI Setup Menu
# Boot into the USB/SD card
## Power off the device
## Press & hold Volume down
## Press power button
## Wait until the surface logo appears
## Release Volume down

## Disable Secure Boot
Boot into the UEFI setup, and select Secure Boot Control > Disable. Now continue with the installation. See the Microsoft steps for more information.

## Boot with Secure Boot
See Secure Boot.

## Installation
I have done the installation with systemd's bootctl Systemd-boot (old Gummiboot). After completing the Installation guide, you should do two more things. Booting in Secure Boot will not work for the new installation, as the vmlinuz has not been registered within its loader.

The easiest way is to do all the setup is the following, just before rebooting:

# Exit from the chroot but do not umount anything
# Move /mnt/boot/EFI/boot/bootx64.efi to /mnt/boot/EFI/boot/loader.efi
# Copy /boot/EFI/boot/bootx64.efi and HashTool.efi to /mnt/boot/EFI/boot/

(If you are unable to find HashTool in /boot, try in /usr/run)

Here, we have enabled Preloader to boot our gummiboot loader, and if it detects that something has not been signed, it will boot the HashTool.efi to sign the vmlinuz-image binary.

The idea is, we take the systemd boot loader and make it the one that PreLoader will boot (the one in its same folder, named loader.efi). Then, we copy both the PreLoader (which is the archiso's bootx64.efi) and the HashTool (already with that name).

This way, with Secure Boot enabled, you will be able to boot your kernel whenever you wish to, signed or not, repeating the hash storing procedure on the next boot.

## Extra steps
## Enabling Touchpad
Ref: GitHub
In order to enable full functionality of the touchpad (e.g. two-finger scrolling, right click), you need to
Install the  package, have the kernel patch applied as well as add the following to :

 Section "InputClass"
   Identifier "Default clickpad buttons"
   MatchDriver "synaptics"
   Option "ClickPad" "true"
   Option "SoftButtonAreas" "50% 0 82% 0 0 0 0 0"
   Option "SecondarySoftButtonAreas" "58% 0 0 15% 42% 58% 0 15%"
 EndSection

## Tuning the Pen
The pen buttons might not work out of the box. Install the  package and comment the  section in . Furthermore add  in the  line of N-Trig in . Note that the purple bluetooth button is recognized but able to be bound to an action.
Ref:Reddit

## Virtual Keyboard
Depending on the desktop environment you are using, you might want to use different virtual keyboard.  provides a reliable and comfortable experience.
A guide for optical tweaking is provided here. If you are using GNOME, these two extension (1, 2) provide a better integration.

## Booting with Secure Boot Enabled
The recommended boot loader for UEFI with Secure Boot enabled is systemd-boot.

To boot with Secure Boot, you will need the following packages:  and .

See Surface Pro 3 and Secure Boot post-install for more information.

* Copy  to .
* Copy  and  to .
* Create an NVRAM entry for PreLoader.efi:

  efibootmgr -d /dev/sdX -p Y -c -L Preloader -l /EFI/systemd/PreLoader.efi

* Verify the entry was made and that it is first in the boot order:

 efibootmgr

* Enroll your kernel in the boot loader: Secure Boot.
* Enroll  and , and then reboot to system.

You should now be able to boot with Secure Boot enabled.

## Enabling Wi-Fi and Bluetooth
The package  is required for the Wi-Fi and Bluetooth since the linux-firmware 20220119 update.

## Accessibility
The appearance of the BIOS is pretty simple and not very colorful, so it might work well with OCR software.

The BIOS can be configured with a keyboard, mouse, or using the touch screen.

## Troubleshooting
## Invalid signature detected check secure boot policy in setup
This happened to me after deleting the Secure Boot database and initializing it with Microsoft & CAs. I also had to do the recovery of the BitLocker partition, but I would follow these steps:

# After the reset, switch off and try to boot from the SD/USB. If you do not succeed and get the message many times:
## Leaving all TPM & Secure Boot enabled and SSD Only alternate system order
## Do another database reset
## Enroll the Microsoft and CAs again
## reboot into SD/USB with volume down
## It should work now
# Follow steps in the Secure Boot installation
# After the full installation of Arch Linux, when you have it working, do the BitLocker recovery

If after doing these steps does not still work. Flash the Archiso image once more and try again,

## Keyboard Cover not working
This can happen sometimes when you restart. The solution was to shutdown and reboot. (not restart)

## Pen/Touchscreen issues in Xournal
When using the  package there is a bug in the last official release of  (0.48.2) where it will incorrectly detect the Surface Pen as the touchscreen device. However it has been fixed in the latest Xournal source as per this bug. Installing the AUR package  builds the latest source including this fix.
Note that you will need to select 'NTRG0001:01 1B96:1B05' as the touchscreen device (Options > Pen and Touch).
