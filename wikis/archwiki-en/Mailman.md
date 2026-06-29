# Mailman

Mailman is a mailing list management system. It is used in conjunction with a mail server.

## Installation
Install the  package.

Mailman can be used in conjunction with Postorius (for configuration) and Hyperkitty (for archiving).

## Configuration
All configuration for Mailman takes place in . The schema explaining all possible configuration options and setting the defaults is stored in .

The configuration is also accessible via the command line. Run the following command as the  user (e.g. using sudo or su):

 mailman conf

## Database
Mailman by default uses an SQLite [https://mailman.readthedocs.io/en/latest/src/mailman/docs/database.html database in , but can be configured to use MariaDB or PostgreSQL.

## SQLite
The default location for the SQLite database is already reflected in the  and therefore does not have to be set in Mailman's configuration.

## MariaDB
Install the  package and configure a database on MariaDB.

## PostgreSQL
Install the  package and create a database using PostgreSQL.

## REST API
Mailman exposes its REST API based on the settings in the  section of the configuration. Make sure to replace the default values for  and  (do not use the example values below).

## ARC
By default DMARC and DKIM are disabled. The configuration takes place in the  section of the configuration file. Make sure to set necessary values and read the documentation about the defaults.

## MTA
To connect a mail-transfer-agent (MTA), it is necessary to configure the  section in the configuration file. Upstream documentation covers examples for postfix, exim and sendmail, but other MTAs are technically possible.

## Postfix
To connect to a local postfix instance the following configuration section can be used:

The postfix configuration has to be extended to ensure compatibility (see upstream notes).

Additionally, postfix needs to be made aware of mailman's transport maps. Depending on the postfix configuration these may look similar to the following.

If  is not directly accessible by mailman for creating the default hash-based alias maps, it is possible to generate regular expression based alias maps instead.
To overwrite the default Python-class based configuration, mailman allows the use of a configuration file. Create the following file:

Add the file to the  section in mailman's configuration file.

Afterwards the  based exports can then be used in the postfix configuration.

To connect to a local postfix instance with a virtual mail setup, first set an alias domain. Afterwards alter the respective configuration.

## Running
Enable and start .

Several systemd services with timers exist, taking care of various aspects of the list management:

* : for sending out daily digests to subscribers
* : for hourly polling of NNTP servers for news
* : for sending out daily notifications to admins about pending requests

## Setup
## Integrate with a mail server
## Integrate with Hyperkitty
Mailman does not automatically archive mails on its own. The Hyperkitty web application is used for this purpose. Based on a plugin, mailman is able to send mails to a Hyperkitty instance for archival.

Install the  package and configure .

Afterwards, make mailman aware of the plugin:

## Tips and tricks
## Migrate from mailman < 3.0
Mailman offers the possibility of importing mailman < 3.0 based list databases (). Run the following command as the  user (e.g. using sudo or su):

 mailman import21 LISTSPEC PICKLE_FILE

Here,  represents a fully-qualified name of a list to import (e.g. ) and  the path to the list's  file.

## REST API
Mailman exposes a [https://mailman.readthedocs.io/en/latest/src/mailman/rest/docs/rest.html#the-rest-server REST API, which can be interfaced using custom tooling, based on .
