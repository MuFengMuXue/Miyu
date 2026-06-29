# Troubleshooting Heroic And Games

This page covers known issues and possible solutions.

# Troubleshooting Heroic

## Problem: Heroic won't open

- Try running Heroic through a terminal to see if there's any error printed out
- If using the Portable EXE on Windows, check the location of your TEMP folder (https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/issues/2223)
- If using MacOS, you might need to run this command to allow-list Heroic: `xattr -r -d com.apple.quarantine /Applications/Heroic.app`

## Problem: Heroic window is blank/glitched

![image](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/assets/188464/1f5d7a1a-969d-43f1-84dd-d52b31642ab3)

This is a known Electron issue that can affect many Electron apps when the GPU cache gets corrupted.

**Possible solution:**
Delete `$HOME/.config/heroic/GPUCache` or `$HOME/.var/app/com.heroicgameslauncher.hgl/config/heroic/GPUCache` (if using Flatpak) and reopen Heroic.

If that still doesn't work, add the `--disable-gpu` flag to the shortcut that opens Heroic. Note that this does NOT disable the GPU for games, only for Heroic's UI, so it's no going to have an impact on the performance.


# Troubleshooting Games

## Known game issues

### Problem: Fall Guys missing files

![image](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/assets/188464/adfd8d7b-5942-4e1f-b5e4-6c9f07f3854c)

This error should not happen anymore since Heroic 2.13.0. If it still happens, check the manual setup guide https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Fall-Guys

### Known fixes

There are many games which have known fixes. We keep track of them here https://github.com/Heroic-Games-Launcher/known-fixes.

You can use that repository as a guide or you can let Heroic apply them automatically if you have the `Auto install known fixes` option enabled in Settings > Advanced > Experimental Features.

Other resources for known fixes are https://github.com/CommandMC/EpicLinux/wiki and https://github.com/derrod/legendary/wiki


### Problem: Fortnite on Linux/Mac (Anticheat denied)

![image](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/assets/188464/0fcea71d-a137-4ff4-b6ea-611c884371ee)

Fornite does NOT work on anything other than Windows. The game may start but you will get kicked out because of the anticheat not supporting Linux/Mac.

The only option on these systems is to use a streaming service like GeForce Now.


## General issues

### Problem: `Failed to open esync shared memory file` error in logs

`0068:err:esync:esync_init Failed to open esync shared memory file; make sure no stale wineserver instances are running without WINEESYNC.`

**Solution:** There's probably a zombie/stale wine process running in the background, make sure that's gone (kill the process or restart the system)


### Problem: `No such file or directory: '.../bin/wine'` error in logs

```
File "legendary/cli.py", line 3148, in <module>
File "legendary/cli.py", line 3063, in mainFile "legendary/cli.py", line 706, in launch_game
File "subprocess.py", line 951, in __init__File "subprocess.py", line 1837, in _execute_child
FileNotFoundError: [Errno 2] No such file or directory: '/home/.../.config/heroic/tools/wine/Wine-GE-latest/bin/wine'
[11578] Failed to execute script 'cli' due to unhandled exception!
```

**Solution:**

If not using flatpak this is typically missing wine dependencies: install [wine dependencies](https://discord.com/channels/812703221789097985/1044301598018515105/1044301598018515105)

If using flatpak, this happens for example when heroic gets updated while it's running. Restart Heroic and this should get fixed.


### Problem: `ValueError: EGS ProgramData path does not exist` error in logs

```
An error has occurred! Try to Logout and Login on your Epic account.
[Core] INFO: Synced app "7179f095efcc4f92a950a6d9dbd9c602" is no longer in the EGL manifest list.[Core] INFO: Game files exist, assuming game is still installed, re-exporting to EGL...Traceback (most recent call last):
File "legendary\cli.py", line 3069, in <module>File "legendary\cli.py", line 2984, in main
File "legendary\cli.py", line 578, in launch_game
File "legendary\core.py", line 566, in get_installed_game
File "legendary\core.py", line 1861, in egl_sync
File "legendary\core.py", line 1847, in egl_restore_or_uninstall
File "legendary\core.py", line 1824, in egl_exportFile "legendary\lfs\egl.py", line 85, in set_manifest
ValueError: EGS ProgramData path does not exist
[13764] Failed to execute script 'cli' due to unhandled exception!
```

**Solution:** run `legendary egl-sync --disable-sync`, or reinstall the official Epic Games Launcher client.


### Problem: Videos don't play on the SteamDeck (or flatpak in general)

Videos for some games don't play (either skipped or just a black screen)

**Possible Solution:** In most cases, this gets fixed by enabling the `Prefer system libraries` option in the game's settings in Heroic.


### Problem: Missing libs for Linux native game

**Possible Solution:** In most cases, this gets fixed by enabling the `Use Steam Runtime` option in the game's settings in Heroic.


### Problem: Anti-tamper error

![image](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/assets/188464/066f2227-95af-4886-96db-41c966ebf508)

**Solution:** This happens because of denuvo after reinstalling or or changing wine versions (or creating new prefixes) multiple times. Waiting a day should reset this security measure.
