> **Warning: running Sway as a `startup` service is not officially supported.**
>
> This guide is community-maintained. Please don't open issues if it doesn't work.

Sway can be integrated with the event driven task and service manager,
[startup](https://gitlab.com/chinstrap/startup).

This integration offers a simple and unified interface for process management
when compared to using Sway standalone. startup can offer integration with
logind or ConsoleKit, device hotplug events, ACPI events, network device
events, and more.

Two main paths can be chosen while performing this integration:

1. startup supervising Sway.
2. Sway supervising startup.

Rather than attempting to explain the benefits of either approach as I see them,
I will allow the reader to decide which is best for them.

## startup supervising Sway

In this integration mode, information from the Sway session must be injected into
startup so that other startup jobs can connect to Sway.

This can be accomplished by adding the following to your Sway config:

```
exec initctl set-env --global SWAYSOCK="$SWAYSOCK"
exec initctl set-env --global I3SOCK="$I3SOCK"
exec initctl set-env --global WAYLAND_DISPLAY="$WAYLAND_DISPLAY"
# include only if xwayland is enabled and startup jobs need to access X
exec initctl set-env --global DISPLAY="$DISPLAY"
exec initctl emit sway-session
```

Next, add a startup job configuration for sway, swayidle, swaybg, and mako.

```
# ~/.config/startup/sway.conf
start on startup
stop on session-end
respawn
normal exit 0
exec env -u UPSTART_JOB sway
```

```
# ~/.config/startup/swayidle.conf
start on sway-session
stop on stopping sway
emits swayidle
emits swayactive
env TIME=60
respawn
exec swayidle timeout "$TIME" 'initctl emit -n swayidle' \
              resume 'initctl emit -n swayactive'
```

```
# ~/.config/startup/swaybg.conf
start on swaybg
stop on stopping sway
respawn
exec swaybg -o '*' -i /usr/share/backgrounds/default -m fill
```

```
# ~/.config/startup/mako.conf
start on sway-session
stop on stopping sway
respawn
reload signal 0
exec mako
```

If you are using logind or CK, you may want to use inhibitors to detect sleep.

```
# ~/.config/startup/elogind-inhibit.conf
start on startup or dbus SIGNAL='PrepareForSleep' ARG0='FALSE' BUS='system' INTERFACE='org.freedesktop.login1.Manager'
stop on session-end or dbus SIGNAL='PrepareForSleep' ARG0='TRUE' BUS='system' INTERFACE='org.freedesktop.login1.Manager'
respawn
exec elogind-inhibit --what=sleep --who=startup --mode=delay --why="Session Sleep Hook" -- pause
pre-stop exec initctl emit sleep
```

Then any user services can inhibit the suspend action by hooking into this
job's stopping event.

```
# ~/.config/startup/swaylock.conf
start on sleep
stop on stopping sway
respawn
normal exit 0
exec swaylock
```

You may want to create additional job configurations for services such as
dbus, gpg/ssh agent, redshift/gammastep, or similar.

Additionally, applications can be started at the beginning of the session
using [dex](https://github.com/jceb/dex).

Once you have configured the jobs you want to run, startup can be invoked as
`startup --user` (e.g. from your shell startup config, as you would have invoked sway).