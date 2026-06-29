# PeerGuardian Linux

PeerGuardian Linux (pgl) is a privacy oriented firewall application.  It blocks connections to and from hosts specified in huge block lists (thousands or millions of IP ranges). pgl is based on the Linux kernel netfilter framework and iptables.

A more native, efficient solution to achieve the same end is to use the ipset kernel module in conjunction with the pg2ipset tool and the ipset-update script.

## Installation
There are two possible packages to install:  includes only the daemon and CLI tools, while  comes complete with a GUI (written using Qt).

## Configuration
*  contains a list of URL for retrieving the various block lists.
* , empty by default, overrides the default settings present in .
*  lists custom IP ranges that will not be filtered.

The default lists in  block many potentially legitimate IP address.  Users are encouraged to exercise best judgment and the information available at I-Blocklist.

It is recommended to disable the filtering of HTTP connections by adding the following to :

Conversely, one could white list all the ports except the ones used by the program to be blocked. The following example only use the block lists to stop incoming traffic on ports 53 (DNS) and 80 (HTTP):

## Server
systemd initialization of the system means that it is quite possible for a server to be briefly unprotected, prior to pgl launch. To ensure adequate protection, extend the unit  with the following:

## LAN
By default, pgl blocks traffic on the local IPv4 addresses. To disable this behavior, edit  to add an exception using the WHITE_IP_* setting:

For further information, please refer to the  section of .

## Starting up
Once comfortable with the configuration of both the daemon and lists, start the  service. To make sure that pgl works as intended, issue this command:

 # pglcmd test

To start pgl automatically at boot, enable the  service.

## Running pgl from within a container
Users running pgl within a Linux Container may need to edit the included  to add the loading of key modules needed by pgl.
