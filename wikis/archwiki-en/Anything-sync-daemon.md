# Anything-sync-daemon

(asd) is a tiny pseudo-daemon designed to manage user specified directories referred to as sync targets from here on out, in tmpfs and to periodically sync them back to the physical disc (HDD/SSD). This is accomplished via a bind mounting step and an innovative use of rsync to maintain synchronization between a tmpfs copy and media-bound backups. Additionally, asd features several crash recovery features.

The design goals and benefits of asd are:

# Transparent user experience
# Reduced wear to physical drives
# Speed

Since the sync target(s) is relocated into tmpfs (RAM disk), the corresponding onslaught of I/O associated with system usage of them is also redirected from the physical drive to RAM, thus reducing wear to the physical drive and also improving speed and responsiveness. The access time of RAM is on the order of nanoseconds while the access time of physical discs is on the order of milliseconds. This is a difference of six orders of magnitude or 1,000,000 times faster.

## Installation
Install the  package.

## Configuration
User managed settings are defined in  which is included in the package.

* At a minimum, define the sync target(s) to be managed by asd in the  array. Syntax below.
* Optionally uncomment and define the location of tmpfs in the  variable.
* Optionally enable the use of overlayfs to improve sync speed even further and use a smaller memory footprint.  Note that this option requires your kernel be configured to use either the 'overlay' kernel module. See #Overlayfs mode for additional details.

Example:

 WHATTOSYNC=('/var/lib/monitorix' '/srv/http' '/foo/bar')

or

 WHATTOSYNC=(
 '/var/lib/monitorix'
 '/srv/http'
 '/foo/bar'
 )

## Usage
Start/enable . Additionally, a provided resync-timer will run an hourly resync from tmpfs back to the disk. The resync-timer is started automatically with  so there is no need to manually start the timer.

## Preview (parse) mode
Run  to view what what asd will do/is doing based on the entries in . It will also provide useful information such as dir size, paths, and if any recovery snapshots have been created.

## Tips and tricks
## Sync at more frequent intervals
The package provided re-sync timer triggers once per hour. Users may optionally redefine this behavior simply by extending the systemd unit. The example below changes the timer to sync once every ten minutes (note that  needs to be cleared before being re-assigned See  for additional options.

## Overlayfs mode
Overlayfs is a simple union file-system mainlined in the Linux kernel version 3.18.0. Starting with asd version 5.54, overlayfs can be used to reduce the memory footprint of asd's tmpfs space and to speed up sync and unsync operations. The magic is in how the overlay mount only writes out data that has changed rather than the entire sync target. The same recovery features asd uses in its default mode are also active when running in overlayfs mode. Overlayfs mode is enabled by uncommenting the  line in  followed by a restart of the daemon.

## Snapshots
Odds are the "last good" backup of your sync target(s) is just fine still sitting happily on your filesystem. Upon restarting asd (on a reboot for example), a check is performed to see if asd was exited in some corrupted state. If it is detected, asd will snapshot the "last good" backup before it rotates it back into place. Note that, since asd tries to decrease the disk usage, it never really "copies" the full contents of the directory and just uses the hardlinks to the previous files. And during the rsync step, it creates new files so that the previous hardlinks are untouched. So trying to modify the directory during the time asd is trying to backup can leave the directory in some corrupted state.

You will find the snapshot in the same directory as the sync target and it will contain a date-time-stamp that corresponds to the time at which the recovery took place. For example, a  snapshot will be  -- of course, the date_time suffix will be different for you.

To restore your snapshots:

* Stop .
* Confirm that the directories created by asd is not present. If they are, asd did not stop correctly for other reasons.
* Move the "bad" copy of the sync target to a backup (do not blindly delete anything).
* Untar the snapshot archive to the expected sync target.

Example using :

 $ cd /foo
 $ mv bar bar-bad
 $ tar -xvf .bar-backup_asd-crashrecovery-20141221_070112.tar.zstd

## Clean all the snapshot with the clean mode
Running  will delete ALL recovery snapshots that have accumulated. Run this only if you are sure that you want to delete them.

## Support
Post in the [https://bbs.archlinux.org/viewtopic.php?id=139141 discussion thread with comments or concerns.
