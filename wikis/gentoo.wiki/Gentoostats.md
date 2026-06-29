**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

**Resources**

[[]][GitWeb](https://gitweb.gentoo.org/proj/gentoostats.git)

[**gentoostats**](https://soc.dev.gentoo.org/gentoostats/static/about.html) can collect several statistics from Gentoo machines. It was a [Google Summer of Code 2011 project](https://www.google-melange.com/gsoc/project/google/gsoc2011/vh4x0r/26001).

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Sending statistics]](#Sending_statistics)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Viewing statistics]](#Viewing_statistics)

## [Installation]

Gentoostats is available through the *betagarden* [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"). The package is unstable, so add it to the [/etc/portage/package.accept_keywords] file.

`root `[`#`]`eselect repository enable betagarden`

`root `[`#`]`emerge --ask gentoostats`

When first installed, the program created a unique identifier for your machine. Use this identifier later to view the statistics of your machine. The identifier is stored in [/etc/gentoostats/auth.cfg].

## [Configuration]

### [Sending statistics]

Sending statistics from a machine is simple. You can control which statistics are sent by editing [/etc/gentoostats/payload.cfg].

`root `[`#`]`gentoostats-send`

## [Usage]

### [Viewing statistics]

The [website](https://soc.dev.gentoo.org/gentoostats/) can be used to view some aggregated statistics. To view the stats in JSON (instead of the regular HTML view), you have to add the \"Accept:application/json\" HTTP Header to your request. For instance:

`user `[`$`]`curl -H "Accept:application/json" http://soc.dev.gentoo.org/gentoostats/arch`

You can also use the command-line interface to request JSON formatted statistics. For instance to view the statistics available on [[[sys-kernel/gentoo-sources]](https://packages.gentoo.org/packages/sys-kernel/gentoo-sources)[]] or view what different architectures are used:

`root `[`#`]`gentoostats-cli search -p gentoo-sources`

`root `[`#`]`gentoostats-cli list arch`

The following options are available:

-   search
    -   *-c*, *\--category*
    -   *-p\',* \--package
    -   *-v\',* \--version
    -   *-r\',* \--repo
    -   *\--min_hosts*
    -   *\--max_hosts*
-   list
    -   *arch*
    -   *feature*
    -   *lang*
    -   *mirror*
    -   *repo*
    -   *package*
    -   *use*