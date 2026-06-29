# Udisks

udisks provides a daemon udisksd, that implements D-Bus interfaces used to query and manipulate storage devices, and a command-line tool udisksctl, used to query and use the daemon.

## Installation
Install the  package.

 is started on-demand by D-Bus and should not be enabled explicitly. It can be controlled through the command-line with .

## Configuration
## Permissions
Actions a user can perform using udisks are restricted with polkit. If the user session is not activated or present (for example, when controlling udisks from a systemd/User service), adjust polkit rules accordingly.

See https://github.com/coldfix/udiskie/wiki/Permissions for common udisks permissions for the  group, and for a more restrictive example. If you are using Dolphin, you may see [https://gist.github.com/Scrumplex/8f528c1f63b5f4bfabe14b0804adaba7.

## Default mount options
It is possible to define default mount options in . Create the file if it does not already exist. The built-in defaults and some examples can be seen in .The options can target specific filesystem types. For example, mount btrfs filesystems with zstd compression enabled:

## Usage
To manually mount a removable drive, for example :

 $ udisksctl mount -b /dev/sdc1

To unmount:

 $ udisksctl unmount -b /dev/sdc1

See  for more.

## Tips and tricks
## Mount helpers
The automatic mounting of devices is easily achieved with udisks wrappers. See also List of applications/Utilities#Mount tools.

*
*
*
*

## udevadm monitor
You may use  to monitor block events and mount drives when a new block device is created. Stale mount points are automatically removed by udisksd, such that no special action is required on deletion.

{{bc|
#!/bin/sh

pathtoname() {
    udevadm info -p /sys/"$1" | awk -v FS== '/DEVNAME/ {print $2}'
}

stdbuf -oL -- udevadm monitor --udev -s block | while read -r -- _ _ event devpath _; do
        if [ "$event" = add ; then
            devname=$(pathtoname "$devpath")
            udisksctl mount --block-device "$devname" --no-user-interaction
        fi
done
}}

## Mount to /media
By default, udisks2 mounts removable drives under the ACL controlled directory . If you wish to mount to  instead, use this rule:

{{hc|/etc/udev/rules.d/99-udisks2.rules|
# UDISKS_FILESYSTEM_SHARED
# ==1: mount filesystem to a shared directory (/media/VolumeName)
# ==0: mount filesystem to a private directory (/run/media/$USER/VolumeName)
# See udisks(8)
ENV{ID_FS_USAGE}=="filesystem|other|crypto", ENV{UDISKS_FILESYSTEM_SHARED}="1"
}}

Since , unlike , is not mounted by default as a tmpfs, you may also wish to create a tmpfiles.d snippet to clean stale mountpoints at every boot:

## Mount loop devices
To easily mount ISO images, use the following command:

 $ udisksctl loop-setup -r -f image.iso

This will create a read only loop device and show the ISO image ready to mount. Remove the  flag to be able to write to it. The name of the created loop device is output by the above  command.

You can unmount, and remount, the image as long as the specific loop device is in place. When done working with the specific loop device, use

 $ udisksctl loop-delete -b /dev/loop0

to delete it. Substitute  with the name of the specific loop device.

Loop devices are cheap. Therefore, many loop devices can be created in practice without worrying about a denial of service issue. See === Hide selected partitions ===

If you wish to prevent certain partitions or drives appearing on the desktop, you can create a udev rule, for example :

 KERNEL=="sda1", ENV{UDISKS_IGNORE}="1"
 KERNEL=="sda2", ENV{UDISKS_IGNORE}="1"

shows all partitions with the exception of  and  on your desktop.

Because block device names can change between reboots, it is also possible to use UUIDs to hide partitions or whole devices. Matching by UUID is only possible after  has been processed, so make sure to choose a file name that will be ordered after it. For example:

{{hc|/etc/udev/rules.d/61-hide-partitions.rules|2=
SUBSYSTEM=="block", ENV{ID_FS_UUID}=="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXXX", ENV{UDISKS_IGNORE}="1"
}}

The above line is also useful to hide multi device btrfs filesystems, as all the devices from a single btrfs filesystem will share the same UUID across the devices but will have different SUB_UUID for each individual device.

## Apply ATA settings
At start-up and when a drive is connected, udisksd will apply configuration stored in the file  where  is the value of the Drive:Id property for the drive. Currently ATA settings are supported. See  for available options. These settings have essentially the same effect as those of hdparm, but they are persistent as long as the udisks daemon is autostarted.

For example, to set standby timeout to 240 (20 minutes) for a drive, add the following:

To obtain the DriveId for your drive, use

Alternatively, use a GUI utility to manage the configuration file, such as .

## Setting noatime by default
If most of the devices mounted with Udisks are flash memories, like USB sticks and SD cards, configuring Udisks to not update files' access time may be beneficial. It causes additional and unexpected writes, despite the memory has apparently only been read. The default  mount option limits excessive writes for main storage. It does not prevent updates if the access time is older than 24 hours, which is often the case on removable media. To set  as the default for all Udisks mounts, add:

This option may be overridden later for specific mounts that do require atime: either in  mount-specific  section or through a udev rule setting {{ic|ENV{UDISKS_MOUNT_OPTIONS_DEFAULTS}="relatime"}}.

## Troubleshooting
## Hidden devices
Udisks2 hides certain devices from the user by default. If this is undesired or otherwise problematic, copy  to  and remove the following section in the copy:

## Broken standby timer
The udisks daemon polls S.M.A.R.T. data from drives regularly. Hard drives with a longer standby timeout than the polling interval may fail to enter standby. Drives that are already spun down are usually not affected. There seems no way to disable polling or change the interval as for  by now. See [https://bugs.launchpad.net/ubuntu/+source/udisks2/+bug/1281588, However, Standby timeout applied by udisks2 seems to be unaffected. To set standby timeout via udisks, see #Apply ATA settings.

Other possible workarounds could be setting the timeout below the polling interval (10 minutes) or forcing a manual spindown using .

## NTFS mount failing
If mounting a ntfs partition fails with the error:
 Error mounting /dev/sdXY at [...: wrong fs type, bad option, bad superblock on /dev/sdXY, missing codepage or helper program, or other error
and in the kernel log with / ran as root:
 ntfs: (device sdXY): parse_options(): Unrecognized mount option windows_names.
The problem is (as of udisks 2.10), the default is using the NTFS-3G driver, and there are 2 solutions for this:

1: Install NTFS-3G, and restart your machine.

2: Configure udisks2. By default, udisks2 is not configured on an Arch system, and no defaults are defined for non-native filesystems. The easiest way to do so, is to copy  to  and uncomment the following lines:

and restart the udisk2 daemon, or restart your machine.

## NTFS file creation failing (filename-dependent)
udisks 2.8.2 introduced a breaking change by adding  to NTFS mount options, preventing creation of Win32-incompatible filenames such as , . Among other things, this causes Steam Proton to stop initializing. To revert this behavior, use:

Bad filenames generally do not cause issues in Windows unless accessed. chkdsk will treat these names as errors and move the renamed files to  folders under filesystem root.

## Automatically turn off an external HDD at shutdown
If an external HDD is not powered off properly at system shutdown, it may be desirable to fix the issue.

Enable .

A service to invoke our script might look like so:

Enable

Do a systemd daemon-reload to apply the new setting.

Reboot or restart  to check if works.

An example script to handle an arbitrary amount of partitions on a single disk looks like so:

{{hc|/usr/local/bin/handle_external_hdds.sh|2=
#!/bin/bash -u

declare -a uuids=(uuid_list)

# Only proceed if the drive is present.
if ! -L "/dev/disk/by-uuid/${uuids[0}" ]]; then
  exit 0
fi

for uuid in "${uuidsdo
  if findmnt "/dev/disk/by-uuid/$uuid"; then
    umount "/dev/disk/by-uuid/$uuid"
  fi
done

# udisksctl powers off proper drive even if its partition is supplied
udisksctl power-off -b "/dev/disk/by-uuid/${uuids[0}"
}}

uuid_list is a list of space delimited UUIDs corresponding to partitions of the device to check, e.g. .

## Slow unmount or corruption of removable media without any writes
Even if nothing seems to be written to a USB stick, memory card, or other removable media, file access times may still be updated. This is a change that needs to be flushed to the device. If that is of concern, consider setting the noatime option for all Udisks mounts.
