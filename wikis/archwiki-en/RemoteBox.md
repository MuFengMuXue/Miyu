# RemoteBox

RemoteBox is an open-source remote client for managing VirtualBox, written in Perl and GTK. It enabled administering a VirtualBox installation on a server, including its guests and interact with them as if they were running locally. While VirtualBox is installed server-side, RemoteBox runs on a client machine. It provides a complete GTK graphical interface with a look and feel very similar to that of VirtualBox's native GUI. If you are familiar with other virtualization software, such as VMWare ESX, then think of RemoteBox as the "poor man's VI client".

## Installation
## Client-side
RemoteBox is the client application, which can be obtained by installing the  package. For remote desktop operations an RDP client is also needed. RemoteBox includes presets for , rdesktop and . As of this writing,  2.0.0.beta1 has been tested and found working. Alternatively VNC can be used with included presets for TigerVNC, ,  and .

## Server-side
The VM host needs a working VirtualBox installation. For remote desktop operations a non-free Oracle VM VirtualBox Extension Pack is needed for RDP support or alternatively an open-source  can be used for VNC support. Also consider installing guest additions ISO for guests to be able to install or update the tools.

VirtualBox installation includes the VirtualBox web service () providing a HTTP(S) server offering API to clients such as RemoteBox. The service should not and also refuses to run as root. For improved security an additional user for running VMs and web service should be created. The user requires a password (to be used for remote login), a home directory (for VirtualBox settings and virtual machines configuration) and a shell (for RemoteBox to be able to login). The rest of this page assumes a  user with primary group .

The provided service file  serves as a template that can be custimized with a drop-in file as follows:

Logging can be enabled by editing the  line in the override file above to include the  directive. For increased verbosity you can also include the  directive. Make sure the vbox user has permissions to write to the configured log file location.

The  directive can be changed to localhost or the hostname to only bind the service locally, or be set to an IP of a single chosen interface. An alternative port from the default 18083 can be set with .

You also need to create a tmpfile rule for 's PID file:

To test  immediately you need to first manually create the  directory:

 # mkdir /run/vboxwebsrv
 # chown vbox:vboxusers /run/vboxwebsrv
 # chmod 755 /run/vboxwebsrv

Now the  can be started and/or enabled.

## Connecting RemoteBox to vboxwebsrv
Open RemoteBox and click the Connect button. Specify the following:

 URL: http:'''':18083
 Username: vbox
 Password: ''''

To make it easier connecting during future sessions, after login go to File > Connection Profiles and create a new connection profile.

## Troubleshooting
If you encounter a login problem connecting to the server, first check that the service is running. From the server console, check  unit status.

It should output that it is running. If not, check logging with journalctl and, if you configured , the 's log file for any leads.

Even with increased verbosity the VirtualBox web service might not give you any useful leads. In that case you can try to run the server manually as vbox from the command line with su or sudo.

 /usr/bin/vboxwebsrv --pidfile /run/vboxwebsrv/vboxwebsrv.pid --host 0.0.0.0

Omit the  and  directives. If the service starts, the problem could be permissions to the log file. Leave it running and check if you can connect with RemoteBox from the client. Also check the  directory gets created and populated with configuration and/or log files.

If you still cannot connect, you can stop the service with  and start it with the  directive. Next, using  or similar check whether  is listening on port 18083. If you see a different port you can try connecting with RemoteBox on that port instead.

Another reason could be a firewall, either on your server, or even on your client.

If you are getting the following error message:
 vboxwebsrv: error: failed to initialize COM! hrc=NS_ERROR_FAILURE

Check that your home directory is writable for the user vbox.
