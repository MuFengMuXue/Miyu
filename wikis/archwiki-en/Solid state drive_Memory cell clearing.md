# Solid state drive/Memory cell clearing

On occasion, users may wish to completely reset the SSD to the initial "clean" state it was manufactured with, thus restoring it to its factory default write performance. Write performance is known to degrade over time even on SSDs with native TRIM support. TRIM only safeguards against file deletes, not replacements such as an incremental save.

Performing the Secure Erase does not reset the wear leveling status of SSD cells - a drive close to the end of its lifespan may become writable for a short while, but it will still fail after a limited amount of writes.

## SATA drive
ATA has two commands for wiping a drive— and .=== Make sure the drive security is not in frozen mode ===

Issue the following command:

 # hdparm -I /dev/sdX | grep frozen

In the security section of the output it should say . If it shows as just  then you cannot continue to the next step. See Solid state drive#Frozen mode for details.

A possible solution is to simply suspend (using S3 not S0ix) the system. Upon waking up, it is likely that the freeze will be lifted. If unsuccessful, one can try hot-(re)plug the data cable (which might crash the kernel). If hot-(re)plugging the SATA data cable crashes the kernel try letting the operating system fully boot up, then quickly hot-(re)plug both the SATA power and data cables. If hot-(re)plugging of SATA cables still crashes the kernel, make sure that AHCI is enabled in the BIOS (AHCI allows hot-(re)plugging operations without a crash). Using a USB-to-SATA adapter is an option if it supports hotplugging. One can also use  via USB.

## Dell Systems
If the command output shows "frozen", you may be able to work around it by:

# Reboot into the Dell BIOS by pressing F2 on startup.
# Set the Internal HDD Password in the BIOS (be careful, the keymap is en_US / qwerty).
# Apply the changes and reboot.
# When prompted for the password by Dell Security Manager, press Escape rather than entering it.  The drive will remain locked but not frozen.
# Skip step 2, and go directly to Step 3 below.

## Enable security by setting a user password
Any password will do, as this should only be temporary. After the secure erase the password will be set back to NULL. In this example, the password is  as shown:

As a sanity check, issue the following command

 # hdparm -I /dev/sdX

The command output should display "enabled":

## Issue the ATA SECURITY ERASE UNIT command
The final step is to issue the ATA SECURITY ERASE UNIT command, instructing the device's firmware to erase its contents. Note for the device used in this example, earlier output states:

 2min for SECURITY ERASE UNIT. 2min for ENHANCED SECURITY ERASE UNIT.

As per ATA specification the enhanced security erase () performs a more elaborate wipe. If the estimated completion time for both commands is equal, it indicates the drive manufacturer shortcut the specification and uses the same erase function for both. A short time (like 2 minutes) in turn indicates the device is self-encrypting and its firmware function will wipe the internal encryption key instead of overwriting all data cells.[https://security.stackexchange.com/questions/62253/what-is-the-difference-between-ata-secure-erase-and-security-erase-how-can-i-en

 # hdparm --user-master u --security-erase PasSWorD /dev/sdX

Wait until the command completes. This example output shows it took about 40 seconds for an Intel X25-M 80GB SSD.

 security_password="PasSWorD"
 /dev/sdX:
 Issuing SECURITY_ERASE command, password="PasSWorD", user=user
 0.000u 0.000s 0:39.71 0.0%      0+0k 0+0io 0pf+0w

The drive is now erased. After a successful erasure the drive security should automatically be set to disabled (thus no longer requiring a password for access). Verify this by running the following command:

 # hdparm -I /dev/sdX

The command output should display "not enabled":

## NVMe drive
The NVMe specification defines a standardized way to format NVMe drives, since those do not use the SATA interface protocol and therefore cannot be cleared in the same way as SATA SSDs. Originally it was the  command (part of the ) which provided this feature, but while it still does Specification 1.3 added support for a dedicated  command.  As described by the NVM Express Consortium:

:These commands are used to securely erase user data from the device. This can be used when deploying a new device, retiring or at device end-of-life, using an SSD for a new application and so on. Sanitize was introduced in NVMe 1.3 specification, so before then NVMe Format was used exclusively to perform secure erase. While both options work, Sanitize is more robust for ensuring the data was properly wiped; format is good for everyday use and testing.

In order to verify what is supported by your drive, use the Identify Controller command:

 # nvme id-ctrl /dev/nvme0 -H | grep -E 'Format |Crypto Erase|Sanitize'

Example output:

Then proceed with either format or sanitize.

## Format command
The Format command is conceptually closer to a mix of hdparm and fdisk, as it allows to set low-level parameters for the drive and additionally to send a secure erase command.

 gives the following details about the Secure Erase Settings (/) option:

:Secure Erase Settings: This field specifies whether a secure erase should be performed as part of the format and the type of the secure erase operation. The erase applies to all user data, regardless of location (e.g., within an exposed LBA, within a cache, within deallocated LBAs, etc). Defaults to 0.

Possible values :

{| class="wikitable"
|-
! Value
! Definitions
|-
| 0
| No secure erase operation requested
|-
| 1
| User Data Erase: All user data shall be erased, contents of the user data after the erase is indeterminate (e.g., the user data may be zero filled, one filled, etc). The controller may perform a cryptographic erase when a User Data Erase is requested if all user data is encrypted.
|-
| 2
| Cryptographic Erase: All user data shall be erased cryptographically. This is accomplished by deleting the encryption key.
|}

While the Format command accepts either the whole NVMe character device (e.g. ) or a specific namespace block device (e.g. ), make sure this feature is supported by your drive before triggering it. E.g. in the output of the Identify Controller command above, we see that the  and  bits are set to zero, which according to the spec means that "the controller supports format on a per namespace basis" (see figure 249 byte row 524 "Format  NVM  Attributes (FNA)").

For example, to format  with a crypto erase to namespace 1:

 # nvme format /dev/nvme0 -s 2 -n 1

Use  to format all the namespaces.

See  for more information and important warnings regarding device/namespace selection.

## Sanitize command
The Sanitize command was created to be "functionally equivalent to the command of the same name in SATA and SAS implementations"From the [https://web.archive.org/web/20200430084547/https://nvmexpress.org/open-source-nvme-management-utility-nvme-command-line-interface-nvme-cli/ aforementioned article:

:According to the NVMe 1.4 specification, "a sanitize operation alters all user data in the NVM subsystem such that recovery of any previous user data from any cache, the non-volatile media, or any Controller Memory Buffer is not possible."
:The big difference between Sanitize and Format is that sanitize ensures caches are deleted, and the process starts again after an unexpected power loss. Sanitize also supports a pattern overwrite for a secure erase operation, which is terrible for NAND endurance but can be used with other types of storage and memory classes, or for more certainty that user data cannot be recovered.

Usage and possible values for the  options are described in .

The difference between Block Erase and Crypto Erase is that Crypto Erase only erases an encryption key (as defined in the NVMe 1.4 specification):

:User Data Erase: All user data shall be erased, contents of the user data after the erase is indeterminate (e.g., the user data may be zero filled, one filled, etc.). The controller may perform a cryptographic erase when a User Data Erase is requested if all user data is encrypted.
:Cryptographic Erase: All user data shall be erased cryptographically. This is accomplished by deleting the encryption key.
:…
:The Block Erase sanitize operation alters user data with a low-level block erase method that is specific to the media for all locations on the media within the NVM subsystem in which user data may be stored;
:The Crypto Erase sanitize operation alters user data by changing the media encryption keys for all locations on the media within the NVM subsystem in which user data may be stored…

You can get an estimation of the time the various methods would take on your drive (if supported):

If instead you get a result such as:

Then be sure that the operation will take a long time to complete. For reference, a Block Erase took around 2-3 hours to complete on the Intel 660p 512GB reporting those results.

To start a Crypto Erase sanitize operation:

 # nvme sanitize device -a start-crypto-erase

For a Block Erase:

 # nvme sanitize device -a start-block-erase

You can follow the progress with the Sanitize Log:

 # nvme sanitize-log /dev/nvme0

Example output for a drive with a Crypto Erase in progress:

When the command has completed successfully:

## Common method with blkdiscard
The  command from the  package offers a  option to "Perform a secure discard. A secure discard is the same as a regular discard except that all copies of the discarded blocks that were possibly created by garbage collection must also be erased. This requires support from the device".

To use it, execute:

 # blkdiscard --secure /dev/device

For devices which do not support a secure erase, a / option fills the device with zeroes instead of simply discarding all blocks on the device by default.

See for a discussion of the general security of blkdiscard and [https://www.ovirt.org/develop/release-management/features/storage/wipe-volumes-using-blkdiscard.html for an illustration of wiping volumes using blkdiscard.

## Troubleshooting
## UEFI boot entries get removed after wiping a drive
Some UEFI implementations remove boot entries referencing nonexistent files upon system startup. If you plan to restore the system from a backup after memory cell clearing, make sure to also restore the boot entry using efibootmgr or by reinstalling the boot loader.
