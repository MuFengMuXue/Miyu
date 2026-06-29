# Umask

The umask utility is used to control the file-creation mode mask, which determines the initial value of file permission bits for newly created files. The behaviour of this utility is standardized by POSIX and described in the POSIX Programmer's Manual. Because umask affects the current shell execution environment, it is usually implemented as built-in command of a shell.

## Meaning of the mode mask
The mode mask contains the permission bits that should not be set on a newly created file, hence it is the logical complement of the permission bits set on a newly created file. If some bit in the mask is set to , the corresponding permission for the newly created file will be disabled. Hence the mask acts as a filter to strip away permission bits and helps with setting default access to files.

The resulting value for permission bits to be set on a newly created file is calculated using bitwise material nonimplication (also known as abjunction), which can be expressed in logical notation:

 R: (D & (~M))

That is, the resulting permissions  are the result of bitwise conjunction of default permissions  and the bitwise negation of file-creation mode mask .

For example, let us assume that the file-creation mode mask is . Here the bitwise representation of each digit represents:

*  stands for the user permission bits not set on a newly created file
*  stands for the group permission bits not set on a newly created file
*  stands for the other permission bits not set on a newly created file

With the information provided by the table below this means that for a newly created file, for example owned by  user and  group,  has all the possible permissions (octal value ) for the newly created file, other users of the  group do not have write permissions (octal value ), and any other user does not have any permissions (octal value ) to the newly created file. So with the  mask taken for this example, files will be created with  permissions.

{| class="wikitable"
|+
! Octal !! Binary !! Meaning
|-
|  ||  || no permissions
|-
|  ||  || execute only
|-
|  ||  || write only
|-
|  ||  || write and execute
|-
|  ||  || read only
|-
|  ||  || read and execute
|-
|  ||  || read and write
|-
|  ||  || read, write and execute
|}

## Display the current mask value
To display the current mask, simply invoke  without specifying any arguments. The default output style depends on implementation, but it is usually octal:

When the  option, standardized by POSIX, is used, the mask will be displayed using symbolic notation. However, the symbolic notation value will always be the logical complement of the octal value, i.e. the permission bits to be set on the newly created file:

## Set the mask value
You can set the umask value through the umask command. The string specifying the mode mask follows the same syntactic rules as the mode argument of chmod (see the POSIX Programmer's Manual for details).

System-wide umask value can be set in  (e.g. ) or in the default shell configuration files (e.g. ). Most Linux distributions, including Arch, set a umask default value of  at . One can also set umask with  but it may be overridden by  or similar.

If you need to set a different value, you can either directly edit such file, thus affecting all users, or call  from your shell's user configuration file, e.g.  to only change your umask, however these changes will only take effect after the next login. To change your umask during your current session only, simply run  and type your desired value. For example, running  will give you read and write permissions for new files, and read, write and execute permissions for new folders.

As mentioned by ,  can also be used in the  section of the Users and groups#User database. See the discussion about setting UMASK in GECOS field

## Set umask value for KDE / Plasma
Setting the umask value via  does no longer work for KDE / Plasma sessions because these are started as systemd user units.

The umask value can be set via  or a systemd drop-in file:

After applying the above, if you don't see services/programs in your user session picking up the new umask value, then you can drop the same file into  and it will be applied to all services in your user session. To check what umask is being used by your user's services/programs run:

 $ ps -u $USER -o pid= | xargs -I % sh -c 'echo PID=%, $(grep '^Umask:' "/proc/%/status"), Process=$(ps -w -p % -o cmd=)'

Using  allows to set the system-wide umask value for both, text console and graphical KDE sessions in one single place. Any changes in  or systemd configuration can be omitted. Therefore,  needs to be enabled in a configuration file that is included by both,  and .

Add the following line to :

 # session    optional   pam_umask.so         umask=022

## Site-specific
Edit  and update the  value. For example:
