# Common Desktop Environment

The Common Desktop Environment is a desktop environment for Unix and OpenVMS, based on the Motif widget toolkit. It was part of the UNIX98 Workstation Product Standard, and was long the "classic" Unix desktop associated with commercial Unix workstations. Despite being a legacy environment, it is still kept alive with support for Linux systems as well.

## Installation
The base CDE system is installed through the  package.

## Usage
CDE requires  to be running. Start the  unit before login.

## dtlogin
The  package supplies  which upon starting will launch the CDE login manager.

## xinit
CDE can be directly launched with  (install ):

 $ export PATH=$PATH:/usr/dt/bin
 $ export LANG=C
 $ startx /usr/dt/bin/Xsession
