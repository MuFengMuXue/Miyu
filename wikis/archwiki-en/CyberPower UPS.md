# CyberPower UPS

This document describes how to install the CyberPower UPS daemon PowerPanel or alternatively the Network-UPS-Tools. The main advantage of using a CyberPower UPS is that it is cheap and it can communicate with your Linux box through either a RS-232 or USB serial connection. In the event of a prolonged power outage, should the CyberPower UPS lose most of its battery capacity, it can tell the Linux box to perform a safe shutdown.

## Using PowerPanel
## Installation
Install the  package.

## Configuration
Edit

Email notifications can be accomplished by editing  and

## Running
Start/enable .

To verify, run:

## Customization
You can check and change the current settings using the  command. (However, the command will not work unless the daemon is up and running.)

The service performs configurable actions in two different scenarios:

* When external power has failed for at least a certain amount of time (60 seconds by default)
* When battery power is low, as determined by either of two conditions:
** Battery capacity is less than a predetermined percentage (35% by default), or
** Remaining runtime (estimated from current power draw) is less than a predetermined number of seconds (300 seconds—that is, 5 minutes—by default)

To check the current settings, use . For example:

The  command also provides an interface for changing the settings. For example, to configure the UPS not to shut down automatically when there is a power failure but battery power is still high:

See  or the PDF user manual for more information on how to configure settings.

## Desktop Notifications
You can modify the  and  scripts to send desktop notifications when power fails or battery is low (respectively). For example, add the following line to either file:

 systemd-run --machine=target_user@.host --user notify-send "Warning: Utility power has failed. Now running on battery." --icon=battery-caution

## Using Network UPS Tools
If you do not wish to use PowerPanel, the Network UPS Tools (NUT) is an alternative. Only one of these programs (PowerPanel or NUT) is required to monitor and shut the system down. You should not use both as they might interfere with one another.

Use instructions from the Wiki page of Network UPS Tools.
