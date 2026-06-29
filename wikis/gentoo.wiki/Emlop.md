**Resources**

[[]][GitHub](https://github.com/vincentdephily/emlop.git)

[[]][Package information](https://packages.gentoo.org/packages/app-portage/emlop)

**emlop** parses emerge logs to yield useful info like merge history and merge time prediction. It draws inspiration from genlop and qlop but aims to be faster, more accurate, and more ergonomic. Emlop is written in Rust.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Examples]](#Examples)
-   [[3] [See also]](#See_also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-portage/emlop`

## [Usage]

### [Invocation]

`user `[`$`]`emlop --help`

    A fast, accurate, ergonomic EMerge LOg Parser
    https://github.com/vincentdephily/emlop

    Usage: emlop [OPTIONS] <COMMAND>

    Commands:
      log       Show log of sucessful merges, unmerges and syncs
      predict   Predict merge times for current or pretended merges
      stats     Show statistics about syncs, per-package (un)merges, and total (un)merges
      accuracy  Compare actual merge time against predicted merge time
      complete  Generate shell completion script

    Options:
      -F, --logfile <file>
              Location of emerge log file

      -v...
              Increase verbosity (defaults to errors only)
                -v:   show warnings
                -vv:  show info
                -vvv: show debug

      -h, --help
              Print help (see a summary with '-h')

      -V, --version
              Print version

    Filter:
      -f, --from <date>
              Only parse log entries after <date>
                2018-03-04|2018-03-04 12:34:56|2018-03-04T12:34: Absolute ISO date
                123456789:                                       Absolute unix timestamp
                1 year, 2 months|10d:                            Relative date

      -t, --to <date>
              Only parse log entries before <date>
                2018-03-04|2018-03-04 12:34:56|2018-03-04T12:34: Absolute ISO date
                123456789:                                       Absolute unix timestamp
                1 year, 2 months|10d:                            Relative date

    Format:
      -H, --header [<bool>]
              Show table header

          --duration <format>
              Output durations in different formats
                hms|(default): 10:30
                hmsfixed:      0:10:30
                secs|s:        630
                human|h:       10 minutes, 30 seconds

          --date <format>
              Output dates in different formats
                ymd|d:               2022-01-31
                (default)|ymdhms|dt: 2022-01-31 08:59:46
                ymdhmso|dto:         2022-01-31 08:59:46 +00:00
                rfc3339|3339:        2022-01-31T08:59:46+00:00
                rfc2822|2822:        Mon, 31 Jan 2022 08:59:46 +00:00
                compact:             20220131085946
                unix:                1643619586

          --utc [<bool>]
              Parse/display dates in UTC instead of local time

          --color [<bool>]
              Enable color (yes/no/auto)
                (default)|auto|a: colored if on tty
                (empty)|yes|y:    colored
                no|n:             not colored

      -o, --output <format>
              Ouput format (columns/tab/auto)
                (default)|auto|a: columns on tty, tab otherwise
                columns|c:        space-aligned columns
                tab|t:            tab-separated values

    Commands and long args can be abbreviated (eg `emlop l -ss --head -f1w`)
    Commands have their own -h / --help
    Exit code is 0 if sucessful, 1 if search found nothing, 2 in case of other errors
    Config can be set in $HOME/.config/emlop.toml, see example in /usr/share/doc/emlop-0.7.0

### [Examples]

Refresh status every 10 seconds:

`user `[`$`]`watch -cn 10 emlop p --color`

Show merge times:

`root `[`#`]`emlop l dev-build/cmake`

    2024-10-12 16:22:34  1:19:56 dev-build/cmake-3.30.2
    2024-10-13 12:36:02       17 dev-build/cmake-3.30.2
    2024-10-21 20:26:52    27:29 dev-build/cmake-3.30.5

## [See also]

-   [q applets](https://wiki.gentoo.org/wiki/Q_applets "Q applets") --- a collection of small, fast [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") **q**uery utilities written in C.