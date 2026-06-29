# Migrate installation to new hardware

This article discusses the steps required for moving an Arch Linux system to new hardware. The goal is to achieve the same Arch Linux installation, in terms of the installed software and configuration that is independent of the hardware.

There are two different approaches to migrating an installation:

# Bottom to top: Install a fresh Arch Linux system on the new hardware, afterwards restore the installed packages and configuration files, e.g. as described in dotfiles.
# Top to bottom: Clone the old harddrive to the new harddrive, or place the old harddrive into the new system; modify configuration files where necessary.
The top to bottom approach gives a more exact reproduction of the original system than the bottom to top approach.

## Adapt to new hardware
Before you begin, research aspects of the new hardware and make a list of differences. Common differences are

## Hard drive vs. SSD
See the article SSD.

## CPU vendor
If you switch the CPU, to a CPU from another vendor (e.g. Intel to AMD), change the Microcode configuration.

## GPU vendor
If you changed the GPU to a GPU from another vendor (e.g. from AMD to NVIDIA) change the graphics driver.

## UEFI vs. MBR boot code booting
If you switch to a more recent mainboard with UEFI, it might be preferable or required to switch from "MBR boot code" booting to UEFI booting. In this case a new EFI system partition is needed.

## Bottom to top
## On the old system
We define here a minimal configuration that carries over from the old to the new system which differentiates this approach from the Installation guide. Think about the configuration files from  and dotfiles in  that you want to copy to the new system, as well as user data files. If you will not have access to the old system from the new system then backup up all the files that you want to copy over.

## List of installed packages
 $ pacman -Qqen > pkglist.txt
 $ pacman -Qqem > pkglist_aur.txt

gives you a nice list of explicitly installed packages from the repositories and from the AUR. Include it in your backup if you make one.

You may also use the following script to give you a better overview of the binaries and libraries installed unbeknownst to pacman (e. g. installed via Steam, Desura or using their own install methods):

 find / -regextype posix-extended -regex "/(sys|srv|proc)|.*/\.ccache/.*" -prune -o -type f \
 -exec bash -c 'file "{}" | grep -E "(32|64)-bit"' \; | \
 awk -F: '{print $1}' | \
 while read -r bin; \
 do pacman -Qo "$bin" &>/dev/null || echo "$bin"; \
 done

## pacman cache
Consider backing up .

## On the new system
## Installation guide first half
For basics about installing a new system, refer to the Installation guide. Follow the first half of the installation guide up to but excluding the pacstrap command.

## Copy pacman cache
Copy the pacman cache found at  from the old to the new system, or from the backup to the new system.

## Installation guide second half
Continue with the installation guide from, and including the pacstrap command, up to the end, but do not reboot. Do not skip the pacstrap command as it does additional work besides the installation of packages.

## Install previously installed software
Edit pkglist.txt (and pkglist_aur.txt) and remove drivers that are not needed on the new system. Then install any other previously installed software with

 # pacman -S --needed -  computer -> new HDD.
* Make use of temporary storage devices like external HDDs, or cloud backups. Data link: old HDD -> old computer -> storage -> new computer -> new HDD. For an overview see the article System backup.
* Transfer data over network, for example with rsync. Data link: old HDD -> old computer -> network -> new computer -> new HDD.

For the first two options, consider that you might need adapters to connect the HDDs (PATA->SATA, USB-HDD-Cases, etc.), and choose a connection that is sufficiently fast.

The last two options require you to use a live linux system on the new computer, as it is not possible to boot from the new hard drive at this point.

## Update fstab
If you are using an Arch Linux Installation Image, mount the new root partition to , and any other partitions required like you would in a normal install (see Installation guide#Mount the file systems).

Insert an arbitrary comment such as  at the end of your . Generate a new fstab file as indicated on Installation guide#Fstab, appending it to the current fstab file. In general, always review the fstab file created by genfstab. In this case, check the older fstab entries before the comment, if they are outdated or duplicates then delete them, and if the old entries remain useful then keep them. For example, mount entries for network drives can be kept. In general it is recommended to use Persistent block device naming.

## Reinstall the boot loader
You might need to reinstall and/or reconfigure the boot loader for the following reasons:

* Different disks, partition layout, or file system
* Adding UEFI boot entries into the new mainboard NVRAM
* Migration from "MBR boot code" booting to UEFI booting
* Migration from USB to SATA/NVMe
* Updating the kernel commandline
** In case of a different GPU, update the framebuffer mode
** Update the Microcode initramfs image

If you are using a Arch Linux live environment, then before reinstalling the boot loader, change root into the new system:

 # arch-chroot /mnt

Refer to the article on your boot loader for instructions on how to (re)install it.

## Regenerate kernel image
It is recommended to regenerate the initramfs image, although initially the fallback initramfs image may work.

## Reconfigure audio
*  volume
** save settings

## Reconfigure network
If the old installation and the migrated installation shall coexist in the same network, set a new hostname with hostnamectl.

Also consider configuration changes that are required after a change in hostname:

*
* other applications using hostname: synergy, nut (network ups tools)
*  (as the root user) should give some hints on the files to be updated

The network interface names may change and if they were hardcoded in your network manager configuration, its configuration will need updating. Find out the new network interface names with:

 # journalctl -k --grep='renamed from eth'
