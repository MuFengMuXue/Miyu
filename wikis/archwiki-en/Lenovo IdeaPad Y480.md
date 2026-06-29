# Lenovo IdeaPad Y480

The Lenovo IdeaPad Y480 is compatible with Arch Linux for the most part. However there are some tidbits we need to tweak in depending on our needs. This article, like many others in this wiki, assumes the user has already read through the Installation guide and related articles and has installed most, if not all, of the needed drivers. We will focus mostly on tweaking the system.

## Intel graphics
This machine has two video cards, an Intel HD 4000 integrated chip and a discrete NVIDIA Geforce 640M LE.

If you only wish to disable the NVIDIA video card and only use the Intel chip for improved battery life, lower temperatures, or less complexity, you can simply install  and then  enter the BIOS and on the "Configuration" tab, change "Graphic Device" from "Switchable Graphic" to "UMA Graphic". If these options are not there, you may need to update the BIOS.  This will leave the NVIDIA card without consuming power.

## NVIDIA graphics
The Intel video card cannot be disabled in the BIOS, so the NVIDIA Optimus technology residing in the machine must be configured in order to access the NVIDIA graphics. See the wiki page on NVIDIA Optimus for an in-depth description of the process.

## Low ALSA Audio
Compared to the audio volume in a Windows OS with the correct Realtek HD drivers, the sound volume in Arch Linux is rather low even with the current ALSA drivers. This is due to ALSA not correctly identifying the sound card's model. We can fix this by using  as explained in Advanced Linux Sound Architecture/Troubleshooting#Wrong model autodetection.

## Removing the WWAN/WLAN Whitelist
According to a techinferno post (Original post here) the BIOS contains a whitelist of wwan/wlan cards. In order to install a wireless card not listed in the whitelist, we need to download and install an unlocked BIOS which can be found here. Once installed, the whitelist will be removed and a lot of hidden BIOS options for tweaking the system will be available.

The provided BIOS package from the downloads page will not install unmodified due to missing a PTDIS parameter in the platform.ini in the third line. The resulting line should be:

 SwitchString=ACEN DCEN CPVER:FHRST RESSEN PTDIS

A working download can be found [https://drive.google.com/folderview?id=0BzueXo1sGj4uaFhDakZLZUFJaXc&usp=sharing here
