# Dm-crypt/Device encryption

This section covers how to manually utilize dm-crypt from the command line to encrypt a system.

## Preparation
Before using , always make sure the  kernel module is loaded.

## Cryptsetup usage
 is the command line tool to interface with dm-crypt for creating, accessing and managing encrypted devices. The tool was later expanded to support different encryption types that rely on the Linux kernel device-mapper and the cryptographic modules. The most notable expansion was for the Linux Unified Key Setup (LUKS) extension, which stores all of the needed setup information for dm-crypt on the disk itself and abstracts partition and key management in an attempt to improve ease of use. Devices accessed via the device-mapper are called block devices. For further information see Data-at-rest encryption#Block device encryption.

The tool is used as follows:

 # cryptsetup action options device name

It has compiled-in defaults for the options and the encryption mode, which will be used if no others are specified on the command line. Have a look at

 $ cryptsetup --help

which lists options, actions and the default parameters for the encryption modes in that order. A full list of options can be found on the man page.
Since different parameters are required or optional, depending on encryption mode and action, the following sections point out differences further. Block device encryption is fast, but speed matters a lot too. Since changing an encryption cipher of a block device after setup is difficult, it is important to check dm-crypt performance for the individual parameters in advance:

 $ cryptsetup benchmark

can give guidance on deciding for an algorithm and key-size prior to installation. If certain AES ciphers excel with a considerable higher throughput, these are probably the ones with hardware support in the CPU.

## Cryptsetup passphrases and keys
An encrypted block device is protected by a key. A key is either:

* a passphrase: see Security#Passwords.
* a keyfile, see #Keyfiles.

Both key types have default maximum sizes: passphrases can be up to 512 characters and keyfiles up to 8192 KiB.

An important distinction of LUKS to note at this point is that the key is used to unlock the master-key of a LUKS-encrypted device and can be changed with root access. Other encryption modes do not support changing the key after setup, because they do not employ a master-key for the encryption. See Data-at-rest encryption#Block device encryption for details.

## Encryption options
Cryptsetup supports different encryption operating modes to use with dm-crypt:

*  for using the default LUKS format version (LUKS1 with   /mnt/stacked.txt

We close the stack to check access works

 # cryptsetup close plain2
 # cryptsetup close plain1

First, let us try to open the file system directly:

 # cryptsetup --type plain --cipher=serpent-xts-plain64 --hash=sha256 --key-size=256 --offset=10 open /dev/sdxY plain2

Why that did not work? Because the "plain2" starting block () is still encrypted with the cipher from "plain1". It can only be accessed via the stacked mapper. The error is arbitrary though, trying a wrong passphrase or wrong options will yield the same. For dm-crypt plain mode, the  action will not error out itself.

Trying again in correct order:

 # cryptsetup close plain2    # dysfunctional mapper from previous try

dm-crypt will handle stacked encryption with some mixed modes too. For example LUKS mode could be stacked on the "plain1" mapper. Its header would then be encrypted inside "plain1" when that is closed.

Available for plain mode only is the option . With it a single device can be segmented into different non-overlapping mappers. We do that in the next example, using a loopaes compatible cipher mode for "plain2" this time:

As the device tree shows both reside on the same level, i.e. are not stacked and "plain2" can be opened individually.

## Cryptsetup actions specific for LUKS
## Key management
It is possible to define additional keys for the LUKS partition. This enables the user to create access keys for safe backup storage  In so-called key escrow, one key is used for daily usage, another kept in escrow to gain access to the partition in case the daily passphrase is forgotten or a keyfile is lost/damaged.  A different key-slot could also be used to grant access to a partition to a user by issuing a second key and later revoking it again.

Once an encrypted partition has been created, the initial keyslot 0 is created (if no other was specified manually). Additional keyslots are numbered from 1 to 7. Which keyslots are used can be seen by issuing

 # cryptsetup luksDump /dev/device

Where  is the block device containing the LUKS header. This and all the following commands in this section work on header backup files as well.

## Adding LUKS keys
Adding new keyslots is accomplished with the  action. For safety it will always, even for already unlocked devices, ask for a valid existing key (a passphrase for any existing slot) before a new one may be entered:

If  is given, cryptsetup will add a new keyslot for . Otherwise it prompts for a new passphrase. To authorize the action with an existing keyfile, the  or  option followed by the "old"  will try to unlock all available keyfile keyslots:

 # cryptsetup luksAddKey /dev/device -d /path/to/keyfile

If it is intended to use multiple keys and change or revoke them, the  or  option may be used to specify the slot:

To show an associated action in this example, we decide to change the key right away:

before continuing to remove it.

## Removing LUKS keys
There are three different actions to remove keys from the header:

*  removes a key by specifying its passphrase/key-file. See .
*  removes a key by specifying its slot (needs another valid key). Obviously, this is extremely useful if you have forgotten a passphrase, lost a key-file, or have no access to it. See .
*  removes all active keys. See .

For above warning it is good to know the key we want to keep is valid. An easy check is to unlock the device with the  option, which will specify which slot it occupies:

Now we can remove the key added in the previous subsection using its passphrase:

If we had used the same passphrase for two keyslots, the first slot would be wiped now. Only executing it again would remove the second one.

Alternatively, we can specify the key slot:

Note that in both cases, no confirmation was required.

To re-iterate the warning above: If the same passphrase had been used for key slots 1 and 6, both would be gone now.

## Backup and restore
If the header of a LUKS encrypted partition gets destroyed, you will not be able to decrypt your data. It is just as much of a dilemma as forgetting the passphrase or damaging a key-file used to unlock the partition. Damage may occur by your own fault while re-partitioning the disk later or by third-party programs misinterpreting the partition table. Therefore, having a backup of the header and storing it on another disk might be a good idea.

## Backup using cryptsetup
Cryptsetup's  action stores a binary backup of the LUKS header and keyslot area:

 # cryptsetup luksHeaderBackup /dev/device --header-backup-file /mnt/backup/file.img

where  is the partition containing the LUKS volume.

You can also back up the plain text header into tmpfs and encrypt it with e.g. GPG before writing it to persistent storage:

 # mount --mkdir -t tmpfs -o noswap tmpfs /root/tmp
 # cryptsetup luksHeaderBackup /dev/device --header-backup-file /root/tmp/file.img
 # gpg --recipient User_ID --encrypt /root/tmp/file.img
 # cp /root/tmp/file.img.gpg /mnt/backup/
 # umount /root/tmp

## Restore using cryptsetup
In order to evade restoring a wrong header, you can ensure it does work by using it as a remote  first:

 # mount /dev/mapper/test /mnt/test && ls /mnt/test
 # umount /mnt/test
 # cryptsetup close test

Now that the check succeeded, the restore may be performed:

 # cryptsetup luksHeaderRestore /dev/device --header-backup-file ./mnt/backup/file.img

Now that all the keyslot areas are overwritten; only active keyslots from the backup file are available after issuing the command.

## Manual backup and restore
The header always resides at the beginning of the device and a backup can be performed without access to cryptsetup as well. First you have to find out the payload offset of the crypted partition:

Second check the sector size of the drive

Now that you know the values, you can backup the header with a simple dd command:

 # dd if=/dev/device of=/path/to/file.img bs=512 count=4040

and store it safely.

A restore can then be performed using the same values as when backing up:

 # dd if=./file.img of=/dev/device bs=512 count=4040

## Re-encrypting devices
The cryptsetup  action allows to re-encrypt LUKS devices. For LUKS2 devices, a re-encryption may be performed online, multiple parallel re-encryption jobs are supported and it is resilient to system failures. A re-encryption of LUKS1 devices can only be performed offline (unmounted), with a single process and less resilience.

See  for the modes of operation and options.

It is possible to change the #Encryption options for LUKS mode. It can also be used to convert an existing unencrypted file system to a LUKS encrypted one or permanently remove LUKS encryption from a device (using ; see Removing system encryption). A re-encryption is also feasible for a detached LUKS header, but mind the warning for the  option. A re-encryption of  modes other than LUKS (e.g. plain-mode) is not supported.

One application of re-encryption may be to secure the data again after a passphrase or keyfile has been compromised and one cannot be certain that no copy of the LUKS header has been obtained. For example, if only a passphrase has been shoulder-surfed but no physical/logical access to the device happened, it would be enough to change the respective passphrase/key only (#Key management).

The following shows an example to encrypt an unencrypted file system partition and a re-encryption of an existing LUKS device.

## Encrypt an existing unencrypted file system
A LUKS encryption header is always stored at the beginning of the device. Since an existing file system will usually be allocated all partition sectors, the first step is to shrink it to make space for the LUKS header.

The default LUKS2 header requires 16 MiB. If the current file system occupies all the available space, we will have to shrink it at least that much. To shrink an existing  file system on  to its current possible minimum:

 # umount /mnt

Now we encrypt it, using the default cipher we do not have to specify it explicitly:

After it finished, the whole  partition is encrypted, not only the space the file system was shrunk to. As a final step we extend the original  file system to occupy all available space again, on the now encrypted partition:

 # mount /dev/mapper/recrypt /mnt

The file system is now ready to use. You may want to add it to your crypttab.

## Re-encrypting an existing LUKS partition
In this example an existing LUKS device is re-encrypted.

In order to re-encrypt a device with its current encryption options, they do not need to be specified:
 # cryptsetup reencrypt /dev/sdxY

Existing keys are retained when re-encrypting a device with a different cipher and/or hash.

Another use case is to re-encrypt LUKS devices which have non-current encryption options. In this case you have to specify the desired new options. Note a LUKS2 header allows individual per-keyslot encryption options, hence a re-encryption will apply to the data segment only.

The ability to change the LUKS header may also be limited by its size. For example, if the device was initially LUKS1 encrypted using a CBC mode cipher and 128 bit key-size, the LUKS header will be half the size of above mentioned  sectors:

To upgrade the encryption options of such a device, consider to convert the header to LUKS2 prior to re-encryption. If the conversion fails due to inadequate header size, you may have to re-encrypt with the  option to make further space for the larger LUKS header before re-encrypting with the desired new encryption. Keep in mind that both methods carry inherent risks: for the header during conversion, and the filesystem data if needed extra header sectors are in use.

## Conversion from LUKS1 to LUKS2 and back
The cryptsetup tool has a  action for LUKS1 and LUKS2 header format conversions. It is advised to create a header backup prior to a conversion. The argument  is required.

Migration from LUKS1 to LUKS2:

 # cryptsetup convert --type luks2 /dev/sdxY

Rollback to LUKS1 (for example, to boot from GRUB with encrypted /boot):

 # cryptsetup convert --type luks1 /dev/sdxY

## Resizing encrypted devices
If a storage device encrypted with dm-crypt is being cloned (with a tool like dd) to another larger device, or  the partition is being enlarged or shrinked, the underlying file system has to be resized. For devices based on LUKS, this is the only necessary step, as LUKS does not store any size information about the partition, but uses the whole size by default, i.e., when no  parameter is passed. To this end, follow necessary steps to resize a partition as usual. An example for the encrypted LUKS device  containing an ext4 filesystem that needs to be enlarged follows:

Firstly, resize the underlying partition with Parted or fdisk. When shrinking a partition, this needs to be done last. Now, open your device and resize the filesystem:

 # cryptsetup luksOpen /dev/sdX2 sdX2
 # e2fsck /dev/mapper/sdX2
 # resize2fs /dev/mapper/sdX2  # Uses all available space on the enlarged LUKS partition

After mounting the mapped enlarged LUKS device, it can be used as before.

 # mount /dev/mapper/sdX2 /mnt/enlarged_sdX2

## LVM on LUKS
See Resizing LVM on LUKS.

## Loopback file system
Assume that an encrypted loopback file system is stored in a file , looped to , mapped to  and mounted on , as in the example at dm-crypt/Encrypting a non-root file system#File container.

If the container file is currently mapped and/or mounted, unmount and/or close it:

 # umount /mnt/secret
 # cryptsetup close secret
 # losetup -d /dev/loop0

Next, expand the container file with the size of the data you want to add. In this example, the file will be expanded by 1 MiB × 1024, which is 1 GiB.

 # dd if=/dev/urandom of=/bigsecret bs=1M count=1024 iflag=fullblock oflag=append conv=notrunc status=progress

Now map the container to the loop device:

 # losetup /dev/loop0 /bigsecret
 # cryptsetup open /dev/loop0 secret

After this, resize the encrypted part of the container to the new maximum size of the container file:

 # cryptsetup resize secret

Finally, perform a file system check and, if it is ok, resize it (example for ext2/3/4):

 # e2fsck -f /dev/mapper/secret
 # resize2fs /dev/mapper/secret

You can now mount the container again:

 # mount /dev/mapper/secret /mnt/secret

## Integrity protected device
If the device was formatted with integrity support (e.g., ) and the backing block device is shrunk, it cannot be opened with this error: .

To fix this issue without wiping the device again, it can be formatted with the previous master key (keeping the per-sector tags valid).

 # cryptsetup luksDump /dev/sdX2 --dump-master-key --master-key-file=/tmp/masterkey-in-tmpfs.key
 # cryptsetup luksFormat /dev/sdX2 --type luks2 --integrity hmac-sha256 --master-key-file=/tmp/masterkey-in-tmpfs.key --integrity-no-wipe
 # rm /tmp/masterkey-in-tmpfs.key

## Keyfiles
What is a keyfile?

A keyfile is a file whose data is used as the passphrase to unlock an encrypted volume.
That means if such a file is lost or changed, decrypting the volume may no longer be possible.

Why use a keyfile?

There are many kinds of keyfiles. Each type of keyfile used has benefits and disadvantages summarized below:

## Types of keyfiles
## Passphrase
This is a keyfile containing a simple passphrase. The benefit of this type of keyfile is that if the file is lost, the data it contained is known and hopefully easily remembered by the owner of the encrypted volume. Nevertheless, this does not add any security over entering a passphrase during the initial system start.

Example:

## Random characters
This is a keyfile containing a block of random characters. The benefit of this type of keyfile is that it is much more resistant to dictionary attacks than a simple passphrase. An additional strength of keyfiles which can be utilized in this situation is the length of data used. Since this is not a string meant to be memorized by a person for entry, it is trivial to create files containing thousands of random characters as the key. The disadvantage is that if this file is lost or changed, it will most likely not be possible to access the encrypted volume without a backup passphrase.

Random character keyfiles may use any character set, but sticking to a portable set of ASCII letters and numbers can make things easier in situations where keyboard layout or Unicode support is unreliable, like typing an emergency password at the startup LUKS unlock stage, or measuring keyfiles with old Unicode-naive POSIX utilities. You can generate such a string like this:

 $ tr -dc '[:alnum:' </dev/urandom | head -c64

Example:

Alternatively, a random (UTF-8) Unicode character keyfile could look like this:

Example: {{ic|W¬hjT}­�DÐ§íŽ�uLÝæ�Ýœ�§aþ�óx±)Ñ)l­éeð��ú=èe}}

## Binary
This is a binary file that has been defined as a keyfile. When identifying files as candidates for a keyfile, it is recommended to choose files that are relatively static such as photos, music, video clips. The benefit of these files is that they serve a dual function which can make them harder to identify as keyfiles. Instead of having a text file with a large amount of random text, the keyfile would look like a regular image file or music clip to the casual observer. The disadvantage is that if this file is lost or changed, it will most likely not be possible to access the encrypted volume without a backup passphrase. Additionally, there is a theoretical loss of randomness when compared to a randomly generated text file. This is due to the fact that images, videos and music have some intrinsic relationship between neighboring bits of data that does not exist for a random text file. However this is controversial and has never been exploited publicly.

Example: images, text, video, ...

## Creating a keyfile with random characters
## Storing the keyfile on a file system
A keyfile can be of arbitrary content and size.

Here dd is used to generate a keyfile of 2048 random bytes, storing it in the file :

 # dd bs=512 count=4 if=/dev/random iflag=fullblock | install -m 0600 /dev/stdin /etc/cryptsetup-keys.d/mykeyfile.key

If you are planning to store the keyfile on an external device, you can also simply change the output file to the corresponding directory:

 # dd bs=512 count=4 if=/dev/random of=/run/media/user/usbstick/mykeyfile.key iflag=fullblock

## Securely overwriting stored keyfiles
If you stored your temporary keyfile on a physical storage device, and want to delete it, remember to not just remove the keyfile later on, but use something like

 # shred --remove --zero mykeyfile

to securely overwrite it. For overaged file systems like FAT or ext2 this will suffice while in the case of journaling file systems, flash memory hardware and other cases it is highly recommended to wipe the entire device.

## Storing the keyfile in tmpfs (with swapping disabled)
Alternatively, you can mount a tmpfs with swapping disabled for storing the keyfile temporarily:

 # mount --mkdir -t tmpfs -o noswap tmpfs /root/mytmpfs
 # cd /root/mytmpfs

The advantage is that it resides in RAM and not on a physical disk, therefore it can not be recovered after unmounting the tmpfs. After copying the keyfile to another secure and persistent file system, unmount the tmpfs again with:

 # umount /root/mytmpfs

## Configuring LUKS to make use of the keyfile
Add a keyslot for the keyfile to the LUKS header:

## Manually unlocking a partition using a keyfile
Use the  option when opening the LUKS device:

 # cryptsetup open /dev/sda2 dm_name --key-file /etc/cryptsetup-keys.d/mykeyfile.key

## Unlocking the root partition at boot
This is simply a matter of configuring mkinitcpio to include the necessary modules or files and configuring the cryptkey kernel parameter to know where to find the keyfile.

Two cases are covered below:

# Using a keyfile stored on an external medium (e.g. a USB stick)
# Using a keyfile embedded in the initramfs

## With a keyfile stored on an external media
## Configuring mkinitcpio
You have to add the kernel module for the drive's file system to the MODULES array in . For example, add  if the file system is Ext4 or  in case it is FAT:

 MODULES=(vfat)

If there are messages about bad superblock and bad codepage at boot, then you need an extra codepage module to be loaded. For instance, you may need  module for  codepage.

Regenerate the initramfs.

## Configuring the kernel parameters
* For a busybox-based initramfs using the encrypt hook, see dm-crypt/System configuration#cryptkey.
* For a systemd based initramfs using the sd-encrypt hook, see dm-crypt/System configuration#rd.luks.key.

## With a keyfile embedded in the initramfs
This method allows to use a specially named keyfile that will be embedded in the initramfs and picked up by the  hook to unlock the root file system () automatically. It may be useful to apply when using the GRUB early cryptodisk feature, in order to avoid entering two passphrases during boot.

Generate the keyfile, give it suitable permissions and add it as a LUKS key:

 # dd bs=512 count=4 if=/dev/random iflag=fullblock | install -m 0600 /dev/stdin /etc/cryptsetup-keys.d/root.key
 # cryptsetup luksAddKey /dev/sdX# /etc/cryptsetup-keys.d/root.key

Include the key in mkinitcpio's FILES array:

Regenerate the initramfs.

For the  hook, the keyfile is specified with the  kernel parameter: in the case of initramfs, the syntax is . The default is  and  can be omitted if initramfs contains a valid key with this path. See dm-crypt/System configuration#cryptkey.

For the above example, set the following kernel parameter when using busybox-based initramfs with the  hook:

 cryptkey=rootfs:/etc/cryptsetup-keys.d/root.key

If using the  hook instead, the keyfile is specified with the  kernel parameter: in the case of initramfs, the syntax is . The default is  (where  is the dm_name used for decryption in #Encrypting devices with cryptsetup) and  can be omitted if initramfs contains a valid key with this path. See dm-crypt/System configuration#rd.luks.key.

On the next reboot you should only have to enter your container decryption passphrase once.

([https://www.pavelkogan.com/2014/05/23/luks-full-disk-encryption/#bonus-login-once source)
