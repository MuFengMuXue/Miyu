## How to add your Heroic library to Steam?
If you're facing problems in launching your Heroic games on Steam, you can take a look at [Heroic Bash Launcher](https://github.com/redromnon/HeroicBashLauncher).

## What is Heroic Bash Launcher?

Heroic Bash Launcher is a tool that helps launch your Heroic Games library directly from the terminal or any game manager/launcher.

It automatically creates launch scripts for each installed game. Each launch script includes the entire launch command (including cloud save syncing) of a game. Yes, it's the same launch command you see when you run `heroic` from the terminal and launch a game.

## Adding your games to Steam

Steam Deck/Flatpak user? [Follow this guide instead.](https://github.com/redromnon/HeroicBashLauncher/wiki/Steam-Deck-(Flatpak)-Guide)

### Syncing
Once you've run the `setup.sh` script, the **_AddToSteam_** bash script will be generated that helps sync your Heroic library to Steam. It basically displays a list of installed games and lets you choose games to be added to Steam.

Once a game is selected the game's launch script will be added as a Non-Steam game, and the relevant artwork will also be downloaded.

### Adding Manually
If you're facing issues or prefer to add games manually, open Steam and add a game's launch script (located in **GameFiles** directory) as a Non-Steam game by performing the following steps:

1. Go to **LIBRARY**
2. Click **ADD A GAME**
3. Select **Add a Non-Steam Game** from the options
4. Select **BROWSE** on the new window that appears
5. For File Type, make sure to choose **All Files**
6. Navigate to `path/to/HeroicBashLauncher/GameFiles` and choose the game's launch file
7. If you want to add more games, repeat steps 4-6
8. Finally, click on **ADD SELECTED PROGRAMS**

You're all setup!
