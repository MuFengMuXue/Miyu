# NordVPN

NordVPN is a personal virtual private network service provider. NordVPN is based in Panama. The country has no mandatory data retention laws and does not participate in the Five Eyes or Fourteen Eyes alliances. On Linux, NordVPN operates through a command-line tool.

## Installation
The NordVPN service and CLI can be installed with the  package. Optionally install  for a GUI.

Having your user being part of the  user group is needed, as the .install file reminds you.

In order to use NordVPN, You must start the  system unit. You may also enable it to make it available on startup.

## Configuration
Here are some of the common commands to use NordVPN:

## Login/Logout
 $ nordvpn login

Logs you in to your NordVPN Account.

 $ nordvpn logout

Logs you out from your NordVPN Account.

## Enable NordLynx (WireGuard)
NordVPN has introduced NordLynx technology which is based on the WireGuard protocol. Compared to default OpenVPN technology, WireGuard provides lower latency, higher speeds and better connection stability. Due to the nature of WireGuard's user identification, NordVPN has introduced NordLynx, which implements a double-NAT protocol on top of WireGuard to supplement increased privacy as well.

Enable it with the below command:

 $ nordvpn set technology nordlynx

To see all available technologies:

 $ nordvpn set technology --help

## Connect to VPN
Connect you to VPN.

Disconnect you from VPN.

 $ nordvpn disconnect

Shows the connection status.

 $ nordvpn status

## Settings
Sets the protocol.

Enables or disables Kill Switch. This security feature blocks your device from accessing the Internet outside the secure VPN tunnel, in case connection with a VPN server is lost. If you start to notice that your connection does not work after you disconnect from VPN, this may be due to the buggy killswitch feature, so you have to disable it.

Enables or disables Threat Protection Lite (Before known as CyberSec). When enabled, the Threat Protection Lite feature will automatically block suspicious websites so that no malware or other cyber threats can infect your device. Additionally, no flashy ads will come into your sight. More information on how it works: https://nordvpn.com/features/threat-protection/

Enables or disables auto connect. When enabled, this feature will automatically try to connect to VPN on operating system startup.

Sets DNS servers.

Adds or removes option from whitelist.

Shows the current settings.

 $ nordvpn settings

## Server List
Shows the country list.

 $ nordvpn countries

Use this command to show cities of specific country.

## Alternative Method: Connecting to NordVPN using NetworkManager
## Installation
1. Install  and .

2. Choose an appropriate server using the NordVPN servers page: https://nordvpn.com/servers/
Download the corresponding OpenVPN configuration file on the NordVPN site: https://nordvpn.com/ovpn/
Save the file to a place in your user home directory or elsewhere that is memorable for future access.

## Configuration
1. Right click on the NetworkManager applet from your desktop environment, and click Edit Connections. Click the Plus sign in the bottom left corner of the Network Connections window that appears.

2. When you choose a connection type, click the drop down menu and scroll all the way down until you reach "Import a saved VPN configuration". Select that option. Now, click Create.

3. Navigate to the directory you extracted all of the OpenVPN files to earlier, then open one of the files from that folder. Generally speaking, you will want to open the file that is associated with the connection you specifically want.

4. After you have opened one of the OpenVPN files, the window that appears should be "Editing ". Type in your NordVPN Username and Password. There is an icon in the password box indicating user permission of the credentials; change the settings as you wish ("Save for all users" if you do not want to enter your password every time you connect).

## Avoid DNS leak
To prevent DNS leak you must:

1. Click on the "IPv4 settings".

2. For method, choose "Automatic (VPN) addresses only" and manually enter the NordVPN DNS adresses in "DNS servers"  "103.86.96.100, 103.86.99.100" (separated by a comma).

3. Click Save at the bottom left of the "Editing " window.

## Automatic connection to the VPN
1. Right click on the NetworkManager applet from your desktop environment, and click Edit Connections.

2. Double click on the ethernet or Wifi connection for whom you want to automatically connect to the VPN

3. On the "General" tab, click on "Automatically connect to VPN when using this connection" in every connection you want, and choosing the right configuration file.

4. Repeat the operation for the other connections you will use with the VPN.

## Disable IPv6
NordVPN is not IPv6 compatible. You may want to completely disable it.

Or you can also:

1. Right click on the NetworkManager applet from your desktop environment, and click Edit Connections.

2. Double click on the ethernet or Wifi connection for whom you want to automatically connect to the VPN

3. On the "ipv6" tab, choose "ignore" in the method box.

## Use a killswitch
The NordVPN killswitch will not work with this method, you will have to create your own using ufw or iptables.

Here is an example with UFW.

## Test your configuration
You can use these sites:

https://ipleak.net/

https://www.dnsleaktest.com/

https://ipv6leak.com/

## Troubleshooting
## No internet after connection
If the network is blocking all the VPN protocols including the proxy connections, connection attempts might fail. Try changing the protocol (e. g. to TCP), using obfuscated servers or the NordLynx protocol.

 $ nordvpn set technology openvpn
 $ nordvpn set protocol tcp
 $ nordvpn set obfuscate on

Note that the list of countries where such servers are installed is much shorter.

Alternatively, there may be a conflict with your local network's subnet, e.g.:

 $ ip route
 default via 10.1.1.1 dev enp0s31f6 proto dhcp metric 100
 10.0.0.0/8 dev enp0s31f6 proto kernel scope link src 10.1.2.86 metric 100
 10.5.0.0/16 dev nordlynx proto kernel scope link src 10.5.0.2

To deal with this, whitelist your network's subnet using, e.g.:

 $ nordvpn whitelist add subnet 10.0.0.0/8

## No internet after disconnection
After disconnecting via , there might no internet on the computer, but pinging (something like ) would still be successful. It is most likely a DNS issue: upon connection to the servers, the local DNS is being overwritten with NordVPN’s DNS to ensure a secure connection to the server. After disconnecting, the DNS is removed, which might be causing problems.
It could be due to a buggy killswitch feature, so you may disable it writing
 $ nordvpn set killswitch disabled

Restarting any running network manager might be required.

## Trouble connecting over terminal
If you are having trouble connecting over the terminal and get errors connecting you need to whitelist your subnet and open a port on NordVPN.
Open a terminal and check what subnets you have.

 $ ip route
 default via 10.1.1.1 dev enp0s31f6 proto dhcp metric 100
 10.0.0.0/8 dev enp0s31f6 proto kernel scope link src 10.1.2.86 metric 100
 10.5.0.0/16 dev nordlynx proto kernel scope link src 10.5.0.2

The second subnet (10.0.0.0/8) is the subnet that we want to whitelist in NordVPN and you can do it with the following command:

 $ nordvpn whitelist add subnet 10.0.0.0/8

If you wish to blacklist the subnet again just run the following command :

 $ nordvpn whitelist remove subnet 10.0.0.0/8

The port 22 is the port that is needed for SSH to work, you can open it with the following command :

 $ nordvpn whitelist add port 22

If you wish to blacklist the port again just run the following command :

 $ nordvpn whitelist remove port 22

See also #Setting systemd-resolved as DNS resolver.

## Random disconnect on terminal
## Resetting the killswitch
If you get randomly disconnected from NordVPN on the terminal and it will not let you reconnect, just disable and re-enable the killswitch:

 $ nordvpn set killswitch off
 $ nordvpn set killswitch on

Most of the time it will not connect with the killswitch off, the linux app for NordVPN is very buggy currently.

## Restarting the daemon
Alternatively, restarting the  can resolve the connection issue.

Due to a recent update, the `iptables` policy is no longer flushed when the daemon restarts. If restarting does not restore the connection, try flushing these tables first with:

 # iptables -F

## Setting systemd-resolved as DNS resolver
A note here is that NordVPN for Linux is apparently designed to use  and can crash when a different DNS resolver is used. You can switch to  by following these steps:

Remove .

Start/enable

Backup the existing resolv.conf:
 # mv /etc/resolv.conf /etc/resolv.conf.bak

Create a symlink to stub-resolv.conf:
 # ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf

Restart

For more information see the original source here.

## Install wireguard-tools
When using NordLynx (NordVPN's WireGuard technology), sometimes the connection still drops, even when using  as a DNS resolver. This is due to an unmentioned dependency on  which should the be installed, then  can be restarted.

## Delay following terminal commands
On desktop systems without a functioning notification system there may be a long delay after executing terminal commands such as  and similar. This may be resolved by installing and initialising a notification agent.
