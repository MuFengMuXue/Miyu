# Hddtemp

Hddtemp is a small utility (with daemon) that gives the hard-drive temperature via S.M.A.R.T. (for drives supporting this feature).

## Installation
Install the  package.

## Usage
Hddtemp requires root user privileges. The command  must be followed by at least one drive's location. You can list several drives separated by spaces:

 # hddtemp /dev/disk/by-id/wwn-0x60015ee0000b237f /dev/sdX2 ... /dev/sdXn

Further usage information is available in .

## Daemon
Running the daemon allows access to the temperature information via TCP/IP as a regular user. This is useful for scripts and system monitors.

The daemon is controlled by .

To get the temperature, connect to the daemon which listens on port 7634.

With :

 $ telnet localhost 7634

With :

 $ nc localhost 7634

Both outputs are similar to:

 |/dev/sda|ST3500413AS|32|C||/dev/sdb|ST2000DM001-1CH164|36|C|

For a better looking statistic:

{{hc|$ nc localhost 7634 |sed 's/|//m' | sed 's/||/ \n/g' | awk -F'|' '{print $1 " " $3 " " $4}'|
/dev/sda 32 C
/dev/sdb 36 C
}}

## Override default disk
The default Hddtemp daemon only monitors . If you have multiple disks, you need to override the default configuration to monitor them.

If you will need to know which hard drives support monitoring, you can check with . Edit :

 ExecStart=
 ExecStart=/usr/bin/hddtemp --daemon --foreground /dev/disk/by-id/wwn-0x60015ee0000b237f /dev/sdb --listen=127.0.0.1

Change the device names to the ones you want to monitor.

After editing, save the file and exit from editor. systemd will apply changes and reload  service automatically.

You can also use the [https://github.com/AndyCrowd/auto-generate-configuration-files/blob/master/gen-customexec.conf-hddtemp.sh auto-generate script will detect supported hard drives using  and print to the stdout.

## Monitors
Hddtemp can be integrated with system monitors. Conky has built in support for Hddtemp in daemon mode. Just enable  and add  to your Conky configuration file.

## Solid State Drives
Hddtemp usually reads field  from the smart data of the drive. In SSDs temperature information is usually stored in field . To obtain these information, one can run:

 # smartctl --all /dev/sdx

or

 # hddtemp --debug /dev/sdx

where  is the drive (use lsblk to check this).

Alternatively, add a new entry in . For example:

 # echo '"Samsung SSD 840 EVO 250GB" 190 C "Samsung SSD 840 EVO 250GB"' >> /etc/hddtemp.db
