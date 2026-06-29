# Timeshift

Timeshift is a tool originally created by Tony George, that is now part of the Xapp project.

Timeshift helps create incremental snapshots of the file system at regular intervals, which can then be restored at a later date to undo all changes to the system.

It supports rsync snapshots for all filesystems, and uses the built-in snapshot features for Btrfs drives configured to use the  and  subvolume layout for root and home directories respectively.

## Installation
Install the  package and enable/start your chosen cron scheduler (see cron#Configuration). This will ensure that snapshots scheduled within the Timeshift application run as intended.

Alternatively,  can be installed instead of using a cron scheduler.

## Configuration
Timeshift can be fully configured using the  graphical user interface, but if running graphical applications is not an option, its configuration file can be edited directly. Copy the template file  to  and edit settings you want to change.

Here is an example of a rsync-based configuration with three weekly snapshots and rules to exclude the ,  and  directories, while including the  directory and its content into the snapshots:

{{hc|/etc/timeshift/timeshift.json|
{
    "backup_device_uuid" : "root-partition UUID",
    "do_first_run" : "false",
    "btrfs_mode" : "false",
    "include_btrfs_home_for_backup" : "false",
    "include_btrfs_home_for_restore" : "false",
    "schedule_weekly" : "true",
    "count_weekly" : "3",
    "date_format" : "%Y-%m-%d %H:%M:%S",
    "exclude" : [
        "/var/cache/**",
        "/var/tmp/**",
        "+ /home/archie/.config/***",
        "/home/archie/**"
    ],
    "exclude-apps" : }
}}

## Usage
Snapshots can be managed through the  graphical user interface, as well as the  command-line user interface tool.

Listing snapshots:

 # timeshift --list

Creating a snapshot:

 # timeshift --create --comments "comment"

Restoring a snapshot:

 # timeshift --restore --snapshot "snapshot"

Deleting a snapshot:

 # timeshift --delete --snapshot "snapshot"

## Configuring btrfs snapshots
Timeshift requires a [https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/SysadminGuide.html#Flat flat Btrfs layout with subvolumes for  and optionally  being named as  and .

## Making a supported Btrfs layout during installation
The instruction below assumes that you are following the installation guide.

Right after the Btrfs filesystem is created and mounted to , create subvolumes named  and . Unmount  and mount the subvolumes using the  parameter:

 # mount -o subvol=@ /dev/root_partition /mnt
 # mount --mkdir -o subvol=@home /dev/root_partition /mnt/home

Proceed with the installation as normal.

## Converting an installed system to the compatible Btrfs layout
The following instructions assume that the system is installed in the top-level (ID=5) subvolume, you may need to adapt these depending on your configuration.

Start by creating a snapshot of your root named  and mount it to :

 # btrfs subvolume snapshot / /@
 # mount -o subvol=@ /dev/root-partition /mnt

Create the  subvolume, move the user data into it and mount it at :

 # mv /mnt/home/* /@home
 # mount -o subvol=@home /mnt/home

Mount your EFI system partition to  if you have one. Chroot into , reinstall and reconfigure the boot loader. For an amd64 EFI system with GRUB, just running:

 # grub-install --target=x86_64-efi --efi-directory=esp --bootloader-id=GRUB
 # grub-mkconfig -o /boot/grub/grub.cfg

would be enough, however if you use any other bootloader that has no automatic configuration, you need to manually add  to the kernel options (see Kernel parameters#Boot loader configuration).

Edit the fstab file so that the entry for  contains  mount option, and add an entry for  with  mount option. Example of how it may look like:

 ...
 UUID=d8efe946-8d28-40d6-943a-70af51a8d2cd  /       btrfs   defaults,subvol=@      0    0
 UUID=d8efe946-8d28-40d6-943a-70af51a8d2cd  /home   btrfs   defaults,subvol=@home  0    0
 ...

Exit the chroot, reboot and confirm with the  command that everything is done correctly. Mount the toplevel using  and cleanup the old root.

## Excluding directories from Btrfs snapshots
Btrfs mode does not support the exclusion of individual files and directories from snapshots. However, it is possible to work around this to some extent by creating additional subvolumes at the top-level and mounting them in place of directories, which will effectively exclude them.

Here is an example of how to exclude the  directory, to prevent the system logs from rolling back and make it easy to inspect them after a system breakage:

Start by mounting the top-level and create the subvolume inside of it:

 # mount -o subvolid=5 /dev/root-partition /mnt
 # btrfs subvolume create /mnt/@var_log

Add a new entry for it to fstab:

 UUID=root-partition-UUID  /var/log   btrfs   defaults,subvol=@var_log  0    0

## GRUB entries for btrfs snapshots
To add snapshots to the GRUB menu each time GRUB configuration is generated, install the  package. It comes with the , which can be enabled to automatically update the GRUB configuration whenever a new snapshot is created.

To make grub-btrfsd work with Timeshift, edit the service by running:

 # systemctl edit --full grub-btrfsd

and change the line:

 ExecStart/usr/bin/grub-btrfsd /.snapshots --syslog

to:

 ExecStart/usr/bin/grub-btrfsd --syslog --timeshift-auto

After saving the changes, restart the service.

## Troubleshooting
## Timeshift GUI not launching on Wayland
Xwayland will only allow the user who started the X server to connect clients to it (see Privilege elevation for graphical applications#XWayland).

Due to Timeshift requiring root permissions, attempting to launch the Timeshift GUI via an application launcher or a terminal with the command  will result in an error containing .

Users encountering this error may also be presented with their authentication agent prompting for a password, only to find that the Timeshift GUI does not launch after entering the password. This is because the command  requires the  package: install it.

If GTK cannot open your display and you get a warning message in the terminal, it means that the root user need the access to the graphical X server (Display :0, :1, etc.)

Normally only the user who started the graphical session can open new windows in your compositor and since your need to execute  with the root user, you are not able to open the GUI

 $ xhost +SI:localuser:root

## Delete button does nothing/"Directory not empty" error
If the delete button silently fails in GUI and  results in

 E: ERROR: Could not destroy subvolume/snapshot: Directory not empty

this means the snapshot contains one or more nested subvolumes and those need to be removed manually. In order to do so, you need to mount the toplevel subvolume and see the subvolume list:

 # mount -o subvolid=5 /dev/root_partition /mnt
 # btrfs subvolume list /mnt

If you see any subvolumes located inside the snapshot, make sure they do not contain anything you would like to copy first and remove them by running:

 # btrfs subvolume remove /mnt/timeshift-btrfs/snapshots/snapshot/@/path/to/subvolume

And remove the snapshot using timeshift as normal. Alternatively, you can remove the whole snapshot and all the nested subvolumes by running .

Typically, this issue occurs because systemd-nspawn creates  and  subvolumes automatically. You can avoid this by creating them as directories in advance [https://github.com/systemd/systemd/issues/853#issuecomment-127758653

 # mkdir -p /var/lib/machines /var/lib/portables
