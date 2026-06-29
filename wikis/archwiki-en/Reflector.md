# Reflector

Reflector is a Python script which can retrieve the latest mirror list from the Arch Linux Mirror Status page, filter the most up-to-date mirrors, sort them by speed and overwrite the file .

## Installation
Install the  package.

Alternatively, the  package can be used as a drop-in replacement.

## Usage
To see all of the available options, run the following command:

 $ reflector --help

## Examples
See .

## Automation
## systemd service
Reflector ships with , which runs Reflector using the options specified in . The default options in that file provide a good starting point and example.

Enable  to run Reflector on boot. To run it immediately, start the service.

## systemd timer
Reflector provides a systemd timer () that starts the #systemd service  weekly. The schedule can be changed by editing .

For changing the default options that  gets started with, edit the configuration file as described in #systemd service. Then, start and enable .

To refresh the mirrorlist ahead of schedule, start .

## pacman hook
 is not updated regularly, invoking reflector because a mirror in some part of the globe was added or removed is not relevant; use the #systemd timer approach instead. If you do not want  to be installed at all, use NoExtract in .
