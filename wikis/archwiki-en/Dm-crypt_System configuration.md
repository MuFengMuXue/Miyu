# Dm-crypt/System configuration

## Unlocking in early userspace
Booting an encrypted root volume requires that the initramfs contains the necessary tools for early userspace to unlock the volume. The instructions on what to unlock are typically passed via kernel parameters.

The following sections describe how to configure mkinitcpio and list which kernel parameters are required.

## mkinitcpio
Depending on the particular scenarios, a subset of the following mkinitcpio hooks will have to be enabled:

{| class="wikitable"
! busybox !! systemd !! Use case
|-
|style="text-align: center;white-space:nowrap;"|
|style="text-align: center;white-space:nowrap;"|
| Needed when the root partition is encrypted or when an encrypted partition needs to be mounted before the root partition. Not needed in other cases as system initialization scripts like  already take care of unlocking other non-root partitions. This hook must be placed after the  or  hook.
|-
|colspan="2" style="text-align: center;white-space:nowrap;"|
| Needed to make keyboards work in early userspace.

|-
|style="text-align: center;white-space:nowrap;"|
|rowspan="2" style="text-align: center;white-space:nowrap;"|
| Provides support for non-US keymaps for typing encryption passwords; it must come before the  hook, otherwise you will need to enter your encryption password using the default US keymap. Set your keymap in , see Keyboard configuration in console#Persistent configuration.
|-
|style="text-align: center;white-space:nowrap;"|
| Loads an alternative console font in early userspace. Set your font in , see Linux console#Persistent configuration.
|}

Other hooks needed should be clear from other manual steps followed during the installation of the system.

## Examples
A typical  configuration using  hook:

A configuration with systemd-based initramfs using  hook:

## Kernel parameters
The kernel parameters you need to specify depend on whether the  hook or the  hook is being used.  and  are specified the same way for both.

## root
The  parameter specifies the  of the actual (decrypted) root file system:

 root=device

* If the file system is formatted directly on the decrypted device file this will be .
* If a LVM gets activated first and contains an encrypted logical rootvolume, the above form applies as well.
* If the root file system is contained in a logical volume of a fully encrypted LVM, the device mapper for it will be in the general form of .

## resume
 resume=device

*  is the device file of the decrypted (swap) filesystem used for suspend to disk. If swap is on a separate partition, it will be in the form of . See also dm-crypt/Swap encryption.

## Using encrypt hook
## cryptdevice
This specifies the device containing the encrypted root on a cold boot. It is parsed by the  hook to identify which device contains the encrypted system:

 cryptdevice=device:dmname:options

*  is the path to the device backing the encrypted device. Usage of persistent block device naming is strongly recommended.
*  is the device-mapper name given to the device after decryption, which will be available as .
*  (optional) are comma separated options, e.g. for TRIM support. If no options are required, omit this parameter (use ).
* If a LVM contains the encrypted root, the LVM gets activated first and the volume group containing the logical volume of the encrypted root serves as device. It is then followed by the respective volume group to be mapped to root. The parameter follows the form of .

## cryptkey
This parameter specifies the location of a keyfile and is required by the  hook for reading such a keyfile to unlock the  (unless a key is in the default location, see below). It can have three parameter sets, depending on whether the keyfile exists as a file in a particular device, a bitstream starting on a specific location, or a file in the initramfs.

For a file in a device the format is:

 cryptkey=device:fstype:path

*  is the raw block device where the key exists. Usage of persistent block device naming is strongly recommended.
*  is the filesystem type of  (or auto).
*  is the absolute path of the keyfile within the device.

Example:

For a bitstream on a device the key's location is specified with the following:

 cryptkey=device:offset:size

where the offset and size are in bytes. For example,  reads a 512 byte keyfile starting at the beginning of the device.

For a file included in the initramfs the format iscryptkey=rootfs:path

Example:

Also note that if  is not specified, it defaults to  (in the initramfs).[https://gitlab.archlinux.org/archlinux/packaging/packages/cryptsetup/-/blob/main/hooks-encrypt#L8

See also dm-crypt/Device encryption#Keyfiles.

## crypto
This parameter is specific to pass dm-crypt plain mode options to the encrypt hook.

It takes the form

 crypto=hash:cipher:keysize:offset:skip

The arguments relate directly to the cryptsetup options. See dm-crypt/Device encryption#Encryption options for plain mode.

For a disk encrypted with just plain default options, the  arguments must be specified, but each entry can be left blank:

 crypto=::::

A specific example of arguments is

 crypto=sha512:twofish-xts-plain64:512:0:

## Using systemd-cryptsetup-generator
systemd-cryptsetup-generator is a systemd unit generator that reads a subset of kernel parameters, and , for the purpose of unlocking encrypted devices. See the  man page for more details about it and all options it supports.

systemd-cryptsetup-generator is run  during the initramfs stage when using the  mkinitcpio hook or the  dracut module.

In what follows, we describe some of the kernel parameters that systemd-cryptsetup-generator interprets.

## rd.luks.name / rd.luks.uuid
Two separate kernel parameters exist to unlock LUKS devices at boot.

Be aware to reference the LUKS container UUID, not the PARTUUID, and not the UUID of the unlocked/mapped file system.

 rd.luks.name=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX=name

Specifies the UUID of the LUKS partition to open, and assigns an explicit name to the unlocked/mapped device (e.g. ).

 rd.luks.uuid=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX

Specifies only the UUID of the LUKS partition to open. No device name is provided. The mapped device name is automatically derived from the UUID and the device will be located at

## rd.luks.key
Specify the location of a password file used to decrypt the device specified by its UUID. There is no default location like there is with the  hook parameter .

If the keyfile is included in the initramfs:

 rd.luks.key=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX=/path/to/keyfile

or

 rd.luks.key=/path/to/keyfile

If the keyfile is on another device:

 rd.luks.key=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX=/path/to/keyfile:UUID=ZZZZZZZZ-ZZZZ-ZZZZ-ZZZZ-ZZZZZZZZZZZZ

Replace  with the identifier of the device on which the keyfile is located.

## rd.luks.options
 rd.luks.options=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX=options

or

 rd.luks.options=options

Set options for the device specified by it UUID or, if not specified, for all UUIDs not specified elsewhere (e.g., crypttab).

This parameter is the analogue of crypttab's options field. The format is the same—options are separated by commas, options with values are specified using . This is roughly equivalent to the third parameter of 's .

For example:

 rd.luks.options=timeout=10s,discard,password-echo=no,tries=1

## Timeout
There are two options that affect the timeout for entering the password during boot:

*  specifies the timeout for querying for a password
*  specifies how long systemd should wait for the rootfs device to show up before giving up (defaults to 90 seconds)

If you want to disable the timeout altogether, then set both timeouts to zero:

 rd.luks.options=timeout=0 rootflags=x-systemd.device-timeout=0

## Password echo
When the user is typing the password, systemd-cryptsetup by default outputs asterisks () for each typed character. This is unlike the  hook, which does not output anything. To silence the output, set the  option:

 rd.luks.options=password-echo=no

## Trusted Platform Module and FIDO2 keys
If a TPM2 chip is available in your system, or you use FIDO2-compatible security key, you can use it to automatically unlock your volume instead of using a password or a keyfile.

In addition to  or , set:

* for TPM2 chip:
* for FIDO2 key:

Alternatively, using :

Here the encrypted volume is mounted under the name  (appearing in ), mounted via the UUID of the storage device, with no password, and retrieving the key from the TPM2 device.

Note that  or  must be provided in the password field order for the TPM2 device to be used, otherwise the value given will be used as a password or key, and if it does not work it will ask you to type in the passkey during boot without attempting to load the key from the TPM2 device.

If specifying the device via UUID as shown above, ensure it is that of the underlying (encrypted) storage device, not the UUID of the decrypted volume that is specified elsewhere as the root filesystem.

## Pinning a LUKS volume
Since systemd v260, it is possible to pin the expected hash of a LUKS volume key in the crypttab configuration using the  option. This option allows you to specify the expected volume key hash and prevents the system from attaching the volume if the hash does not match. The expected hash corresponds to the digest measured in the SHA256 PCR bank of the TPM2 when the  option is used.

This feature helps defend against rogue operating systems that could use copied metadata (such as partition UUIDs) from the real root filesystem to impersonate the original partition. For optimal security, this option should be used in conjunction with a signed unified kernel image.

To determine the expected hash value for the  option:

* Enable .
* Reboot the system.
* Run the following command to retrieve the hash value:

 # grep volume-key /run/log/systemd/tpm2-measure.log | jq --seq '.digests[].digest'

The resulting option in the kernel command line will typically look like this:

 rd.luks.options=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX=tpm2-device=auto,tpm2-measure-pcr=yes,fixate-volume-key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

## rd.luks.data
When using a detached LUKS header, specify the block device with the encrypted data. Must be used together with  to specify the header file location.

See dm-crypt/Specialties#Encrypted system using a detached LUKS header for details and instructions.

## systemd-gpt-auto-generator
If all the prerequisites of systemd#GPT partition automounting are met, you can avoid specifying any  kernel parameters. systemd-cryptsetup-generator will automatically try to unlock the LUKS-encrypted root partition.

To persistently reference discovered partitions in configuration files, use the identifiers from Persistent block device naming#by-designator and gpt-auto. If you want to specify crypttab options for the root partition, use  as the device in . For example,  without kernel options and no password:

## Unlocking in late userspace
## crypttab
The  (encrypted device table) file is similar to the fstab file and contains a list of encrypted devices to be unlocked during system boot up. This file can be used for automatically mounting encrypted swap devices or secondary file systems.

 is read before , so that encrypted devices can be unlocked before the file system inside is mounted. Note that  is read after the system has booted up, therefore it is not a replacement for unlocking encrypted partitions by using mkinitcpio hooks and configuring them by using kernel parameters as in the case of encrypting the root partition.  processing at boot time is made by the  automatically.

See  for details, read below for some examples, and the #Mounting at boot time section for instructions on how to use UUIDs to mount an encrypted device.

To test your crypttab immediately after editing it, reload the systemd manager configuration with a daemon-reload and start the newly generated .

For more on , see #Mounting on demand.

## Mounting at boot time
If you want to mount an encrypted drive at boot time, enter the device's UUID in . You get the UUID (partition) by using the command  and adding it to  in the form:

In case your encrypted device is a LUKS2 volume you may also refer to it by its label if it has one:

You should likely take care that the label set in the LUKS2 header is not the same as the label of the encrypted file system it contains.

The first parameter is your preferred device mapper's name for the encrypted drive. The option  will trigger a prompt during boot to type the passphrase for unlocking the partition. The  option defines a timeout in seconds for entering the decryption password during boot.

## Unlocking with a keyfile
If the keyfile for a secondary file system is itself stored inside an encrypted root, it is safe while the system is powered off and can be sourced to automatically unlock the mount during with boot via crypttab. For example, unlock a crypt specified by UUID:

Then use the device mapper's name (defined in ) to make an entry in :

Since  already is the result of a unique partition mapping, there is no need to specify a UUID for it. In any case, the mapper with the filesystem will have a different UUID than the partition it is encrypted in.

## Mounting a stacked blockdevice
The systemd generators also automatically process stacked block devices at boot.

For example, you can create a RAID setup, use cryptsetup on it and create an LVM logical volume with respective filesystem inside the encrypted block device. A resulting:

will ask for the passphrase and mount automatically at boot.

Given you specify the correct corresponding crypttab (e.g. UUID for the  device) and fstab () entries, there is no need to add additional mkinitcpio hooks/configuration, because  processing applies to non-root mounts only. One exception is when the  hook is used already (e.g. for the root device). In this case  and the initramfs need updating to achieve the correct root raid is picked first.

## Mounting on demand
Instead of using

 # cryptsetup open UUID=... externaldrive

you can start  when you have an entry as follows in your :

That way you do not need to remember the exact crypttab options. It will prompt you for the passphrase if needed.

The corresponding unit file is generated automatically by . You can list all generated unit files using:

 $ systemctl list-unit-files | grep systemd-cryptsetup

## Non blocking mounting
When secondary devices are defined in crypttab without being required for the boot process, the default options will have the cryptsetup service wait for them to be unlocked before the boot process can continue. The  option will avoid this by removing  from the mount service of the specified device. This may be used when devices are unlocked using keyfiles, as without this option the boot process will be delayed by several seconds until the unlock process has finished.

## Troubleshooting
## System stuck on boot/password prompt does not show
If you are using Plymouth, make sure to use the correct modules (see Plymouth#mkinitcpio) or disable it. Otherwise, Plymouth will swallow the password prompt, making a system boot impossible.

## Keyboard or keyfile on filesystem unavailable for unlocking
If you unlock the LUKS device with a keyboard or a keyfile on a filesystem that is not present when generating the initramfs, you might need to add the corresponding modules to the  array of mkinitcpio. This might also be needed when the keyboard is connected through a USB hub. See mkinitcpio#MODULES for more information on this issue and Minimal initramfs#Sorting out modules as a starting point for potential keyboard and filesystem module names to be added.

In general, for keyboards that are not connected to the PC at initramfs generation time, you need to place the  hook before the  hook or only the parts necessary for the currently connected hardware are kept, see mkinitcpio#Common hooks.

## Unresponsive file transfers
Copying large files to encrypted HDD disks may result in unresponsive transfer process. The root cause of the issue are the working queues of dm-crypt, which can be filled in very rapid bursts that exceed the writing speed of the encrypted physical device. A responsive I/O scheduler will not help because the working queues of dm-crypt are implmented as separate buffers before the rest of I/O stack. The issue can be mitigated by disabling the working queues.
