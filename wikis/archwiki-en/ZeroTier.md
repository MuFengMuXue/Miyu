# ZeroTier

ZeroTier is a cross-platform and easy to use virtual LAN / Hamachi alternative, also available on Android, iOS, Mac, and Windows.
A GUI is only available on Mac and Windows according to the developers.

## Installation
Install the  package.

## Configuration
You will need to create an account over at My ZeroTier and create a network and select your desired options, such as support for IPv4 or IPv6 or both. Keep note of the network ID of the newly-created network as you will be needing it later on.

Leave the page for the network that you will use open, as you will need to authorize each computer or device that you connect, and also verify that they get an IP.

To begin start , if one would like it to start at boot enable . To find out your computer id, which will be a 10-digit hexadecimal number similar to 89e92ceee5, run:

where 89e92ceee5 is address and 1.2.4 is the version, followed by its status.

Next you will need to join a network:

 # zerotier-cli join network_id

The network ID is a 16-digit hexadecimal number like 8056c2e21c000001 which you can get on the Networks page.

Back on the network page at my.zerotier, scroll down to the Members section where you should see all addresses that have joined. To authorize each computer or device, check the left-most checkbox and verify that it is given an IP address (this may take 10 or 20 seconds). You may need to run dhcpcd to acquire the new IP address locally.

To verify that all devices can see each other you can ping each address using its associated IP, like so:

One can also see connected peers by running:

and see a list of networks the computer is connected to by running:

 # zerotier-cli listnetworks

## Manual configuration
Manual configuration can be achieved by creating the file  in the program's home directory . This allows you to set various configuration options, such as restricting the service to specific interfaces, or enforcing use of a different port. This file must be valid JSON as it can be re-written by zerotier-one. Below is an example  which stops zerotier-one using docker and bridged interfaces:

{{hc|local.conf|
{
    "settings": {
        "interfacePrefixBlacklist": [ "docker", "br-" ]
    }
}
}}

More information on the available configuration items is available on the program's GitHub repository.

## Troubleshooting
## Devices in virtual network not reachable
Check the unit status of . If you see following error, the TUN/TAP kernel module is probably not loaded:

 ERROR: unable to configure virtual network port: could not open TUN/TAP device: No such file or directory

A reboot should resolve the issue.
