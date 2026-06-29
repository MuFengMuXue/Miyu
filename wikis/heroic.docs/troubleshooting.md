## General Debugging tips:

**First thing to know is that Heroic is just a GUI (Graphical Interface), unlike Lutris, it doesn't call wine/proton directly, it uses Legendary for it. So is good to have in mind that some issues that you might have with some game might not be related with Heroic or even with Legendary as well.**

### Config files

Those are stored under:
* Linux: `$HOME/.config/heroic` (settings, caching, gog installed games and metadata, and logs) and `$HOME/.config/legendary` (epic installed games, metadata, user information, etc).
* Linux/SteamOS (Flatpak): `$HOME/.var/app/com.heroicgameslauncher.hgl/config/heroic/` and `$HOME/.var/app/com.heroicgameslauncher.hgl/config/legendary/`,
* Windows: `%AppData%\heroic` (caching), `%UserProfile%\.config\heroic` and `%UserProfile%\.config\legendary`.
* MacOSX: `$HOME/Library/Application Support/heroic` (caching), `$HOME/.config/heroic` and `$HOME/.config/legendary`.

The General settings for Heroic is the file called `config.json`.
Caching is stored under the `store` folder.
The Game settings and Game Logs (Installation and PlayLogs) are in the `GameConfig` folder.

### Not Supported Games

Right now Heroic doesn't support games that require an external launcher like Origin or Uplay.

### How to read output from game launch

Go to the GamePage clicking on the GameCard, and then click on the Tools tab on the top and then click on Latest Log.
That will open a log file with everything that happened when you tried to launch the game.
With that, you can start troubleshooting and use it to get help on our Discord Server or on any Linux Community.

### Game Won't Launch

Several things can cause that and probably Heroic has little or nothing to do with it.
But, one thing you can check is the Compatibility with the game on ProtonDB, even though there you will find more things related to the game on Steam and might not apply to the Epic Games version.

Another thing is to check the latest log like was said above.

Some games like Borderlands 2 and Borderlands: The Pre-Sequel, need that you install some things on the prefix first. Normally the needed files stay under a folder called `redist` or something similar under the game folder and have all the necessary `exe` or `msi` files. To install them, open the Game Settings and go to the Wine Tab. Then you can use the feature called Install EXE on prefix to install those files.

Sometimes, after a long time without using Heroic, your credentials might expire, we are working on showing a message about that and ask to login again, but for now, nothing is shown and when trying to launch the game, nothing will happen. So you will need to manually click logout and restart Heroic. Login again and then launch your game. All your games will be there, don't worry about them being uninstalled.

### Wine not found error when launching

If you are using an old version of Heroic, prior to 2.3.0, you might encounter this error and it is simple to solve.
Just go to the game settings, wine settings, then select a different wine version and then get back to the other one.
In case you have only one version being shown, try downloading a new version from the Wine Manager.
This is due to some changes that we did on how we handle settings from 2.3.0.

### Game still shows as installed after uninstalling or uninstalled after installing

Most of the time, this can be fixed by Refreshing the Library (found under the User Submenu).
If that doesn't fix it. Call for help in our Discord Server.

### Game installed but on a different path and Heroic can't launch it

For that, you can use the helper on the GamePage that fixes the installed path.
Go to the game page, click on the settings button and choose to change the installed path.
If that doesn't work for some reason, you can fix it manually by changing the path on the `.config/legendary/installed.json` file.

### Heroic doesn't open, never loads games after login or shows a Blank Window

Close the App or kill the process if necessary then:
* Try removing/renaming the Heroic folder and the Legendary folder: `$HOME/.config/legendary`.

And Login again with a NEW SID. It is important that you generate a new SID because after using it the first time it becomes invalid.

![image](https://user-images.githubusercontent.com/77377160/112746130-a63b4500-8fca-11eb-8b72-461f5b80e8f6.png)

### Running Heroic from Terminal/Powershell to debug errors
- Linux: Just open the terminal and type `heroic` if it's installed globally or launch the AppImage from it.
- Windows: Open Powershell and Navigate into `%USER%\AppData\Local\Programs\heroic`. Run `.\Heroic.exe`
- Mac: Open the terminal, navigate to `/Applications/Heroic.app/Contents/MacOS` and run `./Heroic`

### Debugging frontend Errors

By default, when launching Heroic from the terminal, you will be able to see all the backend messages, errors, warnings, etc. But not from the frontend. To enable the frontend logs to show up in the terminal, launch heroic with the `--enable-logging` flag. Like: `heroic --enable-logging` or `ELECTRON_ENABLE_LOGGING=true heroic` on Linux and MacOSX.

### Interesting solved issues
- Protocol Not registered: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/issues/577
- Heroic doesn't load games because of locale issue: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/issues/526
- Issues with missing python libs (especially OpenSuse Tumbleweed): https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/issues/310
- Heroic doesn't load the library: https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/issues/1097
