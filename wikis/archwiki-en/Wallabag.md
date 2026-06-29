# Wallabag

wallabag is a self hostable application for saving web pages.

## Installation
Install the  package.

## Configuration
## PHP
Configure php to allow wallabag in  to work and configure wallabag using .

Give the wallabag user write permissions to

A list of required php modules can be found here. The following snippet is provided for brevity.

## Wallabag
Once wallabag has been properly configured, commands must be run as the wallabag user in order to initialise the database and application state.

## Database
Supported databases are:

* PostgreSQL
* MariaDB

The setup and configuration are not covered here.

## Application Server
## php-fpm
It is recommended to make a copy of  and modify that. If you want to use it, you must change listen to the one which is different from

## Web Server
## nginx
The below configuration is sourced from upstream documentation and slightly amended and modified based on custom php-fpm configure:

{{hc|/etc/nginx/example.conf|2=

server {
    server_name domain.tld www.domain.tld;
    root /usr/share/wallabag/web;

    location / {
        # try to serve file directly, fallback to app.php
        try_files $uri /app.php$is_args$args;
    }
    location ~ ^/app\.php(/|$) {
        fastcgi_pass unix:/run/php-fpm/php-fpm-wallabag.sock;
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        # When you are using symlinks to link the document root to the
        # current version of your application, you should pass the real
        # application path instead of the path to the symlink to PHP
        # FPM.
        # Otherwise, PHP's OPcache may not properly detect changes to
        # your PHP files (see https://github.com/zendtech/ZendOptimizerPlus/issues/126
        # for more information).
        fastcgi_param  SCRIPT_FILENAME  $realpath_root$fastcgi_script_name;
        fastcgi_param DOCUMENT_ROOT $realpath_root;
        # Prevents URIs that include the front controller. This will 404:
        # http://domain.tld/app.php/some-path
        # Remove the internal directive to allow URIs like this
        internal;
    }

    # return 404 for all other php files not matching the front controller
    # this prevents access to other php files you don't want to be accessible.
    location ~ \.php$ {
        return 404;
    }

    error_log /var/log/nginx/wallabag_error.log;
    access_log /var/log/nginx/wallabag_access.log;
}

}}

Generic configuration for other web servers can be found upstream.

## Troubleshooting
## Upgrading between versions
There are upgrade instructions available, dependent on the old and new versions. Generally, cache must be cleaned and database migrations performed by the wallabag user, as shown below.
