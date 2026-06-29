# X resources

X resources file is a user-level configuration dotfile, typically located at . It can be used to set configuration parameters for X client applications. Among other things, it can be used to:

* configure terminal preferences—e.g. terminal colors,
* set DPI, anti-aliasing, hinting and other X font settings,
* change the X resources cursor theme (Xcursor theme),
* theme XScreenSaver,
* configure X applications—such as rxvt-unicode,  and .

## Installation
Install the  package for X server resource database utility and  for X.org documentations.

## Configuration
 and  provide detailed information on X resources mechanism and file syntax.

 is a conventional file name,  does not claim it. You can use any other file names, like  and  (also see #Samples and #Include files).

## Basic syntax
The syntax of an X resources file is a sequence of resource lines as follows:

 application_name.Class.resourceName: value
       application_name.resourceName: value
                  Class.resourceName: value
       application_name*resourceName: value
                       *resourceName: value

 and  substrings will never contain a dot (), the  substring may contain a dot. For example,  is a XScreenSaver internal resource that is specified to set the body font and fallback font:

 xscreensaver-auth.default.Dialog.bodyFont: times new roman 12, dejavu serif 12

;application_name
:The name of the application, such as , , , etc. Also may be called the instance name.

;Class
:The classification used to group resources together. Class names are typically uppercase.

;resourceName
:The name of the resource whose value is to be set. Resources are typically lowercase with uppercase concatenation.

;value
:The actual value of the resource. This can be one of three types:
:* Integer (whole numbers)
:* Boolean (true/false, yes/no, on/off)
:* String (a string of characters) — for example a word (), a color (), or a path ()

;delimiters
*A dot () is a tight binding and is used to separate immediately adjacent components (in other words, to signify each step down into the hierarchy) — in the above example we start at application name, then descend into Class, and finally into the resource itself.
*An asterisk () is a loose binding and is used to represent any number of components, including none.
*A colon () is used to separate the resource name from the value.

## Wildcard matching
Question mark () and asterisk () can be used as wildcards, making it easy to write a single rule that can be applied to many different applications or elements.  is used to match any single component name, while  is used to represent any number of intervening components including none.

Using the previous example, if you want to apply the same font to all programs (not just XScreenSaver) that contain the class name  which contains the resource name , you could write:

 ?.Dialog.headingFont:     -*-fixed-bold-r-*-*-*-100-*-*-*-*-iso8859-1

If you want to apply this same rule to all programs that contain the resource , regardless of its class, you could write:

 *headingFont:    -*-fixed-bold-r-*-*-*-100-*-*-*-*-iso8859-1

See  for more information.

## Comments
Lines starting with an exclamation mark () are ignored, for example:

 ! The following rule will be ignored because it has been commented out
 !Xft.antialias: true

The two-character sequence  (backslash followed by newline), which allows a value to be broken across multiple lines, is also recognized inside the comments. In the following sample all four lines are commented out, despite only one exclamation mark is used:

 ! URxvt.font: xft:Input Mono:size=13:style=Regular, \
               xft:Font Awesome 6 Free:style=Solid,  \
               xft:Segoe UI Symbol:style=Regular,    \
               xft:Noto Emoji:style=Regular

## Include files
To spread resource configuration across multiple files (e.g. to use its own file for each application), use C preprocessor  directive:

If files that are referenced with #include are not reachable from the applied configuration file directory, you need to pass a directory to search for:

 $ xrdb -load -I${HOME}/.config/X11 ~/.Xresources

## Default settings
To see the default settings for your installed X11 applications, look in .

Detailed information on program-specific resources is usually provided in the man page for the program.  is a good example, as it contains a list of X resources and their default values.

To see the currently loaded resources:

 $ xrdb -query -all

## Samples
* Color output in console#Terminal emulators
* Cursor themes#X resources
* Font configuration#Applications without Fontconfig support
* rxvt-unicode#Configuration
*
* Xterm#Configuration
* klassiker (mrdotx) — Rxvt-unicode patch developer dotfiles

## Usage
## Load resource file
Resources are stored in the X server, so have to only be read once. They are also accessible to remote X11 clients (such as those forwarded over SSH).

Load a resource file (such as the conventional ), replacing any current settings:

 $ xrdb ~/.Xresources

Load a resource file, and merge with the current settings:

 $ xrdb -merge ~/.Xresources

## xinitrc
If you are using a copy of the default xinitrc as your  it already merges .

If you are using a custom one, add:

## Getting resource values
If you want to get the value of a resource (for example if you want to use it in a bash script) you can use :

 $ xgetres xscreensaver.Dialog.headingFont
 -*-fixed-bold-r-*-*-*-100-*-*-*-*-iso8859-1

## Troubleshooting
## Parsing errors
Display managers such as GDM may use the  argument for xrdb.

## No output from xrdb -query
It is not rare for  to output nothing. Try following #Load resource file and #xinitrc from above. And note some of the files mentioned there could be empty.
