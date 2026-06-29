# Dm-crypt/Swap encryption

Depending on requirements, different methods may be used to encrypt the swap partition which are described in the following. A setup where the swap encryption is re-initialised on reboot (with a new encryption) provides higher data protection, because it avoids sensitive file fragments which may have been swapped out a long time ago without being overwritten. However, re-encrypting swap also forbids using a suspend-to-disk feature generally.

## Without suspend-to-disk support
In systems where suspend-to-disk (hibernation) is not a desired feature,  can be set up to decrypt the swap partition with a random password with plain dm-crypt at boot-time. The random password is discarded on shutdown, leaving behind only encrypted, inaccessible data in the swap device.

To enable this feature, simply uncomment the line beginning with  in . Change the device parameter to the name of your swap device. For example, it will look something like this:

This will map  to  as a swap partition that can be added in  like a normal swap. If you had a non-encrypted swap partition before, do not forget to disable it - or re-use its fstab entry by changing the device to . The default options should be sufficient for most usage. For other options and an explanation of each column, see  as well as point cryptsetup FAQ 2.3.

## By-id naming
To use a  persistent device naming instead of kernel simple naming, first identify the swap device:

Then use as a persistent reference for the  example partition (if two results are returned as above, choose either one of them):

After a reboot to activate the encrypted swap, you will note that running  shows an arbitrary device mapper entry (e.g. ) for it, while the  command shows crypt in the  column. Due to fresh encryption each boot, the UUID for  will change every time.

## UUID and LABEL
It is dangerous to use crypttab swap with simple kernel device names like  or even . A small change in your device names or partitioning layout and  will see your valuable data formatted on the next boot. Using a PARTLABEL or PARTUUID is safer, but it does not protect you if you then decide to use that partition for something else without removing the crypttab entry first.

It is more reliable to identify the correct partition by giving it a genuine UUID or LABEL. By default that does not work because dm-crypt and  would simply overwrite any content on that partition which would remove the UUID and LABEL too; however, it is possible to specify a swap offset. This allows you to create a very small, empty, bogus filesystem with no other purpose than providing a persistent UUID or LABEL for the swap encryption.

Create a filesystem with label of your choice:

 # mkfs.ext2 -L cryptswap /dev/sdX# 1M

The unusual parameter after the device name limits the filesystem size to 1 MiB, leaving room for encrypted swap behind it.

With this,  now can easily be identified either by UUID or LABEL, regardless of how its device name or even partition number might change in the future. All that is left are the  and  entries. For example, using different encryption options:

Note the offset: it is 2048 sectors of 512 bytes (it is not affected by the dm-crypt sector size), thus 1 MiB. This way the encrypted swap will not affect the filesystem LABEL/UUID, and data alignment works out as well.

Using this setup, the cryptswap will only try to use the partition with the corresponding LABEL, regardless of what its device name may be. Should you decide to use the partition for something else, by formatting it the cryptswap LABEL would also be gone, so  will not overwrite it on your next boot.

## Disabling hibernation
When hibernation is enabled, the Linux kernel will try to read the swap partition at boot time in order to check if the swap contains a valid hibernation image and load the image in memory. When the swap is encrypted with a one-time key, this procedure is useless and can cause latency at boot time.

If hibernation has been enabled on your kernel at compile time (HIBERNATION option enabled), then you can disable it at boot time by setting  on the kernel command line. This kernel parameter not only prevents resuming from swap (like older parameter ) but prevents both hibernation and resume. That way, your desktop won't propose you to hibernate on shutdown menu.

## With suspend-to-disk support
The following three methods are alternatives for setting up an encrypted swap for suspend-to-disk (hibernation). If you apply any of them, be aware that critical data swapped out by the system may potentially stay in the swap over a long period (i.e. until it is overwritten). To reduce this risk consider setting up a system job which re-encrypts swap, e.g. each time the system is going into a regular shut-down, along with the method of your choice.

## Using a swap file
A swap file can be placed in a file system within an encrypted device. Follow the swap file creation instructions in Swap#Swap file and set up hibernation according to Power management/Suspend and hibernate#Configure the initramfs.

When used with a systemd-based initramfs and an encrypted root filesystem, this can be a very simple and flexible method for encrypting swap. After setting up an encrypted root filesystem, the swap file can be made, activated, and added to  and work for hibernation without any further setup.

## Using a swap partition
Use  to create the encrypted container for the swap partition:

 # cryptsetup luksFormat --label swap /dev/device

Open the container to :

 # cryptsetup open /dev/disk/by-label/swap swap

Create a swap filesystem inside the mapped partition:

 # mkswap /dev/mapper/swap

Enable the mapped partition for paging:

 # swapon /dev/mapper/swap

If not using systemd#GPT partition automounting, add the mapped partition to  by adding the following line:

 /dev/mapper/swap none swap defaults 0 0

To set up your system to resume from hibernation, use the  kernel parameter. See Power management/Suspend and hibernate#Pass hibernate location to initramfs for details.

## Using a TPM
The following provides unattended swap decryption with a key stored in the TPM.

You can use systemd-cryptenroll to enroll the key to the Luks container and TPM, and wipe the previously created keyslot containing the password:

 # systemd-cryptenroll --tpm2-device auto /dev/device
 # systemd-cryptenroll --wipe-slot password /dev/device

Check the result with

 # systemd-cryptenroll /dev/device
 SLOT TYPE
    0 tpm2

## Using an additional passphrase or keyfile
The basic setup above has the disadvantage of having to insert an additional passphrase for the swap partition manually on every boot.

## Unlocking the partition in the initramfs
To resume from an encrypted swap partition, the encrypted partition must be unlocked in the initramfs.

## mkinitcpio
## systemd-based initramfs
When using the default systemd-based initramfs with the sd-encrypt mkinitcpio hook, either

* specify the appropriate  kernel parameters to unlock the swap partition, or
* edit  and regenerate the initramfs.

For example, for a TPM backed encrypted swap device:

## busybox-based initramfs
When using a busybox-based initramfs with the encrypt hook, follow the instructions below.

If the swap device is on a different device from that of the root file system, it will not be opened by the  hook, i.e. the resume will take place before  can be used, therefore it is required to create a hook in  to open the swap LUKS device before resuming.

Now you have to create a hook to open the swap at boot time. You can either install and configure , or follow the following instructions. Create a hook file containing the open command:

{{hc|/etc/initcpio/hooks/openswap|
run_hook ()
{
    cryptsetup open /dev/device swap
}
}}

for opening the swap device by typing your password or

{{hc|/etc/initcpio/hooks/openswap|2=
run_hook ()
{
    ## Optional: To avoid race conditions
    x=0;
    while [ ! -b /dev/mapper/root-device ] && [ $x -le 10 ]; do
       x=$((x+1))
       sleep .2
    done
    ## End of optional

    mkdir crypto_key_device
    mount -o ro,noload /dev/mapper/root-device crypto_key_device
    cryptsetup open --key-file crypto_key_device/path-to-the-key /dev/device swap
    umount crypto_key_device
}
}}

for opening the swap device by loading a keyfile from a crypted root device or

{{hc|/etc/initcpio/hooks/openswap|2=
run_hook ()
{
    ## Optional: To avoid race conditions
    x=0;
    while [ ! -b /dev/mapper/root-device ] && [ $x -le 10 ]; do
       x=$((x+1))
       sleep .2
    done
    ## End of optional

    dd if=/dev/mapper/root-device bs=key_size skip=block_number count=1 of=/swap-device.key
    cryptsetup open --key-file /swap-device.key /dev/device swap
    rm /swap-device.key
}
}}

for opening the swap device by extracting a keyfile directly from an encrypted root device without mounting it.

On ext4, the block number can be determined as follows:

 debugfs /dev/mapper/root-device
 extents /path/to/keyfile

The relevant block number will appear under the Physical column in the output.

In this case, the key should be no larger than a single block (4 KiB by default on ext4); otherwise, the file may become fragmented and unlocking may fail.

On some computers race conditions may occur when mkinitcpio tries to mount the device before the decryption process and device enumeration is completed. The commented Optional block will delay the boot process up to 2 seconds until the root device is ready to mount.

Then create and edit the hook setup file:
{{hc|/etc/initcpio/install/openswap|
build ()
{
   add_runscript
}
help ()
{
cat<<HELPEOF
  This opens the swap encrypted partition /dev/device in /dev/mapper/swap
HELPEOF
}
}}

Add the hook  in the  array in , before  but after . Do not forget to add the  hook after .

 HOOKS=(... encrypt openswap resume filesystems ...)

Regenerate the initramfs.

At boot time, the  hook will open the swap partition so the kernel resume may use it. If you use special hooks for resuming from hibernation, make sure they are placed after  in the  array. Please note that because of initramfs opening swap, there is no entry for swap in  needed in this case.

## dracut
Create a keyfile:

 # dd bs=512 count=4 if=/dev/random iflag=fullblock | install -m 0600 /dev/stdin /etc/cryptsetup-keys.d/swap.key

Add the keyfile to LUKS:

 # cryptsetup luksAddKey /dev/device /etc/cryptsetup-keys.d/swap.key

Configure dracut to include the  module and add the  file to the initramfs (See also dracut#Hibernation):

Regenerate the initramfs.

Add the  and  (replace the swap's partition UUID) entries to your kernel command line.
Your kernel command might look like this now:
 kernel /vmlinuz-linux cryptdevice=/dev/sda2:root root=/dev/mapper/root resume=/dev/mapper/swap rd.luks.name=fd839505-3213-4603-9a70-c5a96a24768f=swap rd.luks.key=/etc/cryptsetup-keys.d/swap.key ro

## LVM on LUKS
If the swap volume is in a volume group that gets activated in initramfs, simply follow the instructions in Power management/Suspend and hibernate#Hibernation.

## Known issues
*  in logs. See systemd issue 1620.

## Performance note
The above examples use AES-256-XTS, which is the same as cryptsetup's default algorithm for ordinary disk encryption. This algorithm is unlikely to be a performance bottleneck due to widespread AES acceleration in computers. That said, if a user really does have a very fast disk for swapping, one may want to use AES-128-XTS which is usually 40% faster due to a reduction in round count: replace  with . The key size and round count of AES-128 provides ample safety for non-quantum purposes, as Aumasson argued in Too Much Crypto. (A reduced-round-count AES-256-XTS would be the perfect combination of speed and quantum-safety, but it is not standard and hence not available.)
