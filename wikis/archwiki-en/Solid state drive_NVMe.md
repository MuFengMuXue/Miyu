# Solid state drive/NVMe

NVM Express (NVMe) is a specification for accessing SSDs attached through the PCI Express bus. As a logical device interface, NVM Express has been designed from the ground up, capitalizing on the low latency and parallelism of PCI Express SSDs, and mirroring the parallelism of contemporary CPUs, platforms and applications.

## Installation
NVMe devices should show up as . See Device file#NVMe for an explanation on their naming.

Extra userspace NVMe tools can be found in  or .

See Solid state drive for supported filesystems, maximizing performance, minimizing disk reads/writes, etc.

## Management
List all the NVMe SSDs attached with name, serial number, size, LBA format and serial:

 # nvme list

List information about a drive and features it supports in a human-friendly way:

 # nvme id-ctrl -H /dev/nvme0

List information about a namespace and features it supports:

 # nvme id-ns /dev/nvme0n1

Output the NVMe error log page:

 # nvme error-log /dev/nvme0

Delete a namespace:

 # nvme delete-ns /dev/nvme0n1

Create a new namespace, e.g creating a smaller size namespace to overprovision an SSD for improved endurance, performance, and latency:

 # nvme create-ns /dev/nvme0

See  and  for a list of all commands along with a terse description.

## SMART
Output the NVMe SMART log page for health status, temp, endurance, and more:

 # nvme smart-log /dev/nvme0

NVMe support was added to  in version 6.5.

Currently implemented features (as taken from the wiki):

* Basic information about controller name, firmware, capacity ()
* Controller and namespace capabilities ()
* SMART overall-health self-assessment test result and warnings ()
* NVMe SMART attributes ()
* NVMe error log ()
* Ability to fetch any nvme log ()
* The smartd daemon tracks health (), error count () and temperature ()

See S.M.A.R.T. and the official wiki entry for more information, and see this article for contextual information about the output.

## Secure erase
See Solid state drive/Memory cell clearing#NVMe drive.

## Firmware update
## Generic
Firmware can be managed using . To display available slots and check whether Slot 1 is read-only:

Download and commit firmware to specified slot. In the example below, firmware is first committed without activation (). Next, an existing image is activated (). Refer to the NVMe specification for details on firmware commit action values.

Finally reset the controller to load the new firmware:

 # nvme reset /dev/nvme0

This can also be done manually if needed:

 # echo 1 > /sys/class/nvme/nvme0/reset_controller

## Intel/Solidigm
After Intel SSD business was acquired by SK Hynixits "Memory and Storage Tool" (Intel MAS) lost support for SSDs and can now only be used to manage Optane devices.[https://www.intel.com/content/www/us/en/download/19520/intel-memory-and-storage-tool-cli-command-line-interface.html

Solidigm, the US subsidiary formed from Intel's SSD business acquisition, provides a new utility to manage former Intel SSDs: "The Solidigm Storage Tool, also called SST, assists with managing Solidigm SSDs. It provides access to drive information and health, SMART Attributes, Firmware Updates, diagnostic scans, and secure erase."Install , then check whether your drive has an update available:

If so execute the  command as follows, using the index value given in the previous command:

For more information, refer to the user guide provided on the tool's aforementioned official page.

## Kingston
Kingston does not provide separate firmware downloads on their website, instead referring users to a Windows only utility. Firmware files appear to use a predictable naming scheme based on the firmware revision:

https://media.kingston.com/support/downloads/S5Z42105.zip

Then proceed with the generic flashing instructions.

## Samsung
## Using Samsung Magician Software
Next to "Samsung Magician Software" for Windows users, Samsung also provides SSD firmware as bootable ISO images:

https://semiconductor.samsung.com/consumer-storage/support/tools/

They can be written onto a bootable CD or USB drive, or you can unpack the image and do everything live:

 $ curl -OL https://samsung.com/.../xxx.iso
 $ bsdtar -xf xxx.iso initrd
 $ bsdtar -xf initrd root
 # ./root/fumagician/fumagician

You need to reboot for the firmware update to take effect.

## Using nvme-cli
Instead of using the manufacturer's program you might prefer to use .

As of January 2025, the firmware files on the ISO are encrypted by an AES key hidden inside the  binary [https://github.com/chrivers/samsung-firmware-magicYou will find two encrypted files next to it:

The actual firmware file is:

# encrypted by an AES key,
# then it is inserted into a ZIP file,
# and the ZIP file is encrypted again, yielding the  file. The exact file name may differ between SSD models.

You first need to determine the AES key used. The key can be extracted from the  utility by running [https://github.com/Qwertylex/samdecrypt.sh/blob/a1bc854f565eb3733585a1b551a1990bfd7b7854/README.md

{{hc|$ strings root/fumagician/fumagician  grep -E '^base64 -d  xxd -p -c 32|
bde8eedf5d75327b516decd4d2723209697c4c3e30550d98253319076b4d649a
}}

You can then use the [https://github.com/Qwertylex/samdecrypt.sh/blob/a1bc854f565eb3733585a1b551a1990bfd7b7854/samdecrypt.sh samdecrypt.sh utility to decrypt the file. First, insert the key found above into the script. Then, decrypt the ZIP file (the result will be written into ):

 $ ./samdecrypt.sh root/fumagician/1B2QJXD7.enc

Decompress the ZIP file:

Finally, decrypt the inner file, yielding :

 $ ./samdecrypt.sh ssd_firmware/2B2QKXG7_20241112.enc

You can now upload the firmware image in  manually as explained in the previous section. However, you will need to provide an extra  argument to the download operation # nvme fw-download /dev/nvme0 --fw ssd_firmware/2B2QKXG7_20241112.bin --xfer 0x8000

Afterwards, the commit operation should work normally.

## Western Digital
Western Digital only supports updating via their Windows based Dashboard software. However, the firmware can be downloaded directly if you know where to look.[https://community.frame.work/t/western-digital-drive-update-guide-without-windows-wd-dashboard/20616

First, navigate to the list of all drives and find your drive ().

Under your particular drive model there will be one or more  entries. If there are multiple URLs then you may need to try each one using the directions below and check the  tag for your current firmware version.

Now, download the drive-specific XML file:

 $ curl https://sddashboarddownloads.sandisk.com/url_entry

Inside this drive-specific XML file should be a  tag with a  filename. This is the name of the file you want; you can download it by replacing  from the previous URL with this filename.

A full URL example for a SN850X drive:

 $ curl --remote-name https://sddashboarddownloads.sandisk.com/wdDashboard/firmware/WD_BLACK_SN850X_2000GB/620331WD/620331WD.fluf

Once you have the .fluf file, updating can be performed using the generic flashing instructions. Be aware that this is not officially supported by Western Digital, may not work correctly, and could possibly damage your device. Be extra careful that you are updating with the correct drive and version of firmware.

## Performance
## Sector size
See Advanced Format#NVMe solid state drives.

## Airflow
NVMe SSDs are known to be affected by high operating temperatures and will throttle performance over certain thresholds.=== Testing ===

Raw device performance tests can be run with :

 # hdparm -Tt --direct /dev/nvme0n1

## Power saving
## Allow drive to enter low-power states (APST)
To check NVMe power states, install  or , and run :

When APST is enabled the output should contain "Autonomous Power State Transition Enable (APSTE): Enabled" and there should be non-zero entries in the table below indicating the idle time before transitioning into each of the available states.

If APST is enabled but no non-zero states appear in the table, the latencies might be too high for any states to be enabled by default. The output of  (as the root user) should show the available non-operational power states of the NVME controller. If the total latency of any state (enlat + xlat) is greater than 25000 (25ms) you must pass a value at least that high as parameter  for the  kernel module. This should enable APST and make the table in  (as the root user) show the entries.

## Control background processing during low-power states (NOPPM)
A drive's low-power states may be non-operational states in which the drive accepts only certain management commands.  Version 1.3 of the NVMe specification introduced the Non-Operational Power State Permissive Mode (NOPPM) feature to control background processing in non-operational power states.  When enabled and the drive is in a non-operational power state, the drive may exceed the current power state's declared power limit (but not the limit of the lowest operational power state) to perform background processing, such as garbage collection or refreshing old data.  When disabled, the drive will respect the current state's power limit and defer such processing until it next enters an operational power state, possibly reducing performance until that processing is done.  The default setting is vendor- and drive-specific.

To check if your drive supports NOPPM, use ; the output will include  or .  To change the setting, use , where  is  to disable NOPPM (prefer power saving) or  to enable NOPPM (prefer performance).  By default, the setting will revert to default when the drive is reset (on reboot, and possibly on waking from sleep).  If your drive supports the Save and Select Feature Support (SSFS) feature, you can make your change persistent by appending the  option to the  command.

## Troubleshooting
## Controller failure due to broken APST support
Some NVMe devices may exhibit issues related to power saving (APST). This is a known issue for Kingston A2000 [https://bbs.archlinux.org/viewtopic.php?pid=1926994#p1926994 as of firmware S5Z42105 and has previously been reported on Samsung NVMe drives (Linux v4.10) Also reported for some WesternDigital/Sandisk devices [https://bugzilla.kernel.org/show_bug.cgi?id=208123 and SK Hynix devices A failure renders the device unusable until system reset, with kernel logs similar to:

  nvme nvme0: I/O 566 QID 7 timeout, aborting
  nvme nvme0: I/O 989 QID 1 timeout, aborting
  nvme nvme0: I/O 990 QID 1 timeout, aborting
  nvme nvme0: I/O 840 QID 6 timeout, reset controller
  nvme nvme0: I/O 24 QID 0 timeout, reset controller
  nvme nvme0: Device not ready; aborting reset, CSTS=0x1
  ...
  nvme nvme0: Device not ready; aborting reset, CSTS=0x1
  nvme nvme0: Device not ready; aborting reset, CSTS=0x1
  nvme nvme0: failed to set APST feature (-19)

Other symptoms are Btrfs storage becoming read-only and Ext4 reporting I/O errors.

As a workaround, add the kernel parameter  to completely disable APST, or set a custom threshold to disable specific states.

If setting latency still does not works, try adding  and  (as suggested by [https://lore.kernel.org/r/all/20240711225952.5445-1-bvanassche@acm.org/T/). You may also need to disable NVMe and PCIe power saving measures within the BIOS.

Since March 2021 a firmware update 9 from Kingston is available. As Kingston only supports Windows, downloads for Linux can be found via heise.de or github. It is expected that, as long as the kernel workaround is in place, the firmware update will not do much as the deepest powersaving states are not reached anyway.

The value passed is the maximum exit latency (Ex_Lat). For example, to disable PS4 set .

## Controller failure due to broken suspend support
Some users (for example, see Laptop/HP) have reported suspend failures with certain NVMe drives. As above, the failure renders the device inoperable until system reset, with kernel messages

 nvme nvme0: Device not ready; aborting reset, CSTS=0x3
 nvme nvme0: Removing after probe failure status: -19

As a workaround, add the kernel parameter  to use a software replacement for the hardware IOMMU. (For further details, see this documentation.) This has the potential to cause some slight processing overhead.

Also you can try kernel parameter  or better  on HP laptops with AMD CPU and KIOXIA KBG40ZN* nvme's, after you get I/O error with messages like this:
 Failed to rotate /var/log/journal/*/system.journal: Read-only file system
 nvme nvme0: Device not ready; aborting reset, CSTS=0x3
 BTRFS error (device nvme0n1): bdev /dev/nvme0n1p* errs: wr 2, rd 0, flush 0, corrupt 0, gen 0
