# ConnMan

ConnMan is a command-line network manager designed for use with embedded devices and fast resolve times. It is modular through a plugin architecture, but has native DHCP and NTP support.== Installation ==

Install the  package. , , and  are optional dependencies required for Wi-Fi, Bluetooth, and VPN functionality respectively.

Before enabling , ensure any existing network configuration is disabled.

ConnMan comes with the  CLI, there are various #Front-ends available.

## Front-ends
*
*
*
*
*

## Usage
ConnMan comes with the  command-line interface, see .
If you do not provide any commands  starts as an interactive shell.

ConnMan automatically handles wired connections.

## Wi-Fi
## Enabling and disabling Wi-Fi
To check if Wi-Fi is enabled you can run  and check for the line that says .
To power the Wi-Fi on you can run  or if you need to disable it you can run .
Other ways to enable Wi-Fi could include using the  keys on the laptop to turn it on or running .

## Connecting to an open access point
To scan the network  accepts simple names called technologies. To scan for nearby Wi-Fi networks:

 $ connmanctl scan wifi

To list the available networks found after a scan run (example output):

To connect to an open network, use the second field beginning with :

 $ connmanctl connect wifi_dc85de828967_4d6568657272696e_managed_none

You should now be connected to the network. Check using  or .

## Connecting to a protected access point
For protected access points you will need to provide some information to the ConnMan daemon, at the very least a password or a passphrase.

The commands in this section show how to run  in interactive mode, it is required for running the  command.  To start interactive mode simply type:

 $ connmanctl

You then proceed almost as above, first scan for any Wi-Fi technologies:

 connmanctl> scan wifi

To list services:

 connmanctl> services

Now you need to register the agent to handle user requests.  The command is:

 connmanctl> agent on

You now need to connect to one of the protected services.  To do this easily, just use tab completion for the  service.  If you were connecting to OtherNET in the example above you would type:

 connmanctl> connect wifi_dc85de828967_38303944616e69656c73_managed_psk

The agent will then ask you to provide any information the daemon needs to complete the connection.  The
information requested will vary depending on the type of network you are connecting to.   The agent
will also print additional data about the information it needs as shown in the example below.

 Agent RequestInput wifi_dc85de828967_38303944616e69656c73_managed_psk
   Passphrase = [ Type=psk, Requirement=mandatory
   Passphrase?

Provide the information requested, in this example the passphrase, and then type:

 connmanctl> quit

If the information you provided is correct you should now be connected to the protected access point.

## Using iwd instead of wpa_supplicant
ConnMan can use  to connect to wireless networks. As  will start  when it finds it, it is recommended to uninstall .

Note that ConnMan is probably unnecessary for IWD users, as IWD can handle its own network configuration, in which case  should be stopped.

Currently the -option of  seems to cause that the Wi-Fi interface gets hidden from .

Create the following service file which should cause  to use  to connect to wireless networks, regardless if  is installed.

Then enable/start the  service.

Advantage of using  instead of  is, that the ping times seem to be much more consistent and the connection seems to be more reliable.

## Settings
Settings and profiles are automatically created for networks the user connects to often. They contain fields for the passphrase, essid and other information. Profile settings are stored in directories under  by their service name. To view all network profiles run:

 # cat /var/lib/connman/*/settings

## Technologies
Various hardware interfaces are referred to as Technologies by ConnMan.

To list available technologies run:

 $ connmanctl technologies

To get just the types by their name one can use this one liner:

 $ connmanctl technologies | awk '/Type/ { print $NF }'

To interact with them one must refer to the technology by type. Technologies can be toggled on/off with:

 $ connmanctl enable technology_type

and:

 $ connmanctl disable technology_type

For example to toggle off Wi-Fi:

 $ connmanctl disable wifi

## Tips and tricks
## Avoid changing the hostname
By default, ConnMan changes the transient hostname (see ) on a per network basis. This can create problems with X authority: If ConnMan changes your hostname to something else than the one used to generate the xauth magic cookie, then it will become impossible to create new windows. Symptoms are error messages like  and . Manually resetting the host name fixes this, but a permanent solution is to prevent ConnMan from changing your host name in the first place. This can be accomplished by adding the following to :

 AllowHostnameUpdates=false

Make sure to restart the  after changing this file.

For testing purposes it is recommended to watch the systemd journal and plug the network cable a few times to see the action.

## Prefer Ethernet to wireless
By default ConnMan does not prefer Ethernet over wireless, which can lead to it deciding to stick with a slow wireless network even when ethernet is available. You can tell connman to prefer Ethernet adding the following to :

 [General
 PreferredTechnologies=ethernet,wifi

## Exclusive connection
ConnMan allows you to be connected to both Ethernet and wireless at the same time. This can be useful as it allows programs that established a connection over Wi-Fi to stay connected even after you connect to ethernet. But some people prefer to have only a single unambiguous connection active at a time. That behavior can be activated by adding the following to :

 SingleConnectedTechnology=true

## Connecting to eduroam (802.1X)
WPA2 Enterprise networks such as eduroam require a separate configuration file before connecting to the network. For example, create :

Restart  and  to connect to the new network.

For more information, see  and Wireless network configuration#eduroam.

## Avoiding conflicts with local DNS server
If you are running a local DNS server, it will likely have problems binding to port 53 (TCP and/or UDP) after installing Connman. This is because Connman includes its own DNS proxy which also tries to bind to those ports. If you see log messages from BIND or dnsmasq like

 named[529: could not listen on UDP socket: address in use

this could be the problem. To verify which application is listening on the ports, you can execute  as root.

To fix this connmand can be started with the options  or  by overriding the systemd service file. Create the folder  and add the file :

Make sure to reload the systemd daemon and restart the , and your DNS proxy, after adding this file.

## DNS management
## /etc/resolv.conf
If you want to know the DNS servers received from DHCP while keeping a custom , then append  to the above file (clear the  lines if not needed). Now connman will write them to  instead.

## Using systemd-resolved
ConnMan has systemd-resolved support, which replaces its internal DNS proxy with a module that configures systemd-resolved with the correct DNS servers and search domains for the interface whenever it connects to a network. Using systemd-resolved is known to improve compatibility with Tailscale since ConnMan's internal proxy and Tailscale can fight over , which is better mediated by both talking to resolved instead.

To use this support, ConnMan needs to be rebuilt: checkout the package using the Arch build system, set the configure flag , rebuild the package, and install the modified version. After installing the modified package, set up the stub resolver as  then restart , , and (if using it) .

## Blacklist interfaces
If something like Docker is creating virtual interfaces Connman may attempt to connect to one of these instead of your physical adapter if the connection drops. A simple way of avoiding this is to blacklist the interfaces you do not want to use. Connman will by default blacklist interfaces starting with , ,  and , so those need to be included in the new blacklist as well.

Blacklisting interface names is also useful to avoid a race condition where connman may access  or  before systemd/udev can change it to use a Predictable Network Interface Names like . Blacklisting the conventional (and unpredictable) interface prefixes makes connman wait until they are renamed.

If it does not already exist, create :

 NetworkInterfaceBlacklist=vmnet,vboxnet,virbr,ifb,docker,veth,eth,wlan

Once  has been restarted this will also hide all the  interfaces from GUI tools like Econnman.

## Troubleshooting
## Error /net/connman/technology/wifi: Not supported
Currently, connman does not support scanning for Wi-Fi networks with , at the moment this functionality is available with  only (see [https://web.archive.org/web/20220916045152mp_/https://lists.01.org/hyperkitty/list/iwd@lists.01.org/thread/OISUI4LVSZ5UQ5FA6S3IMDKOJN4NYFBZ/). To connect to Wi-Fi with iwd, enable/start  and then either follow instructions in Iwd to connect to the Wi-Fi or you can also use any of the #Front-ends. In order to have Wi-Fi scanning support from within connman, install  and then restart  after you stop .

## Error /net/connman/technology/wifi: No carrier
You have enabled your Wi-Fi with:

 $ connmanctl enable wifi

If wireless scanning leads to above error, this may be due to an unresolved bug.
If it does not resolve even though wireless preconditions are met, try again after disabling competing network managers and rebooting.

This may also simply be caused by the wireless interface being blocked by rfkill, which can occur after restarting wpa_supplicant. Use  to check.

## "Not registered", or "Method "Connect" with signature ... doesn't exist"
When issuing commands, you may see errors like the following:

From a  prompt:

From the shell:

These errors are produced because the agent is not running. Start the agent from a  prompt with , and try again.

## Error Failed to set hostname/domainname
connman can fail to set hostname or domainname due to lack of .

You will need to edit  (and other like  , etc ...) to modify the  line to add .

See  under  or  for more details.

## Unknown route on connection
A log entry for an unknown route appears each time a connect is done. For example:

 ...
 connmandwlp2s0 {add} route 82.165.8.211 gw 10.20.30.4 scope 0
 connmand[473: wlp2s0 {del} route 82.165.8.211 gw 10.20.30.4 scope 0
 ...

It likely is Connman performing a connectivity check to the ipv4.connman.net host (which resolves to the IP address  at current).See the [https://git.kernel.org/pub/scm/network/connman/connman.git/tree/README#n388 Connman README for more information on why and what - apart from the connecting IP - it transmits.
This behaviour can be prevented by adding the following to :

 EnableOnlineCheck=false

This setting will cause that the default device will not switch to ONLINE, but stay in READY state. However, the connection will still be functional.

The connection itself is also functional (unless behind a captive portal) if the check is blocked by a firewall rule:

 # ip6tables -A OUTPUT -d ipv6.connman.net -j REJECT
 # iptables -A OUTPUT -d ipv4.connman.net,ipv6.connman.net -j REJECT

## File /proc/net/pnp doesn't exist
If you see this in your error log it is caused by bug in connman [https://bbs.archlinux.org/viewtopic.php?id=227689#p1766928 and can be ignored.Bug Report
