# Users and groups

Users and groups are used on GNU/Linux for access control—that is, to control access to the system's files, directories, and peripherals. Linux offers relatively simple/coarse access control mechanisms by default. For more advanced options, see ACL, Capabilities and PAM#Configuration How-Tos.

## Overview
A user is anyone who uses a computer. In this case, we are describing the names which represent those users. It may be Mary or Bill, and they may use the names Dragonlady or Pirate in place of their real name. All that matters is that the computer has a name for each account it creates, and it is this name by which a person gains access to use the computer. Some system services also run using restricted or privileged user accounts.

Managing users is done for the purpose of security by limiting access in certain specific ways. The superuser (root) has complete access to the operating system and its configuration; it is intended for administrative use only. Unprivileged users can use several programs for controlled privilege elevation.

Any individual may have more than one account as long as they use a different name for each account they create. Further, there are some reserved names which may not be used such as "root".

Users may be grouped together into a "group", and users may be added to an existing group to utilize the privileged access it grants.

## Permissions and ownership
From In UNIX Everything is a File:

:The UNIX operating system crystallizes a couple of unifying ideas and concepts that shaped its design, user interface, culture and evolution. One of the most important of these is probably the mantra: "everything is a file," widely regarded as one of the defining points of UNIX.

:This key design principle consists of providing a unified paradigm for accessing a wide range of input/output resources: documents, directories, hard-drives, CD-ROMs, modems, keyboards, printers, monitors, terminals and even some inter-process and network communications. The trick is to provide a common abstraction for all of these resources, each of which the UNIX fathers called a "file." Since every "file" is exposed through the same API, you can use the same set of basic commands to read/write to a disk, keyboard, document or network device.

From Extending UNIX File Abstraction for General-Purpose Networking:

:A fundamental and very powerful, consistent abstraction provided in UNIX and compatible operating systems is the file abstraction. Many OS services and device interfaces are implemented to provide a file or file system metaphor to applications. This enables new uses for, and greatly increases the power of, existing applications — simple tools designed with specific uses in mind can, with UNIX file abstractions, be used in novel ways. A simple tool, such as cat, designed to read one or more files and output the contents to standard output, can be used to read from I/O devices through special device files, typically found under the  directory. On many systems, audio recording and playback can be done simply with the commands, "" and "," respectively.

Every file on a GNU/Linux system is owned by a user and a group. In addition, there are three types of access permissions: read, write, and execute. Different access permissions can be applied to a file's owning user, owning group, and others (those without ownership). One can determine a file's owners and permissions by viewing the long listing format of the ls command:

The first column displays the file's permissions (for example, the file  has permissions ). The third and fourth columns display the file's owning user and group, respectively. In this example, all files are owned by the root user and the root group.

In this example, the  directory is owned by the root user and the vboxsf group. It is also possible to determine a file's owners and permissions using the stat command:

Owning user:

Owning group:

Access rights:

Access permissions are displayed in three groups of characters, representing the permissions of the owning user, owning group, and others, respectively. For example, the characters  indicate that the file's owner has read and write permission, but not execute (), whilst users belonging to the owning group and other users have only read permission ( and ). Meanwhile, the characters  indicate that the file's owner and users belonging to the owning group all have read, write, and execute permissions ( and ), whilst other users are denied access (). The first character represents the file's type.

List files owned by a user or group with the find utility:

 # find / -group groupname

 # find / -group groupnumber

 # find / -user user

A file's owning user and group can be changed with the chown (change owner) command. A file's access permissions can be changed with the chmod (change mode) command.

See , , and Linux file permissions for additional detail.

## Shadow
The user, group and password management tools on Arch Linux come from the  package, which is a dependency of the  meta package.

## File list
{| class="wikitable"
! File || Purpose
|-
|  || Secure user account information
|-
|  || User account information
|-
|  || Contains the shadowed information for group accounts
|-
|  || Defines the groups to which users belong
|}

## User management
To list users currently logged on the system, the who command can be used. To list all existing user accounts including their properties stored in the user database, run  as root. See  for the description of the output format.

To add a new user, use the useradd command:

 # useradd -m -G additional_groups -s login_shell username

; /: the user's home directory is created as . The directory is populated by the files in the skeleton directory. The created files are owned by the new user.
; /: a comma separated list of supplementary groups which the user is also a member of. The default is for the user to belong only to the initial group.
; /: a path to the user's login shell. Ensure the chosen shell is installed if choosing something other than Bash. The default shell for newly created user can be set in .

If an initial login group is specified by name or number, it must refer to an already existing group. If not specified, the behaviour of useradd will depend on the  variable contained in . The default behaviour () is to create a group with the same name as the username.

When the login shell is intended to be non-functional, for example when the user account is created for a specific service,  may be specified in place of a regular shell to politely refuse a login (see ).

See  for other supported options.

## Example adding a user
To add a new user named , creating its home directory and otherwise using all the defaults in terms of groups, directory names, shell used and various other parameters:

 # useradd -m archie

Although it is not required to protect the newly created user  with a password, it is highly recommended to do so:

 # passwd archie

The above useradd command will also automatically create a group called  and makes this the default group for the user . Making each user have their own group (with the group name same as the user name) is the preferred way to add users.

You could also make the default group something else using the  option, but note that, in multi-user systems, using a single default group (e.g. ) for every user is not recommended. The reason is that typically, the method for facilitating shared write access for specific groups of users is setting user umask value to , which means that the default group will by default always have write access to any file you create. See also User Private Groups. If a user must be a member of a specific group specify that group as a supplementary group when creating the user.

In the recommended scenario, where the default group has the same name as the user name, all files are by default writeable only for the user who created them. To allow write access to a specific group, shared files/directories can be made writeable by default for everyone in this group and the owning group can be automatically fixed to the group which owns the parent directory by setting the setgid bit on this directory:

 # chmod g+s our_shared_directory

Otherwise the file creator's default group (usually the same as the user name) is used.

If a GID change is required temporarily you can also use the newgrp command to change the user's default GID to another GID at runtime. For example, after executing  files created by the user will be associated with the  GID, without requiring a re-login. To change back to the default GID, execute newgrp without a groupname.

## Changing user defaults
The default values used for creating new accounts are set in  and can be displayed using . For example, to change the default shell globally, set . A different shell can also be specified individually with the / option. Use  to list valid login shells.

Files can also be specified to be added to newly created user home directories in . This is useful for minimalist window managers where config files need manual configuration to reach DE-familiar behavior. For example, to set up default shortcuts for all newly created users:

 # mkdir /etc/skel/.config
 # cp ~archie/.config/sxhkd /etc/skel/.config

See also: Display manager#Run ~/.xinitrc as a session to add xinitrc as an option to all users on the display manager.

## Example adding a system user
System users can be used to run processes/daemons under a different user,  protecting (e.g. with chown) files and/or directories and more examples of computer hardening.

With the following command a system user without shell access and without a  directory is created (optionally append the   parameter to create a group with the same name as the user, and add the user to this group):

 # useradd --system -s /usr/bin/nologin username

If the system user requires a specific user and group ID, specify them with the / and / options when creating the user:

 # useradd --system -u 850 -g 850 -s /usr/bin/nologin username

## Change a user's login name or home directory
To change a user's home directory:

 # usermod -d /my/new/home -m username

The  option also automatically creates the new directory and moves the content there.

To change a user's login name:

 # usermod -l newname oldname

Changing a username is safe and easy when done properly, just use the usermod command. If the user is associated to a group with the same name, you can rename this with the groupmod command.

Alternatively, the  file can be edited directly, see #User database for an introduction to its format.

Also keep in mind the following notes:

* If you are using sudo make sure you update your configuration to reflect the new username(s) (via the visudo command as root).
* Personal crontabs need to be adjusted by renaming the user's file in  from the old to the new name, and then opening  to change any relevant paths and have it adjust the file permissions accordingly.
* Wine's personal directories/files' contents in ,  and possibly more need to be manually renamed/edited.
* Certain Thunderbird addons, like Enigmail, may need to be reinstalled.
* Anything on your system (desktop shortcuts, shell scripts, etc.) that uses an absolute path to your home dir (i.e. ) will need to be changed to reflect your new name. To avoid these problems in shell scripts, simply use the  or  variables for home directories.
* Also do not forget to edit accordingly the configuration files in  that relies on your absolute path (e.g. Samba, CUPS, so on). A nice way to learn what files you need to update involves using the grep command this way:

## Other examples of user management
To enter user information for the GECOS comment (e.g. the full user name), type:

 # chfn username

(this way chfn runs in interactive mode).

Alternatively the GECOS comment can be set more liberally with:

 # usermod -c "Comment" username

To mark a user's password as expired, requiring them to create a new password the first time they log in, type:

 # chage -d 0 username

User accounts may be deleted with the userdel command:

 # userdel -r username

The  option specifies that the user's home directory and mail spool should also be deleted.

To change the user's login shell:

 # usermod -s /usr/bin/bash username

## User database
Local user information is stored in the plain-text  file: each of its lines represents a user account, and has seven fields delimited by colons.

 account:password:UID:GID:GECOS:directory:shell

Where:

*  is the user name. This field cannot be blank. Standard *NIX naming rules apply.
*  is the user password.
*  is the numerical user ID. In Arch, the first login name (after root) for a so called normal user, as opposed to services, is UID 1000 by default; subsequent UID entries for users should be greater than 1000.
*  is the numerical primary group ID for the user. Numeric values for GIDs are listed in /etc/group.
*  is an optional field used for informational purposes; usually it contains the full user name, but it can also be used by services such as finger and managed with the chfn command. This field is optional and may be left blank.
*  is used by the login command to set the  environment variable. Several services with their own users use , but normal users usually set a directory under .
*  is the path to the user's default command shell. This field is optional and defaults to .

Example:

 archie:x:1001:1003:Archie,some comment here,,:/home/archie:/usr/bin/bash

Broken down, this means: user , whose password is in , whose UID is 1001 and whose primary group is 1003. Archie is their full name and there is a comment associated to their account; their home directory is  and they are using Bash.

The pwck command can be used to verify the integrity of the user database. It can sort the user list by UID at the same time, which can be helpful for comparison:

 # pwck -s

## Automatic integrity checks
Instead of running / manually, the systemd timer , which is part of, and is enabled by, installation of the  package, will start  daily.  will run  and  to verify the integrity of both password and group files.

If discrepancies are reported, group can be edited with the  command and users with . This provides an extra margin of protection in that these commands lock the databases for editing. Note that the default text editor is vi, but an alternative editor will be used if the  environment variable is set, then that editor will be used instead.

## Keeping users on the live system in parity with systemd sysuser.d defaults
As packages adopt the change-sysusers-to-fully-locked-system-accounts, package created system users generated in the past will not inherit new package defaults for the increased security of locked/expired status. These users need to be modified manually for this change. user-analysis.sh does just that.

In addition, the script also identifies orphaned users (those created by a package no longer on the system) and can automatically delete them.

## Group management
 is the file that defines the groups on the system (see  for details). There is also its companion  which is rarely used. Its details are at .

Display group membership with the groups command:

 $ groups user

If  is omitted, the current user's group names are displayed.

The id command provides additional detail, such as the user's UID and associated GIDs:

 $ id user

To list all groups on the system:

 $ cat /etc/group

Create new groups with the groupadd command:

 # groupadd group

Add users to a group with the gpasswd command (see  regarding errors):

 # gpasswd -a user group

Alternatively, add a user to additional groups with usermod (replace  with a comma-separated list):

 # usermod -aG additional_groups username

Modify an existing group with the groupmod command, e.g. to rename the  group to :

 # groupmod -n new_group old_group

To delete existing groups:

 # groupdel group

To remove users from a group:

 # gpasswd -d user group

The grpck command can be used to verify the integrity of the system's group files.

## Group list
This section explains the purpose of the essential groups from the  package. There are many other groups, which will be created with correct GID when the relevant package is installed. See the main page for the software for details.

## User groups
Non-root workstation/desktop users often need to be added to some of following groups to allow access to hardware peripherals and facilitate system administration:

{| class="wikitable"
! Group || Affected files || Purpose
|-
| adm || || Administration group, commonly used to give read access to protected logs. It has full read access to journal files.
|-
| ftp ||  || Access to files served by FTP servers.
|-
| games ||  || Access to some game software.
|-
| http ||  || Access to files served by HTTP servers.
|-
| log || || Access to log files in  created by syslog-ng.
|-
| rfkill ||  || Right to control wireless devices power state (used by rfkill).
|-
| sys || || Right to administer printers in CUPS.
|-
| systemd-journal ||  || Can be used to provide read-only access to the systemd logs, as an alternative to  and  Otherwise, only user generated messages are displayed.
|-
| uucp || , , , ,  || RS-232 serial ports and devices connected to them.
|-
| wheel || || Administration group, commonly used to give privileges to perform administrative actions. It has full read access to journal files and the right to administer printers in CUPS. Can also be used to give access to the sudo and su utilities (neither uses it by default). Gives access to the run0 utility.
|}

## System groups
The following groups are used for system purposes, an assignment to users is only required for dedicated purposes:

{| class="wikitable"
! Group || Affected files || Purpose
|-
| dbus || || used internally by
|-
| kmem || , ,  ||
|-
| locate || , , ,  || See Locate.
|-
| lp || ,  || Access to parallel port devices (printers and others).
|-
| mail ||  ||
|-
| nobody || || Unprivileged group.
|-
| proc ||  || A group authorized to learn processes information otherwise prohibited by  mount option of the [https://docs.kernel.org/filesystems/proc.html proc file system. The group must be explicitly set with the  mount option.
|-
| root ||  || Complete system administration and control (root, admin).
|-
| smmsp || || sendmail group.
|-
| tty || , , ,  ||
|-
| utmp || , ,  || See Wikipedia:utmp#utmp, wtmp and btmp.
|-
|}

## Pre-systemd groups
Before arch migrated to systemd, users had to be manually added to these groups in order to be able to access the corresponding devices. This way has been deprecated in favour of udev marking the devices with a  tag and logind assigning the permissions to users dynamically via ACLs according to which session is currently active. Note that the session must not be broken for this to work (see General troubleshooting#Session permissions to check it).

There are some notable exceptions which require adding a user to some of these groups: for example if you want to allow users to access the device even when they are not logged in. However, note that adding users to the groups can even cause some functionality to break (for example, the  group will break fast user switching and allows applications to block software mixing).

{| class="wikitable"
! Group || Affected files || Purpose
|-
| audio || , ,  || Direct access to sound hardware, for all sessions. It is still required to make ALSA and OSS work in remote sessions, see ALSA#User privileges, otherwise not recommended. Unlike on certain other distros, this group is not used for realtime privileges.
|-
| disk || , ,  || Access to block devices not affected by other groups such as , , and .
|-
| floppy ||  || Access to floppy drives.
|-
| input || ,  || Access to input devices. Introduced in systemd 215 |-
| kvm ||  || Access to virtual machines using KVM.
|-
| optical || ,  || Access to optical devices such as CD and DVD drives.
|-
| scanner ||  || Access to scanner hardware.
|-
| storage || , || Used to gain access to removable drives such as USB hard drives, flash/jump drives, MP3 players; enables the user to mount storage devices.[https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/thread/7ITKMBKKHUB4SUN5SCS7FLSTEILKGIJH/#IEZCAXRIBMXGOMMW7C4Z3ADED32W24ZI
Now solely for direct access to tapes if no custom udev rules is involved.https://gitlab.archlinux.org/archlinux/packaging/packages/systemd/-/blob/main/0001-Use-Arch-Linux-device-access-groups.patch][https://github.com/systemd/systemd/blame/aaaf42cb44d4fcd598fca441a11856f3e8dd06d8/rules.d/50-udev-default.rules.in#L69][https://elixir.bootlin.com/linux/v5.5.6/source/include/scsi/scsi_proto.h#L251.

Also required for manipulating some devices via udisks/udisksctl.
|-
| video || ,  || Access to video capture devices, 2D/3D hardware acceleration, framebuffer (X can be used without belonging to this group).
|}

## Unused groups
The following groups are currently not used for any purpose:

{| class="wikitable"
! Group || Affected files || Purpose
|-
| bin || none || Historical
|-
| daemon || ||
|-
| lock || || Used for lockfile access. Required by e.g. .
|-
| mem || ||
|-
| network || || Unused by default. Can be used e.g. for granting access to NetworkManager (see NetworkManager#Set up PolicyKit permissions).
|-
| power || ||
|-
| uuidd || ||
|-
| users || || The primary group for users when user private groups are not used (generally not recommended), e.g. when creating users with  in  or the / option of useradd.
|}

## Other tools related to these databases
 can be used to read a particular record.

 $ getent group tty

As warned in #User database, using specific utilities such as  and , is a better way to change the databases. Nevertheless, there are times when editing them directly is looked after. For those times, ,  are provided. It is strongly recommended to use these tailored editors over using a general text editor as they lock the databases against concurrent editing. They also help prevent invalid entries and/or syntax errors. Note that Arch Linux prefers usage of specific tools, such as chage, for modifying the shadow database over using  and  from . See also .

 and  are some of the tools for viewing utmp related files.
