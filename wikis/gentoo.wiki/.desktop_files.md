[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (no intro, etc.). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

**.desktop** is a XDG specification designed to allow a standardized way of configuring a program\'s integration into a desktop environment, i.e., how it appears in the desktop environment\'s menu, how it should be launched, etc.

## Contents

-   [[1] [Syntax validation for .desktop files]](#Syntax_validation_for_.desktop_files)
-   [[2] [Update .desktop file database]](#Update_.desktop_file_database)
-   [[3] [Executable bit in .desktop files]](#Executable_bit_in_.desktop_files)
    -   [[3.1] [Executable bit on Ubuntu systems]](#Executable_bit_on_Ubuntu_systems)
-   [[4] [Ideas / Todo]](#Ideas_.2F_Todo)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

### [Syntax validation for .desktop files]

The [official validation tool](https://www.freedesktop.org/wiki/Software/desktop-file-utils/) for [.desktop] files is distributed with the package [[[dev-util/desktop-file-utils]](https://packages.gentoo.org/packages/dev-util/desktop-file-utils)[]]

`user `[`$`]`desktop-file-validate yourfile.desktop`

### [Update .desktop file database]

The [[[dev-util/desktop-file-utils]](https://packages.gentoo.org/packages/dev-util/desktop-file-utils)[]] package also provides the [update-desktop-database] command which can update the desktop file database when making changes to [.desktop] files. This is useful for updating the desktop environments application menu for example.

### [Executable bit in .desktop files]

[.desktop] files in [/usr/share/applications/] should have consistent executable bits.

As of 2017-06-16 many ebuilds (mostly KDE) create executable [.desktop files] ([[[bug #621966]](https://bugs.gentoo.org/show_bug.cgi?id=621966)[]]).

Look for executable [.desktop] files on the system with:

`user `[`$`]`find /usr/share/applications/ -executable -type f`

Please report any violations upstream.

#### [Executable bit on Ubuntu systems]

[The Ubuntu Security Policy](https://wiki.ubuntu.com/SecurityTeam/Policies#Execute-Permission_Bit_Required) makes use of executable bits:

[CODE]

    Applications, including desktops and shells, must not run executable code from files when they are both:

        lacking the executable bit
        located in a user's home directory or temporary directory.

    The GNOME or KDE MIME type handlers must not circumvent this principle.

    This includes *.desktop, *.jar, and *.exe files.

        Look for .desktop files with MimeType= and Exec= lines that do not use "cautious-launcher"

This does not apply to software which is installed via Gentoo ebuilds. Software should not ship a .desktop file with executable bit. The user can set the bit on demand where it is needed.

### [][Ideas / Todo]

-   we could check for the x bit in [https://gitweb.gentoo.org/proj/portage.git/tree/lib/portage/util/\_desktop_entry.py](https://gitweb.gentoo.org/proj/portage.git/tree/lib/portage/util/_desktop_entry.py)
-   In the past there were discussions about **requiring** them to be executable: [https://commit-digest.org/issues/2009-02-08/](https://commit-digest.org/issues/2009-02-08/)
-   2017-06-18 [Jonas Stein (Jstein) ](https://wiki.gentoo.org/wiki/User:Jstein "User:Jstein") asked on the [freedesktop mailing list](https://lists.freedesktop.org/archives/xdg/2017-June/thread.html#13920) about the [.desktop] file.
-   KDE: \"Note: Since KDE 4.3, there are more restrictions on authorized desktop files to prevent users from inadvertently running trojan desktop files. Your application launchers should have the executable bit set to prevent issues.\" source: [kde.org](https://api.kde.org/4.x-api/kdelibs-apidocs/kdecore/html/classKDesktopFile.html#ab9222da1ca239fc3847d31833bc45552)
-   Xfce: please see [[[bug #465740]](https://bugs.gentoo.org/show_bug.cgi?id=465740)[]] about thunar behavior

## [Troubleshooting]

Report bugs in **desktop-file-validate** on [https://gitlab.freedesktop.org/xdg/desktop-file-utils/issues](https://gitlab.freedesktop.org/xdg/desktop-file-utils/issues)

-   [Validation in some cases seems not correct \...](https://forums.gentoo.org/viewtopic-t-1065444-start-5.html) (should be reported upstream)
-   \"desktop-file-validate claims OnlyShowIn is deprecated\" [https://gitlab.freedesktop.org/xdg/desktop-file-utils/issues/52](https://gitlab.freedesktop.org/xdg/desktop-file-utils/issues/52)

## [See also]

-   [Notes_on_ebuilds_with_GUI](https://wiki.gentoo.org/wiki/Notes_on_ebuilds_with_GUI "Notes on ebuilds with GUI")

## [External resources]

-   [https://devmanual.gentoo.org/eclass-reference/desktop.eclass](https://devmanual.gentoo.org/eclass-reference/desktop.eclass)