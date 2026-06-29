# Docs Xml / Manpages / nmblookup.1

nmblookup
	 1
	 Samba
	 User Commands


nmblookup


NetBIOS over TCP/IP client used to lookup NetBIOS
	names


nmblookup

		 -M|--master-browser
		 --recursion
		 -S|--status
		 -r|--root-port
		 -A|--lookup-by-ip
		 -B|--broadcast=BROADCAST-ADDRESS
		 -U|--unicast=UNICAST-ADDRESS
		 -T|--translate
		 -f|--flags
		 -?|--help
		 --usage
		 -d|--debuglevel=DEBUGLEVEL
		 --debug-stdout
		 --configfile=CONFIGFILE
		 --option=name=value
		 -l|--log-basename=LOGFILEBASE
		 --leak-report
		 --leak-report-full
		 -R|--name-resolve=NAME-RESOLVE-ORDER
		 -O|--socket-options=SOCKETOPTIONS
		 -m|--max-protocol=MAXPROTOCOL
		 -n|--netbiosname=NETBIOSNAME
		 --netbios-scope=SCOPE
		 -W|--workgroup=WORKGROUP
		 --realm=REALM
		 name


DESCRIPTION


This tool is part of the   samba
	 7   suite.


nmblookup
 is used to query NetBIOS names
	and map them to IP addresses in a network using NetBIOS over TCP/IP
	queries. The options allow the name queries to be directed at a
	particular IP broadcast area or to a particular machine. All queries
	are done over UDP.


OPTIONS


-M|--master-browser


Searches for a master browser by looking
		up the NetBIOS
name
 with a
		type of  0x1d . If

		name
 is "-" then it does a lookup on the special name
		 __MSBROWSE__ . Please note that in order to
		use the name "-", you need to make sure "-" isn't parsed as an
		argument, e.g. use :
		 nmblookup -M -- - .


--recursion


Set the recursion desired bit in the packet
		to do a recursive lookup. This is used when sending a name
		query to a machine running a WINS server and the user wishes
		to query the names in the WINS server.  If this bit is unset
		the normal (broadcast responding) NetBIOS processing code
		on a machine is used instead. See RFC1001, RFC1002 for details.


-S|--status


Once the name query has returned an IP
		address then do a node status query as well. A node status
		query returns the NetBIOS names registered by a host.


-r|--root-port


Try and bind to UDP port 137 to send and receive UDP
		datagrams. The reason for this option is a bug in Windows 95
		where it ignores the source port of the requesting packet
	 	and only replies to UDP port 137. Unfortunately, on most UNIX
		systems root privilege is needed to bind to this port, and
		in addition, if the   nmbd
		 8   daemon is running on this machine it also binds to this port.


-A|--lookup-by-ip


Interpret
name
 as
		an IP Address and do a node status query on this address.


-B|--broadcast


Send the query to the given broadcast address. Without
		this option the default behavior of nmblookup is to send the
		query to the broadcast address of the network interfaces as
		either auto-detected or defined in the
interfaces
		  parameter of the   smb.conf
	 5   file.


-U|--unicast


Do a unicast query to the specified address or
		host
unicast address
. This option
		(along with the
-R  option) is needed to
		query a WINS server.


-T|--translate


This causes any IP addresses found in the
		lookup to be looked up via a reverse DNS lookup into a
		DNS name, and printed out before each


 IP address .... NetBIOS name


 pair that is the normal output.


-f|--flags


		Show which flags apply to the name that has been looked up. Possible
		answers are zero or more of: Response, Authoritative,
		Truncated, Recursion_Desired, Recursion_Available, Broadcast.


name


This is the NetBIOS name being queried. Depending
		upon the previous options this may be a NetBIOS name or IP address.
		If a NetBIOS name then the different name types may be specified
		by appending '# ' to the name. This name may also be
		'*', which will return all registered names within a broadcast
		area.


EXAMPLES


nmblookup
 can be used to query
		a WINS server (in the same way
nslookup
 is
		used to query DNS servers). To query a WINS server,
nmblookup

		must be called like this:


nmblookup -U server -R 'name'


For example, running :


nmblookup -U samba.org -R 'IRIX#1B'


would query the WINS server samba.org for the domain
		master browser (1B name type) for the IRIX workgroup.


VERSION


This man page is part of version  of
	the Samba suite.


SEE ALSO


  nmbd
	 8  ,   samba
	 7  , and   smb.conf
	 5  .


AUTHOR


The original Samba software and related utilities
	were created by Andrew Tridgell. Samba is now developed
	by the Samba Team as an Open Source project similar
	to the way the Linux kernel is developed.
