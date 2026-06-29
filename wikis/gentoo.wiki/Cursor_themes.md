This article provides instructions for cursor theme management on an X11-based system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Cursor theme is not loaded at all]](#Cursor_theme_is_not_loaded_at_all)
    -   [[3.2] [Cursor keeps going back to default X cursors]](#Cursor_keeps_going_back_to_default_X_cursors)
    -   [[3.3] [GTK 2 and GTK 3]](#GTK_2_and_GTK_3)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [Emerge]

Before installing any new packages, check to see what cursors are available on the system. Cursors can be found beneath the [/usr/share/cursors/] directory.

[[[x11-themes/xcursor-themes]](https://packages.gentoo.org/packages/x11-themes/xcursor-themes)[]] comes with the whiteglass and the redglass themes:

`root `[`#`]`emerge --ask x11-themes/xcursor-themes`

### [Additional software]

Other packages with some Gentoo themed cursors is available as well.

[[[x11-themes/gentoo-xcursors]](https://packages.gentoo.org/packages/x11-themes/gentoo-xcursors)[]] comes with gentoo, gentoo-blue, and gentoo-silver cursor themes:

`root `[`#`]`emerge --ask x11-themes/gentoo-xcursors`

To install all of the cursor themes available from Portage:

`root `[`#`]`emerge --ask x11-themes/blueglass-xcursors x11-themes/chameleon-xcursors x11-themes/comix-xcursors x11-themes/gentoo-xcursors x11-themes/golden-xcursors x11-themes/haematite-xcursors x11-themes/neutral-xcursors x11-themes/obsidian-xcursors x11-themes/pearlgrey-xcursors x11-themes/silver-xcursors x11-themes/vanilla-dmz-aa-xcursors x11-themes/vanilla-dmz-xcursors x11-themes/xcursor-themes`

## [Configuration]

Edit the user\'s [\~/.Xresources] file:

[FILE] **`~/.Xresources`Choose a cursor theme**

    Xcursor.theme: redglass

Cursor size can be optionally chosen as well:

[FILE] **`~/.Xresources`Choose the cursor size**

    Xcursor.size: 16

## [Troubleshooting]

### [Cursor theme is not loaded at all]

For [window managers](https://wiki.gentoo.org/wiki/Window_managers "Window managers") it might be necessary to load the cursor theme before starting the window manager using [xrdb] via [\~/.xinitrc]:

[FILE] **`~/.xinitrc`**

    xrdb -merge ~/.Xresources
    eval $(dbus-launch --sh-syntax --exit-with-session <window_manager>)

Restart *X* to apply the changes:

`user `[`$`]`pkill X `

`user `[`$`]`startx `

### [Cursor keeps going back to default X cursors]

In some desktop environments the mouse theme can change when hovering outside of a window. Inside the window the mouse cursor respects the user\'s choice. But outside the window the mouse cursor changes into the default X cursor.

Create the symlink to the user\'s home path:

`user `[`$`]`ln -s /usr/share/cursors/xorg-x11 ~/.icons`

### [GTK 2 and GTK 3]

With some GTK applications the mouse cursor changes to default settings when it is inside the GTK application window. Users can fix this problem by setting the `gtk-theme-name` and `gtk-cursor-theme-name` variables in the [\~/.config/gtk-3.0/settings.ini] and [\~/.gtkrc-2.0] configuration files. In the examples below the `gentoo` cursor theme has been chosen.

For GTK 3 applications:

[FILE] **`~/.config/gtk-3.0/settings.ini`**

    [Settings]
    gtk-theme-name = gentoo
    gtk-icon-theme-name = gnome
    gtk-cursor-theme-name = gentoo
    gtk-cursor-theme-size = 16

For GTK 2 applications:

[FILE] **`~/.gtkrc-2.0`**

    gtk-theme-name = gentoo
    gtk-icon-theme-name = gnome
    gtk-cursor-theme-name = gentoo

## [See also]

-   [X resources](https://wiki.gentoo.org/wiki/X_resources "X resources") --- configuration options for X applications
-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") --- an open source implementation of the [X server](https://wiki.gentoo.org/wiki/X_server "X server").

## [External resources]

-   [Article on the Arch Linux wiki](https://wiki.archlinux.org/index.php/Cursor_themes)