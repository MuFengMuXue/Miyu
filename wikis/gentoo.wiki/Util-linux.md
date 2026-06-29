**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Base "Project:Base")][Project](https://wiki.gentoo.org/wiki/Project:Base "Project:Base")

[[]][Home](https://git.kernel.org/pub/scm/utils/util-linux/util-linux.git/plain/README)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/util-linux)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Util-linux "wikipedia:Util-linux")

[[]][GitWeb](https://git.kernel.org/cgit/utils/util-linux/util-linux.git)

[[]][GitHub](https://github.com/util-linux/util-linux)

[[]][Bugs (mailing list)](mailto:util-linux@vger.kernel.org)

[[]][Bugs (GitHub)](https://github.com/util-linux/util-linux/issues)

[[]][[#util-linux](ircs://irc.libera.chat/#util-linux)] ([[webchat](https://web.libera.chat/#util-linux)])

The **util-linux** suite contains userspace utilities for Linux-specific system management, including device control, terminal logins, process management, and tty messaging. It is a fundamental block of userspace utilities for Linux systems.

On Linux systems, Gentoo includes the [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] package in the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
        -   [[1.1.1] [kill]](#kill)
        -   [[1.1.2] [tty-helpers]](#tty-helpers)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [addpart]](#addpart)
    -   [[2.2] [agetty]](#agetty)
    -   [[2.3] [blkdiscard]](#blkdiscard)
    -   [[2.4] [blkid]](#blkid)
    -   [[2.5] [blkzone]](#blkzone)
    -   [[2.6] [blockdev]](#blockdev)
    -   [[2.7] [cal]](#cal)
    -   [[2.8] [cfdisk]](#cfdisk)
    -   [[2.9] [chcpu]](#chcpu)
    -   [[2.10] [chfn]](#chfn)
    -   [[2.11] [chmem]](#chmem)
    -   [[2.12] [choom]](#choom)
    -   [[2.13] [chrt]](#chrt)
    -   [[2.14] [chsh]](#chsh)
    -   [[2.15] [col]](#col)
    -   [[2.16] [colcrt]](#colcrt)
    -   [[2.17] [colrm]](#colrm)
    -   [[2.18] [column]](#column)
    -   [[2.19] [ctrlaltdel]](#ctrlaltdel)
    -   [[2.20] [date]](#date)
    -   [[2.21] [delpart]](#delpart)
    -   [[2.22] [dmesg]](#dmesg)
    -   [[2.23] [eject]](#eject)
    -   [[2.24] [fallocate]](#fallocate)
    -   [[2.25] [fdformat]](#fdformat)
    -   [[2.26] [fdisk]](#fdisk)
    -   [[2.27] [fincore]](#fincore)
    -   [[2.28] [findfs]](#findfs)
    -   [[2.29] [findmnt]](#findmnt)
    -   [[2.30] [flock]](#flock)
    -   [[2.31] [fsck]](#fsck)
    -   [[2.32] [fsck.cramfs]](#fsck.cramfs)
    -   [[2.33] [fsck.minix]](#fsck.minix)
    -   [[2.34] [fsfreeze]](#fsfreeze)
    -   [[2.35] [fstrim]](#fstrim)
    -   [[2.36] [getopt]](#getopt)
    -   [[2.37] [hardlink]](#hardlink)
    -   [[2.38] [hexdump]](#hexdump)
    -   [[2.39] [hwclock]](#hwclock)
    -   [[2.40] [ionice]](#ionice)
    -   [[2.41] [ipcmk]](#ipcmk)
    -   [[2.42] [ipcrm]](#ipcrm)
    -   [[2.43] [ipcs]](#ipcs)
    -   [[2.44] [irqtop]](#irqtop)
    -   [[2.45] [isosize]](#isosize)
    -   [[2.46] [kill]](#kill_2)
    -   [[2.47] [last]](#last)
    -   [[2.48] [ldattach]](#ldattach)
    -   [[2.49] [line]](#line)
    -   [[2.50] [logger]](#logger)
    -   [[2.51] [login]](#login)
    -   [[2.52] [look]](#look)
    -   [[2.53] [losetup]](#losetup)
    -   [[2.54] [lsblk]](#lsblk)
    -   [[2.55] [lscpu]](#lscpu)
    -   [[2.56] [lsfd]](#lsfd)
    -   [[2.57] [lsipc]](#lsipc)
    -   [[2.58] [lsirq]](#lsirq)
    -   [[2.59] [lslocks]](#lslocks)
    -   [[2.60] [lslogins]](#lslogins)
    -   [[2.61] [lsmem]](#lsmem)
    -   [[2.62] [lsns]](#lsns)
    -   [[2.63] [mcookie]](#mcookie)
    -   [[2.64] [mesg]](#mesg)
    -   [[2.65] [mkfs]](#mkfs)
    -   [[2.66] [mkfs.bfs]](#mkfs.bfs)
    -   [[2.67] [mkfs.cramfs]](#mkfs.cramfs)
    -   [[2.68] [mkfs.minix]](#mkfs.minix)
    -   [[2.69] [mkswap]](#mkswap)
    -   [[2.70] [more]](#more)
    -   [[2.71] [mount]](#mount)
    -   [[2.72] [mountpoint]](#mountpoint)
    -   [[2.73] [namei]](#namei)
    -   [[2.74] [nsenter]](#nsenter)
    -   [[2.75] [partx]](#partx)
    -   [[2.76] [pg]](#pg)
    -   [[2.77] [pivot_root]](#pivot_root)
    -   [[2.78] [prlimit]](#prlimit)
    -   [[2.79] [readprofile]](#readprofile)
    -   [[2.80] [rename]](#rename)
    -   [[2.81] [renice]](#renice)
    -   [[2.82] [resizepart]](#resizepart)
    -   [[2.83] [rev]](#rev)
    -   [[2.84] [rfkill]](#rfkill)
    -   [[2.85] [rtcwake]](#rtcwake)
    -   [[2.86] [runuser]](#runuser)
    -   [[2.87] [script]](#script)
    -   [[2.88] [scriptlive]](#scriptlive)
    -   [[2.89] [scriptreplay]](#scriptreplay)
    -   [[2.90] [setarch]](#setarch)
    -   [[2.91] [setpriv]](#setpriv)
    -   [[2.92] [setsid]](#setsid)
    -   [[2.93] [setterm]](#setterm)
    -   [[2.94] [sfdisk]](#sfdisk)
    -   [[2.95] [su]](#su)
    -   [[2.96] [sulogin]](#sulogin)
    -   [[2.97] [swaplabel]](#swaplabel)
    -   [[2.98] [swapoff]](#swapoff)
    -   [[2.99] [swapon]](#swapon)
    -   [[2.100] [switch_root]](#switch_root)
    -   [[2.101] [taskset]](#taskset)
    -   [[2.102] [uclampset]](#uclampset)
    -   [[2.103] [ul]](#ul)
    -   [[2.104] [umount]](#umount)
    -   [[2.105] [unshare]](#unshare)
    -   [[2.106] [utmpdump]](#utmpdump)
    -   [[2.107] [uuid]](#uuid)
    -   [[2.108] [uuidgen]](#uuidgen)
    -   [[2.109] [uuidparse]](#uuidparse)
    -   [[2.110] [wall]](#wall)
    -   [[2.111] [wdctl]](#wdctl)
    -   [[2.112] [whereis]](#whereis)
    -   [[2.113] [wipefs]](#wipefs)
    -   [[2.114] [write]](#write)
    -   [[2.115] [zramctl]](#zramctl)
-   [[3] [Listing commands]](#Listing_commands)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [See also]](#See_also)

## [Installation]

### [USE flags]

** Warning**\
Some of these [USE flags](https://wiki.gentoo.org/wiki/USE_flag "USE flag") provide core system functionality, and may be relied upon by users, or software. Some of these USE flags install commands that may conflict with commands provided by other packages. For example disabling the [[[su]](https://packages.gentoo.org/useflags/su)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag could leave a system without the [su] command, and [[[kill]](https://packages.gentoo.org/useflags/kill)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] could conflict with [[[sys-process/procps]](https://packages.gentoo.org/packages/sys-process/procps)[]].

### [USE flags for] [sys-apps/util-linux](https://packages.gentoo.org/packages/sys-apps/util-linux) [[]] [Various useful Linux utilities]

  ------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+cramfs`](https://packages.gentoo.org/useflags/+cramfs)           build mkfs/fsck helpers for cramfs filesystems
  [`+hardlink`](https://packages.gentoo.org/useflags/+hardlink)       build hardlink program
  [`+logger`](https://packages.gentoo.org/useflags/+logger)           build the logger program
  [`+readline`](https://packages.gentoo.org/useflags/+readline)       Enable support for libreadline, a GNU line-editing library that almost everyone wants
  [`+su`](https://packages.gentoo.org/useflags/+su)                   build the su program
  [`+suid`](https://packages.gentoo.org/useflags/+suid)               Install some programs with suid bit set to provide additional functionality. mount/umount: non-root users may mount/umount devices wall/write: non-root users can notify other users su: non-root users may become root
  [`audit`](https://packages.gentoo.org/useflags/audit)               Use sys-process/audit to emit audit messages about system changes
  [`build`](https://packages.gentoo.org/useflags/build)               !!internal use only!! DO NOT SET THIS FLAG YOURSELF!, used for creating build images and the first half of bootstrapping \[make stage1\]
  [`caps`](https://packages.gentoo.org/useflags/caps)                 build setpriv helper (run programs with diff capabilities)
  [`cryptsetup`](https://packages.gentoo.org/useflags/cryptsetup)     Use sys-fs/cryptsetup to have built-in dm-verity in libmount
  [`fdformat`](https://packages.gentoo.org/useflags/fdformat)         build fdformat (floppy disk format)
  [`kill`](https://packages.gentoo.org/useflags/kill)                 build the kill program
  [`magic`](https://packages.gentoo.org/useflags/magic)               Add support for file type detection via magic bytes (usually via libmagic from sys-apps/file)
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)           Add ncurses support (console display library)
  [`nls`](https://packages.gentoo.org/useflags/nls)                   Add Native Language Support (using gettext - GNU locale utilities)
  [`pam`](https://packages.gentoo.org/useflags/pam)                   build runuser helper
  [`python`](https://packages.gentoo.org/useflags/python)             Add optional support/bindings for the Python language
  [`rtas`](https://packages.gentoo.org/useflags/rtas)                 Add support for the Run Time Abstraction Services (RTAS)
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`slang`](https://packages.gentoo.org/useflags/slang)               Add support for the slang text display library (it\'s like ncurses, but different)
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tty-helpers`](https://packages.gentoo.org/useflags/tty-helpers)   install the mesg/wall/write tools for talking to local users
  [`udev`](https://packages.gentoo.org/useflags/udev)                 Enable virtual/udev integration (device discovery, power and storage device support, etc)
  [`unicode`](https://packages.gentoo.org/useflags/unicode)           Add support for Unicode
  [`uuidd`](https://packages.gentoo.org/useflags/uuidd)               build uuidd daemon
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)     Verify upstream signatures on distfiles
  ------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 01:41] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [kill]

Gentoo toolchain developers have decided the [[[sys-process/procps]](https://packages.gentoo.org/packages/sys-process/procps)[]] package will be the default provider of the [kill] utility for the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)").

As a result, enabling the `kill` USE flag usually creates a conflict between the [[[sys-process/procps]](https://packages.gentoo.org/packages/sys-process/procps)[]] and [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] packages. Both packages include the [kill] command, and both packages are capable of conditionally building the [kill] utility by setting the `kill` USE flag (in fact, [[[sys-apps/coreutils]](https://packages.gentoo.org/packages/sys-apps/coreutils)[]] also includes support for a [kill] command).

#### [tty-helpers]

The [mesg], [wall], and [write] utilities are installed using the `tty-helpers` USE flag. This can be viewed by scrolling down in [USE flags](#USE_flags) section above.

For security reasons, these utilities are disabled by default.

### [Emerge]

Since on Linux systems [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] is installed by default, it rarely needs to be installed manually. If for some reason it needs to be installed or reinstalled, for example due to [USE flag](#USE_flags) change, the following command should be used.

`root `[`#`]`emerge --ask --oneshot sys-apps/util-linux`

** Note**\
`--oneshot` is used in the above command because [[[sys-apps/util-linux]](https://packages.gentoo.org/packages/sys-apps/util-linux)[]] is included in the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"), so it should not be added to the [selected set](https://wiki.gentoo.org/wiki/Selected_set_(Portage) "Selected set (Portage)") ([/var/lib/porage/world] file).

## [Usage]

There are many utilities included in the util-linux package.

### [addpart]

Tell the kernel about the existence of a specified [partition](https://wiki.gentoo.org/wiki/Partition "Partition").

`user `[`$`]`addpart --help`

    Usage:
     addpart <disk device>  <start> <length>

    Tell the kernel about the existence of a specified partition.

    Options:
     -h, --help     display this help
     -V, --version  display version

    For more details see addpart(8).

### [agetty]

Open a [tty](https://wiki.gentoo.org/wiki/Terminal_emulator "Terminal emulator") and prompt for login - acts as an alternative Linux [getty].

`user `[`$`]`agetty --help`

    Usage:
     agetty [options] <line> [<baud_rate>,...] [<termtype>]
     agetty [options] <baud_rate>,... <line> [<termtype>]

    Open a terminal and set its mode.

    Options:
     -8, --8bits                assume 8-bit tty
     -a, --autologin <user>     login the specified user automatically
     -c, --noreset              do not reset control mode
     -E, --remote               use -r <hostname> for login(1)
     -f, --issue-file <list>    display issue files or directories
         --show-issue           display issue file and exit
     -h, --flow-control         enable hardware flow control
     -H, --host <hostname>      specify login host
     -i, --noissue              do not display issue file
     -I, --init-string <string> set init string
     -J  --noclear              do not clear the screen before prompt
     -l, --login-program <file> specify login program
     -L, --local-line[=<mode>]  control the local line flag
     -m, --extract-baud         extract baud rate during connect
     -n, --skip-login           do not prompt for login
     -N  --nonewline            do not print a newline before issue
     -o, --login-options <opts> options that are passed to login
     -p, --login-pause          wait for any key before the login
     -r, --chroot <dir>         change root to the directory
     -R, --hangup               do virtually hangup on the tty
     -s, --keep-baud            try to keep baud rate after break
     -t, --timeout <number>     login process timeout
     -U, --detect-case          detect uppercase terminal
     -w, --wait-cr              wait carriage-return
         --nohints              do not print hints
         --nohostname           no hostname at all will be shown
         --long-hostname        show full qualified hostname
         --erase-chars <string> additional backspace chars
         --kill-chars <string>  additional kill chars
         --chdir <directory>    chdir before the login
         --delay <number>       sleep seconds before prompt
         --nice <number>        run login with this priority
         --reload               reload prompts on running agetty instances
         --list-speeds          display supported baud rates
         --help                 display this help
         --version              display version

    For more details see agetty(8).

### [blkdiscard]

Discard the content of sectors on a [device](https://wiki.gentoo.org/wiki/Device_file "Device file").

`user `[`$`]`blkdiscard --help`

    Usage:
     blkdiscard [options] <device>

    Discard the content of sectors on a device.

    Options:
     -f, --force         disable all checking
     -o, --offset <num>  offset in bytes to discard from
     -l, --length <num>  length of bytes to discard from the offset
     -p, --step <num>    size of the discard iterations within the offset
     -s, --secure        perform secure discard
     -z, --zeroout       zero-fill rather than discard
     -v, --verbose       print aligned length and offset

     -h, --help          display this help
     -V, --version       display version

    Arguments:
     <num> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

    For more details see blkdiscard(8).

### [blkid]

Print block device information.

`user `[`$`]`blkid --help`

    Usage:
     blkid --label <label> | --uuid <uuid>

     blkid [--cache-file <file>] [-ghlLv] [--output <format>] [--match-tag <tag>]
           [--match-token <token>] [<dev> ...]

     blkid -p [--match-tag <tag>] [--offset <offset>] [--size <size>]
           [--output <format>] <dev> ...

     blkid -i [--match-tag <tag>] [--output <format>] <dev> ...

    Options:
     -c, --cache-file <file>    read from <file> instead of reading from the default
                                  cache file (-c /dev/null means no cache)
     -d, --no-encoding          don't encode non-printing characters
     -g, --garbage-collect      garbage collect the blkid cache
     -o, --output <format>      output format; can be one of:
                                  value, device, export or full; (default: full)
     -k, --list-filesystems     list all known filesystems/RAIDs and exit
     -s, --match-tag <tag>      show specified tag(s) (default show all tags)
     -t, --match-token <token>  find device with a specific token (NAME=value pair)
     -l, --list-one             look up only first device with token specified by -t
     -L, --label <label>        convert LABEL to device name
     -U, --uuid <uuid>          convert UUID to device name

    Low-level probing options:
     -p, --probe                low-level superblocks probing (bypass cache)
     -i, --info                 gather information about I/O limits
     -H, --hint <value>         set hint for probing function
     -S, --size <size>          overwrite device size
     -O, --offset <offset>      probe at the given offset
     -u, --usages <list>        filter by "usage" (e.g. -u filesystem,raid)
     -n, --match-types <list>   filter by filesystem type (e.g. -n vfat,ext3)
     -D, --no-part-details      don't print info from partition table

     -h, --help                 display this help
     -V, --version              display version

    Arguments:
     <size> and <offset> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

     <dev> specify device(s) to probe (default: all devices)

    For more details see blkid(8).

### [blkzone]

Run zone command on the given block device.

`user `[`$`]`blkzone --help`

    Usage:
     blkzone <command> [options] <device>

    Run zone command on the given block device.

    Commands:
     report       Report zone information about the given device
     capacity     Report sum of zone capacities for the given device
     reset        Reset a range of zones.
     open         Open a range of zones.
     close        Close a range of zones.
     finish       Set a range of zones to Full.

    Options:
     -o, --offset <sector>  start sector of zone to act (in 512-byte sectors)
     -l, --length <sectors> maximum sectors to act (in 512-byte sectors)
     -c, --count <number>   maximum number of zones
     -f, --force            enforce on block devices used by the system
     -v, --verbose          display more details

     -h, --help             display this help
     -V, --version          display version

    Arguments:
     <sector> and <sectors> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

    For more details see blkzone(8).

### [blockdev]

Call block device ioctls from the command line.

`user `[`$`]`blockdev --help`

    Usage:
     blockdev [-v|-q] commands devices
     blockdev --report [devices]
     blockdev -h|-V

    Call block device ioctls from the command line.

    Options:
     -q             quiet mode
     -v             verbose mode
         --report   print report for specified (or all) devices

     -h, --help     display this help
     -V, --version  display version

    Available commands:
     --getsz                   get size in 512-byte sectors
     --setro                   set read-only
     --setrw                   set read-write
     --getro                   get read-only
     --getdiscardzeroes        get discard zeroes support status
     --getss                   get logical block (sector) size
     --getpbsz                 get physical block (sector) size
     --getiomin                get minimum I/O size
     --getioopt                get optimal I/O size
     --getalignoff             get alignment offset in bytes
     --getmaxsect              get max sectors per request
     --getbsz                  get blocksize
     --setbsz <bytes>          set blocksize on file descriptor opening the block device
     --getsize                 get 32-bit sector count (deprecated, use --getsz)
     --getsize64               get size in bytes
     --setra <sectors>         set readahead
     --getra                   get readahead
     --setfra <sectors>        set filesystem readahead
     --getfra                  get filesystem readahead
     --flushbufs               flush buffers
     --rereadpt                reread partition table

    For more details see blockdev(8).

### [cal]

Display a calendar, or some part of it.

`user `[`$`]`cal --help`

    Usage:
     cal [options] [[[day] month] year]
     cal [options] <timestamp|monthname>

    Display a calendar, or some part of it.
    Without any arguments, display the current month.

    Options:
     -1, --one             show only a single month (default)
     -3, --three           show three months spanning the date
     -n, --months <num>    show num months starting with date's month
     -S, --span            span the date when displaying multiple months
     -s, --sunday          Sunday as first day of week
     -m, --monday          Monday as first day of week
     -j, --julian          use day-of-year for all calendars
         --reform <val>    Gregorian reform date (1752|gregorian|iso|julian)
         --iso             alias for --reform=iso
     -y, --year            show the whole year
     -Y, --twelve          show the next twelve months
     -w, --week[=<num>]    show US or ISO-8601 week numbers
     -v, --vertical        show day vertically instead of line
         --color[=<when>]  colorize messages (auto, always or never)
                             colors are enabled by default

     -h, --help            display this help
     -V, --version         display version

    For more details see cal(1).

### [cfdisk]

Display or manipulate a disk partition table.

`user `[`$`]`cfdisk --help`

    Usage:
     cfdisk [options] <disk>

    Display or manipulate a disk partition table.

    Options:
     -L, --color[=<when>]     colorize output (auto, always or never)
                                colors are enabled by default
     -z, --zero               start with zeroed partition table
         --lock[=<mode>]      use exclusive device lock (yes, no or nonblock)
     -r, --read-only          forced open cfdisk in read-only mode

     -h, --help               display this help
     -V, --version            display version

    For more details see cfdisk(8).

### [chcpu]

Configure CPUs in a multi-processor system.

`user `[`$`]`chcpu --help`

    Usage:
     chcpu [options]

    Configure CPUs in a multi-processor system.

    Options:
     -e, --enable <cpu-list>       enable cpus
     -d, --disable <cpu-list>      disable cpus
     -c, --configure <cpu-list>    configure cpus
     -g, --deconfigure <cpu-list>  deconfigure cpus
     -p, --dispatch <mode>         set dispatching mode
     -r, --rescan                  trigger rescan of cpus
     -h, --help                    display this help
     -V, --version                 display version

    For more details see chcpu(8).

### [chfn]

Change [finger](https://en.wikipedia.org/wiki/Finger_(protocol) "wikipedia:Finger (protocol)") informaiton.

`user `[`$`]`chfn --help`

    Usage: chfn [options] [LOGIN]

    Options:
      -f, --full-name FULL_NAME     change user's full name
      -h, --home-phone HOME_PHONE   change user's home phone number
      -o, --other OTHER_INFO        change user's other GECOS information
      -r, --room ROOM_NUMBER        change user's room number
      -R, --root CHROOT_DIR         directory to chroot into
      -u, --help                    display this help message and exit
      -w, --work-phone WORK_PHONE   change user's office phone number

### [chmem]

Set a particular size or range of memory online or offline.

`user `[`$`]`chmem --help`

    Usage:
     chmem [options] [SIZE|RANGE|BLOCKRANGE]

    Set a particular size or range of memory online or offline.

    Options:
     -e, --enable       enable memory
     -d, --disable      disable memory
     -b, --blocks       use memory blocks
     -z, --zone <name>  select memory zone (see below)
     -v, --verbose      verbose output
     -h, --help         display this help
     -V, --version      display version

    Supported zones:
     DMA
     DMA32
     Normal
     Highmem
     Movable
     Device

    For more details see chmem(8).

### [choom]

Display and adjust [OOM-killer](https://en.wikipedia.org/wiki/Out_of_memory#Out_of_memory_management "wikipedia:Out of memory") score.

`user `[`$`]`choom --help`

    Usage:
     choom [options] -p pid
     choom [options] -n number -p pid
     choom [options] -n number [--] command [args...]]

    Display and adjust OOM-killer score.

    Options:
     -n, --adjust <num>     specify the adjust score value
     -p, --pid <num>        process ID

     -h, --help             display this help
     -V, --version          display version

    For more details see choom(1).

### [chrt]

Show or change the real-time scheduling attributes of a process.

`user `[`$`]`chrt --help`

    Show or change the real-time scheduling attributes of a process.

    Set policy:
     chrt [options]  <command> [<arg>...]
     chrt [options] --pid

    Get policy:
     chrt [options] -p

    Policy options:
     -b, --batch          set policy to SCHED_BATCH
     -d, --deadline       set policy to SCHED_DEADLINE
     -f, --fifo           set policy to SCHED_FIFO
     -i, --idle           set policy to SCHED_IDLE
     -o, --other          set policy to SCHED_OTHER
     -r, --rr             set policy to SCHED_RR (default)

    Scheduling options:
     -R, --reset-on-fork       set reset-on-fork flag
     -T, --sched-runtime <ns>  runtime parameter for DEADLINE
     -P, --sched-period <ns>   period parameter for DEADLINE
     -D, --sched-deadline <ns> deadline parameter for DEADLINE

    Other options:
     -a, --all-tasks      operate on all the tasks (threads) for a given pid
     -m, --max            show min and max valid priorities
     -p, --pid            operate on existing given pid
     -v, --verbose        display status information

     -h, --help           display this help
     -V, --version        display version

    For more details see chrt(1).

### [chsh]

Change [login](https://wiki.gentoo.org/wiki/Login "Login") [shell](https://wiki.gentoo.org/wiki/Shell "Shell") for a user.

`user `[`$`]`chsh --help`

    Usage: chsh [options] [LOGIN]

    Options:
      -h, --help                    display this help message and exit
      -R, --root CHROOT_DIR         directory to chroot into
      -s, --shell SHELL             new login shell for the user account

### [col]

Filter out reverse line feeds from standard input.

`user `[`$`]`col --help`

    Usage:
     col [options]

    Filter out reverse line feeds from standard input.

    Options:
     -b, --no-backspaces    do not output backspaces
     -f, --fine             permit forward half line feeds
     -p, --pass             pass unknown control sequences
     -h, --tabs             convert spaces to tabs
     -x, --spaces           convert tabs to spaces
     -l, --lines NUM        buffer at least NUM lines
     -H, --help             display this help
     -v, --version          display version

    For more details see col(1).

### [colcrt]

Filter [nroff](https://en.wikipedia.org/wiki/nroff "wikipedia:nroff") output for CRT previewing.

`user `[`$`]`colcrt --help`

    Usage:
     colcrt [options] [<file>...]

    Filter nroff output for CRT previewing.

    Options:
     -,  --no-underlining    suppress all underlining
     -2, --half-lines        print all half-lines

     -h, --help              display this help
     -V, --version           display version

    For more details see colcrt(1).

### [colrm]

Filter out the specified columns.

`user `[`$`]`colrm --help`

    Usage:
     colrm [startcol [endcol]]

    Filter out the specified columns.

    Options:
     -h, --help     display this help
     -V, --version  display version
    colrm reads from standard input and writes to standard output

    For more details see colrm(1).

### [column]

Columnate lists.

`user `[`$`]`column --help`

    Usage:
     column [options] [<file>...]

    Columnate lists.

    Options:
     -t, --table                      create a table
     -n, --table-name <name>          table name for JSON output
     -O, --table-order <columns>      specify order of output columns
     -N, --table-columns <names>      comma separated columns names
     -l, --table-columns-limit <num>  maximal number of input columns
     -E, --table-noextreme <columns>  don't count long text from the columns to column width
     -d, --table-noheadings           don't print header
     -e, --table-header-repeat        repeat header for each page
     -H, --table-hide <columns>       don't print the columns
     -R, --table-right <columns>      right align text in these columns
     -T, --table-truncate <columns>   truncate text in the columns when necessary
     -W, --table-wrap <columns>       wrap text in the columns when necessary
     -L, --keep-empty-lines           don't ignore empty lines
     -J, --json                       use JSON output format for table

     -r, --tree <column>              column to use tree-like output for the table
     -i, --tree-id <column>           line ID to specify child-parent relation
     -p, --tree-parent <column>       parent to specify child-parent relation

     -c, --output-width <width>       width of output in number of characters
     -o, --output-separator <string>  columns separator for table output (default is two spaces)
     -s, --separator <string>         possible table delimiters
     -x, --fillrows                   fill rows before columns

     -h, --help                       display this help
     -V, --version                    display version

    For more details see column(1).

### [ctrlaltdel]

Set the function of the Ctrl-Alt-Del combination.

`user `[`$`]`ctrlaltdel --help`

    Usage:
     ctrlaltdel hard|soft

    Set the function of the Ctrl-Alt-Del combination.

    Options:
     -h, --help     display this help
     -V, --version  display version

    For more details see ctrlaltdel(8).

### [date]

Display the current [time](https://wiki.gentoo.org/wiki/System_time "System time") in the given FORMAT, or set the system date.

`user `[`$`]`date --help`

    Usage: date [OPTION]... [+FORMAT]
      or:  date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]
    Display the current time in the given FORMAT, or set the system date.

    Mandatory arguments to long options are mandatory for short options too.
      -d, --date=STRING          display time described by STRING, not 'now'
          --debug                annotate the parsed date,
                                  and warn about questionable usage to stderr
      -f, --file=DATEFILE        like --date; once for each line of DATEFILE
      -I[FMT], --iso-8601[=FMT]  output date/time in ISO 8601 format.
                                   FMT='date' for date only (the default),
                                   'hours', 'minutes', 'seconds', or 'ns'
                                   for date and time to the indicated precision.
                                   Example: 2006-08-14T02:34:56-06:00
      -R, --rfc-email            output date and time in RFC 5322 format.
                                   Example: Mon, 14 Aug 2006 02:34:56 -0600
          --rfc-3339=FMT         output date/time in RFC 3339 format.
                                   FMT='date', 'seconds', or 'ns'
                                   for date and time to the indicated precision.
                                   Example: 2006-08-14 02:34:56-06:00
      -r, --reference=FILE       display the last modification time of FILE
      -s, --set=STRING           set time described by STRING
      -u, --utc, --universal     print or set Coordinated Universal Time (UTC)
          --help     display this help and exit
          --version  output version information and exit

    FORMAT controls the output.  Interpreted sequences are:

      %%   a literal %
      %a   locale's abbreviated weekday name (e.g., Sun)
      %A   locale's full weekday name (e.g., Sunday)
      %b   locale's abbreviated month name (e.g., Jan)
      %B   locale's full month name (e.g., January)
      %c   locale's date and time (e.g., Thu Mar  3 23:05:25 2005)
      %C   century; like %Y, except omit last two digits (e.g., 20)
      %d   day of month (e.g., 01)
      %D   date; same as %m/%d/%y
      %e   day of month, space padded; same as %_d
      %F   full date; like %+4Y-%m-%d
      %g   last two digits of year of ISO week number (see %G)
      %G   year of ISO week number (see %V); normally useful only with %V
      %h   same as %b
      %H   hour (00..23)
      %I   hour (01..12)
      %j   day of year (001..366)
      %k   hour, space padded ( 0..23); same as %_H
      %l   hour, space padded ( 1..12); same as %_I
      %m   month (01..12)
      %M   minute (00..59)
      %n   a newline
      %N   nanoseconds (000000000..999999999)
      %p   locale's equivalent of either AM or PM; blank if not known
      %P   like %p, but lower case
      %q   quarter of year (1..4)
      %r   locale's 12-hour clock time (e.g., 11:11:04 PM)
      %R   24-hour hour and minute; same as %H:%M
      %s   seconds since 1970-01-01 00:00:00 UTC
      %S   second (00..60)
      %t   a tab
      %T   time; same as %H:%M:%S
      %u   day of week (1..7); 1 is Monday
      %U   week number of year, with Sunday as first day of week (00..53)
      %V   ISO week number, with Monday as first day of week (01..53)
      %w   day of week (0..6); 0 is Sunday
      %W   week number of year, with Monday as first day of week (00..53)
      %x   locale's date representation (e.g., 12/31/99)
      %X   locale's time representation (e.g., 23:13:48)
      %y   last two digits of year (00..99)
      %Y   year
      %z   +hhmm numeric time zone (e.g., -0400)
      %:z  +hh:mm numeric time zone (e.g., -04:00)
      %::z  +hh:mm:ss numeric time zone (e.g., -04:00:00)
      %:::z  numeric time zone with : to necessary precision (e.g., -04, +05:30)
      %Z   alphabetic time zone abbreviation (e.g., EDT)

    By default, date pads numeric fields with zeroes.
    The following optional flags may follow '%':

      -  (hyphen) do not pad the field
      _  (underscore) pad with spaces
      0  (zero) pad with zeros
      +  pad with zeros, and put '+' before future years with >4 digits
      ^  use upper case if possible
      #  use opposite case if possible

    After any flags comes an optional field width, as a decimal number;
    then an optional modifier, which is either
    E to use the locale's alternate representations if available, or
    O to use the locale's alternate numeric symbols if available.

    Examples:
    Convert seconds since the epoch (1970-01-01 UTC) to a date
      $ date --date='@2147483647'

    Show the time on the west coast of the US (use tzselect(1) to find TZ)
      $ TZ='America/Los_Angeles' date

    Show the local time for 9AM next Friday on the west coast of the US
      $ date --date='TZ="America/Los_Angeles" 09:00 next Fri'

    GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
    Full documentation <https://www.gnu.org/software/coreutils/date>
    or available locally via: info '(coreutils) date invocation'

### [delpart]

Tell the kernel to forget about a specified partition.

`user `[`$`]`delpart --help`

    Usage:
     delpart <disk device>

    Tell the kernel to forget about a specified partition.

    Options:
     -h, --help     display this help
     -V, --version  display version

    For more details see delpart(8).

### [dmesg]

Print or control the kernel messaging buffer.

`user `[`$`]`dmesg --help`

    Usage:
     dmesg [options]

    Display or control the kernel ring buffer.

    Options:
     -C, --clear                 clear the kernel ring buffer
     -c, --read-clear            read and clear all messages
     -D, --console-off           disable printing messages to console
     -E, --console-on            enable printing messages to console
     -F, --file <file>           use the file instead of the kernel log buffer
     -f, --facility <list>       restrict output to defined facilities
     -H, --human                 human readable output
     -J, --json                  use JSON output format
     -k, --kernel                display kernel messages
     -L, --color[=<when>]        colorize messages (auto, always or never)
                                   colors are enabled by default
     -l, --level <list>          restrict output to defined levels
     -n, --console-level <level> set level of messages printed to console
     -P, --nopager               do not pipe output into a pager
     -p, --force-prefix          force timestamp output on each line of multi-line messages
     -r, --raw                   print the raw message buffer
         --noescape              don't escape unprintable character
     -S, --syslog                force to use syslog(2) rather than /dev/kmsg
     -s, --buffer-size <size>    buffer size to query the kernel ring buffer
     -u, --userspace             display userspace messages
     -w, --follow                wait for new messages
     -W, --follow-new            wait and print only new messages
     -x, --decode                decode facility and level to readable string
     -d, --show-delta            show time delta between printed messages
     -e, --reltime               show local time and time delta in readable format
     -T, --ctime                 show human-readable timestamp (may be inaccurate!)
     -t, --notime                don't show any timestamp with messages
         --time-format <format>  show timestamp using the given format:
                                   [delta|reltime|ctime|notime|iso]
    Suspending/resume will make ctime and iso timestamps inaccurate.
         --since <time>          display the lines since the specified time
         --until <time>          display the lines until the specified time

     -h, --help                  display this help
     -V, --version               display version

    Supported log facilities:
        kern - kernel messages
        user - random user-level messages
        mail - mail system
      daemon - system daemons
        auth - security/authorization messages
      syslog - messages generated internally by syslogd
         lpr - line printer subsystem
        news - network news subsystem

    Supported log levels (priorities):
       emerg - system is unusable
       alert - action must be taken immediately
        crit - critical conditions
         err - error conditions
        warn - warning conditions
      notice - normal but significant condition
        info - informational
       debug - debug-level messages

    For more details see dmesg(1).

### [eject]

Eject [removable media](https://wiki.gentoo.org/wiki/Removable_media "Removable media") via software control.

`user `[`$`]`eject --help`

    Usage:
     eject [options] [<device>|<mountpoint>]

    Eject removable media.

    Options:
     -a, --auto <on|off>         turn auto-eject feature on or off
     -c, --changerslot <slot>    switch discs on a CD-ROM changer
     -d, --default               display default device
     -f, --floppy                eject floppy
     -F, --force                 don't care about device type
     -i, --manualeject <on|off>  toggle manual eject protection on/off
     -m, --no-unmount            do not unmount device even if it is mounted
     -M, --no-partitions-unmount do not unmount another partitions
     -n, --noop                  don't eject, just show device found
     -p, --proc                  use /proc/mounts instead of /etc/mtab
     -q, --tape                  eject tape
     -r, --cdrom                 eject CD-ROM
     -s, --scsi                  eject SCSI device
     -t, --trayclose             close tray
     -T, --traytoggle            toggle tray
     -v, --verbose               enable verbose output
     -x, --cdspeed <speed>       set CD-ROM max speed
     -X, --listspeed             list CD-ROM available speeds

     -h, --help                  display this help
     -V, --version               display version

    By default tries -r, -s, -f, and -q in order until success.

    For more details see eject(1).

### [fallocate]

Preallocate space to, or deallocate space from a file.

`user `[`$`]`fallocate --help`

    Usage:
     fallocate [options] <filename>

    Preallocate space to, or deallocate space from a file.

    Options:
     -c, --collapse-range remove a range from the file
     -d, --dig-holes      detect zeroes and replace with holes
     -i, --insert-range   insert a hole at range, shifting existing data
     -l, --length <num>   length for range operations, in bytes
     -n, --keep-size      maintain the apparent size of the file
     -o, --offset <num>   offset for range operations, in bytes
     -p, --punch-hole     replace a range with a hole (implies -n)
     -z, --zero-range     zero and ensure allocation of a range
     -x, --posix          use posix_fallocate(3) instead of fallocate(2)
     -v, --verbose        verbose mode

     -h, --help           display this help
     -V, --version        display version

    Arguments:
     <num> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

    For more details see fallocate(1).

### [fdformat]

Low-level format a floppy disk.

Command only available if the [[[fdformat]](https://packages.gentoo.org/useflags/fdformat)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set.

### [fdisk]

Manipulate partition table.

`user `[`$`]`fdisk --help`

    Usage:
     fdisk [options] <disk>         change partition table
     fdisk [options] -l [<disk>...] list partition table(s)

    Display or manipulate a disk partition table.

    Options:
     -b, --sector-size <size>      physical and logical sector size
     -B, --protect-boot            don't erase bootbits when creating a new label
     -c, --compatibility[=<mode>]  mode is 'dos' or 'nondos' (default)
     -L, --color[=<when>]          colorize output (auto, always or never)
                                     colors are enabled by default
     -l, --list                    display partitions and exit
     -x, --list-details            like --list but with more details
     -n, --noauto-pt               don't create default partition table on empty devices
     -o, --output <list>           output columns
     -t, --type <type>             recognize specified partition table type only
     -u, --units[=<unit>]          display units: 'cylinders' or 'sectors' (default)
     -s, --getsz                   display device size in 512-byte sectors [DEPRECATED]
         --bytes                   print SIZE in bytes rather than in human readable format
         --lock[=<mode>]           use exclusive device lock (yes, no or nonblock)
     -w, --wipe <mode>             wipe signatures (auto, always or never)
     -W, --wipe-partitions <mode>  wipe signatures from new partitions (auto, always or never)

     -C, --cylinders <number>      specify the number of cylinders
     -H, --heads <number>          specify the number of heads
     -S, --sectors <number>        specify the number of sectors per track

     -h, --help                    display this help
     -V, --version                 display version

    Available output columns:
     gpt: Device Start End Sectors Size Type Type-UUID Attrs Name UUID
     dos: Device Start End Sectors Cylinders Size Type Id Attrs Boot End-C/H/S Start-C/H/S
     bsd: Slice Start End Sectors Cylinders Size Type Bsize Cpg Fsize
     sgi: Device Start End Sectors Cylinders Size Type Id Attrs
     sun: Device Start End Sectors Cylinders Size Type Id Flags

    For more details see fdisk(8).

### [fincore]

Count pages of file contents in core.

`user `[`$`]`fincore --help`

    Usage:
     fincore [options] file...

    Options:
     -J, --json            use JSON output format
     -b, --bytes           print sizes in bytes rather than in human readable format
     -n, --noheadings      don't print headings
     -o, --output <list>   output columns
     -r, --raw             use raw output format

     -h, --help            display this help
     -V, --version         display version

    Available output columns:
           PAGES  file data resident in memory in pages
            SIZE  size of the file
            FILE  file name
             RES  file data resident in memory in bytes

    For more details see fincore(1).

### [findfs]

Find a filesystem by label or UUID.

`user `[`$`]`findfs --help`

    Usage:
     findfs [options] =<value>

    Find a filesystem by label or UUID.

    Options:
     -h, --help     display this help
     -V, --version  display version

    For more details see findfs(8).

### [findmnt]

Find a (mounted) [filesystem](https://wiki.gentoo.org/wiki/Filesystem "Filesystem"): list or search mounted filesystems.

`user `[`$`]`findmnt --help`

    Usage:
     findmnt [options]
     findmnt [options] <device> | <mountpoint>
     findmnt [options] <device> <mountpoint>
     findmnt [options] [--source <device>] [--target  | --mountpoint <dir>]

    Find a (mounted) filesystem.

    Options:
     -s, --fstab            search in static table of filesystems
     -m, --mtab             search in table of mounted filesystems
                              (includes user space mount options)
     -k, --kernel           search in kernel table of mounted
                              filesystems (default)

     -p, --poll[=<list>]    monitor changes in table of mounted filesystems
     -w, --timeout <num>    upper limit in milliseconds that --poll will block

     -A, --all              disable all built-in filters, print all filesystems
     -a, --ascii            use ASCII chars for tree formatting
     -b, --bytes            print sizes in bytes rather than in human readable format
     -C, --nocanonicalize   don't canonicalize when comparing paths
     -c, --canonicalize     canonicalize printed paths
     -D, --df               imitate the output of df(1)
     -d, --direction <word> direction of search, 'forward' or 'backward'
     -e, --evaluate         convert tags (LABEL,UUID,PARTUUID,PARTLABEL)
                              to device names
     -F, --tab-file   alternative file for -s, -m or -k options
     -f, --first-only       print the first found filesystem only
     -i, --invert           invert the sense of matching
     -J, --json             use JSON output format
     -l, --list             use list format output
     -N, --task <tid>       use alternative namespace (/proc/<tid>/mountinfo file)
     -n, --noheadings       don't print column headings
     -O, --options <list>   limit the set of filesystems by mount options
     -o, --output <list>    the output columns to be shown
         --output-all       output all available columns
     -P, --pairs            use key="value" output format
         --pseudo           print only pseudo-filesystems
         --shadowed         print only filesystems over-mounted by another filesystem
     -R, --submounts        print all submounts for the matching filesystems
     -r, --raw              use raw output format
         --real             print only real filesystems
     -S, --source <string>  the device to mount (by name, maj:min,
                              LABEL=, UUID=, PARTUUID=, PARTLABEL=)
     -T, --target     the path to the filesystem to use
         --tree             enable tree format output if possible
     -M, --mountpoint <dir> the mountpoint directory
     -t, --types <list>     limit the set of filesystems by FS types
     -U, --uniq             ignore filesystems with duplicate target
     -u, --notruncate       don't truncate text in columns
     -v, --nofsroot         don't print [/dir] for bind or btrfs mounts

     -x, --verify           verify mount table content (default is fstab)
         --verbose          print more details
         --vfs-all          print all VFS options

     -h, --help             display this help
     -V, --version          display version

    Available output columns:
          ACTION  action detected by --poll
           AVAIL  filesystem size available
            FREQ  dump(8) period in days [fstab only]
          FSROOT  filesystem root
          FSTYPE  filesystem type
      FS-OPTIONS  FS specific mount options
              ID  mount ID
           LABEL  filesystem label
         MAJ:MIN  major:minor device number
     OLD-OPTIONS  old mount options saved by --poll
      OLD-TARGET  old mountpoint saved by --poll
         OPTIONS  all mount options
      OPT-FIELDS  optional mount fields
          PARENT  mount parent ID
       PARTLABEL  partition label
        PARTUUID  partition UUID
          PASSNO  pass number on parallel fsck(8) [fstab only]
     PROPAGATION  VFS propagation flags
            SIZE  filesystem size
          SOURCE  source device
          TARGET  mountpoint
             TID  task ID
            USED  filesystem size used
            USE%  filesystem use percentage
            UUID  filesystem UUID
     VFS-OPTIONS  VFS specific mount options

    For more details see findmnt(8).

### [flock]

Utilize serialization using file locks.

`user `[`$`]`flock --help`

    Usage:
     flock [options] <file>|<directory> <command> [<argument>...]
     flock [options] <file>|<directory> -c <command>
     flock [options] <file descriptor number>

    Manage file locks from shell scripts.

    Options:
     -s, --shared             get a shared lock
     -x, --exclusive          get an exclusive lock (default)
     -u, --unlock             remove a lock
     -n, --nonblock           fail rather than wait
     -w, --timeout <secs>     wait for a limited amount of time
     -E, --conflict-exit-code <number>  exit code after conflict or timeout
     -o, --close              close file descriptor before running command
     -c, --command <command>  run a single command string through the shell
     -F, --no-fork            execute command without forking
         --verbose            increase verbosity

     -h, --help               display this help
     -V, --version            display version

    For more details see flock(1).

### [fsck]

Perform a file system check and repair.

** Note**\
Other [fsck.\*] tools may be provided by [[[sys-fs/e2fsprogs]](https://packages.gentoo.org/packages/sys-fs/e2fsprogs)[]] (ext4), or [[[sys-fs/dosfstools]](https://packages.gentoo.org/packages/sys-fs/dosfstools)[]] (fat), or other user space \"helper\" packages.

`user `[`$`]`fsck --help`

    Usage:
     fsck [options] -- [fs-options] [<filesystem> ...]

    Check and repair a Linux filesystem.

    Options:
     -A         check all filesystems
     -C [<fd>]  display progress bar; file descriptor is for GUIs
     -l         lock the device to guarantee exclusive access
     -M         do not check mounted filesystems
     -N         do not execute, just show what would be done
     -P         check filesystems in parallel, including root
     -R         skip root filesystem; useful only with '-A'
     -r [<fd>]  report statistics for each device checked;
                file descriptor is for GUIs
     -s         serialize the checking operations
     -T         do not show the title on startup
     -t <type>  specify filesystem types to be checked;
                <type> is allowed to be a comma-separated list
     -V         explain what is being done

     -?, --help     display this help
         --version  display version

    See the specific fsck.* commands for available fs-options.
    For more details see fsck(8).

### [fsck.cramfs]

Check and repair a compressed ROM filesystem.

Command only available if the [[[cramfs]](https://packages.gentoo.org/useflags/cramfs)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set.

** Note**\
Other [fsck.\*] tools may be provided by [[[sys-fs/e2fsprogs]](https://packages.gentoo.org/packages/sys-fs/e2fsprogs)[]], or [[[sys-fs/dosfstools]](https://packages.gentoo.org/packages/sys-fs/dosfstools)[]], or other packages.

`user `[`$`]`fsck.cramfs --help`

    Usage:
     fsck.cramfs [options] <file>

    Check and repair a compressed ROM filesystem.

    Options:
     -a                       for compatibility only, ignored
     -v, --verbose            be more verbose
     -y                       for compatibility only, ignored
     -b, --blocksize <size>   use this blocksize, defaults to page size
         --extract[=<dir>]    test uncompression, optionally extract into <dir>

     -h, --help               display this help
     -V, --version            display version

    For more details see fsck.cramfs(8).

### [fsck.minix]

Check the consistency of a Minix filesystem.

** Note**\
Other [fsck.\*] tools may be provided by [[[sys-fs/e2fsprogs]](https://packages.gentoo.org/packages/sys-fs/e2fsprogs)[]], or [[[sys-fs/dosfstools]](https://packages.gentoo.org/packages/sys-fs/dosfstools)[]], or other packages.

`user `[`$`]`fsck.minix --help`

    Usage:
     fsck.minix [options] <device>

    Check the consistency of a Minix filesystem.

    Options:
     -l, --list       list all filenames
     -a, --auto       automatic repair
     -r, --repair     interactive repair
     -v, --verbose    be verbose
     -s, --super      output super-block information
     -m, --uncleared  activate mode not cleared warnings
     -f, --force      force check

     -h, --help       display this help
     -V, --version    display version

    For more details see fsck.minix(8).

### [fsfreeze]

Suspend access to a filesystem.

`user `[`$`]`fsfreeze --help`

    Usage:
     fsfreeze [options] <mountpoint>

    Suspend access to a filesystem.

    Options:
     -f, --freeze      freeze the filesystem
     -u, --unfreeze    unfreeze the filesystem

     -h, --help        display this help
     -V, --version     display version

    For more details see fsfreeze(8).

### [fstrim]

Discard/trim unused blocks on a filesystem - useful for solid-state drives.

`user `[`$`]`fstrim --help`

    Usage:
     fstrim [options] <mount point>

    Discard unused blocks on a mounted filesystem.

    Options:
     -a, --all                trim mounted filesystems
     -A, --fstab              trim filesystems from /etc/fstab
     -I, --listed-in <list>   trim filesystems listed in specified files
     -o, --offset <num>       the offset in bytes to start discarding from
     -l, --length <num>       the number of bytes to discard
     -m, --minimum <num>      the minimum extent length to discard
     -v, --verbose            print number of discarded bytes
         --quiet-unsupported  suppress error messages if trim unsupported
     -n, --dry-run            does everything, but trim

     -h, --help          display this help
     -V, --version       display version

    Arguments:
     <num> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

    For more details see fstrim(8).

### [getopt]

Parse command options.

`user `[`$`]`getopt --help`

     getopt <optstring>
     getopt [options] [--] <optstring>
     getopt [options] -o|--options <optstring> [options] [--]

    Parse command options.

    Options:
     -a, --alternative             allow long options starting with single -
     -l, --longoptions <longopts>  the long options to be recognized
     -n, --name          the name under which errors are reported
     -o, --options <optstring>     the short options to be recognized
     -q, --quiet                   disable error reporting by getopt(3)
     -Q, --quiet-output            no normal output
     -s, --shell <shell>           set quoting conventions to those of <shell>
     -T, --test                    test for getopt(1) version
     -u, --unquoted                do not quote the output

     -h, --help                    display this help
     -V, --version                 display version

    For more details see getopt(1).

### [hardlink]

Consolidate duplicate files using hardlinks.

Command only available if the [[[hardlink]](https://packages.gentoo.org/useflags/hardlink)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set.

`user `[`$`]`hardlink --help`

    Usage:
     hardlink [options] <directory>|<file> ...

    Consolidate duplicate files using hardlinks.

    Options:
     -v, --verbose              verbose output (repeat for more verbosity)
     -q, --quiet                quiet mode - don't print anything
     -n, --dry-run              don't actually link anything
     -y, --method <name>        file content comparison method
     -f, --respect-name         filenames have to be identical
     -p, --ignore-mode          ignore changes of file mode
     -o, --ignore-owner         ignore owner changes
     -t, --ignore-time          ignore timestamps (when testing for equality)
     -c, --content              compare only file contents, same as -pot
     -X, --respect-xattrs       respect extended attributes
         --reflink[=<when>]     create clone/CoW copies (auto, always, never)
         --skip-reflinks        skip already cloned files (enabled on --reflink)
     -m, --maximize             maximize the hardlink count, remove the file with
                                  lowest hardlink count
     -M, --minimize             reverse the meaning of -m
     -O, --keep-oldest          keep the oldest file of multiple equal files
                                  (lower precedence than minimize/maximize)
     -x, --exclude <regex>      regular expression to exclude files
     -i, --include <regex>      regular expression to include files/dirs
     -s, --minimum-size <size>  minimum size for files.
     -S, --maximum-size <size>  maximum size for files.
     -b, --io-size <size>       I/O buffer size for file reading (speedup, using more RAM)
     -r, --cache-size <size>    memory limit for cached file content data

     -h, --help                 display this help
     -V, --version              display version

    For more details see hardlink(1).

### [hexdump]

Display file contents in hexadecimal, decimal, octal, or ascii. See also [hex editor](https://wiki.gentoo.org/wiki/Hex_editor "Hex editor").

`user `[`$`]`hexdump --help`

    Usage:
     hexdump [options] <file>...

    Display file contents in hexadecimal, decimal, octal, or ascii.

    Options:
     -b, --one-byte-octal      one-byte octal display
     -c, --one-byte-char       one-byte character display
     -C, --canonical           canonical hex+ASCII display
     -d, --two-bytes-decimal   two-byte decimal display
     -o, --two-bytes-octal     two-byte octal display
     -x, --two-bytes-hex       two-byte hexadecimal display
     -L, --color[=<mode>]      interpret color formatting specifiers
                                 colors are enabled by default
     -e, --format <format>     format string to be used for displaying data
     -f, --format-file <file>  file that contains format strings
     -n, --length <length>     interpret only length bytes of input
     -s, --skip <offset>       skip offset bytes from the beginning
     -v, --no-squeezing        output identical lines

     -h, --help                display this help
     -V, --version             display version

    Arguments:
     <length> and <offset> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

    For more details see hexdump(1).

### [hwclock]

Time clocks utility.

`user `[`$`]`hwclock --help`

    Usage:
     hwclock [function] [option...]

    Time clocks utility.

    Functions:
     -r, --show                      display the RTC time
         --get                       display drift corrected RTC time
         --set                       set the RTC according to --date
     -s, --hctosys                   set the system time from the RTC
     -w, --systohc                   set the RTC from the system time
         --systz                     send timescale configurations to the kernel
     -a, --adjust                    adjust the RTC to account for systematic drift
         --param-get          display the RTC parameter
         --param-set =<value> set the RTC parameter
         --predict                   predict the drifted RTC time according to --date

    Options:
     -u, --utc                       the RTC timescale is UTC
     -l, --localtime                 the RTC timescale is Local
     -f, --rtc <file>                use an alternate file to /dev/rtc0
         --directisa                 use the ISA bus instead of /dev/rtc0 access
         --date <time>               date/time input for --set and --predict
         --delay <sec>               delay used when set new RTC time
         --update-drift              update the RTC drift factor
         --noadjfile                 do not use /etc/adjtime
         --adjfile <file>            use an alternate file to /etc/adjtime
         --test                      dry run; implies --verbose
     -v, --verbose                   display more details

     -h, --help                      display this help
     -V, --version                   display version

    Arguments:
      is either a numeric RTC parameter value or one of these aliases:
       - features: supported features (0x0)
       - correction: time correction (0x1)
       - bsm: backup switch mode (0x2)
       See Kernel's include/uapi/linux/rtc.h for parameters and values.

      and <value> accept hexadecimal values if prefixed with 0x, otherwise decimal.

    For more details see hwclock(8).

### [ionice]

Show or change the I/O-scheduling class and priority of a process.

`user `[`$`]`ionice --help`

    Usage:
     ionice [options] -p ...
     ionice [options] -P ...
     ionice [options] -u <uid>...
     ionice [options] <command>

    Show or change the I/O-scheduling class and priority of a process.

    Options:
     -c, --class <class>    name or number of scheduling class,
                              0: none, 1: realtime, 2: best-effort, 3: idle
     -n, --classdata <num>  priority (0..7) in the specified scheduling class,
                              only for the realtime and best-effort classes
     -p, --pid ...     act on these already running processes
     -P, --pgid ...   act on already running processes in these groups
     -t, --ignore           ignore failures
     -u, --uid <uid>...     act on already running processes owned by these users

     -h, --help             display this help
     -V, --version          display version

    For more details see ionice(1).

### [ipcmk]

Create various IPC resources.

`user `[`$`]`ipcmk --help`

    Usage:
     ipcmk [options]

    Create various IPC resources.

    Options:
     -M, --shmem <size>       create shared memory segment of size <size>
     -S, --semaphore <number> create semaphore array with <number> elements
     -Q, --queue              create message queue
     -p, --mode <mode>        permission for the resource (default is 0644)

     -h, --help               display this help
     -V, --version            display version

    Arguments:
     <size> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

    For more details see ipcmk(1).

### [ipcrm]

Remove certain IPC resources.

`user `[`$`]`ipcrm --help`

    Usage:
     ipcrm [options]
     ipcrm shm|msg|sem <id>...

    Remove certain IPC resources.

    Options:
     -m, --shmem-id <id>        remove shared memory segment by id
     -M, --shmem-key <key>      remove shared memory segment by key
     -q, --queue-id <id>        remove message queue by id
     -Q, --queue-key <key>      remove message queue by key
     -s, --semaphore-id <id>    remove semaphore by id
     -S, --semaphore-key <key>  remove semaphore by key
     -a, --all[=shm|msg|sem]    remove all (in the specified category)
     -v, --verbose              explain what is being done

     -h, --help                 display this help
     -V, --version              display version

    For more details see ipcrm(1).

### [ipcs]

Show information on IPC facilities.

`user `[`$`]`ipcs --help`

    Usage:
     ipcs [resource-option...] [output-option]
     ipcs -m|-q|-s -i <id>

    Show information on IPC facilities.

    Options:
     -i, --id <id>  print details on resource identified by <id>
     -h, --help     display this help
     -V, --version  display version

    Resource options:
     -m, --shmems      shared memory segments
     -q, --queues      message queues
     -s, --semaphores  semaphores
     -a, --all         all (default)

    Output options:
     -t, --time        show attach, detach and change times
     -p, --pid         show PIDs of creator and last operator
     -c, --creator     show creator and owner
     -l, --limits      show resource limits
     -u, --summary     show status summary
         --human       show sizes in human-readable format
     -b, --bytes       show sizes in bytes

    For more details see ipcs(1).

### [irqtop]

Interactive utility to display kernel interrupt information.

`user `[`$`]`irqtop --help`

    Usage:
     irqtop [options]

    Interactive utility to display kernel interrupt information.

    Options:
     -c, --cpu-stat <mode> show per-cpu stat (auto, enable, disable)
     -d, --delay <secs>   delay updates
     -o, --output <list>  define which output columns to use
     -s, --sort <column>  specify sort column
     -S, --softirq        show softirqs instead of interrupts

     -h, --help           display this help
     -V, --version        display version

    The following interactive key commands are valid:
      i      sort by IRQ
      t      sort by TOTAL
      d      sort by DELTA
      n      sort by NAME
      q Q    quit program

    Available output columns:
      IRQ    interrupts
      TOTAL  total count
      DELTA  delta count
      NAME   name

    For more details see irqtop(1).

### [isosize]

Show the length of an ISO-9660 filesystem.

`user `[`$`]`isosize --help`

    Usage:
     isosize [options] <iso9660_image_file> ...

    Show the length of an ISO-9660 filesystem.

    Options:
     -d, --divisor=<number>  divide the amount of bytes by <number>
     -x, --sectors           show sector count and size
     -h, --help              display this help
     -V, --version           display version

    For more details see isosize(8).

### [kill]

Send a signal to a process.

Command only available if the [[[kill]](https://packages.gentoo.org/useflags/kill)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set. See [section](#kill) at top of article.

### [last]

Show a listing of last logged in users.

`user `[`$`]`last --help`

    Usage:
     last [options] [<username>...] [<tty>...]

    Show a listing of last logged in users.

    Options:
     -<number>            how many lines to show
     -a, --hostlast       display hostnames in the last column
     -d, --dns            translate the IP number back into a hostname
     -f, --file <file>    use a specific file instead of /var/log/wtmp
     -F, --fulltimes      print full login and logout times and dates
     -i, --ip             display IP numbers in numbers-and-dots notation
     -n, --limit <number> how many lines to show
     -R, --nohostname     don't display the hostname field
     -s, --since <time>   display the lines since the specified time
     -t, --until <time>   display the lines until the specified time
     -p, --present <time> display who were present at the specified time
     -w, --fullnames      display full user and domain names
     -x, --system         display system shutdown entries and run level changes
         --time-format <format>  show timestamps in the specified <format>:
                                   notime|short|full|iso

     -h, --help           display this help
     -V, --version        display version

    For more details see last(1).

### [ldattach]

Attach a line discipline to a serial line.

`user `[`$`]`ldattach --help`

    Usage:
     ldattach [options] <ldisc> <device>

    Attach a line discipline to a serial line.

    Options:
     -d, --debug             print verbose messages to stderr
     -s, --speed <value>     set serial line speed
     -c, --intro-command <string> intro sent before ldattach
     -p, --pause <seconds>   pause between intro and ldattach
     -7, --sevenbits         set character size to 7 bits
     -8, --eightbits         set character size to 8 bits
     -n, --noparity          set parity to none
     -e, --evenparity        set parity to even
     -o, --oddparity         set parity to odd
     -1, --onestopbit        set stop bits to one
     -2, --twostopbits       set stop bits to two
     -i, --iflag [-]<iflag>  set input mode flag

     -h, --help              display this help
     -V, --version           display version

    Known <ldisc> names:
      TTY           SLIP          MOUSE         PPP           STRIP
      AX25          X25           6PACK         R3964         IRDA
      HDLC          SYNC_PPP      SYNCPPP       HCI           GIGASET_M101
      M101          GIGASET       PPS           GSM0710

    Known <iflag> names:
      IGNBRK        BRKINT        IGNPAR        PARMRK        INPCK
      ISTRIP        INLCR         IGNCR         ICRNL         IUCLC
      IXON          IXANY         IXOFF         IMAXBEL       IUTF8

    For more details see ldattach(8).

### [line]

Read one line.

`user `[`$`]`line --help`

    Usage:
     line [options]

    Read one line.

    Options:
     -h, --help     display this help
     -V, --version  display version

    For more details see line(1).

### [logger]

Enter messages into the system log.

Command only available if the [[[logger]](https://packages.gentoo.org/useflags/logger)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set.

`user `[`$`]`logger --help`

    Usage:
     logger [options] [<message>]

    Enter messages into the [[system log]].

    Options:
     -i                       log the logger command's PID
         --id[=<id>]          log the given <id>, or otherwise the PID
     -f, --file <file>        log the contents of this file
     -e, --skip-empty         do not log empty lines when processing files
         --no-act             do everything except the write the log
     -p, --priority     mark given message with this priority
         --octet-count        use rfc6587 octet counting
         --prio-prefix        look for a prefix on every line read from stdin
     -s, --stderr             output message to standard error as well
     -S, --size <size>        maximum size for a single message
     -t, --tag <tag>          mark every line with this tag
     -n, --server <name>      write to this remote syslog server
     -P, --port         use this port for UDP or TCP connection
     -T, --tcp                use TCP only
     -d, --udp                use UDP only
         --rfc3164            use the obsolete BSD syslog protocol
         --rfc5424[=<snip>]   use the syslog protocol (the default for remote);
                                <snip> can be notime, or notq, and/or nohost
         --sd-id <id>         rfc5424 structured data ID
         --sd-param <data>    rfc5424 structured data name=value
         --msgid <msgid>      set rfc5424 message id field
     -u, --socket <socket>    write to this Unix socket
         --socket-errors[=<on|off|auto>]
                              print connection errors when using Unix sockets

     -h, --help               display this help
     -V, --version            display version

    For more details see logger(1).

### [login]

May belong to [[[sys-apps/shadow]](https://packages.gentoo.org/packages/sys-apps/shadow)[]]. Begin session on the system. See man login, and [login](https://wiki.gentoo.org/wiki/Login "Login").

### [look]

Display lines beginning with a specified string.

`user `[`$`]`look --help`

    Usage:
     look [options] <string> [<file>...]

    Display lines beginning with a specified string.

    Options:
     -a, --alternative        use the alternative dictionary
     -d, --alphanum           compare only blanks and alphanumeric characters
     -f, --ignore-case        ignore case differences when comparing
     -t, --terminate <char>   define the string-termination character

     -h, --help               display this help
     -V, --version            display version

    For more details see look(1).

### [losetup]

Control loop devices.

`user `[`$`]`losetup --help`

    Usage:
     losetup [options] [<loopdev>]
     losetup [options] -f | <loopdev> <file>

    Set up and control loop devices.

    Options:
     -a, --all                     list all used devices
     -d, --detach <loopdev>...     detach one or more devices
     -D, --detach-all              detach all used devices
     -f, --find                    find first unused device
     -c, --set-capacity <loopdev>  resize the device
     -j, --associated <file>       list all devices associated with <file>
     -L, --nooverlap               avoid possible conflict between devices

     -o, --offset <num>            start at offset <num> into file
         --sizelimit <num>         device is limited to <num> bytes of the file
     -b, --sector-size <num>       set the logical sector size to <num>
     -P, --partscan                create a partitioned loop device
     -r, --read-only               set up a read-only loop device
         --direct-io[=<on|off>]    open backing file with O_DIRECT
         --show                    print device name after setup (with -f)
     -v, --verbose                 verbose mode

     -J, --json                    use JSON --list output format
     -l, --list                    list info about all or specified (default)
     -n, --noheadings              don't print headings for --list output
     -O, --output <cols>           specify columns to output for --list
         --output-all              output all columns
         --raw                     use raw --list output format

     -h, --help                    display this help
     -V, --version                 display version

    Available output columns:
             NAME  loop device name
        AUTOCLEAR  autoclear flag set
        BACK-FILE  device backing file
         BACK-INO  backing file inode number
     BACK-MAJ:MIN  backing file major:minor device number
          MAJ:MIN  loop device major:minor number
           OFFSET  offset from the beginning
         PARTSCAN  partscan flag set
               RO  read-only device
        SIZELIMIT  size limit of the file in bytes
              DIO  access backing file with direct-io
          LOG-SEC  logical sector size in bytes

    For more details see losetup(8).

### [lsblk]

List information about block devices.

`user `[`$`]`lsblk --help`

    Usage:
     lsblk [options] [<device> ...]

    List information about block devices.

    Options:
     -A, --noempty        don't print empty devices
     -D, --discard        print discard capabilities
     -E, --dedup <column> de-duplicate output by <column>
     -I, --include <list> show only devices with specified major numbers
     -J, --json           use JSON output format
     -M, --merge          group parents of sub-trees (usable for RAIDs, Multi-path)
     -O, --output-all     output all columns
     -P, --pairs          use key="value" output format
     -S, --scsi           output info about SCSI devices
     -T, --tree[=<column>] use tree format output
     -a, --all            print all devices
     -b, --bytes          print SIZE in bytes rather than in human readable format
     -d, --nodeps         don't print slaves or holders
     -e, --exclude <list> exclude devices by major number (default: RAM disks)
     -f, --fs             output info about filesystems
     -i, --ascii          use ascii characters only
     -l, --list           use list format output
     -m, --perms          output info about permissions
     -n, --noheadings     don't print headings
     -o, --output <list>  output columns
     -p, --paths          print complete device path
     -r, --raw            use raw output format
     -s, --inverse        inverse dependencies
     -t, --topology       output info about topology
     -w, --width <num>    specifies output width as number of characters
     -x, --sort <column>  sort output by <column>
     -y, --shell          use column names to be usable as shell variable identifiers
     -z, --zoned          print zone related information
         --sysroot <dir>  use specified directory as system root

     -h, --help           display this help
     -V, --version        display version

    Available output columns:
        ALIGNMENT  alignment offset
         DISC-ALN  discard alignment offset
              DAX  dax-capable device
        DISC-GRAN  discard granularity
         DISC-MAX  discard max bytes
        DISC-ZERO  discard zeroes data
          FSAVAIL  filesystem size available
          FSROOTS  mounted filesystem roots
           FSSIZE  filesystem size
           FSTYPE  filesystem type
           FSUSED  filesystem size used
           FSUSE%  filesystem use percentage
            FSVER  filesystem version
            GROUP  group name
             HCTL  Host:Channel:Target:Lun for SCSI
          HOTPLUG  removable or hotplug device (usb, pcmcia, ...)
            KNAME  internal kernel device name
            LABEL  filesystem LABEL
          LOG-SEC  logical sector size
          MAJ:MIN  major:minor device number
           MIN-IO  minimum I/O size
             MODE  device node permissions
            MODEL  device identifier
             NAME  device name
           OPT-IO  optimal I/O size
            OWNER  user name
        PARTFLAGS  partition flags
        PARTLABEL  partition LABEL
         PARTTYPE  partition type code or UUID
     PARTTYPENAME  partition type name
         PARTUUID  partition UUID
             PATH  path to the device node
          PHY-SEC  physical sector size
           PKNAME  internal parent kernel device name
           PTTYPE  partition table type
           PTUUID  partition table identifier (usually UUID)
               RA  read-ahead of the device
             RAND  adds randomness
              REV  device revision
               RM  removable device
               RO  read-only device
             ROTA  rotational device
          RQ-SIZE  request queue size
            SCHED  I/O scheduler name
           SERIAL  disk serial number
             SIZE  size of the device
            START  partition start offset
            STATE  state of the device
       SUBSYSTEMS  de-duplicated chain of subsystems
       MOUNTPOINT  where the device is mounted
      MOUNTPOINTS  all locations where device is mounted
             TRAN  device transport type
             TYPE  device type
             UUID  filesystem UUID
           VENDOR  device vendor
            WSAME  write same max bytes
              WWN  unique storage identifier
            ZONED  zone model
          ZONE-SZ  zone size
       ZONE-WGRAN  zone write granularity
         ZONE-APP  zone append max bytes
          ZONE-NR  number of zones
        ZONE-OMAX  maximum number of open zones
        ZONE-AMAX  maximum number of active zones

    For more details see lsblk(8).

### [lscpu]

Display information about the CPU architecture. See also [hardware detection](https://wiki.gentoo.org/wiki/Hardware_detection "Hardware detection").

`user `[`$`]`lscpu --help`

    Usage:
     lscpu [options]

    Display information about the CPU architecture.

    Options:
     -a, --all               print both online and offline CPUs (default for -e)
     -b, --online            print online CPUs only (default for -p)
     -B, --bytes             print sizes in bytes rather than in human readable format
     -C, --caches[=<list>]   info about caches in extended readable format
     -c, --offline           print offline CPUs only
     -J, --json              use JSON for default or extended format
     -e, --extended[=<list>] print out an extended readable format
     -p, --parse[=<list>]    print out a parsable format
     -s, --sysroot <dir>     use specified directory as system root
     -x, --hex               print hexadecimal masks rather than lists of CPUs
     -y, --physical          print physical instead of logical IDs
         --output-all        print all available columns for -e, -p or -C

     -h, --help              display this help
     -V, --version           display version

    Available output columns for -e or -p:
          BOGOMIPS  crude measurement of CPU speed
               CPU  logical CPU number
              CORE  logical core number
            SOCKET  logical socket number
           CLUSTER  logical cluster number
              NODE  logical NUMA node number
              BOOK  logical book number
            DRAWER  logical drawer number
             CACHE  shows how caches are shared between CPUs
      POLARIZATION  CPU dispatching mode on virtual hardware
           ADDRESS  physical address of a CPU
        CONFIGURED  shows if the hypervisor has allocated the CPU
            ONLINE  shows if Linux currently makes use of the CPU
               MHZ  shows the currently MHz of the CPU
            MAXMHZ  shows the maximum MHz of the CPU
            MINMHZ  shows the minimum MHz of the CPU

    Available output columns for -C:
          ALL-SIZE  size of all system caches
             LEVEL  cache level
              NAME  cache name
          ONE-SIZE  size of one cache
              TYPE  cache type
              WAYS  ways of associativity
      ALLOC-POLICY  allocation policy
      WRITE-POLICY  write policy
          PHY-LINE  number of physical cache line per cache t
              SETS  number of sets in the cache; set lines has the same cache index
     COHERENCY-SIZE  minimum amount of data in bytes transferred from memory to cache

    For more details see lscpu(1).

### [lsfd]

List file descriptors. See [changelog](https://github.com/util-linux/util-linux/blob/master/Documentation/releases/v2.38-ReleaseNotes) on introduction of this command.

`user `[`$`]`lsfd --help`

    Usage:
     lsfd [options]

    Options:
     -l, --threads         list in threads level
     -J, --json            use JSON output format
     -n, --noheadings      don't print headings
     -o, --output <list>   output columns
     -r, --raw             use raw output format
     -u, --notruncate      don't truncate text in columns
     -p, --pid     collect information only specified processes
     -Q, --filter <expr>   apply display filter
         --debug-filter    dump the internal data structure of filter and exit
     -C, --counter <name>:<expr>
                           define custom counter for --summary output
         --dump-counters   dump counter definitions
         --summary[=when]  print summary information (only, append, or never)

     -h, --help            display this help
     -V, --version         display version

    Available output columns:
           ASSOC  <string>  association between file and process
          BLKDRV  <string>  block device driver name resolved by /proc/devices
          CHRDRV  <string>  character device driver name resolved by /proc/devices
         COMMAND  <string>  command of the process opening the file
         DELETED  <boolean> reachability from the file system
             DEV  <string>  ID of device containing file
         DEVTYPE  <string>  device type (blk, char, or nodev)
              FD  <number>  file descriptor for the file
           FLAGS  <string>  flags specified when opening the file
           INODE  <number>  inode number
         KTHREAD  <boolean> opened by a kernel thread
         MAJ:MIN  <string>  device ID for special, or ID of device containing file
          MAPLEN  <number>  length of file mapping (in page)
         MISCDEV  <string>  misc character device name resolved by /proc/misc
           MNTID  <number>  mount id
            MODE  <string>  access mode (rwx)
            NAME  <string>  name of the file
           NLINK  <number>  link count
       PARTITION  <string>  block device name resolved by /proc/partition
             PID  <number>  PID of the process opening the file
             POS  <number>  file position
       PROTONAME  <string>  protocol name
            RDEV  <string>  device ID (if special file)
            SIZE  <number>  file size
          SOURCE  <string>  file system, partition, or device containing file
             TID  <number>  thread ID of the process opening the file
            TYPE  <string>  file type
             UID  <number>  user ID number of the process
            USER  <string>  user of the process
            FUID  <number>  user ID number of the file's owner
           OWNER  <string>  owner of the file

    For more details see lsfd(1).

### [lsipc]

List System V inter-process communication (IPC) resources.

`user `[`$`]`lsipc --help`

    Usage:
     lsipc [options]

    Show information on IPC facilities.

    Resource options:
     -m, --shmems      shared memory segments
     -q, --queues      message queues
     -s, --semaphores  semaphores
     -g, --global      info about system-wide usage (may be used with -m, -q and -s)
     -i, --id <id>     print details on resource identified by <id>

    Options:
         --noheadings         don't print headings
         --notruncate         don't truncate output
         --time-format=<type> display dates in short, full or iso format
     -b, --bytes              print SIZE in bytes rather than in human readable format
     -c, --creator            show creator and owner
     -e, --export             display in an export-able output format
     -J, --json               use the JSON output format
     -n, --newline            display each piece of information on a new line
     -l, --list               force list output format (for example with --id)
     -o, --output[=<list>]    define the columns to output
     -P, --numeric-perms      print numeric permissions (PERMS column)
     -r, --raw                display in raw mode
     -t, --time               show attach, detach and change times

     -h, --help               display this help
     -V, --version            display version

    Generic columns:
                KEY  Resource key
                 ID  Resource ID
              OWNER  Owner's username or UID
              PERMS  Permissions
               CUID  Creator UID
              CUSER  Creator user
               CGID  Creator GID
             CGROUP  Creator group
                UID  User ID
               USER  User name
                GID  Group ID
              GROUP  Group name
              CTIME  Time of the last change

    Shared-memory columns (--shmems):
               SIZE  Segment size
             NATTCH  Number of attached processes
             STATUS  Status
             ATTACH  Attach time
             DETACH  Detach time
            COMMAND  Creator command line
               CPID  PID of the creator
               LPID  PID of last user

    Message-queue columns (--queues):
          USEDBYTES  Bytes used
               MSGS  Number of messages
               SEND  Time of last msg sent
               RECV  Time of last msg received
              LSPID  PID of the last msg sender
              LRPID  PID of the last msg receiver

    Semaphore columns (--semaphores):
              NSEMS  Number of semaphores
              OTIME  Time of the last operation

    Summary columns (--global):
           RESOURCE  Resource name
        DESCRIPTION  Resource description
              LIMIT  System-wide limit
               USED  Currently used
               USE%  Currently use percentage

    For more details see lsipc(1).

### [lsirq]

Utility to display kernel interrupt information.

`user `[`$`]`lsirq --help`

    Usage:
     lsirq [options]

    Utility to display kernel interrupt information.

    Options:
     -J, --json           use JSON output format
     -P, --pairs          use key="value" output format
     -n, --noheadings     don't print headings
     -o, --output <list>  define which output columns to use
     -s, --sort <column>  specify sort column
     -S, --softirq        show softirqs instead of interrupts

     -h, --help           display this help
     -V, --version        display version

    Available output columns:
      IRQ    interrupts
      TOTAL  total count
      NAME   name

    For more details see lsirq(1).

### [lslocks]

List local system locks.

`user `[`$`]`lslocks --help`

    Usage:
     lslocks [options]

    List local system locks.

    Options:
     -b, --bytes            print SIZE in bytes rather than in human readable format
     -J, --json             use JSON output format
     -i, --noinaccessible   ignore locks without read permissions
     -n, --noheadings       don't print headings
     -o, --output <list>    define which output columns to use
         --output-all       output all columns
     -p, --pid         display only locks held by this process
     -r, --raw              use the raw output format
     -u, --notruncate       don't truncate text in columns

     -h, --help             display this help
     -V, --version          display version

    Available output columns:
         COMMAND  command of the process holding the lock
             PID  PID of the process holding the lock
            TYPE  kind of lock
            SIZE  size of the lock
            MODE  lock access mode
               M  mandatory state of the lock: 0 (none), 1 (set)
           START  relative byte offset of the lock
             END  ending offset of the lock
            PATH  path of the locked file
         BLOCKER  PID of the process blocking the lock

    For more details see lslocks(8).

### [lslogins]

Display information about known users in the system.

`user `[`$`]`lslogins --help`

    Usage:
     lslogins [options] [<username>]

    Display information about known users in the system.

    Options:
     -a, --acc-expiration     display info about passwords expiration
     -c, --colon-separate     display data in a format similar to /etc/passwd
     -e, --export             display in an export-able output format
     -f, --failed             display data about the users' last failed logins
     -G, --supp-groups        display information about groups
     -g, --groups=<groups>    display users belonging to a group in <groups>
     -L, --last               show info about the users' last login sessions
     -l, --logins=<logins>    display only users from <logins>
     -n, --newline            display each piece of information on a new line
         --noheadings         don't print headings
         --notruncate         don't truncate output
     -o, --output[=<list>]    define the columns to output
         --output-all         output all columns
     -p, --pwd                display information related to login by password.
     -r, --raw                display in raw mode
     -s, --system-accs        display system accounts
         --time-format=<type> display dates in short, full or iso format
     -u, --user-accs          display user accounts
     -Z, --context            display SELinux contexts
     -z, --print0             delimit user entries with a nul character
         --wtmp-file    set an alternate path for wtmp
         --btmp-file    set an alternate path for btmp
         --lastlog      set an alternate path for lastlog

     -h, --help               display this help
     -V, --version            display version

    Available output columns:
               USER  user name
                UID  user ID
              GECOS  full user name
            HOMEDIR  home directory
              SHELL  login shell
            NOLOGIN  log in disabled by nologin(8) or pam_nologin(8)
           PWD-LOCK  password defined, but locked
          PWD-EMPTY  password not required
           PWD-DENY  login by password disabled
         PWD-METHOD  password encryption method
              GROUP  primary group name
                GID  primary group ID
        SUPP-GROUPS  supplementary group names
          SUPP-GIDS  supplementary group IDs
         LAST-LOGIN  date of last login
           LAST-TTY  last tty used
      LAST-HOSTNAME  hostname during the last session
       FAILED-LOGIN  date of last failed login
         FAILED-TTY  where did the login fail?
             HUSHED  user's hush settings
           PWD-WARN  days user is warned of password expiration
         PWD-CHANGE  date of last password change
            PWD-MIN  number of days required between changes
            PWD-MAX  max number of days a password may remain unchanged
          PWD-EXPIR  password expiration date
            CONTEXT  the user's security context
               PROC  number of processes run by the user

    For more details see lslogins(1).

### [lsmem]

List the ranges of available memory with their online status.

`user `[`$`]`lsmem --help`

    Usage:
     lsmem [options]

    List the ranges of available memory with their online status.

    Options:
     -J, --json           use JSON output format
     -P, --pairs          use key="value" output format
     -a, --all            list each individual memory block
     -b, --bytes          print SIZE in bytes rather than in human readable format
     -n, --noheadings     don't print headings
     -o, --output <list>  output columns
         --output-all     output all columns
     -r, --raw            use raw output format
     -S, --split <list>   split ranges by specified columns
     -s, --sysroot <dir>  use the specified directory as system root
         --summary[=when] print summary information (never,always or only)

     -h, --help           display this help
     -V, --version        display version

    Available output columns:
          RANGE  start and end address of the memory range
           SIZE  size of the memory range
          STATE  online status of the memory range
      REMOVABLE  memory is removable
          BLOCK  memory block number or blocks range
           NODE  numa node of memory
          ZONES  valid zones for the memory range

    For more details see lsmem(1).

### [lsns]

List system namespaces.

`user `[`$`]`lsns --help`

    Usage:
     lsns [options] [<namespace>]

    List system namespaces.

    Options:
     -J, --json             use JSON output format
     -l, --list             use list format output
     -n, --noheadings       don't print headings
     -o, --output <list>    define which output columns to use
         --output-all       output all columns
     -p, --task        print process namespaces
     -r, --raw              use the raw output format
     -u, --notruncate       don't truncate text in columns
     -W, --nowrap           don't use multi-line representation
     -t, --type <name>      namespace type (mnt, net, ipc, user, pid, uts, cgroup, time)

     -h, --help             display this help
     -V, --version          display version

    Available output columns:
              NS  namespace identifier (inode number)
            TYPE  kind of namespace
            PATH  path to the namespace
          NPROCS  number of processes in the namespace
             PID  lowest PID in the namespace
            PPID  PPID of the PID
         COMMAND  command line of the PID
             UID  UID of the PID
            USER  username of the PID
         NETNSID  namespace ID as used by network subsystem
            NSFS  nsfs mountpoint (usually used network subsystem)
             PNS  parent namespace identifier (inode number)
             ONS  owner namespace identifier (inode number)

    For more details see lsns(8).

### [mcookie]

Generate magic cookies for xauth.

`user `[`$`]`mcookie --help`

    Usage:
     mcookie [options]

    Generate magic cookies for xauth.

    Options:
     -f, --file <file>     use file as a cookie seed
     -m, --max-size <num>  limit how much is read from seed files
     -v, --verbose         explain what is being done

     -h, --help            display this help
     -V, --version         display version

    Arguments:
     <num> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

    For more details see mcookie(1).

### [mesg]

Display (or do not display) messages from other users.

Command only available if the [[[tty-helpers]](https://packages.gentoo.org/useflags/tty-helpers)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set.

### [mkfs]

Make a Linux filesystem.

`user `[`$`]`mkfs --help`

    Usage:
     mkfs [options] [-t <type>] [fs-options] <device> [<size>]

    Make a Linux filesystem.

    Options:
     -t, --type=<type>  filesystem type; when unspecified, ext2 is used
         fs-options     parameters for the real filesystem builder
         <device>       path to the device to be used
         <size>         number of blocks to be used on the device
     -V, --verbose      explain what is being done;
                          specifying -V more than once will cause a dry-run
     -h, --help         display this help
     -V, --version      display version

    For more details see mkfs(8).

### [mkfs.bfs]

Make an SCO bfs filesystem.

`user `[`$`]`mkfs.bfs --help`

    Usage: mkfs.bfs [options] device [block-count]

    Make an SCO bfs filesystem.

    Options:
     -N, --inodes=NUM    specify desired number of inodes
     -V, --vname=NAME    specify volume name
     -F, --fname=NAME    specify file system name
     -v, --verbose       explain what is being done
     -c                  this option is silently ignored
     -l                  this option is silently ignored
     -h, --help          display this help
     -V, --version       display version

    For more details see mkfs.bfs(8).

### [mkfs.cramfs]

Make [cramfs](https://wiki.gentoo.org/wiki/Cramfs "Cramfs") compressed ROM file system.

`user `[`$`]`mkfs.cramfs --help`

    Usage:
     mkfs.cramfs [-h] [-v] [-b blksize] [-e edition] [-N endian] [-i file] [-n name] dirname outfile

    Make compressed ROM file system.

    Options:
     -v             be verbose
     -E             make all warnings errors (non-zero exit status)
     -b blksize     use this blocksize, must equal page size
     -e edition     set edition number (part of fsid)
     -N endian      set cramfs endianness (big|little|host), default host
     -i file        insert a file image into the filesystem
     -n name        set name of cramfs filesystem
     -p             pad by 512 bytes for boot code
     -s             sort directory entries (old option, ignored)
     -z             make explicit holes
     dirname        root of the filesystem to be compressed
     outfile        output file

     -h, --help     display this help
     -V, --version  display version

    For more details see mkfs.cramfs(8).

### [mkfs.minix]

Make a Minix filesystem.

`user `[`$`]`mkfs.minix --help`

    Usage:
     mkfs.minix [options] /dev/name [blocks]

    Options:
     -1                      use Minix version 1
     -2, -v                  use Minix version 2
     -3                      use Minix version 3
     -n, --namelength <num>  maximum length of filenames
     -i, --inodes <num>      number of inodes for the filesystem
     -c, --check             check the device for bad blocks
     -l, --badblocks <file>  list of bad blocks from file
         --lock[=<mode>]     use exclusive device lock (yes, no or nonblock)

     -h, --help              display this help
     -V, --version           display version

    For more details see mkfs.minix(8).

### [mkswap]

Create a [swap](https://wiki.gentoo.org/wiki/Swap "Swap") area.

`user `[`$`]`mkswap --help`

    Usage:
     mkswap [options] device [size]

    Set up a Linux swap area.

    Options:
     -c, --check               check bad blocks before creating the swap area
     -f, --force               allow swap size area be larger than device
     -p, --pagesize SIZE       specify page size in bytes
     -L, --label LABEL         specify label
     -v, --swapversion NUM     specify swap-space version number
     -U, --uuid UUID           specify the uuid to use
         --verbose             verbose output
         --lock[=<mode>]       use exclusive device lock (yes, no or nonblock)
     -h, --help                display this help
     -V, --version             display version

    For more details see mkswap(8).

### [more]

A file perusal filter for CRT viewing. See [pager](https://wiki.gentoo.org/wiki/Pager "Pager").

`user `[`$`]`more --help`

    Usage:
     more [options] <file>...

    A file perusal filter for CRT viewing.

    Options:
     -d, --silent          display help instead of ringing bell
     -f, --logical         count logical rather than screen lines
     -l, --no-pause        suppress pause after form feed
     -c, --print-over      do not scroll, display text and clean line ends
     -p, --clean-print     do not scroll, clean screen and display text
     -s, --squeeze         squeeze multiple blank lines into one
     -u, --plain           suppress underlining and bold
     -n, --lines <number>  the number of lines per screenful
     -<number>             same as --lines
     +<number>             display file beginning from line number
     +/           display file beginning from pattern match

     -h, --help            display this help
     -V, --version         display version

    For more details see more(1).

### [mount]

See [mount](https://wiki.gentoo.org/wiki/Mount "Mount").

### [mountpoint]

Check whether a directory or file is a mountpoint.

`user `[`$`]`mountpoint --help`

    Usage:
     mountpoint [-qd] /path/to/directory
     mountpoint -x /dev/device

    Check whether a directory or file is a mountpoint.

    Options:
     -q, --quiet        quiet mode - don't print anything
         --nofollow     do not follow symlink
     -d, --fs-devno     print maj:min device number of the filesystem
     -x, --devno        print maj:min device number of the block device

     -h, --help         display this help
     -V, --version      display version

    For more details see mountpoint(1).

### [namei]

Follow a pathname until a terminal point is found.

`user `[`$`]`namei --help`

    Usage:
     namei [options] ...

    Follow a pathname until a terminal point is found.

    Options:
     -x, --mountpoints   show mount point directories with a 'D'
     -m, --modes         show the mode bits of each file
     -o, --owners        show owner and group name of each file
     -l, --long          use a long listing format (-m -o -v)
     -n, --nosymlinks    don't follow symlinks
     -v, --vertical      vertical align of modes and owners
     -h, --help          display this help
     -V, --version       display version

    For more details see namei(1).

### [nsenter]

Run a program with namespaces of other processes.

`user `[`$`]`nsenter --help`

    Usage:
     nsenter [options] [ [<argument>...]]

    Run a program with namespaces of other processes.

    Options:
     -a, --all              enter all namespaces
     -t, --target      target process to get namespaces from
     -m, --mount[=<file>]   enter mount namespace
     -u, --uts[=<file>]     enter UTS namespace (hostname etc)
     -i, --ipc[=<file>]     enter System V IPC namespace
     -n, --net[=<file>]     enter network namespace
     -p, --pid[=<file>]     enter pid namespace
     -C, --cgroup[=<file>]  enter cgroup namespace
     -U, --user[=<file>]    enter user namespace
     -T, --time[=<file>]    enter time namespace
     -S, --setuid <uid>     set uid in entered namespace
     -G, --setgid <gid>     set gid in entered namespace
         --preserve-credentials do not touch uids or gids
     -r, --root[=<dir>]     set the root directory
     -w, --wd[=<dir>]       set the working directory
     -F, --no-fork          do not fork before exec'ing

     -h, --help             display this help
     -V, --version          display version

    For more details see nsenter(1).

### [partx]

Tell the kernel about the presence and numbering of partitions.

`user `[`$`]`partx --help`

    Usage:
     partx [-a|-d|-s|-u] [--nr <n:m> | ] <disk>

    Tell the kernel about the presence and numbering of partitions.

    Options:
     -a, --add            add specified partitions or all of them
     -d, --delete         delete specified partitions or all of them
     -u, --update         update specified partitions or all of them
     -s, --show           list partitions

     -b, --bytes          print SIZE in bytes rather than in human readable format
     -g, --noheadings     don't print headings for --show
     -n, --nr <n:m>       specify the range of partitions (e.g. --nr 2:4)
     -o, --output <list>  define which output columns to use
         --output-all     output all columns
     -P, --pairs          use key="value" output format
     -r, --raw            use raw output format
     -S, --sector-size <num>  overwrite sector size
     -t, --type <type>    specify the partition type
         --list-types     list supported partition types and exit
     -v, --verbose        verbose mode

     -h, --help           display this help
     -V, --version        display version

    Available output columns:
             NR  partition number
          START  start of the partition in sectors
            END  end of the partition in sectors
        SECTORS  number of sectors
           SIZE  human readable size
           NAME  partition name
           UUID  partition UUID
           TYPE  partition type (a string, a UUID, or hex)
          FLAGS  partition flags
         SCHEME  partition table type (dos, gpt, ...)

    For more details see partx(8).

### [pg]

Browse pagewise through text files.

`user `[`$`]`pg --help`

    Usage:
     pg [options] [+line] [+/pattern/] [files]

    Browse pagewise through text files.

    Options:
     -number      lines per page
     -c           clear screen before displaying
     -e           do not pause at end of a file
     -f           do not split long lines
     -n           terminate command with new line
     -p   specify prompt
     -r           disallow shell escape
     -s           print messages to stdout
     +number      start at the given line
     +/pattern/   start at the line containing pattern

     -h, --help     display this help
     -V, --version  display version

    For more details see pg(1).

### [pivot_root]

Change the root filesystem.

`user `[`$`]`pivot_root --help`

    Usage:
     pivot_root [options] new_root put_old

    Change the root filesystem.

    Options:
     -h, --help     display this help
     -V, --version  display version

    For more details see pivot_root(8).

### [prlimit]

Show or change the resource limits of a process.

`user `[`$`]`prlimit --help`

    Usage:
     prlimit [options] [-p PID]
     prlimit [options] COMMAND

    Show or change the resource limits of a process.

    General Options:
     -p, --pid         process id
     -o, --output <list>    define which output columns to use
         --noheadings       don't print headings
         --raw              use the raw output format
         --verbose          verbose output
     -h, --help             display this help
     -V, --version          display version

    Resources Options:
     -c, --core             maximum size of core files created
     -d, --data             maximum size of a process's data segment
     -e, --nice             maximum nice priority allowed to raise
     -f, --fsize            maximum size of files written by the process
     -i, --sigpending       maximum number of pending signals
     -l, --memlock          maximum size a process may lock into memory
     -m, --rss              maximum resident set size
     -n, --nofile           maximum number of open files
     -q, --msgqueue         maximum bytes in POSIX message queues
     -r, --rtprio           maximum real-time scheduling priority
     -s, --stack            maximum stack size
     -t, --cpu              maximum amount of CPU time in seconds
     -u, --nproc            maximum number of user processes
     -v, --as               size of virtual memory
     -x, --locks            maximum number of file locks
     -y, --rttime           CPU time in microseconds a process scheduled
                            under real-time scheduling

    Available output columns:
     DESCRIPTION  resource description
        RESOURCE  resource name
            SOFT  soft limit
            HARD  hard limit (ceiling)
           UNITS  units

    For more details see prlimit(1).

### [readprofile]

Display kernel profiling information.

`user `[`$`]`readprofile --help`

    Usage:
     readprofile [options]

    Display kernel profiling information.

    Options:
     -m, --mapfile <mapfile>   (defaults: "/boot/System.map" and
                                          "/boot/System.map-5.15.77-gentoo-dist")
     -p, --profile   (default:  "/proc/profile")
     -M, --multiplier <mult>   set the profiling multiplier to <mult>
     -i, --info                print only info about the sampling step
     -v, --verbose             print verbose data
     -a, --all                 print all symbols, even if count is 0
     -b, --histbin             print individual histogram-bin counts
     -s, --counters            print individual counters within functions
     -r, --reset               reset all the counters (root only)
     -n, --no-auto             disable byte order auto-detection

     -h, --help                display this help
     -V, --version             display version

    For more details see readprofile(8).

### [rename]

Rename files.

`user `[`$`]`rename --help`

    Usage:
     rename [options] <expression> <replacement> <file>...

    Rename files.

    Options:
     -v, --verbose       explain what is being done
     -s, --symlink       act on the target of symlinks
     -n, --no-act        do not make any changes
     -o, --no-overwrite  don't overwrite existing files
     -i, --interactive   prompt before overwrite

     -h, --help          display this help
     -V, --version       display version

    For more details see rename(1).

### [renice]

Alter the priority of running processes.

`user `[`$`]`renice --help`

    Usage:
     renice [-n]  [-p|--pid] ...
     renice [-n]   -g|--pgrp ...
     renice [-n]   -u|--user <user>...

    Alter the priority of running processes.

    Options:
     -n, --priority <num>   specify the nice value
     -p, --pid              interpret arguments as process ID (default)
     -g, --pgrp             interpret arguments as process group ID
     -u, --user             interpret arguments as username or user ID

     -h, --help             display this help
     -V, --version          display version

    For more details see renice(1).

### [resizepart]

Tell the kernel about the new size of a partition.

`user `[`$`]`resizepart --help`

    Usage:
     resizepart <disk device>  <length>

    Tell the kernel about the new size of a partition.

    Options:
     -h, --help     display this help
     -V, --version  display version

    For more details see resizepart(8).

### [rev]

Reverse lines characterwise.

`user `[`$`]`rev --help`

    Usage: rev [options] [file ...]

    Reverse lines characterwise.

    Options:
     -h, --help     display this help
     -V, --version  display version

    For more details see rev(1).

### [rfkill]

Tool for enabling and disabling [wireless devices](https://wiki.gentoo.org/wiki/Category:Wireless "Category:Wireless").

`user `[`$`]`rfkill --help`

    Usage:
     rfkill [options] command [identifier ...]

    Tool for enabling and disabling wireless devices.

    Options:
     -J, --json             use JSON output format
     -n, --noheadings       don't print headings
     -o, --output <list>    define which output columns to use
         --output-all       output all columns
     -r, --raw              use the raw output format

     -h, --help             display this help
     -V, --version          display version

    Available output columns:
     DEVICE      kernel device name
     ID          device identifier value
     TYPE        device type name that can be used as identifier
     TYPE-DESC   device type description
     SOFT        status of software block
     HARD        status of hardware block

    Commands:
     help
     event
     list   [identifier]
     block   identifier
     unblock identifier
     toggle  identifier

    For more details see rfkill(8).

### [rtcwake]

Enter a system sleep state until a specified wakeup time.

`user `[`$`]`rtcwake --help`

    Usage:
     rtcwake [options]

    Enter a system sleep state until a specified wakeup time.

    Options:
     -a, --auto               reads the clock mode from adjust file (default)
     -A, --adjfile <file>     specifies the path to the adjust file
                                the default is /etc/adjtime
         --date <timestamp>   date time of timestamp to wake
     -d, --device <device>    select rtc device (rtc0|rtc1|...)
     -n, --dry-run            does everything, but suspend
     -l, --local              RTC uses local timezone
         --list-modes         list available modes
     -m, --mode <mode>        standby|mem|... sleep mode
     -s, --seconds <seconds>  seconds to sleep
     -t, --time <time_t>      time to wake
     -u, --utc                RTC uses UTC
     -v, --verbose            verbose messages

     -h, --help               display this help
     -V, --version            display version

    For more details see rtcwake(8).

### [runuser]

Run \<command\> with the effective user ID and group ID of \<user\>.

`user `[`$`]`runuser --help`

    Usage:
     runuser [options] -u <user> [[--] <command>]
     runuser [options] [-] [<user> [<argument>...]]

    Run <command> with the effective user ID and group ID of <user>.  If -u is
    not given, fall back to su(1)-compatible semantics and execute standard shell.
    The options -c, -f, -l, and -s are mutually exclusive with -u.

    Options:
     -u, --user <user>               username
     -m, -p, --preserve-environment      do not reset environment variables
     -w, --whitelist-environment <list>  don't reset specified variables

     -g, --group <group>             specify the primary group
     -G, --supp-group <group>        specify a supplemental group

     -, -l, --login                  make the shell a login shell
     -c, --command <command>         pass a single command to the shell with -c
     --session-command <command>     pass a single command to the shell with -c
                                       and do not create a new session
     -f, --fast                      pass -f to the shell (for csh or tcsh)
     -s, --shell <shell>             run <shell> if /etc/shells allows it
     -P, --pty                       create a new pseudo-terminal

     -h, --help                      display this help
     -V, --version                   display version

    For more details see runuser(1).

### [script]

Make a typescript of a terminal session.

`user `[`$`]`script --help`

    Usage:
     script [options] [file]

    Make a typescript of a terminal session.

    Options:
     -I, --log-in <file>           log stdin to file
     -O, --log-out <file>          log stdout to file (default)
     -B, --log-io <file>           log stdin and stdout to file

     -T, --log-timing <file>       log timing information to file
     -t[<file>], --timing[=<file>] deprecated alias to -T (default file is stderr)
     -m, --logging-format <name>   force to 'classic' or 'advanced' format

     -a, --append                  append to the log file
     -c, --command <command>       run command rather than interactive shell
     -e, --return                  return exit code of the child process
     -f, --flush                   run flush after each write
         --force                   use output file even when it is a link
     -E, --echo <when>             echo input in session (auto, always or never)
     -o, --output-limit <size>     terminate if output files exceed size
     -q, --quiet                   be quiet

     -h, --help                    display this help
     -V, --version                 display version

    For more details see script(1).

### [scriptlive]

Execute terminal typescript.

`user `[`$`]`scriptlive --help`

    Usage:
     scriptlive [options]
     scriptlive [-t] timingfile [-I|-B] typescript

    Execute terminal typescript.

    Options:
     -t, --timing <file>     script timing log file
     -T, --log-timing <file> alias to -t
     -I, --log-in <file>     script stdin log file
     -B, --log-io <file>     script stdin and stdout log file

     -c, --command <command> run command rather than interactive shell
     -d, --divisor <num>     speed up or slow down execution with time divisor
     -m, --maxdelay <num>    wait at most this many seconds between updates
     -h, --help              display this help
     -V, --version           display version

    For more details see scriptlive(1).

### [scriptreplay]

Play back terminal typescripts, using timing information.

`user `[`$`]`scriptreplay --help`

    Usage:
     scriptreplay [options]
     scriptreplay [-t] timingfile [typescript] [divisor]

    Play back terminal typescripts, using timing information.

    Options:
     -t, --timing <file>     script timing log file
     -T, --log-timing <file> alias to -t
     -I, --log-in <file>     script stdin log file
     -O, --log-out <file>    script stdout log file (default)
     -B, --log-io <file>     script stdin and stdout log file

     -s, --typescript <file> deprecated alias to -O

         --summary           display overview about recorded session and exit
     -d, --divisor <num>     speed up or slow down execution with time divisor
     -m, --maxdelay <num>    wait at most this many seconds between updates
     -x, --stream <name>     stream type (out, in, signal or info)
     -c, --cr-mode <type>    CR char mode (auto, never, always)
     -h, --help              display this help
     -V, --version           display version

    For more details see scriptreplay(1).

### [setarch]

Change the reported architecture and set personality flags.

`user `[`$`]`setarch --help`

    Usage:
     setarch [<arch>] [options] [ [<argument>...]]

    Change the reported architecture and set personality flags.

    Options:
     -B, --32bit              turns on ADDR_LIMIT_32BIT
     -F, --fdpic-funcptrs     makes function pointers point to descriptors
     -I, --short-inode        turns on SHORT_INODE
     -L, --addr-compat-layout changes the way virtual memory is allocated
     -R, --addr-no-randomize  disables randomization of the virtual address space
     -S, --whole-seconds      turns on WHOLE_SECONDS
     -T, --sticky-timeouts    turns on STICKY_TIMEOUTS
     -X, --read-implies-exec  turns on READ_IMPLIES_EXEC
     -Z, --mmap-page-zero     turns on MMAP_PAGE_ZERO
     -3, --3gb                limits the used address space to a maximum of 3 GB
         --4gb                ignored (for backward compatibility only)
         --uname-2.6          turns on UNAME26
     -v, --verbose            say what options are being switched on
         --list               list settable architectures, and exit

     -h, --help               display this help
     -V, --version            display version

    For more details see setarch(8).

### [setpriv]

Run a program with different Linux privilege settings.

Command only available if the [[[caps]](https://packages.gentoo.org/useflags/caps)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set.

### [setsid]

Run a program in a new session.

`user `[`$`]`setsid --help`

     setsid [options]  [arguments ...]

    Run a program in a new session.

    Options:
     -c, --ctty     set the controlling terminal to the current one
     -f, --fork     always fork
     -w, --wait     wait program to exit, and use the same return
     -h, --help     display this help
     -V, --version  display version

    For more details see setsid(1).

### [setterm]

Set the attributes of a terminal.

`user `[`$`]`setterm --help`

    Usage:
     setterm [options]

    Set the attributes of a terminal.

    Options:
     --term <terminal_name>        override TERM environment variable
     --reset                       reset terminal to power-on state
     --resize                      reset terminal rows and columns
     --initialize                  display init string, and use default settings
     --default                     use default terminal settings
     --store                       save current terminal settings as default

     --cursor on|off               display cursor
     --repeat on|off               keyboard repeat
     --appcursorkeys on|off        cursor key application mode
     --linewrap on|off             continue on a new line when a line is full
     --inversescreen on|off        swap colors for the whole screen

     --msg on|off                  send kernel messages to console
     --msglevel <0-8>              kernel console log level

     --foreground default|<color>  set foreground color
     --background default|<color>  set background color
     --ulcolor [bright] <color>    set underlined text color
     --hbcolor [bright] <color>    set half-bright text color
            <color>: black blue cyan green grey magenta red white yellow

     --bold on|off                 bold
     --half-bright on|off          dim
     --blink on|off                blink
     --underline on|off            underline
     --reverse  on|off             swap foreground and background colors

     --clear[=<all|rest>]          clear screen and set cursor position
     --tabs[=<number>...]          set these tab stop positions, or show them
     --clrtabs[=<number>...]       clear these tab stop positions, or all
     --regtabs[=1-160]             set a regular tab stop interval
     --blank[=0-60|force|poke]     set time of inactivity before screen blanks

     --dump[=<number>]             write vcsa<number> console dump to file
     --append <number>             append vcsa<number> console dump to file
     --file <filename>             name of the dump file

     --powersave on|vsync|hsync|powerdown|off
                                   set vesa powersaving features
     --powerdown[=<0-60>]          set vesa powerdown interval in minutes

     --blength[=<0-2000>]          duration of the bell in milliseconds
     --bfreq[=<number>]            bell frequency in Hertz

     --help                        display this help
     --version                     display version

    For more details see setterm(1).

### [sfdisk]

Display or manipulate a disk partition table.

`user `[`$`]`sfdisk --help`

    Usage:
     sfdisk [options] <dev> [[-N] ]
     sfdisk [options] <command>

    Display or manipulate a disk partition table.

    Commands:
     -A, --activate <dev> [ ...] list or set bootable (P)MBR partitions
     -d, --dump <dev>                  dump partition table (usable for later input)
     -J, --json <dev>                  dump partition table in JSON format
     -g, --show-geometry [<dev> ...]   list geometry of all or specified devices
     -l, --list [<dev> ...]            list partitions of each device
     -F, --list-free [<dev> ...]       list unpartitioned free areas of each device
     -r, --reorder <dev>               fix partitions order (by start offset)
     -s, --show-size [<dev> ...]       list sizes of all or specified devices
     -T, --list-types                  print the recognized types (see -X)
     -V, --verify [<dev> ...]          test whether partitions seem correct
         --delete <dev> [ ...]   delete all or specified partitions

     --part-label <dev>  [<str>] print or change partition label
     --part-type <dev>  [<type>] print or change partition type
     --part-uuid <dev>  [<uuid>] print or change partition uuid
     --part-attrs <dev>  [<str>] print or change partition attributes

     --disk-id <dev> [<str>]           print or change disk label ID (UUID)
     --relocate <oper> <dev>           move partition header

    Arguments:
     <dev>                     device (usually disk) path
                         partition number
     <type>                    partition type, GUID for GPT, hex for MBR

    Options:
     -a, --append              append partitions to existing partition table
     -b, --backup              backup partition table sectors (see -O)
         --bytes               print SIZE in bytes rather than in human readable format
         --move-data[=<typescript>] move partition data after relocation (requires -N)
         --move-use-fsync      use fsync after each write when move data
     -f, --force               disable all consistency checking
         --color[=<when>]      colorize output (auto, always or never)
                                 colors are enabled by default
         --lock[=<mode>]       use exclusive device lock (yes, no or nonblock)
     -N, --partno <num>        specify partition number
     -n, --no-act              do everything except write to device
         --no-reread           do not check whether the device is in use
         --no-tell-kernel      do not tell kernel about changes
     -O, --backup-file   override default backup file name
     -o, --output <list>       output columns
     -q, --quiet               suppress extra info messages
     -w, --wipe <mode>         wipe signatures (auto, always or never)
     -W, --wipe-partitions <mode>  wipe signatures from new partitions (auto, always or never)
     -X, --label <name>        specify label type (dos, gpt, ...)
     -Y, --label-nested <name> specify nested label type (dos, bsd)

     -G, --show-pt-geometry    deprecated, alias to --show-geometry
     -L, --Linux               deprecated, only for backward compatibility
     -u, --unit S              deprecated, only sector unit is supported

     -h, --help                display this help
     -v, --version             display version

    Available output columns:
     gpt: Device Start End Sectors Size Type Type-UUID Attrs Name UUID
     dos: Device Start End Sectors Cylinders Size Type Id Attrs Boot End-C/H/S Start-C/H/S
     bsd: Slice Start End Sectors Cylinders Size Type Bsize Cpg Fsize
     sgi: Device Start End Sectors Cylinders Size Type Id Attrs
     sun: Device Start End Sectors Cylinders Size Type Id Flags

    For more details see sfdisk(8).

### [su]

Adopt the privileges of other users from the system. See [su](https://wiki.gentoo.org/wiki/Su "Su").

### [sulogin]

Single-user login.

`user `[`$`]`sulogin --help`

    Usage:
     sulogin [options] [tty device]

    Single-user login.

    Options:
     -p, --login-shell        start a login shell
     -t, --timeout <seconds>  max time to wait for a password (default: no limit)
     -e, --force              examine password files directly if getpwnam(3) fails

     -h, --help               display this help
     -V, --version            display version

    For more details see sulogin(8).

### [swaplabel]

Display or change the label or UUID of a swap area.

`user `[`$`]`swaplabel --help`

    Usage:
     swaplabel [options] <device>

    Display or change the label or UUID of a swap area.

    Options:
     -L, --label <label> specify a new label
     -U, --uuid <uuid>   specify a new uuid

     -h, --help          display this help
     -V, --version       display version

    For more details see swaplabel(8).

### [swapoff]

Disable devices and files for paging and swapping.

`user `[`$`]`swapoff --help`

    Usage:
     swapoff [options] [<spec>]

    Disable devices and files for paging and swapping.

    Options:
     -a, --all              disable all swaps from /proc/swaps
     -v, --verbose          verbose mode

     -h, --help             display this help
     -V, --version          display version

    The <spec> parameter:
     -L <label>             LABEL of device to be used
     -U <uuid>              UUID of device to be used
     LABEL=<label>          LABEL of device to be used
     UUID=<uuid>            UUID of device to be used
     <device>               name of device to be used
     <file>                 name of file to be used

    For more details see swapoff(8).

### [swapon]

Enable devices and files for paging and swapping.

`user `[`$`]`swapon --help`

    Usage:
     swapon [options] [<spec>]

    Enable devices and files for paging and swapping.

    Options:
     -a, --all                enable all swaps from /etc/fstab
     -d, --discard[=] enable swap discards, if supported by device
     -e, --ifexists           silently skip devices that do not exist
     -f, --fixpgsz            reinitialize the swap space if necessary
     -o, --options <list>     comma-separated list of swap options
     -p, --priority     specify the priority of the swap device
     -s, --summary            display summary about used swap devices (DEPRECATED)
         --show[=<columns>]   display summary in definable table
         --noheadings         don't print table heading (with --show)
         --raw                use the raw output format (with --show)
         --bytes              display swap size in bytes in --show output
     -v, --verbose            verbose mode

     -h, --help               display this help
     -V, --version            display version

    The <spec> parameter:
     -L <label>             synonym for LABEL=<label>
     -U <uuid>              synonym for UUID=<uuid>
     LABEL=<label>          specifies device by swap area label
     UUID=<uuid>            specifies device by swap area UUID
     PARTLABEL=<label>      specifies device by partition label
     PARTUUID=<uuid>        specifies device by partition UUID
     <device>               name of device to be used
     <file>                 name of file to be used

    Available discard policy types (for --discard):
     once    : only single-time area discards are issued
     pages   : freed pages are discarded before they are reused
    If no policy is selected, both discard types are enabled (default).

    Available output columns:
     NAME   device file or partition path
     TYPE   type of the device
     SIZE   size of the swap area
     USED   bytes in use
     PRIO   swap priority
     UUID   swap uuid
     LABEL  swap label

    For more details see swapon(8).

### [switch_root]

Switch to another filesystem as the root of the mount tree.

`user `[`$`]`switch_root --help`

    Usage:
     switch_root [options] <newrootdir> <init> <args to init>

    Switch to another filesystem as the root of the mount tree.

    Options:
     -h, --help     display this help
     -V, --version  display version

    For more details see switch_root(8).

### [taskset]

Show or change the CPU affinity of a process.

`user `[`$`]`taskset --help`

    Usage: taskset [options] [mask | cpu-list] [pid|cmd [args...]]

    Show or change the CPU affinity of a process.

    Options:
     -a, --all-tasks         operate on all the tasks (threads) for a given pid
     -p, --pid               operate on existing given pid
     -c, --cpu-list          display and specify cpus in list format
     -h, --help              display this help
     -V, --version           display version

    The default behavior is to run a new command:
        taskset 03 sshd -b 1024
    You can retrieve the mask of an existing task:
        taskset -p 700
    Or set it:
        taskset -p 03 700
    List format uses a comma-separated list instead of a mask:
        taskset -pc 0,3,7-11 700
    Ranges in list format can take a stride argument:
        e.g. 0-31:2 is equivalent to mask 0x55555555

    For more details see taskset(1).

### [uclampset]

Show or change the utilization clamping attributes.

`user `[`$`]`uclampset --help`

    Usage:
     uclampset [options]
     uclampset [options] --pid  | --system | <command> <arg>...

    Show or change the utilization clamping attributes.

    Options:
     -m <value>           util_min value to set
     -M <value>           util_max value to set
     -a, --all-tasks      operate on all the tasks (threads) for a given pid
     -p, --pid       operate on existing given pid
     -s, --system         operate on system
     -R, --reset-on-fork  set reset-on-fork flag
     -v, --verbose        display status information
     -h, --help           display this help
     -V, --version        display version

    Utilization value range is [0:1024]. Use special -1 value to reset to system's default.

    For more details see uclampset(1).

### [ul]

Do underlining.

`user `[`$`]`ul --help`

    Usage:
     ul [options] [<file> ...]

    Do underlining.

    Options:
     -t, -T, --terminal TERMINAL  override the TERM environment variable
     -i, --indicated              underlining is indicated via a separate line
     -h, --help                   display this help
     -V, --version                display version

    For more details see ul(1).

### [umount]

Unmount filesystems. See [unmount a filesystem](https://wiki.gentoo.org/wiki/Mount#Unmount_a_filesystem "Mount").

### [unshare]

Run a program with some namespaces unshared from the parent.

`user `[`$`]`unshare --help`

    Usage:
     unshare [options] [ [<argument>...]]

    Run a program with some namespaces unshared from the parent.

    Options:
     -m, --mount[=<file>]      unshare mounts namespace
     -u, --uts[=<file>]        unshare UTS namespace (hostname etc)
     -i, --ipc[=<file>]        unshare System V IPC namespace
     -n, --net[=<file>]        unshare network namespace
     -p, --pid[=<file>]        unshare pid namespace
     -U, --user[=<file>]       unshare user namespace
     -C, --cgroup[=<file>]     unshare cgroup namespace
     -T, --time[=<file>]       unshare time namespace

     -f, --fork                fork before launching
     --map-user=<uid>|<name>   map current user to uid (implies --user)
     --map-group=<gid>|<name>  map current group to gid (implies --user)
     -r, --map-root-user       map current user to root (implies --user)
     -c, --map-current-user    map current user to itself (implies --user)

     --kill-child[=<signame>]  when dying, kill the forked child (implies --fork)
                                 defaults to SIGKILL
     --mount-proc[=<dir>]      mount proc filesystem first (implies --mount)
     --propagation slave|shared|private|unchanged
                               modify mount propagation in mount namespace
     --setgroups allow|deny    control the setgroups syscall in user namespaces
     --keep-caps               retain capabilities granted in user namespaces

     -R, --root=<dir>          run the command with root directory set to <dir>
     -w, --wd=<dir>            change working directory to <dir>
     -S, --setuid <uid>        set uid in entered namespace
     -G, --setgid <gid>        set gid in entered namespace
     --monotonic <offset>      set clock monotonic offset (seconds) in time namespaces
     --boottime <offset>       set clock boottime offset (seconds) in time namespaces

     -h, --help                display this help
     -V, --version             display version

    For more details see unshare(1).

### [utmpdump]

Dump UTMP and WTMP files in raw format.

`user `[`$`]`utmpdump --help`

    Usage:
     utmpdump [options] [filename]

    Dump UTMP and WTMP files in raw format.

    Options:
     -f, --follow         output appended data as the file grows
     -r, --reverse        write back dumped data into utmp file
     -o, --output <file>  write to file instead of standard output
     -h, --help           display this help
     -V, --version        display version

    For more details see utmpdump(1).

### [uuid]

A daemon for generating UUIDs.

`user `[`$`]`uuid --help`

    Usage:
     uuidd [options]

    A daemon for generating UUIDs.

    Options:
     -p, --pid         path to pid file
     -s, --socket      path to socket
     -T, --timeout <sec>     specify inactivity timeout
     -k, --kill              kill running daemon
     -r, --random            test random-based generation
     -t, --time              test time-based generation
     -n, --uuids <num>       request number of uuids
     -P, --no-pid            do not create pid file
     -F, --no-fork           do not daemonize using double-fork
     -S, --socket-activation do not create listening socket
     -d, --debug             run in debugging mode
     -q, --quiet             turn on quiet mode

     -h, --help              display this help
     -V, --version           display version

    For more details see uuidd(8).

### [uuidgen]

Create a new UUID value.

`user `[`$`]`uuidgen --help`

    Usage:
     uuidgen [options]

    Create a new UUID value.

    Options:
     -r, --random        generate random-based uuid
     -t, --time          generate time-based uuid
     -n, --namespace ns  generate hash-based uuid in this namespace
                           available namespaces: @dns @url @oid @x500
     -N, --name name     generate hash-based uuid from this name
     -m, --md5           generate md5 hash
     -s, --sha1          generate sha1 hash
     -x, --hex           interpret name as hex string

     -h, --help          display this help
     -V, --version       display version

    For more details see uuidgen(1).

### [uuidparse]

Parse unique identifiers.

`user `[`$`]`uuidparse --help`

    Usage:
     uuidparse [options] <uuid ...>

    Options:
     -J, --json             use JSON output format
     -n, --noheadings       don't print headings
     -o, --output <list>    COLUMNS to display (see below)
     -r, --raw              use the raw output format
     -h, --help             display this help
     -V, --version          display version

    Available output columns:
         UUID  unique identifier
      VARIANT  variant name
         TYPE  type name
         TIME  timestamp

    For more details see uuidparse(1).

### [wall]

Write a message to all users.

Command only available if the [[[tty-helpers]](https://packages.gentoo.org/useflags/tty-helpers)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set.

### [wdctl]

Show the status of the hardware watchdog.

`user `[`$`]`wdctl --help`

    Usage:
     wdctl [options] [<device> ...]

    Show the status of the hardware watchdog.

    Options:
     -f, --flags <list>     print selected flags only
     -F, --noflags          don't print information about flags
     -I, --noident          don't print watchdog identity information
     -n, --noheadings       don't print headings for flags table
     -O, --oneline          print all information on one line
     -o, --output <list>    output columns of the flags
     -r, --raw              use raw output format for flags table
     -T, --notimeouts       don't print watchdog timeouts
     -s, --settimeout <sec> set watchdog timeout
     -x, --flags-only       print only flags table (same as -I -T)

     -h, --help             display this help
     -V, --version          display version

    The default device is /dev/watchdog0.

    Available output columns:
              FLAG  flag name
       DESCRIPTION  flag description
            STATUS  flag status
       BOOT-STATUS  flag boot status
            DEVICE  watchdog device name

    For more details see wdctl(8).

### [whereis]

Locate the binary, source, and manual-page files for a command. See also [[[sys-apps/which]](https://packages.gentoo.org/packages/sys-apps/which)[]].

`user `[`$`]`whereis --help`

    Usage:
     whereis [options] [-BMS <dir>... -f] <name>

    Locate the binary, source, and manual-page files for a command.

    Options:
     -b         search only for binaries
     -B <dirs>  define binaries lookup path
     -m         search only for manuals and infos
     -M <dirs>  define man and info lookup path
     -s         search only for sources
     -S <dirs>  define sources lookup path
     -f         terminate <dirs> argument list
     -u         search for unusual entries
     -l         output effective lookup paths

     -h, --help     display this help
     -V, --version  display version

    For more details see whereis(1).

### [wipefs]

Wipe signatures from a device.

`user `[`$`]`wipefs --help`

    Usage:
     wipefs [options] <device>

    Wipe signatures from a device.

    Options:
     -a, --all           wipe all magic strings (BE CAREFUL!)
     -b, --backup        create a signature backup in $HOME
     -f, --force         force erasure
     -i, --noheadings    don't print headings
     -J, --json          use JSON output format
     -n, --no-act        do everything except the actual write() call
     -o, --offset <num>  offset to erase, in bytes
     -O, --output <list> COLUMNS to display (see below)
     -p, --parsable      print out in parsable instead of printable format
     -q, --quiet         suppress output messages
     -t, --types <list>  limit the set of filesystem, RAIDs or partition tables
         --lock[=<mode>] use exclusive device lock (yes, no or nonblock)
     -h, --help          display this help
     -V, --version       display version

    Arguments:
     <num> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

    Available output columns:
         UUID  partition/filesystem UUID
        LABEL  filesystem LABEL
       LENGTH  magic string length
         TYPE  superblok type
       OFFSET  magic string offset
        USAGE  type description
       DEVICE  block device name

    For more details see wipefs(8).

### [write]

Send a message to another user.

Command only available if the [[[tty-helpers]](https://packages.gentoo.org/useflags/tty-helpers)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag is set.

### [zramctl]

Set up and control [zram](https://wiki.gentoo.org/wiki/Zram "Zram") devices.

`user `[`$`]`zramctl --help`

    Usage:
     zramctl [options] <device>
     zramctl -r <device> [...]
     zramctl [options] -f | <device> -s <size>

    Set up and control zram devices.

    Options:
     -a, --algorithm lzo|lz4|lz4hc|deflate|842   compression algorithm to use
     -b, --bytes               print sizes in bytes rather than in human readable format
     -f, --find                find a free device
     -n, --noheadings          don't print headings
     -o, --output <list>       columns to use for status output
         --output-all          output all columns
         --raw                 use raw status output format
     -r, --reset               reset all specified devices
     -s, --size <size>         device size
     -t, --streams <number>    number of compression streams

     -h, --help                display this help
     -V, --version             display version

    Arguments:
     <size> arguments may be followed by the suffixes for
       GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

    Available output columns:
            NAME  zram device name
        DISKSIZE  limit on the uncompressed amount of data
            DATA  uncompressed size of stored data
           COMPR  compressed size of stored data
       ALGORITHM  the selected compression algorithm
         STREAMS  number of concurrent compress operations
      ZERO-PAGES  empty pages with no allocated memory
           TOTAL  all memory including allocator fragmentation and metadata overhead
       MEM-LIMIT  memory limit used to store compressed data
        MEM-USED  memory zram have been consumed to store compressed data
        MIGRATED  number of objects migrated by compaction
      MOUNTPOINT  where the device is mounted

    For more details see zramctl(8).

## [Listing commands]

Installed utilities can be obtained by the following command:

`user `[`$`]`cat /var/db/pkg/sys-apps/util-linux*/CONTENTS | grep bin | awk '' FS=/ | cut -d " " -f 1 | sort`

Alternatively the following command can be used if the [[[app-portage/portage-utils]](https://packages.gentoo.org/packages/app-portage/portage-utils)[]] suite is installed:

`user `[`$`]`qlist sys-apps/util-linux | grep bin | awk '' FS=/ | sort`

Or if [[[app-portage/gentoolkit]](https://packages.gentoo.org/packages/app-portage/gentoolkit)[]] is installed:

`user `[`$`]`equery f util-linux | grep /bin`

## [Troubleshooting]

-   [Gentoo Forums: su stopped working](https://forums.gentoo.org/viewtopic-p-8690717.html#8690717)

## [See also]

-   [GNU Coreutils](https://wiki.gentoo.org/wiki/GNU_Coreutils "GNU Coreutils") --- basic file, shell and text manipulation utilities of the GNU operating system; a superset of the utilities specified by the [POSIX \"Shell and Utilities\" volume](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/contents.html).