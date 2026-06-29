Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=LXQt_with_kwin/tr "kwin ile LXQt (10% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=LXQt_with_kwin/ru "LXQt с kwin (100% translated)")

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Optional: Remove OpenBox]](#Optional:_Remove_OpenBox)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Global Keyboard Shortcuts]](#Global_Keyboard_Shortcuts)

## [Installation]

**tip**

------------------------------------------------------------------------

KWinFT (KWin Fast-Track) is a drop-in replacement for KWin. It is provided in the AUR helping with the transition from X11 to Wayland.

If you like to try KWinFT replace the kwin package name in the command below this line with **kwinft**.

[user \$ ][ pamac install kwin systemsettings [COPY TO CLIPBOARD]]

\

### [Optional: Remove OpenBox]

If you had openbox installed, it can now be safely removed:

[user \$ ][ pamac remove openbox [COPY TO CLIPBOARD]]

\

(this will also remove obconf and any other dependencies)

As kwin comes with a builtin compositor you may want to remove compton/picom:

[user \$ ][ pamac remove compton picom [COPY TO CLIPBOARD]]

\

(this will also remove compton-conf and any other dependencies)

**note**

------------------------------------------------------------------------

Use of compton/picom with kwin is still possible. KDE\'s builtin compositor can be disabled in \"KDE Systemsettings\" (free choice!)

\

## [Configuration]

1.  Open LXQt Session Settings
2.  Select **kwin_x11** as window manager

<!-- -->

       <Screenshot TBD>

Logout or reboot and enjoy LXQt with kwin!

### [Global Keyboard Shortcuts]

**note**

------------------------------------------------------------------------

This article describes kwin specific shortcut configuration (e.g. \"Alt+Tab\" for the task switcher). LXQt does not change or manage those! For LXQt global shortcut configuration see [main article](//wiki.manjaro.org/index.php?title=LXQt#Global_Keyboard_Shortcuts "LXQt").

All kwin shortcuts are managed in **\~/.config/kglobalshortcutsrc**.

**warning**

------------------------------------------------------------------------

Editing this file can lead to non-working keys! You have been warned!

Search for the shortcut of choice and edit it. Alternatives are separated by comma (e.g. **Alt+Tab,Alt+Tab,...**).

**tip**

------------------------------------------------------------------------

Changes become effective on next login. (log out/in for testing)