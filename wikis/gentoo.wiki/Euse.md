**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")][Project](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")

[[]][Package information](https://packages.gentoo.org/packages/app-portage/gentoolkit)

[[]][GitWeb](https://gitweb.gentoo.org/proj/gentoolkit.git)

[[]][Bugs (upstream)](https://bugs.gentoo.org/)

[euse] provides functionality to set (disable/enable) and obtain information about [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") in [make.conf](https://wiki.gentoo.org/wiki/Make.conf "Make.conf"), without having to edit the file directly. It is also used to get detailed information about USE flags like description, status of flags (enabled/disabled), type of flag (global/local), etc.

For more information on USE flags, please refer to [USE Flags](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE "Handbook:AMD64/Working/USE").

[euse] is part of the [gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") package.

## Contents

-   [[1] [Invocation]](#Invocation)
-   [[2] [Viewing USE flags]](#Viewing_USE_flags)
-   [[3] [Setting, and unsetting USE flags]](#Setting.2C_and_unsetting_USE_flags)
    -   [[3.1] [Enabling a USE flag]](#Enabling_a_USE_flag)
    -   [[3.2] [Disabling a USE flag]](#Disabling_a_USE_flag)
    -   [[3.3] [Remove (prune) a USE flag]](#Remove_.28prune.29_a_USE_flag)
-   [[4] [See also]](#See_also)
-   [[5] [References]](#References)

### [Invocation]

See [euse \--help] for a complete listing of all invocation options:

`user `[`$`]`euse --help `

    euse (0.5.1-r1)

    Syntax: euse <option> [suboptions] [useflaglist]

    Options: -h, --help           - show this message
             -V, --version        - show version information
             -i, --info           - show descriptions for the given useflags
             -I, --info-installed - show descriptions for the given useflags and
                                    their current impact on the installed system
             -g, --global         - show only global use flags (suboption)
             -l, --local          - show only local use flags (suboption)
             -a, --active         - show currently active useflags and their origin
             -E, --enable         - enable the given useflags
             -D, --disable        - disable the given useflags
             -R, --remove         - remove all references to the given flags from
                                    make.conf and package.use to revert to default
                                    settings
             -P, --prune          - alias for --remove
             -p, --package        - used with -E, -D, and -R to apply to a
                                    specific package only

    Notes: euse currently works for global flags defined
           in make.globals, make.defaults, make.conf, use.force, and use.mask
           and local flags defined in package.use and individual package ebuilds.
           It might have issues with cascaded profiles. If multiple options are
           specified only the last one will be used.

** Note**\
The information provided by [euse \--help] is currently out of date^[\[1\]](#cite_note-1)^. (2021-10)

### [Viewing USE flags]

The [euse -a] command shows the current active USE flags and and where they are activated.

There are 7 \"columns\" that [euse] uses to show whether a flag is set/unset and where the flag has been set. Upper case for set, lower case for unset:

-   +/-: active or not
-   \"E\": set in the **E**nvironment
-   \"C\": set in [make.**C**onf]
-   \"D\": set in [make.**D**efaults]
-   \"G\": set in [make.**G**lobals]
-   \"F\": set in use.force
-   \"m\": flipped in use.mask

Full positive values would be `[+ECDGFm]`, full negative values would be `[-ecdgfM]`, full missing values would be `[-      ]`.

Example [euse -a] output (truncated):

`user `[`$`]`euse -a`

    [...]
    flac                [+  D   ]
    fortran             [+  D   ]
    fuse                [-      ] (fuse)
    gbm                 [-      ] (archive)
    gdbm                [+  D   ]
    gif                 [+  D   ]
    gnutls              [-      ] (gnutls)
    gpm                 [+  D   ]
    gtk                 [+  D   ]
    gui                 [+  D   ]
    hdri                [+ C    ]
    heif                [+ C    ]
    hpcups              [+ C    ]
    hwaccel             [-      ] (hwaccel)
    iconv               [+  D   ]
    [...]

Similarly the [euse -a -g] command is used to view *active* global USE flags. The [euse -a -l] command does the same for active local USE flags. `-g` and `-l` are sub-options to [euse] and need an option before them (like `-a`) to function correctly.

### [][Setting, and unsetting USE flags]

[euse] is able to set, unset, or remove USE flags from [make.conf]. The commands used for this are [euse -E flagname] (enable a flag), [euse -D flagname] (disable a flag), and [euse -P flagname] (remove, or \"prune\", a flag).

** Warning**\
Do not use the [euse -E] or [euse -D] commands by themselves (without a flag). **It will set/unset ALL USE flags** in [/etc/portage/make.conf]. Although a backup is kept at [/etc/portage/make.conf.euse_backup], please be careful while using [euse -E] or [euse -D]!

#### [Enabling a USE flag]

Use the `-E` option to *enable* a USE flag.

`root `[`#`]`euse -E 3dfx`

    /etc/portage/make.conf was modified, a backup copy has been placed at /etc/portage/make.conf.euse_backup

The [/etc/portage/make.conf] file looks like so after the command was run:

[FILE] **`make.conf`After enabling the 3dfx USE flag**

    USE="alsa acpi apache2 -arts cups cdr crypt cscope -doc fbcon \
         firefox gd gif gimpprint gnome gpm gstreamer gtkhtml imlib \
         innodb -java javascript jpeg libg++ libwww mad mbox md5sum \
         mikmod mmx motif mpeg mpeg4 mysql ncurses nvidia \
         ogg odbc offensive opengl pam pdflib perl png python \
         quicktime readline sdl spell sse ssl svga tcltk tiff truetype usb \
         vanilla X xosd xv xvid x86 zlib 3dfx"

#### [Disabling a USE flag]

Use the `-D` option to *disable* a USE flag.

`root `[`#`]`euse -D 3dfx`

    /etc/portage/make.conf was modified, a backup copy has been placed at /etc/portage/make.conf.euse_backup

The example [/etc/portage/make.conf] file, after the command:

[FILE] **`make.conf`After disabling the 3dfx USE flag**

    USE="alsa acpi apache2 -arts cups cdr crypt cscope -doc fbcon \
         firefox gd gif gimpprint gnome gpm gstreamer gtkhtml imlib \
         innodb -java javascript jpeg libg++ libwww mad mbox md5sum \
         mikmod mmx motif mpeg mpeg4 mysql ncurses nvidia \
         ogg odbc offensive opengl pam pdflib perl png python \
         quicktime readline sdl spell sse ssl svga tcltk tiff truetype usb \
         vanilla X xosd xv xvid x86 zlib -3dfx"

** Note**\
[euse -D] does not *remove* flags from [/etc/portage/make.conf], but adds a `-` (minus) before a flag to unset it. Use the `-P` [(prune) option](#Remove_.28prune.29_a_USE_flag) to remove a flag. Alternatively, clean up the file manually in a text editor.

** Tip**\
A disabled USE flag is not the same as the absence of the flag in [make.conf]. A disabled use flag will actively disable features, whereas not listing a flag at all will use the default - enabled or disabled - as set by the package maintainer.

#### [][Remove (prune) a USE flag]

Use the `-P` (prune) option to *remove* a USE flag.

`root `[`#`]`euse -P 3dfx`

The example [/etc/portage/make.conf] file, after the command:

[FILE] **`make.conf`After removing the 3dfx USE flag**

    USE="alsa acpi apache2 -arts cups cdr crypt cscope -doc fbcon \
         firefox gd gif gimpprint gnome gpm gstreamer gtkhtml imlib \
         innodb -java javascript jpeg libg++ libwww mad mbox md5sum \
         mikmod mmx motif mpeg mpeg4 mysql ncurses nvidia \
         ogg odbc offensive opengl pam pdflib perl png python \
         quicktime readline sdl spell sse ssl svga tcltk tiff truetype usb \
         vanilla X xosd xv xvid x86 zlib"

## [See also]

-   [Gentoolkit](https://wiki.gentoo.org/wiki/Gentoolkit "Gentoolkit") --- a suite of tools to ease the administration of a Gentoo system, and [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") in particular.
-   [Useful_Portage_tools](https://wiki.gentoo.org/wiki/Useful_Portage_tools "Useful Portage tools") --- provides a list of Gentoo-specific system management tools, notably for [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), available in the [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").

## [References]

1.  [[[↑](#cite_ref-1)] [[https://bugs.gentoo.org/500940](https://bugs.gentoo.org/500940)]]