# smb.conf Parameters / filename

### `case sensitive`

Section: filename; Context: S; Type: enum; Default: `auto`

See the discussion in the section name mangling .

### `default case`

Section: filename; Context: S; Type: enum; Default: `lower`

See the section on name mangling . Also note the parameter.

### `delete veto files`

Section: filename; Context: S; Type: boolean; Default: `no`

This option is used when Samba is attempting to delete a directory that contains one or more vetoed files or directories or non-visible files or directories (such as dangling symlinks that point nowhere). (see the , , , options). If this option is set to no (the default) then if a vetoed directory contains any non-vetoed files or directories then the directory delete will fail. This is usually what you want. If this option is set to yes , then Samba will attempt to recursively delete any files and directories within the vetoed directory. This can be useful for integration with file serving systems such as NetAtalk which create meta-files within directories you might normally veto DOS/Windows users from seeing (e.g. .AppleDouble ) Setting yes allows these directories to be transparently deleted when the parent directory is deleted (so long as the user has permissions to do so).

### `hide dot files`

Section: filename; Context: S; Type: boolean; Default: `yes`

This is a boolean parameter that controls whether files starting with a dot appear as hidden files.

### `hide files`

Section: filename; Context: S; Type: string; Default: `no file are hidden`

This is a list of files or directories that are not visible but are accessible. The DOS 'hidden' attribute is applied to any files or directories that match. Each entry in the list must be separated by a '/', which allows spaces to be included in the entry. '*' and '?' can be used to specify multiple files or directories as in DOS wildcards. can also be used as a parametric option where NAME in hide files : NAME = specifies a user or group name with the same syntax as . This parametric form can be specified multiple times for different users or groups. This means that "hide files : NAME" set both in the [global] and the share section add up, whereas normally options set in a share section overwrite the default in the [global] section. Each entry must be a Unix path, not a DOS path and must not include the Unix directory separator '/'. Note that the case sensitivity option is applicable in hiding files. Setting this parameter will affect the performance of Samba, as it will be forced to check all files and directories for a match as they are scanned. The example shown above is based on files that the Macintosh SMB client (DAVE) available from Thursby creates for internal use, and also still hides all files beginning with a dot. An example of us of this parameter is: hide files = /.*/DesktopFolderDB/TrashFor%m/resource.frk/ ; Hide some files for anyone and some files for specific users and groups hide files = /hideforall1/ hide files : USER = /hidetoforuser/ hide files : GROUP = /hideforgroup/ hide files : UNIVERSITY\Alumnis = /somefile.txt/ hide files : john@university.org = /anotherfile.txt/ hide files : S-1-5-21-123-456-789-1000 = /secretfile.txt/

### `hide new files timeout`

Section: filename; Context: S; Type: integer; Default: `0`

Setting this parameter to something but 0 hides files that have been modified less than N seconds ago. It can be used for ingest/process queue style workloads. A processing application should only see files that are definitely finished. As many applications do not have proper external workflow control, this can be a way to make sure processing does not interfere with file ingest.

### `hide special files`

Section: filename; Context: S; Type: boolean; Default: `no`

This parameter prevents clients from seeing special files such as sockets, devices and fifo's in directory listings.

### `hide unreadable`

Section: filename; Context: S; Type: boolean; Default: `no`

This parameter prevents clients from seeing the existence of files that cannot be read. Defaults to off. Please note that enabling this can slow down listing large directories significantly. Samba has to evaluate the ACLs of all directory members, which can be a lot of effort.

### `hide unwriteable files`

Section: filename; Context: S; Type: boolean; Default: `no`

This parameter prevents clients from seeing the existence of files that cannot be written to. Defaults to off. Note that unwriteable directories are shown as usual. Please note that enabling this can slow down listing large directories significantly. Samba has to evaluate the ACLs of all directory members, which can be a lot of effort.

### `mangled names`

Section: filename; Context: S; Type: enum; Default: `illegal`

This controls whether non-DOS names under UNIX should be mapped to DOS-compatible names ("mangled") and made visible, or whether non-DOS names should simply be ignored. See the section on name mangling for details on how to control the mangling process. Possible option settings are yes - enables name mangling for all not DOS 8.3 conforming names. no - disables any name mangling. illegal (default) - does mangling for names with illegal NTFS characters. This is the most sensible setting for modern clients that don't use the shortname anymore. If mangling is used then the mangling method is as follows: The first (up to) five alphanumeric characters before the rightmost dot of the filename are preserved, forced to upper case, and appear as the first (up to) five characters of the mangled name. A tilde "~" is appended to the first part of the mangled name, followed by a two-character unique sequence, based on the original root name (i.e., the original filename minus its final extension). The final extension is included in the hash calculation only if it contains any upper case characters or is longer than three characters. Note that the character to use may be specified using the option, if you don't like '~'. Files whose UNIX name begins with a dot will be presented as DOS hidden files. The mangled name will be created as for other filenames, but with the leading dot removed and "___" as its extension regardless of actual original extension (that's three underscores). The two-digit hash value consists of upper case alphanumeric characters. This algorithm can cause name collisions only if files in a directory share the same first five alphanumeric characters. The probability of such a clash is 1/1300. The name mangling (if enabled) allows a file to be copied between UNIX directories from Windows/DOS while retaining the long UNIX filename. UNIX files can be renamed to a new extension from Windows/DOS and will retain the same basename. Mangled names do not change between sessions.

### `mangle prefix`

Section: filename; Context: G; Type: integer; Default: `1`

controls the number of prefix characters from the original name used when generating the mangled names. A larger value will give a weaker hash and therefore more name collisions. The minimum value is 1 and the maximum value is 6. mangle prefix is effective only when mangling method is hash2.

### `mangling char`

Section: filename; Context: S; Type: char; Default: `~`

This controls what character is used as the magic character in name mangling . The default is a '~' but this may interfere with some software. Use this option to set it to whatever you prefer. This is effective only when mangling method is hash.

### `mangling method`

Section: filename; Context: G; Type: string; Default: `hash2`

controls the algorithm used for the generating the mangled names. Can take two different values, "hash" and "hash2". "hash" is the algorithm that was used in Samba for many years and was the default in Samba 2.2.x "hash2" is now the default and is newer and considered a better algorithm (generates less collisions) in the names. Many Win32 applications store the mangled names and so changing to algorithms must not be done lightly as these applications may break unless reinstalled.

### `map archive`

Section: filename; Context: S; Type: boolean; Default: `yes`

This controls whether the DOS archive attribute should be mapped to the UNIX owner execute bit. The DOS archive bit is set when a file has been modified since its last backup. One motivation for this option is to keep Samba/your PC from making any file it touches from becoming executable under UNIX. This can be quite annoying for shared source code, documents, etc... Note that this parameter will be ignored if the parameter is set, as the DOS archive attribute will then be stored inside a UNIX extended attribute. Note that this requires the parameter to be set such that owner execute bit is not masked out (i.e. it must include 100). See the parameter for details.

### `map hidden`

Section: filename; Context: S; Type: boolean; Default: `no`

This controls whether DOS style hidden files should be mapped to the UNIX world execute bit. Note that this parameter will be ignored if the parameter is set, as the DOS hidden attribute will then be stored inside a UNIX extended attribute. Note that this requires the to be set such that the world execute bit is not masked out (i.e. it must include 001). See the parameter for details.

### `map readonly`

Section: filename; Context: S; Type: enum; Default: `no`

This controls how the DOS read only attribute should be mapped from a UNIX filesystem. This parameter can take three different values, which tell smbd 8 how to display the read only attribute on files, where either is set to No , or no extended attribute is present. If is set to yes then this parameter is ignored . This is a new parameter introduced in Samba version 3.0.21. The three settings are : Yes - The read only DOS attribute is mapped to the inverse of the user or owner write bit in the unix permission mode set. If the owner write bit is not set, the read only attribute is reported as being set on the file. If the read only DOS attribute is set, Samba sets the owner, group and others write bits to zero. Write bits set in an ACL are ignored by Samba. If the read only DOS attribute is unset, Samba simply sets the write bit of the owner to one. Permissions - The read only DOS attribute is mapped to the effective permissions of the connecting user, as evaluated by smbd 8 by reading the unix permissions and filesystem ACL (if present). If the connecting user does not have permission to modify the file, the read only attribute is reported as being set on the file. No - The read only DOS attribute is unaffected by permissions, and can only be set by the method. This may be useful for exporting mounted CDs. Note that this parameter will be ignored if the parameter is set, as the DOS 'read-only' attribute will then be stored inside a UNIX extended attribute. The default has changed to no in Samba release 4.9.0 and above to allow better Windows fileserver compatibility in a default install. In addition the default setting of has been changed to Yes in Samba release 4.9.0 and above.

### `map system`

Section: filename; Context: S; Type: boolean; Default: `no`

This controls whether DOS style system files should be mapped to the UNIX group execute bit. Note that this parameter will be ignored if the parameter is set, as the DOS system attribute will then be stored inside a UNIX extended attribute. Note that this requires the to be set such that the group execute bit is not masked out (i.e. it must include 010). See the parameter for details.

### `max stat cache size`

Section: filename; Context: G; Type: integer; Default: `512`

This parameter limits the size in memory of any stat cache being used to speed up case insensitive name mappings. It represents the number of kilobyte (1024) units the stat cache can use. A value of zero, meaning unlimited, is not advisable due to increased memory usage. You should not need to change this parameter.

### `preserve case`

Section: filename; Context: S; Type: boolean; Default: `yes`

This controls if new filenames are created with the case that the client passes, or if they are forced to be the . See the section on NAME MANGLING for a fuller discussion.

### `short preserve case`

Section: filename; Context: S; Type: boolean; Default: `yes`

This boolean parameter controls if new files which conform to 8.3 syntax, that is all in upper case and of suitable length, are created upper case, or if they are forced to be the . This option can be use with yes to permit long filenames to retain their case, while short names are lowered. See the section on NAME MANGLING .

### `stat cache`

Section: filename; Context: G; Type: boolean; Default: `yes`

This parameter determines if smbd 8 will use a cache in order to speed up case insensitive name mappings. You should never need to change this parameter.

### `store dos attributes`

Section: filename; Context: S; Type: boolean; Default: `yes`

If this parameter is set Samba attempts to first read DOS attributes (SYSTEM, HIDDEN, ARCHIVE or READ-ONLY) from a filesystem extended attribute, before mapping DOS attributes to UNIX permission bits (such as occurs with and ). When set, DOS attributes will be stored onto an extended attribute in the UNIX filesystem, associated with the file or directory. When this parameter is set it will override the parameters , , and and they will behave as if they were set to off. This parameter writes the DOS attributes as a string into the extended attribute named "user.DOSATTRIB". This extended attribute is explicitly hidden from smbd clients requesting an EA list. On Linux the filesystem must have been mounted with the mount option user_xattr in order for extended attributes to work, also extended attributes must be compiled into the Linux kernel. In Samba 3.5.0 and above the "user.DOSATTRIB" extended attribute has been extended to store the create time for a file as well as the DOS attributes. This is done in a backwards compatible way so files created by Samba 3.5.0 and above can still have the DOS attribute read from this extended attribute by earlier versions of Samba, but they will not be able to read the create time stored there. Storing the create time separately from the normal filesystem meta-data allows Samba to faithfully reproduce NTFS semantics on top of a POSIX filesystem. The default has changed to yes in Samba release 4.9.0 and above to allow better Windows fileserver compatibility in a default install.

### `veto files`

Section: filename; Context: S; Type: string; Default: `No files or directories are vetoed`

This is a list of files and directories that are neither visible nor accessible. Each entry in the list must be separated by a '/', which allows spaces to be included in the entry. '*' and '?' can be used to specify multiple files or directories as in DOS wildcards. can also be used as a parametric option where NAME in veto files : NAME = specifies a user or group name with the same syntax as . This parametric form can be specified multiple times for different users or groups. This means that "veto files : NAME" set both in the [global] and the share section add up, whereas normally options set in a share section overwrite the default in the [global] section. Each filename must be a unix path, not a DOS path and must not include the unix directory separator '/'. Note that the option is applicable in vetoing files. One feature of the veto files parameter that it is important to be aware of is Samba's behaviour when trying to delete a directory. If a directory that is to be deleted contains nothing but veto files this deletion will fail unless you also set the parameter to yes . Setting this parameter will affect the performance of Samba, as it will be forced to check all files and directories for a match as they are scanned. Examples of use include: ; Veto any files containing the word Security, ; any ending in .tmp, and any directory containing the ; word root. veto files = /*Security*/*.tmp/*root*/ ; Veto some files for anyone and some files for specific users and groups veto files = /vetoforall1/ veto files : USER = /vetotoforuser/ veto files : GROUP = /vetoforgroup/ veto files : UNIVERSITY\Alumnis = /somefile.txt/ veto files : john@university.org = /anotherfile.txt/ veto files : S-1-5-21-123-456-789-1000 = /secretfile.txt/ ; Veto the Apple specific files that a NetAtalk server ; creates. veto files = /.AppleDouble/.bin/.AppleDesktop/Network Trash Folder/

### `veto oplock files`

Section: filename; Context: S; Type: string; Default: `No files are vetoed for oplock grants`

This parameter is only valid when the parameter is turned on for a share. It allows the Samba administrator to selectively turn off the granting of oplocks on selected files that match a wildcarded list, similar to the wildcarded list used in the parameter. You might want to do this on files that you know will be heavily contended for by clients. A good example of this is in the NetBench SMB benchmark program, which causes heavy client contention for files ending in .SEM . To cause Samba not to grant oplocks on these files you would use the line (either in the [global] section or in the section for the particular NetBench share. An example of use is: veto oplock files = /.*SEM/
