# Install Arch Linux with Fake RAID

The purpose of this guide is to enable use of a RAID set created by the on-board BIOS RAID controller and thereby allow dual-booting of Linux and Windows from partitions inside the RAID set using GRUB. When using so-called "fake RAID" or "host RAID", the disc sets are reached from  and not .

## What is "fake RAID"
From Wikipedia:RAID:

:Operating system-based RAID doesn't always protect the boot process and is generally impractical on desktop versions of Windows. Hardware RAID controllers are expensive and proprietary. To fill this gap, cheap "RAID controllers" were introduced that do not contain a RAID controller chip, but simply a standard disk controller chip with special firmware and drivers. During early stage boot-up, the RAID is implemented by the firmware. When a protected-mode operating system kernel such as Linux or a modern version of Microsoft Windows is loaded, the drivers take over.

:These controllers are described by their manufacturers as RAID controllers, and it is rarely made clear to purchasers that the burden of RAID processing is borne by the host computer's central processing unit -- not the RAID controller itself -- thus introducing the aforementioned CPU overhead which hardware controllers do not suffer from. Firmware controllers often can only use certain types of hard drives in their RAID arrays (e.g. SATA for Intel Matrix RAID, as there is neither SCSI nor PATA support in modern Intel ICH southbridges; however, motherboard makers implement RAID controllers outside of the southbridge on some motherboards). Before their introduction, a "RAID controller" implied that the controller did the processing, and the new type has become known in technically knowledgeable circles as "fake RAID" even though the RAID itself is implemented correctly. Adaptec calls them "host RAID".

See also FakeRaidHowto @ Community Ubuntu Documentation for more information.

Despite the terminology, "fake RAID" via  is a robust software RAID implementation that offers a solid system to mirror or stripe data across multiple disks with negligible overhead for any modern system. dmraid is comparable to mdadm (pure Linux software RAID) with the added benefit of being able to completely rebuild a drive after a failure before the system is ever booted. However, be aware that not all BIOS RAID implementations support drive rebuilding. Instead they rely on non-linux software to perform the rebuild. If your system cannot rebuild a drive in the BIOS RAID setup utility, you are strongly encouraged to use mdraid (pure Linux Software Raid via mdadm - see RAID) instead of dmraid or you will find yourself unable to rebuild an array in case of a drive failure - or unable to retrieve information from your array in case of a motherboard failure without a lot of additional work.

## Preparation
* Open up any needed guides (Installation guide) on another machine. If you do not have access to another machine, print it out.
* Download the latest Arch Linux install image.
* Backup all important files since everything on the target partitions will be destroyed.

## Configure RAID sets
* Enter your BIOS setup and enable the RAID controller.
** The BIOS may contain an option to configure SATA drives as "IDE", "AHCI", or "RAID"; ensure "RAID" is selected.
* Save and exit the BIOS setup. During boot, enter the RAID setup utility.
** The RAID utility is usually either accessible via the boot menu (often F8, F10 or CTRL+I) or whilst the RAID controller is initializing.
* Use the RAID setup utility to create preferred stripe/mirror sets.

## Boot the installer
See Installation guide#Pre-installation for details.

## MBR install example using mdadm and Intel FakeRAID
This is here because I spent hours making this work because there is so much information out there on different ways to do it, plus outdated information. It may need integrated into this page better with more explanation but I am wrapping this up at the moment. This is a basic command line dump that shows a successful RAID setup using the MBR partition structure.

It looks like once you create the array in the intel util it writes the RAID metadata. So assembling/creating an array does not need to happen.  I named my array ZERO in the intel util and you can see it in this example.

I am leaving the entire install example as it shows when to configure things during the install.  You are going to have to modify some things to make them work, do not copy and paste!

 # ls /dev/md/
 # parted /dev/md/ZERO_0
 # mklabel msdos
 # mkpart primary ext4 1MiB 100MiB
 # set 1 boot on
 # mkpart primary ext4 100MiB 16.5GiB
 # mkpart primary linux-swap 16.5GiB 100%

Just to see changes:

 # fdisk -l /dev/md/ZERO_0

Create filesystem/swap and activate swap:

 # mkfs.ext4 /dev/md/ZERO_0p1
 # mkfs.ext4 /dev/md/ZERO_0p2
 # mkswap /dev/md/ZERO_0p3
 # swapon /dev/md/ZERO_0p3
 # mount /dev/md/ZERO_0p2 /mnt
 # mkdir /mnt/boot
 # mount /dev/md/ZERO_0p1 /mnt/boot/

Edit  and uncomment multilib on x64 (why not)(do it after chroot too).
Then:

 # pacstrap -K -i /mnt base base-devel
 # genfstab -U /mnt > /mnt/etc/fstab

Edit  and replace UUIDs with (this may be optional):

 /dev/md/ZERO_0p1
 /dev/md/ZERO_0p2
 /dev/md/ZERO_0p3

Then run:

 # mdadm --detail --scan >> /mnt/etc/mdadm.conf

Chroot in for config:

 # arch-chroot /mnt /bin/bash

Edit  and uncomment  and other needed UTF-8 locales. Generate the locales by running:

 # locale-gen

Create the  file, and set the LANG variable accordingly:

Set the time zone:

 # ln -sf /usr/share/zoneinfo/Region/City /etc/localtime

Install .
Edit  and uncomment

Add  to the  array in :

 HOOKS=(base udev autodetect microcode modconf kms keyboard keymap consolefont block mdadm_udev filesystems fsck)

Regenerate the initramfs. Then:

 # grub-install --recheck /dev/md/ZERO_0
 # grub-mkconfig -o /boot/grub/grub.cfg

Create the hostname file:

Update  file appropriately. Then:

 # systemctl enable dhcpcd@enp13s0.service
 # exit
 # umount -R /mnt
 # reboot

Remove the installation medium.

## Load dmraid
Load device-mapper and find RAID sets:

 # modprobe dm_mod
 # dmraid -ay
 # ls -la /dev/mapper/

Example output:

 /dev/mapper/control            <- Created by device-mapper; if present, device-mapper is likely functioning
 /dev/mapper/sil_aiageicechah   <- A RAID set on a Silicon Image SATA RAID controller
 /dev/mapper/sil_aiageicechah1  <- First partition on this RAID set

If there is only one file (), check if your controller chipset module is loaded with . If it is, then dmraid does not support this controller or there are no RAID sets on the system (check RAID BIOS setup again). If correct, then you may be forced to use software RAID (this means no dual-booted RAID system on this controller).

If your chipset module is NOT loaded, load it now. For example:

 # modprobe sata_sil

See  for available drivers.

To test the RAID sets:

 # dmraid -tay

## Install the boot loader
## GRUB2
See GRUB2 for details on configuring GRUB2. grub-bios works out of the box with dm-raid partitions:

  $ grub-install --target=i386-pc --recheck --debug /dev/mapper/sil_aiageicechah

(Optional) Install  if you have other OS like windows.

  $ grub-mkconfig -o /boot/grub/grub.cfg

That's all, grub-mkconfig will generate the configure automatically. You could edit  to modify the configure (timeout, color, etc) before grub-mkconfig.

## Troubleshooting
## Booting with degraded array
One drawback of the fake RAID approach on GNU/Linux is that dmraid is currently unable to handle degraded arrays, and will refuse to activate. In this scenario, one must resolve the problem from within another OS (e.g. Windows) or via the BIOS/chipset RAID utility.

Alternatively, if using a mirrored (RAID 1) array, users may temporarily bypass dmraid during the boot process and boot from a single drive:

# Edit the kernel line from the GRUB menu
## Remove references to dmraid devices (e.g. change  to )
## Append  to prevent a kernel panic when dmraid discovers the degraded array
# Boot the system

## Error: Unable to determine major/minor number of root device
If you experience a boot failure after kernel update where the boot process is unable to determine major/minor number of root device, this might just be a timing problem (i.e.  might be called before /dev/sd* is fully set up and detected). This can effect both the normal and LTS kernel images. Booting the 'Fallback' kernel image should work. The error will look something like this:

 Activating dmraid arrays...
 no block devices found
 Waiting 10 seconds for device /dev/mapper/nvidia_baaccajap5
 Root device '/dev/mapper/nvidia_baaccajap5' doesn't exist attempting to create it.
 Error: Unable to determine major/minor number of root device '/dev/mapper/nvidia_baaccajap5'

To work around this problem:
:* boot the Fallback kernel
:* insert the  hook in the  array of  after the  hook like this:

 HOOKS=(base udev sleep autodetect microcode modconf kms keyboard keymap consolefont block dmraid filesystems fsck)

:* rebuild the kernel image and reboot

## dmraid mirror fails to activate
Does everything above work correctly the first time, but then when you reboot dmraid cannot find the array?

This is because Linux software raid (mdadm) has already attempted to mount the fakeraid array during system init and left it in an umountable state. To prevent mdadm from running, move the udev rule that is responsible out of the way:

 # cd /lib/udev/rules.d
 # mkdir disabled
 # mv 64-md-raid.rules disabled/
 # reboot

## No block devices for partitions on existing RAID array
If your existing array, set up before attempting to install arch, appears in , but does not have any partitions (, etc) re-check the status of your RAID partitions.

Arch may not create block devices for partitions that work in another OS if there are certain, even minor, problems.

 is useful to diagnose and repair most problems. Unfortunately, you may have to repartition from scratch.
