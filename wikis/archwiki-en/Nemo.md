# Nemo

Nemo is a fork of GNOME Files (formerly known as Nautilus). It is also the default file manager of the Cinnamon desktop. Nemo is based on the Files 3.4 code. It was created as a response to the changes in Files 3.6 which saw features such as type ahead find and split pane view removed.

## Installation
Install the  package.

## Extensions
Some programs can add extra functionality to Nemo. Here are a few packages that do just that:

*
*
*
*
*
*
*

See AUR and nemo-extensions github repo for all extensions.

## Configuration
Nemo is simple to configure graphically but not all options are in the preferences screen in Nemo. More options are available in the dconf-editor under .

## Set Nemo as default file browser
To set Nemo as the default file browser, execute the following:

 $ xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search

## Show / hide desktop icons
To enable/disable desktop icons rendering feature in nemo, change the following setting true or false (false to hide, true to show):

 $ gsettings set org.nemo.desktop show-desktop-icons false

This fixes the console warning  for tiling window managers (such as i3).

## Change the default terminal emulator for Nemo
 is set as the default, if it is not installed, neither the "Open in terminal" context menu entry feature will not work, nor shell scripts or terminal applications will not run from Nemo.

You can change the default setting with  to the preferred terminal application.

 $ gsettings set org.cinnamon.desktop.default-applications.terminal exec terminal-name

To be able to run shell scripts from Nemo, make sure you set up the proper argument for the preferred  terminal application (the default is  for ).

 $ gsettings set org.cinnamon.desktop.default-applications.terminal exec-arg argument

## Set keyboard shortcut for "Open in terminal"
If you want to edit keyboard shortcuts, you need first to change /org/cinnamon/desktop/interface/can-change-accels respectively /org/gnome/desktop/interface/can-change-accels if you are using Gnome desktop. You can do that with dconf-editor or with this code in terminal:

 $ gsettings set org.cinnamon.desktop.interface can-change-accels true

or for Gnome:

 $ gsettings set org.gnome.desktop.interface can-change-accels true

Edit or create  and add the following line (replacing "F4" with the desired key combination):

, , and  can be used as key modifiers (for example, ).

## Set bookmarks
The bookmarks can be configured in

## Tips and tricks
## Nemo Actions
Nemo allows the user to add new entries to the context menu. The file  contains an example of a Nemo action. Directories to place custom action files:
*  for system-wide actions
*  for user actions

Action files must have the  file extension.

## Clam Scan
## Moving files
## Meld compare
## Filenames containing spaces
By default, Nemo does not escape filenames. This means that actions for multiple files with some names containing spaces are broken. To fix this, use .

## Network Shares / Virtual Filesystems
By installing  and the various  packages, you can add support for various network based filesystems (e.g. SMB, NFS, WebDAV, Nextcloud) and some mobile phones (Android MTP, Apple AFC).

For more information and other supported virtual filesystems, see File manager functionality.

## Troubleshooting
## Thumbnail generation errors shown in the console
By default, nemo does not generate thumbnails for certain video files due to licensing or patent problems (AVC encoded mp4 and mkv files for example). As such, you might see errors similar to the following in the console:

 CinnamonDesktop-WARNING **: Error creating thumbnail for file:///home/username/video.mp4: Unrecognized image file format

for mp4 and other video files.

To fix this, ensure that you have a thumbnailer for video files installed—see File manager functionality#Thumbnail previews—and also ensure you have the necessary GStreamer packages installed that will allow the video file to be played.

## Desktop icons not shown
Since Nemo v3.4.2, the desktop is managed by nemo-desktop. This can be configured to auto start by copying the file  to  and removing the line .

## (GNOME) Opening a single file opens all files
Nemo was changed since v5.0.1 to allow the sort order to be maintained when passing multiple files to the image viewer. There is also a new GNOME setting to enable or disable it.

To fix this, run:

 $ gsettings set org.nemo.preferences image-viewers-with-external-sort "[]"

See https://github.com/linuxmint/nemo/issues/2771 for more information.
