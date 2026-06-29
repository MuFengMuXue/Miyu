# Fscrypt

fscrypt is a tool for managing the native file encryption support of the ext4, F2FS, UBIFS, CephFS and Lustre file systems.

The underlying encryption mechanism in the kernel, which is integrated into the above file systems, is also sometimes called "fscrypt". To avoid ambiguity, this article calls the kernel feature "Linux native file encryption". With Linux native file encryption, different directories can use different encryption keys. In an encrypted directory, all file contents, filenames, and symlinks are encrypted. All subdirectories are encrypted too. Non-filename metadata, such as timestamps, the sizes and number of files, and extended attributes, is not encrypted.

As this article assumes the use of the fscrypt tool (and optionally pam_fscrypt, which goes along with fscrypt), most of it is not applicable to other userspace tools that can set up Linux native file encryption, for example systemd-homed.

## Alternatives to consider
To protect an entire file system with one password, block device encryption with dm-crypt (LUKS) is generally a better option, as it ensures that all files on the file system are encrypted, and also that all file system metadata is encrypted. fscrypt is most useful to encrypt specific directories, or to enable different encrypted directories to be unlockable independently—for example, per-user encrypted home directories.

Compared to eCryptfs, the Linux native file encryption controlled by fscrypt does not use file system stacking, which makes it more memory-efficient. It also uses more up-to-date cryptography and does not require root privileges to set up, which avoids the need for setuid binaries. eCryptfs is also no longer being actively developed, and its largest users (Ubuntu and Chrome OS) have migrated to other solutions.

See data-at-rest encryption for more information about other encryption solutions, and about what encryption does and does not do.

## Preparations
## Kernel
All officially supported kernels support native file encryption on ext4, F2FS, UBIFS and CephFS.

Users of custom kernels, make sure  is set.

## File system
## ext4
For ext4, the file system on which encryption is to be used must have the  feature flag enabled. To enable it, run:

 # tune2fs -O encrypt /dev/device

## F2FS
For F2FS, use  when creating the file system or  at a later time.

## Userspace tool
Install the  package. Then run:

 # fscrypt setup

This creates the file  and the directory .

Then, if the file system on which encryption is to be used is not the root file system, also run:

 # fscrypt setup mountpoint

where  is where the file system is mounted, e.g. .

This creates the directory  to store fscrypt policies and protectors.

## PAM module
To unlock login passphrase-protected directories automatically at login, and to keep login passphrase-protected directories in sync with changes to the login passphrase, adjust the system PAM configuration to enable pam_fscrypt.

Append the following line to the auth section in :

Insert the following lines before  in the session section:

Finally, append the following line to :

## Encrypt a directory
To encrypt an empty directory, run:

 $ fscrypt encrypt dir

Follow the prompts to create or choose a "protector". A protector is the secret or information that protects the directory's encryption key. The types of protectors include:

* "custom_passphrase". This is exactly what it sounds like, a user defined passphrase.
* "pam_passphrase". This is the login passphrase for a particular user. Directories using this type of protector will be automatically unlocked by pam_fscrypt (if enabled) when that user logs in. Be sure to follow the security recommendations before using this type of protector.

In both cases, the passphrase can be changed later, or the directory can be re-protected with another method.

Example for custom passphrase:

Example for PAM passphrase:

## Lock/unlock a directory
To unlock an encrypted directory, run:

 $ fscrypt unlock dir

fscrypt will prompt for the passphrase.

To lock an encrypted directory, run:

 $ fscrypt lock dir

## Encrypt a home directory
To encrypt a user's home directory, first ensure that all preparations have been completed, including enabling pam_fscrypt.

Then, create a new encrypted directory for the user:

 # mkdir /home/newhome
 # chown user:user /home/newhome
 # fscrypt encrypt /home/newhome --user=user

Select the option to protect the directory with the user's login passphrase.

Then copy the contents of the user's old home directory into the encrypted directory:

 # cp -a -T /home/user /home/newhome

If the cp method was used, check whether the directory is being automatically unlocked on login before actually switching to using it. The simplest way to do this is to reboot and log in as that user. Afterwards, run:

If it says  instead, then something is wrong with the PAM configuration, or the incorrect type of protector was selected.

Otherwise, replace the home directory:

 # mv /home/user /home/oldhome
 # mv /home/newhome /home/user
 # reboot

If everything is working as expected, delete the old home directory:

 # find /home/oldhome -type f -print0 | xargs -0 shred -n1 --remove=unlink
 # rm -rf /home/oldhome

## Encryption within Linux Containers (lxc)
Support to use fscrypt inside Linux Containers (lxc), or more generally in  where the file system's root directory is not visible has been added in v0.2.8.

## Lock directory when container is stopped
A systemd/User unit within the container can lock an encrypted directory when the container is stopped:

## Troubleshooting
See https://github.com/google/fscrypt/blob/master/README.md#troubleshooting for solutions to some common problems and also the open issues on Github.

## ext4: Encrypted files outside fscrypt encrypted directory
Encrypted regular files from an unlocked fscrypt can be moved into an unencrypted directory. While possible, it is not well supported, normally not desired and could led to later issues: It may not be noticed by the user, unless the according protector is locked or worse: deleted. https://github.com/google/fscrypt/issues/393

If you want to decrypt files permanently, copy them from the unlocked fscrypt directory into a regular unencrypted directory.== See also ==

* [https://github.com/google/fscrypt/blob/master/README.md Documentation for the fscrypt tool
* Documentation for Linux native file encryption
* The design document for the fscrypt tool
