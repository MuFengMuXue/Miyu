# AMule

aMule is an eMule-like client for the eDonkey Network and Kademlia networks, supporting multiple platforms.

## Installation
Install the  package.

 is a full featured aMule daemon, running without any user interface (GUI). It is controlled by remote access through aMuleGUI (GTK), aMuleWeb, or aMuleCmd.

## Services
The package provides two systemd services:  and . First you need to configure it. You need to provide passwords for external connection and admin password for . Start  service and  if you require it. Enable them to start aMule every boot.

Once  service is started, it is available at  (or with external address of your host).

## Configuration
At package installation time a new user account amule created. This account is used to run systemd services.

All configuration and temporary files are kept in amule home directory  among them:
* for amuled
* for amuleweb

At the package installation time pacman generates a simple  file with preset external connection password. The same password is used for amuleweb configuration file. One can use the password for connecting amule from other remote clients such as amule-gui.

To generate password, run:
 $ echo -n your password here | md5sum | cut -d ' ' -f 1

The output of the above command is the encrypted password. Now you edit the configuration file by adding following lines under section :

Do not forget that all files under  should be owned by amule user.
 # chown amule:amule -R /var/lib/amule

## amuleweb
## Create configuration files
Start amuleweb using the user you just created to create the configuration file:

 amuleweb --write-config --password=password here --admin-pass=web password here

This command will write the configuration file. The password here is the unencrypted password you used to configure amuled. The password for the log in on the web interface will be set to web password here.

## amulegui
Amulegui is a GTK interface for aMule.

## Configuring notifications
Some automatic actions settings are avaible through Settings > Events. The command notify-send is useful to set notifications, using some amule variables. In example, set the core command in the section Download completed for a notification when a download is complete to:

 notify-send -i amule "%NAME completed (%SIZE bytes)"

The option  includes the amule icon (a custom file may be specified adding its path between apostrophes, instead of "amule" icon filename).

## Docker
A Docker image is available, see https://hub.docker.com/r/ngosang/amule.
