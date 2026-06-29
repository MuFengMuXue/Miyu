# PostgreSQL

PostgreSQL is an open source, community driven, standard compliant object-relational database system.

## Installation
Install the  package. It will also create a system user called postgres.

You can now switch to the postgres user using a privilege elevation program.

## Initial configuration
Before PostgreSQL can function correctly, the database cluster must be initialized:

 initdb -D /var/lib/postgres/data

Where  is the default location where the database cluster must be stored (see #Change default data directory if you want to use a different one).  accepts a number of extra arguments:

* By default, the [https://www.postgresql.org/docs/current/static/locale.html locale and the encoding for the database cluster are derived from your current environment (using $LANG value). If this is not what you want, you can override the defaults using  (where locale is to be chosen amongst the system's available locales) and  (which must match the chosen locale). (Once the database is up, you can check which values were used with .)
* If your data directory resides on a file system without data checksumming, you may wish to enable PostgreSQL's built-in checksumming for increased integrity guarantees - add the  argument to do so. Read #Enable data checksumming for more information. (Once the database is up, you can check if it is enabled with .)
:
* The trust authentication method is used by default, meaning that anyone on the host can connect as any database user. You can use  for safer authentication methods.
* The / option can be used to set any  parameter avoiding the need to manually edit .
* For more options, see  and official documentation.

Example:

 initdb --locale=C.UTF-8 --encoding=UTF8 -D /var/lib/postgres/data --data-checksums

Many lines should now appear on the screen with several ending by :

If these are the kind of lines you see, then the process succeeded. Return to the regular user using .

Finally, start and enable the .

## Create your first database/user
Become the postgres user. Add a new database role/user using the [https://www.postgresql.org/docs/current/static/app-createuser.html createuser command:

 createuser --interactive

Create a new database over which the above user has read/write privileges using the [https://www.postgresql.org/docs/current/static/app-createdb.html createdb command (execute this command from your login shell if the database user has the same name as your Linux user, otherwise add  to the following command):

 $ createdb myDatabaseName

## Familiarize with PostgreSQL
## Access the database shell
Become the postgres user. Start the primary database shell, psql, where you can do all your creation of databases/tables, deletion, set permissions, and run raw SQL commands. Use the  option to connect to the database you created (without specifying a database,  will try to access a database that matches your username).

 psql -d myDatabaseName

Some helpful commands:

Get help:

 => \help

List all databases:

 => \l

Connect to a particular database:

 => \c database

List all users and their permission levels:

 => \du

Show summary information about all tables in the current database:

 => \dt

Exit/quit the  shell:

 => \q

or press .

There are of course many more meta-commands, but these should help you get started. To see all meta-commands run:

 => \?

## Optional configuration
The PostgreSQL database server configuration file is . This file is located in the data directory of the server, typically . This folder also houses the other main configuration files, including the  which defines authentication settings, for both local users and other hosts ones.

## Restricts access rights to the database superuser by default
The defaults  allow any local user to connect as any database user, including the database superuser.
This is likely not what you want, so in order to restrict global access to the postgres user, change the following line:

To:

You might later add additional lines depending on your needs or software ones.

## Require password for login
Edit  and set the authentication method for each user (or  to affect all users) to :

Restart , and then re-add each user's password using .

## Configure PostgreSQL to be accessible exclusively through UNIX Sockets
When initially creating the cluster, append  to the initdb command.

For an existing cluster, edit  and in the connections and authentication section set:

This will disable network listening completely.
After this you should restart  for the changes to take effect.

## Configure PostgreSQL to be accessible from remote hosts
In the connections and authentications section, set the  line to your needs:

You can use  to listen on all available addresses.

Then add a line like the following to the authentication config:

where  is the IP address of the remote client.

See the documentation for [https://www.postgresql.org/docs/current/static/auth-pg-hba-conf.html pg_hba.conf.

After this you should restart  for the changes to take effect.

For troubleshooting take a look in the server log file:

 # journalctl -u postgresql.service

## Configure PostgreSQL authenticate against PAM
PostgreSQL offers a number of authentication methods. If you would like to allow users to authenticate with their system password, additional steps are necessary. First you need to enable PAM for the connection.

For example, the same configuration as above, but with PAM enabled:

The PostgreSQL server is however running without root privileges and will not be able to access . We can work around that by allowing the postgres group to access this file:

 # setfacl -m g:postgres:r /etc/shadow

## Change default data directory
The default directory where all your newly created databases will be stored is . To change this, follow these steps:

Create the new directory and make the postgres user its owner:

 # mkdir -p /pathto/pgroot/data
 # chown -R postgres:postgres /pathto/pgroot

Become the postgres user, and initialize the new cluster:

 initdb -D /pathto/pgroot/data

Edit  to create a drop-in file and override the  and  settings. For example:

If you want to use  directory for default directory or for tablespaces, add one more line in this file:

 ProtectHome=false

## Change default encoding of new databases to UTF-8
When creating a new database (e.g. with ) PostgreSQL actually copies a template database. There are two predefined templates:  is vanilla, while  is meant as an on-site template changeable by the administrator and is used by default. In order to change the encoding of a new database, one of the options is to change on-site . To do this, log into PostgreSQL shell () and execute the following:

First, we need to drop . Templates cannot be dropped, so we first modify it so it is an ordinary database:

 UPDATE pg_database SET datistemplate = FALSE WHERE datname = 'template1';

Now we can drop it:

 DROP DATABASE template1;

The next step is to create a new database from , with a new default encoding:

 CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UNICODE';

Now modify  so it is actually a template:

 UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template1';

Optionally, if you do not want anyone connecting to this template, set  to :

 UPDATE pg_database SET datallowconn = FALSE WHERE datname = 'template1';

Now you can create a new database:

 [postgres$ createdb blog

If you log back in to  and check the databases, you should see the proper encoding of your new database:

## Enable data checksumming
If your database files reside on a file system without checksumming, its data is suspectible to silent data corruption due to bit rot and broken hardware. While those events are rare, you might want to enable PostgreSQL's built-in data checksumming if you care about data integrity. This feature must be enabled on the cluster level, not per-database or per-table.

* To enable checksumming during cluster creation, add the  argument to .
* To verify whenever checksumming is enabled, run  (which should print  or ).
* To toggle checksumming on an existing cluster:
# Stop .
# Run  (or  if you no longer want checksumming). Enabling checksums will rewrite all database pages, which will take a while for large database instances.
# Start .

## Graphical tools
*
*
*
*
*
*
*

For tools supporting multiple DBMSs, see List of applications/Documents#Database tools.

## Set up backups
It is recommended to set up backups for databases containing valuable data. See the Backup and Restore chapter in the PostgreSQL documentation. There is also a list of backup tools in the PostgreSQL wiki, though it may not be up-to-date or complete. Remember that a backup system cannot be trusted unless you perform a test restore from time to time!

## Upgrading PostgreSQL
Upgrading major PostgreSQL versions (e.g. version 14.x to version 15.y) requires some extra maintenance.

Get the currently used database version via

 # cat /var/lib/postgres/data/PG_VERSION

To ensure you do not accidentally upgrade the database to an incompatible version, it is recommended to skip updates to the PostgreSQL packages.

Minor version upgrades are safe to perform. However, if you do an accidental upgrade to a different major version, you might not be able to access any of your data. Always check the PostgreSQL home page to be sure of what steps are required for each upgrade. For a bit about why this is the case, see the versioning policy.

There are two main ways to upgrade your PostgreSQL database. Read the official documentation for details.

## pg_upgrade
The  utility attempts to copy over as much compatible data as possible between clusters and upgrading everything else. It is generally the fastest method to upgrade most instances, although it requires access to binaries for both source and target PostgreSQL versions. Read the  man page to understand what actions it performs. For non-trivial instances (e.g. with streaming replication or log-shipping), read the upstream documentation first.

For those wishing to use , a  package is available that will always run one major version behind the real PostgreSQL package. This can be installed side-by-side with the new version of PostgreSQL. To upgrade from older versions of PostgreSQL there are AUR packages available, e.g. . (You must use the  version packaged with the PostgreSQL version you are upgrading to). If using PostGIS, install .

Note that the database cluster directory does not change from version to version, so before running , it is necessary to rename your existing data directory and migrate into a new directory. The new database cluster must be initialized using the same parameters as the old one.

When you are ready to begin the upgrade:

# While the old database cluster is still online, collect the  arguments used to create it. Refer to #Initial configuration for more information.
# Stop . Check the unit status to be sure that PostgresSQL was stopped correctly. If it failed,  will fail with .
# Upgrade , , and .
# Make sure that  does not exist. If you did not delete it after a previous upgrade, do it now.
# Rename the old cluster directory, then create a new cluster and temporary working directory:
# Initialize the new cluster using the same  arguments as were used for the old cluster:
# Upgrade the cluster, replacing  below, with the old PostgreSQL version number (e.g. ):   If necessary, adjust the configuration files of new cluster (e.g.  and ) to match the old cluster.
# Start  again.
# Optional: Run  to recalculate query analyzer statistics, which should improve query performance shortly after the upgrade. (Adding  argument may improve this command's performance.)
# Optional: Back up the  directory in case you need to restore a previous PostgreSQL version.
# Delete the  directory with old cluster data.
# Delete the  directory.
# If you use , run the stanza-upgrade command.

## Manual dump and reload
You could also do something like this (after the upgrade and install of ).

Stop
 # mv /var/lib/postgres/data /var/lib/postgres/olddata
 # mkdir /var/lib/postgres/data
 # chown postgres:postgres /var/lib/postgres/data
 initdb -D /var/lib/postgres/data --locale=C.UTF-8 --encoding=UTF8 --data-checksums
 [postgres$ /opt/pgsql-14/bin/pg_ctl -D /var/lib/postgres/olddata/ start
 # cp /usr/lib/postgresql/postgis-3.so /opt/pgsql-14/lib/ # Only if postgis installed
 pg_dumpall -h /tmp -f /tmp/old_backup.sql
 [postgres$ /opt/pgsql-14/bin/pg_ctl -D /var/lib/postgres/olddata/ stop
Start
 psql -f /tmp/old_backup.sql postgres

## Troubleshooting
## Improve performance of small transactions
If you are using PostgresSQL on a local machine for development and it seems slow, you could try turning [https://www.postgresql.org/docs/current/static/runtime-config-wal.html#GUC-SYNCHRONOUS-COMMIT synchronous_commit off in the configuration. Beware of the caveats, however.

## PostgreSQL database unable to start after package update when using extensions
The cause in this case is mostly the existing package is not compiled for the newer version (and it may be up-to-date), the solution is rebuilding the package either manually or waiting for an update to the extension package.

## Failing to start a PostgreSQL server with the older version of the database while upgrading to the newer version with extensions
This is caused because the old version of postgres from the package  does not have the required extensions (.so files) in its lib directory. The current solution is dirty, and might cause a lot of problems so keep a backup of the database just in case. Basically backup  or individual .so files to a separate, temporary location, upgrade ,  etc. and then restore the previously backed up files into  (remember to replace XX with the major version of ).

For example, for vectorchord
 # mkdir /tmp/pgsql_update
 # cp -a /usr/lib/postgresql/vchord.so*.so /tmp/pgsql_update
 # pacman -Syu
 # cp -a /tmp/pgsql_update/*.so /opt/pgsql-17/lib/

To know the exact files to copy, check the content of the package of the extension using:
 $ pacman -Ql package_name

## WARNING: database "postgres" has a collation version mismatch
You might see something like this:

 WARNING:  database "postgres" has a collation version mismatch
 DETAIL:  The database was created using collation version X.YY, but the operating system provides version X.ZZ.
 HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE postgres REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.

That means collation provider library ( or ) was updated which might have made some indexes invalid. So that means need to reindex those databases.

You can do that with:

 psql -c 'REINDEX DATABASE' postgres
 [postgres$ psql -c 'ALTER DATABASE postgres REFRESH COLLATION VERSION'

Repeat this above for all other databases by replacing postgres with respective DB name.
