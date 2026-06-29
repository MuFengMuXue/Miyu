# LDAP authentication

This is a guide on how to configure an Arch Linux installation to authenticate against an LDAP directory. This LDAP directory can be either local (installed on the same computer) or network (e.g. in a lab environment where central authentication is desired).

The guide is divided into two parts. The first part deals with how to setup an OpenLDAP server that hosts the authentication directory. The second part deals with how to setup the NSS and PAM modules that are required for the authentication scheme to work on the client computers. If you just want to configure Arch to authenticate against an already existing LDAP server, you can skip to the second part.

; Terminology

NSS (which stands for Name Service Switch) is a system mechanism to configure different sources for common configuration databases. For example,  is a  type source for the  database.

PAM (which stands for Pluggable Authentication Modules) is a mechanism used by Linux (and most *nixes) to extend its authentication schemes based on different plugins.

So to summarize, we need to configure NSS to use the OpenLDAP server as a source for the ,  and other configuration databases and then configure PAM to use these sources to authenticate its users.

## LDAP server setup
## Installation
Install the OpenLDAP server and configure the server and client. After you have completed that, return here.

## Set up access controls
To make sure that no-one can read the (encrypted) passwords from the LDAP server, but still allowing users to edit some of their own select attributes (such as own password and photo), create the temporary LDIF

{{hc|allowpwchange.ldif|2=
dn: olcDatabase={1}mdb,cn=config
changetype: modify
replace: olcAccess
olcAccess: {0}to attrs=cn,givenName,sn,userPassword,shadowLastChange,mail,loginShell,photo by self write by anonymous auth by dn.base="cn=Manager,dc=example,dc=org" write by * none
olcAccess: {1}to * by self read by dn.base="cn=Manager,dc=example,dc=org" write by * read
}}

Import it on database number 0 (cn=config):

 $ slapmodify -n 0 -l allowpwchange.ldif

Then restart  afterwards.

## Populate LDAP tree with base data
Create a temporary file called  with the following text.

Add it to your OpenLDAP tree:

 $ ldapadd -D "cn=Manager,dc=example,dc=org" -W -f base.ldif

Test to make sure the data was imported:

 $ ldapsearch -x -b 'dc=example,dc=org' '(objectclass=*)'

## Adding users
To manually add a user, create an  file like this:

{{hc|user_joe.ldif|
dn: uid=johndoe,ou=People,dc=example,dc=org
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: shadowAccount
uid: johndoe
cn: John Doe
sn: Doe
givenName: John
title: Guinea Pig
telephoneNumber: +0 000 000 0000
mobile: +0 000 000 0000
postalAddress: AddressLine1$AddressLine2$AddressLine3
userPassword: {CRYPT}xxxxxxxxxx
labeledURI: https://archlinux.org/
loginShell: /bin/bash
uidNumber: 9999
gidNumber: 9999
homeDirectory: /home/johndoe/
description: This is an example user
}}

The  in the  entry should be replaced with the value in  or use the  command. Now add the user:

 $ ldapadd -D "cn=Manager,dc=example,dc=org" -W -f user_joe.ldif

You can add a group similarly with

## Client setup
Install the OpenLDAP client as described in OpenLDAP. Make sure you can query the server with .

Depending on your target, choose either online-only or online and offline authentication.

## Online authentication
## NSS configuration
NSS is a system facility which manages different sources as configuration databases. For example,  is a  type source for the  database, which stores the user accounts.

Install the  package.

Edit  which is the central configuration file for NSS. It tells NSS which sources to use for which system databases. We need to add the  directive to the ,  and  databases, so be sure your file looks like this:

 passwd: files ldap
 group: files ldap
 shadow: files ldap

Edit  and change the  and  lines to fit your ldap server setup.

Edit the  and the  if your LDAP server requires a password. Make sure you change the permission of your  to  for  to start properly.

Start  using systemd.

You now should see your LDAP users when running  on the client.

## PAM configuration
The basic rule of thumb for PAM configuration is to include  wherever  is included. Arch moving to  has helped decrease the amount of edits required. For more details about configuring pam, the Red Hat Documentation is quite good. You might also want the upstream documentation for nss-pam-ldapd.

First edit . This file is included in most of the other files in , so changes here propagate nicely. Updates to  may change this file.

Make  sufficient at the top of each section, except in the session section, where we make it optional. Note the incremented numbers in the  lines too. Refer to  if in doubt.

Then edit both  and  identically. The  file is used when the user runs .

Make  sufficient at the top of each section but below , and add  to  in the auth section.

To enable users to edit their password, edit :

## Create home folders at login
If you want home folders to be created at login (eg: if you are not using NFS to store home folders), edit  and add  to the session section above any "sufficient" items. This will cause home folder creation when logging in at a tty, from ssh, xdm, sddm, gdm, etc. You might choose to edit additional files in the same way, such as  and  to enable it for  and . If you do not want to do this for ssh logins, edit  instead of , etc.

## Enable sudo
To enable sudo from an LDAP user, edit . You will also need to modify sudoers accordingly.

You will also need to add in  the following:

## Online and offline authentication with SSSD
See SSSD for an overview and installation.

## SSSD configuration
If it does not exist create .

The above is an example only. See  for the full details.

Finally set the file permissions  otherwise SSSD will fail to start.

## NSCD configuration
Disable caching for passwd, group and netgroup entries in  as it will interfere with sssd caching.

Keep caching enabled for hosts entries otherwise some services may fail to start.

## NSS configuration
Edit  as follows:

## PAM configuration
The first step is to edit  as follows:

These PAM changes will apply to fresh login. To also allow the  command to authenticate through SSSD, edit :

## Enable sudo
Edit  as follows:

Also add sudo service to the list of enabled services and the search base in :

Alternately, configure sudo to allow the desired LDAP users to use sudo.

## Password management
For changing expired passwords when logging in using  add a password entry to  if it is missing:

Start/enable .

You should now be able to see details of your ldap users with  or .

Once you have logged in with a user the credentials will be cached and you will be able to login using the cached credentials when the ldap server is offline or unavailable.
