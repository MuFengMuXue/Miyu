# RetroArch

RetroArch is the reference implementation of the libretro API. It is a modular front-end for video game system emulators, game engines, video games, media players and other applications that offers several uncommon technical features such as multi-pass shader support, real-time rewinding and video recording (using FFmpeg), it also features a gamepad-driven UI on top of a full-featured command-line interface.

## Installation
Install the  package.

## Usage
RetroArch relies on separate libraries, called "cores", for most of its functionality. These can be downloaded per-user within RetroArch itself (via the libretro Buildbot) or you can install them system-wide with  or AUR.

By default RetroArch is configured to load the per-user cores that it downloads. Change your #Configuration if you install them elsewhere.

The command to run a particular core is

 $ retroarch --libretro /path/to/some_core_libretro.so /path/to/rom

## Configuration
When you first run RetroArch it will create the user configuration file .

If you install RetroArch components in your home-directory, you should specify local paths in the global configuration file for downloading cores. For example,

If you install any RetroArch components system-wide with pacman, you should specify these in the global configuration file and include them in your user file. For example,

If you want to override your configuration (for example when running certain cores) you can use the  command line option.

## Tips and tricks
## Enabling the "Online Updater"
If you prefer to install all RetroArch components with the built in updater instead of pacman, you can enable it with a configuration file:

## Enabling "SaveRAM Autosave Interval"
By default, RetroArch only writes SRAM onto disk when it exits without error, which means that there is a risk of losing save data when using crash-prone cores. To change this behavior, open  and set  to n.

With the example above, RetroArch will write SRAM changes onto disk every 600 seconds.

## Filters and shaders
RetroArch can load CG shaders, which are considered old and deprecated, as well as GLSL and Slang shaders.The shaders can be obtained and updated directly inside RetroArch using the Online Updater.

## Reset settings to their default value
To reset a setting or keybind to its default value through the GUI, highlight it and press . To remove a button from a keybind, highlight the keybind and press .

## Troubleshooting
## No cores found
By default RetroArch searches for cores in , which is where the Online Updater installs them. Cores installed with pacman are placed in  and thus will not appear in RetroArch's GUI. You should choose one method of installing cores (pacman or the Online Updater) and change your configuration to match.

If you still face a "No Cores Available" message, you likely need to install the core info files. To solve this:
# Navigate to Settings > Directory, and ensure all configured paths are writable without requiring superuser permissions.
# Go to Settings > User Interface > Menu Item Visibility, and make sure that Show 'Core Downloader is enabled.
# Finally, access Main Menu > Online Updater and proceed to update the core info files. It is also recommended to update all other available components.
Upon restarting RetroArch, you should be able to run ROMs using any of the installed cores.

## Input devices do not operate
You may encounter problems if running on a CLI or a display server other than Xorg or if you use the udev input driver, because  nodes are limited to root-only access. Try adding your user to the  user group then logging in again.

Alternatively, manually add a rule in , with  as its contents. Reload udev rules by running:

 # udevadm control --reload-rules

If rebooting the system or replugging the devices are not options, permissions may be forced using:

 # chmod 666 /dev/input/event*

## Poor video performance
If poor video performance is met, RetroArch may be run on a separate thread by setting  in .

This is, however, a solution that should be not be used if tweaking RetroArch's video resolution/refresh rate fixes the problem, as it makes perfect V-Sync impossible, and slightly increases latency.

## Audio issues with ALSA
When using ALSA the  must match the system's default output rate, usually .

## Save data is lost whenever RetroArch crashes
See #Enabling "SaveRAM Autosave Interval".

## Start game from playlist but reports 'No Items'
If RetroArch reports , try to load game by manually choosing the path of the ROM from Main Menu > Load Content. It seems unreliable to start game from playlist.

It is necessary to force launch RetroArch in Xwayland.

 $ WAYLAND_DISPLAY="" retroarch

You can check the log with  option, there should be  instead

## BIOS files are missing or not accepted
Retroarchs cores are looking for BIOS files at the location set with the  option in .

The GUI menu Settings > Directory > System/BIOS shows the directory as well.

Some of the cores require the files directly in this directory. Other cores need a subdirectory within this directory with a specific name for their specific BIOS files. Some cores even look for their files in the same directory as the ROM file they try to run.

Every installed core provides information on needed files, their MD5 sums and the directory they need to
be placed in. You can find this information in the GUI menu under Settings > Core > Manage Core. Choose a core here to get information on the needed BIOS files for this specific core. RetroArch describes them as "firmware" files on the core info pages.

Further in depth info on BIOS files for many of the supported cores can be found in the official documentation. [https://docs.libretro.com/library/bios/
