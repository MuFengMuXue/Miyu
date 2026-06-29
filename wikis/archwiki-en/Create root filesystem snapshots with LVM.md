# Create root filesystem snapshots with LVM

This article describes how to set up root filesystem LVM snapshot creation during system start. Such snapshots can be used for full system backups with minimal downtime or testing system updates with the option to revert them.

## Prerequisites
You need a system with LVM root filesystem and systemd.
Ensure that LVM snapshots prerequisites are correctly setup.

## Setup
## Option 1: Helper Scripts
An AUR package is available, , which can help automate the following process. It implements similar service and target files to those included in this article. The projects README contains important setup information.

## Option 2: Manual Configuration
If you prefer a fully "manual" setup, you will need to write a systemd service to create a clean snapshot of the root volume during system startup.

Create:

Adapt the  command to match your root volume group and volume name.
Adjust the snapshot size if necessary. If additional filesystems should be snapshotted
during startup you may extend the  property with addtional lvcreate commands,
separated with  (consider there is a space before and after the semicolon, see  for details).

Create a new systemd target:

Adapt the base target, if  is not your default target. If you want to get into your desktop, you need to change it to .

Enable .

If the system is started with the new target, LVM snapshot(s) are created just after mounting the local filesystems.
To get a GRUB menu entry starting this target create  based on the
 entry for your normal startup. The kernel command line is extended to start the new
:

{{bc|1=
### make snapshots ###
menuentry 'Arch GNU/Linux, make snapshots' --class arch --class gnu-linux --class gnu --class os {
...
        echo    'Loading Linux core repo kernel ...'
        linux   /boot/vmlinuz-linux root=/dev/lvmvolume/root ro systemd.unit=make-snapshots.target
        echo    'Loading initial ramdisk ...'
        initrd  /boot/initramfs-linux.img
}
}}

Remember to adjust  if  changes.

After restarting the system with this grub entry  should show up the newly created snapshot.

## Usage
## Backup
To use this functionality for a full system backup, restart your system with the snapshot creation target.
Mount the snapshot volume (and further volumes, if required), preferably using the read-only () option.
Then backup your system, for example with tar as described in Full system backup with tar.

During backup you can continue to use your system normally, since all changes to your regular volumes are invisible in
the snapshots. Do not forget to delete the snapshot volume after the backup &ndash; changes to your regular volume will
use up space in the snapshot due to the copy-on-write operations. If the snapshot space becomes fully used, and LVM
is not able to automatically grow the snapshot, LVM will deny further writes to your regular volumes or drop the
snapshot, which should be avoided.

## Revert updates
Another use for LVM snapshots is testing and reverting of updates. In this case create a snapshot for the system
in a known good state and perform updates or changes afterwards.

If you want to permantly stick to the updates just drop the snapshot with lvremove. If you want to revert to the snapshotted
state issue a  for the snapshot. During the next restart of the system (use the default target) the snapshot
is merged back into your regular volume. All changes to the volume happened after the snapshot are undone.
