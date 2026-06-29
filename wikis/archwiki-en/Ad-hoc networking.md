# Ad-hoc networking

An IBSS (Independent Basic Service Set) network, often called an ad-hoc network, is a way to have a group of devices talk to each other wirelessly, without a central controller. It is an example of a peer-to-peer network, in which all devices talk directly to each other, with no inherent relaying.

For example, ad-hoc networking may be used to share an internet connection.

## Requirements
* An nl80211 compatible wireless device (e.g. ath9k) on all devices which will connect to the network

## Wi-Fi link layer
Since IBSS network is a peer-to-peer network, the steps necessary to set up the Wi-Fi link layer should be the same on all devices.

## Manual method
See Wireless network configuration#iw for a better explanation of the following commands. Make sure that  is installed.

Set the operation mode to ibss:

 # iw interface set type ibss

Bring the interface up (an additional step like  might be needed):

 # ip link set interface up

Now you can create an ad-hoc network. Replace your_ssid with the name of the network and frequency with the frequency in MHz, depending on which channel you want to use. See the Wikipedia page List of WLAN channels for a table showing frequencies of individual channels.

 # iw interface ibss join your_ssid frequency

## wpa_supplicant
Ensure that  is installed, and create a configuration file for it (see wpa_supplicant for details).

{{hc|/etc/wpa_supplicant-adhoc.conf|
ctrl_interface=DIR=/run/wpa_supplicant GROUP=wheel

# use 'ap_scan=2' on all devices connected to the network
# this is unnecessary if you only want the network to be created when no other networks are available
ap_scan=2

network={
    ssid="MySSID"
    mode=1
    frequency=2432
    proto=RSN
    key_mgmt=WPA-PSK
    pairwise=CCMP
    group=CCMP
    psk="secret passphrase"
}
}}

Run wpa_supplicant on all devices connected to the network with the following command:

 # wpa_supplicant -B -i interface -c /etc/wpa_supplicant-adhoc.conf -D nl80211,wext

## Network configuration
The final step is to assign an IP address to all devices in the network. There are multiple ways to do this:

* Assign static IP addresses. See Network configuration#Static IP address for details.
* Running DHCP server on one device. See Router#DNS and DHCP for details.
* Running avahi-autoipd. See Avahi#Obtaining IPv4LL IP address for details.

If you want to share an internet connection to the ad-hoc network, see Internet sharing.

## Tips and tricks
## Using NetworkManager
If you use NetworkManager, you can use nm-applet for ad-hoc network configuration instead of the manual method described above. See NetworkManager#Sharing internet connection over Wi-Fi for details.

## Custom systemd service (with wpa_supplicant and static IP)
You can use the following templates to enable wireless ad-hoc networking:

{{hc|/etc/systemd/system/network-wireless-adhoc@.service|2=
Description=Ad-hoc wireless network connectivity (%i)
Wants=network.target
Before=network.target
BindsTo=sys-subsystem-net-devices-%i.device
After=sys-subsystem-net-devices-%i.device

[Service
Type=oneshot
RemainAfterExit=yes
EnvironmentFile=/etc/conf.d/network-wireless-adhoc@%i

# perhaps rfkill is not needed for you
ExecStart=/usr/bin/rfkill unblock wifi
ExecStart=/usr/bin/ip link set %i up
ExecStart=/usr/bin/wpa_supplicant -B -i %i -D nl80211,wext -c /etc/wpa_supplicant-adhoc.conf
ExecStart=/usr/bin/ip addr add ${addr}/${mask} dev %i

ExecStop=/usr/bin/ip addr flush dev %i
ExecStop=/usr/bin/ip link set %i down

WantedBy=multi-user.target
}}
