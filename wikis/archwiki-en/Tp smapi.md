# Tp smapi

tp_smapi is a set of kernel modules that retrieves information from and conveys commands to the hardware of many ThinkPad laptops before Ivy Bridge processors.

This information is presented through the  filesystem.  Much like the  filesystem,
you can read and write information to these files to get information about and send commands to the hardware.
tp_smapi is highly recommended if you are using a supported ThinkPad laptop.

## Supported laptops
First check whether your laptop is supported. Thinkwiki has a comprehensive list of all supported Thinkpads.
In case your TP does not support stop_threshold but only start_threshold please go here #Workaround for partially supported laptops for a decent workaround.

If you are installing on a recent Thinkpad that has an Ivy Bridge processor or later (any of the ,
 or  models), tp_smapi will not work: use .

## Installation
Install the  package for  or  for . For all other kernels (e.g., ), consider using .

tp_smapi (and its variations) provide the following kernel modules:

; tp_smapi: ThinkPad SMAPI Support
; hdaps: IBM Hard Drive Active Protection System (HDAPS) driver
; thinkpad_ec: ThinkPad embedded controller hardware access ( and  both depend on it)

After a reboot,  and its dependencies will get autoloaded and the sysfs interface under  should be fully functional.

## Features
Here are a couple of useful things you can do using tp_smapi.

## Control battery charging
It is bad for most laptop batteries to hold a full charge for long periods of time. You should try to keep your battery in the 40-80% charged range, unless you need the battery life for extended periods of time.

## General way
tp_smapi lets you control the start and stop charging threshold to do just that.  Run these commands to set these to good values:

 # echo 40 > /sys/devices/platform/smapi/BAT0/start_charge_thresh
 # echo 80 > /sys/devices/platform/smapi/BAT0/stop_charge_thresh

This will cause the battery to begin charging when it falls below 40% charge and stop charging once it exceeds 80% charge. This will extend the lifetime of your battery.

Note that when you remove and re-insert the battery, these thresholds may be reset to their default values.
To work around this, create a script to set these values, and make this script run both at startup and when a battery is inserted.
More specific instructions follow.

Create a script:

{{hc|/usr/sbin/set_battery_thresholds|
#!/bin/sh
# set the battery charging thresholds to extend battery lifespan
echo ${2:-40} > /sys/devices/platform/smapi/BAT${1:-0}/start_charge_thresh
echo ${3:-80} > /sys/devices/platform/smapi/BAT${1:-0}/stop_charge_thresh
}}

Make it executable. With this script to set a battery threshold is very simple,
just type (if set_battery_thresholds is the name of the script):

 set_battery_thresholds 0 96 100

Or run it with no arguments to default to BAT0, and thresholds of 40% and 80%.

Let systemd execute the script at startup. Thus, create the  unit and enable/start it afterwards:

You can also make it run when a battery is inserted. This requires that acpid is installed and running. Edit :

 #... other ACPI stuff
 battery)
   case "$2" in
     BAT0)
       case "$4" in
         00000000)
         ;;
         00000001)
         /usr/sbin/set_battery_thresholds
         ;;
 #... more ACPI stuff

## Check whether settings were accepted
To check whether your settings were accepted check the output of the following:

 $ cat /sys/devices/platform/smapi/BAT0/start_charge_thresh
 $ cat /sys/devices/platform/smapi/BAT0/stop_charge_thresh

## Protect the hard disk from drops
tp_smapi includes a driver to read the accelerometer in your laptop to detect drops and other events that
could cause damage to your hard drive. See the HDAPS page for more information on this useful feature.

## Workaround for partially supported laptops
For partially supported laptops you can still gain control over your battery.
First check what is actually supported:

 $ cat /sys/devices/platform/smapi/BAT0/start_charge_thresh
 $ cat /sys/devices/platform/smapi/BAT0/stop_charge_thresh

If start_charge_thresh is supported but not stop_charge_thresh but you still
want to have your computer stop charging your battery you might have other options.

Note: None of the first two options works on T42p. The third one works on E540.

## 1st option, custom script
* create the script  as above
* copy the original  to
* edit  as above and copy it to

Now copy the following script, make it executable, adjust the values
to your liking and run it every couple of minutes as a root cron.

 #!/bin/bash

 CURRENTCHARGE=$(acpitool -b | cut -d, -f2 | cut -d. -f1 | cut -b2-)

 if [ $CURRENTCHARGE -gt 80 ; then
     cp /etc/acpi/handler.sh.stop /etc/acpi/handler.sh
     echo 99 > /sys/devices/platform/smapi/BAT0/start_charge_thresh
     exit 0
 fi
 if [ $CURRENTCHARGE -lt 60 ]; then
     cp /etc/acpi/handler.sh.start /etc/acpi/handler.sh
       echo 0 > /sys/devices/platform/smapi/BAT0/start_charge_thresh
     exit 0
 fi

 exit 0

## 2nd option, tpacpi-bat
To control the battery charging thresholds, install the Perl script .

Manually set the thresholds by calling

 # tpacpi-bat -v -s startThreshold 0 40
 # tpacpi-bat -v -s stopThreshold 0 80

The example values 40 and 80 given here are in percent of the full battery capacity. Adjust them to your own needs.
You may also want to add these lines to a systemd tmpfile to set them at startup.

The manual setting of thresholds via the command  is not permanent. To set the thresholds permanently,
edit the start and end thresholds accordingly in .

## 3rd option, in kernel
Kernel 4.17 added the option to adjust battery charging thresholds for ThinkPads directly.

 # echo 60 > /sys/class/power_supply/BAT0/charge_stop_threshold
 # echo 40 > /sys/class/power_supply/BAT0/charge_start_threshold

Note that if you try to display the values, you will get only the last one set (start in the example), with 128 added
to it. This is a known issue, but the true value is really set, as you can see from battery behaviour.
Other interesting parameters can be found under .
