**Resources**

[[]][Home](https://gitea.io/)

[[]][Package information](https://packages.gentoo.org/packages/www-apps/gitea)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Gitea "wikipedia:Gitea")

[[]][GitHub](https://github.com/go-gitea/gitea)

[[]]This article has some todo items:\

-

[MariaDB configuration](#Configuration)

[PostgreSQL configuration](#Configuration)

[Services: runit](#Service)

**Gitea** is painless self-hosted [git](https://wiki.gentoo.org/wiki/Git "Git") service, a fork of gogs.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [Systemd]](#Systemd)
-   [[3] [Usage]](#Usage)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

Gitea requires the use of a database backend, the following are supported:

-   [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB")/MySQL
-   [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL")
-   SQLite *\<- recommended for small, private installations*

### [USE flags]

### [USE flags for] [www-apps/gitea](https://packages.gentoo.org/packages/www-apps/gitea) [[]] [A painless self-hosted Git service]

  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+acct`](https://packages.gentoo.org/useflags/+acct)           User and group management via acct-\*/git packages
  [`+filecaps`](https://packages.gentoo.org/useflags/+filecaps)   Use Linux file capabilities to control privilege rather than set\*id (this is orthogonal to USE=caps which uses capabilities at runtime e.g. libcap)
  [`gogit`](https://packages.gentoo.org/useflags/gogit)           (EXPERIMENTAL) Use go-git variants of Git commands.
  [`pam`](https://packages.gentoo.org/useflags/pam)               Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`pie`](https://packages.gentoo.org/useflags/pie)               Build programs as Position Independent Executables (a security hardening technique)
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)         Add support for sqlite - embedded sql database
  --------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-06 01:04] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask www-apps/gitea`

## [Configuration]

### [Files]

-   [/etc/gitea/app.ini] - User configuration file, see [[[bug #714844]](https://bugs.gentoo.org/show_bug.cgi?id=714844)[]]

<!-- -->

-   [/etc/gitea/custom/conf/app.ini] - Recommanded file to edit as said by the documentation inside app.ini (see above).

\
The path does not exist, create it:

\

`root `[`#`]`mkdir -p /etc/gitea/custom/conf`

\

** Warning**\
Do not, as explained in app.ini, copy the whole file to [/etc/gitea/custom/conf/app.ini], instead the user need to picks up what is needed. Look-up for the proper parameters on the [gitea cheat-sheet](https://docs.gitea.com/administration/config-cheat-sheet) page.

### [Service]

#### [OpenRC]

Starting *gitea* in the background:

`root `[`#`]`rc-service gitea start`

Current status of *gitea* service:

`root `[`#`]`rc-service gitea status`

Starting automatically at system boot:

`root `[`#`]`rc-update add gitea default`

\

#### [Systemd]

Starting *gitea* in the background:

`root `[`#`]`systemctl start gitea`

Current status of *gitea* service:

`root `[`#`]`systemctl status gitea`

Starting automatically at system boot:

`root `[`#`]`systemctl enable gitea`

## [Usage]

Start and/or enable **gitea** service.

The web interface should be available at [http://localhost:3000/](http://localhost:3000/), when running at first time, it should be redirected to [http://localhost:3000/install](http://localhost:3000/install).

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose www-apps/gitea`

## [[] See also]

-   [Forgejo](https://wiki.gentoo.org/wiki/Forgejo "Forgejo") --- a fork of [Gitea].

## [External resources]

-   [ArchWiki Gitea](https://wiki.archlinux.org/index.php/Gitea#Usage) - can be helpful while configuration sections is incomplete on Gentoo wiki
-   [Official documentation](https://docs.gitea.io/)