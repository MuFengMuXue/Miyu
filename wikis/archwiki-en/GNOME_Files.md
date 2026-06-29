# GNOME/Files

Files is the default file manager for GNOME. Files attempts to provide a streamlined method to manage both files and applications. Can be extended to provide access to files over the network via various protocols like SFTP, WebDav, NFS, etc.

## Installation
Install the  package. This package is part of the  group. See also File manager functionality#Additional features.

## Extensions
## Network Shares / Virtual Filesystems
By installing  and the various  packages, you can add support for various network based filesystems (e.g. SMB, NFS, WebDAV, Nextcloud) and some mobile phones (Android MTP, Apple AFC).

For more information and other supported virtual filesystems, see File manager functionality.

## Other examples
*
*
:
*
*
*
*
*
*
*
*
*
*
*
:
*

## Integrations
Some applications ship their own integrations with GNOME Files:

*
*
*
*
:

## Integrations which rely on non-free software
Some, although free, might rely on non-free software. The following list provides a few examples:

*
*
*

## Configuration
Files is simple to configure graphically, but not all options are available in the preferences menu. More options are available with dconf-editor under .

## Change default item view
You can change the default view for the items by setting the  variable, e.g. for the list view:

 $ gsettings set org.gnome.nautilus.preferences default-folder-viewer 'list-view'

## Sort by type
To sort files in all folders by type:

 $ gsettings set org.gnome.nautilus.preferences default-sort-order 'type'

## Always show text-entry location
The standard Files toolbar shows breadcrumbs interface for path navigation. To enter the path or URI, either click on a space in the breadcrumbs that is not a button, or press .

To make the location text-entry field always present, use gsettings as shown below:

 $ gsettings set org.gnome.nautilus.preferences always-use-location-entry true

## Tips and tricks
## Thumbnails
See File manager functionality#Thumbnail previews.

Sometimes video thumbnails are not shown. To solve it (as mentioned in No video thumbnails on nautilus), you must install , , , and remove the content of .

## Create a new document from the right-click menu
To get this option one has to create a  folder in your home folder and place an empty file inside the folder through your favorite Terminal by  or by using any other file manager. Then just restart Files.

On non-English installations, the templates directory might have another name. One can find the actual directory with .

The templates directory can be configured in the  file:

 XDG_TEMPLATES_DIR="$HOME/some/path"

## Hiding files
Like most other file managers GNOME Files hides files with names starting with a dot by default.

GNOME Files additionally hides files when their names are listed in a  file in the same directory (one filename per line). See  for an extension that facilitates adding/removing entries from such  files.

## Open current directory in Tilix
If you are using  terminal you can easily add "Open in Tilix" option to the context menu of GNOME Files by installing its optional dependency .

## Add a folder to bookmarks
To add a folder to your bookmarks, simply press  when you have the folder opened in Nautilus. Note that the list of bookmarks is shared with other GNOME-based graphical file managers (e.g. Nemo), so a folder added or removed from one will affect the bookmarks seen in the other.

## Custom scripts
Scripts placed in  can be run from the right click context menu of a file.

The context menu can also be organized into subfolders, e.g.  and .

Scripts have access to the following environment variables:

 NAUTILUS_SCRIPT_SELECTED_FILE_PATHS
 NAUTILUS_SCRIPT_SELECTED_URIS
 NAUTILUS_SCRIPT_CURRENT_URI
 NAUTILUS_SCRIPT_WINDOW_GEOMETRY

Some example scripts:

{{hc|~/.local/share/nautilus/scripts/remove-extension|
#!/bin/sh
echo "$NAUTILUS_SCRIPT_SELECTED_FILE_PATHS"  while read -r filename; do
    mv -n "$filename" "${filename%.*}"
done
}}

## Keybinds
Keybinds to execute scripts can be assigned in the  file:

 ; Example Keybinds
 ; Modifiers:
 F4 open-terminal-here
 x remove-extension

## Troubleshooting
## Files is no longer the default file manager
This can be caused by the file association for directories being reset. Installing  or  tend to do this.

To solve this, open Files, right-click on a folder, and choose Open With Other Application > Files > Select. This will set the association for directories back to Files.

If this does not solve the issue, see File manager functionality#Directories are not opened in the file manager.

## Freezes for a few seconds after every copy operation
In case you have  installed in your system, the problem might be caused by its file sharing module. Deactivate file sharing, and it should stop happening.

## Windows machines with shared folders do not show up in Network view
To activate WSD support, install  to make GNOME/Files discover newer Windows machines in the network view.

## WebDAV missing from mounting options
Install  and restart Nautilus.

## Run as a Program does not work without gnome-console
'Run as a Program' context menu option is hardcoded for  and if you use different terminal and the default gnome terminal is not present, the context menu option will not do anything.

Since it's just executing  (executable for ) directly, you can create script (or symlink if your terminal has the same arguments) named  and place it inside  to use your terminal for 'Run as a Program' context menu option.

Example for using  as a terminal for 'Run as a Program'

## Open directory in an arbitrary terminal
It is possible to open a directory in a terminal emulator with "Open with..." right click menu entry. But the XDG desktop entry of the terminal is expected to contain appropriate  and  values.

Following example shows how to create additional desktop entry for Alacritty terminal emulator which will be recognized by "Open with...".

Run  to apply changes.

If a terminal app became default file manager, it can be fixed with command .

Check flags and desktop entry file of your preferred terminal application to adopt the example.
