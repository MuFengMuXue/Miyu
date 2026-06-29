**Resources**

[[]][Home](https://www.nagios.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Nagios "wikipedia:Nagios")

**Nagios** offers a complete monitoring and alerting for servers, switches, applications, and services.

Nagios is written in perl.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Web server]](#Web_server)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Apache]](#Apache)
    -   [[2.2] [Lighttpd]](#Lighttpd)
    -   [[2.3] [Nginx]](#Nginx)
    -   [[2.4] [Permissions]](#Permissions)
    -   [[2.5] [Boot service]](#Boot_service)
-   [[3] [Testing]](#Testing)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [See also]](#See_also)

## [Installation]

### [Web server]

Decide which web server will be to used and set it up:

-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") with PHP
-   [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd") with [PHP](https://wiki.gentoo.org/wiki/PHP "PHP")
-   [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") with [PHP](https://wiki.gentoo.org/wiki/PHP "PHP") and [fcgiwrap](https://wiki.gentoo.org/index.php?title=Fcgiwrap&action=edit&redlink=1 "Fcgiwrap (page does not exist)")

Once finished return here to and continue reading.

### [USE flags]

Set the proper USE flags for Nagios before it emerging it:

### [USE flags for] [net-analyzer/nagios-core](https://packages.gentoo.org/packages/net-analyzer/nagios-core) [[]] [Nagios core - monitoring daemon, web GUI, and documentation]

  ----------------------------------------------------------------- -------------------------------------
  [`+web`](https://packages.gentoo.org/useflags/+web)               enable web interface
  [`apache2`](https://packages.gentoo.org/useflags/apache2)         Add Apache2 support
  [`classicui`](https://packages.gentoo.org/useflags/classicui)     use the classic web theme
  [`lighttpd`](https://packages.gentoo.org/useflags/lighttpd)       install www-servers/lighttpd config
  [`vim-syntax`](https://packages.gentoo.org/useflags/vim-syntax)   Pulls in related vim syntax scripts
  ----------------------------------------------------------------- -------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-25 23:40] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Do not forget to enable the right USE flags for Nagios plugins ([[[net-analyzer/nagios-plugins]](https://packages.gentoo.org/packages/net-analyzer/nagios-plugins)[]]).

### [Emerge]

Finally install [[[net-analyzer/nagios]](https://packages.gentoo.org/packages/net-analyzer/nagios)[]]:

`root `[`#`]`emerge --ask net-analyzer/nagios`

## [Configuration]

### [Apache]

Enable the Nagios module for Apache:

[FILE] **`/etc/conf.d/apache2`**

    APACHE2_OPTS="... -D NAGIOS"

Since Nagios requires [PHP](https://wiki.gentoo.org/wiki/PHP "PHP") for its web interface, it may needed to be enabled as well if it has not been previously. One way is to simply add `-D PHP5` to `APACHE2_OPTS` and edit [/etc/php/apache2-php\<YOUR_PHP_VERSION\>/php.ini] This should be fine unless PHP is needed for purposes other than hosting Nagios.

If using Apache 2.4 (which is still marked unstable as of April 2015) the [/etc/apache2/modules.d/99_nagios3.conf] file may need to be modified to fit the new authorization directives of Apache 2.4.

Remember to add the `apache` user to group `nagios`:

`root `[`#`]`usermod -a -G nagios apache`

Restart the Apache service to have it recognize the group change:

`root `[`#`]`rc-service apache2 restart`

### [Lighttpd]

Enable the Nagios configuration for Lighttpd:

[FILE] **`/etc/lighttpd/lighttpd.conf`**

    include "nagios.conf"

Configure authentication. More information on how to set this up can be found in the Lighttpd documentation.

[FILE] **`/etc/lighttpd/nagios.conf`**

    $HTTP["url"] =~ "nagios"

Restart the Lighttpd service:

`root `[`#`]`rc-service lighttpd restart`

You may have to create the run folder for lighttpd

`root `[`#`]`mkdir -p /run/lighttpd; chown lighttpd /run/lighttpd`

\

### [Nginx]

See the [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx") guide before continuing if you don\'t have it already setup.

Emerge [[[www-servers/spawn-fcgi]](https://packages.gentoo.org/packages/www-servers/spawn-fcgi)[]] and [[[www-misc/fcgiwrap]](https://packages.gentoo.org/packages/www-misc/fcgiwrap)[]]:

`root `[`#`]`emerge --ask www-servers/spawn-fcgi www-misc/fcgiwrap`

Next, create an init script for a spawn-fcgi instance dedicated to nagios:

`root `[`#`]`ln -s /etc/init.d/spawn-fcgi /etc/init.d/spawn-fcgi.nagios `

`root `[`#`]`cp /etc/conf.d/spawn-fcgi /etc/conf.d/spawn-fcgi.nagios `

Then, configure our spawn-fcgi instance to launch fcgiwrap and listen on a unix socket:

[FILE] **`/etc/conf.d/spawn-fcgi.nagios`**

    # edit these variables:
    FCGI_SOCKET=/run/fcgiwrap.nagios.socket
    FCGI_USER=nagios
    FCGI_GROUP=nginx
    FCGI_EXTRA_OPTIONS="-M 0660"
    FCGI_PORT= # must be empty for the socket to work
    FCGI_PROGRAM=/usr/sbin/fcgiwrap

Don\'t forget to add spawn-fcgi.nagios to the default runlevel and start it:

`root `[`#`]`rc-update add spawn-fcgi.nagios default `

`root `[`#`]`rc-service spawn-fcgi.nagios start `

You may need to change the owner of the /var/nagios folder, so fcgiwrap can access it:

`root `[`#`]`chown nagios:nagios /var/nagios `

Nginx can now be configured to serve our nagios instance. Here\'s an example configuration snippet for nginx, assuming you have defined a php upstream:

[FILE] **`/etc/nginx/nginx.conf`**

    location /nagios
                    fastcgi_pass php;
                    include fastcgi.conf;
                    fastcgi_param SCRIPT_FILENAME $request_filename;
            }

            location /nagios/cgi-bin/
    }

### [Permissions]

Add the user name(s) to the `nagios` group, whom are allowed access to the Nagios service:

`root `[`#`]`gpasswd -a <USER_NAME> nagios`

Once done, completely sign out from all shells and re-login for the update to apply.

### [Boot service]

Start Nagios:

`root `[`#`]`rc-service nagios start`

To start Nagios at boot time, add it the default runlevel:

`root `[`#`]`rc-update add nagios default`

## [Testing]

Open a browser and navigate to [http://localhost/nagios](http://localhost/nagios)

## [Troubleshooting]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=net-analyzer/nagios&order=bug_id%20DESC)[]]

## [See also]

-   [The Gentoo Nagios system monitoring guide](https://wiki.gentoo.org/wiki/Nagios/Guide "Nagios/Guide").