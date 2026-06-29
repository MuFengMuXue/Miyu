# Arch boot process

In order to boot Arch Linux, a Linux-capable boot loader must be set up. The boot loader is responsible for loading the kernel and initramfs before initiating the boot process. The procedure is quite different for BIOS and UEFI systems.

## Firmware types
The firmware is the very first program that is executed once the system is switched on.

## UEFI
The Unified Extensible Firmware Interface has support for reading both the partition table as well as file systems. UEFI does not launch any boot code from the Master Boot Record (MBR) whether it exists or not, instead booting relies on boot entries in the NVRAM.

The UEFI specification mandates support for the FAT12, FAT16, and FAT32 file systems (see UEFI specification version 2.11, section 13.3.1.1), but any conformant vendor can optionally add support for additional file systems; for example, HFS+ or APFS in some Apple's firmwares. UEFI implementations also support ISO 9660 for optical discs.

UEFI launches EFI applications, e.g. boot loaders, boot managers, UEFI shell, etc. These applications are usually stored as files in the EFI system partition. Each vendor can store its files in the EFI system partition under the  directory. The applications can be launched by adding a boot entry to the NVRAM or from the UEFI shell.

The UEFI specification has support for legacy BIOS booting with its Compatibility Support Module (CSM). If CSM is enabled in the UEFI, the UEFI will generate CSM boot entries for all drives. If a CSM boot entry is chosen to be booted from, the UEFI's CSM will attempt to boot from the drive's MBR bootstrap code.

## BIOS
A BIOS or Basic Input-Output System is in most cases stored in a flash memory in the motherboard itself and independent of the system storage. Originally created for the IBM PC to handle hardware initialization and the boot process, it has been replaced progressively since 2010 by UEFI which does not suffer from the same technical limitations.

## System initialization
System switched on, the power-on self-test (POST) is executed. See also Modern CPUs have a backstage cast by Hugo Landau.

## UEFI
# After POST, UEFI initializes the hardware required for booting (disk, keyboard controllers etc.).
# Firmware reads the boot entries in the NVRAM to determine which EFI application to launch and from where (e.g. from which disk and partition).
#* A boot entry could simply be a disk. In this case the firmware looks for an EFI system partition on that disk and tries to find an EFI application in the fallback boot path  ( on systems with a IA32 (32-bit) UEFI). This is how UEFI bootable removable media work.
# Firmware launches the EFI application.
#* This could be a boot loader or the Arch kernel itself using an EFI boot stub.
#* It could be some other EFI application such as the UEFI shell or a boot manager like systemd-boot or rEFInd.

If Secure Boot is enabled, the boot process will verify authenticity of the EFI binary by signature.

## Multibooting
Since each OS or vendor can maintain its own files within the EFI system partition without affecting the other, multi-booting using UEFI is just a matter of launching a different EFI application corresponding to the particular operating system's boot loader. This removes the need for relying on the chain loading mechanisms of one boot loader to load another OS.

See also Dual boot with Windows.

## BIOS
# After POST, BIOS initializes the hardware required for booting (disk, keyboard controllers etc.).
# BIOS launches the first 440 bytes (the Master Boot Record bootstrap code area) of the first disk in the BIOS disk order.
# The boot loader's first stage in the MBR boot code then launches its second stage code (if any) from either:
#* next disk sectors after the MBR, i.e. the so called post-MBR gap (only on a MBR partition table),
#* a partition or a partitionless disk volume boot record (VBR),
#* for GRUB on a GPT partitioned disk—a GRUB-specific BIOS boot partition (it is used in place of the post-MBR gap that does not exist in GPT).
# The actual boot loader is launched.
# The boot loader then loads an operating system by either chain-loading or directly loading the operating system kernel.

## Boot loader
A boot loader is a piece of software started by the firmware—UEFI or BIOS. It is responsible for loading the kernel with the wanted kernel parameters and any external initramfs images.

A boot manager presents a menu of boot options, or provides some other way to control the boot process—i.e. it just runs other EFI executables.

In the case of UEFI, the kernel itself can be directly launched by the UEFI using the EFI boot stub. A separate boot loader or a boot manager can still be used for the purpose of editing kernel parameters before booting.

Systems with 32-bit IA32 UEFI require a boot loader that supports mixed mode booting.

## Feature comparison
{| class="wikitable sortable"
! rowspan="2" | Name
! colspan="2" | Firmware
! colspan="2" | Partition table
! rowspan="2" | Multi-boot
! rowspan="2" | File systems
! rowspan="2" | Notes
|-
! BIOS !! UEFI
! MBR !! GPT
|-
! Clover
|
|
|  ||
|
|
| Can emulate UEFI on legacy BIOS systems.
|-
! EFI boot stub
|
| 1
|  ||
|
|
| The kernel is a valid EFI executable which can be directly launched from UEFI or from another UEFI boot loader.
|-
! GRUB
|
| 3
|  ||
|
|
| Supports RAID, LUKS (but not Argon2 PBKDFs) and LVM (but not thin provisioned volumes). See GRUB for setup-specific limitations.
|-
! Limine
|
| 3
|  ||
|
|
|
|-
! rEFInd
|
|
|  ||
| 4
|
| Supports auto-detecting kernels and parameters without explicit configuration, and supports fastboot |-
! Syslinux
|
|
|  ||
|
|
| No support for certain file system features.Can only access the file system it was installed to.
|-
! systemd-boot
|
| 3
|  ||
| 4
|
| Can only launch binaries from the ESP it is installed to or from the Extended Boot Loader Partition (XBOOTLDR partition) on the same disk.Automatically detects unified kernel images placed in .
|-
! Unified kernel image
|
| 3
|  ||
|
|
| , a kernel, initramfs and kernel command line packed into EFI executable to be loaded directly from UEFI firmware or another boot loader.
|-
!
|
|
|  ||
|
|
| [https://www.gnu.org/software/grub/grub-legacy.html Discontinued in favor of GRUB.
|-
!
|
|
|  ||
|
|
| Discontinued due to limitations (e.g. with Btrfs, GPT, RAID, encryption).
|}

# While the binary can be signed for Secure Boot, it does no following verification, thus breaking the chain of trust.
# File system support is inherited from the firmware. The UEFI specification mandates support for the FAT12, FAT16 and FAT32 file systemsbut vendors can optionally add support for additional file systems; for example, the firmware in Apple Macs supports the HFS+ file system. If the firmware provides an interface for loading UEFI drivers on startup, then support for additional file systems can be added by loading (independently acquired) file system drivers.
# Supports mixed mode booting. I.e. it can boot a 64-bit x86_64 Linux kernel on 32-bit IA32 UEFI.
# A [https://www.rodsbooks.com/efi-bootloaders/principles.html boot manager. It can only launch other EFI applications, for example, Linux kernel images built with  and Windows Boot Manager ().
# Supports loading UEFI file system drivers.

See also Wikipedia:Comparison of boot loaders.

## Kernel
The boot loader boots the vmlinux image containing the kernel.

The kernel functions on a low level (kernelspace) interacting between the hardware of the machine and the programs. The kernel initially performs hardware enumeration and initialization before continuing to userspace. See Wikipedia:Kernel (operating system) and Wikipedia:Linux kernel for a detailed explanation.

## initramfs
An initramfs (''initial RAM file system) image is a cpio archive providing the necessary files for early userspace'' (see below) to successfully start the late userspace. This predominantly means all kernel modules, user space tools, associated libraries, supporting files like udev rules, etc. required to locate, access and mount the root file system. With the concept of initramfs it is possible to handle even more complex setups, like booting from an external drive, stacked devices (logical volumes, software RAIDs, compression, encryption) or running a tiny SSH server in early userspace for remote unlocking or maintenance tasks of the root file system.

The majority of modules will be loaded during later stages of the init process by udev after having switched root to the root file system.

The process is as follows:

# The root file system at  starts out as an empty rootfs, which is a special instance of tmpfs or ramfs. This is the temporary root file system where the initramfs images will be unpacked to.
# The kernel unpacks its builtin initramfs into the temporary root. Arch Linux's officially supported kernels use an empty archive for the builtin initramfs, which is the default when building Linux.
# The kernel unpacks external initramfs images in the order they are specified by the command line passed by the boot loader, overwriting any files from the embedded initramfs or previously unpacked files. Note that multiple initramfs images can be combined in a single file and the kernel will process them in their order in the file.
#* If the first initramfs image is uncompressed, after unpacking it, the kernel will look for CPU microcode updates and ACPI table updates in  and , respectively.
#* After processing the CPU microcode and ACPI table updates, the kernel will proceed to unpack the rest of the initramfs images, if any.

Initramfs images are Arch Linux' preferred method for setting up the early userspace and can be generated with mkinitcpio, dracut or booster.

## Running without initramfs
Since 6.13.8 officially supported kernels have Btrfs and Ext4 drivers built-in This makes it possible for the kernel to use a root partition with these file systems directly and load the rest of external modules needed from there. Although, there are some quirks to keep in mind:

* GPT partition automounting could not be used, so  kernel parameter is always required.
* Persistent block device naming for  is restricted to  and  only [https://github.com/torvalds/linux/blob/v6.14/block/early-lookup.c#L216-L243.
* Mount options for  are limited, e.g.  would not work To mitigate possible side effects, you could make the initial mount read-only using . Desired options could be applied later on remount via fstab.
*  is pointless without initramfs and has issues [https://github.com/systemd/systemd/issues/16953, disable it by setting .

Another thing you really need initramfs for is early microcode loading. But it is not necessary to build full image for that, Arch provides microcode in separate initramfs files, which could be used independently.

If no initramfs image is provided, the kernel always contains still an empty image to start from So there should be no issues with root partition [https://github.com/torvalds/linux/blob/1b907d0507354b74a4f2c286380cd6059af79248/fs/namespace.c#L4222 pinning.

## Early userspace
The early userspace stage, a.k.a. the initramfs stage, takes place in rootfs consisting of the files provided by the #initramfs. Early userspace starts by the kernel executing the  binary as PID 1.

The function of early userspace is configurable, but its main purpose is to bootstrap the system to the point where it can access the root file system. This includes:

*  loads kernel modules, such as any block device modules needed to mount the real root file system.
* Set up the storage stack where the root file system may be lying on, e.g. through dm-crypt, dm-verity, mdadm, LVM, systemd-repart, etc.
** Handle decryption of the real root file system, if applicable.
* Resolve the persistent block device names to real device through udev.
* Load the DRM module, as early KMS is enabled by default.

Note that the early userspace serves more than just setting up the root file system. There are tasks that can only be performed before the root file system is mounted, such as fsck and resuming from hibernation.

At the final stage of early userspace, the real root is mounted at  (in case of a systemd-based initramfs) or at  (in case of a busybox-based one), and then switched to by using  when using systemd-based initramfs or  when using busybox-based initramfs. The late userspace starts by executing the init program from the real root file system.

## Late userspace
The startup of late userspace is executed by the init process. Arch officially uses systemd which is built on the concept of units and services, but the functionality described here largely overlaps with other init systems.

## getty
The init process calls getty once for each virtual terminal (typically six of them). getty initializes each terminal and protects it from unauthorized access. When the username and password are provided, getty checks them against  and , then calls .

## Login
The login program begins a session for the user by setting environment variables and starting the user's shell, based on . The login program displays the contents of /etc/motd (message of the day) after a successful login, just before it executes the login shell. It is a good place to display your Terms of Service to remind users of your local policies or anything you wish to tell them.

## Shell
Once the user's shell is started, it will typically run a runtime configuration file, such as bashrc, before presenting a prompt to the user. If the account is configured to start X at login, the runtime configuration file will call startx or xinit. Jump to #Graphical session (Xorg) for the end.

## Display manager
Additionally, init can be configured to start a display manager instead of getty on a specific virtual terminal. This requires manually enabling its systemd service file. The display manager then starts a graphical session.

## Graphical session (Xorg)
xinit runs the user's xinitrc runtime configuration file, which normally starts a window manager or a desktop environment. When the user is finished and exits, xinit, startx, the shell, and login will terminate in that order, returning to getty or the display manager.
