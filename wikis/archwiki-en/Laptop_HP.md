# Laptop/HP

## Model list
## Compaq
| Presario F700 || 2009-04-07 ||  ||  ||  ||  ||  ||  || Hangs 20-30s when loading ACPI modules on battery power. Some hotkeys do not work. Need to turn  to  in Xorg configuration to fix keyboard layout problems. ||
|-
| Presario CQ60-420ED || 2010-01-22 ||  ||  ||  ||  ||  ||  || Console framebuffer is a bit slow (using ), wireless LED indicator flickers red and blue. ||
|-
| Compaq 6715S || 2012-01-05||  ||  ||  ||  ||  ||  || ||
|-
| Compaq 6720S || 2011-03-19 ||  ||  ||  ||  ||  ||  || ||
|-
| Compaq 8510w || 2015-03-13 ||  ||  ||  ||  ||  ||  ||  ||
|}

## EliteBook
| EliteBook 2560p || 2018-11-02 ||  ||  ||  ||  ||  ||  ||  || As root, run  to recognize smartcards.
|-
| EliteBook 8460p || 2023-11-17 ||  ||  ||  ||  ||  ||  ||  || As root, run  to recognize smartcards.
|-
| EliteBook 2570p || 2021-02-13 ||  ||  ||  ||  ||  ||  || || xHCI IRQ issues
|-
| EliteBook 840 G1 || 2019-10-12 ||  ||  ||  ||  ||  ||  || ||
|-
| EliteBook 850 G3 || 2024-08-05 ||  ||  ||  ||  ||  ||  ||  ||
|-
| EliteBook 840 G8 || 2023-02-05 ||  ||  ||  ||  ||  ||  || || Sometimes there is a significant battery drain of about 1-2% / hour while in suspend
|-
| EliteBook 845 G9 || 2023-08-21 ||  ||  ||  ||  ||  ||  ||  ||
* For Touchscreen: yes Pen: yesNFC: no*WWAN: no*Fingerprint: no*}} || *See dedicated page
|-
| EliteBook x360 1040 G8 || 2025-10-23 ||  ||  ||  ||  ||  ||  ||  || Same fingerprint reader as EliteBook x360 1030 G8
|-
| EliteBook 845 G7 || 2023-08-10 ||  ||  ||  ||  ||  ||  ||  ||
|}

## Envy
| ENVY 14 || 2012-03-04 ||  ||  ||  ||  ||  ||  || ||
|-
| Envy 14-j106tx || 2016-07-22 ||  ||  ||  ||  ||  ||  || ||
|-
| ENVY 17 || 2014-03-05 ||  ||  ||  ||  ||  ||  || ||
|-
| ENVY TouchSmart 17-j113tx || 2017-01-06 ||  ||  ||  ||  ||  ||  || ||
|-
| ENVY x360 Convertible 15-cp0xxx || 2025-02-25 ||  ||  ||  ||  ||  ||  ||  || *Orientation/Rotation detection works, but hinge angle does not.
|-
| ENVY 15-as010ur || 2016-12-05 ||  ||  ||  ||  ||  ||  ||  || Small problem with p2p , possible solution: .Cannot set mute-key led light.
|-
| ENVY 15-ep0020ca (10M52UA) || 2020-09-09 ||  ||  ||  ||  ||  ||  ||  || The model has two SSDs in RAID with enabled Intel RST. BIOS does not have an option to change RAID to AHCI. There is no way to install Linux on this model.
|-
| ENVY 13-ad140ng || 2018-11-21 ||  || * ||  ||   ||  ||  || || hdajackretask should be used to enable the top speaker  override to Internal Speaker,  override to Internal Speaker BackCannot set mute-key led light.
|-
| ENVY 13-ag0009ng || 2025-10-13 ||  || * ||  ||   ||  ||  ||  || hdajackretask should be used to enable the top speaker  override to Internal Speaker,  override to Internal Speaker BackCannot set mute-key led light.*Orientation/Rotation detection works, but hinge angle does not.
|-
| Envy 13-ba1xxx || 2026-03-27 ||  ||  ||  ||  ||  ||  ||  || You may want to manually setup scripts+services for mute/mic mute LED usage.
|-
| ENVY m4-1015dx || 2021-12-03 ||  ||  ||   ||  ||  ||  || || Use hdajackretask to set pin  and  to Internal speaker and  to Internal speaker (LFE)
|-
| ENVY x360 15-dr1948nd/15-ed0985nd || 2021-01-15 ||  ||  ||  ||  ||  ||  || || EFISTUB issues: forcibly sorts EFI boot entries by label length (long>short)
|-
| ENVY x360 15-ds0155ng || 2020-06-17 ||  ||  ||  ||  ||  ||  || ||
|-
| ENVY x360 15-ds0004nf || 2023-12-24 ||  ||  ||  ||  ||  ||  ||  || Cannot set mute-key led light.
|-
| Envy x360 13-ay0779ng || 2022-02-06 ||  ||  ||  ||  ||  ||  ||  ||
|}

## Other
|-
| TouchSmart tx2z || 2010-01-17 ||  ||  ||  ||  ||  ||  || || Known successes with touchscreen and stylus in Ubuntu
|-
| 625 || 2011-08-26 || ||  ||  ||  ||  ||  || ||
|-
| Stream 11-r004nf || 2017-02-03 ||  ||  ||  ||  ||  ||  || ||
|-
| Stream 11-y008nf || 2017-08-24 ||  ||  ||  ||  ||  ||  ||  || Cannot set mute-key led light.
|-
| Omen 15 || 2020-01-26 ||  ||  ||  ||  ||  ||  ||  || HDMI and DP connected to NVIDIA card - run X on it to use video outputs: they do not seem to work on Wayland.
|-
| Notebook 14-cm0007la || 2020-04-26 ||  ||  ||  ||  ||  ||  || Brightness control: not working by default || Wi-Fi and Bluetooth requires GitHub driversINSANE battery discharge: use TLP and RyzenAdj
|-
| Notebook 17-bs511ng || 2020-11-01 ||  ||  ||  ||  ||  ||  || || Fan blows constantly
|-
| Omen 15-ek005na || 2021-03-25 ||  ||  ||  ||  ||  ||  || ||
|-
| Laptop 14-fq1021nr || 2021-11-13 ||  ||  ||  ||  ||  ||  ||  || *Suspend to RAM: broken; NVMe drive fails to resume. Workaround: boot with .• Mute LED on : works as of kernel 6.13.7.• UEFI entered by pressing , allows toggling secure boot, allows EFI image selection. Note: all boot entries other than  are cleared on boot, but this can be worked around by placing the EFI image you want to boot at that location.
|-
| Laptop 14-fq0xxx || 2024-05-23 ||  ||  ||  ||  ||  ||  || ||
|-
| Laptop 14-fq1025nr || 2022-02-26 ||  || * ||  ||  ||  ||  || || • Mute LED, Headphone Jack Detection Works.• * Headphone microphone sometimes is not detected. • * Dummy output still occurs after reboot but less frequent after later kernel versions
|-
| Laptop 15s-eq1124nw || 2021-12-22 ||  ||  ||  ||  ||  ||  || || Suspend to RAM: broken, needs hack mentioned on page.Mute LED on : broken, stays off.
|-
| Laptop 15z-ef2000 || 2022-02-01 ||  ||  ||  ||  ||  ||  || || Mute button LED does not light up.
|-
| Victus 16-d1xxx || 2022-05-24 ||  ||  ||  ||  ||  ||  ||  ||
|-
| Victus 16-s1xxx || 2022-11-08 ||  ||  ||  ||  ||  ||  || Fan and backlight control with kernel module||
|-
| Laptop 17-cn1035cl || 2022-10-11||  || ||  ||  ||  ||  ||  ||
|-
| Laptop 17-cr0778ng || 2024-02-17 ||  ||  ||  ||  ||  ||  || || Sound might be fixed in kernel 6.8-rc4, but is untested. * Webcam privacy shutter works. Mute Button for sound works, but does not light up. Mute Button for microphone does not work at all.
|-
| Dev One || 2022-06-02 || ||  ||  ||  ||  ||  || || install  for fan speed and battery stats
|-
| X2 210 G2 || 2024-02-27 ||  || * ||  ||  ||  ||  ||  || *Sound needs  for headphone detection to work. Mute button LED does not light up.With newer kernels (6.2.?), there seem to be CPU lock-ups if the atomisp-firmware is not installed. Installing  from intel-aero's repository seems to solve this.
|-
| Victus 15-ec2008ax || 2022-12-08 ||  ||  ||  || * ||  ||  || || *Wi-Fi toggles on lid open
|-
| Pro x360 435 G9 Convertible 6F259EA || 2023-07-08 ||  ||  ||  ||  ||  ||  ||
|| *tested with Gnome shell version 44.1
|-
| 15-ba008ca || 2024-06-20 ||  ||  ||  ||  ||  ||  || ||
|-
| Dragonfly 13.5 inch G4 || 2025-08-16 ||  || * ||  ||  ||  ||  ||  || *CS35L41 amplifier needs kernel driver patch available as ; MIPI camera does not have  V4L2 interface like UVC webcams.
|-
| OmniBook Ultra Flip 14-fh000 || 2025-04-02 ||  ||  ||  ||  ||  ||  ||  || Needs Linux >= 6.13.* Speaker/headphones switch issue tracked here.
|-
| Laptop 15s-eq1009no || 2025-07-20 ||  ||  ||  ||  ||  ||  || ||
|-
| OmniBook 7 AI 14-fr0220nw || 2026-02-07 ||  ||  ||  ||  ||  ||  || ||
|-
| Notebook 247 G8 Ryzen 5 3500U || 2026-02-09 ||  ||  ||  ||  ||  ||  ||
|-
|}

## Pavilion
| Pavilion DV2172EA || 2007-07-12 ||  ||  ||  ||  ||  ||  || ||
|-
| Pavilion DM1-1150SL || 2010-02-19 ||  ||  ||  ||  ||  ||  || ||
|-
| Pavilion dv5055ea || 2010-03-11 ||  ||  ||  ||  ||  ||  || || DVD and Multimedia button not working
|-
| Pavilion dv6605ed || 2008-03-31 ||  ||  ||  ||  ||  ||  || Remote: DVD, Quickplay, and Windows MCE buttons do not work ||
|-
| Pavilion dv6018 || 2008-01-26 ||  ||  ||  ||  ||  ||  || || Use  in Xorg configuration for sensors and remote
|-
| Pavilion dv9530em || 2009-06-12 ||  ||  ||  ||  ||  ||  || ||
|-
| Pavilion TX1220US (GA647UA) || 2008-06-24 ||  ||  ||  ||  ||  ||  || Touch screen: (appears to work; have not calibrated)Remote: not workingHot keys: not tested || Hot keys and touch screen reportedly works on other distributions.
|-
| Pavilion dv6-2115sa || 2010-11-06 ||  || * ||  ||  ||  ||  ||  || *To prevent output to both headphones and speakers simultaneously, set the module parameters
|-
| Pavilion g4 || 2014-10-24 ||  ||  ||  ||  ||  ||  || ||
|-
| Pavilion Ultrabook 15-b030st || 2015-06-06 ||  ||  ||  ||  ||  ||   || ||
|-
| Pavilion g6-1d85nr || 2026-03-18 ||  ||  ||  ||  ||  ||  || ||
|-
| Pavilion g6-2379sr || 2016-09-04 ||  ||  ||  ||  ||  ||  || || Big problems with Wi-Fi card RT3290. Best choice is to use LAN Internet, or change Wi-Fi card.Poor sound quality.
|-
| Pavilion 15-cw0xxx || 2020-01-09 ||  ||  ||  ||  ||  ||  || || Install  or CPU speed is capped to 2 GHz
|-
| Pavilion 15-ab214nt || 2019-08-30 ||  ||  ||  ||  ||  ||  || || Hang on boot or shutdown without kernel parameter
|-
| Pavilion 15-au624tx || 2020-04-24 ||  || * ||  ||  ||  ||  || || *Mute LED requires configuration
|-
| Pavilion 15-cx0xxx || 2022-03-19 ||  || * ||  ||  ||  ||  ||  || *Mute LED requires configuration
|-
| Pavilion 14-ce0xxx || 2019-08-28 ||  ||  ||  ||  ||  ||  ||  || Wi-Fi needs out of tree driver from GitHub.
|-
| Pavilion 13-a252ur || 2020-06-16 ||  ||  ||  ||  ||  ||  || ||
|-
| Pavilion 15-cs3019nf || 2021-03-14 ||  ||  ||  ||  ||  ||  || || Ethernet card not supported by ipxe
|-
| Pavilion Gaming 17-cd1013na || 2021-11-25 ||  ||  ||  ||  ||  ||  || Hotkeys: brightness, airplane mode, pause media NOT working (help does not seem to do anything). SD Card Reader: NOT working ("Unassigned class" in lspci). HDMI: Makes the desktop extremely laggy unless duplicating the laptop screen. Keyboard backlight: Sometimes disables the next boot (maybe not a Linux issue), keypresses activate the backlight but not mouse movement. PC speaker: working (use kernel parameter ). || Fans cannot be controlled (NVIDIA GPU can reach up to 90°C). Upower takes up to a minute to realize the charger has been dis/connected.
|-
| Pavilion Gaming 15-ec1086nw || 2021-08-27 ||  ||  ||  ||  ||  ||  || || Fans can not be software controlled, UEFI does not support Secure Boot
|-
| Pavilion Aero 13-be0214nw || 2021-09-17 ||  ||  ||  ||  ||  || * ||  || *Suspend  has issues on kernel 5.14 without  kernel parameter (screen does not light up after waking up and system seems to be unresponsive)Fingerprint scanner () is not supported by libfprintMute light on  does not work
|-
| Pavilion X2 10 || 2022-03-20 ||  ||  ||  ||  ||  ||  ||  || Mute button LED does not light up.With newer kernels (6.2.?), there seems to be an increased likelihood for CPU lock-ups. Using  works.
|-
| Pavilion 15-eh2085cl || 2022-06-09 ||  ||  ||  ||  ||  ||  || || *rtw8852be is broken. Changes to Secure Boot setting must be saved with , not "Save and exit" in the GUI.
|-
| Pavilion x360 Convertible 14-dy1xxx || 2022-12-30 ||  ||  ||  ||  ||  || * ||  || *Has intermittent issues with the lid wake sensor
|-
| Pavilion x360 Convertible 14-dw1xxx || 2025-02-25 ||  || * ||  ||  ||  ||  ||  || *Sound driver does not appear when running  in terminal after installing Arch. You will have to plug in a sound device first, second unplug said device and restart. You should have sound.
|-
| Pavilion Aero 13-be2775ng || 2024-08-03 ||  ||  ||  ||  ||  ||  || ||
|-
| Pavilion Plus 14 (AMD) 14-ey0XXX || 2025-08-16 ||  ||  ||  ||  ||  ||  ||  || Keyboard backlight only via hardware buttons
|-
| Pavilion 15-cs1506sa || 2025-11-30 ||  ||  ||  ||  ||  ||  ||  ||
|}

## ProBook
| ProBook 440 G1 || 2025-06-26 ||  ||  ||  ||   ||    ||  || ||
|-
| ProBook 440 G4 || 2017-06-04 ||  ||  ||  ||   ||    ||  || ||
|-
| ProBook 445 G7 || 2020-08-13 ||  ||    ||    ||    ||  ||  ||  || Fingerprint reader support varies with the manufacturer.e.g. Some variants of the Synaptics FS7604 do not work due to missing drivers.
|-
|ProBook 450 G7  || 2021-12-09 ||  || * ||  ||  ||  ||  || || *Microphone does not work
|-
| ProBook 450 G5 || 2019-05-26 ||  ||  ||  ||   ||  ||  || Fingerprint scanner: works with  and , see Fprint ||
|-
| ProBook 450 G6 || 2019-03-30 ||  ||  ||  ||  ||  ||  ||  ||  button light stuck on.  (Wi-Fi) cannot be set (the other "special" buttons are fine). Touchpad may lag after hibernation.
|-
| ProBook 440 G6 || 2019-11-12 ||  ||  ||  ||   ||  ||  ||  || Touchpad does not work after suspend: reload i2c_hid kernel module to fix
|-
| ProBook 440 G8 || 2024-06-16 ||  ||  ||  ||   ||    ||  || ||
|-
| ProBook 430 G6 || 2019-11-18 ||  ||  ||  ||  ||  ||  || Brightness control works after bios update (2019.11) with kernel 5.3.11Fingerprint scanner: Untested || Touchpad does not work after suspend: reload i2c_hid kernel module to fixSame workaround needed for Ethernet in a bridge
|-
| ProBook x360 435 G7 || 2021-11-23 || * ||  ||  ||  ||  ||  ||  || *Accelerometer does not work with  except with
|-
| ProBook 640 G8 || 2026-04-05 ||  ||  ||  ||  ||   ||  ||  ||
|-
|}

## Spectre
| Spectre x360 (2020) || 2022-02-26 ||  || * ||  ||  ||  ||  ||  || *See dedicated page.
|-
| Spectre x360 13-ap0xxxx || 2020-09-07 ||  || * ||  ||  ||  ||  ||  || *See dedicated page.
|-
| Spectre x360 15-bl1XX || 2021-03-25 ||  ||  ||  ||  ||  ||  || ||
|}

## ZBook
| ZBook 14u G6 || 2021-06-03 ||  ||  ||  ||  ||  ||  || ||
|-
| ZBook 14u G9 || 2023-12-20 ||  ||  ||  ||  ||  ||  || ||
|-
| ZBook Firefly 14 G10 A || 2024-06-14 ||  ||  ||  ||  ||  ||  || ||
|-
| ZBook Firefly 15 G7 || 2024-08-31 ||  ||  ||  ||  ||  ||  ||  ||
|-
| ZBook Power 16 G11 || 2025-03-18 ||  ||  ||  ||  ||  || * || ** || *  required   ** fprintd and  required
|}

## Troubleshooting
## UEFI boot loader not found
Even if UEFI, Arch Linux and (e.g.) GRUB are correctly configured and with the correct UEFI NVRAM variables set, the system may not boot from the HDD/SSD. The problem is that HP hard coded the paths for the OS boot manager in their UEFI boot manager to  to boot Microsoft Windows, regardless of how the UEFI NVRAM variables are changed. There are two workarounds:

## Using the "Customized Boot" path option (recommended, may not be available for all models)
The latest HP firmware allows defining a “Customized Boot” path in the UEFI pre-boot graphical environment.
Select the “Customized Boot” option in the UEFI pre-boot graphical environment under “Boot Options” and set the path to your OS boot loader on the ESP (see EFI system partition), e.g.:

Always verify the correct path to the .efi file. Also, adjust the device boot order (also in the UEFI pre-boot graphical environment) to boot this entry first.

## Change the OS boot loader path to match the hard coded path
Change the UEFI application path of the OS boot loader to that hard coded path.
On your EFI system partition; e.g. with  being the EFI system partition mountpoint:

 # mkdir -p esp/EFI/Microsoft/Boot
 # cp esp/EFI/grub/grubx64.efi esp/EFI/Microsoft/Boot/bootmgfw.efi

or

 # mkdir -p esp/EFI/BOOT
 # cp esp/EFI/grub/grubx64.efi esp/EFI/BOOT/BOOTx64.EFI

## Fan noise
Since Linux 4.1x, laptop's fan may not spin down to a lower rev step (and noise) effectively appearing stuck at higher spinning speed with no apparent temperature reason. Possible workarounds are loading a 3D application, a quick suspend to ram or power off for more than 10 minutes. If those tricks do not work, the max CPU frequency can be set to a lower one. See CPU frequency scaling#Setting maximum and minimum frequencies. Related: [https://bugzilla.kernel.org/show_bug.cgi?id=153281

## Compaq 8510w
Follow the steps outlined in Suspend and hibernate#Hibernation. The suspend to disk process works correctly, but the laptop does not power itself off. To fix this, create the following file:

This file tells systemd to write  instead of  to  before writing  to .

## Pavilion au624tx
For making the mute LED work, append  to 's kernel module parameters.

## Omen 15 ax210TX
For making the mute LED work, append  to 's kernel module parameters.

## ProBook x360 440 G1
For making the mute LED work, append  to 's kernel module parameters.

## ProBook x360 435 G7
## Fingerprint Reader
This Section applies if running  shows a line containing .
There's at least two firmware issues that may make the fingerprint reader not work. Both can be solved with fwupd. Running  shows two sub-devices belonging to the fingerprint reader: The "Prometheus" device and its IOTA Config.
* if  doesn't find the fingerprint reader, try using  to update its firmware (possibly enabling the lvfs-testing remote, see )
* if  now finds the reader, but shows something like , the version of  you're using likely has the bug that prevents it from updating the Prometheus IOTA Config. To fix this, remove fwupd and install an older version of the package (1.5.9 worked) and use it, like before, to update your firmware. It's possible that you'll have to download the firmware package manually from fwupd.org because of a mismatched sha1 checksum in the automatic download. Don't forget to run  afterwards to remove the outdated  package.
* An additional step that may help is resetting the reader's own storage from the BIOS setup, hit  during boot-up to enter the BIOS setup and check the "reset fingerprint on boot" checkbox in the Security section. Make sure none of the operating systems that are currently installed require a fingerprint for anything, though.

## EliteBook U82 family (835 G9/845 G9/865 G9/845 G10)
## Flickering or constant solid white screen
Upgrade to kernel >= 6.2.7 and add the following to your kernel boot parameters:

 amdgpu.sg_display=0

Check it the parameter was applied successfully with:

 $ cat /proc/cmdline

Driver issue tracker: GitLab

## CPU Freq locked at 400-500MHz after AC power unplugged
For EliteBook 845 G10 with AMD Ryzen 7 PRO 7840HS, the CPU frequency may be locked at 400-544MHz when switched to battery, a workaround is to blacklist the `amd_pmf` module.

Driver issue tracker: Bugzilla

## Hardware buttons for volume do not work
If the hardware buttons for volume don't work, add  to 's kernel module parameters.

## Omen 16 ap0032ns
After shuting down from a Linux distribution, HP Omen 16 does not fully shutdown all the devices causing battery draining or energy draining when plugged. This may heat up the PC over 85ºC overnight possibly breaking the components. Unfortunately the latest BIOS (F.06) does not resolve the issue.

To be able to use Arch Linux (and any Linux distribution) there are two ways:

# After shutting down, press the shutdown ACPI button during 5 seconds. This will trigger a hardware shutdown, avoiding any power consumption.
# When using Windows dual boot, boot Windows and shut it down from there.
