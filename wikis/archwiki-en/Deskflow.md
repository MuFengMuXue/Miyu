# Deskflow

Deskflow lets you easily share a single mouse and keyboard between multiple computers (even with different operating systems) without the need for special hardware. It is intended for users with multiple computers on their desk since each system uses its own monitor(s).

Redirecting the mouse and keyboard is as simple as moving the mouse off the edge of your screen. Deskflow also merges the clipboards of all the systems into one, allowing cut-and-paste between systems.

Deskflow is the official upstream of Synergy. The Deskflow project was established to cultivate community-driven development where everyone can collaborate. Synergy sponsors the Deskflow project by contributing code and providing financial support.

## Forks
Historically, a fork called Barrier was created to remove serial key code from the Synergy source code. After disagreements within the project leadership, the active maintainers created a new fork called input-leap.

## Installation
## Deskflow
Install the  package.

Wayland: GNOME 46 or KDE 6.1+ is required for the input capture support.

## Input Leap or Barrier
You can install the  or  package.

## Synergy
Around June of 2023, Symless released Synergy 3 which is paid software. To install the latest version there is a user package .

Once installed, run the GUI to setup your configuration. Then enable/start the  user unit.

Now Synergy 3 will run without the GUI based on the configuration you setup. You can have the GUI open and the service will work along with it.

## Pre-configuration
First determine the IP addresses and host names for each machine and make sure each has a correct hosts file. (You may use IP addresses instead of hostnames as well.)

## Server configuration
In Synergy, the computer with keyboard and mouse you want to share is called the server. See Synergy Configuration File Format for a detailed description of all available sections and options.

## Arch Linux
Synergy stores its configuration under , Barrier uses  or . If the configuration file does not exist, you can use the provided GUI (started with  or , or the desktop launcher) to create it visually. Alternatively you may create it by copying  or , whose comments should give you enough information for a basic configuration; if you need further reference or would like to use more advanced options not available from the GUI, read the guide mentioned above.

If you experience problems and you wish to run the server in the foreground, you can run the following command instead:

 # synergys -f

The synergy server process needs to attach to your user's X session, which means it needs to run as your user. Enable the  user unit.

## Set up encryption on server
To generate a certificate and fingerprint for the server to use.

For Barrier:

Note: Barrier v2.4.0 introduced a new keyfile format, which requires a SHA256 fingerprint and "v2:sha256:$fingerprint" formatted lines. For older versions, make sure the fingerprints are SHA1 and do not include a prefix.

 $ mkdir -p ~/.local/share/barrier/SSL/Fingerprints;
 $ openssl req -x509 -nodes -days 365 -subj /CN=Barrier -newkey rsa:4096 -keyout ~/.local/share/barrier/SSL/Barrier.pem -out ~/.local/share/barrier/SSL/Barrier.pem;
 $ fingerprint=$(openssl x509 -fingerprint -sha256 -noout -in ~/.local/share/barrier/SSL/Barrier.pem | cut -d"=" -f2);
 $ echo "v2:sha256:$fingerprint" > ~/.local/share/barrier/SSL/Fingerprints/Local.txt;

For Synergy:

 $ mkdir -p ~/.synergy/SSL/Fingerprints;
 $ openssl req -x509 -nodes -days 365 -subj /CN=Synergy -newkey rsa:4096 -keyout ~/.synergy/SSL/Synergy.pem -out ~/.synergy/SSL/Synergy.pem;
 $ fingerprint=$(openssl x509 -fingerprint -sha1 -noout -in ~/.synergy/SSL/Synergy.pem | cut -d"=" -f2);
 $ echo "$fingerprint" > ~/.synergy/SSL/Fingerprints/Local.txt;

To activate the SSL plugin, add the  option. (Note that the Synergy GUI will not let you enable encryption without a valid license, whereas the Barrier GUI allows doing so.)

* Starting from the command line:
 $ synergys --enable-crypto

* Start the  user unit

## Windows
# Open the Synergy program
# Select the option Server (share this computer's mouse and keyboard)
# Select Configure interactively
# Click the Configure Server... button
# This opens a window in which you can add screens depending on how many computers/screens you have: just drag the screen icon in the top-right corner to the screens area, and double-click it to edit its settings
# Click OK to close the screens window when you are ready, then click on Start to start the server

On Windows, configuration is saved by default in a  file, but its name and location can of course be changed at pleasure.

If you want to start the Synergy server everytime Windows starts, you have to launch the program as administrator, then go to Edit -> Services and select Install in the Server section; note that at the following reboot Synergy will indeed automatically start, but the tray icon will not display automatically (at least for version 1.4.2 beta on Windows 7). To uninstall the service, do the same thing but obviously select Uninstall.

If you want to start the server from the command-line, here is a Windows command you can place in a  file or just run from :

 C:\Program Files\Synergy+\bin\synergys.exe  -f --debug ERROR --name left --log c:\windows\synergy.log -c C:/windows/synergy.sgc --address 10.66.66.2:24800

## macOS
macOS has a similar configuration as Unix: check the official documentation for more information.

## Configuration examples
This is an example for a basic 3-computers setup:

This should be the example bundled with the Arch Linux package:

The following is a more customized example:

## Clients configuration
## Arch Linux
In a console window, type:

 $ synergyc server-host-name

Or, to run synergy in the foreground:

 $ synergyc -f server-host-name

Here,  is the host name of the server.

## Set up encryption on client
If you use the synergy command line client, copy the file containing the fingerprint  from the server into the clients home directory . To start the synergy command line client with encryption, type:

 $ synergyc --enable-crypto server-host-name

If you want to enable the SSL trust without requiring the GUI on the client you can follow the steps below, but you should confirm the fingerprint that gets displays is the same one your server has in its GUI or in the  on the server per above. The  is required to avoid the openssl client hanging waiting for input.

For Barrier:

Note: Barrier v2.4.0 introduced a new keyfile format, which requires a SHA256 fingerprint and a "v2:sha256:$fingerprint" line format. For older versions, make sure the fingerprints are SHA1 and do not include a prefix.

 $ mkdir -p ~/.synergy/SSL/Fingerprints
 $ fingerprint=$(echo -n | openssl s_client -connect $YOUR_SYNERGY_SERVER:24800 2>/dev/null | openssl x509 -sha256 -noout -fingerprint | cut -d"=" -f2);
 $ echo "v2:sha256:$fingerprint" > ~/.synergy/SSL/Fingerprints/TrustedServers.txt

For Synergy:

 $ mkdir -p ~/.synergy/SSL/Fingerprints
 $ fingerprint=$(echo -n | openssl s_client -connect $YOUR_SYNERGY_SERVER:24800 2>/dev/null | openssl x509 -sha1 -noout -fingerprint | cut -d"=" -f2);
 $ echo "$fingerprint" > ~/.synergy/SSL/Fingerprints/TrustedServers.txt

## Autostart
There exist several ways to automatically start the Synergy client, and they are actually the same that can be used for every other application.

* You can add the next line to your xinitrc:

The following is an alternative:

* Otherwise, if you are using a display manager (GDM, SDDM, ...), or a stand-alone window manager (Openbox, ...), you could exploit its start-up script and add the following:
 synergyc server-host-name

* To start the Synergy client with systemd, create a service file:

Then do a daemon-reload and start the  user unit.

To start the service at login for your user, enable it as a user unit.

Automatically starting Synergy is also documented in its official reference page.

## Windows
After installation, open the Synergy program, select the option Client (use another computer's keyboard and mouse) and type the host name of the server computer in the text box, then click Start to start the client.

If you want to start the Synergy client every time Windows starts, you have to launch the program as an administrator, then go to Edit -> Services and select Install in the Client section.

If you want to start the client from the command-line, here is a Windows command you can place in a  file or just run from .  This points to a configuration file in  and runs in the background like a service.

## macOS
Locate the synergyc program in the synergyc folder and drag it onto the terminal window: the full path will appear in the terminal.
Now append the host name of the server, so that the complete command will look like this:

Then press .

## Known issues
If Arch is being used as a client in a Synergy installation, the server may not be able to wake the client monitor. There are some workarounds, such as executing the following via SSH, if ACPI is enabled (see: Display Power Management Signaling#Runtime settings):

## Troubleshooting
The official documentation has a FAQ and also a troubleshooting page.

## Keyboard AltGr
If you encounter problems with /, add

into the screen/client section.

## Keyboard repeat
If you experience problems with your keyboard repeat on the client machine (Linux host), simply type:

in any console.

## Keyboard mapping
If you experience problems with the keyboard mapping when using the server's keyboard in a client window (e.g a terminal) then re-setting the X key map after starting synergyc may help. The following command sets the keymap to its current value:

 # setxkbmap $(setxkbmap -query | grep "^layout:" | awk -F ": *" '{print $2}')

## No cursor in Gnome
When GNOME does not detect a mouse, it will default to touchscreen mode and hide the cursor. To enable run:

 # dconf write /org/gnome/settings-daemon/plugins/cursor/active false

This can be added to an init script or systemd unit:

 ExecStartPost=dconf write /org/gnome/settings-daemon/plugins/cursor/active false

Mixing xorg and wayland environments also does not currently work. Try starting gnome in xorg for both client and server.

## Client is returning "failed to verify server certificate fingerprint"
You need to copy the content of server's  into client's . See #Set up encryption on client.

## Scroll Lock LED does not light
When using Scroll Lock to lock to a client (or to enter relative mouse move mode), you may run into an issue with your keyboard's Scroll Lock LED not lighting. This can be solved by binding the  key to an empty modifier key.

First, find an empty modifier. In this case, mod3 is available:

Then, add the new mapping.

 $ xmodmap -e 'add mod3 = Scroll_Lock'
 $ echo "add mod3 = Scroll_Lock" >> ~/.Xmodmap

See Xmodmap#Activating the custom table to have  loaded on login.

After making this change, test the LED and screen locking. If you find that you need to press Scroll Lock twice to lock screens, enable  on all screens in .

## Additional mouse buttons do not work in client
If you find that additional mouse buttons (i.e. Mouse4/Mouse5) do not translate to a client, try adding the following to :

 mousebutton(6) = mousebutton(4)
 mousebutton(7) = mousebutton(5)

This will re-map the mouse keys to the proper number. If that does not fix the problem, remove the configuration, stop Synergy, and start it in the foreground with debug logging enabled:

 $ synergys -f -d DEBUG1

Then, move your cursor to the screen of the client with the issue. Click the non-functioning keys, and watch for log entries like this:

 DEBUG1: onMouseDown id=6
 ...
 [2017-09-30T14:56:46 DEBUG1: onMouseUp id=6

The  part will have the right number to use in

## Mouse fixed in certain games
In some applications (like Overwatch or other games) the cursor gets trapped in the middle of the screen.

According to https://github.com/deskflow/deskflow/issues/2631 this is an issue that is known.

Just set relative mouse movement in your settings and make sure to lock the screen.
