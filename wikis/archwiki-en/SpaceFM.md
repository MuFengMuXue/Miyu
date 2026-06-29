# SpaceFM

SpaceFM (a fork of PCManFM)  is a lightweight, highly configurable, desktop-independent multi-panel tabbed file and desktop manager. It features a built-in virtual file system, a udev-based device manager, a customisable menu system, and Bash integration.

## Installation
Install the  package.

Or you can use  package if you need a GTK 2 version.

## Usage
See the User's Manual.

## File searches
SpaceFM provides a built-in file search feature similar to :

 $ spacefm -f

## Desktop management
SpaceFM includes a lightweight desktop manager. It replaces the desktop menu, adds desktop icons, and sets the wallpaper.

To restore the native window manager menu, open

 $ spacefm --desktop-pref

and enable the  option in the  tab. Consider adding the above command to a keybind and/or the native desktop menu for easy access.

To run SpaceFM as a daemon without it managing the desktop [https://ignorantguru.github.io/spacefm/spacefm-manual-en.html#invocation-daemonmode, use:

 $ spacefm -d

How SpaceFM may be autostarted as a daemon process or to manage the desktop for a standalone window manager will depend on the window manager itself. Should a window manager not provide an autostart file, edit xinitrc or xprofile.

## Mounting remote hosts
SpaceFM supports mounting remote hosts via udevil. To add a remote host, add the access URL into the URL bar. A terminal window should pop up showing the mounting process which is useful for error tracing.

An overview of the supported remote hosts is available in the udevil help. For example to mount a remote FTP server:

 ftp://user:pass@sys.domain/share

## Tips and tricks
## Open archive in app instead of extracting
By default, SpaceFM is configured to extract an archive when double clicking on it. If you instead want to open it with your default archive manager such as , then select an archive, right-click for context menu, and then: Open / Archive default / Open With App

## Show custom context menu command only on files/folders
If you have a custom context menu command that should be only shown on selection of files or folders, then add the following rules to :

 MIME Type equals true
 File Is Dir equals true
 File Is Text equals true

## Troubleshooting
## Columns are not resizeable
This should only happen on the first start of SpaceFM (GTK 2 version). === Segmentation faults ===

If SpaceFM crashes with errors such as:

 localhost kernel: [245086.687050 spacefmsegfault at 3e8000003e8 ip 00007fc95c586866 sp 00007fffb1dc9cc0 error 4 in libgtk-x11-2.0.so.0.2400.24[7fc95c446000+435000

SpaceFM uses many different GUI elements, and is thus suspectible to a malfunctioning theme (especially in GTK 3). Try a different theme such as Raleigh (default theme). To do so for SpaceFM only, in GTK 2:

 GTK2_RC_FILES=/usr/share/themes/Raleigh/gtk-2.0/gtkrc spacefm

See https://ignorantguru.github.io/spacefm/spacefm-manual-en.html#invocation-gtkthemes for details.
