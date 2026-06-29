# Linux Quick Start Guide


- [How To Install Heroic Games Launcher](#how-to-install-heroic-games-launcher)
   - [Flatpak](#flatpak)
   - [Non-Flatpak](#non-flatpak)
- [First Steps](#first-steps)
- [How to Add Heroic Games to Steam](#how-to-add-heroic-games-to-steam)
   - [Manual](#manual)
   - [Automatic](#automatic)
- [How to Add Heroic Games to Non-Steam Front-Ends](#how-to-add-heroic-games-to-non-steam-front-ends)
- [Flatpak Permissions](#flatpak-permissions)
   - [Flatseal](#flatseal)
- [Troubleshooting](#troubleshooting)

## How To Install Heroic Games Launcher

### Flatpak

1. If you do not already have Flatpak installed, see [https://flatpak.org/setup/](https://flatpak.org/setup/) for instructions.
   * If you are on SteamOS (Steam Deck) or Bazzite, Flatpaks are pre-installed.
2. Open your software manager and search for "Heroic Games Launcher", double check that the software manager is installing the Flatpak version and install the application.
   * If you are on KDE (SteamOS), the software manager is named "Discover". If you are on GNOME, the software manager is named "Software".
   * Alternatively, you can open a terminal and type `flatpak install com.heroicgameslauncher.hgl` to install the Heroic Games Launcher Flatpak.
3. Once Heroic Games Launcher is installed, open the application and proceed to the next section.

### Non-Flatpak

Heroic is also available as an AppImage and several other formats. To download one of these formats instead, see [https://heroicgameslauncher.com/downloads](https://heroicgameslauncher.com/downloads). Once you have downloaded Heroic, proceed to the next section.

If you are not using the Heroic Flatpak, the [Flatpak Permissions](#flatpak-permissions) section **will not** apply to your install.

## First Steps

1. Open the Heroic Games Launcher.
2. On the left-hand side of the screen, click the `Log in` button and log into your Epic, GOG, or Amazon account. If you have accounts for all three, you may log into all three on this menu.
   * <img src="https://github.com/user-attachments/assets/3912af10-616f-4d3c-b8af-d83f6cc23e33" height="300">
   * Once you have logged into your desired accounts, your Heroic library will now contain games from the various stores. However, make sure to follow all of the steps in this section before you start to install any games.
3. On the left-hand side of the screen, click `Wine Manager`, click `Proton-GE` at the top of the screen, and download either the latest numbered Proton-GE version or `Proton-GE Latest`
   * <img src="https://github.com/user-attachments/assets/40405bb9-d6b8-4027-a856-093657c64055" height="300">
4. You may now proceed to install games from your library. On the left-hand side of the screen, click `Library` (this will only appear if you have logged into an account), select a game to install.
5. If you are on the library view, click the small down arrow to install the game. If you are on the game page, click the `Install` button to install the game.
   * **Library View**
      * <img src="https://github.com/user-attachments/assets/40077b9c-c8c7-4183-a960-169ccde9d123" height="300">
   * **Game Page**
      * <img src="https://github.com/user-attachments/assets/c69d76b8-9043-4155-a928-c62b6e307270" height="300">
6. Installation Page:
   * Typically, if a game offers both Linux and Windows installation options, you will want to select the Windows option. In some cases, the Linux version will work but typically the Linux version may require older libraries or may be outright broken.
   * On the installation page, you may select both the game's installation path and the game's prefix. The game installation folder will contain the primary contents of the game. The prefix is equivalent to a "virtual Windows C: Drive" and will contain any dependencies and game saves.
   * Click `Show Wine Settings` and select the Proton-GE version you installed in Step 4.
   * Once you are satisfied with the options on the installation page, you may press `Install`
7. Once the game is finished installing, you may play the game.

For future installations, you do not need to repeat the Umu and Proton-GE steps above. However, new Proton-GE versions release every few months or so. These releases may contain game-specific fixes and general improvements to Proton.

You do not necessarily need to update to the latest Proton-GE version when it releases but it is typically a good idea to keep up with new releases and to not lag too far behind. When installing new Proton-GE versions, you do not necessarily need to apply these versions to already installed games but rather ensure you are selecting the latest version when you are installing new games.

## How to Add Heroic Games to Steam

If you are on a Steam Deck, non-Steam games added to Steam will automatically appear in Game Mode under the "Non-Steam" tab.

In order to add non-Steam games to Steam, follow the below steps.

### Manual

These steps will cover how to manually add a Heroic game to Steam after it is installed.

1. Open the Heroic Games Launcher.
2. Either install a game or select an already installed game in Heroic.
3. Click the three vertical dots in the top-right section of the screen.
4. Click `Add to Steam`
      * <img src="https://github.com/user-attachments/assets/234336b2-4854-4e8d-9bc8-79015159fd97" height="300">
5. The game will now be added to Steam.

### Automatic

These steps will cover how to automatically add a Heroic game to Steam after it is installed.

1. Open the Heroic Games Launcher.
2. On the left-hand side of the screen, click `Settings`
3. On the left-hand side of the screen, click `Add games to Steam automatically`
      * <img src="https://github.com/user-attachments/assets/ef13d55d-dafa-4111-b7a1-75a360b0d408" height="300">
4. Any newly installed Heroic games will automatically get added to Steam.

## How to Add Heroic Games to Non-Steam Front-Ends

If the front-end you are using supports desktop files, you can create desktop files in Heroic and add these to a folder of your choice. For example, if you are using ES-DE, you may copy these desktop files to the `desktop` folder in order to run Heroic games directly from ES-DE.

1. Open the Heroic Games Launcher.
2. Either install a game or select an already installed game in Heroic.
3. Click the three vertical dots in the top-right section of the screen.
4. Click `Add Shortcut`
      * <img src="https://github.com/user-attachments/assets/bfa56aac-6fe7-45ca-accd-9c599084dced" height="300">
5. A desktop file for the game will be added to the desktop, you may move these to a folder of your choice.
      * <img src="https://github.com/user-attachments/assets/e4ee666b-41d9-4b78-81da-8ea672968ee1" height="300">

## Flatpak Permissions

By design, Flatpaks are sandboxed applications with limited access to your filesystem and host system. This ensures increased security. For more information, see [https://docs.flatpak.org/en/latest/sandbox-permissions.html](https://docs.flatpak.org/en/latest/sandbox-permissions.html). However, sometimes, you may want to grant a Flatpak additional permissions to access a folder it may not have access to otherwise. For Heroic, this would allow you to install games in additional locations or grant Heroic permissions to access additional folders. This section will cover how to use Flatseal to grant Heroic these permissions.

### Flatseal

Flatseal is an application that allows you to easily manage Flatpaks and their permissions.

1. Open your software manager and search for "Flatseal", double check that the software manager is installing the Flatpak version and install the application.
   * If you are on KDE (SteamOS), the software manager is named "Discover". If you are on GNOME, the software manager is named "Software".
   * Alternatively, you can open a terminal and type `flatpak install com.github.tchx84.Flatseal` to install the Flatseal Flatpak.
2. Open Flatseal and select `Heroic Games Launcher` on the left-hand side of the screen.
3. Scroll down to `Filesystem`
   * <img src="https://github.com/user-attachments/assets/011145d0-0c31-40ae-aef1-6f440f5cc418" height="300">
4. Under `Other Files`, type the name of the folder you would like to grant Heroic access to
   * If you are trying to grant Heroic access to an external storage device, keep in mind these external storage devices are mounted as file paths on Linux. Heroic has access to `/media` and `/run/media` by default. However, if there is another storage path, you may add that in Flatseal.
   * If you are trying to grant Heroic access to a folder in your home folder, you may type `~` as a substitute for `home`. For example, if you are trying to grant Heroic access to `$HOME/Applications`, you may type `$HOME/Applications` instead.
   * Added paths will have a blue triangle to the right which will state `Changed by the user` if you hover over the blue triangle.
   * <img src="https://github.com/user-attachments/assets/61e7215f-6553-477f-8edf-74c96086b6ef" height="300">
5. Restart the Heroic Games Launcher if it was open prior to making any permission changes. Once Heroic is restarted, Heroic will now have access to whichever folder you added in Flatseal.

## Troubleshooting

If you installed Heroic as a Flatpak and suddenly notice any issues with Heroic, open a terminal of your choice and enter the command below. The command **will not** remove or clear** any data or configurations.

```
flatpak update && flatpak install --reinstall com.heroicgameslauncher.hgl
```
