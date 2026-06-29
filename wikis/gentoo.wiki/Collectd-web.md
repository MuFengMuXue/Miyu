**Resources**

[[]][Home](http://collectdweb.appspot.com/)

[[]][Twitter](https://twitter.com/collectdweb)

[[]][Facebook](https://www.facebook.com/Collectd-web/132686910095150)

[[]][Google user group](https://groups.google.com/forum/?fromgroups#!forum/collectd-web-users/)

**collectd-web** is a web-based Perl CGI front-end for RRD data collected by [collectd](https://wiki.gentoo.org/wiki/Collectd "Collectd").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Web server]](#Web_server)
        -   [[1.2.1] [Built-in web server]](#Built-in_web_server)
        -   [[1.2.2] [Apache]](#Apache)
        -   [[1.2.3] [nginx]](#nginx)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)

## [Installation]

### [Emerge]

Install [[[www-apps/collectd-web]](https://packages.gentoo.org/packages/www-apps/collectd-web)[]]:

`root `[`#`]`emerge --ask collectd-web`

To display the graphs, [[[net-analyzer/rrdtool]](https://packages.gentoo.org/packages/net-analyzer/rrdtool)[]] needs the USE flags `graph` and `perl`.

### [Web server]

You need also a [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers").

The CGI scripts have to be executable:

`root `[`#`]`chmod +x /usr/share/webapps/collectd-web/*/hostroot/cgi-bin/*.cgi`

#### [Built-in web server]

The collectd-web project offers a simple web server to process the CGI scripts:

`root `[`#`]`cd /usr/share/webapps/collectd-web/*/hostroot/ `

`root `[`#`]`wget `[`https://raw.github.com/httpdss/collectd-web/0.4.1/runserver.py`](https://raw.github.com/httpdss/collectd-web/0.4.1/runserver.py)` `

`root `[`#`]`python2 runserver <ip>  `

Now you need to set up a reverse proxy which will serve static files from [/usr/share/webapps/collectd-web/0.4.0/htdocs] for [/] and for /cgi-bin/ it will proxy the request to the above set up \<ip\> \.

#### [Apache]

It is possible to use [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") to serve the pages. Configuration of the corresponding virtual host needs to be adjusted so that it knows where to find cgi scripts of collectd-web. For default vhost make following modification:

[FILE] **`/etc/apache2/vhosts.d/00_default_vhost.conf`Defining alias to cgi scripts location**

    <VirtualHost *:80>
    ...
        ScriptAlias /collectd-web/cgi-bin/ "/var/www/localhost/cgi-bin/"
    ...
    </VirtualHost>

#### [nginx]

This is an example server section for [nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") using [[[www-misc/fcgiwrap]](https://packages.gentoo.org/packages/www-misc/fcgiwrap)[]]. This setup does not require using the built-in webserver and downloading the extra python script.

`root `[`#`]`emerge --ask fcgiwrap`

`root `[`#`]`systemctl enable fcgiwrap.socket `

`root `[`#`]`systemctl start fcgiwrap.socket `

[FILE] **`/etc/nginx/conf.d/collectd-web.conf`Example nginx confiugration for collectd**

    server

        location /cgi-bin/
    }

Save this as a separate file as suggested above and include it in [/etc/nginx/nginx.conf] and restart nginx:

`root `[`#`]`systemctl restart nginx`

The web interface is then available on [`http://localhost`](http://localhost).

## [Configuration]

Configure [Collectd#rrdtool_plugin](https://wiki.gentoo.org/wiki/Collectd#rrdtool_plugin "Collectd")

Define where collectd-web shall look for rrd files:

[FILE] **`/etc/collectd/collection.conf`**

    datadir: "/var/lib/collectd/rrd"

## [Usage]

Point your browser at the reverse proxy or (in case you using default Apache configuration) at [http://localhost/collectd-web](http://localhost/collectd-web).