**Resources**

[[]][Home](https://lutris.net/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Lutris "wikipedia:Lutris")

[[]][GitHub](https://github.com/lutris/lutris)

[[]][[#Lutris](ircs://irc.libera.chat/#Lutris)] ([[webchat](https://web.libera.chat/#Lutris)])

[][Lutris Discord Server](https://discord.gg/Pnt5CuY)

[[]][[#gentoo-wine](ircs://irc.libera.chat/#gentoo-wine)] ([[webchat](https://web.libera.chat/#gentoo-wine)])

[[]][Package information](https://packages.gentoo.org/packages/games-util/lutris)

**Article status**

[[]]This article has some todo items:\

-   Write a guide for Installers
-   Fix image in reporting bugs

**Lutris** is an open source gaming platform for Linux. It makes gaming on Linux easier by managing, installing and providing optimal settings for games.

Lutris does not sell games - the user needs to provide copies of the games unless they are open source or freeware. Games can be installed anywhere on the system, Lutris does not impose anything.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Multilib dependencies]](#Multilib_dependencies)
-   [[3] [Runners]](#Runners)
-   [[4] [Installer scripts]](#Installer_scripts)
-   [[5] [Game library]](#Game_library)
-   [[6] [Configuration files]](#Configuration_files)
-   [[7] [Runners and the game database]](#Runners_and_the_game_database)
-   [[8] [Command line options]](#Command_line_options)
-   [[9] [Managing libraries]](#Managing_libraries)
    -   [[9.1] [Locating missing libraries]](#Locating_missing_libraries)
    -   [[9.2] [About missing libraries]](#About_missing_libraries)
-   [[10] [Watchers]](#Watchers)
-   [[11] [Debugging]](#Debugging)
-   [[12] [Planned features]](#Planned_features)
-   [[13] [Where to look for help]](#Where_to_look_for_help)
-   [[14] [Troubleshooting]](#Troubleshooting)
    -   [[14.1] [Wine cannot find winemenubuilder.exe]](#Wine_cannot_find_winemenubuilder.exe)
    -   [[14.2] [Wine cannot find FreeType font library]](#Wine_cannot_find_FreeType_font_library)
    -   [[14.3] [Wine version mismatch]](#Wine_version_mismatch)
    -   [[14.4] [No DirectX 10 or 11 adapter or runtime found]](#No_DirectX_10_or_11_adapter_or_runtime_found)
    -   [[14.5] [SESSION_MANAGER environment variable not defined]](#SESSION_MANAGER_environment_variable_not_defined)
    -   [[14.6] [BadWindow (invalid Window parameter)]](#BadWindow_.28invalid_Window_parameter.29)

## [Installation]

### [USE flags]

### [USE flags for] [games-util/lutris](https://packages.gentoo.org/packages/games-util/lutris) [[]] [An open source gaming platform for GNU/Linux]

  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`test`](https://packages.gentoo.org/useflags/test)   Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-08 04:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install Lutris:

`root `[`#`]`emerge --ask games-util/lutris`

## [Multilib dependencies]

** Important**\
Many games require a working multilib system, this includes some abi_x86_32 vulkan loader libraries. Even if Lutris doesn\'t complain about these missing libraries, it\'s always a good idea to add their respective multilib variants in your package.use, as well emerging the abi_x86_32 variant of net-libs/gnutls and libsdl2, otherwise, errors or launch problems in some particular games will occur.

Add these USE flags into your package.use file:

[FILE] **`/etc/portage/package.use/lutris`**

    media-libs/vulkan-loader      abi_x86_32
    media-libs/vulkan-layers      abi_x86_32
    media-libs/freetype           abi_x86_32
    media-libs/libpng             abi_x86_32
    net-libs/gnutls               abi_x86_32
    media-libs/libpulse           abi_x86_32
    media-libs/alsa-lib           abi_x86_32
    media-libs/libsdl2            abi_x86_32

Once the required multilib dependencies are added into the package.use file, update the system:

`root `[`#`]`emerge --ask --changed-use --deep @world`

## [Runners]

Lutris relies on programs known as \'runners\' to provide a vast library of [games](https://lutris.net/games/). These runners (with the exception of Steam and web browsers) are provided by Lutris, and don\'t need to be installed by the system package manager. Refer to the Lutris website for a list of currently supported [runners](https://lutris.net/games).

## [Installer scripts]

Lutris automates installation of games using configuration scripts written in JSON or YAML, which list the various files needed to install a game and can perform a series of actions on them. The syntax of installers is described [docs/installers.rst on Github](https://github.com/lutris/lutris/blob/master/docs/installers.rst), and is also available on [lutris.net](https://lutris.net/) when writing installers.

A web UI is planned to ease the creation of these scripts.

## [Game library]

Users can optionally create an account on [lutris.net](https://lutris.net/) and connect their account to the client. This will allow the user to sync their game library from the website to the client (not the other way around). The user can also sync their Steam library with the Lutris library on the website.

The client does not store [lutris.net](https://lutris.net/) credentials on the system. Instead, when a user authenticates, the website will send a token which will be used to sync the library. This token is stored in [\~/.cache/lutris/auth-token].

## [Configuration files]

The client, runner, and game configuration files are stored in [\~/.config/lutris]. There is no need to manually edit these files as everything should be done from the client.

-   [lutris.conf]: preferences for the client\'s UI

<!-- -->

-   [system.yml]: default configuration for every game

<!-- -->

-   [runners/\*.yml]: runner-specific default configurations

<!-- -->

-   [games/\*.yml]: game-specific configurations

The game configuration can override previously defined runner and system configuration and runner configuration can override system configuration.

## [Runners and the game database]

The data necessary to manage the game library and run games is stored in [\~/.local/share/lutris].

-   [pga.db]: game library, game installation status, locations on the file system, and some additional metadata, all stored in an SQLite database

<!-- -->

-   [runners/\*]: runners downloaded from lutris.net

<!-- -->

-   [icons/\*.png] and [banners/\*.jpg]: game images

## [Command line options]

The following command line arguments are available:

`user `[`$`]`lutris --help`

    Usage:
      lutris [OPTION…] URI

    Run a game directly by adding the parameter lutris:rungame/game-identifier.
    If several games share the same identifier you can use the numerical ID (displayed when running lutris --list-games) and add lutris:rungameid/numerical-id.
    To install a game, add lutris:install/game-identifier.

    Help Options:
      -h, --help                 Show help options
      --help-all                 Show all help options
      --help-gapplication        Show GApplication options
      --help-gtk                 Show GTK+ Options

    Application Options:
      -v, --version              Print the version of Lutris and exit
      -d, --debug                Show debug messages
      -i, --install              Install a game from a yml file
      -e, --exec                 Execute a program with the lutris runtime
      -l, --list-games           List all games in database
      -o, --installed            Only list installed games
      -s, --list-steam-games     List available Steam games
      --list-steam-folders       List all known Steam library folders
      -j, --json                 Display the list of games in JSON format
      --reinstall                Reinstall game
      --display=DISPLAY          X display to use

Additionally, a protocol link (`lutris:`) followed by a game identifier can be passed on the command line:

`user `[`$`]`lutris lutris:quake`

This will install the game if not already installed or launch the game otherwise (unless the `--reinstall` option is passed).

## [Managing libraries]

If the Lutris runtime is disabled (`Lutris->Preferences->System options->Disable Lutris Runtime`), then Lutris will use system the libraries, otherwise it will use the libraries in [\~/.local/share/lutris/runtime/lib\*].

### [Locating missing libraries]

One way of locating missing libraries is to use [e-file] command which is part of [[[app-portage/pfl]](https://packages.gentoo.org/packages/app-portage/pfl)[]].

`user `[`$`]`e-file <file>`

Where `<file>` is the full name of a file (supports wildcards) that is being located.

### [About missing libraries]

** Important**\
Gentoo may require additional dependencies for Lutris games to work out of the box. Those libraries won\'t be included in Lutris and need to be added manually.

Sent reports to [https://github.com/lutris/buildbot/issues](https://github.com/lutris/buildbot/issues)

## [Watchers]

Lutris is using watchers:

    DEBUG    2018-10-07 09:23:49,284 [steam]:Watching Steam folder /home/$USER/.steam/steam/steamapps

To detect games in the native Steam library and add them to the Lutris library if enabled.

## [Debugging]

** Warning**\
Lutris outputs to [stderr] and [stdout] seemingly at random.

The most effective way to debug Lutris and its runners is to invoke [lutris -d] in terminal with unlimited scroll.

Using [lutris -d 2\>&1 lutris.txt] is also recommended.

## [Planned features]

Here\'s what to expect from the future versions of Lutris:

-   Integration with GOG and Humble Bundle
-   Integration with the TOSEC database
-   Management of Personal Game Archives (will allow storing game files on private storage so that they can be re-installed on other devices)
-   Game saves sync
-   Community features (friends list, chat, multiplayer game scheduling)
-   Controller configuration GUI (with xboxdrv support)

## [Where to look for help]

-   **IRC:** #lutris, #gentoo-wine
-   **Discord:** [Gentoo-discord](https://discordapp.com/invite/gentoo), [Linux_Gamers_Group](https://tuxdb.com/lgg), [Linux_Gaming](https://discord.gg/linuxgaming)
-   **Forum:** [https://forums.lutris.net/](https://forums.lutris.net/)

## [Troubleshooting]

### [Wine cannot find winemenubuilder.exe]

**Info:**\

[winemenubuilder.exe] is used in Wine to make Linux menu shortcut from Windows.

    wine: cannot find L"C:\\windows\\system32\\winemenubuilder.exe"

This should be ignored, because Lutris is going to make its own shortcuts at the end of each installation.

**Possible solution:**\

To remove this error message from Wine console:

    Lutris->Manage runners->Wine->Configure runner->DLL overrrides->Key=winemenubuilder.exe
    Lutris->Manage runners->Wine->Configure runner->DLL overrrides->Value=d

This will disable [winemenubuilder.exe]. `Value` can be set to `b` to enable [winemenubuilder.exe] which is ***not*** recommended for the reasons stated above.

### [Wine cannot find FreeType font library]

FreeType is written in C, designed to be small, efficient, highly customizable, and portable while capable of producing high-quality output (glyph images) of most vector and bitmap font formats.

**Error:**

    Wine cannot find the FreeType font library.  To enable Wine to
    use TrueType fonts please install a version of FreeType greater than
    or equal to 2.0.5.
    http://www.freetype.org

**Solution:**\

a\) Emerging [[[media-libs/freetype]](https://packages.gentoo.org/packages/media-libs/freetype)[]]

b\) Installing libfreetype2 library to the location that is set for a process that needs it.

c\) Installing library to the Lutris runtime.

### [Wine version mismatch]

**Error:**\

    wine client error:0: version mismatch 549/566.

**Solution:**\

a\) This issue was resolved in Lutris 0.4.19+.

b\) Invoke [pkill wine && pkill wineserver]. There is a bug which results in Wine mismatch if the Wine version is changed.

### [No DirectX 10 or 11 adapter or runtime found]

**Error:**\

    ERR_GFX_D3D_NOD3D1X_4 - No DirectX 10 or 11 adapter or runtime found. Please install latest DirectX runtime or install a compatible DirectX 10 or 11 video card.

**Solution:**\

a\) Vulkan and/or DXVK is not configured properly. Check [vulkaninfo].

b\) The Wine application needs DirectX libraries. Use Winetricks to install them.

c\) Lutris is missing libraries in its runtime ([\~/.local/share/lutris/runtime/lib\*]).

### [SESSION_MANAGER environment variable not defined]

**Error:**\

    Failed to connect to session manager: Failed to connect to the session manager: SESSION_MANAGER environment variable not defined

**Solution:**\

Was resolved by restarting Lutris (xkill && lutris)

### [][BadWindow (invalid Window parameter)]

This problem seems to appear when virtual Wine window is [xkill]-ed.

**Error:**\

    X Error of failed request:  BadWindow (invalid Window parameter)

**Solution:**\

Solved by invoking [pkill wine]