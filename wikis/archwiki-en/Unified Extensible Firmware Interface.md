# Unified Extensible Firmware Interface

The Unified Extensible Firmware Interface (UEFI) is an interface between operating systems and firmware. It provides a standard environment for booting an operating system and running pre-boot applications.

It is distinct from the MBR boot code method that was used by legacy BIOS systems. See Arch boot process for their differences and the boot process using UEFI. To set up UEFI boot loaders, see Arch boot process#Boot loader.

## UEFI firmware bitness
Under UEFI, every program whether it is an operating system loader or a utility (e.g. a memory testing or recovery tool), should be an EFI application corresponding to the UEFI firmware bitness/architecture.

The vast majority of x86_64 systems, including recent Apple Macs, use x64 (64-bit) UEFI firmware. The only known devices that use IA32 (32-bit) UEFI are older (pre 2008) Apple Macs, Intel Atom System-on-Chip systems (as on 2 November 2013)and some older Intel server boards that are known to operate on Intel EFI 1.10 firmware.

An x64 UEFI firmware does not include support for launching 32-bit EFI applications (unlike x86_64 Linux and Windows versions which include such support). Therefore the EFI application must be compiled for that specific firmware processor bitness/architecture.

## Checking the firmware bitness
The firmware bitness can be checked from a booted operating system.

## From Linux
On distributions running Linux kernel 4.0 or newer, the UEFI firmware bitness can be found via the sysfs interface. Run:

 $ cat /sys/firmware/efi/fw_platform_size

It will return  for a 64-bit (x64) UEFI or  for a 32-bit (IA32) UEFI. If the file does not exist, you have not booted in UEFI mode.

## From macOS
Pre-2008 Macs mostly have IA32 EFI firmware while >=2008 Macs have mostly x64 EFI. All Macs capable of running Mac OS X Snow Leopard 64-bit Kernel have x64 EFI 1.x firmware.

To find out the arch of the EFI firmware in a Mac, type the following into the Mac OS X terminal:

 $ ioreg -l -p IODeviceTree | grep firmware-abi

If the command returns , it is IA32 (32-bit) EFI firmware. If it returns , it is x64 EFI firmware. Most of the Macs do not have UEFI 2.x firmware as Apple's EFI implementation is not fully compliant with UEFI 2.x specification.

## From Microsoft Windows
64-bit versions of Windows do not support booting on a 32-bit UEFI. So, if you have a 32-bit version of Windows booted in UEFI mode, you have a 32-bit UEFI.

To check the bitness run . In the System Summary section look at the values of "System Type" and "BIOS mode".

For 64-bit Windows on a 64-bit UEFI, it will be  and . For 32-bit Windows on a 32-bit UEFI— and . If the "BIOS mode" is not , Windows is not booted in UEFI mode.

## UEFI variables
UEFI defines variables through which an operating system can interact with the firmware. UEFI boot variables are used by the boot loader and used by the operating system only for early system start-up. UEFI runtime variables allow an operating system to manage certain settings of the firmware like the UEFI boot manager or managing the keys for UEFI Secure Boot protocol etc. You can get the list using:

 $ efivar --list

## UEFI variables support in Linux kernel
Linux kernel exposes UEFI variables data to userspace via efivarfs (EFI VARiable FileSystem) interface () - mounted using  kernel module at  - it has no maximum per-variable size limitation and supports UEFI Secure Boot variables. Introduced in kernel 3.8.

## Requirements for UEFI variable support
# Kernel should be booted in UEFI mode via the EFI boot stub (optionally using a boot manager) or by a UEFI boot loader, not via BIOS or CSM (Compatibility Support Module), or Apple's Boot Camp which is also a CSM.
# EFI Runtime Services support should be present in the kernel (, check if present with ).
# EFI Runtime Services in the kernel should not be disabled via the kernel command line, i.e.  kernel parameter should not be used.
#  filesystem should be mounted at , otherwise follow #Mount efivarfs section below.
#  should list (option /) the UEFI variables without any error.

If UEFI Variables support does not work even after the above conditions are satisfied, try the below workarounds:

# If listing of the UEFI variables () leads to  and the system is booted into a realtime kernel, add  to the kernel parameters and reboot (efivarfs functionality is disabled by default on those kernels).
# See #Userspace tools are unable to modify UEFI variable data for more troubleshooting steps

## Mount efivarfs
If  is not automatically mounted at  by systemd during boot, you need to manually mount it to expose UEFI variables to userspace tools like efibootmgr:

 # mount -t efivarfs efivarfs /sys/firmware/efi/efivars

See [https://docs.kernel.org/filesystems/efivarfs.html efivarfs.html for kernel documentation.

## Userspace tools
There are few tools that can access/modify the UEFI variables, namely

*
*
*
*
*
*

## efibootmgr
You will have to install the  package.

To add a new boot option using efibootmgr, you need to know three things:

# The disk containing the EFI system partition (ESP). E.g.: , .
# The partition number of the ESP on that disk. The  in  or .
# The path to the EFI application (relative to the root of the ESP)

For example, if you want to add a boot option for  where  is the mount point of the ESP, run

In this example,  indicates that the ESP is on disk  and has partition number 1. The path to the EFI application relative to the root of the ESP is . So you would create the boot entry as follows:

 # efibootmgr --create --disk /dev/sda --part 1 --loader '\EFI\refind\refind_x64.efi' --label 'rEFInd Boot Manager' --unicode

Get an overview of all boot entries and the boot order:

 # efibootmgr --unicode

To set the boot order:

 # efibootmgr --bootorder XXXX,XXXX --unicode

Where XXXX is the number that appears in the previous output of efibootmgr command.

Delete an unwanted entry:

 # efibootmgr --delete-bootnum --bootnum XXXX --unicode

See  or efibootmgr README for more info.

## Disable UEFI variable access
Access to the UEFI can potentially cause harm beyond the running operating system level. There are dangerous UEFI exploits like LogoFAIL which allows a malicious actor to take full control over the machine. Even hardware-level bricking is possible in some cases of poor UEFI implementation So, as the UEFI variables access is not required for daily system usage, you may want to disable it, to avoid potential security breaches or accidental harm.

Possible solutions are:

* Mount  in read-only mode using fstab. For example:
* Use the  kernel parameter to completely disable OS access to UEFI.

## UEFI Shell
The UEFI Shell is a shell/terminal for the firmware which allows launching EFI applications which include UEFI boot loaders. Apart from that, the shell can also be used to obtain various other information about the system or the firmware like memory map (memmap), modifying boot manager variables (bcfg), running partitioning programs (diskpart), loading UEFI drivers, editing text files (edit), hexedit etc.

## Obtaining UEFI Shell
You can obtain a BSD licensed UEFI Shell from the TianoCore EDK2 project:

* Shell v2:
** On the Arch install medium: . A copy of  from the time the ISO was built.
**  provides UEFI Shells for x64 (x86_64), AA64 (AArch64 a.k.a. ARM64) and RISCV64 (RISC-V 64-bit) UEFI architectures - compiled directly from latest TianoCore EDK2 release.
**  provides x64 Shell for x64 (64-bit) UEFI and IA32 Shell for IA32 (32-bit) UEFI - compiled directly from latest TianoCore EDK2 source.
* Shell v1:
** [https://github.com/tianocore/edk2/tree/UDK2018/EdkShellBinPkg Precompiled UEFI Shell v1 binaries from TianoCore (not updated anymore upstream as of Jan 10, 2014).
* Patched shells:
** Precompiled UEFI Shell v2 binary with bcfg modified to work with UEFI pre-2.3 firmware - from Clover EFI boot loader.
** Precompiled UEFI Shell v2 binary for compatibility with a broad range of firmwares - from the OpenCore boot loader. In the release archive: .

Shell v2 works best in UEFI 2.3+ systems and is recommended over Shell v1 in those systems. Shell v1 should work in all UEFI systems irrespective of the spec. version the firmware follows. More information at ShellPkg and the EDK2 mailing list thread—Inclusion of UEFI shell in Linux distro iso.

## Launching UEFI Shell
Few Asus and other AMI Aptio x64 UEFI firmware based motherboards (from Sandy Bridge onwards) provide an option called Launch EFI Shell from filesystem device. For those motherboards, copy the x64 UEFI Shell to the root of your EFI system partition, named as .

Systems with Phoenix SecureCore Tiano UEFI firmware is known to have embedded UEFI Shell which can be launched using either ,  or  key.

## Important UEFI Shell commands
UEFI Shell commands usually support  option which makes output pause after each page. Run  to list available internal commands. Available commands are either built into the shell or discrete EFI applications.

For more info see Intel Scripting Guide 2008 and Intel "Course" 2011.

## bcfg
bcfg modifies the UEFI NVRAM entries which allows the user to change the boot entries or driver options. This command is described in detail in page 96 (Section 5.3) of the UEFI Shell Specification 2.2 document.

To dump a list of current boot entries:

 Shell> bcfg boot dump -v

To add a boot menu entry for rEFInd (for example) as 4th (numbering starts from zero) option in the boot menu:

 Shell> bcfg boot add 3 FS0:\EFI\refind\refind_x64.efi "rEFInd Boot Manager"

where  is the mapping corresponding to the EFI system partition and  is the file to be launched.

To add an entry to boot directly into your system without a boot loader, see EFI boot stub#bcfg.

To remove the 4th boot option:

 Shell> bcfg boot rm 3

To move the boot option #3 to #0 (i.e. 1st or the default entry in the UEFI Boot menu):

 Shell> bcfg boot mv 3 0

For bcfg help text:

 Shell> help bcfg -v -b

or:

 Shell> bcfg -? -v -b

## map
 displays a list of device mappings i.e. the names of available file systems () and storage devices ().

Before running file system commands such as  or , you need to change the shell to the appropriate file system by typing its name:

 Shell> FS0:
 FS0:\> cd EFI/

## edit
 provides a basic text editor with an interface similar to nano, but slightly less functional. It handles UTF-8 encoding and takes care or LF vs CRLF line endings.

For example, to edit rEFInd's  in the EFI system partition ( in the firmware),

 Shell> edit FS0:\EFI\refind\refind.conf

Press  for help.

## UEFI drivers
UEFI drivers are pieces of software that support some functionality. For example, access to NTFS formatted partitions is usually not possible from a UEFI shell. The  package has drivers that support reading many more file systems from within an EFI shell. A usage example is to copy such driver to a partition that can be accessed from an UEFI shell. Then, from the UEFI shell, issuing commands such as:

 Shell> load ntfs_x64.efi
 Shell> map -r

After the map command has been executed, the user should be able to access NTFS formatted partitions from within a UEFI shell.

## UEFI bootable media
## Remove UEFI boot support from optical media
Most of the 32-bit EFI Macs and some 64-bit EFI Macs refuse to boot from a UEFI(X64)+BIOS bootable CD/DVD. If one wishes to proceed with the installation using optical media, it might be necessary to remove UEFI support first.

Extract the ISO skipping the UEFI-specific directories:

 $ mkdir extracted_iso
 $ bsdtar -x --exclude=EFI/ --exclude=loader/ -f archlinux-version-x86_64.iso -C extracted_iso

Then rebuild the ISO, excluding the UEFI optical media booting support, using  from . Be sure to set the correct volume label, e.g. ; it can be acquired using  on the original ISO.

Burn  to optical media and proceed with installation normally.

## Testing UEFI in systems without native support
## OVMF for virtual machines
OVMF is a TianoCore project to enable UEFI support for Virtual Machines. OVMF contains a sample UEFI firmware and a separate non-volatile variable store for QEMU.

You can install  from the extra repository.

It is advised to make a local copy of the non-volatile variable store for your virtual machine:

 $ cp /usr/share/edk2/x64/OVMF_VARS.4m.fd my_OVMF_VARS.4m.fd

To use the OVMF firmware and this variable store, add following to your QEMU command:

 -drive if=pflash,format=raw,readonly,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
 -drive if=pflash,format=raw,file=my_OVMF_VARS.4m.fd

For example:

 $ qemu-system-x86_64 -enable-kvm -m 1G -drive if=pflash,format=raw,readonly,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd -drive if=pflash,format=raw,file=my_OVMF_VARS.4m.fd …

## DUET for BIOS only systems
DUET was a TianoCore project that enabled chainloading a full UEFI environment from a BIOS system, in a way similar to BIOS operating system booting. This method is being discussed extensively. Pre-build DUET images can be downloaded from one of the repos. Read specific instructions for setting up DUET. However, as of November 2018, the DUET code has been removed from TianoCore git repository.

You can also try Clover which provides modified DUET images that may contain some system specific fixes and is more frequently updated compared to the gitlab repos.

## Troubleshooting
## Boot back to Arch Linux when stuck with Windows
To boot back into Arch Linux when you are stuck with Windows, reach Advanced startup in Windows by the Windows PowerShell command , or via Settings > Update & Security > Recovery > Advanced startup and select Restart now. When you have reached the Advanced startup menu, choose Use a device, which actually contains your UEFI boot options (not limited to USB or CD, but can also boot operating system in hard drive), and choose "Arch Linux".

## Enter firmware setup without function keys
On some laptops, like Lenovo XiaoXin 15are 2020, using keys like  or  does not do anything. This can possibly be fixed by returning laptops to OEM to repair mainboard information, but sometimes this is not possible or not desired. There are however other means to enter firmware setup:

* With systemctl:  This will reboot your computer to firmware setup.
* With GRUB: Press  for command line and in GRUB command line use  to enter firmware setup.
* In Windows: Enter Advanced Startup, see #Boot back to Arch Linux when stuck with Windows.

## Userspace tools are unable to modify UEFI variable data
If any userspace tool is unable to modify UEFI variable data, check for existence of  files. If they exist, delete them, reboot and retry again.
If the above step does not fix the issue, try booting with  kernel parameter to disable kernel UEFI variable storage space check that may prevent writing/modification of UEFI variables.

## Cannot create a new boot entry with efibootmgr
Some kernel and efibootmgr version combinations might refuse to create new boot entries. This could be due to lack of free space in the NVRAM. You can try the solution at #Userspace tools are unable to modify UEFI variable data.

You can also try to downgrade your efibootmgr install to version 0.11.0. This version works with Linux version 4.0.6. See the bug discussion , in particular the closing comment, for more information.

## Windows changes boot order
If you dual boot with Windows and your motherboard just boots Windows immediately instead of your chosen EFI application, there are several possible causes and workarounds.

* Ensure Fast Startup is disabled in your Windows power options
* Ensure Secure Boot is disabled in your firmware (if you are not using a signed boot loader)
* Ensure your UEFI boot order does not have Windows Boot Manager set first e.g. using efibootmgr and what you see in the configuration tool of the UEFI. Some motherboards override by default any settings set with efibootmgr by Windows if it detects it. This is confirmed in a Packard Bell laptop.
* If your motherboard is booting the default boot path (), this file may have been overwritten with the Windows boot loader. Try setting the correct boot path e.g. using efibootmgr.
* If the previous steps do not work, you can tell the Windows boot loader to run a different EFI application. From a Windows administrator command prompt {{ic|bcdedit /set "{bootmgr}" path "\EFI\path\to\app.efi"}}
* Alternatively, deactivate the Windows Boot Manager by running  as root. Replace  with the actual Windows Boot Manager boot number; you can see it by running  with no options.
* Alternatively, you can set a startup script in Windows that ensures that the boot order is set correctly every time you boot Windows.
*# Open a command prompt with administrator privileges. Run  and find your desired boot entry.
*# Copy the identifier, including the brackets, e.g. {{ic|{31d0d5f4-22ad-11e5-b30b-806e6f6e6963}}}
*# Create a batch file with the command {{ic|bcdedit /set "{fwbootmgr}" DEFAULT "{copied-boot-identifier}"}}
*# Open gpedit.msc and under Local Computer Policy > Computer Configuration > Windows Settings > Scripts (Startup/Shutdown), choose Startup
*# Under the Scripts tab, choose the Add button, and select your batch file
:: Note: Windows 10 Home does not officially include gpedit.msc, although there are unsupported workarounds to install it manually.
* Alternatively, Task Scheduler can be used to run a startup script in Windows:
*# Follow steps 1-3 above to create the batch file.
*# Run taskschd.msc, then choose Create Task... from the Action menu.
*# On the General tab:
*#: Enter any suitable Name and Description.
*#: Ensure the user account selected is an "Administrator", not a "Standard User".
*#: Select "Run whether user is logged in or not".
*#: Select "Run with highest privileges".
*# On the Triggers tab, choose "At startup" from the menu, then click OK.
*# On the Actions tab, click New..., then Browse..., and locate the batch file from step 1.
*# On the Conditions tab, untick the Power options so the script runs when on battery power (for laptops).
*# Click OK, and enter the password of the user account selected in step 4 when prompted.

## USB media gets struck with black screen
This issue can occur due to KMS issue. Try disabling KMS while booting the USB.

## UEFI boot loader does not show up in firmware menu
Some firmware do not support custom boot entries. They will instead only boot from hardcoded boot entries.

A typical workaround is to not rely on boot entries in the NVRAM and install the boot loader to one of the common fallback paths on the EFI system partition.

The following sections describe the fallback paths.

## Default boot path for removable drives
The UEFI specification defines default file paths for EFI binaries for booting from removable media. The relevant ones are:

*  for x64 UEFI
*  for IA32 UEFI.

While the specification defines these for removable drives only, most firmware support booting these from any drive.

See the appropriate boot loader article on how to install or migrate the boot loader to the default/fallback boot path.

## Microsoft Windows boot loader location
On certain UEFI motherboards like some boards with an Intel Z77 chipset, adding entries with  or  from the UEFI Shell will not work because they do not show up on the boot menu list after being added to NVRAM.

This issue is caused because the motherboards can only load Microsoft Windows. To solve this you have to place the .efi file in the location that Windows uses.

Copy the  file from the Arch Linux installation medium () to the Microsoft directory your ESP partition on your hard drive (). Do this by booting into EFI shell and typing:

 Shell> mkdir FS1:\EFI\Microsoft
 Shell> mkdir FS1:\EFI\Microsoft\Boot
 Shell> cp FS0:\EFI\BOOT\BOOTx64.EFI FS1:\EFI\Microsoft\Boot\bootmgfw.efi

After reboot, any entries added to NVRAM should show up in the boot menu.

## UEFI/BIOS is stuck on loading screen
This is a recurring problem with Acer laptops, which occurs if  files have not been manually authorized. See  Laptop/Acer#Firmware Setup became inaccessible after Linux installation.

## Boot entries created with efibootmgr fail to show up in UEFI
efibootmgr can fail to detect EDD 3.0 and as a result create unusable boot entries in NVRAM. See efibootmgr issue 86 for the details.

To work around this, when creating boot entries manually, add the  option to the efibootmgr command. E.g.

 # efibootmgr --create --disk /dev/sda --part 1 --loader '\EFI\refind\refind_x64.efi' --label 'rEFInd Boot Manager' --unicode -e 3

To fix boot loader installers, like  and , create a wrapper script  and make it executable:

## UEFI boot entry disappears after removing its referenced drive
Some firmware will remove boot entries referencing drives that are not present during boot. This could be an issue when frequently detaching/attaching drives or when booting from a removable drive.

The solution is to install the boot loader to the default/fallback boot path.

## Boot entries are randomly removed
Some motherboards may remove boot entries due to lack of free space in the NVRAM instead of giving an error at creation. To prevent this from occurring, reduce the amount of boot entries being added by minimizing your entry creation process, as well as reducing the amount of automatic drive boot entries by the Compatibility Support Module (CSM) by disabling it from your UEFI settings. See BBS#1608838.

Another reason why boot entries might have been removed is the fact that UEFI specification allows OEMs to do "NVRAM maintenance" during boot process. Those manufacturers do it simply: they just look up for EFI applications in predefined, hardcoded paths on the device. If they fail to find any, they conclude there is no operating system on the device and wipe all boot entries from NVRAM associated with it, because they assume the NVRAM contains some corrupted or outdated data. If you do not plan to install Windows and still want to load the Linux kernel directly from the firmware, one possible workaround is to create an empty file :

 # mkdir -p esp/EFI/BOOT
 # touch esp/EFI/BOOT/BOOTx64.EFI

And restore the deleted boot entry. Now after reboot the motherboard will see the "Fake OS" and should not wipe other boot entries from NVRAM. You can change the fake operating system loader with an actual EFI application if you want, of course, as long as you keep the standard fallback name.

## Lenovo ThinkPad: boot entries not persistent due to "OS Optimized Defaults"
On recent Lenovo ThinkPad laptops (e.g. T16 Gen 2 AMD models), users report that custom UEFI boot entries (created with  or ) are automatically deleted at each boot, with only Windows Boot Manager and Lenovo’s own entries (PXE, Recovery, Diagnostics) restored.

This is caused by the BIOS option "Restart / OS Optimized Defaults", which resets the UEFI boot variables at each reboot to defaults optimized for Windows.

Solution: Disable "OS Optimized Defaults" in the BIOS/UEFI setup. After doing so, manually created boot entries persist correctly, allowing systemd-boot or other custom boot managers to work as intended.
