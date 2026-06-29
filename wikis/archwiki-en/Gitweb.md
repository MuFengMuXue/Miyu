# Gitweb

zh-Hans:Gitweb
Gitweb is the default web interface that comes with Git.

Gitweb actually supports FCGI natively, so you do not need to wrap it as a CGI script.== Installation ==

To install Gitweb you first have to install  and a web server. Now, if you want to quickly test it, see the help of . Otherwise, if you want a comprehensive setup, keep reading.

For all the examples below, you need to install the  package. ()

## Configuration of web server
## Apache
Add the following to the end of your :

 Alias /gitweb "/usr/share/gitweb"

    DirectoryIndex gitweb.cgi
    Options ExecCGI
    Require all granted

    SetHandler cgi-script

    SetEnv  GITWEB_CONFIG  /etc/gitweb.conf

or alternatively add it to a separate file like
and then add the following to the end of :

 # gitweb configuration
 Include conf/extra/gitweb.conf

If Apache refuses to display Gitweb, but prints the plain source code of the perl script instead, it is very likely that Apache is not configured to permit CGI execution. Make sure that the following is uncommented in :

    LoadModule cgid_module modules/mod_cgid.so

    LoadModule cgi_module modules/mod_cgi.so

then restart  to apply these changes. For further details about CGI execution with Apache, see https://httpd.apache.org/docs/2.4/howto/cgi.html.

## Lighttpd
Add the following to :
 server.modules += ( "mod_alias", "mod_cgi", "mod_redirect", "mod_setenv" )
 url.redirect += ( "^/gitweb$" => "/gitweb/" )
 alias.url += ( "/gitweb/" => "/usr/share/gitweb/" )
 $HTTP["url" =~ "^/gitweb/" {
        setenv.add-environment = (
                "GITWEB_CONFIG" => "/etc/gitweb.conf",
                "PATH" => env.PATH
        )
        cgi.assign = ( ".cgi" => "" )
        server.indexfiles = ( "gitweb.cgi" )
 }

then restart  to apply these changes.
You may also need to add  to the  line for GitWeb to display properly.

## Nginx
Append this location to your nginx configuration (you might want to change the location):

{{hc|/etc/nginx/nginx.conf|
location /gitweb.cgi {
    include fastcgi_params;
    gzip off;
    fastcgi_param   SCRIPT_FILENAME  /usr/share/gitweb/gitweb.cgi;
    fastcgi_param   GITWEB_CONFIG  /etc/gitweb.conf;
    fastcgi_pass    unix:/run/fcgiwrap.sock;
}

location / {
    root /usr/share/gitweb;
    index gitweb.cgi;
}
}}

If you follow Nginx#CGI implementation, try replacing  with .

Finally, install  and start/enable .

## Caddy
Replace the  block of your configuration with:

{{hc|/etc/caddy/Caddyfile|
http:// {
	root * /usr/share/gitweb
	php_fastcgi unix//run/fcgiwrap.sock {
		index gitweb.cgi
		split .cgi
	}
	file_server
}
}}

Install  and start/enable . Then restart .

To use a subpath / subdirectory, wrap the above , , and  directives in a single . Gitweb will parse the  passed from  and rewrite it's relative paths automatically.

## Configuration of Gitweb
See  for the list of all configuration options.

## Basic configuration
Open (or create if it does not exist) the file  and place this in it:

To enable "blame" view (showing the author of each line in a source file), add the following line:

 $feature{'blame'}{'default'} = Now that the configuration is done, restart your web server.

## Adding repositories
To add a repository go to your repository folder, make your repository like so:

 $ mkdir my_repository.git
 $ git init --bare my_repository.git/
 $ cd my_repository.git/
 $ touch git-daemon-export-ok
 $ echo "Short project's description" > description

Next open the  file and add this:

This will fill in the "Owner" field in Gitweb. It is not required.

This assumes that you want to have this repository as "central" repository storage where you push your commits to so the git-daemon-export-ok and --bare are here to have minimal overhead and to allow the git daemon to be used on it.

That is all for making a repository. You can now see it on your http://localhost/gitweb (assuming everything went fine). You do not need to restart Apache for new repositories since the Gitweb CGI script simply reads your repository folder.

## Syntax highlighting
To enable syntax highlighting with Gitweb, you have to first install the  package:

When highlight has been installed, simply add this line to your :
 $feature{'highlight'}{'default'} = [1;

Save the file and highlighting should now be enabled.
