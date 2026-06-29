# ConsoleKit

ConsoleKit2 is a framework for defining and tracking users, login sessions, and seats. Its function is to support multiuser setups. It also works for a single user, but offers no benefits compared to existing methods. == Installation ==

Install the  and  packages.

## Configuration
## ck-launch-session
To launch an X session with ConsoleKit, append the following to the  statement in  e.g.:

 exec ck-launch-session dbus-launch --sh-syntax --exit-with-session openbox-session

This starts Openbox with proper environment variables so it and its children are able to use ConsoleKit.

Display managers like GDM, LXDM and SLiM start ConsoleKit automatically with each X session.

## No display manager
If you are not using a display manager and ConsoleKit is not working (i.e.  command showing ), you should start your window manager using the bash_profile method: Xinit#Autostart X at login.

## Desktop environments
LightDM can be used as a login manager.

## Tips and tricks
## Use D-Bus for power operations
Shut down:

Restart:

Suspend:

Hibernate (suspend to disk):

Hybrid Sleep (suspend + hibernate):

This method assumes that you are given permission to shut the system down via PolicyKit. The default group for this is . To change this, edit  as root.

## Troubleshooting
## Running several applications from ~/.xinitrc
If several applications are to be executed from , not all of these will have ConsoleKit environment variables set. In the following example, only children of Compiz will be able to properly use ConsoleKit, but children of xterm will not.

Typically, this can be an issue when for example using Compiz standalone and some other application launchers, (gnome-do, kupfer, gmrun, xbindkeys, etc.) since children of the application launcher will not be able to use ConsoleKit. A dirty workaround is to have the entire session started by a second script, e.g. . Do not forget dbus-launch, it is likely that you will need it too:

Do not forget to make  executable.

To see whether everything is started correctly:

 $ ck-list-sessions

It should show at least one session like this one:

## Consolekit blocks active TTY
Configure init to start ConsoleKit on an unused TTY, for example:

 /usr/bin/openvt -c 63 -f -- /usr/sbin/console-kit-daemon --no-daemon &

See [https://bugs.freedesktop.org/show_bug.cgi?id=29920 for details.

## Inactive session when launching X on same TTY
Specify the  flag to startx or xinit for example:

 startx -- -keeptty

See also Xorg#Session log redirection.

## Replacing ConsoleKit with systemd-logind
Remove references to  from .

See Session to check the status of your user session.
