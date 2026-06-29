**Resources**

[[]][Home](https://moc.daper.net/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Music_on_Console "wikipedia:Music on Console")

**MOC** (**m**usic **o**n **c**onsole) is a console audio player for Linux/UNIX designed to be powerful and easy to use.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Theme]](#Theme)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Player]](#Player)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Emerge]

The Gentoo repository has [[[media-sound/moc]](https://packages.gentoo.org/packages/media-sound/moc)[]] though the xdch47 overlay allows building without FFmpeg version dependency conflicts.

`root `[`#`]`emerge media-sound/moc`

## [Configuration]

### [Theme]

T, arrow keys, enter, then q changes themes.

To save it, \~/.config/moc must be changed to reference a theme from /usr/share/moc/themes:

`user `[`$`]`ls -1 /usr/share/moc/themes`

    black_orange_theme
    black_theme
    blue_theme
    darkdot_theme
    example_theme
    green_theme
    moca_theme
    nightly_theme
    red_theme
    transparent-background
    white_theme
    yellow_red_theme

[FILE] **`~/.config/moc`**

    Theme = green_theme

## [Usage]

### [Invocation]

`user `[`$`]`mocp --help`

    Music On Console (version 2.6-alpha3-p1)
    Usage: mocp [OPTIONS] [FILE|DIR ...]

    General options:
      -M, --moc-dir=DIR                 Use the specified MOC directory instead of the default
      -m, --music-dir                   Start in MusicDir
      -C, --config=FILE                 Use the specified config file instead of the default (conflicts with '--no-config')
          --no-config                   Use program defaults rather than any config file (conflicts with '--config')
      -O, --set-option='NAME=VALUE'     Override the configuration option NAME with VALUE
      -F, --foreground                  Run the server in foreground (logging to stdout)
      -S, --server                      Only run the server
      -R, --sound-driver=DRIVERS        Use the first valid sound driver
      -A, --ascii                       Use ASCII characters to draw lines
      -T, --theme=FILE                  Use the selected theme file (read from ~/.moc/themes if the path is not absolute)
      -y, --sync                        Synchronize the playlist with other clients
      -n, --nosync                      Don't synchronize the playlist with other clients

    Server commands:
      -P, --pause                       Pause
      -U, --unpause                     Unpause
      -G, --toggle-pause                Toggle between playing and paused
      -s, --stop                        Stop playing
      -f, --next                        Play the next song
      -r, --previous                    Play the previous song
      -k, --seek=N                      Seek by N seconds (can be negative)
      -j, --jump=N                 Jump to some position in the current track
      -v, --volume=[+,-]LEVEL           Adjust the PCM volume
      -x, --exit                        Shutdown the server
      -a, --append                      Append the files/directories/playlists passed in the command line to playlist
      -e, --recursively                 Alias for --append
      -q, --enqueue                     Add the files given on command line to the queue
      -c, --clear                       Clear the playlist
      -p, --play                        Start playing from the first item on the playlist
      -l, --playit                      Play files given on command line without modifying the playlist
      -t, --toggle=CONTROL              Toggle a control (shuffle, autonext, repeat)
      -o, --on=CONTROL                  Turn on a control (shuffle, autonext, repeat)
      -u, --off=CONTROL                 Turn off a control (shuffle, autonext, repeat)
      -i, --info                        Print information about the file currently playing
      -Q, --format=FORMAT               Print formatted information about the file currently playing

    Miscellaneous options:
      -V, --version                     Print version information
          --echo-args                   Print POPT-interpreted arguments
          --usage                       Print brief usage
      -h, --help                        Print extended usage

    Environment variables:

      MOCP_OPTS                         Additional command line options
      MOCP_POPTRC                       List of POPT configuration files

### [Player]

To start the player with a directory:

`user `[`$`]`mocp ~/Music`

Control the player with keyboard [MOC shortcuts](https://gist.github.com/chiragparekh/8868544a8b3cc4d6d6ba):

[FILE]

    List of MOC Keys
      enter  -- starts playing
      s      -- stops playing
      n      -- plays next item from the playlist
      b      -- plays previous item from the playlist
      space  -- pause
      p      -- pause

      S      -- plays at random
      R      -- repeats the same song in a loop,
            Next (X button below) must be OFF
      X      -- switches to play sequentially
      o      -- plays a file from the Internet
      u      -- moves playlist item up
      j      -- moves playlist item down
      Ctrl+u -- adds the URL to the playlist
      g      -- searches marked string in file names
      /      -- searches marked string in file names

      r      -- rereads the directory
      T      -- switches to the theme selection menu
      f      -- toggles display mode of song titles
      TAB    -- switches marker bar between the playlist
            and the file manager panels
      l      -- switches between displaying the playlist
                or the file manager panel
      P      -- switches full path in the playlist
      H      -- toggles hidden files view
      Ctrl-t -- toggles song duration time
      Ctrl-f -- toggles format file view
      m      -- moves to directory entered in config file
      G      -- moves to directory with currently played file
      i      -- moves to marked directory
      U      -- moves to upper directory
      a      -- adds a file to the playlist
      A      -- adds a directory recursively to the playlist
      C      -- clears the playlist
      V      -- saves the playlist
      d      -- removes marked item from the playlist
      Y      -- removes all empty items from the playlist

      < -- decreases volume by 1%
      ,      -- decreases volume by 5%
      >      -- increases volume by 1%
      .      -- increases volume by 5%

      x      -- toggles the mixer channel
      ?      -- shows help

      !      -- goes to a fast dir 1 (set in config file)
      @      -- goes to a fast dir 2
      #      -- goes to a fast dir 3
      $      -- goes to a fast dir 4
      %      -- goes to a fast dir 5
      ^      -- goes to a fast dir 6
      &      -- goes to a fast dir 7
      *      -- goes to a fast dir 8
      (      -- goes to a fast dir 9
      )      -- goes to a fast dir 10

      F1     -- executes ExecCommand1 (set in config file)
      F2     -- executes ExecCommand2
      F3     -- executes ExecCommand3
      F4     -- executes ExecCommand4
      F5     -- executes ExecCommand5
      F6     -- executes ExecCommand6
      F7     -- executes ExecCommand7
      F8     -- executes ExecCommand8
      F9     -- executes ExecCommand9
      F10    -- executes ExecCommand10

## [External resources]

[MOC explained on wiki.archlinux.org](https://wiki.archlinux.org/title/MOC)