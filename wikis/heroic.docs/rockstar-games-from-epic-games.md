# Rockstar Games From Epic Games

This page covers different problems related to launching Rockstar Games owned in Epic.

## Rockstar Launcher opens showing the option to buy the game / Says the game is not owned

> IMPORTANT: Starting Heroic 2.17, all this process should be automated for GTAV and RDR2 for **Linux and Mac**. If it's not, you can configure the `Environment Variables` of the game to include `USE_FAKE_EPIC_EXE=true` in the Advanced tab in the game's settings:

![image](https://github.com/user-attachments/assets/5cad053a-8b97-4158-99af-215ce363da64)

If you are on **WINDOWS**, you have to do these steps manually:
- Download the custom `EpicGamesLauncher.exe` file from https://github.com/Etaash-mathamsetty/heroic-epic-integration/releases (this is NOT the real Epic Games Launcher, it's just a wrapper exe with the same file name)
- Put the `EpicGamesLauncher.exe` file in the install directory of the game (next to the `PlayGTAV.exe` or `PlayRDR2.exe` files)
- Create a text file (1) called `fix.bat` in the install directory (next to the `PlayGTAV.exe`) with this content `start "" EpicGamesLauncher.exe PlayGTAV.exe %*` (replace with `PlayRDR2.exe` as needed) (2)
- In the game's settings in Heroic, in the `Advanced` tab, select the created `fix.bat` file in the `Select an alternative EXE to run` field

Then run the game.

The Rockstar Launcher should open, and, while loading, it should launch the game without getting to the main screen of the Rockstar Launcher.

(1) Make sure the file is a plain text file and not a rich text file
(2) I haven't seen confirmation of the file name for other games like Red Dead Redemption 1, but it's probably a similar pattern

## Denied Anticheat message for GTAV on Linux and Mac

Rockstar updated the game's anticheat solution and did NOT allow running GTA Online on either Mac nor Linux. Because of this, when trying to install GTAV, an dialog will show up explaining this and won't allow the installation of the game.

The story mode does work though, and you can configure Heroic to not block the installation of games with broken anticheat support going to General Settings (in the sidebar) > Advanced > Toggle on the setting "Allow installation of games with broken or denied anticheat".

After that, the game can be installed (though Online mode will still not work).

## GTA V Enhanced Edition

On Linux, you'll need GE-Proton9-27 or newer. It seems to fail with 10-31 and 10-32, use 10-30 if it fails to open the Rockstar Launcher.

On Mac, the Enhanced version of the game currently does not work.

## Rockstar Games on MacOS

To run GTAV or RDR2 on Mac, neither the free `wine-crossover` wine nor the game porting toolkit that can be installed with Heroic work.

The only option that works on Mac is to use the commercial version of [Crossover](https://www.codeweavers.com). Using a Windows 10 bottle seems to work the best.

## GTAV Online

This will ONLY work on Windows. Rockstar added Battleye anticheat without enabling the Linux support https://www.gamingonlinux.com/2024/09/grand-theft-auto-v-gets-battleye-anti-cheat-breaks-online-play-on-steam-deck-linux/. This means online **does NOT work** on Linux nor MacOS and **there's nothing that can be done to fix that**.

## Red Dead Redemption 2 fails to open with `exited unexpectedly`

This is meant to solve this issue:

<img width="948" height="308" alt="image" src="https://github.com/user-attachments/assets/34dc018b-3b2b-431f-80fe-5fa5d6f650c3" />

1. in Heroic, in the game's settings, in the [Environment variables table](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Environment-Variables#how-to-set-environment-variables), add this one (check attached image on how it should look like after added) `Variable Name` => `WINEDLLOVERRIDES`, `Value` => `vulkan-1=n,b`. It should look like this:

<img width="655" height="91" alt="image" src="https://github.com/user-attachments/assets/6b00d378-40c8-41e1-bd36-70effc9e1156" />

2. try to run the game now: it will show a Social Club Error screen, close the game (this is needed so it creates the settings folder)

<img width="899" height="297" alt="image" src="https://github.com/user-attachments/assets/a7910922-f056-4768-b61d-b9bbd54534c0" />

3. then, look for a file called `system.xml` insdie the RDR2 prefix, it should be in something like ... `.../Games/Heroic/Prefixes/Red Dead Redemption 2/drive_c/users/steamuser/Documents/Rockstar Games/Red Dead Redemption 2/Settings/system.xml`

4. open the file with a text editor and look for a line that looks like this: `<API>kSettingAPI_Vulcan</API>` and change it to look like this `<API>kSettingAPI_DX12</API>` (replacing Vulcan with DX12), and save the change

Now the game should launch properly

## "com.epicgames.launcher" protocol issue (only on Windows)

> [!NOTE]
> These steps are only required on Windows. Heroic will automatically apply them on macOS and Linux

When launching a Rockstar title from the Epic Games store, you will encounter the following message:

![image](https://github.com/user-attachments/assets/801c1508-2ab3-4ace-8695-676ff59555ba)

To resolve this, do one of the following:

### Option 1: Use .reg file

Download this .reg file: https://legendary.gl/assets/fnv_fix.reg
Double-click it to merge it into your current registry (feel free to delete the file afterwards)

### Option 2: Add the key yourself

Open up an administrative PowerShell by right-clicking the Windows logo in your taskbar and choosing "Windows PowerShell (Admin)". This will prompt you for administrative access, choose "Yes" there.
In the command prompt that opens, type in `reg add HKCR\com.epicgames.launcher /f` and press enter. Once you've done that, the command prompt should look like this:

![image](https://github.com/user-attachments/assets/aca59f88-419d-46ce-b15b-0f40ee52adcf)
