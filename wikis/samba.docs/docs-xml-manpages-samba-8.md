# Docs Xml / Manpages / samba.8

samba

8

Samba

System Administration tools

samba

Server to provide AD and SMB/CIFS services to clients

samba

-D\|--daemon

-F\|--foreground

-i\|--interactive

-M\|--model=MODEL

--maximum-runtime=seconds

-b\|--show-build

--no-process-group

-d\|--debuglevel=DEBUGLEVEL

--debug-stdout

--configfile=CONFIGFILE

--option=name=value

-l\|--log-basename=LOGFILEBASE

--leak-report

--leak-report-full

-V\|--version

# DESCRIPTION

This program is part of the `samba(7)` suite.

`samba` is the server daemon that provides Active Directory, filesharing and printing services to clients. The server provides filespace and directory services to clients using the SMB (or CIFS) protocol and other related protocols such as DCE/RPC, LDAP and Kerberos.

Clients supported include MSCLIENT 3.0 for DOS, Windows for Workgroups, Windows 95/98/ME, Windows NT, Windows 2000/XP/2003, OS/2, DAVE for Macintosh, and cifsfs for Linux.

An extensive description of the services that the server can provide is given in the man page for the configuration file controlling the attributes of those services (see `smb.conf(5)`. This man page will not describe the services, but will concentrate on the administrative aspects of running the server.

Please note that there are significant security implications to running this server, and the `smb.conf(5)` manual page should be regarded as mandatory reading before proceeding with installation.

# OPTIONS

-D\|--daemon
If specified, this parameter causes the server to operate as a daemon. That is, it detaches itself and runs in the background, fielding requests on the appropriate ports. Operating the server as a daemon is the recommended way of running `samba` for servers that provide more than casual use file and print services. This switch is assumed if `samba` is executed on the command line of a shell.

-F\|--foreground
If specified, this parameter causes the `samba` process to not daemonize, i.e. double-fork and disassociate with the terminal.

-i\|--interactive
If this parameter is specified it causes the server to run "interactively", not as a daemon, even if the server is executed on the command line of a shell. Setting this parameter negates the implicit daemon mode when run from the command line. `samba` also logs to standard output, as if the `-S` parameter had been given.

-M\|--model
This parameter can be used to specify the "process model" samba should use. This determines how concurrent clients are handled. Available process models include:

- *single*

  All Samba services run in a single process. This is not recommended for production configurations.

- *standard*

  A process is created for each Samba service, and for those services that support it (currently only LDAP and NETLOGON) a new processes is started for each new client connection.

  Historically, this was the 'standard' way Samba behaved up until v4.10. Note that this model can be resource intensive if you have a large number of client connections.

- *prefork*

  The default. A process is started for each Samba service, and a fixed number of worker processes are started for those services that support it (currently LDAP, NETLOGON, and KDC). The client connections are then shared amongst the worker processes. Requests for services not supporting prefork are handled by a single process for that service.

  The number of prefork worker processes started is controlled by the `smb.conf(5)` parameter , which defaults to 4.

--maximum-runtime=seconds
Set maximum runtime of the server process till autotermination in seconds.

-b\|--show-build
Print information about how Samba was built.

# FILES

`/etc/rc`
or whatever initialization script your system uses.

If running the server as a daemon at startup, this file will need to contain an appropriate startup sequence for the server.

`/etc/services`
If running the server via the meta-daemon `inetd`, this file must contain a mapping of service name (e.g., netbios-ssn) to service port (e.g., 139) and protocol type (e.g., tcp).

`/usr/local/samba/lib/smb.conf`
This is the default location of the `smb.conf(5)` server configuration file. Other common places that systems install this file are `/usr/samba/lib/smb.conf` and `/etc/samba/smb.conf`.

This file describes all the services the server is to make available to clients. See `smb.conf(5)` for more information.

# DIAGNOSTICS

Most diagnostics issued by the server are logged in a specified log file. The log file name is specified at compile time, but may be overridden on the command line.

The number and nature of diagnostics available depends on the debug level used by the server. If you have problems, set the debug level to 3 and peruse the log files.

Most messages are reasonably self-explanatory. Unfortunately, at the time this man page was created, there are too many diagnostics available in the source code to warrant describing each and every diagnostic. At this stage your best bet is still to grep the source code and inspect the conditions that gave rise to the diagnostics you are seeing.

# VERSION

This man page is part of version of the Samba suite.

# SEE ALSO

`hosts_access(5)` `smb.conf(5)`, `smbclient(8)`, `samba-tool(8)`, `smbd(8)`, `nmbd(8)`, `winbindd(1)`, and the Internet RFC's `rfc1001.txt`, `rfc1002.txt`. In addition the CIFS (formerly SMB) specification is available as a link from the Web page <https://www.samba.org/cifs/>.

# AUTHOR

The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.
