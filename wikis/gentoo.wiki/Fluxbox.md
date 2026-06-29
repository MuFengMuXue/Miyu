This page contains [[changes](https://wiki.gentoo.org/index.php?title=Fluxbox&oldid=1306085&diff=1414877)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Fluxbox/de "Fluxbox (33% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Fluxbox/es "Fluxbox (12% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Fluxbox/hu "Fluxbox (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Fluxbox/ru "Fluxbox (99% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Fluxbox/zh-cn "Fluxbox (17% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Fluxbox/ja "Fluxbox (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Fluxbox/ko "Fluxbox (55% translated)")

**Resources**

[[]][Home](http://fluxbox.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/fluxbox)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Fluxbox "wikipedia:Fluxbox")

[[]][GitHub](https://github.com/fluxbox/fluxbox)

**Fluxbox** is an open-source stacking [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11") that was originally forked from [Blackbox](https://wiki.gentoo.org/wiki/Blackbox "Blackbox"). This guide provides instructions on how to set up the Fluxbox window manager for X11.

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Preparing X11]](#Preparing_X11)
    -   [[3.2] [Display locking]](#Display_locking)
    -   [[3.3] [Themes and artwork]](#Themes_and_artwork)
    -   [[3.4] [Running Fluxbox for the first time]](#Running_Fluxbox_for_the_first_time)
    -   [[3.5] [Fluxbox hotkeys]](#Fluxbox_hotkeys)
    -   [[3.6] [System monitor]](#System_monitor)
    -   [[3.7] [Icons]](#Icons)
    -   [[3.8] [Graphical file managers]](#Graphical_file_managers)
        -   [[3.8.1] [Gentoo File Manager]](#Gentoo_File_Manager)
        -   [[3.8.2] [Rox Filer]](#Rox_Filer)
        -   [[3.8.3] [Thunar File Manager]](#Thunar_File_Manager)
    -   [[3.9] [Image viewers]](#Image_viewers)
    -   [[3.10] [Setting a theme, background, and a startup script]](#Setting_a_theme.2C_background.2C_and_a_startup_script)
    -   [[3.11] [Enabling privileged operations through polkit]](#Enabling_privileged_operations_through_polkit)
    -   [[3.12] [Menu generation]](#Menu_generation)
    -   [[3.13] [Editing menus by hand]](#Editing_menus_by_hand)
    -   [[3.14] [Setting default applications]](#Setting_default_applications)
-   [[4] [Usage]](#Usage)
-   [[5] [Summary]](#Summary)
-   [[6] [External resources]](#External_resources)

## [[] Introduction]

For those who are unfamiliar with Linux\'s desktop model, window managers (WMs) are the applications which are run by X11 to manage other graphical programs. WMs control where each window is placed, its size, and which desktop(s) have access to it. This can be done automatically via a set of user-defined rules, or can be done at runtime with the mouse and possibly keyboard shortcuts, depending on the specific WM.

Some WMs, however, take on more functionality than just window management. Fluxbox also provides a platform for launching applications, configuring keyboard shortcuts and background images, as well as displaying information with the slit. GNOME\'s default WM, Metacity, does not include these things, but they are available through other GNOME programs. Thus, one cannot truly say that Fluxbox is a lightweight WM. However, since Fluxbox includes everything necessary for a basic desktop, many people use it in place of larger desktop suites like [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") or [KDE](https://wiki.gentoo.org/wiki/KDE "KDE").

To make things even more confusing, however, Fluxbox can replace the default WM for GNOME or KDE. For example, some people find that Metacity, GNOME\'s window manager, simply does not have the flexibility they need, but that Fluxbox does not have all the built-in applications and integration they desire from a complete desktop environment. Thus, a person could use Fluxbox to manage the windows and GNOME for the rest. Note, however, that with this setup there are some issues caused by overlapping feature sets.

Fluxbox can also be expanded by third party software. This is often ideal in situations where hardware resources are limited, or as a matter of personal taste.

This article is aimed at those who are new to Fluxbox, curious, or who are wanting to get more out of the Gentoo/Fluxbox experience. The article will also illustrate how to get more (yet quite optional) functionality by using third party programs that work well with Fluxbox.

## [[] Installation]

First, make sure a working X environment has been installed, as shown in the [X Server\'s configuration article](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide").

### [[] USE flags]

### [USE flags for] [x11-wm/fluxbox](https://packages.gentoo.org/packages/x11-wm/fluxbox) [[]] [X11 window manager featuring tabs and an iconbar]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+imlib`](https://packages.gentoo.org/useflags/+imlib)           Add support for imlib, an image loading and rendering library
  [`+slit`](https://packages.gentoo.org/useflags/+slit)             Enables the Fluxbox slit (or dock)
  [`+systray`](https://packages.gentoo.org/useflags/+systray)       Enables the system tray in the Fluxbox toolbar
  [`+toolbar`](https://packages.gentoo.org/useflags/+toolbar)       Enables the Fluxbox toolbar
  [`+truetype`](https://packages.gentoo.org/useflags/+truetype)     Add support for FreeType and/or FreeType2 fonts
  [`bidi`](https://packages.gentoo.org/useflags/bidi)               Enable bidirectional language support
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vim-syntax`](https://packages.gentoo.org/useflags/vim-syntax)   Pulls in related vim syntax scripts
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)       Add support for querying multi-monitor screen geometry through the Xinerama API
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Before installing Fluxbox take a look at some of the available USE flags (listed above).

There is a `vim-syntax` flag to make configuration easier later on. This flag will install `fluxbox-syntax`, a special Fluxbox color scheme for the [vim] text editor. This enables users to more readily see the contents of their keys and init files for Fluxbox. It is a tiny extension for vim and is highly recommended if Fluxbox is to be configured at all.

There are three flags that customize the functionality of Fluxbox: `slit`, `systray` and `toolbar`. These flags are provided so that users who do not need the [slit](http://fluxbox.org/features/) or the [toolbar](http://fluxbox.org/features/) can compile Fluxbox without them. This is useful when needing to run an extremely minimal environment, or when planning to use different applications that provide these features, such as standalone panels or docks.

Once the USE flags have been decided, add them to the [/etc/portage/package.use] file. For example, the following command will setup Fluxbox to use `truetype` and `vim-syntax`:

`root `[`#`]`echo "x11-wm/fluxbox truetype vim-syntax" >> /etc/portage/package.use`

### [[] Emerge]

Installing fluxbox is a matter of emerging it to the system:

`root `[`#`]`emerge --ask x11-wm/fluxbox`

That is it; Fluxbox is now installed! However, it is likely it will not be used efficiently with just those tools. The following sections will help install other potentially necessary packages, and configure Fluxbox and the third party programs to work better for the user. Keep in mind that all these steps are optional, so feel free to pick and choose from what is presented as best suited.

## [[] Configuration]

### [[] Preparing X11]

Fluxbox is simply another program that runs on X11. If desired, one can [startx] and then type [fluxbox] in a [xterm] window. However, to say the least, this is annoying. If one does not desire to boot to the GUI, but instead wants to start X11 manually, it is possible to have X automatically load Fluxbox by executing, as a normal (non-root) user:

`user `[`$`]`echo "exec startfluxbox" > ~/.xinitrc`

The above method is also not ideal for most users, as they want to have the desktop environment *all* the time; it is a pain to type [startx] when desiring to use a GUI every time the system boots. It also presents a security risk to the unaware. If the X11 display is locked using [xlock], but run X11 from a console, then someone with physical access to the system can switch to that console, kill X11, and use whatever account is logged in. The only way to prevent this is to either background X11 or run it in [screen], detach the [screen] session, then logout of the console. This tedious task should not have to be performed. With a graphical login manager this problem does not exist. However, graphical login managers require running X11 as root, which may be a bad thing. There are, as of this writing, no exploits that the author is aware of for the current version, but if one is concerned, then do not use X11 at all or use the above method with [screen]. Note that this is not a Fluxbox issue; it is an issue with X11 itself.

There are a number of graphical login managers to choose from; another manager can be chosen at discretion of the user, however [SLiM](http://slim.berlios.de) will be used for the purpose of this article. SLiM works well for Fluxbox, as well as any other environments that may be installed (such as GNOME, KDE, or Xfce).

`root `[`#`]`emerge --ask x11-misc/slim`

`root `[`#`]`rc-update add display-manager default`

** Important**\
Be sure to emerge [slim] and add **display-manager** to the bootscript, and not the other way around! Switching these will cause failure. One system-wide configuration file will need to be modified:

[FILE] **`/etc/conf.d/display-manager`Setting the display manager to SLiM**

    DISPLAYMANAGER="slim"

### [[] Display locking]

When dealing with WMs a *must have* is a program lock to the X display for preventing unauthorized system access. When installing Fluxbox it would be wise to emerge [vlock](https://wiki.gentoo.org/wiki/Vlock "Vlock") or [[[x11-misc/xlockmore]](https://packages.gentoo.org/packages/x11-misc/xlockmore)[]] so the system can be locked. It is also advisable to enable autolocking of the screen when the system is idle. The package [[[x11-misc/xautolock]](https://packages.gentoo.org/packages/x11-misc/xautolock)[]] can be used to execute [xlock] after a specified timeout. The vast majority of users will also want the ability to set their own background images on the desktop; emerging [[[x11-terms/eterm]](https://packages.gentoo.org/packages/x11-terms/eterm)[]] will make setting desktop background images a possibility. [eterm] also doubles as a nice X11 terminal. [[[media-gfx/feh]](https://packages.gentoo.org/packages/media-gfx/feh)[]] is a more lightweight solution that doubles as a slimmed down image browser.

`root `[`#`]`emerge --ask x11-misc/xlockmore x11-misc/xautolock x11-terms/eterm media-gfx/feh`

To enable autolocking add the following to the [\~/.fluxbox/startup] file above the `exec fluxbox` line:

[FILE] **`~/.fluxbox/startup`**

    xautolock -time 15 -locker "xlock -mode blank" -secure &

### [[] Themes and artwork]

This section can be skipped for a minimal footprint, however it is nice to allow users to customize their WM\'s appearance. Themes specific to Fluxbox, Gentoo artwork for any WM, and themes that can be used on any \*box WM will be installed.

`root `[`#`]`emerge --ask x11-themes/commonbox-styles x11-themes/commonbox-styles-extra x11-themes/fluxbox-styles-fluxmod x11-themes/gentoo-artwork`

### [[] Running Fluxbox for the first time]

Now Fluxbox ready to run for the first time. It will create a directory called [\~/.fluxbox/] in each user\'s home directory, which is where Fluxbox will store its settings and populate them with some default values.

`user `[`$`]`startx`

If SLiM or another display manager has been installed, be sure to start it by becoming root and running:

`root `[`#`]`/etc/init.d/display-manager start`

Choose Fluxbox as the session and login with a regular user.

Once Fluxbox is running, it will look quite plain. A blank desktop with a toolbar at the bottom should be visible. Right-clicking anywhere on the desktop should bring up the menu. From there X applications can be started, or a terminal can be opened run console programs.

### [[] Fluxbox hotkeys]

Fluxbox comes with a very weak set of default keysets. It enables a user to switch windows and desktops, and no more. Before changing it, there are a few things necessary to know. In the Fluxbox keys file, there are some strange modifiers. [Mod1] is commonly known as the [Alt] key, and [Mod4] is the [Super] (AKA Windows) key. Control and Shift are [Ctrl] and [Shift]. However, it is usually best to use Mod1 or Mod4 because other X11 programs tend to use Control and Shift for their own shortcuts.

All of these are independent, so feel free to leave out anything not desired, or to modify the given example to meet special needs. This guide uses what the author assumes to be the most common programs, so also substitute the name of the binary used if it differs from what appears. For more information, read the man page for Fluxbox ([man fluxbox]).

With that out of the way, fire up a text editor (non-root user), point it to [\~/.fluxbox/keys], and begin enhancing some shortcuts!

[FILE] **`~/.fluxbox/keys`Modifying keyboard shortcuts**

    # Locks the X11 display for the current user:
    Mod4 l   :ExecCommand xlock

    # Opens a number of programs with quickkeys. These are just examples, I am sure
    # you get the point...
    Mod1 f   :ExecCommand firefox
    Mod1 t   :ExecCommand thunderbird
    Mod1 o   :ExecCommand oowriter
    Mod1 v   :ExecCommand gvim

    # Fluxbox has no sound control; do a hack to get some
    # (assumes alsa is being used; good luck if using oss :P )
    Mod1 e   :ExecCommand Eterm -name alsa -e alsamixer

    # This launches fbrun, which in turn launches other programs:
    Mod1 r   :ExecCommand fbrun

    # Program Control. It just makes life simpler...
    Mod1 4   :Close
    Mod1 m   :Minimize

    # If using aterm (emerge x11-terms/aterm), the following opens a really nice
    # transparent aterm with no borders, fitting nicely with 1024x768
    # resolution, while still leaving room for conky. Once again, feel free to
    # modify.
    Mod1 a   :ExecCommand aterm -name aterm -sl 3000 -tr +sb -sr -sk -bg black -fg \
    white -fade 90 -bl -tn xterm -fn \
    -misc-fixed-medium-r-normal-*-*-120-*-*-c-*-iso8859-15 -g 116x57

    # Similar to the above, but opens a transparent rooted terminal.
    # The root password must be known to use this:
    Mod1 s   :ExecCommand aterm -name aterm -sl 3000 -tr +sb -sr -sk -bg black -fg \
    white -fade 90 -bl -tn xterm -fn \
    -misc-fixed-medium-r-normal-*-*-120-*-*-c-*-iso8859-15 -g 116x57 -e su -

    # Takes a screenshot using the print button, needs media-gfx/imagemagick
    None 107 :Exec tm=$(date +%F,%T) && import -window root /tmp/screenshot$tm.png \
    && display /tmp/screenshot$tm.png
    Mod1 107 :Exec tm=$(date +%F,%T) && import -frame -window $(xprop _NET_ACTIVE_WINDOW \
    -root | awk '') /tmp/screenshot$tm.png && display /tmp/screenshot$tm.png
    Control 107 :Exec import png:- | display png:-

### [[] System monitor]

It is a common desire to setup a system monitor for X11 on desktop systems. Gkrellm ([[[app-admin/gkrellm]](https://packages.gentoo.org/packages/app-admin/gkrellm)[]]) is a commonly used monitor, but in the spirit of Fluxbox minimalism, a simpler monitor will be used. Welcome [conky]. If desired, use another monitor; there are plenty of instructions elsewhere on the wiki.

`root `[`#`]`emerge --ask app-admin/conky`

The default configuration file for Conky is rather weak, but more info can be found by reading the man page or the [Conky guide](https://wiki.gentoo.org/wiki/Conky/Guide "Conky/Guide").

### [[] Icons]

Fluxbox does not come with a utility or program to draw icons to the desktop; everything is handled by keyboard shortcuts, or the right-click menu. iDesk is a program that can be used to fulfill this need. It is aimed at users of minimal WMs like Fluxbox who want to display icons in the root window, and it even supports funky graphic effects like transparency! Despite its name, iDesk is not affiliated with Apple or Mac. Installing iDesk is as simple as:

`root `[`#`]`emerge --ask x11-misc/idesk`

Once installed, it will be necessary to configure iDesk so that it is able to display icons. Its configuration file can be found at [\~/.ideskrc]. This is a rather lengthy task, and can not be well covered in this article. The following resources might be useful in order to configure iDesk: [man idesk], [iDesk\'s Usage Guide](http://idesk.sourceforge.net/wiki/index.php/Idesk-usage) and this [thread in the Gentoo Forums](https://forums.gentoo.org/viewtopic-t-87262.html).

### [[] Graphical file managers]

It is important to note that Gentoo does not need a file manager. It is perfectly possible, and indeed simpler (in the author\'s humble opinion), to do file manipulation by command-line. However, not everyone agrees\...

Many users who are new to Gentoo/Fluxbox are put off by the lack of a graphical file manager such as [nautilus] in GNOME. Fluxbox itself does not provide such a program, but, as always, one is simple to acquire. There are many choices, but this article will only present three:

1.  [Gentoo file manager](https://wiki.gentoo.org/wiki/Fluxbox#Gentoo_File_Manager "Fluxbox") for the minimalist who likes text only.
2.  [rox](https://wiki.gentoo.org/wiki/Fluxbox#Rox_Filer "Fluxbox") for those who like text *and* graphics.
3.  [thunar](https://wiki.gentoo.org/wiki/Fluxbox#Thunar_File_Manager "Fluxbox") for those who like full graphical file managers.

For those who are not sure what they like, it is also possible to install all three file managers in order to try each one.

#### [[] Gentoo File Manager]

Gentoo is a minimalistic file manager which seeks to provide the benefits of a GUI interface without the bloat which is commonly associated.

`root `[`#`]`emerge --ask app-misc/gentoo`

** Note**\
The Gentoo file manager is a separate project from the Gentoo Linux distribution. For more information on this, see the Gentoo [Name and Logo Usage Guidelines](https://www.gentoo.org/inside-gentoo/foundation/name-logo-guidelines.html).

The Gentoo file manager aims to be fully configurable via GUI, so feel free to tweak.

#### [[] Rox Filer]

Rox Filer is a file manager which uses icons as well as text and is much like Windows\' Explorer.

`root `[`#`]`emerge --ask app-misc/rox-filer`

Rox behaves much like \"traditional\" file managers, so its interface should be intuitive. If not, there always are man pages for further information.

#### [[] Thunar File Manager]

[Thunar](http://thunar.xfce.org/) is a lightweight, fast file manager that, like Rox, behaves much like \"traditional\" file managers. It includes icons and text, and it is easy to use. Though originally designed for [Xfce](http://www.xfce.org), it makes a nice complement to a Fluxbox-based system.

`root `[`#`]`emerge --ask xfce-base/thunar`

### [[] Image viewers]

Many WMs come with utilities to view pictures (images) in a directory. These applications are small and lightweight, and do not allow for editing (which is assumed to be done by tools such as [gimp]). This is necessary when using command line, [gentoo], or [rox] as file managers. Although [thunar] can display image thumbnails having a separate lightweight image viewer is still a good idea.

`root `[`#`]`emerge --ask media-gfx/gqview`

[gqview] can be launched in any directory, and can browse through any supported picture format.

### [][[] Setting a theme, background, and a startup script]

Fluxbox has a number of themes that can be accessed via the right click menu. Navigate to [Fluxbox menu] → [System Styles]. These themes usually set their own background, which is either a single color or a gradient of some type. Most users prefer to set their own backgrounds, and to have those background persist no matter what theme has been chosen. To do so, another one of Fluxbox\'s configuration files must be modified, this one governs Fluxbox\'s startup behavior. Fire up that text editor again; this time point it to the [\~/.fluxbox/startup] file.

If this file was pre-existing then be sure to clear it. Add the following to the newly created file, uncommenting as needed, and filling in values for the CAPS:

[FILE] **`~/.fluxbox/startup`Editing startup scripts for Fluxbox**

    # Gentoo's Fluxbox startup script

    # Programs which need to run constantly, as opposed to a one time execution,
    # this means they need an "&" (ampersand) at the end of the command.

    # Show the Fluxbox splash-screen
    #fbsetbg -C /usr/share/fluxbox/splash.jpg

    # This sets a desktop background image. A program must be setup
    # to do this (x11-terms/eterm is recommended)
    #fbsetbg -f PATH_TO_IMAGE

    # Custom fonts directory
    #xset +fp PATH_TO_FONT_DIRECTORY

    # Starts the icons program
    #idesk &

    # This MUST be the last command!
    exec /usr/bin/fluxbox -log ~/.fluxbox/log

### [[] Enabling privileged operations through polkit]

Fluxbox is able to communicate with core system services over [D-Bus](https://wiki.gentoo.org/wiki/D-Bus "D-Bus") to allow privileged operations, such as shutting down the system. To handle the authorizations towards these operations, [polkit](https://wiki.gentoo.org/wiki/Polkit "Polkit") (formerly known as policykit) can be used.

In order to use polkit, an agent is required. There are several polkit agents available and if a desktop profile is used, one of them will already be installed. Their respective startup files are stored in [/etc/xdg/autostart] but are not considered by fluxbox. Instead, an additional entry should be made to fluxbox\' [startup] file:

[FILE] **`~/.fluxbox/startup`Starting a polkit authentication agent at startup**

    /usr/libexec/polkit-gnome-authentication-agent-1 &

### [[] Menu generation]

The author uses a text editor to create menus. If this sounds appealing, please skip this section and proceed to [Fluxbox](#Editing_Menus_by_Hand).

It is possible to edit [\~/.fluxbox/menu] by hand after using an automatic generator (see next section), to add packages or delete those which are not used. Note when something is deleted from this menu, it does not delete the package from the system; only a link is removed from the individual user\'s menu. The program can still be run by command-line or alternate methods (hotkeys, etc.).

If Fluxbox has been installed then a program called [fluxbox-generate_menu] should also be installed. This program can be used to generate menus. Run it with the following options as a non-root user to generate a menu:

`user `[`$`]`fluxbox-generate_menu -is -ds`

It is recommended [fluxbox-generate_menu] (listed above) is used instead of other programs that accomplish similar tasks. The reason for the recommendation is that other programs may not understand Gentoo\'s filesystem directory structure, where [fluxbox-generate_menu] does.

This can also be done from the Fluxbox menu itself. There is usually an entry in the [Fluxbox] menu called [Regen Menu] which will re-run this script, looking for any new applications that have been installed since the last time it was ran.

** Note**\
It is possible to use this method to auto-generate the menu and still have some manual control over it. Creating and editing a [\~/.fluxbox/usermenu] file by hand (see the next section for syntax) will give the user a personalized menu which will not be erased the next time the script has been run.

### [[] Editing menus by hand]

Fluxbox\'s menu is a text file that follows a simple syntax that is described in this section. The default menu definition is present in the [\~/.fluxbox/menu] file.

Menu entries for executing applications are defined by an `[exec]` element. Entries can be defined under the `[begin]` definition (the menu root), or between a `[submenu]` and its corresponding `[end]` line (submenu definitions). For example:

[FILE] **`~/.fluxbox/menu`Defining new menu entries**

    # Custom fluxbox menu
    [begin] (Fluxbox)
      (...)
      [exec] (XTerm White on Black)
      (...)
      [submenu] (More terminals)
        [exec] (Aterm default)
        [exec] (Rxvt default)
      [end]
      (...)
    [end]

The root menu definition begins with the `[begin]` tag, followed by its name, between parentheses and ends with its corresponding `[end]` tag. All the menu commands (called here, tags) are enclosed by square brackets, menu names will be enclosed between parentheses and the actual commands are enclosed between braces. Comments are allowed in this file, for lines beginning with `#`.

In the example shown above, the first `[exec]` line defines a new entry named \"XTerm White on Black\", which will execute [xterm -ls -fg white -bg black] as if from a command line. Next is a submenu which is defined using the `[submenu]` tag, and after that a section called \"More terminals\", with two more `[exec]` commands. Any submenu definition must have its corresponding `[end]` tag.

There are other menu commands that can be used in the [\~/.fluxbox/menu] file. Read the [official documentation](http://fluxbox.org/docbook.php) available online for more information.

### [[] Setting default applications]

See the [Default applications](https://wiki.gentoo.org/wiki/Default_applications "Default applications") article.

## [[] Usage]

Resize a window by left clicking the tiny window-corner re-sizing tools and drag them around, or hold down the [Mod1] key and right click somewhere near a border, then drag the mouse.

## [[] Summary]

Congratulations! Fluxbox is now installed, configured, and ready to go. If any questions or suggestions come to mind feel free to edit this page, add a suggestion to the associated talk page, and/or file a bug report at Gentoo\'s [Bugzilla](https://bugs.gentoo.org/).

## [External resources]

-   The [Fluxbox wiki](https://fluxbox-wiki.github.io/).
-   Fluxbox developers and users in [[#fluxbox](ircs://irc.libera.chat/#fluxbox)] ([[webchat](https://web.libera.chat/#fluxbox)]) on Libera Chat.

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Jonathan Smith, Alin Dobre, Joshua Saddler, lack**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*