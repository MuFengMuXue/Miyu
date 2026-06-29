# SickChill

SickChill (a fork of SickRage which was abandoned and malicious, which in turn was already a fork of SickBeard) is an automatic video library manager for TV Shows. It watches for new episodes of your favorite shows, and when they are posted it does its magic.

## Installation
Install . It contains the application and a systemd service file.

## Running as a systemd service
Enable/start .

## Password protecting the webui
By default, the SickChill webui running on port 8081 is not protected by a password. To set a username and password, edit the SickChill configuration file at  and change the  and  settings:

## Compatible torrent clients
For some you will need to enable the web-interface to work.

* Transmission
* Deluge
*
*
* "Black Hole" (saves .torrent files to a directory)
* uTorrent
* Synologie DS

## First time usage
SickChill is a web-application that can be accessed on http://localhost:8081, when SickChill reports that it does not know its version, just hit the update button. It will check for updates, restart itself and set its current version. The settings are pretty straightforward. If you already have a storage of series, just point SickChill to it and it will analyze it and try to add your already downloaded series to its own list.
