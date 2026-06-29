# OpenRC

OpenRC is a service manager maintained by the Gentoo developers. OpenRC is dependency based and works with the system provided init program, normally SysVinit.

## Installation
For details on init components, see Init.

Install the  package.

From version 0.25 onward, OpenRC provides its own init at .
Optionally, you can use other inits from, e.g., . Note that when  is used, it must be paired with , and not the  or  commands from other packages, otherwise you will encounter errors.

A basic set of service files are available from the  package.
Other packages may have service files provided outside this package; a search on the AUR is recommended.

To maintain compatibility with historical init scripts, configuration files are installed to .

## Booting
For booting with OpenRC, set the  option in the kernel parameters.

To use OpenRC's built-in init, set .

Note that when using , the  file is not used.

## Configuration
The  directory, and the  file is used for configuration.

For general information on configuring OpenRC, see:

* OpenRC manuals
* Gentoo:OpenRC.

For instructions when migrating from systemd, see Init#Configuration.

## Services
OpenRC services are enabled by issuing  as root. It is recommended to at least enable the following services:
{| class="wikitable"
! Service name
! Runlevel
! Description
|-
| udev
| sysinit
| Device hot-plugging
|-
| alsa
| default
| ALSA state
|-
| acpid
| default
| ACPI events
|-
| dbus
| default
| Messaging bus
|-
| dcron
| default
| Scheduling
|-
| syslog-ng
| default
| System logs
|}

If necessary, create services for each wanted getty by creating symbolic links to . E.g. for :

 # ln -s /etc/openrc/init.d/agetty{,.tty1}
 # rc-update add agetty.tty1 default

To prevent PAM from attempting to register with systemd after logging into the tty (which can sometimes cause problems, it is safe to remove or comment out the lines mentioning systemd in .

See also Gentoo:Systemd#Native services.

## Network
The network is configured through  Modify the  file; both the  () and the  () commands are supported. Below is an example configuration using .

The network service is added to the boot runlevel by default, so no further action is required. See Network configuration for general networking information.

## Boot logs
To enable boot logging, uncomment the  line in . When enabled, boot logs are stored in .

## Hostname
OpenRC sets the hostname from . The file looks as follows:

## Kernel modules
OpenRC uses  instead of . For example:

## Locale
Keyboard layout can be configured via  and . You can also configure the settings through the  file, which is sourced via .

See Gentoo:Localization/Guide#Keyboard layout for the console and Locale for details.

## Usage
This section draws a parallel between systemd and other init systems.

You can omit the  and  extensions, especially if temporarily editing the kernel parameters.

{| class="wikitable" width="100%"
! systemd !! SysVinit !! OpenRC !! Description
|-
|  ||  ||  || List running services status
|-
|  || ||  || Check failed services
|-
|  || ||  || Display all available services.
|-
|  ||  ||  || Change service state.
|-
|  ||  ||  || Turn service on or off.
|-
|  ||  || || Create or modify configuration.
|}

## Tips and tricks
## Quiet booting
To hide boot messages from OpenRC, you can edit  and add  to every openrc command. For further information check with .

## Troubleshooting
## Error while unmounting /tmp
When shutting the system down, you might get an error message such as

This can be fixed by adding

 no_umounts="/tmp"

to

## Disabling IPv6 does not work
One option is to add:

 # Disable ipv6
 net.ipv6.conf.all.disable_ipv6 = 1

in a file with a  extension under

## During shutdown remounting root as read-only fails
If the above happens, edit the  file and put:

 telinit u

after the following line:

 # Flush all pending disk writes now
 sync; sync

## /etc/sysctl.conf not found
By default,  is called to load the sysctl configuration. [https://github.com/OpenRC/openrc/blob/master/init.d/sysctl.in#L40 This includes the  file, which was removed from Arch. To prevent a missing file error, create the file:

 # touch /etc/sysctl.conf

## opentmpfiles-setup failed to start
On booting openrc, you may see lines like these :

 * Setting up tmpfiles.d entries ...
 chattr: Operation not supported while setting flags on /var/log/journal
 chattr: No such file or directory while trying to stat /var/log/journal/%m
 chattr: Operation not supported while setting flags on /var/log/journal/remote
 [ !!
 ERROR: opentmpfiles-setup failed to start

This is caused by  using options that are only valid if journal is on a btrfs filesystem.

See https://github.com/OpenRC/opentmpfiles/issues/2 for details

A workaround is to create an empty  to override the settings.

## Reverting to systemd
Reverting to systemd should be straightforward in most cases. It is essentially the reversal of migrating to OpenRC, with care placed on the following:

* Removal of, or otherwise editing, the  parameter on the kernel command line
* Replacement of any OpenRC-tailored or no-systemd packages with their stock equivalents
