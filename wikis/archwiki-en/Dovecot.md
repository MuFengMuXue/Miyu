# Dovecot

Dovecot is an open source IMAP and POP3 server for Linux/UNIX-like systems, written primarily with security in mind. Dovecot primarily aims to be a lightweight, fast and easy to set up open source mailserver.  For more detailed information, please see the official Dovecot documentation.

This article describes how to set up Dovecot for personal or small office use.

Due to breaking changes in Dovecot's configuration format in version 2.4, Arch Linux offers both the latest release and one from the 2.3 line. The latter will not receive any new features or bug fixes, other than critical security updates.

## Installation
Install the  package for the most recent Dovecot version, or  for the legacy 2.3 line.

## Configuration
Dovecot configuration is stored in .
An example file is shipped with the package. To use the example config a few manual steps are still necessary:
* A  user and group needs to be created
* SSL certificate is necessary or needs to be created

See the official documentation TLDR and SSL and Plaintext Authentication for more information.

On top of that, the developers translated legacy examples to 2.4 syntax
and offer them on GitHub.
The examples are provided in hope they are helpful, but the archive is not
expected to be kept up to date.

## Required settings
 must be set and it has to be the first
setting in the configuration file.  also has
to be set. The values of these settings should match actually used
configuration syntax, names, and formats of files created by Dovecot itself.

## Authentication
User authentication is managed through the  filters.

To enable PAM passdb driver:

{{bc|1=
passdb pam {
    # Additional PAM-specific settings here, if needed.
}
}}

The associated PAM configuration is included in .

See passdb documentation for other drivers and the list of their settings.

## TLS connections
To accept TLS connections, you need to obtain a certificate. This section
assumes you already own one, together with the private key. Both must be
in the PEM format.

First, generate parameters required for Diffie-Hellman key exchange:

 $ openssl dhparam -out dhparams.pem 4096

This operation may take some time. The output goes to .

Finally, configure Dovecot to use all three files:

{{bc|1=
ssl_server {
    cert_file = /path/to/fullchain.pem
    key_file = /path/to/privkey.pem
    dh_file = /path/to/dhparams.pem
}
}}

## Full Text Search
By default Dovecot does not index the full message content, which will result in slow response times for  queries for bigger mailboxes. There are a number of FTS backends Dovecot can be hooked up to.

Dovecot needs a plugin for the chosen search backend. The  plugin is included in  but solr itself is not the easiest to set up. There are packages for Xapian () and Elasticsearch ().

## Starting the server
Start/enable .

## Tips and tricks
Generate hashes with non-default hash functions:

 $ doveadm pw -s SHA512-CRYPT -p "password"

Ensure that the column in the database is large enough. A warning will be emitted if it is too small.

Remember to set the password password scheme:

## Troubleshooting
## warning: pipe flag `D' requires dovecot_destination_recipient_limit = 1
If you cannot receive emails with multiple recipients and there is something like this is your logs:

 mail postfix/pipe72A62733: to=, relay=dovecot, delay=495, delays=495/0.01/0/0.08, dsn=4.3.5, status=deferred (mail system configuration error)
 mail postfix/pipe[663: 72A62733: to=, relay=dovecot, delay=495, delays=495/0.01/0/0.06, dsn=4.3.5, status=deferred (mail system configuration error)
 mail postfix/pipe1614231: warning: pipe flag `D' requires dovecot_destination_recipient_limit = 1

Add  to  and reload postfix.

## dovecot.service does not start after updating to 2.4
Dovecot 2.4 has introduced changes to the configuration files format and variable names. You need to translate your 2.3 configuration to make it compatible with 2.4. See #Configuration for more information.

As a temporary solution  may be installed instead of .

## Dovecot and Postfix: cannot read SSL private key
If running dovecot 2.4 you encounter errors when running "any" dovecot executable as user, such as:

 Fatal: Error in configuration file /etc/dovecot/dovecot.conf line 80: cert_file: open(/etc/letsencrypt/live/server.tld/fullchain.pem) failed: Permission denied

This is a known issue, since "deliver" has to be able to read every configuration. But running  as user is useful, with procmail for instance.

To avoid the problem, dovecot provides a silently failing "include_try" mechanism, that you can use to make file unreadable to user but still enabling root to read SSL keys.

1. Create  that contains the content of {{ic|ssl_server {...}}} (above defined), something like:

 cert_file = /path/to/fullchain.pem
 key_file = /path/to/privkey.pem
 dh_file = /path/to/dhparams.pem

2. Prevent any user but "root" to read this file:

 chmod 600 /etc/dovecot/dovecot-ssl.conf

3. Replace the ssl_server part of  with this:

 ssl_server {
    !include_try /etc/dovecot/dovecot-ssl.conf
 }

4. (to test) The  command should print your "certs_file" lines as root (with your private keys listed) and not be listed as unprivileged user.
