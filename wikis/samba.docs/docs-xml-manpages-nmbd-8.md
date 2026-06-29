# Docs Xml / Manpages / nmbd.8

nmbd
	 8
	 Samba
	 System Administration tools


nmbd


NetBIOS name server to provide NetBIOS
	over IP naming services to clients


nmbd

		 -D|--daemon
		 -i|--interactive
		 -F|--foreground
		 --no-process-group
		 -b|--build-options
		 -p
		 -P
		 -d
		 --debug-stdout
		 --configfile=
		 --option= =
		 -l|--log-basename
		 --leak-report
		 --leak-report-full
		 -V|--version


DESCRIPTION


This program is part of the   samba
	 7   suite.


nmbd
 is a server that understands
	and can reply to NetBIOS over IP name service requests, like
	those produced by SMB/CIFS clients such as Windows 95/98/ME,
	Windows NT, Windows 2000, Windows XP and LanManager clients. It also
	participates in the browsing protocols which make up the
	Windows "Network Neighborhood" view.


SMB/CIFS clients, when they start up, may wish to
	locate an SMB/CIFS server. That is, they wish to know what
	IP number a specified host is using.


Amongst other services,
nmbd
 will
	listen for such requests, and if its own NetBIOS name is
	specified it will respond with the IP number of the host it
	is running on.  Its "own NetBIOS name" is by
	default the primary DNS name of the host it is running on,
	but this can be overridden by the
	in . Thus
nmbd
 will
	reply to broadcast queries for its own name(s). Additional
	names for
nmbd
 to respond on can be set
	via parameters in the   smb.conf
	 5   configuration file.


nmbd
 can also be used as a WINS
	(Windows Internet Name Server) server. What this basically means
	is that it will act as a WINS database server, creating a
	database from name registration requests that it receives and
	replying to queries from clients for these names.


In addition,
nmbd
 can act as a WINS
	proxy, relaying broadcast queries from clients that do
	not understand how to talk the WINS protocol to a WINS
	server.


OPTIONS


-D|--daemon


If specified, this parameter causes

nmbd
 to operate as a daemon. That is,
		it detaches itself and runs in the background, fielding
		requests on the appropriate port. By default,
nmbd

		will operate as a daemon if launched from a command shell.
		nmbd can also be operated from the
inetd

		meta-daemon, although this is not recommended.


-F|--foreground


If specified, this parameter causes
		the main
nmbd
 process to not daemonize,
		i.e. double-fork and disassociate with the terminal.
		Child processes are still created as normal to service
		each connection request, but the main process does not
		exit. This operation mode is suitable for running

nmbd
 under process supervisors such
		as
supervise
 and
svscan

		from Daniel J. Bernstein's
daemontools

		package, or the AIX process monitor.


-i|--interactive


If this parameter is specified it causes the
		server to run "interactively", not as a daemon, even if the
		server is executed on the command line of a shell. Setting this
		parameter negates the implicit daemon mode when run from the
		command line.
nmbd
 also logs to standard
		output, as if the  -S  parameter had been
		given.


-H|--hosts


NetBIOS lmhosts file.  The lmhosts
		file is a list of NetBIOS names to IP addresses that
		is loaded by the nmbd server and used via the name
		resolution mechanism   described in   smb.conf
		 5   to resolve any
		NetBIOS name queries needed by the server. Note
		that the contents of this file are  NOT
		used by
nmbd
 to answer any name queries.
		Adding a line to this file affects name NetBIOS resolution
		from this host  ONLY .


The default path to this file is compiled into
		Samba as part of the build process. Common defaults
		are  /usr/local/samba/lib/lmhosts ,
		 /usr/samba/lib/lmhosts  or
		 /etc/samba/lmhosts . See the   lmhosts
	 5   man page for details on the contents of this file.


-p|--port


UDP port number is a positive integer value.
		This option changes the default UDP port number (normally 137)
		that
nmbd
 responds to name queries on. Don't
		use this option unless you are an expert, in which case you
		won't need help!


--no-process-group


Do not create a new process group for nmbd.


FILES


 /etc/inetd.conf


If the server is to be run by the

inetd
 meta-daemon, this file
		must contain suitable startup information for the
		meta-daemon.


 /etc/rc


or whatever initialization script your
		system uses).


If running the server as a daemon at startup,
		this file will need to contain an appropriate startup
		sequence for the server.


 /etc/services


If running the server via the
		meta-daemon
inetd
, this file
		must contain a mapping of service name (e.g., netbios-ssn)
		to service port (e.g., 139) and protocol type (e.g., tcp).


 /usr/local/samba/lib/smb.conf


This is the default location of
		the   smb.conf
		 5   server
		configuration file. Other common places that systems
		install this file are  /usr/samba/lib/smb.conf
		and  /etc/samba/smb.conf .


When run as a WINS server (see the

		parameter in the   smb.conf
		 5   man page),

nmbd

		will store the WINS database in the file  wins.dat
		in the  var/locks  directory configured under
		wherever Samba was configured to install itself.


If
nmbd
 is acting as a
				browse master  (see the
		parameter in the   smb.conf
	 5   man page,
nmbd

		will store the browsing database in the file  browse.dat
		  in the  var/locks  directory
		configured under wherever Samba was configured to install itself.


SIGNALS


To shut down an
nmbd
 process it is recommended
	that SIGKILL (-9)  NOT  be used, except as a last
	resort, as this may leave the name database in an inconsistent state.
	The correct way to terminate
nmbd
 is to send it
	a SIGTERM (-15) signal and wait for it to die on its own.


nmbd
 will accept SIGHUP, which will cause
	it to dump out its namelists into the file  namelist.debug
	  in the  /usr/local/samba/var/locks
	directory (or the  var/locks  directory configured
	under wherever Samba was configured to install itself). This will also
	cause
nmbd
 to dump out its server database in
	the  log.nmb  file. Additionally, the signal will
	cause reloading
nmbd
 configuration.


        Instead of sending a SIGHUP signal, a request to dump namelists
        into the file and reload a configuration file may be sent using
          smbcontrol
        1   program.


The debug log level of nmbd may be raised or lowered
	using   smbcontrol
	 1   (SIGUSR[1|2] signals
	are no longer used since Samba 2.2). This is to allow
	transient problems to be diagnosed, whilst still running
	at a normally low log level.


VERSION


This man page is part of version  of
	the Samba suite.


SEE ALSO


	  inetd
	 8  ,   smbd
	 8  ,   smb.conf
	 5  ,   smbclient
	 1  ,   testparm
	 1  , and the Internet
	RFC's  rfc1001.txt ,  rfc1002.txt .
	In addition the CIFS (formerly SMB) specification is available
	as a link from the Web page
	https://www.samba.org/cifs/ .


AUTHOR


The original Samba software and related utilities
	were created by Andrew Tridgell. Samba is now developed
	by the Samba Team as an Open Source project similar
	to the way the Linux kernel is developed.
