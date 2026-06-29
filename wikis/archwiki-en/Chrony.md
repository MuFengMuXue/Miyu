# Chrony

This article describes how to set up and run chrony, an alternative NTP client and server that is roaming friendly and designed specifically for systems that are not online all the time.

## Installation
Install the  package.

## Configuration
The smallest useful configuration file (using IP addresses instead of a hostname) would look something like:

Refer to , which will point you to the right answer to any doubts you could still have. Documentation is also available online. See also the related man pages: , , .

## NTP Servers
The first thing you define in your  is the servers your machine will synchronize to.
NTP servers are classified in a hierarchical system with many levels called strata: the devices which are considered independent time sources are classified as stratum 0 sources; the servers directly connected to stratum 0 devices are classified as stratum 1 sources; servers connected to stratum 1 sources are then classified as stratum 2 sources and so on.

It has to be understood that a server's stratum cannot be taken as an indication of its accuracy or reliability. Typically, stratum 2 servers are used for general synchronization purposes: if you do not already know the servers you are going to connect to, you should use the pool.ntp.org servers (alternate link) and choose the server pool that is closest to your location.

The following lines tells chrony to pick 4 sources from the NTP pool (chrony has special handling of pools, so as to not confuse its tracking of server-side drift), and use a burst behavior on startup:

 pool 2.arch.pool.ntp.org iburst maxsources 4

## Offline computers
If your computer is not connected to the internet on startup, it is recommended to use the offline option, to tell Chrony not to try and connect to the servers, until it has been given the go:

 pool 2.arch.pool.ntp.org iburst maxsources 4 offline

It may also be a good idea to either use IP addresses instead of host names, or to map the hostnames to IP addresses in your  file, as DNS resolving will not be available until you have made a connection.

## Using NTS servers
Since version 4.0 chrony supports [https://www.networktimesecurity.org/ Network Time Security (NTS), a cryptographically secured variety of NTP. To use it, add an NTS-secured server, and specify  at the end, like so:

 server time.cloudflare.com iburst nts

You can find a list of all known NTS-supporting servers here.

## Real-Time Clock
During boot the initial time is read from the hardware real-time clock (RTC) and the system time is then set, and synchronised over a period of minutes once the chrony daemon has been running for a while. If the hardware clock is out of sync then the initial system time can be some minutes away from the true time. Chrony.conf has three different mechanisms for handling the RTC:

* The first mechanism is , which simply writes the current time to the RTC periodically. This is the classical method used by ntpd, but turns off RTC drift tracking: this is bad for intermittently running desktops, which does a lot of time-keeping on the RTC.
* The second mechanism is , which overwrites the RTC time only if it goes above a difference threshold. This method can be used with , which allows for keeping track of RTC error.
* The final mechanism is to do nothing about the RTC, but record its error and drift in . The RTC time will stay wrong, but the system time will become correct as chrony has an idea of how wrong it is. The  command in chronyc can still sync the RTC as needed:

In addition,  describes whether RTC runs on UTC.

## Example: intermittently running desktops
An intermittently running desktop would require the use of  to keep track of RTC error. A machine running Arch Linux for five years, accumulated a 300 s error within the RTC.  After a reboot it took chrony a long time to adjust this difference using the above configuration. If we go for the below instead:

This keeps, interestingly, the RTC still out-of-date, but after each re-start, chrony adjusts the accumulated error of the RTC and the system time is quite synchronous to NTP even shortly after a start.

RTC remains out-of-date because we forgot to add the  line telling chrony to adjust the RTC. If we do add it, both the RTC and the system time will become correct.

## Other interesting options
Usefulness:
* : allow chrony to change the time by abrupt sets instead of frequency adjustments. Doing so may surprise running programs, but helps to fix large errors.  may be desirable for computers that are often offline: only the first three changes will be stepped, so surprises are limited to computer startup.

Precision:
*  and :  and  may help increase accuracy without any compatibility cost.
* : some network interface cards can timestamp its packages to account for delays in the network stack. Use  to turn it on: this will not do anything on adapters without such support.
* : keep track of the relationship between software clock errors (usually due to motherboard crystal temperature changes) and a temperature sensor. For those desiring ultimate precision.

## Usage
## Starting chronyd
The package provides  and , see systemd for details.

## Telling chronyd an internet connection has been made
If you are connected to the internet, run:

You may also be interested in the  option to display status:

Chrony should now connect to the configured time servers and update your clock if needed. To tell chrony that you are not connected to the Internet anymore, execute the following:

The online/offline status can be automatically handled by dispatcher services for  and , see below.

## Checking configured NTP servers
To check which NTP servers chrony is actually using, and how precise they are, you can use :
 $ chronyc sources -a -v

   .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
  / .- Source state '*' = current best, '+' = combined, '-' = not combined,
 | /             'x' = may be in error, '~' = too variable, '?' = unusable.
 ||                                                 .- xxxx [ yyyy ] +/- zzzz
 ||      Reachability register (octal) -.           |  xxxx = adjusted offset,
 ||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
 ||                                \     |          |  zzzz = estimated error.
 ||                                 |    |           \
 MS Name/IP address         Stratum Poll Reach LastRx Last sample
 ===============================================================================
 ^+ ptbnts1.ptb.de                1   6   377    50    -38us[  -13us] +/- 8723us
 ^* ptbnts2.ptb.de                1   6   377    49  +2061ns[  +27us] +/- 7538us
 ^+ nts.ntp.se                    2   6   377    51   +594us[ +619us] +/-   15ms
 ^+ nts.sth1.ntp.se               2   6   377    51   +655us[ +680us] +/-   15ms
 ^+ nts.sth2.ntp.se               2   6   377    53   +991us+/-   15ms
 ^+ time.cloudflare.com           3   6   377    49  -1250us[-1250us +/-   10ms

## Notifying network state
If you have specified your pools as offline in , you need to tell chrony that the network status has changed.

You can either use chronyc to notify chrony that your network configuration has changed, or you can use a dispatcher for your relevant network configuration manager.

## NetworkManager
chronyd can go into online/offline mode along with a network connection through the use of NetworkManager's dispatcher scripts. Create some dispatcher using the shipped upstream NetworkManager dispatcher:
 cp /usr/share/doc/chrony/examples/chrony.nm-dispatcher.onoffline /etc/NetworkManager/dispatcher.d/20-chrony-onoffline.sh
 chmod 700 /etc/NetworkManager/dispatcher.d/20-chrony-onoffline.sh

You can alternatively install  from the AUR.

## netctl
Install  from the AUR. This adds a hook to netctl which is run automatically for any connection.

## dhcpcd
Create the following hook:

See
