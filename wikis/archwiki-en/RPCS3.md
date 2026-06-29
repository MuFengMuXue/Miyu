# RPCS3

RPCS3 is an emulator for PlayStation 3 games.

## Installation
Install  or .

To be able to actually run games, the PlayStation 3 system software is required, as indicated in the quickstart guide. Fortunately it is easy to acquire this firmware compared with other Sony systems like the PlayStation 2. Sony even provides the files online, so it is not necessary to dump anything. Download the  file by clicking on the big button.

After installing RPCS3, open it and go to File > Install Firmware, then choose the downloaded file.

## Configuration
In order to play games comfortably, a gamepad should be present. In the most optimal case, it is an original PlayStation 3 controller. Other gamepads are supported as well, make sure Handlers is set to  under the menu entry Pads.

## Installing games
RPCS3 stores its data in . More game directories can be added. It differentiates between disc dumps and downloaded (PSN) games. Put disc dumps into the  directory and the downloaded ones into the  directory.

The usual way of running games is pointing rpcs3 to the directory or installing it, if it is a .pkg file.

## The difference between downloads and disc dumps
Downloaded games (or other content, such as DLCs) usually consist of only two files, a key (or license) and the actual game. The key is usually contained in a tiny .rap file, the game is much bigger in size, usually around 10-15 gigabytes. Put both files into . name of the game is purely cosmetic, as this directory only exists so that the files, which may have random names, do not make the directory listing unreadable.

Disc dumps contain many files and can easily identified by the  directory in it.  and  contain the icon and background for that specific game.

## Troubleshooting
## Enabling the debug menu
Unfortunately many games are still not fully playable and require workarounds. Since not all settings that are visible by default will help with glitches and other bugs, some important configuration is done in the debug menu. See the RPCS3 FAQ on how to enable the debug menu.

## The main window looks odd with a system-wide dark theme
Users which configured their environment to use dark themes may have problems with the default theme. Go to Config > GUI and choose a different theme.

## Graphics suddenly pop in when compiling shaders
Go to Config > GPU and set Shader Mode to Async with Shader Interpreter.

This can help with situations where it takes a while to fully compile the shaders. Objects are invisible until their shader is compiled, which can ruin the fun of e.g cutscenes.

## Weird graphics errors
If the game once worked perfectly and suddenly stopped working after starting it, clear the cache. It is usually found in  and is safe to remove. This location only contains logs and other things that can be regenerated without problems, like compiled shaders and PPU modules. Removing this will cause the next startup to be slower.

## Increasing RLIMIT_MEMLOCK
 Failed to set RLIMIT_MEMLOCK size to 2 GiB. Try to update your system configuration

Install  and add your own user to the  user group.
