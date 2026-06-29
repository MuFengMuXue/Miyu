# Wine

Wine is a compatibility layer capable of running Microsoft Windows applications on Unix-like operating systems.

Wine does not use emulation, binary translation, or virtualization to operate. Instead, Wine provides an implementation of the Win32 API to applications that require it. As Wine's implementation of the Win32 API will naturally differ from what is provided by Microsoft Windows, applications may suffer behavioral, compatibility, or performance penalties when using Wine.

## Installation
Wine can be installed either through the  (development),  (stable) or  (testing) package. Wine Staging is a patched version of Wine, which contains bug fixes and features that have not been integrated into the stable or development branch yet.

If using , see #Using 32-bit Wine builds for additional requirements.

## Optional dependencies
Wine has numerous optional dependencies, which may not be required for basic applications, but should be installed to provide functionality such as sounds, 3D graphics, video playback, etc.

## Sound
By default sound issues may arise when running Wine applications. Ensure only one sound device is selected in winecfg.

## MIDI support
MIDI was a quite popular system for video games music in the 90s. If you are trying out old games, it is not uncommon that the music will not play out of the box.
Wine has excellent MIDI support. However you first need to make it work on your host system, as explained in MIDI. Last but not least you need to make sure Wine will use the correct MIDI output, though by default, no extra configuration may be required.

For MIDI tracks to play in-game, install Microsoft's General MIDI DLS Collection, DirectSound and DirectMusic using  or by searching for them on the dependency manager if using Bottles.

## Other dependencies
Some applications may require additional packages * For encryption support install
* For joystick and gamepad support install
* For media playback programs install , , ,  and
* For NTLM authentication install

## In-prefix dependencies
Aside from system dependencies, many programs require additional fonts and DLLs to be installed to the Wine prefix [https://gitlab.winehq.org/wine/wine/-/wikis/FAQ#my-application-says-some-dll-or-font-is-missing-what-do-i-do. To satisfy these dependencies you can use Winetricks, a primitive "package manager" where each verb either installs something or applies a configuration tweak. There are two ways to use Winetricks:

* Through the CLI: Run .
* Through the GUI: Install  or  then run .

Due to conflicts between dependencies, you may not be able to create the "perfect" Windows installation that can run everything [https://github.com/Winetricks/winetricks/issues/469. Rather, you should treat prefixes as disposable (unless they contain important configurations or data) and use separate prefixes for programs with different dependencies. You can use the #WINEPREFIX environment variable to control which prefix the verbs act on.

Determining the verbs required by a program needs can require much trial and error. See the Bottles dependency page for some of the more common dependencies, as well as the following program-specific resources:

* Wine Application Database. Official resource, but old and may be less maintained than others.
* Lutris website. If you are trying to run a game which happens to be featured on this site, you can click the drop-down menu and then View install script to see what Winetricks verbs are used by Lutris.
* Bottles program repository. Smaller, but not just games.
* ProtonDB. Although Proton has different compatibility than Wine (and you should probably just use Proton if you are on this site), the verbs commented by users may be of use.
** You can also consult the source for the fast-moving protonfixes tool that ships with proton-ge-custom, but beware that it assumes the presence of additional Proton and GE patches that fix games.

If you find yourself spending a lot of time managing prefixes for games, it may be easier to use a third-party application that handles it for you.

## Third-party applications
These have their own communities and websites, and are not supported by the main Wine community. See Wine Wiki for more details.

*
*
*
*
*
*
*
*
*

## Configuration
Configuring Wine is typically accomplished using:

* control — Wine's implementation of the Windows Control Panel, which can be started by running ,
* regedit — Wine's registry editing tool, which can be started by running —see also Useful Registry Keys,
* winecfg — a GUI configuration tool for Wine, which can be started by running .

See Programs for the full list.

## WINEPREFIX
By default, Wine stores its configuration files and installed Windows programs in . This directory is commonly called a "Wine prefix" or "Wine bottle". It is created/updated automatically whenever you run a Windows program or one of Wine's bundled programs such as winecfg. The prefix directory also contains a tree which your Windows programs will see as  (the C-drive).

You can override the location Wine uses for a prefix with the  environment variable. This is useful if you want to use separate configurations for different Windows programs. The first time a program is run with a new Wine prefix, Wine will automatically create a directory with a bare C-drive and registry.

For example, if you run one program with , and another with , the two programs will each have a separate C-drive and separate registries.

To create a default prefix without running a Windows program or other GUI tool you can use:

 $ env WINEPREFIX=~/.customprefix wineboot -u

## Fonts
If Wine applications have unreadable or missing fonts, you may not have any fonts installed. To easily link all of the system fonts so they are accessible from wine:

 $ cd ${WINEPREFIX:-~/.wine}/drive_c/windows/Fonts && for i in /usr/share/fonts/**/*.{ttf,otf}; do ln -s "$i"; done

Wine uses FreeType to render fonts, and FreeType's defaults changed a few releases ago. Try using the following environment variable when running programs in Wine:

 FREETYPE_PROPERTIES="truetype:interpreter-version=35"

Another possibility is to install Microsoft's TrueType fonts into your wine prefix. If this does not help, try running  first, then  as a last resort.

After running such programs, kill all Wine servers and run . Fonts should be legible now.

If the fonts look somehow smeared, run the following command to change a setting in the Wine registry:

 $ wine reg add 'HKEY_CURRENT_USER\Software\Wine\X11 Driver' /v ClientSideWithRender /t REG_SZ /d N

For high resolution displays, you can adjust dpi values in winecfg.

See also Font configuration#Applications without Fontconfig support.

## Enable font smoothing
A good way to improve wine font rendering is to enable cleartype font smoothing.
To enable "Subpixel smoothing (ClearType) RGB":

 $ WINE=${WINE:-wine} WINEPREFIX=${WINEPREFIX:-$HOME/.wine} $WINE regedit /tmp/fontsmoothing.reg 2> /dev/null

If you have installed , there is a simpler way to do this:

For more information, check the original answer

## Desktop launcher menus
When a Windows application installer creates a shortcut Wine creates a .desktop file instead. The default locations for those files in Arch Linux are:

* Desktop shortcuts are put in
* Start menu shortcuts are put in

## Creating menu entries for Wine utilities
By default, installation of Wine does not create desktop menus/icons for the software which comes with Wine (e.g. for winecfg, winebrowser, etc). This can be achieved by installing  or  meta-package (the latter has no additional dependencies), otherwise these instructions will add entries for these applications.

First, install a Windows program using Wine to create the base menu. After the base menu is created, you can create the following files in :

And create the following file in :

If these settings produce a ugly/non-existent icon, it means that there are no icons for these launchers in the icon set that you have enabled. You should replace the icon settings with the explicit location of the icon that you want. Clicking the icon in the launcher's properties menu will have the same effect. A great icon set that supports these shortcuts is .

## Removing menu entries
Menu entries created by Wine are located in . Remove the program's .desktop entry to remove the application from the menu.

In addition to remove unwanted extensions binding by Wine, execute the following commands: $ rm ~/.local/share/mime/packages/x-wine*
 $ rm ~/.local/share/applications/wine-extension*
 $ rm ~/.local/share/icons/hicolor/*/*/application-x-wine-extension*
 $ rm ~/.local/share/mime/application/x-wine-extension*

Sometimes you should also remove  files from  to completely remove items from Wine submenu in KDE.

## Appearance
A similar to XP-looking theme can be [https://archive.org/download/zune-desktop-theme/ZuneDesktopTheme.msi downloaded. To install it, see this upstream wiki article. Lastly, use winecfg to select it.

Wine staging users may instead want to try enabling the option Enable GTK3 Theming under the Staging section of winecfg for a theme that matches the current GTK theme.

## Printing
In order to use your installed printers (both local and network) with wine applications (e.g. MS Word), install the  package, reboot wine (wineboot) and restart your wine application.

## Networking
After installation, the  package may need to be installed for applications making TLS or HTTPS connections to work.

For ICMP (ping), Wine may need the network access as described in the WineHQ FAQ:

 # setcap cap_net_raw+epi /usr/bin/wine-preloader

If issues arise after this (such as an unhandled exception or privileged instruction), remove via:

 # setcap -r /usr/bin/wine-preloader

## Usage
See Wine User's Guide for general information on Wine usage.

See Wine Application Database (AppDB) for additional information on specific Windows applications in Wine.

## Wayland
The Wayland graphics driver is enabled by default, but the X11 driver still takes precedence if both are available To force using the Wayland driver in that case, make sure that the  environment variable is unset:

 $ env -u DISPLAY wine example.exe

To force Wayland prefix-wide, add a string value with name  and data  in

## Stop running Wine
Stopping started executables,  with Ctrl+Z or  with Ctrl+C, might leave processes running in the background. See for example:

All running  and  processes are stopped at once using the [https://gitlab.winehq.org/wine/wine/-/wikis/Wine-User's-Guide#-k-n wineserver -k command. For example:

 $ wineserver -k 15

This command is -dependent, so when using a custom Wine prefix, run:

 $ WINEPREFIX=~/wine/my-prefix wineserver -k

An equivalent command to gracefully finish both executables in the above example is:

 $ kill 997 1021

## 32-bit Windows applications
Upstream Wine supports three ways of running 32-bit Windows applications on a 64-bit system:

*  which runs Wine as a 32-bit Linux application in a 32-bit prefix.
* "Old WoW64", which runs Wine as a 32-bit Linux application in a 64-bit prefix. This allows 32-bit and 64-bit applications to coexist in the same prefix.
* "New WoW64". which runs Wine as a 64-bit Linux application in a 64-bit prefix. 32-bit Windows applications are supported via thunking to 64-bit Wine code. This is most similar to WoW64 on Windows.

Since Wine 10.8-2, Arch Linux enables the new WoW64 mode. Most 32-bit Windows applications will install and run without any additional steps needed.

## Using 32-bit Wine builds
While the new WoW64 mode will work for most applications, it has a few limitations:

* Any existing 32-bit  will no longer work, and should be recreated as 64-bit. Then 32-bit applications can be installed into it.
* A known limitation of the new WoW64 mode is reduced performance for 32-bit applications that use OpenGL directly. (Bug report).
* A few 32-bit Windows applications do not work correctly in WoW64 mode (under either wine or Windows).

As a workaround,  is an alternate wine package that provides 32-bit builds of wine. The  package also currently provides a 32-bit build. These packages require the host system to have 32-bit versions of libraries installed for Wine to be able to run 32-bit applications. Some common 32-bit libraries are listed below. When installing other libraries listed on this page (e.g. those listed in #Other dependencies), you should also install the corresponding  package if you are running a 32-bit application.

## Graphics drivers
You need to install the 32-bit version of your OpenGL graphics driver.

A good sign that your drivers are inadequate or not properly configured is when Wine reports the following in your terminal window:

 Direct rendering is disabled, most likely your OpenGL drivers have not been installed correctly

## Sound
Install the correct packages for the audio driver you want to use:

* For ALSA install  and
* For PulseAudio install
* For PipeWire install  and either:
**  and  to use PulseAudio as a frontend.
** , , and  to use ALSA as a frontend.
* For OSS install

If winecfg still fails to detect the audio driver (Selected driver: (none)), configure it via the registry. For example, to provide full access to the sound hardware (sound playback and mic): open regedit, look for the key HKEY_CURRENT_USER > Software > Wine > Drivers, add a string called Audio and give it the value . Also, it may help to recreate the prefix.

## WINEARCH
If supported, you can use  with  to make separate  and  (old WoW64) environments:

 $ WINEARCH=win32 WINEPREFIX=~/win32 winecfg
 $ WINEPREFIX=~/win64 winecfg

You can also use  in combination with other Wine programs, such as winetricks (using Steam as an example):

 WINEARCH=win32 WINEPREFIX=~/.local/share/wineprefixes/steam winetricks steam

In order to see the architecture of an existing prefix you can check its registry file. The command below reads the system registry of the  prefix and returns  or  depending on the architecture type:

 $ grep '#arch' ~/.wine/system.reg

## Tips and tricks
## Wineconsole
Often you may need to run .exes to patch game files, for example a widescreen mod for an old game, and running the .exe normally through Wine might yield nothing happening. In this case, you can open a terminal and run the following command:

 $ wineconsole cmd

Then navigate to the directory and run the .exe file from there.

## Winetricks
Winetricks is a script to allow one to install base requirements needed to run Windows programs. Installable components include DirectX 9.x, MSXML (required by Microsoft Office 2007 and Internet Explorer), Visual Runtime libraries and many more.

Install the  package (or alternatively ). Then run it with:

 $ winetricks

For using GUI you can install either (GTK) or (Qt).

## Performance
## CSMT
CSMT is a technology used by Wine to use a separate thread for the OpenGL calls to improve performance noticeably. Since Wine 3.2, CSMT is enabled by default.

Note that CSMT may actually hurt performance for some applications - if this is the case, disable it by running  and set the DWORD value for HKEY_CURRENT_USER -> Software > Wine > Direct3D > csmt to 0x00 (disabled).

Further information:
:Phoronix Forum discussion with the CSMT developer Stefan Dösinger

## Force OpenGL mode in games
Some games might have an OpenGL mode which may perform better than their default DirectX mode. While the steps to enable OpenGL rendering is application specific, many games accept the  parameter.

 $ wine /path/to/3d_game.exe -opengl

You should of course refer to your application's documentation and Wine's AppDB for such application specific information.

## DXVK
DXVK is an implementation of DirectX 8, 9, 10, and 11 over Vulkan. It beats the WineD3D driver in performance and compatibility for most games. It does not support DirectX 12, see #VKD3D-Proton instead. DXVK and VKD3D-Proton can and should be installed alongside each other to be able to support all DirectX versions.

To install the latest version, use #Winetricks:

 $ WINEPREFIX=your-prefix winetricks dxvk

You can also specify a version to install. For example, to install a DXVK version with relaxed requirements, use:

 $ WINEPREFIX=your-prefix winetricks dxvk1103

Alternatively, install  or . Then run the following command to activate it in your Wine prefix (by default ):

 $ WINEPREFIX=your-prefix setup_dxvk install --symlink

While using DXVK with a dual graphics setup, Wine prefers the dedicated GPU. On laptops for power saving, this can be overridden:

 $ VK_DRIVER_FILES=/usr/share/vulkan/icd.d/your_driver.json wine executable

## VKD3D-Proton
VKD3D-Proton is a fork of VKD3D which aims to implement the full Direct3D 12 API using Vulkan. The project serves as the development effort for Direct3D 12 support in Proton improving performance and compatibility for DirectX 12 games.

To install the latest version, use #Winetricks:

 $ WINEPREFIX=your-prefix winetricks vkd3d

Alternatively, install  or . Then run the following command to activate it in your Wine prefix (by default ):

 $ WINEPREFIX=your-prefix setup_vkd3d_proton install --symlink

## Synchronization primitives
Some games heavily use Windows synchronization objects to run multi-threaded workloads. Wine provides a user-space implementation through wineserver, but it usually worsens performance in CPU-bound scenarios. There are 3 alternative implementations—NTSync, FSync, and ESync—that improve performance, but you should use only one of them at a time.

MangoHud can be used to check the status of current synchronization method with the option winesync enabled in its configuration file.

## NTSync
NTSync is an in-kernel implementation of synchronization primitives.

Compared to ESync and FSync, NTSync more closely translates the behavior of the Microsoft Windows NT kernel implementation, with performance on par with FSync or smoother. NTSync is more accurate than ESync or FSync without performance degradation.

* Available if you use a kernel version starting from 6.14.
* NTSync was implemented in Wine 10.16, but not included in Proton, because Proton's latest version is based on Wine 10.0 stable, which did not yet include NTSync.
* Proton-GE () can be used if you want a Proton version with NTSync. Alternatively, Proton-TKG can be used.

NTSync does not require setting an environment variable; instead, it will automatically be used if the  kernel module is loaded. ,  and  ship with a file to load the module at boot. If you are using a custom version of Wine or Proton, you can manually create the following file:

## FSync
FSync is an in-kernel Futex2-based implementation of synchronization primitives.

It should generally have better performance than ESync.

* Available if you use a kernel version starting from 5.16.
* Not included in ; you will need a patched version.
* Enabled by default in Proton.

To enable FSync, export the following environment variable before running patched Wine:

 WINEFSYNC=1

## ESync
ESync is a user-space eventfd-based synchronization.

* Not included in ; you will need a patched version.
* Enabled by default in Proton, unless FSync is available.

To enable ESync, export the following environment variable before running patched Wine:

 WINEESYNC=1

## Unregister existing Wine file associations
By default, Wine takes over as the default application for a lot of formats. Some (e.g.  or ) are Windows-specific, and opening them with Wine can be a convenience. However, having other formats (e.g. , , , ) being opened via Wine may not be desired.

Wine's file associations are set in  as  files. Delete the files corresponding to the extensions you want to unregister.

Alternatively, to remove all Wine extensions:

 $ rm -f ~/.local/share/mime/packages/x-wine*
 $ rm -f ~/.local/share/applications/wine-extension*
 $ rm -f ~/.local/share/icons/hicolor/*/*/application-x-wine-extension*
 $ rm -f ~/.local/share/mime/application/x-wine-extension*

Afterwards, update the cache:

 $ update-desktop-database ~/.local/share/applications/
 $ update-mime-database ~/.local/share/mime/

## Prevent Wine from creating filetype associations
This method prevents the creation of filetype associations but retains the creation of XDG .desktop files (that you might see e.g. in menus).

If you want to stop wine from creating filetype associations via winecfg you have to uncheck the "Manage File Associations" checkbox under the Desktop Integration tab. See Wine FAQ

To make the same change via registry add the string  with value  under:

 HKEY_CURRENT_USER\Software\Wine\FileOpenAssociations

You might have to create the key  first!

To make this change via the command-line, run the following command:

 $ wine reg add "HKEY_CURRENT_USER\Software\Wine\FileOpenAssociations" /v Enable /d N

If you want to apply this by default for new Wine prefixes, edit  and add this line for example under the  section:

 HKCU,"Software\Wine\FileOpenAssociations","Enable",2,"N"

To prevent a package upgrade from overriding the modified file, create a pacman hook to make the change automatically:

See Pacman#Hooks for more information.

## Execute Windows binaries with Wine implicitly
The  package installs a binfmt file which will allows you to run Windows programs directly, e.g.  will launch as if you had typed . Service starts by default on boot, if you have not rebooted after installing Wine you can start  to use it right away.

## Dual Head with different resolutions
Installing  might fix dual-head issues with wine (for example, unclickable buttons and menus of application in the right most or bottom most monitor, not redrawable interface of application in that zone, dragging mouse cursor state stucked after leaving application area).

## Burning optical media
To burn CDs or DVDs, you will need to load the  kernel module.

## Proper mounting of optical media images
Some applications will check for the disc to be in drive. They may check for data only, in which case it might be enough to configure the corresponding path as being a CD-ROM drive in winecfg.
However, other applications will look for a name and/or a serial number, in which case the image has to be mounted with these special properties.

Some virtual drive tools do not handle these metadata, like fuse-based virtual drives (Acetoneiso for instance). CDemu will handle it correctly.

## Show FPS overlay in games
Wine features an embedded FPS monitor which works for all graphical applications if the environment variable  is set. This will output the framerate to stdout. You can display the FPS on top of the window thanks to osd_cat from the  package. See winefps.sh for a helper script.

## Running Wine under a separate user account
It may be desirable to run Wine under a specifically created user account in order to reduce concerns about Windows applications having access to your home directory.

First, create a user account for Wine:

 # useradd -m -s /bin/bash wineuser

Now switch to another TTY and start your X WM or DE as you normally would or keep reading...

Afterwards, in order to open Wine applications using this new user account you need to add the new user to the X server permissions list:

 $ xhost +SI:localuser:wineuser

Finally, you can run Wine via the following command, which uses  to launch Wine with the environment variables it expects:

 $ sudo -u wineuser env HOME=/home/wineuser USER=wineuser USERNAME=wineuser LOGNAME=wineuser wine arguments

It is possible to automate the process of running Windows applications with Wine via this method by using a shell script as follows:

Wine applications can then be launched via:

 $ runaswine "C:\path\to\application.exe"

In order to not be asked for a password each time Wine is run as another user the following entry can be added to the sudoers file: . See Sudo#Configuration for more information.

It is recommended to run  as the Wine user and remove all bindings for directories outside the home directory of the Wine user in the "Desktop Integration" section of the configuration window so no program run with Wine has read access to any file outside the special user's home directory.

Keep in mind that audio will probably be non-functional in Wine programs which are run this way if PulseAudio is used. See PulseAudio/Examples#Allowing multiple users to share a PulseAudio daemon for information about allowing the Wine user to access the PulseAudio daemon of the principal user.

## Temp directory on tmpfs
To prevent Wine from writing its temporary files to a physical disk, one can define an alternative location, like tmpfs. Remove Wine's default directory for temporary files and creating a symlink:

 $ rm -r ~/.wine/drive_c/users/$USER/Temp ~/.wine/drive_c/windows/temp
 $ ln -s /tmp/ ~/.wine/drive_c/users/$USER/Temp
 $ ln -s /tmp/ ~/.wine/drive_c/windows/temp

## Prevent installing Mono/Gecko
If Gecko and/or Mono are not present on the system nor in the Wine prefix, Wine will prompt to download them from the internet. If you do not need Gecko and/or Mono, you might want to disable this dialog, by  setting the  environment variable to .

## Remove Wine file bindings
For security reasons it may be useful to remove the preinstalled Wine bindings so Windows applications cannot be launched directly from a file manager or from the browser (Firefox offers to open EXE files directly with Wine!). If you want to do this, you may add the following NoExtract lines in :

 NoExtract = usr/lib/binfmt.d/wine.conf
 NoExtract = usr/share/applications/wine.desktop

## Wine is setting its own applications as defaults
Every time Wine creates (or updates) a prefix it will set its own bundled apps like Notepad and Winebrowser as the default text editor and web browser accordingly.

A way to work around this undesirable behavior is by using this environment variable:

 $ WINEDLLOVERRIDES=winemenubuilder.exe=d ...

## WineASIO
If you need professional audio support under Wine you can use  which provides an Audio Stream Input/Output (ASIO) interface for Wine that you can then use with JACK.

In order to use WineASIO you must install the  package and add yourself to the  user group.

Next you need to register WineASIO in your desired Wine prefix. Register the 32-bit:

 $ regsvr32 /usr/lib32/wine/i386-windows/wineasio32.dll

and/or 64-bit version:

 $ wine64 regsvr32 /usr/lib/wine/x86_64-windows/wineasio64.dll

## Disable starting explorer.exe
If you run a text mode (Command User Interface) executable without X installed, these errors might appear while starting the executable:

This is because  by default starts explorer.exe. Even  starts  according to  output.

Starting explorer including systray can be disabled with this environment setting:

 $ WINEDLLOVERRIDES="explorer.exe=d" wine program.exe

Depending on your CUI program, you might be able to use it with lowest memory footprint by disabling services.exe too:

 $ WINEDLLOVERRIDES="explorer.exe,services.exe=d" wine program.exe

## Troubleshooting
See Wine User's Guide and Wine FAQ (especially its Troubleshooting section) for general tips.

Also refer to the Wine AppDB for an advice on specific applications.

## General installation issues
Each Wine prefix has a lot of persistent state, between the installed programs and the registry. The first step to troubleshooting issues with program installation should be to either create an isolated prefix, or clear the default prefix via . The latter will delete any of the programs and settings you have added to the default prefix.

## Error loading libc.so.6
You might get the following error when running wine:

This is caused by the syscall to  failing:

 mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = -1 EPERM (Operation not permitted)

This is a known bug in the kernel.

Changing the  sysctl value from the default of  seems to fix the problem:

 # sysctl -w vm.mmap_min_addr=32768

## Xwayland problems
If you use Wine under Xwayland, you can activate the option for "Emulating a virtual desktop" in the Graphics Tab in winecfg, to avoid problems with:

* flickering;
* wrong window location;
* wrong mouse cursor location and clicks;
* keyboard detection.

If disabling the Virtual Desktop left you unable to interact with the winecfg window with mouse & keyboard anymore, you can explicitly start winecfg on a Virtual Desktop anyway and reenable it with:

 $ wine explorer /desktop=name,800x600 winecfg

When starting GUI windows (eg. winecfg) with Wayland and none are displayed with these errors in console:

You may try setting the  variable to :

 $ DISPLAY=:1 wine winecfg

## Keyboard input not working
This could be caused by the window manager not switching focus. In the Graphics tab of winecfg, disable the 'Allow the window manager...' options, or set windowed mode with 'Emulate a virtual desktop'.
*Some suggest to toggle all the Window settings, click Apply, then change them back. If that does not work, try the above.

If the keyboard does not work after unfocusing the application, try editing the registry:

* Under , add a string value  and set it to .
* Alternatively, you can use winetricks to set the value:  or use wine reg

## Application fails to start
Some older games and applications assume that the current working directory is the same as that which the executable is in. Launching these executables from other locations will prevent them from starting correctly. Use  before invoking Wine to rule this possibility out.

## EA App fails to launch games
If the total size of the environment variable block exceeds ~32768 characters, when attempting to launch any game from the EA App, an error popup will appear instead (the message has changed through the versions: usually it's a generic "Failed to launch game", but other times it's been "The game hasn't released yet").

This is an issue with the application itself, not Wine. The only way to work around this issue is to unset the large environment variables in your system so that the total size doesn't exceed the threshold. Note that Wine intentionally does not import some environment variables, which alleviates the issue.It is also possible to prevent specific environment variables from being imported by setting an environment variable with the same key prefixed with .[https://gitlab.winehq.org/wine/wine/-/blob/baeb97c3572bfcc41b0c13c8e93aa09ae15b7c35/dlls/ntdll/unix/env.c#L884
