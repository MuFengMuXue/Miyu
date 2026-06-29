[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Busybox&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.busybox.net/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/busybox)

[[]][Wikipedia](https://en.wikipedia.org/wiki/BusyBox "wikipedia:BusyBox")

**BusyBox**, appropriately dubbed \"the Swiss army knife of embedded Linux\", is a utility that combines tiny versions of many common UNIX utilities into a *single, small executable*.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [BusyBox functions]](#BusyBox_functions)
        -   [[2.2.1] [vi]](#vi)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Network not working after BusyBox gets automatically unmerged]](#Network_not_working_after_BusyBox_gets_automatically_unmerged)
-   [[4] [See also]](#See_also)

## [Installation]

** Note**\
Portage, which is required by \@system, **hard depends** on the GNU Coreutils. This means that busybox cannot be used as a replacement for the GNU Coreutils on Gentoo in most situations, and installing busybox will simply result in a busybox binary without symlinks to coreutils set up.

### [USE flags]

### [USE flags for] [sys-apps/busybox](https://packages.gentoo.org/packages/sys-apps/busybox) [[]] [Utilities for rescue and embedded systems]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`livecd`](https://packages.gentoo.org/useflags/livecd)                 !!internal use only!! DO NOT SET THIS FLAG YOURSELF!, used during livecd building
  [`make-symlinks`](https://packages.gentoo.org/useflags/make-symlinks)   Create all the appropriate symlinks in /bin and /sbin.
  [`math`](https://packages.gentoo.org/useflags/math)                     Enable math support in gawk (requires libm)
  [`mdev`](https://packages.gentoo.org/useflags/mdev)                     Create the appropriate symlink in /sbin and install mdev.conf and support files
  [`pam`](https://packages.gentoo.org/useflags/pam)                       Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig)       Use this to restore your config from /etc/portage/savedconfig \$/\$. Make sure your USE flags allow for appropriate dependencies
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sep-usr`](https://packages.gentoo.org/useflags/sep-usr)               Support a separate /usr without needing an initramfs by booting with init=/ginit
  [`static`](https://packages.gentoo.org/useflags/static)                 Make the system rescue shell (/bin/bb) static so you can recover even when glibc is broken
  [`syslog`](https://packages.gentoo.org/useflags/syslog)                 Enable support for syslog
  [`systemd`](https://packages.gentoo.org/useflags/systemd)               Support systemd
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-14 15:43] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/busybox`

## [Usage]

### [Invocation]

To view usage information, and available functions:

`user `[`$`]`busybox --help `

    BusyBox v1.34.1 (2021-12-03 14:51:05 CET) multi-call binary.
    BusyBox is copyrighted by many authors between 1998-2015.
    Licensed under GPLv2. See source distribution for detailed
    copyright notices.

    Usage: busybox [function [arguments]...]
       or: busybox --list[-full]
       or: busybox --show SCRIPT
       or: busybox --install [-s] [DIR]
       or: function [arguments]...

        BusyBox is a multi-call binary that combines many common Unix
        utilities into a single executable.  The shell in this build
        is configured to run built-in utilities without $PATH search.
        You don't need to install a link to busybox for each utility.
        To run external program, use full path (/sbin/ip instead of ip).

    Currently defined functions:
        [, [[, acpid, addgroup, adduser, adjtimex, ar, arch, arp, arping, ascii, ash, awk,
        base32, base64, basename, bb, bbconfig, bbsh, bc, blkdiscard, blkid, blockdev,
        brctl, bunzip2, busybox, bzcat, bzip2, cal, cat, chat, chattr, chgrp, chmod, chown,
        chpasswd, chpst, chroot, chrt, chvt, cksum, clear, cmp, comm, conspy, cp, cpio,
        crc32, crond, cryptpw, cttyhack, cut, date, dd, deallocvt, delgroup, deluser,
        depmod, devmem, df, dhcprelay, diff, dirname, dmesg, dnsdomainname, dos2unix, du,
        dumpkmap, dumpleases, echo, ed, egrep, eject, env, envdir, envuidgid, ether-wake,
        expand, expr, factor, fallocate, false, fatattr, fbset, fdflush, fdformat, fdisk,
        fgconsole, fgrep, find, findfs, flash_eraseall, flash_lock, flash_unlock, flashcp,
        flock, free, freeramdisk, fsck, fsfreeze, fstrim, fsync, ftpd, fuser, getopt,
        getty, ginit, grep, groups, gunzip, gzip, halt, hd, hdparm, head, hexdump, hexedit,
        hostname, httpd, hwclock, i2cdetect, i2cdump, i2cget, i2cset, i2ctransfer, id,
        ifconfig, ifdown, ifenslave, ifplugd, ifup, init, insmod, install, ionice, iostat,
        ip, ipaddr, ipcrm, ipcs, iplink, ipneigh, iproute, iprule, iptunnel, kbd_mode,
        kill, killall, killall5, last, less, link, linux32, linux64, linuxrc, ln, loadfont,
        loadkmap, login, logread, losetup, lpq, lpr, ls, lsattr, lsmod, lsof, lspci,
        lsscsi, lsusb, lzcat, lzma, lzop, lzopcat, makedevs, man, md5sum, mdev, mesg,
        microcom, mim, minips, mkdir, mkdosfs, mke2fs, mkfifo, mkfs.ext2, mkfs.reiser,
        mkfs.vfat, mknod, mkpasswd, mkswap, mktemp, modinfo, modprobe, more, mount,
        mountpoint, mpstat, mt, mv, nameif, nanddump, nandwrite, nbd-client, nc, netcat,
        netstat, nice, nl, nmeter, nohup, nologin, nproc, nsenter, nslookup, ntpd, nuke,
        openvt, partprobe, passwd, paste, patch, pgrep, pidof, ping, pipe_progress,
        pivot_root, pkill, pmap, popmaildir, poweroff, powertop, printenv, printf, ps,
        pscan, pstree, pwd, pwdx, raidautorun, rdate, readahead, readlink, realpath,
        reboot, renice, reset, resize, resume, rev, rm, rmdir, rmmod, route, rtcwake,
        run-init, runlevel, rx, script, scriptreplay, sed, sendmail, seq, setarch,
        setconsole, setfattr, setfont, setkeycodes, setlogcons, setpriv, setserial, setsid,
        setuidgid, sh, sha1sum, sha256sum, sha3sum, sha512sum, showkey, shred, shuf, sleep,
        softlimit, sort, split, ssl_client, start-stop-daemon, stat, strings, stty, su,
        sum, svc, svok, swapoff, swapon, switch_root, sync, sysctl, tac, tail, tar, tc,
        tee, telnet, telnetd, test, tftp, tftpd, time, timeout, top, touch, tr, traceroute,
        true, truncate, ts, tty, ttysize, tunctl, tune2fs, ubiattach, ubidetach, ubimkvol,
        ubirename, ubirmvol, ubirsvol, ubiupdatevol, udhcpc, udhcpd, uevent, umount, uname,
        uncompress, unexpand, uniq, unit, unix2dos, unlink, unlzma, unlzop, unshare, unxz,
        unzip, uptime, users, usleep, vconfig, vi, vlock, volname, w, wall, watch,
        watchdog, wc, wget, which, who, whoami, whois, xargs, xxd, xz, xzcat, yes, zcat,
        zcip

### [BusyBox functions]

To use a tool specifically from BusyBox, execute [busybox], followed by the utility\'s (function\'s) name. For example, the following command will open up BusyBox\'s [ash] shell (type [ctrl]+[d] to quit):

`root `[`#`]`busybox ash`

** Note**\
BusyBox provides independent, or extra, tools to those installed on the system. For example, BusyBox\'s [ash] may be used in place of the system [ash] shell, or even be used if no other [ash] is installed.

#### [vi]

BusyBox ships a fully functioning [vi-like](https://wiki.gentoo.org/wiki/Vi "Vi") editor. To view the limited feature list of the vi command included, use:

`user `[`$`]`busybox vi -H`

    These features are available:
            Pattern searches with / and ?
            Last command repeat with .
            Line marking with 'x
            Named buffers with "x
            Some colon mode commands with :
            Settable options with ":set"
            Signal catching- ^C
            Job suspend and resume with ^Z
            Adapt to window re-sizes
    BusyBox v1.34.1 (2021-11-23 09:49:04 CET) multi-call binary.

    Usage: vi [-c CMD] [-R] [-H] [FILE]...

    Edit FILE

            -c CMD  Initial command to run ($EXINIT also available)
            -R      Read-only
            -H      List available features

** Note**\
BusyBox\'s vi may be used in place of the system vi editor, or be used even if no other vi is installed. BusyBox\'s vi is completely separate from any other version of vi installed on the system, and is contained in the BusyBox binary.

** See also**\
[Text editor](https://wiki.gentoo.org/wiki/Text_editor "Text editor"), [Knowledge Base:Edit a configuration file](https://wiki.gentoo.org/wiki/Knowledge_Base:Edit_a_configuration_file "Knowledge Base:Edit a configuration file").

## [Troubleshooting]

### [Network not working after BusyBox gets automatically unmerged]

Busybox was [removed](https://www.gentoo.org/support/news-items/2021-09-24-busybox-removal-from-system-set.html) from the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") in 2021-09. Some systems may have [implicitly relied on the internal BusyBox DHCP client](https://www.gentoo.org/support/news-items/2021-10-24-netifrc-dhcp-client.html), if the [Handbook](https://wiki.gentoo.org/wiki/Handbook "Handbook") was not strictly followed during installation. This can potentially result in a BusyBox dchp client, set up to configure the network on boot, being removed when performing a [depclean](https://wiki.gentoo.org/wiki/Knowledge_Base:Remove_orphaned_packages "Knowledge Base:Remove orphaned packages"), which might interfere with normal network function.

In this case, the solution may be to simply reinstall a dhcp client. To do this, it may be necesarry to [set up the network manually](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Networking#Using_ifconfig_and_route "Handbook:AMD64/Installation/Networking").

Configuring the network manually will surely be the best solution to install the required package(s), however if a workaround is necessary, it may be possible to download the *distfile* for the dhcp package to be installed (and any dependencies) from another machine or from a LiveCD with working network, and place the file in the [DISTDIR](https://wiki.gentoo.org/wiki/DISTDIR "DISTDIR"), before emerging. Another possibility could be [chrooting](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Base#Chrooting "Handbook:AMD64/Installation/Base") to the Gentoo installation from a liveCD.

If the BusyBox *distfile* is still in the cache, it may be possible to reinstall BusyBox immediately to get the network back up, and possibly install another client.

## [See also]

[toybox](https://wiki.gentoo.org/wiki/Toybox "Toybox") --- a utility that combines tiny versions of many common UNIX utilities into a *single, small executable*.