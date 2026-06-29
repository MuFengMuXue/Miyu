# Iwd

iwd (iNet wireless daemon) is a wireless daemon for Linux written by Intel. The core goal of the project is to optimize resource utilization by not depending on any external libraries and instead utilizing features provided by the Linux Kernel to the maximum extent possible.

iwd can work in standalone mode or in combination with comprehensive network managers like ConnMan, systemd-networkd and NetworkManager.

## Installation
Install the  package.

Optionally, third-party graphical and terminal user interface front-ends can be installed:

*
*
*
*
*

## Usage
The  package provides the client program , the daemon  and the Wi-Fi monitoring tool .

Start/enable  so it can be controlled through the  command or through your preferred iwd front-end.

## iwctl
To get an interactive prompt do:

 $ iwctl

The interactive prompt is then displayed with a prefix of .

To list all available commands:

 help

## Connect to a network
First, if you do not know your wireless device name, list all Wi-Fi devices:

 [iwd# device list

If the device or its corresponding adapter is turned off, turn it on:

 device name set-property Powered on

 [iwd# adapter adapter set-property Powered on

Then, to initiate a scan for networks (note that this command will not output anything):

 station name scan

You can then list all available networks:

 [iwd# station name get-networks

Finally, to connect to a network:

 station name connect SSID

If network is hidden:

 [iwd# station name connect-hidden SSID

If a passphrase is required (and it is not already stored in one of the profiles that iwd automatically checks), you will be prompted to enter it. Alternatively, you can supply it as a command line argument:

 $ iwctl --passphrase passphrase station name connect SSID

## Connect to a network using WPS/WSC
If your network is configured such that you can connect to it by pressing a button (Wikipedia:Wi-Fi Protected Setup), check first that your network device is also capable of using this setup procedure.

 wsc list

Then, provided that your device appeared in the above list,

 [iwd# wsc device push-button

and push the button on your router. The procedure works also if the button was pushed beforehand, less than 2 minutes earlier.

If your network requires to validate a PIN number to connect that way, check the  command output to see how to provide the right options to the  command.

## Disconnect from a network
To disconnect from a network:

 station device disconnect

## Show device and connection information
To display the details of a Wi-Fi device, like MAC address:

 [iwd# device device show

To display the connection state, including the connected network of a Wi-Fi device:

 station device show

## Manage known networks
To list networks you have connected to previously:

 [iwd# known-networks list

To forget a known network:

 known-networks SSID forget

## iwgtk
Alternatively,  provides a GUI front-end through which iwd can be controlled.

Running  without any arguments launches the application window, which can be used to toggle your adapters and devices on/off, change their operating modes, view available networks, connect to available networks, and manage known networks.

## Indicator icon
To launch iwgtk's indicator (tray) icon daemon, run:

 $ iwgtk -i

If the indicator icon does not appear, then your system tray most likely lacks support for the StatusNotifierItem API, in which case you need to run a compatibility layer such as .

The following system trays support StatusNotifierItem, and therefore work out of the box:

* KDE Plasma
* swaybar
* lxqt-panel
* xfce4-panel

The following trays only support XEmbed, and therefore require :

* AwesomeWM
* i3bar
* stalonetray

## Autostart
The most common use case for iwgtk is to start the indicator daemon every time you log into your desktop. If your desktop environment supports the XDG Autostart standard, this should happen automatically due to the  file which is placed in  by the AUR package.

Alternatively, a systemd unit file to start the indicator daemon is provided by the AUR package. If your desktop environment supports systemd's  unit, then iwgtk can be autostarted via systemd by enabling the  user unit.

## Network configuration
By default, iwd stores the network configuration in the directory . The configuration file is named as , where network is the network SSID and .type is the network type, either .open, .psk or .8021x. The file is used to store the encrypted  and optionally the cleartext  and can also be created by the user without invoking . The file can be used for other configuration pertaining to that network SSID as well. For more settings, see .

## WPA-PSK
A minimal example file to connect to a WPA-PSK or WPA2-PSK secured network with SSID "spaceship" and passphrase "test1234":

To calculate the pre-shared key from the passphrase, one of these two methods can be used:

* Enter the passphrase in cleartext in the configuration file:

:The pre-shared key will be appended to the file at the first connect:

* Or the pre-shared key can be calculated from the SSID and the passphrase using wpa_passphrase (from ) or . See wpa_supplicant#Connecting with wpa_passphrase for more details.

## WPA Enterprise
## EAP-PWD
For connecting to a EAP-PWD protected enterprise access point you need to create a file called:  in the  directory with the following content:

If you do not want autoconnect to the AP you can set the AutoConnect option to False and connect manually to the access point via . The same applies to the password, if you do not want to store it plaintext leave the option out of the file and just connect to the enterprise AP.

## EAP-PEAP
Like EAP-PWD, you also need to create a  file in the directory. Before you proceed to write the configuration file, this is also a good time to find out which CA certificate your organization uses. This is an example configuration file that uses MSCHAPv2 password authentication:

MsCHAPv2 passwords can also be stored as an encrypted hash. The correct md4 hash can be calculated with:

 $ iconv -t utf16le | openssl md4 -provider legacy

Insert an EOF after your password by pressing , do not hit . The resulting hash needs to be stored inside the  key.

## TTLS-PAP
Like EAP-PWD, you also need to create a  file in the directory. Before you proceed to write the configuration file, this is also a good time to find out which CA certificate your organization uses. This is an example configuration file that uses PAP password authentication:

## EAP-TLS
EAP-TLS uses x509 client certificates to authenticate you. Like ssh keys, these use public-key cryptography, so the Wi-Fi authentication server never needs to be sent a secret, and you do not need to copy and reuse a password between devices. Usually each device will use a distinct cert, one that can, in theory at least, be revoked without forcing you to change a password or disrupt your other devices.

As with the other enterprise methods you need to know the CA cert your organization uses (), which is used to prove to your device it is connecting to the right place. You also need to have the client certificate, which represents you and will be uploaded on each connection (), and the private key that goes with it (), which is used to prove you own that client certificate.

You can either provide a path to the required certificate or you can embed them inside your configuration.

When you have collected the credentials, put this in your  file:

## eduroam
## Configuration via CAT
Eduroam offers a [https://cat.eduroam.org/ configuration assistant tool (CAT). If your organisation has a profile within the CAT, getting connected to eduroam can be done by downloading the Linux script and running it using python. In newer versions, the CAT can create the necessary iwd configuration file directly. Use
 python3 eduroam-linux-organisation.py --iwd_conf.
Then enter your credentials via the GUI. The configuration file is saved in the current working directory. You have to place it into  manually and restart iwd. Your certificate is saved in , but also included directly into the configuration file.

If the CAT version of your organisation does not support iwd yet, it is possible to extract the necessary configuration options from the CAT python script directly, including the certificate and server domain mask. Additionally, some institutions are upgrading to EAP-TLS, and outsourcing the generation of  to SecureW2, in which case you will need to use their tool as well to generate a client cert.

The following table contains a mapping of iwd configuration options to eduroam CAT install script variables.

{| class="wikitable"
! Iwd Configuration Option !! CAT Script Variable
|-
| essid || one of
|-
|  ||
|-
|  ||
|-
|  || the content of , an absolute path to a .pem file containing  or an embedded certificate.
|-
|  || one of
|-
|  ||  unless it is equal to , in that case use instead
|-
|  ||
|}

where  is the content of  and should be either ,  or .  Once you have extracted all necessary information and converted them to their iwd configuration equivalent you can put them in a configuration file called  as explained in the preceding methods.

If your organisation does not support CAT, you will have to create the configuration file manually using parameters provided to you by the administrators.

## Manually
Another method of connecting to eduroam via iwd is provided here. Create the following file, filling in the necessary values:

## Other cases
More example tests can be found in the test cases of the upstream repository.

## Embedded certificates
Instead of including an absolute path to a PEM file (for certificates and keys), the PEM itself can be included inside the network configuration file.

An embedded PEM can appear anywhere in the settings file using the following format:

 ----- BEGIN CERTIFICATE -----
 PEM data
 ----- END CERTIFICATE -----

where my_ca_cert is any name you can use to identify the certificate inside the configuration file.

Then the embedded certificate can be used anywhere in the settings file a certificate path is required by prefixing the value with

 EAP-TTLS-CACert=embed:my_ca_cert

This  is not limited to CA certificates either. Client certificates, client keys (encrypted or not), and certificate chains can be included.

## WPA over wired ethernet
For WPA on a wired ethernet connection create a config as above,
but place it in the  directory instead.

Afterwards Start/enable .

## Optional configuration
File  can be used for main configuration. See .

## Disable auto-connect for a particular network
Create or edit the file . Add the following section to it:

## Disable periodic scan for available networks
By default when  is in disconnected state, it periodically scans for available networks. To disable periodic scan (so as to always scan manually), create / edit file  and add the following section to it:

## Enable built-in network configuration
Since version 0.19, iwd can assign IP address(es) and set up routes using a built-in DHCP client or with static configuration. It is a good alternative to standalone DHCP clients.

To activate iwd's network configuration feature, create/edit  and add the following section to it:

There is also ability to set route metric with :

## IPv6 support
Since version 1.10, iwd supports IPv6, but it is disabled by default in versions below 2.0.
Since version [https://git.kernel.org/pub/scm/network/wireless/iwd.git/commit/?id=00baa75e963334fc3946490e554641891614c255 2.0, it is enabled by default.

To disable it, add the following to the configuration file:

To enable it in version below 2.0 and higher than 1.10:

This setting is required to be enabled whether you want to use DHCPv6 or static IPv6 configuration.  It can also be set on a per-network basis.

## Setting static IP address in network configuration
Add the following section to  file. For example:

## Select DNS manager
At the moment, iwd supports two DNS managers—systemd-resolved and resolvconf.

Add the following section to  for :

For :

## Configuring MAC address randomization
See MAC address spoofing#iwd.

## Allow any user to read status information
If you want to allow any user to read the status information, but not modify the settings, you can create the following D-Bus configuration file:

## Encrypted network profiles
By default, iwd stores network credentials to the system unencrypted. Since iwd version 1.25, iwd provides experimental support for creating encrypted profiles for systems using systemd.

First, create an encrypted credential. The following example uses systemd-creds and creates an encrypted credential called iwd-secret that is bound to the system's Trusted Platform Module which will be used to create encrypted profiles:

 # systemd-ask-password -n | systemd-creds --tpm2-device=auto --name=iwd-secret encrypt - /etc/credstore.encrypted/iwd-secret.cred

Next, add the  option by creating a drop-in file for the iwd service.

Finally, add the  option with the value being the named credential to the iwd configuration file, reload the systemd manager, and restart the iwd service.

## Troubleshooting
## Verbose TLS debugging
This can be useful, if you have trouble setting up MSCHAPv2 or TTLS. You can set the following environment variable via a drop-in snippet:

Check the iwd logs afterwards by running  as root.

## Restarting iwd.service after boot
On some machines, it is reported that  has to be restarted to work after boot. See  and thread 251432. This probably occurs because iwd starts before wireless network card powers on.

As a workaround, find the unit needed to wait for by  and extend the unit accordingly:

Then reload the systemd manager configuration.

If it does not work, try also
 ExecStartPre=ip link set wlan0 up

## Wireless device is not renamed by udev
Since version 1.0, iwd disables network interface renaming to [https://systemd.io/PREDICTABLE_INTERFACE_NAMES/ predictable network interface names. It installs the following  configuration file which prevents udev from renaming the interface to a predictable, stable name (e.g. ):

As a result the wireless link name  is kept after boot. This resolved a race condition between iwd and udev on interface renaming as explained in iwd udev interface renaming.

If this results in issues try masking it with:

 # ln -s /dev/null /etc/systemd/network/80-iwd.link

## No DHCP in AP mode
Clients may not receive an IP address via DHCP when connecting to iwd in AP mode. It is therefore necessary to enable network configuration by iwd on managed interfaces:

The mentioned file has to be created if it does not already exist.

## Wi-Fi keeps disconnecting due to iwd crash
Some users experience disconnections with Wi-Fi, re-connecting continuously but stabilizing eventually and managing to connect.

Users report crashes (of  in their journal.

The core issue is having multiple conflicting services for managing their network connections. Check that you do not have enabled them at the same time to fix this issue.

## Error loading client private key
To load key files iwd requires the  kernel module. While on boot it gets loaded by  using , that will not be the case if  has just been installed.

If messages such as  show up in the journal when trying to connect to WPA Enterprise networks, manually load the module:

 # modprobe pkcs8_key_parser

## iwd keeps roaming
iwd will roam to other known APs if the connection is too bad.

This will show up in the system log as

You can see the connection signal strength with

 iwctl station wlan0 show | grep RSSI

You can increase the threshold to allow a worse connection. RoamThreshold defaults to -70 and RoamThreshold5G to -76.

## Hostname not sent in DHCP request
Set  in the network's configuration file, not in .

## /etc/resolv.conf: Read-only file system
When using resolvconf as DNS resolution method, it may have trouble writing to  complaining about read-only file system:

To fix this problem, extend the configuration of the  systemd unit by adding drop-in file:

This will allow the  system unit to update . Restart  to make the change effective.

## Connection to iPhone hotspot fails repeatedly
When connecting to an iPhone personal hotspot,  may repeatedly connect and immediately disconnect with  in the journal:

 $ journalctl -b -u iwd
 event: state, old: connected, new: disconnecting
 event: connect-failed, status: 1
 event: state, old: connecting, new: disconnected

This can be caused by MAC address randomization interfering with the iPhone's hotspot authentication. To resolve it, set  in the iwd configuration:

Then restart .

If the issue persists, try setting .
