# TigerVNC

TigerVNC is an implementation of the Virtual Network Computing (VNC) protocol. This article focuses on the server functionality.

## Installation
Install the  package.

## Running vncserver for virtual (headless) sessions
## Initial setup
For a quick start, see the steps below.  Users are encouraged to read  for the complete list of configuration options.

# Create a password using  which will store the hashed password in . Ensure the file's permission is set to . If creating vncserver access for another user, you must be logged in as that user before running vncpasswd.
# Edit  to define user mappings.  Each user defined in this file will have a corresponding port on which its session will run.  The number in the file corresponds to a TCP port.  By default, :1 is TCP port 5901 (5900+1).  If another parallel server is needed, a second instance can then run on the next highest, free port, i.e 5902 (5900+2).
# Create  and at a minimum, define the type of session desired with a line like  where foo corresponds to whichever desktop environment is to run.  One can see which desktop environments are available on the system by seeing their corresponding .desktop files within . For example:

## Starting and stopping tigervnc
Start an instance of the  template and optionally enable it to run at boot time/shutdown. Note that the instance identifier in this case is the display number (e.g. instance  for display number ).

## Expose the local display directly
TigerVNC includes , which can be seamlessly loaded during X initialization for enhanced performance. To utilize this feature, create the following file and then restart X:

## Running x0vncserver to directly control the local display
 also provides  which allows direct control over a physical X session. After defining a session password using the vncpasswd tool, invoke the server like so:

 $ x0vncserver -rfbauth $XDG_CONFIG_HOME/tigervnc/passwd

## With xprofile
A simple way to start x0vncserver is adding a line in one of the xprofile files such as:

## With systemd
## With a system service
This option will allow the users to access the current display, including the login screen provided by the display manager.

The service will be relaunched automatically every time an user logs off of their session.

LightDM is used for the example below, but it should be possible to adapt it to other display managers by modifying the  variable.

As this is a system unit,  refers to

Start/enable .

## With a user service
In order to have a VNC Server running x0vncserver, which is the easiest way for most users to quickly have remote access to the current desktop, create a systemd unit as follows replacing the user and the options with the desired ones:

The  line waits for Xorg to be started by {{ic|${USER}}}.

To login with a specific username and password, replace  by {{ic|1=/usr/bin/x0vncserver -PAMService=login -PlainUsers=${USER} -SecurityTypes=TLSPlain}}.

Start/enable the  user unit.

## Running Xvnc with XDMCP for on demand sessions
One can use systemd socket activation in combination with XDMCP to automatically spawn VNC servers for each user who attempts to login, so there is no need to set up one server/port per user. This setup uses the display manager to authenticate users and login, so there is no need for VNC passwords. The downside is that users cannot leave a session running on the server and reconnect to it later.

To get this running, first set up XDMCP and make sure the display manager is running.
Then create:

Start/enable . Now, any number of users can get unique desktops by connecting to port 5900.

If the VNC server is exposed to the internet, add the  option to  in  (note that  and  are different switches) and follow #Accessing vncserver via SSH tunnels. Since we only select a user after connecting, the VNC server runs as user nobody and uses  directly instead of the  script, so any options in  are ignored. Optionally, autostart vncconfig so that the clipboard works (vncconfig exits immediately in non-VNC sessions). One way is to create:

## Connecting to vncserver
Any number of clients can connect to a vncserver.  A simple example is given below where vncserver is running on 10.1.10.2 port 5901, or :1 in shorthand notation:
 $ vncviewer 10.1.10.2:1

## Passwordless authentication
The  switch enables one to specify the location of the server's  file. This file is expected to be accessible to the user through SSH or physical access to the server. In either case, place the file on the client's file system in a safe location, i.e. one in which only the intended user has read access.

 $ vncviewer -passwd /path/to/server-passwd-file

The password can also be provided directly.

 $ vncviewer -passwd  remote'' option.

## No window decoration / borders / titlebars / cannot move windows around
Start a window manager to fix an empty xterm frame. For example, on Xfce, run .

## Desktop environment is displaying only boxes for font
Some desktop environments might be missing necessary font to display ASCII characters. Install .

## VNC server terminates immediately while using xfce4 session
Create a new .desktop file under . For example:

Make sure the  key is using  to start xfce4 within new session bus instance context. Remember to change  value in  to .
