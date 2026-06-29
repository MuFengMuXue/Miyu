# ZoneMinder

ZoneMinder is an integrated set of applications which provide a complete surveillance solution allowing capture, analysis, recording and monitoring of any CCTV or security cameras attached to a Linux based machine. It is designed to run on distributions which support the Video For Linux (V4L) interface and has been tested with video cameras attached to BTTV cards, various USB cameras and also supports most IP network cameras.

## Installation
Install the  package.

## Apache
1) Edit Apache's  and uncomment the following lines:

 LoadModule proxy_module modules/mod_proxy.so
 LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so
 LoadModule rewrite_module modules/mod_rewrite.so
 LoadModule cgid_module modules/mod_cgid.so
 LoadModule cgi_module modules/mod_cgi.so

2) In the same file, enable ZoneMinder's configuration by adding the following line at the end:

 Include conf/extra/zoneminder.conf

Now start or restart .

## Nginx
1) Edit Nginx's  and add the following line at the end of the  block:

 include sites-enabled/*.conf;

2) Create the  directory if it does not already exist:

 # mkdir -p /etc/nginx/sites-enabled

3) Link ZoneMinder's configuration file from  to :

 # ln -sf /etc/nginx/sites-{available,enabled}/zoneminder.conf

Now start or restart  and .

## MariaDB
1) If you have not already done so, initialize MariaDB's default database:

 # mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql 2> /dev/null

2) Start  and create a database and user for ZoneMinder:

 # mariadb -u root -p < /usr/share/zoneminder/db/zm_create.sql
 # mariadb -u root -p -e "grant select,insert,update,delete,create,drop,alter,index,lock tables,alter routine,create routine,trigger,execute on zm.* to 'zmuser'@localhost identified by 'zmpass';"

## Final steps
Run the following command to create some volatile files and directories that are required by ZoneMinder during runtime:

 # systemd-tmpfiles --create

Then, in addition to any services already started in the above steps, start  and . ZoneMinder's web interface will be accessible at http://localhost:8095.

## Troubleshooting
Logs by default are kept in . You can also inspect the log within the web interface.

See the upstream wiki page: Troubleshooting.

## Flushing application data
This is useful for developers or users that need to wipe all ZoneMinder and start fresh.

## Recreate the database
Drop the ZoneMinder MySQL database and delete the MySQL user:

Recreate the database and user:

Import the preconfigured tables into your newly created zm database:

 # mysql -u root -p zm < /usr/share/zoneminder/db/zm_create.sql

## Flush the cache folders
 # rm -Rf /var/lib/zoneminder/events/* /var/lib/zoneminder/images/* /var/lib/zoneminder/cache/*

## Local video devices
It is important that the user running httpd (usually http) can access your cameras, for example:

That is, add the http user to the video group.

To add a user to the group run the command:

 # usermod -aG video http

## Multiple local USB cameras
If you observe an error like, libv4l2: error turning on stream: No space left on device when using multiple USB video devices (such as multiple webcams), you may need to increase the bandwidth on the bus.

Test first by stopping , then:

 # rmmod uvcvideo
 # modprobe uvcvideo quirks=128

Start  and if the issue is resolved, persist the change by adding the module option to . For example:

 options uvcvideo nodrop=1 quirks=128

(reference)
