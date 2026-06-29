# Deluge

Deluge is a full-featured BitTorrent application written in Python 3. It has a variety of features, including but not limited to: a client/server model, DHT support, magnet links, a plugin system, UPnP support, full-stream encryption, proxy support, and three different client applications. When the server daemon is running, users can connect to it via a console client, a GTK-based GUI, or a Web-based UI. A full list of features can be viewed here.

## Installation
Install  and optionally install . Be sure to read and install the optional dependencies for the gtk client  to enable desktop notifications and appindicator notifications.

## Daemon
Deluge works with a client/server model. The server is referred to as the daemon and runs in the background, waiting for a client (console, gtk, or web-based) to connect.  The client can disconnect, but the daemon continues to run, transferring the torrent files in the queue.

Upon installation, pacman will create a non-privileged deluge user.  This user is meant to run the provided daemon, . Users are able to start the daemon several ways:
# systemd system service (runs as the deluge user).
# systemd user service (runs as another user).
# Running it directly (runs as another user).

## System service
Start/enable .

## User service
A user service will allow  to run when  is started. This is accomplished by creating a user service file:

The deluge user service can now be started and enabled by the user.

The  user service can also be placed in . See systemd/User for more information on user services.

## Configuration
Deluge can be configured through any of the clients as well as by simply editing the JSON-formatted configuration files located in . $HOME refers to the home directory of the user that  is running as. This means that if the daemon is running as the deluge user, the default home directory is .

## Shared directories for downloads/uploads
When using the systemd deluged.service, the shared directory/directories need to be shared so that other users on the system are able to access the data.  The general strategy is to:

# Change the owner and group of the shared directory to deluge:deluge.
# Set the File permissions and attributes on the shared directory to at least 770.
# Add your user (or the user/users needing to access the files) to the deluge group.

Example using :
 # chown -R deluge:deluge /mnt/torrent_data
 # chmod 770 /mnt/torrent_data
 # usermod -a -G deluge YOURUSER

## Firewall
Deluge requires at least one port open for TCP and UDP to allow incoming connections for seeding. If deluge complains that it cannot open a port for incoming connections, users must open port(s) to be used. In this example, ports 56881 through 56889 are opened for TCP and UDP:
 # iptables -A INPUT -p tcp --dport 56881:56889 -j ACCEPT
 # iptables -A INPUT -p udp --dport 56881:56889 -j ACCEPT
Users who are behind a NAT router/firewall must setup the corresponding ports to be forwarded. UPnP may also be used, but that will not work with the local firewall on the system because it requires predefined ports.

On many default configurations, when using iptables with connection tracking (conntrack) set to drop "INVALID" packets, sometimes a great deal of legitimate torrent traffic (especially DHT traffic) is dropped as "invalid." This is typically caused by either conntrack's memory restrictions, or from long periods between packets among peers (see and [https://www.linuxquestions.org/questions/showthread.php?p=5145026). Symptoms of this problem include torrents not seeding, especially when the torrent client has been active for more than a day or two continuously, and consistently low overhead traffic (in one experience, less than 3KiB/s in either in or out) with DHT enabled, even when deluge/libtorrent has been continuously running for more than forty-eight hours and many torrents are active. For this reason, it may be necessary to disable connection tracking of all torrent traffic for optimal performance, even with the listening ports set to ACCEPT (as the causes for dropping INVALID packets, for instance conntrack's memory problems, may supercede any rules to accept traffic to/from those ports).

To fully turn off connection tracking for torrents, specify ports for both Incoming and Outgoing traffic in Deluge, for instance, 56881-56889 for incoming connections and 56890-57200 for outgoing connections.

Then issue the following commands (after substituting the relevant port ranges):
 # iptables -t raw -I PREROUTING -p udp --dport 56881:57200 -j NOTRACK
 # iptables -t raw -I OUTPUT -p udp --sport 56881:57200 -j NOTRACK
 # iptables -t raw -I PREROUTING -p tcp --dport 56881:57200 -j NOTRACK
 # iptables -t raw -I OUTPUT -p tcp --sport 56881:57200 -j NOTRACK
 # iptables -I INPUT -p icmp --icmp-type 3 -j ACCEPT
 # iptables -I INPUT -p icmp --icmp-type 4 -j ACCEPT
 # iptables -I INPUT -p icmp --icmp-type 11 -j ACCEPT
 # iptables -I INPUT -p icmp --icmp-type 12 -j ACCEPT
The ICMP allowances are desirable because once connection tracking is disabled on those ports, those important ICMP messages (types 3 (Destination Unreachable), 4 (Source Quench), 11 (Time Exceeded) and 12 (Parameter Problem)) would otherwise be declared INVALID themselves (as netfilter would not know of any connections that they are associated with), and they would potentially be blocked.

## Plugins
A complete list of plugins can be found on the Deluge Wiki

ltConfig is a useful plugin that allows direct modification to libtorrent settings and has preset support.

It offers additional settings like  (IP to announce to trackers),  (Remove maximum half-open connections limit) and more possible privacy and (seed) speedboost features.

## Clients
## Console
The console client can be run with:
 $ deluge-console
Enter the  command for a list of available commands.

## GTK
The GTK client can be run with:
 $ deluge-gtk
or:
 $ deluge

The GTK client has a number of useful plugins:
* AutoAdd - Monitors directories for .torrent files
* Blocklist - Downloads and imports an IP blocklist
* Execute - Event-based command execution
* Extractor - Extracts archived files upon completion ''(beware of random high disk I/O usage)''
* Label - Allows labels to be assigned to torrents, as well as state, tracker, and keyword filters
* Notifications - Provides notifications (email, pop-up, blink, sound) for events as well as other plugins
* Scheduler - Limits active torrents and their speed on a per-hour, per-day basis
* WebUi - Allows the Web UI to be started via the GTK client

## Web
Just as with deluge daemon mentioned above, the web client can be started several different ways:

# systemd system service (runs as the deluge user).
# systemd user service (runs as another user).
# Running it directly (runs as another user).

Once running, users may connect to the web client by browsing to http://127.0.0.1:8112, if using encryption on https://127.0.0.1:8112 and/or by the host IP-address.

## System service
Deluge ships with , a systemd system unit, which is used to start the Deluge Web UI. The Deluge Web UI uses a Connection Manager, allowing managing of multiple Deluge clients running under the same host or on an entirely different one. Remember to start and optionally enable the  service to allow the Web UI connect to the host Deluge client.

## User service
A user service will allow  to run when  is started. This is accomplished by creating a user service file:

The deluge user service can now be started and enabled by the user.

The  user service can also be placed in . See systemd/User for more information on user services.

## Headless setup
Deluge is quite useful on a headless system, often referred to as a seed box, because of its client/server model. To set up deluge on a headless system, set up the daemon as shown above.

## Create a user
To allow interaction with the server remotely, create a user in . For example:
 $ echo "delugeuser:p422WoRd:10" >> $HOME/.config/deluge/auth

The number 10 corresponds to a level of Admin.  Refer to the following table for additional values:

{| class="wikitable" align="center"
|-
! Level Name !! Level Value
|-
| None || 0
|-
|Read-Only || 1
|-
| Normal || 5
|-
| Admin || 10
|}

## Allow remote
The default settings disallow remote connections. Change the "allow_remote" setting in :
 "allow_remote": true

## Firewall
Open the port for remote access. The following example uses the default daemon port (58846):
 # iptables -A INPUT -p tcp --dport 58846 -j ACCEPT
See iptables for more information on firewall rules.

Users behind a NAT router/firewall must forward the port to access the daemon from outside the network if this behavior is desired.

## Connect
In the console client:
 connect In the GTK client, Edit > Connection Manager > Add.

In the Web client, Connection Manager > Add.

## SSH Tunnel
An SSH tunnel can be created to use an encrypted connection on any client. This requires an extra loopback address to be added, but this can be automated at boot. Without this step, the connection would be considered local. The actual command to establish an SSH tunnel cannot be automated as it requires user input. There are a few possible ways to go about doing that.

 $ ssh -fNL 127.0.0.2:58846:localhost:58846
The port 58846 should be replaced with the port the deluge server is running on and ' should be replaced with the server hosting both deluge and the SSH server.

## Troubleshooting
## No module named service_identity
Upon running  or , one may receive a message like the following:

 :0: UserWarning: You do not have a working installation of the service_identity module: 'No module named service_identity'.
 Please install it from  and make sure all of its dependencies are satisfied.
 Without the service_identity module and a recent enough pyOpenSSL to support it, Twisted can perform only rudimentary TLS
 client hostname verification.  Many valid certificate/hostname mappings may be rejected.

, an optional dependency to , is likely missing. See .

## Web ui .torrent upload does not work
Users running the web ui behind a reverse proxy need to allow embedding for .torrent upload to work (X-Frame-Options ALLOW)

## Execute script not found or not executable
When using the [https://dev.deluge-torrent.org/wiki/Plugins/Execute Execute plugin, the following error message is logged when deluge tries to execute the script:

 :145  Execute script not found or not executable

If  is running as a system service, note that it likely will not be able to access the home directory of other users. Consider putting custom scripts in .

Script permission issues can be debugged as the  user:

 /path/to/script

## Torrents list has completely disappeared after an unexpected shutdown
This usually means the state file has gotten corrupted. It [https://forum.deluge-torrent.org/viewtopic.php?t=55087 has been an intermittent issue since last decade. There should be one backup state file along with a copy of all the previously-running torrents in your deluge profile folder (for systemd users this is usually ) that can be restored to remedy this issue. However, it can get overwritten pretty quickly, especially if you only notice your torrents list after several reboots. A suggested course of action to keep it from happening again is to automate a daily backup of the state file and the torrents.

## Console is unusable
If you run Deluge using the  user, you should access  via the  user, or else you can run into various Python exceptions and bugs.

 deluge-console

or

 # deluge-console -c /srv/deluge/.config/deluge
