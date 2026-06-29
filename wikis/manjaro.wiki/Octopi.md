Other languages:

[English] • ‎[русский](//wiki.manjaro.org/index.php?title=Octopi/ru "Octopi (100% translated)")

## Contents

-   [[1] [What is Octopi?]](#What_is_Octopi.3F)
-   [[2] [Octopi - Usage]](#Octopi_-_Usage)
    -   [[2.1] [Package classification]](#Package_classification)
    -   [[2.2] [Basic usage help]](#Basic_usage_help)
    -   [[2.3] [Alt+key sequences]](#Alt.2Bkey_sequences)
    -   [[2.4] [Control+key sequences]](#Control.2Bkey_sequences)
    -   [[2.5] [F+key sequences]](#F.2Bkey_sequences)
-   [[3] [Accessing the AUR]](#Accessing_the_AUR)
-   [[4] [See Also]](#See_Also)

# [][What is Octopi?]

Octopi is a GUI Software Management (or Package Management) program that can be used instead of, or in addition to, using [pacman](//wiki.manjaro.org/index.php?title=Pacman "Pacman") in the terminal. Octopi is the default package and update manager in some Manjaro editions. (In other editions, the default is [pamac(Add/Remove Software)](//wiki.manjaro.org/index.php?title=Pamac "Pamac"))

Octopi is capable of handling updates, removal and installation of individual packages from the official repositories. It can search for files using its search field.

Octopi uses a panel applet notifier (the Octopi logo) which will turn red when there is a system update available. Right-clicking on the panel applet at any time will give an option to open Octopi on your desktop.

[![Octopimainwindow.png](/images/thumb/3/37/Octopimainwindow.png/600px-Octopimainwindow.png)](//wiki.manjaro.org/index.php?title=File:Octopimainwindow.png)\

# [Octopi - Usage]

## [Package classification]

-   An installed package
-   An installed package (not required by others)
-   A foreign package, installed from AUR
-   A non installed package
-   An outdated package
-   An outdated foreign package
-   A newer than repository package

\

## [Basic usage help]

-   Position the mouse over a package to see its description
-   Double click an installed package to see its contents
-   Right click package to install/reinstall or remove it

\

## [][Alt+key sequences]

-   Alt+1 to switch to \'Info\' tab
-   Alt+2 to switch to \'Files\' tab
-   Alt+3 to switch to \'Transaction\' tab
-   Alt+4 to switch to \'Output\' tab
-   Alt+5 to switch to \'News\' tab
-   Alt+6 or \'F1\' to show this help page

\

## [][Control+key sequences]

-   Ctrl+D or \'File/Sync database\' to sync the local database with latest remote changes (pacman -Sy)
-   Ctrl+U or \'File/System upgrade\' to make a full system upgrade (pacman -Su)
-   Ctrl+L to find a package in the package list
-   Ctrl+F to search for text inside tab Files, News and Usage
-   Ctrl+M or \'Transaction/Commit\' to start installation/removal of selected packages
-   Ctrl+E or \'Transaction/Cancel\' to clear the selection of to be removed/installed packages
-   Ctrl+G or \'File/Get latest distro news\' to retrieve the latest RSS based distro news
-   Ctrl+Q or \'File/Exit\' to exit the application
-   Control+shift+key sequences:
-   Ctrl+Shift+C to clean local packages cache (pacman -Sc)
-   Ctrl+Shift+G to display all package groups
-   Ctrl+Shift+R to remove Pacman\'s transaction lock file
-   Ctrl+Shift+Y to display AUR group

\

## [][F+key sequences]

-   F1 to show this help page
-   F4 to open a Terminal within the selected directory at Files tab
-   F6 to open a File Manager within the selected directory at Files tab
-   F10 to maximize/demaximize package list view
-   F12 to maximize/demaximize Tab\'s view

\

# [Accessing the AUR]

[![Octopi-aur-settings.png](/images/thumb/2/2c/Octopi-aur-settings.png/400px-Octopi-aur-settings.png)](//wiki.manjaro.org/index.php?title=File:Octopi-aur-settings.png)

[![Octopi-alien.png](/images/thumb/5/52/Octopi-alien.png/400px-Octopi-alien.png)](//wiki.manjaro.org/index.php?title=File:Octopi-alien.png)

Octopi can also be use to install and update applications from the [Arch User Repository(AUR)](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository"). Before doing this be sure to review [these considerations](//wiki.manjaro.org/index.php?title=Arch_User_Repository#Overview "Arch User Repository").

To enable support for AUR you first need to install a compatible helper such as trizen or pacaur. trizen is the easiest since it is available in the repos. Either use Octopi to install the package **trizen** or **pacaur** or use pacman in the terminal:

    sudo pacman -S trizen

Once you have installed trizen you can enable support in the Octopi settings by accessing the menu under Tools-\>Options. Then go to the AUR tab and enable trizen. You may also want to enable \"Search for outdated AUR packages\" to allow Octopi to update AUR packages.

To search the AUR using Octopi click on the alien icon to the left of the search bar.

\

# [See Also]

-   The [Octopi website](https://tintaescura.com/projects/octopi/) for the latest improvements in Octopi.
-   An introduction to the [Manjaro way of using the Arch rolling release system](//wiki.manjaro.org/index.php?title=The_Rolling_Release_Development_Model "The Rolling Release Development Model").
-   [Arch User Repository(AUR)](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository").
-   The [Classic Manjaro forum thread](https://web.archive.org/web/20170517182747/https://classicforum.manjaro.org/index.php?topic=2846.0).