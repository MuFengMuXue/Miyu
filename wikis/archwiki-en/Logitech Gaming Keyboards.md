# Logitech Gaming Keyboards

Some Logitech Gaming Keyboards can work on Linux through Unofficial drivers. There are a few packages available
* the python based Gnome15 project
* the C based g15daemon project.
* https://github.com/tolga9009/sidewinderd
* https://github.com/Wattos/logitech-g710-linux-driver
* https://github.com/MatMoul/g810-led
* Animation support with C++ based Keyleds project.
* Gkeys support for G910 Orion Spectrum/Spark:  (https://github.com/JSubelj/g910-gkey-macro-support), or a fork of it supporting M keys and their profile changing ability here (https://github.com/MR-R080T/g910-gkey-macro-support)
* Some Logitech gaming mice and keyboards are remappable using  and . The app includes basic LED led customization and a simple graphical interface.
* LED customization support is available through  for most keyboards.
* basic control and LED effects can be set up using  or

## Install
 and its dependencies are available in the Arch User Repository (AUR). G15daemon drivers still work for the keyboards they supported, but their development was mostly dropped in 2008, the source is still available for anyone to pick up and continue their development, there are a few bugs in them that were never solved. These drivers use the  to interact with the G keys. There is also a  plugin to show system information on the LCD display.

 is available through Arch User Repository. Detailed configuration, effects and LUA scripting are in the project's documentation.

## Supported Models
g15daemon supports:

*G15 (Orange and Blue)
*G11
*Gamepad
*G510 (Requires Patching; Read below)

Gnome15 has a list of supported devices on its front page. The keyboards are:

*G19
*G19s
*G15 (Orange and Blue)
*G13
*G110
*G510 and G510s (Partial)

 supports:
* G710 / G710+
* G105
* (and Microsoft SideWinder X4 / X6, hence name)

 supports:
* Logitech G710 / G710+

 led supports:
* G213
* G410
* G413
* G512
* G513
* G610
* G810
* G815
* G910
* GPRO

 led supports (possible lua scripting):
* G410
* G610
* G810
* G910
* GPro

## G510 on g15daemon
[https://bbs.archlinux.org/viewtopic.php?pid=1421825 Forum Thread (This thread has more detailed instructions and might be helpful for readers from other distributions or less advanced users, it also contains a list of known issues.)

A patch was written to make the G510 keyboard fully compatible with the g15daemon drivers. It is however not compatible with g15macro and as such an alternative approach was needed (which involved heavy modifications of the original code) the result yields much better performance for than using the gnome15 drivers which can currently result in severe input lag for this keyboard.

To apply the patch you must download the  and  sources.

Then download the libg15 and g15daemon patches and modify to your will. The color profiles per M-Led settings are hard coded into the libg15 patch at line 341, 344, 347 and 350 in R,G,B color code.

Then place the files (libg15.patch and g15daemon.patch) into the folders that your packages were downloaded into, after this you must replace the PKGBUILDS with the new ones: g15daemon, libg15
These new PKGBUILDS refer to local sources only, this means they do not fetch sources from the net if they are not present so make sure you hold on to your tar.bz2 files. If you want them to fetch these from the net you can refer to the original PKGBUILDs.

Now install the packages,  comes first,  is required as well before you install g15daemon:

 $ makepkg -fic

This will compile, install and clean up the extracted sources afterwards to avoid cluttering the folder. I also recommend installing  from AUR next. For fluff.

After the installation you need to create the macro script files, and place them into . If you want to create them yourself the files need to be executable and the filenames are corresponding to the label on each key (so for the G1 key use ). Normally these files should use the bash script syntax.

For commands on the G keys to work with graphical applications g15daemon must be started after the X11 session. To do this you must add these commands to your autostart/xinitrc:

 $ sudo g15daemon && sleep 3 && g15stats

And congratulations! you have a working G510 keyboard on Linux :) With a few issues of course (known issues are in the forum thread linked to at the start of this section)
