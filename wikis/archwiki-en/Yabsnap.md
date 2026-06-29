# Yabsnap

Yabsnap is a scheduled snapshot manager for Btrfs partitions written for Arch.

## Installation
Install the  package.

## Configuration
Run the following to create a skeleton config:

 # yabsnap create-config 'configname'

This will create . Edit the file to specify the following:

*  - The location where a subvolume is mounted. E.g. .
*  - The full path and prefix for the snapshot names to be created. E.g.  will create files snapshot backups such as .

You can also edit other parameters to specify when backups will be triggered and cleaned up.

## Main commands
## Viewing snapshots
To review existing snapshots, use:

 $ yabsnap list

## Creating snapshots
To create snapshots for all configs, use:

 # yabsnap create --comment 'COMMENT'

You can also restrict to a specific mounted subvolume. Yabsnap will automatically find the right config for it and use it:

 # yabsnap --source '/home' create --comment 'COMMENT'

## Cleaning up or deleting snapshots
## Automatic cleanups
Yabsnap will automatically delete snapshots based on the configurations in .

## Deleting snapshots
You can also manually remove snapshots, with the following commands:

Specifying full path deletes a specific snapshot:

 # yabsnap delete /.snapshots/@home-20230525120000

Specifying a timestamp deletes all matching snapshots that were taken together:

 # yabsnap delete 20230525120000

## Creating a rollback
## Rollback requirement: Mount by subvol and not subvolid
It is recommended that you mount all the volumes with subvol instead of subvolid.

For example, this can be your fstab entry:

 UUID=/ btrfs rw,noatime,ssd,space_cache=v2,compress=zstd,subvol=/@ 0 0

The reason this works is because rollback mechanism will not edit your fstab file, it will simply ensure that the correct snapshots are mounted in the respective locations.

## Rollback operation
The command for rollback is safe, until you execute the script it generates.

This generates a rollback script:

Change the timestamp to one of your existing snapshots:

 $ yabsnap rollback-gen 20230525081049 | tee ~/rollback.sh

Executing the script will actually cause the rollback to happen. It is recommended that you review the generated lines before rolling back.

Once you have reviewed the generated script for your rollback, you can then make it executable then run it:

 # ~/rollback.sh

This will perform a rollback of all snapshots that were taken at the specified timestamp.

## Comparison with Snapper
It was created to overcome some of the shortcomings of Snapper, specifically it does the following which are difficult or impossible to do in Snapper (as of writing):

* custom destinations for backup [https://github.com/openSUSE/snapper/issues/54 (related issue),
* rollback for all configs (not just the default subvolume),
* has integrated pacman hook support.
