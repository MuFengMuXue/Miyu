[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines"). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

## Contents

-   [[1] [About]](#About)
-   [[2] [Package Requirements]](#Package_Requirements)
    -   [[2.1] [Install Steam]](#Install_Steam)
    -   [[2.2] [Install ARMA 3]](#Install_ARMA_3)
    -   [[2.3] [GPU Driver Requirements]](#GPU_Driver_Requirements)
-   [[3] [Common Startup Parameters]](#Common_Startup_Parameters)
-   [[4] [Folder Locations]](#Folder_Locations)
    -   [[4.1] [Synchronizing Steam Workshop Content with other O/S Platforms]](#Synchronizing_Steam_Workshop_Content_with_other_O.2FS_Platforms)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [ARMA 3 does not Start on x86 64 bit Platforms]](#ARMA_3_does_not_Start_on_x86_64_bit_Platforms)
    -   [[5.2] [ARMA 3 still does not start or shows on the wrong display.]](#ARMA_3_still_does_not_start_or_shows_on_the_wrong_display.)
    -   [[5.3] [Continuing Non-specific Startup Problems]](#Continuing_Non-specific_Startup_Problems)
    -   [[5.4] [Joystick not found]](#Joystick_not_found)
    -   [[5.5] [Joystick not configurable or has incorrect scheme]](#Joystick_not_configurable_or_has_incorrect_scheme)
    -   [[5.6] [No Multi Player Servers Available]](#No_Multi_Player_Servers_Available)
    -   [[5.7] [No Microphone and/or sound through ALSA]](#No_Microphone_and.2For_sound_through_ALSA)
    -   [[5.8] [Taskbar still visible using Fullscreen Mode]](#Taskbar_still_visible_using_Fullscreen_Mode)
-   [[6] [References: Basic]](#References:_Basic)
-   [[7] [References: Scripting]](#References:_Scripting)

## [About]

From the ARMA 3 website: \"*Experience true combat gameplay in a massive military sandbox. Deploying a wide variety of single- and multiplayer content, over 20 vehicles and 40 weapons, and limitless opportunities for content creation, this is the PC's premier military game. Authentic, diverse, open - Arma 3 sends you to war.*\"

The Linux port looks to be a native port (not using Wine), with the binary executable named \"arma.i386\".

The following features have not been ported.

-   BattlEye - Good luck finding any multi-player servers not mandating BattlEye! (2016.04.27 - Recently Bohemia Interactive has stated plans for porting BattlEye to other platforms is actively being worked and supposedly planned for release within the near future?)
-   Controller Input Detection - There is apparently no auto detection for for your joystick or TrackIR device! Nor does it look like any devices are even operable aside from keyboard input. FIXME: See below BI Studio Community Ports within References. Configure joysticks within Steam\'s Big Picture menu. (2016.04.27 - Supposedly there were some improvements recently, and maybe - and I hope - more to come.)
-   No Advanced Flight Model - For those of us whom enjoy breaking tail rotors or main rotors, this is going to make flying boring. Not too mention, requiring a magnifying glass to read the instrument panel! (2016.04.27 - In my experience, although I love the advanced flight model, the advanced flight model does not work well with any other helicopters except the Ghosthawk and Mohawk. The model for some reason adds too much Internet lag for being useful for other helicopters, making them practically not flyable within an Internet Multiplayer setting, due to local or server game resource throughput.)
-   No Launcher - I and most others probably enjoy using command line instead, making debugging easier. This is probably the only item a Linux user can easily do without. (2016.04.27 Still not missing this execution method much at all, except some start-up bugs might be alleviated. New users may also find at first, this start-up method maybe easier.)

As of 2016.12.07, ARMA 3 does work using the Nouveau driver with my NVidia GTX 670. Albeit, a bit slow. The game loads maps (and likely other components) significantly faster within Linux versus Windows.

## [Package Requirements]

### [Install Steam]

Install steam using \"emerge games-util/steam-meta\", or following the appropriate Gentoo Wiki for installing the Steam client.

### [Install ARMA 3]

Once you have Steam installed and have either created or logged into your existing account, search for the ARMA 3 game clicking \"Games\" \> \"View Games Library\" \> \"SteamOS + Linux\" or if you haven\'t purchased the game, then purchase the game clicking \"STORE\" just below the top menu bar. The initial download requires 9-12 hours using DSL.

### [GPU Driver Requirements]

ARMA 3 requires OpenGL 4.1, and doesn\'t appear to be GPU bound due to the various driver implementations.

-   NVIDIA: =x11-drivers/nvidia-drivers-352.30 works
-   AMD: ?

## [Common Startup Parameters]

-   \"-noLogs -nosplash -world=empty -skipIntro\"
-   \"-window\"
-   \"-winxp\"

## [Folder Locations]

The top root folder for all ARMA 3 folders appears to be \"/home/USER/.local/share/bohemiainteractive/arma3/\" which appears to contain the AppDataLocal/ AppDataShared/ GameDocuments/. With the exception of GameDocuments being equivalent to the \"C:\\Users\\user\\Documents\\Arma 3\\\". (Replace USER with your user name!) This is really nice, as we now have a central location for almost all files, with the exception of the main program files still being located under the Steam root folder.

The following lists the equivalent folder locations for Windows folder locations in comparison to Linux folder locations. Aliasing the folder locations with the cd command within the Bash configuration file is probably a good idea! (ie. cd-arma3, cd-arma3-usercfg, \...)

    User Configurations and User Editor Created Missions
    MS Windows: C:\Users\user\Documents\Arma 3\
    Linux: /home/USER/.local/share/bohemiainteractive/arma3/GameDocuments/Arma\ 3\ -\ Other\ Profiles/USER/

    Error RPT logs and Crash Dumps
    MS Windows: C:\Users\USER\AppData\Local\Arma 3
    Linux: /home/USER/.local/share/bohemiainteractive/arma3/AppDataLocal/Arma\ 3/

    ARMA 3 Root Program Folder
    MS Windows: C:\Program Files (x86)/Steam/SteamApps/common/Arma 3/
    Linux: /home/USER/.local/share/Steam/SteamApps/common/Arma\ 3/

### [][Synchronizing Steam Workshop Content with other O/S Platforms]

Workshop content is stored within the following folders.

    MS Windows: /mnt/windows7/Program\ Files\ \(x86\)/Steam/SteamApps/workshop/
    Linux: /home/USER/.local/share/Steam/SteamApps/workshop/

Workshop content appears to be first downloaded to a temporary sub-folder and then moved to a numbered folder within the same folder. Workshop content (or mods) are then also apparently copied into the main game folder. Workshop content or Mods atypically are prefixed with an \"@\" sign. (ie. \@ADR-97)

Here\'s a basic command line implementation for synchronizing workshop content.

    rsync -axv --delete /mnt/windows7/Program\ Files\ \(x86\)/Steam/SteamApps/workshop/ /home/roger/.local/share/Steam/SteamApps/workshop/

Here\'s an advanced example Bash bashrc alias script to automatically synchronize your already downloaded Windows workshop content. Customization is required for your installed Workshop content.

[FILE] **`/home/USER/.bashrc`**

    alias rsync-arma3-workshop="rsync -ax --delete /mnt/windows7/Program\ Files\ \(x86\)/Steam/SteamApps/workshop/ /home/roger/.local/share/Steam/SteamApps/workshop/ && rsync -ax --delete /mnt/windows7/Program\ Files\ \(x86\)/Steam/SteamApps/common/Arma\ 3/@ADR-97\ Weapon\ Pack\ \(Official\ Mod\)/ /home/roger/.local/share/Steam/SteamApps/common/Arma\ 3/@ADR-97/ && rsync -ax --delete /mnt/windows7/Program\ Files\ \(x86\)/Steam/SteamApps/common/Arma\ 3/@Nam/ /home/roger/.local/share/Steam/SteamApps/common/Arma\ 3/@Nam/ && rsync -ax --delete /mnt/windows7/Program\ Files\ \(x86\)/Steam/SteamApps/common/Arma\ 3/@Air\ Cav\ Vietnam/ /home/roger/.local/share/Steam/SteamApps/common/Arma\ 3/@Air\ Cav\ Vietnam/"

## [Troubleshooting]

### [ARMA 3 does not Start on x86 64 bit Platforms]

-   ARMA 3 is a 32 bit application and requires some application dependencies to provide 32 bit libraries and executables. Recently, I just added USE=\"\$ abi_x86_32\" to my make.conf global variables and executed \"emerge -uDNpv world\". Just too many package dependencies for some 32 bit applications to maintain within the package.use file! Although this removes maintaining 100-200 package names within the package.use file, this global solution will add 200-400+ packages to your Gentoo Portage database or \~1 Gigabyte to /usr/lib32 folder depending on how many 32 bit applications you plan to execute on your 64 bit platform. My guess is, you may want to consider the global option when having more than two 32 bit applications.

<!-- -->

    echo "media-libs/libsdl2 abi_x86_32" >> /etc/portage/package.use"
    emerge -a media-libs/libsdl2 abi_x86_32

Or use the following, compiling 32 bit binaries for all system packages, and my currently implemented solution on my computer:

    echo 'USE="$ abi_x86_32"' >> /etc/make.conf
    emerge -uDNav world

-   Another likely more [appropriate solution](https://steamcommunity.com/app/107410/discussions/1/490121928363165584/) is using internal Steam pre-compiled Linux libraries and create another wrapper start script (ie. arma3.sh) within the existing ARMA 3 starting script and binary, using the following statement. (However, this solution may not include some dependencies, such as providing a 32 bit alsa-plugins if your have further customizations within your asoundrc file.)

<!-- -->

    LD_PRELOAD=$HOME/.local/share/Steam/ubuntu12_32/steam-runtime/i386/usr/lib/i386-linux-gnu/libSDL2-2.0.so.0 ./arma3

Change execute permissions (chmod 755 arma3.sh) and execute the game using this file (./arma3.sh). Do not forget to first, login in to steam. Users would use this solution, if for some reason, they cannot utilize the existing starting wrapper script.

### [ARMA 3 still does not start or shows on the wrong display.]

When using multiple monitors or displays, use \"\--eon_force_display=0\". (FIXME: You\'ll likely see the monitor being reported within one of the log files. Either the steam log or \*.RPT file.)

### [Continuing Non-specific Startup Problems]

Try running the game manually instead of using the Steam client. This manual execution method is also the apparent method for debugging Steam wine applications/games and being able to specify the extra Wine execution parameters.

Start and login with the Steam client within one window, without executing the game or application.

Change to the root application/game folder, replacing USER with your login name. \$ cd /home/USER/.local/share/Steam/SteamApps/common/Arma\\ 3

Manually execute arma3 binary \$ ./arma3 \--eon_force_display=0 -world=empty -skipIntro -window

** Note**\
Manually executing this game\'s binary by-passes the existing wrapper start script\'s LD_PRELOAD library assessment. See the previous mention of writing you\'re own wrapper start script to include Steam\'s pre-compiled Linux libraries using the LD_PRELOAD variable.

### [Joystick not found]

First, the Linux ARMA 3 port does not use the MS Windows DirectX method, and requires using SDL2. The ARMA 3 port chose to use Steam Big Picture mode for configuring controllers. First switch to Big Picture mode and verify your controller exists within the Setup \> Controllers menu.

If your joystick controller does not show within the Setup \> Controllers menu, then find your /dev/input/event device file relative to your joystick and make your /dev/input/event\* world readable and possibly writable. (ie. chmod a+rw /dev/input/event15) Restart Steam and navigate back to the controller setup menu and your device should now be found. Also try using the following incantation when starting Steam, \"env SDL_JOYSTICK_DEVICE=/dev/input/event15 steam\" if you\'re still having problems.

### [Joystick not configurable or has incorrect scheme]

Since the ARMA 3 Linux port uses the Steam Big Picture mode for controller configurations, as far as I know, this scheme *seems to be only engineered for Game Pads* and not really meant for joysticks!

I\'ll try to iterate what I\'ve done so far to try to make my joystick usable.

Game controller settings are saved to \"/home/\$USER/.local/share/Steam/config/config.vdf\". (You might find others whom have already configured and published their config.vdf controller settings.) You will only get a save dialogue once you\'ve configured most or the required keys. Once you\'ve saved any button mappings, you can likely use games-util/antimicro (and requires Qt5) for customizing or correcting the joystick axis and button mappings within the config.vdf. Another method instead of using AntiMicro for configuring your joystick, starting emerging (or compiling) libsdl2 and break out of the compile. Change to the root build folder containing the test utility folder. (ie. cd /var/tmp/portage/media-libs/libsdl2-2.0.3-r200/work/SDL2-2.0.3/test) Type \"./configure\" and then \"make\", should build all the utilities, but you\'ll just need the ./controllermap utility and can output the SDL2 game controller mapping for use with Steam\'s SDL_GamepadBind variable. SDL2 game controller mapping definitions can be found here [http://wiki.libsdl.org/SDL_GameControllerAddMapping](http://wiki.libsdl.org/SDL_GameControllerAddMapping) or within SDL_gamecontroller.h, further used within SDL_gamecontroller.c. Another tip, once you have the joystick showing within the ARMA 3 Configure \> Controllers menu, the joystick may show only within the \"Controllers with a Scheme\" menu. Disabling this controller within this menu will then show the controller within the \"Customizable Controllers\" menu. After doing this, the controller will then be detected within the ARMA 3 mapping menus, but only the axis and buttons previously mentioned within the SDL2 SDL_GamepadBind will be detected. (This is as far as I\'ve gotten, and only able to use only one or two buttons and axis. Joystick up axis, left axis, main trigger secondary button, throttle forward axis.) The following text line should be the last line within the config.vdf file.

[FILE] **`/home/USER/.local/share/Steam/config/config.vdf`**

    "SDL_GamepadBind"       "03000000a30600006207000011010000,Saitek Saitek X52 Pro Flight Control System,platform:Linux,a:a1,b:a0,x:b0,y:b0,back:b0,start:a2,platform:Linux,"

The following file is a little better, with most of the axis working except right/left bank inoperable and reversed. Trigger button can\'t be mapped.

[FILE] **`/home/USER/.local/share/Steam/config/config.vdf`**

    "SDL_GamepadBind"       "03000000a30600006207000011010000,Saitek Saitek X52 Pro Flight Control System,platform:Linux,rightx:a0,righty:a1,righttrigger:b15,leftx:a2,lefty:a5,"

The following provides some further game controller variables (ie. back, start, rightx, righty, leftx, lefty, \..., and seem to be further documented within SDL_gamecontroller.c) [http://www-personal.umich.edu/\~bazald/l/api/\_s_d_l\_\_gamecontroller_8c.html](http://www-personal.umich.edu/~bazald/l/api/_s_d_l__gamecontroller_8c.html)

Also note the config.vdf should be able to handle C style comments (ie. \"//\" and even \'/\'), but upon Steam each execution, commented lines appear to be unfortunately removed. Hence, you\'ll need to manually backup the file instead. As such, this is unhappy hacking for me.

### [No Multi Player Servers Available]

The ARMA 3 Linux port is currently stuck at version 1.42. You or somebody else will need to host an ARMA 3 server using the previous 1.42 version. Per the below references, the ARMA 3 Linux/MAC port may unfortunately never see a newer version.

I speculate having no future version releases for the Linux or MAC ports is due to not having the following features; no BattlEye (anti cheat support), completed joystick support, and advanced helicopter controls. Without these features, many users maybe discouraged from using the Linux or MAC ports.

2016.04.28 Still getting kicked-off Multi-player Linux servers with the error, \"You were kicked off the game. (BattlEye: Client not responding.)\" I hope the developers realize; without BattlEye and the Linux client version not being up-to-date, there still will not be a huge following. About the only usefulness the game is under Linux, Single player scenarios and using the Editor. In my past experience with Battlefield 1942 and Enemy Territory, there is a demand for these Multi-player games on Linux. They\'re almost there though, but not quite.

### [][No Microphone and/or sound through ALSA]

Pulse emulation is provided using the package media-sound/apulse.

    LD_LIBRARY_PATH=/usr/lib32/apulse steam

(Microphone now works within the Steam interface, however not tested within the game.)

Another LD_PRELOAD option to try:

    LD_PRELOAD='/usr/lib32/libasound.so.2:/usr/lib64/libasound.so.2' steam

### [Taskbar still visible using Fullscreen Mode]

Even after using \"-posX=0 -posY=0\", taskbar remains visible during fullscreen mode. Try toggling the Configuration \> Video \> Display size from the largest resolution to smallest, and then back again. This works for me as a workaround, but the workaround incurs some minor additional glitches. (I\'m using the DWM window manager.)

## [References: Basic]

-   Bohemia Interactive ARMA 3 official web page: [http://arma3.com/](https://arma3.com/)
-   Bohemia Interactive Experimental Ports: [http://dev.arma3.com/ports](https://dev.arma3.com/ports)
-   Arma 3 Feedback Tracker: [http://feedback.arma3.com/](https://feedback.arma3.com/)
-   Bohemia Interactive ARMA 3 developer hub: [http://dev.arma3.com/](https://dev.arma3.com/)
-   BI Studio Community Ports: [https://community.bistudio.com/wiki/Arma_3_Experimental_Ports](https://community.bistudio.com/wiki/Arma_3_Experimental_Ports)
-   BI Studio Community Developer Change Log: [http://forums.bistudio.com/topic/140837-development-branch-changelog/](http://forums.bistudio.com/topic/140837-development-branch-changelog/)

## [References: Scripting]

-   ArmA: Scripting - Getting Started: [http://community.bistudio.com/wiki/ArmA:\_Scripting\_-\_Getting_Started](http://community.bistudio.com/wiki/ArmA:_Scripting_-_Getting_Started)
-   Category:Scripting Topics: [http://community.bistudio.com/wiki/Category:Scripting_Topics](http://community.bistudio.com/wiki/Category:Scripting_Topics)
-   Category:Scripting Commands: [http://community.bistudio.com/wiki/Category:Scripting_Commands](http://community.bistudio.com/wiki/Category:Scripting_Commands)
-   Category:Arma 3: New Scripting Commands List: [http://community.bistudio.com/wiki/Category:Arma_3:\_New_Scripting_Commands_List](http://community.bistudio.com/wiki/Category:Arma_3:_New_Scripting_Commands_List)