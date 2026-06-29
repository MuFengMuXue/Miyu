# Rsync

rsync is an open source utility that provides fast incremental file transfer.

## Installation
Install the  package.

rsync must be installed on both the source and the destination machine.

## Front-ends
*
*
*

Other tools using rsync are ,  and .

## As cp/mv alternative
 can be used as an advanced alternative for the  or  command, especially for copying larger files:

 $ rsync -P source destination

The  option is the same as , which keeps partially transferred files and shows a progress bar.

You may want to use the / option to recurse into directories.

Files can be copied locally as with cp, but the motivating purpose of rsync is to copy files remotely, i.e. between two different hosts. Remote locations can be specified with a host-colon syntax:

 $ rsync source host:destination

or

 $ rsync host:source destination

Network file transfers use the SSH protocol by default and  can be a real hostname or a predefined profile/alias from .

Whether transferring files locally or remotely, rsync first creates a file-list containing information (by default, it is the file size and last modification timestamp) which will then be used to determine if a file needs to be constructed. For each file to be constructed, a weak and strong checksum is found for all blocks such that each block is of length S bytes, non-overlapping, and has an offset which is divisible by S. Using this information a large file can be constructed using rsync without having to transfer the entire file. For a more detailed practical and mathematical explanation refer to how rsync works and the rsync algorithm, respectively.

To use sane defaults quickly, you could use some aliases:
{{bc|1=
cpr() {
  rsync --archive -hh --partial --info=stats1,progress2 --modify-window=1 "$@"
}
mvr() {
  rsync --archive -hh --partial --info=stats1,progress2 --modify-window=1 --remove-source-files "$@"
} }}

* : output numbers in a human-readable format
* :  displays rsync transfer statistics with verbosity level 1.  prints total transfer progress as opposed to per-file transfer progress ()
* : when comparing the timestamps of two files, treat their timestamps as being equivalent if their timestamps have a difference of less than 1 second
* : remove files from the source directory after they have been successfully synced

## Trailing slash caveat
Arch by default uses GNU cp (part of GNU ). However, rsync follows the convention of BSD cp, which gives special treatment to source directories with a trailing slash "/". Whereas

 $ rsync -r source destination

creates a directory "destination/source" with the contents of "source", the command

 $ rsync -r source/ destination

copies all of the files in "source/" directly into "destination", with no intervening subdirectory - just as if you had invoked it as

 $ rsync -r source/. destination

This behavior is different from that of GNU cp, which treats "source" and "source/" identically (but not "source/."). Also, some shells automatically append the trailing slash when tab-completing directory names. Because of these factors, there can be a tendency among new or occasional rsync users to forget about rsync's different behavior, and inadvertently create a mess or even overwrite important files by leaving the trailing slash on the command line.

Thus it can be prudent to use a wrapper script to automatically remove trailing slashes before invoking rsync:

 #!/bin/bash
 new_args=()
 for i in "${@}"; do
     case "${i}" in
         /)
             i="/"
         ;;
         */)
             i="${i%/}"
         ;;
         esac
     new_args+=("${i}")
 done
 exec rsync "${new_argsThis script can be put somewhere in the path, and aliased to rsync in the shell init file.

## As a backup utility
The rsync protocol can easily be used for backups, only transferring files that have changed since the last backup. This section describes a very simple scheduled backup script using rsync, typically used for copying to removable media.

## Automated backup
For the sake of this example, the script is created in the  directory, and will be run on a daily basis if a cron daemon is installed and properly configured. Configuring and using cron is outside the scope of this article.

First, create a script containing the appropriate command options:

* : indicates that files should be archived, meaning that most of their characteristics are preserved (but not ACLs, hard links or extended attributes such as capabilities)
* : means files deleted on the source are to be deleted on the backup as well

Here,  should be changed to what needs to be backed-up (e.g. ) and  is where the backup should be saved (e.g. ).

Finally, the script must be executable.

## Automated backup with SSH
If backing-up to a remote host using SSH, use this script instead:

* : tells rsync to use SSH
* : is the user on the host
* : groups all these options  (recursive, links, perms, times, group, owner, devices)

## Automated backup with NetworkManager
This script starts a backup when network connection is established.

First, create a script containing the appropriate command options:

* : group all this options  recursive, links, perms, times, group, owner, devices
* : read the relative path of  from this file
* : limit I/O bandwidth; Kilo-bytes per second

The script must be owned by root (see NetworkManager#Network services with NetworkManager dispatcher for details).

## Automated backup with systemd and inotify
Instead of running time interval backups with time based schedules, such as those implemented in cron, it is possible to run a backup every time one of the files you are backing up changes.  units use  to monitor the filesystem, and can be used in conjunction with  files to start any process (in this case your rsync backup) based on a filesystem event.

First, create the  unit that will monitor the files you are backing up:

Then create a  file that will be activated when it detects a change. By default a service file of the same name as the path unit (in this case ) will be activated, except with the  extension instead of  (in this case ).

Now all you have to do is enable/start  like a normal systemd service and it will start monitoring file changes and automatically start .

## Differential backup on a week
This is a useful option of rsync, resulting in a full backup (on each run) and keeping a differential backup copy of changed files only in a separate directory for each day of a week.

First, create a script containing the appropriate command options:

The  option implies  and updates destination files in-place.

## Snapshot backup
The same idea can be used to maintain a tree of snapshots of your files. In other words, a directory with date-ordered copies of the files. The copies are made using hardlinks, which means that only files that did change will occupy space. Generally speaking, this is the idea behind Apple's TimeMachine.

This basic script is easy to implement and creates quick incremental snapshots using the  option to hardlink unchanged files:

{{hc|/usr/local/bin/snapbackup.sh|
#!/bin/sh

# Basic snapshot-style rsync backup script

# Config
OPT="-aPh"
LINK="--link-dest=/snapshots/username/last/"
SRC="/home/username/files/"
SNAP="/snapshots/username/"
LAST="/snapshots/username/last"
date=`date "+%Y-%b-%d:_%T"`

# Run rsync to create snapshot
rsync $OPT $LINK $SRC ${SNAP}$date

# Remove symlink to previous snapshot
rm -f $LAST

# Create new symlink to latest snapshot for the next backup to hardlink
ln -s ${SNAP}$date $LAST
}}

There must be a symlink to a full backup already in existence as a target for . If the most recent snapshot is deleted, the symlink will need to be recreated to point to the most recent snapshot. If  does not find a working symlink, rsync will proceed to copy all source files instead of only the changes.

A more sophisticated version keeps an up-to-date full backup  and in case a certain number of files has changed since the last full backup, it creates a snapshot  of the current full-backup utilizing  to hardlink unchanged files:

To make things really, really simple this script can be run from a systemd/Timers unit.

## Full system backup
This section is about using rsync to transfer a copy of the entire  tree, excluding a few selected directories. This approach is considered to be better than disk cloning with  since it allows for a different size, partition table and filesystem to be used, and better than copying with  as well, because it allows greater control over file permissions, attributes, Access Control Lists and extended attributes.

rsync will work even while the system is running, but files changed during the transfer may or may not be transferred, which can cause undefined behavior of some programs using the transferred files. For mitigation log out all users and shut down all programs and databases.

This approach works well for migrating an existing installation to a new hard drive or SSD.

Run the following command as root to make sure that rsync can access all system files and preserve the ownership:

 # rsync -aAXHv --exclude='/dev/*' --exclude='/proc/*' --exclude='/sys/*' --exclude='/tmp/*' --exclude='/run/*' --exclude='/mnt/*' --exclude='/media/*' --exclude='/lost+found/' / /path/to/backup

By using the  set of options, the files are transferred in archive mode which ensures that symbolic links, devices, permissions, ownerships, modification times, ACLs, and extended attributes are preserved, assuming that the target file system supports the feature. The option  preserves hard links, but uses more memory.

The  option causes files/directories that match the given patterns to be excluded. Instead or in conjunction, the  option excludes files/directories that match patterns (one per line) in , similar to the example described in #Advanced usage of filter rules but without the / syntax.

The directories , , , , and  are included in the above command, but the contents of those directories are excluded. This is because they are populated on boot, but the directories themselves are not created.  is filesystem-specific. Quoting the exclude patterns will avoid expansion by the shell, which is necessary, for example, when backing up over SSH. Ending the excluded paths with  ensures that the directories themselves are created if they do not already exist.

You may want to include additional rsync options, or remove some, such as the following. See  for the full list.

* If you run on a system with very low memory, consider removing  option; however, it should be no problem on most modern machines. There can be many hard links on the file system depending on the software used (e.g. if you are using Flatpak). Many hard links reside under the  directory.
* You may want to add rsync's  option if you are running this multiple times to the same backup directory. In this case make sure that the source path does not end with , or this option will only have effect on the files inside the subdirectories of the source directory, but it will have no effect on the files residing directly inside the source directory.
* If you use any sparse files, such as virtual disks, Docker images and similar, you should add the  option.
* The  option will disable mapping of user and group names; instead, numeric group and user IDs will be transfered. This is useful when backing up over SSH or when using a live system to backup different system disk.
* Choosing  option instead of  will show the overall progress info and transfer speed instead of the list of files being transferred.
* To avoid crossing a filesystem boundary when recursing, add the option /. This will prevent backing up any mount point in the hierarchy.

## Restore a backup
If you wish to restore a backup, use the same rsync command that was executed but with the source and destination reversed (you may also want to add a trailing slash to the source). If you used  options you should probably remove those for the restore command.

## Advanced usage of filter rules
Instead of specifying include and exclude rules separately rsync can read all of these from a single filter file. rsync then processes the rules in a top-down order; the first matching rule wins.

 is a special rsync pattern which matches a folder and all of its contents recursively.

Check  and  for more details.

Then run rsync with:

 $ rsync -aAXHv --filter="merge backup.filter" $SRC $DEST

The key word is the  parameter which will take the filter file and parse the rules in order for each sync-ed file.

## Copy from list of paths
An alternative to the #Advanced usage of filter rules method is to use the  option. This can take an input from a text file containing a list of directory or file paths, with each entry being separated by new lines. It should be noted that the  flag must manually be specified for this option if the user wants recursive directory copying, even when  is already included.

For example, a list of directories and all recursive directories can be archived with the following:

 $ rsync -aAXHvr --files-from="dir_list.txt" $SRC $DEST

## File system cloning
rsync provides a way to do a copy of all data in a file system while preserving as much information as possible, including the file system metadata. It is a procedure of data cloning on a file system level where source and destination file systems do not need to be of the same type. It can be used for backing up, file system migration or data recovery.

rsync's archive mode comes close to being fit for the job, but it does not back up the special file system metadata such as access control lists, extended attributes or sparse file properties. For successful cloning at the file system level, some additional options need to be provided:

 rsync -qaAXHSU SOURCE_DIR DESTINATION_DIR

And their meaning is (from the manpage):

 --acls, -A               preserve ACLs (implies --perms)
 --xattrs, -X             preserve extended attributes
 --hard-links, -H         preserve hard links
 --sparse, -S             turn sequences of nulls into sparse blocks
 --atimes, -U             preserve access (use) times

Additionally, use  if you have other filesystems mounted under the tree that you want to exclude from the copy.

The produced copy can be simply reread and checked (for example after a data recovery attempt) at the file system level with 's recursive option:

 diff -r SOURCE_DIR DESTINATION_DIR

It is possible to do a successful file system migration by using rsync as described in this article and updating the fstab and boot loader as described in Migrate installation to new hardware. This essentially provides a way to convert any root file system to another one.

## As a daemon
rsync can be run as daemon on a server listening on TCP port .

Edit the template , configure a share and start the .

Usage from client, e.g. list server content:

 $ rsync rsync://server/share

transfer file from client to server:

 $ rsync local-file rsync://server/share/

Consider opening TCP port  in the firewall, and using user authentication.

## Example configuration
## Sharing from a list of files
Inside the file list, all the intermediary paths are necessary, except when the  wildcard is used:
