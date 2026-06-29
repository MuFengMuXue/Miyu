# Star Citizen

Star Citizen is a crowdfunded MMO first person space flight simulator, developed by Cloud Imperium Games. The game does not natively support Linux, but there have been promises for a native version.

## Installation
Star Citizen can be installed using the community developed , which runs the game under a custom, Star Citizen tuned Wine runner.

## Alternatives
There are some alternative ways to install the game without using the LUG Helper:

{| class="wikitable"
! Installation
! Frequently successful
! Managed by LUG
|-
| Flatpack
|
|
|-
| Proton
|
|
|-
| Lutris
|
|
|-
| Heroic
|
|
|-
| Bottles
|
|
|-
| Fagus
|
|
|}

## Usage
 $ lug-helper [ -options ]

The lug helper comes with both a graphical and terminal interface. By default, it will start with the graphical interface, prompting the user with a zenity selection menu.

The terminal based mode can be forced using the  or  option. For a list of all available command-line options run:

 $ lug-helper --help

## Game installation
To install the game either select the corresponding options in the graphical interface or run:

 $ lug-helper --no-gui -i

## Post-installation
After installing the game, there are still some recommended options to modify:

* Non-US keyboard layout configuration
* Wayland issue workarounds
* NVIDIA

## Troubleshooting
Because Star Citizen does not have native Linux support, there are a number of issues that can arise during the installation or while running the game.

For any sort of issue with the LUG Helper or the game in general, refer to the corresponding section on the LUG Wiki

## Configuration
There are some ways to customize how the game is being run, as well as options to configure in-game behavior.

## Alternative wine runners
Although the standard LUG Wine Runner is preferred by most users, there may still be some who want to try out other runners. This is a small list of runners recommended by the LUG Wiki:

* RawFox
* Mactan

## Modifying launch script
The installation using the LUG Helper creates a Star Citizen launch scripts which can be easily modified by the user. An upstream version of this script can be found on the LUG Helper GitHub Page.

An example of this may be the addition of environment variables to active certain features, e.g. performance profilers:

 export DXVK_HUD=fps,compiler
 export MANGOHUD=1

## User configuration
Star Citizen supports user configuration files, which can specify graphics options, show debug displays and more.

To make use of this feature, create a file called  in the Star Citizen LIVE directory. When using wine, this directory is commonly located under: . This also applies for custom installation directory names and alternative game version installations.

For available console commands, see the Console Commands page on the unofficial Star Citizen Wiki.
