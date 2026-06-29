# Network UPS Tools

This document describes how to install the Network UPS Tools (NUT). Network UPS Tools is compatible with thousands of models of UPS. You can check the Hardware Compatibility List to see if your UPS is supported.

## Installation
Install the  package.

## Configuration
NUT has 3 daemons associated with it:

* The driver which communicates with the UPS.
* A server (upsd) which uses the driver to report the status of the UPS.
* A monitoring daemon (upsmon) which monitors the upsd server and takes action based on information it receives.

The idea is that if you have multiple systems connected to the UPS, one can communicate the status of the UPS over the network and the others can monitor that status by running their own upsmon services.  NUT has extensive documentation on the configuration however this is going to walk through a simple setup of a USB UPS and the associated server and monitor all in one system (common desktop configuration).

## Driver configuration
The configuration here will depend on the type of UPS you have. Consult the previously mentioned Hardware Compatibility List to find what driver will likely work for your UPS. You can run the tool  which will detect NUT-compatible devices attached to your system.

For many UPS connected by USB, use the  driver. For UPS with serial port, use , where X is the number of serial port (Example: ). For UPS with USB port, use .

You can name the UPS device whatever you like.

Start the driver as root with . If there are no errors, you should see a message like this one for the driver :

If the driver does not start cleanly, make sure you have picked the right one for your hardware. You might need to try other drivers by changing the  value in .

At this point you should be able to start/enable  which will automatically create nut-driver@ systemd service instance and start it.

## Can't claim USB device error
If you receive an error message like this one:

 Can't claim USB device could not detach kernel driver from
 interface 0: Operation not permitted
 Driver failed to start (exit status=1)

Or a less specific one:

 USB communication driver 0.33
 No matching HID UPS found
 Driver failed to start (exit status=1)

It is most likely a problem with permissions for accessing the device. You can fix that by specifying an udev rule that sets the correct group:

{{hc|/etc/udev/rules.d/50-ups.rules|2=
SUBSYSTEM=="usb", ATTR{idVendor}=="XXXX", ATTR{idProduct}=="YYYY", GROUP="nut"
}}

Where  and  are the device manufacturer and product IDs. You can see these either in the error output () or by using .

After this is done, reload and retrigger udev rules by running:

 # udevadm control --reload
 # udevadm trigger

## upsd configuration
By default upsd listens only on localhost  and this is fine for our purpose. Though it is not necessary for following this guide, you can configure upsd beyond the defaults by editing . See .

You will need to add a user for a monitor to connect to the server and issue commands. See .

At this point you should be able to start/enable .

If it has started successfully, you can run  to get information from the UPS. Example output from the command:

## upsmon configuration
The last step is to configure upsmon to listen to upsd and take action on events.

Add the following line to :

 MONITOR upsname@localhost 1 upsduser password primary

Here upsname is the name of the UPS, and upsduser and password is the user and its password you set in .

You can also configure what alerts are sent, where they are sent, what action is taken when the battery is low, and more. See .

Then start/enable .

Your logs should show upsmon starting and monitoring the UPS.

## systemd targets
In order for the systemd service units to start on boot, you must enable  and .

## NUT-Monitor
[https://networkupstools.org/projects.html#_a_href_http_www_lestat_st_en_informatique_projets_nut_monitor_nut_monitor_a NUT-Monitor is a graphical user interface to monitor and manage devices connected to the Network UPS Tools server.

You can install nut-monitor with the  package.

## Troubleshooting
## CyberPower UPS keeps disconnecting/reconnecting
Some CyberPower UPS products are known to keep disconnecting/reconnecting until the driver successfully attaches to it Once the disconnect/reconnect loop starts, it can be difficult for  to establish connection to the UPS using default configuration (which appears to impact the proprietary driver as well).

To mitigate this issue, edit , add the following configuration, then start/enable .

Additionally, consider using  in UPS configuration:

## EATON 5E650iUSB fails to start driver
According to an [https://github.com/networkupstools/nut/issues/630 issue on GitHub, there is a bug in the kernel and the following kernel parameter can be used as a workaround:

 usbhid.quirks=0x0463:0xffff:0x08

## Can't claim USB device: Entity not found
When getting the following error from nut-driver:

 Can't claim USB device Entity not found

Several users report (example [https://bbs.archlinux.org/viewtopic.php?id=290778) that rebooting (power-cycling) the UPS can fix this issue.

Alternatively, you can try  before starting the  systemd service.
