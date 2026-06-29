# Extended attributes

From : "Extended attributes are name:value pairs associated permanently with files and directories". There are four extended attribute classes: security, system, trusted and user.

Extended attributes are also used to set Capabilities.

## User extended attributes
User extended attributes can be used to store arbitrary information about a file. To create one:

 $ setfattr --name=user.checksum --value="3baf9ebce4c664ca8d9e5f6314fb47fb" file.txt

Use getfattr to display extended attributes:

To remove an extended attribute:

 $ setfattr --remove=user.checksum file.txt

To find files with certain extended attributes use :

 $ rh /path/to/dir '"XATTR_REGEX".reea'

Some other user extended attributes include:

* : helps programs know mimetype and set it with less guesswork.
* : used by the Apache httpd module mod_mime_xattr.
* : The name of the application that created the file.

XDG also proposes a set of standardized extended attributes to be used by programs:

* : supported by Dolphin and other file managers.
* : for files downloaded from a url.
* : "true" if a file is included in indexing, "false" otherwise
* : "true" if a file is included in backup, "false" otherwise
*
*
*
*
*
*

 is not part of the official standard, but it has become a "de facto" standard as several popular programs have implemented support for it (see #Software). It is implemented as a CSV list of user-specified tags for each file.

## Preserving extended attributes
{| class=wikitable
! Command || Preserves by default?/Required flag
|-
|  || //
|-
|  || 1
|-
|  ||  for creation and  for extraction
|-
|  ||  for extraction
|-
| rsync ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
| syncthing || by enabling syncXattrs
|}

# mv silently discards extended attributes when the target file system does not support them.

To preserve extended attributes with text editors you need to configure them to truncate files on saving instead of using . Just like you should do for any other data you do not want to lose, you should make regular backups of your extended attributes. To make a full backup of the extended attributes of all files in the current directory (recursively):

 $ getfattr --dump --recursive . > backup.txt

To restore a backup:
 $ setfattr --restore=backup.txt

## Support
## File systems
All major Linux file systems including Ext4, Btrfs, ZFS, and XFS support extended attributes. The kernel allows to have extended attribute names of up to 255 bytes and values of up to 64 KiB, but Ext4 and Btrfs might impose smaller limits, requiring extended attributes to be within a "filesystem block".

NTFS uses Alternative Data Streams to store user. The mount option  or  should be used by default. However, it might not be supported if mount option  is used.  supports mapping Alternative Data Streams to extended attributes in FUSE.

NFS supports extended attributes [https://www.phoronix.com/news/Linux-5.9-NFS-Server-User-Xattr since Linux 5.9.

## Software
{| class="wikitable"
! Application
! Supported extended attributes
! Notes
|-
| baloo
|
|
|-
|
|
| Supported by caja-xattr-tags and caja.eiciel extensions.
|-
| Chromium
|
| Used to support referrer and URL, but was disabled due to privacy and security concerns. See also CVE-2018-20483.
|-
|
|
|
|-
| CURL
|
| Enabled with  flag.
|-
| Dolphin
|
| Dolphin provides comprehensive support for file tagging, including the ability to add tags to files through the context menu, and support for searching by file tags. Tags are stored as CSV in the  attribute. See also Dolphin#File tagging.

[https://bugs.kde.org/show_bug.cgi?id=116617
|-
| Dropbox
|
|
|-
| emacs-vm
|
| Resets mbox xattrs.
|-
| Epiphany
|
|
|-
| Exiftool
|
|
|-
|
|
|
|-
|
|
|
|-
| Firefox
|
|
|-
|
|
|
|-
| Gwenview
|
|
|-
|
|
|
|-
|
|
|
|-
| kio
| |
|-
| Nautilus
|
| Full extended file attributes support can be added by the Nautilus extension from .
|-
|
|
|
|-
|
|
|
|-
|
|
|
|-
|
|
|
|-
| Thunar
|
|
|-
| , yt-dlp
|
| Enabled with  flag.
|-
| Wget
|
| Enabled with  flag.
|-
| webkit
|
|
|}

## Other tagging systems
It might not be possible to use extended attributes due to lack of support of either the file system or software. For this reason, many media formats store metadata included in the file format that can be viewed using programs like Exiftool or more specified ones like  for audio.

* For all files: Exiftool
* For audio: Audio tag editors
* For video:  from FFmpeg

## gvfs
Another filesystem-independent workaround is Gnome virtual filesystem:  which is used to store metadata (gvfsd-metadata). For example, Firefox [https://hg.mozilla.org/mozilla-central/file/tip/toolkit/components/downloads/DownloadPlatform.cpp stores metadata this way and can be viewed with:

 $ gio info --attributes=metadata:: downloaded.html

Other programs that use this approach include:
* Thunar: to save file color highlights.
