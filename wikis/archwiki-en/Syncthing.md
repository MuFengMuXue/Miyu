# Syncthing

Syncthing is an open-source file synchronization client/server application written in Go, which implements its own - equally free - Block Exchange Protocol. All transit communications between syncthing nodes are encrypted using TLS and all nodes are uniquely identified with cryptographic certificates.

## Installation
Install the  package.

Syncthing provides a #Web-GUI for control and monitoring. GUI wrappers like #Syncthing-GTK and #Syncthing Tray (provided in separate packages) also exist.

## Running Syncthing
## Starting Syncthing
Run the  binary manually from a terminal. The multiple optional parameters are described in .

## Autostarting Syncthing
Syncthing can either be installed as a systemd system-wide service or as a systemd user service to run automatically at startup.

## System service
Running Syncthing as a system service ensures that it is running at startup even if the user has no active session, it is intended to be used on a server.
Enable and start the  where myusername is the actual name of the Syncthing user.

## User service: on login
Running Syncthing as a systemd user service ensures that Syncthing only starts after the user has logged into the system (e.g., via the graphical login screen, or ssh). This method is intended to be used on a (multiuser) computer. To run the user service, start/enable the user unit  (i.e. with the  flag).

## User service: on boot
The systemd-user service can be started at boot time (i.e. without logging in) using systemd/User#Automatic start-up of systemd user instances.

## User service: on mount
The Syncthing systemd user service can be started after a specific (optionally encrypted) device has been mounted, and stopped when the device has been unmounted. To create a user service dependent on a mount point, after the device has been mounted, find the systemd mount name by running . Then create a new service similar to the one below:

## Syncthing-GTK
 provides a GTK graphical user interface, desktop notifications and integration with the file managers Nautilus, Nemo and Caja.
Syncthing can be launched by Syncthing-GTK: use the interface settings to run syncthing-gtk at startup, and to state whether to launch the syncthing daemon.

## Web-GUI
Syncthing provides a web interface accessible by default on http://localhost:8384.

## Syncthing Tray
 complements the Web-GUI by providing a Qt-based system tray icon and desktop notifications. There exists a desktop environment neutral version and a Plasmoid for Plasma. It also provides integration with systemd and the Dolphin file manager.

For further remarks, see the pinned comments on the AUR. When you are unsure about configuration it is also advisable to read upstream's README.

The packages also comes with the syncthingctl utility which allows to interact with Syncthing from the command line.

## Configuration
After installation, Syncthing already has a proper start-up configuration although no default sync folder is created. New servers and/or folders can be added by visiting the web interface. For detailed instructions on how to setup a simple network, read Syncthing's getting started.

To add a folder to share, click Add Folder on the left of web interface. On the left is the list of repositories, which are folders you can choose to share with other nodes. On the right is the list of nodes you have added.

To add another node, click Add Node underneath the list of nodes. You will be prompted for their Node ID (which can be found on the other machine by clicking Edit > Show ID) as well as a short name and the address.
If you specify "dynamic" for the address, the syncthing announce server will be used to automatically exchange addresses between nodes. If you want to know more about Node IDs, including the cryptographic implications, you can read the appropriate Syncthing documentation page.

After saving the configuration, the syncthing server restarts automatically. Next, you can either change the configuration of the default node (click its name and then Edit), or create a new one to share data with. Simply tick the node you wish to share the data with, and they will have permission to access it.

## Local network setup
In the typical case several machines share a LAN (Local Area Network) behind a NAT (Network Address Translation) router, it is advised for a versatile configuration to:

* Activate both local and global discovery on each node. This will allow discovery in all situations, including if some of the nodes are mobile devices like laptops or Android phones, and leave the LAN and connect to the internet from the outside. This way they will still be found with global discovery.

* Use a different listen address port for each machine, like , ,  and so forth. This will differentiate the nodes on the global discovery servers and avoid the "Connected to myself - should not happen" message on the other local devices whenever they leave the LAN.

* If running multiple instances for different users on the same machine, set a different port for each user's localAnnouncePort (IPv4 broadcasts) as to avoid Syncthing complaints and choose the same localAnnounceMCAddr (IPv6 multicasts) as to find other devices on the LAN without global discovery (see Options Element).

* If two instances on the same machine should find each other without global discovery, add  as device's second address, e.g.,  and  (see Device Element).

* Enable if possible UPnP port forwarding or manually forward each port to the right machine on the LAN. When a new node is discovered, Syncthing tries to use its configured listening port, 22000 by default. If this port happens to be closed, it will seek another port locally: whenever NAT traversal is enabled in Syncthing, it will attempt to use UPnP to map a random external port to the internal listening port chosen, for example 22000. If UPnP is not supported or if this is not desirable, each port should be manually forwarded to the right machine on the LAN. Eventually, if no open port can be found on both sides, relaying will be used.

## Using inotify
inotify (inode notify) is a Linux kernel subsystem that acts to extend filesystems to notice changes to the filesystem, and report those changes to applications. Syncthing supports inotify and the functionality can be enabled in the configuration menu for individual folders.

## Participate in the infrastructure
One can participate in the Syncthing infrastructure by running a global discovery server or a relay server.

## Running a relay
Syncthing has the ability to connect two devices via a relay when it is not possible to establish a direct connection between them. Relayed connections are end-to-end encrypted in the usual manner, so the relay has no insight into the connection other than the knowledge of the IP addresses and device IDs.

Anyone can run a relay server and it will automatically join the Syncthing relay pool and be available to all Syncthing's users. To run your own relay, install  and Start/Enable . Rate limiting and other options can be configured via the command line. These options can be set in the  directive of the service drop-in file as follows:

## Running a discovery server
Global discovery is used by Syncthing to find peers on the internet.
Any device announces itself at startup to the discovery server which stores the device ID, IP address, port and current time.
Then on request, for a given device ID, it returns the information stored in JSON format, for instance.

As an example, the request  returns {{ic|{"seen":"2020-02-29T14:56:08.34589801Z","addresses":}}.

A list of public of [https://docs.syncthing.net/dev/infrastructure.html#global-discovery-servers global discovery server is provided. In addition, anyone can run a discovery server, to run your own, install the  package.

The default unit file provided by the package stores data at  and appears to work fine if you don't need to customize any flags; see list.

An example replacement unit file follows, which stores data at  instead of . The user/group  needs permissions to be able to read the certificate files. You need to edit the systemd unit file to correctly point to the certificates and to undertake any other configuration change you may want.

To point the client to your discovery server, change the  variable under Settings to  (default port) or whatever port you have reconfigured to. The variable takes a comma-separated list of discovery servers. It is possible to include multiple ones, including the default one.

If you are using self-signed certificates, the client refuses to connect unless you append the discovery server ID to its domain. The ID is printed to stdout upon launching the discovery server. Amend the Global Discovery Servers entry to add the ID: .

## Tips and tricks
## Stop journal spam
Syncthing can be quite noisy even while it is not doing anything. The service ExecStart can be overridden to choose a different log level than INFO. Valid levels are DEBUG, INFO, WARN, and ERROR.

## Run in VirtualBox
It is possible to have Syncthing connect both locally and globally within a VirtualBox virtual machine (VM) while keeping its network adapter in the standard NAT mode (as opposed to bridged networking attached to the host computer's adapter).

To enable this mode, Syncthing should listen to a port in the VM different from the listening port already used by the host.
For example, if the default 22000 port is used by the host, one could use 22001 in the VM.
The listening port in the VM can be changed through Syncthing's Sync Protocol Listen Addresses to  in the GUI Settings.

The 22001/TCP port of the host must be forwarded to the guest in this configuration. This can be done with the following command:
 $ VBoxManage modifyvm myvmname --natpf1 "syncthing,tcp,,22001,,22001"
In this setup, relaying should not be necessary: local devices can connect to the VM on port 22001 while global devices are accessible as long as they have themselves an open port.

## Running through a proxy
Syncthing can be run through a proxy to enable use behind a corporate firewall or tunneling via SSH. According to the using proxies documentation it is necessary to set the  environment variable, and it must indicate a socks5 proxy type.

* If the service is run from a script or from the command line, you must set the variables beforehand as follows:

 export all_proxy="socks5://proxy_address:proxy_port"
 export no_proxy="127.0.0.1"

* If it is run as a service, you must define the variables in the service configuration as follows:

You must then do a daemon-reload and restart the .

This file can be edited using systemd on the  according to the systemd#Editing provided units section.

## Syncthing FUSE
SyncthingFUSE is a FUSE driver which provides access to a syncthing share without actually syncing it to local storage. When you open a file, the contents are served from a local cache, if possible. If the contents are not in the cache, SyncthingFUSE asks peers for the contents and adds them to the cache.  The local cache will not grow larger than a fixed size, though. If no peers are currently available for the file, opening it will fail.

## Troubleshooting
## Database issue
Occasionally, Syncthing may be impacted by database issues. A common symptom of this is when "Out of Sync Items" is reported by the client but never resolved, even after disconnecting devices and restarting Syncthing. To force a rescan of files and resync of the database the next time Syncthing is started, use the following command:

 $ syncthing --reset-database

## Read-only file system error, even when run as root
If Syncthing complains that there is a read-only file system, although the user (e.g. root) has write permissions, check the template unit's definition:

 $ systemctl cat syncthing@.service

Within the  section, there may be a  directive set to , which makes  and  read-only for Syncthing. (See  for more information on this directive.)

To fix the error, add a  directive listing the directory that Syncthing writes backups to, for example using a drop-in file.

## Others
See Debugging Syncthing.
