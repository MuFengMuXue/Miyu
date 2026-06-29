**Resources**

[[]][Home](http://www.portagefilelist.de/)

[[]][Package information](https://packages.gentoo.org/packages/app-portage/pfl)

[[]][GitHub](https://github.com/portagefilelist/client)

**P**ortage **F**ile **L**ist (**PFL**) can be used to search for files (or strings) provided by packages that are not currently installed on a given system. This can be useful to find out what package to install given the name of a file from a desired tool. Optionally, the PFL tool can update the online PFL database from the list of locally installed files.

While most Linux distributions are provided as package archives of files to be installed, Gentoo is a metadistribution: the files to make up each package are generated on the user machine, just before installation, according to the current system configuration ([USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), [CFLAGS](https://wiki.gentoo.org/wiki/CFLAGS "CFLAGS") etc. see [make.conf](https://wiki.gentoo.org/wiki/Make.conf "Make.conf")). As each system\'s files are generated just before a package is installed, there is no fixed central reference of all the files that make up Gentoo. There are so many possible system configurations that it would be impractical to build such a list on a centralized system.

PFL gets around this by querying participating user\'s machines to determine lists of files generated upon installation. These lists are uploaded, anonymously and with the user\'s permission, to the PFL server, to allow anyone to query what packages can provide a file with a given name.

The PFL should reference most file names that can be installed by Portage, though in practice there may be exceptions.

[[equery](https://wiki.gentoo.org/wiki/Equery "Equery")] may be used to determine what package a locally installed file comes from. PFL may be used as an alternative, but only if a network connection is available.

** Tip**\
PFL searches for file **names**, so the actual name of a file installed by a package is needed to find that package. For example, searching the PFL for \"gnome\" will find some packages that are known to install a file named \"gnome\", but not [[[gnome-base/gnome]](https://packages.gentoo.org/packages/gnome-base/gnome)[]] itself. Searching for a package is possible with the [package search](https://www.portagefilelist.de/index.php?p=packages). There is also a [category search](https://www.portagefilelist.de/index.php?p=categories) available.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [e-file]](#e-file)
    -   [[2.2] [pfl]](#pfl)
-   [[3] [Scanned repositories]](#Scanned_repositories)
-   [[4] [Data policy]](#Data_policy)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [app-portage/pfl](https://packages.gentoo.org/packages/app-portage/pfl) [[]] [Searchable online file/package database for Gentoo]

  ----------------------------------------------------------------------- --------------------------------------------------------------------
  [`+network-cron`](https://packages.gentoo.org/useflags/+network-cron)   Adds a cron job which does a weekly submit of the package database
  ----------------------------------------------------------------------- --------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-21 18:40] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[app-portage/pfl]](https://packages.gentoo.org/packages/app-portage/pfl)[]] with the following command:

`root `[`#`]`emerge --ask app-portage/pfl`

## [Usage]

The package provides two cli commands. `e-file` and `pfl`

** Note**\
Mentioned commands and their properties do work with the latest version available. If an older version is used a command or property could be missing.

### [e-file]

The online database can be queried from the command-line to search for files installed by ebuilds. Lets say [glxgears] is required, but it isn\'t installed. To search for the related package:

`user `[`$`]`e-file glxgears`

It is also possible to search from [the PFL website](https://www.portagefilelist.de/). (for example: Search for **glxgears** : [https://www.portagefilelist.de/index.php?fs=glxgears&unique=1](https://www.portagefilelist.de/index.php?fs=glxgears&unique=1))

The search will consider the [Merge /usr](https://wiki.gentoo.org/wiki/Merge-usr "Merge-usr") topic.

Searching for `/usr/bin/ip` will not yield a result within the portage \"database\". The package providing the ip command does install it into `/bin/ip`. So a search for `/bin/ip` does yield results from portage and pfl. But often a user does a `which ip` to get the path of a command, which is `/usr/bin/ip` and use this to query `e-file`. The pfl search does some magic and will result the correct package for both `/usr/bin/ip` and `/bin/ip`

`e-file` does have the additional optional cli options. Use `man e-file` or `e-file --help` to see the complete list and if your version does have the options yet.

Output in plain text. Used if you want unformatted output data.

     --plain
          Output in plain text.

### [pfl]

If the `network-cron` USE flag is set, the command is executed weekly and sends incremental updates to the [website](https://www.portagefilelist.de).

An alternative is to use the provided systemd timer. It is installed by default but inactive. The timer needs to be activated by hand: `systemctl enable pfl.timer`. Just make sure to use either of the crons.

To update the database by hand run:

`user `[`$`]`pfl`

`pfl` does have additional optional cli options. Use `man pfl` or `pfl --help` to see the complete list and if your version does have the options yet.

Pretend. With this option you can view what will be uploaded. It will use but not modify the last run timestamp. The created xml file will be stored and can be viewed with any text editor.

    -p, --pretend
          Collect the data only and do not upload or change the last run value.

Atom. With this option you can update only a specific package. It needs a specific package and version like shown below.

    -a, --atom
          Update only for given atom. E.g. =category/package-1.23 Only specific version syntax is supported.

Repo. With this option only the packages from the given repository will be scanned.

    -r, --repo
          Update only for given repository. Currently supported: gentoo and guru.

## [Scanned repositories]

PFL does collect data from the [official Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository") and [Project GURU](https://wiki.gentoo.org/wiki/Project:GURU "Project:GURU"). Other third party or private repos are not included.

## [Data policy]

The `pfl` command, which is run by cron or manually, does create an xml file which is described by an xsd which can be found here: [schmea.xsd](https://github.com/portagefilelist/server/blob/master/webroot/import/schema.xsd).

Example of the xml file:

    <?xml version="1.0" encoding="UTF-8"?>

        <category name="net-libs">

                <files>
                    <file type="dir">/usr</file>
                    <file type="dir">/usr/share</file>
                    <file type="dir">/usr/share/doc</file>
                    <file type="dir">/usr/share/doc/gnutls-3.8.2</file>
                    <file type="obj">/usr/share/doc/gnutls-3.8.2/README.md.bz2</file>
                    <file type="obj">/usr/share/doc/gnutls-3.8.2/certtool.cfg.bz2</file>
                    <file type="dir">/usr/share/locale</file>
                    <file type="dir">/usr/share/locale/zh_CN</file>
                    <file type="dir">/usr/share/locale/zh_CN/LC_MESSAGES</file>
                    <file type="obj">/usr/share/locale/zh_CN/LC_MESSAGES/gnutls.mo</file>
                    <file type="dir">/usr/share/locale/vi</file>
                    <file type="dir">/usr/share/locale/vi/LC_MESSAGES</file>
                    <file type="obj">/usr/share/locale/vi/LC_MESSAGES/gnutls.mo</file>
                    <file type="dir">/usr/share/locale/uk</file>
                    <file type="dir">/usr/share/locale/uk/LC_MESSAGES</file>
                    <file type="obj">/usr/share/locale/uk/LC_MESSAGES/gnutls.mo</file>
                    <file type="dir">/usr/share/locale/sv</file>
                    ......
                </files>
                <uses>
                    <use>abi_x86_64</use>
                    <use>nls</use>
                    <use>seccomp</use>
                    <use>verify-sig</use>
                    <use>zlib</use>
                    <use>zstd</use>
                </uses>
            </package>
        </category>
        <category name="sec-keys">

                <files>
                    <file type="dir">/usr</file>
                    <file type="dir">/usr/share</file>
                    <file type="dir">/usr/share/openpgp-keys</file>
                    <file type="obj">/usr/share/openpgp-keys/gnutls.asc</file>
                </files>
            </package>
        </category>
    </pfl>

There are no personal or uniqe like data collected or stored in the file. Sending the file to [`https://www.portagefilelist.de/data.php`](https://www.portagefilelist.de/data.php) does follow the rules for a usual HTTP request. The server does store log data with truncated IP address. After processing the uploaded file, the file is removed and only the data needed for e-file or the website is stored.

## [See also]

-   [Equery](https://wiki.gentoo.org/wiki/Equery "Equery") --- a tool to make several common [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") operations simpler.