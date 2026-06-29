# Tiny Tiny RSS

Tiny Tiny RSS is an open source web-based news feed (RSS/Atom) aggregator, designed to allow you to read news from any location, while feeling as close to a real desktop application as possible.

## Installation
Install the  and  packages.

tt-rss is installed into . You will need to make this directory available from your web server. The simplest way is to do:

* With Apache HTTP Server :
:

* With Nginx :
:

## Configuration
## Set up PHP and database
You will need to set up a database using PostgreSQL.

Create a ttrss user and database in PostgreSQL. For example:

 createuser --createdb ttrss
 [postgres$ createdb -U ttrss ttrss

In , enable the following modules:

 extension=curl
 extension=iconv
 extension=intl
 extension=pdo_pgsql ; for PostgreSQL
 extension=pgsql ; for legacy PostgreSQL plugins (still required by default)
 extension=soap

If  is set in  (it is not by default), add  to it.

Application initialization can be done either automatically or manually.

Automatic way:

* remove default configuration file , without this file tt-rss webapp enters installation wizard.
* navigate to (your-servers-root)/tt-rss/ and proceed with the installer.
* save generated configuration file to .

Manual way:

* edit tt-rss configuration file  and update database settings.
* re-create database from :

 $ psql ttrss -U ttrss -f /usr/share/webapps/tt-rss/sql/pgsql/schema.sql

At the end the  file will look like this:

 —however, simply enabling the  service should suffice. Check the service's unit status to verify that it is running fine.

## Troubleshooting
## Integrity constraint violation: 1062 Duplicate entry '1' for key 'ttrss_feeds_feed_url_owner_uid_key'
If you update tt-rss database to schema 137 you might see the error Duplicate entry '1' for key 'ttrss_feeds_feed_url_owner_uid_key. To fix the issue please start database shell, e.g.:
 $ psql -U ttrss tt-rss

And then run query from official forum that drops duplicated database entries.

## PHP UConverter class is missing, it's provided by the Internationalization (intl) module.
If you see this error after upgrading tt-rss, add  to  and restart the  service.

## Unable to install plugins (PI_ERR_NO_WORKDIR)
If you cannot install plugins due to a  error, then this is because in older packages, non-writable  was used by the application server. Please upgrade the system to fix it.
