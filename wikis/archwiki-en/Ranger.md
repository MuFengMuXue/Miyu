# Ranger

ranger is a text-based file manager written in Python. Directories are displayed in one pane with three columns. Moving between them is accomplished with keystrokes, bookmarks, the mouse or the command history. File previews and directory contents show automatically for the current selection.

Features include: vi-style key bindings, bookmarks, selections, tagging, tabs, command history, the ability to make symbolic links, several console modes, and a task view.  ranger has customizable commands and key bindings, including bindings to external scripts. Ranger also comes with its own file opener, .

The closest competitors are lf and Vifm.

## Installation
Install the  package.

## Usage
To start ranger, launch a terminal and run .

{| class="wikitable"
|+
! Key !! Command
|-
|  || Open the manual or list keybindings, commands and settings
|-
| ,  || Launch files
|-
| ,  || Select file in the current directory
|-
| ,  || Travel up and down in the directory tree
|}

## Configuration
After startup, ranger creates a directory . To copy the default configuration to this directory issue the following command:

 $ ranger --copy-config=all

Afterwards, set  as an environment variable to avoid loading the global configuration in addition to the local.

*  - startup commands and key bindings
*  - commands which are launched with
*  - applications used when a given type of file is launched.

 only needs to include changes from the default file as both are loaded. For , if you do not include the whole file, put this line at the top:

 from ranger.api.commands import *

See  for general configuration.

## Move to trash
To add a keybind that moves files to your trash directory  with , amend the configuration file as follows:
{{hc|~/.config/ranger/rc.conf|
...
map DD shell mv %s /home/${USER}/.local/share/Trash/files/
...
}}

Alternatively, use GIO commandline tool provided by  package:

 map DD shell gio trash %s

Inspecting and emptying the "trash" is normally supported by graphical file managers such as , but you can also see the trash with the command , and empty it with: .

## Defining commands
Continuing the above example, add the following entry to empty the trash directory .

To use it, type  and  with tab completion as desired.

## Color schemes
Ranger comes with four color schemes: , ,  and .
You can change your color scheme using:

 set colorscheme scheme

Custom color schemes can be placed in .

## Color highlight in file previews
Install the  package, then copy  to  and edit the variable  in the configuration file of ranger to your liking. The complete list of supported themes can be obtained via .

## File association
Ranger uses its own file opener called .
It is configured in . Run  if it does not exist. For example, the following line makes  the default program for tex files:

 ext tex = kile "$@"

To open all files with , make sure your  and  are set and add:

 else = xdg-open "$1"
 label editor = "$EDITOR" -- "$@"
 label pager  = "$PAGER" -- "$@"

## Tips and tricks
## Archives
These commands use  to perform archive operations.

## Archive extraction
The following command implements archive extraction of the selected items to the current directory.

## Compression
The following command allows users to compress several files on the current directory by marking them and then calling . It supports name suggestions by getting the basename of the current directory and appending several possibilities for the extension. You need to have  installed, otherwise you will see an error message when you create the archive.

## External drives
External drives can be automatically mounted with udev or udisks. The default key mappings to go to common mount points  and  are   and  respectively.

## Hidden files
You can toggle the visibility of hidden files with the following command: , or use  to make hidden files visible.

To make this permanent, add the setting to your configuration file:

Alternatively, hidden files can be toggled by pressing .

## Image mounting
The following command assumes you are using CDemu as your image mounter and some kind of system like autofs which mounts the virtual drive to a specified location ('/media/virtualrom' in this case). Do not forget to change mountpath to reflect your system settings.

To mount an image (or images) to a cdemud virtual drive from ranger you select the image files and then type ':mount' on the console. The mounting may actually take some time depending on your setup (in mine it may take as long as one minute) so the command uses a custom loader that waits until the mount directory is mounted and then opens it on the background in tab 9.

## New tab in current folder
You may have noticed there are two shortcuts for opening a new tab in home ( and ). Let us rebind :

## PDF file preview
## PDF text preview
By default, ranger will preview PDF files as text with no additional configuration needed.

## PDF image preview
You can preview PDF files as an image in ranger by first converting the PDF file to an image. For this feature to work, you need to install , which is part of  package.

Ranger stores the image previews in . You either need to create this directory manually or set  to  in  to tell  to create it automatically at the next start.  However, note that  does not need to be set to  the whole time to preview PDF file as images, only  directory is needed.

To enable this feature, uncomment the appropriate lines in , or add/uncomment these lines in your local file .

## Shell tips
## Synchronize path
Ranger provides a shell function . Running  instead of  will automatically cd to the last browsed folder.

If you launch ranger from a graphical launcher (such as , where TERMCMD is an X terminal), you cannot use . Instead, create an executable script:

And add the following at the end of your shell configuration:

This will launch  only if the  variable is set. It is important to unset this variable again, otherwise launching a subshell from this terminal will automatically relaunch .

## Preventing nested ranger instances
You can start a shell in the current directory with , when you exit the shell you get back to your ranger instance.

When you however forget that you already are in a ranger shell and start ranger again you end up with ranger running a shell running ranger.

To prevent this you can create the following function in your shell's startup file:

 ranger() {
     if [ -z "$RANGER_LEVEL" ]; then
         /usr/bin/ranger "$@"
     else
         exit
     fi
 }

## Image preview on Wayland
Ueberzugpp serves as a drop in replacement for ueberzug, adding Wayland support. It does not support all Wayland compositors, please check if your compositor is supported. See If low quality pixel image is previewed, [https://github.com/jstkdng/ueberzugpp/issues/81#issuecomment-1623923211 change the layer output to kitty even if kitty is not installed.

{{hc|~/.config/ueberzugpp/config.json|
{ "layer": { "output": "kitty"  } }
}}
