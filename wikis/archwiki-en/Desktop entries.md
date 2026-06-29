# Desktop entries

The XDG Desktop Entry specification defines a standard for applications to integrate into application menus of desktop environments implementing the XDG Desktop Menu specification.

## Basics
The format of desktop entries is similar to INI files. These must have a  extension, and contain a  section. Within the  section, keys named  and  are required; other keys can optionally define its appearance in the application menu and other behaviors.

The three available s are:

*  defines how to launch an application and what MIME types it supports (used by XDG MIME Applications). With XDG Autostart Application entries can be started automatically by placing them in specific directories. Application entries use the .desktop file extension. See #Desktop entries for applications.
*  defines a shortcut to a . Link entries use the .desktop file extension.
*  defines the appearance of a submenu in the application menu. Directory entries use the .directory file extension.

The following sections will roughly explain how these are created and validated.

## Desktop environment support
The following table describes desktop environments' support for various features of the Desktop Entry specification.

{| class="wikitable"
|-
! Desktop environment
! Launcher (Package)
! Autostart
! Application
! Link
|-
| COSMIC
|
|
|
|
|-
| Cinnamon
| rowspan="4" | gio ()
| rowspan="4"
| rowspan="4"
| rowspan="4"
|-
| GNOME
|-
| GNOME Flashback
|-
| MATE
|-
| Deepin
| dde-open1 ()
|
|
|
|-
| Enlightenment
| enlightenment_open ()
|
|
|
|-
| KDE Plasma
| kde-open2 ()
|
|
|
|-
| LXDE
| pcmanfm ()
|
|
|
|-
| LXQt
| pcmanfm-qt ()
|
|
|
|-
| Xfce
| exo-open3 ()
|
|
|
|-
| rowspan="5" | Environment-agnostic
| gtk-launch4 ()
|
|
|
|-
| dex ()
|
|
|
|-
| xdg-open ()
|
|
|
|-
| app2unit5 ()
| 6
|
|
|-
| uwsm app5 ()
| 6
|
|
|}

# .desktop files of type Application must have the executable bit set to be launched by dde-open
# If  is unset, then kfmclient from  will be used instead. (KDE Plasma should set this variable under any condition, though.)
# gio (from ) will also be tried
# Only if application is in
# Designed for systemd-managed graphical sessions
# Systemd manages XDG autostart natively

## Usage
Users commonly interact with desktop entries through the main menu of their desktop environment, such as GNOME's "Activity Overview," or a dock or keystroke launcher like dmenu.

Main menu entries are typically installed by new programs in a system-wide location, but users can create their own in their home directory. Menu entries can be modified with one of the graphical tools mentioned below, or with a plain text editor.

Desktop entries can also be invoked from the command line, with a tool like :

 $ dex /usr/share/applications/firefox.desktop

## Desktop entries for applications
Desktop entries for applications, or .desktop files, are basically comprised of a path to an executable with some metadata. They must have  and contain at least the  and  keys, to locate the executable on disk.

These files usually reside in  or  for applications installed system-wide, or  for user-specific applications. User entries take precedence over system entries, and can be used to, for example, hide or change the default icon of a system entry.

## Example .desktop file
Following is an example of a  file for launching an application, with comments to explain each key. It is only meant to give an impression and does not show how to utilize all possible entry keys.

System-wide application entries are typically found in ; you can create your own in  with a text editor, or use one of the available tools to help with that.

## Keys commonly found in application entries
All recognized entries can be found on the freedesktop site. Here are some examples:

*  (required)
*: defines what type of desktop entry this is, as discussed above (required); commonly
*
*: specifies which version of the Desktop Entry spec this entry conforms to (optional)
*  (required)
* ,  and
*: the name of the menu item or icon for this entry, along with other descriptive information about it
*  and
*:when , these keys specify where to find the program it is intended to run

Although  and  are not always exposed by the user interface (e.g. the main menu), they can help user to locate the application based on keywords or concepts. For example:

 Name=Pidgin
 GenericName=Internet messenger

or

 Name=NoteCase
 GenericName=Note manager
 Comment=NoteCase is a hierarchical note manager (outliner), organizing notes in a tree-like structure

Some best practices:

*  should be the official name of the application, as it would appear in the title bar or "About" box
*  is what you would generally call an application that performs this application's functions, i.e., Firefox is a "Web Browser"

## The Exec key
The  key in an application entry is typically the name of an executable which is expected to be in the user's search path, but an absolute path can be specified for greater security.

The  key accepts several "field codes" which can be used to transmit arguments to the launched program, e.g., when used as a drag-and-drop target, or identified as the preferred application for opening a specific type of file or URL. These arguments are passed to the program such that internal whitespace and shell metacharacters are preserved, so you do not need to worry (as much) about quoting.

Here are the most useful field codes:

{| class=wikitable
 ! Field code (reference)
 ! Expands to
 |-
 | ,
 | a single filename, or a list of files, each as a separate argument
 |-
 | ,
 | a single URL, or a list of URLs
 |-
 |
 | two separate arguments to the program: , followed by the value of the
 |}

## Flatpak file forwarding
The  key for Flatpak applications often contains some syntax unique to  .

 Exec=/usr/bin/flatpak run --command=imhex --file-forwarding net.werwolv.ImHex @@u %U @@

See  for the details, but in a nutshell:

 --file-forwarding
    all arguments that are enclosed between a pair of '@@' arguments are interpreted as
    file paths, exported in the document store, and passed to the command in the form of the
    resulting document path. Arguments between '@@u' and '@@' are considered uris, and any file:
    uris are exported. The exports are non-persistent and with read and write permissions for the
    application.

## Context menu actions
Some desktop environments and file managers also register contextual actions with desktop entries, e.g. right-click menu actions for a selected file or files. Pantheon is one example, using a background service called [https://github.com/elementary/contractor#readme Contractor and desktop entries with a  extension.

Here is a simple example using  to send a desktop notification with the path of a selected file:

Here is a more complex example that will convert any PNG files selected to PNMs in parallel:

{{hc|~/.local/share/contractor/png-to-pnm.contract|2=
Entry
Name=Convert to PNM
Icon=image-x-generic
Description=Convert PNGs to PPMs
MimeType=image/png;
TryExec=parallel
TryExec=pngtopnm
# from the spec:
# > Note that the general escape rule for values of type string states
# > that the backslash character can be escaped as ("\\") as well and that
# > this escape rule is applied before the quoting rule.
Exec=sh -c 'parallel pngtopnm {} \\> {.}.pnm ::: "$@"' parallel %F
}}

One thing to note from the above is that if either of the  keys fails, the entry is not shown. It may also be instructive to read what the spec has to say about quoting, but in general it behaves like you are used to from the shell, with the additional requirement that  must be used to produce a literal .

When troubleshooting complex command lines, it can be helpful to prefix the  command with  and examine the system logs for the output (e.g. with ), noting which characters do or do not get passed literally.

## Maintenance
Desktop entries for applications are typically put in place by package's installation scripts and need little attention. Over time, though, broken or outdated .desktop files can accumulate, particularly those installed to your home directory.

When the executable named by a desktop entry's  or  cannot be found on the filesystem, that entry should be hidden from main menus and other launchers automatically. Still, it is worthwhile to do some cleanup of  now and then. The following sections describe how to accomplish that.

## Validation
As some keys have become deprecated over time, you may want to validate your desktop entries using  which is part of the  package. To validate, run:

 $ desktop-file-validate your_file.desktop

This will give you very verbose and useful warnings and error messages.

## Installation
Use  to install desktop file into target directory. For example:

 $ desktop-file-install --dir=$HOME/.local/share/applications ~/app.desktop

This is also useful for customizing existing desktop entries (e.g. from ) via edit options.

## Update database of desktop entries
Usually, desktop entry changes are automatically picked up by the desktop environment.

If this is not the case, and you want to forcefully update the desktop entries defined in , run the following command:

 $ update-desktop-database ~/.local/share/applications

## Icons
See also the Icon Theme Specification.

## Common image formats
Here is a short overview of image formats commonly used for icons.

{| class="wikitable"
|+ Support for image formats for icons as specified by the freedesktop.org standard.
! Extension
! Full Name and/or Description
! Graphics Type
! Container Format
! Supported
|-
| .png
| Portable Network Graphics
| Raster
|
|
|-
| .svg(z)
| Scalable Vector Graphics
| Vector
|
|
|-
| .xpm
| X PixMap
| Raster
|
|
|-
| .gif
| Graphics Interchange Format
| Raster
|
|
|-
| .ico
| MS Windows Icon Format
| Raster
|
|
|-
| .icns
| Apple Icon Image
| Raster
|
|
|-
|}

## Converting icons
See also ImageMagick#Usage.

If you stumble across an icon which is in a format that is not supported by the freedesktop.org standard (like  or ), you can use the magick tool (which is part of the  package) to convert it to a supported/recommended format, e.g.:

 $ magick icon_name.gif icon_name.png

If you convert from a container format like , you will get all images that were encapsulated in the  file in the form . If you want to know the size of the image, or the number of images in a container file like  you can use the identify tool (also part of the  package):

As you can see, the example .ico file, although its name might suggest a single image of size 48x48, contains no less than 6 different sizes, of which one is even greater than 48x48, namely 128x128.

Alternatively, you can use icotool (from ) to extract PNG images from ICO container:

 $ icotool -x icon_name.ico

For extracting images from .icns container, you can use icns2png (provided by ):

 $ icns2png -x icon_name.icns

## Obtaining icons
Although packages that already ship with a .desktop file most certainly contain an icon or a set of icons, there is sometimes the case when a developer has not created a .desktop file, but may ship icons, nonetheless. So a good start is to look for icons in the source package.

You can i.e. first filter for the extension with find and then use grep to filter further for certain buzzwords like the package name, "icon", "logo", etc, if there are quite a lot of images in the source package.

 $ find /path/to/source/package -regex ".*\.\(svg\|png\|xpm\|gif\|ico\)$"

If the developers of an application do not include icons in their source packages, the next step would be to search on their web sites.

Some projects, like  have an artwork/logo page where additional icons may be found. If a project is multi-platform, there may be the case that even if the Linux/UNIX package does not come with an icon, the Windows package might provide one. If the project uses a Version control system like CVS/SVN/etc. and you have some experience with it, you also might consider browsing it for icons.

If everything fails, the project might simply have no icon/logo yet.

## Icon path
The freedesktop.org standard specifies in which order and directories programs should look for icons:

#  (for backwards compatibility)
#
#

## Tools
*
*
*
*
*
*
*
*

## Tips and tricks
## Modify desktop files
For system-wide .desktop files (e.g. those installed from a package), first copy the relevant .desktop file (e.g. from ) to  (e.g. ). This prevents your changes from being overwritten when the package gets updated during system upgrades. The local user-specific .desktop files should automatically take precedence over the system-wide files. Now you can modify the local user-specific .desktop file as needed.

## Modify environment variables
To set environment variables, in the .desktop file, edit the  line to first use the  command to set your variables. For example, with the original line commented out:

Also remove  (or set it to ) if present as it will cause the  line to be ignored.This technique can be appropriated to set a per-application desktop theme, provided you always launch that application from the system menu or another launcher which utilizes the desktop entry specification:

See Dark mode switching for more details.

## Modify command line arguments
To change or add the command line arguments, edit the  line to append the desired options. As an example, with the original line commented out:

Also remove  (or set it to ) if present as it will cause the  line to be ignored.[https://wiki.gnome.org/HowDoI/DBusApplicationLaunching#Changes_to_the_desktop_file

## Hide desktop entries
The visibility of the desktop entry can be controlled in multiple ways. See the Desktop Entry Specification for more information. Add one of the following lines to your .desktop file:
* All desktop environments, choose one (or both) of the following:
** Add the line  for applications that you do not want displayed in the menus.
** Add the line  for applications that you consider deleted and do not want displayed in the menus.
* Specified desktop environments, choose one of the following where  is a semicolon-delimited list of desktop environments (e.g. , ):
** Add the line  to hide the entry only in the specified desktop environments.
** Add the line  to show the entry only in the specified desktop environments.
