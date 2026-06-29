# Snmpd

SNMP is a standard Internet protocol (RFC 1157) designed for the management and monitoring of network devices. Arch Linux offers Net-SNMP, among other  implementations. This article discusses configuration and testing of the  daemon which is part of the  package.

## Installation
There is a single package for  in Arch Linux which contains both the snmpd daemon, and the accompanying utilities.

Install the  package.

## Configuration
## SNMP 1 and 2c
There are three versions of SNMP which are supported by net-snmp: 1, 2c and 3. Versions 1 and 2c start with the same basic configuration, using .

 # mkdir /etc/snmp/
 # echo rocommunity read_only_community_string >> /etc/snmp/snmpd.conf

The above commands will add a community string that can be used for monitoring. Optionally, you can add another community string used for management. This is not recommended unless you have a specific reason to do so.

 # echo rwcommunity read_write_community_string >> /etc/snmp/snmpd.conf

## SNMP 3
SNMP v3 adds security and encrypted authentication/communication. It uses a different configuration scheme in  and additional configuration in .

For the former configuration file in , write directly to it or use the snmpconf wizard:

 # mkdir /etc/snmp/
 # echo rouser read_only_user >> /etc/snmp/snmpd.conf

 $ snmpconf -g basic_setup

For the latter configuration file in , write directly to it or use net-snmp-create-v3-user:

 # mkdir -p /var/net-snmp/
 # echo createUser read_only_user SHA password1 AES password2 > /var/net-snmp/snmpd.conf

 # net-snmp-create-v3-user -ro -a SHA -x AES

Note that once snmpd is (re)started,  will be rewritten, and the clear-text passwords that you have entered will be encrypted.

## Daemon
Start/enable .

## Testing
If using SNMP 1 or 2c, use one of the following commands to test configuration:

 # snmpwalk -v 1 -c read_only_community_string localhost | less
 # snmpwalk -v 2c -c read_only_community_string localhost | less

If using SNMP 3, use the following command to test configuration:

 # snmpwalk -v 3 -u read_only_user -a SHA -A password1 -x AES -X password2 -l authNoPriv localhost | less

Either way, you should see several lines of data looking something like:
