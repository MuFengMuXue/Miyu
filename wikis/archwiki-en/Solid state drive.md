# Solid state drive

This article covers special topics for operating solid state drives (SSDs) and other flash-memory based storage devices.

If you want to partition an SSD for a specific purpose, it may be useful to consider the List of file systems optimized for flash memory.

For general usage, simply choose your preferred file system and enable #TRIM.

## Usage
## TRIM
Compared to hard drives, where deleting a file is only handled at the file system levelSSDs benefit from informing the disk controller when blocks of memory are free to be reused. Since the flash cells they are made of are worn out a little with each write operation, the disk controllers use algorithms to share the write operations on all the cells: this process is called wear leveling. Without the NVMe DEALLOCATE, SAS UNMAP or ATA_TRIM command (supported by most SSDs), the disk controller takes more time to do a write operation as soon as there is no empty memory blocks, as it has to shuffle data around to erase a cell before writing to it (see Wikipedia:Write amplification): a [https://www.techspot.com/review/737-ocz-vector-150-ssd/page9.html TechSpot benchmark shows the performance impact before and after filling an SSD with data.

As of Linux kernel version 3.8 onwards, support for TRIM was continually added for the different file systems. See the following table for an indicative overview:

{| class="wikitable sortable"
! File system !! Continuous TRIM  ( option) !! Periodic TRIM  (fstrim) !! References and notes
|-
| Bcachefs ||  ||  ||
|-
| Btrfs ||  ||  || Asynchronous discard is enabled by default since kernel 6.2.
|-
| exFAT ||  ||  || fstrim is supported since kernel 5.13, |-
| ext3 ||  ||  ||
|-
| ext4 ||  ||  || "discard, nodiscard(*)" in [https://docs.kernel.org/admin-guide/ext4.html?highlight=discard,%20nodiscard(*)#options
|-
| F2FS ||  ||  ||
|-
| JFS ||  ||  || |-
| NILFS2 ||  ||  ||
|-
| rowspan=2 | NTFS
|  ||  || [https://docs.kernel.org/filesystems/ntfs3.html ntfs3 kernel driver only supports continuous TRIM.
|-
|  ||  || NTFS-3G driver only supports periodic TRIM.
|-
| VFAT ||  ||  || fstrim is supported since kernel 4.19, |-
| XFS ||  ||  || [https://xfs.org/index.php/FITRIM/discard
|-
| Swap ||  ||  || Not technically a "file system", but TRIM is still relevant. The "once" option provides scheduled trimming at startup. See .
|}

To verify TRIM support, run:

 $ lsblk --discard

And check the values of DISC-GRAN (discard granularity) and DISC-MAX (discard max bytes) columns. Non-zero values indicate TRIM support.

For SATA SSDs only, the  package can detect TRIM support via  as the root user.  does however not support NVMe SSDs.

## Periodic TRIM
The  package provides  and  systemd unit files. Enabling the timer will activate the service weekly. The service executes  on all mounted file systems on devices that support the discard operation.

The timer relies on the timestamp of  (which it will create upon first invocation) to know whether a week has elapsed since it last ran. Therefore there is no need to worry about too frequent invocations, in an anacron-like fashion.

To query the units activity and status, see journalctl. To change the periodicity of the timer or the command run, edit the provided unit files.

## Continuous TRIM
Instead of issuing TRIM commands once in a while (by default once a week if using ), it is also possible to issue TRIM commands each time files are deleted instead. The latter is known as the continuous TRIM.

Using the  option for a mount in  enables continuous TRIM in device operations. For example:

 /dev/disk/by-designator/root  /  ext4  defaults,discard  0 1

On the ext4 file system, the  flag can also be set as a default mount option using tune2fs:

 # tune2fs -o discard /dev/sd''XY''

Using the default mount options instead of an entry in  is particularly useful for external drives, because such partition will be mounted with the default options also on other machines. This way, there is no need to edit  on every machine.

## Trim an entire device
If you want to trim your entire SSD at once, e.g. for a new install or if you want to sell the drive, you can use the blkdiscard command.

## Trim unpartitioned space
fdisk can trim only the free space sectors between partitions so that those sectors may be reused for wear levelling. Use the  command, and press  at the prompt that follows.

Or use the  option in sfdisk:

 # sfdisk --discard-free /dev/sdX

## LVM
TRIM requests that get passed from the file system to the logical volume are automatically passed to the physical volume(s). No additional configuration is necessary.

No LVM operations (lvremove, lvreduce and all others) issue TRIM requests to physical volume(s) by default. This is done to allow restoring previous volume group configuration with . The setting  in  controls whether discards are sent to a logical volume's underlying physical volumes when the logical volume is no longer using the physical volumes' space.

## dm-crypt
Follow the instructions in dm-crypt/Specialties#Discard/TRIM support for solid state drives (SSD) to enable discard support for LUKS and plain dm-crypt devices.

## swap
To enable discard for swap space, either add the  option to a swap device's entry in fstab or pass  when calling .

Discard is not automatically enabled for swap partitions when using GPT partition automounting.

See  for discussion on when swap is discarded:  or . If  is specified without a specific mode, the default is to enable both.

## Maximizing performance
Follow the tips in Improving performance#Storage devices to maximize the performance of your drives.

## SSD memory cell clearing
On occasion, users may wish to completely reset an SSD's cells to the same virgin state they were at the time the device was installed, thus restoring it to its factory default write performance. Write performance is known to degrade over time even on SSDs with native TRIM support: TRIM only safeguards against file deletes, not replacements such as an incremental save.

The reset can be accomplished by following the appropriate procedure denoted in Solid state drive/Memory cell clearing, either for SATA or NVMe SSDs.

## Security
## Frozen mode
Some motherboard firmware issue a ATA SECURITY FREEZE LOCK command to SATA devices on initialization, setting the drive to frozen mode which transitions it to SEC2 state (security disabled, not locked, frozen). Likewise some SSD (and HDD) are set to this state in the factory already. This can be seen in hdparm and smartctl output:

Operations like formatting the device or installing operating systems are not affected by the frozen mode.

The above hdparm output shows the device is not locked by an HDD-password on boot and the frozen state safeguards the device against malwares which may try to lock it by setting a password to it at runtime.

If you intend to set a password to a "frozen" device yourself, a motherboard BIOS with support for it is required. A lot of notebooks have support, because it is required for hardware encryption, but support may not be trivial for a desktop/server board. For the Intel DH67CL/BL motherboard, for example, the motherboard has to be set to "maintenance mode" by a physical jumper to access the settings.If you intend to erase the SSD, see Securely wipe disk#hdparm and /Memory cell clearing.

## Setting the SATA SSD state to frozen mode after waking up from sleep
When waking up from S3 sleep, the SATA SSD will most likely have reverted to SEC1 state (security disabled, not locked, not frozen), leaving it vulnerable to ATA SECURITY ERASE UNIT commands like those described in /Memory cell clearing.

In order to prevent this issue, a script can be run after waking up from sleep:

If the system has multiple storage devices and/or portable USB-drives, another option is to adapt Hdparm#Persistent configuration using udev rule to issue a  for all drives (incl. HDD).

## Hardware encryption
As noted in #Frozen mode, setting a password for a storage device (SSD/HDD) in the BIOS may also initialize the hardware encryption of devices supporting it. If the device also conforms to the OPAL standard, this may also be achieved without a respective BIOS feature to set the passphrase. See Self-encrypting drives.

## Troubleshooting
It is possible that the issue you are encountering is a firmware bug which is not Linux specific, so before trying to troubleshoot an issue affecting the SSD device, you should first check if updates are available for:

* The SSD's firmware
* The motherboard's BIOS/UEFI firmware

Even if it is a firmware bug it might be possible to avoid it, so if there are no updates to the firmware or you hesitant on updating firmware then the following might help.

## Resolving NCQ errors
Some SSDs and SATA chipsets do not work properly with Linux Native Command Queueing (NCQ). The tell-tale errors in the journal look like:

 ata9: exception Emask 0x0 SAct 0xf SErr 0x0 action 0x10 frozen
 ata9.00: failed command: READ FPDMA QUEUED
 ata9.00: cmd 60/04:00:d4:82:85/00:00:1f:00:00/40 tag 0 ncq 2048 in
 res 40/00:18:d3:82:85/00:00:1f:00:00/40 Emask 0x4 (timeout)

To disable NCQ on boot, add  to the kernel command line in the boot loader configuration. To disable NCQ only for disk 0 on port 9 use:

Alternatively, you may disable NCQ for a specific drive without rebooting via sysfs:

 # echo 1 > /sys/block/sdX/device/queue_depth

If this (and also updating the firmware) does not resolve the problem or causes other issues, then file a bug report.

## Resolving SATA power management related errors
Some SSDs (e.g. Transcend MTS400 or Crucial M550 SSDs) are failing with certain SATA controllers when SATA Active Link Power Management (ALPM), is enabled.

ALPM is enabled by default since linux-4.16, or may be enabled at runtime by a power saving daemon (e.g. TLP, Laptop Mode Tools). See Power management#SATA Active Link Power Management for more on this.

## External SSD with TRIM support
Several USB-to-SATA bridge chips (like VL715, VL716 etc.) and also USB-to-PCIe bridge chips (like the [https://www.jmicron.com/PDF/brief/jms583.pdf JMicron JMS583 used in external NVMe enclosures like IB-1817M-C31) support TRIM-like commands that can be sent through the USB Attached SCSI driver (named "uas" under Linux).

But the kernel may not automatically detect this capability, and therefore might not use it.
Assuming your block device in question is , you can find out whether that is the case by using the command from :

 # sg_readcap -l /dev/sdX

If in its output you find a line stating  then you know that the kernel assumes the device does not support "Logical Block Provisioning Management" because the (LBPME) bit is not set.

If this is the case, then you should next find out whether the "Vital Product Data" (VPD) page on "Logical Block Provisioning" of your device tells of supported mechanisms for unmapping data. You can do this using the command:

 # sg_vpd -a /dev/sdX

Look for lines in the output that look like this:

 Logical block provisioning VPD page (SBC)
   LBPU=1
   LBPWS=0
   LBPWS10=0

This example would tell you the device supports the "UNMAP" command.

Have a look at the output of

 $ cat /sys/block/sdX/device/scsi_disk/*/provisioning_mode

If the kernel did not detect the capability of your device to unmap data, then this will likely return "full". Apart from "full", the kernel SCSI storage driver currently knows the following values for provisioning_mode:

 unmap
 writesame_16
 writesame_10
 writesame_zero
 disabled

For the example above, you could now write "unmap" to "provisioning_mode" to ask the kernel to use that:

 # echo "unmap" >/sys/block/sdX/device/scsi_disk/*/provisioning_mode

This should immediately enable you to use tools like blkdiscard on  or fstrim on file systems mounted on .

If you want to enable a "provisioning_mode" automatically when an external device of a certain vendor/product is attached, this can be automated via the "udev" mechanism. First find the USB Vendor and Product IDs:

 $ cat /sys/block/sdX/../../../../../../idVendor
 $ cat /sys/block/sdX/../../../../../../idProduct

Then create or append to a udev rule file (example here using idVendor 152d and idProduct 0583):

 # echo 'ACTION=="add|change", ATTRS{idVendor}=="152d", ATTRS{idProduct}=="0583", SUBSYSTEM=="scsi_disk", ATTR{provisioning_mode}="unmap"' >>/etc/udev/rules.d/10-uas-discard.rules

(You can also use the  command to look for the relevant idVendor/idProduct.)

## Firmware
If supported by the device vendor, it is recommended to update firmware using the fwupd utility.

To check your current firmware version:

 # smartctl -i /dev/ssd_device

## ADATA
Updating SSD firmware under Linux is not supported by ADATA. A Windows-only utility called SSD ToolBox is provided by ADATA through their support page and through their ADATA XPG support page to monitor, TRIM, benchmark and update ADATA SSD firmware.

## Crucial
Crucial provides an option for updating the firmware with an ISO image. These images can be found after selecting the product on their SSD support page and downloading the "Manual Boot File."

Owners of an M4 Crucial model, may check if a firmware upgrade is needed with .

Users seeing this warning are advised to backup all sensible data and consider upgrading immediately. Check this instructions to update Crucial MX100 firmware by using the ISO image and Grub.

Besides the bootable ISO,  is a command-line tool for flashing firmwares and also offers additional SSD information.

## Intel
Intel has a Linux live system based Firmware Update Tool for operating systems that are not compatible with its Windows Intel® Memory and Storage Tool (GUI) software.

There is also a newer Linux command-line utility that can reflash firmware called the Intel Memory and Storage (MAS) Tool available as .  There is a PDF user guide available.

An example for checking the firmware status is:

 can be omitted if there is only one Intel SSD in the system, or  passed for the second SSD, and so on.

If an update is available, it is performed by running . The PDF user guide suggests that this procedure needs to be performed twice in Linux, with a power cycle in between. The latest firmware for all devices is distributed as part of the MAS Tool itself, so does not need to be downloaded separately.

## Kingston
KFU tool is available for the Sandforce based drives, .

## Mushkin
The lesser known Mushkin brand solid state drives also use Sandforce controllers, and have a Linux utility (nearly identical to Kingston's) to update the firmware.

## OCZ
OCZ has a Command Line Online Update Tool (CLOUT) available for Linux. The existing packages are ,  and .

## Samsung
Although Samsung deems firmware update methods outside of their Magician software as "unsupported", they still can work. The Magician software can create a bootable USB drive containing the firmware update, however Samsung no longer provides the software for consumer SSDs. Samsung also provides pre-made bootable ISO images that can be used to update the firmware. Another option is to use Samsung's magician utility provided by . Magician only supports Samsung-branded SSDs; those manufactured by Samsung for OEMs (e.g., Lenovo) are not supported.

Users preferring to run the firmware update from a live USB created under Linux (without using Samsung's Magician software under Microsoft Windows) can refer to for more details. Note that this blog post details creating a bootable USB drive with Master Boot Record (MBR) that some newer motherboards, e.g. [https://www.intel.com/content/www/us/en/support/articles/000057401/intel-nuc.html Intel NUC no longer support.

## Update under Linux
The SSD firmware can be updated natively (without making a bootable USB stick) as shown below. First visit the Samsung downloads page, go to the "Samsung SSD Firmware" section, and download the latest firmware for your SSD—it should be an ISO image.

Extract the  Linux image from the ISO image:

 $ bsdtar xf samsung_ssd_firmware.iso initrd

Extract . This directory contains the firmware update files:

 $ bsdtar xf initrd root/fumagician

Finally, run  with root privileges and reboot your system (if the firmware was successfully updated).

If after reboot the firmware version does not change, run  and search for errors in the log file. For example, if the log shows 'unzip is not available', install unzip or extract it from the initrd.

## Older SSDs
Some of the SSD firmware ISO images contain a FreeDOS image instead of an  Linux image, so the steps needed to update the SSD firmware differ from above. The following table lists these SSDs (and relevant paths):

{| class="wikitable"
! SSD model !! FreeDOS image path !! Firmware package path
|-
| 470, 830 ||  ||
|-
| 840 ||  || rowspan="2" |
|-
| 840 EVO (mSATA), Pro ||
|}

First, extract the FreeDOS image from the ISO image:

 $ bsdtar xf samsung_ssd_firmware.iso freedos_image_path

Mount the FreeDOS image to :

 # mount freedos_image_path /mnt

Get the disk number of the SSD under Disk Number from the Magician SSD management utility:

 # magician --list

Update the SSD firmware for the specified disk by providing the firmware package path:

 # magician --disk disk_num --firmware-update --fwpackage-path /mnt/firmware_package_path

Finally, verify whether the firmware was successfully updated by checking the version under Firmware from the output of  (with root privileges). Reboot your system if so.

## SanDisk
SanDisk makes ISO firmware images to allow SSD firmware update on operating systems that are unsupported by their SanDisk SSD Toolkit.

One must choose the firmware for the correct SSD model, and the correct capacity that it has (e.g. 60GB, or 256GB). After burning the ISO firmware image, simply restart the PC to boot with the newly created CD/DVD boot disk (may work from a USB stick).

The iso images just contain a linux kernel and an initrd. Extract them to  partition and boot them with GRUB or Syslinux to update the firmware.

See also:

* SanDisk Extreme SSD Manual Firmware update version R211
* SanDisk Ultra SSD Manual Firmware update version 365A13F0
* SanDisk Ultra+ SSD Manual Firmware update version X2316RL - use  as root to determine if a "H2" or "HP" model is used.
