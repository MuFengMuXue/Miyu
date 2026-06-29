# Wine/Proton/Crossover note:

## Linux

On Linux, use the latest GE-Proton if possible.

## MacOS

On MacOS, you MUST use the latest commercial/paid Crossover version (neither wine-crossover, wine-staging nor game-porting-toolkit can run Ubisoft Connect).


## IMPORTANT: Heroic 2.20 has a bug that won't install Ubisoft games when clicking the Install button. Use Option 1 below to install games through the Ubisoft Connect launcher, or rollback to an older version of Heroic to install Ubisoft games directly from Heroic's library.

***


Most Ubisoft games require the UbisoftConnect launcher to be installed in order to run (there are some rare exceptions).

There are 2 options to do this:
1. install the launcher itself with the `Add Game` feature and use it to install games
2. install games with Heroic and install the launcher in the game's prefix

Each option has its benefits and cons:
- Option 1 has the benefit of installing the launcher only once, and you can also install games that you own that are in your Epic account
- Option 2 has the benefit of being able to use Heroic's features like shortcuts or `add to steam`

## Requirements

In both cases you need to download the Ubisoft Connect installer from their site https://ubisoftconnect.com/en-US/ (use the `Download for PC` option).

## Installing option 1 (standalone launcher)

- Click `Add Game`
- Set `Ubisoft Connect` as the App title (after clicking outside the field Heroic should find the image for it)
- Click the `RUN INSTALLER FIRST` option and pick the UbisoftConnectInstaller.exe file
- Proceed to install the launcher and, when finished, UNCHECK the option to run Ubisoft Connect (we need to install some dependency first)
- Click the folder icon in the `Select Executable` field
- Navigate to `drive_c/Program Files (x86)/Ubisoft/Ubisoft Game Launcher/` and select the `UbisoftConnect.exe` file
- Click `FINISH`
- The `Ubisoft Connect` card should show up in your library

![image](https://user-images.githubusercontent.com/188464/212219501-b1c0e14c-9369-463d-83cf-2a3a10f279e1.png)

![image](https://user-images.githubusercontent.com/188464/212219557-676d7d10-0122-49ee-99bf-a4ad5bd7c1d4.png)

Now you can launch Ubisoft Connect, log in, and install any game from it.

To play games this way you'll have to always first launch Ubisoft Connect and then run the game from within that launcher.

Note that to actually run games it may require extra dependencies to be installed using Wine, that is NOT covered in this page.

## Installing option 2 (in game prefix)

### NOTE that this option is not needed anymore, Heroic installs Ubisoft Connect automatically when a Ubisoft game is launched for the first time.

If a Ubisoft game is directly installed by Heroic, trying to run the game will result in no result visible and no output in the logs.

- Click the `RUN EXE ON PREFIX` button
- Search for the UbisoftConnectInstaller.exe
- Complete the installation and close the dialog (you don't need to run Ubisoft Connect to login, you can uncheck that option in the last step)

Now you can run the game and it will execute the Ubisoft Connect Launcher automatically.

!IMPORTANT! Sometimes, there's an issue when closing games executed with this approach. After exiting the game, the UbisoftConnect launcher remains open in the taskbar and, in some cases, it CAN NOT be closed manually, rendering Heroic in a state where the `Playing` status of the game never goes away. You can run `pkill -f Ubisoft -9` in a console to kill all the Ubisoft-related processes to fix this.

## Extra notes:
- The Ubisoft Connect Launcher added with the `Add Game` cannot be accessed by games installed using Heroic unless installed in the same prefix
- Individual games may require extra dependencies to be installed or specific configurations and tweaks to run, that is NOT covered in this page, if you need help with this you can ask on our Discord.
