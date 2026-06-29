## Resident Evil from GOG

### Exit Game

The game does not have an "Exit" option, press F9 twice to exit.

### Graphics Device Error and Videos all black

The game has these 2 issues in both Linux and Mac. At the moment of writing this page (2026-04-10) these are the workarounds:

#### Linux

- Option 1: Use Proton Experimental to fix the videos, add the `WINEDLLOVERRIDES="ddraw=n,b"` [env variable](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Environment-Variables#how-to-set-environment-variables) to fix the Graphics Device Error (You have to enable Steam protons in General Settings > Advanced > `Allow using Valve Proton builds to run games`)
- Option 2: Use GE-Proton or proton-cachyos without proton fixes by adding the `PROTONFIXES_DISABLE=1` [env variable](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Environment-Variables#how-to-set-environment-variables). This fixes both issues but videos use only the top-left quadrant of the screen
- Option 3: Use GE-Proton or proton-cachyos, get a copy of the `SysWOW64/mciavi32.dll` from a Windows installation (not from `System32`), copy the file in the game's install directory, and add this [environment variable](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Environment-Variables#how-to-set-environment-variables) `WINEDLLOVERRIDES="mciavi32=n,b"`. This fixes both issues and videos play properly fullscreen

Extra notes:
- eventually, GE-Proton and proton-cachyos will include the fix from proton experimental and they will work out of the box with no env variables needed
- for option 3, if you don't have a Windows machine, you can extract the mciavi32.dll file from a Windows install ISO, check below for the steps

<details>
  <summary>Extract DLL from Windows ISO</summary>
  For legal reasons, we cannot distribute this file, but you can get it from the official Windows ISO.

  - Download a Windows ISO from Microsoft's website
  - Install `wimtools` or `wimlib` (the command will depend on your distro, like `sudo apt install wimtools`, the tool is `wimlib` on Arch distros)
  - Mount the ISO (the command will depend on your distro, like `sudo mount -o loop Win11.iso /mnt`)
  - Extract the file `wimextract /mnt/sources/install.wim 1 Windows/SysWOW64/mciavi32.dll`
  - You should have the `mciavi32.dll` in the current directory to follow Option 3 instructions
</details>

#### MacOS

For MacOS, the best result I got was using Wine-Crossover-latest and adding wine dll override for the `mciavi32.dll` file. Get a copy of the `SysWOW64/mciavi32.dll` from a Windows installation (not from `System32`), copy the file in the game's install directory, and add this [environment variable](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Environment-Variables#how-to-set-environment-variables) `WINEDLLOVERRIDES="ddraw,mciavi32=n,b"`. The `ddraw` override is needed to fix the Graphics Device error, the `mciavi32` override is needed to fix the black videos.

If you don't have a windows installation to get the DLL from, expand the next details:

<details>
  <summary>Extract DLL from Windows ISO</summary>
  For legal reasons, we cannot distribute this file, but you can get it from the official Windows ISO.

  - Download a Windows ISO from Microsoft's website
  - Install `wimlib` (`brew install wimlib`)
  - Mount the ISO (`hdiutil mount Win11.iso`)
  - Extract the file `wimextract /Volumes/<ISO_NAME>/sources/install.wim 1 Windows/SysWOW64/mciavi32.dll`
  - You should have the `mciavi32.dll` in the current directory to follow the instructions
</details>

Note that Wine Staging will only show the top-left quadrant of the game, clipped, I couldn't fix this. The commercial Crossover and GPTK won't even run the game. Wine-Crossover-latest seems like the best option.

## Resident Evil 2 from GOG

### Exit Game

The game does not have an "Exit" option, press F9 twice to exit.

### Game does not scale to full screen on Linux

If the game looks small centered in the screen, add the `WINEDLLOVERRIDES="ddraw=n,b"` [environment variable](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Environment-Variables#how-to-set-environment-variables).

### Failed to initialize DirectX on MacOS

On MacOS the game seems to work fine with either Wine-Crossover-Latest and Wine-Staging, but needs the `WINEDLLOVERRIDES="ddraw=n,b"` to solve a failed to initialize DirectX crash.

## Resident Evil 3 from GOG

The game seems to work just fine OOTB on Linux.

Press F1 for in-game settings.

### Fix "Internal Error" crash on MacOS

Set the `WINEDLLOVERRIDES="ddraw=n,b"` [environment variable](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Environment-Variables#how-to-set-environment-variables).

### Fix game crashing after initial cinematic on MacOS

This seems to happen with Wine-Crossover-latest. Use Wine-Staging instead.
