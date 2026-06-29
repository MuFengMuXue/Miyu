This article will explain how to use [Git](https://wiki.gentoo.org/wiki/Git "Git") (preferred) or [rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") to create a private local mirror of the [Gentoo ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository").

** Note**\
To help the Gentoo project by providing public mirrors, please see the relevant documentation for [source](https://wiki.gentoo.org/wiki/Project:Infrastructure/Mirrors/Source "Project:Infrastructure/Mirrors/Source") and [rsync](https://wiki.gentoo.org/wiki/Project:Infrastructure/Mirrors/Rsync "Project:Infrastructure/Mirrors/Rsync") mirrors.

## Contents

-   [[1] [Setting up a local mirror]](#Setting_up_a_local_mirror)
-   [[2] [Local Mirror using Rsync]](#Local_Mirror_using_Rsync)
    -   [[2.1] [Setting up the server]](#Setting_up_the_server)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
    -   [[2.3] [Testing the server]](#Testing_the_server)
    -   [[2.4] [Configuring the clients]](#Configuring_the_clients)
        -   [[2.4.1] [Copying the default Gentoo repo file for configuration]](#Copying_the_default_Gentoo_repo_file_for_configuration)
-   [[3] [Local Mirror using Git]](#Local_Mirror_using_Git)
    -   [[3.1] [Setting up the server]](#Setting_up_the_server_2)
        -   [[3.1.1] [Pre-requisites]](#Pre-requisites)
        -   [[3.1.2] [Server Config]](#Server_Config)
            -   [[3.1.2.1] [OpenRC]](#OpenRC_2)
            -   [[3.1.2.2] [systemd]](#systemd_2)
    -   [[3.2] [Testing]](#Testing)
    -   [[3.3] [Configuring Clients]](#Configuring_Clients)
    -   [[3.4] [Troubleshooting]](#Troubleshooting)
    -   [[3.5] [Caveats and Addendum]](#Caveats_and_Addendum)
-   [[4] [References]](#References)
-   [[5] [See also]](#See_also)

## [Setting up a local mirror]

Many users run Gentoo on several machines and need to sync the Gentoo repository on all of them. Using public mirrors is simply a waste of bandwidth at both ends. Syncing only one machine against a public mirror and all others against that computer would save resources on the public mirrors and save users\' bandwidth.

The same holds true for organizations who would like to control the mirror their servers and workstations sync against. Of course, they usually also want to save on bandwidth and traffic costs.

The old-school method of setting up a local mirror is to sync using **rsync**. However, syncing via **git** is both faster and more reliable. This document provides instructions for both, beginning with the rsync method. It is important to consider that if your local mirror uses **rsync** to sync to the public mirrors, then it will be much simpler to also use **rsync** for your local clients. If your local mirror syncs using **git**, then you should also use **git** to sync to it, and in fact in order to use **git** to sync to your local mirror, the local mirror server itself **must** sync to the public mirrors using **git**.

## [Local Mirror using Rsync]

Select which machine is going to be the local rsync mirror and set it up. Choose a computer that can handle the CPU and disk load that an rsync operation requires. The local mirror also needs to be available whenever any of the other computers syncs its ebuild repository. Besides, it should have a static IP address or a name that always resolves to the server. Configuring a DHCP and/or a DNS server is beyond the scope of this guide.

### [Setting up the server]

There is no extra package to install as the required software is already on the computer. Setting up a local rsync mirror is just a matter of configuring the [rsyncd] daemon to make the Gentoo repository directory available for syncing.

Currently, the Gentoo repository is now located by default at: [/var/db/repos/gentoo] . Older legacy installations used [/usr/portage] . Please be sure to enter the proper path in the following example. Create a [/etc/rsyncd.conf] configuration file such as this:

[FILE] **`/etc/rsyncd.conf`**

    pid file = /run/rsyncd.pid
    max connections = 5
    use chroot = yes
    uid = nobody
    gid = nobody
    # Optional: restrict access to some Gentoo boxes
    hosts allow = 192.168.0.1 192.168.0.2 192.168.1.0/24
    hosts deny  = *
    motd file = /etc/rsync/rsyncd.motd

    [gentoo-portage]
    path=/var/db/repos/gentoo
    comment=Gentoo ebuild repository

The `hosts allow` and `hosts deny` settings are optional and not needed. Without them, all clients will be allowed to connect to the mirror. The order in which the options are written is not relevant. The server will always check the `hosts allow` option first and grant the connection if the connecting host matches any of the listed patterns. The server will then check the `hosts deny` option and refuse the connection if any match is found. Any host that does not match anything will be granted a connection. See the man page ([man rsyncd.conf]) for more advanced configuration information.

### [Service]

Now, start the rsync daemon with the following command as the root user:

#### [OpenRC]

`root `[`#`]`/etc/init.d/rsyncd start `

`root `[`#`]`rc-update add rsyncd default `

#### [systemd]

`root `[`#`]`systemctl start rsyncd.service `

`root `[`#`]`systemctl enable rsyncd.service `

### [Testing the server]

It is time to test the rsync mirror. Test first locally and then again from the desired other machine.

Perform the following tests, using the local IP, or hostname. If the hostname can not be resolved by all computers, just refer to it by IP address instead.

`root `[`#`]`rsync 192.168.0.1::`

    gentoo-portage     Gentoo Ebuild Repository

This one-line response indicates good communication with the configured rsync server.

`root `[`#`]`rsync 192.168.0.1::gentoo-portage`

The content of [/var/db/repos/gentoo] should be visible on the mirror.

If the tests are unsuccessful, make sure the **rsyncd** service was actually started, there are no errors in the config file, and a local firewall is not blocking rsyncd\'s **TCP port 873**.

If the tests ARE successful, The rsync mirror is now set up.

Running [emerge \--sync] on this system will keep the server up-to-date. If cron or similar facilities to sync regularly, remember to keep it down to a sensible frequency like once or twice a day.

** Note**\
Please note that most public mirror administrators consider syncing more than once or twice a day an abuse. If the abuse limit is reached most mirrors will ban the abusers IP address from their server(s).

### [Configuring the clients]

Now, make the other computers use the local rsync mirror instead of a public one, by changing the **sync-uri** entry in the appropriate file in [[/etc/portage/repos.conf/]](https://wiki.gentoo.org/wiki/Project:Portage/Sync#Portage_configuration "Project:Portage/Sync").

#### [Copying the default Gentoo repo file for configuration]

One method of configuring the client would be to copy the default repo configuration file for Gentoo from [/usr/share/portage/config/repos.conf] to [/etc/portage/repos.conf/], and then editing the ` sync-uri = ... ` line appropriately.

An example configuration file might look like:

[FILE] **`/etc/portage/repos.conf/gentoo-mirror.conf`**

    # replace HOST_IP with the local IP address of the host machine

    [gentoo]
    location = /var/db/repos/gentoo
    sync-type = rsync
    sync-uri = rsync://HOST_IP/gentoo-portage
    #other options here

** Note**\
The local IP of the server can be found by running `ip addr` on the server.

## [Local Mirror using Git]

Much the same criteria apply to selecting a git local mirror server as for an rsync local mirror. Instead of **rsyncd**, you will be providing your mirror service using **git-daemon**.

### [Setting up the server]

It should go without saying that your local mirror server, and clients, will need [git] installed. There are a few simple pre-requisites beyond this:

#### [Pre-requisites]

-   The repo you want to act as a mirror for has to be synced via [git] already on the server machine (see [Portage_with_Git](https://wiki.gentoo.org/wiki/Portage_with_Git "Portage with Git") if you have not already done this)
-   dev-vcs/git needs to be merged **without** the safe-directories use flag (see addendum below if you need it on for some reason)

#### [Server Config]

Update the git-daemon config to suit our needs:

[FILE] **`/etc/conf.d/git-daemon`**

    GITDAEMON_OPTS="--syslog --export-all --listen=10.0.0.2 --base-path=/var/db/repos"

Substitute your local internal IP or hostname in the \--listen directive, of course. If the server listens on only a single interface or you wish to allow all interfaces, then \--listen is unnecessary. If you are having issues and need to troubleshoot, you can add \--reuseaddr (to aid with quick daemon restarts) and \--verbose for extra context in /var/log/syslog.

Start the service as below:

##### [OpenRC]

`root `[`#`]`rc-service git-daemon start `

`root `[`#`]`rc-update add git-daemon default `

##### [systemd]

`root `[`#`]`systemctl start git-daemon.service `

`root `[`#`]`systemctl enable git-daemon.service `

### [Testing]

To test the server without having to run emaint/eix/emerge every time, you can use:

`user `[`$`]`git ls-remote `[`git://mirrorserver/gentoo`](git://mirrorserver/gentoo)

### [Configuring Clients]

It\'s advisable to make a clean start on your clients, particularly if previously syncing via [rsync]. You can also take the opportunity to update your portage tree location to current standards ([/var/db/repos/gentoo]) if you\'re still using the old-school [/usr/portage]. First remove or comment out **PORTDIR** and anything that references it (typically **DISTDIR** and **PKGDIR**) from [/etc/portage/make.conf], then remove the repository, then recreate it using git:

`root `[`#`]`eselect repository remove -f gentoo `

`root `[`#`]`eselect repository add gentoo git `[`git://mirrorserver/gentoo`](git://mirrorserver/gentoo)` `

[/etc/portage/repos.conf/eselect-repo.conf] should now look something like this (or contain this section):

\

[FILE] **`/etc/portage/repos.conf/eselect-repo.conf`**

    # created by eselect-repo

    [gentoo]
    location = /var/db/repos/gentoo
    sync-type = git
    sync-uri = git://mirrorserver/gentoo

You can of course add additional settings to this section as appropriate (*auto-sync = yes* for example), or move the new section into your [/etc/portage/repos.conf/gentoo.conf] file if you so choose.

This is a good time to verify what your **profile** is currently set to:

`user `[`$`]`ls -l /etc/portage/make.profile`

At this point you can perform an initial sync to your new local mirror:

`root `[`#`]`emaint sync -r gentoo`

After the initial sync, reset your profile:

`root `[`#`]`eselect profile list `

`root `[`#`]`eselect profile set 25 `

(Or, of course, whichever your correct profile is.)

With your profile correctly set, sync a second time, and you should now be all set to go.

### [Troubleshooting]

If **emaint sync** fails on your local clients with a git fetch error:

`root `[`#`]`emaint sync -a`

    >>> Syncing repository 'gentoo' into '/var/db/repos/gentoo'...
    /usr/bin/git clone --depth 1 git://mirror/gentoo .
    Cloning into '.'...
    fatal: unable to connect to mirror:
    mirror[0: 1.2.3.4]: errno=Connection refused

    !!! git clone error in /var/db/repos/gentoo

\...Then you forgot to start the **git-daemon** service on your local mirror, or forgot to add it to the **default** runlevel to make it persistent.

### [Caveats and Addendum]

Obviously your local mirror will only be as up to date as the last time you synced it, just as with any other method. If you aren\'t already using cron to perform a daily sync, you probably should be.

If you need dev-vcs/git to be installed *with* the safe-directories use flag, you can either run it as root (not advised) or pick another user to run it as, but that user will need specific setup to work properly. See ^[\[1\]](#cite_note-1)^ for further information on how to accomplish this.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://forums.gentoo.org/viewtopic-p-8844946.html](https://forums.gentoo.org/viewtopic-p-8844946.html)]]

## [See also]

-   [Local distfiles cache](https://wiki.gentoo.org/wiki/Local_distfiles_cache "Local distfiles cache")
-   [Configuring the network](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Networking "Handbook:AMD64/Installation/Networking")