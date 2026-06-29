[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Install+Desktop+Environments&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Install_Desktop_Environments "Install Desktop Environments (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Install_Desktop_Environments/tr "Masaüstü Ortamlarını Yükleme (1% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Install_Desktop_Environments/ru "Установка окружения рабочего стола (30% translated)") • ‎[עברית](//wiki.manjaro.org/index.php?title=Install_Desktop_Environments/he "התקנת סביבות שולחן עבודה (1% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Install_Desktop_Environments/zh-cn "安装桌面环境 (1% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Desktop Environments]](#Desktop_Environments)
    -   [[2.1] [Issues With of Using Multiple DEs]](#Issues_With_of_Using_Multiple_DEs)
    -   [[2.2] [Screenshots]](#Screenshots)
    -   [[2.3] [Xfce]](#Xfce)
        -   [[2.3.1] [Install a basic Xfce environment]](#Install_a_basic_Xfce_environment)
    -   [[2.4] [KDE Plasma 6]](#KDE_Plasma_6)
        -   [[2.4.1] [Install a basic KDE Plasma environment]](#Install_a_basic_KDE_Plasma_environment)
    -   [[2.5] [GNOME]](#GNOME)
        -   [[2.5.1] [Install a basic GNOME environment]](#Install_a_basic_GNOME_environment)
    -   [[2.6] [Cinnamon]](#Cinnamon)
        -   [[2.6.1] [Install a basic Cinnamon environment]](#Install_a_basic_Cinnamon_environment)
    -   [[2.7] [Budgie]](#Budgie)
        -   [[2.7.1] [Install a basic Budgie environment]](#Install_a_basic_Budgie_environment)
    -   [[2.8] [Cosmic]](#Cosmic)
        -   [[2.8.1] [Install the Cosmic environment]](#Install_the_Cosmic_environment)
    -   [[2.9] [Deepin]](#Deepin)
        -   [[2.9.1] [Install a basic deepin environment]](#Install_a_basic_deepin_environment)
    -   [[2.10] [Enlightenment]](#Enlightenment)
        -   [[2.10.1] [Install a basic E environment]](#Install_a_basic_E_environment)
    -   [[2.11] [LXDE (X11)]](#LXDE_.28X11.29)
        -   [[2.11.1] [Install a basic LXDE environment]](#Install_a_basic_LXDE_environment)
    -   [[2.12] [LXQt (X11 and Wayland)]](#LXQt_.28X11_and_Wayland.29)
        -   [[2.12.1] [Install a basic LXQt environment]](#Install_a_basic_LXQt_environment)
    -   [[2.13] [MATE (X11)]](#MATE_.28X11.29)
        -   [[2.13.1] [Install a basic MATE environment]](#Install_a_basic_MATE_environment)
-   [[3] [Window Managers]](#Window_Managers)
    -   [[3.1] [Stacking Window Managers]](#Stacking_Window_Managers)
        -   [[3.1.1] [Openbox (X11)]](#Openbox_.28X11.29)
        -   [[3.1.2] [FluxBox (X11)]](#FluxBox_.28X11.29)
        -   [[3.1.3] [IceWM (X11)]](#IceWM_.28X11.29)
    -   [[3.2] [Tiling Window Managers]](#Tiling_Window_Managers)
        -   [[3.2.1] [Awesome (X11)]](#Awesome_.28X11.29)
        -   [[3.2.2] [i3 (X11)]](#i3_.28X11.29)

# [Overview]

There are several desktop environments and window managers available for Manjaro, each with their own unique style, interface, and features. Furthermore, it is possible to install multiple environments if desired, which can be selected at the login screen at any time. Users are not restricted to whatever comes pre-installed with a particular flavour of Manjaro.

# [Desktop Environments]

It is worth noting that a desktop environment (DE) is not a single entity; it is actually a collection of different components that work together. This commonly includes a:

-   **window manager** to display, move and resize application windows
-   **file manager** to visually browse, copy and access files, etc.
-   **background provider** to display wallpapers, etc.
-   **panel** to provide a menu and to display information such as the time
-   **settings/configuration manager** to change the look of the environment

And so on. Most desktop environments will also come with their own preferred applications, in addition to various widgets, addons, and extensions to provide extra features. As such, upon entering the commands provided below in your terminal to download and install a desktop environment, you may be prompted to choose from a selection of components provided for it. **To install a full desktop environment** - complete with its own preferred file manager, applications, and so on

Where additional (and optional) extras for a desktop environment are available, the terminal commands to obtain these have also been provided.

Some important information about installing the Manjaro settings packages:

-   The Manjaro settings packages contain the theming and settings to make the desktop the same as in the Manjaro ISOs
-   They have the naming convention manjaro-\<desktop\>-settings i.e. manjaro-xfce-settings
-   They share files so you can only have one at a time installed.
-   If you are coming from gnome you must remove the meta package **manjaro-gnome-assets** before you can install the settings package for another desktop

## [Issues With of Using Multiple DEs]

Installing multiple DEs is not without issues. Here are some things that can pop-up when running more than one DE:

-   The settings packages overlap so you can only have one DE pre-configured with the Manjaro theming. The others will need to have the theming applied manually.
-   You can end up with more than one instance of similar applications. For example, it is common to end up with 2 Bluetooth managers. It takes some tweaking to get a single manager working in multiple DEs.
-   Sometimes two different DEs will share the same configuration files causing strange things to happen, especially with theming.

These issues are greatly reduced by using a different user account for each DE. The command for adding a standard user and setting a password

Example - create a new user named **marci** and set password

[user \$ ][ sudo userad -mU marci && sudo passwd marci [COPY TO CLIPBOARD]]

\

In summary, running multiple DEs is possible and a great way to enjoy Manjaro but it requires a willingness to troubleshoot and work through minor problems. If you are the type of person who wants everything to \"just work\" out of the box, running multiple DEs might not be for you.

## [Screenshots]

The screenshots are for illustrative purposes. It will require additional (undocumented) work to achieve similar result for your system.

## [Xfce]

[![XfceDE.png](/images/thumb/8/88/XfceDE.png/375px-XfceDE.png)](//wiki.manjaro.org/index.php?title=File:XfceDE.png)

[](//wiki.manjaro.org/index.php?title=File:XfceDE.png "Enlarge")

**[Xfce](http://xfce.org/)** or **XFCE**, pronounced as four individual letters, is a lightweight and versatile desktop environment that utilises a classic drop-down/pop-up menu to access applications. It is also compatible with **[Compiz](//wiki.manjaro.org/index.php?title=Compiz_and_Emerald "Compiz and Emerald")**. A little time and effort will also be required to properly customise the desktop to suit personal taste. As of version 18, Manjaro has moved to the gtk3 version of Xfce.

\

\

### [Install a basic Xfce environment]

[user \$ ][ sudo pacman -S xfce4 xfce4-goodies xfce4-terminal network-manager-applet xfce4-notifyd xfce4-whiskermenu-plugin tumbler engrampa [COPY TO CLIPBOARD]]

\

**Optional:** Install and use LightDM, the recommended display manager for Xfce

[user \$ ][ sudo pacman -S lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings [COPY TO CLIPBOARD]]

\

[user \$ ][ sudo systemctl enable lightdm.service \--force [COPY TO CLIPBOARD]]

\

edit **/etc/lightdm/lightdm.conf**, under \[Seat:\*\] replace the greeter-session setting with **greeter-session=lightdm-gtk-greeter**

**Optional:** Install the Manjaro configuration and theming for Xfce

[user \$ ][ sudo pacman -S manjaro-xfce-settings manjaro-settings-manager [COPY TO CLIPBOARD]]

\

To configure LightDM to match the official iso replace the contents of /etc/lightdm/lightdm-gtk-greeter.conf with

\[greeter\]

    background = /usr/share/backgrounds/illyria-default-lockscreen.jpg
    font-name = Cantarell Bold 12
    xft-antialias = true
    icon-theme-name = Papirus
    screensaver-timeout = 60
    theme-name = Matcha-azul
    cursor-theme-name = xcursor-breeze
    show-clock = false
    default-user-image = #avatar-default
    xft-hintstyle = hintfull
    position = 50%,center 50%,center
    clock-format =
    panel-position = bottom
    indicators = ~host;~spacer;~clock;~spacer;~language;~session;~a11y;~power

\

## [KDE Plasma 6]

[![KDEPlasmaDE.png](/images/thumb/6/62/KDEPlasmaDE.png/375px-KDEPlasmaDE.png)](//wiki.manjaro.org/index.php?title=File:KDEPlasmaDE.png)

[](//wiki.manjaro.org/index.php?title=File:KDEPlasmaDE.png "Enlarge")

**[The KDE community](http://www.kde.org/)** offers [Plasma](https://www.kde.org/plasma-desktop), a feature-rich and versatile desktop environment that provides several different styles of menu to access applications. An excellent built-in interface to easily access and install new themes, widgets, etc, from the internet is also worth mentioning.

\

**Warning**

------------------------------------------------------------------------

The various components for Plasma which is available using the internet, should be used with care. Theming on Plasma is not just a bunch of icons and colors - it is based on QML, the Qt model language which is specific for the used version of Qt.

### [Install a basic KDE Plasma environment]

[user \$ ][ sudo pacman -S plasma kio-extras [COPY TO CLIPBOARD]]

\

**Optional:** Install KDE applications

To install a full set of K\* applications use **kde-applications-meta**. This will be \~300 packages(including dependencies)

[user \$ ][ sudo pacman -S kde-applications-meta [COPY TO CLIPBOARD]]

\

**Optional:** Install and use [SDDM](https://wiki.manjaro.org/index.php?title=Install_Display_Managers#SDDM), the recommended display manager for KDE

SDDM is installed as a dependency of plasma. To enable it execute below command and restart the system

[user \$ ][ systemctl enable sddm.service \--force [COPY TO CLIPBOARD]]

\

**Optional:** Install the Manjaro configuration and theming for plasma

[user \$ ][ sudo pacman -S manjaro-kde-settings sddm-breath-theme manjaro-settings-manager [COPY TO CLIPBOARD]]

\

Open plasma settings, go to Startup & Shutdown-\>Login Screen and select \"Breath\"

Alternatively, the newer themes may be installed with:

[user \$ ][ sudo pacman -S plasma-themes-breath [COPY TO CLIPBOARD]]

\

\

## [GNOME]

[![Gnome-de-18.jpg](/images/thumb/d/d8/Gnome-de-18.jpg/375px-Gnome-de-18.jpg)](//wiki.manjaro.org/index.php?title=File:Gnome-de-18.jpg)

[](//wiki.manjaro.org/index.php?title=File:Gnome-de-18.jpg "Enlarge")

**[GNOME](http://www.gnome.org/)** is an intuitive desktop environment that utilises a tablet or smartphone style interface to access applications. It is not compatible with compiz. Although GNOME is very easy to learn and use, it has limited customisation options and it can be difficult to configure.

\

\

\

### [Install a basic GNOME environment]

[user \$ ][ sudo pacman -S gnome [COPY TO CLIPBOARD]]

\

**Optional:** To install extra themes, games, and features

[user \$ ][ sudo pacman -S gnome-extra [COPY TO CLIPBOARD]]

\

**Optional:** Install and use GDM, the recommended display manager for GNOME

GDM is installed as a dependency of GNOME. To enable it:

[user \$ ][ systemctl enable gdm.service \--force [COPY TO CLIPBOARD]]

\

**Optional:** Install the Manjaro configuration and theming for GNOME

[user \$ ][ sudo pacman -S manjaro-gnome-settings manjaro-settings-manager [COPY TO CLIPBOARD]]

\

\

## [Cinnamon]

[![Cinnamon screenshot.jpeg](/images/thumb/7/7f/Cinnamon_screenshot.jpeg/375px-Cinnamon_screenshot.jpeg)](//wiki.manjaro.org/index.php?title=File:Cinnamon_screenshot.jpeg)

[](//wiki.manjaro.org/index.php?title=File:Cinnamon_screenshot.jpeg "Enlarge")

**[Cinnamon](http://cinnamon.linuxmint.com/)** is a desktop environment based on GNOME 3 that utilises a large panel-style menu to access applications. It is not compatible with compiz. Despite being based on GNOME, it has more customisation options and therefore is easier to configure. Windows Vista or 7 users may find Cinnamon\'s interface comfortably familiar.

\

\

### [Install a basic Cinnamon environment]

[user \$ ][ sudo pacman -S cinnamon [COPY TO CLIPBOARD]]

\

**Optional:** Install additional commonly used components

[user \$ ][ sudo pacman -S cinnamon-wallpapers cinnamon-sounds gnome-terminal parcellite [COPY TO CLIPBOARD]]

\

**Optional:** Install and use LightDM, the recommended display manager for cinnamon

[user \$ ][ sudo pacman -S lightdm lightdm-slick-greeter lightdm-settings [COPY TO CLIPBOARD]]

\

[user \$ ][ systemctl enable lightdm.service \--force [COPY TO CLIPBOARD]]

\

Then edit */etc/lightdm/lightdm.conf*, under **\[Seat:\*\]** replace the greeter-session setting with **greeter-session=lightdm-slick-greeter**

**Optional:** Install the Manjaro configuration and theming for Cinnamon

[user \$ ][ sudo pacman -S manjaro-cinnamon-settings adapta-maia-theme kvantum-manjaro [COPY TO CLIPBOARD]]

\

To configure LightDM to match the community edition replace the contents of /etc/lightdm/slick-greeter.conf with

    [Greeter]
    background=/usr/share/backgrounds/greeter_default.jpg
    background-color=#263138
    draw-grid=false
    theme-name=Adapta-Nokto-Eta-Maia
    icon-theme-name=Papirus-Dark-Maia
    font-name='Cantarell 11'
    xft-antialias=true
    xft-hintstyle=hintfull
    enable-hidpi=auto

Set the Manjaro logo on the panel by right-clicking on the menu and clicking configure. Select \"Use a custom icon and label\". Select the Manjaro icon.

\

## [Budgie]

**Note**

------------------------------------------------------------------------

There is not currently a Manjaro settings package for Budgie

[![Budgie.jpg](/images/thumb/b/b9/Budgie.jpg/375px-Budgie.jpg)](//wiki.manjaro.org/index.php?title=File:Budgie.jpg)

[](//wiki.manjaro.org/index.php?title=File:Budgie.jpg "Enlarge")

The **[Budgie Desktop](https://github.com/BuddiesOfBudgie/budgie-desktop)** is a modern desktop designed to keep out the way of the user. It features heavy integration with the GNOME stack in order for an enhanced experience.

\

\

\

\

### [Install a basic Budgie environment]

[user \$ ][ sudo pacman -S budgie-desktop network-manager-applet gnome-control-center gnome-screensaver [COPY TO CLIPBOARD]]

\

**Optional:** Install additional commonly used components

[user \$ ][ sudo pacman -S gnome-terminal nautilus budgie-extras dconf-editor [COPY TO CLIPBOARD]]

\

**Optional:** Install and use LightDM, the recommended display manager for budgie

[user \$ ][ sudo pacman -S lightdm lightdm-slick-greeter lightdm-settings [COPY TO CLIPBOARD]]

\

[user \$ ][ systemctl enable lightdm.service \--force [COPY TO CLIPBOARD]]

\

edit */etc/lightdm/lightdm.conf*, under **\[Seat:\*\]** replace the greeter-session setting with **greeter-session=lightdm-slick-greeter**

To configure LightDM to match the official iso replace the contents of /etc/lightdm/slick-greeter.conf with

    [Greeter]
    background=/usr/share/backgrounds/manjaro-budgie/manjaro-budgie.jpg
    theme-name=Matcha-sea
    icon-theme-name=Papirus-Maia
    draw-grid=false

\

## [Cosmic]

**Note**

------------------------------------------------------------------------

There is not currently a Manjaro settings package for Cosmic

[![Cosmic-desktop.png](/images/thumb/4/45/Cosmic-desktop.png/375px-Cosmic-desktop.png)](//wiki.manjaro.org/index.php?title=File:Cosmic-desktop.png)

[](//wiki.manjaro.org/index.php?title=File:Cosmic-desktop.png "Enlarge")

The **[Cosmic Desktop](https://system76.com/cosmic)** COSMIC is a free and open-source desktop environment for Linux and other Unix-like operating systems. Originally a modified version of GNOME made for Pop! OS, it was later rebuilt from scratch as a standalone desktop environment using the Iced toolkit \-- More info [Wikipedia](https://en.wikipedia.org/wiki/COSMIC_desktop).

### [Install the Cosmic environment]

[user \$ ][ sudo pacman -S cosmic [COPY TO CLIPBOARD]]

\

**Optional:** Enable the cosmic greeter

[user \$ ][ sudo systemctl enable cosmic-greeter \--force [COPY TO CLIPBOARD]]

\

\

## [Deepin]

**Note**

------------------------------------------------------------------------

There is not currently a Manjaro settings package for Deepin

[![Deepin.jpg](/images/thumb/8/8f/Deepin.jpg/375px-Deepin.jpg)](//wiki.manjaro.org/index.php?title=File:Deepin.jpg)

[](//wiki.manjaro.org/index.php?title=File:Deepin.jpg "Enlarge")

The **[Deepin Desktop](https://www.deepin.org/en/dde/)** is an elegant, easy to use desktop. It is lightly configurable.

\

\

\

\

### [Install a basic deepin environment]

[user \$ ][ sudo pacman -S deepin [COPY TO CLIPBOARD]]

\

**Optional:** Install the Deepin applications suite

[user \$ ][ sudo pacman -S deepin-extra [COPY TO CLIPBOARD]]

\

**Optional:** Install and use LightDM, the recommended display manager for deepin

[user \$ ][ sudo pacman -S lightdm [COPY TO CLIPBOARD]]

\

[user \$ ][ systemctl enable lightdm.service \--force [COPY TO CLIPBOARD]]

\

Then edit */etc/lightdm/lightdm.conf*, under **\[Seat:\*\]** replace the greeter-session setting with **greeter-session=lightdm-deepin-greeter**

\

## [Enlightenment]

**Note**

------------------------------------------------------------------------

There is not currently a Manjaro settings package for Enlightenment

[![E20-Green Onix 760.png](/images/thumb/5/5e/E20-Green_Onix_760.png/375px-E20-Green_Onix_760.png)](//wiki.manjaro.org/index.php?title=File:E20-Green_Onix_760.png)

[](//wiki.manjaro.org/index.php?title=File:E20-Green_Onix_760.png "Enlarge")

**[Enlightenment](http://www.enlightenment.org/)**, sometimes known simply as E, is a lightweight desktop environment known for its configurability and tools for creating beautiful user interfaces using its Enlightenment Foundation Libraries (EFL). E started in 1997 as a stacking window manager, emerging as a desktop environment since development release version 0.17. E does not come with a broad array of tools by default, which can be an advantage for experienced users who want to customize their installation, and a disadvantage for users with little or no experience of Linux. E uses a few unique terms, for example referring to panels as "shelves".

### [Install a basic E environment]

[user \$ ][ sudo pacman -S enlightenment terminology [COPY TO CLIPBOARD]]

\

\

## [][LXDE (X11)]

**Note**

------------------------------------------------------------------------

There is not currently a Manjaro settings package for LXDE

[![Lxde17.1.11.jpg](/images/thumb/0/02/Lxde17.1.11.jpg/375px-Lxde17.1.11.jpg)](//wiki.manjaro.org/index.php?title=File:Lxde17.1.11.jpg)

[](//wiki.manjaro.org/index.php?title=File:Lxde17.1.11.jpg "Enlarge")

**[LXDE](https://github.com/lxde)** is a super-lightweight desktop environment that is very similar to XFCE, with the exception that it is not compatible with Compiz. As with XFCE, LXDE is also a somewhat basic desktop environment, lacking some modern features that would be expected, such as a search-bar to find applications and files. However, due to comparatively low resource requirements, it is also an excellent choice for less powerful computers.

See [LXDE on Github](https://github.com/lxde) for recent actvity.

### [Install a basic LXDE environment]

[user \$ ][ sudo pacman -S lxde network-manager-applet [COPY TO CLIPBOARD]]

\

**Optional:** Install and use LightDM, the recommended display manager for lxde

[user \$ ][ sudo pacman -S lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings [COPY TO CLIPBOARD]]

\

[user \$ ][ systemctl enable lightdm.service \--force [COPY TO CLIPBOARD]]

\

**Note**

------------------------------------------------------------------------

Installing LXDE will also result in installing *Openbox* as its default window manager. The LXDM display manager will also be downloaded, although it will be necessary to enable this yourself if you wish to replace your existing display manager.

To configure LightDM to match the community edition replace the contents of /etc/lightdm/lightdm-gtk-greeter.conf with

    [greeter]
    background = /usr/share/backgrounds/lxde-breath.png
    font-name = Cantarell 12
    xft-antialias = true
    icon-theme-name = Arc-Maia
    screensaver-timeout = 60
    theme-name = Adapta-Eta-Maia
    cursor-theme-name = xcursor-breeze
    show-clock = false
    default-user-image = #avatar-default
    xft-hintstyle = hintfull
    position = 50%,center 50%,center
    clock-format =
    panel-position = bottom

\

## [][LXQt (X11 and Wayland)]

**Note**

------------------------------------------------------------------------

There is not currently a Manjaro settings package for LXQt

[![Lxqt-de-18.png](/images/thumb/f/f2/Lxqt-de-18.png/375px-Lxqt-de-18.png)](//wiki.manjaro.org/index.php?title=File:Lxqt-de-18.png)

[](//wiki.manjaro.org/index.php?title=File:Lxqt-de-18.png "Enlarge")

The **[LXQt Desktop Environment](https://lxqt-project.org/)** LXQt is a lightweight Qt desktop environment. It was formed from the merger of the LXDE and Razor-qt projects.

LXQt support both X11 and Wayland protocols. Wayland support is acheived by using the **labwc** window manager.

\

\

\

\

### [Install a basic LXQt environment]

[user \$ ][ sudo pacman -S lxqt xscreensaver [COPY TO CLIPBOARD]]

\

**Optional:** Install and use LightDM, the recommended display manager for LXQt

[user \$ ][ sudo pacman -S lightdm lightdm-slick-greeter lightdm-settings light-locker [COPY TO CLIPBOARD]]

\

[user \$ ][ systemctl enable lightdm.service \--force [COPY TO CLIPBOARD]]

\

edit /etc/lightdm/lightdm.conf, under \[Seat:\*\] replace the greeter-session setting with greeter-session=lightdm-slick-greeter\

## [][MATE (X11)]

**Note**

------------------------------------------------------------------------

There is not currently a Manjaro settings package for Mate

[![Mate.jpg](/images/thumb/0/00/Mate.jpg/375px-Mate.jpg)](//wiki.manjaro.org/index.php?title=File:Mate.jpg)

[](//wiki.manjaro.org/index.php?title=File:Mate.jpg "Enlarge")

**[MATE](https://mate-desktop.org/)** is a desktop environment and the continuation of GNOME 2. Featuring an intuitive and attractive desktop environment while preserving a traditional desktop experience, its aim is to maintain and continue the latest GNOME 2 code base, frameworks, and core applications.

\

\

\

\

### [Install a basic MATE environment]

[user \$ ][ sudo pacman -S mate network-manager-applet [COPY TO CLIPBOARD]]

\

**Optional:** Install MATE applications and configuration tools

[user \$ ][ sudo pacman -S mate-extra dconf-editor [COPY TO CLIPBOARD]]

\

**Optional:** Install and use LightDM, the recommended display manager for MATE

[user \$ ][ sudo pacman -S lightdm lightdm-slick-greeter lightdm-settings [COPY TO CLIPBOARD]]

\

[user \$ ][ systemctl enable lightdm.service \--force [COPY TO CLIPBOARD]]

\

edit **/etc/lightdm/lightdm.conf**, under \[Seat:\*\] replace the greeter-session setting with **greeter-session=lightdm-slick-greeter**

To configure LightDM to match the community edition replace the contents of /etc/lightdm/slick-greeter.conf with

    [Greeter]
    background=/usr/share/backgrounds/manjaro-mate/manjaro-mate.jpg
    theme-name=Adapta-Nokto-Maia
    icon-theme-name=Arc-Maia
    draw-grid=false

\

# [Window Managers]

**Note**

------------------------------------------------------------------------

By nature, building your own desktop environment from a Window Manager will take substantially more time and effort than simply downloading a pre-defined desktop environment.

\

**Warning**

------------------------------------------------------------------------

The images provided below are purely for illustrative purposes only. You will have you put in the necessary time and effort to configure them.

Although desktop environments commonly provide a good range of customisation options to suit personal taste and preference, they may still be seen as somewhat restrictive or controlled in the sense that they merely allow for the personalisation of their pre-defined components. However, certain Window Managers (WM) empower users to take a \'do it yourself\' approach in order to create their own desktop environments. In essence, they may be used as a foundation on which to build upon, as literally every component and every aspect of the desktop is under the direct control and choice of the user. An environment may be as elaborate or as minimalistic as desired, and it is even possible to mix and match various components from other desktop environments.

Therefore extremely powerful and versatile, these window managers also carry the additional benefit of being faster and more resource efficient than pre-defined desktop environments. Interestingly, the super-lightweight LXDE environment is itself built on the Openbox window manager. There are two types of Window Manager: **Stacking** and **Tiling**. These names denote how application windows will behave on your desktop.

## [Stacking Window Managers]

**Stacking window managers** are by far the most popular, and essentially allow application windows to be moved freely around the screen, which may overlap - or \'stack\' - upon one another, hence the name. All popular desktop environments such as Xfce, KDE Plasma and GNOME use stacking window Managers.

### [][Openbox (X11)]

[![Manjarobox.png](/images/thumb/2/2b/Manjarobox.png/375px-Manjarobox.png)](//wiki.manjaro.org/index.php?title=File:Manjarobox.png)

[](//wiki.manjaro.org/index.php?title=File:Manjarobox.png "Enlarge")

**[Openbox](http://openbox.org/)** is by far the most popular Window Manager available. Due to its popularity there is excellent documentation available, as well as a good choice of additional themes that may be downloaded. **To install Openbox, enter the command:**

[user \$ ][ sudo pacman -S openbox obconf lxappearance-obconf [COPY TO CLIPBOARD]]

\

\

### [][FluxBox (X11)]

[![Fluxbox2.png](/images/thumb/8/8c/Fluxbox2.png/375px-Fluxbox2.png)](//wiki.manjaro.org/index.php?title=File:Fluxbox2.png)

[](//wiki.manjaro.org/index.php?title=File:Fluxbox2.png "Enlarge")

**[FluxBox](http://fluxbox.org/)** is another popular Window Manager. It is particularly notable for providing some features not seen in Openbox, such as *tabbing*, which allows for windows to be grouped together. **To install FluxBox, enter the command**:

[user \$ ][ sudo pacman -S fluxbox [COPY TO CLIPBOARD]]

\

\

### [][IceWM (X11)]

[![Icewm2.jpg](/images/thumb/6/6b/Icewm2.jpg/375px-Icewm2.jpg)](//wiki.manjaro.org/index.php?title=File:Icewm2.jpg)

[](//wiki.manjaro.org/index.php?title=File:Icewm2.jpg "Enlarge")

**[IceWM](https://www.ice-wm.org/)** is a Window Manager notable for perhaps being closer to a full desktop environment than Openbox or FluxBox. This includes providing a panel complete with menu, in addition to a workspace switcher. **To install IceWM, enter the command**:

[user \$ ][ sudo pacman -S icewm [COPY TO CLIPBOARD]]

\

\

## [Tiling Window Managers]

**Tiling window managers** - as the name would suggest - tile application windows; each will have their own place on the screen, just like conventional tiles do not overlap. However, unlike conventional tiling, these window managers are usually very flexible, and allow for a multitude of different tiling patterns to suit personal taste and preference. Where stacking window managers focus on using the mouse for navigation, tiling window managers focus on the utilisation of the keyboard instead. As such, they can be much faster to use.

### [][Awesome (X11)]

[![Awesome.png](/images/thumb/1/13/Awesome.png/375px-Awesome.png)](//wiki.manjaro.org/index.php?title=File:Awesome.png)

[](//wiki.manjaro.org/index.php?title=File:Awesome.png "Enlarge")

**[Awesome](http://awesome.naquadah.org/)** is a popular tiling Window Manager, notable for using the **Lua** language for configuration. **To install Awesome, enter the command**:

[user \$ ][ sudo pacman -S awesome vicious [COPY TO CLIPBOARD]]

\

\

### [][i3 (X11)]

[![I3wm.png](/images/thumb/8/8c/I3wm.png/375px-I3wm.png)](//wiki.manjaro.org/index.php?title=File:I3wm.png)

[](//wiki.manjaro.org/index.php?title=File:I3wm.png "Enlarge")

**[i3](http://i3wm.org/)** is arguably the most popular tiling window manager available, and notable for using a single, completely self-contained configuration file. **To install i3, enter the command**:

[user \$ ][ sudo pacman -S i3-wm i3lock i3status [COPY TO CLIPBOARD]]

\

\