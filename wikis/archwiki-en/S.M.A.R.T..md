# S.M.A.R.T.

S.M.A.R.T. (Self-Monitoring, Analysis, and Reporting Technology) is a supplementary component built into many modern storage devices through which devices monitor, store, and analyze the health of their operation.  Statistics are collected (temperature, number of reallocated sectors, seek errors...) which software can use to measure the health of a device, predict possible device failure, and provide notifications on unsafe values.

## Smartmontools
The smartmontools package contains two utility programs for analyzing and monitoring storage devices:  and  and a 3rd database update utility .

Install the  package to use these tools.

SMART support must be available and enabled on each storage device to effectively use these tools. You can use #smartctl to check for and enable SMART support. That done, you can manually #Run a test and #View test results, or you can use #smartd to automatically run tests and email notifications.

## smartctl
smartctl is a command-line tool that "controls the  Self-Monitoring, Analysis and Reporting Technology (SMART) system built into most ATA/SATA and SCSI/SAS hard drives and solid-state drives."

The / option prints a variety of information about a device, including whether SMART is available and enabled:

If SMART is available but not enabled, you can enable it:

 # smartctl --smart=on /dev/device

You may need to specify a device type. For example, specifying  tells smartctl that the device type is ATA, and this prevents smartctl from issuing SCSI commands to that device.

## Run a test
There are three types of self-tests that a device can execute (all are safe to user data):

* Short: runs tests that have a high probability of detecting device problems,
* Extended or Long: the test is the same as the short check but with no time limit and with complete disk surface examination,
* Conveyance: identifies if damage incurred during transportation of the device.
* Selective: tests a range of LBA (read  for more).

The / flag prints which tests a device supports and the approximate execution time of each test. For example:

Use / flag to run a test:

 # smartctl -t short /dev/device
 # smartctl -t long /dev/device
 # smartctl -t conveyance /dev/device
 # smartctl -t select,123+345 /dev/device

## View test results
You can view a device's overall health with the  flag. "If the device reports failing health status, this means either that the device has already failed, or that it is predicting its own failure within the next 24 hours. If this happens get your data off the disk and to someplace safe as soon as you can."

 # smartctl -H /dev/device

You can also view a list of recent test results and detailed information about a device:

 # smartctl -l selftest /dev/device
 # smartctl -x /dev/device

## Generate table with attributes of all disks
 #!/bin/bash
 function drives_csv {
 	declare -A drive_values
 	for d in `smartctl --scan -d scsi | cut -d' ' -f1`; do
 		drive_values["-Drive-----------------"="${drive_valuesfor l in `smartctl -A $d | grep ATTRIBUTE_NAME -A30 | grep -v ATTRIBUTE_NAME | column -H1,3,4,5,6,7,8,9,11,12,13,14,15 -t -o, | sed 's/ //g'`; do
 			key=`echo $l | cut -d',' -f1`
 			value=`echo $l | cut -d',' -f2`
 			existing=${drive_values["$key"}
 			drive_values#~ echo "${key},${drive_values[$key}"
 		done
 	done
 	for key in "${!drive_valuesdo
 		echo "${key}${drive_values[$key}"
 	done | sort
 }
 drives_csv | column -s, -t

## smartd
The smartd daemon monitors SMART statuses and emits notifications when something goes wrong. It can be managed with systemd and configured using the  configuration file. The configuration file syntax is esoteric, and this wiki page provides only a quick reference. For more complete information, read the examples and comments within the configuration file, or read .

## daemon management
To start the daemon, check its status, make it auto-start on system boot and read recent log file entries, simply start/enable the  systemd unit.

## Define the devices to monitor
To monitor for all possible SMART errors on all disks, the following setting must be added in the configuration file.

Note this is the default smartd configuration and the  parameter, which is the default parameter, may be omitted.

To monitor for all possible SMART errors on  and , and ignore all other devices:

To monitor for all possible SMART errors on externally connected disks (USB-backup disks spring to mind) it is prudent to use persistent block device naming:

Note that you may additionally need  for smartd to work.

Now your USB disk will be monitored even if the  path changes during reboot.

## Notifying potential problems
To have an email sent when a failure or new error occurs, use the  option:

To be able to send the email externally (i.e. not to the root mail account) an MTA (Mail Transport Agent) or an MUA (Mail User Agent) will need to be installed and configured. Common MUAs are msmtp and Postfix, but perhaps the easiest dma will suffice. Common MTAs are sendmail and Postfix. It is enough to simply configure S-nail if you do not want anything else, but you will need to follow these instructions.

The  option causes a test email to be sent each time the smartd daemon starts:

Emails can take quite a while to be delivered. To make sure you are warned immediately if your hard drive fails, you may also define a script to be executed in addition to the email sending:

To send an email and a system notification, put something like this into :

 #!/bin/sh
 # Send email
 echo "$SMARTD_MESSAGE" | mail -s "$SMARTD_FAILTYPE" "$SMARTD_ADDRESS"
 # Notify user
 wall "$SMARTD_MESSAGE"

If you are running a desktop environment, you might also prefer having a popup to appear on your desktop. In this case, you can use this script (replace  with the user):

This requires  and a compatible desktop notification server.

You can also put your custom scripts into :

This scripts notifies every logged in users on the system via libnotify.

This script requires ,  and a compatible desktop notification server.

You can execute your custom scripts (remember to make them executable) with

## Power management
If you use a computer under control of power management, you should instruct smartd how to handle disks in low power mode. Usually, in response to SMART commands issued by smartd, the disk platters are spun up. So if this option is not used, then a disk which is in a low-power mode may be spun up and put into a higher-power mode when it is periodically polled by smartd.

More info on smartmontools wiki.

On some devices the  does not work. You get the following error message in syslog:

As an alternative, you can use the  option of smartd. It controls how often smartd spins the disks up to check their status. Default is 30 minutes. To change it, edit .

For more info see .

## Schedule self-tests
smartd can tell disks to perform self-tests on a schedule. The following  configuration will start a short self-test every day between 2-3am, and an extended self test weekly on Saturdays between 3-4am:

## Alert on temperature changes
smartd can track disk temperatures and alert if they rise too quickly or hit a high limit. The following will log changes of 4 degrees or more, log when temp reaches 35 degrees, and log/email a warning when temp reaches 40:

## Complete smartd.conf example
Putting together all of the above gives the following example configuration:

*  smartd scans for disks and monitors all it finds
*  monitor all attributes
*  enable automatic offline data collection
*  enable automatic attribute autosave
*  do not check if disk is in standby, and suppress log message to that effect so as not to cause a write to disk
*  schedule short and long self-tests
*  monitor temperature
*  mail alerts

## update-smart-drivedb
This utility downloads the latest version of  from the smartmontools source repository so that new drives and their parameters are understood.

The downloaded file can replace the default one located at  and is a plaintext file that contains comma separated values for each drive.

If your drive is not yet recognised, it can be submitted upstream.

See  for full command line options.

## Console applications
*

*  (from ) also provides some disk health metrics: in particular, high values in the f_await column mean that the disk does not respond quickly to requests, and might be failing.

## GUI applications
*
*
*
*
*
*

## Troubleshooting
## UAS mode prevents smartmontools usage
In certain situations the Linux "uas" driver disables SAT transfers, which prevents smartmontools (and other tools, e.g. hdparm) from communicating properly with the attached SATA device. For a workaround see https://www.smartmontools.org/wiki/SAT-with-UAS-Linux - which either disables uas mode and falls back to usb-storage mode or overrides the  flag with an  setting at your own risk.
