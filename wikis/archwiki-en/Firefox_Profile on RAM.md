# Firefox/Profile on RAM

Assuming that there is memory to spare, placing Firefox's cache or complete profile to RAM offers significant advantages. Even though opting for the partial route is an improvement by itself, the latter can make Firefox even more responsive compared to its stock configuration. Benefits include, among others:

* reduced drive read/writes;
* heightened responsive feel;
* many operations within Firefox, such as quick search and history queries, are nearly instantaneous.

To do so we can make use of a tmpfs.

Because data placed therein cannot survive a shutdown, a script responsible for syncing back to drive prior to system shutdown is necessary if persistence is desired (which is likely in the case of profile relocation). On the other hand, only relocating the cache is a quick, less inclusive solution that will slightly speed up user experience while emptying Firefox cache on every reboot.

## Relocate cache to RAM only
See Firefox/Tweaks#Turn off the disk cache.

## Place profile in RAM using tools
Relocate the browser profile to tmpfs so as to globally improve browser's responsiveness. Another benefit is a reduction in drive I/O operations, of which SSDs benefit the most.

Use an active management script for maximal reliability and ease of use. Several are available from the AUR.

## Profile-sync-daemon
See the Profile-sync-daemon page for additional info on it.

## firefox-sync
 is sufficient for a user with a single profile; uses a script and systemd service similar to #The script.

Identify and backup your current Firefox profile as #Before you start suggests.

Use a drop-in snippet to pass the profile as an argument with .

Then start/enable the  user unit.

## Place profile in RAM manually
## Before you start
Before potentially compromising Firefox's profile, be sure to make a backup for quick restoration. First, find out the active profile name by visiting  and checking which profile is in use. Replace ' as appropriate and use  to make a backup:

 $ tar zcvfp ~/firefox_profile_backup.tar.gz ~/.mozilla/firefox/xyz.default

## The script
The script is adapted from verot.net's Speed up Firefox with tmpfs.

The script will first move Firefox's profile to a new static location, make a sub-directory in , softlink to it and later populate it with the contents of the profile. As before, and until the end of this article, replace the bold ' strings with the name of your Firefox profile folder. The only value that absolutely needs to be altered is, again, '.

Be sure that rsync is installed, create:

Make the script executable, then run the following to close Firefox and test it:

 $ killall firefox firefox-bin
 $ ls ~/.mozilla/firefox/
 $ ~/.local/bin/firefox-sync.sh xyz.default

Run Firefox again to gauge the results. The second time the script runs, it will then preserve the RAM profile by copying it back to disk.

## Automation
Seeing that forgetting to sync the profile can lead to disastrous results, automating the process seems like a logical course of action.

## systemd
Create the following script:

then, do a daemon-reload and enable/start the  user unit.

## cron job
Manipulate the user's cron table using :

 $ crontab -e

Add a line to start the script every 30 minutes,

 */30 * * * * ~/.local/bin/firefox-sync.sh xyz.default

or add the following to do so every 2 hours:

 0 */2 * * * ~/.local/bin/firefox-sync.sh xyz.default

## Sync at login/logout
Assuming bash is being used, add the script to the login/logout files:

 $ echo 'bash -c "~/.local/bin/firefox-sync.sh xyz.default > /dev/null &"' | tee -a ~/.bash_logout ~/.bash_login

For zsh, use  and  instead:

 $ echo 'bash -c "~/.local/bin/firefox-sync.sh xyz.default > /dev/null &"' | tee -a ~/.zlog{in,out}
