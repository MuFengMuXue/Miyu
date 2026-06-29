# Systemd-homed

is a systemd service providing portable human-user accounts that are not dependent on current system configuration.

It achieves portability by moving all user-related information into a storage medium, optionally encrypted, and creating an  file that contains signed information about the user, password, what groups they belong to, UID/GID and other information that would typically be scattered over multiple files in .

This approach allows not only for a home directory portability, but also provides security by automatically managing a home directory encryption on login and locking it if the system is suspended.

## Installation
systemd-homed is part of and packaged with . The  package since version 20200721.1-2 comes with the necessary PAM configuration to allow systemd-homed user sessions.

## Usage
Start/enable the  service.

## Utilities
## homectl
homectl is the main utility you will use for homed. With it, you can create, update, and inspect users; their home directories; and their  files controlled by the  service.

The simplest usage of  is:

 # homectl create username

This command will create a user with the specified username, a free UID in range 60001–60513, create a group with the same name and a GID equal to the chosen UID, set the specified user as its member, and set the user's default shell to .

The home directory mount point is set to . The storage mechanism is chosen in this order:

#  if supported;
#  if LUKS is not supported and subvolume is supported;
#  if none of the above is supported and no other manual option is specified.

The image path for the LUKS mechanism is set to . The directory path for the directory mechanism is set to .

## userdbctl
A query tool used to inspect users, groups and group memberships provided by both classic UNIX mechanisms and systemd-homed.

## Storage mechanism
## LUKS home directory
A user home directory is stored in a Linux file system, inside an encrypted LUKS (Linux Unified Key Setup) volume inside a loopback file or any removable media.  To use this mechanism provide  to homectl.

If you are using a loopback file, in order to save space, the LUKS2 volume can be made to discard deleted data transparently. To use this mechanism provide  and  to homectl. Doing so can, however, reduce security under certain situations.

If you are using a removable media, make sure that these conditions are met:

* The image contains a GPT partition table. For now it should only contain a single partition, and that partition must have the type UUID . Its partition label must be the user name.
* This partition must contain a LUKS2 volume, whose label must be the user name. The LUKS2 volume must contain a LUKS2 token field of type systemd-homed. The JSON data of this token must have a record field, containing a string with base64-encoded data. This data is the JSON user record, in the same serialization as in , though encrypted. The JSON data of this token must also have an iv field, which contains a base64-encoded binary initialization vector for the encryption. The encryption used is the same as the LUKS2 volume itself uses, unlocked by the same volume key, but based on its own IV.
* Inside of this LUKS2 volume must be a Linux file system, one of ext4, btrfs and XFS. The file system label must be the user name.
* This file system should contain a single directory named after the user. This directory will become the home directory of the user when activated. It contains a second copy of the user record in the  file, like in the other storage mechanisms.

## fscrypt directory
A user home directory is stored the same way as when using the above method, but this time a native filesystem encryption is used. To use this mechanism provide  to homectl.

## Directory or Btrfs subvolume
A user home directory is stored in  and mounted to  using bind mount on unlocking. When this method is used no encryption is provided. To use this mechanism provide  or  to homectl.

## CIFS server
Here, the home directory is mounted from a CIFS (Common Internet File System) server at login. Note that CIFS is implemented via the Samba protocol. Use  on the homectl command line. The local password of the user is used to log into the CIFS service.

## User record properties
You can view an entire user record with:

 # homectl inspect username

You can modify or add to the user record with:

 # homectl update username --property=VALUE

See  for more options.

## Managing users
## Creation
Create a user with LUKS encryption:

 # homectl create username --storage=luks

Create a user with fscrypt encryption (make sure that fscrypt is enabled on the file system):

 # homectl create username --storage=fscrypt

Create a user with a specific UID, shell and groups:

 # homectl create username --shell=/usr/bin/zsh --uid=60100 --member-of=wheel,adm,uucp

Other options can be found in .

## Activation and deactivation
By default, the home of a user is automatically activated upon login.

 # homectl activate username
 # homectl deactivate username

## Deletion
It is possible to delete several users at the same time:

 # homectl remove username username2

## Tips and tricks
## Default mount options for LUKS backend
By default, the home directory will be mounted with  and . See You can override this and/or add extra options with . For example, to enable ACLs, use the standard level 3 zstd compression level, and allow deleting subvolumes as a regular user, use

 $ homectl update user --luks-extra-mount-options acl,compress=zstd,user_subvol_rm_allowed

## Forget key on suspend
The  option can be used with  entries in the files in  to enable forget key on suspend. No session manager at the moment supports this feature. Furthermore, TTY sessions do not support the reauthentication mechanism. So, when session managers start supporting this feature, the suspend option should only be enabled for them. Read  and the [https://github.com/linux-pam/linux-pam/blob/master/doc/sag/Linux-PAM_SAG.xml Linux-PAM System Administrators' Guide for more details.

## SSH remote unlocking
systemd-homed encrypts your home directory using your password, so SSH configured for public key authentication cannot mount it or read . A possible solution is to add authorized keys to your user record and require both public key and password for authentication. Add the following to :

Update your user record with your authorized keys while the user is unlocked using:

 # homectl update username --ssh-authorized-keys=@/path/to/mounted/home/.ssh/authorized_keys

From now on, SSH will ask you to enter your password after completing key-based authentication. systemd-homed will use it to unlock and mount your home directory.

## Mounting encrypted home directory for rescue
If you need to mount a systemd-homed-encrypted directory from a rescue disk or another machine, you will need to decrypt the directory outside of the systemd-homed framework. You may wish to keep a text file or script of this solution from the forums on your rescue disk for emergencies:

 # losetup -fP --show username.home
 # cryptsetup open /dev/loopXpY mappername
 # mount /dev/mapper/mappername /mnt/mountpoint

where,

*  is the file in the  directory with your username and the .home extension as its name
*  is the device in the  directory with the loop number of the loopback device created in the prior step and the partition number of the relevant partition, probably
*  is whatever alias you decide to adopt for the mapped device, e.g.
*  is wherever you want to mount your decrypted home directory

## Setup user with FIDO2 hmac-secret for authentication and encryption
This setup requires a FIDO2 security device, and asks for a pin to login and decrypt the home directory:

 # homectl create username --storage=fscrypt --fido2-device=auto --fido2-with-client-pin=yes --fido2-with-user-presence=no --recovery-key=yes

Setting up a recovery key is recommended in case the device is lost or broken. The recovery key will be used like a password to access the user and files. Instead of using a device pin, it is also possible to ask only for user presence, which requires touching the security device.
Currently, homectl also requires the user to set a password as alternative login which also works as a backup secret.

## Troubleshooting
## Home directory remains active after logging out of Plasma
After logging out of Plasma, there may still be active user processes (e.g. dbus-daemon) that prevent the home directory's deactivation.

This can be solved by enabling Plasma's systemd startup.

## User umask is ignored
There always is an umask set in , so the user's own umask set via homectl is currently ignored. See systemd issue 23007.

To solve this, set the umask in your login shell's startup files e.g.  or .

## Home directory in a dirty state
In the event of a forceful or unexpected shutdown or power outage, it is possible for the home directory to be left in a dirty state. In this case, the user will be locked out and authenticating to the home directory may require manual intervention. The following steps assumes that the LUKS2 encrypted loop back file storage mechanism is used, and fsck can be used in the underlying filesystem to repair it.

First, confirm the state of the loop back  file is dirty and determine the path of the user's loop back file:

 $ homectl inspect username

Next, using the path of the loop back file, follow the steps in #Mounting encrypted home directory for rescue.

Finally, attempt to repair the filesystem using fsck on the opened LUKS2 device:

 # fsck /dev/mapper/mappername

At this point, if the repair was successful, close the LUKS2 container, detach the loop back device, then attempt to re-authenticate normally via the systemd-homed service.
