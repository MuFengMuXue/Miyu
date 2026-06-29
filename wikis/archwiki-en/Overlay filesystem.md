# Overlay filesystem

From the initial kernel commit:

:Overlayfs allows one, usually read-write, directory tree to be overlaid onto another, read-only directory tree. All modifications go to the upper, writable layer. This type of mechanism is most often used for live CDs but there is a wide variety of other uses.

:The implementation differs from other "union filesystem" implementations in that after a file is opened all operations go directly to the underlying, lower or upper, filesystems. This simplifies the implementation and allows native performance in these cases.

Overlayfs has been in the Linux kernel since 3.18.

## Installation
Overlayfs is enabled in the default kernel and the  kernel module is automatically loaded upon issuing a mount command.

## Usage
To mount an overlay use the following  options:

 # mount -t overlay overlay -o lowerdir=/lower,upperdir=/upper,workdir=/work /merged

* The lower directory can be read-only or could be an overlay itself.
* The upper directory is normally writable.
* The workdir is used to prepare files as they are switched between the layers.

The lower directory can actually be a list of directories separated by , all changes in the  directory are still reflected in .

Example:

 # mount -t overlay overlay -o lowerdir=/lower1:/lower2:/lower3,upperdir=/upper,workdir=/work /merged

To add an overlayfs entry to  use the following format:

The  and  mount options are necessary to prevent systemd from hanging on boot because it failed to mount the overlay. The overlay is now mounted whenever it is first accessed and requests are buffered until it is ready. See fstab#Automount with systemd.

## Read-only overlay
Sometimes, it is only desired to create a read-only view of the combination of two or more directories. In that case, it can be created in an easier manner, as the directories  and  are not required:

 # mount -t overlay overlay -o lowerdir=/lower1:/lower2 /merged

When  is not specified, the overlay is automatically mounted as read-only.
