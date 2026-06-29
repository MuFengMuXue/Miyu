# OpenDJ

OpenDJ is an LDAPv3 compliant open source directory service, which has been developed for the Java platform, providing a high performance, highly available, and secure store for managing identities.

It is an alternative to OpenLDAP.

## Installation
 package contains LDAP server and many LDAP related utilities such as  which is also provided by OpenLDAP.

## Configuration
You can start/enable .

## Upgrade
After installing newer  version, you will need to upgrade its database by executing:

 # /usr/share/opendj/upgrade

## Troubleshooting
OpenDJ server log files are located in .

Specifically take a look at  and  files.

You can also check the unit status of .

## Tips
You can use Control Panel for some configuration:

 # OPENDJ_JAVA_ARGS="-Xmx2048m" opendj-control-panel
