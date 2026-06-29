# Mullvad

Mullvad is a VPN service based in Sweden which uses WireGuard.

## Installation
The official GUI client is available as  and .

After installation, you will only have to start/enable .

Alternatively, see #Manual configuration for manually setting up a Mullvad VPN connection without the official GUI.

## Manual configuration
If you do not want to use the official application, you can manually set up a Mullvad VPN connection with WireGuard. As of the 15th January 2026, Mullvad ended OpenVPN support in favour of WireGuard.

If you use NetworkManager you may want to set up dnsmasq to decrease DNS lookup times and decrease the risk of DNS leakages. Follow the steps under DNS_caching_and_conditional_forwarding.

## Using WireGuard
## Using WG-Quick
Install the  and  packages. Log in to Mullvad with your account and then go to the WireGuard configuration file generator. Under Generate a WireGuard key, click generate key to generate a private key, or you can issue the following command to generate a private key and import it.

 # wg genkey

Fill out the next step under Select one or multiple exit locations on the generator and download the file. Extract the file you downloaded to get one or several configuration files depending on your selections. Move the configuration files into .

For this example, we have selected Malmö, Sweden (se-mma-wg-001), as our server location, so the downloaded configuration file is named .

As root, run the following command. Replace se-mma-wg-001 with your selected server.

 # wg-quick up se-mma-wg-001

To stop it, run the following command.

 # wg-quick down se-mma-wg-001

To automatically have it run at boot, enable/start .

## With NetworkManager
To add a WireGuard connection from a config-file, issue following command in terminal:

 # nmcli connection import type wireguard file configuration_file

If the file was called WG1.conf a connection called WG1 should have been added.

If you at any point want to delete the connection, issue the command:

 # nmcli connection delete connection_name

To actually start the WireGuard tunnel, issue command:

 # nmcli connection up connection_name

Make sure the connection is listed when you run nmcli:

 # nmcli

You might want to verify that the private and public keys are correct and corresponds with what you got from your VPN provider:

 # WG_HIDE_KEYS=never wg

You may also want to set the connection's DNS priority if exclusive use of Mullvad's DNS is desired; see #DNS leaks.

Mullvad has provided a shell script to automate this process - with a caveat: the automatically generated configuration files do not contain kill switches, which need to be manually added if you so desire.

## with KDE
KDE settings (`systemsettings kcm_networkmanagement`), which is a frontend for Network Manager, can either import individual files that you download from mullvad's website (linux configuration), or you can open those files and manually add the values.

The required fields are:

{| class="wikitable"
|+ Wiguard config file fields translation to KDE Conections
|-
! settings tab !! field !! mullvad config file
|-
| IP V4 || Method: Manual || n/a
|-
| IP V4 || Address/Netmask || Interface.Address (must split on `,` and interpret the mask value. Same for IPV6)
|-
| IP V6 || Method: Manual (or ignored) || n/a
|-
| Wireguard Interface || Private Key || Interface.PrivateKey
|-
| Peers || Public Key || Peer.PublicKey
|-
| Peers || Allowed IPs || Peer.AllowedIPs
|-
| Peers || Endpoint address || Peer.Endpoing (must split on `:`)
|-
| Peers || Endpoint port || Peer.Endpoing (must split on `:`)

|}

Note that there is an easy to miss "Peers" button in the "Wireguard Interface" tab to open the Peers section.

To use multiple peers, you will have to open the `zip` file, and add one peer from each individual file on the Peers dialog. Note that the "Wireguard Interface" and IP tabs will be the same for all the files inside the `zip` archive you got from mullbad.

## With systemd-networkd
For basic kill-switch functionality you can use iptables to block all outgoing connections except those with fwmark 0x8888:

## DNS leaks
Remember to install the openresolv package to prevent DNS leaks. If you are manually importing WireGuard config files with NetworkManager, you may also want to set the connection's DNS priority to a negative value. This ensures that the system will use Mullvad's DNS server exclusively when the VPN is active.

 # nmcli connection modify connection_name ipv4.dns-priority -1
 # nmcli connection modify connection_name ipv6.dns-priority -1

## IPv6
Mullvad's WireGuard servers fully support IPv6, both inside and outside the tunnel. Users of the GUI app can enable tunneling IPv6 in VPN settings, and enable running the tunnel itself over IPv6 in VPN settings > WireGuard settings > IP version. This may improve performance somewhat by allowing/encouraging larger packet sizes in the WireGuard tunnel. These preferences can be chosen on the WireGuard config generator for manual users.

## Preferring IPv6 inside the tunnel
Because the VPN assigns a unique local address and performs network address translation (an unusual way to configure IPv6 connections to the public Internet),  de-prioritizes IPv6 within the tunnel and will only use it when it is the only available option for a connection. To solve this and prefer IPv6 within the tunnel (as is the default on a standard connection), edit the  file and add the following line:

## Automatic configuration
vopono supports automatically generating configuration files for Mullvad, allowing you to instantly run applications via Mullvad connections in temporary network namespaces. Port forwarding is supported.
