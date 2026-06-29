# MangoHud

MangoHud is a Vulkan and OpenGL overlay for monitoring system performance while inside applications and to record metrics for benchmarking.

## Installation
Install the  package. Since many old games are 32-bit-only, enable the multilib repository and install the  package as well.

## Configuration
MangoHud is configured via the following files, which are read in the following order:

#
#  (case-sensitive)
#  (for Wine applications, case-sensitive, without the  extension)
#
#  (via environment variables)

## Graphical user interface for configuration
A GUI for configuring MangoHud can be installed from  or .

## Usage
## Keyboard commands
The default keyboard shortcuts include:

{| class="wikitable"
! Keyboard shortcut
! Description
|-
|
| Toggle overlay (HUD)
|-
|
| Toggle overlay (HUD) position
|-
|
| Toggle preset
|-
|
| Toggle FPS limit
|-
|
| Toggle logging
|-
|
| Reload configuration
|-
|
| Upload log file
|-
|
| Reset FPS metrics
|}

## Test configuration
Verify if the program has been setup correctly:

 $ mangohud glxgears
 $ mangohud vkcube

## Run a single game
To run a game with MangoHud start it like this:

 $ mangohud game

## Dynamic hooking for OpenGL applications
The  hook is enabled by default for OpenGL applications. Set the environment variable  to disable it in case of problems, like so:

 $ MANGOHUD_DLSYM0 game

## Use with GameMode
To launch a game with both MangoHud and GameMode, chain the two commands into a single one, like this:

 $ mangohud gamemoderun game

## Run a single Steam game
To make Steam start a game with MangoHud, right click the game in the Library, select Properties..., then in the Launch Options text box enter:

 mangohud %command%

## Run a single Steam game with GameMode enabled too
Same as for enabling Steam game to run with Mangohud but also with option to use it alongside GameMode

 mangohud gamemoderun %command%

## Run Steam with MangoHud
To avoid having to change launch options for all games, you may launch Steam directly with MangoHud:

 $ mangohud steam

MangoHud will detect Steam and will avoid loading itself until a game is launched.

## Enable for all Vulkan games
To make MangoHud automatically launch with all Vulkan games, set the following environment variable:

 MANGOHUD=1

## Troubleshooting
## MangoHUD does not work with native OpenGL Linux applications
Some Linux native OpenGL applications override , preventing MangoHUD from loading. Sometimes, it's possible to edit the app's start script to include the path to MangoHUD's files, like so:

 LD_PRELOAD/usr/lib/mangohud/
