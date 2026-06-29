Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Wacom_Tablet_And_Pen/tr "Wacom Tablet ve Kalem (13% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Wacom_Tablet_And_Pen/fr "Tablette et stylet Wacom (23% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Wacom_Tablet_And_Pen/ru "Планшет и перо Wacom (100% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Wacom_Tablet_And_Pen/zh-cn "Wacom 数位板和数位笔 (17% translated)")

## Contents

-   [[1] [Tablets and Pen displays (wacom but not only)]](#Tablets_and_Pen_displays_.28wacom_but_not_only.29)
-   [[2] [Different Desktop Environments]](#Different_Desktop_Environments)
    -   [[2.1] [Cinnamon, Gnome and Budgie]](#Cinnamon.2C_Gnome_and_Budgie)
    -   [[2.2] [KDE Plasma 5]](#KDE_Plasma_5)
    -   [[2.3] [XFCE and probably MATE]](#XFCE_and_probably_MATE)
-   [[3] [Known Issues]](#Known_Issues)
    -   [[3.1] [Slow drag in File Manager]](#Slow_drag_in_File_Manager)
    -   [[3.2] [Gnome DE]](#Gnome_DE)
    -   [[3.3] [The device is not recognized]](#The_device_is_not_recognized)
    -   [[3.4] [KDE Plasma 5]](#KDE_Plasma_5_2)
    -   [[3.5] [Mixed configurations]](#Mixed_configurations)
-   [[4] [More information]](#More_information)

## [][Tablets and Pen displays (wacom but not only)]

## [Different Desktop Environments]

### [][Cinnamon, Gnome and Budgie]

The only thing that is needed to install aside from the default installer is the package `xf86-input-wacom`.

\

### [KDE Plasma 5]

The package `xf86-input-wacom` will be automatically installed when installing the `kcm-wacomtablet` from community repository.

This will add Tablet Settings interface/configuration in the System Settings + the needed background services for KDE Plasma Framework.

### [XFCE and probably MATE]

There is a workaround proposed by [achadwick](https://github.com/achadwick/gsdwacom4xfce) and works just fine. They use the Gnome settings interface.

\

## [Known Issues]

### [Slow drag in File Manager]

Slow drag in File Manager and very slow interaction of Tools and Brushes in Krita. \\ The resolution is to modify the `10-evdev.conf` in `/usr/share/X11/xorg.conf.d/10-evdev.conf`

There might be necessary to make a symlink of it like this:

    sudo ln -s /usr/share/X11/xorg.conf.d/10-evdev.conf /etc/X11/xorg.conf.d/10-evdev.conf

    ~ >>> cat /etc/X11/xorg.conf.d/10-evdev.conf
    #
    # Catch-all evdev loader for udev-based systems
    # We don't simply match on any device since that also adds accelerometers
    # and other devices that we don't really want to use. The list below
    # matches everything but joysticks.

    Section "InputClass"
            Identifier "evdev pointer catchall"
            MatchIsPointer "on"
            MatchDevicePath "/dev/input/event*"
            Driver "evdev"
    EndSection

    #Section "InputClass"
    #        Identifier "evdev keyboard catchall"
    #        MatchIsKeyboard "on"
    #        MatchDevicePath "/dev/input/event*"
    #        Driver "evdev"
    #EndSection

    #Section "InputClass"
    #        Identifier "evdev touchpad catchall"
    #        MatchIsTouchpad "on"
    #        MatchDevicePath "/dev/input/event*"
    #        Driver "evdev"
    #EndSection

    #Section "InputClass"
    #        Identifier "evdev tablet catchall"
    #        MatchIsTablet "on"
    #        MatchDevicePath "/dev/input/event*"
    #        Driver "evdev"
    #EndSection

    #Section "InputClass"
    #        Identifier "evdev touchscreen catchall"
    #        MatchIsTouchscreen "on"
    #        MatchDevicePath "/dev/input/event*"
    #        Driver "evdev"
    #EndSection

\

### [Gnome DE]

In Gnome, if someone wants to use the GDM theme of a custom gnome-shell theme to have a consistent look trough login/log-out/lock-screen, the settings for mapping the buttons will render a blank overlay with no options.

**Resolutions**:

-   Use the default `gnome-shell`, `adwaita` and `gdm`
-   Use the modified `manjaro-gnome-maia-theme`

\

### [The device is not recognized]

The device is not recognized, the xinput doesn't list it, etc, that is most likely due to a not supported device, no specific ID in the `/usr/share/libwacom/` for it.

A possible resolution is to install the `input-wacom-dkms` making sure that the headers for the kernel are installed too, then manually adding the modules to load.

It will not provide a functionality if the modules are not loaded, and still relies in the `xf86-input-wacom`, `libwacom` and the Graphical interface for Tablet settings.

Of course the `xsetwacom` commands work too, but the purpose is to have a GUI for settings and avoid any confusing/miss-passed settings from terminal.

\

### [KDE Plasma 5]

In KDE Plasma 5 the `kcm-wacomtablet` recognizes the pen and tablet but the pen (Stylus) doesn't draw. By default there are no settings for them, the resolution is:

1.  Set the mode to Absolute Mode in the tablet tab and the Area to the desired screen.
2.  To the Stylus tab set the Eraser and Tip to where the slider passes slightly the letter T from the word Soft.
3.  The Raw Sample to the level 5
4.  The Suppress Rate to the level 2
5.  Edit the pressure curve to be slightly curved downwards.
6.  Set Button 3 to Right Mouse Button Click
7.  Set Button 2 to Middle Mouse Button Click
8.  Set Button 1 to Left Mouse Button Click
9.  **DO NOT** check Tap to execute action
10. Click **Apply** button, **disconnect** and **reconnect** the tablet and it should work.

From this point all the settings can be changed and have also the Express Buttons personalized, and calibrate the pen to the screen area.

The settings are stored in `~/.config/tabletprofilesrc`

\

### [Mixed configurations]

Mixed configurations due to use of `xsetwacom` commands and other tools. Resolution is to undo all and start with the GUI Settings.

\

## [More information]

-   Manjaro Forum [Search for Wacom](https://forum.manjaro.org/search?q=wacom%20order%3Alatest_topic)
-   Github [Zeioth/XFCE-Wacom-Settings](https://github.com/Zeioth/XFCE-Wacom-Settings)