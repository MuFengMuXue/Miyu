# Munin

Munin is a networked resource monitoring tool that can help analyze resource trends and bottlenecks.
Munin has a master/node architecture in which the master regularly fetches the data from the nodes and presents the information in graphs through a web interface.
A default installation provides a lot of graphs with almost no work and new graphs can be easily created added as plugins. == Installation ==

Install the  package on the master machine and  on the devices that you whish to monitor.

You can also install them both on the same machine so that the master machine monitors itself.

Further documentation may be found on the [https://munin-monitoring.org/wiki/Documentation Munin documentation wiki.

## Configuration
## Munin master
## Directories
Create a directory where the munin-master will write the generated HTML and graph images. The munin user must have write permission to this directory.

The following example uses , so the generated output can be viewed at http://localhost/munin/, provided that a web server is installed and running:

 # mkdir /srv/http/munin
 # chown munin:munin /srv/http/munin

Uncomment the  entry in  and change it to the directory created in the previous step:

 htmldir /srv/http/munin

## Cron
## crontab
Run the following to have Munin collect data and update the generated HTML and graph images every 5 minutes:

 # crontab /etc/munin/munin-cron-entry -u munin

Configure the email server to send mails to the munin user. If using postfix, add the following:

And run:

 # newaliases

## systemd timer
Instead of a cron job a systemd timer can be used.

This needs a service unit configuration:

And a timer unit configuration:

Now, reload systemd configuration, enable/start  and verify that everything is working:

 # journalctl --unit munin-cron.service
 # less /var/log/munin/munin-update.log

## Permissions
When  is enabled in  ensure the directory  is owned by user and group  so that the  script is able to write the png files to this directory.

 # chown munin: /var/lib/munin/cgi-tmp

## Testing
Once  is configured to run Munin will be ready to start generating graphs. Ensure the  is running on each of the nodes. It may be useful to jump ahead to the #Munin node section and return here once the node are up and running.

By runnning the  command manually as the  user, it will trigger the generation of HTML and graph images immediately without having to wait for the next cron run:

 munin-cron

If the munin logging is configured, the logs are usually found in . Watching the  log in a seperate terminal after running the  command can be helpful in diagnosing issues.

 # tail -f /var/log/munin/munin-update.log

And finally test the interface by pointing your browser to the output directory or [http://localhost/munin/ http://localhost/munin/.

## Munin node
## Daemon
On the nodes, enable/start .

## IPv6
For IPv6 support on munin-node, using:

Install:

*
*

## Customization
Before running munin, you might want to setup the hostname of your system. In , the default hostname is . This can be altered to any preferred hostname. The hostname will be used to group and name the  files in  and further, used to group the html files and graphs in your selected munin-master directory.

## Plugins
Run  with the  option to have Munin suggest plugins it thinks will work on your installation:

 # munin-node-configure --suggest

If there is a suggestion for a plugin you want to use, follow that suggestion and run the command again. When you are satisfied with the plugins suggested by , run it with the  option to have the plugins configured:

 # munin-node-configure --shell | sh

## Adding
Basically all plugins are added in the following manner (although there are exceptions, review each plugin!):

Download a plugin, then copy or move it to :

 # cp plugin /usr/lib/munin/plugins/

Then link the plugin to :

 # ln -s /usr/lib/munin/plugins/plugin /etc/munin/plugins/

Now test your plugin. You do not need to use the full path to the plugin,  should be able to figure it out:

 # munin-run plugin

And restart . Finally, refresh the web page.

## Additional plugins
There are many Munin plugins out there just waiting to be installed. The MuninExchange is an excellent place to start looking, and if you cannot find a plugin that does what you want it is easy to write your own. Have a look at Developing Plugins at the Munin documentation wiki to learn how.

## Removing
If you want to remove a plugin, simply delete the linked file in  - there is no need to remove the plugin from .

 # rm /etc/munin/plugins/plugin

## Debugging
If you come across a plugin that is not working as expected (for example giving you no output at all) it might be interesting to run it directly. Fortunately there is a way to do this. Following the instructions until here, you will for example notice, that the plugin  gives no output at all, when enabled. In order to run the plugin directly:

 # munin-run apache_accesses

The following error:

 LWP::UserAgent not found at /etc/munin/plugins/apache_accesses line 86.

indicates that a perl function could not be found. To resolve the problem, install the missing library, in this case, .

## Permissions
Because many plugins read log files, it is useful to add  user into  group:

 # usermod -a -G log munin

## Web server (optional)
This guide sets up Munin to generate static HTML and graph images and write them in a directory of your choosing. You can view these generated files locally with any web browser. If you want to view the generated files from a remote machine, then you will need to install and configure one of the following web servers:

* Apache HTTP Server
* Lighttpd
* Nginx

Or one of the other servers found in the web server category.

## Apache
## Apache VirtualHost examples
Based on information found here:
* http://guide.munin-monitoring.org/en/stable-2.0/example/webserver/apache-virtualhost.html
* http://munin-monitoring.org/wiki/MuninConfigurationMasterCGI

In the next major release of Munin, things will be much simpler. Check it out:
* https://web.archive.org/web/20180128051736/http://guide.munin-monitoring.org/en/latest/example/webserver/apache-virtualhost.html

## Basic static HTML
    ServerName localhost
    ServerAdmin  root@localhost

    DocumentRoot /srv/http/munin

    ErrorLog /var/log/httpd/munin-error.log
    CustomLog /var/log/httpd/munin-access.log combined

## Static HTML with DynaZoom feature
Install .

You must enable one of these:

*  (or  if using mpm_prefork_module) by uncommenting the line in .
* Or install  and add  in .

    ServerName localhost
    ServerAdmin  root@localhost

    DocumentRoot /srv/http/munin

    ErrorLog /var/log/httpd/munin-error.log
    CustomLog /var/log/httpd/munin-access.log combined

    # Rewrites
    RewriteEngine On

    # Images
    RewriteRule ^/munin-cgi(.*) /usr/share/munin/cgi/$1 # Ensure we can run (fast)cgi scripts

        Require all granted
        Options +ExecCGI

            SetHandler fcgid-script

            SetHandler cgi-script

## DynaZoom Permissions
When Munin cannot draw graphs and logs a similar message to  check to make sure group permissions are set on  so the  directory has writeable group permissions such as .

If group permissions are not set, then

## Full dynamic
Use this VirtualHost if you want to set  and  to . Page loads will take longer because all the HTML and PNG files will be dynamically generated, but the munin-cron run will take less time because it will not execute munin-html and munin-graph. This feature may become necessary for you if your master polls many nodes and the munin-cron risks taking more than 5 minutes.

Install .

You must enable one of these:

*  (or  if using mpm_prefork_module) by uncommenting the line in .
* Or install  and add  in .

    ServerName localhost
    ServerAdmin  root@localhost

    DocumentRoot /srv/http/munin

    ErrorLog /var/log/httpd/munin-error.log
    CustomLog /var/log/httpd/munin-access.log combined

    # Rewrites
    RewriteEngine On

    # Static content in /static
    RewriteRule ^/favicon.ico /etc/munin/static/favicon.ico [L
    RewriteRule ^/static/(.*) /etc/munin/static/$1          # HTML
    RewriteCond %{REQUEST_URI} .html$ [or
    RewriteCond %{REQUEST_URI} =/
    RewriteRule ^/(.*)          /usr/share/munin/cgi/munin-cgi-html/$1 # Images
    RewriteRule ^/munin-cgi(.*) /usr/share/munin/cgi/$1 [L

        Require all granted

    # Ensure we can run (fast)cgi scripts

        Require all granted
        Options +ExecCGI

            SetHandler fcgid-script

            SetHandler cgi-script

## Nginx
## Munin 2.0.x
This example Nginx setup is based on a Munin 2.0.x  master installation. It requires FastCGI and uses the  and  in the  configuration.

Install the ,  and  packages on the Munin-Master.

As we will be using the cgi strategy the systemd socket files need to be enabled. So the  and  sockets are created for the Nginx FastCGI configuration to hook into.

Enable/start  and .

Create the munin vhost configuration file
{{hc|/etc/nginx/sites-available/munin|
server {
    server_name yourhost.example.com;
    listen 80;
    access_log /var/log/nginx/munin-access.log;
    error_log /var/log/nginx/munin-error.log info;
    location ^~ /munin-cgi/munin-cgi-graph/ {
        fastcgi_split_path_info ^(/munin-cgi/munin-cgi-graph)(.*);
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_pass unix:/run/munin/fcgi-graph.sock;
        include fastcgi_params;
    }
    location /munin/static/ {
        alias /etc/munin/static/;
    }
    location /munin/ {
        fastcgi_split_path_info ^(/munin)(.*);
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_pass unix:/run/munin/fcgi-html.sock;
        include fastcgi_params;
    }
}
}}

Then restart the webserver ().

If all goes well, point your browser to your host  and you should see the Munin Overview page.

## Munin 2.1.x
Although Munin 2.1.x versions are not yet available in the Arch repository. It is worth mentioning that the 2.1.x series will no longer use FastCGI and will be replaced with munin-httpd
This page already contains an example configuration.

## Tips and tricks
## MySQL
The MySQL plugin has extra dependencies: , , , and

Additionally it is recommended to access the database through a separate MySQL user. To make another user via the following MySQL commands:

To configure Munin to use this new user, create:

## S.M.A.R.T.
To enable monitoring of S.M.A.R.T. data, install the  package, and use:

Then create the appropriate symlink for each disk to be monitored. As an example for :

## lm_sensors
Install  and configure according to lm_sensors#Configuration. Assuming all goes correctly, create some symlinks:
