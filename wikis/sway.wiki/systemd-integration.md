> :information_source: This guide is community-maintained. Please don't open issues if it doesn't work.

## Managing user applications with systemd

On systemd based Linux distributions, systemd can be used as an alternative way to start and manage user services and applications. Some general examples of services managed by systemd include gpg-agent, pulseaudio, dbus, etc, but in the case of sway, such services may also include waybar, swayidle, mako, and similar. Note that this method works for both X11 and Wayland programs.

In order to integrate sway with systemd and start user applications automatically when sway starts, we need to configure a sway session target that will also bind to the standard [graphical-session.target](https://www.freedesktop.org/software/systemd/man/systemd.special.html#graphical-session.target) user target. This allows services to be started by systemd after sway launches by specifying `WantedBy=sway-session.target` or `WantedBy=graphical-session.target` in the application's systemd unit file.

To configure the sway session target, place the following systemd unit file either locally at `~/.config/systemd/user/sway-session.target`, or globally for all users at `/etc/systemd/user/sway-session.target`:

```ini
[Unit]
Description=sway compositor session
Documentation=man:systemd.special(7)
BindsTo=graphical-session.target
Wants=graphical-session-pre.target
After=graphical-session-pre.target
```

In order for the unit file to work properly, add the following lines to either `/etc/sway/config.d/10-systemd` which will include it in the default config, or add them to the end of the user's config file:

```bash
exec "systemctl --user import-environment {,WAYLAND_}DISPLAY SWAYSOCK; systemctl --user start sway-session.target"
exec swaymsg -t subscribe '["shutdown"]' && systemctl --user stop sway-session.target
```

This imports all of sway's environment variables into the systemd user manager, allowing its services to access these variables (for example the D-Bus session address), and then starts the sway session user target.

Note that the `systemctl` commands must be run synchronously and can't be split into two `exec` statements, since otherwise the session target may be started before `systemctl import-environment` is complete, and services that require certain variables will fail to run.

To walkthrough the stages of how this works:
- The user logs in via sddm or getty and the systemd user manager is automatically started (by pam_systemd and logind).
- When sway is run, it will import the environment variables into the systemd user manager and start the sway session target.
- The systemd user manager will then start all the services that depend on that target, and will provide them access to the imported env variables.

## Sway logging and journalctl

If you'd like sway's output to be handled by journald (like a systemd service), `systemd-cat` can be used for this:
```bash
exec systemd-cat --identifier=sway sway
```

You can print these logs via:

```bash
journalctl --user --identifier sway
```

Using `--follow` and `--boot` might be handy. [`journalctl(1)`](https://www.freedesktop.org/software/systemd/man/journalctl.html) for details.

## Running sway itself as a --user service
> # :warning:  Unsupported instructions
>
> **Running Sway as a systemd service is not supported**, nor recommended, nor required for anything. It may break your setup if you're not familiar enough with systemd.
>
> See [#5160](https://github.com/swaywm/sway/issues/5160) for finer details on some discussion around this.

Place the following unit file either at `~/.config/systemd/user/sway.service` or `/etc/systemd/user/sway.service`:

```ini
[Unit]
Description=sway - SirCmpwn's Wayland window manager
Documentation=man:sway(5)
BindsTo=graphical-session.target
Wants=graphical-session-pre.target
After=graphical-session-pre.target

[Service]
Type=simple
EnvironmentFile=-%h/.config/sway/env
ExecStartPre=systemctl --user unset-environment WAYLAND_DISPLAY DISPLAY # This line make you able to logout to dm and login into sway again
ExecStart=/usr/bin/sway
Restart=on-failure
RestartSec=1
TimeoutStopSec=10
```

This service file will load environment variables from `~/.config/sway/env`, a [KEY=VALUE file](https://www.freedesktop.org/software/systemd/man/systemd.exec.html#EnvironmentFile=). That's a good place to put variables such as `_JAVA_AWT_WM_NONREPARENTING=1` or `CLUTTER_BACKEND=wayland` (note: no need for export there, that is not a shell file).

Now, you want your login manager to start the service via systemd, and not sway directly. In order to do that, it's easiest to just create a new wayland session in `/usr/share/wayland-sessions/sway-session.desktop`:
```ini
[Desktop Entry]
Name=Sway Service
Comment=SirCmpwn's Wayland window manager as a systemd service
Exec=sway-service.sh
Type=Application
```
and put the sway-service.sh somewhere on your PATH (`/usr/local/bin/sway-service.sh` should be fine):
```sh
#! /bin/sh

# first import environment variables from the login manager
systemctl --user import-environment
# then start the service
exec systemctl --wait --user start sway.service
```

Next time you login via gdm/sddm just choose "sway-service", instead of just "sway".

## Start sway **without** login manager like gdm/sddm

Create the file `/etc/systemd/user/sway.service`:

```ini
[Unit]
Description=sway - SirCmpwn's Wayland window manager
Documentation=man:sway(5)
BindsTo=default.target
Wants=default.target
After=default.target

[Install]
WantedBy=default.target

[Service]
Type=simple
EnvironmentFile=-%h/.config/sway/env
ExecStart=/usr/bin/sway
Restart=on-failure
RestartSec=1
TimeoutStopSec=10
```

Then enable the systemd service: `systemctl --user enable sway.service && systemctl --user daemon-reload`. Sway will start after next `tty` login.

## Example service units for other programs

### Waybar

Starts Waybar as part of the sway session and stops it when `graphical-session.target` stops:
```ini
# ~/.config/systemd/user/waybar.service or /etc/systemd/user/waybar.service
[Unit]
Description=Highly customizable Wayland bar for Sway and Wlroots based compositors.
Documentation=https://github.com/Alexays/Waybar/wiki/
PartOf=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/waybar

[Install]
WantedBy=sway-session.target
```
Enable and start the service with `systemctl --user enable --now waybar`.

If you want Waybar to start for any graphical session, you could replace the `WantedBy=` directive with `WantedBy=graphical-session.target` before enabling it (although it might not make sense to use Waybar with gnome or i3).

### swayidle

```ini
[Unit]
Description=Idle manager for Wayland
Documentation=man:swayidle(1)
PartOf=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/swayidle -w \
            timeout 300 'swaylock -f -c 000000' \
            timeout 600 'swaymsg "output * dpms off"' \
                resume 'swaymsg "output * dpms on"' \
            before-sleep 'swaylock -f -c 000000'

[Install]
WantedBy=sway-session.target
```
## Loading environment variables from [`environment.d`](https://www.freedesktop.org/software/systemd/man/environment.d.html)

**Use case:** You want to abide by upcoming `environment.d` way of managing your environment variables

**Anti use-case:** You don't find a good enough reason to abide by `environment.d`'s way.

Handily enough, the `environment.d`'s generator returns plain `KEY=VALUE` pairs, which we can eval-export line by line. You can put something around those lines in your sway startup wrapper script.

_Sure enough: when attempting to start sway via `systemd`, you might use a systemd-recommended method to set this environment, instead._

```sh
#!/bin/bash
...
# Environment
while read -r l; do
    eval export $l
done < <(/usr/lib/systemd/user-environment-generators/30-systemd-environment-d-generator)
...
```

## Related Projects

 * [sway-systemd](https://github.com/alebastr/sway-systemd) Provides systemd integration for Sway but does not run Sway itself as a systemd service
 * [sway-services](https://github.com/xdbob/sway-services) Runs sway itself as a systemd service and provides some other systemd integration
 * [uwsm](https://github.com/Vladimir-csp/uwsm) Universal Wayland Session Manager that wraps sway (or other compositors) into systemd units. Supports XDG autostart, environment management, extendable with plugins.

## Limitations

See [#5160](https://github.com/swaywm/sway/issues/5160).