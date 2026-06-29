# Dual boot with Windows

This is an article detailing different methods of Arch/Windows coexistence.

## Important information
## Windows UEFI vs BIOS limitations
Microsoft imposes limitations on which firmware boot mode and partitioning style can be supported based on the version of Windows used:

* Windows 8/8.1 and 10 x86 32-bit support booting in IA32 UEFI mode from GPT disk only, OR in BIOS mode from MBR disk only. They do not support x86_64 UEFI boot from GPT/MBR disk, x86_64 UEFI boot from MBR disk, or BIOS boot from GPT disk. On market, the only systems known to ship with IA32 (U)EFI are some old Intel Macs (pre-2010 models?) and Intel Atom System-on-Chip (Clover trail and Bay Trail) Windows Tablets, which boot ONLY in IA32 UEFI mode and ONLY from GPT disk.
* Windows 8/8.1 and 10 x86_64 versions support booting in x86_64 UEFI mode from GPT disk only, OR in BIOS mode from MBR disk only. They do not support IA32  UEFI boot, x86_64 UEFI boot from MBR disk, or BIOS boot from GPT disk.
* Windows 11 only supports x86_64 and a boot in UEFI mode from GPT disk.

In case of pre-installed systems, all systems pre-installed with Windows 8/8.1, 10 and 11 boot in UEFI/GPT mode. Up to Windows 10, the firmware bitness matches the bitness of Windows, ie. x86_64 Windows boot in x86_64 UEFI mode and 32-bit Windows boot in IA32 UEFI mode.

An easy way to detect the boot mode of Windows is to do the following* Boot into Windows
* Press  keys to start the Run dialog
* In the Run dialog type  and press Enter
* In the System Information windows, select System Summary on the left and check the value of BIOS mode item on the right
* If the value is , Windows boots in UEFI/GPT mode. If the value is , Windows boots in BIOS/MBR mode.

In general, Windows forces type of partitioning depending on the firmware mode used, i.e. if Windows is booted in UEFI mode, it can be installed only to a GPT disk. If Windows is booted in Legacy BIOS mode, it can be installed only to an MBR disk. This is a limitation enforced by Windows Setup, and as of April 2014 there is no officially (Microsoft) supported way of installing Windows in UEFI/MBR or BIOS/GPT configuration. Thus Windows only supports either UEFI/GPT boot or BIOS/MBR configuration.

Such a limitation is not enforced by the Linux kernel, but can depend on which boot loader is used and/or how the boot loader is configured. The Windows limitation should be considered if the user wishes to boot Windows and Linux from the same disk, since installation procedure of boot loader depends on the firmware type and disk partitioning configuration. In case where Windows and Linux dual boot from the same disk, it is advisable to follow the method used by Windows, ie. either go for UEFI/GPT boot or BIOS/MBR boot. See https://support.microsoft.com/kb/2581408 for more information.

## Boot loader UEFI vs BIOS limitations
Most of the Linux boot loaders installed for one firmware type cannot launch or chainload boot loaders of the other firmware type. That is, if Arch is installed in UEFI/GPT or UEFI/MBR mode in one disk and Windows is installed in BIOS/MBR mode in another disk, the UEFI boot loader used by Arch cannot chainload the BIOS installed Windows in the other disk. Similarly if Arch is installed in BIOS/MBR or BIOS/GPT mode in one disk and Windows is installed in UEFI/GPT in another disk, the BIOS boot loader used by Arch cannot chainload UEFI installed Windows in the other disk.

The only exceptions to this are GRUB in Apple Macs in which GRUB in UEFI mode can boot BIOS installed OS via  command (does not work in non-Apple systems), and rEFInd which technically supports booting legacy BIOS OS from UEFI systems, but [https://rodsbooks.com/refind/using.html#legacy does not always work in non-Apple UEFI systems as per its author Rod Smith.

However if Arch is installed in BIOS/GPT in one disk and Windows is installed in BIOS/MBR mode in another disk, then the BIOS boot loader used by Arch can boot the Windows in the other disk, if the boot loader itself has the ability to chainload from another disk.

Windows Setup creates a 100 MiB EFI system partition (except for Advanced Format 4K native drives where it creates a 300 MiB ESP), so multiple kernel usage is limited. Workarounds include:

* If you are installing Windows from scratch, you can dictate the size of the EFI system partition during installation.  See #The EFI system partition created by Windows Setup is too small
* Mount ESP to  and use a boot loader that has file system drivers and is capable of launching kernels that reside on other partitions.
* Reduce the size of the Windows partition and replace the existing ESP with a new, larger one.
* Backup and delete unneeded fonts in  * Backup and delete unneeded language directories in  (e.g. to only keep ).
* Use a higher, but slower, compression for the initramfs images making sure to decompress the loadable kernel modules and firmware. E.g.

 COMPRESSION="xz"
 COMPRESSION_OPTIONS=(-9e)
 MODULES_DECOMPRESS="yes"

## UEFI Secure Boot
All pre-installed Windows 8/8.1, 10 and 11 systems by default boot in UEFI/GPT mode and have UEFI Secure Boot enabled by default. This is mandated by Microsoft for all OEM pre-installed systems.

Arch Linux install media does not support Secure Boot yet. See Secure Boot#Booting an installation medium.

It is advisable to disable UEFI Secure Boot in the firmware setup manually before attempting to boot Arch Linux. Windows 8/8.1, 10 and 11 SHOULD continue to boot fine even if Secure boot is disabled. The only issue with regards to disabling UEFI Secure Boot support is that it requires physical access to the system to disable secure boot option in the firmware setup, as Microsoft has explicitly forbidden presence of any method to remotely or programmatically (from within OS) disable secure boot in all Windows 8/8.1 and above pre-installed systems

## Fast Startup and hibernation
There are two OSs that can be hibernated, you can hibernate Windows and boot Linux (or another OS), or you can hibernate Linux and boot Windows, or hibernate both OSs.

For the same reason, if you share one EFI system partition between Windows and Linux, then the EFI system partition may be damaged if you hibernate (or shutdown with Fast Startup enabled) Windows and then start Linux, or hibernate Linux and then start Windows. Check the respective section in EFI system partition for mitigation strategies.

 added a [https://sourceforge.net/p/ntfs-3g/ntfs-3g/ci/559270a8f67c77a7ce51246c23d2b2837bcff0c9/ safe-guard to prevent read-write mounting of hibernated NTFS filesystems, but the NTFS driver within the Linux kernel has no such safeguard.

Windows cannot read filesystems such as ext4 by default that are commonly used for Linux. These filesystems do not have to be considered, unless you install a Windows driver for them.

## Windows settings
Fast Startup is a feature in Windows 8 and above that hibernates the computer rather than actually shutting it down to speed up boot times.

There are multiple options regarding the Windows settings for Fast Startup and hibernation that are covered in the next sections.
* disable Fast Startup and disable hibernation
* disable Fast Startup and enable hibernation
* enable Fast Startup and enable hibernation

The procedure of disabling Fast Startup is described in the tutorials for Windows 8, Windows 10 and Windows 11. In any case if you disable a setting, make sure to disable the setting and then shut down Windows, before installing Linux; note that rebooting is not sufficient.

## Disable Fast Startup and disable hibernation
This is the safest option, and recommended if you are unsure about the issue, as it requires the least amount of user awareness when rebooting from one OS into the other. You may share the same EFI system partition between Windows and Linux.

In a Windows command-line shell with administrator privileges:

 > powercfg /H off

## Disable Fast Startup and enable hibernation
This option requires user awareness when rebooting from one OS into the other.
If you want to start Linux while Windows is hibernated, which is a common use case, then
* you must use a separate EFI system partition (ESP) for Windows and Linux, and ensure that Windows does not mount the ESP used for Linux. As there can only be one ESP per drive, the ESP used for Linux must be located on a separate drive than the ESP used for Windows. In this case Windows and Linux can still be installed on the same drive in different partitions, if you place the ESP used by linux on another drive than the Linux root partition.
* you can not read-write mount any filesystem in Linux, that is mounted by Windows while Windows is hibernated. You should be extremely careful about this, and also consider Automount behaviour.
* If you shut down Windows fully, rather than hibernating, then you can read-write mount the filesystem.

## Enable Fast Startup and enable hibernation
The same considerations apply as in case "Disable Fast Startup and enable hibernation", but since Windows can not be shut down fully, only hibernated, you can never read-write mount any filesystem that was mounted by Windows while Windows is hibernated.

## Windows filenames limitations
Windows is limited to filepaths being shorter than 260 characters.

Windows also puts certain characters off limits in filenames for reasons that run all the way back to DOS:

*  (greater than)
*  (colon)
*  (double quote)
*  (forward slash)
*  (backslash)
*  (vertical bar or pipe)
*  (question mark)
*  (asterisk)

These are limitations of Windows and not NTFS: any other OS using the NTFS partition will be fine. Windows will fail to detect these files and running  will most likely cause them to be deleted. This can lead to potential data-loss.

NTFS-3G applies Windows restrictions to new file names through the  option:  (see fstab).

## Installation
The recommended way to set up a Linux/Windows dual booting system is to first install Windows, only using part of the disk for its partitions. When you have finished the Windows setup, boot into the Linux install environment where you can create and resize partitions for Linux while leaving the existing Windows partitions untouched. The Windows installation will create the EFI system partition which can be used by your Linux boot loader. If you are installing Windows from scratch, do note that the EFI System partition created by Windows Setup will be too small for most use cases. See #The EFI system partition created by Windows Setup is too small.

## Windows before Linux
If you already have Windows installed, it will already have created some partitions on a GPT-formatted disk:

* a Windows Recovery Environment partition, generally of size 499 MiB,
* an EFI system partition with a FAT32 filesystem, containing the Windows Boot Manager,
* a Microsoft Reserved Partition, generally of size 128 MiB,
* a Microsoft basic data partition with a NTFS filesystem, which corresponds to ,
* potentially system recovery and backup partitions and/or secondary data partitions (corresponding often to  and above).

Using the Disk Management utility in Windows, check how the partitions are labelled and which type gets reported. The Reserved Partition may not be visible in the Disk Management utility in which case it can be identified using diskpart in windows cmd.  This will help you understand which partitions are essential to Windows, and which others you might repurpose. The Windows Disk Management utility can also be used to shrink Windows (NTFS) partitions to free up disk space for additional partitions for Linux.

You can then proceed with partitioning, depending on your needs. The boot loader needs to support chainloading other EFI applications to dual boot Windows and Linux. An additional EFI system partition should not be created, as it may prevent Windows from booting.

Simply mount the existing partition.

Computers that come with newer versions of Windows often have Secure Boot enabled. You will need to take extra steps to either disable Secure Boot or to make your installation media compatible with secure boot (see above and in the linked page).

## Linux before Windows
Even though the recommended way to set up a Linux/Windows dual booting system is to first install Windows, it can be done the other way around. In contrast to installing Windows before Linux, you will have to set aside a partition for Windows, say 40GB or larger, in advance. Or have some unpartitioned disk space, or create and resize partitions for Windows from within the Linux installation, before launching the Windows installation.

Windows will use the already existing EFI system partition.
Follows an outline, assuming Secure Boot is disabled in the firmware.

# Boot into windows installation. Watch to let it use only the intended partition, but otherwise let it do its work as if there is no Linux installation.
# Follow the #Fast Startup and hibernation section.
# Fix the ability to load Linux at start up, perhaps by following #Cannot boot Linux after installing Windows. It was already mentioned in #Windows before Linux that some Linux boot managers will autodetect Windows Boot Manager. Even though newer Windows installations have an advanced restart option, from which you can boot into Linux, it is advised to have other means to boot into Linux, such as an arch installation media or a live CD.

## Windows 10 with GRUB
The following assumes GRUB is used as a boot loader (although the process is likely similar for other boot loaders) and that Windows 10 will be installed on a GPT block device with an existing EFI system partition (see the "System partition" section in the Microsoft documentation for more information).

Create with program  on the block device the following three new partitions. See for more precise partition sizes.

{| class="wikitable"
! Min size !! Code !! Name !! File system
|-
| 16 MB || 0C01 || Microsoft reserved || N/A
|-
| ~40 GB || 0700 || Microsoft basic data || NTFS
|-
| 300 MB || 2700 || Windows RE || NTFS
|-
|}

Create NTFS file systems on the new Microsoft basic data and Windows RE (recovery) partitions using the mkntfs program from package .

Reboot the system into a Windows 10 installation media. When prompted to install select the custom install option and install Windows on the Microsoft basic data partition created earlier. This should also install Microsoft EFI files in the EFI system partition.

After installation (set up of and logging into Windows not required), reboot into Linux and generate a GRUB configuration for the Windows boot manager to be available in the GRUB menu on next boot.

## Troubleshooting
## Could not create a new partition or locate an existing one
See #Windows UEFI vs BIOS limitations.

## Cannot boot Linux after installing Windows
See Unified Extensible Firmware Interface#Windows changes boot order.

## Restoring an accidentally deleted EFI system partition
If you have a GPT-partitioned disk and erased (e.g. with ) the EFI system partition, you will notice that Windows Boot Manager will either disappear from your boot options, or selecting it will send you back to the UEFI.

To remedy it, boot with a Windows installation media, press  to open the console (or click NEXT > Repair Computer > Troubleshoot... > Advanced > Command Prompt), then start the diskpart utility:

 X:\Sources> diskpart
 DISKPART> list disk

Select the appropriate hard drive by typing:

 DISKPART> select disk number

Make sure that there is a partition of type system (the EFI system partition):

 DISKPART> list partition

Select this partition:

 DISKPART> select partition number

and assign a temporary drive letter to it:

To make sure that drive letter is correctly assigned:

Close diskpart:

 DISKPART> exit

Navigate to  (or what your system drive letter is):

 X:\Sources> cd /d C:\

Next is the "magic" command, which recreate the BCD store (with  for the mount point,  for firmware type, optionally add  for verbose):

 C:\> bcdboot C:\Windows /s G: /f UEFI

You should now have Windows Boot Manager working as a boot option, and thus have access to Windows. Just make sure to never format your EFI system partition again!

See [https://www.reddit.com/r/archlinux/comments/yprrhr/guide_what_to_do_if_you_accidentally_format_your/, and [https://superuser.com/a/1507645.

## The EFI system partition created by Windows Setup is too small
By default, Windows Setup creates a 100 MiB EFI system partition (except for Advanced Format 4K native drives where it creates a 300 MiB ESP). This is generally too small to fit everything you need. You can replace the existing EFI system partition with a new, larger one.

If you are installing Windows from scratch, you can dictate the size of the EFI system partition during installation# Select your installation target and make sure it has no partitions.
# Click New and then the Apply buttons.  The Windows installer will then generate the expected partitions (allocating nearly everything to its primary partition) and just 100MB to the EFI.
# Use the UI to delete the , , and  partitions. Leave the  partition (if present) alone.
# Press  to open the Command Prompt.
# Type  and press  to open the disk partitioning tool.
# Type  and press  to list your disks.  Find the one you intend to modify and note its disk number.
# Type  with the disk number to modify.
# Type  with the desired size of the ESP in Mebibytes (MiB), and press . See the note at EFI system partition#Create the partition for the recommended sizes.
# Type  and press  to format the ESP
# Type  and press  to exit the disk partitioning tool and  followed by  again.

Once Windows is installed, you can resize the primary partition down within Windows and then reboot and go about your usual Arch install, filling the space you just created.

Alternatively, you can use the Arch install media to create a single EFI system partition of your preferred size before you install Windows on the drive. Windows Setup will use the EFI system partition you made instead of creating its own.

## Unable to install Windows Cumulative Update on BIOS system
On BIOS systems, Windows cumulative updates may fail with the error We couldn’t complete the updates. Undoing changes. Don’t turn off your computer. In such case, while in Windows, you need to set the [https://superuser.com/a/1405702 Windows partition as active.

 C:\> diskpart
 DISKPART> list disk
 DISKPART> select disk number
 DISKPART> list partition
 DISKPART> select partition number
 DISKPART> active
 DISKPART> exit

After successfully installing the Windows update, mark back your Linux partition as active, using the commands above.

## Time standard
* Recommended: Set both Arch Linux and Windows to use UTC, following System time#UTC in Microsoft Windows. Some versions of Windows revert the hardware clock back to localtime if they are set to synchronize the time online. This issue appears to be fixed in Windows 10.
* Not recommended: Set Arch Linux to localtime and disable all time synchronization daemons. This will let Windows take care of hardware clock corrections and you will need to remember to boot into Windows at least two times a year (in Spring and Autumn) when DST kicks in. So please do not ask on the forums why the clock is one hour behind or ahead if you usually go for days or weeks without booting into Windows.

## Bluetooth pairing
When it comes to pairing Bluetooth devices with both the Linux and Windows installation, both systems have the same MAC address, but will use different link keys generated during the pairing process. This results in the device being unable to connect to one installation, after it has been paired with the other. To allow a device to connect to either installation without re-pairing, follow Bluetooth#Dual boot pairing.
