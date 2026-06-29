This page contains [[changes](https://wiki.gentoo.org/index.php?title=Mirrorselect&oldid=1410638&diff=1432115)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Mirrorselect/de "Mirrorselect/de (12% translated)")
-   [English]

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")][Project](https://wiki.gentoo.org/wiki/Project:Portage-Tools "Project:Portage-Tools")

[[]][GitWeb](https://gitweb.gentoo.org/proj/mirrorselect.git)

The [mirrorselect] program provides a nice interface to set the [`GENTOO_MIRRORS`](https://wiki.gentoo.org/wiki/GENTOO_MIRRORS "GENTOO MIRRORS") variable and the [Gentoo rsync mirror](https://www.gentoo.org/support/rsync-mirrors/).

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Select the Gentoo source mirror(s)]](#Select_the_Gentoo_source_mirror.28s.29)
    -   [[2.2] [Options]](#Options)
    -   [[2.3] [Select the Gentoo rsync mirror]](#Select_the_Gentoo_rsync_mirror)
-   [[3] [Troubleshooting]](#Troubleshooting)
-   [[4] [See also]](#See_also)

## [Installation]

### [Emerge]

Install [[[app-portage/mirrorselect]](https://packages.gentoo.org/packages/app-portage/mirrorselect)[]]:

`root `[`#`]`emerge --ask app-portage/mirrorselect`

## [Usage]

### [][Select the Gentoo source mirror(s)]

Interactively find [Gentoo source mirrors](https://www.gentoo.org/downloads/mirrors/) (and set or update the [`GENTOO_MIRRORS`](https://wiki.gentoo.org/wiki/GENTOO_MIRRORS "GENTOO MIRRORS") variable):

`root `[`#`]`mirrorselect -i`

    * Modifying /etc/portage/make.conf with new mirrors...
            Reading make.conf
            Moving to /etc/portage/make.conf.backup
            Writing new /etc/portage/make.conf
    * Done.

Notice that a backup copy of [/etc/portage/make.conf] will be created by [mirrorselect] before updating it.

Users can also specify a country (United States of America, for example):

`root `[`#`]`mirrorselect -i -c "United States (USA)"`

The following command finds the 3 fastest servers by downloading 100K from each; it will use all available mirrors in the list:

`root `[`#`]`mirrorselect -s3 -b10 -D`

### [Options]

Please consider using one of these additional options to limit the available mirrors in the list it tests.

`user `[`$`]`mirrorselect --help`

    Usage: mirrorselect [options]

    examples:

             automatic:
                     # mirrorselect -s5
                     # mirrorselect -s3 -b10 -o >> /mnt/gentoo/etc/portage/make.conf
                     # mirrorselect -D -s4

             interactive:
                     # mirrorselect -i -r

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit

      Main modes:
        -a, --all_mirrors   This will present a list of all filtered search
                            results to make it possible to select mirrors you wish
                            to use.  For the -r, --rsync option, it will select
                            the rotation server only. As multiple rsync URL's are
                            not supported.
        -D, --deep          Deep mode. This is used to give a more accurate speed
                            test. It will download a 100k file from each server.
                            Because of this you should only use this option if you
                            have a good connection.
        -i, --interactive   Interactive Mode, this will present a list to make it
                            possible to select mirrors you wish to use.

      Server type selection (choose at most one):
         -c COUNTRY, -country COUNTRY
                            only use mirrors from the specified country NOTE:
                            Names with a space must be quoted eg.:  -c 'South
                            Korea'
        -F, --ftp           ftp only mode. Will not consider hosts of other types.
        -H, --http          http only mode. Will not consider hosts of other types
        -S, --https         https only mode. Will not consider hosts of other
                            types
        -r, --rsync         rsync mode. Allows you to interactively select your
                            rsync mirror. Requires -i or -a to be used.
         -R REGION, -region REGION
                            only use mirrors from the specified region NOTE: Names
                            with a space must be quoted eg.:  -R 'North America'
        -4, --ipv4          only use IPv4
        -6, --ipv6          only use IPv6

      Other options:
         -b BLOCKSIZE, -blocksize BLOCKSIZE
                            This is to be used in automatic mode and will split
                            the hosts into blocks of BLOCKSIZE for use with
                            netselect. This is required for certain routers which
                            block 40+ requests at any given time. Recommended
                            parameters to pass are:  -s 3  -b 10
         -d VERBOSITY, -debug VERBOSITY
                            debug mode, pass in the debug level [1-9]
         -f FILE, -file FILE
                            An alternate file to download for deep testing. Please
                            choose the file carefully as to not abuse the system
                            by selecting an overly large size file.  You must also
                            use the -m, --md5 option.
         -m MD5, --md5=MD5   An alternate file md5sum value used to compare the
                            downloaded file against for deep testing.
        -o, --output        Output Only Mode, this is especially useful when being
                            used during installation, to redirect output to a file
                            other than /etc/portage/make.conf
         -P PROXY, -proxy PROXY
                            Proxy server to use if not the default proxy in the
                            environment
        -q, --quiet         Quiet mode
         -s SERVERS, -servers SERVERS
                            Specify Number of servers for Automatic Mode to
                            select. this is only valid for download mirrors. If
                            this is not specified, a default of 1 is used.
         -t TIMEOUT, -timeout TIMEOUT
                            Timeout for deep mode. Defaults to 10 seconds.
         -e EXCLUDE, -exclude EXCLUDE
                            Exclude host from mirrors list.

### [Select the Gentoo rsync mirror]

** Warning**\
TODO: These instructions will only work if `sync-uri` is not already set in [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")], otherwise it will simply add duplicate entries.

** Note**\
[Gentoo documentation](https://www.gentoo.org/support/rsync-mirrors/) states:\
\
Gentoo is hosted by many mirrors around the globe. Selecting a mirror that is geographically near may help speed up repository syncs.

The default configuration of the [Gentoo repository](https://gitweb.gentoo.org/repo/gentoo.git/tree/) comes from [[[sys-apps/portage]](https://packages.gentoo.org/packages/sys-apps/portage)[]] and is located at [/usr/share/portage/config/repos.conf]. However settings in [[/etc/portage/repos.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf "/etc/portage/repos.conf")] override it.

[mirrorselect] will not create the [[/etc/portage/repos.conf/gentoo.conf](https://wiki.gentoo.org/wiki//etc/portage/repos.conf/gentoo.conf "/etc/portage/repos.conf/gentoo.conf")] file automatically. If that file does not exist, [mirrorselect] will default to using the old [make.conf] [`SYNC`](https://wiki.gentoo.org/wiki/SYNC "SYNC") variable which has been deprecated. In order to avoid this make sure Portage is up to date and copy the [repos.conf] file from Portage\'s [/usr] (library) location to the [/etc] (configuration) location:

`root `[`#`]`emerge --ask --update sys-apps/portage`

`root `[`#`]`mkdir /etc/portage/repos.conf `

`root `[`#`]`cp /usr/share/portage/config/repos.conf /etc/portage/repos.conf/gentoo.conf `

** Note**\
For additional [repos.conf] documentation and configuration please refer to [Portage/Sync#Portage_configuration](https://wiki.gentoo.org/wiki/Project:Portage/Sync#Portage_configuration "Project:Portage/Sync")

Then find a [Gentoo rsync mirror](https://www.gentoo.org/support/rsync-mirrors/) with [mirrorselect] (make sure to use `sync-type = rsync`):

`root `[`#`]`mirrorselect -i -r -o >> /etc/portage/repos.conf/gentoo.conf`

Just navigate to the mirrors of choice and press [Space] to select one (or more) mirrors.

## [Troubleshooting]

In case of problems with rsync mirror it might help to check the [mirrorstats](https://mirrorstats.gentoo.org/rsync/).

## [See also]

-   [Handbook:Parts/Installation/Base#Optional: Selecting mirrors](https://wiki.gentoo.org/wiki/Handbook:Parts/Installation/Base#Optional:_Selecting_mirrors "Handbook:Parts/Installation/Base")
-   [Project:Infrastructure/Mirrors/Source](https://wiki.gentoo.org/wiki/Project:Infrastructure/Mirrors/Source "Project:Infrastructure/Mirrors/Source")
-   [Project:Infrastructure/Mirrors/Rsync](https://wiki.gentoo.org/wiki/Project:Infrastructure/Mirrors/Rsync "Project:Infrastructure/Mirrors/Rsync")