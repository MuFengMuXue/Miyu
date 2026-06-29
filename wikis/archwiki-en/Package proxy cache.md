# Package proxy cache

If you want to install the same Arch packages over and over —e.g. for testing purposes— it could help if you would not have to get the packages every time from the internet. This article shows you how to share packages so that you can greatly decrease your download times.

Which solution is best depends on your individual use-case. The methods can be grouped into #Package cache sharing of the machines, or deploying a #Proxy server for extra caching on one machine and configuring the machines to use it accordingly.

## Package cache sharing
For all solutions to share the package cache, keep in mind that, by default,  removes package tarballs from the cache that correspond to packages that are not installed on the machine the command was issued on. Because pacman cannot predict what packages are installed on all machines that share the cache, it will end up deleting files that should not be.

To clean up the cache so that only outdated tarballs are deleted:

## Read-only cache
Pacman supports cache servers directly. Cache servers will be tried before any non-cache servers, will not be removed from the server pool because of HTTP 404 download errors, and will not be used for database files.

If you are looking for a quick solution, you can simply run a basic temporary webserver which other computers can use as their cache server.

Start serving this directory. For example, with Python http.server module:

 $ python -m http.server -d /var/cache/pacman/pkg/

Then edit  on each client machine to add this server:

If looking for a more standalone solution,  offers a very minimal webserver. Replace the previous  command with e.g.:

 darkhttpd /var/cache/pacman/pkg --no-server-id

You could also run darkhttpd as a systemd service for convenience: see Systemd#Writing unit files.

miniserve, a small web server written in Rust, can also be used:

 $ miniserve /var/cache/pacman/pkg

Then edit  as above with the first url miniserve is available at.

If you are already running a web server for some other purpose, you might wish to reuse that as your local repository server instead. For example, if you already serve a site with nginx, you can add an nginx server block listening on port 8080:

{{hc|/etc/nginx/nginx.conf|
server {
    listen 8080;
    root /var/cache/pacman/pkg;
    server_name myarchrepo.localdomain;
    try_files $uri $uri/;
}
}}

Remember to restart  after making this change.

## Overlay mount of read-only cache
It is possible to use one machine on a local network as a read-only package cache by overlay mounting its  directory. Such a configuration is advantageous if this server has installed on it a reasonably comprehensive selection of up-to-date packages which are also used by other boxes. This is useful for maintaining a number of machines at the end of a low bandwidth upstream connection.

As an example, to use this method:

 # mkdir /tmp/remote_pkg /mnt/workdir_pkg /tmp/pacman_pkg
 # sshfs remote_username@remote_pkgcache_addr:/var/cache/pacman/pkg /tmp/remote_pkg -C
 # mount -t overlay overlay -o lowerdir=/tmp/remote_pkg,upperdir=/var/cache/pacman/pkg,workdir=/mnt/workdir_pkg /tmp/pacman_pkg

After this, run pacman using the option , e.g.:

 # pacman -Syu --cachedir /tmp/pacman_pkg

## Distributed read-only cache
There are Arch-specific tools for automatically discovering other computers on your network offering a package cache. Try , pacserve, , or . pkgdistcache uses Avahi instead of plain UDP which may work better in certain home networks that route instead of bridge between Wi-Fi and Ethernet.

Historically, there was [https://bbs.archlinux.org/viewtopic.php?id=64391 PkgD and multipkg, but they are no longer maintained.

## Read-write cache
In order to share packages between multiple computers, simply share  using any network-based mount protocol. This section shows how to use SSHFS to share a package cache plus the related library-directories between multiple computers on the same local network. Keep in mind that a network shared cache can be slow depending on the file-system choice, among other factors.

First, install any network-supporting filesystem packages: , ,  or .

Then, to share the actual packages, mount  from the server to  on every client machine.

## Two-way with rsync or FTP
Another approach in a local environment is rsync. Choose a server for caching and enable the rsync daemon. On clients synchronize two-way with this share via the rsync protocol. Filenames that contain colons are no problem for the rsync protocol.

Draft example for a client, using  within the share name ensures an architecture-dependent sync:

 # rsync ... rsync://server/share_$(uname -m)/ /var/cache/pacman/pkg/
 # pacman -Syu
 # paccache --remove --keep 3
 # rsync --delete ... /var/cache/pacman/pkg/ rsync://server/share_$(uname -m)/

Instead of relying on unencrypted rsync daemon a more secure security option is rsync over ssh,
Rsync#Automated backup with SSH gives an overview.

In case rsync is not available in your local environment, a simple ftp service is suitable for the two-way sync as well.  provides a  and a  option to sync a local with a remote storage.

## Synchronize pacman package cache using synchronization programs
Use Syncthing or Resilio Sync to synchronize the pacman cache directories (i.e. ).

## Proxy server
For proxy server solutions, keep in mind the machines should only use HTTP mirrors, because a proxy server cannot introspect HTTPS connections by default.

## Dynamic reverse proxy cache using nginx
nginx can be used to proxy package requests to official upstream mirrors and cache the results to the local disk. All subsequent requests for that package will be served directly from the local cache, minimizing the amount of internet traffic needed to update a large number of computers.

In this example, the cache server will run at  and store the packages in .

Install nginx on the computer that is going to host the cache. Create the directory for the cache and adjust the permissions so nginx can write files to it:

 # mkdir /srv/http/pacman-cache
 # chown http:http /srv/http/pacman-cache

Use the nginx pacman cache config as a starting point for . Check that the  directive works for your needs. In the upstream server blocks, configure the  directives with addresses of official mirrors, see examples in the configuration file about the expected format. Once you are satisfied with the configuration file start and enable nginx.

In order to use the cache each Arch Linux computer (including the one hosting the cache) must have the following line at the top of the  file:

{{Note| You will need to create a method to clear old packages, as the cache directory will continue to grow over time.  (which is provided by ) can be used to automate this using retention criteria of your choosing. For example, {{ic|find /srv/http/pacman-cache/ -type d -exec paccache -v -r -k 2 -c {} \;}} will keep the last 2 versions of packages in your cache directory.}}

## Squid
Squid proxy can be setup to only cache arch packages and can be used with aif/pacman/wget/etc with minimal configuration on the client system.

## Install Squid
Install .

## Configure Squid
This is the minimum configuration to get squid cache arch packages.

## Cache Rules
Before defining these rules, remove/comment (if you do not need them) all the default refresh_patterns

That should define that *.pkg.tar.* gets cached, and anything else should not.

## Maximum Filesize
Objects larger than this size will NOT be saved on disk:

## Cache Directory
Set the cache dir and its maximum size and subdirs:

## Shutdown Lifetime
Time to wait until all active client sockets are closed:

## Start Squid
Just start  or if squid is already running restart it.

## Follow Squid access log
To see the access to squid:

You should see this for packages that are directed to original host:

and for packages that are delivered from the cache:

## Manual Arch Install
On the individual machines, add environment variables for your proxy. To do so for testing:

 # export http_proxy='http://your_squid_machine_ip:3128/'
 # export ftp_proxy='ftp://your_squid_machine_ip:3128/'

Now it should use your proxy. Watch the squid logs to verify this. Once it works, add the  and/or  variables in an appropriate place on the installed system, e.g. in .

## Intercepting local requests
If you want all HTTP requests on local machine automagically go through squid, we first need to add an intercepting port for squid:

and iptables rules to redirect all (except the ones from squid) port 80 requests to squid:

## Pacoloco proxy cache server
Pacoloco is an easy-to-use proxy cache server for pacman repositories. It also allows automatic prefetching of the cached packages.

It can be installed as . Open the configuration file and add pacman mirrors:

Restart  and the proxy repository will be available at .

## Flexo proxy cache server
Flexo is yet another proxy cache server for pacman repositories. Flexo is available as . Once installed, start the  unit.

Flexo runs on port  by default. Enter  to the top of your  so that pacman downloads packages via Flexo.
