[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Buildiso+with+AUR+packages%3A+Using+buildpkg&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Buildiso_with_AUR_packages:_Using_buildpkg "Buildiso with AUR packages: Using buildpkg (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Buildiso_with_AUR_packages:_Using_buildpkg/ru "Buildiso с пакетами AUR: Использование buildpkg (100% translated)")

## Contents

-   [[1] [Tools to install]](#Tools_to_install)
-   [[2] [Create directories]](#Create_directories)
-   [[3] [Create your custom package tree]](#Create_your_custom_package_tree)
-   [[4] [Building with buildpkg]](#Building_with_buildpkg)
-   [[5] [Copy package files to online repository]](#Copy_package_files_to_online_repository)
-   [[6] [Build a .db file]](#Build_a_.db_file)
-   [[7] [Upload online-repo to Host Server]](#Upload_online-repo_to_Host_Server)
-   [[8] [Add online-repo to your iso-profile]](#Add_online-repo_to_your_iso-profile)
-   [[9] [Add package names to ISO profile]](#Add_package_names_to_ISO_profile)
-   [[10] [Cleaning build environment]](#Cleaning_build_environment)
-   [[11] [NOTE]](#NOTE)

This tutorial is about creating your own online repository and building a custom package(set) with the help of *buildpkg*. Later, you can install those packages to your customized Manjaro ISO using **buildiso**.

Before you start with this tutorial make sure you have completed the prerequisite steps in [Build Manjaro ISOs with buildiso](//wiki.manjaro.org/index.php?title=Build_Manjaro_ISOs_with_buildiso "Build Manjaro ISOs with buildiso").

The same XFCE ISO profile will be used as example on this Wiki page.

## [Tools to install]

Sync your system with the latest packages and ensure you have the following packages installed.

-   git
-   manjaro-tools-
-   manjaro-tools-

It is important that you match your tools packages - don\'t mix the default and git packages.

## [Create directories]

The first thing you should probably do is create a directory for your online repository. The online repository is called **online-repo** throughout this tutorial and it is located in your home-folder. You however are free to choose name location to your liking. This\'ll help keep things organized. Your repository consist of only this folder:

[user \$ ][ mkdir \~/online-repo/x86_64 [COPY TO CLIPBOARD]]

\

This online repository is created in your home folder, but you can create it anywhere you want.

## [Create your custom package tree]

Create a folder for the packages you want to build. The name is arbitrary decriptor - you can call it anything you think suitable.

[user \$ ][ mkdir \~/pkgbuild [COPY TO CLIPBOARD]]

\

Clone the relevant package(s) from AUR or from Github. Later you might create them yourself! You can select any package to build but as example we build the package `kickshaw`. Kickshaw is modern menu editor for among others openbox. First you add it to your pkgubild repo. Do this using git

[user \$ ][ cd \~/pkgbuild [COPY TO CLIPBOARD]]

\

Clone the example package from AUR

[user \$ ][ git clone https://aur.archlinux.org/kickshaw [COPY TO CLIPBOARD]]

\

Now you have a folder with a `PKGBUILD` file in your pkgbuild repository.

[user \$ ][ ls -R \~/pkgbuild [COPY TO CLIPBOARD]]

\

It is best practice to always familarize yourself with the content of the package to ensure everything is as expected.

## [Building with buildpkg]

The **buildpkg** has some options you need to familiarize yourself with.

buildpkg -h

    Usage: buildpkg [options]
       -p            Build list or pkg [default: default]
       -a <arch>          Arch [default: x86_64]
       -b <branch>        Branch [default: unstable]
       -r <dir>           Chroots directory
                          [default: /var/cache/manjaro-tools]
       -i           Install packages into the working copy of the chroot
       -c                 Recreate chroot
       -w                 Clean up cache and sources
       -n                 Install and run namcap check
       -s                 Sign packages
       -u                 Udev base-devel group (no systemd)
       -q                 Query settings and pretend build
       -h                 This help

Next thing to do is build the package. Please note that you must be located one level above your actual PKGBUILD. Understand this as the `-p` argument is **the name of the folder** holding the PKGBUILD instructionset.

[user \$ ][ buildpkg -p kickchaw [COPY TO CLIPBOARD]]

\

For more examples how to use **buildpkg**, look [here](https://wiki.manjaro.org/index.php?title=Manjaro-tools#buildpkg).

The buildpkg script creates a closed environment for building the package. This is done, so not to pollute your system with build artifacts.

## [Copy package files to online repository]

The resulting package is saved in the location defined in your manjaro-tools.conf on your system (default is the cache folder)

[user \$ ][ ls /var/cache/manjaro-tools/pkg/stable/x86_64 [COPY TO CLIPBOARD]]

\

You should see compressed package files. The file name should end with `.pkg.tar.zst`.

Copy or move your package files to your online repository:

[user \$ ][ mv /var/cache/manjaro-tools/pkg/stable/x86_64 \~/online-repo [COPY TO CLIPBOARD]]

\

## [Build a .db file]

To keep track of available packages the *pacman* package manager uses database files which is downloaded and kept on your computer. You need to create such a database file for your repo. It is crucial that your database filename is the same as your repo name. If your repo is named **online-repo** then your database name must be **online-repo.db.tar.gz**.

Use the command `repo-add` to build a database file inside your designated repo folder

[user \$ ][ cd \~/online-repo/x86_64 [COPY TO CLIPBOARD]]

\

[user \$ ][ repo-add online-repo.db.tar.gz \*.pkg.tar.\* [COPY TO CLIPBOARD]]

\

\~/online-repo/x86_64

    kickshaw-0.5-2-x86_64.pkg.tar.zst
    online-repo.db
    online-repo.db.tar.gz
    online-repo.files
    online-repo.files.tar.gz

Every time you change the content of your online repository, the database must be rebuild! Otherwise, *buildiso* will complain later about missing packages in your online repository.

Two of the files are symlinks which may or may not work on your chosen host so they can be left out.

## [Upload online-repo to Host Server]

Now you need to upload online-repo to your Host Server. Upload everything from online-repo to your Host Server. Your web address as to match the name of the directory folder you created. This is what your web address should look like after upload online-repo to your Host Server.

    http://www.myserver.com/repository/online-repo/x86_64/

## [Add online-repo to your iso-profile]

Create a file

\$/user-repos.conf

    [online-repo]
    SigLevel = Never
    Server = http://www.myserver.com/repository/online-repo/$repo/$arch

Custom online repositories will be added to the resulting **pacman.conf**. This means AUR packages cannot be installed unless you are using webserver to provide `[online-repo]` as shown this article).

NB: **\$** is not the **iso-profiles** directory but the specific sub-directory for a build, e.g. **iso-profiles/manjaro/kde**. Put your file **user-repos.conf** there to be found during the build process.

## [Add package names to ISO profile]

Now you add `kickshaw` to your package list for your ISO profile. This means your **Packages-Desktop** file should look something like this:

\~/iso-profiles/manjaro/xfce/Packages-Desktop

    ffmpegthumbnailer
    gconf # fix qt-theme
    gnome-keyring # fix wlan segfault
    gufw # firewall
    accountsservice
    lightdm-gtk-greeter
    lightdm-gtk-greeter-settings
    light-locker
    manjaro-settings-manager
    menulibre

    ## AUR packages
    kickshaw

## [Cleaning build environment]

For removing your build environment from your hard drive, execute:

[user \$ ][ sudo rm -r /var/lib/manjaro-tools/buildpkg [COPY TO CLIPBOARD]]

\

## [NOTE]

Now, you can continue to [adjust your manjaro-tools.conf](https://wiki.manjaro.org/index.php?title=Build_Manjaro_ISOs_with_buildiso#manjaro-tools.conf) or [build your ISO](https://wiki.manjaro.org/index.php?title=Build_Manjaro_ISOs_with_buildiso#Build_your_ISO).

Creating an online repo requires you to keep the repo up-to-date when changes are made upstream.