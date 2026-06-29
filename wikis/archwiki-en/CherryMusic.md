# CherryMusic

CherryMusic is a web application that lets you remotely stream, browse and manage your music collection.
It is intended to be an alternative to streaming services like Last.fm, Spotify and Grooveshark.

## Installation
Install the  package.

## Optional dependencies
* Live transcoding: , , , , ,  or  (which replaces the aforementioned codecs plus adds WMA decoding)
* Automatic image resizing on displayed cover art:
* Special character search terms:
* GTK system tray icon:

## Configuration
## Quick start
To just get it up and running with a basic setup, issue:

 $ cherrymusic --setup --port 8080

and open the address "localhost:8080" in your browser:

 $ browser localhost:8080

This will let you configure the most important options from within the browser and you can set up the admin account.

If you want CherryMusic to run as a system service and to automatically start on boot, see #systemd service file.

## Manual setup
Start CherryMusic for the initial setup:

 $ cherrymusic

On first startup CherryMusic will create its data and configuration files in  and , print a note to stdout and exit.
Now, edit the configuration file in and change the following lines to match your setup:

Open the address http://localhost:8080 in your browser to create an admin account.

After logging in, populate the search database by clicking Update Music Library in the Admin panel.

If you want CherryMusic to run as a system service and to automatically start on boot, see #systemd service file.

There are many more options to configure, please see this section.

## Fine tuning
See the man pages  and .

## Tips and tricks
## Symlinks in "basedir"
Probably, the most modular and flexible way of populating CherryMusic's music directory (called "basedir") is to create a dedicated directory and only symlink all paths to your music collections into that directory, e.g.:

 $ mkdir ~/.local/share/cherrymusic/basedir
 $ ln -s /path/to/musicdir1 ~/.local/share/cherrymusic/basedir/musicdir1
 $ ln -s /path/to/musicdir2 ~/.local/share/cherrymusic/basedir/musicdir2

## systemd service file
CherryMusic does not come with a daemon yet, but both CherryMusic AUR packages provide a systemd service file. It can be started as , where  is the user that should run CherryMusic (do not use root!).

## Running in a GNU Screen session
To keep CherryMusic running after logout, it can be run in a GNU Screen session.

 $ screen -d -m -S cherrymusic cherrymusic

Since CherryMusic only writes the output to the GNU Screen session, there is nothing to control from within the session. It may be more convenient to use a systemd service file. However, this may still be useful for debugging.

To run it in a GNU Screen session after boot, the following systemd service file can also be created and used:

To finally enable and start the service, see #systemd service file.

## Manually adjust the search parameters of the search algorithm
The search parameters of the search algorithm can be adjusted manually via the file  within your CherryMusic installation.

## Bind CherryMusic to ports less than 1024 (without root access)
To bind CherryMusic (or any other application) to a port less than 1024 you normally need root access. However, you should never run CherryMusic as root! There are several ways around this:

*Use a firewall (iptables or similar) for a port redirect
*Use authbind
*Use Capabilities (more exactly setcap)

For more information, see these references:

https://serverfault.com/questions/268099/bind-to-ports-less-than-1024-without-root-access
https://www.debian-administration.org/article/386/Running_network_services_as_a_non-root_user
https://stackoverflow.com/questions/413807/is-there-a-way-for-non-root-processes-to-bind-to-privileged-ports-1024-on-l

## Troubleshooting
## Missing module wsgiserver2 when using pip for installation
If the error

 ImportError: No module named wsgiserver2

occurs when starting CherryMusic, probably a broken CherryPy package from pip (versions `3.2.6` and `3.4.0` seem to be affected) is used. Here is a description of the problem. To fix this, uninstall CherryPy and reinstall:

 $ pip uninstall cherrypy
 $ pip install --no-use-wheel cherrypy

## Deactivate flash blocker
An active flash blocker can interfere with the web frontend. If you have trouble with things like track selection or playback, try whitelisting the server in your browser's flash blocker/plugin manager.

## CherryMusic does not load on Android Chrome
This might be due to AdBlock Plus being installed in the browser. CM does not feature any ads, so the problem is caused by this plug-in.

## Track scrolling not working behind Nginx
If track scrolling is not working in major desktop browsers behind Nginx and playback stops in the middle of the track and start over from the beginning, the Nginx module  has to be configured.

Change the line  to:

## No startup after unclean shutdown
When the CherryMusic service does not get stopped in a clean way, a  file is left around. This causes the CherryMusic service to abort when it tries to create a new PID file on start. To address this problem, a systemd drop-in file like the following can be created:
