# System76 Galago Pro galp3

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Audio ||  ||
|-
| Microphone || ||
|-
| Speakers || ||
|-
| Webcam || ||
|-
| Bluetooth || ||
|-
| Ethernet ||  ||
|-
| Wireless ||  ||
|-
| SD-card reader ||  ||
|-
| Fingerprint reader || ||
|}

## OEM software
System76 develops a special distribution (Pop!_OS) for their computers, and it comes with many tweaks and tools to ensure a seamless end-user experience.  Arch does not have these out of the box;  and unfortunately, sometimes their computers do not work right without them.  Thankfully, it is possible to get the same first-class hardware support in Arch Linux that you have in Pop!_OS -- it just takes a little elbow grease.

## Packages
All necessary packages can be found in the AUR.  It is recommended to install everything in the list below.

; Modules
*
*
*

; Daemons
*
*  (needed for System76 switchable graphics)

; Firmware
*  (required if you want to update your BIOS and the daemon seems to be needed for things like audio to work right)
*  (required if you want to know when there is a BIOS update available)

(There are also "-git" versions of many of these packages, if you wish to stay bleeding edge.)

## Settings
Once you have installed the above, you will need to tell your computer to use them.

## Services
Enable ,  and : (source)

## Drivers
To make sure all drivers are being loaded correctly, run ;  this will automatically add necessary rules to , and execute .

## BIOS updates
To check your current BIOS version and whether there is a new version available, run  as root.  Keep in-mind that this is a GTK application, so you need to be running X or Wayland for it to run.  (It has no CLI -- it does not even respond to .)

To update your system to the latest firmware on the next boot, run .

## Suspend/hibernate
Out of the box, Arch Linux does not resume a previously suspended or hibernated session. To support hibernation, ensure that you have swap space equal to or greater than your system memory (RAM), and add "resume" to your  file, per the instructions here.

## Function keys
: Only keys with known functions are shown.

{| class="wikitable" style="margin: unset;"
|+ style="text-align: left;" | Multimedia keys
|-
! Key
!title="The key is visible to `xev` and similar tools."| Visible?
!title="The physical key has a symbol on it, which describes its function."| Marked?
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

{| class="wikitable" style="margin: unset;"
|+ style="text-align: left;" | Display keys
|-
! Key
!title="The key is visible to `xev` and similar tools."| Visible?
!title="The physical key has a symbol on it, which describes its function."| Marked?
! Effect
|-
|  ||  ||  || Toggles power to the display
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

{| class="wikitable" style="margin: unset;"
|+ style="text-align: left;" | Number pad keys (NumLock off)
|-
! Key
!title="The key is visible to `xev` and similar tools."| Visible?
!title="The physical key has a symbol on it, which describes its function."| Marked?
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|}

{| class="wikitable" style="margin: unset;"
|+ style="text-align: left;" | Number pad keys (NumLock on)
|-
! Key
!title="The key is visible to `xev` and similar tools."| Visible?
!title="The physical key has a symbol on it, which describes its function."| Marked?
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|}

{| class="wikitable" style="margin: unset;"
|+ style="text-align: left;" | Misc toggle keys
|-
! Key
!title="The key is visible to `xev` and similar tools."| Visible?
!title="The physical key has a symbol on it, which describes its function."| Marked?
! Effect
|-
|  ||  ||  || Toggles max state of fans
|-
|  ||  ||  || Cycle keyboard backlight brightness
|-
|  ||  ||  ||
|-
|  ||  ||  || Toggles power to the webcam
|-
|  ||  ||  ||
|-
|  ||  ||  || Suspends the computer
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

{| class="wikitable" style="margin: unset;"
|+ style="text-align: left;" | Broken keys
|-
! Key
!title="The key is visible to `xev` and similar tools."| Visible?
!title="The physical key has a symbol on it, which describes its function."| Marked?
! Effect
|-
|  ||  ||  || Label: Toggle displaysReality: Apparently behaves like Super_L and XK_l ?
|-
|  ||  ||  || Label: Reality:  (ignores )
|-
|  ||  ||  || Label: Reality:  (ignores )
|}

## Troubleshooting
## system76-firmware: EFI mount point not found
If using  as the ESP mount point, ensure you have the mount present in . You may find the appropriate device to mount by using a combination of  and .

List disks (one device will be designated as "EFI System"):

 # fdisk -l

List devices and mount points, you should see the EFI system device, and confirm whether it is mounted/unmounted:

 # lsblk

If needed, mount it:

 # mount device /efi

Optionally print the fstab configuration for inclusion/merging into

 # genfstab -U /

After doing the above, it might be a good idea to schedule a firmware update:

 # system76-firmware-cli schedule

## With GRUB
After scheduling a firmware update, ensure that GRUB is set to use the EFI system partition like so:

 # grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=grub
 # cp /boot/grub/grub.cfg /boot/grub/grub.cfg.bak
 # grub-mkconfig -o /boot/grub/grub.cfg

Restart to trigger the firmware update.
