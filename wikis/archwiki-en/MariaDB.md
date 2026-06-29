# MariaDB

MariaDB is a reliable, high performance and full-featured database server which aims to be an 'always Free, backward compatible, drop-in' replacement of MySQL. Since 2013 MariaDB is Arch Linux's default implementation of MySQL.== Installation ==

[https://mariadb.com/ MariaDB is the default implementation of MySQL in Arch Linux, provided with the  and  packages.

Install  or , and run the following command before starting the :

 # mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql

Now  can be started and/or enabled.

To simplify administration, you might want to install a front-end.

## Configuration
By default both  user and the user running the server can administer the database.

To administer the server, run mariadb as the user running the server:

 mariadb

Or as root:

 # mariadb

## Add user
Creating a new user takes two steps: create the user; grant privileges. In the below example, the user monty with some_pass as password is being created, then granted full permissions to the database mydb:

## Configuration files
MariaDB configuration options are read from the following files in the given order (according to  output):

 /etc/my.cnf /etc/my.cnf.d/ ~/.my.cnf

Create a configuration file in  with a .cnf extension to ensure that upgrades preserve your configuration.

Depending on the scope of the changes you want to make (system-wide, user-only...), use the corresponding file. See [https://mariadb.com/kb/en/library/configuring-mariadb-with-option-files/ this entry of the Knowledge Base for more information.

## Enable auto-completion
The MariaDB client completion feature is disabled by default. To enable it system-wide edit , and add  under . Note that this must not be placed under . Completion will be enabled next time you run the MariaDB client.

## Using UTF8MB4
Append the following values to the main configuration file located at :

Restart  to apply the changes. Changing the character set does not change existing table formats, only newly created tables, and the protocol interaction that fetches data.

See #Maintenance to optimize and check the database health.

## Using a tmpfs for tmpdir
The directory used by MariaDB for storing temporary files is named tmpdir. For example, it is used to perform disk based large sorts, as well as for internal and explicit temporary tables.

Create the directory with appropriate permissions:

 # mkdir -pv /var/lib/mysqltmp
 # chown mysql:mysql /var/lib/mysqltmp

Add the following tmpfs mount to your  file:

 tmpfs   /var/lib/mysqltmp   tmpfs   rw,gid=mysql,uid=mysql,size=100M,mode=0750,noatime   0 0

Add to your  file under the  group:

 tmpdir      = /var/lib/mysqltmp

Stop , mount  and start .

## Time zone tables
Although time zone tables are created during the installation, they are not automatically populated. They need to be populated if you are planning on using CONVERT_TZ() in SQL queries.

To populate the time zone tables with all the time zones:

 $ mariadb-tzinfo-to-sql /usr/share/zoneinfo | mariadb -u root -p mysql

Optionally, you may populate the table with specific time zone files:

 $ mariadb-tzinfo-to-sql timezone_file timezone_name | mariadb -u root -p mysql

## Security
## Improve initial security
The  command will interactively guide you through a number of recommended security measures, such as removing anonymous accounts and removing the test database:

 # mariadb-secure-installation

## Listen only on the loopback address
By default, MariaDB will listen on the 0.0.0.0 address, which includes all network interfaces. In order to restrict MariaDB to listen only to the loopback address, add the following line in :

 bind-address = localhost

This will bind to both 127.0.0.1 and ::1, and enable MariaDB to receive connections both in IPv4 and IPv6.

## Enable access locally only via Unix sockets
By default, MariaDB is accessible via both Unix sockets and the network. If MariaDB is only needed for the localhost, you can improve security by not listening on TCP port 3306, and only listening on Unix sockets instead. To do this, add the following line in :

 [mariadb
 skip-networking

You will still be able to log in locally as before, but only using Unix sockets.

## Grant remote access
To allow remote access to the MariaDB server, ensure that MariaDB has networking enabled and is listening on the appropriate interface.

Grant any MariaDB user remote access (example for root):

 # mariadb -u root -p

Check current users with remote access privileged:

 SELECT User, Host FROM mysql.user WHERE Host <> 'localhost';

Now grant remote access for your user (here root):

 GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.1.%' IDENTIFIED BY 'my_optional_remote_password' WITH GRANT OPTION;

You can change the '%' wildcard to a specific host if you like. The password can be different from user's main password.

## Configure access to home directories
For security reasons, the systemd service file contains , which prevents MariaDB from accessing files under the ,  and  hierarchies. The  has to be in an accessible location and owned by the  user and group.

You can modify this behavior by creating a supplementary service file as described here.

## Maintenance
## Upgrade databases on major releases
Upon a major version release of  (for example mariadb-10.3.10-1 to mariadb-10.9.4-1), it is wise to upgrade the system database to make new server features available:

 # mariadb-upgrade -u root -p

To upgrade from 10.3.x to 10.9.x:

* perform a clean shutdown of the 10.3.x server
* upgrade the package
* run  (from the new package version) against the new running daemon

If the (new) daemon is not starting, see #Unable to run mariadb-upgrade because MariaDB cannot start.

## Checking, optimizing and repairing databases
 ships with mariadb-check which can be used to check, repair, and optimize tables within databases from the shell. See  for more.  Several command tasks are shown:

To check all tables in all databases:

 $ mariadb-check --all-databases -u root -p -c

To analyze all tables in all databases:

 $ mariadb-check --all-databases -u root -p -a

To repair all tables in all databases:

 $ mariadb-check --all-databases -u root -p -r

To optimize all tables in all databases:

 $ mariadb-check --all-databases -u root -p -o

## Backup
There are various tools and strategies to back up your databases.

If you are using the default InnoDB storage engine, a suggested way of backing up all your bases online while provisioning for point-in-time recovery (also known as "roll-forward", when you need to restore an old backup and replay the changes that happened since that backup) is to execute the following command:

 $ mariadb-dump --single-transaction --flush-logs --events --routines --master-data=2 --all-databases -u root -p > all_databases.sql

This will prompt for MariaDB's root user's password, which was defined during database #Configuration.

Specifying the password on the command line is strongly discouraged, as it exposes it to discovery by other users through the use of  or other techniques. Instead, the aforementioned command will prompt for the specified user's password, concealing it away.

## Compression
As SQL tables can get pretty large, it is recommended to pipe the output of the aforementioned command in a compression utility like :

 $ mariadb-dump --single-transaction --flush-logs --events --routines --master-data=2 --all-databases -u root -p | xz -z > all_databases.sql.xz

Decompressing the backup thus created and reloading it in the server is achieved by doing:

 $ xzcat all_databases.sql.xz | mariadb -u root -p

This will recreate and repopulate all the databases previously backed up (see this or this).

## Non-interactive
If you want to setup non-interactive backup script for use in cron jobs or systemd timers, see option files and this illustration for mariadb-dump.

Basically you should add the following section to the relevant configuration file:

Mentioning a user here is optional, but doing so will free you from having to mention it on the command line. If you want to set this for all tools, including , use the  group.

## Example script
The database can be dumped to a file for easy backup. The following shell script will do this for you, creating a  file in the same directory as the script, containing your database dump:

 #!/bin/sh

 THISDIR=$(dirname $(readlink -f "$0"))

 mariadb-dump --single-transaction --flush-logs --events --routines --master-data=2 --all-databases \
  | xz -z > $THISDIR/db_backup.xz
 echo 'purge master logs before date_sub(now(), interval 7 day);' | mariadb

See also the official  page in the MariaDB manuals.

## Holland Backup
A python-based software package named Holland Backup allows to automate all of the backup work. It supports direct mysqldump, LVM snapshots to tar files (mysqllvm), LVM snapshots with mysqldump (mysqldump-lvm), and  methods to extract the data. The Holland framework supports a multitude of options and is highly configurable to address almost any backup situation.

The main  and  packages provide the core framework; one of the sub-packages (,  and/or  must be installed for full operation. Example configurations for each method are in the  directory and can be copied to , as well as using the  command to generate a base configuration for a named provider.

## Troubleshooting
## Unable to run mariadb-upgrade because MariaDB cannot start
Try run MariaDB in a standalone:

 # mariadbd-safe --datadir=/var/lib/mysql/

And then run:

 # mariadb-upgrade -u root -p

## Reset the root password
# Stop .
# Start the MariaDB server with safety features:
# Connect to it:
# Change root password:
# Kill running mariadbd* processes:
# Start .

## Check and repair all tables
Check and auto repair all tables in all databases, see more:

 # mariadb-check -A --auto-repair -u root -p

## Optimize all tables
Forcefully optimize all tables, automatically fixing table errors that may come up.

 # mariadb-check -A --auto-repair -f -o -u root -p

## OS error 22 when running on ZFS
If using MySQL databases on ZFS, the error  may occur.

A workaround is to disable  in :

## Cannot login through CLI, but phpmyadmin works well
This may happen if you are using a long (>80) password.  CLI cannot handle that many characters in readline mode. So, if you are planning to use the recommended password input mode:

Consider changing the password to smaller one.

## MariaDB binary logs are taking up huge disk space
By default, mariadbd creates binary log files at  with the numbers ascending. These logs are useful for replication master server or data recovery, but these binary logs can easily eat up large amounts of disk space. If you do not plan to use replication or data recovery features, you may disable binary logging by commenting out these lines in  then restart:

 #log-bin=mysql-bin
 #binlog_format=mixed

Or, if you want to keep these logs but keep their size in check and old logs deleted, you can set these limits then restart:

 log-bin=mysql-bin
 expire_logs_days = 10
 max_binlog_size  = 100M

Alternatively, there exists a MariaDB command to manually purge logs older than a specific one. For example, you may see a file named  and want to delete every log older than it. As long as the log-bin=mysql-bin setting is in effect, you would run:

 # mariadb -u root -p"PASSWORD" -e "PURGE BINARY LOGS TO 'mysql-bin.000023;"

## OpenRC fails to start MariaDB
To use MariaDB with OpenRC you need to add the following lines to the  section in the MySQL configuration file, located at .

 user = mysql
 basedir = /usr
 datadir = /var/lib/mysql
 pid-file = /run/mysqld/mysql.pid

You should now be able to start MariaDB using:

 # rc-service mysql start

## Changed limits warning on max_open_files/table_open_cache
Increase the number of file descriptors by creating a systemd drop-in, e.g.:

## 10.4 to 10.5 upgrade crash: "InnoDB: Upgrade after a crash is not supported. The redo log was created with MariaDB 10.4.x"
Before MariaDB 10.5, redo log was unnecessarily split into multiple files.Do NOT ever remove the old binary logs  out of the way.

To resolve this, install MariaDB 10.4. Start it and let it undergo a clean shutdown. After that happens you can upgrade to 10.5 again. Same applies if another version of MariaDB was specified.

## Table 'mysql.xxx' does not exist in engine
Symptom: When running mariadb-upgrade or mariadb-check, it return one or more error like these:

 Table 'mysql.xxx' does not exist in engine

Where "xxx" usually is the system table inside the mysql database.

Steps to fix this,

# Create backup directory outside of MariaDB {{ic|${DATADIR}}}, for example in .
# Copy the offending files from {{ic|${DATADIR}/mysql/xxx.{frm,ibd}}} to backup directory. The  may not exist.
# Drop the tables with DROP TABLE mysql.xxx on the  prompt.
# Run the mariadb-check. On success, the file  and  should be created again.
# Re-run mariadb-upgrade if necessary. You may need the --force option.
