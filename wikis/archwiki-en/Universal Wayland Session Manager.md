# Universal Wayland Session Manager

The Universal Wayland Session Manager (uwsm) wraps standalone Wayland compositors into a set of systemd units on the fly. This provides robust session management including environment, XDG Autostart support, bi-directional binding with login session, and clean shutdown.

## Installation
Install the  package.

## Configuration
## Service startup notification and vars set by compositor
In order to find the current compositor, a Wayland application run as a systemd service needs the  environment variable (or  if they are intended to run through Xwayland). Therefore this and other useful environment variables should be put into the systemd/dbus activation environment once the compositor has set their values.

The command  puts ,  and other environment variables listed via the white-space separated  list into the activation environment. It is recommended to execute this command after the compositor is ready.

If other variables set by the compositors are needed in the activation environment, they can be passed as arguments to  or put into a white-space separated list in . See the examples below:

 exec uwsm finalize VAR1 VAR2 ...
 export UWSM_FINALIZE_VARNAMES=VAR1 VAR2 ...

## Environment variables
All environment variables set in {{ic|${XDG_CONFIG_HOME}/uwsm/env}} are sourced by uwsm and available to all managed compositors and graphical applications run inside such a session.

If you need certain environment variables to be set only for a specific compositor (and graphical applications in that graphical session), then put them in {{ic|${XDG_CONFIG_HOME}/uwsm/env-compositor}} instead.

An example of such a file can be seen below:

## Usage
## Startup
uwsm can be started both by TTY and by a display manager.

## TTY
Add in your  file:

If you want to always start the same compositor, then you can use instead in your  file:

## Display manager
You can create a custom session desktop entry which starts your compositor through uwsm:

## Session termination
If you want to terminate the current uwsm session, then you should use either  (terminates the entire user session) or  (executes code after  or terminates user session, if it replaced the login shell).

## Tips and tricks
## Applications and autostart
By default uwsm launches compositors through a custom systemd service in . Many Wayland compositors allow you to start other applications that would then be launched inside the compositor service, which would uselessly consume compositor resources or even interfere with notification sockets.

To start applications as separate systemd scope units you can use , which can launch both executables

 uwsm app -- /my/program/path

and desktop entries

 uwsm app -- myprogram.desktop

By default uwsm puts launched scope units in  slice. If you want to put them in  or , then you should respectively use options , :

 uwsm app -s b -- background-app.desktop

## Alternatives
Instead of  (which runs as a Python script), you can use a faster alternative:

* uwsm's  script which communicates with uwsm's app daemon.
* , which is a shell script. You can use it as a drop-in replacement of  by setting the  environment variable as follows:
* , which is written in C++, but missing some features.
