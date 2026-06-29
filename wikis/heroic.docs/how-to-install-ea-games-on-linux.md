# EA Games


- [EA Games through Epic Games](#ea-games-through-epic-games)
- [EA Games through the EA Application](#ea-games-through-the-ea-application)
    - [How to Install the EA Application](#how-to-install-the-ea-application)
    - [How to Install EA Games](#how-to-install-ea-games)
- [How to Debug EA Games](#how-to-debug-ea-games)
    - [How to Repair the EA Application](#how-to-repair-the-ea-application)
    - [`Invalid Name` Error](#invalid-name-error)

***

## EA Games through Epic Games

Some Electronic Arts games require the EA App ([link](https://www.ea.com/ea-app)). The description page for these games will contain "Third-Party Manager EA app". When installing EA games from Epic, Heroic will automatically install and manage the EA application.

<img src="https://github.com/user-attachments/assets/173caae3-8a68-4597-b044-bb45bc5c89b7" height="300">

At this time, Heroic will only manage the EA application for EA games bought from the Epic store. If you have an EA game bought directly from EA, you may follow the steps on this page to sideload the EA application.

***

## EA Games through the EA Application

### How to Install the EA Application

1. Download the `Windows EA App` installer, [https://www.ea.com/ea-app#downloads](https://www.ea.com/ea-app#downloads).
2. Open the Heroic Games Launcher.
3. Click `Add Game`.
4. Write `EA App` in the `Game/App Title` field.
5. Click `Show Wine Settings` and select a Proton-GE version of your choice, typically you can select the latest numbered version.
6. Click `RUN INSTALLER FIRST`.
7. Select the `EAAppInstaller.exe` file downloaded from EA's site in Step 1.
8. When you reach the login screen, exit out of the EA application.
9. Click `Set Executable` and navigate to the prefix folder.
    * By default, this path will be `$HOME/Games/Heroic/Prefixes/default/EA App`.
10. Locate the `EADesktop.exe` in the EA prefix folder:
    * By default, this path will be `$HOME/Games/Heroic/Prefixes/default/EA App/drive_c/Program Files/Electronic Arts/EA Desktop/EA Desktop/EADesktop.exe`
11. Click `Open` and click `Finish`.
12. Locate the `EA App` in the Heroic library and click `Play Now`.
13. You may proceed to the next section to learn how to install your EA games.

### How to Install EA Games

**Note:** When installing games through the EA application, EA games will be installed to the following location: `$HOME/Games/Heroic/Prefixes/default/EA App/drive_c/Program Files/EA Games`.

1. Locate the `EA App` in the Heroic library and click `Play Now`.
2. Sign in to the EA application if you have not done so already.
3. Install a game of your choice.
4. When the installation is complete, close out of the EA App.
5. Open the Heroic Games Launcher.
6. Click `Add Game`.
7. In the `Game/App Title` field, type the name of the game.
8. Click `Show Wine Settings`.
9. Under `Show Wine Settings`, select a Proton-GE version of your choice, typically you can select the latest numbered version.
10. Under `Show Wine settings`, select the `WinePrefix` field and select the EA App prefix created in the [How to Install the EA App](#how-to-install-the-ea-app) section.
    * By default, this path will be `$HOME/Games/Heroic/Prefixes/default/EA App`.
11. Click `Select Executable` and navigate to the folder of the game you installed in Step 3.
    * By default, this path will be `$HOME/Games/Heroic/Prefixes/default/EA App/drive_c/Program Files/EA Games/GAMENAME`.
12. Select the game executable, click `Open`, click `Finish`.
13. Locate the newly installed EA game in the Heroic library and click `Play Now`, your game will now be playable directly through the Heroic Games Launcher.

***

## Troubleshoot EA Games

### How to Repair the EA Application

If the EA app suddenly stops working after an update, you will need to re-run the EA installer. This section will cover how to do so.

This section is applicable for EA games both bought through Epic and directly from the EA store.

1. Download the latest `Windows EA App` installer, [https://www.ea.com/ea-app#downloads](https://www.ea.com/ea-app#downloads)
2. In your Heroic library, locate the `EA App` or the affected EA game.
3. Open the `Settings`
4. Click `Run EXE on prefix`
5. Select the `Windows EA App` installer you downloaded in Step 1 and wait for it to finish installing.
6. EA will now be re-installed and repaired.

### `Invalid name` Error

This error means the EA App was NOT installed properly in the prefix/bottle.
