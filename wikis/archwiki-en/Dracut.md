# Dracut

dracut creates an initial image used by the kernel for preloading the block device modules (such as IDE, SCSI or RAID) which are needed to access the root filesystem. Upon installing , you can choose between mkinitcpio, booster, and dracut. dracut is used by Fedora, RHEL and Gentoo, among others. Arch uses mkinitcpio by default.

You can read the full project documentation for dracut in the documentation.

## Installation
Install the  package.

## Usage
 is easy to use and typically does not require user configuration, even when using non-standard setups, like LVM on LUKS.

To generate an initramfs for the running kernel:

 # dracut --add-confdir no-network /boot/initramfs-linux.img

To generate a fallback initramfs run:

 # dracut -f --add-confdir rescue /boot/initramfs-linux-fallback.img

Note that starting from v108 of dracut, in usual configuration fallback initramfs should not be needed as the default initramfs has most of the kernel drivers already included.

 refers to the output image file. If you are using an other kernel, consider changing the file name. For example, for the  kernel, the output file should be named . However, you can name these files whatever you wish as long as your boot loader configuration uses the same file names.

## Additional options
The  flag overwrites the image file if it is already present.

The  option specifies which kernel to use. The argument to this option must match the name of a directory present in .

More flags can be found with .

## Advanced configuration
It is important to note that there are two distinct approaches how the various tasks during initial ramdisk phase are performed:

; Shell (bash/busybox/dash) based initial ramdisk: An init script is started that in turn scans the filesystem of the initial ramdisk for dracut scripts to be executed.

; systemd based (default) initial ramdisk: systemd is already started at the beginning of the initial ramdisk phase. The tasks to be executed are determined by regular systemd unit files. See systemd bootup process.

The concrete variant is determined by the absence or presence of the systemd dracut module. See #dracut modules for more details.

 can be configured by directly passing arguments on the command line (see ). If you wish to always execute  with a certain set of flags, you can save a specified configuration in a  file in . For example:

You can see more configuration options with . Fuller descriptions of each option can be found with . We will describe a few common options in what follows.

## dracut modules
dracut uses a modular approach to build the initramfs (see ). All of dracut 's builtin modules are located in  and can be listed with . Extra modules can be provided by external packages e.g. . dracut 's built-in modules unfortunately lack documentation, although their names can be self-explanatory.

Some of the modules are active/inactive by default, and can be activated/deactivated with / command line argument or with the / persistent config entry lines.

For dracut module documentation, see the upstream dracut documentation.

Most dracut modules are dependent on other dracut modules. As an example the bluetooth dracut module depends on the dbus dracut module.

## TPM2
To make use of systemd 's unlocking of luks2 encrypted volumes using TPM2 through systemd-cryptenroll, install  package and enable the  dracut module.

## Early kernel module loading
Dracut enables early loading (at the initramfs stage, via ) through its  command or  config entry line. For example:

## Kernel command line options
Kernel command line options can be placed in a .conf file in , and set via the  flag. Dracut will automatically source this file and create a  file and place it inside the initramfs directory . For example, your kernel command line options file could look like:

## Miscellaneous notes
It is not necessary to specify the root block device for . From :

: The root device used by the kernel is specified in the boot configuration file on the kernel command line, as always.

However, it may be useful to set some parameters early, and you can enable additional features like prompting for additional command line parameters. See  for all options. Here are some example configuration options:

* Resume from a swap partition:
* Prompt for additional kernel command line parameters:
* Print informational output even if  is set:

## Unified kernel image
dracut can produce unified kernel images with the  command line option or with the  configuration option.

## Tips and tricks
## View information about generated image
You can view information about a generated initramfs image, which you may wish to view in a pager:

 # lsinitrd /path/to/initramfs_or_uefi_image | less

This command will list the arguments passed to  when the image was created, the list of included  modules, and the list of all included files.

## Change compression program
To reduce the amount of time spent compressing the final image, you may change the compression program used.

Simply add any one of the following lines (not multiple) to your dracut configuration:

 compress="cat"
 compress="gzip"
 compress="bzip2"
 compress="lzma"
 compress="xz"
 compress="lzo"
 compress="lz4"
 compress="zstd"

 is the default compression program used.  will make the initramfs with no compression.

You can also use a non-officially-supported compression program:

 compress="program"

## Performance considerations
Some considerations to optimize the boot and initramfs creation performance are:

* Understand and configure the fastest compression. If the kernel modules are already compressed, perhaps there is no need to re-compress the initramfs on creation.

* Understand the impact of including systemd into your initramfs. If it slows things down, omit it. If it makes things faster, include it.

* Consider using dracut-cpio when using a copy-on-write filesystem. See the  option for applicability.

* Minimize the number of kernel modules and dracut modules included in initramfs. As an example: If  is installed (but not required to boot), then you need to explicitly omit the nfs dracut module, otherwise network boot will be enabled in the generated initramfs in default configuration - see https://github.com/dracut-ng/dracut-ng/pull/297.

* Consider adding  dracut module to replace bash.

* Consider  and .

## Generate a new initramfs on kernel upgrade
The  package include hooks for pacman to automatically generate new initramfs images upon each kernel upgrade.

If KERNEL_INSTALL_INITRD_GENERATOR is set on the host system the dracut hook will not generate an initramfs with dracut.

You should stop mkinitcpio from creating and removing initramfs images as well, either by removing  or with the following commands:

 # ln -sf /dev/null /etc/pacman.d/hooks/90-mkinitcpio-install.hook
 # ln -sf /dev/null /etc/pacman.d/hooks/60-mkinitcpio-remove.hook

## Bluetooth keyboard support
Dracut will enable the  module automatically when a Bluetooth keyboard is detected. To enforce the module addition see Dracut#dracut_modules.

However it is required that dracut is in hostonly mode for dracut to auto-discover bluetooth keyboard.

## Limine boot loader support
The  package utilizes limine-entry-tool with dracut and pacman hooks to automate the installation and removal of kernels and boot entries in the Limine boot loader. See Limine#Boot entry automation for more information.

## Troubleshooting
## Hibernation
If resuming from hibernation does not work, you may need to configure  to include the  module. You will need to add a configuration file:

If applicable to your system, you may also want to see instructions to resume from an encrypted swap partition including the dracut specific instructions.

## LVM / software RAID / LUKS
If the kernel has issues auto discovering and mounting LVM / software RAID / LUKS blocks. You can retry generating an initramfs with the following kernel command line options:

 rd.auto rd.lvm=1 rd.dm=1 rd.md=1 rd.luks=1

## A stop job is running for "brltty"
If you have issues booting or very long shutdown processes while the system waits for , add the following to the dracut configuration line:

 omit_dracutmodules+=" brltty "

Alternatively, uninstall  if it is not needed.

## No usable keyslot is available
 Cannot use whirlpool hash for keyslot encryption.
 Keyslot open failed.
 No usable keyslot is available.

A failure to boot with a message similar to the above typically will only require the user to include the  module via .
