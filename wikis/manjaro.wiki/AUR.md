Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=Arch_User_Repository/de "Arch User Repository (59% translated)") • ‎[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Arch_User_Repository/tr "Arch Kullanıcı Deposu (14% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Arch_User_Repository/es "Arch User Repository (AUR) Español (100% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Arch_User_Repository/fr "Dépôt des utilisateurs Arch (AUR) (64% translated)") • ‎[português do Brasil](//wiki.manjaro.org/index.php?title=Arch_User_Repository/pt-br "Repositório de usuários Arch (36% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Arch_User_Repository/ru "Arch User Repository (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Arch_User_Repository/fa "مخزن کاربر آرچ (18% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Arch_User_Repository/zh-cn "Arch 用户软件仓库 (50% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Accessing the AUR]](#Accessing_the_AUR)
    -   [[2.1] [Using GUI Pamac]](#Using_GUI_Pamac)
    -   [[2.2] [Using commandline Pamac]](#Using_commandline_Pamac)
    -   [[2.3] [Installing from the AUR by hand]](#Installing_from_the_AUR_by_hand)
        -   [[2.3.1] [Manual]](#Manual)
    -   [[2.4] [Upgrading the packages installed from the AUR]](#Upgrading_the_packages_installed_from_the_AUR)
-   [[3] [See Also]](#See_Also)

## [Overview]

**Use the AUR at your own risk!**

------------------------------------------------------------------------

**No support** will be provided by the Manjaro team for any issues that may arise relating to software installations from the AUR. When Manjaro is updated, AUR packages might stop working. **This is not a Manjaro issue**

Although Manjaro is very close to Arch Linux and mostly compatible ---being based on Arch Linux itself--- it is not possible to access their official repositories for use in Manjaro. Instead, Manjaro uses its own repositories in order to ensure that any software packages that are accessible, such as system updates and applications, have been fully tested to be compatible and stable before release. It is still possible to access additional software packages from the *[Arch User Repository](https://wiki.archlinux.org/index.php/AUR)* (AUR).

The AUR is managed by the Arch Linux user community itself. Although this repository is unofficial, software packages first placed here can eventually make their way into Arch Linux\'s official (community) repository if they become popular enough.

**AUR, as a community maintained repository, present potential risks and problems.**

Possible risks using AUR packages:

-   Multiple versions of the same packages.
-   Out of date packages.
-   Broken or only partially working packages.
-   Improperly configured packages which download unnecessary dependencies, or do not download necessary dependencies, or both.
-   Malicious packages (although extremely rare).

As such, although much of the software packages provided by the AUR should work, do not expect the installation process to always be quite as straight-forward as when you are using the official Manjaro repositories.

On occasion, it may be necessary to manually identify and install dependencies yourself (such as, after an aborted installation attempt).

**Again, there is no guarantee that any installed software will work properly, if at all.**

\

**Info**

------------------------------------------------------------------------

You should become familiar with the manual build process in order to be prepared to troubleshoot problems.

\

## [Accessing the AUR]

### [Using GUI [Pamac](//wiki.manjaro.org/index.php?title=Pamac "Pamac")]

Open Pamac - the name in menu is *Add/Remove Software* and navigate to the Preferences page. You will be required to enter your password to access it.At Preferences page → select the Third Party tab → and move the slider to enable AUR support. Be sure you have the necessary files for building applications from source

[user \$ ][ pamac install base-devel git [COPY TO CLIPBOARD]]

\

### [Using commandline [Pamac](//wiki.manjaro.org/index.php?title=Pamac "Pamac")]

**Info**

------------------------------------------------------------------------

It is **strongly** recommended to follow this link [AUR website](https://aur.archlinux.org/) and examine the relevant page(s) for any and all software intended to be installed.

\
These pages contain comments from both existing users and package developers, which may provide valuable information (such as, warnings and/or solutions to problems). To search for and install software packages from the AUR, the syntax is:

[user \$ ][ pamac search -a \[software package name\] [COPY TO CLIPBOARD]]

\

For example, if wishing to install *Google Chrome* - first follow this link to **[all Google Chrome build scripts](https://aur.archlinux.org/packages/?K=google-chrome)** and verify which package you want to build.Or you can ask pamac - for *Google Chrome* candidates. Just use the search command and *Google Chrome* as the query. Look over the results or narrow the search parameters - just remember pamac cannot tell you of any issues with build scripts - only the relevant page. E.g. following this link to the **[buildscript for Google Chrome](https://aur.archlinux.org/packages/google-chrome)**

[user \$ ][ pamac search Google Chrome [COPY TO CLIPBOARD]]

\

In the example we choose the standard version of *Google Chrome*. To build the *google-chrome* package with **pamac** enter the following and press enter

[user \$ ][ pamac build google-chrome [COPY TO CLIPBOARD]]

\

You will be presented with the outcome of the chosen build with all dependencies and you will be asked a couple of questions.

1.  Query to edit build files. This is a precaution to verify that the build scripts does not contain malicious actions.
2.  Query to continue download and install dependencies then download the sources, build and install the app.
3.  You will be asked for your password before anything happens.

### [Installing from the AUR by hand]

#### [Manual]

To do that follow the steps given below:

-   Be sure you have the necessary files for building applications from source

[user \$ ][ pamac install base-devel git [COPY TO CLIPBOARD]]

\

-   Clone the PKGBUILD

[user \$ ][ git clone https://aur.archlinux.org/google-chrome.git [COPY TO CLIPBOARD]]

\

-   Change directory to cloned folder

[user \$ ][ cd google-chrome [COPY TO CLIPBOARD]]

\

-   To make/compile the package, run:

[user \$ ][ makepkg -s [COPY TO CLIPBOARD]]

\

This will build the package and pull in any dependencies needed. *Note: it won\'t pull a dependency from the AUR, only from the Manjaro Repos.*. If you list the folder content

[user \$ ][ ls [COPY TO CLIPBOARD]]

\

you\'ll probably find a few new files. You\'re interested in the one that ends with .pkg.tar.zst

-   The final event is running \$sudo pacman -U on that file

[user \$ ][ sudo pacman -U google-chrome-ver.rel.bugfix.build-pkgrel.pkg.zst [COPY TO CLIPBOARD]]

\

And you\'ve done it\...the safest way to install from the AUR. This is essentially what most install scripts do for you.

*Note:* Instead of using *sudo pacman -U google-chrome-ver.rel.bugfix.build-pkgrel.pkg.zst* can also use:

[user \$ ][ makepkg -i [COPY TO CLIPBOARD]]

\

*Note:* To combine above steps into one:

[user \$ ][ makepkg -is [COPY TO CLIPBOARD]]

\

\

### [Upgrading the packages installed from the AUR]

The following command will upgrade **all** packages on the system including AUR builds

[user \$ ][ pamac upgrade -a [COPY TO CLIPBOARD]]

\

## [See Also]

-   [Need to know about Manjaro and AUR](https://forum.manjaro.org/t/need-to-know-about-manjaro-and-aur/103617)
-   [Pacman](http://wiki.manjaro.org/index.php?title=Pacman)