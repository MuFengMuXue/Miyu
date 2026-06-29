# Midnight Commander

Midnight Commander is a visual shell for Unix-like systems. It is an orthodox (two-pane) file manager, supporting standard file operations, virtual filesystems, panelizing of external commands, and user menus. It also includes an internal viewer , editor , and visual diff tool .

As it is based on versatile text interfaces — ncurses or S-Lang — it works on a regular console, inside an X Window terminal, over Secure Shell (SSH) connections, and all kinds of remote shells.

## Installation
Install the  package.

## Skins
Midnight Commander comes with multiple skins by default. You can set the skin in Options > Appearance.

Additional third-party skins can be installed separately:

*
*

See also .

## Configuration
Most of the Midnight Commander settings can be changed from the menus. However, a small number of settings such as clipboard commands, codeset detection and parameters for external editors can only be changed from . See  and following for a complete description of options.

Additionally, the following environment variables are respected:
, , , , ,  (was  prior to v4.8.19), , , , .

See also .

## extfs
extfs allows to easily create new virtual filesystems for Midnight Commander. See  for details.

## Usage
## Interface
In prominent view are two vertical panes. Either can list directory contents, show a plain text preview, file details, or a directory tree (see ). File operations are accessible through the function keys or the mouse. More options are visible in a dynamic user menu () and option menu (). Keys above  ( up to ) are accessible through . Menu and dialog options have one letter highlighted - pressing this letter (or  inside a text entry) directly activates the respective option.

Below, a command line is visible, connected to a subshell. This shell is generally of the same type Midnight Commander was launched from, and may be switched to at will (), see . On this command line, cd is interpreted by Midnight Commander, and not passed to the shell for execution. As such, special completion (such as from Zsh) is unavailable. Files in the pane interact with the command line; for example,  copies the name of a (selected) file to the command line.

Keybindings are generally similar to GNU Emacs. A more strict emacs keymap can be enabled (see ). New users may however use Lynx-like (arrow) keybindings (enabled in Options > Panel options) and mouse clicks for navigation.

Mouse support for Linux virtual consoles can be enabled with General purpose mouse.

## Modules
These can be called via the Midnight Commander interface (with Use internal enabled in Options > Configuration), or separately as symbolic links to the mc binary.

*  — Text and binary file editor, with regex replace, syntax highlighting, macros and shell piping
*  — Text and hex viewer with goto marks and regex search
*  — Compares and edits two files in-place ( )

Per Midnight Commander instance, multiple modules can be run concurrently and you can switch between them using , see . External editors may be used instead, and parameters configured accordingly.

## Tips and tricks
## Start from the menu
Midnight Commander (and likewise,  and its other subcommands) can be run from the  app launcher with the correct desktop entry. For example:

 Entry
 Type=Application
 Version=1.5
 Name=Midnight Commander
 Comment=Visual file manager
 Exec=mc %f
 Icon=MidnightCommander
 MimeType=inode/directory
 Terminal=true
 Categories=ConsoleOnly;FileManager;Utility;

With many terminal emulators gaining D-Bus activation capabilities, it is also possible to create a D-Bus service to trigger them to open a new tab/pane and invoke  there, with a Systemd unit acting as the listener for the trigger.

## Trash support
Midnight Commander does not support a trash can by default.

## Using libtrash
Install the  package, and create an mc alias in the initialization file of your shell (e.g.,  or ):

 alias mc='LD_PRELOAD=/usr/lib/libtrash.so mc'

To apply the changes, reopen your shell session or  the shell initialization file.

Default settings are defined in ; the default trash directory is . You can overwrite these settings per-user in , for example:

Now files deleted by Midnight Commander will be moved to the  directory.

See also this thread on the GNOME mailing list.

## mcedit syntax highlighting
The  section lacks some essential information from the corresponding section of . Read both mcedit and cooledit manual pages, or apply the patch.

## Troubleshooting
## Exit to the current directory
On exit, the shell returns to the directory Midnight Commander was started from, instead of the last active directory. A wrapper script is included, which can be used by adding this line to your  or :

 alias mc=". /usr/lib/mc/mc-wrapper.sh"

For the fish shell use this wrapper: mc.fish.  Place it to  or execute the content inside  shell and than run
 funcsave mc

Another simple workaround is to use the subshell (). This may however interfere with other terminal applications.

## Garbled screen
Press  to redraw the display. This only redraws, but does not refresh () the file list.

## Opening files
Midnight Commander reads the  environment variable to open files, which defaults to xdg-open when unset.

If Midnight Commander is blocked until the resulting process ends, or the process exits together with mc, use :

And set  accordingly:

 $ export MC_XDG_OPEN=~/bin/nohup-open

## Find file shows no results
If the Find file dialog (accessible with , or , or the F9 (menu) > Command > Find file) shows no results, check the current directory for symbolic links. Find file does not follow symbolic links, so use bind mounts (see ) instead, or the External panelize command.

## Broken shortcuts
With certain terminal definitions such as  or , shortcuts such as  may not work or act as different combinations. To remedy this, assign the terminal sequences manually with the Learn keys dialog.

Settings will be stored in the  file, for example for :

## Xterm window title customization
Xterm window title format is hardcoded to , also see the corresponding ticket.

 (Screen list) file manager (Panels:) entry format is hardcoded too.

,  and  do not change Xterm window title at all.
