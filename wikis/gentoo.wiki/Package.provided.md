** Warning**\
Any issues caused by entries here are not Gentoo bugs and should be removed before seeking help. Gentoo dependencies exist for good reason and the project cannot support deviation.

The [/etc/portage/profile/package.provided] file can contain a list of packages (one per line) that Portage should assume have been provided. This is useful for porting to non-Linux systems. It is essentially a list that replaces the [emerge \--inject] syntax.

For example, to manage a copy of the 4.0 kernel, Portage can be told that sys-kernel/vanilla-sources-4.0.2 has been installed.

Portage will not attempt to update a package that is listed in [/etc/portage/profile/package.provided] file unless another package explicitly requires a version that is *newer* than what has been listed. Dependencies that are satisfied by [package.provided] entries may cause installed packages satisfying equivalent dependencies to be removed by [emerge \--depclean] actions (see the ACTIONS section of the emerge man page for more information).

## [Format]

-   Comments begin with `#` (no inline comments).
-   One `DEPEND` atom per line.
-   Relational operators are **not** allowed.
-   Must include a version.
-   USE flags and slot dependencies are not yet supported (See [[[bug #142941]](https://bugs.gentoo.org/show_bug.cgi?id=142941)[]])

## [Example]

[FILE] **`/etc/portage/profile/package.provided`package.provided example**

    # To take care of the kernel
    sys-kernel/vanilla-sources-4.0.2

    # To install a special copy of QT
    dev-qt/qtcore-5.4.1

    # To have modular X but packages want monolithic
    x11-base/xorg-x11-7.4-r2

## [External resources]

-   [https://forums.gentoo.org/viewtopic-t-1069622.html](https://forums.gentoo.org/viewtopic-t-1069622.html) --- Forum talk about drawbacks of package.provided