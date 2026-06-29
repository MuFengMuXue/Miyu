# Tinc

tinc is a Virtual Private Network (VPN) daemon that uses tunnelling and encryption to create a secure private network between hosts on the Internet.

## Installation
Install the  package.

## Configuring a private network
In this example, we will create a virtual private network vpnname between two hosts alpha and beta, where the former is the entry point for the latter, so that beta tries to connect to alpha on startup.

For each virtual private network you have to create a separate directory .

You can also start by copying the sample configuration
 # cp -r /usr/share/tinc/examples/* /etc/tinc/vpnname

In /etc/tinc/vpnname/tinc.conf you specify the name of the hostmachine (which can differ from the actual hostname of the system) and the location of the tun/tap device.

## Configuration of alpha
 and  need to be made executable.

## Configuration of beta
 and  need to be made executable.

## Setting up the hosts
The configuration files for the different hosts are stored in /etc/tinc/vpnname/hosts/ directory. In this example we need the two files on each machine.

After creating a file for each host, you have to generate a key pair using
 # tincd -n vpnname -K
which creates the private key in /etc/tinc/vpnname/tinc.rsa_key.priv and the public key in the corresponding host-file.

In the last step you need to exchange the host configuration files, so that you have both alpha and beta in /etc/tinc/vpnname/hosts/ on each host.

## Starting a private network
After having created the appropriate configuration in , you can test the new private network with:

 # tincd -n vpnname

If you want it at startup, you can enable .

## Using TAP devices and bridges
Sometimes it is reasonable to use TAP devices instead of TUN devices. For example if you want to add the tinc device to an already existing bridge. Just add the "Mode" option to your tinc.conf.

Remember to do that on every host.

Possible tinc-up/down files could look like that:

And finally restart your tinc daemon: .

## Automatically Starting Tinc at boot
Tinc can be configured to automatically start at boot time using systemd units.

If you want to be able to start, stop or reload all of your networks at once, you have to enable

Then for each network that you want to automatically start, enable it individually (e.g. , , etc...)

## Troubleshooting
## I have updated my system and now tinc will not start.
In case of a linux kernel update you have to either restart your system or reinstall the running kernel package.

## I'm running a custom kernel and tinc will not start.
Make sure you have TUN/TAP support enabled.
