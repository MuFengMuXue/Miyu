# Arch Linux Archive

The Arch Linux Archive (ALA)—formerly known as Arch Linux Rollback Machine (ARM)—stores:

* official ISO images and bootstrap tarballs,
* all versions of each package,
* official repositories daily snapshots across time.

You can use it to:

* find a previous version of an official ISO image,
* downgrade to a previous version of one package—e.g. "last version is broken, I want the previous one",
* restore all your packages at a precise moment—e.g. "my system is broken, I want to go back two months ago".

Packages are only kept for a few years, afterwards they are moved to the Arch Linux Historical Archive on the Internet Archive.

## Location
The Arch Linux Archive is available at https://archive.archlinux.org/ and mirrors.

The source code is also available for setting up your own mirror.

## Directories
The Arch Linux Archive is split into three main directories detailed below:

 ├── iso
 ├── packages
 └── repos

## /iso
The iso directory contains official ISO images and bootstrap tarballs sorted by release date:

 ├── 2014.09.03
 ├── 2014.10.01
 ├── 2014.11.01
 ├── 2014.12.01
 ├── 2015.07.01
 ├── 2015.08.01
 ├── 2015.09.01
 └── 2017.04.01
     ├── arch
     ├── archlinux-2017.04.01-x86_64.iso
     ├── archlinux-2017.04.01-x86_64.iso.sig
     ├── archlinux-2017.04.01-x86_64.iso.torrent
     ├── archlinux-bootstrap-2017.04.01-x86_64.tar.gz
     ├── archlinux-bootstrap-2017.04.01-x86_64.tar.gz.sig
     ├── md5sums.txt
     └── sha1sums.txt

## /packages
The packages directory contains all versions of each package with their signatures. One directory by package and package directories are grouped by their first letter:

 ├── packages
 │   ├── a
 │   │   ├── awesome
 │   │   │   ├── awesome-4.3-2-x86_64.pkg.tar.zst
 │   │   │   ├── awesome-4.3-2-x86_64.pkg.tar.zst.sig
 │   │   │   ├── awesome-4.3-3-x86_64.pkg.tar.zst
 │   │   │   ├── awesome-4.3-3-x86_64.pkg.tar.zst.sig
 │   │   │   ├── ...
 │   │   │
 │   │   ├── ...
 │   │   ├── awstats
 │   │   └── axel
 │   │
 │   ├── b
 │   ├── ...
 │   └── z

You can use the magic subdirectory .all to access all packages by their name. It acts as a flat directory containing all versions of every package:

 ├── packages
 │   ├── .all
 │   │   ├── awesome-4.3-2-x86_64.pkg.tar.zst
 │   │   ├── ...
 │   │   ├── zsh-5.8-1-x86_64.pkg.tar.zst
 │   │   ├── zsh-5.8.1-1-x86_64.pkg.tar.zst
 │   │   └── ...

The  directory does not allow listing: there are about a hundred thousand packages. You can download the full package list as a compressed index:

## /repos
The repos directory contains daily snapshots of official mirror organized by date like in the following example:

 repos
 ├── 2013
 │   ├── 08
 │   │   └── 31
 │   │       ├── community
 │   │       ├── community-staging
 │   │       ├── community-testing
 │   │       ├── core
 │   │       ├── extra
 │   │       ├── gnome-unstable
 │   │       ├── kde-unstable
 │   │       ├── lastsync
 │   │       ├── multilib
 │   │       ├── multilib-staging
 │   │       ├── multilib-testing
 │   │       ├── pool
 │   │       ├── staging
 │   │       └── testing
 │   ├── 09
 │   │   ├── 01
 │   │   ├── 02
 │   │   ├── ...
 │   │   ├── 21
 │   │   └── 22
 │   ├── 10
 │   │   ├── 01
 │   │   ├── 02
 │   │   ├── ...
 │   │
 │   ├── 11
 │   └── 12
 ├── 2014
 │   ├── 01
 │   │   ├── 01
 │   │   ├── 02
 │   │   ├── ...
 │   │
 │   ├── 02
 │   ├── 03
 │   ├── ...
 │   └── 09
 │       ├── 01
 │       ├── ...
 │       └── 28
 ├── last
 ├── month
 └── week

## Arch Linux Historical Archive
Maintaining the Arch Linux Archive consumes significant amount of resources, so old packages are cleaned up from time to time. Before removing them, old packages are uploaded to the dedicated Arch Linux Historical Archive collection on the Internet Archive.

The Arch Linux Historical Archive does not provide a way to access a snapshot of Arch Linux packages at a given point in time as the repos directory of the Arch Linux Archive does. However, there is a redirection on the Arch Linux Archive so that downloads for old packages are redirected to the Arch Linux Historical Archive. There should be no visible impact from the user side, except from the fact that https://archive.org is generally quite slow for downloading.

## Finding packages
The Arch Linux Historical Archive collection has an index of all packages.

It is also possible to directly access a package by its ''identifier.  The general pattern for identifiers is . To obtain the sanitized'' package name, simply replace any ,  or  character in the package name by an underscore ().

For example, the identifier for  is . You can then access the details page of this package via https://archive.org/details/archlinux_pkg_lucene__.

It is also possible to run searches with the archive.org Python client:

{{hc|1=$ ia search subject:"archlinux package" subject:'mysql'|2=
{"identifier": "archlinux_pkg_ejabberd-mod_mysql"}
{"identifier": "archlinux_pkg_ejabberd-mod_mysql-svn"}
{"identifier": "archlinux_pkg_gambas3-gb-db-mysql"}
{"identifier": "archlinux_pkg_gambas3-gb-mysql"}
{"identifier": "archlinux_pkg_libgda-mysql"}
}}

## Downloading packages
All available package versions (and their signature) can be accessed via the download page of a package: https://archive.org/download/archlinux_pkg_lucene__.

To download, verify and install a package using pacman:

 # pacman -U https://archive.org/download/archlinux_pkg_cjdns/cjdns-20.5-1-x86_64.pkg.tar.zst

Package verification is controlled by pacman's  option. Note that if you use pacman, you have to figure out the dependencies yourself.

It is also possible to use the archive.org Python client.

Download a specific version of a package:

 $ ia download archlinux_pkg_cjdns cjdns-20.5-1-x86_64.pkg.tar.zst{,.sig}

Download all x86_64 versions of a package, with signatures:

 $ ia download archlinux_pkg_cjdns --glob="*x86_64.pkg.tar.*"

## Tips and tricks
## Downgrade one package
Find the package you want under /packages and let pacman fetch it for installation. For example:

 # pacman -U https://archive.archlinux.org/packages/path/packagename.pkg.tar.zst

Letting pacman fetch it will automatically download the package's detached .sig file and verify it according to  settings.

Alternatively, download and install the package manually using .

See also Downgrading packages#Automation for tools that simplify the process.

## Restore all packages to a specific date
To restore all packages to their version at a specific date—let us say 30 March 2014—you have to direct pacman to this date by using the following  directive in your pacman.conf:

 Server = https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch

Then update the database and force downgrade:

 # pacman -Syyuu

If you get errors complaining about corrupted/invalid packages due to PGP signature, try to first update separately  and . Alternatively, you can decide to temporarily disable signature checking altogether.

## History
* The original Arch Linux Rollback Machine (ARM) was closed on 2013-08-18.
* It was then hosted on seblu.net since 2013-08-31.
* New URL and closing the old ARM hierarchy on 2015-10-13. A new software——was introduced.
* Moved to https://archive.archlinux.org on 2015-12-19.
* Old packages from 2013-2016 uploaded to https://archive.org/details/archlinuxarchive on 2018-06-05.
* The Arch Linux Archive is also added as a WebSeed to the torrents (but not magnet links) since release 2022.10.01.
