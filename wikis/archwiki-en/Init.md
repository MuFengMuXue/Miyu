# Init

Init is the first process started during system boot. It is a daemon process that continues running until the system is shut down. Init is the direct or indirect ancestor of all other processes, and automatically adopts all orphaned processes. It is started by the kernel using a hard-coded filename; if the kernel is unable to start it, panic will result. Init is typically assigned process identifier 1.

The init scripts (or rc) are launched by the init process to guarantee basic functionality on system start and shutdown. This includes (un)mounting of file systems and launching of daemons. A service manager takes this one step further by providing active control over launched processes, or process supervision. An example is to monitor for crashes and restart processes accordingly.

These components combine to the init system. Some inits include the service manager in the init process, or have init scripts in close relation to them. These inits are below referred to as integrated, though entries in different categories may explicitly depend on each other.

## Inits (integrated)
*
*
*
*

## Inits
*
*

## Init scripts
*

## Service managers
*
*
*
*
*

## Configuration
## Migrate running services
To run daemons under the new init, save a list of running daemons:

 $ systemctl list-units --state=running "*.service" > daemons.list

and configure the #Init scripts accordingly. See also === logind ===

[https://www.freedesktop.org/wiki/Software/systemd/logind/ logind requires systemd to be the init process. As such, local sessions and other functionality is not available.

## Device permissions
Add users to respective user groups for device access and reboot. Current group membership should first be checked with .

 # usermod -a -G video,audio,power,disk,storage,optical,lp,scanner,input user

See also Users and groups#Pre-systemd groups. To create group rules for use with Polkit, see Polkit#Bypass password prompt.

## Rootless X
As  does not check if logind is active [https://bugs.freedesktop.org/show_bug.cgi?id=86975#c5, root rights for Xorg need be enabled manually.

## Power management
See  and acpid to replace Power management with systemd.

## Scheduled tasks
Arch uses timer files instead of cron by default.

## Dbus
User instances of dbus-daemon are launched by systemd/User When requiring IPC between desktop applications, restore :

{{hc|1=/etc/X11/xinit/xinitrc.d/30-dbus.sh|2=
#!/bin/bash

# launches a session dbus instance
if [ -z "${DBUS_SESSION_BUS_ADDRESS-}"  && type dbus-launch >/dev/null; then
  eval $(dbus-launch --sh-syntax --exit-with-session)
fi
}}

## Tips and tricks
## systemd-nspawn
systemd-nspawn is a tool for systemd systems. Since Linux 2.6.19, it is possible, however, to run systemd on a non-systemd system by using PID namespace. For it, the kernel needs to be configured with  and ).

The PID namespace creates a new hierarchy of processes starting with PID 1. In addition to this, systemd requires a chrooted root filesystem to be mounted. Hence, you have to at least make a bind mount, because otherwise some services will fail with

 "Failed at step NAMESPACE spawning" due to "Invalid operation"

as systemd tries to remount the root with  option.

To setup a chroot with a new PID namespace, you can use jchroot.[https://github.com/vincentbernat/jchroot.
Make sure not to mount  inside the new root before chrooting, otherwise systemd will detect the chroot environment. You can mount it later once systemd is running.

## Replacing udev
*
*
