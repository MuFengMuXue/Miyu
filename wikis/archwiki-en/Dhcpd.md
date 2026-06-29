# Dhcpd

dhcpd is the older ISC DHCP server.

## Installation
Install the  package.

## Configuration
Assign a static IPv4 address to the interface you want dhcpd to listen on (here ). The specified subnet should not overlap with that of other interfaces:

 # ip link set up dev eth0
 # ip addr add 139.96.30.100/24 dev eth0 # arbitrary address

The default configuration file  contains many uncommented examples, so relocate it:

 # cp /etc/dhcpd.conf /etc/dhcpd.conf.example

To only listen on the subnet , you may create the following minimal configuration file:

{{hc|/etc/dhcpd.conf|
option domain-name-servers 8.8.8.8, 8.8.4.4;
option subnet-mask 255.255.255.0;
option routers 139.96.30.100;
subnet 139.96.30.0 netmask 255.255.255.0 {
  range 139.96.30.150 139.96.30.250;
}
}}

The options used in this configuration file are:

 which contains addresses of DNS servers supplied to the clients. Here we use Google's public DNS servers. If you have configured your own DNS server on a local machine, specify its address in your subnet (here ).

 and  which define a subnet mask and a list of available routers on the subnet;  also defines the default gateway served to the client. For small networks, you can usually use  as a mask and specify an IP address of the machine on which you are running dhcpd (here ).

 which defines options for separate subnets that are applied to the network interfaces on which dhcpd is listening. Here we have defined the range of available IP addresses for a single subnet  (on a single interface ).

For a complete list of options, consult .

## PXE
Preboot Execution Environment (PXE) configuration is done with the following two options:

 is the IP address of the TFTP server, and  is the image to boot.

This section can either be in an entire , or just in a  definition.

## Usage
dhcpd includes two unit files,  and , which can be used to control the daemon. They start the daemon on all network interfaces for IPv4 and IPv6 respectively.
