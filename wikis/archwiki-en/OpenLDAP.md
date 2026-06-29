# OpenLDAP

OpenLDAP is an open-source implementation of the LDAP protocol. An LDAP server basically is a non-relational database which is optimised for accessing, but not writing, data. It is mainly used as an address book (for example email clients) or authentication backend to various services (such as Samba, where it is used to emulate a domain controller, or Linux system authentication, where it replaces ) and basically holds the user data.

This page is a starting point for a basic OpenLDAP installation and a sanity check.

## Installation
OpenLDAP contains both a LDAP server and client. Install it with the package .

## Configuration
## The server
Slapd, the server, stores its configuration directly inside its database. Thus, we need to write our configuration as an LDIF file and import it.

First, create the directory , where your LDAP database contents ("database 1", as OpenLDAP calls it):

 # install -m 0700 -o ldap -g ldap -d /var/lib/openldap/openldap-data/

Now we need to create a place for the LDAP configuration database ("database 0"):

 # install -m 0760 -o root -g ldap -d /etc/openldap/slapd.d

Create a file  containing the following minimal useful configuration:

There are a few options you will need to change:

* Every occurence of  must be replaced with a valid DN. If you own a domain  you will most likely want to choose .
*  must be replaced by a salted and hashed password, which you may generate by running .

Additionally, you might consider to add further schemas and create additional indexes to tune the performance of your database. The specifics will depend on your use case, but here are a few recommendations. For LDAP authentication, you should include the three schemas below to be able to use the  object class used for storing users.

Allow logins to the  user account with , typically selecting the shell . Then import these settings as the  user:

 slapadd -n 0 -F /etc/openldap/slapd.d/ -l /etc/openldap/config.ldif

Alternatively, you may also run this directly as . However, if you do, make sure  remains accessible by :

 # slapadd -n 0 -F /etc/openldap/slapd.d/ -l /etc/openldap/config.ldif
 # chown -R ldap:ldap /etc/openldap/*

If everything worked, you will now have directories underneath  with names such as .

By default, OpenLDAP will listen unencrypted on all interfaces. To make it only listen on local IP interfaces, you may edit the environment file read by :

Finally, start the slapd daemon by starting .

## The client
The client configuration file is located at .

It is quite simple: you will only have to alter  to reflect the suffix of the server, and  to reflect the address of the server, like:

If you decide to use SSL:

* The protocol (ldap or ldaps) in the  entry has to conform with the slapd configuration
* If you decide to use TLS, add a  line to
* If you use a signed certificate from a CA, add the line  in .

## Create initial entry
Once your client is configured, you probably want to create the root entry, and an entry for the Manager role:

The text after the first line is entered on stdin, or could be read from a file either with the  option or a file redirect.

## Test your new OpenLDAP installation
This is easy, just run the command below:

 $ ldapsearch -x '(objectclass=*)' -b 'dc=example,dc=com'

Or authenticating as the rootdn (replacing  by ), using the example configuration we had above:

 $ ldapsearch -D "cn=Manager,dc=example,dc=com" -W '(objectclass=*)' -b 'dc=example,dc=com'

Now you should see some information about your database.

## OpenLDAP over TLS
If you access the OpenLDAP server over the network and especially if you have sensitive data stored on the server you run the risk of someone sniffing your data which is sent clear-text. The next part will guide you on how to setup an SSL connection between the LDAP server and the client so the data will be sent encrypted.

In order to use TLS, you must have a certificate. For testing purposes, a self-signed certificate will suffice. To learn more about certificates, see OpenSSL.

## Create a self-signed certificate
To create a self-signed certificate, type the following:

 $ openssl req -new -x509 -nodes -out slapdcert.pem -keyout slapdkey.pem -days 365

You will be prompted for information about your LDAP server. Much of the information can be left blank. The most important information is the common name. This must be set to the DNS name of your LDAP server. If your LDAP server's IP address resolves to example.org but its server certificate shows a CN of bad.example.org, LDAP clients will reject the certificate and will be unable to negotiate TLS connections (apparently the results are wholly unpredictable).

Now that the certificate files have been created copy them to  (create this directory if it does not exist) and secure them.  must be world readable because it contains the public key.  on the other hand should only be readable for the ldap user for security reasons:

 # mv slapdcert.pem slapdkey.pem /etc/openldap/ssl/
 # chmod -R 755 /etc/openldap/ssl/
 # chmod 400 /etc/openldap/ssl/slapdkey.pem
 # chmod 444 /etc/openldap/ssl/slapdcert.pem
 # chown ldap /etc/openldap/ssl/slapdkey.pem

## Configure slapd for SSL
Edit the configuration to tell LDAP where the certificate files reside by executing the following command:

If you are using a signed SSL Certificate from a certification authority such as Let’s Encrypt, you will also need to specify the path to the root certificates database and your intermediary certificate. You will also need to change ownership of the .pem files and intermediary directories to make them readable to the user :

SSLv2/v3

Disable SSLv2/v3 and use strong ciphers.

TLSProtocolMin specifies the minimum version in wire format, so "3.3" actually means TLSv1.2.

The TLSCipherSuite specifies a list of OpenSSL ciphers from which slapd will choose when negotiating TLS connections, in decreasing order of preference. In addition to those specific ciphers, you can use any of the wildcards supported by OpenSSL. Note: DEFAULT is a wildcard. See  for description of ciphers, wildcards and options supported.

## Start slapd with SSL
You will have to edit the environment file read by  to change the protocol slapd listens on:

Localhost connections do not need to use SSL. So, if you want to access the server locally you should change the  line to:

 SLAPD_URLS="ldap://127.0.0.1 ldaps:///"

Then restart . If it was enabled before, reenable it now.

## Next steps
You now have a basic LDAP installation. The next step is to design your directory. The design is heavily dependent on what you are using it for. If you are new to LDAP, consider starting with a directory design recommended by the specific client services that will use the directory (PAM, Postfix, etc).

A directory for system authentication is the LDAP authentication article.

A nice web frontend is phpLDAPadmin.

## Backup LDAP
It is imperative that we have a backup of our LDAP database and configuration in case we ever need to restore for any number of reasons.

## Export configuration
 [ldap$ slapcat -vF /etc/openldap/slapd.d -n 0 -l "$(hostname)-ldap-mdb-config-$(date '+%F').ldif"

## Export database
 slapcat -v -n 1 -l "$(hostname)-ldap-database-$(date '+%F').ldif"

## Restore LDAP
## Import configuration
 [ldap$ slapadd -v -n 0 -F /etc/openldap/slapd.d -l ''''

## Import database
 slapadd -v -n 1 -F /etc/openldap/slapd.d -l ''''

## Troubleshooting
## slapd configuration checking
You can check configuration settings with

 $ slaptest -F /etc/openldap/slapd.d/ -v

## Client authentication checking
If you cannot connect to your server for non-secure authentication:

 $ ldapsearch -x -H ldap://ldaservername:389 -D cn=Manager,dc=example,dc=exampledomain

and for TLS secured authentication with:

 $ ldapsearch -x -H ldaps://ldaservername:636 -D cn=Manager,dc=example,dc=exampledomain

## LDAP server stops suddenly
If you notice that slapd seems to start but then stops, try running:

 # chown -R ldap:ldap /var/lib/openldap

to allow slapd write access to its data directory as the user "ldap".

## LDAP server does not start
Try starting the server from the command line with debugging output enabled:

 # slapd -u ldap -g ldap -h ldaps://ldaservername:636 -d Config,Stats
