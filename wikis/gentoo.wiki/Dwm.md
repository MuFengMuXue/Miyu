This page contains [[changes](https://wiki.gentoo.org/index.php?title=Dwm&oldid=1261824&diff=1417968)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Dwm/de "Dwm (98% translated)")
-   [English]
-   [italiano](https://wiki.gentoo.org/wiki/Dwm/it "Dwm (75% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Dwm/hu "Dwm (100% translated)")
-   [فارسی](https://wiki.gentoo.org/wiki/Dwm/fa "Dwm/fa (23% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Dwm/ja "dwm (100% translated)")

**Resources**

[[]][Home](https://dwm.suckless.org/)

[[]][Package information](https://packages.gentoo.org/packages/x11-wm/dwm)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dwm "wikipedia:Dwm")

**dwm** (shortened from **d**ynamic **w**indow **m**anager) is a dynamic [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11") from [suckless.org](https://suckless.org/). dwm is a single binary, and its source code is intended to never exceed 2000 [SLOC](https://en.wikipedia.org/wiki/Source_lines_of_code "wikipedia:Source lines of code").

dwm is configured by editing the [C](https://en.wikipedia.org/wiki/C_(programming_language) "wikipedia:C (programming language)") source code, and recompiling it. The suckless website states that the project ***focuses on advanced and experienced computer users***, and - perhaps tongue in cheek - that customization through editing source code \"keeps its userbase small and elitist\".

## Contents

-   [[1] [Window model]](#Window_model)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Starting]](#Starting)
    -   [[3.2] [Main dwm configuration file (dwm.h file)]](#Main_dwm_configuration_file_.28dwm.h_file.29)
    -   [[3.3] [Settings file (dwmrc)]](#Settings_file_.28dwmrc.29)
-   [[4] [Additional features]](#Additional_features)
    -   [[4.1] [dmenu]](#dmenu)
        -   [[4.1.1] [Installation]](#Installation_2)
            -   [[4.1.1.1] [Emerge]](#Emerge_2)
            -   [[4.1.1.2] [Configuration]](#Configuration_2)
            -   [[4.1.1.3] [Usage]](#Usage)
            -   [[4.1.1.4] [Flatpaks]](#Flatpaks)
    -   [[4.2] [Additional status information]](#Additional_status_information)
        -   [[4.2.1] [Conky]](#Conky)
        -   [[4.2.2] [Custom script]](#Custom_script)
-   [[5] [Usage]](#Usage_2)
    -   [[5.1] [Keys and key functions]](#Keys_and_key_functions)
        -   [[5.1.1] [Moving a window manually]](#Moving_a_window_manually)
        -   [[5.1.2] [Default shortcuts]](#Default_shortcuts)
            -   [[5.1.2.1] [Window management]](#Window_management)
            -   [[5.1.2.2] [Utilities]](#Utilities)
            -   [[5.1.2.3] [Changing layout]](#Changing_layout)
        -   [[5.1.3] [Volume keys]](#Volume_keys)
-   [[6] [Customization]](#Customization)
    -   [[6.1] [GTK Theme]](#GTK_Theme)
    -   [[6.2] [Wallpaper]](#Wallpaper)
    -   [[6.3] [Patching]](#Patching)
        -   [[6.3.1] [Patches in /etc/portage/patches/category/application]](#Patches_in_.2Fetc.2Fportage.2Fpatches.2Fcategory.2Fapplication)
        -   [[6.3.2] [Put patches in an ebuild repository configured with Portage]](#Put_patches_in_an_ebuild_repository_configured_with_Portage)
    -   [[6.4] [Assigning applications to window tags]](#Assigning_applications_to_window_tags)
-   [[7] [Troubleshooting]](#Troubleshooting)
    -   [[7.1] [Cursor is the wrong size]](#Cursor_is_the_wrong_size)
    -   [[7.2] [Upgrading to dwm-6.0]](#Upgrading_to_dwm-6.0)
    -   [[7.3] [Fix \" Permission Denied\"]](#Fix_.22_Permission_Denied.22)
    -   [[7.4] [Remap mod key]](#Remap_mod_key)
    -   [[7.5] [Fix Java application misbehaving]](#Fix_Java_application_misbehaving)
    -   [[7.6] [Blank (grey) windows of Java applications]](#Blank_.28grey.29_windows_of_Java_applications)
    -   [[7.7] [Background not redrawing]](#Background_not_redrawing)

## [[] Window model]

dwm is a dynamic window manager, as such it manages windows in tiled, monocle and floating layouts. All of the layouts can be applied dynamically, optimizing the environment for the application in use and the task performed.

Launch a few terminals with [Shift]+[Alt]+[Enter] and dwm will tile the windows between the master and stack. A new terminal appears on the master window. Existing windows are pushed upon a stack to the right of the screen. [Alt]+[Enter] toggles windows between master and stack.

       +------+----------------------------------+--------+
       | tags | title                            | status +
       +------+---------------------+------------+--------+
       |                            |                     |
       |                            |                     |
       |                            |                     |
       |                            |                     |
       |          master            |        stack        |
       |                            |                     |
       |                            |                     |
       |                            |                     |
       |                            |                     |
       +----------------------------+---------------------+

## [[] Installation]

### [[] USE flags]

### [USE flags for] [x11-wm/dwm](https://packages.gentoo.org/packages/x11-wm/dwm) [[]] [a dynamic window manager for X11]

  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig)   Use this to restore your config from /etc/portage/savedconfig \$/\$. Make sure your USE flags allow for appropriate dependencies
  [`xinerama`](https://packages.gentoo.org/useflags/xinerama)         Add support for querying multi-monitor screen geometry through the Xinerama API
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-27 04:57] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Users should consider enabling the [`savedconfig`](https://wiki.gentoo.org/wiki/Savedconfig "Savedconfig") USE flag in order to save customized configuration file to [/etc/portage/savedconfig/x11-wm/dwm-6.0.h] for later editing.

`root `[`#`]`euse --enable savedconfig`

Users with multiple monitors should enable the `xinerama` USE flag regardless of whether or not Xinerama will be used.

`root `[`#`]`euse --enable xinerama`

### [[] Emerge]

Install [[[x11-wm/dwm]](https://packages.gentoo.org/packages/x11-wm/dwm)[]]:

`root `[`#`]`emerge --ask x11-wm/dwm`

## [[] Configuration]

### [[] Starting]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=Dwm&action=edit).

To start dwm use a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or the [startx] command.

If a Display Manager is chosen, such as lightdm, one will need to create a desktop file.

[FILE] **`/usr/share/xsessions/dwm.desktop`**

    [Desktop Entry]
    Encoding=UTF-8
    Name=dwm
    Comment=Dynamic Window Manager
    Exec=dwm
    Icon=dwm
    Type=XSession

Those choosing to go the [startx] route need to create the following file:

[FILE] **`~/.xinitrc`**

    exec dbus-launch --sh-syntax --exit-with-session dwm

### [][[] Main dwm configuration file (dwm.h file)]

As stated previously, the main dwm configuration file is the [/etc/portage/savedconfig/x11-wm/dwm-6.5] file and after each change, dwm needs to be recompiled for any changes to take effect.

In order for the editor to properly display syntax highlighting for C code, create a symlink using a C header filename extension.

`root `[`#`]`ln -s /etc/portage/savedconfig/x11-wm/dwm-6.5 /etc/portage/savedconfig/x11-wm/dwm-6.5.h`

or consult the documentation of your editor of choice on how to change the syntax highlighting used for a file independent of its extension.

To use a new configuration after recompilation, if already within a dwm session, quit dwm ([Mod]+[Shift]+[Q]) then reload it, to replace the currently executing binary in memory.

### [][[] Settings file (dwmrc)]

The default xsession file provided by the Gentoo Ebuild ([/etc/X11/Sessions/dwm]) provides for a default status box that displays system load and the date/time or whatever shell code the user has inside [\~/.dwm/dwmrc]. The present mechanism (as of dwm-6.0) for sending text to a status box in the window manager\'s bar is to use \'xsetroot\', as illustrated by the default xsession mentioned above. With a few lines of shell code, one can use this mechanism to send arbitrary text to the status bar (for example, the CPU temperature, the current track on the music player, number of unread emails, etc.)

## [[] Additional features]

### [[] dmenu]

dmenu is a dynamic menu for X, originally designed for dwm.

#### [[] Installation]

###### [[] Emerge]

Install dmenu:

`root `[`#`]`emerge --ask x11-misc/dmenu`

###### [[] Configuration]

dmenu\'s options can be customized using the [dwm.h] file, such as displaying the menu at the bottom of the display.

[FILE] **`/etc/portage/savedconfig/x11-misc/dmenu-6.5.h`**

    static const char *dmenucmd[] = ;

###### [[] Usage]

By default, [Alt] + [P] key sequence enables the menu.

###### [Flatpaks]

To get Flatpaks listed on dmenu, the user will have to make a symbolic link for the app in [/usr/bin]. Flatpak exports binaries to [/var/lib/flatpak/exports/bin] for system-wide Flatpaks and to [\~/.local/share/flatpak/exports/bin] for per-user Flatpaks. In this example, Mission Center will be used. It is a system resource usage monitor.

(system-wide):

`root `[`#`]`ln -s /var/lib/flatpak/exports/bin/io.missioncenter.MissionCenter /usr/bin/MissionCenter`

(per-user):

`root `[`#`]`ln -s ~/.local/share/flatpak/exports/bin/io.missioncenter.MissionCenter /usr/bin/MissionCenter`

### [[] Additional status information]

To display additional status information on dwm\'s menu bar, one should use [[[x11-apps/xsetroot]](https://packages.gentoo.org/packages/x11-apps/xsetroot)[]], which sets text information into the upper right corner.

First of all, install [[[x11-apps/xsetroot]](https://packages.gentoo.org/packages/x11-apps/xsetroot)[]] if it\'s not installed yet.

Then, use a script or side program to loop current information in dwm status.

`root `[`#`]`emerge --ask x11-apps/xsetroot`

#### [[] Conky]

For example, try [Conky](https://wiki.gentoo.org/wiki/Conky "Conky") to display current information about the system. Prefer installing with `-X` USE flag as only text information is piped through to the dwm instance (USE flags for consideration are `-X hddtemp iostats wifi`\").

`root `[`#`]`emerge --ask app-admin/conky`

An example [\~/.config/conky/conky.conf] file. The configuration file is divided into two sections: `conky.config` and `conky.text`. The `conky.config` section contains options related to Conky, while the `conky.text` section defines what and how information is displayed. To use Conky on your system, you may need to adjust some settings in the `conky.text` section, such as the path to network interfaces or hard drives, as those can vary depending on your system.

[FILE] **`~/.config/conky/conky.conf`**

    conky.config = ;

    conky.text = [[

    M $%/$% | \
    /sda $ /sdb $ \
    /sdc $ | \
    $P0 U $ D $ |$\
    $E0 U $ D $ |$\
    $W0 U $ D $\
    $ $ $\
    CPU $F \
    /sda $F \
    /sdb $F \
         $

    ]]

** Note**\
If Conky was used some time before, pay attention to new syntax with braces and equal signs.

Add a line in the [\~/.xinitrc] file before the dwm execution command, mentioned earlier.

[FILE] **`~/.xinitrc`**

    conky | while read -r; do xsetroot -name "$REPLY"; done &
    exec ck-launch-session dbus-launch --sh-syntax --exit-with-session dwm

#### [[] Custom script]

Instead of emerging side programs, create a simple loop to show date, time, weather and other system information.

For example, to show weather, date and time create a shell script file, in [\~/.scripts/]:

[FILE] **`~/.scripts/xsetloop.sh`**

    #!/bin/sh

    let loop=0
    while true; do
        if [[ $loop%300 -eq 0 ]]; then
            weather="$(curl 'https://wttr.in?format=1')"
            let loop=0
        fi
        xsetroot -name " $weather | $(date '+%b %d %a') | $(date '+%H:%M') "
        let loop=$loop+1
        sleep 1
    done

Since the script is already looped, we just need to set it within xroot in our [\~/.xinitrc] file.

[FILE] **`~/.xinitrc`**

    . ~/.scripts/xsetloop.sh &
    exec ck-launch-session dbus-launch --sh-syntax --exit-with-session dwm

## [[] Usage]

### [[] Keys and key functions]

All (default) dwm key bindings work with a certain `MODKEY`, which is defined in [dwm.h]. The default `MODKEY` value is `Mod1Mask`, which means [Alt] key for PC keyboards. In the rest of this article, [Mod] is used to represent `MODKEY`.

#### [[] Moving a window manually]

To move a window to another window tag manually, hold down the [Mod] key and left click anywhere on the window. Then, while still holding down [Mod], click again on the window tag to move the window to.

#### [[] Default shortcuts]

Those shortcuts are used by default in x11-wm/dwm.

##### [[] Window management]

-   [Mod]+[2] - Display window tag number two
-   [Mod]+[Shift]+[1-9] - Hover mouse over window and press keys. Puts window on tag number specified.
-   [Mod]+[Shift]+[0] - Hover mouse over window and press keys. Puts window on all tags.

##### [[] Utilities]

-   [Mod]+[Shift]+[Enter] - Launch a terminal
-   [Mod]+[Shift]+[C] - Kills a window
-   [Mod]+[P] - dmenu
-   [Mod]+[J] or [Mod]+[K] - Move to another terminal.
-   [Mod]+[Enter] - Toggles Windows between stack and master.
-   [Mod]+[Shift]+[Q] - Quit dwm

##### [[] Changing layout]

-   [Mod]+[F] - Change layout on floating.
-   [Mod]+[T] - Change layout on tiled.

#### [[] Volume keys]

** Warning**\
**\"\...\"** means to be included in x11-wm/dwm **not** at the file end.

Add the following lines to the config file and re-emerge dwm:

[FILE] **`/etc/portage/savedconfig/x11-wm/dwm-6.5`**

    #include <X11/XF86keysym.h>

    ...

    /* commands */
    static const char *upvol[] = ;
    static const char *downvol[] = ;

    // for muting/unmuting //
    static const char *mute[] = ;

    // for pulse compatible //
    static const char *upvol[] = ;
    static const char *downvol[] = ;
    static const char *mute[] = ;

    ...

    static Key keys[] =  },
             },
             },

## [[] Customization]

[dwm is customized through editing its source code](https://wiki.gentoo.org/wiki/Dwm#Main_dwm_configuration_file_.28dwm.h_file.29 "Dwm")

(Put user customization tricks & tips here.)

### [GTK Theme]

Those wishing to customize the GTK theme of applications may use lxappearance:

`root `[`#`]`emerge --ask lxde-base/lxappearance`

### [Wallpaper]

There are a few ways to change the wallpaper in dwm. One of the mainstays is feh:

`root `[`#`]`emerge --ask media-gfx/feh`

Those using a Display Manager will configure feh in their [\~/.xprofile]:

[FILE] **`~/.xprofile`**

    feh --bg-scale /path/to/wallpaper

If startx is used, place that in [\~/.xinitrc].

### [[] Patching]

** Important**\
When customizing dwm via patches, it\'s important to understand how software patches work.

\
Patches aren\'t like an \'addon\' or \'extension\'; they require the source code for the software to be in a specific state, the state it was in when the patch was generated. If the relevant parts of the source code are sufficiently significantly changed - added to / modified / deleted, as happens during the development of new versions of the program - the patch will no longer apply. So the patch will need to be regenerated based on the version of the program it\'s intended to be applied to.

\

That often means either asking the creator/maintainer of the patch to do so. Although it\'s possible for users to do so themselves - by reading the patch, making the appropriate changes to the source code, and the regenerating the patch from that - it should generally not be attempted by a user not familiar with the language(s) of the source code.

Gentoo has a specific way of patching dwm. If the patches are ready to be merged with dwm source, there is special function called `eapply_user` that can be called during the emerge process. This function allows user patches to be applied to the source. Move the necessary patches one of the two locations:

-   [/etc/portage/patches](https://wiki.gentoo.org/wiki//etc/portage/patches "/etc/portage/patches")/category/application
-   An [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository")

#### [][[] Patches in /etc/portage/patches/category/application]

First create the following directory:

`root `[`#`]`mkdir -p /etc/portage/patches/x11-wm/dwm`

Copy the dwm patches to [/etc/portage/patches/x11-wm/dwm/] and make sure each patch is prefixed with a number, like so: [01-name_of_patch.patch]. Also the filename needs to end with `.patch` or `.diff` otherwise Portage will not apply it. For this example we will assume that the patch is located in the home directory (/home/larry) of the user called larry.

`root `[`#`]`cp /home/larry/01-dwm.6.0-xft.patch /etc/portage/patches/x11-wm/dwm/`

Now just install dwm, emerge will take care of applying patches:

`root `[`#`]`emerge --ask x11-wm/dwm`

#### [[] Put patches in an ebuild repository configured with Portage]

Creating an ebuild repository for the dwm patches can help when wanting to share them, either on another machine, or publicly.

Copy x11-wm/dwm from [/var/db/repos/gentoo/] to a [new ebuild repository](https://wiki.gentoo.org/wiki/Creating_an_ebuild_repository "Creating an ebuild repository"), or to whatever repository is appropriate.

Place patches in the files directory (for this example, the repository created to hold these files is named \"dwm_patches\"):

`root `[`#`]`cp /home/larry/01-dwm-6.5-xft.diff /var/db/repos/dwm_patches/x11-wm/dwm/files/`

Open the ebuild file in a text editor, [/var/db/repos/dwm_patches/x11-wm/dwm/dwm-6.5.ebuild], and list them in the PATCHES variable array for automatic patching:

[FILE] **`/var/db/repos/dwm_patches/x11-wm/dwm-6.5.ebuild`**

    PATCHES=( "$/01-dwm-6.5-xft.diff"
              "$/02-dwm-6.5-x11.diff"
    )

Fire up emerge and enjoy:

`root `[`#`]`emerge --ask x11-wm/dwm`

### [[] Assigning applications to window tags]

A user can have their favorite applications start on a different window tag, such as starting [MPlayer](https://wiki.gentoo.org/wiki/MPlayer "MPlayer") on window tag number five.

First, know the *name* of the application recorded by Xorg so dwm can be aware of this window on startup. To find this, start the target application (MPlayer in this example) and then further execute the [xprop] command ([[[x11-apps/xprop]](https://packages.gentoo.org/packages/x11-apps/xprop)[]]). Click on the MPlayer window and [xprop] will report Xorg\'s data on the MPlayer window. Use the second window name identified on the `WM_CLASS(STRING)` line. Now we have the name of the window dwm needs to be aware of.

** Note**\
Sometimes an application will have multiple windows of itself and will report one window with capital letters, while the second will have no capital letters. Wildcard characters are allowed within window names.

[FILE] **`/etc/portage/savedconfig/x11-wm/dwm-6.5.h`**

    static const Rule rules[] =,
    };

## [[] Troubleshooting]

### [Cursor is the wrong size]

Cursor size is set via \~/.Xresources. You can configure it to 8, 16, 24, 32, or 64.

[FILE] **`~/.Xresources`**

    Xcursor.size: 24

### [[] Upgrading to dwm-6.0]

Upgrading from dwm-5.9 to dwm-6.0 incorporated many changes making the previous [config.h] a likely problem for compiling dwm-6.0. Likely problems displayed might be compiler error messages \"\'nmaster\' undeclared\". To resolve, compile and install dwm-6.0 without using the custom [config.h] file and then find the default dwm-6.0 [config.h] file and diff against the old [config.h] file. (Or, decompress the dwm-6.0 tarball to acquire the default dwm-6.0 [config.h] file.)

### [][[] Fix \" Permission Denied\"]

A logind provider, like systemd or elogind, must be running in order to start a X session as non privileged user. If a logind provider is not running and the user issues [startx] dwm fails to start and message similar to this appears:

    (EE) parse_vt_settings: Cannot open /dev/tty0 (Permission denied)

If this is the case and the system is [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC")-based, add elogind to boot and start the service:

`root `[`#`]`rc-update add elogind boot`

`root `[`#`]`/etc/init.d/elogind start`

for more information, please visit [Non root Xorg](https://wiki.gentoo.org/wiki/Non_root_Xorg "Non root Xorg") wiki page.

### [[] Remap mod key]

If there are conflicts with the default dwm [Alt] conflicting with other console interface applications, use the [Esc] while within the console application. The [Esc] is an immediate usable fall back escape key. Another option, redefine the Mod key to use the keyboard [Super] (Windows) or other additional keys near the [Space].

[FILE] **`/etc/portage/savedconfig/x11-wm/dwm-6.5.h`**

    #define MODKEY Mod4Mask         /* Use Super Key */

To assign a second Mod key allowing a user to have a Mod key on both sides of the keyboard, mimic or copy this keys activity to another key on the keyboard. The Microsoft Menu key (or context menu key) on Microsoft keyboards is directly opposite of the [Super] (Windows). The [[[x11-apps/xmodmap]](https://packages.gentoo.org/packages/x11-apps/xmodmap)[]] package is required for this. (For reference, the two key\'s values are: `showkey 125/127` and `xev 133/135` respectively - on MS NEK4000 keyboard.)

[FILE] **`$HOME/.xinitrc`**

    # Top of $HOME/.xinitrc file is a good place for this.
    # This reassigns MS NEK4000 right Menu key to simulate DWM Mod4Key as well.
    xmodmap -e "keycode 135 = Super_L" # reassign MS Menu Keypress to Super_L
    xmodmap -e "remove mod1 = Super_L" # make sure X keeps it out of the mod1 group

Now, a user should have a non-conflicting and easily accessible Mod key on both sides of the keyboard!

### [[] Fix Java application misbehaving]

[Java](https://wiki.gentoo.org/wiki/Java "Java")-based applications are known to misbehave as Java doesn\'t know the WM being used. This result in GUI of specific Java applications to not work properly. To solve this we need to set the window manager name property of the root window. This can be done using the [wmname] tool and set it to `LG3D`.

Install the tool:

`root `[`#`]`emerge --ask x11-misc/wmname`

and set the property name:

`user `[`$`]`wmname LG3D`

To make this setting permanent add this command to [\~/.xinitrc].

** Tip**\
It is also useful to export `AWT_TOOLKIT` if some Java applications are using AWT, as noted below.

### [][[] Blank (grey) windows of Java applications]

Java-based applications, such as [Apache NetBeans](https://en.wikipedia.org/wiki/NetBeans "wikipedia:NetBeans"), does not render properly. To mitigate this problem set the `AWT_TOOLKIT` variable as:

`user `[`$`]`AWT_TOOLKIT=MToolkit; export AWT_TOOLKIT`

To make the action permanent is is required to add the command to the startup script, for example [\~/.xinitrc].

### [[] Background not redrawing]

Sometimes the background may not properly redraw when the current view is switched. For example, some terminal emulators such as [st] don\'t draw the entirety of their allocated window space. In these cases, X root window must have a properly defined color. This can be done with the [xsetroot] command. For example:

`user `[`$`]`xsetroot -solid black`