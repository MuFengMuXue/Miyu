# Dm-verity

Dm-verity uses a tree of sha256 hashes to verify blocks as they are read from a block device. Consequently, this ensures files have not changed between reboots or during runtime. This is useful for extending trust to the OS by mitigating zero days and unauthorized changes to root, as well as enforcing security policies, encryption and userspace security. Verity devices are regular block devices which can be accessed in .

dm-verity is part of the device mapper in the Linux kernel and is implemented using systemd.

This article mainly describes setting up a verity-protected read-only root partition.

## Components
A dm-verity root setup setup consists of the following:

# a  root filesystem image or partition,
# verity hash tree ,
# the root hash of the verity tree ,
# ,
# ,
# verity kernel command line options,
# veritysetup (part of ),
# a unified kernel image which contains a stub EFI loader, kernel, initramfs, kernel command line, and microcode: ,
# Secure Boot.

The unified kernel image and Secure Boot are recommended but not required. Verity is intended to be used as one of the last steps in a boot process that protects the OS and the kernel from changes. It is easily defeated without Secure Boot and unified kernel images.

## Preparation
To enable dm-verity, you must have a working system already installed and configured. See Installation guide for the details.

Typically, it is necessary to have a separate partition or logical volume to store the verity hash data.

The recommended disk layout is similar to this:

## Partitioning
# EFI system partition for the boot loader ();
# XBOOTLDR partition ()
# Root partition (, optionally with encryption, see Data-at-rest encryption).
# Verity partition (), should require 8-10% the size of Root
# Home (optional if you want write access for a user)
# Var (many programs will not run if  is not writable, so it should be separate from the root partition depending on use case)

:

 and  should be writable filesystems. On a server that just has one purpose this may be optional, since e.g. a wireguard server needs no write access to the disk.

 offers an attractive alternative to ext4 or squashfs on the root partition. EROFS, like squashfs, does not allow writes by design and has better performance in many cases than comparable filesystems on flash and solid-state media. It uses lz4 compression by default and was designed for Android phones by Huawei, which make extensive use of dm-verity.

## Possible issues with boot and runtime
Any files that need to be written to during init or changed during runtime must be made writable by some method otherwise the program will not function as expected.

Many programs need write access to . You can use a separate  partition but this will make all of these configuration files writable. Create a folder  and move the files that need write access into it than symlink into , as with the example with NetworkManager below.

Some programs will expect these folders and files to still exist (even read-only) on the root filesystem for early init. For instance, systemd-journald will break if  does not exist or is a symlink. Bind mounts can be useful for this.

One way to find out which files will change when the system is running is to enable the  module, use the system, and check the files in  to see what you may need to address. Any files in this folder were written to the tmpfs overlaid on top of root. Place the module into , add  to the dracut modules list, and  to your kernel command line and regenerate the initramfs. The module can be found at https://github.com/TylerHelt0/dracut-overlayroot.

## Pacman
Since the root filesystem will be mounted read-only and  should be mounted read-write in most cases, the path to the pacman database should be changed to . This will ensure the rootfs always has the correct list of installed packages.
#
# Edit  and set
# To be able to sync lists and check updates, move  to  and symlink it.
# If you wish to be able to change mirrorlist without modifying the root file system, move it to  and symlink it as well.

## NetworkManager
To setup connections with NetworkManager, you need write access to . Move the  folder to  and symlink to it on the root filesystem.

 # ln -sf /etc/NetworkManager/system-connections /var/etc/NetworkManager/system-connections

## Setting up verity
# Boot from a live medium
# Mount your root filesystem as read-only
# Make sure all your changes are perfect
# do

You will now have the rootfs, the verity hash tree, and the roothash. Alternatively you can save the hashes to a file by replacing the  path and write it to the device later.

To test it you can use . The verity device can be mounted from .

## Configuring the kernel command line
Add the following options to your kernel command line:
#
#
#
#
#  or  (the default behavior will just print an error to dmesg and will not prevent untrusted code from running)

If the roothash changes you must also edit the cmdline/rebuild the unified kernel image with the new value. Failure to do so can result in an unbootable system.

## Additional recommended options
#  to prevent changes to root if not using erofs or squashfs
#  to prevents access to a shell if the root is corrupt
#  to prevents access to a shell if boot fails
#  prevents users from accessing kernel memory

## Devices other than root
The use of dm-verity is not limited to the root device. Other devices that need to be verified at boot can be put into  and will be assembled by . See  for more information.

Be aware that it is much easier to remount a non-root partition as RW while the system is running. Integrity violations also will not trigger a reboot. Even if  has verity enabled, it is trivial for a user with root privileges to disable verity on a non-root partition.

## Security considerations
dm-verity does not provide an all-in-one solution but should be used alongside other methods of securing the system when the disk is removed and when the system is fully booted.

## Secure Boot
It is recommended to enable Secure Boot with custom keys after verity is setup.

Verity protection is useless if a virus or attacker can replace the  containing the embedded roothash which would allow any root filesystem to be booted. Signing the kernel image for Secure Boot will prevent the kernel image from being replaced and ensure integrity of the root filesystem as long as the firmware is secure.

 or  can be used to maintain your unified kernel images and keep your boot loader signed.  will also handle your kernel command line.  can be used to create Secure Boot keys.

## Unified kernel image
UKIs bundle together at minimum the linux kernel, an initramfs, CPU microcode, and a cmdline. The advantage to using an UKI is that it prevents changes to both the kernel, initramfs and cmdline when the UKI is signed and used with secureboot. If the cmdline section of the UKI is left blank, it can be supplied by a boot loader like systemd-boot. Otherwise it can only be changed by rebuilding and resigning a new UKI.

UKIs can be directly booted by UEFI if kernel efistub is enabled or if shim/preloader is used.

## Signing kernel modules/DKMS
Packaged kernels ship with pre-signed modules. If kernel lockdown or module signature verification is enabled, modules built with DKMS or pre-built out-of-tree kernel modules will refuse to load. One must create a custom kernel to enable signing and loading of out-of-tree modules.

See Signed kernel modules for more information about signed kernel modules.

## Encryption
Although the verity root device will be tamper-resistant, it provides no confidentiality. It could be located on an unencrypted partition if it contains no secret data. If the kernel is protected by Secure Boot, it would be impossible to replace the data in the root or verity devices without replacing the kernel.

The verity root device can be used to unlock other encrypted devices. If done with keyfiles, the verity root should be encrypted. If using a TPM and systemd-cryptenroll to store keys, the verity root could be unencrypted.

## TPM
A TPM 2.0 can be used to protect encryption keys for the LUKS device containing root. After Secure Boot is enabled, you can use  to bind keys to PCRs. Recommended PCRs are 0,1,5,7. This will stop decryption if the firmware, firmware options, GPT layout or secure boot state is changed, respectively.

The reason for binding on 0,1, and 5 is to ensure attackers cannot replace the motherboard firmware to disable secureboot and consequently disable verity.

You must pass this kernel option:

 rd.luks.options=UUID_of_LUKS=tpm2-device=auto

You may also need to add tpm2 support to your initramfs or include the module if using dracut. See systemd-cryptenroll#Trusted Platform Module for more information.

## systemd-boot
If you use systemd-boot as your boot loader, it will measure the  into PCR 4. This can be used to prevent decryption of root if the kernel image, initramfs, or kernel command line is changed.

## Mandatory access control
During runtime, methods such as OverlayFS, tmpfs, and bind mounts can still be used to get write access on the folders within . For this reason, it is important to still harden the OS. Apparmor, SELinux and other access control mechanisms are useful for this.

## Updating packages
A dm-verity read-only root should not be updated the traditional way with pacman. Verity is intended mostly for embedded devices and others which value code-integrity over the rolling release model. This has the primary benefits of extending trust to the OS and ensuring a device always boots the same way. E.g. an emulator box for normies or a secure web server. dm-verity, combined with other security methods like selinux, eliminate entire classes of zero-days and consequently the need to update is less frequent unless new features are desired. Think about a router running linux: many routers are compromised by malware without the user ever knowing. If the router was verity-protected in a secure way, it would prevent viruses from gaining persistence.

You could use ext4 for  which enables you to mount it rw. You can then do updates, rehash the filesystem, and change the roothash in the cmdline, but it would be better to release incrementally updated images of the filesystems. Disabling verity to do updates on a writable filesystem is as simple as omitting the systemd.verity=1 cmdline option.

## Building images
A VM can be used to maintain a 'rolling' system and imaged when updates are needed. A chroot could work as well. Setup all the partitioning and boot logic the way it is expected to work on the target system, than reboot the VM into a live media and make images of the partitions. If you image the xboot partition, it can be flashed directly to a partition to update the UKI/kernel/initramfs/cmdline. If paired with an image for the root filesystem this is more or less a complete system update.

Systemd already has the logic to retrieve images from an update server (Or local dir) and flash them to partitions which may or may not already exist. It can also install and remove files into existing partitions.

See  and .

## A/B update scheme
Another way to handle updates would be to use a system similar to Android's A/B partition system. This entails having two sets of the root and verity partitions. When an update is necessary the active partition could be copied to the inactive one. The inactive partition could than be updated as normal from chroot or with pacman and 'sealed' with dm-verity. On next boot, the inactive partition becomes the active partition.

If using UKI the UKI must be updated with the root and verity partitions. At minimum the kernel cmdline must be updated with new roothash.

## overlayfs
If the user wants a system that has optional persistence or can install packages which are reverted at reboot, an overlay can be mounted as root with the verity root as the lower dir. The upper dir could be a persistent block device or a tmpfs. If using A/B, one could remount  as a writable OverlayFS and use normal update methods, than copy the contents of the overlayfs into the inactive partition and rehash verity.

If the user requires temporary persistence (for example, the ability to install packages that are reset at boot),  can be passed on the kernel command line.

## Flatpak
Flatpak can be used to install and update apps within  and  without write access to . Flatpak would be ideal to solve most user's needs for installing applications and updating them in a verity-protected desktop PC. Flatpak works on  by default.

## Tips and tricks
## Automation
The above steps can be automated with the package . It will build a squashfs rootfs and sign the roothash with the kernel and the initramfs. On boot, you can decide to boot a persistent system, where changes on the overlayfs are saved, or to boot a volatile system. It also keeps the last rootfs as a backup, so you can decide to boot the last working rootfs.
