# File manager functionality

This article outlines the additional software packages necessary to expand the features and functionality of file managers, particularly where using a window manager such as Openbox. The ability to access partitions and removable media without a password—if affected—has also been provided.

## Overview
A file manager alone will not provide the features and functionality that users of full desktop environments such as Plasma or Xfce will be accustomed to. This is because additional software packages will be required to enable a given file manager to:

* Display and access other partitions
* Display, mount, and access removable media (e.g. USB sticks, optical discs, and digital cameras)
* Enable networking / shared networks with other installed operating systems
* Enable thumbnailing
* Archive and extract compressed files
* Automatically mount removable media

When a file manager has been installed as part of a full desktop environment, most of these packages will usually have been installed automatically. Consequently, where a file manager has been installed for a standalone window manager then - as is the case with the window manager itself - only a basic foundation will be provided. The user must then determine the nature and extent of the features and functionality to be added.

## Additional features
When using a lightweight environment, the more added file manager features, the more memory usage is needed. See also udisks.

## Mounting
* The Gnome virtual filesystem () provides mounting and trash functionality. GVFS uses udisks for mounting functionality and is the recommended solution for most file managers.

Folders used by GVFS:

*  contains  files, where  refers to the various supported file system types.
*  contains mount rules for GVFS. To use one's own rules, create .

Additional packages for installation usually follows the gvfs-* pattern, for example:

* : Windows file shares and anything else using the SMB/CIFS protocol. This internally uses Samba.
* : media players and mobile devices that use MTP
* : digital cameras and mobile devices that use PTP
* : Apple mobile devices

## File manager daemon
Most graphical file managers have the ability to automount devices plugged in while the program is running. You can leverage this for a system-wide solution by running the file manager in daemon mode (i.e. as a background process), if supported. For example, when using PCManFM in Openbox, the following command would be added to the  file:

 pcmanfm -d &

It will also be necessary to configure the file manager itself in respect to volume management (e.g. what it will do and what applications will be launched when certain file types are detected upon mounting).

## Standalone
Another option is to install a separate mount application. The advantages of using this are:

* Less memory may be required to run as a background/daemon process than a file manager
* It is not file-manager-specific, allowing them to be freely added, removed, and switched
*  is not needed to be installed for mounting, lessening memory usage. If it is installed, then its daemon can be masked, and started only on demand. This is useful for example as a fallback for mtp, where some implementations may not work.

## Networks
* : Bluetooth device mounting and file transfers (see Bluetooth)
* : Windows File and printer sharing for Non-KDE desktops (see Samba)
* : Windows File and printer sharing for KDE (see Samba#KDE)
* : FUSE client based on the SSH File Transfer Protocol

## Windows access
If using , to access Windows/Cifs/Samba file shares first open the file manager, and enter the following into the path name, changing  and  as appropriate:

 smb://server_name/share_name

## Apple access
AFP support is included in . To access AFP files first open the file manager, and enter the following into the path name, changing  and  as appropriate:

 afp://server_name/share_name

## sftp access
SFTP support is also included in . To access folders via sftp, open the file manager, and enter the following into the path name, changing  and  as appropriate:

 sftp://user@server_name/folder_name

## WebDAV
For WebDAV, install .

 davs://user@server_name/folder_name

## Thumbnail previews
The following packages enable thumbnailing in most file managers, such as PCManFM, SpaceFM, Thunar, and . They are not needed for KDE's Dolphin or Konqueror, which use a separate thumbnailing system.

 is the core backend for thumbnailing in many file managers. This must be installed to enable thumbnailing for various file types. It is not required for GNOME Files.

Image formats

*  — Thumbnails for .webp image files
*  — Thumbnails for .raw image files
*  — Thumbnails for font files

Video and audio

*  — Thumbnails for video files
*  — Thumbnails for audio files
*  — Thumbnails for video and tagged audio files (used by GNOME Files and )
*  and  - Thumbnails for audio files in Cinnamon/Nemo

Documents and ebooks

*  or  — Thumbnails for .pdf files (used in GNOME and MATE environments)
*  — Rendering library required by some thumbnailers (e.g. ) to generate .pdf thumbnails
*  — Thumbnails for .epub and .mobi ebook files
*  — Thumbnails for .odf (OpenDocument Format) files
*  — Thumbnails for .cbr comic book archive files

Other

*  — Thumbnails for folders
*  — Thumbnails for 3D model files, including .glTF, .stl, .step, .ply, .obj, and .fbx
*  — Thumbnails for Wine .exe

## Use PCManFM to get thumbnails for other file types
PCManFM supports image thumbnails out of the box. However, in order to view thumbnails of other file types, PCManFM uses the information provided in the files located at . The packages which provide a thumbnailer usually add the corresponding .thumbnail file at . For example, in order to get thumbnails for OpenDocument files, you may install  from the official repositories. For video files' thumbnails, the package  is required. For PDF files, you may install  from the official repositories, which provides  and the corresponding file at . However, if you prefer not to install , you can also replicate the functionality of  using 's  command. This is accomplished by creating a new file with the .thumbnailer extension (e.g.: ) at  with the following content:

 Entry
 TryExec=convert
 Exec=convert %i-background "#FFFFFF" -flatten -thumbnail %s %o
 MimeType=application/pdf;application/x-pdf;image/pdf;

Following this example, you can specify custom thumbnailers by creating your own .thumbnail files. Keep in mind that  refers to the input file (the file which will have its thumbnail made),  to the output file (the thumbnail image) and  to the size of the thumbnail. These parameters will be automatically substituted with the corresponding data and passed to the thumbnailer program by PCManFM.

## Archive files
To extract compressed files such as tarballs ( and ) within a file manager, it will first be necessary to install a GUI archiver such as . See List of applications/Utilities#Archiving and compression tools for further information. An additional package such as  must also be installed to support the use of zipped   files. Once an archiver has been installed, files in the file manager may consequently be right-clicked to be archived or extracted.

Archive files are mounted under folder  with automatically created mount point that contains full path to the file in its name where all  are replaced with  and  replaced with  [https://www.owasp.org/index.php/Double_Encoding hex codes.

Example of path to the mounted archive

 /run/user/$(id -u)/gvfs/archive:host=file%253A%252F%252F%252Ffull%252Fpath%252Fto%252Ffile%252Fname.zip

## NTFS read/write support
See the NTFS article.

## Desktop notifications
Some file managers make use of desktop notifications to confirm various events and statuses like mounting, unmounting and ejection of removable media.

## Enable Trash functionality on different filesystems (external drives)
Make trash directories  for each users on the top level of filesystems:

For example (mount point: /media/sdc1, uid: 1000, gid: 1000):
 # mkdir /media/sdc1/.Trash-1000

and  them:
 # chown 1000:1000 /media/sdc1/.Trash-1000

## Troubleshooting
## "Not Authorized" when attempting to mount drives
File managers using udisks require a polkit authentication agent. See polkit#Authentication agents.

## Password required to access partitions
The need to enter a password to access other partitions or mounted removable media will likely be due to the default permission settings of . More specifically, permission may be set to the root account only, not the user account. See Udisks#Configuration for details.

## Directories are not opened in the file manager
You may find that an application that is not a file manager, Audacious or Visual Studio Code for example, is set as the default application for opening directories — an application that specifies that it can handle the  MIME type in its desktop entry can become the default. You can query the default application for opening directories with the following command:

 $ xdg-mime query default inode/directory

To ensure that directories are opened in the file manager, run the following command:

 $ xdg-mime default my_file_manager.desktop inode/directory

where  is the desktop entry for your file manager —  for example.

## D-Bus
Some other applications instead use the  D-Bus protocol (e.g. Firefox). The following shows a list of currently installed services supporting this protocol:

 $ grep -R FileManager1 /usr/share/dbus-1/services

To change what file manager is opened, symlink the file to  or  if XDG_DATA_HOME variable is empty. Additionally, before the changes become active, kill the program currently implementing the D-Bus service.

## Mount points created manually in /etc/fstab are not displayed
Due to this gvfs commit you need to create your mount point inside .
