## How to use Wine and Proton on Heroic

Heroic can use both Wine and Proton in any version.
For wine, Heroic passes the selected version on the Game Settings along with the `WINEPREFIX` to Legendary.
For Proton, Heroic uses the `--wrapper` and `--no-wine` flags on Legendary, to use the Proton wrapper and have Proton-specific configs and libraries to increase compatibility and fix bugs. Also, instead of a `WINEPREFIX`, Heroic uses the `STEAM_COMPAT_DATA_PATH `for it, using the prefix specified on settings.

## Where does Heroic search for Wine and Proton versions?

Heroic searches for the default installed Wine, normally in `/usr/bin/wine`, and uses it as the default to launch games (the Flatpak version of Wine is not supported for now).
For Proton, there are a few pre-defined paths Heroic searches for it, since the default path varies by distribution.
Those are the default folders that Heroic looks for Proton:
- *`$HOME/.config/heroic/tools/wine`*
- *`$HOME/.config/heroic/tools/proton`*
- *`$HOME/.steam/root/compatibilitytools.d`*
- *`$HOME/.steam/steam/steamapps/common`*
- *`$HOME/.local/share/lutris/runners/wine`*
- *`/usr/share/steam`*

You can also extract a custom version of Wine/Proton to `$HOME/.config/heroic/tools/wine` or `$HOME/.config/heroic/tools/proton` respectively.
It is also possible to go to the Global Settings -> Wine and add a custom Wine installation. For that, you can select the wine/proton binary that you want to use. On the custom wine list, they will show as `Proton Custom` or `Wine Custom`.

## How to open Wine Settings, Winetricks/ProtonTricks, or run exe inside the prefix

On the Game Settings, under the Wine tab, it is possible to run WineCFG, Winetricks, or run an EXE inside the prefix.
When clicking the respective buttons, Heroic will run those tools with the selected Wine version or, in the case of Proton, with the Wine binary that is located under `<proton root>/files/bin/wine`.
Since Heroic runs those tools, like Winetricks, inside the right prefix even when using Proton, there is NO NEED of having Protontricks installed, since Protontricks is to be used on Steam specifically.
