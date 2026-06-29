[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Using+Manjaro+for+Beginners&language=en&action=page&filter= "Special:Translate")

Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=Using_Manjaro_for_Beginners/de "Manjaro für Einsteiger (50% translated)") • ‎[English](//wiki.manjaro.org/index.php?title=Using_Manjaro_for_Beginners "Using Manjaro for Beginners (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Using_Manjaro_for_Beginners/tr "Yeni Başlayanlar İçin Manjaro'yu Kullanma (86% translated)") • ‎[español](//wiki.manjaro.org/index.php?title=Using_Manjaro_for_Beginners/es "Manjaro para principiantes (93% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Using_Manjaro_for_Beginners/fr "Utiliser Manjaro -- Guide du débutant (86% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Using_Manjaro_for_Beginners/ru "Использование Manjaro для начинающих (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Using_Manjaro_for_Beginners/fa "نحوه استفاده از مانجارو برای مبتدی‌ها (50% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Using_Manjaro_for_Beginners/zh-cn "初学者使用Manjaro (14% translated)")

## Contents

-   [[1] [Welcome to Manjaro!]](#Welcome_to_Manjaro.21)
    -   [[1.1] [Software Updates and Management using Add/Remove Software (pamac-manager)]](#Software_Updates_and_Management_using_Add.2FRemove_Software_.28pamac-manager.29)
    -   [[1.2] [Manjaro Settings Manager]](#Manjaro_Settings_Manager)
    -   [[1.3] [The Arch User Repository (AUR)]](#The_Arch_User_Repository_.28AUR.29)
    -   [[1.4] [Using the Terminal]](#Using_the_Terminal)
    -   [[1.5] [Using Multiple Kernels]](#Using_Multiple_Kernels)
    -   [[1.6] [Adding Printing Capabilities]](#Adding_Printing_Capabilities)

## [][Welcome to Manjaro!]

This guide provides a brief overview of some key knowledge points necessary to get the most out of using the Manjaro operating system.

### [][Software Updates and Management using Add/Remove Software (pamac-manager)]

[![Screenshot pamac-pkgs.png](/images/thumb/1/13/Screenshot_pamac-pkgs.png/375px-Screenshot_pamac-pkgs.png)](//wiki.manjaro.org/index.php?title=File:Screenshot_pamac-pkgs.png)

[](//wiki.manjaro.org/index.php?title=File:Screenshot_pamac-pkgs.png "Enlarge")

Pamac, in the menus add Add/Remove software, is Manjaro\'s graphical software manager. **Add/Remove Software** is a very simple yet powerful tool to add and remove software packages (applications) from your system. Upon launching, it will automatically check the official Manjaro Repositories for new and updated software. Once complete, simply enter the name or short description of what you want to install or remove, and click the **Find** button. All installed and available software matching your search will then be displayed on the right. Click the name of any result to see more information about it immediately below.

You can also search graphically by Categories, Groups, and Repositories. Searching by Categories allows you to find software related to a certain category, e.g. Music & Audio, Utilities, Development, etc. Searching by Groups allows you to find software related to a certain group, e.g. manjaro-tools. Searching by Repositories allows you to find software in a certain repository, e.g. core, extra, community, or multilib.

\

[![Screenshot pamac update.png](/images/thumb/3/3a/Screenshot_pamac_update.png/375px-Screenshot_pamac_update.png)](//wiki.manjaro.org/index.php?title=File:Screenshot_pamac_update.png)

[](//wiki.manjaro.org/index.php?title=File:Screenshot_pamac_update.png "Enlarge")

A checkbox next to the package name will indicate whether it is installed or not.

-   **To install a package**, click the adjacent checkbox to mark it for installation.
-   **To remove an installed package**, click the adjacent checkbox to mark it for removal.

Once package boxes have been marked and/or cleared, you may undertake more searches before clicking the Apply (check mark) button to conform your choice(s). It really is that simple!

-   **To update packages**, click the Updates tab, look over your selections, then click Apply

The **Pamac Updater** will automatically check and notify you of any available system updates. A full guide to using pamac is available [here](//wiki.manjaro.org/index.php?title=Pamac "Pamac").

\
Your package manager will list the dependencies required for software packages in the information pane. For example, as illustrated, if the VLC Media Player were to be installed, then several other software packages \--such as to allow it to play different media formats\-- would also be automatically be downloaded if not already installed on the system. Without them, the Media Player would not be able to play certain media formats, or perhaps not be able to play anything at all!

**Tip**

------------------------------------------------------------------------

You won\'t need to worry about dependencies yourself, as they will be automatically identified and downloaded for you when necessary.

### [Manjaro Settings Manager]

[![Screenshot msm.png](/images/thumb/2/2e/Screenshot_msm.png/375px-Screenshot_msm.png)](//wiki.manjaro.org/index.php?title=File:Screenshot_msm.png)

[](//wiki.manjaro.org/index.php?title=File:Screenshot_msm.png "Enlarge")

The [Manjaro Settings Manager](//wiki.manjaro.org/index.php?title=Manjaro_Settings_Manager "Manjaro Settings Manager") offers you GUI settings, which are either enabled by Manjaro (i.e. installation of multiple kernels and easy installation of non-proprietary and proprietary graphics drivers) or are missing from at least some of the popular [Desktop Environments and Window Managers](//wiki.manjaro.org/index.php?title=Desktop_Environments "Desktop Environments"). Manjaro Settings Manager is under development and might offer even more settings in the future than illustrated on the left.

\

### [][The Arch User Repository (AUR)]

[![Yaourtsearch.png](/images/thumb/5/5e/Yaourtsearch.png/375px-Yaourtsearch.png)](//wiki.manjaro.org/index.php?title=File:Yaourtsearch.png)

[](//wiki.manjaro.org/index.php?title=File:Yaourtsearch.png "Enlarge")

Although Manjaro is compatible to Arch \--being based on Arch itself\-- it is not possible to access the official repositories of the Arch System to download software. Manjaro instead uses its own official repositories in order to ensure that any software packages provided (e.g., system updates and applications) have been fully tested and are completely stable before release.

However, it is still possible to access additional software packages from the Arch User Repository (AUR), which is managed by the Arch community of users themselves. Although this repository is unofficial, software packages first placed here are known to make their way into Arch\'s official repositories if they become popular enough. A **[guide on how to Access the AUR](//wiki.manjaro.org/index.php?title=Arch_User_Repository "Arch User Repository")** has been provided.

\

### [Using the Terminal]

[![Terminal-88.png](/images/thumb/6/6f/Terminal-88.png/375px-Terminal-88.png)](//wiki.manjaro.org/index.php?title=File:Terminal-88.png)

[](//wiki.manjaro.org/index.php?title=File:Terminal-88.png "Enlarge")

In simple terms, a terminal (or console) is an interface that allows for text commands to be entered and displayed. As it is an exceptionally powerful and versatile tool to use, Arch and other Arch-based systems are notable for relying far more heavily on its use than other (user-friendly) distributions such as *Ubuntu* or *Mint*, which have placed a greater focus on the use of Graphical User Interfaces (GUI).

Although GUIs do undertake many common tasks that have been provided with Manjaro, particularly to assist new users \-- just as with other user-friendly distributions \-- it may on occasion be necessary to use the terminal to get something done. **Most of the guides contained in the wiki rely on using the terminal, particularly where solving problems and tweaking the system is concerned**. For those users who wish to learn more about how Manjaro works, and for those who wish to take full advantage of its versatility, it is highly recommended to learn how to use the terminal. Don\'t worry: it\'s not that hard or scary, and this wiki can be used to guide you every step of the way.

\

### [Using Multiple Kernels]

[![Kernel select.png](/images/thumb/e/e1/Kernel_select.png/375px-Kernel_select.png)](//wiki.manjaro.org/index.php?title=File:Kernel_select.png)

[](//wiki.manjaro.org/index.php?title=File:Kernel_select.png "Enlarge")

The Linux kernel is the core of a Linux operating system. It acts as an interface between your computer\'s hardware and the applications that run on it. Manjaro not only supports the use of multiple kernels (selectable from the boot screen), but allows easy access to the very latest, bleeding-edge kernels as well. All available kernels installed on your system will be presented upon booting up, including back-up copies of each kernel version installed. If sub-menus are in effect, you will need to press Enter on the second item of a set.

Having most of the supported kernels available means you have the ability choose from having bleeding-edge kernel updates or sticking with a stable LTS kernel. No matter what kernel you choose, you will still get access to the latest applications.

A **[guide on how to manage kernels](//wiki.manjaro.org/index.php?title=Manjaro_Kernels "Manjaro Kernels")** has been provided.

\

### [Adding Printing Capabilities]

[![CUPS7.png](/images/thumb/4/4e/CUPS7.png/375px-CUPS7.png)](//wiki.manjaro.org/index.php?title=File:CUPS7.png)

[](//wiki.manjaro.org/index.php?title=File:CUPS7.png "Enlarge")

It is easy to add printers in Manjaro. Full instructions on installing the necessary software are provided in the **[Printing](//wiki.manjaro.org/index.php?title=Printing "Printing")** guide.