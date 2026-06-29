[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=Chrooting_proxy_services&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

[] This article has been flagged for not conforming to the [wiki guidelines](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines "Gentoo Wiki:Guidelines") (this article needs to clearly state it\'s intention and provide an overview of the process before \"diving in\" ; use of [2nd person pronouns](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Guidelines#Avoid_first_and_second_person_writing "Gentoo Wiki:Guidelines")). Please [help Gentoo out](https://wiki.gentoo.org/wiki/Help_improve_Gentoo_by_getting_involved_with_documentation!#Make_articles_conform_to_the_guidelines "Help improve Gentoo by getting involved with documentation!") by starting fixing things.

Today there are many process isolation techniques. Most of them are based on virtualization or containers. Some are focused on security, which is what we want for this.

## Contents

-   [[1] [Kernel options]](#Kernel_options)
-   [[2] [Chroot]](#Chroot)
    -   [[2.1] [Chrooted FreshClamAV]](#Chrooted_FreshClamAV)
    -   [[2.2] [Chrooted Dante Sockd]](#Chrooted_Dante_Sockd)
    -   [[2.3] [Chrooted HAVP + libClamAV]](#Chrooted_HAVP_.2B_libClamAV)
    -   [[2.4] [Chrooted Privoxy]](#Chrooted_Privoxy)
    -   [[2.5] [Chrooted Tor]](#Chrooted_Tor)
-   [[3] [Post install tasks]](#Post_install_tasks)
-   [[4] [See also]](#See_also)

## [Kernel options]

[]We would like to *use hardened chroot* to isolate internet services, but since **hardened-sources** is no longer available and there is no replacement for most of us, therefore we will do without. We leave this section in for those that can still use it.

To create a *hardened jail* we need **hardened-sources** to be installed (it is wise to use one of hardened profiles). So emerge it:

`root `[`#`]`emerge --ask sys-kernel/hardened-sources`

Then set the necessary hardened chroot options:

[KERNEL] **make menuconfig options**

    Security options  --->
        Grsecurity  --->
            [*] Grsecurity
                Customize Configuration  --->
                    Filesystem Protections  --->
                        [*] Chroot jail restrictions
                        [*]   Deny mounts
                        [*]   Deny double-chroots
                        [*]   Deny pivot_root in chroot
                        [*]   Enforce chdir("/") on all chroots
                        [*]   Deny (f)chmod +s
                        [*]   Deny fchdir and fhandle out of chroot
                        [*]   Deny mknod
                        [*]   Deny shmat() out of chroot
                        [*]   Deny access to abstract AF_UNIX sockets out of chroot
                        [*]   Protect outside processes
                        [*]   Restrict priority changes
                        [*]   Deny sysctl writes
                        [*]   Deny bad renames
                        [*]   Capability restrictions

## [Chroot]

As an example, of building chroot services, lets take a look at home proxy server. A home proxy can look something like:

                      +-------------------------------------------------------------+
                      | Chrooted sockd or torsocks <-> Other Internet applications  |
                      |      ^                                                      |
                      |      |                                                      |
                      |                                Chrooted          HTTP*      |
     +----------+     |  Chrooted  <->  Chrooted  <->    HAVP    <->    Internet    |
     | Internet | <-> | <-> Tor         Privoxy            +          applications  |
     +----------+     |                    ^           libClamAV                    |
                      |                    |                                        |
                      |                                                             |
                      |                 Chrooted                                    |
                      |                 FreshClam                                   |
                      +-------------------------------------------------------------+

From a users perspective the best way would be to write an ebuild to build the chroot of the service!!! So generally for a chrooted tor service the Gentoo user wants to run:

`root `[`#`]`emerge --config net-misc/tor`

and that is all\... Except developers don\'t want to support such a complicated ebuild. Therefore, here we will show examples of chrooted init scripts for all services shown above and examples of bash scripts to build the chroots (these should be hooked into the *pkg_config()* function of the respective ebuilds).

First **build and install binary packages** for the services [ClamAV](https://wiki.gentoo.org/wiki/ClamAV "ClamAV"), [tor](https://wiki.gentoo.org/wiki/Tor "Tor"), [Dante](//packages.gentoo.org/packages/net-proxy/dante), [HAVP](//packages.gentoo.org/packages/net-proxy/havp) and [privoxy](https://wiki.gentoo.org/wiki/Privoxy "Privoxy"):

`root `[`#`]`emerge --ask -b app-antivirus/clamav net-vpn/tor net-proxy/torsocks net-proxy/dante net-proxy/havp net-proxy/privoxy`

Then configure all of them, which is beyond the scope of this how-to, though. However, for this setup to work we need `USE=clamav` on HAVP.

The next scripts build chrooted services even when *all file-systems with executables are mounted readonly and all writeable file-systems are mounted with noexec*. Make sure you have write-access to the [/] and [/usr] partitions when you execute these!

**You must manually run the chroot build scripts any time you update or reconfigure the service or update this library!**

### [Chrooted FreshClamAV]

[FILE] **`/etc/init.d/clamd`chrooted freshclam**

    #!/sbin/openrc-run
    # Copyright 1999-2015 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2

    CHROOT="/usr/chroot/clamav"
    PIDCLAMD="/var/run/clamav/clamd.pid"
    PIDFRESH="/var/run/clamav/freshclam.pid"
    daemon_clamd="/usr/sbin/clamd"
    daemon_freshclam="/usr/bin/freshclam"
    daemon_milter="/usr/sbin/clamav-milter"

    extra_commands="logfix"

    depend()

    get_config()
            if(S==1&&\$1~\"^$2\$\")
            }"
    }

    checkconfig() :$" \
                    --mode 0755 --directory `dirname $$`
            if [ ! -c $/dev/null ] ; then
                    mknod -m 666 $/dev/null c 1 3
                    mount -ro remount $/dev
            fi
    }

    start() " = "yes" ]; then
                    checkconfig || return 1
                    if [ -S "$$" ]; then
                            rm -f $$
                    fi
                    ebegin "Starting chrooted clamd"
                    start-stop-daemon --start --quiet \
                            --nicelevel $ \
                            --ionice $ \
                            --pidfile "$$" \
                            --exec chroot $ $
                    eend $? "Failed to start clamd"
            fi

            if [ "$" = "yes" ]; then
                    checkconfig || return 1
                    ebegin "Starting chrooted freshclam"
                    start-stop-daemon --start --quiet \
                            --nicelevel $ \
                            --ionice $ \
                            --pidfile "$$" \
                            --exec chroot $ $ -- -d --pid "$"
                    retcode=$?
                    if [ $ = 1 ]; then
                            eend 0
                            einfo "Virus databases are already up to date."
                    else
                            eend $ "Failed to start freshclam"
                    fi
            fi

            if [ "$" = "yes" ]; then
                    if [ -z "$" ]; then
                            MILTER_CONF_FILE="/etc/clamav-milter.conf"
                    fi

                    ebegin "Starting clamav-milter"
                    start-stop-daemon --start --quiet \
                            --nicelevel $ \
                            --ionice $ \
                            --exec $ -- -c $
                    eend $? "Failed to start clamav-milter"
            fi
    }

    stop() " = "yes" ]; then
                    ebegin "Stopping chrooted clamd"
                    start-stop-daemon --stop --pidfile "$$" --quiet --name clamd
                    eend $? "Failed to stop clamd"
            fi
            if [ "$" = "yes" ]; then
                    ebegin "Stopping chrooted freshclam"
                    start-stop-daemon --stop --quiet \
                    --pidfile "$$" \
                    --name freshclam \
                    --exec chroot $ $ -- -K --pid "$"
                    eend $? "Failed to stop freshclam"
            fi
            if [ "$" = "yes" ]; then
                    ebegin "Stopping clamav-milter"
                    start-stop-daemon --stop --quiet --name clamav-milter
                    eend $? "Failed to stop clamav-milter"
            fi
    }

    logfix() " = "yes" ]; then
                    # fix clamd log permissions
                    # (might be clobbered by logrotate or something)
                    local logfile=$(get_config clamd LogFile)
                    if [ -n "$$" ]; then
                            checkpath --quiet \
                                    --owner "$":"$" \
                                    --mode 640 \
                                    --file $$
                    fi
            fi

            if [ "$" = "yes" ]; then
                    # fix freshclam log permissions
                    # (might be clobbered by logrotate or something)
                    local logfile=$(get_config freshclam UpdateLogFile)
                    if [ -n "$$" ]; then
                            checkpath --quiet \
                                    --owner "$":"$" \
                                    --mode 640 \
                                    --file $$
                    fi
            fi
    }

[FILE] **`clamav-chroot.sh`Build chrooted freshclam**

    #!/bin/bash
    # 20150922
    # GPL-3

    PKGDIR="/var/cache/binpkgs"
    CATEGORY="app-antivirus"
    PN="clamav"
    CHROOT="/usr/chroot/$"
    WORKD=`pwd`

    # Cleaning chroot directory.
    umount "$"/var/lib/$ "$"/var/log/$ "$"/var/run "$"/var/tmp "$"/dev 1>/dev/null 2>&1
    rm -rf "$"

    # Make common directory and symlinks.
    mkdir -p "$"/
    if [ -d /lib64 ]
        then
            mkdir -p "$"/
            cd "$" && ln -s lib64 lib
            cd "$/usr" && ln -s lib64 lib
        else
            mkdir -p "$"/
    fi
    mkdir -p /var/log/$ "$"/var/log/$ "$"/var/run "$"/var/tmp
    chown -R $:$ /var/log/$ "$"/var/log/$
    chmod -R o-rwx /var/log/$ "$"/var/log/$

    # Extract package.
    tar -xjphf `ls $/$/$-0* | tail -n 1` -C "$"

    # Copy necessary libraries.
    cp -pRPd /lib/ld-* "$/lib"
    cp `ldd "$/usr/bin/freshclam" | awk '' | grep "^/lib"` "$/lib"
    cp `ldd "$/usr/bin/freshclam" | awk '' | grep "^/usr/lib"` "$/usr/lib"

    # Copy user information and necessary libraries for it.
    cp -pRPd /lib/libnss* /lib/libnsl* /lib/libresolv* "$/lib"
    cp /usr/lib/libnss3.so "$/usr/lib"
    grep "^$" "/etc/passwd" > "$/etc/passwd"
    grep "$" "/etc/group" > "$/etc/group"

    # fstab stuff.
    if [[ `grep "Clamav chroot stuff." /etc/fstab` == '' ]]
        then
            cat >> /etc/fstab << EOF

    # Clamav chroot stuff.
    /var/lib/$          $/var/lib/$         none    bind,nodev,noexec,nosuid,rw                                     0 0
    /var/log/$          $/var/log/$         none    bind,nodev,noexec,nosuid,rw                                     0 0
    /var/tmp/havp           $/var/tmp               none    bind,nodev,noexec,nosuid,user=$,ro                          0 0
    none                    $/var/run               tmpfs   rw,nodev,noexec,nosuid,relatime,size=1024k,mode=755             0 0
    none                    $/dev                   tmpfs   rw,noexec,nosuid,relatime,size=1024k,nr_inodes=384443,mode=755  0 0
    EOF
    fi
    mount -a

    # Configuration.
    cp -fp /etc/freshclam.conf $/etc/
    cp -fp /etc/clamd.conf $/etc/
    cd $
    cp -f clamd /etc/init.d/
    cp -f clamd $/etc/init.d/

    exit 0

### [Chrooted Dante Sockd]

[FILE] **`/etc/init.d/dante-sockd`chrooted dante-sockd**

    #!/sbin/openrc-run
    # Copyright 1999-2015 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2
    # $Id$

    CHROOT=/usr/chroot/dante
    SOCKD_OPT=""
    [ "$" -gt 1 ] && SOCKD_OPT="$ -N $"
    [ "$" -eq 1 ] && SOCKD_OPT="$ -d"
    [ "$" -eq 1 ] && SOCKD_OPT="$ -n"
    PIDFILE=/var/run/dante/sockd.pid
    SOCKDIR=/var/lock/dante-sockd/

    depend()

    checkconfig() /etc/socks/sockd.conf ] ; then
                    eerror "You need to setup /etc/socks/sockd.conf first"
                    eerror "Examples are in /usr/share/doc/dante[version]/example"
                    eerror "for more info, see: man sockd.conf"
                    return 1
            fi

            /usr/sbin/sockd -V -f $/etc/socks/sockd.conf >/tmp/dante-sockd.checkconf 2>&1
            if [ $? -ne 0 ]; then
                    cat /tmp/dante-sockd.checkconf
                    eerror "Something is wrong with your configuration file"
                    eerror "for more info, see: man sockd.conf"
                    return 1
            fi
            rm /tmp/dante-sockd.checkconf

            DAEMON_UID=`sed -e '/^[ \t]*user[.]notprivileged[ \t]*:/;d' /etc/socks/sockd.conf`

            if [ -n "$DAEMON_UID" ]; then
                    checkpath --quiet --mode 755 --owner "$":root --directory `dirname $$`
                    checkpath --quiet --mode 750 --owner "$":root --directory "$$"
            else
                    checkpath --quiet --mode 755 --directory `dirname $$`
                    checkpath --quiet --mode 750 --directory "$$"
            fi

            return 0
    }

    start() $PIDFILE --make-pidfile --env TMPDIR=$SOCKDIR \
                    --exec chroot $ /usr/sbin/sockd -- $ >/dev/null 2>&1
            eend $? "Failed to start sockd"
    }

    stop() $PIDFILE
            eend $? "Failed to stop sockd"
    }

[FILE] **`dante-chroot.sh`Build chrooted dante-sockd**

    #!/bin/bash
    # 20150922
    # GPL-3

    PKGDIR="/var/cache/binpkgs"
    CATEGORY="net-proxy"
    PN="dante"
    CHROOT="/usr/chroot/$"
    USER="sockd"
    WORKD=`pwd`

    # Cleaning chroot directory.
    umount "$"/var/lock/ "$"/var/log/$ "$"/var/run "$"/dev "$"/tmp 1>/dev/null 2>&1
    rm -rf "$"

    # Make common directory and symlinks.
    mkdir -p "$"/
    if [ -d /lib64 ]
        then
            mkdir -p "$"/lib64
            cd "$" && ln -s lib64 lib
        else
            mkdir -p "$"/
    fi
    mkdir -p /var/log/$ /var/tmp/$ "$"/var/log/$ "$"/var/lock "$"/var/run "$"/tmp
    chown -R $:root /var/log/$ /var/tmp/$ "$"/var/log/$
    chmod -R o-rwx /var/log/$ /var/tmp/$ "$"/var/log/$

    # Extract package.
    tar -xjphf `ls $/$/$* | tail -n 1` -C "$"

    # Copy necessary libraries.
    cp -pRPd /lib/ld-* "$/lib"
    cp `ldd "$/usr/sbin/$" | awk '' | grep "^/lib"` "$/lib"

    # Copy user information and necessary libraries for it.
    cp -pRPd /lib/libnss* /lib/libnsl* /lib/libresolv* "$/lib"
    cp /usr/lib/libnss3.so "$/usr/lib"
    grep "^$" "/etc/passwd" > "$/etc/passwd"

    # fstab stuff.
    if [[ `grep "Dante chroot stuff." /etc/fstab` == '' ]]
        then
            cat >> /etc/fstab << EOF

    # Dante chroot stuff.
    /var/log/$          $/var/log/$         none    bind,nodev,noexec,nosuid,rw                                     0 0
    /var/tmp/$          $/tmp                   none    bind,nodev,noexec,nosuid,rw                                     0 0
    none                    $/var/lock              tmpfs   rw,nodev,noexec,nosuid,relatime,size=1024k,mode=755             0 0
    none                    $/var/run               tmpfs   rw,nodev,noexec,nosuid,relatime,size=1024k,mode=755             0 0
    EOF
    fi
    mount -a

    # Configuration.
    cp -fp /etc/socks/* $/etc/socks/
    cp -fp /etc/conf.d/$-sockd $/etc/conf.d/
    cd $
    cp -f $-sockd /etc/init.d/
    cp -f $-sockd $/etc/init.d/

    exit 0

### [][Chrooted HAVP + libClamAV]

[FILE] **`/etc/init.d/havp`chrooted havp**

    #!/sbin/openrc-run
    # Copyright 1999-2015 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2

    CHROOT=/usr/chroot/$
    PIDFILE=/var/run/$/$.pid

    depend()

    get_havp_opt() ' < /etc/$/$.config`
    }

    checkconfig() /etc/$/$.config ] ; then
                    eerror "No $/etc/$/$.config file exists!"
                    return 1
            fi

            local HAVP_USER
            get_havp_opt USER
            if [ -n "$" ] && ! getent passwd $ > /dev/null ; then
                    eerror "$ user is missing!"
                    return 1
            fi
            local HAVP_GROUP
            get_havp_opt GROUP
            if [ -n "$" ] && ! getent group $ > /dev/null ; then
                    eerror "$ group is missing!"
                    return 1
            fi

            if [ ! -c $/dev/null ] ; then
                    mknod -m 666 $/dev/null c 1 3
                    mount -ro remount $/dev
            fi

            checkpath --directory \
                --owner "$:$" --mode 0755 --directory `dirname $$`
            checkpath --directory \
                --owner "$:$" --mode 0700 $/var/log/havp
            checkpath --directory \
                --owner "$:$" --mode 0750 "$/var/tmp/$"
    }

    start() $ --exec chroot $ /usr/sbin/$ > /dev/null
            eend $?
    }

    stop() $
            eend $?
    }

[FILE] **`havp-chroot.sh`Build chrooted havp**

    #!/bin/bash
    # 20150922  havp-chroot.sh
    # GPL-3

    PKGDIR="/var/cache/binpkgs"
    CATEGORY="net-proxy"
    PN="havp"
    CHROOT="/usr/chroot/$"
    WORKD=`pwd`

    # Cleaning chroot directory.
    umount "$"/var/lib/clamav "$/var/log/$" "$"/var/run "$"/var/tmp "$"/dev 1>/dev/null 2>&1
    rm -rf "$"

    # Make common directory and symlinks.
    mkdir -p "$"/
    if [ -d /lib64 ]
        then
            mkdir -p "$"/
            cd "$" && ln -s lib64 lib
            cd "$/usr" && ln -s lib64 lib
        else
            mkdir -p "$"/
    fi
    mkdir -p /var/log/"$" "/var/tmp/$" "$"/var/lib/clamav "$/var/log/$" "$"/var/tmp/ "$"/var/run
    chown -R $:$ /var/log/$ /var/tmp/$ "$/var/log/$"
    chmod -R o-rwx /var/log/$ /var/tmp/$ "$/var/log/$"
    chmod -R g-rwx /var/log/$ "$"/var/log/$

    # Extract package.
    tar -xjphf `ls $/$/$* | tail -n 1` -C "$"

    # Copy necessary libraries.
    cp -pRPd /lib/ld-* "$/lib"
    cp `ldd "$/usr/sbin/$" | awk '' | grep "^/lib"` "$/lib"
    cp `ldd "$/usr/sbin/$" | awk '' | grep "^/usr/lib"` "$/usr/lib"
    cp -pRPd /usr/lib/libclam* "$/usr/lib"
    cp `ldd "$/usr/lib/libclamav.so" | awk '' | grep "^/lib"` "$/lib"
    cp `ldd "$/usr/lib/libclamav.so" | awk '' | grep "^/usr/lib"` "$/usr/lib"
    cp `ldd "$/usr/lib/libclamunrar_iface.so" | awk '' | grep "^/lib"` "$/lib"
    cp `ldd "$/usr/lib/libclamunrar_iface.so" | awk '' | grep "^/usr/lib"` "$/usr/lib"
    cp `ldd "$/usr/lib/libclamunrar.so" | awk '' | grep "^/lib"` "$/lib"

    # Copy user information and necessary libraries for it.
    cp -pRPd /lib/libnss* /lib/libnsl* /lib/libresolv* "$/lib"
    cp /usr/lib/libnss3.so "$/usr/lib"
    grep "^$" "/etc/passwd" > "$/etc/passwd"
    grep "^$" "/etc/group" > "$/etc/group"

    # fstab stuff.
    if [[ `grep "HAVP chroot stuff/ and /usr file system when execute it! ." /etc/fstab` == '' ]]
        then
            cat >> /etc/fstab << EOF

    # HAVP chroot stuff.
    /var/lib/clamav         $/var/lib/clamav        none    bind,nodev,noexec,nosuid,rw                                     0 0
    /var/log/$          $/var/log/$         none    bind,nodev,noexec,nosuid,rw                                     0 0
    /var/tmp/$          $/var/tmp               none    bind,nodev,noexec,nosuid,rw                                     0 0
    none                    $/var/run               tmpfs   rw,nodev,noexec,nosuid,relatime,size=1024k,mode=755             0 0
    none                    $/dev                   tmpfs   rw,noexec,nosuid,relatime,size=1024k,nr_inodes=384443,mode=755  0 0
    EOF
    fi
    mount -a

    # Configuration.
    cp -fpRPd /etc/$/* $/etc/$/
    cd $
    cp -f $ /etc/init.d/
    cp -f $ $/etc/init.d/

    exit 0

### [Chrooted Privoxy]

[FILE] **`/etc/init.d/privoxy`chrooted privoxy**

    #!/sbin/openrc-run
    # Copyright 1999-2015 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2

    CHROOT=/usr/chroot/$
    CONFFILE=/etc/$/config
    PIDFILE=/var/run/$/$.pid

    depend()

    checkconfig() /$" ]; then
                    eerror "Configuration file $/$ not found!"
                    return 1
            fi
            checkpath --quiet --mode 755 \
                    --owner "$":"$" \
                    --directory `dirname $$`
            if [ ! -c $/dev/null ] ; then
                    mknod -m 666 $/dev/null c 1 3
                    mount -ro remount $/dev
            fi
    }

    start() $" \
                    --exec chroot $ /usr/sbin/privoxy \
                    -- --pidfile "$" \
                    --user privoxy.privoxy "$" #2>/dev/null
            eend $?
    }

    stop() $"
            eend $?
    }

[FILE] **`privoxy-chroot.sh`Build chrooted privoxy**

    #!/bin/bash
    # 20150922
    # GPL-3

    PKGDIR="/var/cache/binpkgs"
    CATEGORY="net-proxy"
    PN="privoxy"
    CHROOT="/usr/chroot/$"
    WORKD=`pwd`

    # Cleaning chroot directory.
    umount "$"/var/log/$ "$"/var/run "$"/dev 1>/dev/null 2>&1
    rm -rf "$"

    # Make common directory and symlinks.
    mkdir -p "$"/
    if [ -d /lib64 ]
        then
            mkdir -p "$"/
            cd "$" && ln -s lib64 lib
            cd "$/usr" && ln -s lib64 lib
        else
            mkdir -p "$"/
    fi

    # Extract package.
    tar -xjphf `ls $/$/$* | tail -n 1` -C "$"

    # Copy necessary libraries.
    cp -pRPd /lib/ld-* "$/lib"
    cp `ldd "$/usr/sbin/$" | awk '' | grep "^/lib"` "$/lib"
    cp `ldd "$/usr/sbin/$" | awk '' | grep "^/usr/lib"` "$/usr/lib"

    # Copy user information and necessary libraries for it.
    cp -pRPd /lib/libnss* /lib/libnsl* /lib/libresolv* "$/lib"
    cp /usr/lib/libnss3.so "$/usr/lib"
    grep "^$" "/etc/passwd" > "$/etc/passwd"
    grep "^$" "/etc/group" > "$/etc/group"

    # fstab stuff.
    if [[ `grep "Privoxy chroot stuff." /etc/fstab` == '' ]];
        then
            cat >> /etc/fstab << EOF

    # Privoxy chroot stuff.
    /var/log/$          $/var/log/$         none    bind,nodev,noexec,nosuid,rw                                     0 0
    none                    $/var/run               tmpfs   rw,nodev,noexec,nosuid,relatime,size=1024k,mode=755             0 0
    none                    $/dev                   tmpfs   rw,noexec,nosuid,relatime,size=1024k,nr_inodes=384443,mode=755  0 0
    EOF
    fi
    mount -a

    # Configuration.
    cp -frp /etc/$/* $/etc/$/
    cd $
    cp -f $ /etc/init.d/
    cp -f $ $/etc/init.d/

    exit 0

### [Chrooted Tor]

[FILE] **`/etc/init.d/tor`Chrooted tor**

    #!/sbin/openrc-run
    # Copyright 1999-2017 Gentoo Foundation
    # Distributed under the terms of the GNU General Public License v2

    CHROOT=/opt/torchroot
    PIDFILE=/var/run/tor/tor.pid
    CONFFILE=/etc/tor/torrc
    SVCNAME=tor
    GRACEFUL_TIMEOUT=$

    # See bug #523552, and https://trac.torproject.org/projects/tor/ticket/5525
    # Graceful = wait 30 secs or so until all connections are properly closed.
    extra_commands="checkconfig"
    extra_started_commands="graceful gracefulstop reload"
    description="Anonymizing overlay network for TCP"
    description_checkconfig="Check for valid config file."
    description_reload="Reload the configuration."
    description_graceful="Gracefully restart."
    description_gracefulstop="Gracefully stop."

    depend()

    checkconfig() $ ] ; then
                    eerror "You need to setup $$ first"
                    eerror "Example is in $$.sample"
                    return 1
            fi

            if [ ! -c $/dev/random ] ; then
                    mknod -m 666 $/dev/null c 1 3
                    mknod -m 644 $/dev/random c 1 8
                    mknod -m 644 $/dev/urandom c 1 9
                    mount -ro remount $/dev
            fi

            #checkpath --quiet --mode 755 --owner "$":"$" --directory `dirname $$`

            # now verify whether the configuration is valid
            /usr/bin/$ --verify-config -f $$ > /dev/null 2>&1
            if [ $? -eq 0 ] ; then
                    einfo "Tor configuration ($$) is valid."
                    return 0
            else
                    eerror "Tor configuration ($$) not valid."
                    /usr/bin/$ --verify-config -f $$
                    return 1
            fi
    }

    start()
            start-stop-daemon --start --pidfile "$$" --quiet --exec chroot $ /usr/bin/$ -- -f "$" --runasdaemon 1 --PidFile "$" > /dev/null 2>&1
            eend $?
    }

    stop() $"
            eend $?
    }

    graceful()

    gracefulstop()  seconds"
            start-stop-daemon -P --stop --signal INT -R $ --pidfile "$$"
            rc=$?
            eend "done"
            eend $rc
    }

    reload() $ ]; then
                    eerror "$ isn't running"
                    return 1
            fi
            checkconfig || return 1
            ebegin "Reloading chrooted Tor configuration"
            start-stop-daemon --signal HUP --pidfile $$
            eend $?
    }

[FILE] **`tor-chroot.sh`Build chrooted tor**

    #!/bin/bash
    # 20170826
    # CC0
    # torchroot generation script
    export TORCHROOT=/opt/torchroot

    mkdir -p $TORCHROOT
    mkdir -p $TORCHROOT/etc/tor
    mkdir -p $TORCHROOT/dev
    mkdir -p $TORCHROOT/usr/bin
    mkdir -p $TORCHROOT/usr/lib
    mkdir -p $TORCHROOT/usr/share/tor
    mkdir -p $TORCHROOT/var/lib

    ln -s /usr/lib  $TORCHROOT/lib
    # Replace this line if you want to copy your own torrc instead of the default one.
    cp /etc/tor/torrc       $TORCHROOT/etc/tor/

    cp /usr/bin/tor         $TORCHROOT/usr/bin/
    cp /usr/share/tor/geoip* $TORCHROOT/usr/share/tor/
    cp /lib/ld-linux-*.so* $TORCHROOT/usr/lib/
    cp /lib/libnss* /lib/libnsl* /lib/libresolv* $TORCHROOT/usr/lib/
    cp $(ldd /usr/bin/tor | awk '' | grep --color=never "^/") $TORCHROOT/usr/lib/
    cp -r /var/lib/tor      $TORCHROOT/var/lib/
    chown -R tor:tor $TORCHROOT/var/lib/tor

    sh -c "grep --color=never ^tor /etc/passwd > $TORCHROOT/etc/passwd"
    sh -c "grep --color=never ^tor /etc/group > $TORCHROOT/etc/group"

    mknod -m 644 $TORCHROOT/dev/random c 1 8
    mknod -m 644 $TORCHROOT/dev/urandom c 1 9
    mknod -m 666 $TORCHROOT/dev/null c 1 3

    if [[ "$(uname -m)" == "x86_64" ]]; then
      cp /lib64/ld-linux-*.so* $TORCHROOT/usr/lib/
      ln -s /usr/lib $/lib64
    fi

## [Post install tasks]

-   properly configure [iptables], so only [tor] service can output packets to the internet;
-   properly setup proxy variables to all your internet applications and torify them;
-   install and properly configure [some privacy addons](https://prism-break.org/en/categories/gnu-linux/#web-browser-addons) to you browser.

## [See also]

-   [Tor](https://wiki.gentoo.org/wiki/Tor "Tor") --- an onion routing Internet anonymity system.
-   [Chroot Guide](https://wiki.gentoo.org/wiki/Project:X86/Chroot_Guide "Project:X86/Chroot Guide")
-   [Chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot") --- a Unix system utility used to change the apparent root directory to create a new environment logically separate from the main system\'s root directory.
-   [Jail](https://wiki.gentoo.org/wiki/Jail "Jail") --- how to use the **jail** tool to set up a [chroot](https://wiki.gentoo.org/wiki/Chroot "Chroot")