# Hamachi

Hamachi is a proprietary, commercial VPN software by LogMeIn, Inc. With Hamachi you can organize two or more computers with an Internet connection into their own virtual network for direct secure communication.

## Installation
Install the  package.

The following GUI frontends for Hamachi are available:

* (Gtk4, Vala)
* (Qt5, Python)

## Configuration
Hamachi is configured in  (create that file if it does not exist).
Unfortunately, it is not easy to find a comprehensive list of possible configuration options, so here are a few that you can use.

## Using the hamachi command line tool as a regular user
In order to use the  command line tool as a regular user, add the following line to the configuration file:

## Automatically setting a custom nickname
Normally, Hamachi uses your system's hostname as the nickname that other Hamachi users will see. If you want to automatically set a custom nickname every time Hamachi starts, add the following line to the configuration file:

 Setup.AutoNick YourNicknameHere

You can also manually set a nickname using the  command line tool:

 # hamachi set-nick YourNicknameHere

However, this needs to be done every time Hamachi is (re-)started, so if you always want to use the same nickname, setting it automatically (as explained above) is probably easier.

## Usage
Start .

To get a list of all the commands, run:

 $ hamachi --help

You can set Hamachi to start at every boot by enabling .
