# PCManFM

PCManFM is an extremely fast and lightweight file manager and the standard file manager of LXDE. It uses GTK for its UI and GVFS (within GNOME's GIO library) to provide virtual filesystem functionality such as trashing files and mounting remote filesystems.

PCManFM-Qt is a port to Qt which is the standard file manager of LXQt. Despite using Qt as the UI toolkit, PCManFM-Qt retains GVFS rather than using KDE's KIO At their cores, both file managers are desktop-environment-agnostic.

## Installation
Install one of the following the packages:

* GTK 3:
* Qt6:

Optionally also install  for support for mounting volumes (with udisks), managing trash, and exploring remote filesystems. Certain protocols such as SMB may require additional dependencies mentioned in Gvfs.

## Desktop management
PCManFM can manage the desktop, including setting a background wallpaper and showing desktop icons. To launch the desktop manager, run:

 $ pcmanfm --desktop

The native desktop menu of the window manager will be replaced with that provided by PCManFM. The native menu can be restored from the PCManFM menu by selecting Desktop Preferences and then enabling the Show menus provided by window managers when desktop is clicked option in the Advanced tab.

## Desktop preferences
If using the native desktop menu provided by a window manager, enter the following command to set or amend desktop preferences at any time:

 $ pcmanfm --desktop-pref

Consider adding this command to a keybind and/or the native desktop menu for easy access.

## Creating new icons
Files can be dragged and dropped directly onto the desktop. To create shortcuts for applications, copy their  files to the  directory. Do not drag and drop the files there as they will be moved completely. The command is:

 $ cp /usr/share/applications/name-of-application.desktop ~/Desktop

For example to create a desktop shortcut for :

 $ cp /usr/share/applications/lxterminal.desktop ~/Desktop

For those who used the XDG user directories program to create their  directories, no further configuration will be required.

## Daemon mode
To run PCManFM as a background daemon (i.e. to automatically mount removable media), use:

 $ pcmanfm --daemon-mode

Only one instance of PCManFM may run as a daemon at atime.

Should automount fail, see udisks.

## Autostarting
PCManFM may be autostarted as a daemon process or to manage the desktop.

## Additional features and functionality
Less experienced users should be aware that a file manager alone — especially when installed in a standalone window manager such as Openbox — will not provide the features and functionality users of full desktop environments such as Xfce and KDE will be accustomed to. Review the file manager functionality article for further information.

## Tips and tricks
## Get thumbnails for other file types
See File manager functionality#Use PCManFM to get thumbnails for other file types.

## Set the terminal emulator
You can configure what terminal emulator PCManFM should use for Tools > Open Current Folder in Terminal under Edit > Preferences > Advanced.

## Integrate an archiver
It is possible to choose the integrated archiver under Edit > Preferences > Advanced. PCManFM and PCManFM-Qt both support , ,  and  [https://github.com/lxde/libfm/blob/5346a5390a0881d5713a71e15f371132680056ee/data/archivers.list PCManFM-Qt additionally supports , which is the default choice for LXQt.

## Adding custom items to the context menu
PCManFM supports [https://web.archive.org/web/20180627170128/http://www.nautilus-actions.org/?q=node/377 Desktop file specification extension (DES-EMA) which allows you to add arbitrary items to the context menu of files and directories. To add your own items, create  (if it does not already exist) and add  files inside:

You can bind one or more profiles to a single action by listing their id separated by semicolons. Profiles allow you to specify which commands to execute for which file types — thus the same action can run different commands depending on the type of file selected. Besides specific MIME types (e.g.  for text files), you can use the following general types:

*  - any files;
*  - any directories;
*  - any files and directories.

## Templates are accessible under Create New...
PCManFM adds the files in  as Create New... context menu items on startup.

## Thumbnails
Like some other file managers (e.g. Nautilus), PCManFM will load previews of all images in a folder. To not abuse the HDD, keep the number of images in a folder to a hundred.

## Troubleshooting
## "Open With" dialog window empty
If you do not see any applications to choose from in the open with dialog, then you can try removing  and instead install . Furthermore, set the following environment variables:

*
*

## No "Applications"
You can try this method: Delete all files in the  directory, and run PCManFM again.

PCManFM requires the environment variable  to be set. The value of the variable should match the beginning of a file present in the  directory. See #"Open With" dialog window empty.

See these threads for more information: and especially this post from the Linux Mint forums: [https://forums.linuxmint.com/viewtopic.php?f=175&t=53986#p501920

## No icons
If you are using a window manager instead of a desktop environment and you have no icons for folders and files, specify a GTK icon theme.

If you have e.g.  installed, edit  or  and add the following line:

 gtk-icon-theme-name = "oxygen"

Else, use an different one (gnome, hicolor, and locolor do not work). To list all installed icon themes:

 $ ls ~/.icons/ /usr/share/icons/

If none of them is suitable, install one. To list all installable icon packages:

 $ pacman -Ss icon-theme

## No "Previous/Next Folder" functionality with mouse buttons
A method to fix this is with Xbindkeys.

Install ,  and edit  to contain the following:

Actual button codes can be obtained with package .

Add:

 xbindkeys &

to your  to execute xbindkeys on log-in.

## --desktop parameter not working or crashing X-server
Make sure you have ownership and write permissions on .

Setting the wallpaper either by using the  parameter or editing  solves the problem.

## Terminal emulator advanced configuration not saved
Make sure you have the right permissions on the libfm configuration file:

 $ chmod -R 750 ~/.config/libfm
 $ chmod 640 ~/.config/libfm/libfm.conf

## Make PCManFM remember your preferred Sort Files settings
You can use View > Sort Files to change the order in which PCManFM lists the files, but PCManFM will not remember that the next time you start it. To make it remember, go to Edit > Preferences and close. That will write your current sort_type and sort_by values into .

## "Not authorized" error when attempting to mount drive
Make this polkit rule in :

{{hc|/etc/polkit-1/rules.d/00-mount-internal.rules|
polkit.addRule(function(action, subject) {
   if ((action.id == "org.freedesktop.udisks2.filesystem-mount-system" &&
      subject.local && subject.active && subject.isInGroup("storage")))
      {
         return polkit.Result.YES;
      }
});
}}

And add yourself to the storage user group.

## Operation not supported
Check first if you forgot to install the optional dependency , otherwise see the article on Session permissions.

## Passwords are forgotten on system restart
Install a keyring application like GNOME/Keyring, KDE Wallet or  for network shares or an SSH agent if appropriate.

## Empty Network place in PCManFM
Install  and .

Also check that  is enabled and started.
