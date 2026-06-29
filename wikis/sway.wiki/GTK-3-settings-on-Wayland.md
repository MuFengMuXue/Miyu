GTK+ is known for not picking up some variables from `${XDG_CONFIG_HOME}/gtk-3.0/settings.ini`, most notably themes.

This happens because when GTK+ uses the wayland backend, a subset of variables are pulled from the `gsettings` schema `org.gnome.desktop.interface`, whereas on X11 GTK talks to a XSETTINGS daemon that usually does this for you, or when missing, falls back to the user's setting.ini file.

This only applies for settings that belong to `org.gnome.desktop.interface`. Some settings, like `gtk-application-prefer-dark-theme`, are still read from your `settings.ini`.

Cursor themes can be set in GTK for now, but a better solution is to let sway handle it for you. Support for [the cursor shape protocol](https://wayland.app/protocols/cursor-shape-v1) has been [merged](https://github.com/swaywm/sway/pull/7571) and is in sway 1.9.  You also need clients to use the protocol (which usually depends on their toolkit library version).

## Workarounds

### Setting GTK_THEME

If you only care about your GTK theme, you can export the `GTK_THEME` environment variable before running your GTK programs. While this is quite simple, it's also fairly limited, since there are no environment variables to set other settings, like icon/cursor themes.

This also may cause issues with applications reading the theme from `GtkSettings` as this is a development environment variable and does not change that value.

### Setting values in `gsettings`

The proper workaround is to call `gsettings set org.gnome.desktop.interface <key> <value>` yourself at any point before starting any GTK program, for each setting that you want set. A good place to do so is either your shell's rc files, or using `exec` in your sway config.

You can list valid keys for the schema using `gsettings list-keys org.gnome.desktop.interface`; you most notably want to set `gtk-theme`, `cursor-theme` and `icon-theme`:

```
set $gnome-schema org.gnome.desktop.interface

exec_always {
    gsettings set $gnome-schema gtk-theme 'Your theme'
    gsettings set $gnome-schema icon-theme 'Your icon theme'
    gsettings set $gnome-schema cursor-theme 'Your cursor Theme'
    gsettings set $gnome-schema font-name 'Your font name'
}
```

If you'd rather have those values picked from your settings.ini file, here is a small convenient script to do just that:

```bash
#!/bin/sh

# usage: import-gsettings
config="${XDG_CONFIG_HOME:-$HOME/.config}/gtk-3.0/settings.ini"
if [ ! -f "$config" ]; then exit 1; fi

gnome_schema="org.gnome.desktop.interface"
gtk_theme="$(grep 'gtk-theme-name' "$config" | sed 's/.*\s*=\s*//')"
icon_theme="$(grep 'gtk-icon-theme-name' "$config" | sed 's/.*\s*=\s*//')"
cursor_theme="$(grep 'gtk-cursor-theme-name' "$config" | sed 's/.*\s*=\s*//')"
font_name="$(grep 'gtk-font-name' "$config" | sed 's/.*\s*=\s*//')"
gsettings set "$gnome_schema" gtk-theme "$gtk_theme"
gsettings set "$gnome_schema" icon-theme "$icon_theme"
gsettings set "$gnome_schema" cursor-theme "$cursor_theme"
gsettings set "$gnome_schema" font-name "$font_name"
```

Importing the gtk, icon, and cursor themes:

```
exec_always import-gsettings
```


### Removing the rounded corners and dropshadow of themes like Adwaita

If you use 1 pixel border the theme's shadow can leak underneath, also sway's border can only be without border radius so to remove any of these issues make a file at `${XDG_CONFIG_HOME}/gtk-3.0/gtk.css` put following selectors there.

```
/** Some apps use titlebar class and some window */
.titlebar,
window {
	border-radius: 0;
	box-shadow: none;
}

/** also remove shadows */
decoration {
	box-shadow: none;
}

decoration:backdrop {
	box-shadow: none;
}
```


## XSettings

Some GTK applications running via XWayland, and some Java applications, need an XSettings daemon running in order to pick up the themes and font settings.

One implementation is [xsettingsd](https://codeberg.org/derat/xsettingsd).

Gnome (or rather, the Gnome Settings Daemon) provides its own XSettings daemon, usually installed at `/usr/lib/xsettings`.