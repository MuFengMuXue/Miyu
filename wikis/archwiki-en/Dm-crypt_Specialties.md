# Dm-crypt/Specialties

## Securing the unencrypted boot partition
The  partition and the Master Boot Record are the two areas of the disk that are not encrypted, even in an encrypted root configuration. They cannot usually be encrypted because the boot loader and BIOS (respectively) are unable to unlock a dm-crypt container in order to continue the boot process. An exception is GRUB, which gained a feature to unlock a LUKS encrypted  - see dm-crypt/Encrypting an entire system#Encrypted boot partition (GRUB).

This section describes steps that can be taken to make the boot process more secure.

## Booting from a removable device
Using a separate device to boot a system is a fairly straightforward procedure, and offers a significant security improvement against some kinds of attacks. Two vulnerable parts of a system employing an encrypted root filesystem are

* the Master Boot Record, and
* the  partition.

These must be stored unencrypted in order for the system to boot. In order to protect these from tampering, it is advisable to store them on a removable medium, such as a USB drive, and boot from that drive instead of the hard disk. As long as you keep the drive with you at all times, you can be certain that those components have not been tampered with, making authentication far more secure when unlocking your system.

It is assumed that you already have your system configured with a dedicated partition mounted at . If you do not, please follow the steps in dm-crypt/System configuration#Kernel parameters, substituting your hard disk for a removable drive.

Prepare the removable drive ().

 # gdisk /dev/sdx #format if necessary. Alternatively, cgdisk, fdisk, cfdisk, gparted...
 # mkfs.ext2 /dev/sdx1 #for BIOS systems
 # mkfs.fat -F 32 /dev/sdx1 #for UEFI systems
 # mount /dev/sdx1 /mnt

Copy your existing  contents to the new one.

 # cp -ai /boot/* /mnt/

Mount the new partition. Do not forget to update your fstab file accordingly.

 # umount /boot
 # umount /mnt
 # mount /dev/sdx1 /boot
 # genfstab -p -U / > /etc/fstab

Update GRUB.  should detect the new partition UUID automatically, but custom menu entries may need to be updated manually.

 # grub-mkconfig -o /boot/grub/grub.cfg
 # grub-install /dev/sdx #install to the removable device, not the hard disk. for BIOS systems
 # grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub #for UEFI systems

Reboot and test the new configuration. Remember to set your device boot order accordingly in your BIOS or UEFI. If the system fails to boot, you should still be able to boot from the hard drive in order to correct the problem.

## chkboot
Referring to an article from the ct-magazine (Issue 3/12, page 146, 01.16.2012, the following script checks files under  for changes of SHA-1 hash, inode, and occupied blocks on the hard drive. It also checks the Master Boot Record. The script cannot prevent certain type of attacks, but a lot are made harder. No configuration of the script itself is stored in unencrypted . With a locked/powered-off encrypted system, this makes it harder for some attackers because it is not apparent that an automatic checksum comparison of the partition is done upon boot. However, an attacker who anticipates these precautions can manipulate the firmware to run their own code on top of your kernel and intercept file system access, e.g. to , and present the untampered files. Generally, no security measures below the level of the firmware are able to guarantee trust and tamper evidence.

The script with installation instructions is [https://ftp.heise.de/pub/ct/listings/1203-146.zip available (Author: Juergen Schmidt, ju at heisec.de; License: GPLv2). There is also package  to install. The AUR package is recommended, as it has additional helpful scripts.

## Juergen Schmidt's script
As  needs to be executed right after login, you need to add it to the autostart (e.g. under KDE -> System Settings -> Startup and Shutdown -> Autostart; GNOME 3: gnome-session-properties).

With Arch Linux, changes to  are pretty frequent, for example by new kernels rolling-in. Therefore it may be helpful to use the scripts with every full system update. One way to do so:

 #!/bin/sh
 #
 # Note: Insert your '''' and execute it with sudo for pacman & chkboot to work automagically
 #
 echo "Pacman update Quickcheck before updating" &
 sudo -u '''' /usr/local/bin/chkboot_user.sh
 /usr/local/bin/chkboot.sh
 sudo -u '''' /usr/local/bin/chkboot_user.sh
 echo "Pacman update [2 Syncing repos for pacman"
 pacman -Syu
 /usr/local/bin/chkboot.sh
 sudo -u '''' /usr/local/bin/chkboot_user.sh
 echo "Pacman update All done, let us roll on ..."

## AUR package
After installing, enable .

You may want to add  to the end of your mkinitcpio hooks, so that your chkboot hashes get updated every time mkinitcpio regenerates your initramfs. You can do this by adding  to the end of the  array in .

The AUR package also comes with an  script, which will cause a graphical window to pop up with a warning if  changes are detected. You can make use of this script by adding it to the startup scripts of your graphical environment.

## mkinitcpio-chkcryptoboot
 is a mkinitcpio hook that performs integrity checks during early-userspace and advises the user not to enter their root partition password if the system appears to have been compromised. Security is achieved through an encrypted boot partition, which is unlocked using GRUB's  module, and a root filesystem partition, which is encrypted with a password different from the former. This way, the initramfs and kernel are secured against offline tampering, and the root partition can remain secure even if the  partition password is entered on a compromised machine (provided that the chkcryptoboot hook detects the compromise, and is not itself compromised at run-time).

This hook requires  release >=2.00 to function, and a dedicated, LUKS encrypted  partition with its own password in order to be secure.

## Installation
Install  and edit . If you want the ability of detecting if your boot partition was bypassed, edit the  and  variables, with values known only to you. You can follow the advice of using two hashes as is suggested right after the installation. Also, be sure to make the appropriate changes to the kernel command line in . Edit the  line in , and insert the  hook before . When finished, regenerate the initramfs.

## Technical overview
 consists of an install hook and a run-time hook for mkinitcpio. The install hook runs every time the initramfs is rebuilt, and hashes the GRUB EFI stub () (in the case of UEFI systems) or the first 446 bytes of the disk on which GRUB is installed (in the case of BIOS systems), and stores that hash inside the initramfs located inside the encrypted  partition. When the system is booted, GRUB prompts for the  password, then the run-time hook performs the same hashing operation and compares the resulting hashes before prompting for the root partition password. If they do not match, the hook will print an error like this:

 CHKCRYPTOBOOT ALERT!
 CHANGES HAVE BEEN DETECTED IN YOUR BOOT LOADER EFISTUB!
 YOU ARE STRONGLY ADVISED NOT TO ENTER YOUR ROOT CONTAINER PASSWORD!
 Please type uppercase yes to continue:

In addition to hashing the boot loader, the hook also checks the parameters of the running kernel against those configured in . This is checked both at run-time and after the boot process is done. This allows the hook to detect if GRUB's configuration was not bypassed at run-time and afterwards to detect if the entire  partition was not bypassed.

For BIOS systems the hook creates a hash of GRUB's first stage boot loader (installed to the first 446 bytes of the bootdevice) to compare at the later boot processes. The main second-stage GRUB boot loader  is not checked.

## AIDE
Alternatively to above scripts, a hash check can be set up with AIDE which can be customized via a very flexible configuration file.

## Using GPG, LUKS, or OpenSSL encrypted keyfiles
The following forum posts give instructions to use two factor authentication, gpg or openssl encrypted keyfiles, instead of a plaintext keyfile described earlier in this wiki article [https://bbs.archlinux.org/viewtopic.php?id=120243 System Encryption using LUKS with GPG encrypted keys:

* GnuPG: Post regarding GPG encrypted keys This post has the generic instructions.
* OpenSSL: Post regarding OpenSSL encrypted keys This post only has the  hooks.
* OpenSSL: Post regarding OpenSSL salted bf-cbc encrypted keys This post has the  initcpio hooks, install, and encrypted keyfile generator scripts.
* LUKS: Post regarding LUKS encrypted keys with a  initcpio hook. Or #Encrypted /boot and a detached LUKS header on USB below with a custom encrypt hook for initcpio.

Note that:

* You can follow the above instructions with only two primary partitions, one boot partition (required because of encryption) and one primary LVM partition. Within the LVM partition you can have as many partitions as you need, but most importantly it should contain at least root, swap, and home logical volume partitions. This has the added benefit of having only one keyfile for all your partitions, and having the ability to hibernate your computer (suspend to disk) where the swap partition is encrypted. If you decide to do so your hooks in  should look like this: and you should add  to your kernel parameters.
* If you need to temporarily store the unencrypted keyfile somewhere, do not store them on an unencrypted disk. Even better make sure to store them to RAM such as .
* If you want to use a GPG encrypted keyfile, you need to use a statically compiled GnuPG version 1.4 or you could edit the hooks and use
* It is possible that an update to OpenSSL could break the custom  mentioned in the second forum post.

## Remote unlocking of root (or other) partition
Imagine a headless system or a system not physically accessible. Additionally, one or more LUKS encrypted partitions (root or others) or volumes need to be unlocked during startup. In this case you need to be able to connect via network and provide a password during early boot (initramfs) phase. This can be achieved by using one or more mkinitcpio hook(s) that configure a network interface and start some kind of SSH server. Some packages listed below contribute various mkinitcpio build hooks to ease the configuration. The following tutorials add a remote unlocking method in addition to the existing local console password prompt.

## systemd based initramfs (built with mkinitcpio)
For systemd based initramfs the AUR package  provides a collection of build hooks (aka install hooks) to achieve network connectivity and SSH login during early boot. Depending on the concrete setup this either gives you access to the initramfs environment via busybox' dash or just a password prompt.

A minimal setup:

When building the initramfs with  this setup copies the already existing configuration of systemd-networkd from the main system and also tries to copy / convert existing SSH server keys from an existing TinySSH or OpenSSH installation.  needs to be installed (but not necessarily enabled) on the main system. There are some more configuration parameters to cover more use cases. See the documentation of  for further details.

## Busybox based initramfs (built with mkinitcpio)
For busybox based initramfs the  package provides the ,  and  hooks needed for network connectivity and SSH access during the boot process. After installing the package, check its optional dependencies and manually install those required by the hooks you plan to use. E.g. to use the  and  hooks, you have to install  and . You also need to install the  package which provides the  hook, a drop-in replacement for the  hook that prompts for the passphrase upon SSH login.

# If you don't have an SSH key pair yet, generate one on the client system (the one which will be used to unlock the remote machine).
# Add your SSH public key(s) or copy an existing  file to the remote machine's  or  file.
# Add the  hooks to the HOOKS array in , before , and regenerate the initramfs. The  hook replaces the  hook.
# Configure the required  parameter and add the  kernel parameter to your boot loader configuration. E.g. if you use DHCP for network configuration:  The hook will wait up to 120 seconds for a response from the DHCP server. This can be adjusted with the  kernel parameter. Alternatively, configure a static IP:  You can also specify the subnet mask and gateway if necessary:  The  parameter supports many more options, e.g configuring multiple interfaces, etc. For more info see the hook's documentation:  The examples above assume an Ethernet connection. If using Wi-Fi instead, install the  package and create a wpa_supplicant configuration:  Then add the  hook before  in , make sure your Wi-Fi related modules are in the MODULES array, and use  as the kernel parameter.
# Restart the remote system and ssh to it on port 222 as the  user. The SSH server in the initramfs generates its own set of host keys and listens on a non-standard port by default to allow your SSH client to verify a separate set of host keys for the initramfs and the main SSH server. Reusing host keys from the main SSH server isn't recommended as the initramfs image may be world-readable which would expose them and make the system vulnerable to MITM attacks. Both the listening port and the host key types can be configured, see the hook documentation for details ( or ). You will be prompted for the passphrase to unlock the encrypted device. After unlocking, the system will complete its boot process and you can ssh to it as you normally would.

## systemd based initramfs (built with dracut)
If you are using dracut instead of mkinitcpio, you might want to check out dracut-sshd as an alternative to the above options.

## One-time password-less reboot
Another method that can be used to reboot a remote, headless or otherwise inaccessible system whilst not needing to be at the terminal to type the encrypted root drive password, is to use a temporary keyfile. This will need to be placed in a location that is accessible to the kernel at boot, the cryptkey boot parameter will be needed, and that particular keyfile will need to be registered as a valid key by way of the "cryptsetup luksAddKey" command.

This can be done conveniently with the help of . The procedure described to setup that tool on the script's readme file might serve as a template for setting up a home-made solution also. Do take a look at the discussion in the Security considerations section.

## Discard/TRIM support for solid state drives (SSD)
Solid state drive users should be aware that, by default, TRIM commands are not enabled by the device-mapper, i.e. block-devices are mounted without the  option unless you override the default.

The device-mapper maintainers have made it clear that TRIM support will never be enabled by default on dm-crypt devices because of the potential security implications.Minimal data leakage in the form of freed block information, perhaps sufficient to determine the filesystem in use, may occur on devices with TRIM enabled. An illustration and discussion of the issues arising from activating TRIM is available in the [https://asalor.blogspot.de/2011/08/trim-dm-crypt-problems.html blog of a cryptsetup developer. If you are worried about such factors, keep also in mind that threats may add up: for example, if your device is still encrypted with the previous (cryptsetup &2
            ;;
    esac
done

if resolved=$(resolve_device "${cryptdev}" ${rootdelay}); then
    if $headerFlag  cryptsetup isLuks ${resolved} >/dev/null 2>&1; then
        [ ${DEPRECATED_CRYPT} -eq 1 ] && warn_deprecated
        dopassphrase=1
}}

Now edit the mkinitcpio.conf to add the  and  hooks, the  to  and the  to , apart from other configuration the system requires:

This is required so the LUKS header is available on boot allowing the decryption of the system, exempting us from a more complicated setup to mount another separate USB device in order to access the header. After this set up the initramfs is created.

Next the boot loader is configured to specify the  also passing the new  option for this setup:

 cryptdevice=/dev/disk/by-id/your-disk_id:enc:header

To finish, following dm-crypt/Encrypting an entire system#Post-installation is particularly useful with a  partition on an USB storage medium.

## Encrypted /boot and a detached LUKS header on USB
Rather than embedding the  and keyfile into the initramfs image, this setup will make your system depend entirely on the usb key rather than just the image to boot, and on the encrypted keyfile inside of the encrypted boot partition. Since the header and keyfile are not included in the initramfs image and the custom encrypt hook is specifically for the usb's by-id, you will literally need the usb key to boot.

For the usb drive, since you are encrypting the drive and the keyfile inside, it is preferred to cascade the ciphers as to not use the same one twice. Whether a meet-in-the-middle attack would actually be feasible is debatable. You can do twofish-serpent or serpent-twofish.

## Preparing the disk devices
 will be assumed to be the USB drive,  will be assumed to be the main hard drive.

Prepare the devices according to dm-crypt/Drive preparation.

## Preparing the USB key
Use gdisk to partition the disk according to the layout shown here, with the exception that it should only include the first two partitions. So as follows:

Before running , look at the Encryption options for LUKS mode and Ciphers and modes of operation first to select your desired settings.

Prepare the boot partition but do not  any partition yet and Format the EFI system partition.

 # mount /dev/mapper/cryptboot /mnt
 # dd if=/dev/urandom of=/mnt/key.img bs=filesize count=1 iflag=fullblock
 # cryptsetup luksFormat /mnt/key.img
 # cryptsetup open /mnt/key.img lukskey

filesize is in bytes but can be followed by a suffix such as . Having too small of a file will get you a nasty  error. As a rough reference, creating a 4M file will encrypt it successfully. You should make the file larger than the space needed since the encrypted loop device will be a little smaller than the file's size.

With a big file, you can use  and  to navigate to the correct position (see Gentoo:Custom Initramfs#Encrypted keyfile).

Now you should have  opened in a loop device (underneath ), mapped as .

## The main drive
 # truncate -s 16M /mnt/header.img
 # cryptsetup --key-file=/dev/mapper/lukskey --keyfile-offset=offset --keyfile-size=size luksFormat /dev/sda --offset 32768 --header /mnt/header.img

Pick an offset and size in bytes (8192 KiB is the maximum keyfile size for ).

 # cryptsetup open --header /mnt/header.img --key-file=/dev/mapper/lukskey --keyfile-offset=offset --keyfile-size=size /dev/sda enc
 # cryptsetup close lukskey
 # umount /mnt

Follow Preparing the logical volumes to set up LVM on LUKS.

See Partitioning#Discrete partitions for recommendations on the size of your partitions.

Once your root partition is mounted,  your encrypted boot partition as  and your EFI system partition as .

## Installation procedure and custom encrypt hook
Follow the installation guide up to the  step but do not do it yet, and skip the partitioning, formatting, and mounting steps as they have already been done.

In order to get the encrypted setup to work, you need to build your own hook, which is thankfully easy to do and here is the code you need. You will have to follow Persistent block device naming#by-id and by-path to figure out your own  values for the usb and main hard drive (they are linked -> to  or ).

You should be using the  instead of just  or  because  can change and this ensures it is the correct device.

You can name  anything you want, and custom build hooks can be placed in the  and  folders of . Keep a backup of both files ( them over to the  partition or your user's  directory after you make one).  is not a typo.

{{hc|/etc/initcpio/hooks/customencrypthook|output=
#!/usr/bin/ash

run_hook() {
    modprobe -a -q dm-crypt >/dev/null 2>&1
    modprobe loop
    [ "${quiet}" = "y" ] && CSQUIET=">/dev/null"

    while [ ! -L '/dev/disk/by-id/usbdrive-part2' ]; do
     echo 'Waiting for USB'
     sleep 1
    done

    cryptsetup open /dev/disk/by-id/usbdrive-part2 cryptboot
    mount --mkdir /dev/mapper/cryptboot /mnt
    cryptsetup open /mnt/key.img lukskey
    cryptsetup --header /mnt/header.img --key-file=/dev/mapper/lukskey --keyfile-offset=offset --keyfile-size=size open /dev/disk/by-id/harddrive enc
    cryptsetup close lukskey
    umount /mnt
}
}}

 is your USB drive , and  is your main hard drive .

 # cp /usr/lib/initcpio/install/encrypt /etc/initcpio/install/customencrypthook

Now edit the copied file and remove the  section as it is not necessary.

The  and  arrays are empty, and you should not have to replace  array entirely just edit in  after  and before , and make sure  and  are removed.

## Boot loader
Finish the Installation Guide from the  step. To boot you would need either GRUB or efibootmgr. Note you can use GRUB to support the encrypted disks by Configuring the boot loader but editing the  is not necessary for this set up.

Or use direct UEFI Secure Boot by generating keys with  then signing the initramfs and kernel and creating a bootable .efi file for your EFI system partition with . Before using cryptboot or sbupdate note this excerpt from Secure Boot#Using your own keys:

 # efibootmgr --create --disk /dev/device --part partition_number --label "Arch Linux Signed" --loader "EFI\Arch\linux-signed.efi" --unicode

See  for an explanation of the options.

Make sure the boot order puts  first. If not change it with .

## Changing the LUKS keyfile
 # cryptsetup --header /boot/header.img --key-file=/dev/mapper/lukskey --keyfile-offset=offset --keyfile-size=size luksChangeKey /dev/mapper/enc /dev/mapper/lukskey2 --new-keyfile-size=newsize --new-keyfile-offset=newoffset

Afterwards,  and shred or dd the old keyfile with random data before deleting it, then make sure that the new keyfile is renamed to the same name of the old one:  or other name.
