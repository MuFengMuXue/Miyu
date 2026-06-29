# Gocryptfs

From gocryptfs:

:gocryptfs uses file-based encryption that is implemented as a mountable FUSE filesystem. Each file in gocryptfs is stored one corresponding encrypted file on the hard disk.
:The highlights are: Scrypt password hashing, GCM encryption for all file contents, EME wide-block encryption for file names with a per-directory IV.

See the gocryptfs project home for further introduction of its features, benchmarks, etc. See Data-at-rest encryption#Comparison table for an overview of alternative methods and EncFS for the direct alternative.

## Installation
Install  or .

As a FUSE filesystem, gocryptfs is fully configurable by the user and stores its configuration files in the user's directory paths.

## Usage
See  and its examples first. As a first-time user, check the gocryptfs best practices next.

Upon initialization of the cryptography for a directory, the master key is output before it is cryptographically wrapped in the  file. It can be used to recreate the configuration with a restore procedure. If it happens that the master key itself is lost but the configuration file available, see  for how to output it again with the encryption password.

## Example using normal mode
Create  directory to store encrypted data, and  directory to access them decrypted. Then, run gocryptfs initialization to setup encryption.

To open the encrypted directory  and access it from :

You now have a working gocryptfs that is stored in  and mounted to . You can verify this by creating a blank file in the  directory. This file will show up encrypted in the  directory.

When done unmount the plain directory, optionally delete the empty folder:

To show filesystem information use the  option, consistency can be checked with .

## Example using reverse mode
A major application for file-based encryption methods are encrypted backups. FUSE-based filesystems are flexible for this, since they allow a wide array of backup destinations using standard tools. For example, a gocryptfs-encrypted FUSE mount point can be easily created directly on a Samba/NFS share or Dropbox location, synchronized to a remote host with rsync, or just be manually copied to a remote backup storage.

The reverse mode of gocryptfs is particularly useful for creating encrypted backups, since it requires virtually no extra storage capacity on the machine to back up.

The following shows an example of user archie creating a backup of :

First, archie initializes the configuration for the home directory:

Second, an empty directory for the encrypted view of the home directory is created and mounted:

Third, archie creates a backup of the encrypted directory, a simple local copy for this example:

 $ cp -a /tmp/crypt /tmp/backup

and done.

The encrypted directory can stay mounted for the user session, or be unmounted manually:
 $ fusermount -u /tmp/crypt
 $ rmdir /tmp/crypt

To restore from the encrypted backup, a plain-text view is mounted using gocryptfs's normal mode:

Now the required files can be restored.

## Example using the FIDO2 option
Options to use U2F hardware tokens, instead of a password, to initialize and mount an encrypted directory are available. It is possible to enforce or toggle FIDO2 token options for PIN/user-presence (touch)/user-verification (fingerprint) verification for the decryption (see ).

The following initializes, mounts and unmounts an encrypted directory with a token and PIN-verification:

The user-presence interaction () was used, because the token defaults to it. Using a  option would toggle it during initialization.

## Mounting automatically with pam_mount
If the encrypted directory uses the same password as your user account, you can automount it on login with pam_mount.

While the gocryptfs command works with fuse3 when directly invoked, pam_mount tries to use  from fuse2.

You need to add pam_mount to  as specified in pam_mount#Login manager configuration and configure the directories to mount in a  configuration. An example is given below:

## GUI wrappers
There are a couple of applications available that provide a graphical user interface for gocryptfs.

## SiriKali
A Qt/C++ GUI application that manages gocryptfs, eCryptfs, , EncFS, fscrypt, and securefs encrypted folders. It can also connect to SSH servers using SSHFS. Install it from .

## gocryptfs-ui
A bash script gocryptfs-ui provides a simple  GUI around the gocryptfs command line utility to mount and unmount an encrypted directory. It includes a desktop launcher. Install it from .

## cryptor
cryptor is a / based application providing a GUI to create and mount encrypted directories. It can store configuration files with a list of encrypted directories, has tray-icon support and includes a desktop launcher. Install it from .
