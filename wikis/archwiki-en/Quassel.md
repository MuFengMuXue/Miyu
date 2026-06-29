# Quassel

Quassel (sometimes referred to as Quassel IRC) is a cross-platform IRC client introduced in 2008. It is dual-licensed under GPLv2 and GPLv3, while most graphical data is licensed under the LGPL and provided by the Oxygen Team. The Quassel client uses the Qt framework for its user interface.

Quassel is split up into two parts by a server-client model; a client and a core. There is also a monolithic version of the official client that does not require a core. The core(server) is the application that actually does the communication with IRC networks, while the client(s) only communicates with the core. This gives the user a flexibility of having the same instance to IRC networks on different clients (e.g. mobile, desktop) at the same time.

## Installation
## Basic usage
Just install the  (or  if you are not on KDE or you want to install fewer dependencies) package if you only want to use Quassel from a single computer (e.g. for quickly asking for support on Arch IRC channels).

## Configuration
## Setting up a bouncer (Quassel core) to be permanently online
Install  on the server and  (or ) on your desktop.

Obtain a TLS certificate. Concatenate both the private key and the certificate into :

 # cat private_key.pem certificate.pem > /var/lib/quassel/quasselCert.pem
 # chown quassel:quassel /var/lib/quassel/quasselCert.pem

Open TCP port  in your firewall.

Start core by starting .

Start the client and connect to core:

 $ quasselclient

Accept your self-created certificate.

Now set up your IRC-servers and IRC-nicknames on the core.

If you choose to use PostgreSQL as backend you will need to create a database and user for quasselcore.

 psql -c "CREATE USER quassel WITH PASSWORD myPassword;"
 [postgres$ psql -c "CREATE DATABASE quassel WITH OWNER quassel ENCODING 'UTF8';"

See also PostgreSQL instruction on Quassel wiki.

Once it all works, you can enable  to start automatically on system boot.

## Setting up multiple clients to connect through the same core
If you want additional users to be able to use the same core, run as the quassel user:

 quasselcore --configdir=/var/lib/quassel --add-user

It will then prompt you for a new account's username and password.

## Spell checking
For spell checking, make sure hunspell and a language dictionary for it are installed. Enable it by selecting the check-boxes in Settings > Configure Quassel... > Spell Checking and restarting your client.

## Tips and tricks
## Viewing logs
In addition to the tools listed in the [https://bugs.quassel-irc.org/projects/quassel-irc/wiki/Quassel_Logging Quassel wiki,  allows searching through the database.

## Waiting until the network is up to start
By default,  is only depending on . To wait until the network is up, edit the unit to use network-online.target instead:
