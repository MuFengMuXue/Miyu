# Pi-hole

Pi-hole project is a DNS sinkhole that compiles a blocklist of domains from multiple third-party sources. Pi-hole uses  (a dnsmasq fork) to seamlessly drop any and all requests for domains in its blocklist. Running it effectively deploys network-wide ad-blocking without the need to configure individual clients. The package comes with an optional web administration interface.

## Installation
Install the  package.

## Configuration
## FTL (Faster Than Light)
Pi-hole's FTL is a DNS resolver/forwarder and a database-like wrapper/API that provides long-term storage of requests which users can query through the "long-term data" section of the WebGUI. Data are collected and stored in two places:

# Daily data are stored in RAM and are captured in real-time within
# Historical data (several days/weeks/months) are stored on the file system  and written out at a user-specified interval.

 is statically enabled; re/start it. For FTL configuration, see upstream documentation.

## FTL Integrated Web interface
Pi-hole has a powerful, user-friendly, but completely optional web interface. As well as changing settings, the user can analyse and visualise DNS queries handled by Pi-hole.

## Update hosts file
 ships with an empty  file which is known to prevent Pi-hole from fetching block lists.  One must append the following to this file to ensure correct operation, noting that ip.address.of.pihole should be the actual IP address of the machine running Pi-hole (e.g. 192.168.1.250) and myhostname should be the actual hostname of the machine running Pi-hole:

For more, see Issue#1800.

## Making devices use Pi-hole
To use Pi-hole, devices within the network should use Pi-hole's IP address as their sole DNS server. To accomplish this, there are generally two methods:

# In the router's LAN DHCP settings, set Pi-hole's IP address as the only DNS server available for connected devices.
# Manually configure each device to use Pi-hole's IP address as their only DNS server.

More information about making other devices use Pi-hole can be found at upstream documentation.

## Usage
Change the computer's network settings so the only DNS server in use is .

If using DHCP to lease IP addresses from an external router, append  to  for DNS queries to resolve.

Test DNS queries independently of network-configured nameserver in  using the  command of  package with  .

## Usage
Both standalone and server versions can be controlled via CLI, but only server version can be controlled via web interface.

## Using web interface
Go to pi.hole or  to access web interface.

## Using CLI
## Pi-hole DNS management
By default Pi-hole uses the Google DNS server. Change which DNS servers Pi-hole uses with:

 # pihole-FTL --config dns.upstreams 'Specify multiple DNS servers by separating their addresses with commas.

## Forced update of ad-serving domains list
To update the blocked domain list, execute:

 $ pihole -g

## Temporarily disable Pi-hole
Pi-hole can be paused via CLI by executing:

 $ pihole disable time

Leaving the value for  blank, the disabling will be permanent until later manual reenabling.
 can be expressed in seconds or minutes with syntax  and . For example, to disable Pi-hole for 5 minutes:

 $ pihole disable 5m

At any time, reenable Pi-hole by executing:

 $ pihole enable

## Tips and tricks
## Password-protected web interface
To password-protect the Pi-hole web interface, run the following command and enter the password:

 # pihole setpassword

To disable the password protection, set a blank password.

## Cloudflare DoH
Pi-hole can be configured to use Cloudflared to achieve DNS over HTTPS functionality.

To make Cloudflared work with Pi-hole, simply start cloudflared and configure Pi-hole to use it as its DNS entry.

Using the suggested service file for cloudflared, that would be:

Test that Pi-hole is working with:

 $ drill archlinux.org @127.0.0.1 -p 53

## Optimise for solid state drives
If Pi-hole is running on a solid state drive (SD card, SSD, etc.), it is recommended to change the  value to at least one hour to minimize writes to the database:

## Disable query logging
Both daily and historic data collected by default contain query data that might be considered sensitive.

To disable the query database for historic data, set the privacy level to Anonymous mode in the web administration (Settings > Privacy) or edit the  value in the configuration file:

To also disable the logging for daily data, use the following command:

 # pihole logging off

## Use with VPN server
Pi-hole can be used by connected VPN clients.

## OpenVPN
An OpenVPN server can be configured to advertise a Pi-hole instance to its clients. Add the following two lines to :

 push "redirect-gateway def1 bypass-dhcp"
 push "dhcp-option DNS Pi-hole-IP"

If it still does not work, try creating a file  with the following content:

 interface=tun0

It may be necessary to make  listen on .

## WireGuard
WireGuard clients can be configured to use the Pi-hole DNS server. In the client configuration file, specify the following line:

 DNS = Pi-hole-IP

In order for the DNS to be functional from the VPN, Pi-hole has to listen to all local interfaces:

 # pihole-FTL --config dns.listeningMode LOCAL

See more information in WireGuard#Client configuration.

## Additional blocklists
Pi-hole was intended to block ads, but it can also be used to block other unwanted content:

# Tracking domains
# Malware domains
# Piracy sites
# Fake news sites
# Phishing sites

There are many sources providing these blocklists. Some examples: [https://firebog.net/ firebog.net and oisd.nl.

## Block/Allow domains using regex
To add a wildcard domain to the denylist, use the following pihole command:

 $ pihole --wild yourdomain.com

To block a domain with a custom regex:

 $ pihole --regex '^example\.com$'

To remove the same domain from the denylist, just add  flag to the pihole command:

See also regex tutorial.

## Use Unbound as upstream DNS server
By default, Pi-hole forwards requests to upstream DNS servers, which might lead to privacy concerns.
See upstream documentation for a guide on setting up Unbound locally to resolve DNS requests.

## Troubleshooting
## Odd behavior in the web interface after an upgrade
Some strange/unexplained rendering issues in the web GUI can often be fixed by clearing one's browser cache.

## Data loss on reboot
Systems without a RTC such as some ARM devices will likely experience loss of data in the query log upon rebooting.  When systems lacking a RTC boot, the time is set after the network and resolver come up.  Aspects of Pi-hole can get started before this happens leading to the data loss.  An incorrectly set RTC can also cause problems.  See: Installation guide#Time and System time.

For devices lacking a RTC:
A hacky work-around for this is to use drop-in files against  wherein a delay is built in calling  in a  statement.  Note that the value of "x" in the sleep time depends on how long the specific hardware takes to establish the time sync.

Issue#11008 against systemd-timesyncd is currently preventing the use of the time-sync.target to automate this.

## Failed to start Pi-hole FTLDNS engine
It is possible that  is already using port 53, which is required for .
To resolve this, disable the stub listener by creating a drop-in snippet for systemd-resolved's configuration file:

Then restart  and .

For more information, see .

Alternatively, tell dnsmasq to bind to each interface explicitly, instead of the wildcard , by uncommenting the line  in . This will avoid conflicting with , which listens on .

## DNSMasq package conflict
Since Pi-hole-FTL 4.0, a private fork of dnsmasq is integrated in the FTL sub-project. The original  package is now conflicting with  and will be uninstalled when upgrading from a previous version. It is still possible to use the previous dnsmasq configuration files, just ensure that  in the original  is not commented out.

## Unknown status and changes not being saved
The issue, as seen in , is with systemd-sysusers created user , which is created in expired state. To fix it, run:

 # chage --expiredate -1 http

## Slow loading times
If browsers report "Resolving host" or it just takes longer to load pages than usual, ensure that  looks exactly like this:

If it takes very long to load pages, it can be a problem with  call in pihole script  called through php.  Verify it while loading page with: . Kill it and if the page is displayed, replace  call in pihole script (there is only one) with:

## Prevent DNS resolution issues for other virtual hosts
By default, the DNS service (pihole-FTL) will be bind to the  IP address:

This will prevent any other virtual host onto the same machine hosting the pihole instance (such as docker containers) to get DNS resolution.In order to solve this, you need to create a config file in  with the following content (where  is the IP address of your Pi-hole) :

Then, you need to restart the  to apply changes.

## Interface not up when pihole starts
If after booting domain name resolution does not work, and the journal shows an error message like:

 pihole-FTL [... FATAL ERROR in dnsmasq core: unknown interface wlo1

Then it might be that the interface name is wrong, or the interface is not up when pihole tries to run.

# Check the interface name with . If it is wrong, set  to the correct value in
# If the interface is right, it may not be up when pihole is started (even if the systemd service depends on ). Set  in  to a value greater than 0 (expressed in seconds).

Reboot to verify the issue is fixed.

Reference.

## DNS cache evictions greater than zero
The cache size should be increased when this number is larger than zero. You can set the cache limit at  by uncommenting or adding the following setting with your desired number.

After changes have been performed, restart .

Reference.

## Missing web GUI after upgrade to version 6
After upgrading from version 5 to 6, you may encounter error 404 Site not found when accessing the web GUI. Nevertheless, the web GUI is likely still reachable at port .

Reason: Pi-hole now includes its own web server.

The previous lighttpd server was probably running on port  during the upgrade, thus setting  as the default listening port. Also, if another web server was listening on port  during the upgrade, the Pi-hole web GUI would be unavailable completely. See After resolving the interfering web server, you can reset the web GUI's listening port to  by editing the  key in  section of , or through the new web GUI at Settings > System > turn on Expert mode in the upper right corner > All settings > Webserver and API > webserver.port.
