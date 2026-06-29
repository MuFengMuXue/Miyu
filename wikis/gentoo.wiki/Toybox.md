[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Toybox&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://landley.net/toybox/)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/toybox)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Toybox "wikipedia:Toybox")

**toybox** is a utility that combines tiny versions of many common UNIX utilities into a *single, small executable*.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Using toybox functions]](#Using_toybox_functions)
-   [[3] [See also]](#See_also)

## [Installation]

** Note**\
Portage, which is required by \@system, **hard depends** on the GNU Coreutils. This means that toybox cannot be used as a replacement for the GNU Coreutils on Gentoo in most situations, and installing toybox will simply result in a toybox binary without symlinks to coreutils set up.

### [USE flags]

### [USE flags for] [sys-apps/toybox](https://packages.gentoo.org/packages/sys-apps/toybox) [[]] [Common linux commands in a multicall binary]

  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig)   Use this to restore your config from /etc/portage/savedconfig \$/\$. Make sure your USE flags allow for appropriate dependencies
  ------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-10-17 06:16] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/toybox`

## [Usage]

### [Invocation]

To view usage information use

`user `[`$`]`toybox --help`

    Toybox 0.8.6 multicall binary: https://landley.net/toybox (see toybox --help)

    usage: toybox [--long | --help | --version | [COMMAND] [ARGUMENTS...]]

    With no arguments, "toybox" shows available COMMAND names. Add --long
    to include suggested install path for each command, see
    https://landley.net/toybox/faq.html#install for details.

    First argument is name of a COMMAND to run, followed by any ARGUMENTS
    to that command. Most toybox commands also understand:

    --help          Show command help (only)
    --version       Show toybox version (only)

    The filename "-" means stdin/stdout, and "--" stops argument parsing.

    Numerical arguments accept a single letter suffix for
    kilo, mega, giga, tera, peta, and exabytes, plus an additional
    "d" to indicate decimal 1000's instead of 1024.

    Durations can be decimal fractions and accept minute ("m"), hour ("h"),
    or day ("d") suffixes (so 0.1m = 6s).

Available functions:

`user `[`$`]`toybox `

    [ acpi arch ascii base32 base64 basename blkdiscard blkid blockdev bunzip2 bzcat cal cat catv
    chattr chgrp chmod chown chroot chrt chvt cksum clear cmp comm count cp cpio crc32 cut date
    devmem df dirname dmesg dnsdomainname dos2unix du echo egrep eject env expand factor fallocate
    false fgrep file find flock fmt free freeramdisk fsfreeze fstype fsync ftpget ftpput getconf
    grep groups gunzip halt head help hexedit hostname hwclock i2cdetect i2cdump i2cget i2cset
    iconv id ifconfig inotifyd insmod install ionice iorenice iotop kill killall killall5 link
    linux32 ln logger login logname losetup ls lsattr lsmod lspci lsusb makedevs mcookie md5sum
    microcom mix mkdir mkfifo mknod mkpasswd mkswap mktemp modinfo mount mountpoint mv nbd-client
    nc netcat netstat nice nl nohup nproc nsenter od oneit partprobe passwd paste patch pgrep pidof
    ping ping6 pivot_root pkill pmap poweroff printenv printf prlimit ps pwd pwdx pwgen readahead
    readelf readlink realpath reboot renice reset rev rfkill rm rmdir rmmod rtcwake sed seq setfattr
    setsid sha1sum sha224sum sha256sum sha384sum sha3sum sha512sum shred sleep sntp sort split
    stat strings su swapoff swapon switch_root sync sysctl tac tail tar taskset tee test time timeout
    top touch true truncate tty tunctl ulimit umount uname unicode uniq unix2dos unlink unshare
    uptime usleep uudecode uuencode uuidgen vconfig vmstat w watch watchdog wc which who whoami
    xargs xxd yes zcat

To create one html file with usage informations for all commands run:

`user `[`$`]`toybox help -a -h > /tmp/toybox.html`

Open [toybox.html] in a web browser.

### [Using toybox functions]

To use a tool specifically from toybox, execute [toybox], followed by the utility\'s (function\'s) name. For example, the following command will run toybox\'s [uname] utility:

`user `[`$`]`toybox uname -a`

    Linux pi400 5.10.63-v8 #1 SMP PREEMPT Sun Dec 5 15:48:04 CET 2021 aarch64 Toybox

## [See also]

-   [Busybox](https://wiki.gentoo.org/wiki/Busybox "Busybox") --- a utility that combines tiny versions of many common UNIX utilities into a *single, small executable*.