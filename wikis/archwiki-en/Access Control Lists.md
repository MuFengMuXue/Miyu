# Access Control Lists

Access control list (ACL) provides an additional, more flexible permission mechanism for file systems. It is designed to assist with UNIX file permissions. ACL allows you to give permissions for any user or group to any disk resource.

## Installation
The  package is a dependency of systemd, it should already be installed.

## Enable ACL
To enable ACL, the filesystem must be mounted with the  option. You can use fstab entries to make it permanent on your system.

There is a possibility that the  option is already active as one of the default mount options on the filesystem. Btrfs and Ext2/3/4 filesystems are affected by this. Use the following command to check ext2/3/4 formatted partitions for the option:

Also check that the default mount options are not overridden, in such case you will see  in  in the relevant line.

You can set the default mount options of a filesystem using the  command, for example:

 # tune2fs -o acl /dev/sdXY

Using the default mount options instead of an entry in  is very useful for external drives, such partition will be mounted with  option also on other Linux machines. There is no need to edit  on every machine.

## Usage
## Set ACL
The ACL can be modified using the setfacl command.

To set permissions for a user ( is either the user name or ID):

 # setfacl -m "u:user:permissions"

To set permissions for a group ( is either the group name or ID):

 # setfacl -m "g:group:permissions"

To set permissions for others:

 # setfacl -m "other:permissions"

To allow all newly created files or directories to inherit entries from the parent directory (this will not affect files which will be moved into the directory):

 # setfacl -dm "entry"

To remove a specific entry:

 # setfacl -x "entry"

To remove the default entries:

 # setfacl -k

To remove all entries (entries of the owner, group and others are retained):

 # setfacl -b

The example below helps clarify two distinct steps in how the ACL mask works in , especially in the context of the  and default behavior:

# Recalculation of the mask (bitwise OR / "union")
# Applying the mask (bitwise AND / limiting)

 user:bob: rw-
 group:dev: r--
 group:: r-x
 → mask: rwx (union)

 Effective rights:
 bob: rw-
 dev: r--
 group:: r-x

The 2003 USENIX document POSIX Access Control Lists on Linux has more information.

## Show ACL
To show permissions, use:

 # getfacl

## Examples
Set all permissions for user  to file named :

 # setfacl -m "u:johnny:rwx" abc

Check permissions:

Change permissions for user :

 # setfacl -m "u:johnny:r-x" abc

Check permissions:

Remove all ACL entries:

 # setfacl -b abc

Check permissions:

## Output of ls command
You will notice that there is an ACL for a given file because it will exhibit a  (plus sign) after its Unix permissions in the output of .

## Execution permissions for private files
The following technique describes how a process like a web server can be granted access to files that reside in a user's home directory, without compromising security by giving the whole world access.

In the following we assume that the web server runs as the user  and grant it access to 's home directory .

The first step is granting execution permissions for the user :

 # setfacl -m "u:http:--x" /home/geoffrey

Since the user  is now able to access files in , others no longer need access:

 # chmod o-rx /home/geoffrey

Use  to verify the changes:

As the above output shows, 's no longer have any permissions, but the user  is still able to access the files, thus security might be considered increased.

If you need to give write access for the user  on specific directories and/or files, run:

 # setfacl -dm "u:http:rwx" /home/geoffrey/project1/cache
