# Full system backup with tar

This article will show you how to do a full system backup with tar.

Backing up with tar has the advantages of simplicity and using compression that can help save disk space. The process only requires a few steps, they are:

# Boot from a LiveCD
# Change root to the Linux install
# Mount additional (if any) partitions/drives
# Add exclusions
# Use the backup script to backup

To minimize downtime the backup can alternatively be performed on a running system using LVM snapshots,
if all filesystems reside on LVM volumes.

## Boot with LiveCD
Many Linux bootable CDs, USBs, etc. have the ability to let you change root to your install. While changing root is not necessary to do a backup, it provides the ability to run the script without the need to transfer it to a temporary drive or having to locate it on the filesystem. The Live medium must be of the same architecture that your Linux install currently is (i.e. i686 or x86_64).

## Changing root
Firstly, you should have a scripting environment set up on your current Linux install. This means that you are able to execute any scripts that you may have as if they are regular programs. Refer to this article for more information on setting up a scripting environment. The next step is to change root. When you change root, you do not need to mount any temporary file systems (, , and ). These temporary file systems get populated on boot, and it is not recommended to back them up because doing so can interfere with the normal (and necessary) population process, which can change on any upgrade. To change root, you will need to mount your current Linux install's root partition. For example:

 # mkdir /mnt/arch
 # mount /dev/your-partition-or-drive

Use  to list your partitions and drives. Now chroot:

 # cd /mnt/arch
 # chroot . /bin/bash

This example uses Bash but you can use other shells if available. You will now be in your scripted environment (this is provided that you have your  sourced on entry):

## Mount other partitions
Other partitions that you use (if any) will need to be mounted in their proper places (e.g. if you have a separate  partition).

## Exclude file
tar has the ability to ignore specified files and directories. The syntax is one definition per line. tar also has the capability to understand regular expressions (regexps). For example:

## Backup script
Backing up with GNU  is straight-forward process. Here is a basic script that can do it and provide a couple checks. You will need to modify this script to define your backup location and exclude file (if you have one), and then run this command after you have ed and mounted all your partitions.

{{bc|1=
#!/bin/bash
# full system backup

# Backup destination
backdest=/opt/backup

# Labels for backup name
#PC=${HOSTNAME}
pc=pavilion
distro=arch
type=full
date=$(date "+%F")
backupfile="$backdest/$distro-$type-$date.tar.zst"

# Exclude file location
prog=${0##*/} # Program name from filename
excdir="/home//.bin/root/backup"
exclude_file="$excdir/$prog-exc.txt"

# Check if chrooted prompt.
echo -n "First chroot from a LiveCD.  Are you ready to backup? (y/n): "
read executeback

# Check if exclude file exists
if [ ! -f $exclude_file ]; then
  echo -n "No exclude file exists, continue? (y/n): "
  read continue
  if [ $continue == "n" ]; then exit; fi
fi

if [ $executeback = "y" ]; then
  # -p, --acls and --xattrs store all permissions, ACLs and extended attributes.
  # Without both of these, many programs will stop working!
  # It is safe to remove the verbose (-v) flag. If you are using a
  # slow terminal, this can greatly speed up the backup process.
  tar --exclude-from="$exclude_file" --acls --xattrs -cpvaf "$backupfile" /
fi
}}

## Restoring
To restore from a previous backup, mount all relevant partitions, change the current working directory to the root directory, and execute

 # tar --acls --xattrs-include=* -xpaf backupfile

replacing backupfile with the backup archive. Removing files that had been added since the backup was made must be done manually. Recreating the filesystem(s) is an easy way to do this.

## Tips and tricks
## Backup with parallel compression
To back up using parallel compression (SMP), use  which is multithreaded by default:

 # tar -cvaf /path/to/chosen/directory/etc-backup.tar.xz /etc

Store  on one or more offline media, such as a USB stick, external hard drive, or CD-R. Make sure to occasionally verify the integrity of the backup process by comparing original files and directories with their backups. It's possible to maintain a list of hashes of the backed up files to make the comparison quicker.
Restore corrupted  files by extracting the  file in a temporary working directory, and copy over individual files and directories as needed. To restore the entire  directory with all its contents, execute the following command as root:

 # tar -xvaf etc-backup.tar.xz -C /
