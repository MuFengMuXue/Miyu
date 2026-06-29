<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Where is Proton installed?](#where-is-proton-installed)
- [Where is the Proton configuration file?](#where-is-the-proton-configuration-file)
- [How does Proton manage WINE prefixes?](#how-does-proton-manage-wine-prefixes)
- [Where are my saved games located?](#where-are-my-saved-games-located)
- [Where are Proton's Wine binaries located?](#where-are-protons-wine-binaries-located)
- [None of my games are launching / "prefix not owned by you" error](#none-of-my-games-are-launching--prefix-not-owned-by-you-error)
- [My game has a graphics launcher that only runs once and I need to change stuff!](#my-game-has-a-graphics-launcher-that-only-runs-once-and-i-need-to-change-stuff)
- [How to enable DXVK HUD with Proton.](#how-to-enable-dxvk-hud-with-proton)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Where is Proton installed?

Proton is located in the "Proton 3.7" directory in your steam library folder, under "common". An example path to the Proton directory is:  
```$HOME/.local/share/Steam/steamapps/common/Proton 3.7/```  
Keep in mind that Proton will be installed in the same library as the first Steam Play game you try to launch, and will only be installed in one location. So if you have a library located in `/mnt/data/SteamLibrary/`, Proton should be located at:  
```/mnt/data/SteamLibrary/steamapps/common/Proton 3.7/```


# Where is the Proton configuration file?

The configuration file is called `user_settings.py` and it is located in the "Proton 3.7" directory. You can either manually create the file, or edit the sample configuration `user_settings.sample.py` by renaming it to `user_settings.py`. 

# How to enable Proton logs?

Add this as a Steam launch option for the game:
`PROTON_LOG=1 %command%`

How?
1. Right-click on the game title under the Library in Steam and select Properties.
1. Under the General tab click the Set launch options... button.
1. Enter the above code in.

Logs will be saved to $HOME/steam-$STEAM_APP_ID.log, overwriting any previous log with that name.

# How does Proton manage WINE prefixes?

Proton creates a new WINE prefix for each game. These prefixes are located in the same library as the game, in the `steamapps/compatdata/[appid]/pfx/` directory ([appid] being the game's [Application ID](https://developer.valvesoftware.com/wiki/Steam_Application_IDs)).  
The default WINE prefix for Proton is located in the `Proton 3.7/dist/share/default_pfx/` directory.

# Where are my saved games located?

Saved games are stored in the game's WINE prefix. For example, if a game's save folder is located in  
```C:\Users\username\My Documents\My Games\SaveFolder```  
on Windows, the folder would be located in  
```(path-to-prefix)/drive_c/users/username/My Documents/My Games/SaveFolder```  
The [How does Proton manage WINE prefixes?](#how-does-proton-manage-wine-prefixes) section covers how to find a game's WINE prefix.

# Where are Proton's WINE binaries located?

All of Proton's binaries and libraries are stored in `Proton 3.7/dist/`. The main WINE executable is located at `Proton 3.7/dist/bin/wine`. 


# None of my games are launching / "prefix not owned by you" error

This is likely caused by attempting to launch games from a library located on an NTFS partition which is not owned by your user. See [#35](https://github.com/ValveSoftware/Proton/issues/35#issuecomment-414949271) for information on how to fix this.

# My game has a graphics launcher that only runs once and I need to change stuff!

In this case, you have a few options:

* Remove the compatdata folder `~/.local/share/Steam/steamapps/compatdata/<APPID>` and relaunch the game
* Delete or modify the ini/settings file (if the game saves one)
* Reinstall the game
* Launch the exe manually with Proton (requires a desktop launcher file, untested)

# How to enable DXVK HUD with Proton.

In launch options 
* `DXVK_HUD=1 %command%` **or** 
* `DXVK_HUD=fps,devinfo %command%`

See [the DXVK README](https://github.com/doitsujin/dxvk/blob/master/README.md#hud) for a full list of HUD configuration options.

# Enabling controller rumble support

Proton does support controller rumble, however, the Steam for Linux client's Gamepad Configuration Support feature [does not support rumble](https://github.com/ValveSoftware/steam-for-linux/issues/4338). To work around this, disable Gamepad Configuration Support in the Steam client settings. If rumble still does not work, this may indicate a bug in Proton.

# Proton exits with 'pid X != Y, skipping destruction..'
Based on https://github.com/ValveSoftware/Proton/issues/131#issuecomment-415117673 this is generally harmless and is part of steam game startup procedure which is unrelated to Proton.