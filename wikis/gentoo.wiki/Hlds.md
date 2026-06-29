[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Steamcmd&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Steamcmd&action=edit).

**Resources**

[[]][Official documentation](https://developer.valvesoftware.com/wiki/SteamCMD)

[[]][Package information](https://packages.gentoo.org/packages/games-server/steamcmd)

**steamcmd** is the command-line version of the [Steam](https://wiki.gentoo.org/wiki/Steam "Steam") client for dedicated servers. It uses [SteamPipe](https://developer.valvesoftware.com/wiki/SteamPipe) to download content and primarily used to set up game servers that are available through Steam.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Adding the Steam license]](#Adding_the_Steam_license)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Server deployment]](#Server_deployment)
    -   [[2.1] [hlds]](#hlds)
    -   [[2.2] [cstrike]](#cstrike)
-   [[3] [server]](#server)
    -   [[3.1] [hlds]](#hlds_2)
    -   [[3.2] [cstrike]](#cstrike_2)
-   [[4] [Metamod]](#Metamod)
-   [[5] [amxmodx]](#amxmodx)
-   [[6] [Fast download FTP]](#Fast_download_FTP)
-   [[7] [Downgrading steam packages]](#Downgrading_steam_packages)
-   [[8] [External resources]](#External_resources)

## [Installation]

### [Adding the Steam license]

First it is needed to accept the Steam License(s):

If a global license file is used for all packages:

`root `[`#`]`echo "games-server/steamcmd Steam license(s)" >> /etc/portage/package.license`

Else in it\'s own licence file, per package, as example:

`root `[`#`]`echo "games-server/steamcmd Steam license(s)" >> /etc/portage/package.license/steamcmd`

### [Emerge]

`root `[`#`]`emerge --ask games-server/steamcmd`

## [Server deployment]

There are known bugs requiring these commands to be ran several times rather than once.

** Note**\
see external resources at the bottom of this page for a list of game mod numbers for other mods.

### [hlds]

`steam ~/steamcmd/``./steamcmd.sh +login anonymous +force_install_dir "../hlds/" +app_set_config 90 +app_update 90 validate +quit`

### [cstrike]

`steam ~/steamcmd/``./steamcmd.sh +login anonymous +force_install_dir "../hlds/" +app_set_config 90 mod cstrike +app_update 90 mod cstrike validate +quit`

## [server]

### [hlds]

`steam ~/hlds/``./hlds_run +maxplayers 32`

### [cstrike]

`steam ~/hlds/``./hlds_run -game cstrike -autoupdate +maxplayers 32 +map de_dust2`

## [Metamod]

We will use metamod and amxmodx to make administration of your new servers easy.

** Note**\
replace \<mod\> with the hlds mod you\'re using. example \'cstrike\' for counter strike.

`steam ~/hlds/<mod>``mkdir -p addons/metamod/dlls`

** Warning**\
Commands under this bar are experimental & not yet tested extensively.

Download Metamod:

`steam ~/hlds/<mod>/addons/metamod/dlls/``wget `[`http://downloads.sourceforge.net/project/metamod/Metamod%20Binaries/1.20/metamod-1.20-linux.tar.gz`](http://downloads.sourceforge.net/project/metamod/Metamod%20Binaries/1.20/metamod-1.20-linux.tar.gz)

Decompress Metamod:

`steam ~/hlds/<mod>/addons/metamod/dlls/``tar -xf metamod*.tar.gz`

Remove Metamod Archive:

`steam ~/hlds/<mod>/addons/metamod/dlls/``rm metamod*.tar.gz`

Activate Metamod:

[FILE] **`~/hlds/<mod>/liblist.gam`**

    gamedll "cstrike/addons/metamod/dlls/metamod.dll"
    gamedll_linux "cstrike/addons/metamod/dlls/metamod_i386.so"

** Note**\
At this point restart the server and note if metamod version and copyright dates come up.

## [amxmodx]

As amxmodx is a metamod plugin, you will need to tell metamod to load amxmodx.

`steam ~/hlds/<mod>``echo "linux addons/amxmodx/dlls/amxmodx_mm_i386.so" >> addons/metamod/plugins.ini `

`steam ~/hlds/<mod>``wget `[`http://sourcemod.otstrel.ru/amxmodx-1.8.2-base-linux.tar.gz`](http://sourcemod.otstrel.ru/amxmodx-1.8.2-base-linux.tar.gz)` `

`steam ~/hlds/<mod>``tar -xf amxmodx*.tar.gz `

`steam ~/hlds/<mod>``rm amxmodx*.tar.gz`

Then download amxmodx mod specific files and install them to addons/amxmodx/ (sitting next to metamod)

[http://www.amxmodx.org/downloads.php](http://www.amxmodx.org/downloads.php)

amxmodx requires steam ids to know who has administrative powers over your server. To extract steam ids from halflife & mods open a game terminal using \~ & type status, look for your in game player name & copy down the id for later insertion into server files. See:

-   [adding admins to amxmodx](https://wiki.alliedmods.net/Adding_Admins_(AMX_Mod_X))
-   [configuring amxmodx plugins](https://wiki.alliedmods.net/Configuring_AMX_Mod_X)
-   [inserting custom plugins](http://www.amxmodx.org/doc/index.html?page=source%2Fplugins%2Fplugins.htm#install)

## [Fast download FTP]

Install a FTP server to enable fast downloading. Rsync maps and other resources to a FTP directory mirroring the hlds information with out copying passwords or exposing critical configurations.

## [Downgrading steam packages]

Packages can be downgraded with workflow described here [Steam/Client troubleshooting](https://wiki.gentoo.org/wiki/Steam/Client_troubleshooting#SteamVR_doesn.27t_work_after_it_was_updated_.28as_steam_package.29_and_no_workaround_exists "Steam/Client troubleshooting"). AppID, DepotIDs, ChangelistIDs and paths should be replaced with proper values for this package.

## [External resources]

-   [Official steamcmd wiki](https://developer.valvesoftware.com/wiki/SteamCMD#Linux_Game_Server_Managers)
-   [list of server numbers to install other hlds mods](https://developer.valvesoftware.com/wiki/Dedicated_Servers_List)
-   [server performance fps settings](https://support.steampowered.com/kb_article.php?ref=5386-HMJI-5162)
-   [http://metamod.org](http://metamod.org)
-   [http://www.amxmodx.org/](http://www.amxmodx.org/)