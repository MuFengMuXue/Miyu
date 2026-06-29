# Hdparm

hdparm and sdparm are command line utilities to set and view hardware parameters of hard disk drives. hdparm can also be used as a simple benchmarking tool.

Originally, hdparm was created for IDE disks and sdparm for SCSI disks. Nowadays, storage device interfaces are an enhanced mixture of both IDE and SCSI, so  and  complement each other.

## Installation
Install the  package. For use with SCSI devices, install the  package.

## Usage
## Disk info
To get information about hard disks, run the following:

 # hdparm -I /dev/sda

## Benchmarking
hdparm can be used for Benchmarking#hdparm.

## Power management configuration
Modern hard drives support numerous power management features. The most common ones are summarized in the following table. See  for the complete list.

{| class="wikitable"
! Parameter !! Description
|-
|  || Set the Advanced Power Management feature. Possible values are between 1 and 255, low values mean more aggressive power management and higher values mean better performance. Values from 1 to 127 permit spin-down, whereas values from 128 to 254 do not. A value of 255 completely disables the feature.
|-
|  || Set the standby (spindown) timeout for the drive. The timeout specifies how long to wait in idle (with no disk activity) before turning off the motor to save power. The value of 0 disables spindown, the values from 1 to 240 specify multiples of 5 seconds and values from 241 to 251 specify multiples of 30 minutes.
|-
|  || Set the Automatic Acoustic Management feature. Most modern hard disk drives have the ability to speed down the head movements to reduce their noise output. The possible value depends on the disk, some disks may not support this feature.
|}

To query current value of , pass the parameter without a value:

 # hdparm -B /dev/sda

To apply different value, for example set APM to 127:

 # hdparm -B 127 /dev/sda

## Write cache
Write caching is the process of temporarily caching files in the drive's embedded memory before writing them to the disk, which is essentially a performance boost. Write cache is a feature provided by most hard drives, and it is enabled by default in most cases. To check if that's the case, run:

 # hdparm -W /dev/sdX

If it is disabled, one may enable it with:

 # hdparm -W 1 /dev/sdX

Conversely, to disable it, use:

 # hdparm -W 0 /dev/sdX

For an example of forcing disk write caches to be persistently disabled on a machine, we can create a local script  that uses hdparm and  to periodically probe all attached disks and apply the desired setting. This will disable write caches on boot when the service is first ran, and can catch within 30 seconds any infrequent cases that re-enable the write cache, i.e. disk additions and system suspensions.

Make sure the script is executable. We can then run this daemon under systemd by creating a local unit:

Enable  to start it at boot.

## Power off a hard disk drive
A typical usage case, where such a feature is looked for, is with disks connected to a cheap external USB/SATA/FireWire enclosure, or bridge. If it does not properly issue a stop command to the drive when turning off the power switch, the drive is forced to do an emergency head retract. Regularly doing that will, sooner or later, break the drive. One solution is, after one is sure the data has been written to the media, to run a command to power off the drive:

 # hdparm -Y /dev/sdX

## Tips and tricks
## Querying the status of the disk without waking it up
Invoking hdparm with the query option is known to wake-up some drives.  In this case, consider  provided by smartmontools to query the device which will not wake up a sleeping disk. For example:

## Persistent configuration using udev rule
To make the setting persistent across reboot or sleep, one can use a udev rule:

Because a disk device can be assigned randomly to a changing , the disk can also be identified by its serial as explained in Udev#Identifying a disk by its serial.

Systems with multiple hard drives can apply the rule in a flexible way according to some criteria. For example, to apply power-saving settings to all rotational drives (hard disk with rotational head, excluding in particular solid state drives), use the following rule:

{{hc|/etc/udev/rules.d/69-hdparm.rules|2=ACTION=="addchange", SUBSYSTEM=="block", ENV{DEVTYPE}=="disk", KERNEL=="sd*", ATTRS{queue/rotational}=="1", RUN+="/usr/bin/hdparm -B 127 $env{DEVNAME}"}}

## Reapplying configuration after wakeup
If the configuration is lost after system suspension/hibernation, it can be reapplied using systemd-sleep.

Put a script into  and make it executable:

## Putting a drive to sleep directly after boot
A device which is rarely needed can be put to sleep directly at the end of the boot process. This does not work with the above udev rule because it happens too early. In order to issue the command when the boot is completed, just create a systemd service and enable it:

## Working with unsupported hardware
Some drives do not support spin down via hdparm. A diagnostic error message similar to the following is a good indication this is the case:

For some other drives, the hdparm command is acknowledged but the drive do not respect the parameters (either APM or spin down timer). This was observed with a Toshiba P300 (model HDWD120) HDD.

Such drives can be spun down using  which ships with a systemd service. One need to edit  and the  value, then start and enable .

Example using a 10 min idle time for  and a 1 min idle time for :

 HD_IDLE_OPTS="-i 0 -a /dev/sda -i 600 -a /dev/disk/by-uuid/01CF0AC9AA5EAF70 -i 60"

the leading  parameter indicates that hd-idle is disabled on other drives.

## Power management for Western Digital hard disk drives
Western Digital hard drives have a special idle3 timer which controls how long the drive waits before positioning its heads in their park position and entering a low power consumption state. There are different ways to amend the idle3 state:

* hdparm features the  flag:
** Specify a value of zero () to disable the WD idle3 timer completely: , which is not recommended by  though—hdparm developers recommend a setting of 30 seconds for Linux use.
** See #Persistent configuration using udev rule to automatically use this parameter on supported hard drives.
* idle3ctl—provided by the  package:
** Disable the timer completely: .
** Set the timer to 30 seconds: .

## Troubleshooting
## APM level reset after suspend
The APM level may get reset after a suspend requiring it to be re-executed after each resume. This can be automated with the following systemd unit (adapted from a forum thread):

Alternatively, create a hook in /usr/lib/systemd/system-sleep.
