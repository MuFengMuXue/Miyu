# Unified kernel image

A unified kernel image (UKI) is a single executable which can be booted directly from UEFI firmware, or automatically sourced by boot loaders with little or no configuration. It is the combination of a UEFI boot stub program like , a Linux kernel image, an initramfs, and further resources in a single UEFI PE file.

This file, and therefore all these elements can then easily be signed for use with Secure Boot.

## Preparing a unified kernel image
There are several ways to generate a UKI image and install it to the proper place (the esp/Linux directory). Currently several tools compete for doing this functionality, so choose one of the following based on your needs and your likings.

## mkinitcpio
mkinitcpio will assemble the UKI itself unless  is installed. In which case, UKI creation will be offloaded to ukify unless this is explicitly disabled with the   option. Note: when offloading to ukify mkinitcpio forcibly supplies it a configuration file from {{ic|{/etc,/usr/lib}/kernel/uki.conf}}.

## Kernel command line
mkinitcpio supports reading kernel parameters from command line files in the  directory. Mkinitcpio will concatenate the contents of all files with a .conf extension in this directory and use them to generate the kernel command line. Any lines in the command line file that start with a  character are treated as comments and ignored by mkinitcpio. Take care to remove entries pointing to microcode and initramfs.

For example:

Alternatively,  can be used to configure the kernel command line.

For example:

## .preset file
Next, modify , or the preset that you are using, as follows, with the appropriate mount point of the EFI system partition:

* Un-comment (i.e. remove ) the  parameter for each item in ,
* Optionally, comment out  to avoid storing a redundant  file,
* Optionally, add or un-comment the  parameter to each  line for which you want to add a splash image.

Here is a working example  for the  kernel and the Arch splash screen.

## pacman hook
Updates to systemd-stub (part of ), microcode (both  and ), and  kernel will automatically trigger a UKI rebuild. But you may want to review other pacman hooks in the  directory.

## Building the UKIs
Finally, make sure that the directory for the UKIs exists and regenerate the initramfs. For example, for the linux preset:

 # mkdir -p esp/EFI/Linux
 # mkinitcpio -p linux

Optionally, remove any leftover  from  or .

## kernel-install
Kernel-install is part of  and requires  to build unified kernel images. Make sure kernel-install is properly set up.

To generate UKIs, install  and set the  layout to :

Any configuration for #ukify must be done in  in order to be used by kernel-install, e.g.

Alternatively, for mkinitcpio to generate the UKI, set it as the default :

In that case,  is not necessary. You can also set a different , see .

Reinstall the kernel packages that you use in order for the change to take effect.

## dracut
See dracut#Unified kernel image and dracut#Generate a new initramfs on kernel upgrade.

## ukify
Install the  package. Since ukify cannot generate an initramfs on its own, if required, it must be generated using, e.g., dracut, mkinitcpio or booster.

A minimal working example can look something like this:

 # ukify build --linux=/boot/vmlinuz-linux \
               --initrd=/boot/initramfs-linux.img \
               --cmdline="quiet rw"

For further information, see .

## Manually
Put the kernel command line you want to use in a file, and create the bundle file using .

For microcode, first concatenate the microcode file and your initramfs, as follows:

 $ cat esp/cpu_manufacturer-ucode.img esp/initramfs-linux.img > /tmp/combined_initramfs.img

When building the unified kernel image, pass in  as the initramfs. This file can be removed afterwards.

{{bc|1=
$ align="$(objdump -p /usr/lib/systemd/boot/efi/linuxx64.efi.stub  awk '{ if ($1 == "SectionAlignment"){print $2} }')"
$ align=$((16#$align))
$ osrel_offs="$(objdump -h "/usr/lib/systemd/boot/efi/linuxx64.efi.stub"  awk 'NF==7 {size=strtonum("0x"$3); offset=strtonum("0x"$4)} END {print size + offset}')"
$ osrel_offs=$((osrel_offs + "$align" - osrel_offs % "$align"))
$ cmdline_offs=$((osrel_offs + $(stat -Lc%s "/usr/lib/os-release")))
$ cmdline_offs=$((cmdline_offs + "$align" - cmdline_offs % "$align"))
$ splash_offs=$((cmdline_offs + $(stat -Lc%s "/etc/kernel/cmdline")))
$ splash_offs=$((splash_offs + "$align" - splash_offs % "$align"))
$ initramfs_offs=$((splash_offs + $(stat -Lc%s "/usr/share/systemd/bootctl/splash-arch.bmp")))
$ initramfs_offs=$((initramfs_offs + "$align" - initramfs_offs % "$align"))
$ linux_offs=$((initramfs_offs + $(stat -Lc%s "initramfs-file")))
$ linux_offs=$((linux_offs + "$align" - linux_offs % "$align"))

$ objcopy \
    --add-section .osrel="/usr/lib/os-release" --change-section-vma .osrel=$(printf 0x%x $osrel_offs) \
    --add-section .cmdline="/etc/kernel/cmdline" \
    --change-section-vma .cmdline=$(printf 0x%x $cmdline_offs) \
    --add-section .splash="/usr/share/systemd/bootctl/splash-arch.bmp" \
    --change-section-vma .splash=$(printf 0x%x $splash_offs) \
    --add-section .initrd="initramfs-file" \
    --change-section-vma .initrd=$(printf 0x%x $initramfs_offs) \
    --add-section .linux="vmlinuz-file" \
    --change-section-vma .linux=$(printf 0x%x $linux_offs) \
    "/usr/lib/systemd/boot/efi/linuxx64.efi.stub" "linux.efi"
}}

A few things to note:

* The offsets are dynamically calculated so no sections overlap, as recommended in * The sections are aligned to what the  field of the PE stub indicates (usually 0x1000).
* The kernel image must be in the last section, to prevent in-place decompression from overwriting the sections that follow, as stated in [https://github.com/systemd/systemd/commit/0fa2cac4f0cdefaf1addd7f1fe0fd8113db9360b#commitcomment-84868898.

After creating the image, copy it to the EFI system partition:

 # cp linux.efi esp/EFI/Linux/

To create a UKI with xen, see == Signing the UKIs for Secure Boot ==

## sbctl
 provides a kernel-install script, a mkinitcpio post-hook, and pacman hooks to sign updated binaries.

## mkinitcpio
By using a mkinitcpio post hook, the generated unified kernel images can be signed for Secure Boot. Create the following file and make it executable:

Replace  and  with the paths to the key pair you want to use for signing the image.

## ukify
To automatically sign UKIs using , set the following in your configuration file (you can copy and edit the template from ):

## Booting
## Limine
Limine does not automatically detect unified kernel images (UKIs). However,  can be manually configured to load them.

Example 1: Booting a UKI from the default EFI system partition

If a UKI file is stored in , add the following configuration to :

Example 2: Booting a UKI from another partition

If a UKI file is located on a different FAT32 partition, use  with the PARTUUID instead:

For more details about supported paths and configuration options, see the [https://github.com/limine-bootloader/limine/blob/v8.x/CONFIG.md#Paths Limine Paths documentation.

## systemd-boot
systemd-boot searches in  for unified kernel images, and there is no further configuration needed. See

## rEFInd
rEFInd will autodetect unified kernel images on your EFI system partition, and is capable of loading them. They can also be manually specified in , by default located at:

{{hc|esp/EFI/refind/refind.conf|2=
menuentry "Arch Linux" {
    icon \EFI\refind\icons\os_arch.png
    ostype Linux
    loader \EFI\Linux\arch-linux.efi
}
}}

Keep in mind that no kernel parameters from  will be passed when booting this way. If the UKI was generated without a  section, specify the kernel parameters in the menu entry with an  line.

## GRUB
GRUB can chainload UKIs as described in GRUB#Chainloading a unified kernel image.

## Directly from UEFI
efibootmgr can be used to create a UEFI boot entry for the .efi file:

 # efibootmgr --create --disk /dev/sdX --part partition_number --label "Arch Linux" --loader '\EFI\Linux\arch-linux.efi' --unicode

See  for an explanation of the options.
