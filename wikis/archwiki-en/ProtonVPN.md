# ProtonVPN

ProtonVPN is a VPN provider that utilizes the OpenVPN and WireGuard protocol.

## Installation
Install one of the following:

## OpenVPN
Install the  package, then follow the OpenVPN setup.

## WireGuard
Install the  package. Ensure  is also installed. Then follow the WireGuard setup.

## Official ProtonVPN client
Install  for the GUI application, or  for the CLI version.

The  and  packages may be installed for integration into the GNOME and Plasma desktop environments, respectively.

You must also use NetworkManager, otherwise the VPN will not connect. You can still use your current network manager, although running multiple network managers is not recommended.

## Setup
## OpenVPN setup
Download one or more OpenVPN configuration files from ProtonVPN Downloads page.

Copy the  client configuration files into  and make backup of original.

Follow OpenVPN#The update-systemd-resolved custom script to make sure that all your network traffic uses VPN (Note: The steps mention a  file, which corresponds to the  files.) If you use systemd older than 229, follow OpenVPN#The update-resolv-conf custom script.

For usage instructions, see Using OpenVPN.

## WireGuard setup
Download WireGuard configuration files by signing into ProtonVPN and go to Downloads → WireGuard configuration.

Move the  files into . Some users have had issues if the  filename is too long, but a known error is that the dash  in the filename will prevent the config from being read. This is a problem, since ProtonVPN automatically puts dashes in your file upon download. You need to manually rename it to remove them.

If you have not already, start/enable .

## Usage
## Using OpenVPN
Connect to the VPN:

 # openvpn /etc/openvpn/client/client_config_file.ovpn

Provide OpenVPN / IKEv2 Username from the ProtonVPN Account page.

Press  to close the VPN connection.

## Using WireGuard
To add and bring up an interface, replace CONFIG_FILE with the configuration file, e.g. :

 # wg-quick up CONFIG_FILE

To check the status of the connection, run

 # wg

To tear down and remove the interface:

 # wg-quick down CONFIG_FILE

## Tips and tricks
## Enable VPN on boot
;OpenVPN: For systemd service configuration, see OpenVPN#systemd service configuration.
;Wireguard: For systemd service configuration, see WireGuard#Persistent configuration.

## Only run certain applications through VPN with network namespaces
vopono supports automatic configuration file generation for ProtonVPN, and allows you to run applications inside temporary network namespaces so only those run through the VPN.

## Save login information
To retain VPN credentials for subsequent connections, create the following file with your own login information on two lines and place it in the directory where you will run the startup script listed above.

Then add the line  to any relevant  files.

## SysTray/Indicator
For the system/tray indicator to work, ensure you have installed  and .

## Prevent IPv6 leaks
ProtonVPN's servers default to using the IPv6 internet protocol with their official Linux client. If IPv6 leaks are observed, you can prevent them by blocking IPv6 traffics or disabling IPv6. See IPv6#Disable IPv6.

## Enable Port Forwarding
For paid ProtonVPN users, port forwarding can be enabled.

* For proton-vpn-gtk-app it is supported as a setting. When enabled, the forwarded port will be displayed when you connect to a server.
* For OpenVPN and Wireguard installations, refer to ProtonVPN's documentation to enable port forwarding.

## Troubleshooting
## Official client will not connect
You may see an error message like “Unknown reason occurred.” when attempting to connect.

Install NetworkManager (and configure if needed), as it needs to be running for ProtonVPN official clients to connect, whether you are using the GUI or CLI application.

## "Invalid username." error
When signing in to ProtonVPN through the , the error "Invalid username." may be thrown if your account password is greater than 72 characters or contains extended-ASCII characters.

To resolve the issue, access your account via the ProtonVPN website (https://protonvpn.com/) and update your password to one less than 72 characters, with no extended-ASCII characters.
