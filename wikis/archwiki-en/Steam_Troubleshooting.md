# Steam/Troubleshooting

# Make sure that you have followed Steam#Installation.
# If the Steam client / a game is not starting and/or you have error message about a library, read #Steam runtime and see #Debugging shared libraries.
# If the issue is related to networking, make sure that you have forwarded the required ports for Steam.
# If the issue is about a game, consult Steam/Game-specific troubleshooting.

## Steam runtime
Steam for Linux ships with its own set of libraries called the Steam runtime. By default Steam launches all Steam Applications within the runtime environment. The Steam runtime is located at .

If you mix the Steam runtime libraries with system libraries you will run into binary incompatibility issues, see steam-for-linux issue #4768. Binary incompatibility can lead to the Steam client and games not starting (manifesting as a crash, as hanging or silently returning), audio issues and various other problems.

The  package offers two ways to launch Steam:

*  (alias ), which overrides runtime libraries known to cause problems via the  environment variable (see ).
* , the default Steam launch script

As the Steam runtime libraries are older they can lack newer features, e.g. the OpenAL version of the Steam runtime lacks HRTF and surround71 support.

## Steam native runtime
The  package depends on over 130 packages to pose a native replacement of the Steam runtime, some games may however still require additional packages.

This package provides the  script, which launches Steam with the  environment variable and  flag, making it ignore its runtime and only use system libraries.

You can also use the Steam native runtime without  by manually installing just the packages you need. See #Finding missing runtime libraries.

## Debugging shared libraries
To see the shared libraries required by a program or a shared library run the  command on it, see . The  and  environment variables can alter which shared libraries are loaded, see . To correctly debug a program or shared library it is therefore important that these environment variables in your debug environment match the environment you wish to debug.

If you figure out a missing library you can use pacman or pkgfile to search for packages that contain the missing library.

## Finding missing game libraries
If a game fails to start, a possible reason is that it is missing required libraries. You can find out what libraries it requests by running .  is likely located somewhere in . Please note that most of these "missing" libraries are actually already included with Steam, and do not need to be installed globally.

## Finding missing runtime libraries
If individual games or Steam itself is failing to launch when using  you are probably missing libraries. To find the required libraries run:

 $ cd ~/.steam/root/ubuntu12_32
 $ file * | grep ELF | cut -d: -f1 | LD_LIBRARY_PATH=. xargs ldd | grep 'not found' | sort | uniq

Alternatively, run Steam with  and use the following command to see which non-system libraries Steam is using (not all of these are part of the Steam runtime):

 $ for i in $(pgrep steam); do sed '/\.local/!d;s/.*  //g' /proc/$i/maps; done | sort | uniq

## Debugging Steam
The Steam launcher redirects its stdout and stderr to . This means you do not have to run Steam from the command-line to see that output.

It is possible to debug Steam to gain more information which could be useful to find out why something does not work.

You can set  environment variable with one of , , , ,  and then start .

For example with

 $ DEBUGGER=gdb steam

 will open, then type  which will start  and once crash happens you can type  to see call stack.

## Runtime issues
## 'GLBCXX_3.X.XX' not found when using Bumblebee
This error is likely caused because Steam packages its own out of date . See #Finding missing runtime libraries about working around the bad library. See also steam-for-linux issue 3773.

## Steam>Warning: failed to init SDL thread priority manager: SDL not found
Solution: install the  package.

## Game crashes immediately
This is likely due to #Steam runtime issues, see #Debugging shared libraries.

Disabling the in-game Steam Overlay in the game properties might help.

And finally, if those do not work, you should check Steam's output for any error from the game. You may encounter the following:

*
*

In these cases, try replacing the  file from the problematic game with one of a game that works. This error usually happens for games that were not updated recently when Steam runtime is disabled. This error has been encountered with AYIM, Bastion and Monaco.

If the game crashes with

it's likely that conflicting versions of Vulkan are installed.  and NVIDIA Vulkan drivers are mutually exclusive. This is solved by uninstalling the unneeded driver. To obtain information about the chipset vendor one can run:

 # lshw -C display | grep vendor

To get a list of installed packages

 # pacman -Qs vulkan

## Game and Steam crashes after game start
If the following error is output:

 failed to dlopen engine.so error=/home/GAMEPATH/bin/libgcc_s.so.1: version `GCC_7.0.0' not found (required by /usr/lib32/libopenal.so.1)

moving the incompatible lib can be a workaround.

 mv .local/share/Steam/steamapps/common/GAME/bin/libgcc_s.so.1 .local/share/Steam/steamapps/common/GAME/bin/libgcc_s.so.1.b

## Some games freeze at start when in focus
A combination of using , specific Proton versions and NVIDIA driver version 535 is known to freeze some games using DXVK/Vulkan at launch under Xorg. Using Alt+Tab allows bringing Steam in focus, and the game seems to run properly in the background. Solution: disable  or downgrade NVIDIA drivers.

## Version `CURL_OPENSSL_3` not found
This is because  alone is not compatible with previous versions. You need to install the compatibility libraries:

One of the following messages may show up:

 # Nuclear Throne
 ./nuclearthrone: /usr/lib32/libcurl.so.4: version `CURL_OPENSSL_3' not found (required by ./nuclearthrone)

 # Devil Daggers
 ./devildaggers: /usr/lib/libcurl.so.4: version `CURL_OPENSSL_3' not found (required by ./devildaggers)

You need to install either  or  and link the compatibility library manually:

 # Nuclear Throne
 $ ln -s /usr/lib32/libcurl-compat.so.4.4.0 "LIBRARY/steamapps/common/Nuclear Throne/lib/libcurl.so.4"

 # Devil Daggers
 $ ln -s /usr/lib/libcurl-compat.so.4.4.0 LIBRARY/steamapps/common/devildaggers/lib64/libcurl.so.4

## Steam webview/game browser not working in native runtime (Black screen)
Since the new Steam Friends UI update, the client webview is not working correctly with the native-runtime.

 ./steamwebhelper: error while loading shared libraries: libpcre.so.3: cannot open shared object file: No such file or directory

It can be solved preloading glib libraries; Those do not require libpcre and selinux to work.

 $ LD_PRELOAD="/usr/lib/libgio-2.0.so.0 /usr/lib/libglib-2.0.so.0" steam-native

Alternatively, you may create a symbolic link to the native Arch libpcre library.

 # ln -s /usr/lib/libpcre.so /usr/lib64/libpcre.so.3

Since update from around 3/3/2022, there are some reports of black screen still persisting after applying above workaround.

The workaround for now is to run Steam with the  option. More information can be found in Github Steam-For-Linux repository Issue #8451 and #8420.

## Steam: An X Error occurred
When using an NVIDIA GPU and proprietary drivers, Steam may fail to start and (if run from the terminal) produce errors of the form:

 Steam: An X Error occurred
 X Error of failed request:  GLXBadContext
 Major opcode of failed request:  151
 Serial number of failed request:  51
 xerror_handler: X failed, continuing

Ensure the lib32- NVIDIA driver for your card is installed, and matches the main package version with:

 # pacman -Qs nvidia

You may need to change which mirrors you are using to install the drivers if they do not match.

If you are using AMD, have enabled 10-bit color depth, and are having this problem. You will likely need to disable 10-bit color depth.

Another issue that causes this error message can be solved by removing the config.vdf file:

 $ rm ~/.local/share/Steam/config/config.vdf

## Steam: Compatibility tool configuration failed
If you are trying to run a native game using Proton but get a Steam compatibility tool error immediately after starting the game, you might have to reinstall the runtime.

# Navigate to your Steam library.
# In the dropdown above your game list check the Tools option to make them visible.
# Search for Proton, right click on each installed tool, visit Properties, open the Local files tab and click Verify integrity of tool files for each entry.
# Search for Steam Linux Runtime and repeat the same procedure. If none are available, install the latest Steam Linux Runtime - Soldier.

## Game starts but closes immediately with custom kernel
Make sure that you have enabled User namespace in General setup -> Namespaces support.

## Steam Library won't start
Opening the Steam library either displays nothing, or a brief splash, but no window appears. Running  in a terminal window gives this error:

 Assertion 'device' failed at src/libsystemd/sd-device/device-private.c:103, function device_get_tags_generation(). Aborting.

Bugs reports are filed: #79006

See also discussion at: Steam failing to launch since systemd 253.5-2 update

A workaround is to install .

## Graphical issues
## Black main screen on Intel iGPUs
On some systems that use Intel integrated graphics running Steam on Wayland will make only the webviews not render, with functional dropdowns and other menus. Going to Steam -> Settings -> Interface, then disabling Enable GPU accelerated rendering in web views might fix the problem.

## Blurry text and graphics with Xwayland and HiDPI
When Steam runs as an Xwayland client under a compositor that uses HiDPI scaling, you may find that Steam and games are rendered at half resolution and then upscaled to fit the HiDPI screen. This results in blurry graphics.

One option is to run Steam under a nested gamescope compositor. Install the  package:

 $ gamescope -f -m 1 -e -- steam -gamepadui

This runs Steam in "big picture" mode (actually Steam Deck mode), in fullscreen, without scaling (i.e. at full resolution). The same settings should also propagate to games run under Steam.

Another option is to configure your compositor to prevent Xwayland from scaling applications entirely. For example, Hyprland users can add

 xwayland {
   force_zero_scaling = true
 }

to the hyprland.conf file to prevent Xwayland from scaling any applications. Note that all applications that use Xwayland will stop scaling, and so on HiDPI displays, text and other elements in those applications may become too small to be comfortably viewed.

## Steam flicker/blink with black screen not loading Store/Library or other pages
When Steam is started on Wayland (not confirmed X11) with dual graphics in some cases Steam client is unstable display black screen and flicker/blink. This is due to the option  being enabled in the desktop entry.

## Fix by editing desktop entry
First, make a user copy of the desktop entry for Steam (from ). Then, change the option:

If opened, close Steam and relaunch.

## Bypass desktop entry
The desktop entry options do not take effect if you start Steam from the terminal, bypassing the issue.

 $ steam &

Ampersand (&) at the end is to run Steam in background, terminal can be closed after Steam starts.

## Audio issues
If the sections below do not address the issue, using the #Steam native runtime might help.

## Configure PulseAudio
Games that explicitly depend on ALSA can break PulseAudio. Follow the directions for PulseAudio#ALSA to make these games use PulseAudio instead.

If you are using PipeWire, then instead install  and set up PipeWire#PulseAudio clients.

## No audio or 756 Segmentation fault
First #Configure PulseAudio and see if that resolves the issue. If you do not have audio in the videos which play within the Steam client, it is possible that the ALSA libraries packaged with Steam are not working.

Attempting to playback a video within the Steam client results in an error similar to:

 ALSA lib pcm_dmix.c:1018:(snd_pcm_dmix_open) unable to open slave

A workaround is to rename or delete the  folder and the  files. They can be found at:

 ~/.steam/steam/ubuntu12_32/steam-runtime/i386/usr/lib/i386-linux-gnu/

An alternative workaround is to add the  library to the  environment variable:

 $ LD_PRELOAD='/usr/$LIB/libasound.so.2 '${LD_PRELOAD} steam

If audio still will not work, adding the PulseAudio libraries to the  variable may help:

 $ LD_PRELOAD='/usr/$LIB/libpulse.so.0 /usr/$LIB/libpulse-simple.so.0 '${LD_PRELOAD} steam

Be advised that their names may change over time. If so, it is necessary to take a look in

 ~/.steam/ubuntu12_32/steam-runtime/i386/usr/lib/i386-linux-gnu

and find the new libraries and their versions.

Bugs reports have been filed: #3376 and #3504

## FMOD sound engine
The FMOD audio middleware package is a bit buggy, and as a result games using it may have sound problems.

It usually occurs when an unused sound device is used as default for ALSA. See Advanced Linux Sound Architecture#Set the default sound card.

:Affected games: Hotline Miami, Hotline Miami 2, Transistor

## PulseAudio & OpenAL: Audio streams cannot be moved between devices
If you use PulseAudio and cannot move an audio stream between sinks, it might be because recent OpenAL versions default to disallow audio streams from being moved. Try to add the following to your :

 allow-moves=true

## Cracking Microphone in Steam Voice and Games
If you experience cracking with your audio input while using Steam Voice or in games, you can try to launch Steam with the environmental variable

## Steam client issues
## Cannot browse filesystem to add a library folder or library folder appears as empty
If the file chooser is empty when trying add a library folder, or if a previously set up folder now appears with 0 games installed, this can be the result of an incorrect timestamp on the root directory or in the library folder. Timestamps can be checked with stat:

 $ stat path

If the timestamp is in the future, run

 $ touch path

to reinitialize it to the current date, then re-run Steam.

## Cannot add library folder because of missing execute permissions
If you add another Steam library folder on another drive, you might get the error message:

 New Steam library folder must be on a filesystem mounted with execute permissions

Make sure you are mounting the filesystem with the correct flags in your , usually by adding  to the list of mount parameter. The parameter must occur after any  or  parameter since these can imply .

This error might also occur if your library folder does not contain a  directory. Previous versions used  instead, so ensure the name is fully lowercase.

This error can also occur because of Steam runtime issues and may be fixed following the #Finding missing runtime libraries section or due to no space being left on the device. For debugging purposes it might be useful to run Steam from the console and observe the log.

## Unusually slow download speed
If your Steam (games, software…) download speed through the client is unusually slow, but browsing the Steam store and streaming videos is unaffected, installing a DNS cache program, such as dnsmasq can help [https://steamcommunity.com/app/221410/discussions/2/616189106498372437/.

Something else that might help would be disabling IPv6. See for more information.

Another potential fix is to disable HTTP2 [https://github.com/ValveSoftware/steam-for-linux/issues/10248 by creating the file:

To increase the server connections at the potential cost of negatively affecting speeds, add:

## "Needs to be online" error
If the Steam launcher refuses to start and you get an error saying: "Fatal Error: Steam needs to be online to update" while you are online, then there might be issues with name resolving.

Try installing , , , ,  or .

This may also be as simple as DNS resolution not correctly working and is not always obvious since modern browsers will use their own DNS servers. Follow Domain name resolution.

Steam may have issues if systemd-resolved is providing DNS resolution. Make sure  is present to resolve this.

If DNS resolution works but the Steam launcher still shows the same error message, enabling DNS caching e.g. via the "Name Service Caching Daemon", , has shown to work around this issue.

It is unclear what exactly running  does to make it work again though. Please check the talk page for more info.

## Steam forgets password
:Related: steam-for-linux#5030

Steam for Linux has a bug which causes it to forget the password of some users.

As a workaround, after logging in to Steam, run

 # chattr +i ~/.steam/registry.vdf

This will set the file's immutable bit so Steam cannot modify, delete, or rename it and thus not log you out.

## Preventing crash memory dumps
Every time Steam crashes, it writes a memory dump to . If Steam falls into a crash loop, the dump files can become quite large. When  is mounted as tmpfs, memory and swap file can be consumed needlessly.

To prevent this, link  to :

 # ln -s /dev/null /tmp/dumps

Or alternatively, create and modify permissions on . Then Steam will be unable to write dump files to the directory.

 # mkdir /tmp/dumps
 # chmod 600 /tmp/dumps

This also has the added benefit of Steam not uploading these dumps to Valve's servers.

## Steam license problem with playing videos
Steam uses Google's Widevine DRM for some videos. If it is not installed you will get the following error:

 This video requires a license to play which cannot be retrieved. This may be a temporary network condition. Please restart the video to try again.

To solve this issue follow the Streaming Videos on Steam support page.

## No context menu for joining/inviting friends
Since the new Steam Friends UI update, it may be the case that in the right-click menu the entries for "Join Game", "Invite to Game" and "View Game Info" are missing.

In order to fix this, it maybe be necessary to install .

## Slow and unresponsive user interface
If you experience extremely slow and sluggish performance when using the Steam client it might help to disable the Enable GPU accelerated rendering in web views option under the Interface tab in the Steam client settings.

The friends list can also cause this problem. Two workarounds are mentioned in https://github.com/ValveSoftware/steam-for-linux/issues/7245:

* Moving the friends list to another monitor * Disabling animated avatars. Open Settings and navigate to Friends & Chat. Set  Enable Animated Avatars & Animated Avatar Frames in your Friends List and Chat > OFF [https://github.com/ValveSoftware/steam-for-linux/issues/7245#issuecomment-813443906.

## Steam fails to start correctly
One troubleshooting step is to run

 $ steam --reset

This can fix various issues that come with a broken install.

## Missing taskbar menu
If clicking your Steam taskbar icon does not give you a menu, it may be necessary to install the  and  packages and restart Steam.

## "Your browser does not support the minimum set of features required to watch this broadcast" error
See steam-for-linux issue 6780

If you get an error stating "Your browser does not support the minimum set of features required to watch this broadcast" when attempting to watch a stream/broadcast try the following troubleshooting steps:

# Navigate to Community > Broadcasts. If the page displays "Updating Steam" wait a few minutes to see if the process completes and cancel it after a while in case it does not. Now test if you are able to watch broadcasts, e.g. by clicking on one of the ones display under Community > Broadcasts.
# Start a broadcast while in Big Picture mode (View > Big Picture Mode). If a broadcast starts fine while in Big Picture mode check if it still works after switching back to the main interface.
# Trigger the Steam client to directly unlock H.264 decoding using the following command: . The Steam client should start headless and run the unlock command. Wait a minute to be sure the process completes, then close and relaunch the Steam client.

## Using system titlebar and frame
Currently Steam client tries to manage its windows itself, but it does it improperly, see steam-for-linux#1040. As a workaround you can use steamwm project. Run Steam like this: . Also the project provides a skin that removes unnative control buttons and frame, but leaves default skin decorations.

## More selective DPMS inhibition
By default, the Steam client totally disables screensaving when it is running, whether a game is launched or not.

A workaround to this issue is provided by : run  or .

This will allow your screen to turn off if Steam is running, but will keep inhibiting the screensaver if a game is launched.

See Issue 5607 at Valve's GitHub for the details.

## Enabling fractional scaling
If the text and icons in the Steam client window are too small to read on your display, it may be beneficial to enable fractional scaling. The Steam client has a settings option to enable it, at Settings > Interface > Scale text and icons to match monitor settings. Enabling this should tell the client to use the system's fractional scaling settings.

However, if this does not automatically work, there is a command line parameter to force fractional scaling. Running Steam with the  flag will scale the client to 1.5x size. This value can be changed to the correct scaling factor for your monitor. If you wish to make this change permanent, you can edit the  field in the  file.

## Steam Beta crashes
If you are using Steam Beta (which can be confirmed with the presence of  in the logs) and encounter breaking bugs, manually switch back to non-Beta:

 $ rm -f ~/.local/share/Steam/package/beta

Report the issue after looking for duplicates at https://github.com/ValveSoftware/steam-for-linux.

## Cannot access store page (client displays error -105 or -102)
If the store page is inaccessible but other networking features (such as game downloads) are working, it may be a DNS resolution failure. A possible solution is to ensure systemd-resolved is enabled and started, then create the  symlink as explained in systemd-resolved#DNS.

Other solution would be to flush DNS as explained here Run  or  as root.

## Steam client restarts while a game is running
A work around is to disable the Enable GPU accelerated rendering in web views option under the Interface tab in the Steam client settings.

## Steam Remote Play issues
See Steam#Steam Remote Play.

## Remote Play does not work from Arch Linux host to Arch Linux guest
Chances are you are missing . Once you install that, it should work as expected.

With that, Steam should no longer crash when trying to launch a game through Remote Play.

## Hardware decoding not available
Remote Play hardware decoding uses , but Steam requires , where as Arch defaults to 64bit.

As a basic set, this is  and . Intel graphics users will also require both  and .

For more information about vaapi see hardware video acceleration.

It may also be necessary to remove the Steam runtime version of libva, in order to force it to use system libraries. The current library in use can be found by using:

 $ pgrep steam | xargs -I {} cat /proc/{}/maps | grep libva

If this shows locations in  Steam is still using its packaged version of libva. This can be rectified by deleting the libva library files at , so that Steam falls back to the system libraries.

## Big Picture Mode minimizes itself after losing focus
This can occur when you play a game via Remote Play or if you have a multi-monitor setup and move the mouse outside of BPM's window. To prevent this, set the  environment variable and restart Steam.

See also the [https://github.com/ValveSoftware/steam-for-linux/issues/4769 steam-for-linux issue 4769.

## Other issues
## Steam Library in NTFS partition
If your Steam library resides in NTFS partition it is probable that games residing there could not start.

The trouble is that Wine uses a colon in its  directory, and when mounted with the  option, is instructed to not create such colon names which can confuse Windows. Not adding it is not that unsafe: Windows will act fine besides being unable to open the symlink (which it will not need to do anyways);  may delete the link, but it is easily recreated.

Better workaround: mount without . This option is often added by GUI file explorers via udisks for caution, but adding a real fstab line will give it a proper way to do so.

# Run  and extract the line containing the ntfs partition, e.g.
# Write the line into , editing it to use the proper options without . With the earlier example, we would write
# Unmount the partition, then remount.

Alternatively, disable udisks use of  globally following instructions in udisks#NTFS file creation failing (filename-dependent).

Other workaround: move the  and  to a non-NTFS drive, then create symbolic link in their original locations. You may be wasting some space on your otherwise important Linux drive, however.

 $ mv SteamLibrary/steamapps/common/Proton\ x.y /home/user/dir/
 $ mv SteamLibrary/steamapps/compatdata /home/user/dir/
 $ ln -s /home/user/dir/Proton\ x.y/ SteamLibrary/steamapps/common/Proton\ x.y
 $ ln -s /home/user/dir/compatdata/ SteamLibrary/steamapps/compatdata

## Wrong ELF class
If you see this message in Steam's console output

 ERROR: ld.so: object '~/.local/share/Steam/ubuntu12_32/gameoverlayrenderer.so' from LD_PRELOAD cannot be preloaded (wrong ELF class: ELFCLASS32): ignored.

you can safely ignore it. It is not really any error: Steam includes both 64- and 32-bit versions of some libraries and only one version will load successfully. This "error" is displayed even when Steam (and the in-game overlay) is working perfectly.

## Multiple monitors setup
A setup with multiple monitors may prevent games from starting. Try to disable all additional displays, and then run a game. You can enable them after the game successfully started.

Also you can try running Steam with this environment variable set:

 $ export LD_LIBRARY_PATH=/usr/lib32/nvidia:/usr/lib/nvidia:$LD_LIBRARY_PATH

## Text is corrupt or missing
Try installing , ,  (Steam updater window shows void squares instead of all non-Latin characters if this package not installed) and  (for Asian characters), then restart Steam to see whether the problem is solved.

## SetLocale('en_US.UTF-8') fails at game startup or typing non-ASCII characters does not work in the Steam client
You need to generate the  locale. See Locale#Generating locales.

## Missing libc
This could be due to a corrupt Steam executable. Check the output of:

 $ ldd ~/.local/share/Steam/ubuntu12_32/steam

Should  claim that it is not a dynamic executable, then Steam likely corrupted the binary during an update. The following should fix the issue:

 $ cd ~/.local/share/Steam/
 $ ./steam.sh --reset

If it does not, try to delete the  directory and launch Steam again, telling it to reinstall itself.

This error message can also occur due to a bug in Steam which occurs when your  directory ends in a slash (Valve GitHub issue 3730). This can be fixed by editing  and changing  to , then logging out and in again. Afterwards, Steam should repair itself automatically.

## Games do not launch on older Intel hardware
:source

On older Intel hardware which does not support OpenGL 3, such as Intel GMA chips or Westmere CPUs, games may immediately crash when run. It appears as a  error in , but looking in  it shows a GLXBadFBConfig error.

This can be fixed, by forcing the game to use a later version of OpenGL than it wants. Add  to your launch options.

## Mesa: Game does not launch, complaining about OpenGL version supported by the card
Some games are badly programmed, to use any OpenGL version above 3.0. With Mesa, an application has to request a specific core profile. If it does not make such a request, only OpenGL 3.0 and lower are available.

This can be fixed, by forcing the game to use a version of OpenGL it actually needs. Add  to your launch options.

## 2K games do not run on XFS partitions
If you are running 2K games such as Civilization 5 on XFS partitions, then the game may not start or run properly due to how the game loads files as it starts. === Steam controller not being detected correctly ===

See Gamepad#Steam Controller.

## Steam controller makes a game crash
See Gamepad#Steam Controller makes a game crash or not recognized.

## Steam hangs on "Installing breakpad exception handler..."
[https://bbs.archlinux.org/viewtopic.php?id=177245 BBS#177245

You have an NVIDIA GPU and Steam has the following output:

 Running Steam on arch rolling 64-bit
 STEAM_RUNTIME is enabled automatically
 Installing breakpad exception handler for appid(steam)/version(0_client)

Then nothing else happens. Ensure you have the correct drivers installed as well as their 32-bit versions (the 64-bit and 32-bit variants have to have the same versions): see NVIDIA#Installation.

## Killing standalone compositors when launching games
Utilizing the  switch, you can kill standalone compositors (such as Xcompmgr or picom) - which can cause lag and tearing in some games on some systems - and relaunch them after the game ends by adding the following to your game's launch options.

 killall compositor && %command%; nohup compositor &

You can also add -options to  or , of course.

Steam will latch on to any processes launched after  and your Steam status will show as in game. So in this example, we run the compositor through  so it is not attached to Steam (it will keep running if you close Steam) and follow it with an ampersand so that the line of commands ends, clearing your Steam status.

If your compositor supports running in daemon mode, you can use it instead. For example,  has the  /  option to daemonize its process:

 killall picom && %command%; picom -b

## Symbol lookup error using DRI3
Steam outputs this error and exits.

 symbol lookup error: /usr/lib/libxcb-dri3.so.0: undefined symbol: xcb_send_request_with_fds

To work around this, run Steam with , disabling DRI3 for Steam.

## Launching games on NVIDIA Optimus laptops
To be able to play games which require using NVIDIA GPU (for example, Hitman 2016) on Optimus enabled laptop, you should start game with primusrun prefix in launch options. Otherwise, game will not work.

Right click the game in your Steam library and select Properties > GENERAL > LAUNCH OPTIONS. Change options to

 primusrun %command%

Running Steam with primusrun used to work. While Steam has changed some behavior that now running Steam with primusrun would not have effect on launching games. As a result, you need to set launch options for each game (and you do NOT have to run Steam with primusrun).

For primusrun, VSYNC is enabled by default it could result in a mouse input delay lag, slightly decrease performance and in-game FPS might be locked to a refresh rate of a monitor/display. In order to disable VSYNC for primusrun default value of option  needs to be overridden by environment variable.

 vblank_mode=0 primusrun %command%

Same with optirun that uses primus as a bridge.

 vblank_mode=0 optirun -b primus %command%

If that did not work try:

 LD_PRELOAD="libpthread.so.0 libGL.so.1" __GL_THREADED_OPTIMIZATIONS=1 optirun %command%

For more details see Bumblebee#Primusrun mouse delay (disable VSYNC).

## HiDPI
HiDPI support should work out of the box, although on some systems it is necessary to force it setting the  cli option or the  environment variable to set the desired scale factor.

## Protocol support under KDE Plasma
If you are getting an error after running a game through web browser (or executing the link through xdg-open)

 Error — KIOExec
 File not found: steam://run/440

Go to System Settings -> Applications -> File Associations, add new, select  group and name it , then under Application Preference Order you have to add Steam. Apply changes, It should be working now.

## The game crashes when using Steam Linux Runtime - Soldier
Since Proton 5.13 Steam uses the Steam Linux Runtime - Soldier by default. Some games crash when using it.

To bypass it, you can:

* Manually build a proton without the Steam Runtime
* Replace the Soldier entry point script:

{{hc|~/.steam/steam/steamapps/common/SteamLinuxRuntime_soldier/_v2-entry-point|
#!/bin/bash

shift 2
exec "${@}"
}}

## Games running with Proton 5.13+ have no Internet connectivity
If you are using systemd-resolved as your DNS resolver, ensure you have created the  symlink as described in systemd-resolved#DNS.

The file should contain something similar to:

## "could not determine 32/64 bit of java"
A forgotten install of the  package caused this with at least one game. Early on there were conflicts between the system and the Steam runtime versions of some libraries, and that package helped resolve some of them. It is unclear whether it is still helpful, but uninstalling it resolved the above error message for Project Zomboid. The solution was discovered by noticing that running the  command from the command line worked, but switching the launch options to  showed Steam was trying to run the exact same command, but there were a lot of -prefixed libraries inserted in the preload and path.

## Stuttering with Vulkan
If you notice a constant intense stutter every 1-2 seconds, there may be conflicts in your vsync settings. Manually configuring vsync in the parameters will possibly fix it.

Go to the game properties and configure it in Launch Options:

 DXVK_FRAME_RATE=60 %command%

## Force OpenGL emulation
Some, especially older games might not work with the default Vulkan (DXVK) wrapper Proton uses. Try running the application with WineD3D OpenGL wrapper instead:

 PROTON_USE_WINED3D=1 %command%

## File picker does not see anything but Steam library
See . You need to install .

## DirectX errors on hybrid graphics
For laptop with Intel/NVIDIA Hybrid graphics encountering the following error:

 A d3d11-compatible gpu (feature level 11.0, shader model 5.0) is required to run the engine.

It's probably because your game is running on the iGPU instead of the dedicated GPU and you need to configure PRIME. If it's still not doing it, try using Direct3D instead of DXVK.

## No Internet Connection when downloading
If you see No Internet Connection while downloading games, a possible solution is clearing the download cache (Steam > Settings > Downloads > Clear Download Cache).

## Poor performance or stuttering after launching Steam
If you experience reduced performance or stuttering, lasting anywhere from a few seconds to a couple of minutes after launching Steam, it may be cased by bugged or outdated Proton installations.

Remove bugged Proton installed under app ID 0: . You may also need to remove outdated and problematic Proton versions, including custom ones like GE-Proton, especially .

For more details, see steam-for-linux#8114.

## Very long startup and slow user interface response
Steam's use of  in its Chromium backend to refer to itself. Due to the way systemd-resolvd attempts to resolve this host (via  by default for some users) this issue can hang the interface. This causes very long startups (if it ever starts) and a slow-responding (or not at all) user interface. This issue can temporary be addressed by editing  to change  to  and restarting systemd-resolvd. For more details, see == See also ==

* [https://bbs.archlinux.org/viewforum.php?id=32 Multimedia and Games / Arch Linux Forums
* ValveSoftware/steam-for-linux – Issue tracking for the Steam for Linux client
* Steam Community discussions of the game
* Steam Support FAQ
