[[]][Home](http://www.dict.org/)

[[]][Package information](https://packages.gentoo.org/packages/app-text/dictd)

[[]][Wikipedia](https://en.wikipedia.org/wiki/DICT "wikipedia:DICT")

**[dictd]** is a server implementing [the DICT protocol](https://en.wikipedia.org/wiki/DICT "wikipedia:DICT"), allowing clients to search dictionaries.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Dictionaries]](#Dictionaries)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Server configuration]](#Server_configuration)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Clients]](#Clients)
        -   [[3.1.1] [dict]](#dict)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-text/dictd](https://packages.gentoo.org/packages/app-text/dictd) [[]] [Dictionary Client/Server for the DICT protocol]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`dbi`](https://packages.gentoo.org/useflags/dbi)           Enable dev-db/libdbi (database-independent abstraction layer) support
  [`judy`](https://packages.gentoo.org/useflags/judy)         Build Judy-based (dev-libs/judy) plugin implementing fast \"exact\" and especially \"lev\" strategies
  [`minimal`](https://packages.gentoo.org/useflags/minimal)   Don\'t build server but dict client, dictzip and dictfmt only.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-text/dictd]](https://packages.gentoo.org/packages/app-text/dictd)[]]:

`root `[`#`]`emerge --ask app-text/dictd`

### [Dictionaries]

At least one dictd dictionary package must be installed before starting the server. Dictionaries in the dict format can be found in the [app-dicts](https://packages.gentoo.org/categories/app-dicts) category with the prefixes `dictd-` and `freedict-`.

The WordNet dictionary is available as [[[app-dicts/dictd-wn]](https://packages.gentoo.org/packages/app-dicts/dictd-wn)[]].

Other dictd dictionary packages are available on [GURU](https://wiki.gentoo.org/wiki/Project:GURU/Information_for_End_Users "Project:GURU/Information for End Users"). The [[[app-dicts/dictd-meta]](https://packages.gentoo.org/packages/app-dicts/dictd-meta)[]] package installs the following packages:

-   [[[app-dicts/dictd-devils]](https://packages.gentoo.org/packages/app-dicts/dictd-devils)[]] - The Devil\'s Dictionary
-   [[[app-dicts/dictd-elements]](https://packages.gentoo.org/packages/app-dicts/dictd-elements)[]] - Jay Kominek\'s database of the elements
-   [[[app-dicts/dictd-foldoc]](https://packages.gentoo.org/packages/app-dicts/dictd-foldoc)[]] - The Free On-line Dictionary of Computing
-   [[[app-dicts/dictd-gazetteer]](https://packages.gentoo.org/packages/app-dicts/dictd-gazetteer)[]] - The original U.S. Gazetteer Place and Zipcode Files
-   [[[app-dicts/dictd-gcide]](https://packages.gentoo.org/packages/app-dicts/dictd-gcide)[]] - Collaborative International Dictionary of English (incl. Webster 1913)
-   [[[app-dicts/dictd-jargon]](https://packages.gentoo.org/packages/app-dicts/dictd-jargon)[]] - The Jargon File
-   [[[app-dicts/dictd-misc]](https://packages.gentoo.org/packages/app-dicts/dictd-misc)[]] - Hitchcock\'s and Easton\'s Bible Dictionaries
-   [[[app-dicts/dictd-vera]](https://packages.gentoo.org/packages/app-dicts/dictd-vera)[]] - Virtual Entity of Relevant Acronyms
-   [[[app-dicts/dictd-wn]](https://packages.gentoo.org/packages/app-dicts/dictd-wn)[]] - WordNet

A thesaurus is also available on GURU: [[[app-dicts/dictd-moby-thesaurus]](https://packages.gentoo.org/packages/app-dicts/dictd-moby-thesaurus)[]].

The freedict packages install [.tar.gz files available on SourceForge](https://freedict.sourceforge.net/download/linux/); additional FreeDict dictionaries, in .tar.xz format, are [available for downloading from freedict.org](https://freedict.org/downloads/#dictionary-downloads). To install one of these dictionaries, run:

`root `[`#`]`tar -xvJf <name>.xz -C /usr/share/dict/ --strip-components=1 --exclude=COPYING`

and then restart the dictd service.

## [Configuration]

### [Server configuration]

[/etc/dict/dict.conf] lists dictionary servers, one per line. By default, it contains:

[FILE] **`/etc/dict/dict.conf`**

    # This is the configuration file for dict.
    # Usually all you will ever need here is the server keywords.
    # Refer to the dict manpage for other options.
    # It will only check the second server if the first fails
    server localhost
    server dict.org

Refer to the [[[dict(1)]](https://man.archlinux.org/man/dict.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page for possible configuration options.

[/etc/dict/dictd.conf] configures individual dictionaries; refer to [[[dictd(8)]](https://man.archlinux.org/man/dictd.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] for possible configuration options. On OpenRC systems, this file should not need to be edited manually - even if installing new dictionaries manually rather than via a package, the new dictionaries should be configured by the service script automatically upon (re-)starting.

### [Service]

#### [OpenRC]

Add the service to the default runlevel:

`root `[`#`]`rc-update add dictd default`

Start the service:

`root `[`#`]`rc-service dictd start`

If additional dictionaries are added, be sure to restart the service:

`root `[`#`]`rc-service dictd restart`

#### [systemd]

To have the dictd daemon start when the system starts:

`root `[`#`]`systemctl enable dictd.service`

To start the dictd daemon immediately:

`root `[`#`]`systemctl start dictd.service`

To check if the service has started:

`root `[`#`]`systemctl status dictd.service`

To restart the service:

`root `[`#`]`systemctl restart dictd.service`

## [Usage]

### [Clients]

The [[[app-text/dictd]](https://packages.gentoo.org/packages/app-text/dictd)[]] package provides the [[[dict(1)]](https://man.archlinux.org/man/dict.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] client, but other clients include [[[app-dicts/gnome-dictionary]](https://packages.gentoo.org/packages/app-dicts/gnome-dictionary)[]], [[[xfce-extra/xfce4-dict]](https://packages.gentoo.org/packages/xfce-extra/xfce4-dict)[]], and `dictionary.el` in [[[app-editors/emacs]](https://packages.gentoo.org/packages/app-editors/emacs)[]] 28 and later.

#### [dict]

To search for the word \'penguin\':

`user `[`$`]`dict penguin`

To list available databases:

`user `[`$`]`dict -D`

    Databases available:
     gcide          The Collaborative International Dictionary of English v.0.48
     moby-thesaurus Moby Thesaurus II by Grady Ward, 1.0
     wn             WordNet (r) 3.0 (2006)

To search for the word \'penguin\' in a specific database:

`user `[`$`]`dict -d gcide penguin`

## [External resources]

-   [FreeDict](https://freedict.org/) - free bilingual dictionaries