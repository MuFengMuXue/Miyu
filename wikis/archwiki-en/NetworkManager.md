# NetworkManager

NetworkManager is a program for providing detection and configuration for systems to automatically connect to networks.

NetworkManager can be useful for both wireless and wired networks. For wireless networks, NetworkManager prefers known wireless networks and has the ability to switch to the most reliable network.  NetworkManager-aware applications can switch from online and offline mode.

NetworkManager also prefers wired connections over wireless ones, has support for modem connections and certain types of VPN.

## Installation
NetworkManager can be installed with the package , which contains a daemon, a command line interface (nmcli) and a curses‐based interface (nmtui).

## Enable NetworkManager
After installation, you should start/enable . Once the NetworkManager daemon is started, it will automatically connect to any available "system connections" that have already been configured. Any "user connections" or unconfigured connections will need nmcli or an applet to configure and connect.

## Additional interfaces
*  for a graphical user interface,
*  for a system tray applet (see the #nm-applet section).

## Mobile broadband support
NetworkManager uses ModemManager for mobile broadband connection support.

Install  and . Afterwards enable and start .

It may be necessary to restart  for it to detect ModemManager. After you restart it, re-plug the modem again and it should be recognized.

Add connections from a front-end (e.g. ) and select mobile broadband as the connection type. After selecting your ISP and billing plan, APN and other settings should be filled in automatically using information from .

## PPPoE / DSL support
Install  package for PPPoE / DSL connection support. To actually add PPPoE connection, use  and add new DSL/PPPoE connection.

## VPN support
NetworkManager since version 1.16 has native support for WireGuard, all it needs is the  kernel module. Read the WireGuard in NetworkManager blog post for details.

Support for other VPN types is based on a plug-in system. They are provided in the following packages:

*  for OpenConnect
*  for OpenVPN
*  for PPTP Client
*  for strongSwan
*
*
*
*
*
*
*

## Usage
NetworkManager comes with  and .

## nmcli examples
List nearby Wi-Fi networks:

 $ nmcli device wifi list

Connect to a Wi-Fi network:

 $ nmcli device wifi connect SSID_or_BSSID password password

Connect to a hidden Wi-Fi network:

 $ nmcli device wifi connect SSID_or_BSSID password password hidden yes

Connect to a Wi-Fi on the  interface:

 $ nmcli device wifi connect SSID_or_BSSID password password ifname wlan1 profile_name

Disconnect an interface:

 $ nmcli device disconnect ifname eth0

Get a list of connections with their names, UUIDs, types and backing devices:

 $ nmcli connection show

Activate a connection (i.e. connect to a network with an existing profile):

 $ nmcli connection up name_or_uuid

Delete a connection:

 $ nmcli connection delete name_or_uuid

See a list of network devices and their state:

 $ nmcli device

Turn off Wi-Fi:

 $ nmcli radio wifi off

## Edit a connection
For a comprehensive list of settings, see .

Firstly, you need to get a list of connections:

Here you can use the first column as connection-id used later. In this example, we pick  as a connection-id.

You have three methods to configure a connection  after it has been created:

; nmcli interactive editor
: . Usage is well documented from the editor.

; nmcli command line interface
: . See  for usage. For example, you can change its IPv4 route metric to 200 using  command.
To remove a setting, pass an empty field ("") to it like this:
:

; Connection file
: In , modify the corresponding  file . Do not forget to reload the configuration file with .

## nmtui
NetworkManager ships a text user interface (TUI) for managing connections, the system hostname and radio switches. It can be launched by running .

## Front-ends
To provide integration with a desktop environment, most users will want to install an applet. This not only provides easy access to network selection and configuration, but also provides the agent necessary for securely storing secrets. Various desktop environments have their own applet; otherwise, you can use #nm-applet.

## GNOME
GNOME has a built-in tool, accessible from the Network settings.

## KDE Plasma
Install the  package. After that, add it to the KDE taskbar via the Panel options > Add widgets > Networks menu.

## nm-applet
 is a GTK 3 front-end which works under Xorg environments with a systray.

To store connection secrets install and configure an application which implements the Secret Service D-Bus API such as GNOME/Keyring, KDE Wallet, or KeePassXC.

Be aware that after enabling the tick-box option  for a connection, NetworkManager stores the password in plain-text, though the respective file is accessible only to root (or other users via ). See #Encrypted network keyphrases.

In order to run  without a systray, you can use  or . For example, you can add a script like this one in your path:

When you close the stalonetray window, it closes  too, so no extra memory is used once you are done with network settings.

The applet can show notifications for events such as connecting to or disconnecting from a Wi-Fi network. For these notifications to display, ensure that you have a notification server installed - see Desktop notifications. If you use the applet without a notification server, you might see some messages in stdout/stderr, and the applet might hang. See In order to run  with such notifications disabled, start the applet with the following command:

 $ nm-applet --no-agent

## Appindicator
As of version 1.18.0 Appindicator support is [https://gitlab.archlinux.org/archlinux/packaging/packages/network-manager-applet/-/commit/527448fb2a87d85055f504f463dfe961dccd75c3 available in the official  package. To use nm-applet in an Appindicator environment start the applet with the following command:

 $ nm-applet --indicator

## networkmanager-dmenu
Alternatively there is  which is a small script to manage NetworkManager connections with dmenu or rofi instead of . It provides all essential features such as connection to existing NetworkManager Wi-Fi or wired connections, connect to new Wi-Fi connections, requests passphrase if required, connect to existing VPN connections, enable/disable networking, launch nm-connection-editor GUI, connect to Bluetooth networks.

## switchboard
Pantheon's  offers a desktop environment-agnostic way to configure NetworkManager when combined with  and . It can be ran with the following command:

 $ io.elementary.settings

## Configuration
NetworkManager may require some additional steps to be able run properly. Make sure you have configured  as described in Network configuration#Set the hostname section.

NetworkManager has a global configuration file at . Additional configuration files can be placed in . Usually no configuration needs to be done to the global defaults.

After editing a configuration file, the changes can be applied by running:

 # nmcli general reload

## NetworkManager-wait-online
Enabling  also enables , which is a oneshot system service that waits for the network to be configured. The latter has , so it will finish only when  itself is enabled or pulled in by some other unit. See also systemd#Running services after the network is up.

By default,  waits for NetworkManager startup to complete, rather than waiting for network connectivity specifically (see ). If  finishes before the network is really up, resulting in failed services on boot, extend the unit to remove the  from the  line:

 ExecStart=
 ExecStart=/usr/bin/nm-online -q

Be aware that this can cause [https://lists.fedoraproject.org/archives/list/users@lists.fedoraproject.org/thread/EGC324JD3HJCGVN7J55WYPRLFDA3TP7N/ other issues.

In some cases, the service will still fail to start successfully on boot due to the timeout setting being too short. Edit the service to change  from  to a higher value.

## Set up PolicyKit permissions
By default, all users in active local sessions are allowed to change most network settings without a password. See General troubleshooting#Session permissions to check your session type. In most cases, everything should work out of the box.

Some actions (such as changing the system hostname) require an administrator password. In this case, you need to add yourself to the  group and run a Polkit authentication agent which will prompt for your password.

For remote sessions (e.g. headless VNC), you have several options for obtaining the necessary privileges to use NetworkManager:

# Add yourself to the  group. You will have to enter your password for every action. Note that your user account may be granted other permissions as well, such as the ability to use sudo without entering the root password.
# Add yourself to the  group and create  with the following content: {{bc|
polkit.addRule(function(action, subject) {
  if (action.id.indexOf("org.freedesktop.NetworkManager.") == 0 && subject.isInGroup("network")) {
    return polkit.Result.YES;
  }
});
}} All users in the  group will be able to add and remove networks without a password (which means you do not have to run a Polkit authentication agent, so this option will also work in SSH sessions).

## Proxy settings
NetworkManager does support some proxy settings. While they can not be directly modified using nmtui, nm-applet and nmcli support those.
See the proxy settings in .

Additionally, custom proxy commands can always be run using dispatcher scripts, see #Dispatcher examples.

See also Proxy settings.

## Checking connectivity
NetworkManager can try to reach a webserver after connecting to a network in order to determine if it is e.g behind a captive portal. The default host (configured in ) is ping.archlinux.org (a CNAME alias of redirect.archlinux.org). To use a different webserver or to disable connectivity checking, create , see . Below is an example of using GNOME servers (it does not require the use of GNOME):

To disable NetworkManager's connectivity check, use the following configuration. This can be useful when connected to a VPN that blocks connectivity checks.

## Captive portals
For those behind a captive portal, the desktop manager may automatically open a window asking for credentials. If your desktop does not, you can use  package (however, it currently has a broken NetworkManager dispatcher script). Alternatively, you can create a NetworkManager dispatcher script with the following content:

{{hc|/etc/NetworkManager/dispatcher.d/90-open_captive_portal|
#!/bin/sh -e
# Script to dispatch NetworkManager events
#
# Runs shows a login webpage on walled garden networks.
# See NetworkManager(8) for further documentation of the dispatcher events.

PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

if [ -x "/usr/bin/logger" ]; then
    logger="/usr/bin/logger -s -t captive-portal"
else
    logger=":"
fi

wait_for_process() {
    PNAME=$1
    while [ -z "$(/usr/bin/pgrep $PNAME)" ]; do
        sleep 3;
    done
}

#launch the browser, but on boot we need to wait that nm-applet starts
start_browser() {
    local user="$1"
    local display="$2"

    export DISPLAY="$display"
    wait_for_process nm-applet

    export XAUTHORITY="/home/$user/.Xauthority"

    $logger "Running browser as '$user' with display '$display' to login in captive portal"
    sudo -u "$user" --preserve-env=DISPLAY,XAUTHORITY -H xdg-open http://capnet.elementary.io 2>&1 > /dev/null
}

# Run the right scripts
case "$2" in
    connectivity-change)
    $logger -p user.debug "dispatcher script triggered on connectivity change: $CONNECTIVITY_STATE"
    if [ "$CONNECTIVITY_STATE" = "PORTAL" ]; then
        # Match last column of who's output with ' :least one digit '
        who | awk '$NF ~ /\(:{ print $1 " " substr($NF, 2, length($NF)-2) };' | \
        while read user display; do
            start_browser $user $display || $logger -p user.err "Failed for user: '$user' display: '$display'"
        done
    fi
    ;;
    *)
    # In a down phase
    exit 0
    ;;
esac
}}

Make the script executable. But that script assumes you use X and simply opens http page. It might not work for everyone.

You will need to restart  or reboot for this to start working. Once you do, the dispatcher script should open a login window once it detects you are behind a captive portal.

Simple solution is [https://github.com/Seme4eg/captive-portal-sh captive-portal-sh - shell script that obtains captive portal URL and opens it in your default browser (for Wayland users only).

Another solution is  based on Google Chrome.

## iwd support for captive portal support on legacy hardware
Some older Wi-Fi chips (e.g. Broadcom BCM4360) require the proprietary  driver, which lacks support for the OWE/Elliptic-Curve handshake that many captive-portal hotspots use before presenting a login page. By switching NetworkManager’s Wi-Fi backend to  (see #Using iwd as the Wi-Fi backend), which implements the full OWE key exchange in userspace over the existing driver, you can complete the encrypted association, obtain a DHCP lease, and trigger the portal “PORTAL” state. Once that is done, any dispatcher script or browser-launcher will reliably pop up the login page on hardware that otherwise could never fully connect.

## DHCP client
By default NetworkManager uses its internal DHCP client. The internal DHCPv4 plugin is based on the nettools' n-dhcp4 library, while the internal DHCPv6 plugin is made from code based on systemd-networkd.

To use a different DHCP client install one of the alternatives:

*  - dhcpcd
*  - dhclient

To change the DHCP client backend, set the option  with a configuration file in . E.g.:

## DNS management
NetworkManager's DNS management is described in the GNOME project's wiki page—Projects/NetworkManager/DNS.

## DNS caching and conditional forwarding
NetworkManager has a plugin to enable DNS caching and conditional forwarding (previously called "split DNS" in NetworkManager's documentation) using dnsmasq or systemd-resolved. The advantages of this setup is that DNS lookups will be cached, shortening resolve times, and DNS lookups of VPN hosts will be routed to the relevant VPN's DNS servers. This is especially useful if you are connected to more than one VPN.

## dnsmasq
Make sure  has been installed. Then set  with a configuration file in :

Now run  as root. NetworkManager will automatically start dnsmasq and add  to . The original DNS servers can be found in . You can verify dnsmasq is being used by doing the same DNS lookup twice with  and verifying the server and query times.

## Custom dnsmasq configuration
Custom configurations can be created for dnsmasq by creating configuration files in . For example, to change the size of the DNS cache (which is stored in RAM):

You can check the configuration file syntax with:

 $ dnsmasq --test --conf-file=/dev/null --conf-dir=/etc/NetworkManager/dnsmasq.d

See  for all available options.

## IPv6
Enabling  in NetworkManager may break IPv6-only DNS lookups (i.e. ) which would otherwise work. In order to resolve this, creating the following file will configure dnsmasq to also listen to the IPv6 loopback:

In addition,  also does not prioritize upstream IPv6 DNS. Unfortunately NetworkManager does not do this (Ubuntu Bug). A workaround would be to disable IPv4 DNS in the NetworkManager config, assuming one exists.

## DNSSEC
The dnsmasq instance started by NetworkManager by default will not validate DNSSEC. To enable DNSSEC validation, thus breaking DNS resolution with name servers that do not support it, create the following configuration file:

## systemd-resolved
NetworkManager can use systemd-resolved as a DNS resolver and cache. Make sure that systemd-resolved is properly configured and that  is started before using it.

systemd-resolved will be used automatically if  is a symlink to ,  or .

You can enable it explicitly by setting  with a configuration file in :

## DNS resolver with an openresolv subscriber
If openresolv has a subscriber for your local DNS resolver, set up the subscriber and configure NetworkManager to use openresolv.

Because NetworkManager advertises a single "interface" to resolvconf, it is not possible to implement conditional forwarding between two NetworkManager connections. See NetworkManager issue 153.

This can be partially mitigated if you set  in Any queries for domains that are not in search domain list will not get forwarded. They will be handled according to the local resolver's configuration, for example, forwarded to another DNS server or resolved recursively from the DNS root.

## Custom DNS servers
## Setting custom global DNS servers
To set DNS servers for all connections, specify them in  using the syntax  in a section named . For example:

## Setting custom DNS servers in a connection
## Setting custom DNS servers in a connection (GUI)
Setup will depend on the type of front-end used; the process usually involves right-clicking on the applet, editing (or creating) a profile, and then choosing DHCP type as Automatic (specify addresses). The DNS addresses will need to be entered and are usually in this form: .

## Setting custom DNS servers in a connection (nmcli / connection file)
To set up DNS Servers per connection, you change the  and  settings (and their associated  and ) in the connection settings.

If  is set to  (when you use DHCP/RA), you need to set  to .

To use DNS over TLS (requires systemd-resolved), specify the DNS servers using the syntax  and additionally set the  setting to . For example, to use Quad9:

## /etc/resolv.conf
NetworkManager's  management mode is configured with the  setting.  sets it to  as opposed to the upstream default . The setting and its values are documented in the  man page.

NetworkManager also offers hooks via so called dispatcher scripts that can be used to alter the  after network changes. See #Network services with NetworkManager dispatcher and  for more information.

## Unmanaged /etc/resolv.conf
To stop NetworkManager from touching , set  with a configuration file in :

After that  might be a broken symlink that you will need to remove. Then, just create a new  file.

## Use openresolv
To configure NetworkManager to use openresolv, set  with a configuration file in :

## Firewall
You can assign a firewalld zone based on your current connection. For example a restrictive firewall when at work, and a less restrictive one when at home.

This can also be done with NetworkManager dispatcher.

## Network services with NetworkManager dispatcher
There are quite a few network services that you will not want running until NetworkManager brings up an interface. NetworkManager has the ability to start services when you connect to a network and stop them when you disconnect (e.g. when using NFS, SMB and NTPd).

To activate the feature you need to enable and start the .

Once the service is active, scripts can be added to the  directory.

Scripts must be owned by root, otherwise the dispatcher will not execute them. For added security, set group ownership to root as well:

 # chown root:root /etc/NetworkManager/dispatcher.d/10-script.sh

Make sure the file is executable.

The scripts will be run in alphabetical order at connection time, and in reverse alphabetical order at disconnect time. To ensure what order they come up in, it is common to use numerical characters prior to the name of the script (e.g.  or  (which ensures that the portmapper is up before NFS mounts are attempted).

Scripts will receive the following arguments:

* Interface name: e.g.
* Action: up, down, vpn-up, vpn-down, ... (see  for the complete list)

## Avoiding the dispatcher timeout
If the above is working, then this section is not relevant. However, there is a general problem related to running dispatcher scripts which take longer to be executed. Initially an internal timeout of three seconds only was used. If the called script did not complete in time, it was killed. Later the timeout was extended to about 20 seconds (see the [https://bugzilla.redhat.com/show_bug.cgi?id=982734 Bugtracker for more information). If the timeout still creates the problem, a work around may be to use a drop-in file for the  to remain active after exit:

Now start and enable the modified  service.

## Dispatcher examples
## Automatically set the timezone
Create a NetworkManager dispatcher script and make it executable:

Alternatively, the tool  automatically sets the timezone based on the geolocation of the IP address. This comparison of the most popular IP geolocation apis may be helpful in deciding which API to use in production.

## Mount remote directory with sshfs
As the script is run in a very restrictive environment, you have to export  in order to connect to your SSH agent. There are different ways to accomplish this, see this message for more information. The example below works with GNOME Keyring, and will ask you for the password if not unlocked already. In case NetworkManager connects automatically on login, it is likely gnome-keyring has not yet started and the export will fail (hence the sleep). The  to match can be found with the command  or .

## Mounting of SMB shares
Some SMB shares are only available on certain networks or locations (e.g. at home). You can use the dispatcher to only mount SMB shares that are present at your current location.

The following script will check if we connected to a specific network and mount shares accordingly:

The following script will unmount all SMB shares before a software initiated disconnect from a specific network:

The following script will attempt to unmount all SMB shares following an unexpected disconnect from a specific network:

An alternative is to use the script as seen in NFS#Using a NetworkManager dispatcher:

Create a symlink inside  to catch the  events:

 # ln -s ../30-smb.sh /etc/NetworkManager/dispatcher.d/pre-down.d/30-smb.sh

## Mounting of NFS shares
See NFS#Using a NetworkManager dispatcher.

## Use dispatcher to automatically toggle wireless depending on LAN cable being plugged in
The idea is to only turn Wi-Fi on when the LAN cable is unplugged (for example when detaching from a laptop dock), and for Wi-Fi to be automatically disabled, once a LAN cable is plugged in again.

Create the following dispatcher scriptreplacing  with your ethernet interface's device name.

Remember to make the script executable. You can verify that it works by restarting , running , and checking that  (or whatever your Wi-Fi interface is called) is in . If you encounter unexpected behavior, check the journal of .

## Use dispatcher to connect to a VPN after a network connection is established
In this example we want to connect automatically to a previously defined VPN connection after connecting to a specific Wi-Fi network. First thing to do is to create the dispatcher script that defines what to do after we are connected to the network.

If you would like to attempt to automatically connect to VPN for all Wi-Fi networks, you can use the following definition of the ESSID: . Remember to set the script's permissions accordingly.

Trying to connect with the above script may still fail with  complaining about 'no valid VPN secrets', because of [https://developer.gnome.org/NetworkManager/0.9/secrets-flags.html the way VPN secrets are stored. Fortunately, there are different options to give the above script access to your VPN password.

1: One of them requires editing the VPN connection configuration file to make NetworkManager store the secrets by itself rather than inside a keyring that will be inaccessible for root: open up  and change the  and  from  to .

If that alone does not work, you may have to create a  in a safe location with the same permissions and ownership as the dispatcher script, containing the following:

The script must be changed accordingly, so that it gets the password from the file:

2: Alternatively, change the  and put the password directly in the configuration file adding the section :

  ....
  password-flags=0

  [vpn-secrets
  password=your_password

## Use dispatcher to disable IPv6 on VPN provider connections
Many commercial VPN providers support only IPv4. That means all IPv6 traffic bypasses the VPN and renders it virtually useless. To avoid this, dispatcher can be used to disable all IPv6 traffic for the time a VPN connection is up.

As an alternative, dispatcher can be used to temporarily set the IPv6 mode of the device used by the VPN connection to . This will avoid NetworkManager log spam about IPv6 being disabled. This script will not work if multiple devices or connections provide IPv6 connectivity, but could be adapted to iterate over multiple devices. Note that any change to the connection (using  or a desktop environment) will reapply the entire connection to the device and re-enable IPv6 (if it is enabled in the connection).

{{hc|/etc/NetworkManager/dispatcher.d/10-vpn-ipv6|
#!/bin/sh

case "$2" in
	vpn-up)
		nmcli device modify "${DEVICE_IFACE}" ipv6.method link-local
		;;
	vpn-down)
		nmcli device reapply "${DEVICE_IFACE}"
		;;
esac
}}

## OpenNTPD
See OpenNTPD#Using NetworkManager dispatcher.

## Dynamically set NTP servers received via DHCP with systemd-timesyncd
When roaming between different networks (e.g. a company's LAN, Wi-Fi at home, various other Wi-Fi now and then) you might want to set the NTP server(s) used by timesyncd to those provided by DHCP. However, NetworkManager itself is not capable to communicate with systemd-timesyncd to set the NTP server(s).

The dispatcher can work around it.

Create the overlay directory for your systemd-timesyncd configuration  if it does not already exist. Inside , put the following:

{{hc|/etc/NetworkManager/dispatcher.d/10-update-timesyncd|
#!/bin/sh

[ -z "$CONNECTION_UUID" ] && exit 0
INTERFACE="$1"
ACTION="$2"

case $ACTION in
up | dhcp4-change | dhcp6-change)
	# `DHCP6_DHCP6_NTP_SERVERS` with double `DHCP6` is the correct variable name as varified by `printenv` as of NetworkManager 1.56.0-1
	set -- ${DHCP6_DHCP6_NTP_SERVERS-} ${DHCP4_NTP_SERVERS-}
	servers=$*
	[ -n "$servers" ] || exit 0
	mkdir -p /etc/systemd/timesyncd.conf.d
	cat "/etc/systemd/timesyncd.conf.d/${CONNECTION_UUID}.conf"
		NTP=$servers
	THE_END
	systemctl restart systemd-timesyncd.service
	;;
down)
	rm -f "/etc/systemd/timesyncd.conf.d/${CONNECTION_UUID}.conf"
	systemctl restart systemd-timesyncd.service
	;;
esac
}}

Every time NetworkManager sets up a new network connection () or gets some update for an existing connection ( or ) and the provided connection data contains information about NTP server(s) ( and ), a connection specific overlay configuration file is written to , containing the provided NTP server(s). Whenever a connection is taken down () the connection specific overlay file is removed. After each change to the configuration of systemd-timesyncd, this service is restarted to pick up the updated configuration. The use of connection specific configuration files is intentional so that when two or more connections are managed by NetworkManager in parallel the different NTP server names in the configuration are not overwritten as , ,  and  actions might come in an arbitrary order.

## Testing
NetworkManager applets are designed to load upon login so no further configuration should be necessary for most users.  If you have already disabled your previous network settings and disconnected from your network, you can now test if NetworkManager will work. The first step is to start .

Some applets will provide you with a  file so that the NetworkManager applet can be loaded through the application menu.  If it does not, you are going to either have to discover the command to use or logout and login again to start the applet.  Once the applet is started, it will likely begin polling network connections with for auto-configuration with a DHCP server.

To start the GNOME applet in non-xdg-compliant window managers like awesome:

 nm-applet --sm-disable &

For static IP addresses, you will have to configure NetworkManager to understand them.  The process usually involves right-clicking the applet and selecting something like 'Edit Connections'.

## Tips and tricks
## Encrypted network keyphrases
By default, NetworkManager stores passwords in clear text in the connection files at . To print the stored passwords, use the following command:

 # grep -r '^psk=' /etc/NetworkManager/system-connections/

The passwords are accessible to the root user in the filesystem and to users with access to settings via the GUI (e.g. ).

It is preferable to save the passwords in encrypted form in a keyring instead of clear text. The downside to this is that the connections have to be set up for each user.

In order to read and write to the keyring, there must be a secret agent available. This can be one of:

*  with the  option
* One of the graphical interfaces from #Front-ends

If you make neither of these available, then authentication will fail with the error

On a single user machine, it is enough to set up encryption for root partition. See: Dm-crypt.

## Using GNOME Keyring
The keyring daemon has to be started and the keyring needs to be unlocked for the following to work.

Furthermore, NetworkManager needs to be configured not to store the password for all users. Using GNOME's , run  from a terminal, select a network connection, click Edit, select the Wi-Fi Security tab and click on the right icon of password and check Store the password only for this user.

## Using KDE Wallet
Using KDE's , click the applet, click on the top right Settings icon, click on a network connection, in the General configuration tab, untick All users may connect to this network. If the option is ticked, the passwords will still be stored in clear text, even if a keyring daemon is running.

If the option was selected previously and you un-tick it, you may have to use the  option first to make the password disappear from the file. Alternatively, delete the connection first and set it up again.

## Sharing internet connection over Wi-Fi
You can share your internet connection (e.g. 3G or wired) with a few clicks.  Please note that a firewall may interfere with internet sharing.

You will need a Wi-Fi card which supports AP mode, see Software access point#Wi-Fi device must support AP mode for details.

Install the  package to be able to actually share the connection. Note that NetworkManager starts its own instance of dnsmasq, independent of , as a DHCP server. See #dnsmasq for the caveats.

Create the shared connection:

* Click on applet and choose Create new wireless network.
* Follow wizard (choose WPA2 or higher, be sure to use at least 8 character long password, lower lengths will fail).
** Choose either Hotspot or Ad-hoc as Wi-Fi mode.

The connection will be saved and remain stored for the next time you need it.

## Sharing internet connection over Ethernet
Scenario: your device has internet connection over Wi-Fi and you want to share the internet connection to other devices over Ethernet.

Requirements:

* Install the  and  packages to be able to actually share the connection. Note that NetworkManager starts its own instance of dnsmasq, independent of , as a DHCP server. See #dnsmasq for the caveats.
* Your internet connected device and the other devices are connected over a suitable Ethernet cable (this usually means a cross over cable or a switch in between).
* Internet sharing is not blocked by a firewall.

Steps:

* Run  from terminal.
* Add a new Ethernet connection.
* Give it some sensible name. For example "Shared Internet"
* Go to "IPv4 Settings".
* For "Method:" select "Shared to other computers".
* Save

Now you should have a new option "Shared Internet" under the Wired connections in NetworkManager.

## Checking if networking is up inside a cron job or script
Some cron jobs require networking to be up to succeed. You may wish to avoid running these jobs when the network is down. To accomplish this, add an if test for networking that queries NetworkManager's nm-tool and checks the state of networking. The test shown here succeeds if any interface is up, and fails if they are all down. This is convenient for laptops that might be hardwired, might be on wireless, or might be off the network.

This is useful for a  script that runs fpupdate for the F-Prot virus scanner signature update, as an example. Another way it might be useful, with a little modification, is to differentiate between networks using various parts of the output from nm-tool; for example, since the active wireless network is denoted with an asterisk, you could grep for the network name and then grep for a literal asterisk.

## Connect to network with secret on boot
By default, NetworkManager will not connect to networks requiring a secret automatically on boot. This is because it locks such connections to the user who makes it by default, only connecting after they have logged in. To change this, do the following:

# Right click on the  icon in your panel and select Edit Connections and open the Wireless tab
# Select the connection you want to work with and click the Edit button
# Check the boxes “Connect Automatically” and “Available to all users”
# Additionally, ensure that under "Wi-Fi Security", "Store password for all users (not encrypted)" is selected

Log out and log back in to complete.

## OpenConnect with password in KWallet
While you may type both values at connection time,  0.9.3.2-1 and above are capable of retrieving OpenConnect username and password directly from KWallet.

Open "KDE Wallet Manager" and look up your OpenConnect VPN connection under "Network Management|Maps". Click "Show values" and
enter your credentials in key "VpnSecrets" in this form (replace username and password accordingly):

 form:main:username%SEP%username%SEP%form:main:password%SEP%password

Next time you connect, username and password should appear in the "VPN secrets" dialog box.

## Ignore specific devices
Sometimes it may be desired that NetworkManager ignores specific devices and does not try to configure addresses and routes for them. You can quickly and easily ignore devices by MAC or interface-name by using the following in :

 [keyfile
 unmanaged-devices=mac:00:22:68:1c:59:b1;mac:00:1E:65:30:D1:C4;interface-name:eth0

After editing the file, run  as root. Afterwards you should be able to configure interfaces without NetworkManager altering what you have set.

## Configuring MAC address randomization
See MAC address spoofing#NetworkManager.

## Turn off hostname sending
NetworkManager by default sends the hostname to the DHCP server.

To disable sending your hostname to the DHCP server globally, set the  and  options with a configuration file in . E.g.:

To disable sending your hostname to the DHCP server for a specific connection (or alternatively, enable it for a connection if it is disabled globally), add the following to your network connection file:

## Enable IPv6 Privacy Extensions
See IPv6#NetworkManager.

## Configure a unique DUID per connection
The DHCPv6 Unique Identifier (DUID) is a value used by the DHCPv6 client to identify itself to DHCPv6 servers. NetworkManager supports 3 types of DUID:

* DUID-UUID (RFC 6355): generated from an Universally Unique IDentifier (UUID).
* DUID-LL (RFC 3315): generated from the Link-Layer address (a.k.a. MAC address).
* DUID-LLT (RFC 3315): generated from the Link-Layer address plus a timestamp.

If the internal NetworkManager's DHCP client is in use (the default) it will identify itself with a global and permanent DUID-UUID generated from the machine-id (). This means that all connections share the same UUID, which may be a privacy breach.

Fortunately, NetworkManager is able to provide unique DUIDs per connection, derived from the connection's stable-id and a per-host unique key. You can enable that by adding the following configuration under :

The  and  values are also supported. For further information read the description for  in .

## Working with wired connections
By default, NetworkManager generates a connection profile for each wired ethernet connection it finds. At the point when generating the connection, it does not know whether there will be more Ethernet adapters available. Hence, it calls the first wired connection "Wired connection 1". You can avoid generating this connection, by configuring  (see ), or by simply deleting it. Then NetworkManager will remember not to generate a connection for this interface again.

You can also edit the connection (and persist it to disk) or delete it. NetworkManager will not re-generate a new connection. Then you can change the name to whatever you want. You can use something like  for this task.

## Using iwd as the Wi-Fi backend
To enable the experimental iwd backend, first install  and then create the following configuration file:

To use MAC randomization with iwd see MAC address spoofing#iwd.

Alternatively, you can install , a modified package configured to build NetworkManager working exclusively with iwd, with the main difference being that iwd is required and wpa_supplicant can be uninstalled after building.

## Running in a network namespace
If you would like to run NetworkManager inside a network namespace (e.g., to manage a specific device which should be used by selected applications), bring the device down before moving it to the namespace:

 $ ip link set dev MY_DEVICE down
 $ ip link set dev MY_DEVICE netns MY_NAMESPACE
 $ ip netns exec MY_NAMESPACE NetworkManager
 ...
 $ ip netns exec MY_NAMESPACE killall NetworkManager

otherwise NetworkManager will later fail to establish the connection with a  error.

## Automatically connect to VPN
NetworkManager can be set to automatically connect to a VPN when connecting to the internet, on a per network basis. The VPN connection itself can be added in GNOME's NetworkManager front-end, but to make it automatically use the VPN  must be used. Other front-ends might not have this limitation.

First, make sure to make the VPN connection available to all users. In the GNOME this is a matter of checking a box under the  tab. Under the  tab, in the password field, click the icon on the right side in the field, and set it to .

Then find the UUID of the VPN connection, and add that to  of the Internet connection:

 # UUID=$(nmcli --get-values connection.uuid connection show name-of-VPN-connection)
 # nmcli connection modify name-of-Internet-connection connection.secondaries "$UUID"

Now when NetworkManager is restarted and you connect to the Internet connection you have configured, you should automatically get connected to the VPN.

## Troubleshooting
## No prompt for password of secured Wi-Fi networks
When trying to connect to a secured Wi-Fi network, no prompt for a password is shown and no connection is established. This happens when no keyring package is installed. An easy solution is to install . If you want the passwords to be stored in encrypted form, follow GNOME Keyring to set up the gnome-keyring-daemon.

## Network management disabled
When NetworkManager shuts down but the pid (state) file is not removed, you will see a  message. If this happens, remove the file manually:

 # rm /var/lib/NetworkManager/NetworkManager.state

## Problems with internal DHCP client
If you have problems with getting an IP address using the internal DHCP client, consider using another DHCP client, see #DHCP client for instructions. This workaround might solve problems in big wireless networks like eduroam.

## DHCP problems with dhclient
If you have problems with getting an IP address via DHCP, try to add the following to your :

  interface "eth0" {
    send dhcp-client-identifier 01:aa:bb:cc:dd:ee:ff;
  }

Where  is the MAC address of this NIC. The MAC address can be found using the  command from the  package.

## 3G modem not detected
See Mobile broadband modem#NetworkManager.

## Switching off WLAN on laptops
Sometimes NetworkManager will not work when you disable your Wi-Fi adapter with a switch on your laptop and try to enable it again afterwards. This is often a problem with rfkill. To check if the driver notifies rfkill about the wireless adapter's status, use:

 $ watch -n1 rfkill list all

If one identifier stays blocked after you switch on the adapter you could try to manually unblock it with (where X is the number of the identifier provided by the above output):

 # rfkill event unblock X

## Static IP address settings revert to DHCP
Due to an unresolved bug, when changing default connections to a static IP address,  may not properly store the configuration change, and will revert to automatic DHCP.

To work around this issue you have to edit the default connection (e.g. "Auto eth0") in , change the connection name (e.g. "my eth0"), uncheck the "Available to all users" checkbox, change your static IP address settings as desired, and click Apply.  This will save a new connection with the given name.

Next, you will want to make the default connection not connect automatically.  To do so, run  (not as root). In the connection editor, edit the default connection (e.g. "Auto eth0") and uncheck "Connect automatically".  Click Apply and close the connection editor.

## Cannot edit connections as normal user
See #Set up PolicyKit permissions.

## Forget hidden wireless network
Since hidden networks are not displayed in the selection list of the Wireless view, they cannot be forgotten (removed) with the GUI. You can delete one with the following command:

 # rm /etc/NetworkManager/system-connections/SSID.nmconnection

This also works for any other connection.

## VPN not working in GNOME
When setting up OpenConnect or vpnc connections in NetworkManager while using GNOME, you will sometimes never see the dialog box pop up and the following error appears in :

 localhost NetworkManager[1361719690.10506 get_secrets_cb(): Failed to request VPN secrets #3: (6) No agents were available for this request.

This is caused by the GNOME NetworkManager Applet expecting dialog scripts to be at , when NetworkManager's packages put them in .
As a "temporary" fix (this bug has been around for a while now), make the following symlink(s):

* For OpenConnect:
* For VPNC (i.e. Cisco VPN):

This may need to be done for any other NetworkManager VPN plugins as well, but these are the two most common.

## Unable to connect to visible European wireless networks
WLAN chips are shipped with a default regulatory domain. If your access point does not operate within these limitations, you will not be able to connect to the network. Fixing this is easy:

# Install .
# Uncomment the correct country code in .
# Reboot the system, because the setting is only read on boot.

## Automatic connect to VPN on boot is not working
The problem occurs when the system (i.e. NetworkManager running as the root user) tries to establish a VPN connection, but the password is not accessible because it is stored in the GNOME Keyring of a particular user.

A solution is to keep the password to your VPN in plaintext, as described in step (2.) of #Use dispatcher to connect to a VPN after a network connection is established.

You do not need to use the dispatcher described in step (1.) to auto-connect anymore, if you use the new "auto-connect VPN" option from the  GUI.

## systemd bottleneck
Over time the log files () can become very large. This can have a big impact on boot performance when using NetworkManager, see: systemd#Boot time increasing over time.

## Regular network disconnects, latency and lost packets (Wi-Fi)
NetworkManager does a scan every 2 minutes.

Some Wi-Fi drivers have issues when scanning for base stations whilst connected/associated. Symptoms include VPN disconnects/reconnects and lost packets, web pages failing to load and then refresh fine.

Running  as root will indicate that this is taking place, messages like the following will be contained in the logs at regular intervals.

 NetworkManager[410:   (wlp3s0): roamed from BSSID 00:14:48:11:20:CF (my-wifi-name) to (none) ((none))

If roaming is not important, the periodic scanning behavior can be disabled by locking the BSSID of the access point in the Wi-Fi connection profile.

## Unable to turn on Wi-Fi with Lenovo laptop (IdeaPad, Legion, etc.)
There is an issue with the  module on some Lenovo models due to the Wi-Fi driver incorrectly reporting a soft block. The card can still be manipulated with , but managers like NetworkManager break. You can verify that this is the problem by checking the output of  after toggling your hardware switch and seeing that the soft block persists.

Unloading the  module should fix this. (warning: this may disable the laptop keyboard and touchpad also!).

## nm-applet disappears in i3wm
If you use the  for notifications you must edit the unit and add the following:

After reloading the daemons restart . Exit i3 and start it back up again and the applet should show on the tray.

## Unit dbus-org.freedesktop.resolve1.service not found
If  is not started, NetworkManager will try to start it using D-Bus and fail:

 dbus-daemon[system Activating via systemd: service name='org.freedesktop.resolve1' unit='dbus-org.freedesktop.resolve1.service' requested by ':1.23' (uid=0 pid=1012 comm="/usr/bin/NetworkManager --no-daemon ")
 dbus-daemon[system Activation via systemd failed for unit 'dbus-org.freedesktop.resolve1.service': Unit dbus-org.freedesktop.resolve1.service not found.
 dbus-daemon[system Activating via systemd: service name='org.freedesktop.resolve1' unit='dbus-org.freedesktop.resolve1.service' requested by ':1.23' (uid=0 pid=1012 comm="/usr/bin/NetworkManager --no-daemon ")

This is because NetworkManager will try to send DNS information to systemd-resolved regardless of the  setting in .This can be disabled with a configuration file in :

See .

## Secrets were required, but not provided
If you received the following error when attempting to connect to a network:

This error can have numerous causes and you should read the journal (filter it with ). For example, if NetworkManager took too long to establish connection, it will believe that the password is incorrect:

You can try deleting the connection profile and creating a new one:

 $ nmcli connection delete SSID
 $ nmcli device wifi connect SSID password password

You can also try disabling MAC address randomization:

## WPA Enterprise connection with iwd
If you try to connect to an WPA Enterprise network like 'eduroam' with NetworkManager with the iwd backend then you will get the following error from NetworkManager:

  Connection 'eduroam' is not avialable on device wlan0 because profile is not compatible with device (802.1x connections must have IWD provisioning files)

This is because NetworkManager can not configure a WPA Enterprise network. Therefore you have to configure it using an iwd configuration file  like described in iwd#WPA Enterprise.

## Failed to request VPN secrets
If you get this error:
 Failed to request VPN secrets #1: No agents were available for this request.

It is either because the password is empty or you have to set up PolicyKit permissions.

## OpenVPN connections fail with "secrets: failed to request VPN secrets" warn
The package  requires  and optionally  (Gtk3) when integrated within the GNOME-Shell. If  is required but not installed a message will be  printed to the system log:

## OpenVPN connections fail with OpenSSL "ca md too weak" error
Since  was updated to version 3, certificates generated with legacy cryptographic algorithms are rejected by default. Attempting to use  with such a setup can result in the following error in the logs:

The correct approach is to have the OpenVPN server administrator generate and re-issue more secure certificates. However, as an immediate work-around, OpenVPN requires . This may not be possible through the plugin GUI, but it is possible with nmcli. Separately, you will also need to enable the legacy provider in OpenSSL.

Firstly, obtain the name of the VPN connection with the issue, from the output of the following:

 $ nmcli connection show

Assuming the connection name is vpn.example.com, use nmcli like so:

 $ nmcli connection modify vpn.example.com +vpn.data tls-cipher=DEFAULT:@SECLEVEL=0

The change should instantly be reflected in .

As for OpenSSL, edit  as described on the [https://wiki.openssl.org/index.php/OpenSSL_3.0#Providers OpenSSL wiki.

Specifically, at the end of the  section add . Under  uncomment . Lastly, add a new section  that also contains the line . Excluding most other preexisting configuration sections, the end result will look something like:

Finally, restart the  to have the new OpenSSL configuration take effect.

## WPA Enterprise connections fail to authenticate with OpenSSL "unsupported protocol" error
Since  was updated to version 3, "SSL 3, TLS 1.0, TLS 1.1, and DTLS 1.0 only work at security level 0" by default. Attempting to authenticate to a Wi-Fi network only supporting older standards results in the following error in the logs:

The correct approach is to convince the institution's administrator to upgrade the encrypted networking tunnel protocol to TLS 1.3 and optionally drop support for deprecated security standards, including TLS 1.0/1.1, DTLS 1.0 and SSL 1-3. However, as an immediate workaround, there are multiple ways to allow TLS 1.0 and/or 1.1 by default. One way would be to manually patch or revert the breaking changes in OpenSSL (As this also lowers security for all other programs using OpenSSL level 1, it is not recommended. Instead, one can directly set the level used by wpa_supplicant, like described in [https://bbs.archlinux.org/viewtopic.php?id=286417#p2104492 BBS#286417. To only change the affected connection, it is possible to set  or  in the  section of the connection's configuration file. This may not be possible through GUIs, but it is possible with nmcli.

Firstly, obtain the name of the Wi-Fi connection with the issue, from the output of the following:

 $ nmcli connection show

Assuming the connection uses TLS 1.0 and its name is Example Wi-Fi, use nmcli like so:

 $ nmcli connection modify 'Example Wi-Fi' 802-1x.phase1-auth-flags 32

And for a TLS 1.1 connection, type "64" instead:

 $ nmcli connection modify 'Example Wi-Fi' 802-1x.phase1-auth-flags 64

The change should instantly be reflected in .

Finally, restart the  to have the new OpenSSL configuration take effect.
