**Resources**

[[]][Home](https://matt.ucc.asn.au/dropbear/dropbear.html)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/dropbear)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Dropbear_(software) "wikipedia:Dropbear (software)")

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/dropbear)

[[]]This article has some todo items:\

-   add systemd commands where blank

Dropbear is a lightweight SSH server. It runs on a variety of POSIX-based platforms.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Server]](#Server)
        -   [[2.1.1] [Files]](#Files)
            -   [[2.1.1.1] [OpenRC]](#OpenRC)
            -   [[2.1.1.2] [systemd]](#systemd)
    -   [[2.2] [Client]](#Client)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Client]](#Client_2)
-   [[4] [Troubleshooting]](#Troubleshooting)
-   [[5] [Removal]](#Removal)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-misc/dropbear](https://packages.gentoo.org/packages/net-misc/dropbear) [[]] [Small SSH 2 client/server designed for small memory environments]

  ------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------
  [`+shadow`](https://packages.gentoo.org/useflags/+shadow)                 Enable shadow password support
  [`+syslog`](https://packages.gentoo.org/useflags/+syslog)                 Enable support for syslog
  [`+test-async`](https://packages.gentoo.org/useflags/+test-async)         Enable tests using dev-python/asyncssh
  [`bsdpty`](https://packages.gentoo.org/useflags/bsdpty)                   Add support for legacy BSD pty\'s rather than dynamic UNIX pty\'s \-- do not use this flag unless you are absolutely sure you actually want it
  [`legacy-ciphers`](https://packages.gentoo.org/useflags/legacy-ciphers)   Enable support for deprecated, soon-to-be-dropped DSA keys. See https://marc.info/?l=openssh-unix-dev\>m=170494903207436\>w=2.
  [`minimal`](https://packages.gentoo.org/useflags/minimal)                 Install a very minimal build (disables, for example, plugins, fonts, most drivers, non-critical features)
  [`multicall`](https://packages.gentoo.org/useflags/multicall)             Build all the programs as one little binary (to save space)
  [`pam`](https://packages.gentoo.org/useflags/pam)                         Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`savedconfig`](https://packages.gentoo.org/useflags/savedconfig)         Use this to restore your config from /etc/portage/savedconfig \$/\$. Make sure your USE flags allow for appropriate dependencies
  [`static`](https://packages.gentoo.org/useflags/static)                   !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)           Verify upstream signatures on distfiles
  [`zlib`](https://packages.gentoo.org/useflags/zlib)                       Add support for zlib compression
  ------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-10 15:02] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-misc/dropbear`

## [Configuration]

For manual and help use following command:

`user `[`$`]`dropbear -h`

    Dropbear server v2025.88 https://matt.ucc.asn.au/dropbear/dropbear.html
    Usage: dropbear [options]
    -b bannerfile   Display the contents of bannerfile before user login
                    (default: none)
    -r keyfile      Specify hostkeys (repeatable)
                    defaults:
                    - rsa /etc/dropbear/dropbear_rsa_host_key
                    - ecdsa /etc/dropbear/dropbear_ecdsa_host_key
                    - ed25519 /etc/dropbear/dropbear_ed25519_host_key
    -D              Directory containing authorized_keys file
    -R              Create hostkeys as required
    -F              Don't fork into background
    -e              Pass on server process environment to child process
    -E              Log to stderr rather than syslog
    -m              Don't display the motd on login
    -w              Disallow root logins
    -G              Restrict logins to members of specified group
    -s              Disable password logins
    -g              Disable password logins for root
    -B              Allow blank password logins
    -t              Enable two-factor authentication (both password and public key required)
    -T              Maximum authentication tries (default 10)
    -j              Disable local port forwarding
    -k              Disable remote port forwarding
    -a              Allow connections to forwarded ports from any host
    -c command      Force executed command
    -p [address:]port
                    Listen on specified tcp port (and optionally address),
                    up to 10 can be specified
                    (default port is 22 if none specified)
    -P PidFile      Create pid file PidFile
                    (default /var/run/dropbear.pid)
    -l <interface>
                    interface to bind on
    -i              Start for inetd
    -W <receive_window_buffer> (default 24576, larger may be faster, max 10MB)
    -K <keepalive>  (0 is never, default 0, in seconds)
    -I <idle_timeout>  (0 is never, default 0, in seconds)
    -z    disable QoS
    -V    Version

The listed running options can be used below to configure the [/etc/conf.d/dropbear] daemon.

### [Server]

#### [Files]

Edit [/etc/conf.d/dropbear] - Global (system wide) configuration file for the SSH daemon. Add at least the `-w` parameter to the configuration file file to disable root login while running dropbear daemon.

[FILE] **`/etc/conf.d/dropbear`Disable Root logins via SSH**

    # /etc/conf.d/dropbear: config file for /etc/init.d/dropbear

    # -w disables root logins
    # -p changes the TCP port number to listen on, default TCP port 22
    DROPBEAR_OPTS="-w"

Assigning a different TCP port number `-p` to f.e.: 2222 at the beginning, saves the possible default port assingment collision, when running OpenSSH on the same system.

[FILE] **`/etc/conf.d/dropbear`Disable Root logins via SSH, run on port 2222**

    # /etc/conf.d/dropbear: config file for /etc/init.d/dropbear

    # -w disables root logins
    # -p changes the TCP port number to listen to 2222
    DROPBEAR_OPTS="-w -p 2222"

##### [OpenRC]

`root `[`#`]`rc-update add dropbear default`

`root `[`#`]`rc-service dropbear start`

##### [systemd]

### [Client]

## [Usage]

### [Client]

The SSH client software to open a SSH session to target node, is called `dbclient`.

`user `[`$`]`dbclient -h`

    Dropbear SSH client v2025.88 https://matt.ucc.asn.au/dropbear/dropbear.html
    Usage: dbclient [options] [user@]host[/port][,[user@]host/port],...] [command]
    -p <remoteport>
    -l <username>
    -t    Allocate a pty
    -T    Don't allocate a pty
    -N    Don't run a remote command
    -f    Run in background after auth
    -q    quiet, don't show remote banner
    -y    Always accept remote host key if unknown
    -y -y Don't perform any remote host key checking (caution)
    -s    Request a subsystem (use by external sftp)
    -o option     Set option in OpenSSH-like format ('-o help' to list options)
    -i <identityfile>   (multiple allowed, default ~/.ssh/id_dropbear)
    -A    Enable agent auth forwarding
    -L <[listenaddress:]listenport:remotehost:remoteport> Local port forwarding
    -g    Allow remote hosts to connect to forwarded ports
    -R <[listenaddress:]listenport:remotehost:remoteport> Remote port forwarding
    -W <receive_window_buffer> (default 24576, larger may be faster, max 10MB)
    -K <keepalive>  (0 is never, default 0)
    -I <idle_timeout>  (0 is never, default 0)
    -z    disable QoS
    -B <endhost:endport> Netcat-alike forwarding
    -J  Use program pipe rather than TCP connection
    -c <cipher list> Specify preferred ciphers ('-c help' to list options)
    -m <MAC list> Specify preferred MACs for packet verification (or '-m help')
    -b    [bind_address][:bind_port]
    -V    Version

To open a SSH session to a target node use following command. In example below it is shown how to login using `larry` username, to `gentoo.org` server, running the SSH service on TCP port `2222`.

`user `[`$`]`dbclient larry@gentoo.org/2222`

## [Troubleshooting]

Verify the used TCP ports bound to a running dropbaer daemon:

`root `[`#`]`ss -tulpen | egrep 'Net|drop'`

    Netid State  Recv-Q Send-Q   Local Address:Port Peer Address:PortProcess
    tcp   LISTEN 0      1000           0.0.0.0:2222      0.0.0.0:*    users:(("dropbear",pid=32739,fd=4)) ino:55966 sk:1004 <->
    tcp   LISTEN 0      0              0.0.0.0:22        0.0.0.0:*    users:(("sshd",pid=9680,fd=3)) ino:27008 sk:81b26748
    tcp   LISTEN 0      1000              [::]:2222         [::]:*    users:(("dropbear",pid=32739,fd=5)) ino:55967 sk:1005 v6only:1 <->

Showing dropbear runs on port `2222`, on all local interfaces, using IPv4 `0.0.0.0` and IPv6 `[::]`.

## [Removal]

`root `[`#`]`emerge --ask --depclean --verbose net-misc/dropbear`

## [See also]

-   [OpenSSH](https://wiki.gentoo.org/wiki/OpenSSH "OpenSSH") --- the ubiquitous tool for logging into and working on remote machines securely.