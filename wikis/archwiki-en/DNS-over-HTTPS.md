# DNS-over-HTTPS

DNS-over-HTTPS is an implementation of DNS over HTTPS. It can act as a stub resolver.

## Installation
Install the  package.

## Client startup
## Disable any services bound to port 53
To see if any programs are using port 53, run:

 $ ss -lp 'sport = :domain'

If the output contains more than the first line of column names, you need to disable whatever service is using port 53. You are ready to proceed once the above command outputs nothing more than the following line:

 Netid State   Recv-Q  Send-Q   Local Address:Port     Peer Address:Port Process

## Change system DNS server
Change your system's DNS server to an address in the  section of the configuration file. If you don't know what you're doing,  is recommended.

This can be accomplished either through your Network Manager or through editing :/etc/resolv.conf.

## Startup
Start or enable .

## Test configuration
To test if your system's DNS works, type  into the command line. Note that this will work before DNS-over-HTTPS is configured, assuming you had a DNS configuration before installing this.

## Client configuration
The client configuration file is  by default

## Select preferred upstream DNS server
To select a preferred DNS server, uncomment one of the profiles.

If your preferred server is not listed, you may use the following template in the  section.

## Troubleshooting
## Service does not start properly in wired connection
As explained by the developer:
:ArchLinux doesn’t come with a default network management framework, thus systemd comes without online detection pre-configured.
:If you are on Wi-Fi, I suggest making sure systemd’s online detection can function properly. I believe your system have already installed some network management framework such as NetworkManager to help you manage Wi-Fi passwords.
:Or, if you are on wired network, simply modifying the .service file to disable online detection would be the easiest solution. Installing NetworkManager for a non-mobile machine might be against the K.I.S.S. principle, and we don’t want it.

Upstream suggests to use a drop-in snippet to your service file to:
