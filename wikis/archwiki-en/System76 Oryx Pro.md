# System76 Oryx Pro

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
! !! !!
|-
| Audio ||  ||
|-
| Webcam ||  ||
|-
! !! !!
|-
| Bluetooth ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|-
! !! !!
|-
| Card reader ||  ||
|-
| Fingerprint reader || ||
|-
! !! !!
|}
This article is specifically about the System76 Oryx Pro versions 6-8, all of which share the same chassis and a very similar architecture.

## Booting
The System76 Oryx Pro comes with two NVMe M.2 slots. Older models (pre-oryp6) have space for a 2.5" SSD/HDD. Booting from NVMe requires the use of EFI, while booting over SATA/AHCI does not. If you are not sure what to use, EFI is a sensible and safe default for all configurations of this machine.

## Accessibility
## BIOS
The BIOS menu is extremely minimalist, with essentially no settings outside of boot order. All entries can be accessed from the keyboard, and should be easy to OCR.

There is no official documentation around which buttons to press to enter the BIOS. The splash screen says that  opens the overall BIOS menu, and  starts the Pop!_OS recovery partition.

Within the BIOS menu, you can use the arrow keys (/) to move the cursor, the Enter/Return key to activate or save things, / to relocate things, and  to cancel an operation or to go back to a previous menu. All lists are vertical, and progress from top-to-bottom.
# The first option in the BIOS menu is Boot Default, and it is where your cursor starts out. Activate this to continue the boot as if you had not pressed  at all.
# The second option is One Time Boot. This provides a menu of all boots known to the BIOS, in the order the BIOS knows to boot them. The cursor starts at the top of this menu. Activate one to boot to it.
# The third option is Change Boot Order. This one is a bit odd, as you have to press  twice to use it, after which you will be in an ordered list of possible boots, which can be mutated using the controls describe above. Note that  must be pressed twice to return to the main menu. There is an open ticket to simplify this flow here.
# The fourth (and final) option is Firmware Configuration Information. This page simply lists information about the firmware.

## LEDs
There is no diagnostic LED on the motherboard. The official technical documentation does not discuss whether the motherboard beeps when there is an issue, nor does it say what such beeps could mean.

There are three status LEDs on the front-left of the bottom half of the laptop. The left LED is for power, the center LED is for the battery, and the right LED is for IO. More information can be found in the official technical documentation.

## Installation
System76 develops a special distribution (Pop!_OS) for their computers, and it comes with many tweaks and tools to ensure a seamless end-user experience. Arch does not have these out of the box; and unfortunately, sometimes their computers do not work right without them. Thankfully, it is possible to get the same first-class hardware support in Arch Linux that you have in Pop!_OS -- it just takes a little elbow grease.

The rest of this article will assume you have followed the steps given in this section.

## Recovery partition
If you are replacing Pop!_OS on the NVMe that came with your laptop, it is recommended to leave the recovery partition intact. The BIOS is hard-coded to attempt to boot this on , and this recovery partition can be a handy way to get out of a tight spot if something should happen that renders your Arch install unbootable.

System76 automatically updates this recovery partition from within Pop!_OS; at present, it is not known how to update it from within Arch Linux.

It may be possible to replace the contents of this recovery partition with any LiveCD you want, but as of now it is not known if anyone has tried.

Note that the normal boot process as well as the UEFI boot menu both work fine without the Pop!_OS recovery partition, it is just that the  shortcut will not work. So if you are fine with using a live ISO or another partition that you prepare manually as recovery, that will not be a problem. You can for example have another normal Pop!_OS installation as a separate partition that you boot into for recovery operations via the UEFI boot menu.

## Packages
It is recommended to install everything in the list below.

There are also "-git" versions of many of these packages, if you wish to be bleeding edge.

## Modules
*
*
*

## Daemons
*
*  (needed for System76 switchable graphics and charging thresholds)
*  (seems to be needed for things like audio to work right)

## Activation
Once you have installed the above, you will need to tell your computer to use them.

## Services
Enable the following services: (source)

*
*
*  (the systemd service has a different name than the package)

## Modules
To make sure all drivers are being loaded correctly, run ; this will automatically add necessary rules to , and execute .

## Firmware
Install the following:

*  (required if you want to know when there is a BIOS update available)
*  (required if you want to update your BIOS)

To check your current BIOS version and whether there is a new version available, run  as root. Keep in-mind that this is a GTK application, so you need to be running X or Wayland for it to run. (It has no CLI -- it does not even respond to .)

To update your system to the latest firmware on the next boot, run .

## EC
"EC" refers to the "embedded controller", and is where the bulk of user-relevant settings exist in the BIOS.

System76 may not provide firmware updates for your model forever; and those they do provide often do not come out in a timely manner. Thankfully, you can flash the latest version of the EC from GitHub (with all its numerous fixes) yourself, by first cloning the repository and then running the following command:  -- just make sure to replace  with your actual model (e.g. "oryp8"). System76 performs QA on all PRs before they are merged into master, meaning that master can generally be considered stable.

## BIOS Settings
## Boot entries
The boot screen seems to never remove old, broken entries; so if you have installed several times, you will need to remove these dead entries yourself. The command for this is  (replace  with the index you would like to remove) (source). It is safe to remove not-dead entries; the BIOS seems to automatically detect and re-add them.

## Fan curve
The Oryx Pro's fan curve is hard-coded, meaning you have to configure, compile, and flash your own custom version of the EC in order to change your fan curve. (There is an open issue to add runtime-configurable fan curves here.).

The default fan curve for the all System76 computers is designed to minimize noise (source). Unfortunately, in the Oryx Pro's case, this goal is taken to an extreme:  by default, the fans will only reach 100% at 90°C; and your CPU starts to throttle well before that point. By setting a custom fan curve that reaches 100% at Tjunction (typically a few degrees above 70°C), you can easily avoid such unnecessary throttling.

There is a PR available that fixes these issues for the oryp7.

## Voltages
There is no user-configurable option to change voltages at the BIOS-level. However, some have managed to disable the Plundervolt mitigations, in doing so re-acquiring the ability to undervolt their Oryx Pros from userland. There is an issue on GitHub requesting a toggle in the BIOS for this mitigation.

## Secure Boot
System76's implementation of Coreboot supports Secure Boot as of 2023-03-22, and an official release of this firmware exists for the Oryx Pros covered by this article.

## Graphics
This system comes complete with an integrated (Intel) and discrete (NVIDIA) graphics card. The external ports (DP over Mini-DP, DP over USB-C, HDMI) are tied to the discrete NVIDIA card.

Graphics options:

* System76: If you want to use the hybrid graphics mode developed by System76, follow the instructions in #Installation and #OEM switchable graphics. This seems to use PRIME behind the scenes.
* Bumblebee: Some users have reported getting success with Bumblebee. Your mileage may vary if you are using a more complete DE like GNOME; this has only been tested with .
* NVIDIA: When in doubt, NVIDIA's official drivers should always work.

## OEM switchable graphics
To enable System76's switchable graphics, run  once; and then put  before every application you want to start with your dGPU. Note that this will only work for applications that use GLVND. (source)

To verify whether switchable graphics is working, run  and . These commands should succeed and have different vendors. If the latter command fails, go to #prime-run not working. (Note that you can limit the output to just the relevant information by appending  to the aforementioned commands.)

## NVIDIA graphics
On some System 76 hardware it is impossible to use an external monitor without very noticeable lag just moving the cursor around a desktop environment, unless using the NVIDIA graphics card exclusively. On Pop!_OS this is accomplished by changing the graphics mode to NVIDIA in the menu, but that just runs  so you can do this manually on Arch. The main important thing that it does is write a config file into  like this, which causes X11 to use the NVIDIA graphics card as the primary GPU, rather than using the integrated graphics card by default and rendering specific applications on NVIDIA:

Note the mention of X11 specifically. Yes, the  power utility is apparently hardcoded for its NVIDIA graphics mode to only configure X11 properly, even though the latest Pop!_OS uses Wayland. This has been reported upstream. As a workaround, if you require NVIDIA graphics mode on Wayland, you can configure your desktop environment manually. For example, here are the instructions for GNOME.

Another thing to note is that  does not actually check the system configuration before reporting what it thinks the current mode is. By default it will say the mode is  after installation, even though it is not. You still need to run  one time to generate the config files.

## Audio
Audio should work fine out-of-the-box.  If audio worked in Pop!_OS, you are probably just missing a kernel patch that has not yet been mainlined.  Your options are (1) patch the kernel yourself, (2) wait for the patch to be added to the official Linux kernel, or (3) attempt a workaround.

As an example of option #3, in case this is any help for future issues:  At release, audio on the oryp7 and oryp8 could be made to work by adding  to , which got the kernel to use the  quirk (source);  but this was not always a perfect fix (source).

## Quality
The speakers in the Oryx Pro 7 (and likely also those in the oryp6 and oryp8) are very low-quality.  The two speakers are likely to play at noticeably different volumes, and many pitches play distortedly.  You are probably going to want to install  to help you correct for some of these deficiencies, as it will give you access to a system-wide equalizer.  Setting a high pass at around 96 Hz can prevent beating noises at low pitches.  Pitches between around 96 Hz and 512 Hz can, if made loud enough, suddenly transition to a higher pitch and much higher volume, and there really is no good way around this other than carefully configuring your equalizer.  Setting a low pass at around 12 kHz can help avoid issues where high sounds play at a much lower pitch and higher volume.

## Microphone
The microphone on the oryp7, when run at 100% volume, will produce horribly clipped and distorted sound.  Lower the volume to around 33% (1/3), and the mic will start to sound good.

You will want to use  on the mic, as well, since it has no noise cancelling by default and is very prone to picking up the laptop's fans.

## Network
## Ethernet
The oryp7 has a Realtek ethernet chip whose in-tree Linux driver is (as of Linux v5.15) guaranteed to fail link autonegotiation. You can work around this issue by manually setting your onboard ethernet's link negotiation to 'ignore' or '100mbps' (How you do so depends on your computer's network manager.); however, both options mean that your Internet speed will be capped at 100mbps. In order to get your ethernet port to work at speeds above that, you will need to install Realtek's out-of-tree driver, with , , or  (Although r8168 is out-of-tree, it is still open-source and GPL-licensed.). Once installed, you need to blacklist the default r8169 driver: .

## Wi-Fi
Wi-Fi may not work before you have installed the requisite System76 packages, as listed above.

## Suspend/Hibernate
See Power management/Suspend and hibernate and NVIDIA/Tips and tricks#Preserve video memory after suspend.

## Function keys
: Only keys with known functions are shown.

{| class="wikitable" style="margin: unset;"
|+ style="text-align: left;"| Oryx Pro 6-8
! style="width: 1rem; height: 1rem;" |
! Key
!title="The key is visible to `xev` and similar tools."| Visible?
!title="The physical key has a symbol on it, which describes its function."| Marked?
! Effect
|-
! rowspan="5" style="writing-mode: vertical-lr;" | Control
|-
| 1+ ||  ||  ||
|-
| 2+ ||  ||  ||
|-
| 2++3 ||  ||  ||
|-
| ++3 ||  ||  ||
|-
! !! !! !! !!
|-
! rowspan="5" style="writing-mode: vertical-lr;" | Display
|-
| + ||  ||  || Toggles power to the display
|-
| + ||  ||  || +4
|-
| + ||  ||  ||
|-
| + ||  ||  ||
|-
! !! !! !! !!
|-
! rowspan="5" style="writing-mode: vertical-lr;" | Keyboard
|-
| + ||  ||  || Changes keyboard color
|-
| + ||  ||  || Toggles power to keyboard backlight
|-
| + ||  ||  || Dims keyboard backlight
|-
| + ||  ||  || Brightens keyboard backlight
|-
! !! !! !! !!
|-
! rowspan="5" style="writing-mode: vertical-lr;" | Media
|-
| + ||  ||  ||
|-
| + ||  ||  ||
|-
| + ||  ||  ||
|-
| + ||  ||  ||
|-
! !! !! !! !!
|-
! rowspan="6" style="writing-mode: vertical-lr;" | Misc
|-
| + ||  ||  || Toggles max state of fans
|-
| + ||  ||  ||
|-
| + ||  ||  || Toggles power to the webcam
|-
| + ||  ||  ||
|-
| + ||  ||  || Suspends the computer
|-
! !! !! !! !!
|}
# The  in this combo is ignored on older versions of the EC.
# The  in this combo is ignored unless you have compiled and flashed an unreleased version of the EC.
# / and / have the same scancodes on PS/2-style keyboards, so they require additional modifiers for the OS to understand them. (source)
# This key depends on your layout, and may be different if you are not using QWERTY.

## Keyboard lighting
You can control the brightness and color of your keyboard's LEDs. To do so, install  and then run , with  being how bright you want the keyboard (on a scale of 0-255) and  being a 6-digit color hex (e.g. ""). Since the keyboard's LEDs are controlled from the commandline, it is possible to script patterns and light shows.

Note that these settings are not maintained across boots; so you will need to reapply them on startup.

## Hardware
The Oryx Pro 7 (and likely also its cousin models, 6 and 8), while a capable machine, has a number of noticeable shortcomings in hardware that, thankfully, can be largely resolved by a little elbow grease.

## Model correspondences
The Oryx Pro, like most (all?) System76 laptops to-date, are derived from Sager/Clevo models. The below table shows which models correspond to each other. This can be useful when shopping for parts online.

{| class="wikitable"
! System76 !! Clevo !! Sager
|-
|  || ||
|-
|  ||  ||
|-
|  || ||
|}

## Heatsinks
## Thermal paste/pads
As confirmed to an attendee of Southeast Linuxfest 2022 by a System76 employee, System76 (like most OEMs) uses the cheapest, most-generic thermal paste it can find, in order to reduce costs at scale. Repasting your CPU/GPU can result in noticeable improvements to the speed at which they decrease in temperature after a spike, but it will not prevent such spikes from happening; see the "Main heatsink" subsection here for information about why that is.

Upgrading the stock thermal pads can also improve heat transfer, but System76 has confirmed (via support ticket) that it does not have any documentation on the proper thicknesses to use for these pads, meaning that replacing them bears risk that replacing the paste does not.

## Main heatsink
The heatsink that cools the CPU and GPU does not have enough thermal capacity to cool them (the CPU especially). What this means, in practice, is that you will see WILD temperature swings at even mild usage:  it is common to see going from 1% usage to 10% usage result in a jump from 50°C to 90°C in less than a second. The only solution to this, is to add more thermal capacity to the heatsink. The easiest and cheapest way to do this, is to lay thermal pads on-top of the main heatsink, until those pads start to squish into the aluminium chassis at the bottom. This will substantially ameliorate such jumps in temperature, and the corresponding fan spin-up that follows them. (source)  An added benefit of tying your main heatsink to your bottom chassis, is that the bottom chassis is fan-cooled, just like your main heatsink -- which means that not only are you adding extra thermal capacity, you are also increasing the amount of active cooling you have.

## PCH
The PCH comes without a heatsink, and will idle around 85°C. This is obviously not good for longevity. Adding a small heatsink to it can make a nice difference; but you can get an even bigger one by first building up the area around the PCH with thermal tape until you are level with the die, and then affixing a wider heatsink to the whole area. Yet more gains can be had by removing the insulating plastic directly above this heatsink, and replacing it with a thermal pad; this will create thermal contact between your DIY PCH heatsink and the laptop's aluminium chassis. Combining all of these tricks gets a PCH that idles around 40°C -- that's an unheard-of 45°C drop.

## Wi-Fi card
The Wi-Fi card comes without a heatsink, and can idle around the 65°C range. Adding a heatsink and ensuring thermal contact with the aluminium chassis can lower this by 15°C.

## Noise
## Fans
Many, though not all, users have reported hearing a "clicky" noise in the fans when they spin up or down. System76 has introduced a 25% floor for fan speeds, in an effort to reduce this; but it still happens for some users, especially when the fans turn on and off. The "best" solution, if you are affected by this, is to file a ticket with System76 support, asking for new fans. If you are under warranty, these should be provided to you if you can procure an audio recording of the clicking; if you are not, then you will have to pay for the fans.  It may also be helpful to demonstrate that your fans, when run at the same percent, have significantly different speeds.

In addition to or as an alternative to replacing the fans, you can also try changing the speed floor. Some people will be able to use values as low as 20%; others may need to go up to 30% or higher. See #Firmware for more information around how to change your fan curves.

A maximally effective solution is to set your fans to turn on at 0°C at the speed floor;  then, try progressively lower and lower speed floors, until you reach the one where the fan continuously clicks.  Increase that number by 1;  that is the minimum quiet speed for your fans.  This solution completely avoids the clicky sounds you hear on spin up/down, except for when the system turns on/off.  This solution will also, for most users, allow the fans to spin at lower speeds than the default floor of 25%.

## Coil whine
Some users report very noticeable coil whine. There is not much that can be done about this, but you can try coating your motherboard and other components in insulating varnish, taking great care to avoid coating surfaces you might want to attach thermally-conductive material to later-on. This coating may not completely resolve the issue, but it should help to mute it somewhat. Beware, though, that such varnishes are typically seriously toxic, and significant precautions may be necessary for you to work with them safely.

Working around the fan creaking/clicking on spin-up/spin-down by running the fans 100% of the time helps to mask the coil whine.

## Keyboard
## Spacebar actuation issues
The space bar may never actuate if pressed on its sides (demonstration), and this seems to be a common problem ([https://www.reddit.com/r/System76/comments/impqaz/comment/jncw7sz/?utm_source=share&utm_medium=web2x&context=3). This is because it is quite flimsy and not built within tight tolerances, meaning that pressing down on one end not only bends that end down more than the rest of the key, but also raises the other end of the key up. These two factors result in the actual space button (located dead-center) never actuating.

One option for fixing this may be to replace the stabilizers, since this will stiffen the key. The stock stabilizers are made of some magnetic, springy material (almost certainly some kind of steel), and are 20ga thick. Unfortunately, it is exceedingly difficult to find a stiff steel wire at that thickness; and no other thickness will work, because your replacement wire has to fit into the tiny hooks on the underside of the key.

An option for working around this issue (without actually fixing it), is to shim the center of the key. This can be done with something as simple as duct tape. One piece is not enough, two pieces effectively fixes the issue (maybe 98% of the time), and three pieces is too thick (causes the key to fire endlessly much of the time, and ruins the feel of the keypress).

An alternative to duct tape that will also add some extra rigidity to the key (thus helping fix the actual issue, rather than just working around it) is to pour a layer of epoxy or superglue into the "bowl" made by the center stabilizer (which forms a kind of loop around the key). However, this is a very permanent solution, and if you make the key too thick, you will have trouble ever making it thinner again.

## Spacebar stabilizer issue
The central spacebar stabilizer may eventually decide it no longer wants to stay attached to the spacebar.  Should this happen, just leave the stabilizer off -- it does not actually seem to make a noticeable difference in typing, at least if you have shimmed the spacebar as per the above.

## Ethernet jack
The Ethernet jack does a very poor job of holding cords still, and the wires inside it are quite delicate.  You may run into enough issues getting consistent Ethernet, that it becomes worthwhile to buy a replacement Wi-Fi card so that you can get Wi-Fi before you install the System76 packages listed here.

## Troubleshooting
## Unable to boot from USB
Boot to the BIOS menu, press  on the One Time Boot option, and re-plug your flash drive. The screen should freeze momentarily; after this, your flash drive should appear in the list.

## Weird hardware issues
Shut down − do not simply restart when encountering weird issues (e.g. where  throws a strange error, and rebooting does not help). As explained by a System76 engineer at Southeast Linuxfest 2022, shutting down hard-resets certain components that stay on during reboots.

Another possibility is that you are trying to run TLP or Laptop Mode Tools alongside  -- these packages conflict with each other, and combining them is not supported.

## Bad thermals
For software-level fixes, see #BIOS Settings.

For hardware-level fixes, see #Heatsinks.

## fancontrol not working
 does not currently support runtime configuration of fan speeds, so  and  will not work. There is an open feature request for this, though.

In the meantime, you can hard-code a custom fan curve per the instructions in #BIOS Settings.

## prime-run not working
Create a configuration file for Xorg: (source)

Change the  fields above to match the first field in the output of this command:  (you can omit leading zeroes). You will need to restart your X server for this to take effect.

## Xorg fails to start with "No devices detected"
If you find (normally after an update & restart) that launching X (via  or otherwise) does not work, you may confirm that the  device is installed and working by doing the following:

Confirm the error in . The  kernel module should successfully load. You may also confirm the error with  or .

Check whether both integrated and discrete graphics cards are available:

If you do not see the second entry (or some similar NVIDIA card), make sure the card has been turned on by  (use  to explore options):

 # system76-power graphics

Check whether the discrete NVIDIA graphics card is powered on using :

 # system76-power graphics power

To power the discrete NVIDIA graphics card on, supply "on" as an argument (i.e. ). After doing so and querying again, you should see:

Once the card is powered on, it should show up in the output of , and be detectable by Xorg, given that the appropriate NVIDIA driver is installed.

## system76-firmware: EFI mount point not found
If using the new (replacement) EFI mount point , ensure you have the mount present in . You may find the appropriate device to mount by using a combination of  and :

List disks (one device will be designated as EFI System):

 # fdisk -l

List devices and mount points, you should see the EFI system device, and confirm whether it is mounted/unmounted:

 # lsblk

Then mount the device:

 # mount device /efi

Optionally print the fstab configuration for inclusion/merging into :

 # genfstab -U /

After doing the above, it might be a good idea to schedule a firmware update:

 # system76-firmware-cli schedule

## With GRUB
After scheduling a firmware update, ensure that GRUB is set to use the EFI system partition like so:

 # grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=grub
 # cp /boot/grub/grub.cfg /boot/grub/grub.cfg.bak
 # grub-mkconfig -o /boot/grub/grub.cfg

Restart to trigger the firmware update.

## X does not start
If you have anything plugged-into the HDMI port on the back, this is why. Unplug your HDMI cord, boot the computer, and plug it back in after X starts. This issue only happens when the NVIDIA card is used for display, either in  or  mode; so if you do not want NVIDIA to do your graphics anyway, switching to  or  will fix this problem. If you actually do want to use your NVIDIA card, though, there is currently no known fix; but watching Linus swear at NVIDIA may prove therapeutic. Worth noting, though:  Pop!_OS handles this just fine, so there may be something missing in Arch that is not missing in Pop!_OS.

## Laptop powers off suddenly when under heavy loads
Known issue;  no fix yet.

You can mitigate the damage caused by this by ensuring that you do not set any options in fstab that increase your likelihood of losing data on crashes.

## Power cable disconnects randomly
No known solution.  To avoid additional annoyance, you should change your power settings to not change monitor or keyboard backlight brightness on power connect/disconnect.

## Screen falls out
Tape it back in.  And contact support;  you are not the first (or last) to have this issue.  (examples: To avoid this happening to you, never leave your Oryx Pro half-closed, because gravity is apparently strong-enough to pull the screen out overnight.

## Screw threads come out
There is really no way to repair these -- superglue is not strong-enough to hold them in-place.  The only solution is to replace the chassis, but it may be hard getting a warranty replacement on this basis alone.  The best option is probably to just stop using any corresponding screws.

## Keyboard backlight not turning on
If your keyboard backlight is no longer turning on, there is a chance this issue will self-correct, even if the backlight does not come on for a whole week. If you are still under warranty, it is likely you can get a replacement from System76 for this issue.  Otherwise, you may need to purchase a replacement keyboard.
