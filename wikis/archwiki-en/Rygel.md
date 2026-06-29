# Rygel

Rygel is a streaming media server compatible with many DLNA/UPnP clients including the Sony PlayStation, Microsoft Xbox, smart televisions, DLNA speakers and many smartphones. Rygel will automatically transcode media to a format compatible with the client device. It can also utilise published media hierarchies from external applications like Rhythmbox and DVB Daemon through the D-Bus MediaServer specification. It is under active development and is a part of the GNOME project.

## Installation
Install the  package.

## Starting
On a GNOME environment, go to Settings > Sharing > Media Sharing, then turn Media Sharing on. In Folders add or exclude the folders you want to share or not, and in Networks select in which network should the media be shared.

On non-GNOME environments, the  user unit can be enabled to have it start automatically.

To start  manually, any user can run in a terminal:

 $ rygel -g 5

## Configuration
Rygel can be configured globally () or per-user (). The default  is well documented. The command  generates the  and allows some basic configuration.

More information on these and other configuration options can be found with .

If you use  behind a firewall (nftables,  iptables, etc.), add a rule to allow the connection to the listening port (see By default,  assigns a port dynamically which may change from one session to another if the   sets . To control the listening port (here 50000), start  as follows:

 $ rygel -g -p 50000

## Troubleshooting
When starting Rygel from the command line, there are several options that might help you troubleshoot any strange behaviour. Find out more about these options with .
