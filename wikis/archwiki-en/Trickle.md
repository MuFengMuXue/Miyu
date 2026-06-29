# Trickle

trickle is a portable lightweight userspace bandwidth shaper, that either runs in collaborative mode (together with trickled) or in stand alone mode.

It works by preloading its own socket library wrappers, that limit traffic by delaying data.

Trickle runs entirely in userspace. == Installation ==

Install the  package.

## Usage
If you are running the daemon (see below), just start any program with "trickle" in front of it:

 # trickle pacman -Syu

Otherwise also specify upload and download limit as well as other configuration options (see [https://github.com/mariusae/trickle/blob/master/trickle.1 trickle(1) for more information):

 # trickle -s -d200 -u50 pacman -Syu

## Modifying other systemd services
Modify  for a desired systemd service,  appending . For example:

 ExecStart=/usr/bin/daemon

changes to

 ExecStart=/usr/bin/trickle /usr/bin/daemon

When using the standalone mode, also add the configuration options as described in #Usage. Restart the daemon, which should now have shaped bandwith.

## Use with rsync
Instead of putting trickle in front of the rsync command (which will not work, since rsync presumably forks the ssh process), you call rsync like this:

 rsync --rsh="trickle -d 10 -u 10 ssh" SRC DEST

## Daemon configuration
If you want to have application specific settings with trickled, create the optional  file as described in the trickled.conf(5) man page. For example:
 Priority = 1
 Time-Smoothing = 0.1
 Length-Smoothing = 2
 [ftp
 Priority = 8
 Time-Smoothing = 5
 Length-Smoothing = 20
