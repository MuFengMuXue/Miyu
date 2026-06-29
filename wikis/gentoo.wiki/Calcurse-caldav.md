[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Calcurse&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[[]][Home](https://www.calcurse.org/)

[[]][Package information](https://packages.gentoo.org/packages/app-office/calcurse)

[[]][GitWeb](https://git.calcurse.org/calcurse.git/)

[[]][Official documentation (calcurse)](https://www.calcurse.org/files/manual.html)

[[]][Official documentation (calcurse-caldav)](https://www.calcurse.org/files/calcurse-caldav.html)

calcurse is a TUI calendar and scheduling application. It supports hooks, CalDAV, TODO items, and more.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [CalDAV syncing]](#CalDAV_syncing)

## [Installation]

### [USE flags]

### [USE flags for] [app-office/calcurse](https://packages.gentoo.org/packages/app-office/calcurse) [[]] [A text-based calendar and scheduling application]

  --------------------------------------------------------- ----------------------------------------------------------------------------------------------------------
  [`caldav`](https://packages.gentoo.org/useflags/caldav)   Support CalDAV
  [`doc`](https://packages.gentoo.org/useflags/doc)         Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  --------------------------------------------------------- ----------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-03 09:25] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-office/calcurse`

## [Configuration]

### [CalDAV syncing]

To sync from a CalDAV server, first ensure calcurse is built with the `caldav` USE flag enabled.

Next, is a basic configuration file for syncing with CalDav:

[FILE] **`~/.config/calcurse/caldav/config`**

    [General]
    Hostname = example.com:8443
    Path = /calendars/larry/default/
    AuthMethod = basic
    InsecureSSL = No
    HTTPS = Yes
    SyncFilter = cal,todo
    DryRun = no

    [Auth]
    Username = larry@example.com
    Password = SuperSecretPassword

** Note**\
It is generally recommended to not hardcode passwords into plaintext files. calcurse-caldav supports getting the password from a command, via `PasswordCommand`, similar to [aerc].