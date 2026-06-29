# Xpra

From Xpra's README:

: Xpra is known as "screen for X" : its seamless mode allows you to run X11 programs, usually on a remote host, direct their display to your local machine, and then to disconnect from these programs and reconnect from the same or another machine(s), without losing any state. Effectively giving you remote access to individual graphical applications. It can also be used to access existing desktop sessions and start remote desktop sessions.
: Xpra is open-source (GPLv2+) with clients available for many supported platforms and the server includes a built-in HTML5 client. Xpra is usable over a wide variety of network protocols and does its best to adapt to any network conditions.

## Installation
Install the  package on the server and the clients.

## Usage
## Run application "single shot"
To run an application remotely over SSH without starting an xpra server on the host it is running on in advance, you can simply use this command on your client machine:
 $ xpra seamless ssh://user@host "command"
or the old way
 $ xpra start ssh://user@host --exit-with-children --start-child="command"

Where "command" is the command you would start on the remote hosts shell. This will start xpra remotely and shuts down the xpra server when the command exits.

If you see , try to use your normal system ssh client instead of the integrated Paramiko SSH client:

 $ xpra start --ssh="ssh" ssh://user@host --exit-with-children --start-child="command"

## Run applications in a persistent xpra server on the remote host
If you want to have a persistent server on the remote machine, you can start an xpra server on the machine where you want to run the applications (we are using display number 7 here):

 $ xpra start :7

Now you can start an application, e.g. firefox:

 $ DISPLAY=:7 firefox

Or, if you want to start a screen session and execute the programs from there to be able to close the console:

 $ DISPLAY=:7 screen
 starts
 $ firefox

Note that if you start  like this you do not have to specify the display number when executing programs. They will be running on the xpra display automatically.

After running these commands, you do not see any windows yet. To actually see the applications on your display, you have to connect to the xpra server. If you are connecting to an xpra display on the same machine, start the xpra client like this:

 $ xpra attach :7

Or, if you are connecting to a remote machine over ssh:

 $ xpra attach ssh://user@example.com/7

After starting the client, any programs running on the remote server display are displayed on your local screen. To detach, type  or use the command:

 $ xpra detach ssh://user@example.com/7

Programs continue to run on the server and you can reattach again later.

You can stop the server with:

 $ xpra stop :7

on the machine where the server is running, or remotely:

 $ xpra stop ssh://user@example.com/7

## Run whole desktop environment
To run whole desktop (on the server side):

 $ xpra start-desktop :7 --start-child=xfce4-session --exit-with-children

where:
*  is a number of xorg DISPLAY session
*  run xfce4 session as child on xpra server
*  mean that server will be closed after session logout (children exit)

To attach it (on the server side):

 $ xpra attach :7

To attach it (on the client side):

 $ xpra attach ssh://user@example.com/7

To detach press ctrl+c on terminal or run:

 $ xpra detach :7

## Shadow remote desktop
To clone:
* display must be auth by this same user as ssh login to
* display must be shown on remote screen

To shadow desktop run this on the client side:

 $ xpra shadow ssh://DISPLAY_user@example.com/DISPLAY_number

## As xorg sandbox
Sandboxing can be achieved with firejail:

* for application sandbox (change  to your interface name or to ):
* xpra attach, etc:

## More
For a complete manual, see .

## Tips and tricks
## Start at boot
## Server
It is possible to start the xpra server at boot using a systemd unit.

Create the unit file:

{{hc|/etc/systemd/system/xpra@.service|2=
Description=xpra display

[Service
Type=simple
User=%i
EnvironmentFile=/etc/conf.d/xpra
ExecStart=/usr/bin/xpra --no-daemon start ${%i}

WantedBy=multi-user.target
}}

Now create the configuration, adding a line for each username you want to have an xpra display:

Enable the service for each username that owns a display. In this example, the service would be .

## Client
## Method 1: .xinitrc
Add to your  file the line necessary to start the connection, adding an & at the end of the line.

Make sure to add such line before the  line.

For example, on a remote client it could be:

## Method 2: systemd user session
Configure your session to use systemd user session. Read Systemd/User for details.

Create the following service unit:

Create the configuration file, using the options you want:

The service name would be in the format of .

Example:

Enable that service as a user unit.

## Troubleshooting
## Error: Only console users are allowed to run the X server
If the execution fails with this error message in the log file you need to make the following changes:

Create the following:

## Error: failed to connect to display :100
Sometimes this errors are produced:

To solve it is necessary run with . Example:

 $ xpra start ssh://$USER@$SERVER/100 --start-child=/usr/bin/terminator --xvfb=/usr/bin/Xorg
