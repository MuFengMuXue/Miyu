# Tor

The Tor Project (The onion routing) is an open source implementation of onion routing that provides free access to an anonymous proxy network. Its primary goal is to enable online anonymity by protecting against traffic analysis attacks.

Users of the Tor network run an onion proxy software on their machines, which presents a SOCKS interface to its clients. This software connects out to Tor, periodically negotiating a virtual circuit through the Tor network. Tor employs cryptography in a layered manner (hence the 'onion' analogy), ensuring forward secrecy between routers.

Through this process the onion proxy manages networking traffic for end-user anonymity. It keeps a user anonymous by encrypting traffic, sending it through other nodes of the Tor network, and decrypting it at the last node to receive your traffic before forwarding it to the server you specified. One trade off is that using Tor can be considerably slower than a regular direct connection, due to the large amount of traffic re-routing. Additionally, although Tor provides protection against traffic analysis it cannot prevent traffic confirmation at the boundaries of the Tor network (i.e. the traffic entering and exiting the network). See Wikipedia:Tor (anonymity network) for more information.

## Installation
Install the  package to use the Tor Browser, which is the only supported way to browse the web anonymously using Tor.

Users intending to manually use Tor with other software, run relays, or host onion services should install the  package. The majority of this article covers this usage.

Nyx is a command line monitor for Tor, it provides bandwidth usage, connection details and on-the-fly configuration editing. To use it, install the  package.

## Usage
Start/enable . Alternatively, launch it manually as the  user:

 /usr/bin/tor

To use a program over Tor, configure it to use  or  as a SOCKS5 proxy, with port  for plain Tor with standard settings.

The proxy supports remote DNS resolution: use  for DNS resolution from the exit node (instead of  for a local DNS resolution).

To check if Tor is functioning properly, visit https://check.torproject.org/ with Tor Browser or CURL:

 $ curl -x socks5h://localhost:9050 -s https://check.torproject.org

## Configuration
Tor reads its configurations from the file  by default, or if the latter is not found, from . The configuration options are explained in .

Drop-in files are supported by enabling:

To reload the configuration after a change, reload .

## Tor ControlPort
Some programs may require access to your Tor ControlPort to gain low-level control over your Tor node.

The  allows other programs to monitor and modify your Tor node's configuration while it is running, or get details about the status of the Tor network and its circuits.

To enable it, add to your :

 ControlPort 9051

From [https://spec.torproject.org/control-spec/protocol-outline.html The Tor Control Protocol:

: For security, the stream (Tor Control) should not be accessible by untrusted parties.

To enhance security, restrict access to the  using a cookie file, control password, or both.

## Nyx
Assuming the  is set in , you can start  by running:

 $ nyx

To watch Tor connections in nyx add to your :

 DisableDebuggerAttachment 0

## Set a Tor Control cookie file
Add to your :

Restart  to apply the change.

Enabling  restricts access to the  by enforcing file permissions on the Tor cookie file and the Tor data directory.

Add users to the  user group to give them access to the Tor cookie file.

You can use this command to check the permissions:

## Set a Tor Control password
Convert your password from plaintext to hash:

Add the generated hash to your :

 HashedControlPassword your_hash

## Open Tor ControlSocket
If a program requires access to your Tor , such as a Unix domain Socket, add the following to your :

Add the user who will run the program to the  user group.

Restart  and relaunch the program.

To verify the  permissions:

## Testing
To test your , run  with:

 $ echo -e 'PROTOCOLINFO\r\n' | nc 127.0.0.1 9051

To test your , run  with:

 $ echo -e 'PROTOCOLINFO\r\n' | socat - UNIX-CLIENT:/var/lib/tor/control_socket

Both commands should print:

See [https://spec.torproject.org/control-spec/commands.html The Tor Control Protocol for more commands.

## Web browsing
The only way to browse anonymously is with the supported Tor Browser, which uses a patched version of Firefox. It can be installed with the  package and launched from the terminal by the torbrowser-launcher command.

## HTTP proxy
Tor offers a built-in tunneled HTTP proxy and can also be used with an HTTP proxy like Privoxy; however, using the SOCKS5 library is generally recommended.

## Tor
Add following line to your  file to set port  on your  as HTTP proxy:

 HTTPTunnelPort 127.0.0.1:8118

Refer to Tor manual for further information.

## Firefox
The SmartProxy or FoxyProxy add-ons allow you to specify multiple proxies for different URLs or for all your browsing. After restarting Firefox manually set Firefox to port  on , which is where Privoxy are running. These settings can be access under Add > Standard proxy type. Select a proxy label (e.g Tor) and enter the port and host into the HTTP Proxy and SSL Proxy fields. To check if Tor is functioning properly visit the Tor Check website and toggle Tor.

## Privoxy
You can also use this setup in other applications like messaging (e.g. Jabber, IRC clients). Applications that support HTTP proxies you can connect to Privoxy (i.e. ). To use SOCKS proxy directly, you can point your application at Tor (i.e. ). A problem with this method though is that applications doing DNS resolves by themselves may leak information. Consider using Socks4A (e.g. with Privoxy) instead.

## Instant messaging
In order to use an instant messaging client with tor, we do not need an HTTP proxy like privoxy. We will be using tor's daemon directly which listens to port 9050 by default.

## Pidgin
You can set up Pidgin to use Tor globally, or per account. To use Tor globally, go to Tools -> Preferences -> Proxy. To use Tor for specific accounts, go to Accounts > Manage Accounts, select the desired account, click Modify, then go to the Proxy tab. The proxy settings are as follows:

 Proxy type: SOCKS 5
 Host: 127.0.0.1
 Port: 9050

## Pacman
Pacman download operations (repository databases, packages, and public keys) can be done using the Tor network.

Advantages:
* Attackers monitoring your Internet connection and specifically targeting your machine can no longer observe its updates. This makes it difficult for them to deduce which packages you have installed, their versions, or your update frequency. However, they can still learn the software and versions you use by other means, such as watching packets from your HTTP server or probing the machine, which reveals the installed HTTP server and its version.
* If a mirror is not an onion service, a malicious exit relay in your Tor circuit may watch your updates and decide to attack you, but it is unlikely to deanonymize you.
* Attackers trying to prevent your machine from getting security fixes by making it believe there are no new updates will have a harder time, as they cannot target your machine specifically.

Disadvantages:
* Longer update times due to longer latency and lower throughput. This can pose a big security risk if updates need to be applied as quickly as possible, especially on machines directly connected to the Internet. That is the case when there is a major security flaw that is easy to probe and exploit, and attackers have already begun targeting as many systems as they can before those systems are updated.

Reliability with Tor:
* You no longer need a working DNS.
* You depend on the Tor network and the exit nodes not blocking the updates.
* You rely on the Tor daemon to work properly. The Tor daemon may not work if there is insufficient disk space available. "Reserved blocks gid:" in ext4, quotas, or other means can fix that.
* If you are in a country where Tor is blocked, or if there are very few or no Tor users, you should use bridges.

Note on GPG:
On stock Arch, pacman only trust keys which are either signed by you (that can be done with ) or signed by 3 of 5 Arch master keys. If a malicious exit node replaces packages with ones signed by its key, pacman will not let the user install the package.

## Running a Tor relay
The Tor network is reliant on people contributing bandwidth and setting up services. There are several ways to contribute to the network.

A usual Tor circuit consists of:
 Tor User -> Guard Relay -> Middle Relay -> Exit Relay -> Destination (i.e. example.com)

See the official documentation and Expectations for Relay Operators for more information.

## Running a Middle/Guard relay
Also known as non-exit relays: A guard relay is the first hop in a Tor circuit, while a middle relay acts as the second hop.

This means that your machine will act as an entry node or forwarding relay and, unlike a bridge, it will be listed in the public Tor directory. Your IP address will be publicly visible in the Tor directory but the relay will only forward to other relays or Tor exit nodes, not directly to the internet.

To setup a non-exit relay, see and [https://community.torproject.org/relay/setup/post-install/.

## Running a Tor bridge
A Tor bridge is a Tor relay that is not listed in the public Tor directory, thus making it possible for people to connect to the Tor network when governments or ISPs block all public Tor relays. Visit https://bridges.torproject.org/ for more information and instructions on how to get bridge addresses.

To setup a Tor bridge, see and [https://community.torproject.org/relay/setup/post-install/.

## Running a Tor exit relay
Any requests from a Tor user to the regular internet must exit the Tor network at some point, and exit relays provide this essential service. To the destination host, these requests will appear to originate from your machine. This means that running an exit relay is typically viewed as more legally burdensome than running other types of Tor relays.

Before becoming an exit relay, it is strongly recommended to read Legal resources and tips for running an exit node.

To setup an exit relay, see and [https://community.torproject.org/relay/setup/post-install/.

## Configuration
Using the , you can configure which services you wish to allow through your exit relay.

Make the relay an exit relay:

 ExitRelay 1

Allow all traffic:

 ExitPolicy accept *:*

Allow only IRC ports  but nothing else to exit from relay:

 ExitPolicy accept *:6660-6667,reject *:*

By default, Tor will block certain ports. You can use the  to override this, for example accepting NNTP:

 ExitPolicy accept *:119

## +100Mbps Exit Relay configuration example
If you run a fast exit relay (+100Mbps) with  and , the following configuration changes might serve as inspiration to setup Tor alongside iptables firewall and pdnsd as DNS cache. It is important to first read Relay Post-install and good practices.

## Tor
## Raise maximum number of open file descriptors
To handle more than 32768 connections,  can be raised To successfully raise  limit, you may also have to append the following:

Check if the  (filedescriptor) limit is successfully raised with  as the tor user.

## Start tor.service as root to bind Tor to privileged ports
To bind Tor to privileged ports the service must be started as root. Please specify  option in .

## Tor configuration
An example configuration:

See  for details.

Tor opens a socks proxy on port 9050 by default — even if you do not configure one. Set  if you plan to run Tor only as a relay, and not make any local application connections yourself.

 changes logging to stdout, which is also the Tor default.

,  and  enables  to connect to Tor and display connections.

 and  lets Tor listen on port 443 and 80.

 displays [https://gitlab.torproject.org/tpo/core/tor/-/raw/main/contrib/operator-tools/tor-exit-notice.html tor-exit-notice.html on port 80.

 should reflect your public IP and netmask, which can be obtained with the command , so exit connections cannot connect to the host or neighboring machines public IP and circumvent firewalls.

 reduces disk writes and wear on SSD.

 "will attempt to lock all current and future memory pages, so that memory cannot be paged out".

If  returns that your CPU supports AES instructions and  returns that the module is loaded, you can specify  which tries "to use built-in (static) crypto hardware acceleration when available", see https://www.torservers.net/wiki/setup/server#aes-ni_crypto_acceleration.

,  and  require that you start the Tor service as  as described in #Start tor.service as root to bind Tor to privileged ports.

Use the  option to properly reduce Tor’s privileges.

## iptables
Setup and learn to use iptables. Instead of being a Simple stateful firewall where connection tracking would have to track thousands of connections on a tor exit relay this firewall configuration is stateless.

 and  disables connection tracking in the  table.

 is the default  target and drops input traffic we do not specifically .

 is the default  target and only relevant if the host is a normal router, not  when the host is an onion router.

 is the default  target and allows all outgoing connections.

 allow already established incoming TCP connections per the rules below and TCP connections established from the exit node.

 allow all incoming UDP connections because we do not use connection tracking.

 allow ICMP.

 allow incoming connections to the .

 allow incoming connections to the .

 allows all connections on the loopback interface.

## pdnsd
You can use pdnsd to cache DNS queries locally, so the exit relay can resolve DNS faster and the exit relay does not forward all DNS queries to an external DNS recursor.

{{hc|/etc/pdnsd.conf|2=
...
perm_cache=102400                       ## (Default value)*100 = 1MB * 100 = 100MB
...
server {
    label= "resolvconf";
    file = "/etc/pdnsd-resolv.conf";    ## Preferably do not use /etc/resolv.conf
    timeout=4;                          ## Server timeout, this may be much shorter than the global timeout option.
    uptest=query;                       ## Test availability using empty DNS queries.
    query_test_name=".";                ## To be used if remote servers ignore empty queries.
    interval=10m;                       ## Test every 10 minutes.
    purge_cache=off;                    ## Ignore TTL.
    edns_query=yes;                     ## Use EDNS for outgoing queries to allow UDP messages larger than 512 bytes. May cause trouble with some legacy systems.
    preset=off;                         ## Assume server is down before uptest.
 }
...
}}

This configuration stub shows how to cache queries to your normal DNS recursor locally and increase pdnsd cache size to 100MB.

## Uncensored DNS
If your local DNS recursor is in some way censored or interferes with DNS queries, see Alternative DNS services for alternatives and add them in a separate server-section in  as per Pdnsd#DNS servers.

## Ensuring relay is working
To verify the function of your tor relay,
check that  started correctly with the journal or the unit status.
If there are no errors, run  to ensure your relay is making connections.
Do not be concerned if your new relay is slow at first; this is normal.
After approximately 3 hours, your relay should be published and searchable on Relay Search.

## Tor DNS
DNS queries can be performed through the command-line interface by using . For example:

The tor 0.2.x series also provides a built-in DNS forwarder. To enable it, add the following lines to the Tor configuration file and restart the daemon:

This will allow tor to accept DNS requests (listening on port ) like a regular DNS server, and resolve the domain via the Tor network.

A downside of both methods is that they are only able to resolve DNS queries for A, AAAA and PTR records; MX and NS queries are never answered. For more information see this Debian-based introduction.

## Using Tor DNS systemwide
It is possible to configure your system to use Tor DNS for any A, AAAA, and PTR queries your system makes, regardless of whether you eventually use Tor to connect to your final destination. To do this, configure your system to use  as its DNS server and edit the  line in  to show:

 DNSPort 53

Alternatively, you can use a local caching DNS server, such as dnsmasq or pdnsd, which will also compensate for Tor DNS being a little slower than traditional DNS servers. The following instructions will show how to set up dnsmasq for this purpose. Note, if you are using NetworkManager you will need to add your configuration file to the location outlined in NetworkManager#dnsmasq.

Change the tor setting to listen for the DNS request in port  and install .

Modify its configuration file so that it contains:

These configurations set dnsmasq to listen only for requests from the local computer, and to use Tor DNS at its sole upstream provider. It is now necessary to edit  so that your system will query only the dnsmasq server:

Start the .

Finally, if you use dhcpcd you need to change its settings so that it does not alter the  file. Add this line in the configuration file:

If you already have an  line, add  separated by a comma.

## Torsocks
 allows you to use an application through the Tor network without requiring any configuration changes to the application itself. From :

:torsocks is a wrapper between the torsocks library and the application in order to make every Internet communication go through the Tor network.

For a comparison of  with its predecessor, see Usage example:

 $ torsocks elinks checkip.dyndns.org
 $ torsocks wget -qO- https://check.torproject.org/ | grep -i congratulations

## Transparent Torification
In some cases it is more secure and often easier to transparently torify an entire system instead of configuring individual applications to use Tor's socks port, not to mention preventing DNS leaks. Transparent torification can be done with iptables in such a way that all outbound packets are redirected through Tor's TransPort, except the Tor traffic itself. Once in place, applications do not need to be configured to use Tor, though Tor's SOCKSPort will still work. This also works for DNS via Tor's DNSPort, but realize that Tor only supports TCP, thus UDP packets other than DNS cannot be sent through Tor and therefore must be blocked entirely to prevent leaks.

Using iptables to transparently torify a system affords comparatively strong leak protection, but it is not a substitute for virtualized torification applications such as Whonix, or TorVM [https://www.whonix.org/wiki/Comparison_with_Others. Transparent torification also will not protect against fingerprinting attacks on its own, so it is recommended to use an amnesic solution like Tails instead. Applications can still learn your computer's hostname, MAC address, serial number, timezone, etc. and those with root privileges can disable the firewall entirely. In other words, transparent torification with iptables protects against accidental connections and DNS leaks by misconfigured software, it is not sufficient to protect against malware or software with serious security vulnerabilities.

When a transparent proxy is used, it is possible to start a Tor session from the client as well as from the transparent proxy, creating a "Tor over Tor" scenario.
Doing so produces undefined and potentially unsafe behavior. In theory, the user could get six hops instead of three in the Tor network. However, it is not guaranteed that the three additional hops received are different; the user could end up with the same hops, possibly in reverse or mixed order.
The Tor Project opinion is that this is unsafe [https://gitlab.torproject.org/legacy/trac/-/wikis/doc/TorifyHOWTO#tor-over-tor.

To enable transparent torification, use the following file for  and  (internally used by systemd's  and ).

This file also works for , so you may symlink it:

 # ln -s /etc/iptables/iptables.rules /etc/iptables/ip6tables.rules

Then make sure Tor is running, and start/enable the  and  systemd units.

You may want to add  and  to whatever systemd unit logs your user in (most likely a display manager), to prevent any user processes from being started before the firewall up. See systemd.

## Tips and tricks
## Kernel capabilities
To run tor as a non-root user and use a port lower than , you can use kernel capabilities to allow it to bind to privileged ports:

 # setcap CAP_NET_BIND_SERVICE=+eip /usr/bin/tor

If you use , it is also possible to use systemd to grant tor the appropriate permissions. This has the benefit that permissions do not need to be reapplied after every tor upgrade:

Refer to superuser.com for further explanations.

## Using system tor in Tor Browser
When using the Tor Browser, it is possible to use the running  instead of establishing a second connection to the Tor network.
Instructions are provided in the starter file for the browser, which by default is located at .

As of version , you can follow these steps:
# In , look for the option  and copy down the address and port there. If no address is given, it is  by default, and if not port is given it is  by default.
# Follow the steps in #Tor ControlPort and #Set a Tor Control password, and copy down both the password and control port you have set.
# In the Tor Browser, navigate to  and set the following preferences:
# Edit the start file of the Tor Browser, which by default is . Replace  with the control password in the following line: {{bc|1=setControlPortPasswd ${TOR_CONTROL_PASSWD:='"secret"'}}}
# Restart the Tor Browser. If successful, there should be a message on the startup page explaining that the connection is not managed by the Tor Browser, and  should log a line saying .

## Running Tor in a chroot
For security purposes, it may be desirable to run Tor in a chroot. The following script will create an appropriate chroot in :

{{hc|~/torchroot-setup.sh|2=
#!/bin/sh
export TORCHROOT=/opt/torchroot

mkdir -p $TORCHROOT
mkdir -p $TORCHROOT/etc/tor
mkdir -p $TORCHROOT/dev
mkdir -p $TORCHROOT/usr/bin
mkdir -p $TORCHROOT/usr/lib
mkdir -p $TORCHROOT/usr/share/tor
mkdir -p $TORCHROOT/var/lib
mkdir -p $TORCHROOT/var/log/tor/

ln -s /usr/lib  $TORCHROOT/lib
cp /etc/hosts           $TORCHROOT/etc/
cp /etc/host.conf       $TORCHROOT/etc/
cp /etc/localtime       $TORCHROOT/etc/
cp /etc/nsswitch.conf   $TORCHROOT/etc/
cp /etc/resolv.conf     $TORCHROOT/etc/

cp /usr/bin/tor         $TORCHROOT/usr/bin/
cp /usr/share/tor/geoip* $TORCHROOT/usr/share/tor/
cp /lib/libnss* /lib/libnsl* /lib/ld-linux-*.so* /lib/libresolv* /lib/libgcc_s.so* $TORCHROOT/usr/lib/
cp $(ldd /usr/bin/tor | awk '{print $3}'|grep --color=never "^/") $TORCHROOT/usr/lib/

### /var/log/tor/notices.log is only needed if you run hidden services
# cp /var/log/tor/notices.log $TORCHROOT/var/log/tor/

cp -r /var/lib/tor      $TORCHROOT/var/lib/
cp /etc/tor/torrc       $TORCHROOT/etc/tor/

chown tor:tor $TORCHROOT
chmod 700 $TORCHROOT
chown -R tor:tor $TORCHROOT/var/lib/tor
chown -R tor:tor $TORCHROOT/var/log/tor

sh -c "grep --color=never ^tor /etc/passwd > $TORCHROOT/etc/passwd"
sh -c "grep --color=never ^tor /etc/group > $TORCHROOT/etc/group"

mknod -m 644 $TORCHROOT/dev/random c 1 8
mknod -m 644 $TORCHROOT/dev/urandom c 1 9
mknod -m 666 $TORCHROOT/dev/null c 1 3

if [ "$(uname -m)" = "x86_64" ]; then
  cp /usr/lib/ld-linux-x86-64.so* $TORCHROOT/usr/lib/.
  ln -sr /usr/lib64 $TORCHROOT/lib64
  ln -s $TORCHROOT/usr/lib ${TORCHROOT}/usr/lib64
fi

}}

After running the script as root, Tor can be launched in the chroot with the command:

 # chroot --userspec=tor:tor /opt/torchroot /usr/bin/tor

or, if you use systemd, overload the service:

## Running Tor in a systemd-nspawn container with a virtual network interface
In this example we will create a systemd-nspawn container named  with a virtual macvlan network interface.

See systemd-nspawn and systemd-networkd for full documentation.

## Host installation and configuration
In this example the container will reside in :

 # mkdir -p /srv/container/tor-exit

Install the .

Install ,  and  as per systemd-nspawn#Create and boot a minimal Arch Linux container:

 # pacstrap -K -ci /srv/container/tor-exit base tor nyx

Symlink to register the container on the host, as per systemd-nspawn#Management:

 # ln -s /srv/container/tor-exit/ /var/lib/machines/

## Virtual network interface
Create a drop-in configuration file for the container:

 creates a "macvlan" interface named  and assigns it to the container, see systemd-nspawn#Use a "macvlan" or "ipvlan" interface for details. This is advisable for security as it will allow you to give a private IP to the container, and it will not know what your machine's IP is. This can help obscure DNS requests.

 per #Raise maximum number of open file descriptors.

Set up systemd-networkd according to your network in .

## Start and enable systemd-nspawn
Start/enable .

## Container configuration
Login to the container (see systemd-nspawn#machinectl):

 # machinectl shell root@tor-exit

## Start and enable systemd-networkd
Start and enable .  displays if  is correctly configured.

## Configure Tor
See #Running a Tor relay.

## Java
One can ensure a java application proxies its connections through Tor by defining its environment variable:

 JAVA_OPTIONS="$JAVA_OPTIONS -DsocksProxyHost=localhost -DsocksProxyPort=9050"

## Troubleshooting
## Tor Browser proxy problems
Tor Browser typically works without significant customization. If the bundled proxy fails with  for any website, consider reinstallation by removing the  directory (make sure to back up important files).
