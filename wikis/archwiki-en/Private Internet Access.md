# Private Internet Access

Private Internet Access is a subscription-based VPN service.

## Manual
## NetworkManager applet approach
## Installation
Download OpenVPN configuration files from PIA. Extract the ZIP file to a place in your user home directory or elsewhere that is memorable for future access. It is worth noting that even when WireGuard can be used on the Linux binary and on the app, PIA has yet to provide WireGuard files for configuration. In other words, only OpenVPN can be used when using the NetworkManager approach.

Install and configure NetworkManager along with the NetworkManager applet and OpenVPN plugin.

## Configuration
#Right click on the NetworkManager applet from your desktop environment and click Edit Connections. Click the Plus sign in the bottom left corner of the Network Connections window that appears.
#When you choose a connection type, click the drop-down menu and scroll all the way down until you reach "Import a saved VPN configuration". Select that option. Now, click Create.
#Navigate to the directory you extracted all of the OpenVPN files to earlier, then open one of the files from that folder. Generally speaking, you will want to open the file that is associated with the connection you specifically want.
#After you have opened one of the OpenVPN files, the window that appears should be "Editing ". Type in your Username and Password that you received from Private Internet Access. There is an icon in the password box indicating user permission of the credentials; change the settings as you wish.
#Now, click Advanced. Next to "Use LZO data compression", click the drop-down menu to select "adaptive" and next to "Set virtual device type", click the menu and make sure "TUN" is selected.
#Next, go to the security tab and select as cipher "AES-128-CBC" and as HMAC Authentication "SHA-1".
#Click the OK button at the bottom left of the window to save this change.
#Go to the "IPv6 Settings" tab and select for "Method" "Ignore" since PIA blocks IPv6 addresses #Click Save at the bottom right of the "Editing " window.

## Usage
Left click on the NetworkManager applet. There is a VPN Connections menu. Inside it should be the VPN connection you saved. Click on it to connect to Private Internet Access.

When a gold lock has appeared over the NetworkManager applet, you are successfully connected to Private Internet Access. Visit [https://www.privateinternetaccess.com/ Private Internet Access and confirm that you are connected by referring to the status message at the top of their homepage.

## OpenVPN command line approach
## Installation
Download OpenVPN configurations from PIA. Unzip the file and move all files to . Ensure the files have  as the owner.

## Usage
See OpenVPN#Starting OpenVPN.

To test to see if you have successfully connected to the VPN, see this article which recommends the following four tools:
* DNS Leak
* IPv6 Leak
* Speed Test
* WebRTC

## Aur approach
## Official installation script
Private Internet Access has an installation script that sets up NetworkManager for use with the VPN. Download the script here and then run to set up.

## Official Linux client
Private Internet Access now has an official client for Linux with support for Arch. Download the client from this page, unzip the file (e.g. ) and run the installation script (.e.g. ).

## Packages
*
*
## Installation
Install .

The package provides a tool that downloads the OpenVPN configuration files and stores them in . However, it updates the file names to better support using them on the command line.

Configuration for the package is stored in .

## After installation
If there are any issues with connectivity and you are running , please restart .

## Usage
## Enabling auto-login
Enabling auto-login allows a user to connect to the VPN service without having to type any passwords on the command line (needed when using ). To set this up, you must do the following:

*Create
*Add your username and password in the file. Make sure LINE 1 is your username and LINE 2 is your password. Do not add any other text to the file or it will not work (this is a limitation of OpenVPN):

*Change permissions of the file to 0600 and owner to root:root:
  This secures the access to the file from non-root users. Read more on File permissions and attributes. It is required when activating auto-login.
*Run  as root.
**If you have  installed, it will create the configuration files for . Make sure to restart  to see them.
**If you have  installed, it will create the configuration files for . Start  if not running already. It will auto load the profiles.
**Regardless, it will create the OpenVPN  files in .

## Manually connecting to VPN
{{bc|# openvpn --config /etc/openvpn/client/{config_file_name}}} {{ic|{config_file_name}}} will be listed in the /etc/openvpn directory or run .

## Automatically connecting to VPN
## For connman
*enable the .
*Run  as root (if you have not already)

* Get a list of all connman services and find the name of the VPN config  in the second column

* Connect to your VPN chosen VPN config to create a connman settings file for it:

* Edit the relevant settings file, e.g
* Change the  line to , save, exit, reboot

## For  you can look here: OpenVPN#systemd service configuration.
## Advanced options
*Create
*For the  section:
{| class="wikitable"
! scope="col" style="width:5%;"  | option
! scope="col" style="width:10%;" | option values
! scope="col" style="width:10%;" | description
|-
|openvpn_auto_login
|True,False
|Default: True; Configures if OpenVPN configuration files should have auto-login enabled. See #Enabling auto-login
|}

*For the  section:

{| class="wikitable"
! scope="col" style="width:5%;"  | option
! scope="col" style="width:10%;" | option values
! scope="col" style="width:10%;" | description
|-
|apps
|cm, nm
|Default: all; This configures which applications are configured. The application will configure all applications installed; however, if a user only needed configurations for Conman, then setting this to 'cm' would generate only those configurations even if they had NetworkManager installed. OpenVPN configurations are always generated. cm = Conman; nm = NetworkManager
|-
|port
|See for list: PIA's Support - Which encryption/auth settings should I use for ports on your gateways?
|Default: 1198
|}

## Example configuration
The configuration enables auto-login, configures only Connman and OpenVPN, uses port 8080 over UDP, and configures only US East, US West, Japan, UK London, and UK Southampton VPN endpoints. OpenVPN is always configured.

## Troubleshooting
## Using NetworkManager's applet
In order to use the  to connect:

# Right click the NetworkManager icon in the system tray
# and click Configure Network Connections...
# then click Add
# choose Import VPN...
# browse to  or whichever configuration you would like to use
# then click Open
# Remove only the  from the  (if present) as only the domain name should be in this box
# for the  type in your  username
# for the  type in the password that goes with your  username
# then click Advanced...
# set  and set it to
# click on the Security tab
# set the  to
# set the  to
# click OK
# click OK again

## DNS Leaks
Concerning DNS Leaks (see python-pia/#13), NetworkManager leaks information due to how  is setup. The script below was posted by @maximbaz to work around the problem. You may need to disable IPv6 if you continue to get leaks.

## vopono
vopono is a tool to run specific applications via a VPN connection with temporary network namespaces. Automatic configuration generation is supported for PrivateInternetAccess.

It includes kill switch support by default, and support for forwarding and proxying ports from the network namespace to the host so you can run daemons and servers via the VPN whilst the rest of the system is unaffected.
## Tips and tricks
## Internet "kill switch"
The following iptables rules only allow network traffic through the  interface, with the exception that traffic is allowed to PIA's DNS servers and to port 1197, which is used in establishing the VPN connection:

This ensures that if you are disconnected from the VPN unknowingly, no network traffic is allowed in or out.

If you wish to additionally access devices on your LAN, you will need to explicitly allow them. For example, to allow access to devices on , add the following two rules (before any REJECT rule):

 -A INPUT -s 192.168.0.0/24 -j ACCEPT
 -A OUTPUT -d 192.168.0.0/24 -j ACCEPT

Additionally, the above rules block the ICMP protocol, which is probably not desired. See this thread for potential pitfalls of using these iptables rules as well as more details.

## Setting PIA DNS
If you find that Network Manager is controlling your host's DNS settings, and therefore your host cannot resolve any address, you will have to manually set the DNS server and attributes.
You should note a symbolic link when running the following command:

 $ ls -l /etc/resolv.conf

Remove the symbolic link with
Then create a new  and add the following:

Next regenerate resolvconf by typing:

 # resolvconf -u

Finally make the file immutable so no other application can modify it:

 chattr +i /etc/resolv.conf

## Troubleshooting
## I cannot connect to OpenVPN using PIA manager, or OpenVPN does not work
PIA manager still uses OpenVPN under the hood, so even if you do not directly use one of the OpenVPN methods, you still need it. Firstly, check that it is installed. If you used one of the installation scripts, this should be done for you.

If you are getting errors like , that probably means TAP/TUN is not currently running. Either your kernel does not have it, in which case install a kernel which does (or compile a fresh one), or it is not currently running, in which case it needs to be started:

 # modprobe tun
