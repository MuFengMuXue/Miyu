# Netatalk

Netatalk is a free, open-source implementation of the Apple Filing Protocol (AFP). It allows Unix-like operating systems to serve as file servers for Macintosh computers.

## Installation
Install the  package.

## Configuration
Start/enable .

Besides the configuration files that are installed (and checked during upgrade), netatalk may generate two files  or  which holds the system UUID, and  or  which holds volume UUIDs for TimeMachine. These files may remain after package removal and should be kept in most cases to disambiguate the services broadcast over the local network.

Netatalk 3.x uses a single configuration file, . See  and the following example (make sure processes have write access to ):

## Guest access
In order to allow guest read-only access to your shared folders, add following line to the  section:

To allow guest read/write access, first, allow read-only access as in the previous example and then add following lines to a particular share section:

## iptables
If you use the iptables package for firewall services, consider adding the following (replace  with  as necessary):

## Enable Bonjour/Zeroconf
Bonjour/Zeroconf is now a requirement of netatalk and is compiled by default. No configuration is necessary, netatalk will register its own services using the dbus link. Make sure you set  to the desired string (see  on a Mac for a full list).

You may need to start and enable  if it is not running yet.
