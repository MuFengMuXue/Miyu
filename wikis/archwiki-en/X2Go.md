# X2Go

X2Go enables to access a graphical desktop of a computer over the network. The protocol is tunneled through the Secure Shell protocol, so it is encrypted.

## Installation
Two parts are available. They can be installed with the following packages:

*  - X2Go server
*  - X2Go client based on Qt5

## Server side
## Configure Secure Shell daemon
X2Go uses Secure Shell in order to work, so you need to configure sshd daemon to allow X11 forwarding. Follow the instructions at OpenSSH#X11 forwarding and OpenSSH#Daemon management.

## Check fuse kernel module is loaded
In order for the server to be able to access files on the client computer, the fuse module is needed.
One can check that  returns a match, otherwise load the  kernel module.

## Setup SQLite database
Run the following command on the server to initialize the SQLite database (which is required in order for the x2go server to work):
 # x2godbadmin --createdb

## Control published applications
X2Go can publish the installed applications in a menu to the client.
This is controlled by the files in . This location however is not created by default and can be created by creating a symlink to .
Alternatively instead of creating a symlink one could also create a folder and link only the desired applications instead.

See for more information.

## Start X2Go server daemon
Now all you need to do is start the system .

## Client side
Run X2Go Client on the client computer, the one that wants to access the server:
 $ x2goclient
For the list of available options, see .

You can now create several sessions, which then appear on the right side and can be selected by a mouse click. Each entry consists of your username, hostname, IP, and port for SSH connection. Furthermore you can define several speed profiles (coming from modem up to LAN) and the desktop environment you want to start remotely.

## Access the local desktop
To access the local desktop, the one currently running on the server rather than a new one, one can choose the option "X2Go/X11 Desktop Sharing" or "Connection to local desktop" (depending on the version of your client) in "session type" in the X2Go Client as long as the users match, if it is user foo accessing the session of user foo.

However to access the local desktop of a different user, one needs to install  and launch .

## Exchange data between client and server (desktop)
On the X2Go client (e.g. laptop) local directories could be shared. The server will use fuse and SSHFS to access this directory and mount it to a subdirectory media of your home directory on the server. This enables you to have access to laptop data on your server or to exchange files. It is also possible to mount these shares automatically at each session start.

## Leave a session temporarily
Another special feature of X2Go is the possibility of suspending a session. This means you can leave a session on one client and reopen it even from another client at the same point. This can be used to start a session in the LAN and to reopen it later on a laptop. The session data are stored and administered in a SQLite database on the server in the meanwhile. The state of the sessions is protocolled by a process named x2gocleansessions.

## Troubleshooting
## The desktop environment does not start
## Local session prevents X2Go new session
It happens that when a desktop session already runs locally and X2Go tries to start a new one, it fails.
This is typically an issue related to D-Bus, see [https://bugzilla.redhat.com/show_bug.cgi?id=1350004 for details.

If D-Bus fails to start, try using a Custom desktop command instead of the default session type. For the command, use the desktop starter as an option of , for example . This is a way to launch a session bus instance, set the appropriate environment variables so that the new session can find the bus.

## Path issue
It may be that the desktop environment's executable, startkde, startgnome or startxfce4 is not in the  when logging in using SSH. In this case, do not simply choose the defaults of KDE, Gnome or XFCE but use the full paths to the executable, for example . You can also start openbox or another window manager.
You should be asked for your server's password and user name, now and after login you will see the X2Go logo for a short time, and the desktop.

## No selection screen in x2goclient
A regression in  causes ss to show no result when specifying the  flag, as done in . See [https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=799, for more information.

## Sessions do not logoff correctly
Due to [https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=914 this bug the X2Go sessions might not logoff correctly. The script that initiates the session spits out many log lines that might confuse X2go. A simple workarround is to create a custom session script and redirect the log output either to a file or to  and then point your X2Go-client to this custom script.

Here is a sample script for an XFCE session:

  #!/bin/sh
  #
  #xfce4-session spits out quite a bit of text during logout, which I guess
  #confuses x2go so we would get a black screen and session hang.
  #adding redirect to a logfile like "~/logfile" or "/dev/null" nicely solved it
  # see https://bugs.x2go.org/cgi-bin/bugreport.cgi?bug=914
  /usr/bin/xfce4-session > /dev/null

## Notification area disappeared
If you log in, but the notification area is missing, you can use exactly the same fix as for #Local session prevents X2Go new session.

## Shared folders do not mount (Windows Clients)
The ssh-daemon used by the X2go windows client uses depreceated ssh-dss keys by default and because Arch does not accept them your shared folders will not mount. Check out this bug report for more information.

This can be solved on the windows side by generating different type of key:

  C:\Program Files (x86)\x2goclient\ssh-keygen -b 2048 -t rsa

And simply replace  and  with the newly generated key files.

Other workarrounds from might help, too.

## Compositing window manager fails for remote session
When the computer running the x2goserver is also used for local sessions, compositing window managers fail to load through the remote connections with x2goclient, and an simpler window manager should be used instead. The following example uses Compiz and GNOME Flashback, but could be modified for other desktop environments.

Create a script to detect which window manager to use:

Then create a matching session file:

Create a corresponding desktop file:

You should now be able to connect remotely without issues.

## /bin/bash: No such file or directory when connect (or what ever shell you use)
In you ssh configuration, if you chroot a user, this user need to have their own /bin directory inside their chrooted directory. If not, you will not be able to connect.

## X2Go client: Cannot connect to remote X2Go server from local Wayland session: "The connection with the remote server was shut down"
X2Go client launches as expected from a local Wayland session but attempting to connect to a remote X2Go server fails. This problem is usually caused by Qt on Wayland.

Follow the instructions in Desktop entries#Modify environment variables and change the lines starting with

 Exec=x2goclient

to

 Exec=env QT_QPA_PLATFORM=xcb x2goclient

## X2Go client: Cannot connect to xyz:22 - Could not apply options
x2go client can not parse custom user ssh configuration files with tokens.

This ssh configuration

 Host xyz
     IdentitiesOnly yes
     IdentityFile %d/.ssh/%L.key

will result in connection failure with debug output:

 x2go-DEBUG-../src/sshmasterconnection.cpp:622> "Cannot connect to xyz:22" - "Couldn't apply options"

This ssh configuration works:

 Host xyz
     IdentitiesOnly yes
     IdentityFile ~/.ssh/mysupersecret.key

## X2Go server: localhost ssh tunnel on server fails with sshd error: error: connect_to localhost port xyz: failed.
X2Go server requires IPv4 for localhost ssh tunnel on the server. If you configure the sshd server to use IPv6 only

 AddressFamily inet6

X2Go client connections will fail.

## Performance issues
In case of performance issues (applications are unresponsive or freeze), try to turn off sound support, printing support and file share tunneling.

## Suspending sessions causes performance slowing down
In some cases, when the X2Go client starts a process in the server, if the X2Go session is suspended before the process ends, there is a drop in the server performance running the process. In this case add the option

 X2GO_NXOPTIONS="sleep=0"

to the  file. Reported in [https://www.mail-archive.com/x2go-user@lists.x2go.org/msg03855.html.
