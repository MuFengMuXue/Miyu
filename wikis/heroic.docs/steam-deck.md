# Steam Deck


- [Usage](#usage)
- [How to Install Heroic Games Launcher](#how-to-install-heroic-games-launcher)
   - [Flatpak **(Recommended)**](#flatpak-recommended)
       - [Flatpak Permissions](#flatpak-permissions)
   - [AppImage](#appimage)
       - [Game Mode](#game-mode)
   - [How to Add Heroic Games to Steam/Game Mode](#how-to-add-heroic-games-to-steamgame-mode)
       - [Manual](#manual)
       - [Automatic](#automatic)
   - [HDR](#hdr)
       - [Flatpak](#flatpak)
       - [AppImage](#AppImage)
   - [Common Issues](#common-issues)
       - [Mangohud does not work](#mangohud-does-not-work)
       - [Gamescope not available](#gamescope-not-available)

## Usage

It is intended to install and configure games from desktop mode only. Running Heroic itself through Game Mode is not supported and you may encounter issues doing so.

The proper way to use Heroic with the Steam Deck is to open Heroic in desktop mode, install and update games from there. You may need to play games at least once in desk top mode to confirm that they are functioning properly and in the case where a game requires user interaction on first launch, such as associating your Epic account with the game via a web browser pop up.

Once a game is installed, you can add it to steam through the 3 dot menu on the game page, or by selecting "auto add to steam" from the heroic settings on the side bar.

## How to Install Heroic Games Launcher

### Flatpak (Recommended)

To install Heroic Games Launcher using the Flatpak, follow the below steps. The Flatpak is the recommended packaging method to use Heroic Games Launcher on the Steam Deck.

1. Switch to **Desktop mode**.
2. Open the app store (Discover).
3. Search for "Heroic".
4. There should be a result for Heroic Games Launcher. Click install.
5. You should now be able to launch Heroic like any other application on your Steam Deck!

#### Flatpak Permissions

Purpose: Give permissions to SD Card, other partitions, external drives, etc.

Flatpak's containerization while intended for increased security does limit Heroic's permissions to several system's features and folders. It is necessary to give extra permissions to Heroic.

**If you are using KDE (includes the Steam Deck):**

1. Open the `System Settings`
2. On the left-hand side, click `Applications` under the `Personalization` section
3. On the left-hand side, click `Flatpak Permission Settings`
4. In the list of applications, locate Heroic Games Launcher and click it to open the permissions menu.
5. On the right-hand side under the `Permissions` menu, locate the `Filesystem Access` section.
6. Click `Add New` and add your preferred path.
7. When finished, set it to `read/write` and click `OK`
8. Restart Heroic Games Launcher.

**If you are not using KDE:**

In this case we will need to install Flatseal from the Discover or another Linux Store that you use.

1. Search for and install Flatseal on your Store, Discover on Steam Deck.
    * ![image](https://user-images.githubusercontent.com/26871415/167460932-af7100b7-7a26-4e4e-8ca9-db1bb9d9d4fb.png)
2. Open Flatseal and Search for Heroic Games Launcher:
    * ![image](https://user-images.githubusercontent.com/26871415/167461051-3b2f5cf7-c38e-4a63-bbdb-ce6c0302175f.png)
3. Looks for the Filesystem section and add the folders you need to access like shown on the image above.
4. Restart Heroic.

### AppImage

To install Heroic Games Launcher using the AppImage, follow the below steps.

1. Switch to Desktop Mode.
2. Open the Heroic "Releases" page, [https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/releases](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/releases)
3. Download the `Heroic-*.*.*.AppImage` file
   * Depending on when you are reading this page, the version # may differ
   * If you do not see the AppImage, click `Show all ## assets`
4. Move the newly downloaded AppImage to the `/home/deck/Applications` folder
   * If you do not have an `Applications` folder, it is recommended you create one but you may place the AppImage wherever you would like
5. Right click the AppImage, click `Properties`, `Permissions`, check `Is Exectuable`
6. Double click the AppImage to open Heroic.

#### Game Mode

Though it is not recommended to use Heroic in Game Mode, you may add the AppImage to Game Mode by following the below steps. If you are using Heroic in Game Mode, it is highly recommended you only do so to launch your games. Installing, updating, and managing your games should be done in Desktop Mode.

1. Switch to Desktop Mode, right click the Heroic AppImage, and click `Add to Steam`
2. Switch to Game Mode, open the Heroic shortcut by clicking it once.
3. Click the `Gear` icon on the right-hand side of the screen.
4. Click `Properties`
5. On the left-hand side of the screen, click `Shortcut`
6. Scroll down to `Launch Options`
7. Type `--no-sandbox`
8. Heroic will now launch in Game Mode.

## How to Add Heroic Games to Steam/Game Mode

Non-Steam games added to Steam will automatically appear in Game Mode under the "Non-Steam" tab. In order to add non-Steam games to Steam, follow the below steps.

### Manual

These steps will cover how to manually add a Heroic game to Steam after it is installed.

1. In Desktop Mode, open Heroic.
2. Either install a game or select an already installed game in Heroic.
3. Click the three vertical dots in the top-right section of the screen.
4. Click `Add to Steam`
5. The game will now be added to Steam and appear under the "Non-Steam" tab in Game Mode.

### Automatic

These steps will cover how to automatically add a Heroic game to Steam after it is installed.

1. In Desktop Mode, open Heroic.
2. On the left-hand side of the screen, click `Settings`
3. On the left-hand side of the screen, click `Add games to Steam automatically`
4. Any newly installed Heroic games will automatically get added to Steam and appear under the "Non-Steam" tab in Game Mode.


## HDR

### Flatpak

- [Installing Gamescope](#installing-gamescope)
- [Optional: Freezing Gamescope Updates](#optional-freezing-gamescope-updates)
- [Validating Gamescope's Version](#validating-gamescopes-version)

#### Installing Gamescope

The Heroic Flatpak requires the Gamescope Flatpak to enable HDR. However, the Flatpak Gamescope version must match the version of the natively installed Gamescope. As of December 11th, 2024, the Steam Deck Gamescope is on version `3.15.14`. The natively installed Gamescope is close enough to the latest version of the Flatpak meaning the only step required to enable HDR is to install the Flatpak Gamescope.

To enable HDR with the Flatpak version of Heroic, follow the below steps.

1. Switch to Desktop Mode.
2. Open Konsole.
3. Type the following command and press enter:
    * `flatpak install org.freedesktop.Platform.VulkanLayer.gamescope`
    * Locate `runtime/org.freedesktop.Platform.VulkanLayer.gamescope/x86_64/24.08` in the list and confirm your selection by typing the respective number. For example, if it is the third item in the list, type `3` and press enter.
4. The Flatpak Gamescope will now be installed and HDR will now work in Game Mode.

#### Optional: Freezing Gamescope Updates

If the Gamescope Flatpak updates and is no longer in sync with the natively installed Gamescope, HDR may stop working. As an optional step, you may mask the Gamescope Flatpak in order to "freeze" its updates.

1. Switch to Desktop Mode.
2. Open Konsole
3. Type the following command and press enter:
    * `sudo flatpak mask org.freedesktop.Platform.VulkanLayer.gamescope`
4. The Gamescope Flatpak will now be masked and its updates will be "frozen".

To unmask the Gamescope Flatpak, use the following command:

`sudo flatpak --remove mask org.freedesktop.Platform.VulkanLayer.gamescope`

#### Validating Gamescope's Version

1. Switch to Desktop Mode.
2. Open Konsole.
3. Type the following command and press enter:
    * `gamescope --version`
    *  As of December 11th, 2024, the Gamescope version currently installed should be `3.15.14`, note this down for the next step.
4. Open [https://flathub.org/apps/org.freedesktop.Platform.VulkanLayer.gamescope](https://flathub.org/apps/org.freedesktop.Platform.VulkanLayer.gamescope) in a web browser of your choice.
5. Locate the version number at the top of the page and compare it to the version number you gathered in Step 3.
    * As of December 11th, 2024, the version gathered in Step 3 should be `3.15.14` and the version on the link above should be `3.14.24`. These versions are close enough for the Gamescope Flatpak to work through the Heroic Games Launcher.

### AppImage

HDR will work out of the box with the AppImage.

## Common Issues

### Mangohud does not work

Check if you have installed the Flatpak version of Mangodhud: `flatpak install org.freedesktop.Platform.VulkanLayer.MangoHud`, make sure to install the one that uses the flatpak runtime `24.08`.

### Gamescope not available

Check if you have installed the Flatpak version of Gamescope: `flatpak install org.freedesktop.Platform.VulkanLayer.gamescope/x86_64/24.08`

If you are on a Steam Deck, the Flatpak version of Gamescope must match the natively installed version. If these versions do not match, you may experience increased crashing in other Flatpaks.
