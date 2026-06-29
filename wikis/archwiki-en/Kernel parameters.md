# Kernel parameters

There are three ways to pass options to the kernel and thus control its behaviour:

# When building the kernel—in the kernel's  file. See Kernel#Compilation for details.
# When starting the kernel—using command line parameters (usually through a boot loader, or as well in unified kernel image).
# At runtime—through the files in  (see sysctl) and .

Between the three methods, the configurable options differ in availability, their name and the method in which they are specified. This page only explains the second method (kernel command line parameters) and shows a list of the most used kernel parameters in Arch Linux.

Most parameters are associated with subsystems and work only if the kernel is configured with those subsystems built in. They also depend on the presence of the hardware they are associated with.

Kernel command line parameters either have the format , or , or .

## Boot loader configuration
Kernel parameters can be set either temporarily by editing the boot entry in the boot loader boot selection menu, or permanently by modifying the boot loader configuration file.

The following examples add the  and  parameters to the Clover, GRUB, GRUB Legacy, LILO, Limine, rEFInd, Syslinux and systemd-boot boot loaders.

## Clover
* Add them to :

:

## GRUB
* Press  when the menu shows up and add them on the  line:

:

: Press  to boot with these parameters.

* To make the change persistent after reboot, you could manually edit /boot/grub/grub.cfg with the exact line from above, or if using grub-mkconfig:

:Edit  and append your kernel options between the quotes in the  line:

::

:And then automatically re-generate the  file with:

::

## GRUB Legacy
* Press  when the menu shows up and add them on the  line:

:

: Press  to boot with these parameters.

* To make the change persistent after reboot, edit  and add them to the  line, exactly like above.

## LILO
* Add them to  using  or :

:

## Limine
* To temporarily add kernel parameters, press  when the boot entry selection screen appears and modify the  line:

:

* To apply changes permanently, edit the  line in the Limine configuration file:

:
:  is alias of

## rEFInd
* Press , , , or  on the desired menu entry and press it again on the submenu entry. Add kernel parameters at the end of the string:

:

: Press  to boot with these parameters.

* To make the change persistent after reboot, edit  and append them between the quotes in all required lines, for example

:

* If you have disabled auto-detection of OSes in rEFInd and are defining OS stanzas instead in  to load your OSes, you can edit it like:

: {{bc|
menuentry "Arch Linux" {
    ...
    options  "root=UUID=0a3407de-014b-458b-b5c1-848e92a327a3 rw quiet splash"
    ...
}
}}

## Syslinux
* Press  when the menu shows up and add them at the end of the string:

:

: Press  to boot with these parameters.

* To make the change persistent after reboot, edit  and add them to the  line:

:

## systemd-boot
* Press  when the menu appears and add the parameters to the end of the string:

:

: Press  to boot with these parameters.

* To make the change persistent after reboot, edit  (assuming you set up your EFI system partition) and add them to the  line:

:

* If you are using a unified kernel image to boot, edit .

## dracut
dracut is capable of embedding the kernel parameters in the initramfs, thus allowing to omit them from the boot loader configuration. See dracut#Kernel command line options. Note that this only works for parameters understood by dracut, like  and . They do not become real kernel parameters.

## EFI boot stub
See EFI boot stub#Using UEFI directly.

## Hijacking cmdline
Even without access to your boot loader it is possible to change your kernel parameters to enable debugging (if you have root access). This can be accomplished by overwriting  which stores the kernel parameters. However  is not writable even as root, so this hack is accomplished by using a bind mount to mask the path.

First create a file containing the desired kernel parameters:

Then use a bind mount to overwrite the parameters:

 # mount --bind -o ro /root/cmdline /proc/cmdline

You can  to confirm that your change was successful.

## Parameter list
This list is not comprehensive. In addition to the kernel itself, other programs can also read parameters from  and change their behavior.

* For a mostly complete list of options understood by the kernel and boot loaders, see The kernel's command-line parameters. A basic list is in .
* For options understood by systemd, see .
* For options understood by mkinitcpio with a busybox based initial ramdisk, see  and Mkinitcpio#Runtime customization.
* For options understood by dracut, see .

{| class="wikitable"
!parameter!!Description
|-
| init || Run specified binary instead of  as init process. The  package symlinks  to  to use systemd. Set it to  to boot to the shell.
|-
| initrd || Specify the location of the initial ramdisk. For UEFI boot managers and an EFI boot stub, the path must be specified using backslashes () as path separators.
|-
| cryptdevice || Specify the location of a dm-crypt-encrypted partition plus a device mapper name.
|-
| debug || Enable kernel debugging (events log level).
|-
| lsm || Set the initialisation order of the Linux security modules, used to enable AppArmor, SELinux or TOMOYO.
|-
| maxcpus || Maximum number of processors that an SMP kernel will bring up during bootup.
|-
| mem || Force usage of a specific amount of memory to be used.
|-
| netdev || Network devices parameters.
|-
| nomodeset || Disable Kernel mode setting.
|-
| panic || Time before automatic reboot on kernel panic.
|-
| resume || Specify a swap device to use when waking from hibernation.
|-
| ro || Mount root device read-only on boot. This is mkinitcpio's default1.
|-
| root || Root file system. See init/do_mounts.c for kernel's supported device name formats. Note that an initramfs with udev supports more name formats. A setup compatible with systemd#GPT partition automounting allows to omit the parameter entirely or to alternatively use .
|-
| rootflags || Root file system mount options. Useful for setting options that cannot be applied by remounting (i.e. by ). For example, the  option of an XFS root volume or  option of Btrfs when using a subvolume as root.
|-
| rw || Mount root device read-write on boot. This is the kernel's default1.
|-
| systemd.unit || Boot to a specified target.
|-
| video || Override framebuffer video defaults.
|}

# The kernel uses  if neither  or  are explicitly set on kernel command line (see ). However, mkinitcpio uses  as the default value overriding the kernel's default (see ). Boot loaders may also have their own configured default, for example, grub-mkconfig uses  (see  as a reference).
