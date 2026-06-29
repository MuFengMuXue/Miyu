# Self-encrypting drives

Hardware-based full-disk encryption (FDE) is now available from many hard disk (HDD) vendors, becoming increasingly common especially for solid state drives. The term "self-encrypting drive" (SED) is now common when referring to HDDs or SSDs with built-in full-disk encryption. OPAL is a set of specifications for self-encrypting drives developed by the Trusted Computing Group.

## Overview
Many self-encrypting drives available today implement the OPAL, Ruby or Enterprise standards developed by the Trusted Computing Group (TCG). Other standards such as Opalite and Pyrite only offer a subset of the functionalities offered by OPAL, and might not even offer any actual encryption of data at rest The hardware manufactured according to the standards is [http://www.wavesys.com/self-encrypting-drive-compatibility-list labeled accordingly.

Unlocking of the drive can be done during operating system runtime using software utilities, in a pre-boot authentication environment, or with a #BIOS based ATA-password on power up.

Refer to the #Advantages and #Disadvantages sections to better understand and decide if hardware-based full-disk encryption is what you want.

## Key management technical implementation
Key management takes place within the disk controller and encryption keys are usually 128 or 256 bit Advanced Encryption Standard (AES).

Self-encrypting drives adhering to the TCG OPAL 2.0 standard specification (almost all modern self-encrypting drives) implement key management via an authentication key, and a 2nd-level data encryption key. The data encryption key is the key against which data on the drive is actually encrypted. The authentication key is the user-facing 1st-level passphrase which decrypts the data encryption key (which in turn decrypts the data). This approach has specific advantages:

* Allows the user to change the passphrase without losing the existing encrypted data on the disk
** This improves security, as it is fast and easy to respond to security threats and revoke a compromised passphrase
* Facilitates near-instant and cryptographically secure full disk erasure.

For those who are familiar, this concept is similar to the LUKS key management layer often used in a dm-crypt deployment. Using LUKS, the user can have multiple different keys (passphrases or keyfiles) to decrypt the master-key, which in turn decrypts the underlying data. This approach allows the user to change or revoke these keys as required without needing to re-encrypt the data, as the master 2nd-level encryption key is unchanged (itself being re-encrypted by the new passphrase).

In fact, in drives featuring full-disk encryption, data is always encrypted with the data encryption key when stored to disk, even if there is no password set (e.g. a new drive). Manufacturers do this to make it easier for users who do not wish to enable the security features of the self-encrypting drive. These self-encrypting drives can be thought of as having a zero-length password by default that always transparently encrypts the data  (similar to how passwordless SSH keys can provide somewhat secure access without user intervention).

If a user wishes to "enable" encryption at a later stage, they are able to configure an authentication key (such as a passphrase) which encrypts the existing data encryption key. The user will then be prompted for their passphrase when decrypting the data encryption key in the future. Crucially, because the existing data encryption key is not regenerated, setting a passphrase allows for the drive to be locked while preserving existing encrypted data on the disk, avoiding the need for the drive to be re-encrypted. On the flip-side, there is no way to re-encrypt the data itself, other than a secure full disk erasure.

## Advantages
* Easier to setup (compared to software-based encryption)
* Notably transparent to the user, except for initial bootup authentication
* Data-at-Rest protection
* Increased performance (CPU is freed up from calculations to encrypt and decrypt)
* The main CPU and RAM are eliminated as possible attack targets
* Optimally fast and #Secure disk erasure (sanitation) (regardless of disk size)
* Protection from alternative boot methods due to the possibility to encrypt the MBR, rendering the drive inaccessible before pre-boot authentication

## Disadvantages
* The configuration of suspend and hibernate modes is difficult and may be impossible, depending on the systems' EFI implementation.

* A re-encryption of the data is not possible without a secure disk erasure.

* Exploitations
:* Constant-power exploits
::Typical self-encrypting drives, once unlocked, will remain unlocked as long as power is provided. This vulnerability can be exploited by means of altering the environment external to the drive, without cutting power, in effect keeping the drive in an unlocked state. For example, it has been shown (by researchers at University of Erlangen-Nuremberg) that it is possible to reboot the computer into an attacker-controlled operating system without cutting power to the drive. The researchers have also demonstrated moving the drive to another computer without cutting power.:* Key-in-memory exploits
::When the system is powered down into S3 ("sleep") mode, the drive is powered down, but the drive keeps access to the encryption key in its internal memory (NVRAM) to allow for a resume ("wake"). This is necessary because for system booted with an arbitrary operating system there is no standard mechanism to prompt the user to re-enter the pre-boot decryption passphrase again. An attacker (with physical access to the drive) can leverage this to access the drive. Taking together known exploits the researchers summarize "we were able to break hardware-based full-disk encryption on eleven [of twelve of those systems provided they were running or in standby mode".Note, however, S3 ("sleep") is not currently supported by sedutil (the current available toolset for managing a TCG OPAL 2.0 self-encrypting drives via Linux)
:* Compromised firmware
::The firmware of the drive may be compromised (backdoor) and data sent to it thus potentially compromised (decryptable by the malicious third party in question, provided access to physical drive is achievable). A study demonstrated methods for compromising device firmware, as well as applying invalid passwords to access data on OPAL devices.[https://www.ieee-security.org/TC/SP2019/papers/310.pdf If data is encrypted by the operating system (e.g. dm-crypt), the encryption key is unknown to the compromised drive, thus circumventing this attack vector entirely.

## Linux support
The kernel supports OPAL self-encrypting drives via the  option.All officially supported kernels are built with this option enabled.

[https://github.com/Drive-Trust-Alliance/sedutil sedutil, under the umbrella of The Drive Trust Alliance (DTA), is "an Open Source (GPLv3) effort to make core Self Encrypting Drive technology freely available to developers."cryptsetup, the command line utility for dm-crypt, gained limited OPAL support. See the [https://mirrors.edge.kernel.org/pub/linux/utils/cryptsetup/v2.7/v2.7.0-ReleaseNotes cryptsetup 2.7.0 release notes to check whether its capabilities suffice for your purpose.

## Using sedutil
Install the  package, which contains the sedutil-cli tool, and helper scripts to create a custom pre-boot authorization (PBA) image based off the current operating system in use (e.g. for setting a custom console keymap).  Alternatively, you can install sedutil solely for acquiring the sedutil-cli toolset, but download and use the precompiled PBA image (for BIOS or UEFI) provided by the Drive Trust Alliance.

For devices connected via SATA,  must be set to  (true) in order to use sedutil. Either add  to the kernel parameters, or by setting  to  on a running system.

## Encrypting the root (boot) drive
These instructions assume you have the sedutil-cli tool installed (via the  package, or by other means)

## Check if your disk supports OPAL
 # sedutil-cli --isValidSED DRIVE

If you get something like

 sedutil:: Invalid or unsupported device: /dev/nvme1n1

then your disk does not support OPAL. On the contrary, the following output means OPAL standards 2.x are supported, as the drive has a 2 (or a 12 for both OPAL 1 and 2) in the second column indicating OPAL 2 support:

 /dev/nvme2n1 SED -2--- HFS512GEJ9X110N                         :51070C30

Windows version of sedutils outputs (for an unsupported drive):

 \\.\PhysicalDrive0 NO --- CT1000P3PSSD8    R413

The letter "P" in the column means the drive supports PYRITE rather than OPAL.

You may also run  and look for a section like below being present:

 OPAL 2.15 function (0x0203)
     Base comID = 0x0888, Initial PIN = 0x0, Reverted PIN = 0x0, comIDs = 1
     Locking Admins = 4, Locking Users = 9, Range Crossing = N

## Download the rescue image (optional)
Note that this rescue image was built in 2017 and its PBA-Image, on newer AMD-Laptops causes the internal keyboard-input to fail - thus requiring an external keyboard to enter the Disk Password. You might want to build your own PBA instead.

Download a rescue system for a machine provided by the Drive Trust Alliance, e.g. .

## Create a bootable drive
Decompress the rescue image (if required):

 $ gunzip RESCUE64.img.gz

Create a bootable drive using the downloaded rescue image, for example using dd:

 # dd bs=4M if=path/to/RESCUE64.img of=/dev/sdx status=progress conv=fsync oflag=direct

## Using Pre-boot Authorisation (PBA)
The following steps will install a PBA image in your EFI/BIOS which will start before your system and prompt you for a password. If the password is correct, it will unlock the drive and reboot into the normal operating system boot loader.

## Encrypting your drive
## Enable locking
Boot into the rescue system and use the output of  to help identify the correct drive, e.g. .

Setup the drive initially, which will be set both SID and Admin1 passwords to the same PASSWORD of your choice:

 # sedutil-cli --initialsetup PASSWORD DRIVE

Then enable the global locking range 0 (i.e. the entire drive):

 # sedutil-cli --enablelockingrange 0 PASSWORD DRIVE
 # sedutil-cli --setmbrdone off PASSWORD DRIVE

## Set a password
To optionally change the PASSWORD from initial setup prior to continuing with setup:

 # sedutil-cli --setsidpassword PASSWORD NEW_SID_PASSWORD DRIVE

will change both the SID and Admin1 to NEW_SID_PASSWORD. To only change the Admin1 password:

 # sedutil-cli --setadmin1pwd PASSWORD NEW_ADMIN1_PASSWORD DRIVE

## Install the Pre-boot Authorisation
Install the Pre-boot Authorisation (PBA) image:

 # gunzip /usr/sedutil/UEFI64-*.img.gz
 # sedutil-cli --loadPBAimage PASSWORD /usr/sedutil/UEFI64-*.img DRIVE

Power off the computer to lock the drive.

When the computer is next powered on, the PBA should ask for your password; then unlock the drive and chain-load the decrypted operating system.

## Troubleshooting: PBA Cold Reboot Locks Drives Again
In some cases, the PBA will load, accept the password, and unlock the drives but when chain-loading to the decrypted operating system it will do a "cold" reboot which powers off the disks for a moment and result in the drives locking again. So you get stuck in a loop of always unlocking the drives but never booting from them.

If this is the case, you will need to edit the  to guarantee it does a "warm" reboot:

 # losetup --find --show ./UEFI64-*.img
 # partprobe /dev/loop0
 # mount /dev/loop0p1 /mnt
 # cd /mnt/EFI/boot
 # $EDITOR syslinux.cfg # add " reboot=warm" (no quotes) to the end of the line starting with  "append"
 # cd -
 # sync
 # umount /mnt
 # losetup -D

Now you can copy the image to the drive again with:

 # sedutil-cli --loadPBAimage PASSWORD ./UEFI64-*.img DRIVE

If you are using the recovery image the above might not work ( fails with ), you can edit the file on your computer and copy it on the recovery USB drive (but after the end of the recovery image)

 # dd bs=4M if=UEFI64.img of=DRIVE seek=100

 will skip 400 MiB from the start of the drive to avoid overwriting the recovery image itself.

Then, once the recovery is started you can get your image:

 # dd bs=4M if=DRIVE of=UEFI64.img skip=100 count=10

× should be more then the file size.

Truncate file to actual size:

 # truncate -s IMGSIZE UEFI64.img

## Troubleshooting: UEFI loses its boot configuration
If you use an EFI boot stub and configured UEFI to boot your kernel directly, after the disk is unlocked the firmware might forget all its configuration (and it loses it on every unlock). In that case you can install an UEFI boot loader to the default/fallback boot path  and then the firmware would be able to boot it with its default configuration.

It will be helpful to have an USB flash installation medium: if you plug it in after unlocking the disk, it will auto-boot and let you configure your now-unlocked boot disk.

## Using a mkinitcpio hook
Instead of using a PBA, the drive can be setup to only encrypt the root partition whilst leaving the  partition accessible. This way, the system can boot and a  hook used to unlock the drive before the rest of the boot sequence is completed. This has the advantage of not needing to install a PBA and reboot, and also allows for easier support of resume from S3 sleep.

## Encrypting your drive
Follow the steps outlined above to create a rescue system, then boot into it.

The first command will delete everything off of the drive. Omitting it will not save your data, because setting up the new locking range will destroy it anyway, and it might cause the subsequent commands to refuse operation.

 # sedutil-cli --yesIreallywanttoERASEALLmydatausingthePSID PSID DRIVE
 # sedutil-cli --initialsetup PASSWORD DRIVE
 # sedutil-cli --setMBREnable off PASSWORD DRIVE

The PSID (physical security identifier) can only be found on the physical drive label (the sticker on top of the drive).

## Partition the drive
Partition the drive as desired, making sure the EFI and/or  partitions are at the start of the disk, immediately followed by the root partition. For example:

# 1G, FAT32,
# ext4,

Or a slightly more complex setup:

# 100M, FAT32, EFI
# 2G, ext4,
# ext4,
# Swap

It is important the EFI and/or  partitions have enough space to hold all of the kernel images you may want to install. It will not be possible to expand these later without destroying all of the data in the root partition, as the encryption headers would be overwritten.

## Enable locking
Use  to help identify the correct drive, e.g. , then use  to find:

* RANGE_START = "Start" of the root partition
* RANGE_LENGTH = "Sectors" of the root partition

In the example below, RANGE_START would be 2097152 and RANGE_LENGTH 974675968. It is important that these numbers are divisible by 8 to work with , rounding may be necessary.

 Device       Start       End   Sectors   Size Type
 /dev/sda1     2048   2097151   2095104  1023M EFI System
 /dev/sda2  2097152 976773119 974675968 464.8G Linux filesystem

Create locking range 1 to only cover the root partition (and optionally swap):

 # sedutil-cli --setupLockingRange 1 RANGE_START RANGE_LENGTH PASSWORD DRIVE
 # sedutil-cli --enablelockingrange 1 PASSWORD DRIVE

## Lock boot partition as read-only (optional)
For extra security, the EFI and/or  partitions can be locked as read-only. Identify the RANGE_START and RANGE_LENGTH in the same manner as for the root partition, then issue the following commands:

 # sedutil-cli --setupLockingRange 2 RANGE_START RANGE_LENGTH PASSWORD DRIVE
 # sedutil-cli --readonlyLockingRange 2 PASSWORD DRIVE

## Install the operating system
You may now install the operating system, taking care to use the existing partitions and not alter them in any way. Once done, reboot into the new system without powering off first.

## Setup mkinitcpio
## Custom mkinitcpio hook
Create a custom mkinitcpio hook to ask for the drive password on boot:

{{hc|/etc/initcpio/install/sedutil|
#!/bin/bash

help() {
    cat  /dev/null 2> /dev/null
	return $?
}

is_opal_locked() {
	local locked=$(sedutil-cli --query "$1"  grep -A1 '^Locking function (0x0002)'  grep -Po '(?<=Locked = )test "$locked" = "Y"
	return $?
}

get_block_device_info() {
	sedutil-cli --query "$1"  gawk '/^\//{print;exit}'
	if [ $? != 0  ; then
		msg "Unable to query $1"
	fi
}

opal_unlock() {
	while true ; do
		stty -echo
		echo "Password for"
		echo -n "$2: "
		read pass
		stty echo

		# Unlock root range for read/write
		sedutil-cli --setlockingrange 1 rw "$pass" "$1"
		# Uncomment to also unlock boot range
		# sedutil-cli --setlockingrange 2 rw "$pass" "$1"
		if [ $? != 0 ] ; then
			echo "Failed to unlock!"
			continue
		fi

		echo "Unlocked!"
		break
	done
}
}}

## Custom hook in mkinitcpio config
Edit you mkinitcpio configuration to add the sedutil hook before udev. It is important the hook runs before udev, otherwise udev will get stuck trying to access the encrypted drive and cause I/O errors.

## Regenerate mkinitcpio image
Finally, regenerate the initramfs.

You may now reboot your system. If all goes well, the hook will prompt for a password to unlock your drive and then proceed with the rest of the boot process. If something went wrong, you can boot into the rescue system, manually unlock the drive, then reboot into your normal system using the default initcpio image and proceed to debug your system.

## Accessing the drive from a live distribution
The easiest way is to boot the encrypted SSD first, in order to run the shadow MBR. Then press the key that prompts the boot menu and boot whatever device you prefer. Such a way the SED will be completely transparent.

Another way is to directly boot into the live distribution and use sedutil to unlock the SSD:

 # sedutil-cli --setlockingrange 0 rw password drive
 # sedutil-cli --setmbrdone on password drive
 # partprobe drive

Verify that you followed the instructions after the note in #Linux support.

## Disable locking
If you want to turn off Locking and the PBA:

 # sedutil-cli --disableLockingRange 0 password drive
 # sedutil-cli --setMBREnable off password drive

## Re-enable locking and the PBA
You can later re-enable locking and the PBA using this command sequence

 # sedutil-cli --enableLockingRange 0 password drive
 # sedutil-cli --setMBREnable on password drive

## Encrypting a non-root drive
A secondary drive that is not used for the system root, for example a separate drive hosting a permanent /data partition or a portable USB-drive, can be setup.

A non-root drive does not require loading a PBA. So, activating the encryption is as simple as running:

 # sedutil-cli --initialsetup password drive
 # sedutil-cli --enableLockingRange 0 password drive
 # sedutil-cli --setMBREnable off password drive

If it is a portable drive and/or you want to unlock the drive manually, you should do the as in #Accessing the drive from a live distribution, but you need just the first command, because MBR shadowing has not been enabled:
 # sedutil-cli --setlockingrange 0 rw password drive

This will unlock the drive until it is disconnected or your machine goes into suspend, beware that this may cause loss of data.

## Changing the passphrase
Changing the passphrase does not lose existing data on the drive, and does not require re-encryption of data.

 # sedutil-cli --setSIDPassword password newpassword device
 # sedutil-cli --setAdmin1Pwd password newpassword device

Read the #Key management technical implementation section above to learn about how this is implemented securely within the drive, and why it is possible to change the passphrase without losing the existing encrypted data on the drive.

## Waking up from suspend
Suspending the system results in a crash by default, because power is being cut from the drive and that causes it to lock itself. In order to wake up from suspend the kernel should know a hashed password for the disk. This functionality is in-kernel since 4.11, but it is only available via a fork of sedutil, either  or . Note the latter has additional features but a slightly different command syntax Generate a hashed password for the block device specified as :

 # sedutil-sleep --printPasswordHash password /dev/device

## Preparing drive for sleep
## With mkinitcpio hook
If already using a mkinitcpio hook to unlock the drive on boot, then you can simply add code as below to the hook to also prepare the drive for sleep. Make sure this code is placed after the command that unlocks the ranges , otherwise it will fail. In this example,  is a variable containing the password for unlocking, while  is a variable containing the device to prepare for sleep, typically the root partition (e.g. ).

## With systemd service
Create a systemd service, inserting hashes for each device:

## Using cryptsetup
cryptsetup can be used to perform the initial setup of OPAL equivalent to the example of sedutil, albeit not for USB-drives. cryptsetup is always used on block devices, i.e. an individual partition, and adds a LUKS header to it which includes a LUKS encrypted OPAL key to unlock it. See  for details.

cryptsetup's advantage over sedutil is that, besides the initial  command, no special setup is required. It is just a LUKS device like any other which allows using all features LUKS provides and the option of using systemd-cryptenroll.

See the [https://mirrors.edge.kernel.org/pub/linux/utils/cryptsetup/v2.7/v2.7.0-ReleaseNotes cryptsetup 2.7.0 release notes for command examples with OPAL related output of the LUKS header.

## Encrypting a partition
Encrypting a partition with OPAL requires the OPAL admin password. If you have not previously set one, you will need to erase all data on the drive with  to be able to create a new OPAL admin password. Follow the instructions in #Secure disk erasure to perform the erase.

OPAL hardware encryption can be set up on a partition using  option . This will avoid the performance penalty that software encryption brings to an encrypted partition and the CPU.

Alternatively, the  option can be used to setup both OPAL hardware encryption and dm-crypt software encryption at the same time. The default dm-crypt encryption options for LUKS2 apply and can be configured.

For example, with  as the partition on a drive with OPAL support:

Subsequent to the setup, the block device can be opened and formatted with a filesystem, see dm-crypt/Device encryption#Unlocking/Mapping LUKS partitions with the device mapper. Only the LUKS passphrase is required from now on, because the header automatically unlocks the OPAL encryption.

## Removing a locking range
Since OPAL locking ranges are neither readable nor writable while in a locked state, an encrypted partition cannot be repurposed until the OPAL locking range spanning it is removed.

To remove OPAL encryption from a partition use :

## Secure disk erasure
Whole disk erasure is very fast, and remarkably simple for a self-encrypting drive. Simply passing a cryptographic disk erasure (or crypto erase) command (after providing the correct authentication credentials) will have the drive self-generate a new random data encryption key internally. This will permanently discard the old key, thus rendering the encrypted data irrevocably un-decryptable. The drive will now be in a 'new drive' state.

Read the #Key management technical implementation section above to learn more about how this is implemented securely within the drive.

The Solid state drive/Memory cell clearing article covers comprehensive guides to perform the erasure securely.

The following shows an example output by using  to perform it:

The  option returns the  output.

The PSID (physical security identifier) can only be found on the physical drive label (the sticker on top of the drive).

## Suspend/hibernation support
Nothing special is required, they work exactly as with regular LUKS since OPAL reuses the existing LUKS framework.

See dm-crypt/Swap encryption.

## BIOS based ATA-password
Previous to the industry's TCG OPAL 2.0 standard initiative, the relevant ATA standard defined an "ATA security feature set" for full-disk encryption using self-encrypting drives. This relies on the PC BIOS, not the drive, to feature an unlocking mechanism utilizing the BIOS to setup the user's encryption passphrase. This legacy BIOS-based (ATA) method was considered more unreliable to setup and prone to error with regard to interoperability between PC vendors.Typical errors include, for example, inabilities to unlock a device once it is plugged into a system from a different hardware vendor. Hence, the availability of BIOS support for the legacy password mechanism decreases in availability, particularly for consumer hardware.

See Solid state drive#Security for more information.
