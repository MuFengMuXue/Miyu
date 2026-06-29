# Legacy Wiki Home

[Lutris](http://lutris.net) is an open gaming platform for Linux. It helps you install and manage your games in a unified interface. Our goal is to support every game that runs on Linux, from native to Windows games (via Wine) to emulators and browser games. The desktop application and the website are libre software, your contributions are welcome! More information can be found in the [About](https://lutris.net/about/) page.

This Lutris Wiki features additional information on how to use Lutris.

## Integrations

Lutris can interact with different systems, enhancing your gaming experience.

### GOG

Starting with the 0.5.0, you can connect your GOG account with the Lutris client. This will let you import your GOG library in Lutris and automatically download the games without having to get them from GOG.com yourself.

To connect your GOG account, open the "Import games" dialog and select the GOG tab. Here you will have a connect button which will let you enter your GOG credentials.

### Steam

Running Lutris games from [Steam](http://store.steampowered.com/) allows you to easily both install and run games directly from [Steam Big Picture](http://store.steampowered.com/bigpicture). Perform the following steps to add Lutris games to Steam:

1. Make sure you're in Steam Desktop mode (not Big Picture Mode)
1. Select *Games* -> *Add a non-Steam game to my Library*
1. Click *Browse*, filter by file type of *All Files*, and the find the executable of `lutris`
1. Right click on the new "lutris" shortcut and select *Properties*
1. Rename the title to the name of the game you would like to add. For example: [`SuperTux`](https://lutris.net/games/supertux/)
1. Set the launch options to `lutris:rungame/supertux`, where [`supertux`](https://lutris.net/games/supertux/) is the slug of the game, found in the URL of the game on the [Lutris website](https://lutris.net)
1. Add an icon from either [Steam Banners](http://steambanners.booru.org/) or [TheGamesDB](http://thegamesdb.net/)

### Kodi

You can run Lutris games from [Kodi](https://kodi.tv/) by installing the [Lutris Kodi Addon](https://github.com/robloach/script.lutris#lutris-kodi-addon).
