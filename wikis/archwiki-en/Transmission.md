# Transmission

Transmission is a light-weight and cross-platform BitTorrent client.

## Installation
There are three packages providing the transmission client:

*  &ndash; The daemon, with CLI tools and a #Web interface.
*  &ndash; The graphical interface utilizing GTK 4.
*  &ndash; The graphical interface utilizing Qt 6.

There are also various third-party clients to connect to the daemon with:

*  &ndash; Curses interface for the daemon.
*  &ndash; Curses interface for the daemon.
*  &ndash; GTK 3 graphical interface for the daemon.
* ,  &ndash; Graphical interface for the daemon developed with Lazarus.
*  &ndash; A rewrite of the transgui project using Tauri.

## Configuring the GUI version
Both GUI versions, transmission-gtk and transmission-qt, can function autonomously without a formal back-end daemon.

GUI versions are configured to work out-of-the-box, but the user may wish to change some of the settings. The default path to the GUI configuration files is .

A guide to configuration options can be found on Transmission's Github.

## Transmission daemon and CLI
The commands for transmission-cli are:

; transmission-daemon: starts the daemon.
; transmission-remote: invokes the CLI for the daemon, whether local or remote, followed by the command you want the daemon to execute.
; transmission-show: returns information on a given torrent file.
; transmission-create: creates a new torrent.
; transmission-edit: add, delete, or replace a tracker's announce URL.
; transmission-cli: (deprecated in favor of transmission-remote) starts a non-daemonized local instance of transmission, for manually downloading a torrent.
; tremc: (requires ) starts the curses interface for the daemon, whether local or remote.

## Starting and stopping the daemon
Transmission's daemon can be run:

* As the user transmission, by starting/enabling . The user can be changed as explained in #Choosing a user.
* As your own user, by running under your user name:

:

Starting the daemon will create an initial configuration file. See #Configuring the daemon.

The Transmission daemon can be stopped with:

 $ transmission-remote --exit

An alternative option is:

 $ pkill -3 transmission-daemon

## Reducing journal spam
Running transmission-daemon can lead to a lot of unwanted journal entries. Output can be filtered by starting it with a small wrapper script. The following example also provides some notifications:

{{hc|transwrap.sh|
#!/bin/zsh
killall transmission-daemon 2> /dev/null
transmission-daemon --foreground --log-info 2>&1 | while read line; do
	echo $line |
		grep -v "announcer.c:\|platform.c:\|announce done (tr-dht.c:" |
		grep -v "Saved.*variant.c:" |
		while read line; do
			echo $line | grep -q "Queued for verification (verify.c:" &&
				notify-send --app-name="Transmission Started" "${line#* * }"
			echo $line | grep -q "changed from .Incomplete. to .Complete." &&
				notify-send --app-name="Transmission Complete" "${line#* * }"
			echo $line | systemd-cat --identifier="TransWrap" --priority=5
		done 2>&1 > /dev/null
	done&disown

}}

## Run only while connected to network
## Netctl
It may be desirable to run transmission only on certain networks. The following script checks that the connection is to a list of authorized networks and then proceeds to launch transmission-daemon.

{{hc|/etc/netctl/hooks/90-transmission.sh|
#!/bin/bash

# The SSIDs for which we enable this.
declare -A ssids=(
    ["network_2"=y
)

if ${ssids[$SSID} ]]; then
    case $ACTION in
        CONNECT|REESTABLISHED)
            # Need to wait, otherwise doesn't seem to bind to 9091.
            sleep 30
            systemctl start transmission
            ;;
        *)
            systemctl stop transmission
            ;;
    esac
fi

}}

## Choosing a user
Choose how you want to run :

* As a separate user,  by default (recommended for increased security).
By default, transmission creates a user and a group , with its home files at , and runs as this "user". This is a security precaution, so transmission, and its downloads, have no access to files outside of . Configuration, operation, and access to downloads needs to be done with "root" privileges (e.g. by using sudo).

* Under your own user. To set this up, override the provided service file and specify your username:

## Configuring the daemon
Create an initial configuration file by starting the daemon.

* If running Transmission under the username , the configuration file will be located at .

* If running Transmission under your own username, the configuration file will be located at .

One can customize the daemon by using a Transmission client or using the included web interface accessible via http://localhost:9091 in a supported browser.

A guide to configuration options can be found on the Transmission web site: https://github.com/transmission/transmission/blob/main/docs/Editing-Configuration-Files.md

A recommendation for those running under username  is to create a shared download directory with the correct permissions to allow access to both the  user and system users, and then to update the configuration file accordingly. For example:

 # mkdir /mnt/data/torrents
 # chown -R facade:transmission /mnt/data/torrents
 # chmod -R 775 /mnt/data/torrents

Now  will be accessible for the system user  and for the  group to which the  user belongs. Making the target directory world read/writable is highly discouraged (i.e. do not chmod the directory to 777). Instead, give individual users/groups appropriate permissions to the appropriate directories.

An alternative is to add your user to the  group () and then modify the permissions on the  and  directories to allow  access by members of the  group.

## Host whitelist
If you plan to access the Transmission daemon over the network using the server's hostname, you need to add this hostname to  in .
Otherwise, you will get a "421 Misdirected Request" error when accessing the server.

If you connect to the daemon using the server's IP-address, this is not required.

## Watch dir
If you want to Automatically add .torrent files from a folder, but you find that the  and  options set in the configuration file do not work, you can start the transmission daemon with the flag .

If you are using systemd, edit the  unit as described in systemd#Editing provided units.

## Enable IPv6
By default, the daemon only listens for IPv4 connections. To also listen for IPv6 connections, change the  option to  in .

## CLI Examples
If you want to remove all finished torrents you can use the following command with your own username and password:

 # transmission-remote -n 'username:password' -l | grep 100% | awk '{print $1}'| paste -d, -s | xargs -i transmission-remote -t {} -r

Seed a torrent which has already been downloaded:

 # transmission-remote --torrent=example.torrent -a example.torrent --verify --download-dir=/dir/to/folder --start

## Notification
Stop transmission-daemon and add these in :

    "script-torrent-added-enabled": true,
    "script-torrent-added-filename": "path/to/transmission-handler.sh",
    "script-torrent-done-enabled": true,
    "script-torrent-done-filename": "path/to/transmission-handler.sh",

{{hc|transmission-handler.sh|
#!/bin/bash

percentage=$(transmission-remote -t $TR_TORRENT_ID -l | awk -v ID="$TR_TORRENT_ID" '$0 ~ ID{print $2}')

if [ $percentage != "100%"
then
     notify-send --app-name="Transmission Started" "Transmission: started $TR_TORRENT_NAME"
else
     notify-send --app-name="Transmission Complete" "Transmission: downloaded $TR_TORRENT_NAME"
fi
}}

## Web interface
## The GUI way
Once Transmission is installed, you can easily set up the web interface. All you need to do is click the edit menu and select preferences. Click the Remote tab and enable Allow remote access.

Here, you have the opportunity to change the default listening port from 9091.

Check the Use authentication and fill in a username and password so that authentication can be used.

To increase security, you can restrict access from any IP address by enabling Only allow these IP addresses.

Now you are ready to launch the web interface by either clicking on the Open web client, which makes your default web browser open it, or manually reaching  with any supported web browser.

If you have not changed the listening port, the default one is 9091. In this case, the link is

## The CLI way
You do not need a graphical interface to set up the web interface, the daemon offers the very same options. You can reach the web interface without specifing any flags. See #Starting and stopping the daemon

Nevertheless, you can specify everything that you see in the previous section:

 is equivalent to

## Optional web UI theme
If the default user interface of the web app seems outdated and less fancy than expected, try using https://git.eigenlab.org/sbiego/transmission-web-soft-theme for a simple CSS theme.

https://github.com/ronggang/transmission-web-control also provides a full replacement that can coexist with the default UI.

## Usage as makepkg DLAGENT
Transmission can be used as magnet download agent for makepkg with the  download agent.

Magnet URIs need their prefix to be changed from  to .

## Troubleshooting
## Cannot access the daemon over the network
The daemon is started after  was initialised. However, if you enable the service  as opposed to the device-specific service, such as  for example, it may happen that Transmission is started too early and cannot bind to the network interface. Thus, the web interface is unreachable. A possible solution is to add the  line to the unit's configuration file:

## Web interface cannot be reached
Even if you use the graphical interface, you still need to install  in order for web interface to work.

## Failed to set send/receive buffer
Transmission might display either of these messages in the journal on startup:

 UDP Failed to set receive buffer: requested 4194304, got 425984
 UDP Failed to set send buffer: requested 1048576, got 425984

These can be fixed by setting  and  with sysctl.

## transmission-remote frequently times out or web interface is unresponsive
Transmission does not handle disk IO asynchronously, causing it to become unresponsive when doing heavy writes, see Consider putting transmission's download directory on faster storage, such as an ssd instead of an hdd.

## Missing tray icon for transmission-gtk
Tray icon for GTK 4 version is [https://github.com/transmission/transmission/discussions/5065 not working for now. There is an option to use the GTK 3 version .

## Missing application icon
When using Wayland, Transmission won't have an application icon. Additionally, the application will be called something generic like "com.transmissionbt.transmission_66311_8913005".

Other than using X11, there isn't much that can be done. It requires code changes to Transmission. Also see the related GitHub issue.

## 401: Unauthorized
The following error may appear when using  after setting a username and password for the web interface:

This happens because a username and password were set. After this, all commands from  must be authenticated. See: transmission-remote commands are erroring with Unauthorized user
