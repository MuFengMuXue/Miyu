# Network Time Protocol daemon

Network Time Protocol is the most common method to synchronize the software clock of a GNU/Linux system with internet time servers. It is designed to mitigate the effects of variable network latency and can usually maintain time to within tens of milliseconds over the public Internet. The accuracy on local area networks is even better, up to one millisecond.

The NTP Project provides a reference implementation of the protocol called simply NTP. This article further describes how to set up and run the NTP daemon, both as a client and as a server.

See System time#Time synchronization for other NTP implementations.

## Installation
Install the  package. By default, ntpd works in client mode without further configuration. You can skip to #Usage if you want to use the Arch Linux default configuration file for it. For server configuration, see #NTP server mode.

## Configuration
The main daemon is ntpd, which is configured in . Refer to  for detail.

## Connection to NTP servers
NTP servers are classified in a hierarchical system with many levels called strata: the devices which are considered independent time sources are classified as stratum 0 sources; the servers directly connected to stratum 0 devices are classified as stratum 1 sources; servers connected to stratum 1 sources are then classified as stratum 2 sources and so on.

It has to be understood that a server's stratum cannot be taken as an indication of its accuracy or reliability. Typically, stratum 2 servers are used for general synchronization purposes: if you do not already know the servers you are going to connect to, you should choose a server pool close to your location from the pool.ntp.org servers (alternative link).

Since ntp version 4.2.7.p465-2, Arch Linux uses its own default vendor pool of NTP servers provided by the NTP Pool Project (see ). Modify those to suit your needs, e.g. if you want to use your country's servers with an option:

The  option is recommended, and sends a burst of packets only if it cannot obtain a connection with the first attempt. The  option always does this, even on the first attempt, and should never be used without explicit permission and may result in blacklisting.

## Leap seconds file
In order for the system to be able to provide the International Atomic Time to an application that requests it, the list of leap seconds must be loaded. The list is part of the  package and can be loaded by adding the following line to the NTP configuration file:

 leapfile /usr/share/zoneinfo/leap-seconds.list

## NTP server mode
If setting up an NTP server, check that you have orphan mode enabled, so that, in case it loses internet access, it will continue serving time to the network; enable orphan mode using the  configuration parameter (you can set up to stratum 15) so that it will never be used unless internet access is lost:

 tos orphan 15

Next, define the rules that will allow clients to connect to your service (localhost is considered a client too) using the restrict command; you should already have a line like this in your file:

 restrict default nomodify nopeer noquery

This restricts everyone from modifying anything and prevents everyone from querying the status of your time server:  prevents reconfiguring ntpd (with ntpq or ntpdc), and  is important to prevent dumping status data from ntpd (also with ntpq or ntpdc).

You can also add other options:

 restrict default kod limited nomodify notrap nopeer noquery

If you want to change any of these, see the full docs for the "restrict" option in , the detailed ntp instructions and #Usage.

Following this line, you need to tell ntpd what to allow through into your server; the following line is enough if you are not configuring an NTP server:

 restrict 127.0.0.1

If you want to force DNS resolution to the IPv6 namespace, write  before the IP address or host name ( forces IPv4 instead), for example:

 restrict -6 default kod limited nomodify notrap nopeer noquery
 restrict -6 ::1    # ::1 is the IPv6 equivalent for 127.0.0.1

Lastly, specify the drift file (which keeps track of your clock's time deviation) and optionally the log file location:

 driftfile /var/lib/ntp/ntp.drift
 logfile /var/log/ntp.log

A very basic configuration file will look like this:

## Usage
The package has a default client-mode configuration and its own user and group to drop root privileges after starting. If you start it from the console, you should always do so with the  option:

 # ntpd -u ntp:ntp

The  option is employed by the two included systemd services. These services also use the  option, which disables a threshold (so-called panic-gate). Hence, they will synchronize time even in case the ntp-server's time exceeds the threshold deviation from the system clock.

Both services are tied to the system's resolver, and will start synchronizing when an active network connection is detected.

## Start ntpd at boot
Enable the daemon with . See also #Running in a chroot.

Use ntpq to see the list of configured peers and status of synchronization:

 $ ntpq -p

The delay, offset and jitter columns should be non-zero. The servers ntpd is synchronizing with are prefixed by an asterisk. It can take several minutes before ntpd selects a server to synchronize with; try checking after 17 minutes (1024 seconds).

## Synchronize time once per boot
Alternatively, enable  to synchronize time once (option ) and non-forking (option ) per boot, instead of running the daemon in the background. This method is discouraged on servers, and in general on machines that run without rebooting for more than a few days.

If the synchronized time should be written to the hardware clock as well, configure the provided unit as described in systemd#Editing provided units before starting it:

## Tips and tricks
## Start ntpd on network connection
ntpd can be started by your network manager, so that the daemon only runs when the computer is online.

## Netctl
Append the following lines to your netctl profile:

 ExecUpPost="systemctl start ntpd.service"
 ExecDownPre="systemctl stop ntpd.service"

## NetworkManager
The ntpd daemon can be brought up/down along with a network connection through the use of NetworkManager's dispatcher scripts. The  package installs one, pre-configured to start and stop the ntpd service with a connection.

## KDE
KDE can use NTP (ntp must be installed) by right clicking the clock and selecting Adjust date/time. However, this requires the ntp daemon to be disabled before configuring KDE to use NTP. === Using ntpd with GPS ===

Most of the articles online about configuring ntpd to receive time from a GPS suggest to use the SHM (shared memory) method. However, at least since ntpd version 4.2.8, a much better method is available. It connects directly to gpsd, so  needs to be installed.

Add these lines to your :

This will work as long as you have gpsd working. It connects to gpsd via the local socket and queries the "gpsd_json" object that is returned.

To test the setup, first ensure that gpsd is working by running:

 $ cgps -s

Then wait a few minutes and run . This will show if ntpd is talking to gpsd:

## Running in a chroot
Create a new directory  if it does not exist and a file named  inside with the following content:

 [Service
 ExecStart=
 ExecStart=/usr/bin/ntpd -g -u ntp:ntp -i /var/lib/ntp

Then, edit  to change the driftfile path such that it is relative to the chroot directory, rather than to the real system root. Change:
 driftfile       /var/lib/ntp/ntp.drift

to
 driftfile       /ntp.drift

Create a suitable chroot environment so that getaddrinfo() will work by creating pertinent directories and files (as root):

 # mkdir /var/lib/ntp/etc /var/lib/ntp/lib /var/lib/ntp/proc
 # mkdir /var/lib/ntp/usr /var/lib/ntp/usr/lib
 # touch /var/lib/ntp/etc/resolv.conf /var/lib/ntp/etc/services

and by bind-mounting the aformentioned files:

 # mount -a

Finally, restart  daemon again. Once it restarted you can verify that the daemon process is chrooted by checking where {{ic|/proc/{PID}/root}} symlinks to:

 # ps -C ntpd | awk '{print $1}' | sed 1d | while read -r PID; do ls -l /proc/$PID/root; done

should now link to  instead of .

It is relatively difficult to be sure that your driftfile configuration is actually working without waiting a while, as ntpd does not read or write it very often. If you get it wrong, it will log an error; if you get it right, it will update the timestamp. If you do not see any errors about it after a full day of running, and the timestamp is updated, you should be confident of success.

## Restrict listening sockets
You can limit sockets ntpd is listening to using the interface option:
 interface | ignore | drop | ipv4 | ipv6 | wildcard | name | address/prefixlen

like
