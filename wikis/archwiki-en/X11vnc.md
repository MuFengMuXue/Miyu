# X11vnc

x11vnc is a VNC server, it allows remote access, view and control of real X displays (i.e. a display corresponding to a physical monitor, keyboard, and mouse) with any VNC viewer. While it is not developed any longer by its original author Karl Runge, LibVNC and x11vnc's community on GitHub have taken over the development.

x11vnc, unlike xvnc of TigerVNC, by default, connects to an existing X display. However, one can use  option to launch and connect to a new headless (virtual) X server.

Also note that x11vnc is not shipped with a VNC client (VNC viewer). Any VNC viewer should do the job and be compatible with the x11vnc server while not necessarily using all its functionalities. TigerVNC's vncviewer is a recommended client.

## Installation
Install the  package.

## Usage
First, start an X display, either by startx or through a display manager. You can also use a headless X display too.

Then, run the following command, all available options are explained in .
 $ x11vnc

By default, x11vnc tries to connect to the X display provided by  option, or environment's  variable's value otherwise, or to the :0 display if neither of the earlier are provided.

 $ x11vnc -display :1

Another option is to place the x11vnc command line in a script which is called at login, for example:

 x11vnc -wait 50 -noxdamage -passwd PASSWORD -display :0 -forever -o /var/log/x11vnc.log -bg

 option sets the time in milliseconds to pause between each poll from the X server's frame buffer.

 option disables X Damage extension. See #Session closes unexpectedly.

 option keeps x11vnc server up, listening for further client connection, even after the first client disconnected. See #Persistent x11vnc server.

## Setting a password
x11vnc provides many options to set and manage authentication passwords; a few of them are described in this section. Read  manpage to find and read about all of them.

 option is used as the general purpose password flag:

 $ x11vnc -usepw

It uses the password found in , where the password is obscured with a fixed key in a VNC compatible format, otherwise passwords found in . If none of these files can be located, it prompts the user for a password, which is saved in  and is used right away.

The VNC viewer should then prompt for a password when connecting.

,  and  options allow one to see, use or set the RFB's authentication password, respectively.

 option can be used to provide a LibVNCServer password file which allows one to set multiple passwords and also passwords for view only connections.

## Port setting
By default, x11vnc searches for the first free port from 5900 and use it for both IPv4 and IPv6 VNC connections, despite what is the X display number it's connected to.

 argument, sets port 5900 plus the number of display. For example:

 $ x11vnc -display :3 -N

That will result to using port number 5903 for this VNC server.

 argument, sets port to the first free port from number n.

 argument can be used to set the VNC port explicitly to n.

In all three cases above, an additional port with the same number will be used for IPv6 connections; aside a 5900 IPv6 port, which also will be used if free. So you will end up with three open ports for that x11vnc server, one for IPv4 and two for IPv6. For example:

 $ x11vnc -display :2 -rfbport 5905

That will connect to X server of display number 2 and listen to IPv4 port 5905 and IPv6 ports 5905 and 5900 for VNC client connections.

For setting IPv6 port directly, use  option.

## Passing X authority file
For a x11vnc server to connect to an X display server, it needs to access the display’s X authority file, authorising itself.

To pass on the target display’s X authority file to the x11vnc server, you can set  environment variable to the appropriate file path before calling x11vnc command or through  option:

 $ x11vnc -display :0 -env XAUTHORITY=/home/user/.Xauthority

Where user is the username of the user who is running the X server.

You also can use the  argument following with X authority file address:

 $ x11vnc -display :0 -auth ~/.Xauthority

Alternatively, you can use  option, which will try to guess the XAUTHORITY filename for the target X display and use it:

 $ x11vnc -display :1 -auth guess

Generally, if the desired X display is not launched by your current user, accessing its X authority file requires running x11vnc as root or as the user who has the permission of reading X authority file of the target X display:

 # x11vnc -display :1 -auth /home/user/.Xauthority

## Running from xinetd
X11vnc can be run using a xinetd service, which only starts X11vnc once a user connects.

Create an xinetd service entry for x11vnc, for example:

{{hc|/etc/xinetd/x11vnc|
service x11vncservice
{
       port            = 5900
       type            = UNLISTED
       socket_type     = stream
       protocol        = tcp
       wait            = no
       user            = root
       server          = /usr/bin/x11vnc
       server_args     = -inetd -o /var/log/x11vnc.log -noxdamage -display :0 -auth guess
       disable         = no
}
}}

After reloading , X11vnc will start once a client connects to port 5900.

## As a systemd service
To run x11vnc when system boots, use a drop-in unit file for . The content should be like the following

Replace the second ExecStart with the command you run interactively. Enable  if needed.

## Starting with display managers
A typical use case is to start x11vnc server for the login session itself before any user has logged into an X session.
Display managers usually put their X authorisation files in directories not accessible by regular users, launching x11vnc with root privileges necessary.

## Automatic discovery of display manager's X authority file
x11vnc command tries to find the current display manager's X authority file when it's provided with  option and environment's  variable is bound to :

 $ x11vnc -find -env FD_XDM=1 -auth guess

## GDM
 # x11vnc -display :0 -auth /var/lib/gdm/:0.Xauth

Newer versions of GDM uses /run/user. Example for user 120 (gdm), used for login screen.

 # x11vnc -display :0 -auth /run/user/120/gdm/Xauthority

or see Troubleshooting section below

## LightDM
Running in bash:

 # x11vnc -display :0 -auth /var/run/lightdm/root/\:0

## LXDM
 # x11vnc -display :0 -auth /var/run/lxdm/lxdm-\:0.auth

## SDDM
SDDM uses an unpredictable UUID for the auth file therefore one needs to:

 # x11vnc -display :0 -auth $(find /var/run/sddm/ -type f)

Embedding this into a systemd .service file will require a trick to evaluate the find command as shown here [https://gist.github.com/nickjacob/9909574.

If the above method does not work, an alternative is to start x11vnc when SDDM runs the Xsetup script. To do this, add the following line into :

 /usr/bin/x11vnc -auth /var/run/sddm/* -display :0 >/dev/null 2>&1 &

## SLIM
 # x11vnc -display :0 -auth /var/run/slim.auth

## Persistent x11vnc server
By default, x11vnc terminates upon client's (VNC viewer's) disconnection and/or X server's termination. However, There are a few ways to keep up x11vnc server in such situations.

 or  arguments specify that x11vnc do not terminate after viewer's disconnection and wait for further possible connections, with no timeouts. Next connection requests can be from the same or any other client:

 $ x11vnc -many

However, display's termination by any mean still terminates x11vnc.

 flag, creates a loop that tries to start x11vnc server up again after it terminated for any reason. By default, this will keep trying every two seconds indefinitely.

 $ x11vnc -loop

Retry times and frequency can be adjusted as follows:

 $ x11vnc -loop5000,5

This will effectively make the server to restart after its termination for 5 times, each 5 seconds, until it's established; reconnecting to a display server and VNC client.

One can combine both  and  flags; making x11vnc server to do not stop by client's disconnection at all, and also restart if the X display is terminated until an X server with the same display number and X authority file is up again.

 $ x11vnc -display :1 -forever -loop5000

## View-only connection
By default, VNC clients can both view and also control X desktops they are connected to.  make current server view-only so that VNC viewers only can watch desktop and not interact with it.

## Multicat DNS broadcasting
Many VNC clients have the ability to discover zeroconf VNC servers advertised on their local networks.

To advertise a VNC server with zeroconf protocol start it with  or  or  options. These three options are aliases. For example:

 $ x11vnc -display :0 -mdns

You also need to have your Avahi or mDNS daemon running, and your port 5353 of UDP open which depends on your firewall configuration.

## Sharing standalone X windows
Instead of sharing an entire X display with clients, x11vnc can connect to an X server to only poll a window of that X display. This is specially usefull with  option.

To do so start x11vnc with  or  options; where id denotes the ID of an X window which can be acquired using .  parameter can be used instead, which will make x11vnc call  directely and then extract the ID of the chosen X window, interactively. For example:

 $ x11vnc -id pick

 option will poll an X window directly, which will omit new windows open by that windows; popups menus and transient toplevels may not be seen. In contrast,  option will shift a root view to that window, which resolves that problem.

Note, closing the X window that x11vnc server is connected to terminates x11vnc.

## Accessing
Get a VNC client on another computer, and type in the IP address of the computer running x11vnc. Hit connect, and you should be set.

If you are attempting to access a VNC server / computer (running x11vnc) from outside of its network then you will need to ensure that it has port 5900 forwarded.

## SSH tunnel
You need to have SSH installed and configured.

Use the  flag with x11vnc for it to bind to the local interface. Once that is done, you can use SSH to tunnel the port; then, connect to VNC through SSH.

Simple example (from http://www.karlrunge.com/x11vnc/index.html#tunnelling):

 $ ssh -t -L 5900:localhost:5900 remote_host 'x11vnc -localhost -display :0'

(You will likely have to provide passwords/passphrases to login from your current location into your remote_host Unix account; we assume you have a login account on remote_host and it is running the SSH server)

And then in another terminal window on your current machine run the command:

 $ vncviewer -PreferredEncoding=ZRLE localhost:0

## Troubleshooting
1. You can check your ip address and make sure port 5900 is forwarded by visiting this website.

2. Tested only on GNOME + GDM

If you cannot start the tunnel, and get error like XOpenDisplay(":0") failed,
Check if you have a  directory.
If that does not exist, You can create one easily (Actually a symlink to actual one) by running command given below as normal user NOT ROOT OR USING Sudo as below:

 $ ln -sv $(dirname $(xauth info | awk '/Authority file/{print $3}')) ~/.Xauthority

then try above tunneling example and it should work fine.
Further if you want this to be automatically done each time Xorg is restarted, create the xprofile file & make is executable as below

 $ ln -sf $(dirname $(xauth info | awk '/Authority file/{print $3}')) ~/.Xauthority

3. GNOME 3 and x11vnc

If you are using GNOME 3 and x11vnc and you get the following errors

 *** XOpenDisplay failed (:0)

 *** x11vnc was unable to open the X DISPLAY: ":0", it cannot continue.

Try running x11vnc like

 $ x11vnc -noxdamage -many -display :0 -auth /var/run/gdm/$(sudo ls /var/run/gdm | grep $(whoami))/database -forever -bg

Please update if this works / not works for any other display manager or desktop environment.

## Screensaver problem
If screensaver starts every 1-2 second, start x11vnc with  key.

## IPv6 port different from IPv4 port
The default behavior for the command:
 $ x11vnc -display :0 -rfbport 5908
is for the server to listen to TCP port 5908 and TCP6 port 5900.
For the server to listen to the same TCP6 port, also use the  option to force the IPv6 listening port.
For example:
 $ x11vnc -display :0 -rfbport 5908 -rfbportv6 5908

## Copying and Pasting
If copying and pasting does not work as expected, particularly if pasting to the
remote side is not working or clipboard behaviour is not as expected, try adding
:

 $ x11vnc -xkb -display :0

Although the documentation does not indicate  specifically for
clipboard problems, it resolved an issue where vim complained that there was
nothing in the  register.

## Session closes unexpectedly
x11vnc enables the X Damage extension by default, which significantly reduces the load when the screen is not changing much and detects changed areas more quickly. This extension is known to cause issuesand it may cause the session to close unexpectedly with  messages appearing at the log. This issue can be circumvented by using the  option.

## Tips and tricks
## Run x11vnc "system-wide" in (GDM and GNOME Shell)
Perform the following steps to run x11vnc in GDM to log in and then run x11vnc in a GNOME shell user session for a "system-wide" x11vnc:

First we need to create a systemd service to launch an x11vnc server in GDM:

This will start an x11vnc server protected by the password stored at  that shows GDM to any connected VNC client, however as you may notice, if you click on any of the users, as soon as you log in, all the VNC clients will show a black screen. To fix this, we need to create another systemd service that will start another x11vnc server in the GNOME Shell session as soon as you log in:

Now, you need to keep the following in mind:

# As you may notice in the  part of the systemd service, the command that executes can be separated in two tasks: first it stops  (killing the GDM x11vnc server) and then it starts the x11vnc server for the user in the GNOME shell session. This is done because if you keep running the GDM x11vnc server in the background, the new x11vnc server for the user will use the next available port, and you would need to change your client connection settings to connect either to the GDM x11vnc server or for your user-specific x11vnc server. A setup like this is useful because the GDM x11vnc server stops as soon as you log in into your account.
# You need to create a service like this for each user that you want to have this functionality. (Do not forget to replace  and  with your actual username.)
# You may need to change the  part of the command to match your system settings. You can view your current display by running . Use the resulting output to match the systemd service.

Now, as you might notice,  is executed as your (probably) unprivileged user. This presents a problem if we want to stop the , so we need to allow the user to stop the GDM service. This can be accomplished using sudo, but we need to allow the execution of only that specific command without a password.

Edit the sudoers file to add:

 YOUR_USER ALL=(root) NOPASSWD: /usr/bin/systemctl stop x11vnc-gdm.service

Now you simply need to enable  and . When you restart your computer, both of them will start running and you can connect to your GDM and GNOME Shell using VNC.

## Run x11vnc "system-wide" in (SDDM and Plasma)
To run x11vnc when the system boots into SDDM (if the aforementioned methods do not work for you), just edit  as follows:

Remember to change  in the path, or use the preferred auth method. Disable the old  and reload the systemd manager configuration. Reenable the  unit afterwards. You may need to put the service to sleep for a while, otherwise it will not start properly.

## Change x11vnc password in each boot
A setup like this could be useful if you need to share your desktop with several people that you do not trust and if you do not want to manually change the password every time. Such a setup would generate boot-unique passwords, so if you share your password with someone, you only need to reboot your computer (or re-run the systemd service) to change the password.

The new generated password will be stored as plain text in , so it can be accessed with

 $ cat /home/$USER/.vnc/autovncpass

To accomplish this, perform the following steps:

First install the  package.

Then, create the following script anywhere in your home directory:

Now we need to create a systemd unit file that will execute the script at boot time:

Finally, start/enable the service to change the password. You can access the current password with

 $ cat /home/$USER/.vnc/autovncpass
