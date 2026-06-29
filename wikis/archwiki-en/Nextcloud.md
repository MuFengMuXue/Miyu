# Nextcloud

Nextcloud is a suite of client-server-software that (by means of so-called apps) allows all kinds of sharing, collaboration and communication, e.g.:

* file sharing
* personal information manager (contacts, calendar, tasks)
* messaging (mail, chat, video conferencing)
* collaborative editing of documents (text, Office integration)

Nextcloud is open source and based on open standards. Data sovereignty is a big plus, i.e. with your own instance of Nextcloud, you break free from proprietary (and potentially untrustworthy) services like Dropbox, Office 365, or Google Drive.

Depending on your needs Nextcloud can be deployed from single-board computers (like e.g. a Raspberry Pi) all the way up to full scale data centers serving millions of users. With an elaborated authorization scheme and the option for federation (connecting discrete instances) Nextcloud is well suited for use in enterprise environments.

Nextcloud is a fork of ownCloud. See Wikipedia:Nextcloud#History.

## Setup overview
A complete installation of Nextcloud comprises (at least) the following components:

A web server paired with an application server on which runs Nextcloud (i.e. the PHP code) using a database.

This article will cover MariaDB/MySQL and PostgreSQL as databases and the following combinations of web server and application server:

* nginx &rarr; uWSGI (plus uwsgi-plugin-php)
* nginx &rarr; FPM,
* Apache HTTP server (using mod_proxy_uwsgi) &rarr; uWSGI (plus uwsgi-plugin-php)
* Apache HTTP server (using mod_proxy_fcgi) &rarr; FPM

The Nextcloud package complies with the web application package guidelines. Among other things this mandates that the web application be run with a dedicated user - in this case . This is one of the reasons why the application server comes into play here. For the very same reason it is not possible anymore to execute Nextcloud's PHP code directly in the Apache process by means of .

## Installation
Install the  package. This will pull in quite a few dependent packages. Most of the required PHP extensions will be taken care of this way.

It is recommended to also install the packages

*  for the argon2 hashing algorithm and
*  and  for preview generation

(preferrably as dependent package). Other optional dependencies will be covered later depending on your concrete setup (e.g. what database you choose).

Mind that some modules (namely bcmath, exif, gmp, intl and sysvsem) come with . So no explicit installation is required for those.

## Configuration
## PHP
This guide does not tamper with PHP's central configuration file  but instead puts Nextcloud specific PHP configuration in places where it does not potentially interfere with settings for other PHP based applications. These places are:

* A dedicated copy of  in  (for the  command line tool and the background job). This is literally a copy of the original  as provided by the  package with some Nextcloud specific additions / modifications.

* Corresponding settings in the configuration of the application server. These will be covered in the section about application servers.

Make a copy of  to  (or even better, extract  from the php-legacy package tarball below ). Although not strictly necessary, change ownership of the copy:

Most of the required PHP modules listed in Nextcloud's documentation are already enabled in the just copied bare PHP installation configuration file. Additionally enable the following extensions:

Depending on the database you are going to use enable the corresponding  module. See Database below.

Set  to your preferred timezone, e.g.:

Raise PHP's memory limit to at least 512MiB:

Optional: For additional security configure . This limits the locations where Nextcloud's PHP code can read and write files. Proven settings are

Depending on what additional extensions you configure you may need to extend this list, e.g.  in case you opt for Valkey.

It is not necessary to configure opcache here as this  is only used by the  command line tool and the background job, i.e. by short running PHP processes.

## Nextcloud
Add the following entries to Nextcloud's configuration file:

Adapt the given example hostname . In case your Nextcloud installation will be reachable via a subfolder (e.g. )  and  have to be modified accordingly.

## System and environment
To make sure the Nextcloud specific  is used by the  tool set the environment variable :

 NEXTCLOUD_PHP_CONFIG=/etc/webapps/nextcloud/php.ini

As a privacy and security precaution create the dedicated directory for session data:

 # install --owner=nextcloud --group=nextcloud --mode=700 -d /var/lib/nextcloud/sessions

## Database
MariaDB/MySQL is the canonical choice for Nextcloud.

:The MySQL or MariaDB databases are the recommended database engines.Most information concerning databases with Nextcloud deals with MariaDB/MySQL. The Nextcloud developers admit to have [https://github.com/nextcloud/server/issues/5912#issuecomment-318568370| less detailed expertise with other databases.

PostgreSQL is said to deliver better performance and overall has fewer quirks compared to MariaDB/MySQL. SQLite is mainly supported for test / development installations and not recommended for production. The list of supported databases also contains Oracle database. This product will not be covered here.

## MariaDB / MySQL
Since MariaDB has been the default MySQL implementation in Arch Linux since 2013this text only mentions MariaDB.

In case you want to run your database on the same host as Nextcloud install, configure and start  (if you have not done so already). See the corresponding article for details. Do not forget to initialize MariaDB with . It is recommended for additional security to configure MariaDB to only listen on a local Unix socket:

Nextcloud's own documentation [https://docs.nextcloud.com/server/stable/admin_manual/configuration_database/linux_database_configuration.html#database-read-committed-transaction-isolation-level recommends to set the transaction isolation level to READ-COMMITTED. This is especially important when you expect high load with many concurrent transactions.

The other recommendation to set  is obsolete. The default  in recent MariaDB versions is at least as good as the recommended . In any case the setting is only relevant when replication is applied.

Start the CLI tool  with database user root (default password is empty, but hopefully you change it as soon as possible):

 $ mysql -u root -p

Create the user and database for Nextcloud with:

 is a placeholder for the actual password of DB user nextcloud you must choose. Quit the tool with .

So that you have decided to use MariaDB as the database of your Nextcloud installation you have to enable the corresponding PHP extension:

Further configuration (related to MariaDB) is not required (contrary to the information given in Nextcloud's admin manual).

Now setup Nextcloud's database schema with:

Mind the placeholders (e.g. ) and replace them with appropriate values. This command assumes that you run your database on the same host as Nextcloud. Enter  and see Nextcloud's documentation for other options. See Using the "occ" command line tool for Arch-specific details about this tool.

## PostgreSQL
Consult the corresponding article for detailed information about PostgreSQL. In case you want to run your database on the same host as Nextcloud install, configure and start  (if you have not done so already). For additional security in this scenario it is recommended to configure PostgreSQL to only listen on a local UNIX socket:

Especially do not forget to initialize your database with . After having done so start PostgreSQL's CLI tool psql and create the database user  and the database of the same name:

 is a placeholder for the password of database user nextcloud that you have to choose.

Install the additional package  (preferrably as dependent package) and enable the corresponding PHP extension in :

Now setup Nextcloud's database schema with:

Mind the placeholders (e.g. ) and replace them with appropriate values. This command assumes that you run your database on the same host as Nextcloud. Enter  and see Nextcloud's documentation for other options. See Using the "occ" command line tool for Arch-specific details about this tool.

## Application server
There are two prevalent application servers that can be used to process PHP code: uWSGI or FPM. FPM is specialized on PHP. The protocol used between the web server and FPM is fastcgi. The tool's documentation leaves room for improvement. uWSGI on the other hand can serve code written in a handful of languages by means of language specific plugins. The protocol used is uwsgi (lowercase). The tool is extensively documented - albeit the sheer amount of documentation can become confusing and unwieldy.

## uWSGI
uWSGI has its own article. A lot of useful information can be found there. Install  and the plugin  (preferrably as dependent packages). To run Nextcloud's code with (or in) uWSGI you have to configure one uWSGI specific configuration file () and define one systemd service.

## nextcloud.ini
The  package includes a sample configuration file already in the right place . In almost any case you will have to adapt this file to your requirements and setup. Find a version with lots of commented changes (compared to the package's version). It assumes a no-frills Nextcloud installation for private use (i.e. with moderate load).

In general keep the enabled extensions, extension specific settings and  in sync with  (with the exception of opcache).

## uWSGI service
The package  provides a template unit file (). The instance ID (here nextcloud) is used to pick up the right configuration file. Enable and start .

In case you have more than a few (e.g. 2) services started like this and get the impression this is a waste of resource you might consider using emperor mode.

## FPM
In case you opt to use FPM as your application server install  (preferably as dependent package).

Configuration consists of a copy of  relevant for all applications served by FPM and a so-called pool file specific for the application (here Nextcloud). Finally you have to tweak the systemd service file.

## php-fpm.ini
As stated earlier this article avoids modifications of PHP's central configuration in . Instead create a FPM specific copy.

Make sure it is owned and only writeable by root (). Enable the op-cache, i.e. uncomment the line

and put the following parameters below the existing line :

## nextcloud.conf
Next you have to create a so called pool file for FPM. It is responsible for spawning dedicated FPM processes for the Nextcloud application. Create a file  - you may use this functional version as a starting point.

Again make sure this pool file is owned and only writeable by root (i.e. ). Depending on whether access log is configured (it is with above sample ) you may need to create the corresponding directory (here ). Adapt or add settings (especially ,  and ) to your liking. The settings  and  must be consistent with the corresponding settings in  (but not ).

The settings done by means of  and  could instead be specified in . But mind that settings in  apply for all applications served by FPM.

## systemd service
FPM is run as a systemd service. You have to modify the service configuration to be able to run Nextcloud. This is best achieved by means of a drop-in file:

* It replaces the  line by a start command that uses the  covered in the previous section.
* The directories  and  (and everything below) are made writable. The  in the original service definition causes ,  and  to be mounted read-only for the FPM processes.
* If you want to use hardware transcoding (e.g. in the memories app) you need to explicitly allow access to your graphics device as  hides any devices from the FPM processes. For example adding  and  to the drop-in file allows usage of a properly configured Intel iGpu.

Do not forget to enable/start the service php-fpm-legacy.

## Keep /etc tidy
The Nextcloud package unconditionally creates the uWSGI configuration file . Of course it is of no use when you run FPM instead of uWSGI (and it does no harm whatsoever). In case you nevertheless want to get rid of it, just add the following NoExtract line to :

## Web server
There is an abundance of web servers you can choose from. Whatever option you finally pick you have to keep in mind that the Nextcloud application needs to be run with its own system user nextcloud. So you will need to forward your requests to one of the above mentioned application servers.

## nginx
Configuration of nginx is way beyond the scope of this article. See the relevant article for further information. Also consult Nextcloud's documentation for an elaborated configuration. It is up to you how to include this snippet into your nginx' configuration. One common approach is to use directories  and  to separate configurations for various servers (aka virtual hosts). See Nginx#Managing server entries for details.

If using the example nginx config from the Nextcloud documentation linked above, the root directory should be changed to:

The usage of the block {{ic|upstream php-handler { ... } }} is not necessary. Just specify  in the  block that deals with forwarding request with PHP URIs to the application server. When using uWSGI instead of FPM replace this  block with:

{{hc|cloud.mysite.com.conf|
location ~ \.php(?:$/) {
    include uwsgi_params;
    uwsgi_modifier1 14;
    # Avoid duplicate headers confusing OC checks
    uwsgi_hide_header X-Frame-Options;
    uwsgi_hide_header X-XSS-Protection;
    uwsgi_hide_header X-Content-Type-Options;
    uwsgi_hide_header X-Robots-Tag;
    uwsgi_hide_header X-Download-Options;
    uwsgi_hide_header X-Permitted-Cross-Domain-Policies;
    uwsgi_pass unix:/run/uwsgi/nextcloud.sock;
}
}}

Things you might have to adapt (not exhaustive):

* Your server name ( clauses 2x), i.e. the server part of the URL your Nextcloud installation will be reachable with.
* The name of the certificate and key you use for SSL / TLS.
* If and where you want an access log written to.
* The location where Certbot (or any other ACME client) will put the domain verification challenges. Usage of  instead of  is probably more adequate here.
* The path used to reach your Nextcloud installation. (The part right to the server name &amp; port section in the URL.)
* What application server (uWSGI or FPM) you are using, i.e. how and where nginx will pass requests that need to trigger some PHP code. (See above.)
* Configure OCSP stapling. (Note that Let's Encrypt does not support OCSP anymore, so if you are using a Let's Encrypt certificate, there is no need for this.)

There is no need to install any additional modules since nginx natively supports both protocols FastCGI and uwsgi.

## Apache HTTP server
Find lots of useful information in the article about the Apache HTTP Server. Nextcloud's documentation has some sample configuration that can also be found in . Both implicitly rely on mod_php that cannot be used anymore. mod_proxy_fcgi or mod_proxy_uwsgi need to be applied.

Information about how to integrate Apache with FPM can be found here in this wiki. uWSGI's documentation has some information about how to integrate Apache with PHP by means of uWSGI and mod_proxy_uwsgi. Mind that the Apache package comes with both modules mod_proxy_fcgi and mod_proxy_uwsgi. They need to be loaded as required.

The following Apache modules are required to run Nextcloud:

Also uncomment the following directive to pull in TLS configuration parameters:

Consult Mozilla's SSL configurator for details about how to optimize your TLS configuration.

Refer to the following two sample configuration files depending on how you want to access your Nextcloud installation:

* In case your Nextcloud installation is accessed via a dedicated host name (e.g. ) put this fragment into .
* In case your Nextcloud installation is located in a subfolder of your web site (e.g. ) put this fragment in your .

Of course you must adapt these sample configuration files to your concrete setup. Replace the  directive by  when you use uWSGI.

The Nextcloud package comes with a  that already takes care of a lot of rewriting and header stuff. Run  to adapt this file. Parameter  in  is vital for this.

## Background jobs
Nextcloud requires certain tasks to be run on a scheduled basis. See Nextcloud's documentation for some details. The easiest (and most reliable) way to set up these background jobs is to use the systemd service and timer units that are already installed by . The service unit needs some tweaking so that the job uses the correct PHP ini-file (and not the global ). Create a drop-in file and add:

After that enable/start  (not the service).

As recommended by the documentation add the parameter

to Nextcloud's configuration file. The value is the hour of the day in UTC defining the start of a 4 hours window. Time consuming jobs that need to be run only once a day will be scheduled in this time frame, i.e. outside working hours.

## In-memory caching
Nextcloud's documentation recommends to apply some kind of in-memory object cache to significantly improve performance.

## APCu
Install  (preferrably as dependent package). Enable the extension in the relevant configuration files. These are

*  used by the  command and the background jobs and
* depending on the application server you use either
**  in case of uWSGI or
**  in case of FPM.

In  add the lines

preferably somewhere below .

For the other two files the setting to activate APCu is already in place and only needs to be uncommented. Two other configuration parameters related to APCu are also already there. No need to touch  or .

Restart your application server (not the web server as Nextcloud's documentation claims). Add the following line to your Nextcloud configuration file:

## Valkey (Redis)
Valkey was forked from Redis version 7.2.4 in March 2024 due to license issues. Nextcloud's documentation still only mentions Redis. However, one year later Valkey can still be considered a drop-in replacement for Redis. (Future will show how long this will stand.)

Valkey can be run locally (i.e. on the same host as Nextcloud) or on a different machine. (For more information see Nextcloud's documentation.) In any case install  and  (preferrably as dependent packages).

Enable these extensions in  and, depending on the application server you use, in  or . This can be done by locating the existing sections where other extensions are enabled and adding two additional lines corresponding to  and .

Alternatively, you can enable the required extensions  and  in their respective initialization files in  by uncommenting the  lines.

In case you have specified the  option in the above configuration files and use Valkey locally with a local Unix socket, you have to extend the list of directories where PHP is allowed to read and write files. Locate the relevant lines in the files specified above and add  the directory containing the local Unix socket created by Valkey, e.g. .

Extend your Nextcloud configuration as follows:

Again, adapt  as required. ,  and  are optional.

In case Valkey runs on a different machine:

 is just a placeholder. Adapt to your actual setup.

## Security hardening
See the Nextcloud documentation and Security. Nextcloud additionally provides a Security scanner.

## Synchronization
## Desktop
The official client can be installed with the  package. Please keep in mind that using  with Nextcloud is not supported.

The desktop client basically syncs one or more directories of your desktop computer with corresponding folders in your Nextcloud's file service. It integrates nicely with your desktop's file manager (Dolphin in KDE Plasma, Nautilus in Gnome) displaying overlays representing synchronization and share status. The context menu of each file gets an additional entry Nextcloud to manage sharing of this file and getting the public or internal share link. Nextcloud's documentation has a volume exclusively about the desktop client.

In case the integration does not work as described consult the optional dependencies of package . E.g. Nautilus requires . Install as dependent package.

By default nextcloud provides a dbus activated service that might be triggered by a lot of randomly seeming things like opening a file dialog. You can add the following to your pacman config to disable it, before installing the client.

## Thunderbird
Since version 102 Thunderbird fully supports CalDAV and CardDAV - even with auto detection (i.e. you do not have to provide long URLs to access your calendars and address books). See Nextcloud's documentation for details.

## Mounting files with davfs2
If you want to mount your Nextcloud using WebDAV, install  (as described in davfs2).

To mount your Nextcloud, use:

 # mount -t davfs https://cloud.mysite.com/remote.php/dav/files/username/ /path/to/mount

You can also create an entry for this in :

## Mounting files in GNOME Files (Nautilus)
You can access the files directly in Nautilus ('+ Other Locations') via the WebDAV protocol. Use the link as shown in your Nextcloud installation Web GUI (e.g. ) but replace the protocol name  by . Nautilus will ask for user name and password when trying to connect.

## Android
Download the official Nextcloud app from Google Play or F-Droid.

To enable contacts and calendar sync (Android 4+):

# Download DAVx5 (Play Store, F-Droid).
# Create a new DAVdroid account in the Account settings and specify your server URL (e.g. ) and login / password pair.

{{Note|There is no need for the {{ic|/remote.php/{carddav,webdav}}} part if you configured your web server with the proper redirections, as illustrated in the above section Web server. DAVdroid will find itself the right URLs.}}

## iOS
Download the official Nextcloud app from the App Store.

## Tips and tricks
## Using the "occ" command line tool
A useful tool for server administration is . Refer to Nextcloud's documentation for details. You can perform many common server operations with , such as managing users and configuring apps.

A convenience wrapper around the original  is provided with  which automatically runs as the default user (nextcloud), using the default PHP executable and PHP configuration file. The environment variables ,  and  can be used to specify a non-default user, PHP executable and PHP configuration file (respectively). Especially the latter (using ) is necessary when Nextcloud was setup in a way as described in the sections Configuration and Application server, i.e. using a PHP configuration specific to Nextcloud. In this case put  in your .

When using package  instead of the recommended package  you also have to set , i.e. .

## Pacman hook
The  package comes with a pacman hook that takes care of automatically upgrading the Nextcloud database after the package has been updated. Take a look .

Unfortunately, this hook unconditionally uses the global  when running , i.e. it does not take into account the value of environment variable  as mentioned above in Using the "occ" command line tool.

As a possible workaround make a copy of the delivered hook file in the appropriate location:

and change the line starting with  to:

## Running Nextcloud in a subdirectory
The instructions in section Web server will result in a setup where your Nextcloud installation is reachable via a dedicated server name, e.g. . If you would like to have Nextcloud located in a subdirectory. e.g. , then:

* For nginx refer to the section in Nextcloud's documentation that explicitly covers this topic.
* For apache edit the  you included and comment out the  part of the include file.

## Docker
See the Nextcloud repository on Docker Hub for running Nextcloud in Docker.

## Office integration
There are currently three different solutions for office integration:

* Collabora Online
* ONLYOFFICE
* MS Office Online Server

All three have in common that a dedicated server is required and your web server needs to be adapted to forward certain requests to the office service. The actual integration with Nextcloud is then accomplished by means of a Nextcloud app specific for one of the above products.

Mind that all three products are aimed at businesses, i.e. you will have to pay for the office service. Only Collabora offers a developers plan (CODE) for free. ONLYOFFICE offers a Home Server plan for a reasonable price.

For installation, setup instructions and integration with Nextcloud consult:

* Collabora online, app
* ONLYOFFICE, app
* MS Office Online Server, app

## Disabling app recommendations
By default, Nextcloud recommends apps to new clients, which can result in a lot of notifications. To disable this, disable the recommendations app using .

## Backup calendars and address books with calcardbackup
The  package can be installed and configured to provide regular backups of the calendar and/or address book databases. Edit  to your liking and then start and enable .

## Data directory on different drive
Over time the  of you Nextcloud installation will probably grow considerably. The location of this directory is specified in , typically:

It is advisable to put this directory on a separate file system with enough space, in many cases on a separate drive. This additionally offers the option to implement some form of redundancy on that file system (aka RAID). A (non-exhaustive) list of options how to accomplish that:

* Change the above mentioned configuration entry to point to some other location on a separate file system.

* Create a symbolic link at  referencing a location on a separate file system.

* Mount a separate file system on  (or one of its parent directories).

To a lesser extend the same applies for the writable apps directory that is also specified in , typically:

Do not try to change anything with the entry in the same array that has  (the so-called read-only apps directory).

## Troubleshooting
## Reading the log
By default, the logs of the web application are available in . The entries (lines) are in JSON format and can be very long. Readability can be greatly improved by using :

 # jq . /dev/null
}}

All folders reported with

(and that can also be found in the writeable apps directory) can be safely deleted from . Other double installed apps (i.e. those belonging to a package) should be removed from .

## Login page loop
As mentioned in a post in the forum, this issue can be fixed by setting correct permissions on the sessions directory. (See Nextcloud's documentation for details.) It is also possible that the sessions directory is missing altogether. The creation of this directory is documented in System and environment.

 should look like this:

Also, this can be caused by a full file system due to an extensive size of . In the past there have been bugs flooding the log file with error messages, e.g. this one. In this case, truncating the log file and restarting uwsgi or php-fpm-legacy helps.

## Environment variables not available
Depending on what application server you use custom environment variables can be provided to Nextcloud's PHP code.

## FPM
Add one or more lines in  as per Nextcloud's documentation, e.g.:

## uWSGI
Add one or more lines in , e.g.:

Mind there must not be any blanks around the second .

## You are accessing your instance over a secure connection, however your instance is generating insecure URLs
If you get the following message in your administration settings:

:You are accessing your instance over a secure connection, however your instance is generating insecure URLs. This most likely means that you are behind a reverse proxy and the overwrite config variables are not set correctly. Please read the documentation page about this.

Add the following in your configuration file: Replace  with your public IP.

## Nextcloud reports corrupted index (MariaDB)
If Nextcloud reports corrupted indices (e.g. during  commands or in Administration > Logging) you can repair your database by executing:

If the command fails, it still will point out the table  containing a corrupted index. Repair it by logging into mariadb:

Replace  to match your findings.

## Failed to fetch the Collabora capabilities endpoint
In case you get responses with:

: Failed to fetch the Collabora capabilities endpoint: Client error: `GET http://localhost/wapps/richdocumentscode/proxy.php?req=/hosting/capabilities` resulted in a `404 Not Found` response

double-check your  that entry  has been set as described in section Configuration / Nextcloud.

## Reset after failed login attempts
To unblock an IP address after too many failed login attempts, run

 $ occ security:bruteforce:reset IP_address

## uwsgi logs 'unavailable modifier requested: 0' in journal
This may happen when attempting to use Apache with mod_proxy_uwsgi.  According to https://uwsgi-docs.readthedocs.io/en/latest/Apache.html#mod-proxy-uwsgi,  mod_proxy_uwsgi does not know how to set modifiers to tell uwsgi what scripting to use, and always sends zero.  It appears from several config examples that the modifier expected by uwsgi for php is 14.  The solution suggested in the above site is to set php (or, php_legacy) to be modifier 0 in your nextcloud ini file (/etc/uwsgi/nextcloud.ini) by preceding the plugin name with '0:'.  The line would look something like this:

## Permission denied in apache error log connecting to nextcloud uwsgi socket
By default the permissions on the nextcloud uwsgi socket do not allow writing by any user other than the user called out in the nextcloud uwsgi ini file, however the web server user (http) needs to have write access.   The following can be added to the uwsgi netcloud.ini file to allow http group to write to it;
