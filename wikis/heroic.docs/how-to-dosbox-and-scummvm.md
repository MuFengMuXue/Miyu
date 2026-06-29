# How To: DOSBOX and SCUMMVM

## Introduction

This page describes how to run DOSBOX and ScummVM games using native builds of those tools.

## Automatic Native Runners

> [!NOTE]
> Automatic native runners feature is used only on Linux, for Windows builds of games.
> Only from GOG and Amazon

Starting with Heroic 2.15.0, all DOSBox and ScummVM games will be ran using the native builds of those tools.

The locations Heroic will scan and the tools that will be used

|  | Flatpak | PATH |
|--------|--------|--------|
| DOSBox | `io.github.dosbox-staging` | `dosbox` |
| ScummVM | `org.scummvm.ScummVM` | `scummvm` |

> [!WARNING]
> The only supported build of DOSBox is DOSBox-Staging.
> It is the only version that handles configuration files tailored for usage on Windows.

## Heroic Games Launcher Flatpak

In case of the Heroic Flatpak, you will need to add permissions to allow Heroic to run commands outside of its Flatpak sandbox. To grant Heroic this permission, see the steps below. Note that this will be used only to run and detect flatpak versions of DOSBox and ScummVM.

> [!NOTE]
> If you are on a Steam Deck and you installed the Heroic Games Launcher from Discover, you are using the Heroic Games Launcher Flatpak.

1. Open your software manager and search for "DOSBox Staging", double check that the software manager is installing the Flatpak version and install the application.
   * If you are on KDE (SteamOS), the software manager is named "Discover". If you are on GNOME, the software manager is named "Software".
   * Alternatively, you can open a terminal and type `flatpak install io.github.dosbox-staging` to install the DOSBOX Staging Flatpak.
2. Open your software manager and search for "Flatseal", double check that the software manager is installing the Flatpak version and install the application.
   * If you are on KDE (SteamOS included), the software manager is named "Discover". If you are on GNOME, the software manager is named "Software".
   * Alternatively, you can open a terminal and type `flatpak install com.github.tchx84.Flatseal` to install the Flatseal Flatpak.
3. Open Flatseal and select `Heroic Games Launcher` on the left-hand side of the screen.
4. Scroll down to `Session Bus`, `Talks`, click the `+` icon and type the following:
   * `org.freedesktop.Flatpak`
   * ![image](https://github.com/user-attachments/assets/8eaf0d36-ef45-43b4-a164-516d69b15d2f)
5. The input will automatically be saved, you may now exit out of Flatseal. If you had the Heroic Games Launcher open previously, exit and reopen the application for the Flatpak permission to properly apply.
6. Heroic will now automatically use DOSBOX Staging for any applicable games.

***

## Advanced Configuration

### Manually getting DOSBOX/ScummVM command arguments

This section describes how to obtain command line arguments used to launch games, for scripting purposes.

#### For games installed using Linux offline installers
Those are schemes for commands using both tools used when launching games using packaged binary. You can check what arguments are passed exactly in `start.sh` file.

- Dosbox `dosbox -conf "${conf_1}" -conf "${conf_2}" -no-console -c exit`
- Scummvm `scummvm -c "${conf}" --themepath=scummvm`


#### Getting launch arguments - Windows builds
For windows builds, if you are missing some files you should try running the game in heroic first. Heroic will run setup when creating the prefix.

1. Navigate into game files
2. Locate and open `goggame-<GAMEID>.info` file (<GAMEID> is a number like 1207658695)
3. Look for the playTask that contains `"isPrimary": "true"` - this is the default launch command
4. In most cases arguments are dependant on working directory so keep this in mind when making the command.

In example command will look like
`/path/to/scummvm -c "/path/to/beneath.ini" beneath`


##### Sample goggame.info file

```json
{
    "buildId": "51156444997712340",
    "clientId": "49002505861146264",
    "gameId": "1207658695",
    "language": "English",
    "languages": [
        "en-US"
    ],
    "name": "Beneath a Steel Sky",
    "playTasks": [
        {
            "arguments": "-c \"..\\beneath.ini\" beneath",
            "category": "game",
            "isPrimary": true,
            "languages": [
                "*"
            ],
            "name": "Beneath a Steel Sky",
            "path": "ScummVM\\scummvm.exe",
            "type": "FileTask",
            "workingDir": "ScummVM"
        },
        {
            "category": "document",
            "languages": [
                "*"
            ],
            "name": "Manual",
            "path": "Manual.pdf",
            "type": "FileTask"
        },
        {
            "category": "document",
            "languages": [
                "*"
            ],
            "link": "http://www.gog.com/support/beneath_a_steel_sky",
            "name": "Support",
            "type": "URLTask"
        },
        {
            "category": "document",
            "languages": [
                "*"
            ],
            "name": "Walkthrough",
            "path": "Walkthrough.pdf",
            "type": "FileTask"
        }
    ],
    "rootGameId": "1207658695",
    "version": 1
}
```
