[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-DMenu&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=DMenu "DMenu (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=DMenu/tr "DMenu (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=DMenu/ru "DMenu (100% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Tips & Tricks]](#Tips_.26_Tricks)
    -   [[2.1] [warning: no locale support]](#warning:_no_locale_support)

# [Overview]

dmenu is a dynamic menu for X, originally designed for dwm. It manages large numbers of user-defined menu items efficiently.

\

# [][Tips & Tricks]

## [warning: no locale support]

Sometimes for no apparent reason users face the following dmenu problem:

A. When calling dmenu from a key binding in their environment dmenu comes up but when they continue to select anything in dmenu, it disappears from the screen and does not execute anything. B. Trying to start dmenu from the terminal, the error \"warning: no locale support\" appears.

Assuming that you have correctly set up your system\'s LOCALE settings, here is a simple solution to this problem:

Edit file **/usr/bin/dmenu_run** and add a line setting your LANG variable to your actual language locale before the line that calls dmenu:

    #!/bin/sh
    LANG="en_GB.UTF-8"                                 <-- Change it according to your locale.
    dmenu_path | dmenu "$@" | $