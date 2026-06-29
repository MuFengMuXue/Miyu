# Fdisk

util-linux fdisk is a dialogue-driven command-line utility that creates and manipulates partition tables and partitions on a hard disk. Hard disks are divided into partitions and this division is described in the partition table.

This article covers 3 partitioning tools with different interfaces:

*  - the main dialog-driven interactive tool,
*  - scripting-friendly tool, used for automatic provisioning and backing up/restoring partitioning,
*  - TUI-oriented interactive tool, often considered more user-friendly.

## Installation
fdisk and its associated utilities are provided by the  package, which is a dependency of the  meta package.

## List partitions
To list partition tables and partitions on a block device, you can run the following, where device is a name like , , , etc.:

 # fdisk -l /dev/sda

## Backup and restore partition table
Before making changes to a hard disk, you may want to backup the partition table and partition scheme of the drive. You can also use a backup to copy the same partition layout to numerous drives.

For both GPT and MBR you can use sfdisk to save the partition layout of your device to a file with the / option. Run the following command for device :

 # sfdisk -d /dev/sda > sda.dump

The file should look something like this for a single ext4 partition that is 1 GiB in size:

To later restore this layout you can run:

 # sfdisk /dev/sda >}} cursor and the inverted background - you can move the selection with up/down arrow keys.
* On the bottom, cfdisk displays details on the currently selected partition and a list of commands that can be performed on it - use left/right arrow keys to select a command, then Enter to run it. Help text is displayed under the commands.
* Similar to standard fdisk, all actions are queued up and executed only when you run the  command - nothing happens on the disk until then. You can quit the program at any time to safely discard all your changes.
* If your disk does not have a partition table already, you will be prompted to create one. If you want to change the existing partition table format, you must either wipe the disk contents or use classic fdisk to clear and recreate the partition table.
