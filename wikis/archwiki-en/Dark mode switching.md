# Dark mode switching

Switching between light and dark modes/themes is nice to have. It allows you to switch to dark mode on sunset or toggle modes with a keyboard shortcut.

The switch between themes can apply to currently running programs, probably requiring a daemon, or only to newly launched ones.
This article focuses on switching at runtime, so toggling during use affects currently running programs.

Switching between light and dark mode requires support from applications or application toolkits like GTK and Qt.

If you don't need live theme switching, to quickly set a dark theme system-wide Install , ,  and  and Export ,  and .

## Tools
*
*
*

## Toolkits
## GTK
To change the light/dark mode, you have to change the used theme.

Most themes do have a dark variant and those have by convention the suffix . For example the default GTK theme  has the variant .

To permanently change to the dark variant, see GTK#Dark theme variant

To switch themes instantly for running programs, either a daemon providing the xsettings spec or gsettings is required. For desktops running with Xorg, an xsettings daemon is needed. For desktops running with Wayland, gsettings is queried. To query gsettings configuration, GTK requires the  XDG Desktop Portal, provided by , to be running.

## xsettings daemon
xsettings is queried for Xorg sessions.

The xsettings daemon from Xfce is xfsettingsd, which is provided by the  package.

To query current GTK theme:

 $ xfconf-query -c xsettings -p /Net/ThemeName

To set GTK theme:

 $ xfconf-query -c xsettings -p /Net/ThemeName -s "new-theme"

Changes to this entry are instant and affect all GTK applications.

## gsettings
gsettings is queried for Wayland sessions. For this to work, you need xdg-desktop-portal-gtk running.

To query the current GTK theme:

 $ gsettings get org.gnome.desktop.interface gtk-theme

To set the GTK theme:

 $ gsettings set org.gnome.desktop.interface gtk-theme "new-theme"

Alternatively, if your theme does not apply the dark scheme to Gtk4 applications, you can request the dark variant of the default theme:

 $ gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
or light variant:
 $ gsettings set org.gnome.desktop.interface color-scheme 'prefer-light'

Changes to this entry are instant and affect all GTK applications.

Note that not all GTK themes support both light and dark variants. Notably, if you are using KDE, the Breeze GTK theme does not support it. You can switch to Adwaita theme by running the command below.

## KDE
If you are using KDE and want to switch dark and light modes on the fly (even at the cost of different themes for Qt and GTK apps), you can switch the GTK theme to one that supports both dark and light variant - like the default Adwaita theme.
You can switch to the Adwaita theme by running:

 $ gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita'

and if you want to revert to KDE default theme, run:

 $ gsettings set org.gnome.desktop.interface gtk-theme 'Breeze'

Doing this will allow you to switch theme even on already running apps using the color-scheme command above. It will also respect the KDE dark/light setting, that can be switched on in KDE Settings.

## Qt
Qt has theme support similar to GTK.

One method to theme Qt applications is using GTK for styling.
Changes to the GTK theme then affect Qt applications as well.

Another method is using a native Qt theme, e.g. . To switch between themes, you can follow Qt#Configuration of Qt 5/6 applications under environments other than KDE Plasma.

## Applications
## Firefox
Firefox automatically uses the current GTK theme mode and adapts the appearance of the browser accordingly. See Firefox#Dark themes for some more settings and caveats.

To change web content smartly, the Dark Reader Add-On is recommended.

By setting  to , Dark Reader activates automatically with dark GTK themes.

## Libreoffice
LibreOffice automatically uses the current GTK theme mode. To manually set it, use:

 Tools > Options > Preferences > View > Appearance > Mode: Dark.

## Thunderbird
Thunderbird conforms with the current GTK Theme, but some changes are recommended.

See Thunderbird#Theming tweaks.

## Visual Studio Code
To change the theme in Visual Studio Code, this script may help.

It also supports automatic theme switching based on the system theme. Configure the  file to include .

The following settings can also be customized to set which light and dark themes are used when switching. By default, they are set to  and , respectively:
 "workbench.preferredLightColorTheme": "Default Modern Light",
 "workbench.preferredDarkColorTheme": "Default Modern Dark",

If  is set to , it will take precedence over the  setting.

## IntelliJ
The Auto Dark Mode plugin will automatically switch themes based on the current GTK theme once installed.

## Alacritty
Alacritty has support for multiple custom color schemes. The configuration syntax and published color schemes can be found here.

To quickly change theme, you should declare a pointer to each color scheme, for example . Then you can switch to a color scheme by simply setting . This change to the configuration file is instant and affects all currently running instances. If not, you may have to set .

The borders and title bar are themed with GTK. To abide by the GTK theme, you should set the setting  to the default .

## Ghostty
Ghostty has support for  Light and Dark Themes

To use it, add a line to the configuration file specifying the themes for dark and light mode:
 theme = dark:catppuccin-frappe,light:catppuccin-latte
Link to docs

## Obsidian
Obsidian automatically adapts its theme to the system theme by default.

This can be set in:
 Settings > Appearance > Base color scheme > Adapt to system
