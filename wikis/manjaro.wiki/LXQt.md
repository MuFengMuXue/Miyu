Other languages:

[Deutsch](//wiki.manjaro.org/index.php?title=LXQt/de "LXQt/de (51% translated)") • ‎[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=LXQt/tr "LXQt (3% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=LXQt/ru "LXQt (100% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=LXQt/fa "اِل‌ایکس‌کیوت (LXQt) (22% translated)") • ‎[日本語](//wiki.manjaro.org/index.php?title=LXQt/ja "LXQt/ja (12% translated)")

## Contents

-   [[1] [Overview]](#Overview)
-   [[2] [Installation]](#Installation)
-   [[3] [Window Managers]](#Window_Managers)
    -   [[3.1] [KWin]](#KWin)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Global Keyboard Shortcuts]](#Global_Keyboard_Shortcuts)
-   [[5] [Theming]](#Theming)
    -   [[5.1] [Kvantum]](#Kvantum)
    -   [[5.2] [Window Theming]](#Window_Theming)
    -   [[5.3] [GTK Theming]](#GTK_Theming)
    -   [[5.4] [Panel Theming]](#Panel_Theming)
    -   [[5.5] [Change Mouse Cursor]](#Change_Mouse_Cursor)
    -   [[5.6] [Change Icon Theme]](#Change_Icon_Theme)
    -   [[5.7] [Change Icons of Applications and System Settings]](#Change_Icons_of_Applications_and_System_Settings)
        -   [[5.7.1] [Example:]](#Example:)
    -   [[5.8] [Create Custom Icon on Panel]](#Create_Custom_Icon_on_Panel)
        -   [[5.8.1] [Example:]](#Example:_2)
    -   [[5.9] [Create Custom Icon in Start Menu / Mainmenu]](#Create_Custom_Icon_in_Start_Menu_.2F_Mainmenu)
    -   [[5.10] [Change Order of Icons on Panel]](#Change_Order_of_Icons_on_Panel)
    -   [[5.11] [Change Icon of Start Menu / Mainmenu]](#Change_Icon_of_Start_Menu_.2F_Mainmenu)
-   [[6] [See Also]](#See_Also)

# [Overview]

**LXQt** is a free and open source lightweight Qt desktop environment that was formed from the merger of the [LXDE](//wiki.manjaro.org/index.php?title=Install_Desktop_Environments#LXDE "Install Desktop Environments") and Razor-qt projects. It is focused on being a classic desktop with a modern look and feel. The official website for LXQt can be accessed [here](https://lxqt-project.org/).

\

[![Lxqt-de-18.png](/images/thumb/f/f2/Lxqt-de-18.png/600px-Lxqt-de-18.png)](//wiki.manjaro.org/index.php?title=File:Lxqt-de-18.png)

\

# [Installation]

Instructions for installing LXQt can be found on the [Install Desktop Environments](//wiki.manjaro.org/index.php?title=Install_Desktop_Environments#LXQt "Install Desktop Environments") page.

\

# [Window Managers]

LXQt is designed to be used with any window manager and does not provide one by its own.

\

## [KWin]

See article [LXQt_with_kwin](//wiki.manjaro.org/index.php?title=LXQt_with_kwin "LXQt with kwin")

\

# [Configuration]

LXQt provides the **lxqt-config** (LXQt Settings) application for configuration.

## [Global Keyboard Shortcuts]

Global shortcuts can be configured by the **lxqt-config-globalkeyshortcuts** application (LXQt settings -\> Global Shortcuts):

       <Screenshot TBD>

**warning**

------------------------------------------------------------------------

Mapping the Super_L/Super_R keys (\<Meta\> without a second key) can lead to unexpected behaviour and is not recommended!

\

**note**

------------------------------------------------------------------------

Some window manager (kwin, openbox, etc.) specific shortcuts are not configurable by LXQt (e.g. \"Alt+Tab\" for the task switcher). Those are configured by the window manager.

\

# [Theming]

In can take a few steps to get everything matching on LXQt since it is a collection of things. There are a few different things that are separately themed:

-   GTK2/GTK3
-   QT
-   Openbox
-   LXQt panels

\

## [Kvantum]

Using Kvantum is a good way to get a matching qt5 and openbox theme with a modern look

\
To install Kvantum and set a theme that matches your preferences follow the instructions [here](//wiki.manjaro.org/index.php?title=Kvantum "Kvantum").

\
After saving the settings in Kvantum Manager, open the \"LXQt Configuration Center\" and select \"Appearance\". Set the \"Qt Style\" on the \"Widgets Style\" tab to Kvantum.

\

\

**Tip**

------------------------------------------------------------------------

Using a Kvantum theme that has a matching GTK theme will give everything a uniform look

\

## [Window Theming]

The window title bars are drawn onto your screen by the window manager you use. The default window manager of LXQt is Openbox.

\
To configure OpenBox, open the \"LXQt Configuration Center\" and select \"Openbox Settings\". Then select the same theme you choose in Kvantum.

\

## [GTK Theming]

LXQt now provides an easy way to set the themes for GTK2 and GTK3 applications.

\
Open the \"LXQt Configuration Center\" and select \"Appearance\". On the \"Widget Style\" there are dropdowns to select the GTK styles.

\

## [Panel Theming]

Panel theming is available via the LXQt Configuration Center \--\> LXQt Appearance \--\> LXQt Theme

\

## [Change Mouse Cursor]

Mouse cursor theming is available via the LXQt Configuration Center \--\> LXQt Appearance \--\> Cursor.

`Adwaita` is the default mouse cursor theme in LXQt. Other mouse cursor themes can be downloaded. Example of a mouse cursor theme:

    sudo pacman -S xcursor-menda

\

## [Change Icon Theme]

The icon theme can be changed via LXQt Configuration Center \--\> LXQt Appearance \--\> Icon Theme

The default icon theme of LXQt is *oxygen-icons*. It is a relatively large download, but pretty complete.

\

## [Change Icons of Applications and System Settings]

The path of icons is saved in `.desktop` files. For each application you can find their corresponding `.desktop` files in one of these two locations:

    /usr/share/applications/

    ~/.local/share/applications/

Note that all folder names beginning with a dot are hidden folders. You need to make them visible by clicking `View --> Show Hidden` in your PcManFM-Qt File Browser. The `~` directory is your home folder.

\
Open a `.desktop` file with a text editor with root privileges and look for the following line:

    Icon=

Insert the path to the icon you want to use after the `=` symbol. A lot of system icons can be found in this location:

    /usr/share/icons/

\

### [Example:]

If you want to use a flag icon, use this line in the `.desktop` file:

    Icon=/usr/share/icons/gnome/48x48/apps/locale.png

\

## [Create Custom Icon on Panel]

Right click on your panel and choose \"Add panel widget\". Then add a Quick Launch / Starter widget. A text will appear on your panel.

You can drag and drop any icon (from your start menu / mainmenu or your custom icon file) there in order to create a Quick Launch / Starter icon in your panel. You can even drop multiple icons / icon files on one Quick Launch / Starter widget.

But if you want your custom icon in your panel, you must first create your own `.desktop` file (please keep reading).

### [Example:]

For demonstration purposes, let\'s create a custom icon, which will shut down our computer when clicked:

First, let\'s create a new file (e.g. in your home directory or any other directory you want): Right click and choose \"Create New\" \--\> \"Blank File\". Name the file `ShutDown.desktop`. You can choose any name you want, but the `.desktop` in the end is important.

Next, edit this file with a text editor. It\'s file content is supposed to look like:

    [Desktop Entry]
    Type=Application
    Name=ShutDown
    Comment=Shut down my computer
    Exec=poweroff
    Icon=/usr/share/icons/Menda-Circle/actions/scalable/bottom.svg

-   `Name=` is the name of the icon
-   `Comment=` gets shown when you hover with your mouse cursor over the icon
-   `Exec=` defines the terminal command, which is executed when the icon is clicked
-   `Icon=` specifies the path to the icon

\
Finally, you can drag and drop your custom icon file onto a Quick Launch / Starter widget in your panel (as described in the beginning of this chapter) to create your custom panel icon.

\

## [][Create Custom Icon in Start Menu / Mainmenu]

Read the [previous chapter](https://wiki.manjaro.org/index.php?title=LXQt_Theming#Create_Custom_Icon_on_Panel) of this Wiki tutorial in order to get familiar with the content of `.desktop` files.

Now, a custom `.desktop` files needs to get created (as root) in this location:

    /usr/share/applications/

Please look at other `.desktop` files as examples for the `.desktop` file content: All have a category specified, e.g.

    Categories=Qt;KDE;Settings;

This setting is important for the Start Menu / Mainmenu category this custom icons appears in. Use it.

Another important line in the `.desktop` file is:

    OnlyShowIn=LXQt;

If this is set to another desktop environment, set it to LXQt or delete this line entirely in order to see this custom icon in your Start Menu / Mainmenu.

\

## [Change Order of Icons on Panel]

You can click the right mouse button on top of a panel element in order to move it. Alternatively, you can move panel elements by holding `CTRL+Left Mouse` and draging the element. These methods work for all panel elements, except Quick Launch / Starter elements with added icons.

Quick Launch / Starter elements have \"Move Left\" and \"Move Right\" as right click options, which do enable you to freely move it. Just click the \"Remove from quicklaunch\" in order to remove the icon from the Quick Launch Widget.

Now, you can move the Quick Launch Widget like all other panel elements. After you have moved the Quick Launch Widget to the desired position on your panel, follow [this tutorial](https://wiki.manjaro.org/index.php?title=LXQt_Theming&action=edit#Create_Custom_Icon_on_Panel) to add your icon again.

\

## [][Change Icon of Start Menu / Mainmenu]

This Icon can be changed by opening the following folder with root privileges:

    /usr/share/lxqt/themes/<theme name>/

Replace \<theme name\> with the name of the theme you are currently using. The name of your current theme can be found in `System Settings>LXQT Configuration Center>LXQtAppearance>LXQt Theme`. The Start Menu icon will only get changed for \<theme name\>. All other themes still use the default icon!

In this folder, you find a `mainmenu.png` file. It is the icon of your Start Menu (called \"Mainmenu\" in LXQt). Replace this file with the icon file you want to use. Rename your icon file to the same name.

\
Great icons can be found in this thread: [https://forum.manjaro.org/index.php?topic=15613.0](https://forum.manjaro.org/index.php?topic=15613.0)

\
In order to see the changes logout and log in again. If you want to see the changes immediately run the following commands:

    killall lxqt-panel
    lxqt-panel

\

# [See Also]

-   You can find more pages about LXQt in the Manjaro Wiki [here](https://wiki.manjaro.org/index.php?title=Desktop_Environments#LXQt).