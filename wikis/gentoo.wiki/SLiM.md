**Resources**

[[]][Home](https://slim-fork.sourceforge.io/)

[[]][Package information](https://packages.gentoo.org/packages/x11-misc/slim)

[[]][GitHub (up to v1.3.6)](https://github.com/iwamatsu/slim)

[[]][SourceForge (from v1.3.7)](https://sourceforge.net/projects/slim-fork/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/SLiM "wikipedia:SLiM")

** Note**\
The original SLiM project, from which versions up to 1.3.6 were obtained, was abandoned in 2013. Subsequent versions are from an actively maintained fork by a different author.

**SLiM** (**S**imple **L**og**i**n **M**anager) is a desktop-independent graphical [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager"). Being fast and having only a few dependencies, it is a popular choice among users of lightweight window managers such as [Openbox](https://wiki.gentoo.org/wiki/Openbox "Openbox").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
            -   [[2.2.1.1] [With display-manager]](#With_display-manager)
            -   [[2.2.1.2] [With the deprecated xdm init script]](#With_the_deprecated_xdm_init_script)
        -   [[2.2.2] [systemd]](#systemd)
    -   [[2.3] [Session selection]](#Session_selection)
        -   [[2.3.1] [Upstream-style configuration]](#Upstream-style_configuration)
        -   [[2.3.2] [Default configuration (Gentoo-style)]](#Default_configuration_.28Gentoo-style.29)
            -   [[2.3.2.1] [Setting a global default session]](#Setting_a_global_default_session)
            -   [[2.3.2.2] [Setting a default session for one user]](#Setting_a_default_session_for_one_user)
                -   [[2.3.2.2.1] [Per-user default session using bundled session files]](#Per-user_default_session_using_bundled_session_files)
                -   [[2.3.2.2.2] [Per-user default session using the customized \~/.xsession file]](#Per-user_default_session_using_the_customized_.7E.2F.xsession_file)
                -   [[2.3.2.2.3] [Per-user default session without using any default session files]](#Per-user_default_session_without_using_any_default_session_files)
    -   [[2.4] [More tweaks]](#More_tweaks)
        -   [[2.4.1] [Theme selection]](#Theme_selection)
        -   [[2.4.2] [NumLock state on login]](#NumLock_state_on_login)
        -   [[2.4.3] [Autologin]](#Autologin)
        -   [[2.4.4] [Unlock keyrings]](#Unlock_keyrings)
            -   [[2.4.4.1] [GNOME Keyring]](#GNOME_Keyring)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Failed to connect to socket /var/run/dbus/system_bus_socket]](#Failed_to_connect_to_socket_.2Fvar.2Frun.2Fdbus.2Fsystem_bus_socket)
    -   [[3.2] [SLiM starts but leaves a blank screen after login]](#SLiM_starts_but_leaves_a_blank_screen_after_login)
    -   [[3.3] [On fresh installs, slim starts but fails to load any sessions]](#On_fresh_installs.2C_slim_starts_but_fails_to_load_any_sessions)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [x11-misc/slim](https://packages.gentoo.org/packages/x11-misc/slim) [[]] [Simple Login Manager resurrected]

  ------------------------------------------------------------- ----------------------------------------------------------------------------------------
  [`branding`](https://packages.gentoo.org/useflags/branding)   Enable Gentoo specific branding
  [`pam`](https://packages.gentoo.org/useflags/pam)             Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  ------------------------------------------------------------- ----------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[x11-misc/slim]](https://packages.gentoo.org/packages/x11-misc/slim)[]]:

`root `[`#`]`emerge --ask x11-misc/slim`

** Note**\
Enable the `pam` USE flag for [[[x11-misc/slim]](https://packages.gentoo.org/packages/x11-misc/slim)[]] if the [slimlock] command is needed for locking the screen.

## [Configuration]

### [Files]

Most global configuration is done in the [/etc/slim.conf] file. However, this references several helper scripts which may contain further configuration.

### [Service]

#### [OpenRC]

##### [With display-manager]

Set SLiM as the default display manager:

[FILE] **`/etc/conf.d/display-manager`**

    DISPLAYMANAGER="slim"

To start SLiM on boot, add display-manager to the default runlevel:

`root `[`#`]`rc-update add display-manager default`

To start SLiM now:

`root `[`#`]`rc-service display-manager start`

##### [With the deprecated xdm init script]

Set SLiM as the default display manager:

[FILE] **`/etc/conf.d/xdm`**

    DISPLAYMANAGER="slim"

To start SLiM on boot, add xdm to the default runlevel:

`root `[`#`]`rc-update add xdm default`

To start SLiM now:

`root `[`#`]`/etc/init.d/xdm start`

#### [systemd]

To start SLiM on boot:

`root `[`#`]`systemctl enable slim`

To start SLiM now:

`root `[`#`]`systemctl start slim`

### [Session selection]

SLiM starts the user\'s preferred desktop session through a helper. There are several options for how this is done.

#### [Upstream-style configuration]

This method provides full flexibility per user, at the cost of requiring all users to have the helper script in their home directory.

Make the config section look like this:

[FILE] **`/etc/slim.conf`Modifying slim.conf**

    # login_cmd           exec /bin/sh - ~/.xinitrc %session
    login_cmd           exec /bin/bash -login ~/.xinitrc %session
    # login_cmd           exec /bin/bash -login /usr/share/slim/Xsession %session

Each user must setup a window manager of choice in their [\~/.xinitrc]. If the user chooses a different session from the login page, that will be passed as an argument to the script. If \$1 is empty it should run the user\'s default session.

#### [][Default configuration (Gentoo-style)]

** Note**\
In the following paragraphs [Awesome window manager](https://wiki.gentoo.org/wiki/Awesome "Awesome") is used as an example window manager.

By default, SLiM is configured to make all sessions in [/etc/X11/Sessions/] accessible --- they can be cycled through by pressing the [F1] key. This behavior is acquired by setting the options below:

[FILE] **`/etc/slim.conf`Editing session behavior**

    login_cmd            exec /bin/bash -login /usr/share/slim/Xsession %session
    ...
    sessiondir           /etc/X11/Sessions

If no changes are made to [/etc/X11/Sessions/] then users will need to press [F1] while logging-in to select the desired session.

In following sections several methods of setting one session as the default are described.

** Warning**\
Some window managers do not provide session file and therefore cannot be seen in [/etc/X11/Sessions/] by SLiM. In that case use the [second method](#Per-user_default_session_using_the_customized_.7E.2F.xsession_file) of setting a default session for one user (using a custom [\~/.xsession] file), because neither global nor \"per-user bundled session files\" methods will work. You may also want to file a bug, asking a developer to add a session file to the ebuild.

##### [Setting a global default session]

Set a default session for all users of the computer by modifying the `XSESSION` variable. To do this, create and edit file [/etc/env.d/90xsession] file. The example below sets the Awesome window manager as the default session.

[FILE] **`/etc/env.d/90xsession`**

    XSESSION="awesome"

After saving the file run [env-update]:

`root `[`#`]`env-update`

##### [Setting a default session for one user]

Besides (or instead of) setting *global default* sessions, it is possible to let each user choose a default session.

There are three approaches to accomplishing the task:

-   Use the SLiM session script ([/usr/share/slim/Xsession]) to trigger session script from [/etc/X11/Sessions/]
-   Use the SLiM session script to trigger user-created session script
-   Force users to set everything by themselves

The first and second possibilities are generally preferred. However, if for any reason you do not want to set any defaults, you may choose the third approach.

###### [Per-user default session using bundled session files]

The simplest way to set a default session for one user is to make a symbolic link from the session file to [\~/.xsession]

`user `[`$`]`ln -s /etc/X11/Sessions/awesome ~/.xsession`

An alternative is to put session command in the [\~/.xsession] file:

[FILE] **`~/.xsession`**

    /etc/X11/Sessions/awesome

You will only need to make sure the file is executable:

`user `[`$`]`chmod u+x ~/.xsession`

###### [][Per-user default session using the customized [\~/.xsession] file]

Sometimes you need to customize the launcher script, e.g. to run other programs before starting the window manager or to start a window manager with a customized command. The method above does not allow such modifications, but it can be achieved by using default session script (instead of the one provided by window manager) and launching WM through the [\~/.xsession] file.

To run your sessions this way, make sure you have no global default session set (or set it to `XSESSION="custom"` in [/etc/env.d/90xsession] like described above). Then edit the [\~/.xsession] file located in the user\'s home directory, putting the window manager launcher at the end.

The file may look like this:

[FILE] **`~/.xsession`**

    #!/bin/sh

    # Run urxvt daemon
    urxvtd -q -o -f
    # Set xserver parameters
    xset s 0
    xset dpms 0 0 1800
    # Launch awesome
    exec /usr/bin/awesome

** Tip**\
It might be helpful to look at the window manager session files in [/etc/X11/Sessions/] to find how things are done.

** Important**\
By default SLiM evaluates [/usr/share/slim/Xsession] first, then [/etc/X11/Sessions/Xsession], and [\~/.xsession] is called last, so there is no need to duplicate entries from that two previous files.

Finally, remember to make sure the file is executable:

`user `[`$`]`chmod u+x ~/.xsession`

###### [Per-user default session without using any default session files]

If you do not like **any** defaults from [/usr/share/slim/Xsession] and [/etc/X11/Sessions/Xsession], you can let your users set everything by themselves. It is generally not a good idea, but sometimes you may need it.

** Warning**\
You must be sure that **every** user will know what they are expected to do and that they will have enough knowledge to create [\~/.xinitrc] by themselves. For example, when configuring SLiM in this way, neither [.Xresources] nor [.Xkbmap] files are read by default and no errorfiles are created.

Start by editing [/etc/slim.conf] in the following way:

[FILE] **`/etc/slim.conf`**

    #login_cmd            exec /bin/bash -login /usr/share/slim/Xsession %session
    login_cmd           exec /bin/bash -login ~/.xinitrc %session
    ...
    #sessiondir           /etc/X11/Sessions
    sessions            awesome,i3

In the *sessions* line you may put the names of window managers you are planning to use.

Then create and edit [\~/.xinitrc] file, which may look as below:

[FILE] **`~/.xinitrc`**

    #!/bin/sh
    #
    # Custom xinitrc file for Gentoo

    DEFAULT_SESSION="awesome"

    # Redirect errors to a file in user's home directory if we can
    for errfile in "$HOME/.wm-errors" "$/wm-$USER" "/tmp/wm-$USER"
    do
        if ( cp /dev/null "$errfile" 2> /dev/null )
        then
            chmod 600 "$errfile"
            exec > "$errfile" 2>&1
            break
        fi
    done

    # Define Xresources
    userresources=$HOME/.Xresources

    # Merge what is available
    if [ -f "$userresources" ]; then
        xrdb -merge "$userresources"
    fi

    # Run urxvt daemon
    urxvtd -q -o -f
    # Set xserver parameters
    xset s 0
    xset dpms 0 0 1800

    # Start WM
    case $1 in
    awesome|i3)
            exec $1
            ;;
    *)
            exec $DEFAULT_SESSION
            ;;
    esac

Finally make sure the file is executable:

`user `[`$`]`chmod u+x ~/.xinitrc`

### [More tweaks]

#### [Theme selection]

** Note**\
You can install the package [[[x11-themes/slim-themes]](https://packages.gentoo.org/packages/x11-themes/slim-themes)[]] for having various nice-looking themes you can choose from.

Theme selection is done by changing the following line:

[FILE] **`/etc/slim.conf`**

    current_theme    slim-gentoo-simple

You can easily find what themes are available on your system:

`user `[`$`]`ls /usr/share/slim/themes/`

You can preview a theme by running the following command while Xorg is running:

`user `[`$`]`slim -p /usr/share/slim/themes/<theme name>`

#### [NumLock state on login]

The NumLock key can be turned on or off by default:

[FILE] **`/etc/slim.conf`**

    numlock    on

#### [Autologin]

Change `<USER>` in the example below to an appropriate user name:

[FILE] **`/etc/slim.conf`**

    default_user        <USER>
    auto_login          yes

#### [Unlock keyrings]

The following section will describe how to make SLiM automatically unlock different keychains automatically when you log in.

##### [GNOME Keyring]

First make sure you have [[[gnome-base/gnome-keyring]](https://packages.gentoo.org/packages/gnome-base/gnome-keyring)[]] (include [[[app-crypt/seahorse]](https://packages.gentoo.org/packages/app-crypt/seahorse)[]] if you want a GUI). To configure SLiM to unlock your GNOME Keyring automatically you have to edit its PAM configuration file. To do so open [/etc/pam.d/slim] and modify it to look similar to the text below. Lines ending with comment `#keyring` should be added.

[FILE] **`/etc/pam.d/slim`**

    auth    include     system-local-login
    auth  optional  pam_gnome_keyring.so #keyring
    account include     system-local-login
    session include     system-local-login
    session optional    pam_gnome_keyring.so auto_start #keyring

Once this change has been made your keyring should be automatically unlocked next time you log in.

## [Troubleshooting]

### [][Failed to connect to socket [/var/run/dbus/system_bus_socket]]

This error is caused when [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") hasn\'t been started. It is possible that it wasn\'t added to the default run level. To fix this type the following:

`root `[`#`]`rc-update add dbus default`

This will ensure that D-Bus is running when you boot up your computer. It may be that this has already been added by other window manager, but I had to do this when using awesome WM.

### [SLiM starts but leaves a blank screen after login]

This error is caused when SLiM is built with the `elogind` USE flag, and required alongside

`root `[`#`]`rc-update add xdm default`

the use of

`root `[`#`]`rc-update add elogind default`

### [][On fresh installs, slim starts but fails to load any sessions]

In this error, slim will start and be responsive (you can type the username for example) but after the login no sessions will be loaded and you will get a blank screen. Pressing F1 to change the session will result in nothing. This can occur when dbus is not being loaded when the system starts. To add dbus to the default runlevel, use:

`root `[`#`]`rc-update add dbus default`

## [See also]

-   [SDDM](https://wiki.gentoo.org/wiki/SDDM "SDDM") --- a modern [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") that supports both the [X server](https://wiki.gentoo.org/wiki/X_server "X server") and the [Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland") protocol.
-   [LightDM](https://wiki.gentoo.org/wiki/LightDM "LightDM") --- a cross-desktop [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") whose aim is to be the standard display manager for the X server.