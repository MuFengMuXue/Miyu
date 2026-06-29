## List with several Legendary and Wine Workarounds:
[EpicLinux Wiki](https://github.com/CommandMC/EpicLinux/wiki)

## Save Game paths
For Cloud Sync to work as expected, where a game saves and syncs is very important to get right. Ensure that Heroic's save location is actually where the game saves are! You can check for the correct folder on the website called PCGamingWiki. (Windows games, for example, are likely saving directly inside the WINEPREFIX root, for obvious reasons)

## Heroic-specific

### Humankind

------

If your game is crashing on launch, you need to enable the EOS overlay.

### SUPERHOT

------

The SUPERHOT launcher does not work with Heroic, since it also uses some Electron components. Luckily, bypassing it is easy:
1. Open up the game-specific settings for SUPERHOT.
2. At the "Select an alternative EXE to run" option, type in "SH.exe".


### Redout: Enhanced Edition

------

This game runs good by using Wine Staging, it just needs a few extra steps:
1. Install VcRedist 2015-2018 (using winetricks or downloading from Microsoft Website) on the Wine Prefix.
2. Go to the game settings and activate DXVK and VKD3D.
3. If the game complains about DX12 not being supported, go to the game `Settings` > `Other` and add `-dx11` to the Game Arguments.
4. The game should open just fine now.

### HITMAN 3

------

The game requires to be run on any "FShack" build of Wine or Proton, otherwise it will crash. Once installed, the game will try and download a faulty update, and thus, needs updates disabled.
1. Open up the game-specific settings for HITMAN 3.
2. Under "Other", go to "Game Arguments", and add `DXVK_CUSTOM_VENDOR_ID=10de %command% --skip-version-check` to the text field.

### Bioshock Collection

------

For the game to run we need to skip the launcher and use Wine-GE and DXVK on the prefix. This is valid for all 3 games of the collection.
1. To skip the launcher, go to the game settings.
2. Then go to **Other Settings**.
3. On **Select an Alternative EXE to Run** select `{GameFolder}/Binaries/Win32/ShippingPC-XGame.exe`.
4. On **Wine settings** select the latest **WINE-GE** (tested on WINE-GE-Proton7-15). If it's not available, you can download it using the **Wine Manager** in Heroic.
5. Activate **DXVK**.
6. Disable `ESYNC` and `FSYNC` to avoid texture issues.
7. Now the game should open just fine.

### Heroes of Might and Magic 3: Complete (from GOG)

------

There seems to be a problem with the game's `xdd.dll` file in the installation folder, it seems to be incompatible with Wine's ddraw. That makes the game fail to open.

There are 2 solutions for the problem

*Option 1: Replace `xdd.dll`*
- Run the game once so the prefix is created
- Look for the `ddraw.dll` inside the prefix's `drive_c/windows/syswow64/` folder
- Copy that file in the game's install directory as `xdd.dll`, replacing the file that's in there

*Option 2: Modify `Heroes3.exe`*
- Run this command to modify the content of the `Heroes3.exe` executable to use `ddraw.dll` instead of `xdd.dll`:
- `sed --in-place 's/xdd\.dll../ddraw.dll/' Heroes3.exe`

Based on [this GOG forum post](https://www.gog.com/forum/heroes_of_might_and_magic_series/if_you_cant_get_homm3_to_work_after_the_latest_update_on_linux_with_wine_read_this/post3).

### Warhammer: Shadow of the Horned Rat

------

The game uses the `ROBOCOPY` command during setup but this is not implemented by Wine, so some files must be copied manually for this game to work.

1. Run the game once so the prefix is created, it will fail to open
2. Look for the `gogdlConfig/heroic_gogdl/gog-support/1433929853/1433929853` folder inside Heroic's config folder (check https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Removing-Uninstalling-Heroic-Games-Launcher to find the correct path for your system)
3. Copy the content of the `sys32` folder in the `drive_c/windows/system32` and `drive_c/windows/syswow64` folders inside the game's prefix
4. Now the game should run

### Hogwarts Legacy on MacOS

------

If you are on an Intel mac, your only option to get the game working is the commercial version of Crossover. If you are on an Apple Silicon (M chip), you can use the free Game Porting Toolkit 3.

#### Error: Visual C++ Runtime missing

<img width="558" height="261" alt="image" src="https://github.com/user-attachments/assets/8e08b46a-86cd-4b9e-9f9d-9db95c860223" />

Heroic tries to autoinstall the `vcrun2022` package with Winetricks, but if you don't have the correct setup for it, it will fail. Make sure this is configured properly before running the game https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Using-Heroic-on-a-Mac-computer#winetricks-setup

If you are still having issues with Visual C++ runtime, read https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Installing-Visual-C---Runtime

#### AMD driver warning

<img width="561" height="338" alt="image" src="https://github.com/user-attachments/assets/c0b92276-7891-4d6e-9a96-ec97abeae9cb" />

This can be ignored, it's not a real problem. Apple's GPU is incorrectly detected as problematic but it works just fine.

#### Frozen in AMD driver warning after closing the game

When using the Game Porting Toolkit 3, you have to disable the MSync and ESync options in Heroic's settings for the game to open a second time.

#### "Failed to initialize Directx 12. Graphics drivers may require an update, or graphics adapter may not be supported" error

When using Crossover, if you get this warning, try creating a Windows 10 bottle instead of a Windows 11 bottle.

#### Error: "Failed to open file descriptor ....Phoenix.uproject"

<img width="481" height="211" alt="image" src="https://github.com/user-attachments/assets/82e99ac3-9820-4610-99a8-e818d0240529" />

This seems to only happen when the game is installed in an external driver. Currently, the only workaround I know to avoid this is to install the game in an internal drive.

Since you are here, it means you already installed the game, so you can move it to another drive using the `Move` option in the 3-dots menu.

### EA App games

------

For MacOS games, check https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/EA-Games-on-Mac
For Linux games, check https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/How-to-install-EA-Games-on-Linux
