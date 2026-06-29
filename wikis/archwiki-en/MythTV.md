# MythTV

MythTV is an application suite designed to provide an amazing multimedia experience.
It provides PVR functionality to a Linux based computer and also supports other media types.
Combined with a nice, quiet computer and a decent TV, it makes an excellent centerpiece to a home theater system.

## Structure
The MythTV system is split into a backend and a frontend. Each component has its own functions:

## mythbackend
* Schedule and record television programming
* Stream video data to the frontend
* Flag commercial breaks
* Transcode videos from one format to another

## mythfrontend
* Provide a pretty GUI
* Play back recorded content
* Provide an interface to schedule programs

The frontend and backend may be on separate computers on a network, and there may also be multiple frontends. This architecture allows for a central media distribution system that can reach anywhere a network can. This is a remarkably flexible system, and it even allows very low power machines to act as perfectly usable frontends.

## Hardware requirements
All systems are going to need a tuner card. The Hauppauge PVR series of cards (150, 250, 350, and 500) are very popular for use with MythTV due to fairly decent Linux support and low CPU usage. Other cards, like those based on the BT878 chipset, are also used. Unlike the PVR series, BT878 based cards require significant amounts of CPU power to save the video, as these cards output raw frames and not compressed streams.

## Software requirements
A working Xorg (graphical) environment is necessary. For setting MythTV up, a remote access via X11-forwarding mechanism is sufficient.

## Installation
Install the  package and any desired plugins. The package creates the mythtv user.

At this point a generic MythTV installation is present that must be refined into a backend, a frontend, or both.

## Backend setup
Before setting up your backend, make sure you have a functioning video capture card or a firewire input from a STB. Unfortunately, that part of setup is outside the scope of this article. If you are in the United States, get an account at Schedules Direct (this service provides TV listings at a minimal cost). Users outside the United States will need to use screen scrapers (xmltv) to do the same job.

## Setting up the database
Install  and start .

If other machines in the LAN are expected to connect to the masterbackend server, comment out the "skip-networking" line in  at this point.

Setup mysql with a password:

 # mysql_secure_installation

Create the database structure:

 $ mysql -u root -p  mysql

Some setups refuse frontends from remote machines.  To fix this:

 # mysql -u root -p
 mysql> GRANT ALL ON mythconverg.* TO 'user'@'host.net' IDENTIFIED BY 'password';
 Query OK, 0 rows affected (0.00 sec)
 mysql> FLUSH PRIVILEGES;
 Query OK, 0 rows affected (0.00 sec)

* Replace user with the user name running on the frontend (default: mythtv).
* Replace host.net with the host name or IP address of the remote box needing access.  Other common values are %.local and 192.168.1.%.
* Replace password with a suitable password (default: mythtv).

Example:

 # mysql -u root -p
 mysql> GRANT ALL ON mythconverg.* TO 'mythtv'@'192.168.0.%' IDENTIFIED BY 'mythtv';
 Query OK, 0 rows affected (0.00 sec)
 mysql> FLUSH PRIVILEGES;
 Query OK, 0 rows affected (0.00 sec)

## Setting up the master backend
Load up your WM (lxde is a good choice for light-weight builds, but anything will work.)

Now run the mythtv-setup program

 $ mythtv-setup

If your backend runs on a headless server, mythtv-setup can be run via OpenSSH#X11 forwarding by running:
 $ ssh -X user@backend '. /etc/profile.d/perlbin.sh && LANG=C.UTF-8 mythtv-setup'

* General menu
:If this is your master backend, put its IP address in the first and fourth fields, identifying this computer as your master and giving its network IP address.
:On the next page, enter the paths where recordings and the live TV buffer will be stored. LVM or RAID solutions provide easily accessible large scale storage. But again, those are outside the scope of this article. Set the live TV buffer to a size you can handle and leave everything else alone.
:On the next page, set the settings to your locale. NTSC is mostly used in North America, and be sure to set whether using cable or broadcast.
:On the next two pages, leave everything as is unless you know for sure you want to change it.
:On the next page, if you have a fast backend that can handle recordings and flagging jobs simultaneously, it is recommended to set CPU usage to "High", maximum simultaneous jobs to 2, and to check the commercial flagging option.
:On the next page, set these options to taste. Automatic commercial flagging is highly recommended.
:Ignore the next page and finish.

* Capture card menu
:Select your card type from the drop down list. Hauppauge PVR users will select the MPEG-2 encoder card option.
:Point mythtv-setup to the proper location, usually

* Video sources menu
:This is where it gets important to have a source for TV listings. Schedules Direct users should create a new video source, name it, select the North America (Schedules Direct) option, and fill in their logon information. In order to verify that it is correct, go ahead and retrieve the listings.

* Input connections menu
:This menu is rather self-explanatory. All you need to do is pick an input on the capture card and tell myth which video source it connects to. Most users will select their tuner and leave all the other inputs alone. Satellite users will select a video input, and on the next page provide the command to change channels on their STB using an external channel change program. This is also outside the scope of this article.

* Channel editor menu
:This menu is safe to ignore

* Exit the program (Esc)

* Run mythfilldatabase
 $ mythfilldatabase

This should populate your mysql database with TV listings for the next two weeks (or so).

## Enable the mythbackend daemon
Enable the  systemd unit.

## Troubleshooting
## PVR150
If you cannot open  of your PVR150, install the firmware, located in the  package.

## Opening DVB frontend device failed
The kernel takes time to register the frontend devices (such as those of TurboSight TBS 62x1) and they may not be available when systemd starts . This leads to the following error recorded in the system log:
 # DVBChanOpening DVB frontend device failed.
 # eno:No such file or directory (2)
 # DVBChan[1(/dev/dvb/adapter0/frontend0): Failed to open DVB frontend device due to fatal error or too many attempts.
 # ChannelBase: CreateChannel() Error: Failed to open device /dev/dvb/adapter0/frontend0
 # Problem with capture cardsCard 1failed init

The solution consists in starting the  only after the devices are available:
* Create file :
 #
 # Create systemd device units for capture devices
 #
 SUBSYSTEM=="video4linux", TAG+="systemd"
 SUBSYSTEM=="dvb", TAG+="systemd"
 SUBSYSTEM=="firewire", TAG+="systemd"
* Create a drop-in unit file for  as follows:

See MythTV wiki's page Systemd mythbackend Configuration for further details.

## Frontend setup
Compared to the backend, getting a frontend running is simple. The frontend machine needs permission to access the database on the backend machine. On the backend machine, follow the instructions to grant remote access in the MariaDB article. On the frontend machine, install the mythtv packages using pacman as above. Afterward, make sure you are in an X environment as a normal user and run mythfrontend. It will pop up a menu asking about the IP address of the backend and the local computer's name and IP address. Fill in this information and your frontend should be functional.

On the other hand, the frontend has more options than a luxury car. All of those are an article on their own. There are a few notable options that should be set to ensure a good working setup. If you do not have an interlaced monitor (and almost nobody does), you will need to deinterlace your television output. Go into the TV playback menu and select kernel deinterlacing or bob2x deinterlacing. Try both and see which you like better. Also, in the general settings page, it is good to set up your ALSA setup settings, but those vary so greatly it is not worth suggesting values here.

## MythTV plugins
There are a number of plugins available for MythTV in the AUR. They range from RSS readers to DVD players. Take a look at them. Simply installing the package on the frontend computer should impart the intended functionality. There is rarely any additional setup, and when there is, the install file will mention it.

## Hints to a Happy Myth System
But not full articles (yet)
* Run ntpd or openntpd on your backend to make sure it always has the right time.
* LIRC on your frontend allows you to use a remote control, which is wonderful in a living room.
* Use gdm, sddm, or xdm to automatically log in your frontend, and ~/.xinitrc to load mythfrontend on boot.
* Set the "automatically run mythfilldatabase" option on one of your frontends to make sure you always have listings.
* Do not forget to use the verbosity statements and log file location arguments to mythfrontend so you can see when things break.
* Do not run your frontend as root, create a mythtv user

## Using GDM to autologin your Mythfrontend
In , add the following statements under the heading:

FYI - GDM will not autologin as root

## Using XDM to automically login to your MythFrontend
Find in your /etc/inittab file the following line:
 id:3:initdefault:

Change to:
 id:5:initdefault:

Then add the following below it (or anywhere in the file):
 x:5:respawn:su - MYTHUSER -c startx

If you would like to start mythfrontend on booting into Xorg, edit (or create if none exists) your MYTHUSER's .xinitrc file and add the following line:
 mythfrontend

## Optmize your system
Be sure to have a look at [https://www.mythtv.org/wiki/Optimizing_Performance Optimizing Performance at the MythTV Wiki for how to keep your data stores happy, as well as optimize your system in various other ways to get the most out of your Myth box.
