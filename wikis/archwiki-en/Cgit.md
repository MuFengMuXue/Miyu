# Cgit

cgit is an attempt to create a fast web interface for the git version control system, using a built in cache to decrease pressure on the git server.

## Installation
Install the  package.

To use cgit a web server must be installed and configured on the system.

## Configuration of web server
## Apache
Add the following to the end of your :

 ScriptAlias /cgit "/usr/lib/cgit/cgit.cgi/"
 Alias /cgit-css "/usr/share/webapps/cgit/"

    AllowOverride None
    Options None
    Require all granted

    AllowOverride None
    Options ExecCGI FollowSymlinks
    Require all granted

or alternatively add it to a separate file like
and then add the following to the end of :

 # cgit configuration
 Include conf/extra/cgit.conf

This allows you to access cgit via your.server.com/cgit. Make sure that Apache is configured to permit CGI execution by having the following uncommented in :

    LoadModule cgid_module modules/mod_cgid.so

    LoadModule cgi_module modules/mod_cgi.so

then restart  to apply these changes. For further details about CGI execution with Apache, see https://httpd.apache.org/docs/2.4/howto/cgi.html.

## Lighttpd
The following configuration will let you access cgit through http://your.server.com/git or http://your.server.com/cgit. The cgit url is not perfect (for example you will see "cgit.cgi" in all repos' url) but works.

Create the file :
 server.modules += ( "mod_cgi", "mod_alias" )

 $HTTP=~ "^/cgit" {
     server.document-root = "/usr/share/webapps/"
     server.indexfiles = ("cgit.cgi")
     cgi.assign = ("cgit.cgi" => "")
     mimetype.assign = ( ".css" => "text/css" )
 }

 alias.url += (
     "/git" => "/usr/share/webapps/cgit/cgit.cgi",
 )
 $HTTP["url" =~ "^/git" {
     cgi.assign = ( "" => "" )
 }
And include this file in :
 include "conf.d/cgit.conf"
and restart the .

## Lighttpd sub-domain
This alternative Lighttpd configuration will serve cgit on a sub-domain like git.example.com with optional SSL support, and rewrites creating nice permalinks:

{{bc|1=
server.modules += ( "mod_cgi", "mod_rewrite" )

#$SERVER== ":443" {
$SERVER["socket" == ":80" {
    #ssl.engine                    = "enable"
    #ssl.pemfile                   = "/etc/lighttpd/ssl/git.example.com.pem"

    server.name          = "git.example.com"
    server.document-root = "/usr/share/webapps/cgit/"

    index-file.names     = ( "cgit.cgi" )
    cgi.assign           = ( "cgit.cgi" => "" )
    mimetype.assign      = ( ".css" => "text/css" )
    url.rewrite-once     = (
        "^/cgit/cgit.css"   => "/cgit.css",
        "^/cgit/cgit.png"   => "/cgit.png",
        "^/(=> "/cgit.cgi?url=$1&$2",
    )
}
}}

## Nginx
## Using fcgiwrap
The following configuration uses  and will serve cgit on a subdomain like .

Start and enable . Then, configure Nginx:

{{hc|/etc/nginx/nginx.conf|2=
worker_processes          1;

events {
  worker_connections      1024;
}

http {
  include                 mime.types;
  default_type            application/octet-stream;
  sendfile                on;
  keepalive_timeout       65;
  gzip                    on;

  # Cgit
  server {
    listen                80;
    server_name           git.example.com;
    root                  /usr/share/webapps/cgit;
    try_files             $uri @cgit;

    # Configure HTTP transport
    location ~ /.+/(info/refs|git-upload-pack) {
        include             fastcgi_params;
        fastcgi_param       SCRIPT_FILENAME     /usr/lib/git-core/git-http-backend;
        fastcgi_param       PATH_INFO           $uri;
        fastcgi_param       GIT_HTTP_EXPORT_ALL 1;
        fastcgi_param       GIT_PROJECT_ROOT    /srv/git;
        fastcgi_param       HOME                /srv/git;
        fastcgi_pass        unix:/run/fcgiwrap.sock;
    }

    location @cgit {
      include             fastcgi_params;
      fastcgi_param       SCRIPT_FILENAME /usr/lib/cgit/cgit.cgi;
      fastcgi_param       PATH_INFO       $uri;
      fastcgi_param       QUERY_STRING    $args;
      fastcgi_param       HTTP_HOST       $server_name;
      fastcgi_pass        unix:/run/fcgiwrap.sock;
    }
  }
} }}

## Using uwsgi
The following example will setup cgit using the native cgi plugin for uwsgi.

First, install  and .

Add below server block to your configuration:

{{hc|/etc/nginx/nginx.conf|
server {
  listen 80;
  server_name git.example.com;
  root /usr/share/webapps/cgit;

  # Serve static files with nginx
  location ~* ^.+(cgit.(css|png)|favicon.ico|robots.txt) {
    root /usr/share/webapps/cgit;
    expires 30d;
  }
  location / {
    try_files $uri @cgit;
  }
  location @cgit {
    gzip off;
    include uwsgi_params;
    uwsgi_modifier1 9;
    uwsgi_pass unix:/run/uwsgi/cgit.sock;
  }
}
}}

Add a uwsgi configuration for cgit.

Enable and start the corresponding socket .

## Caddy
The following configuration uses  and will serve cgit on a subdomain like .

Make sure to give Caddy ownership of the socket and set permissions correctly by editing the systemd socket as follows:

Start and enable . Then, configure Caddy:

{{hc|/etc/caddy/conf.d/cgit|2=
git.example.com

@assets path /cgit.css /cgit.js /cgit.png /favicon.ico /robots.txt
handle @assets {
	root * /usr/share/webapps/cgit
	file_server
}

reverse_proxy unix//run/fcgiwrap.sock {
	transport fastcgi {
		env SCRIPT_FILENAME /usr/lib/cgit/cgit.cgi
	}
}
}}

## h2o
Package  has its own CGI wrapper fastcgi-cgi, which supports cgit with the following configuration.

## Configuration of cgit
See  for the list of all configuration options.

## Basic configuration
Before you can start adding repositories you will first have to create the basic cgit configuration file at .

 #
 # cgit config
 #

 # The defaults
 #css=/cgit.css
 #logo=/cgit.png

 # Following lines work with the above Apache config
 #css=/cgit-css/cgit.css
 #logo=/cgit-css/cgit.png

 # Following lines work with the above Lighttpd config
 #css=/cgit/cgit.css
 #logo=/cgit/cgit.png

 # Allow http transport git clone
 #enable-http-clone=0

 # if you do not want that webcrawler (like google) index your site
 robots=noindex, nofollow

 # if cgit messes up links, use a virtual-root. For example, cgit.example.org/ has this value:
 virtual-root=/

## Adding repositories
Now you can add your repos:

 #
 # List of repositories.
 # This list could be kept in a different file (e.g. '/etc/cgitrepos')
 # and included like this:
 #   include=/etc/cgitrepos
 #

 repo.url=MyRepo
 repo.path=/srv/git/MyRepo.git
 repo.desc=This is my git repository

 # For a non-bare repository (repository with the working tree)
 repo.url=MyOtherRepo
 repo.path=/srv/git/MyOtherRepo/.git
 repo.desc=That's my other git repository

Or else, it is also possible to configure cgit to automatically search for the repo:

 scan-path=/srv/git/

If you use the method above, add the descriptions to  file and add the following lines to show the author:

If you are coming from gitweb and want to keep the descriptions and owner information, then use:

 enable-git-config=1

## Syntax highlighting
cgit supports syntax highlighting when viewing blobs. To enable syntax highlighting, you have several options.

## Using python-pygments
Install  and add the filter in

 source-filter=/usr/lib/cgit/filters/syntax-highlighting.py

To change the coloring style, modify the  argument that is passed to  in the  file. For instance, to change the coloring style to 'tango':

  formatter = HtmlFormatter(encoding='utf-8', style='tango')

To get a list of all coloring styles that are available, do:

  $ python
  >>> from pygments.styles import get_all_styles
  >>> list(get_all_styles())
  ['manni', 'igor', 'xcode', 'vim', 'autumn', 'vs', 'rrt', 'native', 'perldoc', 'borland', 'tango', 'emacs', 'friendly', 'monokai', 'paraiso-dark', 'colorful', 'murphy', 'bw', 'pastie', 'paraiso-light', 'trac', 'default', 'fruity'

## Using highlight
Install the  package.

Copy  to . Then, in the copied file, comment out version 2 and comment in version 3.
You may want to add  to the options of highlight for a more colorful output without editing cgit's css file.

Enable the filter in

 source-filter=/usr/lib/cgit/filters/syntax-highlighting-edited.sh

## Formatting the about page
cgit can display a formatted about page with Markdown, reStructuredText, man page syntax, text files, and html files.

* For Markdown formatting, install .
* For reStructeredText formatting, install .
* To use the man page syntax install .

The script  is used with the about-filter or repo.about-filter in . For example:

 about-filter=/usr/lib/cgit/filters/about-formatting.sh
 readme=:README
 readme=:README.md

The way  works is by running particular scripts in the  subdirectory based on the input file's extension.
The above configuration allows plain text and Markdown formatting as long as  or  is located in the root of the repo's default branch and the script is given executable permission.

For a more lightweight Markdown converter, install  and create a new filter  that runs .

## Integration
## Gitosis
If you want to integrate with gitosis you will have to run two commands to give Apache permission to look through the folder.

 # chgrp http /srv/gitosis
 # chmod a+rx /srv/gitosis

## Gitolite
If you added repositories managed by gitolite you have to change the permissions so the web server can access the files.

* Add the http user to the gitolite group:
**  as the root user.
* Change permission for future repositories:
** Edit . Change the  to
** See also: https://gitolite.com/gitolite/rc.html#specific-variables
* Change permission for the gitolite home directory, and existing repositories. Run the following two commands:
** as the root user.
** as the root user.
* If you use scan-path in conjunction with project-list, change permission for the project list. Run the following command:
** as the root user.

## Troubleshooting
The following troubleshooting subsections largely outline issues that are caused by the order of settings in the cgit configuration file. To be safe, try to ensure that all global settings are defined before scan-path.

## snapshots does not show properly
If you have enabled scan-path as well as snapshots, the order in cgitrc matters. According to cgit mailing list, snapshots should be specified before scan-path

 snapshots=tar.gz tar.bz2 zip
 scan-path=/path/to/your/repositories

## readme files are not found, about tab not shown
If you have added one or more readme entries, which define the files that cgit will search for when populating the about tab, and you are sure that they match the README files in your repository but the about tab does not show, ensure that readme entries are specified before scan-path.

## source-filter does not work properly
If you have enabled scan-path, again, the order in cgitrc matters. source-filter should be specified before scan-path, otherwise it will have no effect.
