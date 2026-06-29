# Steam/Game-specific troubleshooting

See Steam/Troubleshooting first.

This page assumes familiarity with the Steam#Directory structure, Steam#Launch options, environment variables, the Steam runtime and shared libraries. The  pseudo-variable is used to refer to a game's directory. When the text reads "run the game with " it is implied that you either update your launch options or run the game from the command-line with the environment variable.

## Common steps
## OpenSSL 1.0 setup
Some Steam games are built against OpenSSL 1.0. ()

Install  and run the game with .

## Missing libcurl.so.4 or version CURL_OPENSSL_3 not found
Install  and run the game with .

## Steam Link
Currently Steam Link does not work with Wayland. You will only see a blank screen or even flickering when connecting to a Steam host running on Wayland. So you have to disable Wayland, for example:

And restart the login manager before continuing.

## Squares or invisible symbols, special characters and cyrillic letters in Source-based games
Any special character may produce a square or an empty space mark in the game, main menu and game console. In practice, any characters other than latin ones are not working. The problem is that  is configured as the system primary default font for latin sans-serif fonts.

First, make sure that per-user font customization files are enabled, i.e. the following file exist:

 /etc/fonts/conf.d/50-user.conf

Next, create  file in your fontconfig directory with the following content or if the file already exist, append only the alias section to the file:

## PipeWire & FMOD
If you are using PipeWire and do not have any sound in games utilising FMOD as an audio backend then you may require . Such games include Project Zomboid, Don't Starve, and Unrailed.

You will see similar to the following in your logs if this affects you.

 FMOD Error: An invalid object handle was used.
 [00:00:10: FMOD Error: Can't play event dontstarve/HUD/click_mouseover: An invalid object handle was used.

## tcmalloc.cc error in Source 1 games
If games such as like Counter-Strike Source, Portal, Team Fortress 2 crash at startup with the following error:

 src/tcmalloc.cc:278] Attempt to free invalid pointer 0x9e13ad0
 ~/.local/share/Steam/steamapps/common/Team Fortress 2/hl2.sh: line 72:  6280 Aborted                 (core dumped) ${GAME_DEBUGGER} "${GAMEROOT}"/${GAMEEXE} "$@"

Install , and point the crashing game to the proper library using:

 LD_PRELOAD=/usr/lib32/libtcmalloc_minimal.so

From this steam community post.

## Crash with Unity games
Games using Unity, e.g. Papers Please, Vampire Survivors, expect PulseAudio to be installed and will quietly crash with SIGSEGV on running if it is not installed. You can also use PipeWire with .

## Split lock detection / mitigation
Split lock detection is a warning to aid developers, mitigation on the other hand is designed to hinder performance in order to encourage developers to write better code. This results in significantly reduced performance under a myriad of gaming scenariosincluding Counter-Strike Source engine games and games using BattleEye anti-cheat.

Since kernel 6.2, a new sysctl tunable[https://lore.kernel.org/lkml/20221212191524.553244-1-dave.hansen@linux.intel.com/ of  is available (by default) to enable mitigation, instead of the olderkernel parameter.

Upon setting:

 # echo "kernel.split_lock_mitigate = 0" > /etc/sysctl.d/99-splitlock.conf

The kernel will log Steam / Cef lock splitting, but without the sequential access penalty.

Additionally, GameMode can be used to toggle this kernel parameter at runtime.

## Games
## 7 Days To Die
If the game crashes on start, add the following to Steam launch options:

 LD_PRELOAD="libpthread.so.0 libGL.so.1" __GL_THREADED_OPTIMIZATIONS=1 %command% -force-glcore

If the game does not recognize your screen's resolution, launch the game with Game Launcher and check the Unity screen selector option to correct the resolution. This will give you a GUI in which you can select the correct screen when the game is started.

If that does not help try running the game in 32-bit mode by checking the respective option in the Game-engine in the launcher options.

It will help the game performance if the GLCore option is checked in launcher options.

## Age of Wonders 3
If game fails to start at launch you will need to create a pthread_yield.so file. Do the following in a text editor:

 extern int sched_yield(void);

 int pthread_yield()
 {
 	return sched_yield();
 }

Then save file as a pthread_yield.c then issue following command in terminal in the directory that has the file:

 $ gcc -m32 -shared -fPIC pthread_yield.c -o pthread_yield.so

Copy pthread_yield.so in the AOW3 game directory and then edit the AoW3Launcher.sh file and add the following:

 export LD_PRELOAD="pthread_yield.so"

Do this at the bottom of the file but before exec ./AoW3Launcher after this the game should then launch as normal.

## Alien Isolation
## Missing libpcre.so.3 and libidn.so.11
 $ ln -s /usr/lib/libpcre.so GAME/lib/x86_64/libpcre.so.3'
 $ ln -s /usr/lib/libidn.so GAME/lib/x86_64/libidn.so.11'

Append  to your .[https://steamcommunity.com/app/214490/discussions/0/154644705028020291/

## Missing libcrypt.so.1
Install the package . === Amnesia: The Dark Descent ===

Dependencies:
[https://steamcommunity.com/app/221410/discussions/0/864957183198111387/

*
*
*
*

## Gamepad not working
The version of libSDL2 shipped with the game seems to be out-of-date and may not support your gamepad yet. Simply remove or rename , the linker will fall back to using the up-to-date version from .

## Amnesia: Rebirth
If you encounter a popup with  on startup which immediately closes the game and you are using PipeWire, install these packages if they are not already: ,  and . Reboot and re-open the game.

## And Yet It Moves
Dependencies:

*
*
*
*

## Game does not start
When the game refuses to launch and prints one of the following error messages:

 readlink: extra operand ‘Yet’
 Try 'readlink --help' for more information.

 This script must be run as a user with write priviledges to game directory.

Open  and surround {{ic|${BASH_SOURCE}} in the following line with double quotes.

 ayim_dir="$(dirname "$(readlink -f ${BASH_SOURCE[0})")"

## Anomaly Warzone Earth
## Leave fullscreen
There are no in-game settings for this, but fullscreen can be toggled with

## Infinite loading
Create file  next to the game executable: src

 #define _GNU_SOURCE
 #include
 #include
 #include
 #include
 #include
 static int (*_realSemTimedWait)(sem_t *, const struct timespec *) = NULL;

 int sem_timedwait(sem_t *sem, const struct timespec *abs_timeout)
 {
     if (abs_timeout->tv_nsec >= 1000000000)
     {
         //fprintf(stderr, "to: %lu:%lu\n", abs_timeout->tv_sec, abs_timeout->tv_nsec);
         ((struct timespec *)abs_timeout)->tv_nsec -= 1000000000;
         ((struct timespec *)abs_timeout)->tv_sec++;
     }
     return _realSemTimedWait(sem, abs_timeout);
 }

 __attribute__((constructor)) void init(void)
 {
     _realSemTimedWait = dlsym(RTLD_NEXT, "sem_timedwait");
 }

Compile with

Launch with

## Gamepad not working
You have to enable keyboard control and map gamepad to keys.

Config for Steam:

## Aquaria
## Mouse pointer gets stuck in one direction
If the mouse pointer gets stuck in one direction, make sure  contains .

If that does not fix the issue, try unplugging any joysticks or joystick adapter devices you have plugged in.

## ARK: Survival Evolved
## Game does not start, displays text window with unreadable text
Run the game with .

## Gray water
Download the TheCenter map and copy  from that map into TheIsland as described here.

Ragnarok uses TheIsland's texture, so the same procedure fixes the issue on Ragnarok as well.

## Segmentation fault on startup
Caused by the games packaged libopenal. Use system libopenal to solve the segfault by running the game with with

## Crash on joining a game
Set steam to 'offline mode' and try again

## Audiosurf 2
## error. unable to load song  ,came back with zero duration
If you get this in your log, install .

## BADLAND: Game of the Year Edition
Refer to #Missing libcurl.so.4 or version CURL_OPENSSL_3 not found.

## Barony
## Broken/Incorrect Textures
Use the following launch options:

 LD_PRELOAD="$LD_PRELOAD ./libSDL2-2.0.so.0 ./libSDL2_ttf-2.0.so.0 ./libSDL2_image-2.0.so.0" %command%

The issue is caused by a newer version of SDL than what the game bundles, this workaround simply has the game use the bundled libraries instead, as described here.

## BATTLETECH
## Game freezes after opening studio credits (opening cinematic does not play)
Try installing  (as suggested in the Paradox forums).

## Game does not start
Try deleting , this should make the game run again.

## Beat Cop
## "BeatCop.x86_64" is not responding
Run  instead of .

## Binding of Isaac: Rebirth
## No sound
Prepend  to .

Adjust the audio levels in the game options.

## BioShock Infinite
## Game launching on wrong monitor in fullscreen mode
Add the following launch option:

 --eon_force_display=1

Various more fixes and tweaks can be found here

## Audio crackling
Change the launch options to

 PULSE_LATENCY_MSEC=60 %command%

Discussion on the variable can be found in Proton issue #1209. Lower values maintain lower audio latency but crackling may still occur; higher values are more likely to eliminate crackling but allow for higher audio latency.

## BLACKHOLE
Refer to #Missing libcurl.so.4 or version CURL_OPENSSL_3 not found.

## Black Mesa
If the game have crashing on start, install  for 32bit version of  which is needed Source.

Also add this to the game's launch command line in Steam's preferences:

 %command% -oldgameui

## Block'hood
## White screen on startup
When launched the game may only display a white screen with no interface and no way to play the game. Add "-screen-fullscreen 0" to launch options.

## The Book of Unwritten Tales
Dependencies:

*
*

If the game does not start, uncheck: Properties > Enable Steam Community In-Game.

The game is known to segfault when opening the settings and possibly during or before playing. A workaround from the Steam discussions is to replace the game's  with one from Debian's repositories. To do that download this deb file, and extract it with :

 $ dpkg -x libogre-*.deb outdir

Now replace  with the one extracted from the  package.

## BRAIN/OUT
If the game does not start with error message saying "invalid app configuration".
Go to the game directory:

 $ cd ~/.steam/steam/steamapps/common/BrainOut/

Run the game directly:

 $ java -jar brainout-steam.jar

You need to have steam running in the background.

## The Book of Unwritten Tales: The Critter Chronicles
See #The Book of Unwritten Tales.

To prevent the game from crashing at the end credits, change the size of the credits image as described here.

## Borderlands 2
## Proton troubleshooting
## Game crashes instantly on launch
Borderlands 2 is a 32-bit DirectX 9 based game, therefore it is possible on 64-bit installs to be missing 32-bit Vulkan drivers. Installing the steam-native-runtime or specifically the appropriate multilib drivers (lib32-nvidia-utils or lib32-vulkan-radeon for NVIDIA and AMD Radeon respectively) may resolve the issue.

## Linux Native troubleshooting
## Migrating saves from other platforms
Borderlands 2 does not support cross-platform Steam Cloud syncing,
you have to manually copy the files between platforms.
Save locations can be found here.
Make sure your user can access the files.

## Using Ctrl Key
Borderlands 2 does not allow the  key to be used by default. The game seems to be accessing keycodes and not keysyms, therefore xmodmap has no affect. A workaround is using setkeycodes to map the Ctrl-scancode to some other key, as described in Map scancodes to keycodes#Using setkeycodes. I use  (as root) to map Ctrl to Alt before starting the game and  to restore the default.

## Logging into SHiFT
Out of the box you will not be able to log into SHiFT since the game expects certificates to be in , which is where Ubuntu stores them. Arch however uses .
To resolve the problem, run the game with .

## Game crashes nearly instantly
The game crashes in libopenal directly after launch.

Possible solution 0: Run the game with the  flag. It no longer crashes in libopenal with a general protection error.

Possible solution 1: As of lib32-openal version 1.18.0-1, the game crashes instantly. The possible solutions are to downgrade lib32-openal to 1.17.2-1, or to start the game with .

In case there are messages like this in the terminal:

 [  671.617205] Borderlands2segfault at 0 ip           (null) sp 00000000ff9a462c error 14 in Borderlands2[8048000+235a000

The following change may help (source):

 LD_PRELOAD='./libcxxrt.so:/usr/$LIB/libstdc++.so.6' %command%

Possible solution 2: Launch steam as  as described in #Steam native runtime. If the game still fails to launch even after installing the  meta package, then you might be missing some libraries. You can find those missing libraries as described in #Debugging shared libraries.

## Borderlands: The Pre-Sequel
See #Borderlands 2.

## Keyboard not working
This can occur with certain window managers e.g. dwm. Try a different window manager, or install  and run:

 $ wmname LG3D

see Java#Impersonate another window manager for more information.

## Not starting via Steam
If the game appears as Running, then syncs and closes when you launch it from Steam, try creating a  in the game directory
containing . This should resolve the issue and let you start the game directly from the game directory. If that does not work, try using the .

## Celeste
## Steam overlay is missing text
Add the following launch option (as documented in this issue):

 -gldevice:Vulkan

## Chaos Engine
Set your launch options to:

 LD_PRELOAD="/usr/lib32/libpng16.so.16" %command%

If such error is seen in terminal output of steam-native:

 /home/username/.local/share/Steam/steamapps/common/Chaos engine/TheChaosEngineSteam: /home/username/.local/share/Steam/steamapps/common/Chaos engine/lib/libz.so.1: version `ZLIB_1.2.9' not found (required by /usr/lib32/libpng16.so.16)
 /home/username/.local/share/Steam/steamapps/common/Chaos engine/TheChaosEngineSteam: /home/username/.local/share/Steam/steamapps/common/Chaos engine/lib/libz.so.1: version `ZLIB_1.2.3.4' not found (required by /usr/lib32/libpng16.so.16)

Then link the system libz.so:

 $ cd ~/.local/share/Steam/steamapps/common/Chaos\ engine/lib
 $ mv libz.so.1 libz.so.1.old
 $ ln -s /lib/libz.so.1

## Cities in Motion 2
## Dialog boxes fail to display properly
You will not be able to read or see anything, and you will have this in your logs:

 Fontconfig error: "/etc/fonts/conf.d/10-scale-bitmap-fonts.conf", line 69: non-double matrix element
 Fontconfig error: "/etc/fonts/conf.d/10-scale-bitmap-fonts.conf", line 69: wrong number of matrix elements

A workaround for the bug  is to remove line 69 from  (i.e. ).

## Cities Skylines
## Game not starting
If you set  environment variables globally, because you want to switch all your Electron apps use Wayland natively, you should know that the game launcher of Cities Skylines currently is Electron-based and compiled as x11-only, without Wayland support. So it will crashed when you try to start it. As workaround you should set  to the Steam's command line for this game. So the game will work using Xwayland.

If you set  to something other than , Cities Skylines will put some files in  and some hard-coded in . Unset the variable to fix this issue.

## Textures not rendering properly
Run the game with .

## Game crashes in loading screen when Node Controller or Intersection Marking tool are enabled in Content Manager
If the game crashes with one or both of the above mods enabled when loading a save or starting a new game but works fine with both mods disabled, install .

## Civilization V
Run the game with .If  is not in , you may need to install  after making sure multilib is enabled.

For old versions of PulseAudio (8 logical cores. This includes many common CPUs, especially Ryzen 7 and i7 series parts. To diagnose this problem, check the output of dmesg:

 # journalctl -k | grep -E "Civ5XP.*segfault"

One solution is to run , which limits the number of cores that the game can access[https://steamcommunity.com/app/8930/discussions/0/1693788384127278334/. It is convenient to run this in the launch options:

 LD_PRELOAD=/usr/lib32/libopenal.so.1 taskset -c 0-7 %command%

Another solution is to set  to  in , which is stored in the game directory.==== Game crashes after intro video with "Unable to load texture (LoadingBaseGame.dds)" / configuration reset at startup ====

The issue is a result of the game calling some file in a case-insensitive manner.

The solution is either to install the game on a case-insensitive file system like VFAT, or on a mount point for .

It is not enough the game is in a case-insensitive filesystem, but also the configuration/data directory at "~/.local/share/Aspyr/Sid Meier's Civilization 5" needs to be in a case-insensitive filesystem or mount point. If the data directory is in a case-sensitive filesystem, the game will not work correctly and symptoms such as configuration getting constantly reset can be observed.

## Steam Overlay not working
An invisible Steam Overlay can be fixed by preloading the overlay renderer in the launch options:

 LD_PRELOAD='/home/username/.local/share/Steam/ubuntu12_32/gameoverlayrenderer.so' %command%

## Crashes during __memcpy_ssse3
This appears to be a memory alignment bug that can be corrected by compiling the libraries with . GDB can also be used to run it as-is with the following launch options:

 LD_PRELOAD=/usr/lib/libcurl.so.4 /bin/gdb -windows -batch -return-child-result -nx -eval-command="run" -exec=%command%

## Civilization: Beyond earth
If you are getting an instant crash/close upon launch, make sure you have the following packages installed:

*
*
*

You also need an older version of lib32-tbb which provides libtbb.so.2. To get this:

# Download the [https://archive.ubuntu.com/ubuntu/pool/universe/t/tbb/libtbb2_4.2~20130725-1.1ubuntu1_i386.deb libtbb2 deb-package from the Ubuntu archive.
# Unpack  from  into the game directory.

Note that if you have a globally installed 32-bit libtbb.so.2, you will need to run the game with:

# Run the game with .

To force it to use this version. This version also resolves crashes with the following backtrace:

    #0  0x08b71d06 in FireGrafix::DynamicsLock::DynamicsLock(Graphics::SurfaceSet**, FireGrafix::SurfaceSetPoolAllocator*, unsigned short) ()
    #1  0x08c25ffc in cvLandmarkVisSystem::cvLandmarkVisDynamicConstantUpdaterSS::HandleBuildingShaderSkinned(Graphics::FGXShaderPackageInstanceView*, FireGrafix::FGXModelNode*, FGXVector4*) ()
    #2  0x08c25f34 in cvLandmarkVisSystem::cvLandmarkVisDynamicConstantUpdaterSS::UpdateNode(Graphics::FGXShaderPackageInstanceView*, FireGrafix::FGXModelNode*, FGXVector4*) ()
    #3  0x08c25e2c in FireGrafix::FGXModelRenderByNodeSSExample_Shadow::RenderNode(unsigned int*, FireGrafix::FGX_SPIV_GENERIC*, FireGrafix::FGXModelNode*, FGXVector4*) ()
    #4  0x08c24ff5 in cvLandmarkVisSystem::LandmarkRenderJob::Execute(unsigned int) ()
    #5  0x093d26d9 in Platform::JobTask::execute() ()
    #6  0xf749f3c0 in ?? () from /usr/lib32/libtbb.so.2
    #7  0xf7497551 in ?? () from /usr/lib32/libtbb.so.2
    #8  0xf7495fc3 in ?? () from /usr/lib32/libtbb.so.2
    #9  0xf7491b7e in ?? () from /usr/lib32/libtbb.so.2
    #10 0xf7491db7 in ?? () from /usr/lib32/libtbb.so.2
    #11 0xf78f4346 in start_thread () from /usr/lib32/libpthread.so.0
    #12 0xf7716026 in clone () from /usr/lib32/libc.so.6

## Civilization VI
Although there is a native #Civilization VI Linux version, many users report better performance with the #Civilization VI Windows version.

## Civilization VI Linux version
Either run with steam-native, launch option , and go to Properties > Compatibility, check "Force the use of a specific Steam Play compatiblity tool" and select "Steam Linux runtime".

If you are using Wayland, you might need to also set , as the game's launcher uses a version of Qt which only supports Xorg (see Wayland#Qt), another way is to replace the bundled Qt with one provided by Arch Linux Some versions of the game also seem to require adding  and will otherwise refuse to start with an error message that reads "An unrecoverable error has occurred, and Civilization VI cannot continue."

Follow #OpenSSL 1.0 setup.

Ensure that Steam Workshop mods are disabled as certain ones may cause issues following loading.

## Steam Overlay not working
Since the introduction of the new launcher, the steam overlay does not work in this game. To get it working again, simlpy skip the launcher as described in #Launcher unable to load page.

## If Segfault Immediately on Start
This is a strange corner case which happens infrequently at best (and the prerequisites for reproducing it are unknown), but the crash would look like this:

# Immediate segfault on start, before any windows get created
# The game creates
# The string  appears in the backtrace output when running the game under
## To run under , first launch a shell and change into the game directory.
## Then  (otherwise the game will not launch outside of Steam itself)
## Then run something like
## The relevant info towards the end of the output should look like this:

    Thread 3 "Civ6" received signal SIGSEGV, Segmentation fault.
    [Switching to Thread 0x7fffe5d06700 (LWP 12315)
    0x000000000201121e in AppHost::BugSubmissionPackager::BugSubmissionPackager(unsigned long, String::BasicT, (String::Encoding)4> const&, String::BasicT, (String::Encoding)0> const&, AppHost::ModuleVersionInfo const&) ()
    #0  0x000000000201121e in AppHost::BugSubmissionPackager::BugSubmissionPackager(unsigned long, String::BasicT, (String::Encoding)4> const&, String::BasicT, (String::Encoding)0> const&, AppHost::ModuleVersionInfo const&) ()
    #1  0x000000000200c796 in AppHost::_INTERNAL::SetupFXSPlatform(AppHost::AppEnvironment const*, AppHost::AppOptions*)
        ()
    #2  0x000000000200fea0 in AppHost::RunApp(int, char**, AppHost::Application*) ()
    #3  0x000000000200f9bc in AppHost::RunApp(char*, AppHost::Application*) ()
    #4  0x0000000001112d98 in WinMain ()
    #5  0x00000000010bdab0 in ?? ()
    #6  0x00000000010bfb31 in ThreadHANDLE::ThreadProc(void*) ()
    #7  0x00007ffff473e08a in start_thread () from /usr/lib/libpthread.so.0
    #8  0x00007ffff38f747f in clone () from /usr/lib/libc.so.6

If all of that is the case for you, the fix is pretty simple.  Edit  and change the line reading  to .

Presumably this fix will prevent any automated bug reports from reaching Aspyr, should you encounter crashes/bugs in the future, but it will at least let the game launch properly.

## If Crash with Error "undefined symbol FT_Done_MM_Var"
If the game crashed with:

 ./GameGuide/Civ6: symbol lookup error: /usr/lib/libfontconfig.so.1: undefined symbol: FT_Done_MM_Var

The solution is to set launch options to:

 LD_PRELOAD=/usr/lib/libfreetype.so.6 %command%

## If the game ends up being a grey-color blank screen
The solution is to disable mods.

## If the computer becomes irresponsive after "Loading" screen
This may be caused by amdgpu driver crash due to insuffcient video memory. If running an integrated graphics (eg. AMD Renoir), try allocating more memory in your BIOS.

## Multi-monitor and wayland: mismatched resolution
Wayland does not define a primary monitor, so the game will show the available resolutions of an arbitrary monitor; it may not have the same size and the mouse may be off. A solution is to set an Xwayland monitor as primary.

To find the list of Xwayland monitors:

To set (eg) the XWAYLAND4 monitor as the primary:

## Launcher window is huge (wrong scaling)
If the launcher window is huge (sometimes bigger than the screen), then the scaling is wrong. Add  to the launch options and on next start the launcher should be usable.

## Launcher unable to load page
The launcher often shows errors like . It is possible to bypass the launcher by editing the games startup configuration  and changing the line  to .

## Civilization VI Windows version
To play the Windows version of Civ VI, first you must force Proton usage. Then, you need to bypass the launcher which is buggy through proton. To skip the launcher, right click on the game, click Properties, and set the following Launch options:

 eval $( echo "%command%" | sed "s/2KLauncher\/LauncherPatcher.exe'.*/Base\/Binaries\/Win64Steam\/CivilizationVI.exe'/" )

## The Clockwork Man
Requires  (pulled in by ).

## Company of Heroes 2
Make sure you have  installed.

## Missing libpcre.so.3 and libidn.so.11
Like with #Alien Isolation you need to symlink  to , as well as  to , otherwise the game will fail to start.

## Cossacks 3
## No sound
Use the steam-runtime, e.g. set the launch options to:

 ~/.steam/root/ubuntu12_32/steam-runtime/run.sh %command%

## Flashing screen with primus
Set in the launch options.

## Counter-Strike: Source (CS:S)
## Invisible symbols, special characters and cyrillic letters
Check #Squares or invisible symbols, special characters and cyrillic letters in Source-based games

## Counter-Strike: Global Offensive (CS:GO)
## Game cannot launch and crash with black screen
CSGO not running on my Arch

This problem was found after the kernel update to 5.17: the game does not start properly.

A possible workaround is to change , rename it to , then add  to the startup parameters. The game will lose the background of the main game interface, but can run normally.

## Game starts on the wrong screen
csgo-osx-linux issue #60

If it happens, go into fullscreen windowed or windowed mode and drag the window to the correct monitor. Then go back into fullscreen, the game should now be on the correct monitor.

## Cannot reach bottom of the screen on menus
csgo-osx-linux issue #594

If you have a secondary monitor you might have a part of your lower screen you cannot reach in menus.
If on GNOME you can try to open the overview (Super key) and drag the game to the other monitor and back.

If you are not on GNOME or dragging the window back and forth did not work you can try to install  and run this command, where X and Y is the offset of the window and H and W is the size.

 $ wmctrl -r "Counter-Strike: Global Offensive - OpenGL" -e 0,X,Y,W,H

Example (Secondary monitor: On the left, 2560x1600. Gaming monitor: On the right, 2560x1440) :

 $ wmctrl -r "Counter-Strike: Global Offensive - OpenGL" -e 0,2560,0,1600,1200

Here X and Y are 2560,0 to move the window to the monitor on the right and W and H are 1600,1200 is set to match the in-game resolution.

## Sound is played slightly delayed
csgo-osx-linux issue #45

See PulseAudio/Troubleshooting#Laggy sound for a possible solution.

## Mouse not working in-game
If your mouse works in the main menu but not in-game, run the game with .
If it still does not work, turn off "Raw Input" in the in-game settings.

## Brightness slider not working
Install  and run  to find out the name of your connected display output.

Edit  and add the following lines (adapt output_name):

 # gamma correction
 xrandr --output output_name --gamma 1.6:1.6:1.6 # play with values if required
 STATUS=42
 while [$STATUS -eq 42; do
  ...
 done
 # restore gamma
 xrandr --output output_name --gamma 1:1:1
 exit $STATUS

## Microphone not working
csgo-osx-linux issue #573

CS:GO uses the default PulseAudio sound device ignoring what is configured in Steam settings.

First find out the source name of your microphone (it should start with ):

 $ pacmd list-sources

Then set the default device (change the name accordingly):

 $ pacmd set-default-source device_name

Also lower the microphone level to 60% otherwise you will get some nasty background noise and you will be difficult to understand (change the name accordingly):

 $ pacmd set-source-volume device_name 0x6000

## Mouse is unrensponsive or moves slowly
Set launch options to:

 vblank_mode=0 %command%

Works with almost any other game.

## Game crashes on startup with game controller plugged in
* The solution is to add  to the launch options: csgo-osx-linux issue #1757

* Another solution: delete startup video: csgo-osx-linux issue #2659

## Some texts are missing or mis-positioned
Generate the  locale will solve the problem.

## Stuck on map loading "Initializing World"/"Loading Resources" with AMD Radeon RX 6000 series
csgo-osx-linux issue #2801

When using the amdgpu driver, some users experience a problem with map loading taking longer than one minute and being stuck on "Initializing World" or "Loading Resources".
You can try the following workaround:

Create the file:

{{hc|/etc/udev/rules.d/70-amdgpu-mclk.rules|2=
KERNEL=="card0", SUBSYSTEM=="drm", DRIVERS=="amdgpu", ATTR{device/power_dpm_force_performance_level}="manual", ATTR{device/pp_dpm_mclk}="1 2 3"
}}

This disables the lowest memory clock state "0".

Activate immediately with:

 # udevadm control --reload && udevadm trigger

## Creeper World 3: Arc Eternal
## Game does not start
Search for  (might be in ).

If it says somewhere in :

 FMOD failed to get number of drivers ... An error occured that was not supposed to.  Contact support.

Unity is probably having problem with some PulseAudio libraries.

Remove or rename all instances of libpulse-simple* files in , , , .

## CrossCode
## If FontConfig errors on start
Download the latest version of nwjs from [https://nwjs.io/ here and extract its contents into your CrossCode directory, overwriting the files.

Be sure to rename  to  after.

This solution was documented to work with CrossCode 1.2 and nwjs 0.41.2 and is based on this steam post

## Crash during startup : X server probably went away
If the game crashes on startup, with the logs ending with a line like the following:

 X IO error received (X server probably went away)

Add  to the launch options (as documented [https://steamcommunity.com/app/368340/discussions/1/1733213724900972605/?&ctp=6#c3185738591085997507 in this steam post).

## Crusader Kings II
## No audio
SDL uses PulseAudio by default, so to use it with ALSA you need to set the  environment variable.

## Oddly sized starting window
You can make full screen mode the default by setting  in .

## DLCs not detected
If the DLC tab in the launcher is not selectable, rename the  directory in the game directory to .

## Game takes ages to start
If you are using a NVIDIA graphics card, make sure you have enabled the DRM kernel mode setting.

## Game does not start at all
If the game stopped launching after Patch 3.3 (when the game became 64-bit only), install .

## Crypt of the NecroDancer
## Crashes after splash screen
The following error occurs if launching Steam from the terminal.

 FMOD ERROR: UpdateFMOD SystemUpdate: This command failed because System::init or System::setDriver was not called.

This error is solved by installing .

## Game does not launch at all (Wayland)
On Wayland, it is currently (as of May 2024) necessary to add  to your launch options. If you have not added any launch options, also add  at the end of your launch options. Game should launch normally.

## The Curious Expedition
## Game stuck on loading screen
The Electron shipped with this game is too old for Arch Linux.

Install  and run the game with .

## Death Road To Canada
## No music
Prepend  to .

## Deus Ex: Mankind Divided
Follow #OpenSSL 1.0 setup.

Requires  & .

Also if you use Bumblebee set your launch options to:

 LD_PRELOAD="$LD_PRELOAD:libpthread.so.0:libGL.so.1" __GL_THREADED_OPTIMIZATIONS=1  optirun %command%

If the game will not activate and you are running systemd-resolved and Proton, follow Steam/Troubleshooting#Games running with Proton 5.13+ have no Internet connectivity.

## Dirt
Follow #OpenSSL 1.0 setup.

## Dirt Rally
Run the beta version: right click on the game, then Properties… > Betas, enter the code: "feraldirtsupport" and click Check Code, finally, choose feral_support_branch as the version.

To use the native libraries, installing  and  is required.

If you use Wayland, start the game with . Similarly, if you use PipeWire, start the game with  - other backends might also work, but the default one does not.

Due to changes in how linking works, the game might not properly load its bundled dependencies. To fix this, you can either run the game with  or symlink the libraries from  to .The game may also segfault if you use an AMD Zen 3 or newer CPU. To fix this you can hack together a small shared library to replace the  function and make sure the allocated memory has the  access flag.[https://news.ycombinator.com/item?id=25821288. Here is an example:

 $ cat game.c
 #include
 #include
 #include

 int mprotect(void *addr, size_t len, int prot) {
   if (prot == PROT_EXEC) {
     prot |= PROT_READ;
   }
   return syscall(__NR_mprotect, addr, len, prot);
 }

You can then compile the library and move the shared object to the game libraries:

 $ gcc game.c -shared -o game.so
 $ mv game.so GAME/lib/

After that you can add  to the game launch options.

## Divinity: Original Sin - Enhanced Edition
## Game does not start when using Bumblebee optirun or primusrun
Edit  to use primusrun:

 LD_LIBRARY_PATH="." primusrun ./EoCApp

## Game does not work with mesa
It is a known bug and they have no intention of fixing it, see the bug.

Workaround(see [https://bugs.freedesktop.org/show_bug.cgi?id=93551#c46 step by step guide)

Get the following file:
https://bugs.freedesktop.org/attachment.cgi?id=125302
and rename it to

Then execute:

 $ gcc -s -O2 -shared -fPIC -o divos-hack.{so,c} -ldl

Copy the  to the game directory.

For GOG version, go to the said game directory and run Divinity with the following command:

 $ allow_glsl_extension_directive_midshader=true LD_PRELOAD="divos-hack.so" ./runner.sh

For steam, open a console, change to the divinity directory with

 $ cd ~/.steam/steam/steamapps/common/Divinity Original Sin Enhanced Edition

Launch steam and got o the preferences of the game, and open the "Set Launch Options" dialogue. There, put the following

 allow_glsl_extension_directive_midshader=true LD_PRELOAD="divos-hack.so:$LD_PRELOAD" %command%

Then just start the game.

## Doki Doki Literature Club
Linux version is shipped with the Windows version, but can only be installed with Steam Play.

Native version can be started with this launch option:

## Don't Starve Together
If you get a crash on start in , the problem is likely a bug in SDL1.3. Unfortunately, DST is statically linked and we cannot use  to replace libSDL with something newer. The bug has been reported to the developer, but a possible workaround is to patch  to not crash when it is incorrectly given a null parameter.

## Dota 2
Dependencies:

*
*

## In-game font is unreadable
Run the game with .

## Error with libpangoft2
# Install the  package.
# Remove  and  in .
# If you are using Bumblebee add  to your launch options.

## The game does not start
If you run the game from the terminal and, although no error is shown, try disabling: Steam > Settings > In-Game > Enable Steam Community In-Game.

Apparently the game #The Book of Unwritten Tales has the same problem. It also describes a workaround that is untested in Dota 2.

## Game runs on the wrong screen
See GitHub Dota 2 issue #11

## Game does not start with libxcb-dri3 error message
After a recent Mesa update, Dota 2 stopped working. The error message is:

 SDL_GL_LoadLibrary(NULL) failed: Failed loading libGL.so.1: /usr/lib32/libxcb-dri3.so.0: undefined symbol: xcb_send_fd

## Game has no audio
This might happen because Dota 2 is trying to output through ALSA, which has already been taken over by PulseAudio. Try installing  and setting in-game audio output to 'Default'.

## Steam overlay
Steam distributes a copy of libxcb which is incompatible with the latest xorg libxcb. See [https://github.com/ValveSoftware/steam-for-linux/issues/3093.

## Clear or disable shader cache for troubleshooting purposes
To clear shader cache delete delete the 570 (Dota's app ID) directory under the steam shadercache directory e.g.

 /home/username/steam/steamapps/shadercache/

To disable shader cache add the following to dota's launch options:

 -vulkan_disable_steam_shader_cache

## Chinese tips and player names not shown
The Chinese characters in tips and player names are displayed as block characters.

The problem is caused by the font packages: ,  and .

See GitHub Steam issue #1688

## Chinese input method problem
Dota2 is compatible with IBus and Fcitx. XIM support Should be enabled.

 XMODIFIERS=@im=fcitx %command%

## Devil Daggers
Refer to #Missing libcurl.so.4 or version CURL_OPENSSL_3 not found.

## Drox Operative
If the game fails to start with "Couldn't find Database/database.dbl!", manually extract the assets. assets003.zip will overwrite some files from the previous files.

 $ cd "~/.steam/root/steamapps/common/Drox Operative/Assets"
 $ unzip assets00=== Dungeon Souls ===

For AMD cards this game crashes on launch, unless you start it like this:

 R600_DEBUG=mono %command%

## Dying Light
## Game crashes on startup
The game runs with the Steam setting "Force the use of a specific Steam Play compatibility tool" > "Steam Linux Runtime"

## Dynamite Jack
Requires .

## Sound Issues
When running on 64-bit Arch Linux, there may be "pops and hisses" when running Dynamite Jack. This could be caused by not having  set. (However, even with  set, the game may still sometimes start with this issue. Exiting and restarting the game seems to make the problem go away.)

## Game does not start
If running steam with the , Dynamite Jack may have a problem starting. Check the steam error messages for this message:

 /home/username/.steam/root/steamapps/common/Dynamite Jack/bin/main: error while loading shared libraries: libSDL-1.2.so.0: cannot open shared object file: No such file or directory

Install  from multilib and Dynamite Jack should start up.

## Empire Total War
## Weird unreadable fonts
Open , then find  and change it from 1 to 0.

## Euro Truck Simulator 2
## Shows only a black screen
Select safe mode when the game starts up.

## Firewatch
If Firewatch starts but does not show anything, try running Steam with

 $ STEAM_RUNTIME_PREFER_HOST_LIBRARIES=0 steam

## Football Manager 2014
This game will not run when installed on an XFS or ReiserFS filesystem. Workaround is to install on an ext4 filesystem.

## FORCED
Requires .

This game has 32-bit and 64-bit binaries. For some reason, Steam will launch the 32-bit binary even on 64-bit Arch Linux.
When manually launching the 64-bit binary, the game starts, but cannot connect to Steam account, so you cannot play.
So install 32-bits dependencies, and launch the game from Steam.

## For the King
## With steam-native
Starts with black page. Requires to be told to use the libSDL2 shipping with Steam

Add to Steam launch options for game:

 LD_PRELOAD=~/.local/share/Steam/ubuntu12_32/steam-runtime/amd64/usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0 %command%

Note however, that this disables the Steam overlay as a side effect.

## With steam-runtime
It works out of the box.

For the full experience, run FTK via steam-runtime instead of steam-native.

## FTL: Faster than Light
## Compatibility
After installation, FTL may fail to run due to a 'Text file busy' error (characterised in Steam by your portrait border going green then blue again). The easiest way to mend this is to just reboot your system. Upon logging back in FTL should run.

The Steam overlay in FTL does not function as it is not a 3D accelerated game. Because of this the desktop notifications will be visible. If playing in fullscreen, therefore, these notifications in some systems may steal focus and revert you back to windowed mode with no way of going back to fullscreen without relaunching. The binaries for FTL on Steam have no DRM and it is possible to run the game without Steam running, so in some cases that may be optimum - just ensure that you launch FTL via the launcher script in  rather than the FTL binary in the $arch directory.

## Problems with open-source video driver
FTL may fail to run if you are using an opensource driver for your video card. There are two solutions: install a proprietary video driver or delete (rename if you are unsure) the library "libstdc++.so.6" inside . This is if you are using a 64bit system. In case you are using a 32bit system you have to remove (rename) the same library located into .

## Artifacts when launching, Problems with openGL
Using the open source drivers, ATI for radeon cards, the game can display artifacts on screen. Run the game with

## Game Dev Tycoon
## Game does not start
You might get an error about missing .

Run the game with .

## Garry's Mod
## Game does not start
When an error about a missing  appears, try the following:

 $ cd ~/.steam/root/steamapps/common/GarrysMod/bin/
 $ ln -s libawesomium-1-7.so.0 libawesomium-1-7.so.2
 $ ln -s ../garrysmod/bin/client.so ./

If the error mentions a missing library for , install .

## Opening some menus causes the game to crash
Most menus work fine, but ones with checkboxes (LAN multiplayer, mounted games list) do not work at all. This is a bug in the menu code.

If you prefer the default menu style and do not mind a hacky solution: [https://github.com/Facepunch/garrysmod-issues/issues/86#issuecomment-30935491 Simon311 has written code with instructions to fix it.

If you do not care for the default menu style and want a more stable but feature-incomplete solution, Facepunch developer robotboy655 has written a new menu.

## Game crashes after attempting to join server
While in the process of joining a server, downloading resources, etc, the game seems to hang and after a while, perhaps during the "sending client info" portion the game crashes, usually without any error messages. Error does not give much information, however, the process for Garry's mod is killed.

This issue arises more often when joining servers with many addons like DarkRP servers specifically.

The problem seems to correlate with a weak GPU and the game is timing out from the server, so if the GPU is the problem, lowering the graphics settings to the minimum should fix the problem.

The problem seems to be related to RAM usage, once you hit around 2GB of RAM used, the game will crash. Servers with many addons have much more RAM usage, and lowering graphics settings to the minimum lowers RAM usage and mitigates crashes.

Using the experimental x86-64 branch may help mitigate this issue, however keep in mind that some addons may return errors while using this branch.

## Gods will be watching
Follow #OpenSSL 1.0 setup.

## GRID Autosport
Follow #OpenSSL 1.0 setup.

## Black screen when trying to play
Run the game with .

## Guns of Icarus Online
If you encounter problems, check out the error log:

 ~/.config/unity3d/Muse Games/GunsOfIcarusOnline/Player.log

## version `CURL_OPENSSL_4' not found (required by /usr/lib/libdebuginfod.so.1)
Install the package  and include 'libcurl.so.4' in your LD_PRELOAD in your shell environment like so:

 export LD_PRELOAD=$LD_PRELOAD libcurl.so.4

## Hack 'n' Slash
## Crashes when trying to load a game
Prepend  to .

## Hacker Evolution
Requires .

## Half-Life
## Invisible text
Half-Life uses microsoft fonts to display text, see Microsoft fonts for ways to install them.

## Half-Life 2 and episodes
## Cyrillic fonts problem
This problem can be solved by deleting "Helvetica" font.

## Hammerwatch
## The game does not start via Steam
Prepend  to .

## No sound
Hammerwatch opens with a popup: "Sound Error" -- "Could not initialize OpenAL, no sounds will be played.  Try updating your OpenAL drivers."

OpenAL, which Hammerwatch uses, defaults to PulseAudio. To change that, add the following line to :

 drivers=alsa,pulse

This way, Hammerwatch will use ALSA.  This solution was found here.

## Harvest: Massive Encounter
Dependencies:

*
*
*
*
*
*

## Compatibility
If the game refuses to launch and throws you into a library installer loop, run the  executable instead of the  script.

## Hatoful Boyfriend
## Japanese text invisible
Install  and .

## HEARTBEAT
## If FontConfig Errors on Start
Follow the same process described in #CrossCode.

## HuniePop
## Game crashes upon launch
Install .

## Hyper Light Drifter
## The controller does not work
Install  and run the game with .

See the following Steam Community discussions:

* Controller Issues
* Common Bugs + Known Issues

It is suggested to run the next_update branch to get new fixes,
there however currently is a libcurl segfault keeping it from starting without special workarounds.

## Missing libcurl.so.4 or version CURL_OPENSSL_3 not found
Refer to #Missing libcurl.so.4 or version CURL_OPENSSL_3 not found.

## Rome Total War Remastered
## Slowness of loading screen for open-source drivers
Install  and then change the renderer option in the game launcher to llvmpipe after a system restart.

Once done the loading screen scene would then be fixed and should load up as normal for open-source drivers.

## Imperator: Rome
Paradox Launcher freezes or crashes after start. Set your launch options to:

 LD_PRELOAD=/usr/lib/libc.so.6 %command%

If the screen freezes every ~3 seconds, run:

 # chmod o-rx /dev/input/

After playing, undo it with:

 # chmod o+rx /dev/input/

## The Impossible Game
Dependencies:

*
*

## The Inner World
Requires  for sound support.

## Bringing up the inventory or main menu
Hold the tab key.

## Cutscenes
The game has cutscenes. It starts directly with a cutscene before you start the actual game in the backyard. To see these cutscenes you need to use Oracle's Java instead of the OpenJDK.

Furthermore you need the package .

There seem to be problems with the Steam overlay. Try to run the game directly with .

Note that cutscenes open in a new window. So pay attention to that and switch to the new window to enjoy the movies.

See the Steam Forums for details.

## Insurgency
## Game does not start
Set the following launch option:

 LD_PRELOAD='/usr/$LIB/libstdc++.so.6:/usr/$LIB/libgcc_s.so.1:/usr/$LIB/libxcb.so.1:/usr/$LIB/libgpg-error.so' %command%

## Interloper
Requires .

## Game does not start
The game can sometimes segfault due to an incompatibility with the Steam Runtime's .

## Invisible Apartment
Requires .

## Game does not start
If the game does not run when you launch it via Steam, try to directly run  in the game directory.

## Joe Danger 2: The Movie
Requires .

## Compatibility
Game only worked after obtaining from the Humble Bundle directly and  was installed.

## Kerbal Space Program
See Kerbal Space Program.

## Killing Floor
## Cannot change screen resolution
If trying to modify the resolution in-game crashes your desktop environment, edit :

 WindowedViewportX=width
 WindowedViewportY=height
 FullscreenViewportX=width
 FullscreenViewportY=height
 MenuViewportX=width
 MenuViewportY=height

 [SDLDrv.SDLClient
 WindowedViewportX=width
 WindowedViewportY=height
 FullscreenViewportX=width
 FullscreenViewportY=height
 MenuViewportX=width
 MenuViewportY=height

## Windowed mode
Uncheck fullscreen in the options menu, and press  to stop mouse capturing.

## Stuttering sound
KillingFloor comes with its own OpenAL library .

Back it up, install  or  (if using a 64bit system).

Then symlink the installed system library ( or ) to .

## Left for Dead 2
## Missing Chinese font
L4D2 looks for the WenQuanYi font to render Chinese text with. You can either install a package that provides the font, such as  or , or configure a fallback font:

## Game Light Too Dark
Reasons of too dim in-game environment light varies, one of which is dedicated GPU is not employed.

According to multiple steam guide, please run this game using NVIDIA GPU with 32-bit libraries support.

## Lethal League
Requires .

## Life is Strange
Requires      .

## Little Racers STREET
Install .

Move/backup .

Symlink  to .

## The Long Dark
## Game does not start
The 64-bit version fails to start. Either use the 32-bit version  in the game directory or start the 64-bit version like so:

 LD_PRELOAD=~/.steam/root/ubuntu12_32/steam-runtime/amd64/usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0 ./tld.x86_64

## Game starts, but some overlay text is missing and cutscenes shows black screen
In addition to the command above, add the following to the Steam launch command:

 -screen-fullscreen 0 -screen-width WIDTH_PIXELS -screen-height HEIGHT_PIXELS

For example, if you have a screen resolution of 1280x720 and are launching the x64 version from the terminal (within the directory which contains the binaries), the full command would be:

 $ LD_PRELOAD=~/.steam/root/ubuntu12_32/steam-runtime/amd64/usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0 ./tld.x86_64 -screen-fullscreen 0 -screen-width 1280 -screen-height 720

and from Steam, the complete game launch options would be:

 LD_PRELOAD=~/.steam/root/ubuntu12_32/steam-runtime/amd64/usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0 %command% -screen-fullscreen 0 -screen-width 1280 -screen-height 720

## Cutscenes are still black
Turn off Vertical Sync in the Display options, and/or set POST FX to Low in the Quality options, and/or turn global Quality options down a notch.

## Cursor disappears
Go to Options > Controls, and set mouse locking to unlocked.

The options is visible only if you are navigating using your (invisible) mouse. It will not show up when navigating with a controller.
One solution is to go to Options -> Controls with a controller before switching to the mouse and trying to blindly it the setting.

## Grand Theft Auto V
## BattleEye connection issues
See #BattlEye.

Modify launch options to include :

## Game crashes in Online
If you experience crashes in GTA Online (e.g. when creating a new character), set these launch options:

 PROTON_NO_ESYNC=1 WINEDLLOVERRIDES=winedbg.exe=d %command%

## Graphical Issues using a NVIDIA GPU
Try launch options: -force-glcore42 -force-clamped

## Magicka 2
## Indefinitely stuck at start
The game does not start if the output of the command "ip -s link" is longer than 4096 characters. That is because, in the function bitsquid::network_info(char*), where they query the networking information, they do not handle that case correctly.
See this picture for reference.
It was reported to upstream (Pieces Interactive) but Magicka 2 does not seem to be maintained anymore.

A dirty fix is to wrap your ip binary, as such:

## Mark of the Ninja
## Bad sound
Prepend  to .

## Metro: Last Light
The game does not allow you to change its resolution on a multi-monitor setup on GNOME with the AMD Catalyst drivers. A temporary workaround is to disable the side monitors.
Jason over at unencumbered by facts managed to get it working with his multi-monitor setup using a single display server, he however is using NVIDIA.

## Metro: 2033 Redux
## No sound
Install .

## No image
Try setting  in .

## Middle-earth: Shadow of Mordor
## Floating heads
Run the game with .

## Mount & Blade: Warband
## Segmentation fault (core dumped) with Wayland
Use Xorg instead, or force the session to use  as .

## DLC chooser
Requires building .

## Crash on startup
Set launch options to:

 LD_LIBRARY_PATH="." %command%

## Move or Die
## No Sound
Install .
Remove file "Move or Die/Love/linux32/libogg.so.0"

## Multiwinia
Requires .

## Crash on startup
If Multiwinia crashes on startup on X64 systems, force launching the 32-bit executable by replacing  with the following script:

See === Natural Selection 2 ===

 is required, furthermore, you must also execute
 $ ln -s /usr/lib/libsndio.so x64/libsndio.so.6.1
within the root of the NS2 directory.
This is because NS2 uses an older outdated version of sndio, but it is still compatible with the new version, thankfully.

For a more minimal solution, one can attempt to set the audio driver used through the environment variable . For example,  or .

The environment variable  must not be set to .
Try setting  to  if it still does not work.

## No Man's Sky
## Black screen at start
Edit  and set  to  and  to .

## White screen at start
If you get a white screen, it may seem like the game has froze, but it has not. Hold down  to continue.

## Nuclear Throne
Refer to #Missing libcurl.so.4 or version CURL_OPENSSL_3 not found.

## OneShot
## Game fails to start
This problem occurs because the game use outdated libraries. Go to the game directory and remove , , , ,  and . Those files usually have an equivalent already installed on the system.

## File _______ will not run
The executable _______ may fail when run from the Documents directory. It also exists in the game directory and will run from there.

## Game fails to start on Wayland
Run the game with .

## Oxygen Not Included
## World generation hangs
This problem occurs with locales that use comas instead of dots to separate decimals.

Set launch options in steam to .[https://steamcommunity.com/app/457140/discussions/3/1488866180617243731/#c1488866813753688864

## Graphics errors, corruption and lines through tiles
This is a result of using the Zink MESA driver. If you have this globally enabled, disable it specifically for this game and launch it normally.

## Pandora: First Contact
## Launch issue
If the game refuses to launch at start you will need to replace bundled libraries by those from the main system.

Replace the bundled files in the game binaries directory with symlinks to , ,  and  from  to allow the game to launch as normal.

## Patrick's Parabox
## Blank Screen
Add the following to Steam launch options:

 LD_PRELOAD=Patrick\'s\ Parabox_Data/Plugins/libfmodstudio.so %command%

## Penumbra: Overture
Dependencies:

*
*
*
*
*
*

## Windowed mode
There is no in-game option to change to the windowed mode, you will have to edit  to activate it.

Find  and change it to , after this the game should start in windowed mode.

## Portal 2
## Game does not start
Several OpenGL-related errors (such as  or ) are caused by Portal&nbsp;2 bundling an old libstdc++ file. This error is especially common with open source Radeon drivers ().

A problem with libstdc can be fixed by running the game with .

## Resolution too low
When the game starts with a resolution so low that you cannot reach the game settings,
run the game in windowed mode using the  flag.

## Missing non Latin font
The phenomenon is no menu in Portal. Portal and Portal2 use Helvetica, add the following lines to :

         Helvetica

         Source Han Sans CN

You can replace "Source Han Sans CN" by your favoriate and existing font.

## Prison Architect
## ALSA error when using PulseAudio or PipeWire
The error:

 ALSA lib pcm_dmix.c:1018:(snd_pcm_dmix_open) unable to open slave

was resolved by installing:

*
*
*

per PulseAudio#ALSA.

Alternatively, if running the game through Steam, you can force the game to be ran through proton, and that can resolve other audio errors.

You can do this by opening the game's properties through steam, and under "general" tick the "Force the use of a specific Steam Play comparability tool", and then select a proton version from the dropdown below

## Game only starting in safe mode
If the game does not start, but Steam thinks it is running, probably the Paradox launcher has problems running properly.
If this is the case, you will find some processes running in background:

Kill them all, then modify the game startup options as follows:

 LD_PRELOAD=/usr/lib64/libc.so %command%

Eventually, if the above option has not worked, an option to skip it:

 ./PrisonArchitect %command%

Note: even if we are using another executable to start the game,  has to be added at the end of the command to trick Steam.

## Project Zomboid
## No sound
Prepend  to .

In the game, go to the options and set all audio to the proper volume.

## Redshirt
Requires  if you use PulseAudio.

## Revenge of the Titans
Requires  and .

## Rise of the Tomb Raider
Run in an X session.

## Game does not start
If running in X session is not available or is not preferred, another alternative is to create the script:

and make it executable.

After this the game was found to have loaded on Linux according to some game testers.

## Risk of Rain
Refer to #Missing libcurl.so.4 or version CURL_OPENSSL_3 not found.

## Rock Boshers DX: Directors Cut
Requires .

## Saints Row: The Third
## Impossible to save custom display settings
Although game settings menu allows to choose custom display settings, the game may have problems saving them.

In such case, adjust these settings manually in the game's configuration file .

The comments in this file explain well all the settings and acceptable values.

## Incorrect screen resolution in game
This can occur when game is launched in a multi-head environment, with some monitors rotated, etc., so the game detects available screen resolutions incorrectly.

In such case, adjust  and  options in the  file. Also, one must set option .

## Saints Row IV
## Game fails to launch after update to new NVIDIA drivers
Run the game with  appended to the .

## Game causes GPU lockup with mesa drivers
Saints Rows IV can cause a GPU lockup when trying to play on certain AMD
hardware using open source drivers: Bug 93475.

A workaround is to run the game with .

## Serious Sam 3: BFE
## No audio
Try running:

 # mkdir -p /usr/lib/i386-linux-gnu/alsa-lib/
 # ln -s /usr/lib32/alsa-lib/libasound_module_pcm_pulse.so /usr/lib/i386-linux-gnu/alsa-lib/

If that does not work, try tweaking  as proposed by the Steam community (Serious Sam 3: BFE uses OpenAL to output sound). If you are not using PulseAudio, you may want to write the following configuration:

## SJ-19 Learns to Love
If the game crashes at startup with this error in Steam's output:

 /home/username/.local/share/Steam/steamapps/common/SJ-19 Learns To Love/sj-19-linux/sj-19-learns-to-love.x86_64: error while loading shared libraries: libsteam_api.so: cannot open shared object file: No such file or directory

Right click the game in steam, select Properties, and set this in Launch Options:

 LD_LIBRARY_PATH=./sj-19-linux %command%

## Slay the Spire
If the game does not start or crashes at startup, install .

If the game crashes with the xrandr stacktrace:

It is likely due to a known bug in LWJGL. The workaround is to change the xrandr configuration to only contain the resolution (For example:  should become .

If the game does not move sink input, you can edit the following file to allow sink moves:

## Stick Fight: The Game
If the game does not launch, try appending  to force using WINE direct3D. To do this you must have  installed.

## Songbringer
## Launch error with Wayland
Install  and run the game with .

## Space Pirates and Zombies
Requires .

## No audio
Try running:

 # mkdir -p /usr/lib/i386-linux-gnu/alsa-lib/
 # ln -s /usr/lib32/alsa-lib/libasound_module_pcm_pulse.so /usr/lib/i386-linux-gnu/alsa-lib/

If that does not work, try tweaking  as proposed by the Steam community (Serious Sam 3: BFE uses OpenAL to output sound). If you are not using PulseAudio, you may want to write the following configuration:

## Spacechem
Dependencies:

*
*
*

## Game crash
The shipped x86 version of Spacechem does not work on x64 with the game's own libSDL* files, and crashes with some strange output.

To solve this just remove the three files , ,  from the game directory.

## Splice
Requires .

## The Stanley Parable
## Game will not start
As discussed in the Steam store page, remove  from the game directory.

## Shadow Tactics: Blades of the Shogun
Dependencies:

*
*
*

## Stardew Valley
## Unable to move or input text
When in game, you are stuck in your bed as you cannot move your character or you cannot enter text into the input fields when starting a new game. This is a bug with the SDL2 lib bundled with the game.

Install .

Modify this config line:

To this (the period is removed at the beginning of target):

## Steel Storm: Burning Retribution
## Start with black screen
The game by default tries to launch in fullscreen mode with a resolution of 1024x768,
which does not work on some devices (for example the Samsung Series9 laptop with Intel hd4000 video).

Run the game in windowed mode by using the  flag. Then change the resolution in-game.

## Stellaris
## No window opening, only sound
Happens with some AMD GPU and mesa combination, set  in .

On some window managers (e.g. Xmonad) you should set .

## Immediate crash to desktop
## Steam using Proton instead of Linux Runtime
To diagnose, run Steam in a terminal and launch Stellaris. Ignore any errors mentioning "LD_PRELOAD" and look for this error:

 /home/username/.local/share/Steam/steamapps/common/Stellaris/dowser.exe: /home/username/.local/share/Steam/steamapps/common/Stellaris/dowser.exe: cannot execute binary file

If you see that error then the solution is to force Steam to use the Linux runtime for Stellaris:

# Right-click on Stellaris and select "Properties..."
# Select the "Compatibility" tab.
# Select "Force the use of a specific Steam Play compatibility tool".
# Select "Steam Linux Runtime 1.0 (scout)"

## Missing libnss_sss.so.2
It seems that Stellaris requires a 32bit libnss_sss.so.2 to operate. You can confirm if this is your problem by running

 $ strace ~/.local/share/Steam/steamapps/common/Stellaris/stellaris 2>&1 | grep sss

and seeing if you get output like

 openat(AT_FDCWD, "/usr/lib32/tls/i686/sse2/libnss_sss.so.2", O_RDONLY|O_LARGEFILE|O_CLOEXEC) = -1 ENOENT (No such file or directory)

If this is indeed your problem, download the libnss-sss package from Ubuntu's repository extract the libnss_sss.so.2  from the downloaded package, and place it at ~/.local/share/Steam/steamapps/common/Stellaris. The game should now load properly.

## Game instantly crashes to desktop on Wayland
Append  to your launch options.

## Launcher is blank
This is a recurring problem on Linux following the Machine Age expansion. If this happens to you, back up all your custom empires and savegames (found in  and  for cloud saves). If you have no other Paradox games installed, then remove the Paradox Interactive directory underneath .

If you have other Paradox games installed, then do not remove the entire Paradox directory. Just remove the Stellaris directory and the launcher-v2 directory.

Attempt to run the game again. The launcher should open normally after re-downloading. Once the game launches properly, close the game and put your empires and savegames back in their directories from where you got them.

## Stephen's Sausage Roll
## No sound
If using native libraries and  is installed, Unity may try to use that library for sound and fail.
To test if this is the problem, try removing  or renaming the package files that are named .  To see which  files are relevant, run:

If renaming any of those files works for you, you can proceed with the following instructions (revert any renaming you just did).  Browse to the game's directory:

 $ cd "$HOME/.steam/root/steamapps/common/Stephen's Sausage Roll"

And create a sub-directory that we can use to hold 0-byte look-alike library files:

 $ mkdir noload/

Use  to create 0-byte versions of the above files that we want the dynamic linker to skip, e.g.:

 $ touch noload/{libpulse-simple.so,libpulse-simple.so.0,libpulse-simple.so.0.1.0}

After you have created these 0-byte files, you can now attempt to run the game binary directly, telling the dynamic linker to use our 0-byte files:

 $ LD_LIBRARY_PATH="noload/:$LD_LIBRARY_PATH" ./Sausage.x86_64

If everything works up to this point, prepend  to your .

Again, this should work because Steam checks for a  directory relative to the game's directory.  The dynamic linker should respect the  variable and fail to load the necessary  files.  The game should then fallback to plain ALSA.

## Superbrothers: Sword & Sworcery EP
Dependencies:

*
*  if you use PulseAudio

The game bundles an outdated version of libstdc++ which prevents the game from starting. [https://steamcommunity.com/app/204060/discussions/0/364039785161291413 The following can be observed when you run Steam and S&S from the terminal:

 libGL error: unable to load driver: i965_dri.so
 libGL error: driver pointer missing
 libGL error: failed to load driver: i965
 libGL error: unable to load driver: i965_dri.so
 libGL error: driver pointer missing
 libGL error: failed to load driver: i965
 libGL error: unable to load driver: swrast_dri.so
 libGL error: failed to load driver: swrast

To solve this problem remove . After that the game will use the libstdc++ from Steam.

## System Shock 2
You get these errors when running it with the native client:

 C:\windows\system32\winedevice.exe: symbol lookup error: /usr/lib32/libX11.so.6: undefined symbol: xcb_wait_for_reply64
 C:\windows\system32\wineboot.exe: symbol lookup error: /usr/lib32/libX11.so.6: undefined symbol: xcb_wait_for_reply64

Just delete or rename the libxcb library it got shipped with:

 mv /mnt/olhdd/steam/steamapps/common/SS2/lib/libxcb.so.1{,.old}
 mv /mnt/olhdd/steam/steamapps/common/SS2/lib/libxcb.so.1.1.0{,.old}

## Game does not launch
If you encounter the game not launching, do the following:

# Move  from the  directory within the main Steam common directory and transfer it to the  main game directory, not the  subdirectory.
# Put  into the launch options.

Once all of these have been implemented, the game should work.

## Resolution fix
You may encounter some resolution problems with this game on Steam not working properly in full screen mode. Do the following:

# Open  in the  directory, you may have to search for it via the search mode while in the game directory.
# Place  or  depending on your resolution and put  into bottom of the  file.
# Go to  and next to the display setting place a semicolon prefix next to the  option so it should be like this:

It should then properly not go off-screen and should stay full screen within the active main screen.

## Sven Co-op
## No sound in-game (FMOD ex error code 60)
If using PipeWire, make sure you have installed .

## Tabletop Simulator
## CJK characters not showing in game
Install  and .

## Team Fortress 2
As of an update in September 2023, the game will not have the correct version of  and will silently crash during launch.

Follow the fix outlined in #tcmalloc.cc error in Source 1 games

## HRTF setup
Assuming HRTF (head-related transfer function) has been properly set up in the operating system, HRTF will not be enabled unless you disable the original processing. To do so, add this to your autoexec

 dsp_slow_cpu 1

For best results, also change the following:

 snd_spatialize_roundrobin 1
 dsp_enhance_stereo 0
 snd_pitchquality 1

## Loading screen freeze
If you are a non-English (speaking) user, you have to enable "en_US.UTF-8" in the locale.gen! Generate a new locale after that.

## No audio
It happens if there is no PulseAudio in your system.
If you want to use ALSA, you need to launch Steam or the game directly with
(From SteamCommunity).

If it still does not work, you may also need to set the environment variable AUDIODEV. For instance . Use  to list the available sound cards.

## Slow loading textures
If you are using Chris' FPS Configs or any other FPS config, you may have set  to . This spawns multiple threads for texture loading, which may cause more jittering and lag on Linux, especially on alternative kernels. Try setting it to , the default.

## "Invalid color format" Error at loading screen on integrated Intel Atom/BayTrail HD Graphics
Add the following to the game startup options:

 -force_vendor_id 0x10DE -force_device_id 0x1180

These options deceive the game engine that we are having a NVIDIA GPU, not Intel/AMD.

## Wrong mouse sensitivity
TF2 ships with an old version of libSDL2.so.
Following mastercomfig's guide helps using the Steam Runtime instead of using the bundled libSDL2 version and updates the Steam Runtime by using the Distribution shipped version.

## Terraria
See the KNOWN ISSUES & WORKAROUNDS​ section of the release announcement.

## Input Issues
The symptoms of this problem are: When moving after standing still, your character seems to vary their speed, if wearing running boots they do not activate. When jumping with an item for double jumping sometimes you double jump even if you just jumped once. Going up/down ropes seems slow/choppy.

The solution is to preload the system SDL2 libraries:  For more information: Terraria Forums

## This War of Mine
## Game does not start
This happens because of an incompatibility with the newer version of . To fix the problem, set your launch options to:

 LD_PRELOAD=./libcurl.so.4 %command%

## Sound glitches with Steam native
The bundled  might not work correctly, try symlinking  to .

## Ticket to Ride
Dependencies:

*
*

As lib32-gstreamer0.10-base is quite hard to build you can use multilib-alucryd repo for this package

## The Tiny Bang Story
## Missing libGLEW.so.1.6
 # ln -s /usr/lib32/libGLEW.so.1.10.0 /usr/lib32/libGLEW.so.1.6

## Tomb Raider (2013)
## Game immediately closes
Tomb Raider has a very heavy amount of dependency on the Steam runtime, the easiest solution is to just run it using the runtime.

If this does not solve the problem, look up the shared library dependencys of the main executable. Go into your steam directory and do

 $ ldd steamapps/common/Tomb\ Raider/bin/TombRaider | grep found

Note all missing librarys and try installing them from the standard repositories and the AUR. If after that you are still missing librarys you can search on the web for them and download corresponding packaged .rpm x86 (32bit) files and extract them into  to provide the missing librarys. Run ldd again and see whether you have all the necessary librarys installed. If there are no more missing librarys and the added librarys are of the correct version, architecture and 32/64bit word length and are placed on one of the linkers search paths then the game should work.

Another alternative to this is to do the following in the Launch options:

 LD_LIBRARY_PATH="$HOME/.local/share/Steam/steamapps/common/Tomb Raider/lib/i686:$LD_LIBRARY_PATH" %command%

## Steam Controller not working in-game
If your Steam Controller is correctly recognized and paired but still not working in-game try the following:

* In Steam, non Big Screen, go to Settings > Account > Beta participation > Change... and in the dropdown select box select Steam Beta Update
* Restart Steam
* Go to Big Screen and start Tomb Raider

Correctly recognized means you can control the desktop mouse and Steam in Big Picture mode and the controller is shown in the Big Picture settings.

## Failed to Initialize Direct3D
This can happen when switching monitors.

You need to manually edit the preferences file (found in ~/.local/share/feral-interactive/Tomb Raider/) and change the ExclusiveFullscreen option to 0. After this you should be able to successfully start the game (after which you may exit and revert that option to a 1 to restore fullscreen).

## Stuck at the start menu
Tomb Raider for Linux will not start if there are any active VPNs that use TUN devices. This is because it makes incorrect assumptions about the return value of . The only reason it calls  is to get the MAC address for a Version 1 UUID, and fall back to a different algorithm if  returns no interfaces at all.

One optional solution for such a situation is listed down below, which fixes assumptions made by Tomb Raiders about the output of  (see tomb_raider_vpn_fix/releases for the original code):

{{bc|1=
#include
#include
#include

int getifaddrs(struct ifaddrs **ifap) {
   fprintf(stderr, "\n\n\n---------------- dummied out getifaddrs()!\n\n\n");
   *ifap = NULL;
   return 0;
}

void freeifaddrs(struct ifaddrs *ifap) {
   /* do nothing */
}
}}

Compile it using

 $ gcc -m32 -fPIC -shared file_name.c -o file_name.so -ldl -Wall

Then use the following launch option:

 env LD_PRELOAD=$LD_PRELOAD:path/to/file_name.so %command%

## Torchlight 2
## Libfreetype/libfontconfig Incompatibility
If you are experiencing issues with launching games such as Torchlight 2 or Civilization IV, it could be due to using a newer libfontconfig than the game currently supports.

Right click the game in Steam, and set the following as its launch option:

 LD_PRELOAD=/usr/lib/libfreetype.so.6 %command%

then attempt launching the game.

Alternately, re-naming or deleting these 2 files will force it to use your system's libraries:

 Torchlight 2/game/lib/libfreetype.so.6
 Torchlight 2/game/lib64/libfreetype.so.6

## Locale incompatibility
Some users report that Torchlight 2 does not work if you do not have en_US.UTF8 in your locale.

Double check you have generated the locale needed in Steam Installation Requirements.

## Tower Unite
## Graphical glitches
This is a known issue, and it occurs because the shaders had not been ported to Linux yet by the developers.
To minimize glitches and make the game playable add  to your launch options,
set Ocean Quality to "Potato" and Effects Quality to "Low" in the game settings.

## Towns / Towns Demo
Requires Java.

## Transistor
## Crash on launch / FMOD binding crash / audio issues
Run the game with:

 LD_PRELOAD='/usr/lib/libstdc++.so.6:/usr/lib/libgcc_s.so.1:/usr/lib/libxcb.so.1:/usr/lib/libasound.so.2'

Otherwise, run the game via shell and set up proper audio device for FMOD, as discussed in Also, check out this thread [https://steamcommunity.com/app/237930/discussions/2/492378265893557247/.

## Game does not start on Wayland
The game will not start with SDL set to use Wayland. You can have only the game run in X11 by adding the following launch options in Steam:

 SDL_VIDEODRIVER=x11 %command%

## Transmissions: Element 120
Dependencies:

*
*

## Troubleshooting
Make sure you have all libraries installed. Above the standard set required by Steam runtime, the game requires few additional ones. The typical error message that indicates that is

 AppFramework : Unable to load module vguimatsurface.so!

To find missing dependencies go into the game directory and run:

 LD_LIBRARY_PATH=bin ldd bin/vguimatsurface.so

Look for entries that say not found.

## Transport Fever 2
## Game will not launch
Rename or delete the following files in game directory () as discussed in *
*

## Trine 2
## Sound
If sound plays choppy, try:

## Resolution
If the game resolution is wrong when using a dual monitor setup and you cannot see the whole window edit  and change the options  and  to the resolution of your monitor on which you want to play the game.

## Tropico 5
## Blank screen with sound only on startup
Run the game with .

## Unbound: Worlds Apart
If your controller does not work, try selecting the game in your inventory, click the gear icon on the right,
then Properties, Controller, and select Disable Steam Input in the dropdown.

## Unity of Command
Requires .

## Squares
If squares are shown instead of text, try removing .

## No audio
If you get this error:

 ALSA lib dlmisc.c:254:(snd1_dlobj_cache_get) Cannot open shared library /usr/lib/i386-linux-gnu/alsa-lib/libasound_module_pcm_pulse.so

Try running:

 # mkdir -p /usr/lib/i386-linux-gnu/alsa-lib/
 # ln -s /usr/lib32/alsa-lib/libasound_module_pcm_pulse.so /usr/lib/i386-linux-gnu/alsa-lib/

## Unity3D
Games based on the Unity3D engine, like War For The Overworld or Pixel Piracy may need the package  to understand that they run on Linux and work properly.

## Locale settings
Games made in C# often have a problem with some locales (e.g. Russian, German) because developers do not specify locale-agnostic number formatting. This can result in some game screens loading only partially, problems with online features or other bugs.

To work around this, run the game with .

Affected games: FORCED, Gone Home, Ichi, Nimble Quest, Syder Arcade.

## Unity 5 sound problems
The sound system in Unity 5 changed and to be able to play games created with it you must most likely install and run PulseAudio.

Another solution is to disable the Steam runtime: in the launch options for the game, write this:

Another solution is to prevent Unity from trying to use PulseAudio using . Once it is installed, use the following as launch options :

Affected games: Kerbal Space Program, SUPERHOT, ClusterTruck

## Game launching on wrong monitor in fullscreen mode
Unity games that do not support monitor selection will most likely launch the game on a wrong monitor.

The problem is that Unity games write the default parameter  to the game config file.

This will lead to the game launching on a non-primary monitor.

When changing to value into  for the according game, the game will start on the correct (primary) monitor.

A Unity game config file usually resides in .

Affected games: Cities: Skylines, Tabletop Simulator, Assault Android Cactus, Wasteland 2, Tyranny, Beat Cop.

Be aware that some games do not support setting that parameter, it will simply be ignored. This is the case for Pillars of Eternity, Kentucky Route Zero, Sunless Sea.

## Chinese/Japanese/Korean display bug
Install  and . Then

 $ fc-cache -fv

## Game does not respond
Add the following line to your launch options :

 SDL_DYNAMIC_API=/usr/lib/libSDL2-2.0.so %command%

## No window opens on Wayland
See Unity3D#No window opens: Desktop is 0 x 0 @ 0 Hz.

## Unrest
Requires .

## Volgarr the Viking
Delete the  directory in the game directory to get rid of the libGL errors.

## War Thunder
## No audio
If there is no audio after launching the game, install .

## Blank screen
If having a green or blank screen on startup, run the game with . [https://forum.warthunder.com/index.php?/topic/267809-linux-potential-workaround-for-mesa-drivers-black-screen/ ==== Launcher fails to auto-close  ====

When running through Steam a startup option must be set or the War Thunder Launcher will not auto-close when the game exits. Doing so will prevent it from being reported as the running game on the Steam Community, and more importantly running up CPU and RAM usage in the background. Put  in the Launch Options/Parameters of War Thunder on Steam.

## Victor Vran
## Launch failure
The game might die on launch with the following (or similar) console print:

 Auto configuration failed
 4034673992:error:25066067:DSO support routines:DLFCN_LOAD:could not load the shared library:dso_dlfcn.c:185:filename(libssl_conf.so): libssl_conf.so: cannot open shared object file: No such file or directory

Add the following line to your launch options:

 OPENSSL_CONF=/dev/null %command%

## Warhammer 40,000: Dawn of War II
Dependencies:

*
*

The start script does not point to the right direction of .

To fix it open  and replace the following lines:

{{bc|HAS_LSB_RELEASE=$(command -v lsb_release)
if [ -n "${HAS_LSB_RELEASE}"  && [ "$(lsb_release -c | cut -f2)" = "trusty" ]; then
	LD_PRELOAD_ADDITIONS="/usr/lib/x86_64-linux-gnu/libasound.so.2:${LD_PRELOAD_ADDITIONS}"
fi }}

with:

{{bc|1=LD_PRELOAD_ADDITIONS="/usr/lib64/libasound.so.2:${LD_PRELOAD_ADDITIONS}"}}

## Wasteland 2
If Wasteland 2 immediately exits when you try to launch it there may not be enough system file descriptors available.  To increase the descriptor limit, edit  and add the line:

 * hard nofile 524288

Then reboot for the new limit to take effect, Wasteland 2 should now launch and this setting might also fix other games.

## We Were Here
## Stuck on black screen or logo on launch
Add  to launch options. === Worms W.M.D ===

The game includes a script with a minor workaround included in the  script, however this workaround alone does not usually work. The game seems to be trying to use libraries which depend on out-of date libraries. It also depends on . It is unlikely the game will run on modern systems or be updated again by the developer.

As of today (Jan/2026) the steps below will not work, left as a reference. A newer solution exists in [https://bbs.archlinux.org/viewtopic.php?id=307036 the BBS which is similar (simpler).

Add a script called myrun.sh to the game directory (~/.local/share/Steam/steamapps/common/WormsWMD on a standard steam install). Remember to make it executable (chmod +x)

Add the script to the game launch options in Steam

Run the game using the "Play Worms W.M.D" option.

The current working script is as follows

{{hc|head=myrun.sh|output=
#!/bin/bash

_libraries=(
	lib/libQt5*.so.5
	/usr/lib/libwavpack.so.1
	"$STEAM_RUNTIME"/amd64/lib/x86_64-linux-gnu/libdbus-1.so.3
    "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libcurl-gnutls.so.4
    "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libidn.so.11
    "$STEAM_RUNTIME"/lib/x86_64-linux-gnu/libgcrypt.so.11
    "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/librtmp.so.0
)

export LD_PRELOAD="${_librariesexec "$@" > ~/worms-stdout.log 2> ~/worms-stderr.log
}}

So, editing the script is needed. At the moment (2/2024) the following works on a system, however this may change at any time (edit  and  as required):

{{hc|head=Run.sh|output=
#!/bin/bash

export LOGFILE=${HOME}/wormswmd.log

export LC_ALL=C.UTF-8
export LD_LIBRARY_PATH="/usr/lib:/usr/local/lib"

export STEAM_ROOT=~/.steam
export PLATFORM=bin32
export STEAM_RUNTIME=$STEAM_ROOT/$PLATFORM/steam-runtime

export WORMSWMDINSTALLDIR=${HOME}/.steamapps/steamapps/common/WormsWMD

export LD_PRELOAD="$(
        printf "%s " "$WORMSWMDINSTALLDIR"/lib/libQt5*.so* \
                ${HOME}/.steam/steam/ubuntu12_32/steam-runtime/amd64/lib/x86_64-linux-gnu/libdbus-1.so.3 \
                ${HOME}/.steam/steam/ubuntu12_32/steam-runtime/amd64/lib/x86_64-linux-gnu/libdbus-1.so.3.5.8 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libcurl-gnutls.so.4 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libidn.so.11 \
                "$STEAM_RUNTIME"/lib/x86_64-linux-gnu/libgcrypt.so.11 \
                "$STEAM_RUNTIME"/lib/x86_64-linux-gnu/libwrap.so.0 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/librtmp.so.0 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libhogweed.so.4 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libnettle.so.6 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libsndfile.so.1 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libFLAC.so.8 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libpulse.so.0 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libjson.so.0 \
                "$STEAM_RUNTIME"/usr/lib/x86_64-linux-gnu/libpulsecommon-1.1.so \
        lib/libicuuc.so.56
)"

chmod a+x ./Worms\ W.M.Dx64
./Worms\ W.M.Dx64 >> $LOGFILE
}}

Now the game should run from Steam using the "Play Worms W.M.D (Run.sh)" option.

You may also try to run  directly but this is unlikely to work because of the reasons stated above, or run the script  from a terminal to see what libraries it is missing currently if the above script is not working for you.

If the game crashes after playing the intro movies, add the Steam Runtime dbus libraries to the game's library directory (but this is already covered by the  in the example ):

 $ ln -s ~/.steam/steam/ubuntu12_32/steam-runtime/amd64/lib/x86_64-linux-gnu/*dbus* ~/.steam/steam/steamapps/common/WormsWMD/lib

See also Steam community discussions [https://steamcommunity.com/app/327030/discussions/2/133257959065155871/, and [https://steamcommunity.com/app/327030/discussions/0/4033601726325456210/.

Steam overlay does not seem to work at the moment, possibly the game is still looking for some incompatible libraries.

On some systems there are terrain bugs where holes in terrain are not rendered properly and worms can fall through terrain unexpectedly. These bugs can make the game unplayable in many situations and there is no known fix for them.

## Witcher 2: Assassin of Kings
Dependencies:

*
*
*
*
*

## Game does not start
The game will not start with SDL set to use wayland. You can have only the game run in x11 by adding the following launch options in steam:

 SDL_VIDEODRIVER=x11 %command%

If the game does not run, enable error messages:

 $ LIBGL_DEBUG=verbose ./witcher2

## Wizardry 6: Bane of the Cosmic Forge
Requires DOSBox.

To fix the crash at start, open  and:

# comment the line
# change the beginning of the line starting with  to

## World of Goo
## Changing resolution
To change the game resolution edit the Graphics display section in . For example:

## X3: Terran Conflict
## Game crashes on startup
The game may crash on startup because it is linked to libz version 1.2.9, while the latest version of this library in Arch Linux is higher. The following message in the terminals appears in this case:
 ./X3TC_config: lib/libz.so.1: version 'ZLIB_1.2.9' not found (required by /usr/lib32/libpng16.so.16

Renaming or removing lib/libz.so.1 may help.

## X Rebirth
## Game crashes on startup
The game may crash on startup because it is linked to the shadergl function of the game. Do the follow in the  file.

 --- ./common.fh.orig
 +++ ./common.fh

 @@ -574 +574 @@
 -       /*      OUT_COLOR.rgb *= 0.0001; OUT_COLOR.rgb += half3(specstr);/**/   \
 +       /*      OUT_COLOR.rgb *= 0.0001; OUT_COLOR.rgb += half3(specstr);*/     \

 @@ -622 +622 @@
 -       /*      OUT_COLOR.rgb *= 0.0001; OUT_COLOR.rgb += LightColor.xyz/ 10;/**/       \
 +       /*      OUT_COLOR.rgb *= 0.0001; OUT_COLOR.rgb += LightColor.xyz/ 10;*/ \

After this workaround is implemented the game should load as normal.

## XCOM
Dependencies:

*
*  (required to enable keyboard functionality in-game)

## Hangs on startup
If you are running a hybrid graphics system, try:

 __GL_THREADED_OPTIMIZATIONS=0 primusrun %command%

## Graphical glitches on Intel HD
XCOM: Enemy Unknown may not recognize the SDL2 shared libraries shipped with the Steam runtime.
Check if the binary finds all required files and install missing packages if necessary ( and ).

## XCOM 2
## Unable to start with steam native
Needs  which is not available in arch repositories, loading it from steams runtime seems to work.

 LD_PRELOAD="$HOME/.local/share/Steam/ubuntu12_32/steam-runtime/usr/lib/x86_64-linux-gnu/libgconf-2.so.4" %command%

## Unable to start needs command line launch option
If having  in the game directory but the game still does not work put the following in the launch options.

 LD_LIBRARY_PATH=./lib/x86_64/:../lib/x86_64/ %command% -allowconsole

If the above command on Steam does not work for you then its possible that this may work as an alternative.

 LD_LIBRARY_PATH=/usr/lib:$HOME/.local/share/Steam/ubuntu12_32/steam-runtime/amd64/lib/x86_64-linux-gnu/:$HOME/.steam/steam/steamapps/common/XCOM\ 2/lib/x86_64/ %command%

## Anti-cheat
Anti-cheat software is a common component of modern games. There are many anti-cheat implementations, most of which target Windows. Some may work without any further configuration. Consult are we anti cheat yet for a comprehensive and crowd-sourced list of games using anti-cheats and their compatibility with GNU/Linux or Wine/Proton.

## BattlEye
BattlEye is a cross platform anti-cheat software used by Grand Theft Auto: Online. Native runtime binaries can be installed directly from the Steam store.
