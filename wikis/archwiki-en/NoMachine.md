# NoMachine

NoMachine enables you to access a graphical desktop of a computer over the network.

Until version 3.x, NoMachine was known as NX and available under GPL. There are derivatives based on core NX libraries like FreeNX and X2Go. The major drawback of these is that they utilise a built-in X server of nxagent, which originates from the year 2005 and some current X applications cannot run due to unsupported features available only in newer versions of X libraries.

Unlike some other remote desktop solutions (e.g. TeamViewer), NoMachine does not require an intermediary server to establish the connection.

Since NoMachine version 4, the software is proprietary and currently two editions are available: Free and Enterprise. Clients exist for Linux, MS Windows, macOS, Android and iOS.

The free edition allows to connect to an existing X display (also known as display shadowing of a live session with a physical display) or, if no X display is available (e.g. on head-less machines), NoMachine tries to start its own X server with the default Desktop environment automatically. The major limitation of the free edition is that only a single remote desktop session may run on the server.

## Installation
Install the  package.

It includes both server and client tar balls. Note that the setup actually takes place by a post-installation script and therefore the list of files shown by command  is not complete!

In particular, the majority of NoMachine files are kept within  directory, but a few more are added:

 /etc/NX
 /etc/pam.d/nx
 /usr/lib/systemd/system/nxserver.service
 /usr/local/share/applications/NoMachine*.desktop
 /usr/share/polkit-1/actions/org.freedesktop.pkexec.nomachine.policy

The files created by NoMachine Player are stored in:

 $HOME/.nx
 $HOME/Documents/NoMachine

The post-install script also creates a new user .

If you have X2Go or FreeNX installed as well, do not get confused that some files use similar names (i.e. ).

The  does not need to be enabled and started on computers which will be used only as the client, but it must run on the server.

## Usage
On the target computer, start/enable  via systemd, or via menu in your desktop: Internet > NoMachine > NoMachine Service, which does the same via a GUI and offers extra info and configuration.

On the client, start the "Player" (menu Internet > NoMachine > NoMachine. Or start it with

 /usr/NX/bin/nxplayer

It will search the LAN for available NoMachine servers or, if disabled or in a different subnet/WAN, you can type in the target hostname or IP address manually. The login credentials are the same as used for the user on the target computer.

## Troubleshooting
## Headless server
Install the  package

For correct environment setup those changes are needed:

Change  in  and add the following in front of your starting command:

 env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus

Example for starting Xfce:

 DefaultDesktopCommand "env DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus /usr/bin/startxfce4"

## Separate NoMachine X session in parallel with existing X session
In default setup, the Free edition of NoMachine connects the client directly to an existing X session on the remote computer, even if it runs the X Display Manager only. This may be unwanted, because no other user may use the target computer locally at the same moment and because any person with physical access to the target computer can see on the physical display, what the remotely connected user is doing.

However, it is possible to setup NoMachine to check only for a particular DISPLAY, e.g.  and it will ignore the existing X session on  (standard setup in Arch Linux) and start a new virtual session for the remotely connecting user.

To do so, edit the key  in :

 PhysicalDisplays :10

## Problems with default keyboard in display manager
When NoMachine connects to the display manager on the target computer and the user tries to login as if sitting at the target computer, the user authentication may fail due to a different keymap. A workaround is to type the user's password e.g. in a text editor and copy it via clipboard to the NoMachine session.

Once the user is logged in to the remote desktop environment, running  ('cz' stands for the Czech keyboard as an example) should resolve the problem with key mappings.

## Connecting via SSH
The free edition of NoMachine does not allow to use the SSH protocol to connect to the target computer and only NX protocol (listening on port  by default) is used.

If it is not preferred to open yet another port on the firewall, a workaround is to create a standard SSH tunnel between client and target computer and connect through it:

On the client computer, for example:

 $ ssh -L 4000:localhost:4000 user@targetmachine -fN

Then, start NoMachine Player and try to connect to  with the NX protocol. The connection will be tunneled to the targetmachine and redirected to the server's localhost port .

## Virtualbox guest audio stream lost on reconnection
If using PulseAudio audio interface, nxserver will restart pulseaudio on client disconnection, virtualbox guest machine can not connect to the new pulseaudio automatically, thus audio stream lost. A workaround is to provide a dummy pulseaudio in your PATH for nxserver.

 $ ln -s /usr/bin/true /some/path/prior/to/usr/bin/pulseaudio
 $ which -a pulseaudio
 /some/path/prior/to/usr/bin/pulseaudio
 /usr/bin/pulseaudio
Then reinstall the  package to regenerate , and recheck the pulseaudio start command.
 $ grep -i pulse /usr/NX/etc/node.cfg
 AudioInterface pulseaudio
 CommandStartPulseAudio "/some/path/prior/to/usr/bin/pulseaudio --high-priority=no"
Finally restart .

## PackageKit keeps asking for authentication in discover after uninstalling nomachine
The  uninstaller leaves a polkit rules file behind, causing PackageKit to prompt for authentication every time it refreshes system repositories. To restore the previous behavior, you can manually remove this file after uninstalling NoMachine.

 # rm /usr/share/polkit-1/rules.d/55-org.nomachine.rules

## Graphical issues (especially with Wayland) after uninstalling NoMachine
See this forum post. NoMachine alters some permissions by means of files in /etc/udev/rules.d and /etc/X11/xorg.conf.d, but these don't get removed properly after uninstalling NoMachine. This leads to graphical issues under X, and not booting properly at all under Wayland (with errors like ). To solve this, remove the following directories and files:
 /etc/opt/VirtualGL
 /usr/share/gdm/greeter/autostart/virtualgl.desktop
 /etc/modprobe.d/virtualgl.conf
 /etc/udev/rules.d/99-virtualgl-dri.rules
 /etc/X11/xorg.conf.d/99-virtualgl-dri

Also remove the line regarding nomachine in the file .

## LD_PRELOAD issue after uninstalling NoMachine
NoMachine alters the configuration files of some display managers to configure LD_PRELOAD.
These configuration changes are not restored after uninstalling NoMachine.
This is indicated by a preload error after uninstalling NoMachine:

 ERROR: ld.so: object ‘/usr/NX/lib/libnxegl.so’ from LD_PRELOAD cannot be preloaded (cannot open shared object file): ignored

To solve this, uninstall NoMachine "as in the guide" or consider reinstalling your display manager.

If using KDE Plasma, you may be able to solve this by removing  if it is present and then logging out/in again, or rebooting.
