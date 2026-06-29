# Mumble

From Wikipedia, the free encyclopedia:

:Mumble is a voice over IP (VoIP) application primarily designed for use by gamers, similar to programs such as TeamSpeak and Ventrilo.

This page goes over installation and configuration of both the client portion of the software (Mumble) and the server portion (Murmur).

## Client
## Installation
Install the  package.

## Configuration
When you first launch the client, a configuration wizard will take you through the setup process.
Settings can be changed later through the menu.

For a discussion of advanced settings, see the
official documentation.
The
Mumbleguide
is a good starting point.

## Server
The Mumble project maintains a good guide for setting up the server.
What follows is a quick-and-dirty, abridged version of that guide.

## Installation
Install the  package.

The post-install script will tell you to reload dbus and set the supervisor password.
SQLite is used as the default database. The default configuration does not use dbus, so you can ignore that if you want.
Setting the supervisor password is recommended, however.

## Set supervisor password
To set the supervisor password, run this command as the mumble-server user (default ):

 mumble-server -ini /etc/mumble/mumble-server.ini -supw PASSWORD

This will also create a SQLite database in the defined directory inside of the configuration file

## Configuration
## Network
If you use a firewall, you will need to open TCP and UDP ports 64738.
Depending on your network, you may also need to set a static IP, port forwarding, etc.

## Configuration File
The default Murmur configuration file is at  and is heavily commented.
Reading through all the comments is highly recommended.
More information can be found on the Mumble wiki [https://wiki.mumble.info/wiki/Murmur.ini here.

## Startup
Enable/start . If all went smoothly, you should have a functioning Murmur server.

## SSL/TLS
By default, mumble-server will auto-generate a certificate for you and use that.

Alternatively, you can use either a self-signed certificate as described in OpenSSL, or a publicly trusted one with Let's Encrypt.

Edit  and tell it where your key and cert are:

## Troubleshooting
## Push-to-talk on Wayland
Currently with Wayland/GNOME/Sway, push-to-talk will not work without the window being in focus. Wayland does not allow clients that are not focused to sniff input. This is considered a security feature.

Since Mumble 1.4, the Mumble IPC can be used to toggle push-to-talk. These commands can be bound to global hotkeys in your Wayland compositor:

 $ mumble rpc starttalking
 $ mumble rpc stoptalking
