This page contains [[changes](//wiki.manjaro.org/index.php?title=Pacman_Overview&oldid=49243&diff=49893)] which are not marked for translation.

Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=Pacman_Overview/de "Pacman Übersicht (90% translated)") • ‎[English] • ‎[español](//wiki.manjaro.org/index.php?title=Pacman_Overview/es "Descripción de Pacman (98% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Pacman_Overview/fr "Aperçu de Pacman (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Pacman_Overview/ru "Обзор Pacman (100% translated)") • ‎[中文](//wiki.manjaro.org/index.php?title=Pacman_Overview/zh "Pacman总览 (6% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Pacman_Overview/zh-cn "Pacman 简介 (36% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing Updates]](#Installing_Updates)
-   [[3] [Searching for Packages]](#Searching_for_Packages)
-   [[4] [Installing Packages]](#Installing_Packages)
-   [[5] [Removing Packages]](#Removing_Packages)
-   [[6] [Viewing and Removing Orphans]](#Viewing_and_Removing_Orphans)
-   [[7] [Downloading Packages without Installing]](#Downloading_Packages_without_Installing)
-   [[8] [Determining which Package Owns a File]](#Determining_which_Package_Owns_a_File)
-   [[9] [Cleaning the Cache]](#Cleaning_the_Cache)
-   [[10] [The Configuration File, pacman.conf]](#The_Configuration_File.2C_pacman.conf)
    -   [[10.1] [Enabling Color Output]](#Enabling_Color_Output)
    -   [[10.2] [Showing PacMan Eating Power Pills]](#Showing_PacMan_Eating_Power_Pills)
-   [[11] [Troubleshooting]](#Troubleshooting)
-   [[12] [See Also]](#See_Also)

# [Overview]

Manjaro\'s package manager, [Pamac](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Pamac "Special:MyLanguage/Pamac") ships with most Manjaro editions. All Manjaro editions include [pacman](https://www.archlinux.org/pacman/), the package manager from upstream Arch Linux. Pacman includes some advanced features not found in Pamac.

Key points to know:

-   Pacman is already installed in Manjaro Linux by default
-   Pacman is mainly developed/maintained by Arch Linux developers
-   Pacman can only be used from the command line, if you would prefer a graphical package manager please see [Pamac](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Pamac "Special:MyLanguage/Pamac") or [Octopi](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Octopi "Special:MyLanguage/Octopi")
-   Pacman can only use the official Manjaro [repository](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Repositories_and_Servers "Special:MyLanguage/Repositories and Servers"). There are separate articles available for accessing the [Arch User Repository(AUR)](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Arch_User_Repository "Special:MyLanguage/Arch User Repository"), using [flatpaks](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Flatpak "Special:MyLanguage/Flatpak") and using [snaps](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Snaps "Special:MyLanguage/Snaps")

\

# [Installing Updates]

Update the package database and update all packages on the system

[user \$ ][ sudo pacman -Syu [COPY TO CLIPBOARD]]

\

Update all packages on the system and allow packages to be downgraded. Downgrading should be only be needed when switching to an older branch. For example, switching from Testing to Stable.

[user \$ ][ sudo pacman -Syuu [COPY TO CLIPBOARD]]

\

\

# [Searching for Packages]

To search the Manjaro repositories for available packages you can use the command `pacman -Ss keyword`. It will search both the package name and the description for the keyword. For example, to search for packages containing the keyword smplayer you could use:

[user \$ ][ pacman -Ss smplayer [COPY TO CLIPBOARD]]

\

You can search your installed packages in the same manner using `-Qs` instead of `-Ss`. To search your installed packages for smplayer:

[user \$ ][ pacman -Qs smplayer [COPY TO CLIPBOARD]]

\

\
Once you have found a package you can use `pacman -Qi` to get more information about an installed packages or `pacman -Si` for packages in the repos. Following the example above you could use

[user \$ ][ pacman -Si smplayer [COPY TO CLIPBOARD]]

\

\
Finally, for a list of all installed packages on your system, enter the following command:

[user \$ ][ pacman -Ql [COPY TO CLIPBOARD]]

\

\

# [Installing Packages]

**Never install a package without updating the system first**

------------------------------------------------------------------------

On a rolling release this can lead to an unbootable system

To install a software package, the basic syntax is `pacman -S packagename`. However, installing a package without updating the system will lead to a partial upgrade situation so all the examples here will use `pacman -Syu packagename` which will install the package and ensure the system is up to date. For example, to install smplayer the command is:

[user \$ ][ sudo pacman -Syu smplayer [COPY TO CLIPBOARD]]

\

You will then be presented a list of software to install. You may notice this list has more packages than you requested. This is because many packages also have dependencies which are packages that must be installed in order for the software you selected to function properly.

Pacman can also directly install packages from the local system or a location on the internet. The format of that command is `pacman -U packagelocation`. For example, to install a copy of your package cache you could do something like:

[user \$ ][ sudo pacman -U /var/cache/pacman/pkg/smplayer-19.5.0-1-x86_64.pkg.tar.xz [COPY TO CLIPBOARD]]

\

Alternatively, you could get it directly from one of Manjaro\'s mirrors:

[user \$ ][ sudo pacman -U https://mirror.alpix.eu/manjaro/stable/community/x86_64/smplayer-19.5.0-1-x86_64.pkg.tar.xz [COPY TO CLIPBOARD]]

\

\

**Warning**

------------------------------------------------------------------------

When using pacman -U it is up to you to ensure that the package you are installing is fully compatible with your system.

# [Removing Packages]

**Always review the package list before confirming when removing packages**

------------------------------------------------------------------------

If you are not careful you can easily remove your entire desktop due to dependencies.

\
To remove a software package, the basic syntax is `sudo pacman -R packagename`. We could remove the smplayer package we installed above with:

[user \$ ][ sudo pacman -R smplayer [COPY TO CLIPBOARD]]

\

\
This will remove the package, but will leave all the dependencies behind. If you also want to remove the unneeded dependencies you could use `pacman -Rsu packagename` as seen in this example:

[user \$ ][ sudo pacman -Rsu smplayer [COPY TO CLIPBOARD]]

\

\
Sometimes when you try to remove a package you will not be able to because there are other packages which depend on it. You can use `pacman -Rc packagename` to remove a package and everything that depends on it. Be careful to heed the above warning when using this option.

[user \$ ][ sudo pacman -Rc smplayer [COPY TO CLIPBOARD]]

\

\
The most nuclear option is `pacman -Rcs packagename`.

**Use this with extreme caution, or don't use it at all**

------------------------------------------------------------------------

-Rcs will remove every package that depends on packagename regardless of whether a package is needed for something else. This could render Manjaro unusable.

Pacman usually also creates backup configuration files when deleting packages. To remove those, you can add `n` to any of the examples above. For example:

[user \$ ][ sudo pacman -Rn smplayer [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo pacman -Rsun smplayer [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo pacman -Rcn smplayer [COPY TO CLIPBOARD]]

\

\

# [Viewing and Removing Orphans]

To list all *orphans*, installed packages that are not used by anything else and should no longer be needed:

[user \$ ][ pacman -Qdt [COPY TO CLIPBOARD]]

\

\
To remove all the orphans:

[user \$ ][ sudo pacman -Rs \$(pacman -Qdtq) [COPY TO CLIPBOARD]]

\

\

# [Downloading Packages without Installing]

In some cases it may be useful to download a package without installing. For example, to install on a different system that is not connected to the internet. This can be done with `pacman -Sw packagename`. For example:

[user \$ ][ sudo pacman -Sw smplayer [COPY TO CLIPBOARD]]

\

\
The package and any rerquired dependencies will be downloaded to your pacman cache at `/var/cache/pacman/pkg`

\

# [Determining which Package Owns a File]

It is often useful to understand which package installed a file on your system. This is easy to do with pacman using `pacman -Qo /path/to/filename`. For example:

[user \$ ][ pacman -Qo /usr/bin/smplayer [COPY TO CLIPBOARD]]

\

\

# [Cleaning the Cache]

When pacman installs packages, it keeps a copy of all the old packages you have downloaded. This cache can be very useful if you have to install older packages in an emergency. However, left unchecked, this cache will grow very large over time. Systems running [Pamac](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Pamac "Special:MyLanguage/Pamac") will already have access to its automated pacman cache cleaning functions. It is also possible to clean them manually using pacman.

To clear the cache of packages that are no longer installed, enter the following command:

[user \$ ][ sudo pacman -Sc [COPY TO CLIPBOARD]]

\

\
Otherwise, to clear the cache completely, enter the following command (and use with care):

[user \$ ][ sudo pacman -Scc [COPY TO CLIPBOARD]]

\

\
A safer way to remove old package cache files is to remove all packages except for the latest three package versions using `paccache`:

[user \$ ][ paccache -rvk3 [COPY TO CLIPBOARD]]

\

\

# [][The Configuration File, pacman.conf]

Pacman\'s settings are located in `/etc/pacman.conf`. This file is owned by root, please see [this guide](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Viewing_and_editing_configuration_files "Special:MyLanguage/Viewing and editing configuration files") if you need more information on how to edit this file. A full reference to these options can be found in the Arch Wiki linked below. This sections features some settings that may be of particular interest to Manjaro users.

\

**Note**

------------------------------------------------------------------------

pacman.conf settings are case sensitive

## [Enabling Color Output]

By default, pacman\'s output is monochrome but enabling colored output can make the output easier to read if your terminal supports colors. This can be enabled by uncommenting or adding the following line to the file

    Color

## [Showing PacMan Eating Power Pills]

If you are bored of simply watching lines of hashes while downloading software packages in the terminal, why not change the progress bar to Pacman eating power pills instead? To enable this, simply add the line:

    ILoveCandy

# [Troubleshooting]

A separate page for pacman troubleshooting is available **[here](//wiki.manjaro.org/index.php?title=Special:MyLanguage/pacman_troubleshooting "Special:MyLanguage/pacman troubleshooting")**.

\

# [See Also]

-   [System Maintenance](//wiki.manjaro.org/index.php?title=Special:MyLanguage/System_Maintenance "Special:MyLanguage/System Maintenance")
-   [Pacman-mirrors](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Pacman-mirrors "Special:MyLanguage/Pacman-mirrors")
-   [Pacman troubleshooting](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Pacman_troubleshooting "Special:MyLanguage/Pacman troubleshooting")
-   [Downgrading packages](//wiki.manjaro.org/index.php?title=Special:MyLanguage/Downgrading_packages "Special:MyLanguage/Downgrading packages")
-   [ArchWiki: pacman](https://wiki.archlinux.org/index.php/Pacman)
-   [ArchWiki: pacman tips](https://wiki.archlinux.org/index.php/Pacman_tips)
-   [ArchWiki: pacman performance](https://wiki.archlinux.org/index.php/Improve_pacman_performance)