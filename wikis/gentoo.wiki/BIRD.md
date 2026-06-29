[[]][Home](https://bird.network.cz/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/bird)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Bird_Internet_routing_daemon "wikipedia:Bird Internet routing daemon")

[[]][GitHub](https://github.com/CZ-NIC/bird)

[[]][GitLab](https://gitlab.com/gitlab.nic.cz/labs/bird/)

[[]][[#bird](ircs://irc.libera.chat/#bird)] ([[webchat](https://web.libera.chat/#bird)])

**BIRD** (recursive acronym for BIRD Internet Routing Daemon) is a routing daemon implementing OSPF, RIPv2 & BGP, Babel for IP on Unix-like operating systems.

\

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
        -   [[3.1.1] [show]](#show)
        -   [[3.1.2] [configure]](#configure)
        -   [[3.1.3] [verify]](#verify)
    -   [[3.2] [Unmerge]](#Unmerge)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/bird](https://packages.gentoo.org/packages/net-misc/bird) [[]] [A routing daemon implementing OSPF, RIPv2 & BGP for IPv4 & IPv6]

  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+client`](https://packages.gentoo.org/useflags/+client)               Build the ncurses/readline full featured CLI
  [`+filecaps`](https://packages.gentoo.org/useflags/+filecaps)           Use Linux file capabilities to control privilege rather than set\*id (this is orthogonal to USE=caps which uses capabilities at runtime e.g. libcap)
  [`custom-cflags`](https://packages.gentoo.org/useflags/custom-cflags)   Build with user-specified CFLAGS (unsupported)
  [`debug`](https://packages.gentoo.org/useflags/debug)                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`libssh`](https://packages.gentoo.org/useflags/libssh)                 Enables net-libs/libssh binding, mendatory for RPKI support
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ----------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-24 21:20] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-misc/bird`

## [Configuration]

Extract the default bird example configuration file:

`root `[`#`]`bzcat /usr/share/doc/bird-2.*/bird.conf.example.bz2 >/etc/bird.conf`

Content of the default configration file, without comments:

[FILE] **`/etc/bird.conf`**

    log syslog all;
    protocol device

    protocol direct

    protocol kernel ;
    }

    protocol kernel ;
    }

    protocol static

Adjust the daemon configuration file to run as [bird] default system user/group:

[FILE] **`/etc/conf.d/bird`**

    # /etc/init.d/bird

    # Options to pass to the bird process
    # See https://bird.network.cz/?get_doc&v=20&f=bird-1.html#ss1.3
    # BIRD_GROUP and BIRD_USER will be appended to BIRD_OPTS

    BIRD_GROUP="bird"
    BIRD_USER="bird"
    #BIRD_OPTS=""

Add **larry** to the [bird] system group:

`root `[`#`]`gpasswd -a larry bird`

### [Files]

-   [/etc/bird.conf] - Global (system wide) configuration file.
-   [/etc/conf.d/bird] - System daemon configuration file.

### [Service]

#### [OpenRC]

Start the daemon:

`root `[`#`]`rc-service bird start`

Add the daemon to the default bootup routine:

`root `[`#`]`rc-update add bird default`

#### [systemd]

There is no systemd unit installed by the package at the moment.

** Note**\
If the main routing table is large, you may want to remove the [myhostname] module from the [host] entry in [/etc/nsswitch.conf] to avoid slow DNS lookups [\[1\]](https://github.com/systemd/systemd/issues/11384)

## [Usage]

### [Invocation]

To configure and operate BIRD, the routing daemon, use the [birdc] client:

`user `[`$`]`birdc`

Show basic mode commands, use the [?] key for displaying help:

`bird>``? `

    quit                                           Quit the client
    exit                                           Exit the client
    help                                           Description of the help system
    show ...                                       Show status information
    dump ...                                       Dump debugging information
    eval <expr>                                    Evaluate an expression
    echo ...                                       Control echoing of log messages
    disable ( | "" | all) [message]  Disable protocol
    enable ( | "" | all) [message]  Enable protocol
    restart ( | "" | all) [message]  Restart protocol
    reload  | "" | all          Reload protocol
    debug ...                                      Control protocol debugging via BIRD logs
    mrtdump ...                                    Control protocol debugging via MRTdump files
    restrict                                       Restrict current CLI session to safe commands
    configure ...                                  Reload configuration
    down                                           Shut the daemon down
    graceful restart                               Shut the daemon down for graceful restart
    bird>

#### [show]

Use the [show status] command, to verify the BIRD daemon is up and running:

`bird>``show status `

    BIRD 2.0.12
    Router ID is 192.0.2.1
    Hostname is gentoobird
    Current server time is 2023-10-08 19:02:39.392
    Last reboot on 2023-10-08 18:41:26.247
    Last reconfiguration on 2023-10-08 18:41:26.247
    Daemon is up and running

#### [configure]

Use the [configure ?] to show basic routing configuration commands:

`bird>``configure ? `

    configure ["<file>"] [timeout [<sec>]]         Reload configuration
    configure soft ["<file>"] [timeout [<sec>]]    Reload configuration and ignore changes in filters
    configure timeout [<sec>]                      Reload configuration with undo timeout
    configure confirm                              Confirm last configuration change - deactivate undo timeout
    configure undo                                 Undo last configuration change
    configure status                               Show configuration status
    configure check ["<file>"]                     Parse configuration and check its validity

#### [verify]

Use the [configure check] command, to verify the current, running BIRD configuration file is sane:

`bird>``configure check `

    Reading configuration from /etc/bird.conf
    Configuration OK

Use the [show ?] to display more IP routing and system verification commands:

`bird>``show ? `

    show status                                    Show router status
    show memory                                    Show memory usage
    show protocols [ | ""]      Show routing protocols
    show interfaces                                Show network interfaces
    show route ...                                 Show routing table
    show symbols ...                               Show all known symbolic names
    show bfd ...                                   Show information about BFD protocol
    show babel ...                                 Show information about Babel protocol
    show ospf ...                                  Show information about OSPF protocol
    show rip ...                                   Show information about RIP protocol
    show static [<name>]                           Show details of static protocol

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-misc/bird`

## [See also]

-   [iproute2](https://wiki.gentoo.org/wiki/Iproute2 "Iproute2") --- a tool developed to unify network interface configuration, routing, and tunneling for Linux systems.
-   [static_routing](https://wiki.gentoo.org/wiki/Static_routing "Static routing") --- covers routing of the IP protocol in the Linux kernel.
-   [Frr](https://wiki.gentoo.org/wiki/Frr "Frr") --- a set of unified tools to configure and manage dynamic routing protocols.

## [External resources]

-   [Official BIRD 3.x User\'s Guide](https://bird.network.cz/?get_doc&f=bird.html&v=30)
-   [Notes on BIRD\'s preference value specifics](https://bird.network.cz/pipermail/bird-users/2019-March/013146.html)