Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=Pamac/de "Pamac (75% translated)") • ‎[English] • ‎[français](//wiki.manjaro.org/index.php?title=Pamac/fr "Pamac (26% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Pamac/ru "Pamac (100% translated)") • ‎[עברית](//wiki.manjaro.org/index.php?title=Pamac/he "Pamac/he (17% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Pamac/fa "پَمَک‌ (Pamac) (42% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Pamac/zh-cn "Pamac (14% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing Pamac]](#Installing_Pamac)
-   [[3] [Using the Pamac GUI]](#Using_the_Pamac_GUI)
    -   [[3.1] [Installing Software]](#Installing_Software)
    -   [[3.2] [Removing Software]](#Removing_Software)
    -   [[3.3] [Preferences]](#Preferences)
        -   [[3.3.1] [AUR (Arch User Repository)]](#AUR_.28Arch_User_Repository.29)
-   [[4] [Using the Pamac CLI]](#Using_the_Pamac_CLI)
    -   [[4.1] [Locating and Installing Packages]](#Locating_and_Installing_Packages)
    -   [[4.2] [Removing Packages]](#Removing_Packages)
    -   [[4.3] [Identifying Installed Packages]](#Identifying_Installed_Packages)
    -   [[4.4] [Displaying Detailed Package Information]](#Displaying_Detailed_Package_Information)
    -   [[4.5] [Updating the System]](#Updating_the_System)
    -   [[4.6] [Dealing with Orphaned Packages]](#Dealing_with_Orphaned_Packages)
    -   [[4.7] [Cleaning the Cache]](#Cleaning_the_Cache)
    -   [[4.8] [Other Useful Pamac Functions]](#Other_Useful_Pamac_Functions)

\

# [Overview]

Pamac (Add/Remove Software) is Manjaro\'s Package Manager. It is based on libalpm with AUR and Appstream support. It focuses on providing an easy to use interface while still providing a powerful set of features.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) | **This article or section is out of date.**                                                                                                                  | [![Tango-dialog-warning.png](/images/d/d8/Tango-dialog-warning.png)](//wiki.manjaro.org/index.php?title=File:Tango-dialog-warning.png) |
|                                                                                                                                                                                                                          |                                                                                                                                                              |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                  |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | **Reason:** Screenshots are dated. ([Discuss](//wiki.manjaro.org/index.php?title=Talk:Pamac&action=edit&redlink=1 "Talk:Pamac (page does not exist)")) |                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                          | :::                                                                                                                                                          |                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[![Pamac GTK3 on Plasma 6 with package information sidebar](/images/thumb/5/51/Pamac-main-with-package-info.png/800px-Pamac-main-with-package-info.png)](//wiki.manjaro.org/index.php?title=File:Pamac-main-with-package-info.png "Pamac GTK3 on Plasma 6 with package information sidebar")

# [Installing Pamac]

Pamac is pre-installed on many Manjaro Editions but if your system does not have it it can be easily installed. Pamac comes in several different packages:

-   `pamac-gtk3` - A Package Manager based on libalpm with AUR and Appstream support (GTK3)
-   `pamac-gtk` - A Package Manager based on libalpm with AUR and Appstream support (GTK4)
-   `pamac-cli` - A CLI Package Manager based on libalpm with AUR support
-   `pamac-tray-icon-plasma` - Pamac tray icon for Plasma users
-   `pamac-gnome-integration` - Pamac GNOME integration
-   `libpamac` - Library for Pamac package manager based on libalpm

\
These packages can be installed using pacman. For example, to install the GTK4 version, you can use the command:

[user \$ ][ sudo pacman -Syu pamac-gtk [COPY TO CLIPBOARD]]

\

\

# [Using the Pamac GUI]

To launch the package manager you use your application launcher\'s search function. The full name is **Add/Remove Software** and it resides in the **System** section of the application launcher. You may also be able to start the GUI using the command line

[user \$ ][ pamac-manager [COPY TO CLIPBOARD]]

\

## [Installing Software]

[![Pamac-gtk-optional-deps.png](/images/thumb/3/3c/Pamac-gtk-optional-deps.png/400px-Pamac-gtk-optional-deps.png)](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-optional-deps.png)

[](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-optional-deps.png "Enlarge")

\
To install packages, simply check the box next to the packages. Once you have selected all the packages you want to install, click the Apply button at the bottom of the page.

\
If any of the packages have optional dependencies (packages that enable additional functionality) you will see a window like the one to the left which allows to select the ones you would like to install.

[![Pamac-gtk-transaction-summary.png](/images/thumb/c/c4/Pamac-gtk-transaction-summary.png/400px-Pamac-gtk-transaction-summary.png)](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-transaction-summary.png)

[](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-transaction-summary.png "Enlarge")

\
After you have selected optional dependencies, you should see a window similar to the one pictured on the left. This lists all the packages that will be installed, upgraded or removed by the action. Once you have reviewed the list, press the Apply button to install the packages.

\
You may notice this list has more packages than you selected in the GUI. This is because many packages also have dependencies which are packages that must be installed in order for the software you selected to function properly. You may also notice that packages are being removed even though you didn\'t select any packages to remove. This is happening in the example to the left where you can see `clutter` and `cogl` are being removed. They are being removed because they conflict with `deepin-clutter` and `deepin-cogl` which provide the same functionality.

\

## [Removing Software]

[![Pamac-gtk-remove-summary.png](/images/thumb/4/4f/Pamac-gtk-remove-summary.png/400px-Pamac-gtk-remove-summary.png)](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-remove-summary.png)

[](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-remove-summary.png "Enlarge")

\
Removing software is as simple as unchecking the packages you want to remove and clicking the Apply button at the bottom of the page.

\
Once you do, you should see a screen similar to the one on the left which lists all the packages that are about to be removed. You may notice this list contains more packages than you selected. This is because when you remove a package that other packages depend on, those packages are also removed.

\

**Carefully review the Transaction Summary before accepting the package removal.**

------------------------------------------------------------------------

Some packages have many packages which depend on them and you don\'t want to inadvertently remove your whole desktop environment

## [Preferences]

You can access the preferences by clicking on the three dots in the upper right corner and selecting preferences.

\

[![Pamac-gtk-preferences-general.png](/images/thumb/6/69/Pamac-gtk-preferences-general.png/400px-Pamac-gtk-preferences-general.png)](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-preferences-general.png)

[](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-preferences-general.png "Enlarge")

\
The General tab of preferences contains several settings, most of which are self-explanatory.

\

-   Remove unrequired dependencies - This removes dependencies which are no longer required by any package
-   Check available disk space - Checks to ensure you have sufficient disk space available before downloading and installing packages
-   Maximum parallel downloads - The number of concurrent downloads allowed
-   Enable downgrade - This allows packages to be downgraded as well as upgraded. This is important when [switching branches](//wiki.manjaro.org/index.php?title=Switching_Branches "Switching Branches").
-   Check for updates - Disabling this will stop pamac from looking for updates. In most cases, turning this off on a [rolling release](//wiki.manjaro.org/index.php?title=The_Rolling_Release_Development_Model "The Rolling Release Development Model") distro like Manjaro is a bad idea.
-   Ignore updates for - This is a list of packages that you don\'t want to be upgraded. This is inherently dangerous practice and should only be used by advanced users.

\

**Ignoring updates for individual packages will leave you in an unsupported \"partial upgrade\" state.**

------------------------------------------------------------------------

It is common for innocuous looking ignored packages to leave your system unbootable

\

#### [][AUR (Arch User Repository)]

[![Pamac-gtk-preferences-aur.png](/images/thumb/1/16/Pamac-gtk-preferences-aur.png/400px-Pamac-gtk-preferences-aur.png)](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-preferences-aur.png)

[](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-preferences-aur.png "Enlarge")

Pamac is also capable of using scripts from the [Arch User Repository(AUR)](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") to install or update packages. Please carefully read the considerations in the [linked page](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") prior to enabling support for AUR.

If you enable AUR support, you may also select, \"Check for updates from AUR\" so software you install from AUR won\'t become outdated. An alternative is creating an account on AURweb and subscribe to notifications for the scripts you are using on a permanent basis.

Checking for \"development package\" updates will allow updates on \*-git packages which are built from the latest source code to also be updated.

\

**Any use of the AUR is at your own risk.**

------------------------------------------------------------------------

**DISCLAIMER:** AUR scripts are created for Arch Linux by Arch Linux Users. AUR packages are user-produced content. These PKGBUILDs are completely unofficial and have not been thoroughly vetted.

\

The \"Build directory\" is where AUR packages will be built. Using \"tmp\" usually will provide the best performance but very large packages may fail to build. In this case, select a location with more available space.

[![Pamac-gtk-preferences-cache.png](/images/thumb/9/9e/Pamac-gtk-preferences-cache.png/400px-Pamac-gtk-preferences-cache.png)](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-preferences-cache.png)

[](//wiki.manjaro.org/index.php?title=File:Pamac-gtk-preferences-cache.png "Enlarge")

\
When pamac installs packages, it keeps a copy of all the old packages you have downloaded. This cache can be very useful if you have to install older packages in an emergency. However, left unchecked, this cache will grow very large over time. These preferences allow your cache to be automatically managed based on your preferences.

\
The first option allows you to set a number for how many copies of each package are retained. In other words, if you have downloaded 25 versions of Firefox over the life of your install and you set this number to \"3\", only the most recent 3 versions will be retained. Unless you are very short on disk space, it is recommended to set this to at least 2.

\
By selecting \"Remove only the versions of uninstalled packages\", pamac will retain all versions of packages you still have installed.

# [Using the Pamac CLI]

Pamac also includes a fully functional CLI for when you don\'t have a working GUI or for those that prefer to manage packages that way.

\

**Do not use sudo with pamac.**

------------------------------------------------------------------------

Using sudo with pamac can have undesirable effects, especially when building packages. It also can lead to Permission issues with the database. Pamac will ask for escalated rights only if needed.

## [Locating and Installing Packages]

To search for available packages you can use the command `pamac search`. For example, to search the repos for packages containing the word smplayer:

\

[\$] [pamac search smplayer]\

    smplayer-themes  1:20.11.0-2                                         extra
        Themes for SMPlayer
    smplayer-skins  1:20.11.0-4                                          extra
        Skins for SMPlayer
    smplayer  25.6.0-1                                                   extra
        Media player with built-in codecs that can play virtually all
        video and audio formats

\

As you can see, this will also show you which packages are already installed. If you would like to search both the repos and [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") you add `-a` like this:

\

[\$] [pamac search \--aur smplayer]\

    papirus-smplayer-theme-git  20181024-2                                 AUR
        Papirus theme for SMPlayer (git version)
    buuf-smplayer  1.0-0                                                   AUR
        Theme for SMPlayer
    smplayer-themes  1:20.11.0-2                                         extra
        Themes for SMPlayer
    smplayer-skins-git  20.11.0.rc3d8454-1                                 AUR
        Skins for SMPlayer
    smplayer-skins  1:20.11.0-4                                          extra
        Skins for SMPlayer
    smplayer-git  24.5.0.10283.r3.gc817337-1                               AUR
        Media player with built-in codecs that can play virtually all
        video and audio formats
    smplayer  25.6.0-1                                                   extra
        Media player with built-in codecs that can play virtually all
        video and audio formats

\
Once you have identified the packages you wish to install, you can install them with command `pamac install`. For example, if we wanted to install `smplayer` and `smplayer-themes` we could use the command:

[user \$ ][ pamac install smplayer smplayer-themes [COPY TO CLIPBOARD]]

\

\

**tip**

------------------------------------------------------------------------

When using install, pamac will check to see if packages are installed and only install the ones not already installed

\
If you want to install packages from [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository") you use the command `pamac build`. Sticking with the above example, if you decided you wanted to install `umplayer` instead you could use the command:

[user \$ ][ pamac build umplayer [COPY TO CLIPBOARD]]

\

## [Removing Packages]

The command `pamac remove` can be used to uninstall packages installed from the repos or [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository"). For example, if you wanted to remove all the packages installed above, you could use the command:

[user \$ ][ pamac remove smplayer smplayer-themes umplayer [COPY TO CLIPBOARD]]

\

\

\

**Carefully review the list of packages before confirming.**

------------------------------------------------------------------------

Some packages have many packages which depend on them and you don\'t want to inadvertently remove your whole desktop environment

## [Identifying Installed Packages]

To display a list of all installed packages, you can use the command:

[user \$ ][ pamac list -i [COPY TO CLIPBOARD]]

\

## [Displaying Detailed Package Information]

To display detailed information on a package that is in the repos or installed on your system, use the command `pamac info`. Keeping with our example of SMPlayer :

[user \$ ][ pamac info smplayer [COPY TO CLIPBOARD]]

\

\
If you also would like to check packages in [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository"), you could use:

[user \$ ][ pamac info -a smplayer [COPY TO CLIPBOARD]]

\

\

## [Updating the System]

To check if updates are available, you can use the command:

[user \$ ][ pamac checkupdates -a [COPY TO CLIPBOARD]]

\

\
To update all installed packages installed from the repos or [AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository"), you can use the command:

[user \$ ][ pamac upgrade -a [COPY TO CLIPBOARD]]

\

\

**update / upgrade**

------------------------------------------------------------------------

pamac update and pamac upgrade are exactly the same. You can use them interchangeably.

## [Dealing with Orphaned Packages]

To check to see if there any orphaned packages (packages which are no longer needed) installed, you can use:

[user \$ ][ pamac list -o [COPY TO CLIPBOARD]]

\

\
To remove all orphans use the command:

[user \$ ][ pamac remove -o [COPY TO CLIPBOARD]]

\

\

## [Cleaning the Cache]

When pamac installs packages, it keeps a copy of all the old packages you have downloaded. This cache can be very useful if you have to install older packages in an emergency. However, left unchecked, this cache will grow very large over time.

Otherwise, to clear the cache completely, enter the following command (and use with care):

[user \$ ][ pamac clean [COPY TO CLIPBOARD]]

\

A safer way to remove old package cache files is to remove all packages except for the latest three package versions using:

[user \$ ][ pamac clean \--keep 3 [COPY TO CLIPBOARD]]

\

\

## [Other Useful Pamac Functions]

To see which package owns a certain file on your system, use the command `pamac search -f`. For example:

[user \$ ][ pamac search -f /usr/bin/smplayer [COPY TO CLIPBOARD]]

\

\
To force a package to be installed even if it is already installed, use `pamac reinstall`. For example:

[user \$ ][ pamac reinstall smplayer [COPY TO CLIPBOARD]]

\