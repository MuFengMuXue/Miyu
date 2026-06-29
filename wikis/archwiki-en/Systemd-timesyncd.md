# Systemd-timesyncd

From the systemd mailing list:

:systemd-timesyncd is a daemon that has been added for synchronizing the system clock across the network. It implements an SNTP client. In contrast to NTP implementations such as chrony or the NTP reference server this only implements a client side, and does not bother with the full NTP complexity, focusing only on querying time from one remote server and synchronizing the local clock to it. Unless you intend to serve NTP to networked clients or want to connect to local hardware clocks this simple NTP client should be more than appropriate for most installations. The daemon runs with minimal privileges, and has been hooked up with networkd to only operate when network connectivity is available. The daemon saves the current clock to disk every time a new NTP sync has been acquired (and every 60 seconds), and uses this to possibly correct the system clock early at bootup, in order to accommodate for systems that lack an RTC such as the Raspberry Pi and embedded devices, and make sure that time monotonically progresses on these systems, even if it is not always correct. To make use of this daemon a new system user and group "systemd-timesync" needs to be created on installation of systemd.

## Configuration
When starting, systemd-timesyncd will read the configuration file from , which looks like this:

To add time servers or change the provided ones, uncomment the relevant line and list their host name or IP separated by a space. Alternatively, you can use a configuration snippet in , see .

For example, you can use any servers provided by the NTP pool project or use the default Arch ones (also provided by the NTP pool project):

To verify your configuration:

{{hc|$ timedatectl show-timesync --all|2=
LinkNTPServers=
SystemNTPServers=
FallbackNTPServers=0.arch.pool.ntp.org 1.arch.pool.ntp.org 2.arch.pool.ntp.org 3.arch.pool.ntp.org
ServerName=0.arch.pool.ntp.org
ServerAddress=103.47.76.177
RootDistanceMaxUSec=5s
PollIntervalMinUSec=32s
PollIntervalMaxUSec=34min 8s
PollIntervalUSec=1min 4s
NTPMessage={ Leap=0, Version=4, Mode=4, Stratum=2, Precision=-21, RootDelay=177.398ms, RootDispersion=142.196ms, Reference=C342F10A, OriginateTimestamp=Mon 2018-07-16 13:53:43 +08, ReceiveTimestamp=Mon 2018-07-16 13:53:43 +08, TransmitTimestamp=Mon 2018-07-16 13:53:43 +08, DestinationTimestamp=Mon 2018-07-16 13:53:43 +08, Ignored=no PacketCount=1, Jitter=0 }
Frequency=22520548
}}

Further to the daemon configuration, NTP servers may also be provided via a systemd-networkd .network file with a  option or, dynamically, via a DHCP server (when the  option is enabled in the  or  section).

The NTP server to be used will be determined using the following rules:

* Any per-interface NTP servers obtained from  configuration or via DHCP take precedence.
* The NTP servers defined in  will be appended to the per-interface list at runtime and the daemon will contact the servers in turn until one is found that responds.
* If no NTP server information is acquired after completing those steps, the NTP server host names or IP addresses defined in  will be used.

## Usage
## Enable and start
To enable and start it, simply run:

 # timedatectl set-ntp true

Alternatively (e.g. when running in chroot), start/enable .

## Check service
The synchronization process might be noticeably slow. This is expected, one should wait a while before determining there is a problem. To check the service status, use:

## Check verbose
To see verbose service information, use:

## View non default config
To see the non default configuration options set and files from which those options are being derived, use:

## View log
To view the last 24 hours of logged events, use:
