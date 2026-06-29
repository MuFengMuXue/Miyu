Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Flatpak/tr "Flatpak (8% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Flatpak/fr "Flatpak (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Flatpak/ru "Flatpak (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Flatpak/fa "فِلَت‌پَک (94% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installing Flatpak]](#Installing_Flatpak)
-   [[3] [Using Flatpak]](#Using_Flatpak)
    -   [[3.1] [Managing Flatpaks via Discover]](#Managing_Flatpaks_via_Discover)
    -   [[3.2] [Managing Flatpaks via Gnome Software]](#Managing_Flatpaks_via_Gnome_Software)
-   [[4] [Managing Flatpaks via the CLI]](#Managing_Flatpaks_via_the_CLI)
    -   [[4.1] [Finding and Installing Flatpaks]](#Finding_and_Installing_Flatpaks)
    -   [[4.2] [Displaying Detailed Flatpak Information]](#Displaying_Detailed_Flatpak_Information)
    -   [[4.3] [Getting a list of installed Flatpaks]](#Getting_a_list_of_installed_Flatpaks)
    -   [[4.4] [Updating Flatpaks]](#Updating_Flatpaks)
    -   [[4.5] [Removing Flatpaks]](#Removing_Flatpaks)
-   [[5] [Removing Flatpak Support]](#Removing_Flatpak_Support)

### [Overview]

[Flatpak](https://flatpak.org/) is a distro independent method for packaging and distributing Linux software.

\
Using software distributed by Flatpak has a couple of distinct advantages:

-   Software that is not compatible with current system libraries will still work when packaged as a Flatpak
-   Delta upgrades make upgrades more network efficient in the long-term

\
There are some other considerations to be aware of:

-   Flatpaks are not updated as part of your system updates, they must be updated separately
-   Only themes that have been ported to Flatpak will work with Flatpaks
-   A large set of shared runtimes will need to be installed to use Flatpaks

[![Flatpaklogo.png](/images/thumb/a/ad/Flatpaklogo.png/250px-Flatpaklogo.png)](//wiki.manjaro.org/index.php?title=File:Flatpaklogo.png)

\

### [Installing Flatpak]

Flatpak is available in the Manjaro repos as `flatpak`, with `libpamac-flatpak-plugin` for support in the pamac GUI and can be installed with your favorite package manager or using the command

\

[user \$ ][ pamac install flatpak libpamac-flatpak-plugin [COPY TO CLIPBOARD]]

\

### [Using Flatpak]

#### [Managing Flatpaks via Discover]

[![Kdediscover.png](/images/thumb/8/82/Kdediscover.png/400px-Kdediscover.png)](//wiki.manjaro.org/index.php?title=File:Kdediscover.png)

One way to manage your Flatpaks is with the application [Discover](https://userbase.kde.org/Discover) from the KDE project. You can install the package `discover` with your favorite package manager or the command:

[user \$ ][ pamac install discover [COPY TO CLIPBOARD]]

\

Once installed you can run **Discover** and you will be able to browse, install and update Flatpaks with a familiar store interface.

**tip**

------------------------------------------------------------------------

Discover can also install and update software from the Manjaro repos if you install the package `packagekit-qt5`

#### [Managing Flatpaks via Gnome Software]

[![Gnomesoftware.png](/images/thumb/a/a0/Gnomesoftware.png/400px-Gnomesoftware.png)](//wiki.manjaro.org/index.php?title=File:Gnomesoftware.png)

Another way to manage your Flatpaks is with the application [Gnome Software](https://wiki.gnome.org/Apps/Software) from the Gnome project. You can install the package `gnome-software` with your favorite package manager or the command:

[user \$ ][ pamac install gnome-software [COPY TO CLIPBOARD]]

\

Once installed you can run **Software** and you will be able to browse, install and update Flatpaks with a familiar store interface.

**tip**

------------------------------------------------------------------------

Gnome Software can also install and update software from the Manjaro repos

### [Managing Flatpaks via the CLI]

#### [Finding and Installing Flatpaks]

You can use the command `flatpak search` to search for available Flatpaks. For example, if you wanted to install VLC here is what it might look like:

[user \$ ][ flatpak search vlc [COPY TO CLIPBOARD]]

\

    Name                                                Description                                                                Application ID                               Version              Branch               Remotes
    MakeMKV plugin for VLC                              Provides MakeMKV features for direct Blu-ray playback in VLC.              org.videolan.VLC.Plugin.makemkv                                   3-18.08              flathub
    Bluray Java menus (BDJ) plugin for VLC              Provides Bluray Java menus (BDJ) support in VLC.                           org.videolan.VLC.Plugin.bdj                                       3-18.08              flathub
    VLC                                                 VLC media player, the open-source multimedia player                        org.videolan.VLC                                                  stable               flathub
    FDK-AAC Encoding Plugin for VLC                     Provides better AAC encoding and HE profiles support.                      org.videolan.VLC.Plugin.fdkaac                                    3-1.6                flathub

From this output we can see that VLC and some related applications via Flatpak. To install VLC, we would use it\'s \"Application ID\", shown above with the command

[user \$ ][ flatpak install org.videolan.VLC [COPY TO CLIPBOARD]]

\

This will install the application as well as any required run-times. Once the application is installed you should be able to run it from your menu as you would with any application.

#### [Displaying Detailed Flatpak Information]

You can get more details about a specific Flatpak using the command `flatpak info`. For example:

[user \$ ][ flatpak info org.videolan.VLC [COPY TO CLIPBOARD]]

\

    VLC - VLC media player, the open-source multimedia player
              ID: org.videolan.VLC
             Ref: app/org.videolan.VLC/x86_64/stable
            Arch: x86_64
          Branch: stable
         License: GPL-2.0+
          Origin: flathub
      Collection: org.flathub.Stable
    Installation: system
       Installed: 81.4 MB
         Runtime: org.kde.Platform/x86_64/5.12
             Sdk: org.kde.Sdk/x86_64/5.12
          Commit: 87a8e23cefe6c3f4962d303d3724db399872e68379a52b7553089f5540c9a883
          Parent: 8f0c0e0bd79bfeb8748bb53e8476ee1f2deffc0e131ea5fb2890505e449df8a2
         Subject: Update shared-modules for udev (d3f66ebc)
            Date: 2019-05-06 13:30:44 +0000

\

#### [Getting a list of installed Flatpaks]

To show a list of all the Flatpaks and run-times that are currently installed you can use the command:

[user \$ ][ flatpak list [COPY TO CLIPBOARD]]

\

#### [Updating Flatpaks]

Updating your collection of Flatpaks is a simple process. Simply run the command:

[user \$ ][ flatpak upgrade [COPY TO CLIPBOARD]]

\

\

#### [Removing Flatpaks]

You can remove Flatpaks with the command `flatpak uninstall`. For example:

[user \$ ][ flatpak uninstall org.videolan.VLC [COPY TO CLIPBOARD]]

\

### [Removing Flatpak Support]

If you no longer wish to have support for the Flatpack in your system you can remove it from the system by simply removing the package `flatpak` with your favorite package manager or with the command

[user \$ ][ pamac remove flatpak [COPY TO CLIPBOARD]]

\

\
To also remove any installed Flatpaks you need to remove the directories containing them. These are `/var/lib/flatpak` and `~/.local/share/flatpak`. For example, you could use the command

[user \$ ][ sudo rm -r /var/lib/flatpak [COPY TO CLIPBOARD]]

\

[user \$ ][ rm -r \~/.local/share/flatpak [COPY TO CLIPBOARD]]

\