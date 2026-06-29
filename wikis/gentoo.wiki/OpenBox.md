This page contains [[changes](https://wiki.gentoo.org/index.php?title=Openbox&diff=1441455)] which are not marked for translation.

\

**Resources**

[[]][Home](http://openbox.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/openbox)

[[]][Guide](https://wiki.gentoo.org/wiki/Openbox/Guide "Openbox/Guide")

[[]][Wikipedia](https://en.wikipedia.org/wiki/Openbox "wikipedia:Openbox")

[[]][GitHub](https://github.com/danakj/openbox)

**Openbox** is a highly configurable stacking [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11") with extensive standards support. It was originally forked from [Blackbox](https://wiki.gentoo.org/wiki/Blackbox "Blackbox"). It is used by the [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE") as its default window manager and [KDE](https://wiki.gentoo.org/wiki/KDE "KDE") can also use Openbox as its window manager instead of its default window manager, KWin.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Starting]](#Starting)
    -   [[2.2] [autostart]](#autostart)
    -   [[2.3] [environment]](#environment)
    -   [[2.4] [menu.xml]](#menu.xml)
        -   [[2.4.1] [Dynamic generation]](#Dynamic_generation)
            -   [[2.4.1.1] [openbox-menu]](#openbox-menu)
            -   [[2.4.1.2] [obmenu-generator]](#obmenu-generator)
            -   [[2.4.1.3] [MenuMaker]](#MenuMaker)
        -   [[2.4.2] [Manual configuration]](#Manual_configuration)
    -   [[2.5] [rc.xml]](#rc.xml)
        -   [[2.5.1] [Key binding examples]](#Key_binding_examples)
-   [[3] [Tips]](#Tips)
    -   [[3.1] [Icons in the Openbox menu]](#Icons_in_the_Openbox_menu)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [x11-wm/openbox](https://packages.gentoo.org/packages/x11-wm/openbox) [[]] [Standards compliant, fast, light-weight, extensible window manager]

  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`branding`](https://packages.gentoo.org/useflags/branding)                           Enable Gentoo specific branding
  [`debug`](https://packages.gentoo.org/useflags/debug)                                 Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`imlib`](https://packages.gentoo.org/useflags/imlib)                                 Add support for imlib, an image loading and rendering library
  [`nls`](https://packages.gentoo.org/useflags/nls)                                     Add Native Language Support (using gettext - GNU locale utilities)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                             !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`session`](https://packages.gentoo.org/useflags/session)                             Enables support for session managers
  [`startup-notification`](https://packages.gentoo.org/useflags/startup-notification)   Enable application startup event feedback mechanism
  [`svg`](https://packages.gentoo.org/useflags/svg)                                     Add support for SVG (Scalable Vector Graphics)
  [`xdg`](https://packages.gentoo.org/useflags/xdg)                                     Install the python xdg files for xdg autostart
  ------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 23:41] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Emerge Openbox:

`root `[`#`]`emerge --ask x11-wm/openbox`

## [Configuration]

There are four configuration files:

-   [[autostart](https://wiki.gentoo.org/wiki/Openbox#autostart "Openbox")]
-   [[environment](https://wiki.gentoo.org/wiki/Openbox#environment "Openbox")]
-   [[menu.xml](https://wiki.gentoo.org/wiki/Openbox#menu.xml "Openbox")]
-   [[rc.xml](https://wiki.gentoo.org/wiki/Openbox#rc.xml "Openbox")]

[/etc/xdg/openbox/] contains the system-wide default version of these files. [\~/.config/openbox/] is used to store the user-specific custom version of these files, though it needs to be created and populated.

For example:

`user `[`$`]`mkdir -p ~/.config/openbox/ `

`user `[`$`]`cp /etc/xdg/openbox/* ~/.config/openbox/ `

`user `[`$`]`vim ~/.config/openbox/autostart`

### [Starting]

To start Openbox it is possible to use a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or the [startx] command.

To use [startx], set the `XSESSION` variable your shell to `openbox`, for example:

[FILE] **`~/.bashrc`Openbox with startx**

    # ...other .bashrc content...
    export XSESSION=openbox

Note that there are an infinite number of ways of achieving the above and this example only applies to bash for users using [\~/.bashrc] and those who wish to start X manually from the command line.

Also note that a common misconception is to create a [\~/.xinitrc] file - please do not do that, as it will prevent X from executing all the automatically provided scripts in [/etc/X11/xinit/xinitrc.d/] - if you wish to add anything in particular, you can create an executable file in that directory.

** Important**\
A shell-agnostic alternative is to set the XSESSION variable under [/etc/env.d/]. Please see the [Using startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide") section of the [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") article for further details.

### [autostart]

The [autostart] script is the place to execute specific commands and programs when Openbox starts. It makes no difference if Openbox is started using the [startx] command or a display manager, [autostart] will be executed either way.

[FILE] **`~/.config/openbox/autostart`Openbox autostart example**

    # Sets the wallpaper to an image of choice.
    wallpaper="planet.jpeg"

    # Sets the DESKTOP_ENV variable to "OPENBOX"
    DESKTOP_ENV="OPENBOX"

    # The following are examples on how to call programs;
    # unless programs are called in a daemon mode like the
    # conky example below an ampersand (&) will need to be included
    # in order to start the command and fork it to the background
    # See job control for more information.
    conky --daemonize

    # Waits one second then starts the NetworkManager applet.
    sleep 1 && nm-applet --sm-disable &

    # Starts a light-weight X11 desktop panel.
    fbpanel &

    # Starts a lightweight image viewer to display the wallpaper.
    feh --bg-scale ~/Artwork/$ &

    # Starts a simple battery monitor for the system tray.
    batti &

    # Starts a program that turns on numlock in X (after the X server starts).
    numlockx &

### [environment]

The [environment] script is the place to export global variables and configure the Openbox environment.

[FILE] **`~/.config/openbox/environment`Openbox environment example**

    eval $(gpg-agent --daemon)
    eval $(gnome-keyring-daemon)
    if which dbus-launch >/dev/null && test -z "$DBUS_SESSION_BUS_ADDRESS"; then
           eval `dbus-launch --sh-syntax --exit-with-session`
    fi
    LANG="el_GR.UTF8"

### [menu.xml]

The [menu.xml] file defines the right-click Openbox menus. By default the right-click menu is predefined with some common applications, so unless the applications are installed on the system most of the default links on the menu will not be operational.

#### [Dynamic generation]

##### [openbox-menu]

[openbox-menu] can dynamically generate new Openbox right-click menus based off information defined in the [/etc/xdg/menus/] directory.

Install [[[x11-misc/openbox-menu]](https://packages.gentoo.org/packages/x11-misc/openbox-menu)[]]:

`root `[`#`]`emerge --ask x11-misc/openbox-menu`

To create a new menu for the present user:

`user `[`$`]`openbox-menu`

##### [obmenu-generator]

[obmenu-generator] can generate either static or dynamic (pipe) menus based on a user-modifiable schema and the .desktop files installed by most applications. It supports themed icons and arbitrarily nested submenus.

[http://trizenx.blogspot.co.uk/2012/02/obmenu-generator.html](http://trizenx.blogspot.co.uk/2012/02/obmenu-generator.html)

[https://github.com/trizen/obmenu-generator](https://github.com/trizen/obmenu-generator)

Install [[[x11-misc/obmenu-generator]](https://packages.gentoo.org/packages/x11-misc/obmenu-generator)[]]:

`root `[`#`]`emerge --ask x11-misc/obmenu-generator`

To generate a static menu with icons:

`user `[`$`]`obmenu-generator -i -s`

To generate a pipe menu with icons:

`user `[`$`]`obmenu-generator -i -p`

Add \'-c\' to automatically reconfigure a running instance of Openbox:

`user `[`$`]`obmenu-generator -i -s -c`

##### [MenuMaker]

[maker] can automatically configure your menu, and also works with JWM, IceWM, BlackBox, FluxBox, PekWM and others.

Install [[[x11-misc/menumaker]](https://packages.gentoo.org/packages/x11-misc/menumaker)[]]:

`root `[`#`]`emerge --ask x11-misc/menumaker`

To generate a static menu for OpenBox with sakura terminal:

`user `[`$`]`mmaker -vf OpenBox -t Sakura`

If no terminal is specified, xtem will be used by default. You can check the availiable terminal emulators, terminals and otehr options by running:

`user `[`$`]`mmaker --help`

#### [Manual configuration]

[FILE] **`~/.config/openbox/menu.xml`Openbox menu.xml example**

    <?xml version="1.0" encoding="UTF-8"?>
    <openbox_menu>
        <menu id="root-menu" label="OpenBox 3">
            <menu id="2" label="Editors">
                <item label="Mousepad"> <action name="Execute">
                    <execute>mousepad</execute>
                </action> </item>
                <item label="Xournal"> <action name="Execute">
                    <execute>xournal</execute>
                </action> </item>
            </menu>
            <menu id="18" label="Games">
                <item label="Nibbles"> <action name="Execute">
                    <execute>gnome-nibbles</execute>
                </action> </item>
                <item label="DeSmuME (Gtk)"> <action name="Execute">
                    <execute>desmume</execute>
                </action> </item>
            </menu>
            <menu id="5" label="Network">
                <item label="FireFox"> <action name="Execute">
                    <execute>firefox</execute>
                </action> </item>
            </menu>
            <menu id="19" label="File Managers">
                <item label="File Manager PCManFM"> <action name="Execute">
                    <execute>pcmanfm</execute>
                </action> </item>
            </menu>
            <separator/>
            <menu id="40" label="OpenBox">
                <menu id="client-list-menu"/>
                <item label="Reconfigure"> <action name="Reconfigure"/> </item>
                <separator/>
                <item label="Exit"> <action name="Exit"/> </item>
            </menu>
        </menu>
    </openbox_menu>

In this example shown is a couple of applications in different categories. Each submenu goes inside the root `<menu>` which must go inside the `<openbox_menu>` tag. Specify a name for the subcategory to be displayed with the label \"attribute\", also specify an `"id"` for each submenu inside the main menu tag, which must be unique, but can be any positive number aside from 1 which is reserved for the parent `<menu tag>`. Items inside menus are specified with the `<item>` tag, and the name to be displayed is as in the `<menu>` tag case specified with the `"label"` attribute. The actions executed by the item are specified with the tag `<action>` which will likely want to used with the `label name="Execute"`, in that case, inside the `<action>` tag to define an `<execute>` tag and inside that tag place a terminal instruction to be called when the user clicks that button, for example `"firefox"` to start Firefox or `"loginctl poweroff"` to turn off the system, to give some examples.

On each `<item>`tag there\'s also the possibility to specify an icon using the `"icon"` attribute with must be filled with a path pointing to the icon wanting to display in the menu.

### [rc.xml]

The [rc.xml] file defines Openbox behavior, keyboard bindings, and mouse bindings.

The following is a list of special key \'modifiers\':

  ----- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Key   Description
  S     [Shift] key
  C     [Ctrl] key
  A     [Alt] key
  W     Super (windows) key
  M     Meta key
  H     Hyper key
  ----- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To make a key binding, combine modifiers and a key. They are separated with the `-` (dash) sign.

** Important**\
Case matters! **S** (uppercase) equates to the [Shift] key while **s** (lowercase) is the *[s] alphabet key*.

#### [Key binding examples]

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------
  Keybinding                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Modifier
  [Alt]+[o]                                                                                                                                                                                                                                                                                                                                                A-o
  [Ctrl]+[Alt]+[x]                                                                                                                                                                          C-A-x
  [Ctrl]+[Alt]+[Shift]+[y]   C-A-S-y
  [Shift]+[s]                                                                                                                                                                                                                                                                                                                                              S-s
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------

** Important**\
Any custom key bindings should go between `<keyboard>` and `</keyboard>` tags in [rc.xml].

To open a [xterm] window with **Super+[t]**, add the following to the [rc.xml] file:

[FILE] **`~/.config/openbox/rc.xml`XTerm key bind example**

    <keybind key="W-t">
      <action name="Execute">
        <command>xterm</command>
      </action>
    </keybind>

To open Openbox\'s right-click menu with **Super+[x]**, and Openbox\'s middle-click menu with **Super+[z]**, add the following to the [rc.xml] file:

[FILE] **`~/.config/openbox/rc.xml`Root-Menu key bind example**

    <keybind key="W-x">
      <action name="ShowMenu">
        <menu>root-menu</menu>
      </action>
    </keybind>

    <keybind key="W-z">
      <action name="ShowMenu">
        <menu>client-list-combined-menu</menu>
      </action>
    </keybind>

## [Tips]

### [Icons in the Openbox menu]

Openbox is able to have icons next to menu entries.

1.  To emerge Openbox with imlib support add `imlib` USE flag to x11-wm/openbox in [/etc/portage/package.use]

    :::: cmd-box


    `root `[`#`]`echo "x11-wm/openbox imlib" >> /etc/portage/package.use`


    ::::
2.  Re-emerge Openbox so that support for the `imlib` USE flag is considered:

    :::: cmd-box


    `root `[`#`]`emerge --ask --changed-use x11-wm/openbox`


    ::::
3.  Add a \<showIcons\>yes\</showIcons\> line to the \<menu\> section of the [rc.xml] file.
4.  Add in menu.xml icon=\"\\" like this:

    ::: box-caption
    [FILE] **`~/.config/openbox/menu.xml`Manually add icons to Openbox example**
    :::

    :::
        <menu label="Shells" icon="/usr/share/icons/shell.png">
        <item label="xterm" icon="/usr/share/icons/xterm.png">
            <action name="Execute">
                <execute>xterm</execute>
            </action>
        </item>
    :::

## [See also]

-   [Tint2](https://wiki.gentoo.org/wiki/Tint2 "Tint2") --- a lightweight panel/taskbar specifically made for [Openbox], but it can also work with other window managers.
-   [Openbox/Guide](https://wiki.gentoo.org/wiki/Openbox/Guide "Openbox/Guide") --- covers the basics on installing and configuring the OpenBox window manager.
-   [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE") --- a free desktop environment with comparatively low resource requirements.

## [External resources]

-   [Openbox page on the Arch Linux wiki](https://wiki.archlinux.org/title/Openbox)