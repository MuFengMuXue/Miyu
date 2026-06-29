# XDG MIME Applications

The XDG MIME Applications specification builds upon the shared MIME database and desktop entries to provide default applications.

# Applications describe what MIME types they can handle using desktop entries.
#  registers a pacman hook to build a cache database of MIME types handled by desktop entries, see .
# Applications can install new MIME types by placing XML files in .
#  registers a pacman hook to build the Shared MIME-Info database cache, see .
# Desktop environments and users can change default applications and add or remove MIME type to application associations using mimeapps.list files.

## Shared MIME database
The XDG Shared MIME-info Database specification facilitates a shared MIME database across desktop environments and allows applications to easily register new MIME types system-wide.

The database is built from the XML files installed by packages in  using the tools from .

The files in  should not be directly edited, however it is possible to maintain a separate database on a per-user basis in the  tree.

"URI scheme handling are handled through applications handling the  MIME type, where foo is the URI scheme in question."[https://specifications.freedesktop.org/shared-mime-info-spec/latest/ar01s02.html#id-1.3.18

## New MIME types
This example defines a new MIME type  and assigns it to any file with a name ending in .foo. Simply create the following file:

And then update the MIME database:

 $ update-mime-database ~/.local/share/mime

Of course this will not have any effect if no desktop entries are associated with the MIME type. You may need to create new desktop entries or modify mimeapps.list.

## mimeapps.list
The XDG standard is the most common for configuring desktop environments. Default applications for each MIME type are stored in  files, which can be stored in several locations. They are searched in the following order, with earlier associations taking precedence over later ones:

{| class="wikitable"
! Path !! Usage
|-
|  || user overrides
|-
|  || system-wide overrides
|-
|  || (deprecated) user overrides
|-
|  || distribution-provided defaults
|}

Additionally, it is possible to define desktop environment-specific default applications in a file named  where  is the name of the desktop environment (from the  environment variable). For example,  defines system-wide default application overrides for Xfce. These desktop-specific overrides take precedence over the corresponding non-desktop-specific file. For example,  takes precedence over  but is still overridden by .

To discover all the files that are scanned it is possible to enable debug mode by setting the environment variable XDG_UTILS_DEBUG_LEVEL=2: e.g. the  command will print each configuration file it is searching for MIME information.

## Format
Consider the following example:

Each section assigns one or more desktop entries to MIME types.
* Added Associations indicates that the applications support opening that MIME type. For example,  and  can open JPEG images. This might affect the application list you see when right-clicking a file in a file browser.
* Removed Associations indicates that the applications do not support that MIME type. For example,  cannot open H.264 video.
* Default Applications indicates that the applications should be the default choice for opening that MIME type. For example, JPEG images should be opened with . This implicitly adds an association between the application and the MIME type. If there are multiple applications, they are tried in order.

Each section is optional and can be omitted if unneeded.

## Utilities
While it is possible to configure default applications and MIME types by directly editing mimeapps.list and the shared MIME database, there are many tools that can simplify the process. These tools are also important because applications may delegate opening of files to these tools rather than trying to implement the MIME type standard themselves.

If you use a desktop environment you should first check if it provides its own utility. That should be preferred over these alternatives.

The official xdg-utils contain tools for managing MIME types and default applications according to the XDG standard (xdg-mime). Most importantly it provides xdg-open which many applications use to open a file with its default application.

## lsdesktopf
 provides several methods of searching the MIME database and desktop MIME entries.

For example, to see all MIME extensions in the system's .desktop files that have MIME type  you can use  or to search in the XML database files use . To get a quick overview of how many and which .desktop files can be associated with a certain MIME type, use . To see all file name extensions in XML database files, use .

## selectdefaultapplication
 is GUI application that lists up all applications supporting various mimetypes and lets you quickly set it as default for all or some of the mimetypes it supports (by modifying ).

It shows the "readable" name and file extensions as well, so you do not need to remember the name of the mimetypes.

## Troubleshooting
If a file is not being opened by your desired default application, there are several possible causes. You may need to check each case.

## Missing desktop entry
A desktop entry is required in order to associate an application with a MIME type. Ensure that such an entry exists and can be used to (manually) open files in the application.

## Missing association
If the application's desktop entry does not specify the MIME type under its  key, it will not be considered when an application is needed to open that type. Edit mimeapps.list to add an association between the .desktop file and the MIME type.

## Non-default application
If the desktop entry is associated with the MIME type, it may simply not be set as the default. Edit mimeapps.list to set the default association.

## Nonstandard association
Applications are free to ignore or only partially implement the XDG standard. Check for usage of deprecated files such as  and . If you are attempting to open the file from another application (e.g. a web browser or file manager) check if that application has its own method of selecting default applications.

## Variables in .desktop files that affect application launch
Desktop environments and file managers supporting the specifications launch programs according to definition in the .desktop files. See Desktop entries#Desktop entries for applications.

Usually, configuration of the packaged .desktop files is not required, but it may not be bug-free. Even if an application containing necessary MIME type description in the .desktop file  variable that is used for association, it can fail to start correctly, not start at all or start without opening a file.

This may happen, for example, if the  variable is missing internal options needed for how to open a file, or how the application is shown in the menu. The  variable usually begins with ; for its currently supported options, see exec-variables.

The following table lists the main variable entries of .desktop files that affect how an application starts, if it has a MIME type associated with it.

{| class="wikitable"
! Variable names !! Example 1 content !! Example 2 content !! Description
|-
| DBusActivatable || DBusActivatable=true || DBusActivatable=false || Application interact with D-Bus.  See also configuration: D-Bus.
|-
| MimeType || MimeType=application/vnd.oasis.opendocument.text || MimeType=application/vnd.sun.xml.math || List of MIME types supported by application
|-
| StartupWMClass || StartupWMClass=google-chrome || StartupWMClass=xpad || Associate windows with the owning application
|-
| Terminal || Terminal=true || Terminal=false || Start in default terminal
|}

## Empty MIME associations / open with menu in KDE
Install  and run
or add  to .
