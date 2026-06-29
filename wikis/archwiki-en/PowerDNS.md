# PowerDNS

PowerDNS is a DNS server, written in C++ and licensed under the GPL. PowerDNS features a large number of different backends ranging from simple BIND style zonefiles to relational databases and load balancing/failover algorithms.

## Installation
Install the  package.

Next you can review the configuration file located at .

## Backends
To configure PowerDNS to use specific backend you will need to set the  option in configuration file.
Also depending on particular backend you use, you will have to configure it.

For PostgreSQL, MySQL and SQLite you can find database table creation SQL files located at .

## PostgreSQL backend
Firstly you will need to create a user and database where PowerDNS can store data, then import the schema:

 $ psql -U  -d  -a -f /usr/share/doc/powerdns/schema.pgsql.sql

And finally update configuration file to use the backend:

## MySQL backend
Install and run a MySQL server. Create a new user, and a new database and import the schema into the db:

Enable the key for primary zone's outgoing transfer:

 pdnsutil activate-tsig-key example.net example primary

On secondary, import the key:

Enable the key for secondary zone's transfer request:

 [powerdns$ pdnsutil activate-tsig-key example.net example secondary
