# Apache HTTP Server

The Apache HTTP Server, or Apache for short, is a very popular web server, developed by the Apache Software Foundation.

This article describes how to set up Apache and how to optionally integrate it with PHP.

## Installation
Install the  package.

## Configuration
Apache configuration files are located in . The main configuration file is , which includes various other configuration files. The default configuration file should be fine for a simple setup. By default, it will serve the directory  to anyone who visits your website.

To run Apache, start . If everything is working correctly, visiting http://localhost/ should display a simple index page.

For optional further configuration, see the following sections.

## Advanced options
See the full list of Apache configuration directives and the directive quick reference.

These options in  might be interesting for you:

 User http
:For security reasons, as soon as Apache is started by the root user (directly or via startup scripts) it switches to this UID. The default user is http, which is created automatically during installation.

 Listen 80
:This is the port Apache will listen to. For Internet-access with router, you have to forward the port.

:If you want to setup Apache for local development you may want it to be only accessible from your computer. Then change this line to .

 ServerAdmin you@example.com
:This is the admin's email address which can be found on e.g. error pages.

 DocumentRoot "/srv/http"
:This is the directory where you should put your web pages.

:Change it, if you want to, but do not forget to also change  to whatever you changed your  to, or you will likely get a 403 Error (lack of privileges) when you try to access the new document root. Do not forget to change the  line to , otherwise you will get a 403 Error. Remember that the DocumentRoot directory and its parent folders must allow execution permission to others (can be set with ), otherwise you will get a 403 Error.

 AllowOverride None
:This directive in  sections causes Apache to completely ignore  files. Note that this is now the default for Apache 2.4, so you need to explicitly allow overrides if you plan to use  files. If you intend to use  or other settings in  files, you can allow which directives declared in that file can override server configuration. For more info refer to the Apache documentation.

More settings can be found in :

To turn off your server's signature:
 ServerSignature Off

To hide server information like Apache and PHP versions:
 ServerTokens Prod

## User directories
User directories are available by default through http://localhost/~yourusername/ and show the contents of  (this can be changed in ).

If you do not want user directories to be available on the web, comment out the following line in :

 Include conf/extra/httpd-userdir.conf

Ensure that the Apache web server has sufficient permissions to traverse the user's home directory and access files within . Directory traversal requires execute () permission on each parent directory in the path, independent of the read () permissions on the target files.

The recommended method is to use Access Control Lists (ACLs) to grant access to the  user only:

 $ setfacl -m u:http:x ~
 $ setfacl -R -m u:http:rx ~/public_html

Avoid using world-executable permissions (e.g. ), as this weakens the security of your home directory.

You also need to edit the configuration of the systemd service in the drop-in file

 ProtectHome=no

Do a daemon-reload and restart  to apply the changes. See also Umask#Set the mask value.

## TLS
Firstly obtain a certificate. If you own a public domain, you can use Transport Layer Security#ACME clients.

In , uncomment the following three lines:
 LoadModule ssl_module modules/mod_ssl.so
 LoadModule socache_shmcb_module modules/mod_socache_shmcb.so
 Include conf/extra/httpd-ssl.conf

If using Certbot (), the following line needs to be uncommented as well:
 LoadModule rewrite_module modules/mod_rewrite.so

After obtaining a key and certificate, make sure the  and  lines in  point to the key and certificate. If a concatenated chain of CA certificates was also generated, add that filename against .

Finally, restart  to apply any changes.

## Virtual hosts
If you want to have more than one host, uncomment the following line in :
 Include conf/extra/httpd-vhosts.conf

In  set your virtual hosts. The default file contains an elaborate example that should help you get started.

To test the virtual hosts on your local machine, add the virtual names to your  file:
 127.0.0.1 domainname1.dom
 127.0.0.1 domainname2.dom

Restart  to apply any changes.

## Managing many virtual hosts
If you have a huge amount of virtual hosts, you may want to easily disable and enable them. It is recommended to create one configuration file per virtual host and store them all in one folder, eg: .

First create the folder:
 # mkdir /etc/httpd/conf/vhosts

Then place the single configuration files in it:
 # nano /etc/httpd/conf/vhosts/domainname1.dom
 # nano /etc/httpd/conf/vhosts/domainname2.dom
 ...

In the last step,  the single configurations in your :
 #Enabled Vhosts:
 Include conf/vhosts/domainname1.dom
 Include conf/vhosts/domainname2.dom

You can enable and disable single virtual hosts by commenting or uncommenting them.

A very basic vhost file will look like this:

## Extensions
## PHP
First install PHP, then follow one of the next three subsections below.  Finally, test the installation as described in the final subsection.

## Using libphp
This method is probably the easiest, but is also the least scalable: it is suitable for a light request load. It also requires you to change the mpm module, which may cause problems with other extensions (e.g. it is not compatible with #HTTP/2).

Install .

In , comment the line:

 #LoadModule mpm_event_module modules/mod_mpm_event.so

and uncomment the line:

 LoadModule mpm_prefork_module modules/mod_mpm_prefork.so

To enable PHP, add these lines to :

* Place this at the end of the  list:
 LoadModule php_module modules/libphp.so
 AddHandler php-script .php
* Place this at the end of the  list:
 Include conf/extra/php_module.conf

then restart .

## Using apache2-mpm-worker and mod_fcgid
This method provides improved performance and memory usage when serving multiple requests.

Install  and .

Create the needed directory and symlink it for the PHP wrapper:
 # mkdir /srv/http/fcgid-bin
 # ln -s /usr/bin/php-cgi /srv/http/fcgid-bin/php-fcgid-wrapper

Create  with the following content:

Edit :
* Uncomment the loading of the actions module:
* Load the FCGID module after the loading of the unixd module (on which it is dependent) - you may wish to place this within the  block:
* Ensure that the inclusion of the MPM configuration is uncommented (it is uncommented in the default installed version of this file):
* Add an inclusion of your new FCGID configuration:

Restart .

## Using php-fpm and mod_proxy_fcgi
This method provides "an alternative PHP FastCGI implementation with some additional features (mostly) useful for heavy-loaded sites" [https://www.php.net/manual/en/install.fpm.php.

Install .

Enable proxy modules:

Create  with the following content:

And include it at the bottom of :
 Include conf/extra/php-fpm.conf

You can configure PHP-FPM in , but the default setup should work fine.

Start and enable , then restart .

## Test whether PHP works
To test whether PHP was correctly configured, create a file called  in your Apache  directory (e.g.  or ) with the following contents:

Then go to http://localhost/test.php or http://localhost/~/test.php as appropriate.

## HTTP/2
To enable HTTP/2 over TLS support, uncomment the following line in :
 LoadModule http2_module modules/mod_http2.so

And add the following line:
 Protocols h2 http/1.1

To debug, you can set only the module rather than the entire server to  or :

     LogLevel http2:info

For more information – including extra HTTP/2 feature settings – see the mod_http2 documentation.

## Troubleshooting
## Apache Status and Logs
See the status of the Apache daemon with systemctl.

Apache logs can be found in

## Error: PID file /run/httpd/httpd.pid not readable (yet?) after start
Comment out the  line in :

## /run/httpd not being created at boot
If  as the root user complains about "unsafe path transition", check ownership of your root directory.

 ls -la /
 chown root:root /

## Apache is running a threaded MPM, but your PHP Module is not compiled to be threadsafe.
If when loading  the  fails, you may get an error like this in the journal:

 Apache is running a threaded MPM, but your PHP Module is not compiled to be threadsafe.  You need to recompile PHP.

This is because PHP includes support for a module that is not threadsafe, and you are trying to use a threaded MPM. One solution to fix this is to use a non-threaded MPM. Try replacing  with :

and restart .

## AH00534: httpd: Configuration error: No MPM loaded.
You might encounter this error after a recent upgrade. This is only the result of a recent change in  that you might not have reproduced in your local configuration. To fix it, uncomment the following line:

and restart .

## AH00072: make_sock: could not bind to address
This can be caused by multiple things. Most common issue being that something is already listening on a given port, check via ss that this is not happening:

 # ss -lnp | grep -e :80 -e :443

If you get any output, stop the given service that's taking up the port or kill the runaway process that is causing the port to be bound, and try again.

Another issue could be that Apache is not starting as root for some reason - try starting it manually and see if you still get the AH0072 error.

 # httpd -k start

Finally, you can also have an error with your configuration and you are listening twice on the given port. Following is an example of a bad configuration that will trigger this issue:

 Listen 0.0.0.0:80
 Listen === AH01071: Got error 'Primary script unknown' ===

This can be caused by  in the php-fpm systemd unit file if you are serving files in  such as in a virtual host environment. You can disable this feature by editing the php-fpm unit file and restarting . Alternatively, move your document root.

## Changing the max_execution_time in php.ini has no effect
If you changed the  in  to a value greater than 30 (seconds), you may still get a  response from Apache after 30 seconds. To solve this, add a  directive to your http configuration right before the  block:

and restart .

## PHP-FPM: errors are not being logged separately per virtual host
If you have multiple virtual hosts, it may be desirable to have each of them output their error logs to separate files (using the ErrorLog Apache directive). If this is not working for you, confirm that PHP-FPM is configured to log errors to syslog:

It is also possible that the pool configuration is overriding it. Ensure the following line is commented out:
