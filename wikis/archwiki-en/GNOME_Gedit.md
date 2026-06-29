# GNOME/Gedit

gedit is a general-purpose text editor for GNOME.

## Installation
Install the  package.

For additional features, install the  package.

Gedit can use multiple spell checking dictionaries, see Language checking.

## Configuration
## Do not end files with a new line
If you want to ensure that gedit does not end files with a newline, execute the following:

 $ gsettings set org.gnome.gedit.preferences.editor ensure-trailing-newline false

## Save backup versions of edited files
If desired, gedit can create a backup copy of an edited file - the contents of the backup file will be the same as the contents of the original file before the edit was made and then saved. The backup file's name will be the same as original file's name but suffixed with a ~ symbol. Hence, for the file called  the backup copy would have the name . Backup files are hidden by default.

To enable this behaviour, access gedit's Preferences panel (for GNOME Shell users, this can be found in gedit's global menu). In the preferences panel, click on the Editor tab and tick the option Create a backup copy of files before saving.

## Syntax highlighting
Gedit comes out-of-box with several syntax highlight thanks to , so this section show exceptions.

## PKGBUILD
Install  to have syntax highlight in PKGBUILDs.
