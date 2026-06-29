# ICC profiles

As it pertains to general desktop use, an ICC profile is a binary file which contains precise data regarding the color attributes of an input, or output device. Single, or multiple profiles can be applied across a system and its devices to produce consistent and repeatable results for graphic and document editing and publishing. ICC profiles are typically calibrated with a (tristimulus) colorimeter, or a spectrophotometer when absolute color accuracy is required.

## Utilities
*
*
*
*
*
*

## Profile generation
Color management is a workflow of hardware calibration, software profiling and embedding the profile into the picture or video. It is all based on using an ICC profile.

## Colorimeter or spectrometer
It is highly recommended to use a colorimeter or spectrometer device for hardware-assisted display, printer and scanner calibration. For home use there are several affordable colorimeters available. Some are well- or even better-supported under Linux than on other operating systems. Frequently recommended devices are X-Rite ColorMunki Display and DataColor Spyder5 Express. You can find more Linux-supported devices listed in the AgyllCMS documentation.

## Argyll CMS
The Argyll Color Management System is a complete suite of command-line profile creation and loading tools listed under .

Review the official Argyll CMS documentation for details on how to profile selected devices.

## Monitor calibration and profiling with additional calibration hardware
There is a GUI frontend for ArgyllCMS called DisplayCal, available as . In most common cases you will want to use its default settings. It is a common way to calibrate to a daylight color of 6500K and gamma 2,2. Read the DispalGui documentation for more. Many tutorials are available on the net.

## Scanner calibration
Follow the scanner part of the scanner calibration tutorial.
Sometimes the vendor drivers for Windows includes the ICC profiles: extract the vendor setup.exe and the maybe contained CAB files and search for .ICC files. The  util may help you to verify the content, e.g. "...Microsoft color profile 2.0, type Lino, RGB/Lab-scnr device...".

## Printer calibration
See .

## File transfer
Profile generation on a Windows or macOS system is one of the easiest and most widely recommended methods to obtain a ICC monitor profile. Since ICC color profiles are written to an open specification, they are compatible across operating systems. Transferring profiles from one OS to another can be used as a workaround for the lack of support for certain spectrophotometers or colorimeters under Linux: one can simply produce a profile on a different OS and then use it in a Linux workflow. Note that the system on which the profile is generated must host the exact same video card and monitor for which the profile is to be used. Once generation of an ICC profile, or a series of profiles is complete on a Windows system, copy the file(s) from the default path:

 C:\WINDOWS\System32\spool\drivers\color

macOS generally stores ICC profiles in:

*
*
*

Once the appropriate  files have been copied, install the device profiles to your desired system. Common installation device profiles directories on Linux include:

*
*
*

## Gnome Color Manager
On Gnome, an ICC profile can easily be created by using . Under Gnome, this is accessible via the Control Center and is pretty straightforward to use. You will need a colorimeter device to use this feature.

## ThinkPads
See color profiles for IBM/Lenovo ThinkPad notebook monitor profile (generic) support.

The ThinkWiki instructions can be used to extract other ThinkPad driver executables from Lenovo, such as the Monitor INF File for Windows 11 for X1 Carbon Gen 10, X1 Yoga Gen 7, Z13, Z16.

## Loading ICC profiles
ICC profiles are loaded either by the session daemon or by a dedicated ICC loader. Both Gnome and KDE have daemons capable of loading ICC profiles from . If you use colord in combination with either  or , the profile will be loaded automatically. If you are not using either Gnome or KDE, you may install an independent daemon, xiccd, which does the same but does not depend on your desktop environment. Do not start two ICC-capable daemons (e.g. gnome-settings-daemon and ) at the same time.

If you are not using any ICC-capable session daemon, make sure you use only one ICC loader - either xcalib, dispwin, dispcalGUI-apply-profiles or others. Otherwise, you can easily end up with an uncontrolled environment. (The most recently run loader sets the calibration, and the earlier loaded calibration is overwritten.)

Before using a particular ICC loader, you should understand that some tools set only the calibration curves (e.g. xcalib), some tools set only the display profile to X.org _ICC_PROFILE atom (e.g. xicc), and other tools do both tasks at once (e.g. dispwin, dispcalGUI-apply-profiles).

## xiccd
 is a simple bridge between colord and X. It allows non-GNOME and non-KDE desktop environment to load and apply icc profiles.

Make sure  is installed, then install .

Copy your icc profiles to the profile directory.

 # cp icc_profile /usr/share/color/icc/colord/

Start .

If  was already running, you need to restart , otherwise new profiles will not show up.

Execute  in a terminal as a backend and ignore any verbose messages. Keep  running during the next steps.

 $ xiccd

This will enumerate displays and register them for colormgr(colord).

Open another terminal and execute . Note the  of your screen.

 $ colormgr get-devices

Note the  which you added earlier and want to use.

 $ colormgr get-profiles

Add your profile to the display device.

 # colormgr device-add-profile device_id profile_id

Make the profile as the default to the display device.

 # colormgr device-make-profile-default device_id profile_id

Double-check that  installed  so that it autostarts at system startup.

 # cat /etc/xdg/autostart/xiccd.desktop

Close all terminals, and reboot the system to check whether the icc profile is being applied.
If  was already running, you need to restart .

## xcalib
xcalib is a lightweight monitor calibration loader which can load an ICC monitor profile to be shared across desktop applications. Install the package .

To load profile  in :

 $ xcalib -d :0 /usr/share/color/icc/P221W-sRGB.icc

This can be autostarted at the start of the Xorg server, the desktop environment or the window manager.

## dispwin
dispwin is a part of .

To load the profile  in :

 $ dispwin -d0 /home/archie/.color/icc/906w-6500K.icc

This can be autostarted at the start of the Xorg server, the desktop environment or the window manager.

## Wayland
Wayland supports color management through color profiles, but the user interface for managing these profiles is currently not implemented properly. However, you can manually add a color profile through the following steps:

Firstly, copy your .icc color profile file to the  directory.

Run  to obtain the available color profiles, and  to obtain the IDs of the attached devices.

To assign a color profile to a device, use the command . The device ID is obtained from the output of  and the profile ID from .

For example, if your device ID is "DP-3" and the profile ID is "icc-5fb87663ba378cadf463ba64d92dced3", the command would look like:

 $ colormgr device-add-profile DP-3 icc-5fb87663ba378cadf463ba64d92dced3

With these steps, you can manually manage your color profiles in Wayland until the user interface is fully implemented. Once the ICC profile is added with this method, it will show up and work as expected in system settings like Color Manager in the KDE Plasma settings.

## Applications that support ICC profiles
* Xsane can use ICC profiles for color-corrected scanning.
* CUPS can use ICC profiles for color-corrected printing using Colord, but the actual implementation and usability is unclear.
* GIMP can use ICC profiles for display of the image being edited. The use of the installed ICC profile has to be explicitly enabled in the settings dialog: Image > Color Management > Assign Color Profile. Do not forget to include the profile when saving/exporting the image.
* mpv can take an ICC profile into account when playing a video. The command line argument is:  or . Only  and  do color management; compatibility/fallback VO drivers will silently ignore the ICC profile options.
* Firefox, by default, uses the system-wide ICC profile only when displaying images that are already tagged with an ICC profile. To assume that untagged images use sRGB and apply color correction also to them, set the  preference to 1. Firefox can also use an ICC profile using the configuration option .
* Both Eye of Gnome () and Eye of MATE () automatically use the system-installed ICC profile.
* scanimage from  package can include an ICC profile into a TIFF file with the  option
