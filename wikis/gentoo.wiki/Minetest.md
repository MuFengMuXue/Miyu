[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Luanti&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.luanti.org/)

[[]][Package information](https://packages.gentoo.org/packages/games-engines/minetest)

[[]][GitHub](https://github.com/luanti-org/luanti)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Luanti "wikipedia:Luanti")

**Luanti** (formerly **Minetest**, see [[[bug #943292]](https://bugs.gentoo.org/show_bug.cgi?id=943292)[]]) is a voxel game engine. Luanti should not be confused with [Minetest Game](https://content.luanti.org/packages/Minetest/minetest_game/), which uses this engine.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Flatpak]](#Flatpak)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Server]](#Server)
        -   [[2.1.1] [Server-side game installation]](#Server-side_game_installation)
        -   [[2.1.2] [Server-side mod installation]](#Server-side_mod_installation)
        -   [[2.1.3] [Server configuration]](#Server_configuration)
        -   [[2.1.4] [OpenRC]](#OpenRC)
        -   [[2.1.5] [systemd]](#systemd)
-   [[3] [SELinux]](#SELinux)
    -   [[3.1] [OpenRC service policy]](#OpenRC_service_policy)
        -   [[3.1.1] [Installation of OpenRC service policy]](#Installation_of_OpenRC_service_policy)
        -   [[3.1.2] [Removal of OpenRC service policy]](#Removal_of_OpenRC_service_policy)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [The server is not running]](#The_server_is_not_running)
    -   [[4.2] [No sound]](#No_sound)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Unmerge]](#Unmerge)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [games-engines/minetest](https://packages.gentoo.org/packages/games-engines/minetest) [[]] [A free open-source voxel game engine with easy modding and game creation]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+client`](https://packages.gentoo.org/useflags/+client)         Build Minetest client
  [`+curl`](https://packages.gentoo.org/useflags/+curl)             Add support for client-side URL transfer library
  [`+server`](https://packages.gentoo.org/useflags/+server)         Build Minetest server
  [`+sound`](https://packages.gentoo.org/useflags/+sound)           Enable sound support
  [`+test`](https://packages.gentoo.org/useflags/+test)             Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`leveldb`](https://packages.gentoo.org/useflags/leveldb)         Enable LevelDB backend
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)         Add ncurses support (console display library)
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`postgres`](https://packages.gentoo.org/useflags/postgres)       Add support for the postgresql database
  [`prometheus`](https://packages.gentoo.org/useflags/prometheus)   Enable prometheus client support
  [`redis`](https://packages.gentoo.org/useflags/redis)             Enable redis backend via dev-libs/hiredis
  [`spatial`](https://packages.gentoo.org/useflags/spatial)         Enable SpatialIndex AreaStore backend
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-04 09:36] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask games-engines/minetest`

** Important**\
As of 2025-01-24 the package (v5.9.1) incorrectly defines build dependencies, as a workaround install the missing dependency manually:

`root `[`#`]`emerge --ask --oneshot x11-apps/xinput`

Wayland users must also install [Xwayland](https://wiki.gentoo.org/wiki/Xwayland "Xwayland") or Luanti will not start.

### [Flatpak]

Luanti can also be installed via [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak"). To install the [official package](https://flathub.org/apps/net.minetest.Minetest), run:

`user `[`$`]`flatpak remote-add --user --if-not-exists flathub `[`https://flathub.org/repo/flathub.flatpakrepo`](https://flathub.org/repo/flathub.flatpakrepo)

`user `[`$`]`flatpak install --user flathub net.minetest.Minetest`

To run Luanti use the following command:

`user `[`$`]`flatpak run --user net.minetest.Minetest`

** Important**\
Wayland users must also install [Xwayland](https://wiki.gentoo.org/wiki/Xwayland "Xwayland") or Luanti will not start.

## [Configuration]

### [Server]

#### [Server-side game installation]

All games should be manually downloaded and installed in the [/var/lib/minetest/.minetest/games/] directory. Games can be downloaded from the [official website](https://content.luanti.org/packages/?type=game). The games are distributed as zip archives that need to be extracted. As an example, to install the [Minetest Game](https://content.luanti.org/packages/Minetest/minetest_game/), the following steps should be performed:

`root `[`#`]`cd /var/lib/minetest/.minetest/games `

`root `[`#`]`wget `[`https://content.luanti.org/packages/Minetest/minetest_game/releases/29428/download/`](https://content.luanti.org/packages/Minetest/minetest_game/releases/29428/download/)` -O minetest_game.zip `

`root `[`#`]`unzip minetest_game.zip`

** Note**\
The game release used in this example may be outdated, retrieve a new link via the mentioned above website.

In order to launch the game, provide its name to the [[[minetestserver(6)]](https://manpages.org/minetestserver/6)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") using the `--gameid` command line argument (`--gameid minetest_game` for the above example).

The worlds will be located in the [/var/lib/minetest/.minetest/worlds/] directory.

#### [Server-side mod installation]

As games, mods need to be downloaded manually and installed in the [/var/lib/minetest/.minetest/mods/] directory. Mods can be downloaded from the [official website](https://content.luanti.org/packages/?type=mod). However, it is important to check the compatibility of the mod with the installed game, as well as to install all its dependencies. As an example, to install the [Mobs Monster](https://content.luanti.org/packages/TenPlus1/mobs_monster/) mod, the [Mobs Redo API](https://content.luanti.org/modnames/mobs/) mod must also be installed, otherwise Luanti will crash with no error messages. After the mods were installed, the [world.mt] file needs to be modified to load the mods:

[FILE] **`/var/lib/minetest/.minetest/worlds/world/world.mt`**

    load_mod_mobs = true
    load_mod_mobs_monster = true

#### [Server configuration]

The configuration is done in the [/etc/minetest/minetest.conf] file, which must be created manually. An example script can be found [here](https://github.com/luanti-org/luanti/blob/master/minetest.conf.example) (check the `## Server` section).

The minimal configuration file requires only one field to be specified (replace `7777:777:7777:7777::1` with the IP address):

[FILE] **`/etc/minetest/minetest.conf`**

    bind_address = 7777:777:7777:7777::1

** Note**\
Luanti supports [IPv6](https://wiki.gentoo.org/wiki/IPv6 "IPv6") addresses.

Luanti uses port 30000 by default, which is recommended ^[\[1\]](#cite_note-1)^.

Luanti only uses [UDP protocol](https://en.wikipedia.org/wiki/User_Datagram_Protocol "wikipedia:User Datagram Protocol"), all other traffic can be safely dropped by a firewall.

#### [OpenRC]

** Note**\
This section assumes that the [/etc/minetest/minetest.conf] file is created as described above.

The Luanti package comes with a [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") service script, which is designed to simplify server startup.

-   [/etc/init.d/minetest-server] - Run script for OpenRC.
-   [/etc/conf.d/minetest-server] - Configuration run script for OpenRC.

** Important**\
\*[/etc/conf.d/minetest-server] must be modified to read the [/etc/minetest/minetest.conf] file (add `--config /etc/minetest/minetest.conf` to the `ARGS`)

-   [/etc/conf.d/minetest-server] must be modified to launch the desired game (add `--gameid GAME_ID_GOES_HERE` to the `ARGS`)

To start the server, run the command:

`root `[`#`]`rc-service minetest-server start`

To start the server at system boot, run:

`root `[`#`]`rc-update add minetest-server default`

#### [systemd]

** Note**\
This section assumes that the [/etc/minetest/minetest.conf] file is created as described above.

To start the server, issue the following:

`root `[`#`]`systemctl start minetest-server`

If the server should automatically start when the system reboots, run:

`root `[`#`]`systemctl enable minetest-server`

## [SELinux]

As of 2025-01-24, there are no official [SELinux](https://wiki.gentoo.org/wiki/SELinux "SELinux") policies for Luanti.

### [OpenRC service policy]

The following policy covers only the server side of Luanti and assumes that the server will run via the OpenRC service.

[FILE] **`luanti-server.te`**

    # License: 0BSD

    policy_module(luanti-server, 1.0)

    gen_require(`
      attribute file_type, non_security_file_type, non_auth_file_type;
      type nsfs_t;
      type initrc_t;
      type var_lib_t;
      type var_log_t;
      type cert_t;
      type usr_t;
      type etc_t;
      type urandom_device_t;
      type unreserved_port_t;
      type node_t;
      role system_r;
      class file getattr;
      class process setcap;
    ')

    # Allow to drop the root privileges
    allow initrc_t self:process setcap;

    ##
    # Type declarations.
    #
      type luanti_server_t;
      type luanti_server_exec_t;

      domain_type(luanti_server_t)
      domain_entry_file(luanti_server_t, luanti_server_exec_t)

      type luanti_server_data_t;
      typeattribute luanti_server_data_t file_type, non_security_file_type, non_auth_file_type;

      type luanti_server_game_data_t;
      typeattribute luanti_server_game_data_t file_type, non_security_file_type, non_auth_file_type;

      type luanti_server_mod_data_t;
      typeattribute luanti_server_mod_data_t file_type, non_security_file_type, non_auth_file_type;

      type luanti_server_world_data_t;
      typeattribute luanti_server_world_data_t file_type, non_security_file_type, non_auth_file_type;

      type luanti_server_log_t;
      typeattribute luanti_server_log_t file_type, non_security_file_type, non_auth_file_type;

    ##
    # Domain transition.
    #
      domtrans_pattern(initrc_t, luanti_server_exec_t, luanti_server_t)
      role system_r types luanti_server_t;

    ##
    # Requirements.
    #
      # Access to /var/log/minetest
      allow luanti_server_t var_log_t:dir ;
      allow luanti_server_t luanti_server_log_t:dir ;
      allow luanti_server_t luanti_server_log_t:file ;

      # Access to /var/lib/minetest
      allow luanti_server_t var_lib_t:dir ;
      allow luanti_server_t luanti_server_data_t:dir ;
      allow luanti_server_t luanti_server_data_t:file ;

      # Access to /var/lib/minetest/.minetest/games
      allow luanti_server_t luanti_server_game_data_t:dir ;
      allow luanti_server_t luanti_server_game_data_t:file ;

      # Access to /va/lib/minetest/.minetest/mods
      allow luanti_server_t luanti_server_mod_data_t:dir ;
      allow luanti_server_t luanti_server_mod_data_t:file ;

      # Access to /var/lib/minetest/.minetest/worlds
      allow luanti_server_t luanti_server_world_data_t:dir ;
      allow luanti_server_t luanti_server_world_data_t:file ;

      # Access to /usr/share/minetest
      allow luanti_server_t usr_t:dir read;
      allow luanti_server_t usr_t:file ;

      # Access to /etc/minetest
      allow luanti_server_t etc_t:file ;

      # Signals
      allow luanti_server_t self:process signal;

      # SSL
      allow luanti_server_t cert_t:dir search;
      allow luanti_server_t cert_t:file ;

      # Sockets
      allow luanti_server_t self:udp_socket ;
      allow luanti_server_t unreserved_port_t:udp_socket name_bind;
      allow luanti_server_t node_t:udp_socket node_bind;

      # urandom
      allow luanti_server_t urandom_device_t:chr_file ;

[FILE] **`luanti-server.fc`**

    /usr/bin/minetestserver  gen_context(system_u:object_r:luanti_server_exec_t)
    /var/log/minetest(/.*)? gen_context(system_u:object_r:luanti_server_log_t)
    /var/lib/minetest(/.*)? gen_context(system_u:object_r:luanti_server_data_t)
    /var/lib/minetest/.minetest/games(/.*)? gen_context(system_u:object_r:luanti_server_game_data_t)
    /var/lib/minetest/.minetest/mods(/.*)? gen_context(system_u:object_r:luanti_server_mod_data_t)
    /var/lib/minetest/.minetest/worlds(/.*)? gen_context(system_u:object_r:luanti_server_world_data_t)

#### [Installation of OpenRC service policy]

[.te] and [.fc] files defined above should be in the same directory.

`root `[`#`]`make -f /usr/share/selinux/strict/include/Makefile`

`root `[`#`]`semodule --install luanti-server`

`root `[`#`]`restorecon /usr/bin/minetestserver `

`root `[`#`]`restorecon -R /var/lib/minetest `

`root `[`#`]`restorecon -R /var/log/minetest `

#### [Removal of OpenRC service policy]

`root `[`#`]`semodule --remove luanti-server`

`root `[`#`]`restorecon /usr/bin/minetestserver `

`root `[`#`]`restorecon -R /var/lib/minetest `

`root `[`#`]`restorecon -R /var/log/minetest `

## [Troubleshooting]

### [The server is not running]

If the server is not running, the server status should be checked.

OpenRC:

`root `[`#`]`rc-service minetest-server status`

systemd:

`root `[`#`]`systemctl status minetest-server`

### [No sound]

If there is no sound in the client, set the necessary (depending on the system configuration) USE flags of the [[[media-libs/openal]](https://packages.gentoo.org/packages/media-libs/openal)[]] package and recompile it.

### [USE flags for] [media-libs/openal](https://packages.gentoo.org/packages/media-libs/openal) [[]] [Software implementation of the OpenAL 3D audio API]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`alsa`](https://packages.gentoo.org/useflags/alsa)               Add support for media-libs/alsa-lib (Advanced Linux Sound Architecture)
  [`coreaudio`](https://packages.gentoo.org/useflags/coreaudio)     Build the CoreAudio driver on Mac OS X systems
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`gui`](https://packages.gentoo.org/useflags/gui)                 Enable support for a graphical user interface
  [`jack`](https://packages.gentoo.org/useflags/jack)               Add support for the JACK Audio Connection Kit
  [`oss`](https://packages.gentoo.org/useflags/oss)                 Add support for OSS (Open Sound System)
  [`pipewire`](https://packages.gentoo.org/useflags/pipewire)       Enable support for the media-video/pipewire audio backend
  [`portaudio`](https://packages.gentoo.org/useflags/portaudio)     Add support for the crossplatform portaudio audio API
  [`pulseaudio`](https://packages.gentoo.org/useflags/pulseaudio)   Add sound server support via media-libs/libpulse (may be PulseAudio or PipeWire)
  [`sdl`](https://packages.gentoo.org/useflags/sdl)                 Add support for Simple Direct Layer (media library)
  [`sndio`](https://packages.gentoo.org/useflags/sndio)             Enable support for the media-sound/sndio backend
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-06 19:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose games-engines/minetest`

## [See also]

-   [Games](https://wiki.gentoo.org/wiki/Games "Games") --- a landing page for many of the games (especially open source variants) available in Gentoo\'s main ebuild repository.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://dev.luanti.org/setting-up-a-server/](https://dev.luanti.org/setting-up-a-server/)]]