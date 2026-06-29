# Uniform look for Qt and GTK applications

Qt and GTK based programs both use a different widget toolkit to render the graphical user interface. Each come with different themes, styles and icon sets by default, among other things, so the "look and feel" differ significantly. This article will help you make your Qt and GTK applications look similar for a more streamlined and integrated desktop experience.

## Overview
To get a similar look between the toolkits, you will most likely have to modify the following:
* Theme: The custom appearance of an application, widget set, etc. It usually consists of a style, an icon theme and a color theme.
* Style: The graphical layout and look of the widget set.
* Icon Theme: A set of global icons.
* Color Theme: A set of global colors that are used in conjunction with the style.

You can choose various approaches:
* Modify GTK and Qt styles separately with the tools listed below for each toolkit and aim for choosing similarly looking themes (style, colors, icons, cursors, fonts).
* Use a special theme engine, which intermediates the modification of the other graphical toolkit to match your main toolkit.

## Styles for both Qt and GTK
There are widget style sets available for the purpose of integration, where builds are written and provided for both Qt and GTK, all major versions included. With these, you can have one look for all applications regardless of the toolkit they had been written with.

## GTK ports of Qt themes
These are themes originally created for a Qt environment, but was later ported to GTK.

## Breeze
Breeze is the default Qt style of KDE Plasma. It can be installed with the  package and the  package for GTK 2 and GTK 3.

Once installed, you can use one of the many GTK configuration tools to change the GTK theme.

If running KDE Plasma, install , log-out and log-in again, and then go to System Settings > Colors & Themes > Application Style  > Configure GNOME/GTK Application Style…. Fonts, icon themes, cursors, and widget styles set in System Settings affect GTK settings automatically; only the GTK theme should be set manually using the previously mentioned module.

If you are not running KDE Plasma, you can use  and  to apply breeze to qt applications, you can also change the color scheme to be Breeze-Dark.

## Qt ports of GTK themes
These are themes originally created for a GTK environment, but was later ported to Qt.

## Adwaita
Adwaita is the default GNOME theme. The GTK 3 version is included in the  package, while the GTK 2 version is in . adwaita-qt is a Qt port of the Adwaita theme. Unlike #QGtkStyle, which mimics the GTK 2 theme, it provides a native Qt style made to look like the GTK 3 Adwaita. It can be installed with the  and  packages for the Qt 5 and 6 respectively.

To set the Qt style, set the following environment variable: . Alternatively, use  package. For more detailed instructions, see Qt#Configuration of Qt 5/6 applications under environments other than KDE Plasma.

## GTK themes ported to Kvantum
Kvantum () is an SVG-based style customizer for Qt6 that comes with a variety of built-in or external styles, including versions of some of popular GTK themes such as Adapta, Arc, Ambiance, Libadwaita and Materia. More themes can be found on the KDE Store. For Qt5 you additionally need the  package.

Kvantum works as a Qt style instead of a Qt platform theme. To set Kvantum for all Qt applications, set it in  for Qt6 or  for Qt5 respectively, or use the environment variable .

## Theme configuration
To configure a theme variant for Kvantum, such as KvLibadwaita, edit the configuration file:

or use the kvantummanager GUI.

## Theme engines
A theme engine can be thought of as a thin layer API which translates themes (excluding icons) between one or more toolkits. These engines add some extra code in the process and it is arguable that this kind of a solution is not as elegant and optimal as using native styles.

## QGtk3Style
This is a platform theme built into  starting with version 5.7.0 and . It can be used to style Qt5 and Qt6 applications according to current GTK3 style. It can be enabled by setting the following environment variable: . For users of Adwaita it can be used together with #QAdwaitaDecorations for a complete look.

## QGtkStyle
This Qt style uses GTK 2 to render all components to blend in with GNOME and similar GTK based environments. Beginning with Qt 4.5, this style is included in Qt. It requires  to be installed and configured.

This is the default Qt4 style in Cinnamon, GNOME and Xfce, and the default Qt5 style in Cinnamon, GNOME, MATE, LXDE and Xfce. In other environments:

* For Qt4, it can be enabled with Qt Configuration (), choose GTK under Appearance > GUI Style. Alternatively, edit the  (system-wide) or  (user-specific) file:

* For Qt 5, it can be enabled by installing  and setting the following environment variable:

* For Qt 6, it can be enabled by installing  and choosing the qt6gtk2 style in , or alternatively setting the following environment variable:

For full uniformity, make sure that the configured GTK theme supports both GTK 2 and GTK 3. If your preferred theme has inconsistent rendering after configuring Qt to use GTK2, install  and choose a theme. You should also make sure that the preferred theme is installed in  as  directory is not being scanned for active GTK 2 theme.

## QAdwaitaDecorations
QAdwaitaDecorations is Qt decoration plugin implementing Adwaita-like client-side decorations for Wayland. It can be installed with the  and  packages. After installing, set  to environment variable.

## QWhiteSurGtkDecorations
QWhiteSurGtkDecorations is Qt decoration plugin implementing WhiteSur-gtk-like client-side decorations for Wayland. It can be installed with the  and  packages. After installing, set  to environment variable.

## Tips and tricks
## Using a GTK icon theme in Qt applications
If you are running Plasma, run  and select the icon-theme under System Settings > Application Style > GTK.

If you are using GNOME, run  and change the  key under org > gnome > desktop > interface to your preferred icon theme.

If you are not using a desktop environment, for example if you are running a minimal system with , install  and set the icon-theme as explained above.
You might also have to set the value of  in your profile. See Environment variables#Defining variables for the possible ways to obtain the desired result.

{{Note|If the icon theme was not applied, you might want to check if the name that you entered of your preferred theme, was in the correct format. For example, if you want to apply the currently active icon theme to your Qt applications, you can find the correct format of its name with the command:

{{bc|1=$ awk -F= '/icon-theme/ {print $2}' ~/.gtkrc-2.0}}
}}

## Add Title bar and frame to GTK3 applications under KDE Plasma
To have GNOME/GTK applications display with a KDE/Plasma title bar and frame, disable client-side decorations as described in GTK#Client-side decorations.

## Improve subpixel rendering of GTK applications under KDE Plasma
See Font configuration#LCD filter.

## Consistent file dialog under KDE Plasma
To have the same file dialog across applications in KDE Plasma, you can use XDG Desktop Portals.

Install  and  as a first step.

## Environment variable method
Historically, setting the environment variable  was sufficient for most applications. Some newer GTK applications may use  instead (see [https://gitlab.gnome.org/GNOME/gtk/-/blob/636827800525770715bba96671edb2fc0234ccc2/NEWS#L34 GTK NEWS), while others (like Betterbird 128.5.2esr-bb19, as noted in the discussion) still require the original variable. You may need to test which variable works with your specific applications, or use both to ensure maximum compatibility.

## Configuration method
Since  1.18.0, direct configuration of the portal system is recommended.

## Set the preferred portal backend
This can be configured per-user or system-wide.

User-specific configuration

Create the configuration directory:

 $ mkdir -p ~/.config/xdg-desktop-portal/

Append the following to :

System-wide configuration

As root, create the directory:

 # mkdir -p /etc/xdg/xdg-desktop-portal/

Create the file  with the following content:

## Force the desktop environment for the portal service
This ensures that the portal service uses the correct backend, regardless of the current desktop environment.

User-specific configuration

Create the override directory:

 $ mkdir -p ~/.config/systemd/user/xdg-desktop-portal.service.d/

Append the following to :

System-wide configuration

As root, create the directory:

 # mkdir -p /etc/systemd/user/xdg-desktop-portal.service.d/

Create the file  with the following content:

## Restart the portal service
Reload the systemd user daemon and restart the portal service:

This configuration method is independent of the current desktop environment and is considered more robust against future changes than relying solely on environment variables.

## Application compatibility
Not all GTK applications support KDE file dialogs correctly:

* Applications using electron should use at least electron 14 (see #19159) and properly implement this function.
* VSCode has a pull request for fixing a problem, see #126113.
* GIMP has not implemented use of the portal yet, see bug report.

## Synchronizing bookmarks
There are still lots of GTK applications that do not implement portal properly (abandoned applications, or authors are focused on other tasks). To simplify file picking from such applications, you can at least synchronize bookmarks from dolphin to nautilus. Use this command:

 $ awk -F\" '/ $HOME/.config/gtk-3.0/bookmarks

Alternatively, use  for that purpose. There you can manually edit and sync bookmarks to both sides.

## Application-specific settings
In addition to the environment variable approach, some GTK applications have their own settings for forcing use of XDG Portals:

* Firefox — See Firefox#XDG Desktop Portal integration

## Troubleshooting
## Themes not working in GTK applications
If the style or theme engine you set up is not showing in your GTK applications then it is likely your GTK settings files are not being loaded for some reason. You can check where your system expects to find these files by doing the following:

 $ export | grep gtk

Usually the expected files should be  for GTK1 and  or  for GTK 2.x.

## GTK applications do not use svg (breeze) icons after system upgrade
Try to run this to fix this issue:

 # gdk-pixbuf-query-loaders --update-cache

## GTK applications do not fully use KDE system settings
To further integrate Plasma settings on GTK applications, one may want to install ,  and . This will offer proper Qt bindings for GTK.

## kde-gtk-config "System Settings > Application Style > GTK" menu missing
When  breaks and the "Application Style > GTK" menu is missing from System Settings, it is possible to choose GTK configuration tools like  and  to be able to configure GTK 2 and GTK 3 styles.
 is desktop independent even if it comes from the LXDE project (it does not require other parts of the LXDE desktop).  is a GTK3 settings editor, designed to work properly in wlroots-based Wayland environment. The look and feel is strongly influenced by LXAppearance, but nwg-look is intended to free the user from a few inconveniences.

## Dolphin theming does not match Nautilus well
Check the section Mismatched folder view background colors for how to deal with weird coloring.

## The KDE Plasma XDG Desktop Portal is not being used
Follow XDG Desktop Portal#Force desktop environment with .

## Qt5: kvantum is not available as a style in the Qt settings app
Be sure to have  installed.

## QT_QPA_PLATFORMTHEME=kde does not style kde portal
Make sure that  is set for systemd services. Since the KDE portal is started by systemd through a dbus call https://bugs.kde.org/show_bug.cgi?id=512377 you can use the following configuration for setting this variable to a Wayland session:
