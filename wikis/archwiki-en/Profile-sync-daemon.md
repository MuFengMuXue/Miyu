# Profile-sync-daemon

(psd) is a tiny pseudo-daemon designed to manage browser profile(s) in tmpfs and to periodically sync back to the physical disc (HDD/SSD). This is accomplished by an innovative use of rsync to maintain synchronization between a tmpfs copy and media-bound backup of the browser profile(s). Additionally, psd provides several crash recovery features.

The design goals and benefits of psd are:

# Transparent user experience
# Reduced wear to physical drives
# Speed

Since the profile(s), browser cache, etc. are relocated into tmpfs (RAM disk), the corresponding I/O associated with using the browser is also redirected from the physical drive to RAM, thus reducing wear to the physical drive and also greatly improving browser speed and responsiveness.

Starting with psd version 7,  is used to reduce the memory footprint of psd's tmpfs space and to speed up sync and unsync operations. The magic is in how the overlay mount only writes out data that has changed rather than the entire profile.

## Installation
Install the  package.

## Configuration
When you run psd for the first time, it will create  (referred to hereafter as the configuration file) which contains all settings. You can run the  command before using  to create this file without starting synchronization.

* Optionally define which browsers are to be managed in the  array. If none are defined, the default is all detected browsers.
* Optionally disable the use of crash-recovery snapshots (not recommended). Do this in the  variable.
* Optionally define the number of crash-recovery snapshots to keep. Do this in the  variable.

Example: Let us say that Chromium, Opera and Firefox are installed but only Chromium and Opera are to be sync'ed to tmpfs since the user keeps Firefox as a backup browser and it is seldom used:

 BROWSERS=(chromium opera)

Beginning with version 7 of psd, support for  is required. This feature requires at least a Linux kernel version of 4.18 or greater.

## Supported browsers
Currently, the following browsers are auto-detected and managed:

* Chromium
*
* Epiphany
*
* Firefox (all flavors including stable, beta, and nightly)
*
*
*
*
* Luakit
* Opera
* Otter Browser
*
* Qutebrowser
*
*
*
*

## Usage
Start/enable the  user unit. Additionally, a provided resync-timer will run an hourly resync from tmpfs back to the disk. The resync-timer is started automatically with  so there is no need to manually start the timer.

## Preview (parse) mode
Run  to view what psd will do/is doing based on . It will also provide useful information such as profile size, paths, and if any recovery snapshots have been created.

## Tips and tricks
## Sync at more frequent intervals
The package provided re-sync timer triggers once per hour. Users may optionally redefine this behavior simply by extending the systemd unit. The example below changes the timer to sync once every ten minutes (note that  needs to be cleared before being re-assigned See  for additional options.

## Allocate more memory to accommodate profiles in /run/user/xxxx
The standard way of controlling the size of  is the RuntimeDirectorySize directive in  (see  for more). By default, 10% of physical memory is used but one can increase it safely. Remember that tmpfs only consumes what is actually used; the number specified here is just a maximum allowed.

## Snapshots
Odds are the "last good" backup of your browser profiles is just fine still sitting happily on your filesystem. Upon restarting psd (on a reboot for example), a check is performed to see if the symlink to the tmpfs copy of your profile is valid. If it is invalid, psd will snapshot the "last good" backup before it rotates it back into place. This is more for a sanity check that psd did no harm and that any data loss was a function of something else.

You will find the snapshot in the same directory as the browser profile and it will contain a date-time-stamp that corresponds to the time at which the recovery took place. For example, chromium will be  -- of course, the date_time suffix will be different for you.

To restore your snapshots:

* Stop the  user unit.
* Confirm that there is no symlink to the tmpfs browser profile directory. If there is, psd did not stop correctly for other reasons.
* Move the "bad" copy of the profile to a backup (do not blindly delete anything).
* Copy the snapshot directory to the name that browser expects.

Example using Chromium:

 $ mv ~/.config/chromium ~/.config/chromium-bad
 $ cp -a ~/.config/chromium-backup-crashrecovery-20130912_153310 ~/.config/chromium

At this point you can launch chromium which will use the backup snapshot you just copied into place. If all is well, close the browser and restart psd. You may safely delete  at this point.

## Clean all the snapshot with the clean mode
Running  will delete ALL recovery snapshots that have accumulated. Run this only if you are sure that you want to delete them.

## Support
Post in the [https://bbs.archlinux.org/viewtopic.php?pid=1026974 discussion thread with comments or concerns.
