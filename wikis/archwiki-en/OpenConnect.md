# OpenConnect

OpenConnect is free open-source software for client-to-site VPNs. It allows you to connect to various commercial so-called SSL VPN servers/gateways/concentrators, namely:
* Cisco AnyConnect anyconnect
* Palo Alto Networks (PAN) GlobalProtect gp
* Junos/Ivanti Pulse Secure pulse, see also Pulse Connect Secure
* Juniper Network Connect nc
* Fortinet fortinet
* F5 f5
* Array Networks array

## Installation
For integration with NetworkManager which you probably use if you have a desktop environment like GNOME or KDE, install the  package. It will pull in the  package as a dependency. If you do not need the integration, install only the  package.

Some VPNs are set up for split routing and therefore split DNS. To cater for that and in general, it's recommended to use systemd-resolved and the resolv.conf stub mode. To verify that this is the case, run  and look for the line "resolv.conf mode: stub" in the Global section. Understanding the full output can be very useful so it's probably a good idea to study it. When connected to a VPN, the output will look roughly like this:

## Usage
## Plain OpenConnect
OpenConnect has many options, see . In the simplest case, you are using a Cisco AnyConnect VPN, thus you only have to provide the address, then enter your username and password when prompted:

 $ sudo openconnect vpnserviceaddr

If you use a VPN type other than Cisco AnyConnect, add the "--protocol" option specifying either nc, gp, pulse, f5, fortinet, or array:

 $ sudo openconnect --protocol=vpntype vpnserviceaddr

The username can be provided too:

 $ sudo openconnect --protocol=vpntype -u user vpnserviceaddr

Some VPNs offer different authentication groups for different access configurations like for example for a full tunnel or split tunnel connection. To show the different offered auth-groups and to get more information about the service in general, use:

 $ sudo openconnect --protocol=vpntype --authenticate vpnserviceaddr

Some VPNs require gathering information about your computer when connecting. In that case the "--csd-wrapper" option can help. Scripts to use and adapt can be found under "/usr/lib/openconnect/".

 $ sudo openconnect --protocol=vpntype --csd-wrapper=script vpnserviceaddr

Some VPNs delegate authentication to an identity provider (IdP) like Google, Microsoft AzureActiveDirectory, or Okta. This scenario is often called single sign-on (SSO) and usually employs the SAML 2.0 standard or the OIDC standard. It goes like this: In a browser or webview, you open the VPN's SSO address which redirects to the IdP which sends you back to the VPN page where you end up with a cookie. The cookie must be passed to openconnect using the option "-C,--cookie" or "--cookie-on-stdin". To copy the cookie from your browser, use its developer tools.

 $ sudo openconnect --protocol=vpntype --cookie-on-stdin vpnserviceaddr

For Fortinet SSO VPNs, you can use  to fetch the cookie instead of fiddling with your browser's developer tools:

 $ sudo openconnect --protocol=fortinet -C "$(openfortivpn-webview vpnserviceaddr)" vpnserviceaddr

OpenConnect passes a couple of environment variables to a script in order to configure IP routing and DNS routing. By default that's "/etc/vpnc/vpnc-script". It supports a few environment variables that you can set if needed, e.g. "CISCO_SPLIT_DNS" to add additional DNS domains to the network interface besides the ones pushed by the VPN:

 $ sudo CISCO_SPLIT_DNS=~internal.example.com,~10.in-addr.arpa openconnect --protocol=vpntype vpnserviceaddr

You can use your own script instead of the default one using the option "-s,--script":

 $ sudo openconnect --protocol=vpntype -s script vpnserviceaddr

You can also team up OpenConnect with a proxy like  in order to do SSH-style port-forwarding. E.g. a connection to localhost:13389 using rdesktop gets forwarded through the VPN to the RDS service rds.int.example.net:3389 if you run:

 $ openconnect --protocol=vpntype --script-tun -s "ocproxy -L 13389:rds.int.example.net:3389" vpnserviceaddr
 $ rdesktop localhost:13389

## With NetworkManager
NetworkManager can be controlled via command line interface , via terminal user interface , and via many desktop environments, thanks to its D-Bus API. For NetworkManager a VPN is just another connection of type "vpn". To create one based on OpenConnect named "MyOrgVPN" with the CLI, run:

Activating the connection using  (i.e. without ) or GNOME's menu in the top right corner or GNOME settings, a.k.a. control center, works in most cases as one would expect: a window opens and asks for a username, password, and possibly 2FA/MFA; even SSO scenarios often work if the VPN type is anyconnect or gp. For other desktop environments you might have to install , , or some other package in order to control NetworkManager connections.

Activating the connection using  or  or  does not work the way one would expect though: instead of getting asked for a username, etc., one gets asked for "Cookie (vpn.secrets.cookie)". To provide it, you can use a Bash script like this one:
{{hc|~/vpn-up.bash|
#!/usr/bin/bash

connection_name=$(nmcli -t -g type,name connection \
	| grep -Po '^vpn:\K.*' \
	| sed 's/\\:/:/g' | fzf
)
eval "$(nmcli -t -g vpn.data connection show "$connection_name" \
	| grep -Po '(^|[ ,])(protocol|gateway)\ =\ \
	| sed 's/ //g')"
eval "$(openconnect --authenticate --protocol="$protocol" "$gateway")"
nmcli connection up "$connection_name" \
	passwd-file '
LOCAL_USERNAME=
REMOTE_USERNAME=
# Assuming the use of pass(1):
PASSWORD_CMD="su ${LOCAL_USERNAME} -c \"pass ${REMOTE_USERNAME} | head -n 1\""

ExecUpPost="${PASSWORD_CMD} | /usr/bin/openconnect --background --pid-file=${PIDFILE} --interface='${Interface}' --authgroup='${AUTHGROUP}' --user='${REMOTE_USERNAME}' --passwd-on-stdin ${SERVER}"
ExecDownPre="kill -INT $(cat ${PIDFILE}) ; resolvconf -d ${Interface} ; ip link delete ${Interface}"
}}

This allows execution like:

 $ netctl start vpn
 $ netctl restart vpn
 $ netctl stop vpn

Note that this relies on  having a gpg-agent running, with the passphrase for the PGP key already cached.

If pass's interactive query is wanted, use the following line for :

 DISPLAY=":0"
 PASSWORD_CMD="su ${LOCAL_USERNAME} -c \"DISPLAY=${DISPLAY} pass ${REMOTE_USERNAME} | head -n 1\""

Adjust the  variable as necessary.

## Troubleshooting
## Cisco AnyConnect
For Cisco AnyConnect VPNs, if you try to use 2FA/MFA but it is not prompting you for the passcode, you need to set the useragent to . This is an issue with Cisco, here is the [https://gitlab.com/openconnect/openconnect/-/issues/665 relevant issue in the OpenConnect project.

## Issues caused by AnyConnectLocalPolicy.xml
 Automatic profile updates are disabled and the local VPN profile does not match the secure gateway VPN profile.

Is caused by . To fix it edit the file and set
 false

## Issues caused by IPv6
In some cases, Cisco AnyConnect fails to establish a VPN connection due to conflicts with IPv6.

 AnyConnect was not able to establish a connection to the specified secure gateway.
Can be temporary fixed by disabling ipv6:
 # sysctl -w net.ipv6.conf.all.disable_ipv6=1
