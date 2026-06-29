**Resources**

[[]][Home](https://github.com/shellinabox/shellinabox)

[[]][Package information](https://packages.gentoo.org/packages/www-misc/shellinabox)

[shellinabox] allows access to the command-line from web based terminal emulator. It is useful for web-based administrator access to a system. It is accessible to any JavaScript and CSS enabled web browser and does not require any additional browser plugins.^[\[1\]](#cite_note-1)^.

** Warning**\
Connections to [shellinaboxd] are not secure unless SSL/TLS certificates have been installed or generated.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Securing the connection]](#Securing_the_connection)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
    -   [[4.1] [Unmerge]](#Unmerge)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

Cannot load package information. Is the atom *www-misc/shellinabox* correct?

### [Emerge]

`root `[`#`]`emerge --ask www-misc/shellinabox`

## [Configuration]

### [Securing the connection]

The default configuration exposes a login shell with SSL disabled on the localhost interface only.

Information about the procedure for generating self-signed SSL certificates is [explained here](https://code.google.com/p/shellinabox/issues/detail?id=59#c15).

To generate an SSL certificate for use shellinabox the following commands can be issued:

`root `[`#`]`cd /etc/shellinabox/cert `

`root `[`#`]`openssl genrsa -des3 -out server.key 1024 `

`root `[`#`]`openssl req -new -key server.key -out server.csr `

`root `[`#`]`cp server.key server.key.org `

`root `[`#`]`openssl rsa -in server.key.org -out server.key `

`root `[`#`]`openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt `

`root `[`#`]`cat server.crt server.key > certificate.pem `

For Gentoo user convenience, the ebuild maintainer has provided the above commands in a file located here: [/etc/shellinabox/cert/gen_ssl_cert.bash]

This script can simply be executed in order to generate the SSL certificate:

`root `[`#`]`cd /etc/shellinabox/cert `

`root `[`#`]`bash gen_ssl_cert.bash `

### [Service]

#### [OpenRC]

Add the service to the default runlevel:

`root `[`#`]`rc-update add shellinaboxd default`

Start the service now:

`root `[`#`]`rc-service shellinaboxd start`

#### [systemd]

To start the service at boot:

`root `[`#`]`systemctl enable shellinaboxd`

Start the service now:

`root `[`#`]`systemctl start shellinaboxd`

## [Usage]

After the service is running, open a web browser to the IP address of the system and port `4200`:

`user `[`$`]`firefox http://localhost:4200`

### [Invocation]

`root `[`#`]`shellinaboxd --help`

    Usage: shellinaboxd [OPTIONS]...
    Starts an HTTP server that serves terminal emulators to AJAX enabled browsers.

    List of command line options:
      -b, --background[=PIDFILE]  run in background
      -c, --cert=CERTDIR          set certificate dir (default: $PWD)
          --cert-fd=FD            set certificate file from fd
          --css=FILE              attach contents to CSS style sheet
          --cgi[=PORTMIN-PORTMAX] run as CGI
      -d, --debug                 enable debug mode
      -f, --static-file=URL:FILE  serve static file from URL path
      -g, --group=GID             switch to this group (default: nogroup)
      -h, --help                  print this message
          --linkify=[none|normal|aggressive] default is "normal"
          --localhost-only        only listen on 127.0.0.1
          --no-beep               suppress all audio output
      -n, --numeric               do not resolve hostnames
      -m, --messages-origin=ORIGIN allow iframe message passing from origin
          --pidfile=PIDFILE       publish pid of daemon process
      -p, --port=PORT             select a port (default: 4200)
      -s, --service=SERVICE       define one or more services
      -t, --disable-ssl           disable transparent SSL support
          --disable-ssl-menu      disallow changing transport mode
          --disable-utmp-logging  disable logging to utmp and wtmp
      -q, --quiet                 turn off all messages
          --unixdomain-only=PATH:USER:GROUP:CHMOD listen on unix socket
      -u, --user=UID              switch to this user (default: nobody)
          --user-css=STYLES       defines user-selectable CSS options
      -v, --verbose               enable logging messages
          --version               prints version information
          --disable-peer-check    disable peer check on a session

    Debug, quiet, and verbose are mutually exclusive.

    One or more --service arguments define services that should be made available
    through the web interface:
      SERVICE := <url-path> ':' APP
      APP     := 'LOGIN' | 'SSH' [ : <host> ] | USER ':' CWD ':' CMD
      USER    := 'AUTH' | <username> ':' <groupname>
      CWD     := 'HOME' | <dir>
      CMD     := 'SHELL' | <cmdline>

    <cmdline> supports variable expansion:
      $ - number of columns
      $     - gid id
      $   - group name
      $    - home directory
      $   - number of rows
      $    - name of remote peer
      $  - value of HTTP header field 'X-Real-IP'
      $     - user id
      $     - the URL that serves the terminal session
      $    - user name

    One or more --user-css arguments define optional user-selectable CSS options.
    These options show up in the right-click context menu:
      STYLES  := GROUP *
      GROUP   := OPTION *
      OPTION  := <label> ':' [ '-' | '+' ] <css-file>

    OPTIONs that make up a GROUP are mutually exclusive. But individual GROUPs are
    independent of each other.

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose www-misc/shellinabox`

## [See also]

-   [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") --- the default shell on Gentoo systems and a popular [shell](https://wiki.gentoo.org/wiki/Shell "Shell") program found on many Linux systems.
-   [Ssh](https://wiki.gentoo.org/wiki/Ssh "Ssh") --- the ubiquitous tool for logging into and working on remote machines securely.

## [External resources]

-   [https://www.unixmen.com/shellinabox-a-web-based-ajax-terminal-emulator/](https://www.unixmen.com/shellinabox-a-web-based-ajax-terminal-emulator/) - A guide on setting up shellinabox.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://code.google.com/archive/p/shellinabox/](https://code.google.com/archive/p/shellinabox/)]]