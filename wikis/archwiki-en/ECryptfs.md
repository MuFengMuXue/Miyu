# ECryptfs

This article describes basic usage of eCryptfs. It guides you through the process of creating a private and secure encrypted directory within your home directory to store sensitive files and private data.

In implementation eCryptfs differs from dm-crypt, which provides a block device encryption layer, while eCryptfs is an actual file-system &ndash; a stacked cryptographic file system. For comparison of the two you can refer to Data-at-rest encryption#Block device vs stacked filesystem encryption. One distinguished feature is that the encryption is stacked on an existing filesystem; eCryptfs can be mounted onto any single existing directory and does not require a separate partition (or size pre-allocation).

## Basics
As mentioned in the summary eCryptfs does not require special on-disk storage allocation effort, such as a separate partition or pre-allocated space. Instead, you can mount eCryptfs on top of any single directory to protect it. That includes, for example, a user's entire home directory or single dedicated directories within it. All cryptographic metadata is stored in the headers of files, so encrypted data can be easily moved, stored for backup and recovered. There are other advantages, but there are also drawbacks, for instance eCryptfs is not suitable for encrypting complete partitions which also means you cannot protect swap space with it (but you can, of course, combine it with Dm-crypt/Swap encryption). If you are just starting to set up disk encryption, swap encryption and other points to consider are covered in Data-at-rest encryption#Preparation.

To familiarize with eCryptfs a few points:

* As a stacked filesystem, a mounting of an eCryptfs directory refers to mounting a (stacked) encrypted directory to another unencrypted mount point (directory) at Linux kernel runtime.
* It is possible to share an encrypted directory between users. However, the encryption is linked to one passphrase so this must be shared as well. It is also possible to share a directory with differently encrypted files (different passphrases).
* Several eCryptfs terms are used throughout the documentation:
** The encrypted directory is referred to as the lower and the unencrypted as the upper directory throughout the eCryptfs documentation and this article. While not relevant for this article, the Overlay filesystem introduced with Linux 3.18 uses the same upper/lower nomenclature for the stacking of filesystems.
** The mount passphrase (or key) is what gives access to the encrypted files, i.e. unlocks the encryption. eCryptfs uses the term wrapped passphrase to refer to the cryptographically secured mount passphrase.
**  refers to a File's Encryption Key Encryption Key (see kernel documentation).
**  refers to a File Name Encryption Key, a key to (optionally) encrypt the filenames stored in the encrypted directory.

Before using eCryptfs, the following disadvantages should be checked for applicability.

## Deficiencies
* Ease of use
:The  package provides several different ways of setting up eCryptfs. The high-level #Ubuntu tools are the easiest to use, but they hard-code the lower directory path and other settings, limiting their usefulness. The package also includes low-level tools which are fully configurable, but they are somewhat more difficult to use compared to alternatives like EncFS.

* File name length
:File names longer than 143 bytes cannot be encrypted (with the  option) when stacked on a filesystem with a maximum file name length of 255 bytes.This can break some programs in your home directory (for example Symfony caching).

* Network storage mounts
:eCryptfs has long-standing [https://bugs.launchpad.net/ecryptfs/+bug/277578 bugs when used on top of NFS and possibly other networked filesystems, for example, #Mounting may fail on a remote host when connecting via Mosh. It is always possible to use eCryptfs on a local directory and then copy the encrypted files from the local directory to a network host. However, if you want to set up eCryptfs directly on top of an NFS mount, with no local copy of the files, eCryptfs may crash or behave incorrectly. If in doubt, EncFS may be a better choice in this case.

* Sparse files
:Sparse files written to eCryptfs will produce larger, non-sparse encrypted files in the lower directory. For example, in an eCryptfs directory running  creates a 1GB encrypted file on the underlying filesystem, with the corresponding resource (disk space, data throughput) requirements. If the same file were created on an unencrypted filesystem or a filesystem using block device encryption, it would only take a few kilobytes.

:This should be considered before encrypting large portions of the directory structure, though in most cases the disadvantages will be minor. If you need to use large sparse files, you can work around this issue by putting the sparse files in an unencrypted directory or using block device encryption for them.

## Setup & mounting
Before starting setup, check the eCryptfs documentation. The software is distributed with a very comprehensive set of manual pages.

eCryptfs has been included in Linux since version 2.6.19. Start by loading the  module:

 # modprobe ecryptfs

To actually mount an eCryptfs filesystem, you need to use userspace tools provided by the  package. Unfortunately, due to the poor design of these tools, you must choose between three ways of setting up eCryptfs, each with different tradeoffs:

# Use the high-level #Ubuntu tools, which sets things up automatically, but requires the lower directory to be , and allows only one encrypted filesystem per user.
# Use ecryptfs-simple, which is an easy way to mount eCryptfs filesystems using any lower directory and upper directory.
# #Manual setup, which involves separate steps for loading the passphrase and mounting eCryptfs, but allows complete control over the directories and encryption settings.

## Ubuntu tools
Most of the user-friendly convenience tools installed by the  package assume that a very specific eCryptfs setup is being used, namely the one that is officially used by Ubuntu (where it can be selected as an option during installation). Unfortunately, these choices are not just default options, but are actually hard-coded in the tools. If this setup does not suit your needs, then you cannot use the convenience tools and will have to follow the steps at #Manual setup instead.

The setup used by these tools is as follows:

* each user can have only one encrypted directory that is managed by these tools:
** either full  directory encryption, or
** a single encrypted data directory (by default , but this can be customized).
* the lower directory for each user is always
* the encryption options used are:
** cipher: AES
** key length: 16 bytes (128 bits)
** key management scheme: passphrase
** plaintext passthrough: enabled
* the configuration / control info for the encrypted directory is stored in a bunch of files at
**  text file - contains the path where the upper directory should be mounted (e.g.  or )
**  text file - contains the signature used to identify the mount passphrase in the kernel keyring
**  file - the mount passphrase, encrypted with the login passphrase
** ,  files - if they exist, the  module will (assuming it is loaded) automatically mount/unmount this encrypted directory when the user logs in/out

## Encrypting a data directory
For a full  directory encryption see #Encrypting a home directory

Before the data directory encryption is setup, decide whether it should later be mounted manually or automatically with the user log-in.

To encrypt a single data directory as a user and mount it manually later, run:
 $ ecryptfs-setup-private --nopwcheck --noautomount

and follow the instructions. The option  enables you to choose a passphrase different to the user login passphrase and the option  is self-explanatory. So, if you want to setup the encrypted directory automatically on log-in later, just leave out both options right away.

The script will automatically create the  and  directory structures as described in the box above. It will also ask for two passphrases:

;login passphrase: This is the password you will have to enter each time you want to mount the encrypted directory. If you want auto-mounting on login to work, it has to be the same password you use to login to your user account.

;mount passphrase: This is used to derive the actual file encryption master key. Thus, you should not enter a custom one unless you know what you are doing - instead press Enter to let it auto-generate a secure random one. It will be encrypted using the login passphrase and stored in this encrypted form in . Later it will automatically be decrypted ("unwrapped") again in RAM when needed, so you never have to enter it manually. Make sure this file does not get lost, otherwise you can never access your encrypted folder again! You may want to run  to see the mount passphrase in unencrypted form, write it down on a piece of paper, and keep it in a safe (or similar), so you can use it to recover your encrypted data in case the  file is accidentally lost, corrupted, or you forget the login passphrase.

The mount point ("upper directory") for the encrypted folder will be at  by default. However, you can manually change this right after the setup command has finished running, by doing:

 $ mv ~/Private /path/to/new/folder
 $ echo /path/to/new/folder > ~/.ecryptfs/Private.mnt

To actually use your encrypted folder, you will have to mount it - see #Mounting below.

## Encrypting a home directory
The wrapper script  will set up an encrypted home directory for a user and take care of migrating any existing files they have in their not yet encrypted home directory.

To run it, the user must be logged out and own no processes. The best way to achieve this is to log the user out, log into a console as the root user, and check that  returns no output.  You also need to ensure that you have , , and  installed. Once the prerequisites have been met, run:

 # modprobe ecryptfs
 # ecryptfs-migrate-home -u username

and follow the instructions. After the wrapper script is complete, follow the instructions for auto-mounting - see #Auto-mounting below. To complete this process, it is imperative that the user logs in before the next reboot.

Once everything is working, the unencrypted backup of the user's home directory, which is saved to , should be deleted.

## Mounting
## Manually
Executing the wrapper

 $ ecryptfs-mount-private

and entering the passphrase is all needed to mount the encrypted directory to the upper directory , described in #Ubuntu tools.

Likewise, executing

 $ ecryptfs-umount-private

will unmount it again.

The tools include another script useful in accessing the encrypted  data or home directory. Executing   as root will search the system (or an optional specific path) for the directory, interactively query the passphrase for it, and mount the directory. It can, for example, be used from a live-CD or different system to access the encrypted data in case of a recovery. Note that if booting from an Arch Linux ISO you must first install the . Further, it will only be able to mount  directories created with the Ubuntu tools.

## Auto-mounting
The default way to auto-mount an encrypted directory is via PAM. See  and - for more details - 'PAM MODULE' in:

 /usr/share/doc/ecryptfs-utils/README

For auto-mounting, it is required that the encrypted directory passphrase is identical to the user's log-in password.

Use these steps to set up auto-mounting:

1. Check if ,  and  exist (these are automatically created by ecryptfs-setup-private).

2. Add ecryptfs to the pam-stack exactly as following to allow transparent unwrapping of the passphrase on login:

Open  and after the line containing  (or  if present) add:

 auth default=ignore pam_succeed_if.so service = systemd-user quiet
 auth    required    pam_ecryptfs.so unwrap
Next, above the line containing  (or  if present) insert:
 password    optional    pam_ecryptfs.so
And finally, after the line  add:
 session default=ignore pam_succeed_if.so service = systemd-user quiet
 session    optional    pam_ecryptfs.so unwrap

3. Re-login and check output of mount which should now contain a mountpoint, e.g.:

 /home/username/.Private on /home/username/Private type ecryptfs (...)

for the user's encrypted directory. It should be perfectly readable at .

The latter should be automatically unmounted and made unavailable when the user logs off.

## ecryptfs-simple
Use ecryptfs-simple if you just want to use eCryptfs to mount arbitrary directories the way you can with EncFS. ecryptfs-simple does not require root privileges or entries in , nor is it limited to hard-coded directories such as . The package is available to be installed as  and from Xyne's repos.

As the name implies, usage is simple:

Simple mounting:

 $ ecryptfs-simple /path/to/foo /path/to/bar

Automatic mounting: prompts for options on the first mount of a directory then reloads them next time:

 $ ecryptfs-simple -a /path/to/foo /path/to/bar

Unmounting by source directory:

 $ ecryptfs-simple -u /path/to/foo

Unmounting by mountpoint:

 $ ecryptfs-simple -u /path/to/bar

## Manual setup
The following details instructions to set up eCryptfs encrypted directories manually. This involves two steps. First, the passphrase is processed and loaded into the kernel keyring. Second, the filesystem is actually mounted using the key from the keyring.

There are two ways to add the passphrase to the kernel keyring in the first step. The simpler option is , which uses a single passphrase to encrypt the files. The disadvantage is that you cannot change the passphrase later. It works like this:

 $ ecryptfs-add-passphrase
 Passphrase:
 Inserted auth tok with sig into the user session keyring

You can also pipe a passphrase into . Keep in mind that if you leave your passphrase in a file, it will usually defeat the purpose of using encryption.

As an alternative to a plain passphrase, you can use a "wrapped passphrase", where the files are encrypted using a randomly generated key, which is itself encrypted with your passphrase and stored in a file. In this case, you can change your passphrase by unwrapping the key file with your old passphrase and rewrapping it using your new passphrase.

In the following we [https://stackoverflow.com/a/3980713 prompt for the wrapping passphrase and do a generation similar to the source and then use ecryptfs-wrap-passphrase to wrap it with the given password to :

 $ mkdir ~/.ecryptfs
 $ ( stty -echo; printf "Passphrase: " 1>&2; read PASSWORD; stty echo; echo 1>&2; head -c 48 /dev/random | base64; echo "$PASSWORD"; ) \
   | ecryptfs-wrap-passphrase ~/.ecryptfs/wrapped-passphrase >/dev/null

Do not use a passphrase with more than 64 characters as this will result in an error later when using .

Next, we can enter our passphrase to load the key into the keyring:

 $ ( stty -echo; printf "Passphrase: " 1>&2; read PASSWORD; stty echo; echo $PASSWORD; ) | ecryptfs-insert-wrapped-passphrase-into-keyring ~/.ecryptfs/wrapped-passphrase -
 Inserted auth tok with sig into the user session keyring

In either case, when you successfully add the passphrase to the kernel keyring, you will get a "key signature" like  which you will need in the next step.

There are two different ways of manually mounting eCryptfs, described in the following sections. The first way, using , can be run as a regular user and involves setting up some configuration files. This method does not allow you to change the encryption settings, such as key size. The second way is to use a raw  command, which gives you complete control over all settings, but requires you to either run it as root, or add an entry to  which lets a user mount eCryptfs.

## With configuration files
This method involves running  from the  package, after first loading your passphrase. This binary requires no root privileges to work by default.

First choose a name for your configuration files in  and decide on the lower and upper directories. In this example we use  for the configuration files, put in encrypted data in , and mount the decrypted files at . Create the required directories:

 $ mkdir ~/.secret ~/secret ~/.ecryptfs

Now specify the directories in , using full paths. Its format looks like the one in  without the mount options:

 $ echo "$HOME/.secret $HOME/secret ecryptfs" > ~/.ecryptfs/secret.conf

Write the key signature you got from  or  (see above) into :

 $ echo 78c6f0645fe62da0 > ~/.ecryptfs/secret.sig

If you also want to enable filename encryption, add a second passphrase to the keyring (or reuse the first passphrase) and append its key signature to :

  $ echo 326a6d3e2a5d444a >> ~/.ecryptfs/secret.sig

Finally, mount  on :

 $ mount.ecryptfs_private secret

When you are done, unmount it:

 $ umount.ecryptfs_private secret

## Raw mount command
By running the actual  command manually, you get complete control over the encryption options. The disadvantage is that you need to either run  as root, or add an entry to  for each eCryptfs directory so users can mount them.

First create your private directories. In this example, we use the same ones as the previous section:

 $ mkdir -m 700 ~/.secret
 $ mkdir -m 500 ~/secret

To summarize:

* Actual encrypted data will be stored in the lower  directory
* While mounted, decrypted data will be available in  directory
** While not mounted nothing can be written to this directory
** While mounted it has the same permissions as the lower directory

Now, supposed you have created the wrapped keyphrase above, you need to insert the encryption key once to the root user's keyring:

 # ( stty -echo; printf "Passphrase: " 1>&2; read PASSWORD; stty echo; echo $PASSWORD; ) | ecryptfs-insert-wrapped-passphrase-into-keyring /home/username/.ecryptfs/wrapped-passphrase -
 Inserted auth tok with sig [7c5d3dd8a1b49db0 into the user session keyring

so that the following mount command succeeds:

 # mount -i -t ecryptfs /home/username/.secret /home/username/secret -o ecryptfs_sig=7c5d3dd8a1b49db0,ecryptfs_fnek_sig=7c5d3dd8a1b49db0,ecryptfs_cipher=aes,ecryptfs_key_bytes=32,ecryptfs_unlink_sigs

*  sets the data passphrase key signature.
*  sets the filename passphrase key signature; you can omit this option if you do not want to encrypt filenames.
*  can be 16, 24, or 32 to change the encryption key size.
*  will remove the passphrase(s) from the keyring when you unmount, so you have to add the passphrase(s) back again in order to re-mount the filesystem.
* There are a few other options listed in .

Once you have chosen the right mount options, you can add an entry to  so regular users can mount eCryptfs on these directories. Copy the mount options to a new  entry and add the options  and . The full entry will look similar to (bold entries added):

* The  option is important, because otherwise systemd will error trying to mount the entry directly on boot.
* The  option enables to mount the directory as a user.
** The user mount will default to option . If you want to have at least executable files in your private directory, you can add  to the fstab options.

The setup is now complete and the directory should be mountable by the user.

## Mounting
To mount the encrypted directory as the user, the passphrase must be unwrapped and made available in the user's keyring. Following above section example:

 $ ecryptfs-insert-wrapped-passphrase-into-keyring ~/.ecryptfs/wrapped-passphrase
 Passphrase:
 Inserted auth tok with sig into the user session keyring

Now the directory can be mounted without the mount helper questions:

 $ mount -i ~/secret

and files be placed into the  directory. The above two steps are necessary every time to mount the directory manually.

To unmount it again:

 $ umount ~/secret

To finalize, the preliminary passphrase to wrap the encryption passphrase may be changed:

 $ ecryptfs-rewrap-passphrase ~/.ecryptfs/wrapped-passphrase
 Old wrapping passphrase:
 New wrapping passphrase:
 New wrapping passphrase (again):

The unmounting should also clear the keyring, to check the user's keyring or clear it manually:

 $ keyctl list @u
 $ keyctl clear @u

## Auto-mounting
Different methods can be employed to automount the previously defined user-mount in  on login. As a first general step, follow point (1) and (2) of #Auto-mounting.

Then, if you login via console, a simple way is to specify the user-interactive mount and umount in the user's shell configuration files, for example Bash#Configuration files.

Another method is to automount the eCryptfs directory on user login using pam_mount. To configure this method, add the following lines to :

 mount -i %(VOLUME) "%(before=\"-o\" OPTIONS)"

Please prefer writing manually these lines instead of simply copy/pasting them (especially the lclmount line). Otherwise, you might get some corrupted characters.
Explanation:

* the first line indicates where the user-based configuration file is located (here )
* the second line overwrites the default required mount options which are unnecessary ("nosuid,nodev")
* the last line indicates which mount command to run (eCryptfs needs the  switch).

Then set the volume definition, preferably to :

"noroot" is needed because the encryption key will be added to the user's keyring.

Finally, edit  as described in the pam_mount article.

## Optional step
To avoid needlessly wasting time unwrapping the passphrase, you can create a script that will check pmvarrun to see the number of open sessions:

With the following line added before the eCryptfs unwrap module in your PAM stack:

 auth    [success=ignore default=1    pam_exec.so     quiet /usr/local/bin/doecryptfs
 auth    required                      pam_ecryptfs.so unwrap

The article suggests adding these to , but the changes will need to be added to all other places you login, such as .

## Usage
## Symlinking into the encrypted directory
Besides using your private directory as storage for sensitive files, and private data, you can also use it to protect application data. Firefox for example has an internal password manager, but the browsing history and cache can also be sensitive. Protecting it is easy:

 $ mv ~/.mozilla ~/Private/mozilla
 $ ln -s ~/Private/mozilla ~/.mozilla

## Removal of encryption
There are no special steps involved, if you want to remove your private directory. Make sure it is un-mounted and delete the respective lower directory (e.g. ), along with all the encrypted files. After also removing the related encryption signatures and configuration in , all is gone.

If you were using the #Ubuntu tools to setup a single directory encryption, you can directly follow the steps detailed by:

 $ ecryptfs-setup-private --undo

and follow the instructions.

## Backup
If you want to move a file out of the private directory just move it to the new destination while  is mounted.

With eCryptfs the cryptographic metadata is stored in the header of the files. Setup variants explained in this article separate the directory with encrypted data from the mount point. The unencrypted mount point is fully transparent and available for a backup. Obviously this has to be considered for automated backups, if one has to avoid leaking sensitive unencrypted data into a backup.

You can do backups, or incremental backups, of the encrypted (e.g. ) directory, treating it like any other directory.

Further points to note:

* If you used the Ubuntu tools for #Encrypting a home directory, be aware the location of the lower directory with the encrypted files is outside the regular user's  at .
* It should be ensured to include the eCryptfs setup files (located in  usually) into the regular or a separate backup.
* If you use special filesystem mount options, for example , do extra checks on restore integrity.

## Known issues
## Mounting may fail on a remote host when connecting via Mosh
This is a known issue of Mosh server, which does not keep the eCryptfs  directory mounted.
