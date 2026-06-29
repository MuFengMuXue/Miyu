# Steam

Steam is a popular game distribution platform by Valve.

## Installation
Enable the multilib repository and install the  package (recommended).

Alternatively, install the  package for running Steam with native system libraries; see /Troubleshooting#Steam runtime.

In order to run Steam:

* You must install the 32-bit version of the OpenGL graphics driver appropriate for your system.
* If not already done during installation, you must generate the en_US.UTF-8 locale to prevent invalid pointer errors.
* If you need to add library folders or add non-Steam games to your Steam library, install XDG Desktop Portal with a backend providing a file chooser.
* If using systemd-resolved for DNS, follow the steps to fix  in order for Steam to be able to resolve hostnames.
* If using the Big Picture Mode (Steam Deck UI), NetworkManager may be required for the network-related panels to work correctly.
*  must be increased in order to run some games without crashing; see Gaming#Increase vm.max_map_count.

## SteamCMD
Install  for the command-line version of Steam.

## Directory structure
The default Steam install location is . If Steam cannot find it, it will prompt you to reinstall it or select the new location. This article uses the  symlink to refer to the install location.

## Library folders
Every Steam application has a unique AppID, which you can find by either looking at its Steam Store page path or visiting SteamDB.

Steam installs games into a directory under .  normally is
 but you can also have multiple library folders (Steam > Settings > Storage > (+) Add Drive).

In order for Steam to recognize a game it needs to have an
 file in . The appmanifest file uses the
KeyValues format and its  property
determines the game directory name.

## Usage
 steam [ -options ] [ steam:// URL ]

For the available command-line options see the Command Line Options article on the Valve Developer Wiki.

Steam also accepts an optional Steam URL, see the Steam browser procotol.

## Launch options
When you launch a Steam game, Steam executes its launch command with .
To let you alter the launch command Steam provides launch options,
which can be set for a game by right-clicking on it in your library, selecting Properties and clicking on Set Launch Options.

By default Steam simply appends your option string to the launch command. To set environment variables or
pass the launch command as an argument to another command you can use the  substitute.

## Examples
* only arguments:
* environment variables:
* completely different command:

## Tips and tricks
## Start minimized
It is possible to have Steam start minimized to the system tray, rather than taking focus. Add  to the list of command line arguments; see Desktop entries#Modify desktop files for doing this by default.

## Small mode
Steam supports an alternative, minimal UI with just your game list - the store, community and cover collection views are hidden. You can switch to it with View > Small Mode. To go back to the standard UI, select View > Large Mode.

You can also launch Steam with this argument:

## Proton Steam Play
Valve developed a compatibility tool for Steam Play based on Wine and additional components named Proton. It allows you to launch many Windows games (see compatibility list).

It is open-source and available on GitHub. Steam will install its own versions of Proton when Steam Play is enabled.

"Proton Experimental" is enabled by default on the Steam client: Steam > Settings > Compatibility. You can enable Steam Play for games that have and have not been whitelisted by Valve in that dialog.

Proton supports Easy AntiCheat integration if the developer activates it, however EAC may require a particular patched version of glibc: if a game is been reported to be working but is not in your machine, try using Steam Flatpak because it comes with glibc patched. Additionally, setting the procfs mount option "hidepid" to a hardened value may cause Easy Anti-Cheat to fail with the message "Launch Error: 261".

## Force Proton usage
If needed, to force enable Proton or a specific version of Proton for a game, right click on the game, click Properties > Compatibility > Force the use of a specific Steam Play compatibility tool, and select the desired version. Doing so can also be used to force games that have a Linux port to use the Windows version.

## Use Proton outside of Steam
To use Proton outside of Steam, the best way to do so is through .

Take a look at the upstream repository for more information, including its documentation.

## Compatibility layers other than Proton
There are compatibility tools other than Proton/Wine.

*
*

You can also use  to manage them:

# Close Steam
# Install
# Open protonup-qt and install desired tools
# Start Steam
# In the game properties window, select Force the use of a specific Steam Play compatibility tool and select the desired tool.

## Steam Input
When a controller is plugged in while Steam is running, Steam's default behavior is to leave it alone and let games use it as-is. The gamepad's evdev and joystick devices are exposed by the kernel, and games may use them using APIs such as SDL2 as if Steam were not in the picture.

The Steam Input subsystem offers an abstraction layer which allows for more advanced functionality such as rebinding buttons and axes, having game-specific profiles, and doing higher-level button mappings based on in-game actions. The Steam Input Configurator (SIC) is the part of the system that implements this functionality. To enable Steam Input for a controller, go to Steam > Settings > Controller > External Gamepad Settings. Here you will find toggles to Enable Steam Input corresponding to your controller.

## Steam Input Configurator
See Steam Input Configurator for configurator usage instructions.

When SIC is enabled for a controller, there are a few different controller devices:

* The virtual Steam Controller, used by games that utilize the Steam Input API. All rebindings and Steam-specific features are functional.
** This is not to be confused with the Valve Steam Controller, the physical controller.
* An evdev device representing an emulated Xbox 360 controller, used by games that do not support Steam Input. Basic rebindings are in effect. * The original controller evdev device, whose inputs are passed through the SIC. Rebindings are not in effect, but games should be defaulting to the 360 controller instead.
* The joystick analogues of the above two devices.

The SIC's behavior is context dependent:

* When launching a game that supports the Steam Input API, it is using the SIC in native mode. The game receives "actions" rather than raw inputs to handle.
** This works for games running in Proton that would be using Steam Input on Windows.
** Even though it's theoretically not needed, the emulated 360 controller is still present.
** A game may choose to provide both support for the Steam Input, and traditional input API libraries that defer to evdev and joystick under the hood. When the game is launched with Steam and with SIC enabled for the controller, Steam Input takes higher priority.
** A game can also choose to only support Steam Input. For example, in Among Us, a gamepad will not work unless you have the SIC running.
* When launching a game that does not support Steam Input, it is (unknowingly) using the SIC in legacy mode. The game receives its expected low-level raw inputs from what seems to be a 360 controller, but they are actually spoofed by the SIC to emulate the desired behavior of native mode.
** This is the case for native games that use evdev or joystick, as well as Windows games running through Proton that use DirectInput or XInput.
* When launching a game that supports neither Steam Input nor other gamepad APIs, SIC can activate a profile that emulates gamepad support as described below.
* When Big Picture has focus, the current Big Picture profile is in effect. This is not configurable.
* When anything else has focus, the current Desktop profile is in effect, configurable via Steam > Settings > Controller > Desktop Layout.
* When anything has focus, additional global bindings can be configured via Steam > Settings > Controller > Guide Button Chord Layout. This is not available on a Steam Deck.

Games are rated on how comprehensive their gamepad support is. This is dependent on the controller model.

* Supports Your Controller, indicating that the game has full controller support. This can be achieved even if the game does not use the Steam Input API; the focus is on accessibility regardless of API.
* Mostly Playable With Your Controller, indicating that the game has partial gamepad support. Even if the game is using the Steam Input API, there are instances like Team Fortress 2 where certain parts are still inaccessible to warrant this rating.
* Controllers Not Supported, indicating the game does not have native gamepad support.
* Unknown Controller Support, indicating that Valve has not yet verified the controller support of a game.

In cases where the game does not have full gamepad support, SIC tries to fill the gaps. For example, in Bloons Tower Defense 5, a game that requires you to point and click, Steam will automatically activate the Keyboard (WASD) and Mouse profile, allowing you to use your gamepad to move and click.

## Recommended Steam Input usage
To summarize what this all means for usage:

* Enabling "Configuration Support" is recommended for enhanced gamepad support such as rebinding to one's liking, or automated fixes like Nintendo-style button remapping or keyboard/mouse.
* For some games, enabling this is outright required if they do not support traditional gamepad APIs.
* By default, if you have enabled this, then the controller will not work with non-Steam games because the 360 controller takes precedence over the original controller device, but the default Desktop profile has the buttons disabled. To fix this, you can either:
** Have the configuration change action sets. Some official desktop configurations will switch to a gamepad mode when the start button is held. If the configuration for your controller does not have this, you can add it by adding a new action set to the configuration, setting the set to contain gamepad buttons, adding an Extra Command to the start button, setting the extra command to Change Action Set, and then setting that extra command to activate on long press.
** Set your Desktop profile to the template for Gamepad. This will pass through the inputs to the 360 controller, making the default device usable for other programs.
** Have the other game use the original device if it supports this. Note that the game will not benefit from any Steam Input rebindings.
** Disable the whole feature for the controller so Steam does not create the 360 controller at all. Note that Steam games would then not benefit from the enhanced gamepad support.
** Close Steam when using the other games.

## Disabling Steam Input
If you wish to completely disable Steam Input, launch Steam with the -nojoy argument, and also disable Steam Input for each game individually, as there is no global option for doing so.

## HiDPI
See HiDPI#Steam.

## Big Picture Mode from a display manager
To start Steam in Big Picture Mode from a display manager with Gamescope as its compositor:

* Install .
* Create the following desktop entry with the following contents:

Then instruct your display manager to launch gamescope.

## Steam Remote Play
Steam has built-in support for [https://store.steampowered.com/streaming/ remote play.

See this Steam Community guide on how to setup a headless streaming server on Linux.

## Sharing games with Windows when using Proton
If you use Proton (Steam Play) for launching your games, and still keep a Windows installation for some reason (for example, if some game has problems with anti cheat or if you want to make a comparison tests with Windows), you may want to store your games in a common partition instead of keeping two copies of game one per OS.

To add another folder for library, click on Steam > Settings > Downloads > STEAM LIBRARY FOLDERS, then on the ⊕ (Plus) button.

There are four file systems, that can be read/write by both Windows and Linux.

## NTFS
See Using a NTFS disk with Linux and Windows for more information on how to configure that. To launch games from an NTFS drive, follow the steps from Steam/Troubleshooting#Steam Library in NTFS partition.

Using ntfs has disadvantages. It happens often that shaders cache folder becomes corrupted. Messages saying  You cannot fix that from linux. You need to boot to Windows and use chkdsk for that.

## exFAT
This filesystem has disadvantage that it is case-insensitive. You will get such message:  See issue #7665

Also it is problematic to create symlinks on exfat, so you cannot use the method of symlinking compatdata as in ntfs method.

## Btrfs
Btrfs has a fairly mature Windows Driver.

NTFS can be also converted into Btrfs, see Btrfs#NTFS to Btrfs conversion.

This filesystem eliminates most NTFS/exFAT compatibility issues, but sharing a Steam library between Windows and Linux has limitations:

Valve officially discourages sharing Steam libraries between OSes. Even with correct WinBtrfs UID/GID mappings, Windows processes create lock-files and staging folders owned by , causing "Disk write failure" or "content file locked" errors in Linux.

After Windows usage you must run:

{{bc|
# chown -R $USER:$USER /path/to/steam_library/steamapps
$ find /path/to/steam_library/steamapps -name "*.lock" -delete
$ rm -rf /path/to/steam_library/steamapps/{downloading,temp}/*
}}

Only then start Steam on Linux. For reliable operation, keep separate libraries per OS.

## UDF
This filesystem can be used without issue, but to ensure compatibility, it must be formatted to the correct UDF revision. Linux lacks write support for revisions 2.50 and higher. Therefore, revision 2.01 is required for proper functionality.

The UDF block size must match the logical sector size of the partition. This value can be obtained using :

 # blockdev --getss /dev/the_partition_to_be_formatted

The partition is then formatted to UDF using  provided by . For both HDDs and SSDs, the appropriate media type is .

 # mkfs.udf --utf8 --label=label --blocksize=block-size --media-type=hd --udfrev=0x0201 /dev/the_partition_to_be_formatted

Where:

*  is the name of the target partition (e.g. ,  etc.).
*  is the desired volume label.
*  is the output of the  command.

Alternatively, graphical tools like  can be used to handle formatting. They correctly manage UDF revision selection to ensure compatibility.

## Faster shader pre-compilation
In certain circumstances shader pre-compilation may only use one core, however this can be overridden by the user, example to use 8 cores:

## Disable HTTP2 for faster downloads
Some systems and configurations seem to have issues with HTTP2. Disabling HTTP2 will probably yield faster downloads on those configurations.
You can either use the console command  or set it in  like so:

## Run games using discrete GPU
On hybrid graphics laptops, Steam runs games using the integrated GPU by default. See PRIME#PRIME GPU offloading to switch to the more powerful discrete GPU for specific games.

## Flatpak
Steam can also be installed with Flatpak as  from Flathub. The easiest way to install it for the current user is by using the Flathub repository:

 $ flatpak --user remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
 $ flatpak --user install flathub com.valvesoftware.Steam
 $ flatpak run com.valvesoftware.Steam

The Flatpak application currently does not support themes. Also you currently cannot run games via /, see Issue#869 for more details.

Steam installed via Flatpak is not able to access your home directory and overriding this will cause Steam to not run because it is not safe. However, you can freely add directories outside the home directory. If you want to add an external library, run the following command to add it:

 $ flatpak override --user com.valvesoftware.Steam --filesystem=/path/to/directory

Launching Steam with Flatpak might warn you about installing the  package. This package currently does not exist but  can be installed instead, see Gamepad#Device permissions.

## Asian Font Problems with Flatpak
If you are having problem getting Asian fonts to show in game, it is because org.freedesktop.Platform does not include it. First try mounting your local font :

 $ flatpak run --filesystem=~/.local/share/fonts --filesystem=~/.config/fontconfig com.valvesoftware.Steam

If that does not work, consider this hack: make the fonts available by directly copying the font files into org.freedesktop.Platform's directories, e.g.

 /var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/version/hash/files/etc/fonts/conf.avail
 /var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/version/hash/files/etc/fonts/conf.d
 /var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/version/hash/files/share/fonts

## Steam Flatpak start (run) issues
After launch, Steam will try to download files and you will see a progress bar. If it crashes, you may try to give additional permissions to the flatpak package:

 $ flatpak permission-set background background com.valvesoftware.Steam yes
 $ flatpak run com.valvesoftware.Steam

For an alternative way to control permissions, install flatseal.

## SteamCMD in flatpak
SteamCMD can also be used within the flatpak.

 $ flatpak run --command=steamcmd com.valvesoftware.Steam

## Steam settings to reduce video card memory usage
This is useful for video cards with a small amount of video memory.

Make a copy of the Steam shortcut:

 $ cp /usr/share/applications/steam.desktop ~/.local/share/applications/steam_minimal.desktop

and change the  and  sections in the shortcut copy:

As a result, when launching the Steam Minimal (Runtime) shortcut you will get an ascetic interface, which is still functional enough to install and run games, and when launching the standard Steam (Runtime) shortcut you will get a full-fledged client.

## Limit permission to create arbitrary keyboard input to a specific user group
By default, the Steam package will place an udev rule, which basically allows any logged in user to create arbitrary (globally available) input devices which includes virtual keyboards. This may allow things like sandbox escape.

The following pacman hook can be used to modify the global uinput permission to be only granted to a specific user group.

When creating the group, be sure to create a system group:

 # groupadd --system steam

Then add the users, you want to be able to use "Steam Input", to this group.

## Troubleshooting
See Steam/Troubleshooting.
