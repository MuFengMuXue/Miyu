# APC UPS

This document describes how to install the APC UPS daemon. The APC UPS can communicate with the Linux system through either a RS-232 or USB serial connection. In the event of a prolonged power outage, should the APC UPS lose most of its battery capacity, it can tell the Linux box to perform a safe shutdown.

## Install the package
Install the  package.

## Configure APC UPS
The main configuration file for the APC UPS daemon can be found in . The default configuration is for devices connected over a USB cable.

## Test
First, enable and start .

Next, wait about a minute and confirm the daemon is running and properly monitoring the battery:

To fully test your setup:
# Change  from  to  in the  file.
# Shut off power to the UPS at the circuit breaker.
# Observe that your Linux box powers down, in short order.
# Turn the circuit breaker power back on.
# Power on your Linux box.
# Change  from  back to  in the  file.

Do not unplug the UPS to test it, as it is not safe for the UPS or for your computer to disconnect the ground plug.

When everything is ok, all that is left to do is enable the  service.

## Hibernating instead of shutting down
You can make your system hibernate instead of shutting down. First, make sure the system hibernates cleanly. To set up hibernation, see Power management/Suspend and hibernate.

## Create the hibernate script
Create this in  as root:

Make it executable.

## Link the hibernate script for apcupsd to use it
Create a symbolic link from the  directory to the script. The result is the apcupd's apccontrol script, in this directory, will call the hibernate script instead of doing the default shutdown action for these operations.

 # ln -s /usr/local/bin/hibernate /etc/apcupsd/doshutdown

If you are running apcupsd as a client to another machine running apcupsd as a server and want your machine to hibernate if the server is shutdown or if communication to the server is lost then you may also wish to add:

 # ln -s /usr/local/bin/hibernate /etc/apcupsd/remotedown

## Make apcupsd kill UPS power once the hibernate is done
Once the PC has hibernated successfully, it is common practice to switch off the UPS in order to conserve battery charge and prevent full battery drain. This can be achieved through a power suspend event in systemd.

Create  and put the following contents in it:

Make the script executable.

Now you can test your setup.

## Troubleshooting
## The desktop environment will also sense the UPS if connected by USB cable
For example, the default KDE setting is to put the computer in sleep if it has been on UPS battery for more than 10 minutes and the mouse has not moved. On many computers this causes a crash. This can be changed from KDE System Settings > Power Management > On battery.

## hid-generic : control queue full
If you are using a systemd-based initramfs you might run into the "control queue full" log message happening many times every second. You will want to add  to you  and regenerate your initramfs.
