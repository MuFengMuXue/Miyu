**Resources**

[[]][Home](https://irssi.org/)

[[]][Package information](https://packages.gentoo.org/packages/net-irc/irssi)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Irssi "wikipedia:Irssi")

[[]][[#irssi](ircs://irc.libera.chat/#irssi)] ([[webchat](https://web.libera.chat/#irssi)])

**irssi** is a powerful text-mode IRC client for connecting to internet relay chat (IRC) networks. Non-standard features are implemented with perl scripts, rather than in the core. Irssi can range from a functional, no-frills client to a highly-customized and automated client.^[\[1\]](#cite_note-1)^ Irssi can handle multiple IRC connections simultaneously, thus it is possible to be active in channels on different networks at the same time.^[\[2\]](#cite_note-2)^

## Contents

-   [[1] [Install]](#Install)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Screen]](#Screen)
        -   [[3.1.1] [Detaching screen sessions]](#Detaching_screen_sessions)
        -   [[3.1.2] [Attaching screen sessions]](#Attaching_screen_sessions)
    -   [[3.2] [tmux]](#tmux)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)
-   [[6] [References]](#References)

## [Install]

### [USE flags]

### [USE flags for] [net-irc/irssi](https://packages.gentoo.org/packages/net-irc/irssi) [[]] [A modular textUI IRC client with IPv6 support]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+perl`](https://packages.gentoo.org/useflags/+perl)             Add optional support/bindings for the Perl language
  [`+proxy`](https://packages.gentoo.org/useflags/+proxy)           Adds support for a loadable IRC proxy module
  [`otr`](https://packages.gentoo.org/useflags/otr)                 Adds support for a loadable IRC otr module
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-19 02:48] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[net-irc/irssi]](https://packages.gentoo.org/packages/net-irc/irssi)[]]:

`root `[`#`]`emerge --ask net-irc/irssi`

To run the program, simply open up a terminal and type [irssi]. Read the manual [man irssi] to see all available command-line options. More on using Irssi can be found in the usage section below.

## [Configuration]

The first time [irssi] is invoked by a user a configuration file will be created in [\~/.irssi/config] This can be modified with the [/set] command while in the client by typing [/set option value]. Typing [/set] by itself will display available options and their current values.

For changes to remain persistent over restarts, modify the configuration file found at [\~/.irssi/config]. See the following example:

[FILE] **`~/.irssi/config`Example configuration**

    ...
    settings = ;
      ...
    };

## [Usage]

As mentioned above [irssi] is started by invoking:

`user `[`$`]`irssi`

While in the Irssi interface command-line options can be issued in order to have Irssi perform the desired actions.

Connect to a IRC network, here `irc.libera.chat`:

[/connect irc.libera.chat]

Set the user name to `larry`:

[/nick larry]

Starting [irssi] using the above options with one command-line invocation:

`user `[`$`]`irssi -c irc.libera.chat -n larry`

Optionally certain channels may require registration before speaking is permitted. For these types of channels, register with the service and then login with the chosen nickname and password:

`user `[`$`]`irssi irc.libera.chat 6667 larry:password`

Join the `#gentoo` IRC channel:

[/join #gentoo]

Leave the `#gentoo` channel:

[/leave #gentoo]

Save configured settings:

[/save]

Quit an Irssi IRC session:

[/quit] or [/exit]

### [Screen]

[[screen](https://wiki.gentoo.org/wiki/Screen "Screen")] is a useful tool that allows a user to manipulate multiple windows inside of a single terminal session. Each window operates independently of the others and acts like another terminal.^[\[3\]](#cite_note-3)^

If [irssi] is currently open, close it using the [/quit] command and start screen by typing:

`user `[`$`]`screen`

This opens a new screen session. To someone who has not used screen before it may appear that invoking the [screen] command above did nothing. This is not the case; there was something that happened by running screen, using the `-list` option will show the user that there is now an open screen session:

`user `[`$`]`screen -list`

Starting [irssi] *inside* the screen session will create a helpful use case. Start [irssi] again *inside* the [screen] session:

`user `[`$`]`irssi`

While inside a [screen] session special keystrokes are used in order to provide control. [Ctrl]+[a] is the keystroke needed to beseech control of screen.

#### [Detaching screen sessions]

To detach a [screen] session press: [Ctrl]+[a] then [d]

#### [Attaching screen sessions]

To re-attach to a running [screen] session type:

`user `[`$`]`screen -rd`

### [tmux]

[tmux] is another good way to manage [irssi] sessions. Start a [tmux] session for [irssi] by typing:

`user `[`$`]`tmux new-session -s irssi`

Once inside the [tmux] session start [irssi] by typing:

`user (tmux session)``irssi`

[Ctrl]+[b] is the keystroke needed to grab control of [tmux]. To detach the [irssi] session press [Ctrl]+[b] then the [d] key. If everything went properly the [irssi] session should detach and the focus returned to the shell prompt.

To re-attach a session use the `attach-session -t <session_name>` argument (where `<session_name>` is the name used for the [irssi] session):

`user `[`$`]`tmux attach-session -t irssi`

For more information on the details of using [tmux] see the [[tmux] article](https://wiki.gentoo.org/wiki/Tmux "Tmux").

## [See also]

-   [Quassel](https://wiki.gentoo.org/wiki/Quassel "Quassel") --- a daemon/headless IRC client written in C++ that supports 24/7 connectivity.
-   [Screen](https://wiki.gentoo.org/wiki/Screen "Screen") --- a program that enables the creation of multiple sessions and virtual terminals within a single terminal.
-   [Tmux](https://wiki.gentoo.org/wiki/Tmux "Tmux") --- a program that enables a number of terminals (or windows), each running a separate program, to be created, accessed, and controlled from a single screen or terminal window.
-   [WeeChat](https://wiki.gentoo.org/wiki/WeeChat "WeeChat") --- a light, extensible, actively maintained, well documented, highly featured text-mode [IRC](https://wiki.gentoo.org/wiki/IRC "IRC") client.

## [External resources]

-   [Official irrsi documentation](https://irssi.org/documentation)
-   [irssi scripts index](https://scripts.irssi.org/)
-   [IRC protocol RFC 1459](https://tools.ietf.org/html/rfc1459)

## [References]

1.  [[[↑](#cite_ref-1)] [Matt Sparks. [A Guide to Efficiently Using Irssi and Screen](https://quadpoint.org/articles/irssi/), [Matt Sparks](https://quadpoint.org/), December 19th, 2004. Retrieved on January 10th, 2015.]]
2.  [[[↑](#cite_ref-2)] [Matt Sparks. [A Guide to Efficiently Using Irssi and Screen](https://quadpoint.org/articles/irssi/), [Matt Sparks](https://quadpoint.org/), December 19th, 2004. Retrieved on January 10th, 2015.]]
3.  [[[↑](#cite_ref-3)] [Matt Sparks. [A Guide to Efficiently Using Irssi and Screen](https://quadpoint.org/articles/irssi/), [Matt Sparks](https://quadpoint.org/), December 19th, 2004. Retrieved on January 10th, 2015.]]