# Systemd

From the project web page:

:systemd is a suite of basic building blocks for a Linux system. It provides a system and service manager that runs as PID 1 and starts the rest of the system. systemd provides aggressive parallelization capabilities, uses socket and D-Bus activation for starting services, offers on-demand starting of daemons, keeps track of processes using Linux control groups, maintains mount and automount points, and implements an elaborate transactional dependency-based service control logic. Other parts include a logging daemon, utilities to control basic system configuration like the hostname, date, locale, maintain a list of logged-in users and running containers and virtual machines, system accounts, runtime directories and settings, and daemons to manage simple network configuration, network time synchronization, log forwarding, and name resolution.

Historically, what systemd calls "service" was named daemon: any program that runs as a "background" process (without a terminal or user interface), commonly waiting for events to occur and offering services. A good example is a web server that waits for a request to deliver a page, or an ssh server waiting for someone trying to log in. While these are full featured applications, there are daemons whose work is not that visible. Daemons are for tasks like writing messages into a log file (e.g. , ) or keeping your system time accurate (e.g. ntpd). For more information see .

## Basic systemctl usage
The main command used to introspect and control systemd is systemctl. Some of its uses are examining the system state and managing the system and services. See  for more details.

## Using units
Units commonly include, but are not limited to, services (.service), mount points (.mount), devices (.device) and sockets (.socket).

When using systemctl, you generally have to specify the complete name of the unit file, including its suffix, for example . There are however a few short forms when specifying the unit in the following systemctl commands:

* If you do not specify the suffix, systemctl will assume .service. For example,  and  are equivalent.
* Mount points will automatically be translated into the appropriate .mount unit. For example, specifying  is equivalent to .
* Similar to mount points, devices are automatically translated into the appropriate .device unit, therefore specifying  is equivalent to .

See  for details.

The commands in the below table operate on system units since  is the implied default for systemctl. To instead operate on user units (for the calling user), use systemctl --user without root privileges. See also systemd/User#Basic setup to enable/disable user units for all users.

{| class="wikitable"
! Action || Command || Note
|-
! colspan="3" | Analyzing the system state
|-
| Show system status ||  ||
|-
| List running units ||  or ||
|-
| List failed units ||  ||
|-
| List installed unit files1 ||  ||
|-
| Show process status for a PID ||  || cgroup slice, memory and parent
|-
! colspan="3" | Checking the unit status
|-
| Show a manual page associated with a unit ||  || as supported by the unit
|-
| Status of a unit ||  || including whether it is running or not
|-
| Check whether a unit is enabled ||  ||
|-
! colspan="3" | Starting, restarting, reloading a unit
|-
| Start a unit immediately ||  as root ||
|-
| Stop a unit immediately ||  as root ||
|-
| Restart a unit ||  as root ||
|-
| Reload a unit and its configuration ||  as root ||
|-
| Reload systemd manager configuration2 ||  as root || scan for new or changed units
|-
! colspan="3" | Enabling a unit
|-
| Enable a unit to start automatically at boot ||  as root ||
|-
| Enable a unit to start automatically at boot and start it immediately ||  as root ||
|-
| Disable a unit to no longer start at boot ||  as root ||
|-
| Disable a unit to no longer start at boot and stop it immediately ||  as root ||
|-
| Reenable a unit3 ||  as root || i.e. disable and enable anew
|-
! colspan="3" | Masking a unit
|-
| Mask a unit to make it impossible to start4 ||  as root ||
|-
| Unmask a unit ||  as root ||
|}

# See  for the directories where available unit files can be found.
# This does not ask the changed units to reload their own configurations (see the Reload action).
# For example, in case its  section has changed since last enabling it.
# Both manually and as a dependency, which makes masking dangerous. Check for existing masked units with:

## Power management
polkit is necessary for power management as an unprivileged user. If you are in a local systemd-logind user session and no other session is active, the following commands will work without root privileges. If not (for example, because another user is logged into a tty), systemd will automatically ask you for the root password.

{| class="wikitable"
! Action || Command
|-
| Shut down and reboot the system ||
|-
| Shut down and power-off the system ||
|-
| Suspend the system ||
|-
| Put the system into hibernation (write RAM to disk) ||
|-
| Put the system into hybrid-sleep state (also called suspend-to-both, it saves RAM to disk and then suspends) ||
|-
| First suspend the system, then wake up after a configured time in order to just hibernate the system ||
|-
| Perform a reboot of the userspace-only with a #Soft reboot. ||
|-
|}

## Soft reboot
Soft reboot is a special kind of a userspace-only reboot operation that does not involve the kernel. It is implemented by  and can be invoked through . As with kexec, it skips firmware re-initialization, but additionally the system does not go through kernel initialization and initramfs, and unlocked dm-crypt devices remain attached.

When  contains a valid root file system hierarchy (e.g. is the root mount of another distribution or another snapshot), soft-reboot would switch the system root into it, allowing for switching to another installation without losing states managed by kernel, e.g. networking.

## Writing unit files
The syntax of systemds unit files () is inspired by XDG Desktop Entry Specification .desktop files, which are in turn inspired by Microsoft Windows .ini files. Unit files are loaded from multiple locations (to see the full list, run ), but the main ones are (listed from lowest to highest precedence):

* : units provided by installed packages
* : units installed by the system administrator, deleted on power-off (useful for #Editing provided units)
* : units installed by the system administrator

Look at the units installed by your packages for examples, as well as .

 can help verifying the work. See the  section of that page.

## Handling dependencies
With systemd, dependencies can be resolved by designing the unit files correctly. The most typical case is when unit A requires unit B to be running before A is started. In that case add  and  to the  section of A. If the dependency is optional, add  and  instead. Note that  and  do not imply , meaning that if  is not specified, the two units will be started in parallel.

Dependencies are typically placed on services and not on #Targets. For example,  is pulled in by whatever service configures your network interfaces, therefore ordering your custom unit after it is sufficient since  is started anyway.

## Service types
There are several different start-up types to consider when writing a custom service file. This is set with the  parameter in the  section:

*  (default): systemd considers the service to be started up immediately. The process must not fork. Do not use this type if other services need to be ordered on this service, unless it is socket activated.
* : systemd considers the service started up once the process forks and the parent has exited. For classic daemons, use this type unless you know that it is not necessary. You should specify  as well so systemd can keep track of the main process.
* : this is useful for scripts that do a single job and then exit. You may want to set  as well so that systemd still considers the service as active after the process has exited. Setting  is appropriate for the units which change the system state (e.g., mount some partition). See also for the differences of simple and oneshot.
* : identical to , but with the stipulation that the daemon will send a signal to systemd when it is ready. The reference implementation for this notification is provided by libsystemd-daemon.so.
* : the service is considered ready when the specified  appears on DBus's system bus.
* : systemd will delay execution of the service binary until all jobs are dispatched unless these take longer than 5s, where the service binary is started anyway. Other than that its behaviour is very similar to . It should never be used for service ordering and is intended for helping with console output readability.

See the  man page for a more detailed explanation of the  values.

## Editing provided units
To avoid conflicts with pacman, unit files provided by packages should not be directly edited. There are two safe ways to modify a unit without touching the original file: create a new unit file which overrides the original unit or create drop-in snippets which are applied on top of the original unit. For both methods, you must reload the unit afterwards to apply your changes. This can be done either by editing the unit with  (which reloads the unit automatically) or by reloading all units with:

 # systemctl daemon-reload

## Replacement unit files
To replace the unit file , create the file  and reenable the unit to update the symlinks.

Alternatively, run:

 # systemctl edit --full unit

This opens  in your editor (copying the installed version if it does not exist yet) and automatically reloads it when you finish editing.

## Drop-in files
To create drop-in files for the unit file , create the directory  and place .conf files there to override or add new options. systemd will parse and apply these files on top of the original unit.

The easiest way to do this is to run:

 # systemctl edit unit --drop-in=drop_in_name

This opens the file  in your text editor (creating it if necessary) and automatically reloads the unit when you are done editing.
Omitting the  option will result in systemd using the default file name  .

## Revert to vendor version
To revert any changes to a unit made using  do:

 # systemctl revert unit

## Examples
For example, if you simply want to add an additional dependency to a unit, you may create the following file:

As another example, in order to replace the  directive, create the following file:

Note how  must be cleared before being re-assigned [https://bugzilla.redhat.com/show_bug.cgi?id=756787#c9. The same holds for every item that can be specified multiple times, e.g.  for timers.

One more example to automatically restart a service:

## Service logging levels
For services that send logs directly to journald or syslog, you can control their verbosity by setting a numeric value between 0 and 6 for the  parameter in the  section using the methods described above. For example:

The standard log levels are identical to those used to filter the journal. Setting a lower number excludes all higher and less important log messages from your journal.

## Suppressing a service's standard output
If a service is echoing stdout and/or stderr output, by default this will end up in the journal as well. This behavior can be suppressed by setting  and/or  in the  section. Other values than  can be used to further tweak this behavior. See .

## Targets
systemd uses targets to group units together via dependencies and as standardized synchronization points. They serve a similar purpose as runlevels but act a little differently. Each target is named instead of numbered and is intended to serve a specific purpose with the possibility of having multiple ones active at the same time. Some targets are implemented by inheriting all of the services of another target and adding additional services to it. There are systemd targets that mimic the common SystemVinit runlevels.

## Get current targets
The following should be used under systemd instead of running :

 $ systemctl list-units --type=target

## Create custom target
The runlevels that held a defined meaning under sysvinit (i.e., 0, 1, 3, 5, and 6); have a 1:1 mapping with a specific systemd target. Unfortunately, there is no good way to do the same for the user-defined runlevels like 2 and 4. If you make use of those it is suggested that you make a new named systemd target as  that takes one of the existing runlevels as a base (you can look at  as an example), make a directory , and then symlink the additional services from  that you wish to enable.

## Mapping between SysV runlevels and systemd targets
{| class="wikitable"
! SysV Runlevel !! systemd Target !! Notes
|-
| 0 || poweroff.target || Halt the system.
|-
| 1, s, single || rescue.target || Single user mode.
|-
| 2, 4 || multi-user.target || User-defined/Site-specific runlevels. By default, identical to 3.
|-
| 3 || multi-user.target || Multi-user, non-graphical. Users can usually login via multiple consoles or via the network.
|-
| 5 || graphical.target || Multi-user, graphical. Usually has all the services of runlevel 3 plus a graphical login.
|-
| 6 || reboot.target || Reboot
|-
| emergency || emergency.target || Emergency shell
|-
|}

## Change current target
In systemd, targets are exposed via target units. You can change them like this:

 # systemctl isolate graphical.target

This will only change the current target, and has no effect on the next boot. This is equivalent to commands such as  or  in Sysvinit.

## Change default target to boot into
The standard target is , which is a symlink to . This roughly corresponds to the old runlevel 5.

To verify the current target with systemctl:

 $ systemctl get-default

To change the default target to boot into, change the  symlink. With systemctl:

Alternatively, append one of the following kernel parameters to your boot loader:

*  (which roughly corresponds to the old runlevel 3),
*  (which roughly corresponds to the old runlevel 1).

## Default target order
systemd chooses the  according to the following order:

# Kernel parameter shown above
# Symlink of
# Symlink of

## systemd components
Some (not exhaustive) components of systemd are:

* kernel-install — to automatically move kernels and their respective initramfs images to the boot partition;
*  — may be used to determine boot-up performance,  statistics and retrieve other state and tracing information, and to verify the correctness of unit files. It is also used to access special functions useful for advanced debugging.
* systemd-boot — simple UEFI boot manager;
* systemd-creds — to securely store and retrieve credentials used by systemd units;
* systemd-cryptenroll — Enroll PKCS#11, FIDO2, TPM2 token/devices to LUKS2 encrypted volumes;
* systemd-firstboot — basic system setting initialization before first boot;
* systemd-homed — portable human-user accounts;
*  — session management;
* systemd-networkd — network configuration management;
* systemd-nspawn — light-weight namespace container;
* systemd-repart — creates partition tables, adds or grows partitions;
* systemd-resolved — network name resolution;
*  / run0 — Temporarily and interactively acquire elevated or different privileges.
*  — a UEFI boot stub used for creating unified kernel images;
*  — creates system users and groups and adds users to groups at package installation or boot time;
* systemd-timesyncd — system time synchronization across the network;
* systemd/Journal — system logging;
* systemd/Timers — monotonic or realtime timers for controlling .service files or events, reasonable alternative to cron.

## systemd.mount - mounting
systemd is in charge of mounting the partitions and filesystems specified in . The  translates all the entries in  into systemd units; this is performed at boot time and whenever the configuration of the system manager is reloaded.

systemd extends the usual fstab capabilities and offers additional mount options. These affect the dependencies of the mount unit. They can, for example, ensure that a mount is performed only once the network is up or only once another partition is mounted. The full list of specific systemd mount options, typically prefixed with , is detailed in .

An example of these mount options is automounting, which means mounting only when the resource is required rather than automatically at boot time. This is provided in fstab#Automount with systemd.

## GPT partition automounting
On UEFI-booted systems, GPT partitions such as , , , etc. can be mounted automatically following the Discoverable Partitions Specification. These partitions can thus be omitted from fstab, and if the root partition is automounted, then  can be omitted from the kernel command line. See .

The prerequisites are:

* When using mkinitcpio, the systemd hook is required to automount the  partition.
* All automounted partitions must reside on the same physical disk as the ESP.
* The correct GPT partition types must be set. See Partitioning#Partition scheme.
* The boot loader must set the LoaderDevicePartUUID EFI variable, so that the used EFI system partition can be identified. This is supported by systemd-boot, , Limine, GRUB (with grub-mkconfig generated ; custom  requires loading the bli module) and rEFInd (not enabled by default). This can be verified by running  and checking if there is a line with  under  or  when booting via Unified kernel images.

udev will create symlinks to the discovered partitions which can be used to reference the partitions and volumes in configuration files.

## /var
For  automounting to work, the PARTUUID must match the SHA256 HMAC hash of the partition type UUID keyed by the machine ID. The required PARTUUID can be obtained using:

 $ systemd-id128 -u var-partition-uuid

## systemd-sysvcompat
The primary role of  (required by ) is to provide the traditional linux init binary. For systemd-controlled systems,  is just a symbolic link to its  executable.

In addition, it provides four convenience shortcuts that SysVinit users might be used to. The convenience shortcuts are , ,  and . Each one of those four commands is a symbolic link to , and is governed by systemd behavior. Therefore, the discussion at #Power management applies.

systemd-based systems can give up those System V compatibility methods by using the  boot parameter (see, for example, /bin/init is in systemd-sysvcompat ?) and systemd native  command arguments.

## systemd-tmpfiles - temporary files
systemd-tmpfiles creates, deletes and cleans up volatile and temporary files and directories. It reads configuration files in  and  to discover which actions to perform. Configuration files in the former directory take precedence over those in the latter directory.

Configuration files are usually provided together with service files, and they are named in the style of . For example, the Samba daemon expects the directory  to exist and to have the correct permissions. Therefore, the  package ships with this configuration:

Configuration files may also be used to write values into certain files on boot. For example, if you used  to disable wakeup from USB devices with , you may use the following tmpfile instead:

An exclamation mark  signifies that the line is only applied at boot. This will prevent re-enabling the wakeup trigger if systemd-tmpfiles is run again after boot (for example by the pacman hook).

It is possible to write multiple lines to the same file, either with  in the argument or using the  type on multiple lines (including the first one) for appending:

See the  and  man pages for details.

## Drop-in configuration files
Configuration files provided by packages should not be directly edited to avoid conflicts with pacman updates. For this, many (but not all) systemd packages provide a way to modify the configuration, but without touching the original file by creation of drop-in snippets. Check the package manual to see if drop-in configuration files are supported.

To create a drop-in configuration file for the unit file , create the directory  and place .conf files there to override or add new options. systemd will parse and apply these files on top of the original unit.

Check the overall configuration:

 $ systemd-analyze cat-config systemd/unit.conf

The applied drop-in snippets file(s) and content will be listed at the end. Restart the service for the changes to take effect.

## Tips and tricks
## Socket activation
Some packages provide a .socket unit. For example,  provides a  unitIf  is enabled (and  is left disabled), systemd will not start CUPS immediately; it will just listen to the appropriate sockets. Then, whenever a program attempts to connect to one of these CUPS sockets, systemd will start  and transparently hand over control of these ports to the CUPS process.

## GUI configuration tools
*
*
*

## Running services after the network is up
To delay a service until after the network is up, include the following dependencies in the .service file:

The network wait service of the network manager in use must also be enabled so that  properly reflects the network status.

* If using NetworkManager,  should be enabled together with . Check if this is the case with . If it is not enabled, then reenable .
* In the case of netctl, enable the  (unless you are using netctl-auto; see ).
* If using systemd-networkd,  should be enabled together with . Check if this is the case with . If it is not enabled, then reenable .

For more detailed explanations, see the discussion in the [https://systemd.io/NETWORK_ONLINE/#discussion Network configuration synchronization points.

If a service needs to perform DNS queries, it should additionally be ordered after :

See .

For  to have any effect it needs a service that pulls it in via  and orders itself before it with . Typically this is done by local DNS resolvers.

Check which active service, if any, is pulling in  with:

 $ systemctl list-dependencies --reverse nss-lookup.target

## Enable installed units by default
By default, Arch Linux does not make use of systemd presets, and does not enable most services on installation.

If you wish for systemd presets to be honored when packages are installed, you will need to create a a pacman hook in order to run  or  whenever a new systemd unit is installed. Something like

{{hc|/etc/pacman.d/scripts/systemd-presets-hook|
#!/bin/sh -e

while read -r f; do
    unit="${f##*/}"
    # alternatively, you could read all the units and pass them to systemctl preset in a single invocation
    systemctl preset "$unit"
done
}}

Arch Linux ships with  containing . This causes systemctl preset to disable all units by default, such that when a new package is installed, the user must manually enable the unit.

To enable units by default instead, simply create a symlink from  to  or replace with a file containing  in order to override the configuration file. This will cause systemctl preset to enable all units that get installed—regardless of unit type—unless specified in another file in one systemctl presets configuration directories. User units are not affected. It is also possible to configure higher priority files with more specific rules on what should be enabled. See  for more information.

## Sandboxing application environments
See systemd/Sandboxing.

## Notifying about failed services
In order to notify about service failures, an  directive needs to be added to the according service file, for example by using a drop-in configuration file. Adding this directive to every service unit can be achieved with a top-level drop-in configuration file. For details about top-level drop-ins, see .

Create a top-level drop-in for services:

This adds  to every service file. If some_service_unit fails,  will be started to handle the notification delivery (or whatever task it is configured to perform).

Create the  template unit:

You can create the  script and define what to do or how to notify. Examples include sending e-mail, showing desktop notifications, using gotify, XMPP, etc. The  will be the name of the failed service unit and will be passed as an argument to the script.

In order to prevent a recursion for starting instances of  again and again if the start fails, create an empty drop-in configuration file with the same name as the top-level drop-in (the empty service-level drop-in configuration file takes precedence over the top-level drop-in and overrides the latter one):

 # mkdir /etc/systemd/system/failure-notification@.service.d
 # touch /etc/systemd/system/failure-notification@.service.d/toplevel-override.conf

## Notifying with e-mail
You can set up systemd to send an e-mail when a unit fails. Cron sends mail to  if the job outputs to stdout or stderr, but many jobs are setup to only output on error. First you need two files: an executable for sending the mail and a .service for starting the executable. For this example, the executable is just a shell script using , which is in packages that provide .

Whatever executable you use, it should probably take at least two arguments as this shell script does: the address to send to and the unit file to get the status of. The .service we create will pass these arguments:

Where  is the user being emailed and  is that user's email address. Although the recipient is hard-coded, the unit file to report on is passed as an instance parameter, so this one service can send email for many other units. At this point you can start  to verify that you can receive the emails.

Then simply edit the service you want emails for and add  to the  section.  passes the unit's name to the template.

## Automatically turn off an external HDD at shutdown
See udisks#Automatically turn off an external HDD at shutdown.

## Troubleshooting
## Investigating failed services
To find the systemd services which failed to start:

 $ systemctl --failed

To find out why they failed, examine their log output. See systemd/Journal#Filtering output for details.

## Diagnosing boot problems
systemd has several options for diagnosing problems with the boot process. See boot debugging for more general instructions and options to capture boot messages before systemd takes over the boot process. Also see systemd debugging documentation.

## Diagnosing a systemd-provided service
If some service provided by systemd itself misbehaves, or you want to get more information about what it is doing, set the  environment variable to .

For example, to run the systemd-networkd daemon in debug mode, edit the service temporarily using  and add the two lines:

Then, start watching the journal for the service with 's / option, and restart systemd-networkd.

## Shutdown/reboot takes terribly long
If the shutdown process takes a very long time (or seems to freeze), most likely a service not exiting is to blame. systemd waits some time for each service to exit before trying to kill it. To find out whether you are affected, see Shutdown completes eventually in the systemd documentation.

A common problem is a stalled shutdown or suspend process. To verify whether that is the case, you could run either of these commands and check the outputs

The solution to this would be to cancel these jobs by running

 # systemctl cancel
 # systemctl stop systemd-suspend.service

and then trying shutdown or reboot again.

## Short lived processes do not seem to log any output
If running  as root does not show any output for a short lived service, look at the PID instead. For example, if  fails, and  shows that it ran as PID 123, then you might be able to see output in the journal for that PID, i.e. by running  as root. Metadata fields for the journal such as  and  are collected asynchronously and rely on the  directory for the process existing. Fixing this requires fixing the kernel to provide this data via a socket connection, similar to . In short, it is a bug. Keep in mind that immediately failed services might not print anything to the journal as per design of systemd.

## Boot time increasing over time
After using  a number of users have noticed that their boot time has increased significantly in comparison with what it used to be. After using  NetworkManager is being reported as taking an unusually large amount of time to start.

The problem for some users has been due to  becoming too large. This may have other impacts on performance, such as for  or . As such the solution is to remove every file within the folder (ideally making a backup of it somewhere, at least temporarily) and then setting a journal file size limit as described in systemd/Journal#Journal size limit.

## systemd-tmpfiles-setup.service fails to start at boot
Starting with systemd 219,  specifies ACL attributes for directories under  and, therefore, requires ACL support to be enabled for the filesystem the journal resides on.

See Access Control Lists#Enable ACL for instructions on how to enable ACL on the filesystem that houses .

## Disable emergency mode on remote machine
You may want to disable emergency mode on a remote machine, for example, a virtual machine hosted at Azure or Google Cloud. It is because if emergency mode is triggered, the machine will be blocked from connecting to network.

To disable it, mask  and .

## Error "Unit xxx.service not found", but service does exist
You may be trying to start or enable a user unit as a system unit.  indicates, which units reside where. By default systemctl operates on system services.

See systemd/User for more details.

## Manually renewing LoaderDevicePartUUID after changing EFI partition UUID
Some bootloaders only set the  variable when it is empty. Consequently, even if the UUID of the EFI partition changes, the bootloader will not update . By deleting the EFI variable with the commands below, the bootloader will then repopulate it with the new UUID.

 # chattr -i /sys/firmware/efi/efivars/LoaderDevicePartUUID-4a67b082-0a4c-41cf-b6c7-440b29bb8c4f
 # rm /sys/firmware/efi/efivars/LoaderDevicePartUUID-4a67b082-0a4c-41cf-b6c7-440b29bb8c4f
