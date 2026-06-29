This page contains [[changes](https://wiki.gentoo.org/index.php?title=X_without_Display_Manager&diff=1412872)] which are not marked for translation.

Traditionally, the X11 session is started by a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager"). However, when running a single-user system, display managers are not strictly necessary. This article describes how to start an X11 session without a display manager.

## Contents

-   [[1] [Starting X11 from console]](#Starting_X11_from_console)
    -   [[1.1] [Using startx]](#Using_startx)
    -   [[1.2] [Using a dedicated session runner]](#Using_a_dedicated_session_runner)
-   [[2] [Starting X11 automatically]](#Starting_X11_automatically)
    -   [[2.1] [Starting X11 on console login]](#Starting_X11_on_console_login)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [Multiple X sessions/Virtual consoles]](#Multiple_X_sessions.2FVirtual_consoles)
    -   [[2.3] [X11 autologin with systemd]](#X11_autologin_with_systemd)
        -   [[2.3.1] [Method 1]](#Method_1)
        -   [[2.3.2] [Method 2]](#Method_2)
    -   [[2.4] [Links]](#Links)
-   [[3] [Automatic user selection]](#Automatic_user_selection)
-   [[4] [Custom text in console logon]](#Custom_text_in_console_logon)

## [Starting X11 from console]

### [Using startx]

See the [Using startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide") section of the [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") article.

### [Using a dedicated session runner]

Some of the desktop environments provide their own replacements for [startx]. For example, Xfce4 provides [startxfce4]:

`user `[`$`]`startxfce4 -- vt7`

## [Starting X11 automatically]

### [Starting X11 on console login]

To avoid having to run *startx* after login, logging in to a specific vt may be configured to start X11 automatically. One of the ways to achieve this is to put code into the shell\'s login script (e.g. [\~/.bash_profile]):

** Important**\
The **GPU** could have not been yet initialized when *startx* is executed. An easy solution would be to add *sleep 5;* before *startx*.

#### [OpenRC]

[FILE] **`~/.bash_profile`X11 autostart with login on tty1**

    if shopt -q login_shell; then
        [[ -f ~/.bashrc ]] && source ~/.bashrc
        [[ -t 0 && $(tty) == /dev/tty1 && ! $DISPLAY ]] && exec startx
    else
        exit 1 # Somehow this is a non-bash or non-login shell.
    fi

#### [systemd]

[FILE] **`~/.bash_profile`X11 autostart with login on vt8**

    if [[ ! $ && $ == 8 ]]; then
        exec startx
    fi

The `XDG_VTNR` variable specifies the VT number. To use another VT adjust the number accordingly.

The additional `DISPLAY` check is necessary because the snippet will be executed on both graphical and non-graphical logins. Since `XDG_VTNR` will be set to the same value in the shells started within the X11 session (e.g. terminals), it is necessary to prevent them from trying to start X11.

The [exec] command causes the login shell to be replaced by the X11 session. This means that the user won\'t be able to use the shell used to start X11 anymore, and whenever the X11 session terminates, user will be logged back out. To remain logged in into vt, remove the [exec] word.

** Important**\
The `DISPLAY` check is fairly fragile. Make sure it isn\'t influenced by side-effects from earlier in the login process.

Ensure the user has permission to execute the [\~/.bash_profile] script:

`user `[`$`]`chmod u+x ~/.bash_profile`

### [][Multiple X sessions/Virtual consoles]

An alternate method is to auto-login to a Window Manager (WM) or a Desktop Environment (DE) depending on the Virtual Console (VT) used to login. A *fallback* session can be easily achieved in this manner. Just grab the following file excerpts to get going:

First, set up the sessions or WM or DE to use depending on the VT:

[FILE] **[`~/.xinitrc`](https://github.com/tokiclover/dotfiles/blob/master/.xinitrc)**

    # $Header: ~/.xinitrc, 2014/11/22 Exp $
    ...
    case $(tty | cut -b9-) in
        (1) exec enlightenment_start;;
        (2) exec lxsession          ;;
        (3) exec openbox-session    ;;
    esac

And then set up the login shell accordingly:

[FILE] **[`~/.bash_login`](https://github.com/tokiclover/dotfiles/blob/master/.bash_login)**

    # $Header: ~/.bash_login, 2014/11/30 Exp $
    ...
    # Auto startx depending on the VT
    if [[ -z "$DISPLAY" && $(id -u) -ge 1000 ]] ; then
        TTY=$(tty)
        [[ "$" != "$TTY" && "$" = "3" ]] &&
            startx 1>~/.log/xsession-errors 2>&1 &
        unset TTY
    fi
    ...

Or else, a [zsh](https://wiki.gentoo.org/wiki/Zsh "Zsh") variant could be used instead.

[FILE] **[`~/.zlogin`](https://github.com/tokiclover/dotfiles/blob/master/.zlogin)**

    # $Header: ~/.zlogin, 2014/11/30 Exp $
    ...
    # Auto startx depending on the tty
    if [[ -z $DISPLAY ]] && (( $EUID != 0 ))  != $TTY ]] && (( $ <= 3 )) &&
            startx 1>~/.log/xsession-errors 2>&1 &
    }
    ...

The previous files can be used to login into an [Enlightenment](https://wiki.gentoo.org/wiki/Enlightenment "Enlightenment") or [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE") session without needing any *middle man* or rather Display Manager (DM)! and [Openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox") session as a fallback session using VT 1, 2, and 3.

Adapt to preferred DE or WM.

### [X11 autologin with systemd]

#### [Method 1]

In order to obtain complete X11 autologin, it is possible to use the getty/login autologin feature along with the aforementioned trick.

First, create a new service file like the following:

[FILE] **`/etc/systemd/system/x11.service`An example service file for X11 autologin**

    [Unit]
    After=systemd-user-sessions.service

    [Service]
    ExecStart=/sbin/mingetty --autologin username --noclear tty8 38400

    [Install]
    WantedBy=multi-user.target

*username* replaced by the user\'s username, and *tty8* being the tty the X11-starting login to be performed on. It should be noted that this tty will be used for login and console output, and X11 can be started on any other tty.

** Note**\
This way can only be used for vt7+. Earlier vts are used by default getty generator and require a different kind of hackery.

Afterwards, add the previous snippet to bashrc (with the same vt specified), enable the service:

`root `[`#`]`systemctl enable x11.service`

In order to avoid relying on the *DISPLAY+XDG_VTNR* trick to determine whether to start X11, the two above approaches may be extended by using a dedicated environment variable to distinguish the specific shell where X11 is to be started.

First, create a dedicated *login* wrapper:

[FILE] **`/usr/local/sbin/x11login`X11 vt login wrapper**

    #!/bin/sh
    exec /bin/login "$" START_X11=1

This causes the user to be logged in with *START_X11=1* environment variable set. Then, tell getty to use that file instead of the default [/bin/login]:

[FILE] **`/etc/systemd/system/x11.service`X11 autologin service using login wrapper**

    [Unit]
    After=systemd-user-sessions.service

    [Service]
    ExecStart=/sbin/mingetty --autologin username --loginprog=/usr/local/sbin/x11login --noclear tty8 38400

    [Install]
    WantedBy=multi-user.target

Finally, modify [\~/.bashrc] (or equivalent) to use the variable rather than guessing:

[FILE] **`~/.bashrc`X11 autostart checking dedicated variable**

    if [[ $ == 1 ]]; then
        unset START_X11
        exec startx
    fi

Remember to unset the variable before starting X11 \-- otherwise all the X11 terminals would have it set and try to spawn another X11 session.

#### [Method 2]

An alternative method is to use [su] and [xinit] for direct login in X.

Service example:

[FILE] **`/etc/systemd/system/xinit-login.service`An example service file for X11 autologin using su and xinit**

    [Unit]
    After=systemd-user-sessions.service

    [Service]
    ExecStart=/bin/su username -l -c /usr/bin/xinit -- VT08

    [Install]
    WantedBy=multi-user.target

[startx] can be used rather than [xinit].

In case X startup fails with the error *Xorg.wrap: Only console users are allowed to run the X server* then read man Xorg.wrap how to allow any user to do so.

### [Links]

-   [http://mywiki.wooledge.org/DotFiles](http://mywiki.wooledge.org/DotFiles)

## [Automatic user selection]

On a 1-user system it\'s possible to avoid typing the username, so the login prompt will ask only for the password. E.g. adjust [/etc/inittab] so that the third terminal asks about the password only:

[FILE] **`/etc/inittab`Preselect user in TERMINALS section**

    c3:2345:respawn:/sbin/agetty --noclear --skip-login --login-options=my_user 38400 tty3 linux

Of course, one can have various preselected users on different terminals, e.g. user_a on tty1 and user_b on tty2.

## [Custom text in console logon]

It is possible to create a simple wrapper for [/bin/login] to show supplementary information on the console logon screen. E.g. on a 1-user system one may wish to see if there are any new emails without logging in. First, create a simple bash wrapper for [/bin/login]:

[FILE] **`/root/login.sh`Wrapper for /bin/login**

    #!/bin/bash

    # Show sender and subject of all new emails:
    egrep -r --max-count=2 '^(From|Subject|$):' ~email_user/.maildir/new

    # Show user count, terminal, time, kernel version:
    echo $(who -q) $(tty) $(date '+[%b-%-d %-H:%M]') $(uname -r)

    # Continue with normal login:
    exec /bin/login preselected_login_user

The last line calls the actual [/bin/login] which will do all the heavy lifting. Omit the user name in that line to be prompted for it. Passing a username results in being prompted about the password only.

Finally edit [/etc/inittab] to use [login.sh] wrapper, here on tty2:

[FILE] **`/etc/inittab`Use login.sh wrapper**

    c2:2345:respawn:/sbin/agetty --noclear --skip-login --login-program=/root/login.sh 38400 tty2 linux