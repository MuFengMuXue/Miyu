# FuseISO

FuseISO is a FUSE module to let unprivileged users mount ISO filesystem images (.iso, .nrg, .bin, .mdf and .img).

## Installation
Install the  package.

## Usage
## Mounting
To mount an image:

 $ fuseiso image directory

The destination mount point must be writable and have no other mounted files or devices to it.

Run  for all the available options.

## Unmounting
To unmount the image:

 $ fusermount -u directory

The command can be used to disconnect other storage devices mounted by other mount tools.

## Integration
## GNOME Files
For users of GNOME there is an easy way of using fuseiso from the nautilus-context menu.

First you will need the  package, then you need to save the following scripts to a folder of your choice (e.g. ):

Make them executable.
Now, start Actions for Nautilus.

Add a new action with the following settings:

* On the Basic tab:
** Label for the command: Mount ISO
** Command line to execute: /path_to_scripts/filemanager-actions-iso-mount.sh %F
** Current working directory: %d
* On the Path patterns tab, add each of the following patterns:
***.iso
***.nrg
***.bin
***.img
***.mdf

With this action you can mount ISO-images to your Desktop. It will create a folder in ~/Desktop with the name of the iso. fuseiso will mount the iso to this folder.

And a second one:

* On the Basic tab:
** Label for the command: Unmount ISO
** Command line to execute: /path_to_scripts/filemanager-actions-iso-umount.sh %F
** Current working directory: %d
* On the Path patterns tab, add each of the following patterns:
***.iso
***.nrg
***.bin
***.img
***.mdf

This second action will unmount the mounted iso and remove the folder from the desktop.

Save the configuration then restart Nautilus with nautilus -q in a Terminal window.

Sometimes you have to logout to be able to mount any image of the given types simply by right clicking it in Files and selecting Mount ISO. To unmount it again, just right click the corresponding folder on your desktop and select Unmount ISO.

## Nemo
Nemo as a file browser has a packaged function on right click to mount an iso with the  package. unmount is done by clicking on the respective icon of the mounted iso, just like one would do for USB drives.
