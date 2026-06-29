Without configuring portals, you may find that many desktop actions such as "open in browser" or "select a file" do not work. Not all distributions ship the necessary configuration files in their Sway package (Arch Linux is one that does it), so we need to know how to do it ourselves.

Make sure you have installed both the `gtk` and `wlr` portal backends.

## Setup the environment
From [xdg-desktop-portal-wlr](https://github.com/emersion/xdg-desktop-portal-wlr/tree/master?tab=readme-ov-file#running):
> Make sure `XDG_CURRENT_DESKTOP` is set. Make sure `WAYLAND_DISPLAY` and `XDG_CURRENT_DESKTOP` are imported into D-Bus.

See [Systemd and dbus activation environments](https://github.com/swaywm/sway/wiki#systemd-and-dbus-activation-environments)

If dbus implementation is `dbus-broker`, systemd activation environment is used:

```
exec systemctl --user set-environment "WAYLAND_DISPLAY=${WAYLAND_DISPLAY}" "XDG_CURRENT_DESKTOP=${XDG_CURRENT_DESKTOP:-sway:wlroots}"
```
If classic dbus is used, it has its own separate one:

```sh
exec dbus-update-activation-environment WAYLAND_DISPLAY "XDG_CURRENT_DESKTOP=${XDG_CURRENT_DESKTOP:-sway:wlroots}"
```
`XDG_CURRENT_DESKTOP` should be passed through in case it was set before sway (i.e. by a Display Manager)

## Set the portals Sway should use
From `portals.conf(5)`:
> Desktop environments and OS vendors should provide a configuration for their chosen portal backends in `/usr/share/xdg-desktop-portal/DESKTOP-portals.conf`, where DESKTOP is the desktop environment name as it would appear in the `XDG_CURRENT_DESKTOP` environment variable.

If your distribution didn't include it with the Sway package, you'll need to create a `sway-portals.conf` file.

> Users can override those defaults, or provide configuration for an otherwise unsupported desktop environment, by writing a file `~/.config/xdg-desktop-portal/portals.conf`. Users of more than one desktop environment can use desktop-specific filenames such as kde-portals.conf which will only be used in the appropriate desktop environment.

Create `~/.config/xdg-desktop-portal/sway-portals.conf` with the following settings:
```ini
[preferred]
default=gtk
org.freedesktop.impl.portal.Screenshot=wlr
org.freedesktop.impl.portal.ScreenCast=wlr
```

> Similarly, system administrators can provide a default configuration for all users in `/etc/xdg-desktop-portal/DESKTOP-portals.conf` or `/etc/xdg-desktop-portal/portals.conf`.

Restart Sway to apply the changes.