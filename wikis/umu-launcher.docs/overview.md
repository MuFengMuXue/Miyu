# umu-launcher Overview

## Description

### What is this?

This is a unified launcher for Windows games on Linux. It is essentially a copy of the [Steam Runtime Tools](https://gitlab.steamos.cloud/steamrt/steam-runtime-tools) and [Steam Linux Runtime](https://gitlab.steamos.cloud/steamrt/steam-runtime-tools/-/blob/main/docs/container-runtime.md) that Valve uses for [Proton](https://github.com/ValveSoftware/Proton), with some modifications made so that it can be used outside of Steam.

### Why is it called UMU?

An umu is an above-ground oven of hot volcanic stones originating from Polynesian culture. After the stones are heated, the top layer is removed and the food placed on top to heat/cook. We chose the name because Valve's containerization tool is named pressure-vessel. We're "preparing" the pressure vessel similar to how you would use a stove top pressure-cooker -- by placing it on our umu's "stovetop"

### What does it do?

When Steam launches a Proton game, it launches it like this:

```
/home/tcrider/.local/share/Steam/ubuntu12_32/reaper SteamLaunch AppId=348550 -- /home/tcrider/.local/share/Steam/ubuntu12_32/steam-launch-wrapper -- /home/tcrider/.local/share/Steam/steamapps/common/SteamLinuxRuntime_sniper/_v2-entry-point --verb=waitforexitandrun -- /home/tcrider/.local/share/Steam/compatibilitytools.d/GE-Proton8-27/proton waitforexitandrun /home/tcrider/.local/share/Steam/steamapps/common/Guilty Gear XX Accent Core Plus R/GGXXACPR_Win.exe
```

We can ignore this `/home/tcrider/.local/share/Steam/ubuntu12_32/steam-launch-wrapper`, it's just a process runner with no real value other than forwarding environment variables (more on that later).

I managed to pull the environment variables it uses by making Steam run `printenv` for the game's command line. We needed these envvars because Proton expects them in order to function. With them we can essentially make Proton run without needing steam at all.

Next this part `/home/tcrider/.local/share/Steam/steamapps/common/SteamLinuxRuntime_sniper/_v2-entry-point`

The first part `/home/tcrider/.local/share/Steam/steamapps/common/SteamLinuxRuntime_sniper/` is steam-runtime-tools compiled and is used alongside the sniper runtime container used during Proton builds.

The second part `_v2-entry-point` is just a bash script which loads Proton into the container and runs the game.

So, umu is basically a copy paste of `SteamLinuxRuntime_sniper`, which is a compiled version of steam-runtime-tools. We've renamed `_v2-entry-point` to `umu` and added `umu-run` to replace `steam-launch-wrapper`.

When you use `umu-run` to run a game, it uses the specified `WINEPREFIX`, Proton version, executable, and arguments passed to it to run the game in Proton, inside Steam's runtime container JUST like if you were running the game through Steam, except now you're no longer limited to Steam's game library or forced to add the game to Steam's library. In fact, you don't even have to have Steam installed.

### How do I use it?

```
umu-run "$HOME/Games/epic-games-store/drive_c/Program Files (x86)/Epic Games/Launcher/Portal/Binaries/Win32/EpicGamesLauncher.exe" -opengl -SkipBuildPatchPrereq
```

Optionally, with `WINEPREFIX`,`GAMEID`,`STORE`, and `PROTONPATH`:
```
WINEPREFIX=$HOME/Games/epic-games-store GAMEID=umu-dauntless STORE=egs PROTONPATH="$HOME/.steam/steam/compatibilitytools.d/GE-Proton8-28" umu-run "$HOME/Games/epic-games-store/drive_c/Program Files (x86)/Epic Games/Launcher/Portal/Binaries/Win32/EpicGamesLauncher.exe" -opengl -SkipBuildPatchPrereq
```

Notes:

- `WINEPREFIX` designates where to create the wine prefix. If not specified it will default to /home/username/Games/umu/GAMEID
- `GAMEID` designates a corresponding umu-id from the [umu-database](https://umu.openwinecomponents.org/) for games that have fixes that need to be applied. Defaults to umu-default
- `PROTONPATH` designates the full path to a specific proton version. Alternatively you can use value "GE-Proton" to auto-download and use the latest GE-Proton build. Defaults to UMU-Proton. (UMU-Proton is the latest stable version of Valve's proton tool with UMU compatibility added)
- `STORE` designates what storefront to use. UMU uses GAMEID and STORE to search the [umu-database](https://umu.openwinecomponents.org/) for fixes to apply to a game. Defaults to "none".

See the [documentation](https://github.com/Open-Wine-Components/umu-launcher/blob/main/docs/umu.1.scd) for more examples and the [project's wiki](https://github.com/Open-Wine-Components/umu-launcher/wiki/Frequently-asked-questions-(FAQ)) for Frequently Asked Questions.

**Note**: umu-launcher will automatically use and download the latest Steam Runtime that is required by Proton, and move its files to `$HOME/.local/share/umu`.

### What does this mean for other launchers (Lutris, Bottles, Heroic, Legendary, etc.)?

- Everyone can use + contribute to the same protonfixes, no more managing individual install scripts per launcher
- Everyone can run their games through Proton just like a native Steam game
- No Steam or Steam binaries required
- A unified online database of game fixes (protonfixes)

Right now protonfixes packages a folder of 'gamefixes' however it could likely be recoded to pull from online quite easily. The idea is to get all of these tools using this same `umu-run` and just feeding their envvars into it. That way any changes that need to happen can happen in proton-ge and/or protonfixes, or a 'unified proton' build based off GE, or whatever they want.

### What does this mean for other launchers (Lutris, Bottles, Heroic, Legendary, etc.)?

- Everyone can use + contribute to the same protonfixes, no more managing individual install scripts per launcher
- Everyone can run their games through Proton just like a native Steam game
- No Steam or Steam binaries required
- A unified online database of game fixes (protonfixes)

Right now protonfixes packages a folder of 'gamefixes' however it could likely be recoded to pull from online quite easily. The idea is to get all of these tools using this same `umu-run` and just feeding their envvars into it. That way any changes that need to happen can happen in proton-ge and/or protonfixes, or a 'unified proton' build based off GE, or whatever they want.
