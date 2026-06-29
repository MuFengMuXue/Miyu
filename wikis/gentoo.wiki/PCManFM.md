**Resources**

[[]][Home](https://wiki.lxde.org/en/PCManFM)

[[]][Package information](https://packages.gentoo.org/packages/x11-misc/pcmanfm)

[[]][Wikipedia](https://en.wikipedia.org/wiki/PCMan_File_Manager "wikipedia:PCMan File Manager")

[[]][GitWeb](https://git.lxde.org/gitweb/?p=lxde/pcmanfm.git)

[[]][Bugs (upstream)](https://sourceforge.net/p/pcmanfm/bugs/)

**Article status**

[[]]This article has some todo items:\

-   #1 Review KDE style section
-   #2 Review desktop icon instructions

**PCMan** **F**ile **M**anager (PCManFM) is a powerful yet lightweight file manager application, default file manager of [LXDE](https://wiki.gentoo.org/wiki/LXDE "LXDE"). Written by Hong Jen Yee.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Openbox integration]](#Openbox_integration)
    -   [[2.2] [Adding desktop icons]](#Adding_desktop_icons)
    -   [[2.3] [File templates]](#File_templates)
        -   [[2.3.1] [KDE style]](#KDE_style)
        -   [[2.3.2] [GNOME style]](#GNOME_style)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [x11-misc/pcmanfm](https://packages.gentoo.org/packages/x11-misc/pcmanfm) [[]] [Fast lightweight tabbed filemanager]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2024-11-21 07:49] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

PCManFM can be easily installed via [emerge]:

`root `[`#`]`emerge --ask x11-misc/pcmanfm`

## [Configuration]

### [Openbox integration]

To have PCManFM start (on a per-user basis) when using Openbox as a window manager add it to the user\'s [\~/.config/openbox/autostart] file.

[FILE] **`~/.config/openbox/autostart`Starting PCManFM with Openbox**

    pcmanfm --desktop &

** Note**\
The `&` (ampersand) on the end of the above command is important. The `&` sends the `pcmanfm` process to the background so that Openbox\'s [autostart] file can continue executing.

### [Adding desktop icons]

Generally speaking, desktop icons for installed applications can be found in the [/usr/share/applications/] folder. In order to add an application link to the Desktop simply copy the appropriate shortcut from the [/usr/share/applications/] directory to the user\'s desktop directory. Follow the syntax in the example below by substituting `application.desktop` for the application of choice:

`user `[`$`]`cp /usr/share/applications/application.desktop ~/Desktop/`

If the copied link for the application does not show up on the desktop try refreshing the session by logging out and logging back in.

### [File templates]

Like [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME")\'s Nautilus and [KDE](https://wiki.gentoo.org/wiki/KDE "KDE")\'s Dolphin file managers, PCManFS (version 1.2.0 and up) makes use of context menu file templates for quick file creation. PCManFS supports *both* the KDE style and GNOME style of template creation. Users can decide which method to use. For Gnome users or new users in general the quickest and most straight forward option would be to skip to [GNOME style](https://wiki.gentoo.org/wiki/PCManFM#GNOME_style "PCManFM"). For transitioning KDE users the following [KDE style](https://wiki.gentoo.org/wiki/PCManFM#KDE_style "PCManFM") section should be helpful.

** Note**\
In order for templates to work the [[[x11-libs/libfm]](https://packages.gentoo.org/packages/x11-libs/libfm)[]] package (version 1.2.0 and up) needs to be installed. Portage *should* pull in this package automatically on `~amd64` systems. If for some reason it is not available it can be manually installed.

#### [KDE style]

To create new file templates using the KDE style [.desktop] files must be defined in the proper locations. Global templates should be placed in [/usr/share/templates] while local (per-user) templates should be placed in [\~/.local/share/templates] If these folders do not exist they will need to be created.

For global templates:

`root `[`#`]`mkdir -p /usr/share/templates/.source`

For local templates:

`user `[`$`]`mkdir -p ~/.local/share/templates`

The contents of the [.desktop] files should follow this scheme:

[FILE] **`/usr/share/templates/text.desktop`**

    [Desktop Entry]
    Comment=<Comment on template>
    Icon=<Icon name for template>
    Name=<Name for template>
    Type=Link
    URL=

If the above folder(s) did not exist before PCManFM was running, then the folder(s) will be ignored until PCManFM is restarted. Either log out and log back in or use `kill` to end the PCManFM process.

`user `[`$`]`killall pcmanfm`

After a refresh the newly created template files can be accessed via the context menu\'s (right-click) [Create New] entry.

#### [GNOME style]

To use the GNOME style of templates make a folder titled [\~/Templates] in the user\'s home directory:

`user `[`$`]`mkdir ~/Templates`

Fill the [\~/Templates] folder with desired template files. In order to work as most users expect, the template files must contain the data they are supposed to represent. For example, to have bash.sh, text.txt, and a document.odt as file templates create one of each *type* of file in the [\~/Templates] directory. This process involves saving a file of each type with the associated program. A template of an empty text file should be created with a text editor, the bash script file should contain a line starting with `#!/bin/bash`, and an empty open document text file should be created and then saved with an open document text editor ([LibreOffice](https://wiki.gentoo.org/wiki/LibreOffice "LibreOffice") or [OpenOffice](https://wiki.gentoo.org/index.php?title=OpenOffice&action=edit&redlink=1 "OpenOffice (page does not exist)")).

`user `[`$`]`ls ~/Templates`

    bash.sh  file.txt  document.odt

If the [\~/Templates] folder did not exist before PCManFM was running, then the folder will be ignored until PCManFM is restarted. Either log out and log back in or use `kill` to end the PCManFM process.

`user `[`$`]`killall pcmanfm`

After a refresh the newly created template files can be accessed via the context menu\'s (right-click) [Create New] entry.

[[[x11-misc/xdg-user-dirs]](https://packages.gentoo.org/packages/x11-misc/xdg-user-dirs)[]] can configure the location of [\~/Templates]:

`user `[`$`]`xdg-user-dirs-update --set TEMPLATES .config/Templates`

## [Usage]

### [Invocation]

`user `[`$`]`pcmanfm --help`

    Usage:
      pcmanfm [OPTION...] [FILE1, FILE2,...]

    Help Options:
      -h, --help                   Show help options
      --help-all                   Show all help options
      --help-gtk                   Show GTK+ Options

    Application Options:
      -p, --profile=PROFILE        Name of configuration profile
      -d, --daemon-mode            Run PCManFM as a daemon
      --no-desktop                 No function. Just to be compatible with nautilus
      --desktop                    Launch desktop manager
      --desktop-off                Turn off desktop manager if it's running
      --desktop-pref               Open desktop preference dialog
      --one-screen                 Use --desktop option only for one screen
      -w, --set-wallpaper=FILE     Set desktop wallpaper from image FILE
      --wallpaper-mode=MODE        Set mode of desktop wallpaper. MODE=(color|stretch|fit|crop|center|tile|screen)
      --show-pref=N                Open Preferences dialog on the page N
      -n, --new-win                Open new window
      -f, --find-files             Open a Find Files window
      --role=ROLE                  Window role for usage by window manager
      --display=DISPLAY            X display to use

## [See also]

-   [File managers](https://wiki.gentoo.org/wiki/File_managers "File managers") --- a computer program that allows for the manipulation of files and directories on a computer\'s [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem").