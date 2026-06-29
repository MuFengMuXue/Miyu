# Preload

Preloading is the action of putting and keeping target files into the RAM. The benefit is that preloaded applications start more quickly because reading from the RAM is always quicker than from the hard drive. However, part of your RAM will be dedicated to this task, but no more than if you kept the application open. Therefore preloading is best used with large and often-used applications like Firefox and LibreOffice.

## Go-preload
gopreload is a small daemon created in the Gentoo forum.

## Installation
Install . To use it, first run this command in a terminal for each program you want to preload at boot:

 # gopreload-prepare program

For regular users, take ownership of  and :

 # chown username:users /usr/share/gopreload/enabled /usr/share/gopreload/disabled

and then gopreload each program you want to preload:

 $ gopreload-prepare program

Then, as instructed, press  when the program is fully loaded. This will add a list of files needed by the program in . To load all lists at boot, enable the systemd service file .

To disable the loading of a program, remove the appropriate list in  or move it to .

It is advised to run gopreload-prepare after system upgrades to refresh the file lists.
For the task, the following batch tool come handy:

 # gopreload-batch-refresh.sh

Just let it run without using the system.

## Configuration
The configuration file is located in

## Preload
preload is a program written by Behdad Esfahbod which runs as a daemon and records statistics about usage of programs using Markov chains; files of more frequently-used programs are, during a computer's spare time, loaded into memory. This results in faster startup times as less data needs to be fetched from disk.

## Installation
Install the  package. You may now start the systemd service , and/or enable it in order to start at boot.

## Configuration
The configuration file is located in , it contains default settings that should be suitable for regular users. The  option lets you configure how often to ping the preload system to update its model of which applications and libraries to cache.
