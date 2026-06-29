# Pam mount

pam_mount can be used to automatically mount an encrypted home partition (encrypted with, for example, LUKS or ECryptfs) on user log in.
It will mount your  (or whatever mount point you like) when you log in using your login manager or when logging in on console. The encrypted drive's passphrase should be the same as your linux user's password, so you do not have to type in two different passphrases to login.

## Configuration
Install the  package.

## Global (system) configuration
The module is configured in , see  for details. Edit the file as follows:

Notes:
* Insert 2 new lines at the end of the file, but before the last closing tag, .
*  should be replaced with your user name.
*  should be replaced with the corresponding device or container file.
*  can be changed to any  that is present in .  should work fine in most cases. Use  so that the loop device gets closed at logout for volumes needing it.
* Add mount options, if needed. Note that  does not read  and so all options must be specified. In the example,  matches the local  parameter idmap config ... : range = so that pam_mount is not called for a Unix only user. Kerberos is indicated by krb5, SMB3.0 is specified because the other end may not support SMB1 which is the default. Signing is enabled with the i on the end of krb5i. See  for more details.

## Local (per-user) configuration
pam_mount also supports allowing users to define their own mounts on login in files inside their home directories. Please consider the potential security implications of this change. To enable it, make sure the following line is present and active in :

It will have the effect of allowing each user to set their mounts in . The per-user config files only support  keywords, e.g.:

There are also some restrictions with regards to the mount options that you can and cannot select and some of them are mandatory (, , , , these can be lifted by editing ). Bind mounts appear to be unsupported. Ownership checks are also performed on the mountpoints.

## LUKS volumes
LUKS encrypted volumes can be configured simply as follows:

The volume is unlocked and mounted with mount.crypt, see  for details about the options.

## Veracrypt volumes
pam_mount does not support Veracrypt volumes natively, but there is a workaround:

If you also have LUKS volumes, you can use a different fstype for Veracrypt volume instead of  with , for example  with . Just make sure you do not use NCP filesystem.

## F2FS encryption
There is a trick to make pam_mount add a F2FS decryption key to your session keyring. The salt you chose when encrypting directory(es) with f2fscrypt needs to match the one in  (0x1111 in below example) and passphrase needs to match the user's login password. This example assumes you are not mounting FUSE filesystems with pam_mount. If you do, choose a different  tag pairs instead of  and , like .

 does not do anything except trigger the commands in  and . After login you can verify that your session keyring has a F2FS decryption key:

## Login manager configuration
In general, you have to edit configuration files in  so that pam_mount will be called on login. The correct order of entries in each file is important. It is necessary to edit  as shown below. If you use a display manager make sure its file includes . Example configuration files follow, with the added lines in bold.

The  line before  in session skips  ( means skip the next  lines) if the  service is running through the PAM stack (i.e. ). This avoids double mount attempts and errors relating to dropped privileges when the  instance is starting up. See and [https://www.suse.com/support/kb/doc/?id=000019569 for details.
