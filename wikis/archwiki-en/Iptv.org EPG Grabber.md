# Iptv.org EPG Grabber

Iptv.org EPG Grabber is a nodejs/html application with utilities for downloading the EPG for thousands of TV channels from hundreds of sources.
It can later be used by Kodi, MythTV, Tvheadend and other compatible Television and Home Theater front-end media players.

## Installation
Install the  package.

## Usage
First step is to create a working directory for  EPG grabber. The working directory will be saved to the home directory of the active user or to a chosen path. All configuration and output files are stored in the working directory.

To create a working directory type:

 # iptvorg-epg -d /path/to/working_directory

At this point all necessary files are created and it's now possible to grab EPG data from a chosen site or custom channels xml configuration file.

To generate EPG guide file (default:), type:

 # iptvorg-epg -d /path/to/working_directory -s my.site.example

In addition to the command above, it can be combined with ,  and .

For a full listing of the active sites (including status), type:

 # iptvorg-epg -ps

For a full usage information, type:

 # iptvorg-epg --help

## Custom channels list
With custom channels list it is possible to use multiple channels from multiple sites lists.
An example XML file is included in the working directory called . Make sure to place any custom XML channels file inside the working directory.

To generate a custom EPG guide file, type:

 # iptvorg-epg -d /path/to/working_directory -c my.channels.xml

## Configuration
Iptvorg-epg can be run in different ways, both manually and automated. For automated solutions custom scripts and systemd unit can be used. It is also possible to run the EPG grabber with the command ...

Here is an example systemd service to run with iptvorg-epg:

This can be combined with a timer (runs every day at 6:00) like this:

Remember to enable/start any custom systemd services.
