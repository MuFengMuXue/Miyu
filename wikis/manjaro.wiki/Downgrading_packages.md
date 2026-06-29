Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Downgrading_packages/tr "Paketlerin sürümünü düşürme (4% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Downgrading_packages/fr "Rétrogradation de paquets (88% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Downgrading_packages/ru "Понижение версии пакетов (100% translated)")

## Contents

-   [[1] [Introduction]](#Introduction)
-   [[2] [The easy way using Manjaro Downgrade]](#The_easy_way_using_Manjaro_Downgrade)
    -   [[2.1] [Installing Manjaro Downgrade]](#Installing_Manjaro_Downgrade)
    -   [[2.2] [Using Manjaro Downgrade]](#Using_Manjaro_Downgrade)
    -   [[2.3] [Adding packages to the ignore list]](#Adding_packages_to_the_ignore_list)
-   [[3] [Downgrading packages manually]](#Downgrading_packages_manually)
    -   [[3.1] [Ensuring downgraded packages won\'t be upgraded again]](#Ensuring_downgraded_packages_won.27t_be_upgraded_again)

**Warning**

------------------------------------------------------------------------

Downgrading packages will almost always leave you in an unsupported partial upgrade state. These instructions are intended for advanced users who understand the consequences of downgrading packages

# [Introduction]

There are sometimes circumstances that require downgrading a package temporarily. While this should not be an issue for Manjaro users on the stable branch, it is sometimes needed when using the unstable branch.

\

# [The easy way using Manjaro Downgrade]

**manjaro-downgrade** is an application that helps automate the process of locating and downgrading packages.

\

## [Installing Manjaro Downgrade]

First you need to install Manjaro Downgrade, which is available in the official repositories of Manjaro. This can be done with the following command: pamac install manjaro-downgrade

## [Using Manjaro Downgrade]

To use **manjaro-downgrade** simply run the command followed by the name of the package you want to downgrade. For example:

manjaro-downgrade firefox

This will result in output which looks like this:

    Available packages:
        1)  firefox    55.0.3  1  x86_64  (remote)
        2)  firefox    60.0.1  1  x86_64  (remote)
        3)  firefox    64.0.2  1  x86_64  (remote)
        4)  firefox    64.0.2  1  x86_64  (local)
        5)  firefox    65.0    1  x86_64  (remote)
        6)  firefox    65.0    2  x86_64  (remote)
        7)  firefox    65.0.1  1  x86_64  (remote)
        8)  firefox    65.0.2  1  x86_64  (remote)
    -   9)  firefox    66.0    0  x86_64  (local)
       10)  firefox    66.0    1  x86_64  (remote)
       11)  firefox    66.0.1  1  x86_64  (remote)
       12)  firefox    66.0.2  1  x86_64  (remote)
       13)  firefox    66.0.3  1  x86_64  (remote)
       14)  firefox    66.0.4  1  x86_64  (remote)
    +  15)  firefox    66.0.5  1  x86_64  (remote)
    +  16)  firefox    66.0.5  1  x86_64  (local)

The entries listed as \"local\" are versions from your local package cache. The entries identified as \"remote\" are available from the Arch Linux Archive(ALA).

\

**Warning**

------------------------------------------------------------------------

Installing packages from the ALA is inherently dangerous as sometimes Manjaro needs custom versions of certain packages. Doing this can result in a broken system. As a result, downgrading from the ALA is disabled by default on the stable branch. If needed, you can enable it by setting the environment variable

    DOWNGRADE_FROM_ALA=1

\

## [Adding packages to the ignore list]

After downgrading the package, you should see a message similar to this:

    add firefox to IgnorePkg? [y/n]

If you answer \"y\", the package will no long be upgraded in future updates until you manually remove it from the **IgnorePkg** line of **/etc/pacman.conf**

\

# [Downgrading packages manually]

The directory `/var/cache/pacman/pkg` contains old versions of packages. First look for the package that you wish to downgrade is this directory then use `pacman -U` to install it. For example, it could look like this:

\
We have to use the following command to install the previously installed version of the packages that need to be downgraded:

sudo pacman -U /var/cache/pacman/pkg/firefox-64.0.2-1-x86_64.pkg.tar.xz

## [][Ensuring downgraded packages won\'t be upgraded again]

In order to stop these packages from being upgraded the next time you run updates, you can add them to the ignore list in **/etc/pacman.conf**. Look for the section that looks like this:

    # Pacman won't upgrade packages listed in IgnorePkg and members of IgnoreGroup

    # IgnorePkg =

Remove the comment in front of **IgnorePkg** and add the package name to the list. When you are done it should look like this:

    # Pacman won't upgrade packages listed in IgnorePkg and members of IgnoreGroup

    IgnorePkg = firefox

Once this is done the package will no long be upgraded in future updates until you manually remove it from the **IgnorePkg** line of **/etc/pacman.conf**