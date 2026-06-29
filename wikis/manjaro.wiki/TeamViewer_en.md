[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-TeamViewer&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=TeamViewer "TeamViewer (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=TeamViewer/tr "TeamViewer (36% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=TeamViewer/ru "TeamViewer (100% translated)")

## Contents

-   [[1] [Installing TeamViewer]](#Installing_TeamViewer)
    -   [[1.1] [Installing from the Arch User Respository(AUR)]](#Installing_from_the_Arch_User_Respository.28AUR.29)
-   [[2] [Tips & Tricks]](#Tips_.26_Tricks)
    -   [[2.1] [Connection is not ready]](#Connection_is_not_ready)
-   [[3] [See Also]](#See_Also)

\

[![200px-Teamviewer-logo-big.svg.png](/images/d/da/200px-Teamviewer-logo-big.svg.png)](//wiki.manjaro.org/index.php?title=File:200px-Teamviewer-logo-big.svg.png)

[Teamviewer](https://en.wikipedia.org/wiki/TeamViewer) is a proprietary software application for remote control, desktop sharing, online meetings, web conferencing and file transfer between computers.

\

# [Installing TeamViewer]

Teamviewer can be only be installed from source.

\

## [][Installing from the Arch User Respository(AUR)]

To install TeamViewer from the [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") using your favorite package manager or the command:

    pamac build teamviewer

# [][Tips & Tricks]

## [Connection is not ready]

If TeamViewer does not detect the teamviewerd deamon, you can reinstall the deamon by

    sudo teamviewer --daemon enable

If it\'s not enabled or started you can use

    systemctl enable teamviewerd

    systemctl start teamviewerd

\

\

# [See Also]

[AUR:TeamViewer](https://aur.archlinux.org/packages/teamviewer/) [The TeamViewer Community](https://community.teamviewer.com)