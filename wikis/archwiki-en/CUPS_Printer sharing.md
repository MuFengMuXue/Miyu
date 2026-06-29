# CUPS/Printer sharing

This article contains instruction on sharing printers from a GNU/Linux system.

{| class="wikitable sortable"
|+ Client support
! Protocol
! Linux
! Windows
! macOS
|-
! Discovery (DNS-SD/mDNS)
| CUPS with Avahi
| Native support since Windows 10
| Bonjour
|-
! Internet Printing Protocol
| CUPS
| Control Panel > Programs > Turn Windows features on or off > Print and Document Services > Internet Printing Client
| Native support
|-
! SMB shared printer
| Samba with CUPS
| Native support
| Native support
|-
! Line Printer Daemon protocol
| CUPS
| Control Panel > Programs > Turn Windows features on or off > Print services >'LPD Print Service and LPR Port Monitor''
| Native support
|-
|}

## Creating class for multiple printers
In CUPS, a class is a group of printers which appears to clients as a single printer. When a client selects to print to the class, CUPS selects any printer in the group to accept the print job. This may be especially useful when one printer from the class must be removed. If it is excluded from the class, end users will not notice any change because the print job will be queued to another printer in the class. Creating and managing classes can be done from CUPS Web GUI.

## Printer sharing
## DNS-SD advertisement
To announce the printer to the network over DNS-SD/mDNS (Bonjour in Apple world), Avahi must be installed and running on the server.

To enable it, either select Share printers connected to this system in the web interface, or manually set  in :

Afterwards restart .

Note that "browsing" at the print server is a different thing from "browsing" at a remote networked host.  On the print server,  provides the DNS-SD protocol support which the  broadcasts.  The  service is unnecessary on the print server, unless also broadcasting the old CUPS protocol, or the print server is also "browsing" for other networked printers.  On the remote networked host, the  service is required to "browse" for network broadcasts of print services, and running  will also automatically start .

The  service will be automatically started when a USB printer is plugged in, however this may not be the case for other connection types. If  is not running,  does not broadcast the print services, so in that case the systemd unit service file must be modified to start on boot, and then the service must again be "enabled/installed" with the new dependency. To do this, edit the service file  section to add a  dependency, and then enable and start the  service.

## Sharing via Internet Printing Protocol
The server can be configured using either the web interface or by manually editing .

Open up the web interface to the server, select the Administration tab, look under the Server heading, and enable the "Share printers connected to this system" option. Save your change by clicking on the Change Settings button. The server will automatically restart.

On the server computer (the one directly connected to the printer), allow access to the server by modifying the location directive. For instance:

Also make sure the server is listening on the IP address the client will use:

There are more configuration possibilities, including automatic methods, which are described in detail in Using Network Printers and .

After making any modifications, restart .

If CUPS is started using socket activation, create a drop-in snippet for  so that socket activation also works for remote connections:

## Sharing via Samba
Samba is an implementation of the Windows file and printer sharing protocols, even the most vintage ones.

To configure Samba on the Linux server, edit  file to allow access to printers. File  can look something like this:

That should be enough to share the printer, yet adding an individual printer entry may be desirable:

Please note that this assumes configuration was made so that users must have a valid account to access the printer. To have a public printer, set  to , and remove the  line. To add accounts, set up a regular GNU/Linux account and then set up a Samba password on the server. See Samba#User management.

After this, restart  and .

See Samba's documentation Setting up Samba as a Print Server for more details.

## Sharing via Line Printer Daemon protocol
Enable and start .

## Remote administration
Once the server is set up as described in #Printer sharing, it can also be configured so that it can be remotely administered. Add the allowed hosts to the  block in , using the same syntax as described in #Sharing via Internet Printing Protocol. Note that three levels of access can be granted:

            #access to the server
 	#access to the admin pages
 	#access to configuration files

To give remote hosts access to one of these levels, add an  statement to that level's section. An  statement can take one or more of the forms listed below:

 Allow from all
 Allow from host.domain.com
 Allow from *.domain.com
 Allow from ip-address
 Allow from ip-address/netmask
 Allow from @LOCAL

Deny statements can also be used. For example, to give full access to all hosts on your local network interfaces, edit  to include this:

 # Restrict access to the server...
 # By default only localhost connections are possible

    Order allow,deny
    Allow from @LOCAL

 # Restrict access to the admin pages...

    Order allow,deny
    Allow from @LOCAL

 # Restrict access to configuration files...

    AuthType Basic
    Require user @SYSTEM
    Order allow,deny
    Allow from @LOCAL

You might also need to disable the HTTPS requirement, when using the default self-signed certificate generated by CUPS:

 DefaultEncryption IfRequested

This should avoid the error: 426 - Upgrade Required when using the CUPS web interface from a remote machine.

## Kerberos
Kerberos can be used to authenticate users accessing a remote CUPS server. This assumes that your machine has a keytab and it will need a ticket for "HTTP". Instead of using  you must use  - encryption is required for auth (hence https) and the full hostname is needed so that Kerberos/Negotiate can work. In addition, the server must be configured in  to use a  of .

If you are using Samba's winbind NSS support, you can add an AD group name to  - in the following example  might be an AD group:

## Troubleshooting
See CUPS/Troubleshooting for general troubleshooting tips.

## Cannot print with GTK applications
If you get a getting printer information failed message when you try to print from GTK applications, add this line to your :

## Permission errors on Windows
Some users fixed  (Windows clients) errors by using a slightly different syntax:

 smb://workgroup/username:password@hostname/printer_name

## Local Printing is fine, but no printing via Network
Depending on the printer (Especially for unidirectional label-printers) one side must be configured with the -driver to be able to print

## Other operating systems
More information on interfacing CUPS with other printing systems can be found in the CUPS manual, e.g. on http://localhost:631/help/network.html.
