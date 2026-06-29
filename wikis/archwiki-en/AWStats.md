# AWStats

From AWStats - Free log file analyzer for advanced statistics:

:AWStats is a free powerful and featureful tool that generates advanced web, streaming, ftp or mail server statistics, graphically. This log analyzer works as a CGI or from command line and shows you all possible information your log contains, in few graphical web pages. It uses a partial information file to be able to process large log files, often and quickly. It can analyze log files from all major server tools like Apache log files (NCSA combined/XLF/ELF log format or common/CLF log format), WebStar, IIS (W3C log format) and a lot of other web, proxy, wap, streaming servers, mail servers and some ftp servers.

## Installation
Install the  package. When Apache HTTP Server is used as a web server, the  package is required as well.

## Configuration
## Enable mod_perl for Apache
To enable  in Apache, you should add following line to Apache configuration ():

 LoadModule perl_module modules/mod_perl.so

## Configure Apache to log for AWStats
By default AWStats requires Apache to record access logs as 'combined'. Unless you want a different behavior, you should set your access log format as 'combined'. To do so, your Apache configuration should look like this:

     ServerAdmin zxc@returnfalse.net
     DocumentRoot "/srv/http/xxx"
     ServerName www.returnfalse.net
     ErrorLog "/var/log/httpd/returnfalse-error_log"
     CustomLog "/var/log/httpd/returnfalse-access_log" combined

The important line here is:

 CustomLog "/var/log/httpd/returnfalse-access_log" combined

## Including AWStats configuration in Apache's configuration
If you set the log format, then next step is including AWStats configuration file in Apache. The package in the AUR has a default one, and it is working without any problem, if you enable the following lines in the Apache configuration ():

     LoadModule cgid_module modules/mod_cgid.so

     LoadModule cgi_module modules/mod_cgi.so

But in case you want to create your own configuration, you can use this (using mod_perl instead of cgid_module or cgi_module):

 LoadModule perl_module modules/mod_perl.so

 Alias /awstatsclasses "/usr/share/webapps/awstats/classes/"
 Alias /awstatscss "/usr/share/webapps/awstats/css/"
 Alias /awstatsicons "/usr/share/webapps/awstats/icon/"
 ScriptAlias /awstats/ "/usr/share/webapps/awstats/cgi-bin/"

     AddHandler perl-script .pl
     AddHandler perl-script .cgi
     PerlResponseHandler ModPerl::Registry
     PerlOptions +ParseHeaders

     Options None
     AllowOverride None
     Require all granted

 DirectoryIndex index.html index.htm awstats.pl

Include this file (in AUR case, the path is ) to Apache's main configuration:

 Include conf/extra/httpd-awstats.conf

Now if you have done all steps correctly, you should be able to see AWStats running on http://localhost/awstats/awstats.pl after restarting Apache's  unit.

One last thing, which is the actual aim, make AWStats read logs and convert them to stats.

## AWStats Configuration
The package comes with an script to update stats shown on AWStats. This script reads AWStats configuration files in  and updates the stats for the sites that are defined in these configuration files. Instead of creating these configuration files, you can use AWStats' configuration tool. Run:

 # perl /usr/share/awstats/tools/awstats_configure.pl

and follow the instructions. If you successfully created a configuration file there is one thing that you should modify manually. Open the configuration file created by  with your favorite text editor. Then find the line on which  variable is defined, and set it as the path that Apache logs accesses (which you set to be logged as 'combined' format before):

 # LogFile=/var/log/httpd/returnfalse-access_log

Now you can run the script to test the results, e.g. if you have a  then run

 # /usr/share/awstats/tools/awstats_buildstaticpages.pl config=apache -update -awstatsprog=/usr/share/webapps/awstats/cgi-bin/awstats.pl -dir=/srv/http/awstats

## Nginx
If your web server software is nginx, follow steps below:

1. Install awstats as described above. It is necessary to get the folders and files owned by user  and group  with the following command:

 # chown -R http:http /usr/share/webapps/awstats/

2. Use the awstats configuration tool to generate a site configuration file as described above. Make sure the following lines are set correctly:

 LogFile="/var/log/nginx/access.log"
 LogFormat=1

3. To make the Perl scripts of awstats work on nginx, create  with the following code:

  array("pipe", "r"),  // stdin is a pipe that the child will read from
    1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
    2 => array("pipe", "w")   // stderr is a file to write to
 );
 $newenv = $_SERVER;
 $newenv= $_SERVER["X_SCRIPT_FILENAME";
 $newenv= $_SERVER["X_SCRIPT_NAME";
 if (is_executable($_SERVER{
    $process = proc_open($_SERVER["X_SCRIPT_FILENAME", $descriptorspec, $pipes, NULL, $newenv);
    if (is_resource($process)) {
        fclose($pipes$head = fgets($pipes[1);
        while (strcmp($head, "\n")) {
            header($head);
            $head = fgets($pipes}
        fpassthru($pipes[1);
        fclose($pipesfclose($pipes[2);
        $return_value = proc_close($process);
    } else {
        header("Status: 500 Internal Server Error");
        echo("Internal Server Error");
    }
 } else {
    header("Status: 404 Page Not Found");
    echo("Page Not Found");
 }
 ?>

4. Add these directives to the domain nginx configuration file:

 location ^~ /awstatsicons {
    alias /usr/share/webapps/awstats/icon/;
    access_log off;
 }
 location ^~ /awstatscss {
    alias /usr/share/webapps/awstats/examples/css/;
    access_log off;
 }
 location ^~ /awstatsclasses {
    alias /usr/share/webapps/awstats/examples/classes/;
    access_log off;
 }
 location ~ ^/cgi-bin/.*\.(cgi|pl|py|rb) {
    gzip off;
    fastcgi_pass  unix:/var/run/php-fpm/php-fpm.sock;
    fastcgi_index cgi-bin.php;
    fastcgi_param SCRIPT_FILENAME    /etc/nginx/cgi-bin.php;
    fastcgi_param SCRIPT_NAME        /cgi-bin/cgi-bin.php;
    fastcgi_param X_SCRIPT_FILENAME  /usr/share/webapps/awstats$fastcgi_script_name;
    fastcgi_param X_SCRIPT_NAME      $fastcgi_script_name;
    fastcgi_param QUERY_STRING       $query_string;
    fastcgi_param REQUEST_METHOD     $request_method;
    fastcgi_param CONTENT_TYPE       $content_type;
    fastcgi_param CONTENT_LENGTH     $content_length;
    fastcgi_param GATEWAY_INTERFACE  CGI/1.1;
    fastcgi_param SERVER_SOFTWARE    nginx;
    fastcgi_param REQUEST_URI        $request_uri;
    fastcgi_param DOCUMENT_URI       $document_uri;
    fastcgi_param DOCUMENT_ROOT      $document_root;
    fastcgi_param SERVER_PROTOCOL    $server_protocol;
    fastcgi_param REMOTE_ADDR        $remote_addr;
    fastcgi_param REMOTE_PORT        $remote_port;
    fastcgi_param SERVER_ADDR        $server_addr;
    fastcgi_param SERVER_PORT        $server_port;
    fastcgi_param SERVER_NAME        $server_name;
    fastcgi_param REMOTE_USER        $remote_user;
 }

5. You can access the awstats page of your site at "http://your_domain.com/cgi-bin/awstats.pl?config=your_domain.com" Optionally, you may want to add this rewrite rule to the nginx site configuration file:

 location ~ ^/awstats {
    rewrite ^ http://your_domain.com/cgi-bin/awstats.pl?config=your_domain.com;
 }

With this, you can access your awstats page simply by typing "http://your_domain.com/awstats" in the address bar of your browser.

## Caddy
If your web server software is , install  to get FastCGI working, then change your Caddyfile using the template below as appropriate for your configuration.

1. Install awstats as described above. It is necessary to get the folders and files owned by user  and group  with the following command:

 # chown -R http:http /usr/share/webapps/awstats/

2. Use the awstats configuration tool to generate a site configuration file as described above. Make sure the following lines are set correctly:

 LogFile="/var/log/caddy/site_combined.log"
 LogFormat=1

3. Create your Caddyfile  configuration file with these directives:

{{bc|
awstats.hostname.com {
#basicauth /cgi-bin username password
root /usr/share/webapps/awstats
log / /var/log/caddy/site_combined.log "{combined}"
gzip

fastcgi /cgi-bin/ unix:/var/run/fcgiwrap.sock {
env SCRIPT_DIR /usr/share/webapps/awstats/cgi-bin/
env SCRIPT_FILENAME /usr/share/webapps/awstats/cgi-bin/awstats.pl
        }
}
awstats.hostname.com/awstatsclasses {
        root /usr/share/webapps/awstats/classes
}
awstats.hostname.com/awstatscss {
        root /usr/share/webapps/awstats/css
}
awstats.hostname.com/awstatsicons/ {
        root /usr/share/webapps/awstats/icon
}
awstats.hostname.com/js {
	root /usr/share/webapps/awstats/js
}
}}

You should now be able to view your site at the following URL:

 https://awstats.hostname.com/cgi-bin/awstats.pl?config=awstats.hostname.com

## Generating Statistics
You can generate the latest statistics of all your sites manually by issuing the following command:

 /usr/share/awstats/tools/awstats_updateall.pl now -awstatsprog=/usr/share/webapps/awstats/cgi-bin/awstats.pl

## systemd
This process can be automated via an (hourly) systemd timer script. You will first need to create the  and  units:

You can then start the service and enable the timer.

## cron
This process can be automated by cron. See AWStats cron template:  However, if you are using logrotate, you have to make sure the cronjob starts right before logrotate runs. Otherwise, statistics will be lost because loratate will change the access log file name to a different name not accessible by awstats. A better way to deal with this is to use web server specific logrotate script normally located in /etc/logrotate.d to trigger the awstats calculation. An example of nginx logrotate script is provided here. Note the addition of a prerotate directive:

 /var/log/nginx/*log {
  daily
  missingok
  notifempty
  create 640 http log
  compress
  sharedscripts
  prerotate
    # Trigger awstats computation
    /usr/share/awstats/tools/awstats_updateall.pl now -awstatsprog=/usr/share/webapps/awstats/cgi-bin/awstats.pl
  endscript
  postrotate
     test ! -r /run/nginx.pid || kill -USR1 `cat /run/nginx.pid`
  endscript
 }

## GeoIP (optional)
To add geo ip support, install Geo::IP module using cpan. (See Perl#CPAN.pm for more details.) Alternatively, install . Add the following line to each of the awstats site configuration files located in :

 LoadPlugin="geoip GEOIP_STANDARD /usr/share/GeoIP/GeoIP.dat"

If you install  you can also add these to your awstats site configuration:

 LoadPlugin="geoip_city_maxmind GEOIP_STANDARD /usr/share/GeoIP/GeoIPCity.dat"
 LoadPlugin="geoip_asn_maxmind GEOIP_STANDARD /usr/share/GeoIP/GeoIPASNum.dat+http://enc.com.au/itools/autnum.php?asn="
