# Snapper

Snapper is a tool created by openSUSE's Arvin Schnell that helps with managing snapshots of Btrfs subvolumes, thin-provisioned LVM volumes, and (experimentally) Bcachefs subvolumes. It can create and compare snapshots, revert between snapshots, and supports automatic snapshots timelines.

## Installation
Install the  package.

Additionally, GUIs are available with , , and .

## Creating a new configuration
Before creating a snapper configuration for a Btrfs subvolume, the subvolume must already exist. If it does not, you should create it before generating a snapper configuration.

To create a new snapper configuration named  for the Btrfs subvolume at , run:

 # snapper -c config create-config /path/to/subvolume

This will:

* Create a configuration file at  based on the default template from .
* Create a subvolume at  where future snapshots for this configuration will be stored. A snapshot's path is , where  is the snapshot number.
* Add  to  in .

For example, to create a configuration file for the subvolume mounted at , run:

 # snapper -c root create-config /

At this point, the configuration is active. If your cron daemon is running, snapper will take #Automatic timeline snapshots. If you do not use a cron daemon, you will need to use the systemd service and timer. See #Enable/disable.

See also .

## Taking snapshots
## Automatic timeline snapshots
A snapshot timeline can be created with a configurable number of hourly, daily, weekly, monthly, and yearly snapshots kept. When the timeline is enabled, by default a snapshot gets created once an hour. Once a day the snapshots get cleaned up by the timeline cleanup algorithm. Refer to the  variables in  for details.

## Enable/disable
If you have a cron daemon, this feature should start automatically. To disable it, edit the configuration file corresponding with the subvolume you do not want to have this feature and set:

 TIMELINE_CREATE="no"

If you do not have a cron daemon, you can use the provided systemd units. Start and enable  to start the automatic snapshot timeline. Additionally, start and enable  to periodically clean up older snapshots.

## Set snapshot limits
The default settings will keep 10 hourly, 10 daily, 10 monthly and 10 yearly snapshots. You may want to change this in the configuration, especially on busy subvolumes like . See #Preventing slowdowns.

Here is an example section of a configuration named  with only 5 hourly snapshots, 7 daily ones, no monthly and no yearly ones:

## Change snapshot and cleanup frequencies
If you are using the provided systemd timers, you can edit them to change the snapshot and cleanup frequency.

For example, when editing the , add the following to make the frequency every five minutes, instead of hourly:

 OnCalendar=
 OnCalendar=*:0/5

When editing , you need to change . To make cleanups occur every hour instead of every day, add:

 [Timer
 OnUnitActiveSec=1h

See systemd/Timers and systemd#Drop-in files.

## Manual snapshots
## Single snapshots
By default snapper takes snapshots that are of the single type, having no special relationship to other snapshots.

To take a snapshot of a subvolume manually, do:

 # snapper -c config create --description desc

The above command does not use any cleanup algorithm, so the snapshot is stored permanently or until deleted.

To set a cleanup algorithm, use the  flag after  and choose either , , , or .  sets snapper to periodically remove snapshots that have exceeded a set number in the configuration file. For example, to create a snaphot that uses the  algorithm for cleanup do:

 # snapper -c config create -c number

See #Automatic timeline snapshots for how  snapshots work and see #Pre/post snapshots on how  and  work.

## Pre/post snapshots
The other type of snapshots - pre/post snapshots - are intended to be created as a pair, one before and one after a significant change (such as a system update).

If the significant change is/can be invoked by a single command, then  can be used to invoke the command and automatically create pre/post snapshots:

 # snapper -c config create --command cmd

Alternatively, the pre/post snapshots can be created manually.

First create a pre snapshot:

 # snapper -c config create -t pre -p

Note the number of the new snapshot (it is required to create the post snapshot).

Now perform the actions that will modify the filesystem (*e.g.*, install a new program, upgrade, etc.).

Finally, create the post snapshot, replacing  with the number of the pre snapshot:

 # snapper -c config create -t post --pre-number N

See also #Wrapping pacman transactions in snapshots.

## Snapshots on boot
To have snapper take a snapshot of the  configuration, enable . (These snapshots are of type single.)

## Managing snapshots
## List configurations
To list all configurations that have been created do:

 # snapper list-configs

## List snapshots
To list snapshots taken for a given configuration config do:

 # snapper -c config list

## Restore snapshot
A file may be kept as is when restoring a snapshot, either because was not included in the snapshot (e.g. it resides on another subvolume), or because a filter configuration excluded the file.

## Filter configuration
Some files keep state information of the system, e.g. . Such files should never be reverted. The default configuration in arch linux ensures this. To help users, snapper allows one to ignore these files. Each line in all files  and  specifies a pattern. When snapper computes the difference between two snapshots it ignores all files and directories matching any of those patterns. Note that filters do not exclude files or directories from being snapshotted. For that, use subvolumes or mount points.

See also the Directories That Are Excluded from Snapshots in the SLES 12 SP5 documentation.

## Restore using the default layout
If you are using the default layout of snapper, each snapshot is sub-subvolume in the  directory of a subvolume, e.g. .

To restore  using one of snapper's snapshots, first boot into a live Arch Linux USB/CD.

Mount btrfs root-volume into  using the UUID:

 # mount -t btrfs -o subvol=/ /dev/disk/by-uuid/UUID_of_root_volume /mnt
 # cd /mnt

If the snapper service is running on a running system, stop it. Check if any  are running, then stop them.

Move a broken/old subvolume out of the way e.g.  to :

 # mv @home @home-backup

Find the number of the snapshot that you want to recover (there is one line for each snapshot, so you can easily match up number and date of each snapshot):

Remember the .

Create a new snapshot  from snapshot number  to be restored.

 # btrfs subvolume snapshot @home-backup/.snapshots/number/snapshot @home

Get the directory  back to the healthy subvolume, e.g.

 # mv @home-backup/.snapshots @home/

If subvolid was used for the  mount entry option in fstab, instead of , change subvolid in the  file (assuming that  is the subvolume that is mounted as  in the system) to the new subvolid that can be found with .

Reboot.

Check if your system is working as intended, the delete the old/broken snapshot (e.g. ) if desired. You should check if it contains useful data that you can get back.

## Restore a home directory using srt
srt is the Snapper snapshot restore tool. If you have created a subvolume for each users home directory and you have configured your users  directory and your users snapper profile as described in srt-README.md you can quickly and easily restore snapper snapshots of users home directories using a dialog TUI interface.

## Delete a snapshot
To delete a snapshot number  do:

 # snapper -c config delete N

Multiple snapshots can be deleted at one time. For example, to delete snapshots 65 and 70 of the root configuration do:

 # snapper -c root delete 65 70

To delete a range of snapshots, in this example between snapshots 65 and 70 of the root configuration do:

 # snapper -c root delete 65-70

To free the space used by the snapshot(s) immediately, use :

 # snapper -c root delete --sync 65

To delete all snapshots, the  subvol and the snapper configuration files for a configuration:

 # snapper -c config delete-config

## Access for non-root users
Each config is created with the root user, and by default, only root can see and access it.

To be able to list the snapshots for a given config for a specific user, simply change the value of  in your  file. You should now be able to run  as a normal user.

Eventually, you want to be able to browse the  directory with a user, but the owner of this directory must stay root. Therefore, you should change the group owner by a group containing the user you are interested in, such as  for example:

 # chmod a+rx .snapshots
 # chown :users .snapshots

## Tips and tricks
## Using Snapper as regular user
To enable a regular user to use snapper (e.g. for  snapshots), you can use the  option.

 # snapper -c home_user create-config /home/user
 # snapper -c home_user set-config "ALLOW_USERS=user" SYNC_ACL="yes"

See === Wrapping pacman transactions in snapshots ===

There are a couple of packages used for automatically creating snapshots upon a pacman transaction:

*
*
*
*
*
*  (See Limine#Snapper snapshot integration for Btrfs for details.)

## Booting into read-only snapshots
Users who rely on  or  or  should note that by default, Snapper's snapshots are read-only, and there are some inherent difficulties booting into read-only snapshots. Many services, such as a desktop manager, require a writable  directory, and will fail to start when booted from a read-only snapshot.

To work around this, you can either make the snapshots writable, or use the developer-approved method of booting the snapshots with overlay filesystem, causing the snapshot to behave similar to a live CD environment.

To boot snapshots with overlayfs:

* Ensure  is installed on your system.
* Add  to the end of the  array in . For example:
* Regenerate the initramfs.

Further reading:

* [https://github.com/Antynea/grub-btrfs/blob/master/initramfs/readme.md grub-btrfs README (includes instructions for those who use  instead of )
* Discussion on Github

## Backup non-Btrfs boot partition on pacman transactions
If your  partition is on a non Btrfs filesystem (e.g. an ESP) you are not able to do snapper backups with it. See System backup#Snapshots and /boot partition to copy the boot partition automatically on a kernel update to your Btrfs root with a hook. This also plays nice together with .

## Incremental backup to external drive
Some tools can use snapper to automate backups. See Btrfs#Incremental backup to external drive.

## Suggested filesystem layout
Here is a suggested file system layout for easily restoring the subvolume  that is mounted at root to a previous snapshot:
{| class="wikitable"
|+ Filesystem layout
! Subvolume !! Mountpoint
|-
| @ || /
|-
| @home || /home
|-
| @snapshots || /.snapshots
|-
| @var_log || /var/log
|}

 subvolid=5
   |
   ├── @ -|
   |     contained directories:
   |       ├── /usr
   |       ├── /bin
   |       ├── /.snapshots
   |       ├── ...
   |
   ├── @home
   ├── @snapshots
   ├── @var_log
   └── @...

The subvolumes  are mounted to any other directory that should have its own subvolume.

If you were to restore your system to a previous snapshots of , these other subvolumes will remain unaffected. For example, this allows you to restore  to a previous snapshot while keeping your  unchanged, because of the subvolume that is mounted at .

This layout allows the snapper utility to take regular snapshots of , while at the same time making it easy to restore  from an Arch Live CD if it becomes unbootable.

In this scenario, after the initial setup, snapper needs no changes, and will work as expected.

## Configuration of snapper and mount point
It is assumed that the subvolume  is mounted at root . It is also assumed that  is not mounted and does not exist as folder, this can be ensured by the commands:

 # umount /.snapshots
 # rm -r /.snapshots

Then create a new configuration for . Snapper create-config automatically creates a subvolume  with the root subvolume  as its parent, that is not needed for the suggested filesystem layout, and can be deleted.

 # btrfs subvolume delete /.snapshots

After deleting the subvolume, recreate the directory .

 # mkdir /.snapshots

Now mount  to . For example, for a file system located on :

 # mount -o subvol=@snapshots /dev/sda1 /.snapshots

To make this mount permanent, add an entry to your fstab.

Or if you have an existing fstab entry remount the snapshot subvolume:

 # mount -a

Give the folder  permissions.

This will make all snapshots that snapper creates be stored outside of the  subvolume, so that  can easily be replaced anytime without losing the snapper snapshots.

## Restoring / to its previous snapshot
To restore  using one of snapper's snapshots, first boot into a live Arch Linux USB/CD.

Mount the toplevel subvolume (subvolid=5). That is, omit any  or  mount flags.

Find the number of the snapshot that you want to recover:

 # grep -r '' /mnt/@snapshots/*/info.xml

The output should look like so, there is one line for each snapshot, so you can easily match up number and date of each snapshot.
 /mnt/@snapshots/number/info.xml:  2021-07-26 22:00:00

Remember the .

Now, move  to another location (e.g. ) to save a copy of the current system. Alternatively, simply delete  using .

Create a read-write snapshot of the read-only snapshot snapper took:

 # btrfs subvolume snapshot /mnt/@snapshots/number/snapshot /mnt/@

Where  is the number of the snapper snapshot you wish to restore.

If subvolid was used for the  mount entry option in fstab, instead of , change subvolid in the  file to the new subvolid that can be found with . Also change the boot loader configuration such as , if it contains the subvolid.

Finally, unmount the top-level subvolume (ID=5), then mount  to  and your ESP or boot partition to the appropriate mount point. Change root to your restored snapshot in order to regenerate your initramfs image.

Your  has now been restored to the previous snapshot. Now just simply reboot.

## Restoring other subvolumes to their previous snapshot
See #Restore snapshot.

## Deleting files from snapshots
If you want to delete a specific file or folder from past snapshots without deleting the snapshots themselves,  is a script that adds this functionality to Snapper. This script can also be used to manipulate past snapshots in a number of other ways that Snapper does not currently support.

If you want to remove a file without using an extra script, you just need to make your snapshot subvolume read-write, which you can do with:

 # btrfs property set /path/to/.snapshots//snapshot ro false

Verify that :

 # btrfs property get /path/to/.snapshots//snapshot
 ro=false

You can now modify files in  like normal.  You can use a shell loop to work on your snapshots in bulk.

## Preventing slowdowns
Keeping many snapshots for a large timeframe on a busy filesystem like , where many system updates happen over time, can cause serious slowdowns. You can prevent it by:

* Creating subvolumes for things that are not worth being snapshotted, like , , , and .
* Editing the default settings for hourly/daily/monthly/yearly snapshots when using #Automatic timeline snapshots.

## updatedb
By default,  (see locate) will also index the  directory created by snapper, which can cause serious slowdown and excessive memory usage if you have many snapshots. You can prevent  from indexing over it by editing:

## Disable quota groups
There are reports of significant slow downs being caused by quota groups, if for instance  takes many minutes to return a result this could be the cause. See To determine whether or not quota groups are enabled use the following command:

 # btrfs qgroup show /

Quota groups can then be disabled with:

 # btrfs quota disable /

## Count the number of snapshots
If disabling quota groups did not help with slow down, it may be helpful to count the number of snapshots, this can be done with:

 # btrfs subvolume list -s / | wc -l

## Create subvolumes for user data and logs
It is recommended to store directories on their own subvolume, rather than the root subvolume , if they contain user data e.g. emails, or logs. That way if a snapshot of  is restored, user data and logs  will not also be reverted to the previous state. A separate timeline of snapshots can be maintained for user data. It is not recommended to create snapshots of logs in . This makes it easier to troubleshoot.

Directories can also be skipped during a restore using #Filter configuration. See the [https://documentation.suse.com/sles/12-SP5/html/SLES-all/cha-snapper.html#snapper-dir-excludes SLES documentation for examples and reasons to skip certain paths.

## Cleanup based on disk usage
## Troubleshooting
## Snapper logs
Snapper writes all activity to  - check this file first if you think something goes wrong.

If you have issues with hourly/daily/weekly snapshots, the most common cause for this so far has been that the cronie service (or whatever cron daemon you are using) was not running.

## IO error
If you get an 'IO Error' when trying to create a snapshot please make sure that the .snapshots directory associated to the subvolume you are trying to snapshot is a subvolume by itself.

Another possible cause is that .snapshots directory does not have root as an owner (You will find  in the ).

## Orphaned snapshots causing wasted disk space
It is possible for snapshots to get 'lost', where they still exist on disk but are not tracked by snapper. This can result in a large amount of wasted, unaccounted-for disk space. To check for this, compare the output of

 # snapper -c  list
to
 # btrfs subvolume list -o /.snapshots

Any subvolume in the second list which is not present in the first is an orphan and can be deleted manually.
