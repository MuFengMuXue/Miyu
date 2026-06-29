# FreeNX

FreeNX, German text, is a system that allows you to access your desktop from another computer over the Internet. The program is open source, secure (SSH based), fast and versatile. License: GPL. It was the non-commercial version of NoMachine, which has meanwhile switched to closed source. A good FreeNX alternative is X2Go.

## Installation
Get FreeNX/Nomachine from  or . Both server and client packages are included in the package.
The sshd daemon (available in openssh package) must be installed and running for it to function properly.

## Configuration
## Server
## SSHD
For freenx authentication to work, sshd has to be setup properly.
You need to allow RSAauthentication, Password Authentication, and you also need to include nx public keys to Authorizedkeysfile.

If you do not want to allow password login globally, add match block at the end of file like below: :
 RSAAuthentication yes
 PubkeyAuthentication yes
 PasswordAuthentication no
 PermitEmptyPasswords yes
 AuthorizedKeysFile /usr/NX/home/nx/.ssh/authorized_keys /usr/NX/home/nx/.ssh/authorized_keys2
 #
 #
 #
 Match Address 127.0.0.1
   PasswordAuthentication yes

## Main configuration
The main configuration file is located at .

If you are running your SSH daemon on a port other than the default port 22, you will need to uncomment and update:

If you use KDE or GNOME desktop environments you do not need to edit this file, as the defaults with the modified MD5SUM command should work in this case.  If you use another window manager such as Fluxbox/Openbox or Xfce, you may need to edit this file slightly (see below).

Or if you are not using CDE but Xfce you could simply edit CDE line like below and start cde from the client:
 CommandStartCDE = "/usr/bin/startxfce4"

For an overview of the install and uninstall procedures, run the following after installing :

## Keys
Keys are used to authenticate the clients with the server by default. You could used the default key created during installation or you could create a new pair.
If you create your own key pair, make sure you add the directory of the public key to authorizedkeyfiles in sshd_config and also SSHAuthorizedKeys in node.cfg. And Do not forget to send the private key to the client.

The public key can be found here check :
 /usr/NX/home/nx/.ssh/authorized_keys2
The private key can be found here:
 /usr/NX/share/keys/server.id_dsa.key

Recreation of random keys:

 /usr/NX/bin/nxserver --keygen

You can check if the nxserver is running by:

 /usr/NX/bin/nxserver --status

You can also check if a desired user can be logged on by:

 /usr/NX/bin/nxserver --usercheck USERNAME

## Starting the server
As of installation nxserver is set to start up automatically, however, you are likely to need to restart the server after setting up:

 /usr/NX/bin/nxserver --restart

## Client
For Arch Linux the client was chosen in #Installation.

## Windows
Get the client from nomachine's homepage: https://www.nomachine.com.

## Configuration
As mentioned above, the client must contain the correct key to connect to the server.  If you are using the custom keys generated during install, you need to copy the client key to the following locations:
* Windows:
* Arch Linux:

After moving the keys you may have use the nxclient GUI to import the new keys.  From the configuration dialog press the 'Key...' button and import the new client key.

## Running
After installing nxclient on Arch Linux, executables are available in  symlinked to . At the first run of , the user will be led through a wizard.

## Keyboard shortcuts
{| class="wikitable"
! Keyboard Shortcut
! Description
|-
|
| Toggles full-screen mode.
|-
|
| Shows the terminate, suspend dialog.
|-
|
| Maximizes or minimizes the window.
|-
|
| Drags the viewport, so you can view different portions of the desktop.
|-
|
| Moves the viewport by an incremental amount of pixels.
|-
|
| Activates "screen-scraping" mode, so all the GetImage originated by the clients will be forwarded to the real display.
By pressing the sequence again, nxagent will revert to the usual "fast" mode.
|-
|
| lazy image encoding
|-
|
| Emergency-exit and kill-window
|}

## Leaving fullscreen
There is a magic-pixel in the top right corner of nearly every nx-application
in fullscreenmode. Left-click the pixel and application-window gets iconified.

## Tips on resume
* Resume is a bit experimental, crashes might appear after session has resumed. You have to find out which applications like resuming and which do not ;) .
* Resuming between Linux and Windows sessions does not work. UPDATE: It appears that version 3.2.0-14 is able to resume Windows-suspended sessions.
* If resume fails let it time out and do not use the cancel button, else sessions will stay open and consume RAM on server. To kill such sessions use the Session Admin program to kill them.

## Fix DPI settings
If you like to have the same font-sizes/dpi sizes on all your client session, set the X resource . For example putting the following line into a user's  makes their "desktop" a 100dpi.
 Xft.dpi: 100

## FreeNX to existing display
Usually, when connecting to a NX server, a new X session is created. Sometimes it might be useful, to connect to an existing X session, e.g. the root session. This is not possible with NX in default setup, but can be reached, using  and . Install them on the NX server system.

x11vnc will serve the X session, we have to create a file  to give x11vnc some options, e.g.:

 display :0
 shared
 forever
 localhost
 rfbauth /home/user/.x11vnc/passwd

Create the VNC password file:

 $ mkdir $HOME/.x11vnc
 $ x11vnc -storepasswd PASSWORD $HOME/.x11vnc/passwd
 $ chmod 600 $HOME/.x11vnc/passwd

Create a shell script, which starts the x11vnc service, if not running and starts the vncviewer provided by the package tightvnc.

{{bc|
#!/bin/sh
VNC_VIEWER=vncviewer
VNC_SERVER=x11vnc
VNC_RESOLUTION=1024x786
VNC_PASSWD=/home/USER/.x11vnc/passwd
VNC_PORT=5900

if [ -z "$(pgrep ${VNC_SERVER})" ]; then
	echo $VNC_SERVER not running, starting...
	exec $VNC_SERVER &
	sleep 5
fi

exec $VNC_VIEWER -geometry $VNC_RESOLUTION -passwd $VNC_PASSWD localhost::$VNC_PORT
}}

Save this script with a texteditor of your choice, e.g. under . Make it executable and create a symbolic link, e.g:

 $ chmod +x $HOME/shell/nxvnc.sh
 # ln -s /home/USER/shell/nxvnc.sh /usr/local/bin/nxvnc

At this point, you might want to test the current configuration:
 $ /usr/local/bin/nxvnc

If the x11vnc service and a vncviewer session is started, you configuration works well. You are now able to connect to the current X session using your NX client with following options:

You are able to connect to your current X session via NX client now.

: — FreeNX to existing display (opensuse.org)

## Setting up non-KDE or GNOME desktop managers
Before following anything in this part, make sure the server working setup and accepting connections. This section only deals with problems once NXClient has logged on.

It is quite simple (once the server is setup) to connect to GNOME and KDE sessions, however connecting to other window managers (Fluxbox, Xfce, whatever) is slightly different.

Choosing "custom" and using a command like startx of startfluxbox will either result in a blank screen after the !M logo or the Client to present an error complaining about lack of a X server. A way around this is open a session with the command "startx", and the another with the command to start your window-manager-of-choice.

If you do not want to do this, you can start X by installing a login manager like SLIM or XDM. I would recommend using SLiM because of its small size.

(Authors note: This is how I got fluxbox, xfce and others to work on my arch installation- however, I have now removed slim from inittab and set the run level back to 3, and yet I can still login perfectly with NXClient. Possibly try this if you get your system working this way, if like me you have a low memory machine.)

## Alternative fix
A simple fix without resorting to the above seems to involve a simple edit to the configuration file.  This should work for Fluxbox/Openbox/XFCE or any other window manager that uses the  startup file in a call to startx.

Simply edit the configuration file  as root and change:
 #USER_X_STARTUP_SCRIPT=.Xclients
to:
 USER_X_STARTUP_SCRIPT=.xinitrc
Remember to remove the # symbol from the start of the line.

Then in the client under configuration settings, choose Custom as the desktop, and click on settings:
* In the first group select -  '
* In the second group select - '

## Problems
## Keyboard Mapping problems
Keyboard layout aways falls back to en_US.

After login, run setxkbmap with your layout.

Example:

  $ setxkbmap -layout br

or create the file

  # touch /usr/share/X11/xkb/keymap.dir

Creating this file will fix the issue for the next logins.

## Debug problems
Edit the nxserver configuration file  and change:

  #SESSION_LOG_CLEAN=1

to

  SESSION_LOG_CLEAN=0

Then you can look/debug the log files in:

  $HOME/.nx/T-C-hostname-display-session-id
For succesfull connections and:

  $HOME/.nx/F-C-hostname-display-session-id
For failed ones.

## Authentication OK, but connection fails
If you are trying to start KDE edit  and search for:

  COMMAND_START_KDE=startkde

Replace for:

  COMMAND_START_KDE=/usr/bin/startkde

## Key changes
Change the key in GUI setup to new generated key.

## Wrong password / No connection possible / Key-based authentication
* If you have changed your ssh daemon to run on an alternate port, be sure to modify SSHD_PORT within /etc/nxserver/node.conf.

* If you get always wrong password or no connection after authentication was done and you are sure that you typed it correct, check that your server can connect to itself using localhost by ssh.

* If you messed up your key files, create new ones or fix the old ones, it is probably caused by a wrong known_hosts file.

* If you get wrong password or login, put ENABLE_PASSDB_AUTHENTICATION="1" in  and add a user by
 # /usr/bin/nxserver --adduser # /usr/bin/nxserver --passwd [username

* The above commands are also necessary if you have disabled password authentication in ssh and instead are using key-based authentication.

## NX crashes on session startup
If your NX Client shows the NX logo then disappears with a Connection Problem dialog afterwards.

## NX logo then blank screen
If you see the NX logo (!M) then a blank screen.

This problem can be solved by running a login manager- The problem is that X11 is not started, and it appears that "startx" or similar do not work from the freenx client.
Follow these instructions to setup a login manager and load it at startup: Display manager

Blind: If this does not resolve your issues, be aware that freenx and bash_completion do not play well together. I only got things to work after removing bash_completion from the .bashrc.

## GDM/XDM Session Menu Error with non-KDE or GNOME Desktop Managers (more common with non-Arch Linux users)
Problem: A session menu comes up talking about "chooseSessionListWidget." A window manager never loads.

Double check to see if .xinitrc is executable, if not make it so:

 stat -c "%A" ~/.xinitrc

Keep in mind this command should be executed along with pertinent instructions on this page about setting up non-KDE or GNOME desktop managers.

## Cannot connect because command sessreg not found
If you get the following error while connecting:

  /usr/bin/nxserver: line 941: sessreg: command not found
  NX> 280 Exiting on signal: 15

then you have to install the package .

## Broken resume with Cairo 1.12.x
Latest cairo updates broke the render extension. After resuming a session all characters from before suspending will not get rendered. To fix this add this single line to  .

  AGENT_EXTRA_OPTIONS_X="-norender"

## Eclipse crashes when editing a file
 The program 'Eclipse' received an X Window System error.
 This probably reflects a bug in the program.
 The error was 'BadValue (integer parameter out of range for operation)'.
 (Details: serial 8414 error_code 2 request_code 149 minor_code 26)

Start eclipse using (see https://bugs.eclipse.org/bugs/show_bug.cgi?id=386955):
 $ eclipse -vmargs -Dorg.eclipse.swt.internal.gtk.cairoGraphics=false
