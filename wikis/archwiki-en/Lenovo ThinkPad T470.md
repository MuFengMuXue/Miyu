# Lenovo ThinkPad T470

{| class="wikitable archwiki-table-laptop"
! Device !! PCI/USB ID !! Working?
|-
| GPU (Intel 620) ||  ||
|-
| GPU (Intel 520) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Ethernet (Intel I219-V) ||  ||
|-
| Ethernet (Intel I219-LM) ||  ||
|-
| Wireless (Intel 8265/8275) ||  ||
|-
| Wireless (Intel 8260) ||  ||
|-
| Bluetooth ||  ||
|-
| Webcam ||  ||
|-
| IR Camera ||  ||
|-
| TrackPoint ||  ||
|-
| Touchpad ||  ||
|-
| Touchscreen ||  ||
|-
| Fingerprint Reader ||  ||
|-
| SD Card Reader ||  ||
|-
|}
For a general overview of laptop-related articles and recommendations, see Laptop.

## Firmware
The T470 is one of the models supported officially by Lenovo through the fwupd firmware update program.
If you are using a UEFI boot scheme, this is probably the easiest and most officially supported way to keep all the firmware programs updated.

If it does not work for you or if you prefer these methods, it is still possible to do the BIOS update by booting on a specially crafted disk or  USB stick.
By visiting the downloads section (T470) an ISO can be downloaded and burned to disk which will perform the update from Lenovo. Or extracted and copied on a USB Stick.

Another option that works if you got a CD-ISO from Lenovo is to follow this guide and convert the ISO to an IMG prior to dd-ing it to a USB stick.

## Kernel and hardware support
Hardware video acceleration with Kaby Lake seems to work fine via va-api.

As noted in Intel graphics, the  driver seems to cause more issue than the builtin  Xorg driver.
Works fine without the intel driver (on a Skylake configuration).

suspend-resume results in the fan holding at 100% without ever spinning down. This is being tracked on the kernel bugtracker. The issue seems to be resolved by BIOS 1.43.

## Fingerprint reader
As of writing this, the fingerprint reader is still under prototype development, but seems working fine on the T470.

To get the sensor working, install the  package, and its dependencies:  and  (which conflicts with the  package in the official repositories, so uninstall this package first if it is installed). Enable/start the .

If this fingerprint reader had been previously set up, either through Windows (dual-booted or through a Windows virtual machine), or from a previous setup of fprintd, you will likely need to reset the Validity fingerprint reader to factory defaults (must first stop ):

Then, start  again. You can now enroll your fingers with  as a regular (non-root) user. You may verify your enrolled fingerprints with .

After setting up the fingerprint sensor is complete, one can use it to login or authenticate for  or .

For login, edit  by adding  as sufficient to the top of the auth section:

Note, the  command from the python-validity README.md does not exist in Arch, and the lines it adds to files in the  directory do not work. See the  manual for details.

Do the same for sudo with  or su with

Sometimes the  service breaks after suspension of the device, a fix for this issue is to make a custom service to restart the service on exiting suspend. the name of this service does not matter but the location does see Systemd.
here is a service that does the job:

## Screen backlight
Without the  driver (), neither  or  brightness control are working.
It is possible that, with the good  kernel parameters, the backlight related keys do their job.

Other workaround exists, such as described on this post or in the wiki acpid#Enabling backlight control.
Using the  package as a  replacement works well.
You can also check this repository as a base to add the ACPI rules to call  when backlight keys are pressed.

## UEFI boot
After configuring the BIOS setup to allow UEFI boot (either UEFI only or both), it works flawlessly.

For booting directly with EFISTUB, the kernel executable (e.g. ) may need to be renamed with a .efi extension (e.g. ) otherwise it will fail to load.

## BIOS GPT boot
I can confirm that issue. Even with a recent bios (1.52), it does not work.

I had to trick my ThinkPad into UEFI (because my bios is locked, found that method by pure luck).
It works by installing the syslinux boot loader on your freshly installed arch (be sure to follow the GPT specific instructions at Syslinux#GUID partition table) and the boot that syslinux with the arch install iso ('Boot existing OS' -> press  -> replace  with ). Syslinux should show you an option to boot the Arch Linux installation in UEFI mode. Mount you Arch installation,  into it and install GRUB (or your favorite boot loader) for UEFI. That did the trick for me.

You have to create a proper EFI system partition. Have a look at partitioning.

## Special buttons
See Laptop/Lenovo#Special buttons.

## Function keys for model 20K7 25th Anniversary Edition
{| class="wikitable"
! Special Key !! Visible?1 !! Marked?2 !! Effect
|-
|  ||  ||  || XF86WakeUp
|-
|  ||  ||  || No Effect
|-
|  ||  ||  || XF86ScreenSaver
|-
|  ||  ||  || XF86Battery
|-
|  ||  ||  || XF86Sleep
|-
|  ||  ||  || XF86TouchpadToggle
|-
|   ||  ||  || XF86WebCam
|-
|  ||  ||  || XF86Display
|-
|  ||  ||  || XF86WLAN
|-
|  ||  ||  || XF86Tools
|-
|  ||  ||  || XF86Bluetooth
|-
|  ||  ||  || No Effect
|-
|  ||  ||  || XF86Favorites
|-
|  ||  ||  || XF86MonBrightnessUp
|-
|  ||  ||  || XF86MonBrightnessDown
|-
|  ||  ||  || Cycle Keyboard Backlight
|-
|   ||  ||  || XF86AudioMute
|-
|  ||  ||  || XF86AudioLowerVolume
|-
|  ||  ||  || XF86AudioRaiseVolume
|-
| ||  ||  || XF86AudioMicMute
|-
|  ||  ||  || XF86AudioPrev
|-
|  ||  ||  || XF86AudioStop
|-
|  ||  ||  || XF86AudioPlay
|-
|  ||  ||  || XF86AudioNext
|-
|  ||  ||  || Menu
|-
|  ||  ||  || XF86Back
|-
|  ||  ||  || XF86Forward
|}
# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function
