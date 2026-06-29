This page contains [[changes](https://wiki.gentoo.org/index.php?title=Nginx&oldid=1293674&diff=1422582)] which are not marked for translation.

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Nginx/de "Nginx (92% translated)")
-   [English]
-   [Türkçe](https://wiki.gentoo.org/wiki/Nginx/tr "Nginx (23% translated)")
-   [español](https://wiki.gentoo.org/wiki/Nginx/es "Nginx (100% translated)")
-   [français](https://wiki.gentoo.org/wiki/Nginx/fr "Nginx (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Nginx/hu "nginx (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Nginx/ru "nginx (78% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Nginx/zh-cn "Nginx (55% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Nginx/ja "nginx (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Nginx/ko "Nginx (34% translated)")

**Resources**

[[]][Home](https://nginx.org/en/)

[[]][Official documentation](https://nginx.org/en/docs/)

[[]][Package information](https://packages.gentoo.org/packages/www-servers/nginx)

[[]][GitHub](https://github.com/nginx/nginx)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Nginx "wikipedia:Nginx")

**NGINX** is a robust, small, high performance [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers") and reverse proxy server. It is a good alternative to popular web servers like [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") and [lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Expanded USE flags]](#Expanded_USE_flags)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
    -   [[1.4] [Installation verification]](#Installation_verification)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Single site access]](#Single_site_access)
    -   [[2.2] [Multiple site access]](#Multiple_site_access)
    -   [[2.3] [PHP support]](#PHP_support)
    -   [[2.4] [IP address access list]](#IP_address_access_list)
    -   [[2.5] [Basic authentication]](#Basic_authentication)
    -   [[2.6] [Geolocation using GeoIP2]](#Geolocation_using_GeoIP2)
        -   [[2.6.1] [Downloading Maxmind GeoIP2 databases]](#Downloading_Maxmind_GeoIP2_databases)
        -   [[2.6.2] [Add GeoIP2 support to NGINX]](#Add_GeoIP2_support_to_NGINX)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Service control]](#Service_control)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [systemd]](#systemd)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Validate configuration]](#Validate_configuration)
    -   [[4.2] [Verify processes are running]](#Verify_processes_are_running)
    -   [[4.3] [Verify bound addresses and ports]](#Verify_bound_addresses_and_ports)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [[] Installation]

Before immediately installing the [[[www-servers/nginx]](https://packages.gentoo.org/packages/www-servers/nginx)[]] package, first take a good look at the USE flags for NGINX.

### [[] Expanded USE flags]

NGINX uses modules to enhance its features. To simplify the maintenance of this modular approach, the NGINX ebuild uses [`USE_EXPAND`](https://wiki.gentoo.org/wiki//etc/portage/make.conf#USE_EXPAND "/etc/portage/make.conf") flags to denote which modules should be installed.

-   HTTP related modules can be enabled through the `NGINX_MODULES_HTTP` variable
-   Stream (generic TCP/UDP proxying) related modules can be enabled through the `NGINX_MODULES_STREAM` variable
-   Mail (POP3/IMAP4/SMTP proxying) related modules can be enabled through the `NGINX_MODULES_MAIL` variable

These variables need to be set in [/etc/portage/package.use], if it is a file, or in a file inside it, for example [/etc/portage/package.use/nginx]. The variables descriptions can be found in [[/var/db/repos/gentoo/profiles/desc/nginx_modules_http.desc](https://gitweb.gentoo.org/repo/gentoo.git/plain/profiles/desc/nginx_modules_http.desc)], [[/var/db/repos/gentoo/profiles/desc/nginx_modules_stream.desc](https://gitweb.gentoo.org/repo/gentoo.git/plain/profiles/desc/nginx_modules_stream.desc)], and [[/var/db/repos/gentoo/profiles/desc/nginx_modules_mail.desc](https://gitweb.gentoo.org/repo/gentoo.git/plain/profiles/desc/nginx_modules_mail.desc)].

For example, to enable the `fastcgi` module:

[FILE] **`/etc/portage/package.use/nginx`**

    www-servers/nginx NGINX_MODULES_HTTP: fastcgi

### [[] USE flags]

### [USE flags for] [www-servers/nginx](https://packages.gentoo.org/packages/www-servers/nginx) [[]] [Robust, small and high performance HTTP and reverse proxy server]

  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+http`](https://packages.gentoo.org/useflags/+http)               Enable core HTTP support
  [`+http-cache`](https://packages.gentoo.org/useflags/+http-cache)   Enable HTTP cache support
  [`+http2`](https://packages.gentoo.org/useflags/+http2)             Enable HTTP2 module support
  [`+modules`](https://packages.gentoo.org/useflags/+modules)         Enable loadable module support
  [`+pcre2`](https://packages.gentoo.org/useflags/+pcre2)             Enable support for pcre2
  [`aio`](https://packages.gentoo.org/useflags/aio)                   Enable asynchronous I/O support
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable support for debugging log
  [`http3`](https://packages.gentoo.org/useflags/http3)               Enable HTTP3 module support
  [`ktls`](https://packages.gentoo.org/useflags/ktls)                 Enable Kernel TLS offload (kTLS)
  [`libatomic`](https://packages.gentoo.org/useflags/libatomic)       Use dev-libs/libatomic_ops instead of builtin atomic operations
  [`mail`](https://packages.gentoo.org/useflags/mail)                 Enable POP3/IMAP4/SMTP mail proxy server
  [`pcre`](https://packages.gentoo.org/useflags/pcre)                 Add support for Perl Compatible Regular Expressions
  [`pcre-jit`](https://packages.gentoo.org/useflags/pcre-jit)         Enable JIT for pcre
  [`rtmp`](https://packages.gentoo.org/useflags/rtmp)                 NGINX-based Media Streaming Server
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                   Enable HTTPS module for http. Enable SSL/TLS support for POP3/IMAP/SMTP for mail.
  [`stream`](https://packages.gentoo.org/useflags/stream)             Enable generic TCP/UDP proxying and load balancing
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`threads`](https://packages.gentoo.org/useflags/threads)           Add threads support for various packages. Usually pthreads
  [`vim-syntax`](https://packages.gentoo.org/useflags/vim-syntax)     Pulls in related vim syntax scripts
  ------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 23:02] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [[] Emerge]

With the USE flags set, install [[[www-servers/nginx]](https://packages.gentoo.org/packages/www-servers/nginx)[]]:

`root `[`#`]`emerge --ask www-servers/nginx`

### [[] Installation verification]

The default NGINX configuration defines an HTTP virtual server listening on loopback address but does not define a root directory. To test out the installation, use an existing directory or create a new root directory, for example [/var/www/localhost/htdocs]:

`root `[`#`]`mkdir -p /var/www/localhost/htdocs`

Then, uncomment the `root` directive inside the `server` block:

[FILE] **`/etc/nginx/nginx.conf`Setting the root directive**

    server

** Tip**\
You can copy a sample welcome page to the root directory. For example, if [/var/www/localhost/htdocs] was chosen, use the following command to copy the welcome page to the root:

`root `[`#`]`cp /usr/share/nginx/index.html /var/www/localhost/htdocs`

The NGINX package installs an init service script and a systemd unit allowing administrators to stop, start, or restart the service. If running OpenRC, issue the next command to start the NGINX service:

`root `[`#`]`rc-service nginx start`

If using systemd, use the following command to start NGINX:

`root `[`#`]`systemctl start nginx.service`

To verify that NGINX is properly running, point a web browser to [http://localhost](http://localhost) or use a command-line tool like [curl]:

`user `[`$`]`curl http://localhost`

## [[] Configuration]

The NGINX configuration is specified in the [/etc/nginx/nginx.conf] file.

### [[] Single site access]

The following example shows a single-site access, without dynamic capabilities (such as [PHP](https://wiki.gentoo.org/wiki/PHP "PHP")).

[FILE] **`/etc/nginx/nginx.conf`Gentoo\'s default configuration**

    user nginx nginx;
    worker_processes auto;

    events

    http
    }

### [[] Multiple site access]

It is possible to leverage the `include` directive to split the configuration in multiple files:

[FILE] **`/etc/nginx/nginx.conf`Multisite configuration**

    user nginx nginx;
    worker_processes auto;

    events

    http

[FILE] **`/etc/nginx/conf.d/local.conf`Simple host**

    server

[FILE] **`/etc/nginx/conf.d/local-ssl.conf`Simple SSL host**

    server

### [[] PHP support]

Add the following lines to the NGINX configuration to enable PHP support. In this example NGINX is exchanging information with the PHP process via a UNIX socket.

[FILE] **`/etc/nginx/nginx.conf`Enabling PHP support**

    ...
    http
        }
    }

To support this setup, PHP needs to be built with FastCGI Process Manager support ([[[dev-lang/php]](https://packages.gentoo.org/packages/dev-lang/php)[]]), which is handled through the `fpm` USE flag:

`root `[`#`]`echo "dev-lang/php fpm" >> /etc/portage/package.use/php`

Rebuild PHP with the `fpm` USE flag enabled:

`root `[`#`]`emerge --ask dev-lang/php`

** Note**\
Using UNIX socket communication is the preferred and recommended configuration

For PHP 7.0 and newer PHP versions use following configuration:

[FILE] **`/etc/php/fpm-php8.2/fpm.d/www.conf`Running PHP with UNIX socket support**

    listen = /run/php-fpm.socket
    listen.owner = nginx

Set the timezone in the php-fpm [php.ini] file. Substitute the `<PUT_TIMEZONE_HERE>` text in the FileBox below with the appropriate timezone information:

[FILE] **`/etc/php/fpm-php8.2/php.ini`Setup timezone in php.ini**

    date.timezone = <PUT_TIMEZONE_HERE>

Start the [php-fpm] daemon:

`root `[`#`]`rc-service php-fpm start`

Add [php-fpm] to the default runlevel:

`root `[`#`]`rc-update add php-fpm default`

Restart [nginx] with changed configuration:

`root `[`#`]`rc-service nginx restart`

Alternatively, for systemd:

`root `[`#`]`systemctl enable php-fpm@8.2 `

`root `[`#`]`systemctl start php-fpm@8.2 `

`root `[`#`]`systemctl restart nginx.service`

### [[] IP address access list]

The next example shows how to allow access to a particular URL (in this case [/nginx_status]) only to:

-   certain hosts (e.g. *192.0.2.1 127.0.0.1*)
-   and IP networks (e.g. *198.51.100.0/24*)

[FILE] **`/etc/nginx/nginx.conf`Enabling and configuring an IP access lists for /nginx_status page**

    http
        }
    }

### [[] Basic authentication]

NGINX allows limiting access to resources by validating the user name and password:

[FILE] **`/etc/nginx/nginx.conf`Enabling and configuring user authentication for the / location**

    http
        }
    }

The [domain.htpasswd] file can be generated using:

`user `[`$`]`echo -n 'foo:' >> domain.htpasswd`

This will create the [domain.htpasswd] file, containing a row for the user \'foo\'.

** Note**\
The string with the user name should end with \':\', this is the separator field between the user name and the password.

`user `[`$`]`openssl passwd >> domain.htpasswd`

This will add the password to the line for the user \'foo\'. The password will be asked in the prompt, once it\'s over, the file could be opened and will contain something like this:

[FILE] **`/etc/nginx/domain.htpasswd`Content of the domain.htpasswd file, for user foo with a ciphered password**

    foo:$1$lpC3de5Y$dnh6jegS1qlfZVo7rGExz/

The password is not in plain text, rather it is encrypted with using OpenSSL.

### [[] Geolocation using GeoIP2]

The GeoIP2 module makes use of GeoIP2 databases by [Maxmind](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data?lang=en) or similar. Using Maxmind is already supported in Gentoo through [[[net-misc/geoipupdate]](https://packages.gentoo.org/packages/net-misc/geoipupdate)[]]. However, [registration of an account](https://www.maxmind.com/en/geolite2/signup) is required in order to obtain a free license key and download the free database.

#### [[] Downloading Maxmind GeoIP2 databases]

Once an account is created, install and configure geoipupdate:

`root `[`#`]`emerge --ask net-misc/geoipupdate`

Enter the account and license key:

[FILE] **`/etc/GeoIP.conf`Add your account info**

    AccountID YOURID
    LicenseKey YOURKEY
    EditionIDs GeoLite2-ASN GeoLite2-City GeoLite2-Country

After that, you\'ll need to download the databases:

`root `[`#`]`geoipupdate `

In order receive updates automatically in the future, add this command to a weekly cronjob or systemd timer.

#### [[] Add GeoIP2 support to NGINX]

To enable to modules and rebuild NGINX:

[FILE] **`/etc/portage/package.use/nginx`Add the modules to NGINX**

    www-servers/nginx NGINX_MODULES_HTTP: geo geoip2

** Note**\
The **geoip** module only supports the GeoIP legacy database.

Rebuild NGINX with the third party modules enabled:

`root `[`#`]`emerge --ask www-servers/nginx`

Once NGINX has been rebuild, point NGINX to the databases and the GeoIP2 variables:

[FILE] **`/etc/nginx/nginx.conf`Pointing to the GeoIP2 databases and its values**

    http

        geoip2 /usr/share/GeoIP/GeoLite2-ASN.mmdb
    ...
    }

The `auto_reload` option will allow updating the database without restarting NGINX.

For the GeoIP2 values to show up in a PHP application, assign them as **`fastcgi_param`** values:

[FILE] **`/etc/nginx/fastcgi.conf`Add GeoIP2 support to PHP**

    ...
    fastcgi_param GEOIP2_CITY_BUILD_DATE $geoip2_metadata_city_build;
    fastcgi_param GEOIP2_CITY $geoip2_data_city_name;
    fastcgi_param GEOIP2_CITY_GEONAMEID $geoip2_data_city_geonameid;
    fastcgi_param GEOIP2_CONTINENT_CODE $geoip2_data_continent_code;
    fastcgi_param GEOIP2_CONTINENT_GEONAMEID $geoip2_data_continent_geonameid;
    fastcgi_param GEOIP2_CONTINENT_NAME $geoip2_data_continent_name;
    fastcgi_param GEOIP2_COUNTRY_GEONAMEID $geoip2_data_country_geonameid;
    fastcgi_param GEOIP2_COUNTRY_CODE $geoip2_data_country_code;
    fastcgi_param GEOIP2_COUNTRY_NAME $geoip2_data_country_name;
    fastcgi_param GEOIP2_COUNTRY_IN_EU $geoip2_data_country_is_eu;
    fastcgi_param GEOIP2_LOCATION_ACCURACY_RADIUS $geoip2_data_location_accuracyradius;
    fastcgi_param GEOIP2_LATITUDE $geoip2_data_location_latitude;
    fastcgi_param GEOIP2_LONGITUDE $geoip2_data_location_longitude;
    fastcgi_param GEOIP2_LOCATION_METROCODE $geoip2_data_location_metrocode;
    fastcgi_param GEOIP2_LOCATION_TIMEZONE $geoip2_data_location_timezone;
    fastcgi_param GEOIP2_POSTAL_CODE $geoip2_data_postal_code;
    fastcgi_param GEOIP2_REGISTERED_COUNTRY_GEONAMEID $geoip2_data_rcountry_geonameid;
    fastcgi_param GEOIP2_REGISTERED_COUNTRY_ISO $geoip2_data_rcountry_iso;
    fastcgi_param GEOIP2_REGISTERED_COUNTRY_NAME $geoip2_data_rcountry_name;
    fastcgi_param GEOIP2_REGISTERED_COUNTRY_IN_EU $geoip2_data_rcountry_is_eu;
    fastcgi_param GEOIP2_REGION_GEONAMEID $geoip2_data_region_geonameid;
    fastcgi_param GEOIP2_REGION $geoip2_data_region_iso;
    fastcgi_param GEOIP2_REGION_NAME $geoip2_data_region_name;

    fastcgi_param GEOIP2_ASN $geoip2_data_autonomous_system_number;
    fastcgi_param GEOIP2_ASN_ORG $geoip2_data_autonomous_system_organization;

## [[] Usage]

### [[] Service control]

#### [[] OpenRC]

Start NGINX web server:

`root `[`#`]`rc-service nginx start`

Stop NGINX web server:

`root `[`#`]`rc-service nginx stop`

Add NGINX to the default runlevel so that the service starts automatically on system reboot:

`root `[`#`]`rc-update add nginx default`

Reload NGINX configuration without dropping connections:

`root `[`#`]`rc-service nginx reload`

Restart the NGINX service:

`root `[`#`]`rc-service nginx restart`

#### [[] systemd]

Start NGINX web server:

`root `[`#`]`systemctl start nginx`

Stop NGINX web server:

`root `[`#`]`systemctl stop nginx`

Check the status of the service:

`root `[`#`]`systemctl status nginx`

Enable service to start automatically on system reboot:

`root `[`#`]`systemctl enable nginx`

Reload NGINX configuration without dropping connections:

`root `[`#`]`systemctl reload nginx`

Restart the NGINX service:

`root `[`#`]`systemctl restart nginx`

## [[] Troubleshooting]

In case of problems, the following commands can help troubleshoot the situation.

### [[] Validate configuration]

Verify that the running NGINX configuration has no errors:

`root `[`#`]`rc-service nginx configtest`

    nginx                     | * Checking NGINX's configuration ...
    nginx                     |nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
    nginx                     |nginx: configuration file /etc/nginx/nginx.conf test is successful            [ ok ]

Alternatively, if using systemd:

`root `[`#`]`/usr/sbin/nginx -t`

    nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
    nginx: configuration file /etc/nginx/nginx.conf test is successful

By running [nginx] with the `-t` option, it will validate the configuration file without actually starting the [nginx] daemon. Use the `-c` option with the full path to the file to test configuration files in non-default locations. See [nginx(8)] for details.

### [[] Verify processes are running]

Check if [nginx] processes are running:

`user `[`$`]`ps aux | egrep 'nginx|PID'`

      PID TTY      STAT   TIME COMMAND
    26092 ?        Ss     0:00 nginx: master process /usr/sbin/nginx -c /etc/nginx/nginx.conf
    26093 ?        S      0:00 nginx: worker proces

### [[] Verify bound addresses and ports]

Verify NGINX daemon is listening on the right TCP port (such as 80 for HTTP or 443 for HTTPS):

`root `[`#`]`ss -tulpn | grep :80`

    tcp   LISTEN 0      0          0.0.0.0:80         0.0.0.0:*    users:(("nginx",pid=6253,fd=52),("nginx",pid=6252,fd=52))

## [[] See also]

-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") --- an efficient, extensible [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers"). It is one of the most popular web servers used the Internet.
-   [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd") --- a fast and lightweight [web server](https://wiki.gentoo.org/wiki/Category:Web_servers "Category:Web servers").

## [[] External resources]

-   [https://nginx.org/en/docs/beginners_guide.html](https://nginx.org/en/docs/beginners_guide.html) - A [nginx] beginner\'s guide. Helpful for those who do not know much about [nginx].
-   [https://github.com/nginxinc/nginx-wiki](https://github.com/nginxinc/nginx-wiki) - The archived NGINX wiki.
-   [https://github.com/h5bp/server-configs-nginx](https://github.com/h5bp/server-configs-nginx) - H5BP nginx config.
-   [https://gentoo.org/support/news-items/2025-07-05-nginx-packaging-changes.html](https://gentoo.org/support/news-items/2025-07-05-nginx-packaging-changes.html)