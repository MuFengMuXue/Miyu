# Wvdial

WvDial is a Point-to-Point Protocol dialer: it dials a modem and starts ppp in order to connect to the Internet.

## Installation
Install the  package.

## Configuration
When wvdial starts, it first loads its configuration from  and  . If  is not present, the easiest way to create it is to use the provided configuration utility wvdialconf:

 # wvdialconf /etc/wvdial.conf

It helps in generating the configuration file needed by wvdial. wvdialconf detects your modem, and fills in automatically the Modem, maximum Baud rate, and a good initialization string (Init options) and generates or updates the wvdial configuration file () based on this information.

It is safe to run wvdialconf if a configuration file already exists. In that case, only the Modem, Baud, Init, and Init2 options are changed in the Defaults section, and only if autodetection is successful.

After you have filled in your login information, wvdial ought to work. You can move to the next section. However for providers of USB modems that require a specific Init string and user/password combination,  can help generate a wvdial configuration (based on the  package).

A typical  looks like this after manual configuration:

## Usage
There are a few different ways of giving regular users the ability to use wvdial to dial a ppp connection. This document describes three different ways, each of them differ in difficulty to set up and the implication on security.

wvdial is to be run as root with the following command:

 # wvdial option

Leave option blank if you have not added a section or if  is auto-generated.

 # wvdial

## suid
As normal users cannot use wvdial to dial a PPP connection by default, change permissions:

 # chmod u+s /usr/bin/wvdial

You should see the following permissions:

 # ls -l /usr/bin/wvdial
 -rwsr-xr-x  1 root root 114368 2005-12-07 19:21 /usr/bin/wvdial

## Group
Another, slightly more secure way is to set up a group called  (call the group as preferred) and give members of this group permission to run wvdial as root.

First create the group and add the users to it:

 # groupadd dialout
 # gpasswd -a username dialout

Then set the group and adjust the permissions on wvdial:

 # chgrp dialout /usr/bin/wvdial
 # chmod u+s,o= /usr/bin/wvdial

The files should have the following permissions:

## sudo
sudo arguably offers the most secure option to allow regular users to establish dial-up connections using wvdial. It can be used to give permission both on a per-user and group basis. Another benefit of using sudo is that it is only needed to do the setup once; both previous solutions will be "undone" when a new package of wvdial is installed.

To give a specific user permission to run wvdial as root, add the following line (changing the username), create the following drop-in file using the  command as root:

To give all members of a group ( in this case) the same permission:

If  shows a pppd entry, it means that the session is ready.

## Tips and tricks
The following are applicable to USB modems.

## Low connection speed
See USB 3G Modem#Low connection speed.

## Auto Reconnect
If wvdial randomly drops connection you can use script below:

 #! /bin/bash
 (
    while : ; do
        wvdial
        sleep 10
    done
 ) &

## Multiple devices
Often there will be several devices (at , ,  for example). If in doubt about which to use, try each of them in turn or use  (a link set up by usb_modeswitch) which should point to the correct one. Once the configuration files are prepared, the internet connection is established by running:

 $ wvdial options

If necessary additional setup commands can be placed in a simple script like this:

 usb_modeswitch
 sleep 2
 modprobe usbserial vendor=0xVVVV product=0xMMMM maxSize=4096
 sleep 2
 wvdial thenet

where VVVV is the hexadecimal vendor ID from lsusb, MMMM is the hexadecimal product ID when in modem mode, and "thenet" is the name of the section in  which you wish to use. The maxSize option may or may not be necessary. It simplifies matters if you disable the SIM PIN, but if you require it, run  before .

The final wvdial command should start pppd and the obained IP address should be visible in the terminal output. At that point the internet connection should be live, which can be easily checked with a web browser or by pinging an external IP address.
