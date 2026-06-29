# Default applications

Programs implement default application associations in different ways. While command-line programs traditionally use environment variables, graphical applications tend to use XDG MIME Applications through either the GIO API, the Qt API, or by executing , which is part of xdg-utils. Because xdg-open and XDG MIME Applications are quite complex, various alternative resource openers were developed. The following table lists example applications for each method.

{| class=wikitable
! Method !! Uses XDG !! Application examples !! Checking association
|-
| GIO's GAppInfo || Yes || Firefox, GNOME Files, PCManFM, Thunar, Thunderbird, Telegram ||
|-
|  || By default || Chromium (Open downloaded file) ||
|-
| Custom || Usually not || mc, ranger ||
|-
| Environment variables || No || man, sudoedit, systemctl ||
|-
| D-Bus's FileManager1 || org.freedesktop.FileManager1 || Firefox (Open containing folder), Zotero (Show file), Telegram (Show in folder) ||
|}

Many desktop environments and graphical file managers provide a GUI for configuring default applications.

## Background information
Programs sometimes need to open a file or a URI in the user's preferred application. To open a file in the user's preferred application the filetype needs to be detected (usually using filename extensions or magic numbers mapped to MIME types) and there needs to be an application associated with the filetype.

Heirloom UNIX programs used mime.types for MIME type detection and mailcap for application association.

## Resource openers
* XDG MIME Apps: implements the XDG MIME Applications specification
* RegEx rules: allows MIME types to be associated with applications using regular expressions
* URI support: allows arbitrary URI schemes to be associated with applications

{| class="wikitable sortable"
! Name !! Package !! XDG MIME Apps !! RegEx rules !! URI support
|-
|xdg-open || xdg-utils ||  ||  ||
|-
| ||  ||  ||  ||
|-
| ||  ||  ||  ||
|-
|mimeo ||  ||  ||  ||
|-
|mimi || ,  ||  ||  ||
|-
|busking ||  ||  ||  ||
|-
| || ranger ||  ||  ||
|-
|handlr ||  ||  ||  ||
|-
|clifm ||  ||  ||  ||
|-
|mimejs-git ||  ||  ||  ||
|}

## xdg-open
xdg-open (part of xdg-utils) implements XDG MIME Applications and is used by many programs.

Because of the complexity of the xdg-utils version of xdg-open, it can be difficult to debug when the wrong default application is being opened. Because of this, there are many alternatives that attempt to improve upon it. Several of these alternatives replace the  executable, thus changing the default application behavior of most applications. Others simply provide an alternative method of choosing default applications.

## perl-file-mimeinfo
 provides the tools  and . These have a slightly nicer interface than their  equivalents:

 # determine a file's MIME type
 $ mimetype photo.jpeg
 photo.jpeg: image/jpeg

 # choose the default application for this file
 $ mimeopen -d photo.jpeg
 Please choose an application

     1) Feh (feh)
     2) GNU Image Manipulation Program (gimp)
     3) Pinta (pinta)

 use application #

 # open a file with its default application
 $ mimeopen -n photo.jpeg

Most importantly, xdg-utils programs will actually call  instead of  for MIME type detection if it does not detect your desktop environment. This is important because  does not follow the XDG standard.

## mimeo
 provides the tool , which unifies the functionality of  and .

In the following example we see how to associate SVG files with Inkscape:

 # determine a file's MIME type
 $ mimeo --mimetype Svg_example2.svg
 Svg_example2.svg
  image/svg+xml

 # determine desktop file associated with executable "inkscape"
 $ mimeo --app2desk inkscape
 inkscape
  org.inkscape.Inkscape.desktop

 # find desktop file path
 $ mimeo --finddesk org.inkscape.Inkscape.desktop
 /usr/share/applications/org.inkscape.Inkscape.desktop

 # choose the default application for this MIME type
 $ mimeo --prefer image/svg+xml org.inkscape.Inkscape.desktop

 # check association
 $ mimeo --mime2desk image/svg+xml
 image/svg+xml
  org.inkscape.Inkscape.desktop

 # open a file with its default application
 $ mimeo Svg_example2.svg

One can also find the path to the  file:
 $ mimeo --mimeapps-list
 /home/user/.config/mimeapps.list

However a big difference with xdg-utils is that mimeo also supports custom "association files" that allow for more complex associations. For example, passing specific command line arguments based on a regular expression match:

 # open youtube links in VLC without opening a new instance
 vlc --one-instance --playlist-enqueue %U
   ^https?://(www.)?youtube.com/watch\?.*v=

 patches xdg-utils so that  falls back to mimeo if no desktop environment is detected.

## handlr
, written in Rust, provides the functionality of  and  with a streamlined interface.
 is a fork of  with regex support.

Compared to , it includes:
* setting associations by extension, removing the need to look up or remember mime types
* validation for mime types and extensions
* removal of invalid entries from
* intelligent detection of mime types from file content in case filename is ambiguous
* autocompletion of mimes, extensions, and desktop entries
* setting arbitrary commands as handlers based on regular expressions

 # The following two are identical
 handlr set .png feh.desktop
 handlr set image/png feh.desktop

 # List default apps
 handlr list

 # Get the handler for a mime/extension
 $ handlr get .png --json
 {"handler":"pqiv.desktop","name":"pqiv","cmd":"/usr/bin/pqiv"}

 # Launch a handler with optional path/URL
 handlr launch x-scheme-handler/https
 handlr launch x-scheme-handler/https -- https://google.ca

To use  as a replacement for , shadow it with following script:

 #!/usr/bin/bash
 handlr open "$@"

## clifm
Lira, 's built-in resource opener, can be used as a standalone resource opener via the  command line option. The configuration file () supports regular expressions for both MIME types and file names (or file extensions). A few examples:

 # Open a regular file
 clifm --open /etc/hosts

 # Open a directory
 clifm --open /media/data

 # Open an URL (via the application associated to the text/http MIME type in the configuration file)
 clifm --open www.archlinux.org

## Minimalist replacements
The following packages conflict with and provide  because they provide their own  script.

If you want to use one of these resource openers while still being able to use , install them manually in a PATH directory before .

* ,  - 130-line Bash script, can change command arguments for each MIME type
*  - 80-line Perl script similar to mimi but also supports regex rules

## run-mailcap
