**Resources**

[[]][Home](http://www.ivarch.com/programs/pv.shtml)

[[]][Man page](http://man7.org/linux/man-pages/man1/pv.1.html)

**pv** (Pipe Viewer) is a command line tool to view verbose information about data streamed/piped *through* it. The data can be of any source like files, block devices, network streams etc. It shows the amount of data passed through, time running, progress bar, percentage and the estimated completion time.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Copy files]](#Copy_files)
    -   [[2.3] [Pipe input]](#Pipe_input)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/pv](https://packages.gentoo.org/packages/sys-apps/pv) [[]] [Pipe Viewer: a tool for monitoring the progress of data through a pipe]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)             Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`ncurses`](https://packages.gentoo.org/useflags/ncurses)         Add ncurses support (console display library)
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-26 05:41] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[sys-apps/pv]](https://packages.gentoo.org/packages/sys-apps/pv)[]] using the following command:

`root `[`#`]`emerge --ask sys-apps/pv`

## [Usage]

[pv] is mostly used with other programs which lack the ability to monitor progress.

### [Invocation]

`user `[`$`]`pv --help`

    Usage: pv [OPTION] [FILE]...
    Concatenate FILE(s), or standard input, to standard output,
    with monitoring.

      -p, --progress           show progress bar
      -t, --timer              show elapsed time
      -e, --eta                show estimated time of arrival (completion)
      -I, --fineta             show absolute estimated time of arrival
                               (completion)
      -r, --rate               show data transfer rate counter
      -a, --average-rate       show data transfer average rate counter
      -b, --bytes              show number of bytes transferred
      -T, --buffer-percent     show percentage of transfer buffer in use
      -A, --last-written NUM   show NUM bytes last written
      -F, --format FORMAT      set output format to FORMAT
      -n, --numeric            output percentages, not visual information
      -q, --quiet              do not output any transfer information at all

      -W, --wait               display nothing until first byte transferred
      -D, --delay-start SEC    display nothing until SEC seconds have passed
      -s, --size SIZE          set estimated data size to SIZE bytes
      -l, --line-mode          count lines instead of bytes
      -0, --null               lines are null-terminated
      -i, --interval SEC       update every SEC seconds
      -w, --width WIDTH        assume terminal is WIDTH characters wide
      -H, --height HEIGHT      assume terminal is HEIGHT rows high
      -N, --name NAME          prefix visual information with NAME
      -f, --force              output even if standard error is not a terminal
      -c, --cursor             use cursor positioning escape sequences

      -L, --rate-limit RATE    limit transfer to RATE bytes per second
      -B, --buffer-size BYTES  use a buffer size of BYTES
      -C, --no-splice          never use splice(), always use read/write
      -E, --skip-errors        skip read errors in input
      -S, --stop-at-size       stop after --size bytes have been transferred
      -R, --remote PID         update settings of process PID

      -P, --pidfile FILE       save process ID in FILE

      -d, --watchfd PID[:FD]   watch file FD opened by process PID

      -h, --help               show this help and exit
      -V, --version            show version information and exit

    Please report any bugs to .

### [Copy files]

The easiest way to use [pv] is by using a file as the input stream and direct the output stream into another file:

`user `[`$`]`pv /etc/portage/make.conf > ~/make.conf`

This is the same as (per default all output is turned on):

`user `[`$`]`pv -p -t -e -r -b /etc/portage/make.conf > ~/make.conf`

That is, according to the [invocation](#Invocation) (listed above):

-   `-p`: Display a progress bar.
-   `-t`: Display the total elapsed time.
-   `-e`: Estimate the completion time.
-   `-r`: Display the current transfer rate.
-   `-b`: Display the total bytes transferred.

### [Pipe input]

The estimated completion time and progress bar can only be displayed if [pv] knows the total size of the input stream. For example if we use [cat] to produce the input stream and pipe it to [pv]:

`user `[`$`]`cat /etc/portage/make.conf | pv -p -t -e -r -b > ~/make.conf`

The size can be given to [pv] to estimate the time, in this example 1 kB:

`user `[`$`]`cat /etc/portage/make.conf | pv -s1k > ~/make.conf`

Just pipe the data through [pv] and use it in a different program in the end. In this example we see how fast we can download the [index.html] file from www.gentoo.org using [curl] and count the number of words in it:

`user `[`$`]`curl www.gentoo.org | pv | wc -w`

Or have more verbose output using [[dd](https://wiki.gentoo.org/wiki/Dd "Dd")]:

`user `[`$`]`dd if=/mnt/mylargefile.img | pv | dd of=~/mycopy.img`

## [See also]

-   [Dd](https://wiki.gentoo.org/wiki/Dd "Dd") --- a utility used to copy raw data from a source into sink, where source and sink can be a block device, file, or piped input/output.
-   [Dcfldd](https://wiki.gentoo.org/wiki/Dcfldd "Dcfldd") --- an enhanced [[dd](https://wiki.gentoo.org/wiki/Dd "Dd")] tool that includes additional features for forensics and security.
-   [Ddrescue](https://wiki.gentoo.org/wiki/Ddrescue "Ddrescue") --- a tool provided by GNU to retrieve data from failing (block) storage devices like disk drives, CDROMs, or memory sticks, etc.