# Docs / Plymouthd

plymouth

Developer

Kristian

Høgsberg

Developer

Ray

Strode

plymouthd

8

System Administration

plymouthd

The plymouth daemon

plymouthd

OPTION

# Description

The `plymouthd` daemon is usually run out of the initrd. It does the heavy lifting of the plymouth system, logging the session and showing the splash screen.

The `plymouth` is used to send commands to plymouthd that control its behaviour.

# Options

The following options are understood:

`--help`
Show summary of options.

`--attach-to-session`
Redirect console messages from screen to log.

`--no-daemon`
Do not daemonize.

`--debug`
Output debugging information.

`--debug-file=STRING`
File to write debugging information to.

`--mode=MODE`
Set mode to either boot or shutdown.

`--pid-file=STRING`
Write the PID of the daemon to a file.

`--kernel-command-line=STRING`
Fake kernel commandline to use.

`--tty=STRING`
TTY to use instead of default.

# See Also

`grub(8)`, `plymouth(8)`, `plymouth(1)`, <http://www.freedesktop.org/wiki/Software/Plymouth>
