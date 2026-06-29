**Resources**

[[]][Home](https://apps.ankiweb.net/)

[[]][Official documentation](https://docs.ankiweb.net/#/)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/anki)

[[]][Bugs (upstream)](https://github.com/ankitects/anki/issues)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Anki_(software) "wikipedia:Anki (software)")

[[]][GitHub](https://github.com/ankitects/anki)

[[]][[#anki](ircs://irc.libera.chat/#anki)] ([[webchat](https://web.libera.chat/#anki)])

**Anki** is a flashcard memory training program that uses the science of spaced repetition to expedite the learning process and enhance recall^[\[1\]](#cite_note-1)^.

This article covers [Anki Desktop](https://github.com/ankitects/anki), the official desktop application. There\'s also an optional web synchronization service called [AnkiWeb](https://ankiweb.net/about).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
        -   [[1.1.1] [Optional features]](#Optional_features)
    -   [[1.2] [Flatpak]](#Flatpak)
    -   [[1.3] [Python Wheel]](#Python_Wheel)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
        -   [[2.1.1] [Files]](#Files)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Installation]

### [Emerge]

Install [[[app-misc/anki]](https://packages.gentoo.org/packages/app-misc/anki)[]] using [emerge]:

`root `[`#`]`emerge --ask app-misc/anki`

** Important**\
Anki depends on [[[dev-qt/qtwebengine]](https://packages.gentoo.org/packages/dev-qt/qtwebengine)[]], which requires ≥48GB of *available* RAM depending on [your `MAKEOPTS`](https://wiki.gentoo.org/wiki/Knowledge_Base:Emerge_out_of_memory#Decrease_number_of_parallel_compiler_processes_for_some_ebuilds "Knowledge Base:Emerge out of memory"). On a high core count system this dependency can be built in a reasonable amount of time, perhaps taking a few hours. On a budget quad core, building Anki can take the better part of a day. The RAM requirement can be satisfied with a [swap partition](https://wiki.gentoo.org/wiki/Swap "Swap") if needed, not just physical RAM. If emerge fails to build [[[app-misc/anki]](https://packages.gentoo.org/packages/app-misc/anki)[]] ensure that you have either enough physical RAM or a large enough swap partition to continue.

#### [Optional features]

Anki offers additional features that can be enabled by installing additional packages. These will be shown to the user after installing Anki. Some notable features are:

\- [[[dev-python/orjson]](https://packages.gentoo.org/packages/dev-python/orjson)[]]: Will (in theory) result in faster database operations.

### [Flatpak]

** Important**\
This method uses third party installation from Flathub (which can be potentially compromised by attackers) and therefore should not used in trusted environments.

Anki is also packaged as a Flatpak, which may be desirable since [[[app-misc/anki]](https://packages.gentoo.org/packages/app-misc/anki)[]] depends on [[[dev-python/PyQtWebEngine]](https://packages.gentoo.org/packages/dev-python/PyQtWebEngine)[]] to build.

The Anki flatpak is available from [Flathub](https://flathub.org/apps/details/net.ankiweb.Anki):

`user `[`$`]`flatpak install flathub net.ankiweb.Anki `

`user `[`$`]`flatpak run net.ankiweb.Anki `

### [Python Wheel]

Anki\'s beta version can be installed on both x86_64 and ARM systems using [pip](https://wiki.gentoo.org/wiki/Pip "Pip") rather easily. Refer to [Anki\'s documentation](https://betas.ankiweb.net/#via-pypipip) as for how do this.

## [Configuration]

### [Environment variables]

-   `ANKIDEV` - If set, additional logging messages will be printed to standard output and automatic backups will be disabled.^[\[2\]](#cite_note-env-2)^
-   `TRACESQL` - If set, SQL statements will be printed at execution time.^[\[2\]](#cite_note-env-2)^
-   `LOGTERM` - If set, messages bound for *collection2.log* will also be printed to standard output.^[\[2\]](#cite_note-env-2)^
-   `ANKI_PROFILE_CODE` - If set, Python profiling data will be sent to standard output upon exit.^[\[2\]](#cite_note-env-2)^

#### [Files]

-   [\$XDG_DATA_HOME/Anki2] - the main configuration directory^[\[3\]](#cite_note-3)^.

** Note**\
If Anki was installed [via Flatpak](https://wiki.gentoo.org/wiki/Anki#Flatpak "Anki"), the configuration files will be located in [\~/.var/app/net.ankiweb.Anki/] instead.

## [Usage]

### [Invocation]

`user `[`$`]`anki --help`

    usage: anki [OPTIONS] [file to import]

    Anki 2.1.15

    optional arguments:
      -h, --help            show this help message and exit
      -b BASE, --base BASE  path to base folder
      -p PROFILE, --profile PROFILE
                            profile name to load
      -l LANG, --lang LANG  interface language (en, de, etc)

## [Troubleshooting]

See the [official Linux Anki documentation](https://docs.ankiweb.net/platform/linux/installing.html) for Linux-specific issues.

## [External resources]

-   [AnkiWeb](https://ankiweb.net/about) -- The companion web service to the desktop Anki application.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://docs.ankiweb.net/background.html#background](https://docs.ankiweb.net/background.html#background)]]
2.  [[↑ ^[2.0](#cite_ref-env_2-0)^ ^[2.1](#cite_ref-env_2-1)^ ^[2.2](#cite_ref-env_2-2)^ ^[2.3](#cite_ref-env_2-3)^] [[https://github.com/ankitects/anki/blob/main/docs/development.md#environmental-variables](https://github.com/ankitects/anki/blob/main/docs/development.md#environmental-variables)]]
3.  [[[↑](#cite_ref-3)] [[https://docs.ankiweb.net/files.html#file-locations](https://docs.ankiweb.net/files.html#file-locations)]]