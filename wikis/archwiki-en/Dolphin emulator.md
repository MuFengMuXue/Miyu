# Dolphin emulator

Dolphin is a Nintendo GameCube and Wii emulator, currently supporting the x86_64 and AArch64 architectures. Dolphin is available for Linux, macOS, Windows, and Android. It is a free and open source, community-developed project.
Dolphin was the first GameCube and Wii emulator, and currently the only one capable of playing commercial games.

## Installation
Install the  package.

## Playing
Click on browse to set a directory of ISOs so that they are shown as a library on Dolphin's default screen. Otherwise just click Open and select the file.

Also check the official configuration guide and performance guide.

## Dolphin's Wiki
Whenever a game does not work properly, try reading its page on Dolphin's wiki. Listed there are tips on setting up the emulator for each game, version compatibility charts, testing entries, troubleshooting and video previews. Contributions, such as testing entries and workarounds are welcome and help other users.

Here is a  search action command for searching on Dolphin's wiki:

 exo-open --launch WebBrowser https://wiki.dolphin-emu.org/index.php?search=%u

## Use gamepad motion controls
Dolphin can use the motion sensors included with gamepads, such as the DualShock 4 or Switch Pro Controller, to emulate the motion in Wii Remotes.

The easiest way to set this up is to choose the SDL controller instead of the evdev controller in the controller configuration. Motion Inputs should already be set up by the Default mapping.

If moving the gamepad doesn't produce a reaction, SDL might not have permission to read the motion sensors: see Gamepad#Device permissions.

If you cannot use SDL for some reason and need motion controls with evdev, see this guide.

## Themes
To change the theme of Dolphin, place a css file in  directory. Then go to the interface tab in the options and check the Use Custom User Style box. Click on the User Style tab to change the theme.

## Troubleshooting
## Input is not detected after emulation window loses focus once
Enable Render to Main Window under Graphics Settings, or enable Background Input under Controller Settings. == See also ==

* Wikipedia:Dolphin (emulator)
* [https://dolphin-emu.org/docs/guides/performance-guide/ Dolphin's performance guide.
* Dolphin's FAQ
* Dolphin's wiki entry for legally obtaining game dumps.
