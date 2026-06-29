# VeraCrypt

VeraCrypt is fork of TrueCrypt, a free open source on-the-fly encryption (OTFE) program. Some of its features are:
* Virtual encrypted disks within files that can be mounted as real disks.
* Encryption of an entire hard disk partition or a storage device/medium.
* All encryption algorithms use the LRW mode of operation, which is more secure than CBC mode with predictable initialization vectors for storage encryption.
* "Hidden volumes" within a normal "outer" encrypted volume. A hidden volume can not be distinguished from random data without access to a passphrase and/or keyfile.

For more details on how TrueCrypt compares to other disk encryption solution, see Data-at-rest encryption#Comparison table.

## Installation
Install the  package.

## Accessing a TrueCrypt or VeraCrypt container using cryptsetup
 supports opening VeraCrypt and TrueCrypt containers natively, without the need of the  package. Use the following command as a guideline.
 $ cryptsetup --type tcrypt open container-to-mount container-name

If using a custom Personal Iteration Multiplier (PIM), use the  option to be promoted for the PIM.

Replace  with the device file under  or the path to the file you wish to open. Upon successful opening, the plaintext device will appear as , which you can  like any normal device.

If you are using key files, supply them using the  option, to open a hidden volume, supply the  option and for a partition or whole drive that is encrypted in system mode use the  option.

See  for more details and all supported options.

## Automounting using /etc/crypttab
Since version 206, systemd supports (auto)mounting TrueCrypt containers at boot or runtime using .

The following example setup will mount  in system encryption mode as soon as  is accessed using systemd's automounting logic. The passphrase to open the volume is given in . Note that the device file given in  needs to be the one from  and not, for example, from  for automounting logic to kick in. Other than that you can still reliably identify the encrypted volume itself inside of  using device file names from .

For a standard truecrypt volume, use tcrypt instead of tcrypt-system. And for a hidden one, use tcrypt-hidden. For a veracrypt volume, use tcrypt-veracrypt alongside tcrypt.

Instead of auto, you can put directly your filesystem, and put usual mount options. It is useful with NTFS for mounting as a normal user.

See  for more details and options supported.

## Encrypting a file as a virtual volume
The following instructions will create a file that will act as a virtual filesystem, allowing you to mount it and store files within the encrypted file. This is a convenient way to store sensitive information, such as financial data or passwords, in a single file that can be accessed from Linux, Windows, or Macs.

To create a new truecrypt file interactively, type the following in a terminal:
 $ veracrypt -t -c

Follow the instructions, choosing the default values unless you know what you are doing:

 Volume type:
  1) Normal
  2) Hidden
 Select 1

 Enter file or device path for new volume: /home/user/EncryptedFile.tc

 Enter volume size (bytes - size/sizeK/sizeM/sizeG): 32M

 Encryption algorithm:
  1) AES
  2) Blowfish
  3) CAST5
  4) Serpent
  5) Triple DES
  6) Twofish
  7) AES-Twofish
  8) AES-Twofish-Serpent
  9) Serpent-AES
 10) Serpent-Twofish-AES
 11) Twofish-Serpent
 Select [1: 1

 Hash algorithm:
  1) RIPEMD-160
  2) SHA-1
  3) Whirlpool
 Select 1

Filesystem:
 1) None
 2) FAT
 3) Linux Ext2
 4) Linux Ext3
 5) Linux Ext4
Select [2:

 Enter password for new volume '/home/user/EncryptedFile.tc': *****************************
 Re-enter password: *****************************

 Enter keyfile path Please type at least 320 randomly chosen characters and then press Enter:

 Done: 32.00 MB  Speed: 10.76 MB/s  Left: 0:00:00
 Volume created.

You can now mount the new encrypted file to a previously-created directory:
 $ veracrypt -t /home/user/EncryptedFile.tc /home/user/EncryptedFileFolder

Once mounted, you can copy or create new files within the encrypted directory as if it was any normal directory. When you are you ready to re-encrypt the contents and unmount the directory, run:
 $ veracrypt -t -d

Again, this will require administrator privileges through the use of sudo. After running it check if the files that are to be encrypted are indeed no longer in the directory. (might want to try unimportant data first) If they are still there, note that rm does not make the data unrecoverable.

For more information about truecrypt in general, run:
 $ man veracrypt

Several options can be passed at the command line, making automated access and creation a simple task.  The man page is highly recommended reading.

## Encrypting a physical volume
If you want to use a keyfile, create one with this command:
 veracrypt --create-keyfile /etc/disk.key
By default both passphrase and key will be needed to unlock the volume.

Create a new volume in the device :
 # veracrypt --volume-type=normal -c /dev/sda1

Map the volume to :
 # veracrypt -N 1 /dev/sda1

If this command does not for you try this to map the volume:
 # veracrypt --filesystem=none --slot=1 /dev/sda1

Simply format the disk like you normally would choosing your favourite file system, except use the path . E.g. for ext4 use:
 # mkfs.ext4 /dev/mapper/truecrypt1

Mount the volume:
 # mount /dev/mapper/truecrypt1 /media/disk

Map and mount a volume:
 # veracrypt /dev/sda1 /media/disk

Unmount and unmap a volume:
 # veracrypt -u /dev/sda1

## Creating a hidden volume
First, create a normal outer volume as described in #Encrypting a physical volume.

Map the outer volume to :
 # veracrypt -N 1 /dev/sda1

Create a hidden truecrypt volume in the free space of the outer volume:
  # veracrypt --type hidden -c /dev/sda1
You need to use another passphrase and/or keyfile here than the one you used for the outer volume.

Unmap the outer truecrypt volume and map the hidden one:
 # veracrypt -d /dev/sda1
 # veracrypt -N 1 /dev/sda1
Just use the passphrase  you chose for the hidden volume and TrueCrypt will automatically choose it before the outer.

Create a file system on it (if you have not already) and mount it:
 # mkfs.ext4 /dev/mapper/truecrypt1
 # mount /dev/mapper/truecrypt1 /media/disk

Map and mount the outer volume with the hidden write-protected:
 veracrypt -P /dev/sda1 /media/disk

## Mount a special filesystem
In the following example I want to mount a ntfs-volume, but TrueCrypt does not use ntfs-3g by default (so there is no write access; checked in version 6.1).
The following command works for me:
 veracrypt --filesystem=ntfs-3g --mount /file/you/want/to/mount
You may also want to mount ntfs volume without execute flag on all files
 veracrypt --filesystem=ntfs-3g --fs-options=users,uid=$(id -u),gid=$(id -g),fmask=0113,dmask=0002

## Mount volumes via fstab
First of all, we need to write a script which will handle the way mounting via fstab is done. Place the following in :
{{bc|
#!/bin/sh
DEV="$1"
MNTPT="$2"
OPTIONS=""
TCOPTIONS=""

shift 3
IFS=','
for arg in $*; do
    case "$arg" in
        system)                   TCOPTIONS=(${TCOPTIONS[*} --m=system);;
        fs*)                      TCOPTIONS=(${TCOPTIONS--filesystem=${arg#*=});;
        keyfiles*)                TCOPTIONS=(${TCOPTIONS[*} --keyfiles=${arg#*=});;
        password*)                TCOPTIONS=(${TCOPTIONS--password=${arg#*=}) && echo "password triggered" ;;
        protect-hidden*)          TCOPTIONS=(${TCOPTIONS[*} --protect-hidden=${arg#*=});;
        *)                        OPTIONS="${OPTIONS}${arg},";;

    esac
done

/bin/veracrypt --text --non-interactive ${DEV} ${MNTPT} ${TCOPTIONS--fs-options="${OPTIONS%,*}"
}}
Also do not forget to make the file executable.

Finally, add the device to fstab somewhat like this:

 /dev/sdb3 /mnt truecrypt fs=vfat,defaults 0 0

## Mount volumes as a normal user
TrueCrypt needs root privileges to work: this procedure will allow normal users to use it, also giving writing permissions to mounted volumes.

Both methods below require Sudo.  Make sure it is configured before proceeding.

## Method 1: add a veracrypt group
Create a new group called veracrypt and give it the necessary permissions. Any users that belongs to that group, will be able to use TrueCrypt.
 # groupadd veracrypt

Edit the sudo configuration:
 # visudo

Append the following lines at the bottom of the sudo configuration file:
 # Users in the veracrypt group are allowed to run VeraCrypt as root.
 %veracrypt ALL=(root) NOPASSWD:/usr/bin/veracrypt

You can now add your users to the veracrypt group:
 # gpasswd -M first_user,second_user,etc veracrypt

After that, you can mount your device by

 # veracrypt --mount /path/to/device /path/to/mountpoint

Default mountpoint is . Normally, it is not necessary to explicitly specify the filesystem of your device using the  flag.

It is definitely reasonable to give veracrypt some permission masks. Otherwise, every file on your mounted device will be executable. So instead of the above, you can use

 # veracrypt --fs-options=users,uid=$(id -u),gid=$(id -g),fmask=0113,dmask=0002 --mount /PATH/TO/DEVICE /PATH/TO/MOUNTPOINT

and add this line to your bash configuration file,  as an alias:

 alias tc1='veracrypt --fs-options=users,uid=$(id -u),gid=$(id -g),fmask=0113,dmask=0002 --mount /path/to/device"" /path/to/mountpoint'

To mount this specific device, use

 # tc1

as a normal user.

## Method 2: sudo simplified
Simply enable desired user to run truecrypt without a password:
 # visudo

Append the following:
 USERNAME ALL = (root) NOPASSWD:/usr/bin/veracrypt

alternatively, if you make use of the wheel group:
 %wheel ALL = (root) NOPASSWD:/usr/bin/veracrypt

If you have any difficulties with permissions as a normal user, just add the  flag to the truecrypt mount command, for example:
 $ veracrypt -u /home/user/EncryptedFile.tc /home/user/EncryptedFileFolder

## Automatic mount on login
Simply add:
{{bc|
$ veracrypt /home/user/Encrypted File.tc /home/user/Encrypted File Folder  Preferences > Mount Options'').

## FAT
Similarly, FAT32 volumes created using Windows may use Unicode rather than ISO 8859-1. In order to use UTF-8 globally, set the mount option:
 iocharset=utf8

Alternatively, when mounting volumes locally use:
 --fs-options=iocharset=utf8

Since linux-4.14.4, UTF8 charset is enabled by default. So in order to mount volumes using ISO 8859-1 encoding, you need to use , see .

## Unmount error (device mapper)
If you always get a message "device-mapper: remove ioctl failed: Device or resource busy" when attempting to dismount your truecrypt volume, the solution is to goto: Setting > Preferences > System Integration > Kernel Service and check the box
 Do not use kernel cryptographic services

## Mount error (device mapper, truecrypt partition)
When attempting to mount your truecrypt volume, a message like this one may appear:

 Error: device-mapper: create ioctl failed: Device or resource busy
 Command failed
If so, run:
 # cryptsetup remove /dev/mapper/truecrypt1

## Failed to set up a loop device
If you get a message "Failed to set up a loop device" when trying to create/mount a TrueCrypt volume, it may be because you updated your kernel recently without rebooting.
Rebooting should fix this error.

Otherwise, check if loop has been loaded as kernel module:

 $ lsmod | grep loop

If not listed, retry the TrueCrypt command after . Should it work, consider to add loop to the modules in :

 # tee /etc/modules-load.d/truecrypt.conf  /etc/modprobe.d/eightloop.conf

Change  to the number of devices you need.

## System partition passwords need en_US keymap
If you are using Xorg (which you most likely are, should you not know what that is), use the following command to use US keymap until restart:

 # setxkbmap us

## Permission denied on NTFS volume
If you cannot modify the filesystem, although permissions seem to be correct, this can be a result of not having NTFS-3G installed, see NTFS.

## Corrupted standard volume file system
In case you cannot access your VeraCrypt volume or container anymore, install . See more information on [https://www.cgsecurity.org/wiki/Recover_a_TrueCrypt_Volume CGSecurity page.

 $ ./truecrypt -t --filesystem=none /data/data_for_testdisk/truecrypt.dd
 Enter password for /data/data_for_testdisk/truecrypt.dd:
 Enter keyfile Protect hidden volume? (y=Yes/n=No) [No:
 Enter system administrator password:
 $ mount
 ...
 truecrypt on /tmp/.truecrypt_aux_mnt1 type fuse.truecrypt (rw,nosuid,nodev,allow_other)
 # testdisk /tmp/.truecrypt_aux_mnt1/volume
