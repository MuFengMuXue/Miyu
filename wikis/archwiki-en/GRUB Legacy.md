# GRUB Legacy

GRUB Legacy is a multiboot boot loader previously maintained by the GNU Project. It was derived from GRUB, the GRand Unified Bootloader, which was originally designed and implemented by Erich Stefan Boleyn.

Briefly, the boot loader is the first software program that runs when a computer starts. It is responsible for loading and transferring control to the Linux kernel. The kernel, in turn, initializes the rest of the operating system.

## Supported file systems
GRUB legacy bundles its own support for multiple file systems, notably FAT32, ext2, ReiserFS or XFS (although v4 only).

## Installation
GRUB Legacy can be installed from the  package.

Additionally, GRUB must be installed to the boot sector of a drive or partition to serve as a boot loader. This is covered in #Boot loader installation.

## Configuration
The configuration file is located at . Edit this file to suit your needs.

*  -- time to wait (in seconds) before the  operating system is automatically loaded.
*  -- the default boot entry that is chosen when the  has expired.

An example configuration (with  on a separate partition) is provided with the package.

## Finding GRUB's root
GRUB must be told where its files reside on the system, since multiple instances may exist (i.e., in multi-boot environments). GRUB files always reside under , which may be on a dedicated partition.

If you are unaware of the location of , use the GRUB shell  command to locate the GRUB files. Enter the GRUB shell as root by:

 # grub

The following example is for systems without a separate  partition, wherein  is merely a directory under :

 grub> find /boot/grub/stage1

The following example is for systems with a separate  partition:

 grub> find /grub/stage1

GRUB will find the file, and output the location of the  file. For example:

This value should be entered on the  line in your configuration file. Type  to exit the shell.

## Dual booting with Windows
Add the following to the end of your  (assuming that your Windows partition is on the first partition of the first drive):

If Windows is located on another hard disk, the  command must be used. This will make your Windows install think it is actually on the first drive. Assuming that your Windows partition is on the first partition of the second drive:

## Dual booting with GNU/Linux
This can be done the same way that an Arch Linux install is defined. For example:

## chainloader and configfile
To facilitate system maintenance, the  or  command should be used to boot another Linux distribution that provides an "automagic" GRUB configuration mechanism (e.g. Debian, Ubuntu, openSUSE). This allows the distribution to manage its own  and boot options.

* The  command will load another boot loader (rather than a kernel image); useful if another boot loader is installed in a partition's boot sector (GRUB, for example). This allows one to install a "main" instance of GRUB to the MBR and distribution-specific instances of GRUB to each partition boot record (PBR).

* The  command will instruct the currently running GRUB instance to load the specified configuration file. This can be used to load another distribution's  without a separate GRUB installation. The caveat of this approach is that other  may not be compatible with the installed version of GRUB; some distributions heavily patch their versions of GRUB.

For example, GRUB is to be installed to the MBR and some other boot loader (be it GRUB or LILO) is already installed to the boot sector of .

 ---------------------------------------------
 |   |           |           |   %           |
 | M |           |           | B %           |
 | B |  (hd0,0)  |  (hd0,1)  | L %  (hd0,2)  |
 | R |           |           |   %           |
 |   |           |           |   %           |
 ---------------------------------------------
   |                           ^
   |       chainloading        |
   -----------------------------

One can simply include in :

 title Other Linux
 root (hd0,2)
 chainloader +1

Or, if the boot loader on  is GRUB:

 title Other Linux
 root (hd0,2)
 configfile /boot/grub/menu.lst

The  command can also be used to load the MBR of a second drive:

 title Other drive
 rootnoverify (hd1)
 chainloader +1

## Dual booting with GNU/Linux (GRUB2)
If the other Linux distribution uses GRUB2 (e.g. Ubuntu 9.10+), and you installed its boot loader to its root partition, you can add an entry like this one to your :

Selecting this entry at boot will load the other distribution's GRUB2 menu assuming that the distribution is installed on .

## Boot loader installation
## Manual recovery of GRUB libs
The  files are expected to be in , which may not be the case if the boot loader was not installed during system installation or if the partition/filesystem was damaged, accidentally deleted, etc.

Manually copy the GRUB libs like so:
 # cp -a /usr/lib/grub/i386-pc/* /boot/grub

## General notes about boot loader installation
GRUB may be installed from a separate medium (e.g. a LiveCD), or directly from a running Arch install. GRUB is seldom required to be reinstalled and installation is not necessary when:

* The configuration file is updated.
* The  package is updated.

Installation is necessary when:

* A boot loader is not already installed.
* Another operating system overwrites the Linux boot loader.
* The boot loader fails for some unknown reason.

Before continuing, a few notes:

* Be sure that your GRUB configuration is correct () before proceeding. Refer to Finding GRUB's root to ensure your devices are defined correctly.
* GRUB must be installed on the MBR (first sector of the hard disk), or the first partition of the first storage device to be recognized by most BIOSes. To allow individual distributions the ability to manage their own GRUB menus, multiple instances of GRUB can be used, see #chainloader and configfile.
* Installing GRUB may need to be done from within a ed environment (i.e. from installed environment via a separate medium) for cases like RAID configurations or if you forgot/broke your GRUB installation. You will need to Change root from a LiveCD or another Linux installation to do so.

First, enter the GRUB shell:

 # grub

Use the  command with the output from the  command (see #Finding GRUB's root) to instruct GRUB which partition contains stage1 (and therefore, ):

 grub> root (hd1,0)

## Installing to the MBR
The following example installs GRUB to the MBR of the first drive:

 grub> setup (hd0)

## Installing to a partition
The following example installs GRUB to the first partition of the first drive:

 grub> setup (hd0,0)

After running , enter  to exit the shell. If you chrooted, exit your chroot and unmount partitions. Now reboot to test.

## Alternate method (grub-install)
Use the  command followed by the location to install the boot loader. For example to install GRUB to the MBR of the first drive:

 # grub-install /dev/sda

GRUB will indicate whether it successfully installs. If it does not, you will have to use the GRUB shell method.

## Tips and tricks
## Framebuffer resolution
One can use the resolution given in the , but you might want to use your LCD wide-screen at its full native resolution. Here is what you can do to achieve this:

On Wikipedia, there is a list of extended framebuffer resolutions (i.e. beyond the ones in the VBE standard).

If the desired resolution does not work with the codes obtained from the table, it usually is because the graphics card manufacturers are free to choose any number they wish, as this is not part of the VBE 3 standard. These codes may change from one card to the other (possibly even for the same manufacturer).

Instead of using that table, use one of the tools mentioned below to get the correct code:

## GRUB recognized value
This is an easy way to find the resolution code using only GRUB itself.

On the kernel line, specify that the kernel should ask you which mode to use.

 kernel /vmlinuz-linux root=/dev/sda1 ro vga=ask

Now reboot. GRUB will now present a list of suitable codes to use and the option to scan for even more.

You can pick the code you would like to use (do not forget it, it is needed for the next step) and boot using it.

Now replace  in the kernel line with the correct one you have picked.

e.g. the kernel line for  would be:

 kernel /vmlinuz-linux root=/dev/sda1 ro vga=0x369

## hwinfo
# Install the   package.
# Run  as root.
# Pick up the code corresponding to the desired resolution.
# Use the 6 digit code with 0x prefix in  kernel option in . Or convert it to decimal to avoid the use of 0x prefix.

Example output of hwinfo:

 Mode 0x0364: 1440x900 (+1440), 8 bits
 Mode 0x0365: 1440x900 (+5760), 24 bits

And the kernel line:

 kernel /vmlinuz-linux root=/dev/sda1 ro vga=0x0365

## Naming partitions
## By Label
If you alter (or plan to alter) partition sizes from time to time, you might want to consider defining your drive/partitions by a label. You can label ext2, ext3, ext4 partitions by:

 e2label /dev/drive|partition label

The label name can be up to 16 characters long but cannot have spaces for GRUB to understand it. Then define it in your :

 kernel /boot/vmlinuz-linux root=/dev/disk/by-label/Arch_Linux ro

## By UUID
The UUID (Universally Unique IDentifier) of a partition may be discovered with  or . It is defined in  with either:

 kernel /boot/vmlinuz-linux root=/dev/disk/by-uuid/uuid_number

or:

 kernel /boot/vmlinuz-linux root=UUID=uuid_number

## Boot as root (single-user mode)
At the boot loader, select an entry and edit it ( key). Append the following parameters to the kernel options:
 single init=/bin/bash
This will start in single-user mode (init 1), i.e. you will end up to a root prompt without being asked for password.
This may be useful for recovery features, like resetting the root password.
However, this is a huge security flaw if you have not set any #Password protection for grub.

## Password protection
You can enable password protection in the GRUB configuration file for operating systems you wish to have protected. Boot loader password protection may be desired if your BIOS lacks such functionality and you need the extra security.

First, choose a password you can remember and then encrypt it:

Then add your password to the beginning of the GRUB configuration file at  (the password must be at the beginning of the configuration file for GRUB to be able to recognize it):

Then for each operating system you wish to protect, add the  command:

It is always possible to reset your BIOS settings by setting the appropriate jumper on the motherboard (see your motherboard's manual, as it is specific to every model). So in case other have access to the hardware, there is basically no way to prevent boot breakthroughs.

## Restart with named boot choice
If you realize that you often need to switch to some other non-default OS (e.g. Windows) having to reboot and wait for the GRUB menu to appear is tedious. GRUB offers a way to record your OS choice when restarting instead of waiting for the menu, by designating a temporary new default which will be reset as soon as it has been used.

Supposing a simple  setup like this:

Arch is the default (0). We want to restart in to Windows. Change  to  -- this will record the current default in a  file in the GRUB directory whenever the savedefault command is used. Now add the line  to the bottom of the Windows entry. Whenever Windows is booted, it will reset the default to Arch, thus making changing the default to Windows temporary.

Now all that is needed is a way to easily change the default manually. This can be accomplished using the command . So, to reboot into Windows, enter the following commands:

 # grub-set-default 1

Then reboot.

For ease of use, you might wish to setup sudo and add  amongst the commands the user is allowed to issue without supplying a password.

## LILO and GRUB interaction
If the LILO package is installed on your system, uninstall it. As some tasks (e.g. kernel compilation using ) will make a LILO call, and LILO will then be installed over GRUB. LILO may have been included in your base system, depending on your installer media version and whether you selected/deselected it during the package selection stage.

## GRUB boot disk
First, format a floppy disk:

 # fdformat /dev/fd0
 # mke2fs /dev/fd0

Now mount the disk:

 # mount -t ext2 /dev/fd0 /mnt/fl

Install GRUB to the disk:

 # grub-install --root-directory=/mnt/fl '(fd0)'

Copy your  file to the disk:

 # cp /boot/grub/menu.lst /mnt/fl/boot/grub/menu.lst

Now unmount your floppy:

 # umount /mnt/fl

Now you should be able to restart your computer with the disk in the drive and it should boot to GRUB. Make sure that your floppy disk is set to have higher priority than your hard drive when booting in your BIOS first, of course.

See also: [https://www.supergrubdisk.org/ Super GRUB Disk.

## Hide GRUB menu
The  option can be used in order to hide the menu by default. That way no menu is displayed and the default option is going to be automatically selected after the timeout passes.
Still, you are able to press  and the menu shows up. To use it, just add to your :
 hiddenmenu

## Troubleshooting
## GRUB Error 17
The first check to do is to unplug any external drive. Seems obvious, but sometimes we get tired ;)

If your partition table gets messed up, an unpleasant "GRUB error 17" message might be the only thing that greets you on your next reboot. There are a number of reasons why the partition table could get messed up. Commonly, users who manipulate their partitions with GParted -- particularly logical drives -- can cause the order of the partitions to change. For example, you delete  and resize , then finally re-create what used to be  only now it appears at the bottom of the list,  for example. Although the physical order of the partitions/logical drives has not changed, the order in which they are recognized has changed.

Fixing the partition table is easy. Boot from your Arch CD/DVD/USB, login as root and fix the partition table:

 # fdisk /dev/sda

Once in disk, enter emode, [fix the partition order, then the table and exit.

You can verify that the partition table was indeed fixed by issuing an . Now you just need to fix GRUB. See #Boot loader installation.

Basically you need to tell GRUB the correct location of your  then re-write GRUB to the MBR on the disk.

For example:

 # grub

 grub> root (hd0,6)
 grub> setup (hd0)
 grub> quit

See [https://stringofthoughts.wordpress.com/2009/05/24/grub-error-17-debianubuntu for a more in-depth summary of this section.

## /boot/grub/stage1 not read correctly
If you see this error message while trying to set up GRUB, and you are not using a fresh partition table, it is worth checking it.

 # fdisk -l /dev/sda

This will show you the partition table for . So check here, whether the "Id" values of your partitions are correct.
The "System" column will show you the description of the "Id" values.

If your boot partition is marked as being "HPFS/NTFS", for example, then you have to change it to "Linux". To do this, go to fdisk,

 # fdisk /dev/sda

change a partition's system id with , select your partition number and type in the new system id (Linux = 83).
You can also list all available system ids by typing  instead of a system id.

If you have changed a partitions system id, you should your partition table and then [write it.

Now try to set up GRUB again.

See also the forum post reporting this problem.

## Accidental install to a Windows partition
If you accidentally install GRUB to a Windows partition, GRUB will write some information to the boot sector of the partition, erasing the reference to the Windows boot loader. (This is true for NTLDR the boot loader for Windows XP and earlier, unsure about later versions).

To fix this you will need to use the Windows Recovery Console for your Windows release. Because many computer manufacturers do not include this with their product (many choose to use a recovery partition) Microsoft has made them available for download. If you use XP, look at this page to be able to turn the floppy disks to a Recovery CD. Boot the Recovery CD (or enable Windows Recovery mode) and run  to repair the partition boot sector. After this, you will have to install GRUB again---this time, to the MBR, not to the Windows partition---to boot Linux.

## Edit GRUB entries in the boot menu
Once you have selected an entry in the boot menu, you can edit it by pressing key . Use tab-completion if you need to discover devices then  to exit. Then you can try to boot by pressing .

## device.map error
If an error is raised mentioning  during installation or boot, run:

 # grub-install --recheck /dev/sda

to force GRUB to recheck the device map, even if it already exists. This may be necessary after resizing partitions or adding/removing drives.

## KDE reboot pull-down menu fails
If you have opened a sub-menu with the list of all operating systems configured in GRUB, selected one, and upon restart, you still booted your default OS, then you might want to check if you have the line:

 default saved

in .

## GRUB fails to find or install to any virtio /dev/vd* or other non-BIOS devices
I had trouble installing GRUB while installing Arch Linux in an virtual KVM machine using a virtio device for hard drive. To install GRUB, I figured out the following:
Enter a virtual console by typing  or any other F-key for a free virtual console.
This assumes that your root file system is mounted in the folder  and the boot file system is either mounted or stored in the folder .

1. Assure that all needed GRUB files is present in your boot directory (assuming it is mounted in  folder), by issuing the command:

 # ls /mnt/boot/grub

2. If the  folder already contains all the needed files, jump to step 3. Otherwise, do the following commands (replacing ,  and  with the real paths and file names). You should also have the  file written to this folder:

 # mkdir -p /mnt/boot/grub                # if the folder is not yet present
 # cp -r /boot/grub/stage1 /boot/grub/stage2 /mnt/boot/grub
 # cp -r your_kernel your_initramfs /mnt/boot

3. Start the GRUB shell with the following command:

 # grub --device-map=/dev/null

4. Enter the following commands. Replace , and  with the correct device and partition corresponding to your setup.

 device (hd0) /dev/vda
 root (hd0,0)
 setup (hd0)
 quit

5. If GRUB reports no error messages, then you probably are done. You also need to add appropriate modules to the ramdisk. For more information, please refer to QEMU#Preparing an Arch Linux guest.
