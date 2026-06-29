**Resources**

[[]][Home](https://rakshasa.github.io/rtorrent/)

[[]][Package information](https://packages.gentoo.org/packages/net-p2p/rtorrent)

[[]][Wikipedia](https://en.wikipedia.org/wiki/RTorrent "wikipedia:RTorrent")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/rtorrent)

[[]][GitHub](https://github.com/rakshasa/rtorrent)

**rTorrent** is a highly configurable [BitTorrent](https://wiki.gentoo.org/wiki/BitTorrent "BitTorrent") client based on libtorrent and ncurses.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Basics]](#Basics)
    -   [[2.2] [Watching a directory]](#Watching_a_directory)
    -   [[2.3] [Ratio handling]](#Ratio_handling)
-   [[3] [Adding a self-signed certificate]](#Adding_a_self-signed_certificate)
-   [[4] [Customizing the daemonizer]](#Customizing_the_daemonizer)
    -   [[4.1] [Using openrc (default, built-in daemon)]](#Using_openrc_.28default.2C_built-in_daemon.29)
    -   [[4.2] [Using openrc with dtach as daemonizer]](#Using_openrc_with_dtach_as_daemonizer)
        -   [[4.2.1] [Arrow keys not working]](#Arrow_keys_not_working)
            -   [[4.2.1.1] [Any terminal]](#Any_terminal)
            -   [[4.2.1.2] [Konsole]](#Konsole)
            -   [[4.2.1.3] [XTerm]](#XTerm)
        -   [[4.2.2] [Localization]](#Localization)
        -   [[4.2.3] [Modifying scheduling priority]](#Modifying_scheduling_priority)
        -   [[4.2.4] [Controlling rTorrent exit]](#Controlling_rTorrent_exit)
-   [[5] [Make rTorrent default application for magnet links]](#Make_rTorrent_default_application_for_magnet_links)
-   [[6] [XMLRPC]](#XMLRPC)

## [Installation]

### [USE flags]

### [USE flags for] [net-p2p/rtorrent](https://packages.gentoo.org/packages/net-p2p/rtorrent) [[]] [BitTorrent Client using libtorrent]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)         Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`lua`](https://packages.gentoo.org/useflags/lua)             Enable Lua scripting support
  [`selinux`](https://packages.gentoo.org/useflags/selinux)     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)     Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tinyxml2`](https://packages.gentoo.org/useflags/tinyxml2)   Use vendor tinyxml2 instead of xmlrpc-c. This allows significant reduction in overhead
  [`xmlrpc`](https://packages.gentoo.org/useflags/xmlrpc)       Support for xml-rpc library
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-09 15:37] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[net-p2p/rtorrent]](https://packages.gentoo.org/packages/net-p2p/rtorrent)[]]:

`root `[`#`]`emerge --ask net-p2p/rtorrent`

## [Configuration]

`user `[`$`]`curl -Ls "`[`https://raw.githubusercontent.com/wiki/rakshasa/rtorrent/CONFIG-Template.md`](https://raw.githubusercontent.com/wiki/rakshasa/rtorrent/CONFIG-Template.md)`" \`

        | grep -A9999 '^######' | grep -B9999 '^### END' \
        | sed -re "s:/home/USERNAME:$HOME:" >~/.rtorrent.rc

`user `[`$`]`mkdir ~/rtorrent`

The rTorrent configuration is stored in the user\'s [\~/.rtorrent.rc]. A lot can be configured, for this reason, the configuration is divided in sections.

Any configuration should start with using the modernized rTorrent wiki config template. The configuration is loaded from the file [\~/.rtorrent.rc] by default (that is the hidden file [.rtorrent.rc] in your user home directory). This configuration uses *0.9.x* syntax and is tested using *0.9.6*.

[FILE] **`/home/larry/.rtorrent.rc`**

    # Instance layout (base paths)
    method.insert = cfg.basedir, private|const|string, (cat,"/home/larry/rtorrent/")
    method.insert = cfg.watch,   private|const|string, (cat,(cfg.basedir),"watch/")
    method.insert = cfg.logs,    private|const|string, (cat,(cfg.basedir),"log/")
    method.insert = cfg.logfile, private|const|string, (cat,(cfg.logs),"rtorrent-",(system.time),".log")

    # Create instance directories
    execute.throw = bash, -c, (cat,\
        "builtin cd \"", (cfg.basedir), "\" ",\
        "&& mkdir -p .session download log watch/")

    # Listening port for incoming peer traffic (fixed; you can also randomize it)
    network.port_range.set = 50000-50000
    network.port_random.set = no

    # Peer settings
    throttle.max_uploads.set = 100
    throttle.max_uploads.global.set = 250

    throttle.min_peers.normal.set = 20
    throttle.max_peers.normal.set = 60
    throttle.min_peers.seed.set = 30
    throttle.max_peers.seed.set = 80
    trackers.numwant.set = 80

    protocol.encryption.set = allow_incoming,try_outgoing,enable_retry

    # Limits for file handle resources, this is optimized for
    # an `ulimit` of 1024 (a common default). You MUST leave
    # a ceiling of handles reserved for rTorrent's internal needs!
    network.http.max_open.set = 50
    network.max_open_files.set = 600
    network.max_open_sockets.set = 300

    # Memory resource usage (increase if you have a large number of items loaded,
    # and/or the available resources to spend)
    pieces.memory.max.set = 1800M
    network.xmlrpc.size_limit.set = 4M

    # Basic operational settings (no need to change these)
    session.path.set = (cat, (cfg.basedir), ".session")
    directory.default.set = (cat, (cfg.basedir), "download/")
    log.execute = (cat, (cfg.logs), "execute.log")
    ##log.xmlrpc = (cat, (cfg.logs), "xmlrpc.log")
    execute.nothrow = bash, -c, (cat, "echo >",\
        (session.path), "rtorrent.pid", " ", (system.pid))

    # Other operational settings (check & adapt)
    encoding.add = utf8
    system.umask.set = 0027
    system.cwd.set = (directory.default)
    network.http.dns_cache_timeout.set = 25
    ##network.http.capath.set = "/etc/ssl/certs"
    ##network.http.ssl_verify_peer.set = 0
    ##network.http.ssl_verify_host.set = 0
    ##pieces.hash.on_completion.set = no
    ##keys.layout.set = qwerty

    ##view.sort_current = seeding, greater=d.ratio=
    schedule2 = monitor_diskspace, 15, 60, ((close_low_diskspace, 1000M))

    # Some additional values and commands
    method.insert = system.startup_time, value

And here is a simple start script that you should use before you tackle auto-starting rTorrent at boot time. First make it work for you, then add the bells and whistles. Copy the script to [\~/rtorrent/start], and make it executable using:

`user `[`$`]`chmod a+x ~/rtorrent/start`

[FILE] **`~/rtorrent/start`**

    #! /bin/bash
    #
    # rTorrent startup script
    #
    umask 0027
    cd $(dirname "$0")

    # Check for running process
    export RT_SOCKET=$PWD/.scgi_local
    test -S $RT_SOCKET && lsof $RT_SOCKET >/dev/null \
        &&
    test ! -e $RT_SOCKET || rm $RT_SOCKET

    # Clean up after rTorrent ends
    _at_exit()
    trap _at_exit INT TERM EXIT

    # Start rTorrent (optionally with configuration loaded
    # from the directory this script is stored in)
    rtorrent -D -I  # -n -o import=$PWD/rtorrent.rc

You can call it in a simple shell prompt first, but for normal operation it must be launched in a [tmux](https://wiki.gentoo.org/wiki/Tmux "Tmux") session, like so:

`user `[`$`]`tmux -2u new -n rTorrent -s rtorrent "~/rtorrent/start; exec bash"`

The [exec bash] keeps your tmux window open if rTorrent exits, which allows you to actually read any error messages in case it exited unexpectedly.

You can of course add more elaborate start scripts, like a [cron](https://wiki.gentoo.org/wiki/Cron "Cron") watchdog, init.d scripts, or [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") units, see the rTorrent wiki for examples.

### [Basics]

These options are pretty straightforward:

[FILE] **`/home/larry/.rtorrent.rc`**

    # Global upload and download rate in KiB. "0" for unlimited.
    #throttle.global_down.max_rate.set_kb = 0
    throttle.global_up.max_rate.set_kb = 75

    # Default directory to save the downloaded torrents.
    directory.default.set = /home/larry/media/

    # Default session directory. When restarting rtorrent, the torrents from this directory will be restarted.
    session.path.set = /home/wim/media/session

### [Watching a directory]

You can configure rTorrent to watch one or more directories for new torrent files and queue them automatically. You can also set a download directory for each watch directory (rather than downloading to the default download directory).

[FILE] **`/home/larry/.rtorrent.rc`**

    # A watch directory downloading to the default location
    schedule2 = watch_directory_3,5,300,load.start=/home/larry/media/watch/*.torrent

    # Watch directories with customized download directories
    schedule2 = watch_directory_1,5,60,"load.start=/home/larry/media/watch_series/*.torrent,d.directory.set=/home/larry/media/series"
    schedule2 = watch_directory_2,5,5,"load.start=/home/larry/media/watch_music/*.torrent,d.directory.set=/home/larry/media/music"
    schedule2 = watch_directory_3,5,300,"load.start=/home/larry/media/watch_movies/*.torrent,d.directory.set=/home/larry/media/movies"

    # Restart torrents that have been copied back and stop those that have been deleted
    schedule2 = tied_directory,1,30,start_tied=
    schedule2 = untied_directory,1,30,close_untied=

    # Close torrents when diskspace is low.
    schedule2 = low_diskspace,5,60,close_low_diskspace=100M

** Note**\
Several commands can be scheduled to run depending on two values, *start* and *interval*. The command in question is called every interval, beginning at start. The values can be seconds or a time format.

[FILE] **`/home/larry/.rtorrent.rc`**

    # Execute command after 5 seconds and again every 5 minutes
    schedule2 = some_command,5,300,foo

    # Execute command immediately and at 03:00
    schedule2 = some_command,0,03:00,foo
    default

### [Ratio handling]

You can control seed time by making it dependent on each torrent\'s ratio. Each torrent is seeded for a minimum of `min.set` percent. if a total of `upload.set` has been uploaded. If `upload.set` is not reached, it will seed a maximum of `max.set` percent. Read the [wiki](https://github.com/rakshasa/rtorrent/wiki/RTorrentRatioHandling) on the GitHub site for different ratio groups.

[FILE] **`/home/larry/.rtorrent.rc`**

    # First, enable the default ratio group, which controls all loaded torrents. Set the limits for the group next.
    group.seeding.ratio.enable=
    group2.seeding.ratio.min.set=200
    group2.seeding.ratio.max.set=300
    group2.seeding.ratio.upload.set=20M

## [Adding a self-signed certificate]

Some trackers use SSL certificates, however most are not signed for various reasons. rTorrent uses the database located in [/etc/ssl/certs/ca-certificates.crt]. You also may want to use HTTPS because some ISPs (like Comcast) perform bandwidth shaping, effectively slowing down BitTorrent (regardless of whether your use is legitimate).

Add a certificate (if the domain was *mytracker.net* and the port was *443*):

`root `[`#`]`openssl s_client -connect mytracker.net:443 </dev/null 2>/dev/null | sed -n '/BEGIN CERTIFICATE/,/END CERTIFICATE/p' >> /etc/ssl/certs/ca-certificates.crt`

You need to re-hash after adding a certificate:

`root `[`#`]`c_rehash`

Try with [curl]:

`user `[`$`]`curl `[`https://mytracker.net:443`](https://mytracker.net:443)

You should not get a warning regarding the self-signed certificate.

Restart rTorrent. If using the daemon:

`root `[`#`]`rc-service rtorrent restart`

## [Customizing the daemonizer]

The Gentoo ebuild installs a good basic init script for both [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") and [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd"). However, it can be enhanced in various ways if needed. The following examples are completely optional.

### [][Using openrc (default, built-in daemon)]

This uses the built-in daemon mode, disabling the user interface. You can only control it via [XML-RPC](#XMLRPC).

Change the `USER` variable to the current user account, or (better) a separate account:

[FILE] **`/etc/conf.d/rtorrent`**

    #USER="$USER"
    USER="p2p"

Starting rTorrent in the background, and run at system boot:

`root `[`#`]`rc-service rtorrent start `

`root `[`#`]`rc-update add rtorrent default `

### [Using openrc with dtach as daemonizer]

It is also possible to work in the user interface, and use an external daemonizer like [screen]. A smaller alternative to the [[[app-misc/screen]](https://packages.gentoo.org/packages/app-misc/screen)[]] package is [[[app-misc/dtach]](https://packages.gentoo.org/packages/app-misc/dtach)[]]. This is all what\'s needed for using [dtach] instead of the built-in daemon.

Save next two files to the system:

[FILE] **`/etc/init.d/rtorrentd`**

    #!/sbin/openrc-run
    # Copyright 1999-2024 Gentoo Authors
    # Distributed under the terms of the GNU General Public License v2

    description="rTorrent BitTorrent client over dtach"

    PWHOME="$(getent passwd $USER | awk -F ':' '')"
    dtach_tmpfile="$(mktemp -u /tmp/rtorrentd.XXXXXXXXXX)"
    rtorrent_command="/usr/bin/rtorrent"

    description_attach="Attaches to the session (interactive console) of the rTorrent client"
    extra_started_commands="attach"

    start_stop_daemon_args="--env HOME=$ --env LANG=$ --env TERM=$"
    command="/usr/bin/dtach"
    command_args="-n $ $ $"
    command_user="$USER"
    ##command_user="$USER:$GROUP"
    pidfile="/run/rtorrentd.pid"
    ## Graceful exit:
    #retry="-INT/15/-INT/5/-KILL/5"

    depend()


    start_post()
     | awk '')"
       pgrep -P $ 1>$ 2>/dev/null || return 1

       ## Modifying scheduling priority:
       #renice -n 5 $(cat $) >/dev/null
       ## and/or
       #ionice -c 3 -p $(cat $)

       ## Group access to the rTorrent session:
       #chmod g+rw $

       return 0
    }

    stop_pre()
    ) -o comm=)" = "rtorrent main" || rm -f $
    }

    attach()
    ) -o ppid= | awk '')"
       dtach_tmpfile="$(cat /proc/$/cmdline | awk -F '\000' '')"

       if [ -S "$" ]; then
          if [ "$" = "yes" ]; then
             tput smkx ; eval "$" -a "$" "$" ; tput rmkx
          else
             eval "$" -a "$" "$"
          fi
       else
          eerror "The determined socket file for dtach could not be found!"
          eerror "Did the process crash?"
       fi
    }

Change the `USER` variable to the current user account, or (better) a separate account:

[FILE] **`/etc/conf.d/rtorrentd`**

    #USER="$USER"
    USER="p2p"
    ##GROUP="$GROUP"
    LANG="$LANG"

    TERM="xterm"
    #ENABLE_ARROWS="yes"

    RTORRENT_OPTS=""
    DTACH_OPTS=""

`root `[`#`]`chmod +x /etc/init.d/rtorrentd `

`root `[`#`]`emerge -av app-misc/dtach `

If needed, give access to group members of the configured user. Add this at the end of the `start_post()` section of the init script:

[FILE] **`/etc/init.d/rtorrentd`**

    chmod g+rw $

Starting *rTorrent* in the background, and run at system boot:

`root `[`#`]`rc-service rtorrentd start `

`root `[`#`]`rc-update add rtorrentd default `

Login as user, or execute as a group member to attach the *rtorrentd* session:

`user `[`$`]`su - p2p `

`user `[`$`]`dtach -a /tmp/rtorrentd.* `

To detach the *rtorrentd* session again: press [Ctrl]+[\\] on the keyboard.

If the arrow keys don\'t work, enter this in one go instead:

`user `[`$`]`tput smkx; dtach -a /tmp/rtorrentd.*; tput rmkx `

It is easier to use the `attach` function of the init script instead:

`user `[`$`]`rc-service rtorrentd attach `

It has a configuration option to enable the arrow keys:

[FILE] **`/etc/conf.d/rtorrentd`**

    ENABLE_ARROWS="yes"

When the arrow keys still don\'t work, [start reading here](#Arrow_keys_not_working).

#### [Arrow keys not working]

First check the value of the `TERM` variable the terminal application uses, and set it in the config file.

`user `[`$`]`echo $TERM`

Changing the `TERM` variable:

[FILE] **`/etc/conf.d/rtorrentd`**

    #TERM="xterm"
    TERM="linux"

`root `[`#`]`rc-service rtorrentd restart`

If the arrow keys still do not work, try setting the `TERM` value to `linux`, even if the terminal application uses `xterm`. Although this setting is wrong, it doesn\'t seem to matter that much currently. However, it\'s preferred to enable the arrow keys in the terminal application instead.

It is [a known limitation of *dtach*](http://sourceforge.net/p/dtach/bugs/7/) (and [screen]?), that reattaching the session in another terminal, drops the working arrow keys.

##### [Any terminal]

Enter \"keyboard transmit mode\" and leave \"keyboard transmit mode\", using [tput]:

`user `[`$`]`tput smkx `

`user `[`$`]`<Here your command to reattach the `*`rTorrent`*` session> `

`user `[`$`]`tput rmkx `

##### [Konsole]

If [Konsole](https://wiki.gentoo.org/wiki/Konsole "Konsole") doesn\'t switch to \"Application Cursor Mode\", you can create custom key bindings. To create the [.keytab] file with hacked bindings:

`user `[`$`]`sed 's:^\(keyboard.*\)\":\1 +AppCuKeys\":;s:E\[\([ABCDFH]\):EO\1:' /usr/share/konsole/default.keytab > ~/.local/share/konsole/default+AppCuKeys.keytab `

Restart *Konsole*, and create a new profile with the key bindings named \"Default (XFree 4) +AppCuKeys\". If you set `TERM="linux"` in your init script, choose \"Linux console\" key bindings instead. Select this profile, when you reattached the *rtorrentd* session as a user.

##### [XTerm]

[XTerm](https://wiki.gentoo.org/wiki/XTerm "XTerm") has \"Enable Application Cursor Keys\" in the toolbar, and you can set it by default in [\~/.Xresources]:

[FILE] **`~/.Xresources`**

    XTerm*vt100.appcursorDefault: true

`user `[`$`]`xrdb -merge ~/.Xresources`

If there\'s no toolbar, rebuild *XTerm*:

`root `[`#`]`USE="toolbar" emerge -av x11-terms/xterm`

#### [Localization]

Environment variable, if you set `LANG` in your users [\~/.bashrc] file. This doesn\'t affect translations, but only character set and sorting.

[FILE] **`/etc/conf.d/rtorrentd`**

    #LANG="$LANG"
    LANG="nl_NL@euro"

#### [Modifying scheduling priority]

If hashing operations appear a bit heavy, try adding this in the `start_post()` section of the init script:

[FILE] **`/etc/init.d/rtorrentd`**

    renice -n 5 $(cat $) >/dev/null
    # and/or
    ionice -c 3 -p $(cat $)

#### [Controlling rTorrent exit]

By default, the application is closed by the TERM signal. A more graceful exit would be to issue the INT signal, which is equivalent to the [Ctrl]+[q] key press in the rTorrent interface. This way, seeding quota get a last chance to be reported to the tracker. A second [Ctrl]+[q] key press is TERM exit, without waiting for the trackers to respond. After that, a KILL signal is justified.

Changing exit signals, and 1 or more seconds waiting time:

[FILE] **`/etc/init.d/rtorrentd`**

    retry="-INT/15/-INT/5/-KILL/5"

## [Make rTorrent default application for magnet links]

Add protocol handler under \"Added Associations\" section:

[FILE] **`~/.config/mimeapps.list`**

    [Added Associations]
    x-scheme-handler/magnet=rtorrent.desktop;

Now create rTorrent shortcut:

[FILE] **`~/.local/share/applications/rtorrent.desktop`**

    [Desktop Entry]
    Type=Application
    Name=rtorrent
    Exec=urxvtc -name rtorrent -e rtorrent %U
    MimeType=x-scheme-handler/magnet;
    NoDisplay=true

## [XMLRPC]

Configure rtorrent with the [\--with-xmlrpc-c] flag and add the following to:

[FILE] **`/etc/lighttpd.conf`**

    scgi_local = /home/larry/rtorrent/rpc.socket
    server.modules += ( "mod_scgi" )
    scgi.server = (
                    "/RPC2" =>
                      ( "127.0.0.1" =>
                        (
                          "socket" => "/home/user/rtorrent/rpc.socket",
                          "check-local" => "disable",
                          "disable-time" => 0,
                        )
                      )
                  )

The web server will now route xmlrpc requests to rtorrent, which is listening only on connections from the local machine or on the local socket file. Also make sure the /RPC2 location is properly protected.

To make it accessible from anywhere, use **scgi_port = :5000**. This is however not recommend as rtorrent has no access control, which means the http server is responsible for handling that. Anyone who can send rtorrent xmlrpc commands is likely to have the ability to execute code with the privileges of the user running rtorrent.

You may also use **scgi_local = /foo/bar** to create a local domain socket, which supports file permissions. Set the rw permissions of the directory the socket will reside in to only allow the necessary processes. This is the recommended way of using XMLRPC with rtorrent, though not all http servers support local domain sockets for scgi.

If any of your downloads have non-ascii characters in the filenames, you must also set the following in .rtorrent.rc to force rtorrent to use the UTF-8 encoding. The XMLRPC standard requires UTF-8 replies, and rtorrent presently has no facilities to convert between encodings so it might generate invalid replies otherwise.

[FILE] **`/home/larry/.rtorrent.rc`UTF-8 Encoding**

    encoding_list = UTF-8