# EncFS

EncFS is a userspace stackable cryptographic file-system similar to eCryptfs, and aims to secure data with the minimum hassle. It uses FUSE to mount an encrypted directory onto another directory specified by the user. It does not use a loopback system like some other comparable systems such as TrueCrypt and dm-crypt.

EncFS is definitely the simplest software if you want to try disk encryption on Linux.

Advantages of EncFS: Firstly, it does not require any root privileges to implement; any user can create a repository of encrypted files. Secondly, one does not need to create a single file and create a file-system within that; it works on existing file-system without modifications.

Disadvantages: The encrypted files are not stored in their own file, someone who obtains access to the system can still see the underlying directory structure, the number of files, their sizes and when they were modified. They cannot see the contents, however.

This particular method of securing data is obviously not perfect, but there are situations in which it is useful.

For more details on how EncFS compares to other disk encryption solutions, see Data-at-rest encryption#Comparison table.

## Comparison to eCryptFS
eCryptFS is implemented in kernelspace and therefore a little bit harder to configure. You have to remember various encryption options (used cyphers, key type, etc...). With EncFS this is not the case, because it stores the encryption metadata information in a per-directory configuration file (). So you do not have to remember anything (except the passphrase).

The performance of both depends on the type of disk activity. While eCryptFS can perform faster in some cases because there is less overhead by context switching (between kernel and userspace), EncFS has advantages in other cases because the encryption metadata is centralized and not stored in the individual files' headers. For more information benchmark examples are provided by the EncFS project.

## Installation
Install the  package.

## Usage
To create a secured repository, type:
 $ encfs ~/.encrypted ~/origin
Note that absolute paths must be used. This will be followed by a prompt about whether you want to go with the default options, expert configuration or a paranoid preset. The first is a fairly secure default setup. The second allows specifying algorithms and other options. After entering a key for the encryption, the encoded file-system will be created and mounted. The encoded files are stored, in this example, at , and their unencrypted versions in .

To unmount the file-system, type:
 $ fusermount -u ~/name

To remount the file-system, issue the first command, and enter the key used to encode it. Once this has been entered, the file-system will be mounted again.

## Changing the password
To change the password of a directory encrypted by EncFS, the following command can be used:

 $ encfsctl passwd ~/.name

In this example,  is the path to the directory which contains the encoded files. The tool will ask for your current password and afterwards, you will be able to set a new one.

## User friendly mounting
## Gnome Encfs Manager
The Gnome Encfs Manager is an easy to use manager and mounter for encfs stashes featuring per-stash configuration, Gnome Keyring support, a tray menu inspired by Cryptkeeper but using the AppIndicator API and lots of unique features.

Both  and a slightly more up to date  are available.

## Mount using encfsui
A bash script encfsui provides a simple  gui around the EncFS command line utility to mount and unmount an encrypted directory. It includes a desktop launcher. Install it from .

## Mount via fstab
Adding an entry in  will allow you to mount the encfs volume with a simple  and you will be prompted for your password.

The  option prevents an attempt to mount the volume at boot, which could delay the boot process while it waits for a password to be entered.   can be omitted if only the  user should be able to mount the volume.

## Mount at login using pam_encfs
Install . See also:
* https://web.archive.org/web/20160505055352/http://pam-encfs.googlecode.com/svn/trunk/README
* https://web.archive.org/web/20160428084352/http://pam-encfs.googlecode.com/svn/trunk/pam_encfs.conf
* https://wiki.edubuntu.org/EncryptedHomeFolder
* https://code.google.com/archive/p/pam-encfs/

## Single password
## /etc/pam.d/
Note that when you are using try_first_pass parameter to pam_unix.so then you will have to set EncFS to use same password as you are using to login (or vice-versa) and you will be entering just single password. Without this parameter you will need to enter two passwords.

## setup pam_encfs for all login methods
Put encfs line to /etc/pam.d/system-login as follows:

## login
This section tells how to make encfs automount when you are logging in by virtual terminal.

Edit the file :

## gdm
This section explains how to make encfs automount when you are logging in by GDM.

Edit the file .

Insert (do not overwrite) the following into the bottom of gdm-password:

Save and exit.

## Configuration
Edit  :

Recommended: comment out the line

 encfs_default --idle=1

This flag will unmount your encrypted folder after 1 minute of inactivity.  If you are automounting this on login, you probably would like to keep this mounted for as long as you are logged in.

At the bottom, comment any existing demo entries and add:

Also, if you see the following line, remove  from the options. Otherwise, it will be in conflict with  defined above.

Next, edit :
Uncomment:

 user_allow_other

To test your config, open a new virtual terminal (e.g. ) and login.  You should see pam successfuly mount your EncFS folder.

## Mount at login using pam_mount
Install and configure pam_mount as explained on its wiki page. EncFS mounts can be specified in pam_mount's configuration file as follows:

The EncFS mounts need to have the same password than your user account. The  option makes it possible to mount the encrypted file system even when the mount point is non-empty. You may remove this option if this is not the desired behaviour.

It is possible to mount multiple EncFS folders at login specifying multiple consecutive  entries in the configuration file.

## Encrypted backup
## Backup encrypted directory
An encrypted directory may be backed up and restored to another location like it is. This is possible, because the configuration file for the encryption options/metadata is actually stored in the directory itself in plaintext in the hidden  file. This poses no direct problem, because the password is not in it.

However, if you - for example - store the backup on a remote location (e.g. in the cloud) or a portable device, you might feel uncomfortable about it. In this case it also is no problem to manually move the file out of the directory before creating the backup. You can even move it permanently and still mount and access the files, if you pass its location to encfs via the  environment variable. For the #Usage example above:
 $ mv ~/.name/.encfs6.xml ~/.
 $ ENCFS6_CONFIG=~/.encfs6.xml encfs ~/.name ~/name

## Backup plaintext directory
The following example assumes you want to create an encrypted  backup of an existing plaintext directory  which contains the file .

First, we create the encrypted backup of the existing plaintext directory:

 $ encfs --reverse ~/mythesis /tmp/thesisbackup

Note the directory order is reversed to normal usage in this case. Using the  option has two effects: Firstly, the configuration file is now stored in the plaintext directory and  only contains it in encrypted form. Secondly, the files in  are not persistent. They will vanish once it is unmounted (no, this is not due to usage of the  mountpoint).

For the second reason, now is the time to copy the encrypted files to the desired backup location, before unmounting the temporary encfs directory again:
 $ cp -R /tmp/thesisbackup/* /mnt/usbstick/
 $ fusermount -u /tmp/thesisbackup
and done.

To restore (or view) the backup, we need access to the encryption options in plaintext, which has to be passed to encfs with the environment variable  (we use a different directory in order not to mess up the existing ):

 $ ENCFS6_CONFIG=~/mythesis/.encfs6.xml encfs ~/mnt/usbstick/thesisbackup ~/restoremythesis

If you now list the restore location, it will contain two files:

 $ ls -la ~/restoremythesis
 ...
 -rw-r--r--  1 student student    1078  3. Jan 12:33 .encfs6.xml
 -rw-r--r--  1 student student      42  3. Jan 12:33 thesis.txt
 ...
