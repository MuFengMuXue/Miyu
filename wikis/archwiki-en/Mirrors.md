# Mirrors

This page is a guide to selecting and configuring your mirrors, and a listing of current available mirrors.

## Official mirrors
The official Arch Linux mirror list is available from the  package. To get an even more up-to-date list of mirrors, use the Pacman Mirrorlist Generator page.

Check the status of the mirrors by visiting the Mirror Status page. It is recommended to only use mirrors that are up to date, i.e. not out of sync.

If you want your mirror to be added to the official list, see DeveloperWiki:NewMirrors. In the meantime, add it to the Unofficial mirrors article.

## IPv6-ready mirrors
The Pacman Mirrorlist Generator can also be used to find a list of current IPv6 mirrors.

## Mirrors supporting rsync over TLS
There is no filter for mirrors supporting rsync over TLS on the mirrorlist generator page: they are listed below. The pkgbuild.com mirrors are managed by the Arch Linux DevOps team while others are contributed by the community. For more information about setting one up see DeveloperWiki:NewMirrors.

* rsync://berlin.mirror.pkgbuild.com/packages/ — Tier 1 Arch Linux Germany geomirror
* rsync://frankfurt.mirror.pkgbuild.com/packages/ — Tier 1 Arch Linux Germany geomirror
* rsync://singapore.mirror.pkgbuild.com/packages/ — Tier 1 Arch Linux Singapore geomirror
* rsync://johannesburg.mirror.pkgbuild.com/packages/ — Tier 1 Arch Linux South Africa geomirror
* rsync://umea.mirror.pkgbuild.com/packages/ — Tier 1 Arch Linux Sweden geomirror
* rsync://taipei.mirror.pkgbuild.com/packages/ — Tier 1 Arch Linux Taiwan geomirror
* rsync://london.mirror.pkgbuild.com/packages/ — Tier 1 Arch Linux United kingdom geomirror
* rsync://losangeles.mirror.pkgbuild.com/packages/ — Tier 1 Arch Linux USA geomirror
* rsync://mirror.funami.tech/arch — YuruMirror Tier 1 mirror located in South Korea
* rsync://de.mirror.shibe.party/archlinux/ — Tier 2 mirror in Germany
* rsync://fr.mirror.shibe.party/archlinux/ — Tier 2 mirror in France
* rsync://ftp.io.kr/arch — Tier 2 mirror in South Korea
* rsync://mirror.keiminem.com/archlinux - Tier 1 mirror in South Korea
* rsync://mirror2.keiminem.com/archlinux - Tier 1 mirror in South Korea

## Enabling a specific mirror
To enable mirrors, edit  and locate your geographic region. Uncomment mirrors you would like to use.

For example:

 ## Worldwide
 #Server = https://geo.mirror.pkgbuild.com/$repo/os/$arch
 #Server = http://mirror.rackspace.com/archlinux/$repo/os/$arch
 Server = https://mirror.rackspace.com/archlinux/$repo/os/$arch

See #Sorting mirrors for tools that help choosing mirrors.

It is also possible to specify mirrors in . For the core repository, the default setup is:

 Include = /etc/pacman.d/mirrorlist

To use the kernel.org mirror as a default mirror, add it before the  line:

 [core
 Server = https://mirrors.kernel.org/archlinux/$repo/os/$arch
 Include = /etc/pacman.d/mirrorlist

pacman will now try to connect to this mirror first. Proceed to do the same for core-testing, extra, and extra-testing, if applicable.

## Force pacman to refresh the package lists
Mirrors can be out of sync and the package list from the old mirror may not correspond to the package list of the new mirror, even though the dates of the lists may suggest that they do.

After creating/editing , issue the following command:

 # pacman -Syyu

Passing two / flags forces pacman to refresh all package lists even if they are considered to be up to date.

## Sorting mirrors
When downloading packages, pacman uses the mirrors in the order they are listed in , i.e. the order servers appear in the list sets their priority. If a package download fails (e.g. file not found, connection timeout), the next list entry is used.

It is not optimal to only rank mirrors based on speed since the fastest servers might be out-of-sync. Instead, make a list of mirrors sorted by their speed, then remove those from the list that are out of sync according to their status.

It is recommended to regularly repeat this process to keep the list of mirrors up-to-date.

## List by speed
## Ranking an existing mirror list
The  package provides a Bash script, , which can be used to rank the mirrors according to their connection and opening speeds to take advantage of using the fastest local mirror.

Back up the existing :

 # cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup

To prepare  for ranking with rankmirrors, the following actions can be carried out:

* Edit  and uncomment the servers to be tested
* If the servers in the file are grouped by country, one can extract all the servers of a specific country by using: {{bc|1=$ awk '/^## Country Name$/{f=1; next}f==0{next}/^$/{exit}{print substr($0, 1);}' /etc/pacman.d/mirrorlist.backup}}
* To uncomment every mirror, run the following  line:
* Finally, rank the mirrors, here with the operand  to only output the 6 fastest mirrors:

## Fetching and ranking a live mirror list
In order to start with a shortlist of up-to-date mirrors based in some countries and feed it to rankmirrors one can fetch the list from the Pacman Mirrorlist Generator. The command below pulls the up-to-date mirrors in either France or the United Kingdom which support the https protocol, it uncomments the servers in the list and then ranks them and outputs the 5 fastest.

 $ curl -s "https://archlinux.org/mirrorlist/?country=FR&country=GB&protocol=https&use_mirror_status=on" | sed -e 's/^#Server/Server/' -e '/^#/d' | rankmirrors -n 5 -

## Server-side ranking
The official Pacman Mirrorlist Generator provides an easy way to obtain a ranked list of mirrors. Because all ranking is done on a single server that takes multiple factors into account, the amount of load on the mirrors and the clients is significantly lower compared to ranking on each individual client.

## Client-side ranking
*
*
*
*
*

## Troubleshooting
## Missing mirrorlist
In case you encounter the following error:

 error: config file /etc/pacman.d/mirrorlist could not be read: No such file or directory

Get the mirrorlist directly from the website:

 # curl -o /etc/pacman.d/mirrorlist https://archlinux.org/mirrorlist/all/

Be sure to uncomment a preferred mirror as described in #Enabling a specific mirror.

Alternatively, use one of the methods for generating a mirrorlist listed under #Sorting mirrors.

## Misbehaving mirrors
If you are certain a mirror is not operating properly and that is not reflected on the mirrors status page, change the mirror and consider opening a bug report. For mirrors the issue should be opened in the arch-mirrors project at the Arch Linux GitLab. You may also send a mail to mirrors@archlinux.org.

## Pacman fails to retrieve a package from a HTTP mirror
See Pacman#Packages cannot be retrieved on installation first. If that doesn't help, use a HTTPS mirror.

## Pacman fails to retrieve data over HTTPS
If pacman fails to retrieve files due to TLS related errors, first make sure your system time is correct. TLS certificates need to be rejected, if local time is outside certificate's validity period. NTP is recommended, but not a requirement - in particular while fixing more pressing issues.

Many mirrors accept plain HTTP connections, despite this not being exposed in . Visit the Official Mirrorlist Generator to find servers that do.
