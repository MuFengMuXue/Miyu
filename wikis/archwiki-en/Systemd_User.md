# Systemd/User

systemd offers the ability to manage services under the user's control with a per-user systemd instance, enabling them to start, stop, enable, and disable their own user units. This is convenient for daemons and other services that are commonly run for a single user, such as mpd, or to perform automated tasks like fetching mail.

## How it works
As per default configuration in , the  module automatically launches a  instance when the user logs in for the first time. This process will survive as long as there is some session for that user, and will be killed as soon as the last session for the user is closed. When #Automatic start-up of systemd user instances is enabled, the instance is started on boot and will not be killed. The systemd user instance is responsible for managing user services, which can be used to run daemons or automated tasks with all the benefits of systemd, such as socket activation, timers, dependency system, and strict process control via cgroups.

Similar to system units, user units are located in the following directories (ordered by ascending precedence):

*  where units provided by installed packages belong.
*  where units of packages that have been installed in the home directory belong.
*  where system-wide user units are placed by the system administrator.
*  where the user puts their own units.

When a systemd user instance starts, it brings up the per user target . Other units can be controlled manually with . See .

## Basic setup
All the user units will be placed in . If you want to start units on first login, execute  for any unit you want to be autostarted.

## Environment variables
Units started by user instance of systemd do not inherit any of the environment variables set in places like  etc. There are several ways to set environment variables for them:
* For users with a  directory, create a .conf file in the  directory with lines of the form . Affects only that user's user unit. See  for more information.
* Use the  option in  file. Affects all user units.
* Add a drop-in configuration file in , see #Service example
* Add a drop-in configuration file in  (affects all users), see #Service example
* At any time, use  or . Affects all user units started after setting the environment variables, but not the units that were already running.
* Using the  command provided by dbus. Has the same effect as , but also affects the D-Bus session. You can add this to the end of your shell initialization file.
* For "global" environment variables for the user environment you can use the  directories which are parsed by some generators. See  and  for more information.
* You can also write a  script which can produce environment variables that vary from user to user, this is probably the best way if you need per-user environments (this is the case for , , etc).

One variable you may want to set is .

After configuration, the command  can be used to verify that the values are correct. You may need to run  for changes to take effect immediately.

## systemd user instance
The above only addresses default environment variables for user units. However, the systemd user instance itself is also affected by some environment variables. In particular, certain specifiers (see ) are affected by XDG variables.

However, the systemd user instance will only use environment variables that are set when it is started. In particular, it will not try parsing files, see upstream bug #29414 (closed WONTFIX). Therefore, if such environment variables are needed, they should be set in a drop-in configuration file, see #Service example.

systemd does not provide introspection tools to check these values, however, something like the following service can be used to help checking that the specifiers expand as expected:

{{hc|$XDG_CONFIG_HOME/systemd/user/test-specifiers.service|2=
Type=oneshot
ExecStart=printf '(systemd)=(envvar)\n'
ExecStart=printf '%%s=%%s\n' %C "${XDG_CACHE_HOME}"
ExecStart=printf '%%s=%%s\n' %E "${XDG_CONFIG_HOME}"
ExecStart=printf '%%s=%%s\n' %L "${XDG_STATE_HOME}"/log
ExecStart=printf '%%s=%%s\n' %S "${XDG_STATE_HOME}"
ExecStart=printf '%%s=%%s\n' %t "${XDG_RUNTIME_DIR}"
}}

## Service example
Create the drop-in directory  and inside create a file that has the extension .conf (e.g. ):

## Re-using the shell login environment
If you normally set your environment through the shell login mechanisms (i.e. in , , , or similar), the shell login environment can be read into a systemd user instance using the  logic (as above). Create the following script:

The script invokes your  as a login shell, and dumps the resulting environment, while removing ephemeral shell variables. This is executed only once, on manager start, and can be reloaded on demand, using .

It provides the same environment block one gets with a non-interactive login shell — the same environment one would see after loging in through Getty or SSH, but not including anything set in , , and friends — including the system-wide environment from  and . This is similar to what e.g. gnome-shell does, which is [https://gitlab.gnome.org/GNOME/gnome-session/-/blob/e360e3d4438331818088aff5bbc0243c2d865943/gnome-session/leader-main.c#L233 starting a login shell, and updating systemd with the resulting environment.

## DISPLAY and XAUTHORITY
 is used by any X application to know which display to use and  to provide a path to the user's  file and thus the cookie needed to access the X server. If you plan on launching X applications from systemd units, these variables need to be set. systemd provides a script in  to import those variables into the systemd user session on X launch. So unless you start X in a nonstandard way, user services should be aware of the  and .

## PATH
If you customize your  and plan on launching applications that make use of it from systemd units, you should make sure the modified  is set on the systemd environment. Assuming you set your  in , the best way to make systemd aware of your modified  is by adding the following to  after the  variable is set:

## pam_env
Environment variables can be made available through use of the  module. See Environment variables#Using pam_env for configuration details.

## Automatic start-up of systemd user instances
The systemd user instance is started after the first login of a user and killed after the last session of the user is closed. Sometimes it may be useful to start it right after boot, and keep the systemd user instance running after the last session closes, for instance to have some user process running without any open session. Lingering is used to that effect. Use the following command to enable lingering for your own user, if polkit is installed:

 $ loginctl enable-linger

Without polkit or to enable lingering for a different user:

 # loginctl enable-linger username

To list all users which have the permit for lingering see column "LINGER" with :

 $ loginctl list-users

or inspect . To revoke lingering:

 # loginctl disable-linger username

## Writing user units
See systemd#Writing unit files for general information about writing systemd unit files.

## Example
The following is an example of a user version of the mpd service:

## Example with variables
The following is a user service used by , which takes into account variable home directories where Folding@home can find certain files:

As detailed in , the  variable is replaced by the home directory of the user running the service. There are other variables that can be taken into account in the systemd manpages.

## Reading the journal
The journal for the user can be read using the analogous command:

 $ journalctl --user

To specify a unit, one can use

 $ journalctl --user-unit myunit.service

Or, equivalently:

 $ journalctl --user -u myunit.service

## Temporary files
systemd-tmpfiles allows users to manage custom volatile and temporary files and directories just like in the system-wide way (see systemd#systemd-tmpfiles - temporary files). User-specific configuration files are read from  and , in that order. For this functionality to be used, it is needed to enable the necessary systemd user units for your user:

 $ systemctl --user enable systemd-tmpfiles-setup.service systemd-tmpfiles-clean.timer

The syntax of the configuration files is the same than those used system-wide. See the  and  man pages for details.

## Xorg and systemd
There are several ways to run xorg within systemd units. Below there are 3 options, either by starting a new user session with an xorg process, launching xorg from a systemd user service, or launching xinit and application as a service.

## Xorg as a systemd user service
Alternatively, xorg can be run from within a systemd user service. This is nice since other X-related units can be made to depend on xorg, etc, but on the other hand, it has some drawbacks explained below.

 provides integration with systemd in two ways:

* Can be run unprivileged, delegating device management to logind (see Hans de Goede commits around [https://gitlab.freedesktop.org/xorg/xserver/-/commit/82863656ec449644cd34a86388ba40f36cea11e9 this commit).
* Can be made into a socket activated service (see this commit).

Unfortunately, to be able to run xorg in unprivileged mode, it needs to run inside a session. So, right now the handicap of running xorg as user service is that it must be run with root privileges (like before 1.16), and cannot take advantage of the unprivileged mode introduced in 1.16.

This is how to launch xorg from a user service:

1. Make xorg run with root privileges for any user, by editing . This builds on Xorg#Xorg as Root by adding the stipulation that this need not be done from a physical console. That is, 's default of  is being overwritten with ; see .

2. Add the following units to

{{hc|~/.config/systemd/user/xorg@.service|2=
Description=Xorg server at display %i

Requires=xorg@%i.socket
After=xorg@%i.socket

[Service
Type=simple
SuccessExitStatus=0 1

ExecStart=/usr/bin/Xorg :%i -nolisten tcp -noreset -verbose 2 "vt${XDG_VTNR}"
}}

where {{ic|${XDG_VTNR}}} is the virtual terminal where xorg will be launched, either hard-coded in the service unit, or set  in the systemd environment with

 $ systemctl --user set-environment XDG_VTNR=1

3. Make sure to configure the  environment variable as explained above.

4. Then, to enable socket activation for xorg on display 0 and tty 2 one would do:

 $ systemctl --user set-environment XDG_VTNR=2     # So that xorg@.service knows which vt use
 $ systemctl --user start xorg@0.socket            # Start listening on the socket for display 0

Now running any X application will launch xorg on virtual terminal 2 automatically.

The environment variable  can be set in the systemd environment from , and then one could start any X application, including a window manager, as a systemd unit that depends on .

## xinit and application as a systemd service
The service below is an example to run xinit and  with user privilege.

See also .

## Some use cases
## Window manager
To run a window manager as a systemd service, you first need to run #Xorg as a systemd user service. In the following we will use awesome as an example:

## Persistent terminal multiplexer
Rather than logging you into a window manager session for your user session by default, you may want to automatically run a terminal multiplexer (such as screen or tmux) in the background.

Create the following:

Separating login from X login is most likely only useful for those who boot to a TTY instead of to a display manager (in which case you can simply bundle everything you start in ).

The dependency , like the  above, allows starting anything which should run before the multiplexer starts (or which you want started at boot regardless of timing), such as a GnuPG daemon session.

You then need to create a service for your multiplexer session. Here is a sample service, using tmux as an example and sourcing a gpg-agent session which wrote its information to . This sample session, when you start X, will also be able to run X programs, since  is set:

Enable ,  and any services you created to be run by , start  as usual and you should be done.

## Kill user processes on logout
Arch Linux builds the  package with , setting  to  by default. This setting causes user processes not to be killed when the user logs out. To change this behavior in order to have all user processes killed on the user's logout, set  in .

Note that changing this setting breaks terminal multiplexers such as tmux and GNU Screen. If you change this setting, you can still use a terminal multiplexer by using  as follows:

 $ systemd-run --scope --user command args

For example, to run  you would do:

 $ systemd-run --scope --user screen -S foo

Using  will keep the process running after logout only while the user is logged in at least once somewhere else in the system and  is still running.

After the user logs out of all sessions,  will be terminated too, by default, unless the user has "lingering" enabled [https://github.com/systemd/systemd/blob/76153ad45f09b6ae45464f2e03d3afefbb4b2afe/NEWS#L274. To effectively allow users to run long-term tasks even if they are completely logged out, lingering must be enabled for them. See #Automatic start-up of systemd user instances and  for details.

## Troubleshooting
## Runtime directory '/run/user/1000' is not owned by UID 1000, as it should
 systemdpam_systemd(systemd-user:session): Runtime directory '/run/user/1000' is not owned by UID 1000, as it should.
 systemd[1867: Trying to run as user instance, but $XDG_RUNTIME_DIR is not set

If you see errors such as this and your login session is broken, it is possible that another system (non-user) service on your system is creating this directory. This can happen for example if you use a docker container that has a bind mount to . To fix this, you can either fix the container by removing the mount, or disable/delay the docker service.

## "A stop job is running for User Manager for UID 1000"
If you see this message during shutdown, usually with a 2 minute timeout, it means that one of the user services did not stop in a timely manner. This can be caused by a misbehaving application which spawned a transient service earlier. You can simply wait for the timeout to expire, but if this bothers you, you can either create an override for the misbehaving service or reduce the global timeout for all user services.

## Finding and overriding the misbehaving service
To troubleshoot this problem, start the systemd debug shell:

 # systemctl start debug-shell

Then, reboot or shut down the system. When the problem occurs, switch to the debug shell using . To find out which service is preventing the shutdown, run:

 # systemctl --user list-jobs

For most open source applications, this problem should be reported to the respective maintainers such that an override isn't necessary. For closed source applications, however, an override can be created like so:

This will shorten the timeout of that particular service to 1 second. The  parameter is only required for transient services which do not create a  file on disk. The override will work regardless. Instead of the timeout,  can be used. This will cause the service to be killed immediately when the user manager is stopped. Only use this if you know the service can handle it.

## Changing the timeout value
If you don't care which service is preventing the shutdown, you can change the global timeout for all user services in a similar manner:

After this timeout, any user services which haven't gracefully stopped will be killed, which is equivalent to a sudden power loss. Adjust this value for your particular use case. Setting the timeout too low may cause data corruption depending on the application.
