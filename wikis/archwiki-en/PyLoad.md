# PyLoad

pyLoad is a fast, lightweight and full featured download manager for many One-Click-Hoster, container formats like DLC, video sites or just plain http/ftp links (supported hosts). It aims for low hardware requirements and platform independence to be runnable on all kind of systems (desktop pc, netbook, NAS, router). Despite its strict restriction it is packed full of features just like webinterface, captcha recognition, unrar and much more.

pyLoad is divided into core and clients, to make it easily remote accessible.

Available clients (screenshots):

* a web interface
* a command line interface
* a GUI written in Qt
* and an Android client.

## Installation
Install .

## Configuration
Create all the files with:
 # pyload

This will give you a jump start, by providing a basic but working setup. Being a basic setup, there are more options and you should at least look at them, since some sections are untouched by the Assistant, like the permissions section.

## Manual
You can also directly edit  (located in  by default.

While also editable with the web interface, you can change the plugins configuration by editing .

Extraction passwords are stored in .

## Scripts
For more info on this read .

If you are interested in running userscripts, before running, you need to

 # chown user /opt/pyload/scripts/

(the user being the one you defined in pyload.conf / permissions settings)
in order for pyLoadCore to create the necessary folders.

## Running
## Essential
 # pyload

To run pyLoad in the background, use:
 # pyload --daemon

## Interfacing with pyLoad
Using the web interface, with default settings, then:
 http://localhost:8000

## Daemon
To start pyload start pyload service.

To have it started automatically on boot, enable pyload service.
