**Resources**

[[]][Package information](https://packages.gentoo.org/packages/x11-misc/xdg-utils)

This article lists methods of setting [default applications], particularly in Linux [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") that follow [freedesktop.org](https://freedesktop.org/) standards and specifications. Note, however, that not all software and environments do so.

[MIME types](https://en.wikipedia.org/wiki/MIME "wikipedia:MIME") describe the kind of content a file contains, such as `text/plain`, `image/gif`, and `audio/mp3`. These types are often used to determine which applications should be used to open particular files.

## Contents

-   [[1] [Setting default applications]](#Setting_default_applications)
    -   [[1.1] [Via a file manager]](#Via_a_file_manager)
    -   [[1.2] [Via the desktop environment]](#Via_the_desktop_environment)
    -   [[1.3] [Via setting a MIME type\'s default application directly]](#Via_setting_a_MIME_type.27s_default_application_directly)
        -   [[1.3.1] [Using the xdg-\* suite of programs]](#Using_the_xdg-.2A_suite_of_programs)
        -   [[1.3.2] [Manually editing mimeapps.list files]](#Manually_editing_mimeapps.list_files)
    -   [[1.4] [Via the mailcap(5) file]](#Via_the_mailcap.285.29_file)
-   [[2] [See also]](#See_also)

## [Setting default applications]

### [Via a file manager]

In many cases it suffices to use a desktop\'s [file manager](https://wiki.gentoo.org/wiki/File_managers "File managers") to to set default applications for specific file types (e.g. via a right-click context menu); refer to the specific file manager manual.

### [Via the desktop environment]

Some desktop environments, like [GNOME](https://wiki.gentoo.org/wiki/GNOME "GNOME") or [KDE](https://wiki.gentoo.org/wiki/KDE "KDE"), allow setting default applications via their configuration systems.

In [XFCE](https://wiki.gentoo.org/wiki/XFCE "XFCE"), use [xfce4-mime-settings] from the [[[xfce-base/xfce4-settings]](https://packages.gentoo.org/packages/xfce-base/xfce4-settings)[]] package.

### [][Via setting a MIME type\'s default application directly]

#### [][Using the xdg-\* suite of programs]

The `xdg-*` suite of programs, such as [[[xdg-open(1)]](https://man.archlinux.org/man/xdg-open.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] and [[[xdg-mime(1)]](https://man.archlinux.org/man/xdg-mime.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")], can be used to query and manage the default applications for various MIME types. For details, refer to the [XDG/Software](https://wiki.gentoo.org/wiki/XDG/Software "XDG/Software") page.

#### [Manually editing mimeapps.list files]

[\$XDG_CONFIG_HOME/mimeapps.list] (previously, [\~/.config/mimeapps.list] and [\$XDG_DATA_HOME/applications/mimeapps.list]) is typically used to specify associations between MIME types and applications. The location of [mimeapps.list] files and their precedence is specified in the \"[Association between MIME types and applications](https://standards.freedesktop.org/mime-apps-spec/mime-apps-spec-1.0.html)\" freedesktop.org standard.

[FILE] **`~/.config/mimeapps.list`Set Qutebrowser as the default browser**

    x-scheme-handler/http=org.qutebrowser.qutebrowser.desktop
    x-scheme-handler/https=org.qutebrowser.qutebrowser.desktop

A particular desktop environment (DE) might also support [\$XDG_CONFIG_HOME/\$desktop-mimeapps.list], to allow associations to be set per-DE.

### [][Via the mailcap(5) file]

The [[[mailcap(5)]](https://man.archlinux.org/man/mailcap.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] file can be used by email software (and sometimes by other software) to specify associations between MIME types and applications. Refer to the man page for details.

## [See also]

-   [XDG/Base Directories](https://wiki.gentoo.org/wiki/XDG/Base_Directories "XDG/Base Directories") --- standard directories specified by [freedesktop.org](https://freedesktop.org) (formerly the [X Desktop Group](https://wiki.gentoo.org/wiki/XDG "XDG"))
-   [XDG/Software](https://wiki.gentoo.org/wiki/XDG/Software "XDG/Software") --- command-line programs for managing and using default applications for particular [MIME](https://en.wikipedia.org/wiki/MIME "wikipedia:MIME") types