# Dolphin

Dolphin is the default file manager of KDE. For the video game console emulator, see Dolphin emulator.

## Installation
Install the  package.

## Extensions
* : adds archiving and compression support
* : adds audio CD support
* : extends tagging support (see #File tagging)
* : adds Git, Bazaar, Mercurial and Dropbox support and some mounting actions
* : allows managing files as administrator
*  : adds Google Drive support (see #KIO slaves)
* : adds the Compare files dialog (Alternatively, select two files: {right click} > Open With > {your diff tool}.)
* : integrated terminal panel

## File previews
* : video files (based on ffmpeg)
*  : *.ico, *.cur files and embedded *.exe icons
* : android package files
* : image files, PDFs and Blender *.blend files
* : plugins for the thumbnailing system (for development purposes only)
* : Gimp *.xcf files, *.heic files (with )
*  : embedded *.AppImage icons
* : *.webp, *.tiff, *.tga, *.jp2 files
* : *.raw files
* : fast and accurate SVG image thumbnails
*  : audio files

## Configuration
## Single click to open folders/files
To configure Single-Click to open items, install and run KDE’s  and select the desired behavior under Quick Settings > Clicking files or folders.
Then run the following to respect the setting: .
(see Alternatively, install and run  from the terminal, which will then give you the option to enable Single-Click (and change the theme etc.) from the Interface tab.

If you use Kvantum theme engine - use kvantum manager > Configure Active Theme > Miscellaneous > Click behavior.

## Change the default terminal emulator
Dolphin and other KDE applications use  by default.  To change the default terminal emulator, run  and select your Terminal Emulator or write the launch command into the selection field in the Other... popup. (The second option will create a new local desktop entry for this command.)

For example, to launch tmux in alacritty inside Dolphin, type  after selecting .

The setting can also be directly changed by modifying the configuration file . For example, to use alacritty add in the  section:

Where  takes a command and  a desktop entry (TerminalService seems to be optional).
Note, that this does not influence the terminal within the dolphin window (opened with ).

To change the internal Dolphin terminal window go to Keyboard > Shortcuts and choose your preferred terminal and set the Launch shortcut to  , overriding Konsole's shortcut. Note that terminals opened this way might not follow the background color as specified in the terminal's configuration file, but otherwise should be identical to an instance launched in a window.

## KIO slaves
Dolphin uses KIO slaves for network access, trash and other functionality, unlike GTK file managers which use GVFS. Available protocols are shown in the location bar (editable mode) [https://docs.kde.org/stable5/en/dolphin/dolphin/location-bar.html#location-bar-editable. To quickly bookmark them, right-click in the workspace, and select "Add to Places".

You can install KIO slaves manually. For example, to browse your Google Drive in Dolphin, install .

## Tips and tricks
## File tagging
Dolphin provides extensive support for file tagging. Add tags to a file by right-clicking the file and selecting Assign Tags. Tags on a file can be viewed in the Properties menu or in the Information panel. To show tags in a column in the Details View Mode, right-click on any header and choose Tags from the menu.

Dolphin uses the  extended attribute to store tags directly along with each file. Baloo indexes these tags into its own database to allow for faster searching and maintains a list of all known tags.
Activate Baloo to show a list of all indexed tags within the Places panel and make searching for files by their tags possible.

## Hiding custom files/directories
Files/directories can be hidden by creating a  file (in the same directory) that contains the names of the files/directories that should be hidden (one per line).

## Creating custom service menus
Custom service menu entries can be added to dolphin with special  files in one of the following Paths (see *
*

This adds a  menu item on all application mime types.

## Troubleshooting
## Device names shown as "X GiB Harddrive"
Create a filesystem label, or a partition label, and Dolphin will show this label in the device list instead of the size. See Persistent block device naming#by-label.

## Moving files into trash takes long on external drives
For moving files into the Trash, it is required that the user has exclusive access rights to the Trash. The rationale being that you do not want that others can see what you deleted. For that, a folder such as  is created on the external drive, with permission mode .

If the correct access permissions cannot be set, dolphin will (unlike GNOME) move the files to the trash in the home directory, which takes time.

To mount USB-Sticks / external HDDs, Dolphin uses Udisks. FAT32 / EXFAT / NTFS do not support UNIX file permission, udisk mounts them by default with mode 755.
To configure udisks to mount these drives with mode 700, have a look at the file . Copy the file (the name should end with .conf), uncomment the relevant part and add for the three filesystems to the lines with xyz_defaults the options .

(Background information: [https://bugs.kde.org/show_bug.cgi?id=76380#c62, === Transparent fonts ===

Fonts in selection frames may become transparent when using the GTK Qt style. Native Qt styles such as Cleanlooks and Oxygen are unaffected.

## Crashes on mounted SMB share
See Samba#Unable to overwrite files.

## Icons not showing
If icons are not displayed in Dolphin, install and run , choose one icon theme at the Icon Theme tab, and Apply.

If icons are still not displayed in Dolphin, set the  variable to  in your xprofile. Alternatively, start Dolphin with the platform theme flag:

 $ dolphin --platformtheme qt6ct

Also make sure to install and inherit a fallback icon theme like hicolor or Adwaita when you are using an uncommon, incomplete icon theme.

## Icons are too big
If icons are too big on Dolphin outside of a KDE environment, start it with:

 $ XDG_CURRENT_DESKTOP=KDE KDE_SESSION_VERSION=6 QT_AUTO_SCREEN_SCALE_FACTOR=0 dolphin

## Mismatched folder view background colors
When running Dolphin under something other than Plasma, it is possible the background color in the folder view pane will not match the system Qt theme. This is because Dolphin reads the folder view's background color from the  section in . Change the following line to the RGB value you prefer (it may be given in the form #RRGGBB or R,G,B):

If you get a blue border around the folder view pane (if you are in split view it will only be around the focused pane), you may get rid of it by applying the  style sheet via the qt6ct app. This [https://unix.stackexchange.com/a/683366 answer describes what  to do to get the adwaita dark theme working for dolphin under Gnome.

Alternatively, use  to manage your Qt6 theming. For instructions on usage see the Kvantum project homepage.

## Zsh profile not loading in integrated terminal
If your zsh profile is not loading, try editing your current profile. Right-click on the integrated terminal then Edit Current Profile... and edit the launch command to

## GTK applications are not using Dolphin
See Uniform look for Qt and GTK applications#Consistent file dialog under KDE Plasma.

## Unable to install any context menu plugins
When you go to Dolphin menu Settings > Configure Dolphin > Context Menu > Download New Services and try to install any service, you get this error message:

 /usr/bin/servicemenuinstaller: error while loading shared libraries: libpackagekitqt6.so.1: cannot open shared object file: No such file or directory

This can be solved by installing . Then restart Dolphin.

## Dolphin cannot find applications (when running under another window manager)
This can be resolved by installing the  package and running:

 $ XDG_MENU_PREFIX=arch- kbuildsycoca6 --noincremental

This updates the KService desktop-file system configuration cache (see ), which many KDE-applications rely on for selecting desktop entries. The  argument is optional.  is needed, because  creates a XDG Desktop Menu with an  prefix (see xdg-menu).

The XDG Desktop Menu files can be found in .

Normally,  does not need to be manually installed as it is part of the  package, which is a dependency of .
