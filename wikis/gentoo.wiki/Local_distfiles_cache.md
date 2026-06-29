This article details some approaches to setting up a local distfiles cache which will save bandwidth when several machines are running Gentoo on the same local area network. It is a good idea to cache distfiles on one of them and let the rest download from that one. This saves bandwidth for both the network owner and the public source mirrors.

## Contents

-   [[1] [Setting up the server]](#Setting_up_the_server)
    -   [[1.1] [Using net-misc/apt-cacher-ng]](#Using_net-misc.2Fapt-cacher-ng)
        -   [[1.1.1] [Installing software]](#Installing_software)
        -   [[1.1.2] [Configuring for Gentoo]](#Configuring_for_Gentoo)
        -   [[1.1.3] [Configuring mirrors]](#Configuring_mirrors)
        -   [[1.1.4] [Starting the service]](#Starting_the_service)
    -   [[1.2] [Using www-servers/nginx]](#Using_www-servers.2Fnginx)
        -   [[1.2.1] [Setting up nginx VHost]](#Setting_up_nginx_VHost)
        -   [[1.2.2] [Restart nginx server]](#Restart_nginx_server)
-   [[2] [Setting up clients]](#Setting_up_clients)
-   [[3] [Open issues]](#Open_issues)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Setting up the server]

Select the machine that is going to serve the local distfiles cache and set it up. It will need to have enough free disk space to store all of the packages that are used by any machines on the network. The server machine will also need to be available whenever any other computer emerges a new package, and other computers on the network will need to be able to reach it using a static IP address or hostname.

There are a number of ways in which the cache can be implemented. This page describes a simple setup using [[[net-misc/apt-cacher-ng]](https://packages.gentoo.org/packages/net-misc/apt-cacher-ng)[]].

An alternative is to configure [[[www-servers/nginx]](https://packages.gentoo.org/packages/www-servers/nginx)[]] to act as a proxy server for any available mirror, a configuration example can be found below.

### [][Using [[[net-misc/apt-cacher-ng]](https://packages.gentoo.org/packages/net-misc/apt-cacher-ng)[]]]

#### [Installing software]

Install net-misc/apt-cacher-ng:

`root `[`#`]`emerge --ask net-misc/apt-cacher-ng`

#### [Configuring for Gentoo]

Apt-cacher-ng includes support for the Gentoo source mirrors, but some configuration is still needed. Since it is designed primarily for use with the Debian package management system, there are some types of files used in Gentoo distfiles which by default it refuses to download. To change this behavior, create the file [/etc/apt-cacher-ng/gentoo.conf]:

[FILE] **`/etc/apt-cacher-ng/gentoo.conf`**

    PfilePatternEx: .*

** Warning**\
This will most likely cause bad behavior for other distributions. Using the same apt-cacher-ng installation to cache files for Gentoo as well as another distribution is not recommended.

As mentioned in this [forum post](https://forums.gentoo.org/viewtopic-p-8561293.html?sid=31d5c3ab21b66d486c6e7923d712b50a#8561293), using apt-cacher-ng as the portage http proxy breaks the openpgp key refresh process. To avoid that, configure apt-cacher-ng to pass through https traffic:

[FILE] **`/etc/apt-cacher-ng/gentoo.conf`Pass https requests without caching**

    PassThroughPattern: ^(.*):443$

#### [Configuring mirrors]

Configure the list of public Gentoo mirrors from which apt-cacher-ng will download source packages:

[FILE] **`/etc/apt-cacher-ng/backends_gentoo`**

    http://mirror1...
    http://mirror2...

#### [Starting the service]

Now start the cache service:

`root `[`#`]`rc-service apt-cacher-ng start`

To start the service at boot:

`root `[`#`]`rc-update add apt-cacher-ng default`

### [][Using [[[www-servers/nginx]](https://packages.gentoo.org/packages/www-servers/nginx)[]]]

Instead of using [[[net-misc/apt-cacher-ng]](https://packages.gentoo.org/packages/net-misc/apt-cacher-ng)[]] and in case [[[www-servers/nginx]](https://packages.gentoo.org/packages/www-servers/nginx)[]] is already available, the latter can be used as a caching proxy for LAN clients.\
A major disadvantage of this setup is that the proxy server, if it uses itself, stores all packages twice, once in the nginx proxy cache and once in [\$.

#### [Setting up nginx VHost]

Add the following to [/etc/nginx/nginx.conf] or some other file included into nginx server configuration:

[FILE] **`/etc/nginx/nginx.conf`**

    server
    }

    proxy_cache_path    /path/to/distfiles/cache levels=1:2
            keys_zone=distfiles:5m
            max_size=10g
            inactive=7d
            use_temp_path=off;

    upstream distfiles

** Note**\
Make sure to replace all IP addresses and hostnames with valid ones. If IPv6 is not yet deployed, just remove the line `listen [2001:db8::1]:3142;` completely. Also decide upon which port to use for the cache, for simplicity this example uses the same port as Apt-cacher-ng.

** Note**\
Replace `mirror1` and `mirror2` with mirrors used by the machine, at best selected by running [[[app-portage/mirrorselect]](https://packages.gentoo.org/packages/app-portage/mirrorselect)[]].

** Note**\
Upon start nginx will create the directory specified in `proxy_cache_path` directive with 0755 and the nginx user and group, which are safe defaults but can be changed if needed.

This configuration retains downloaded packages for at most 7 days until they would be redownloaded by nginx. Also, the maximum disk space used by the cache is up to 10GB and nginx will pause all subsequent requests for the same file until either one request has been completed by downloading from the mirror server or the one-minute-timeout has been reached. These values could and should be modified to local necessities, especially so, if downstream is slower to deliver large package files.

#### [Restart nginx server]

`root `[`#`]`nginx -t`

If everything is reported ok, nginx can be forced to be restarted or to reload its configuration:

`root `[`#`]`nginx -s restart`

`root `[`#`]`nginx -s reload`

After this, clients can use nginx as a caching proxy as outlined below.

## [Setting up clients]

On all machines which are to use the distfiles cache (including the cache server itself), add the following to [/etc/portage/make.conf]:

[FILE] **`/etc/portage/make.conf`**

    http_proxy="http://distfilescache:3142"

** Note**\
Replace `distfilescache` with the name or IP address of the cache server.

## [Open issues]

-   Apt-cacher-ng installs a cron job to delete unreferenced files from the cache. Since the Gentoo cache contains no index files, this probably deletes either everything or nothing from it.

<!-- -->

-   If `sync-type` is set to `webrsync` in [/etc/portage/repos.conf], apt-cacher-ng will cache the snapshots. This is good if multiple machines are set up to use webrsync, but in the preferable case that a [local rsync mirror](https://wiki.gentoo.org/wiki/Local_Mirror "Local Mirror") is being used, it is just a waste of space.

## [See also]

-   [Local Mirror](https://wiki.gentoo.org/wiki/Local_Mirror "Local Mirror")

## [External resources]

-   [Running a Gentoo distfiles caching mirror on Debian](//serverfault.com/a/559076)
-   [Apt-Cacher-NG User Manual](//www.unix-ag.uni-kl.de/~bloch/acng/html/)