# Mkinitcpio

mkinitcpio is a Bash script used to create initramfs images. There are two distinct approaches how the various tasks during initial ramdisk phase are performed:

; systemd-based initial RAM file system
: systemd is already started at the beginning of the initial ramdisk phase. The tasks to be executed are determined by regular systemd unit files. See systemd bootup process.
: Pros:
:* Tightly integrated with the rest of the systemd ecosystem, leading to a more consistent and streamlined boot process.
:* Parallelize certain boot tasks more effectively, potentially leading to faster overall boot times in some scenarios.
:* More comprehensive set of features like systemd-cryptsetup-generator with  or GPT partition automounting.
: Cons:
:* More dependencies and larger size: Generally results in a larger initramfs due to the inclusion of systemd binaries and its dependencies. This can slightly increase boot time.

; Busybox-based initial RAM file system
: An init script is started that in turn scans the filesystem of the initial ramdisk for scripts to be executed (here in this context called runtime hooks).
: Pros:
:* Lightweight and smaller in size, fewer dependencies.
:* The init script and runtime hooks are executed sequentially, making it easier to identify which step caused problems during boot.

The concrete variant is determined by the presence or absence of the  hook in the  array of . See #Hook list for more details.

mkinitcpio has been developed by the Arch Linux developers and from community contributions.

## Installation
The  package is a dependency of the kernel packages, so most users will already have it installed.

## Image creation and activation
## Automated generation
Every time a kernel is installed or upgraded, a pacman hook automatically generates a .preset file saved in . For example  for the official stable  kernel package. A preset is simply a list of information required to create initial ramdisk images, instead of manually specifying the various parameters and the location of the output files. By default, it contains the instructions to create only the first image, the second one must be explicitly enabled:

# The default ramdisk image created following the directives specified in the configuration.
# The fallback ramdisk image, same as above except that the autodetect hook is skipped during creation, thus including a full range of modules which supports most systems.

After creating the preset, the pacman hook calls the mkinitcpio script which generates the image(s), using the information provided in the preset.

## Manual generation
To run the script manually, refer to the  manual page for instructions. In particular, to (re-)generate an initramfs image based on the preset provided by a kernel package, use the / option followed by the preset to utilize. For example, for the  package, use the command:

 # mkinitcpio -p linux

To (re-)generate initramfs images based on all existing presets, use the / switch. This is typically used to regenerate all the initramfs images after a change of the global configuration:

 # mkinitcpio -P

Users may create any number of initramfs images with a variety of different configurations. The desired image must be specified in the respective boot loader configuration file.

## Customized generation
Users can generate an image using an alternative configuration file. For example, the following will generate an initial ramdisk image according to the directions in  and save it as .

 # mkinitcpio --config /etc/mkinitcpio-custom.conf --generate /boot/initramfs-custom.img

If generating an image for a kernel other than the one currently running, add the kernel release version to the command line. The installed kernel releases can be found in , the syntax is consistent with the output of the command  for each kernel.

 # mkinitcpio --generate /boot/initramfs-custom2.img --kernel 5.7.12-arch1-1

## Unified kernel images
mkinitcpio can create unified kernel images (UKIs) either by itself or via . If  is absent or explicitly disabled using , the UKI will be assembled by mkinitcpio itself. Advanced features of ukify will not be available then.

See unified kernel image for details about UKI generation.

## Configuration
The primary configuration file for mkinitcpio is . Drop-in configuration files are also supported, e.g.  (they aren't taken into account if mkinitcpio is called with / option and/or use a preset containing ). Additionally, preset definitions are provided by kernel packages in the  directory (e.g. ).

Users can modify seven variables within the configuration file, see  for more details:

; : Kernel modules to be loaded before any boot hooks are run.
; : Additional binaries to be included in the initramfs image.
; : Additional files to be included in the initramfs image.
; : Hooks are scripts that execute in the initial ramdisk.
; : Used to compress the initramfs image.
; : Extra arguments to pass to the  program. Usage of this setting is strongly discouraged. mkinitcpio will handle special requirements for compressors (e.g. passing  to xz), and misusage can easily lead to an unbootable system.
; : Whether to decompress loadable kernel modules and firmware files or to keep them in their original compressed form.

## MODULES
The  array is used to specify modules to load before anything else is done.

Modules suffixed with a  will not throw errors if they are not found. This might be useful for custom kernels that compile in modules which are listed explicitly in a hook or configuration file.

## BINARIES and FILES
These options allow users to add files to the image. Both  and  are added before hooks are run, and may be used to override files used or provided by a hook.  are auto-located within a standard  and are dependency-parsed, meaning any required libraries will also be added.  are added as-is. For example:

 FILES=(/etc/modprobe.d/modprobe.conf)

 BINARIES=(kexec)

Note that as both  and  are Bash arrays, multiple entries can be added delimited with spaces.

## HOOKS
The  array is the most important setting in the file. Hooks are small scripts describing what will be added to the initramfs image. Some hooks are accompanied by a so-called runtime hook providing startup functionality, such as starting a daemon, or assembling a stacked block device.

Hooks are referred to by their name, and executed in the order they are listed in the  array of the configuration file. The recommended order of the hook list should be followed unless you know what you are doing.

The default  setting should be sufficient for most simple, single disk setups. For root filesystems based on stacked devices or spanning multiple devices such as LVM, RAID, or dm-crypt, see the respective wiki pages for further necessary configuration.

## Build hooks
Build hooks (aka install hooks) are shell script files sourced by the bash shell during execution of mkinitcpio and usually contain two functions:  and . The  function describes the modules, binaries and other files to be added to the initramfs image. An API, documented by , serves to facilitate the addition of these items. The  function outputs a short description about functionality and usage of the hook.

For a list of all available hooks:

 $ mkinitcpio -L

Use mkinitcpios / option to output help for a specific hook, for example:

 $ mkinitcpio -H udev

Build hooks are located in , custom build hooks can be placed in .

## Runtime hooks
Each build hook listed in the  array may be accompanied by zero or one runtime hook of the same name. Runtime hooks are shell scripts sourced by the busybox  shell during initramfs phase. They are responsible for startup tasks such as starting a daemon, or assembling a stacked block device. A build hook installs the corresponding runtime hook by calling . Runtime hooks may contain several functions:

: Functions of this name will be run once the API file systems have been mounted and the kernel command line has been parsed. This is generally where additional daemons, such as udev, which are needed for the early boot process are started from.

: Functions of this name are run shortly after the early hooks. This is the most common hook point, and operations such as assembly of stacked block devices should take place here.

: Functions of this name are run after the root device has been mounted. This should be used, sparingly, for further setup of the root device, or for mounting other file systems, such as .

: Functions of this name are run as late as possible, and in the reverse order of how they are listed in the  array in the configuration file. These hooks should be used for any last minute cleanup, such as shutting down any daemons started by an early hook.

With the exception of , these functions are executed in the order the corresponding build hooks are listed in the  array. Runtime hooks are located in , custom runtime hooks can be placed in .

## Post hooks
Post hooks are shell scripts or executables run after an image has been (re)generated in order to perform additional tasks like signing.

To each executable the following arguments are passed in this order:

# the kernel used (may be empty in some circumstances);
# the generated initramfs image;
# (optional) the generated unified kernel image.

Additionally, the following environment variables are set:

 the full kernel version.

 the default location where the kernel should be located on order to be booted.

Post hooks are located in  (hooks provided by packages) and  (custom hooks).

## Hook list
A table of hooks and how they affect image creation and runtime follows.

{| class="wikitable"
! busybox init !! systemd init !! Build hook !! Runtime hook (busybox init only)
|-
|  ||  || Sets up all initial directories and installs base utilities and libraries. Always keep this hook as the first hook unless you know what you are doing, as it provides critical busybox init when not using systemd hook.

Optional when using the systemd hook as it only provides a busybox recovery shell. In addition to enabling base, you'll need to add  to your kernel parameters to use the shell.
|
|-
|  ||rowspan="3"  || Adds udevd, udevadm, and a small subset of udev rules to your image. || Starts the udev daemon and processes uevents from the kernel; creating device nodes. As it simplifies the boot process by not requiring the user to explicitly specify necessary modules, using it is recommended.
|-
|  || Adds support for  on a separate partition. See #/usr as a separate partition for details. || Mounts the  partition after the real root has been mounted.
|-
|-
|  || Adds  and  kernel modules to allow resuming when using a hibernation image compression algorithm other than the compile-time default. Adds the  binary to support resuming from a hibernation image specified via the  UEFI variable. || Tries to resume from the "suspend to disk" state. See Hibernation for further configuration.
|-
|  ||  || Sets the required modules to enable Btrfs for using multiple devices with Btrfs. You need to have  installed to use this. This hook is not required for using Btrfs on a single device where the  hook suffices. || Runs  to assemble a multi-device Btrfs root file system when udev hook or systemd hook is not present. The  package is required for this hook.
|-
|colspan="2"  || Shrinks your initramfs to a smaller size by creating a whitelist of modules from a scan of sysfs. Be sure to verify included modules are correct and none are missing. This hook must be run before other subsystem hooks in order to take advantage of auto-detection. Any hooks placed before 'autodetect' will be installed in full. ||
|-
|colspan="2"  || Prepends an uncompressed initramfs image with early microcode update files for Intel and AMD processors. Uses microcode files from  and  if they are available or extracts  and  otherwise.

If the autodetect hook runs before this hook, it will only add early microcode update files for the processor of the system the image is built on.

The use of this hook replaces the now deprecated  flag, and the  option in the preset files. This also allows you to drop the microcode  lines from your boot configuration as they are now packed together with the main initramfs image.
|
|-
|colspan="2"  || Includes modprobe configuration files from  and . ||
|-
|colspan="2"  || Adds GPU modules to provide early KMS start. Additionally adds modules that are required by privacy screens built into the LCD panel of some laptops. ||
|-
|colspan="2"  || Adds the necessary modules for keyboard devices. Use this if you have a USB or serial keyboard and need it in early userspace (either for entering encryption passphrases or for use in an interactive shell). As a side effect, modules for some non-keyboard input devices might be added too, but this should not be relied on.

|
|-
|  ||rowspan="2"  || Adds the specified console keymap(s) from  to the initramfs. If you use system encryption, especially full-disk encryption, make sure you add it before the  hook. || Loads the specified console keymap(s) from  during early userspace.
|-
|  || Adds the specified console font from  to the initramfs. || Loads the specified console font from  during early userspace.
|-
|colspan="2"  || Adds block device modules. If the autodetect hook runs before this hook, it will only add modules for block devices used on the system. Exceptions are the , , , , , ,  and  modules which will always be added unconditionally. ||
|-
|  ||  || Adds the necessary modules for a network device. You must have  installed to use this, see #Using net for details. || Provides handling for an NFS-based root file system.
|-
|  ||  || Provides support for fakeRAID root devices. You must have  installed to use this. Note that it is preferred to use mdadm with the mdadm_udev hook with fakeRAID if your controller supports it. See #Using RAID for details. || Locates and assembles fakeRAID block devices using .
|-
|colspan="2"  || Provides support for assembling RAID arrays via udev. You must have  installed to use this. See RAID#Configure mkinitcpio for details. ||
|-
|  ||  || Adds the  kernel module and the  tool to the image. You must have  installed to use this.  || Detects and unlocks an encrypted root partition. See #Runtime customization for further configuration.
For sd-encrypt see dm-crypt/System configuration#Using systemd-cryptsetup-generator.
|-
|colspan="2"  || Adds the device mapper kernel module and the  tool to the image. You must have  installed to use this. This is necessary if you have your root file system on LVM. ||
|-
|colspan="2"  || This includes necessary file system modules into your image. This hook is required unless you specify your file system modules in . ||
|-
|colspan="2"  || Adds the fsck binary and file system-specific helpers to allow running fsck against your root device (and  if separate) prior to mounting. If added after the autodetect hook, only the helper specific to your root file system will be added. Usage of this hook is strongly recommended, and it is required with a separate  partition. It is highly recommended that if you include this hook that you also include any necessary modules to ensure your keyboard will work in early userspace.

The use of this hook requires the  parameter to be set on the kernel command line (discussion). See fsck#Boot time checking for more details.
|
|-
|colspan="2"  || Adds ACPI Machine Language (.aml) files found in  and  to the early uncompressed initramfs image so that the kernel can override ACPI tables (e.g. DSDT) very early during boot.||
|}

## COMPRESSION
The kernel supports several formats for compression of the initramfs: , , lzma (), , lzo (),  and . By default mkinitcpio uses zstd compression for kernel version 5.9 and newer and gzip for kernel versions older than 5.9.

The provided  has the various  options commented out. Uncomment one if you wish to switch to another compression method and make sure you have the corresponding compression utility installed. If none is specified, the default method is used. If you wish to create an uncompressed image, specify  in the configuration file or use  on the command line.

## COMPRESSION_OPTIONS
These are additional flags passed to the program specified by , such as:

 COMPRESSION_OPTIONS=(-9)

This option can be left empty; mkinitcpio will ensure that any supported compression method has the necessary flags to produce a working image.

With the default zstd compression, to save space for custom kernels (especially with a dual boot setup when using the EFI system partition as ), the  option is very effective. However, systems with limited RAM may not be able to decompress initramfs using this option. The  option may also be desired to see details during the initramfs generation. For example:

 COMPRESSION="zstd"
 COMPRESSION_OPTIONS=(-v -5 --long)

Highest, but slowest, compression can be achieved by using xz with the  compression level and also decompressing the loadable kernel modules and firmware:

 COMPRESSION="xz"
 COMPRESSION_OPTIONS=(-9e)
 MODULES_DECOMPRESS="yes"

## MODULES_DECOMPRESS
 controls whether the kernel module and firmware files are decompressed during initramfs creation. The default value is .

Arch compresses its kernel modules and  with zstd at level 19. When using a higher compression than that for the initramfs, setting  will allow to reduce the initramfs size even further. This comes at the expense of increased RAM and CPU usage at early boot which negatively affects systems with limited RAM or weak CPUs since the kernel will spend more time to decompress the whole initramfs image than it would take to decompress the individual modules and firmware upon loading them.

## Runtime customization
Runtime configuration options can be passed to  and certain hooks via the kernel command line. Kernel command-line parameters are often supplied by the boot loader. The options discussed below can be appended to the kernel command line to alter default behavior. See Kernel parameters and Arch boot process for more information.

## init from base hook
; : This is the most important parameter specified on the kernel command line, as it determines what device will be mounted as your proper root device. mkinitcpio is flexible enough to allow a wide variety of formats; see Persistent block device naming#Kernel parameters for examples.

; : If  or  is specified,  pauses the boot process (after loading hooks, but before mounting the root file system) and launches an interactive shell which can be used for troubleshooting purposes. This shell can be launched after the root has been mounted by specifying . Normal boot continues after exiting from the shell.

; : Disable hooks at runtime by adding . For example:

; : Alter the order in which modules are loaded by specifying modules to load early via . (This may be used, for example, to ensure the correct ordering of multiple network interfaces.)

See Boot debugging and  for other parameters.

## Using RAID
See RAID#Configure mkinitcpio.

## Using net
Required packages

 requires the  package.

Kernel parameters

Comprehensive and up-to-date information can be found in the official [https://docs.kernel.org/admin-guide/nfs/nfsroot.html kernel documentation.

ip=

This parameter tells the kernel how to configure IP addresses of devices and also how to set up the IP routing table. It can take up to nine arguments separated by colons: .

If this parameter is missing from the kernel command line, all fields are assumed to be empty, and the defaults mentioned in the kernel documentation apply. In general this means that the kernel tries to configure everything using autoconfiguration.

The  parameter can appear alone as the value to the  parameter (without all the  characters before). If the value is  or , no autoconfiguration will take place, otherwise autoconfiguration will take place. The most common way to use this is .

For parameters explanation, see the kernel documentation.

Examples:

 ip=127.0.0.1:::::lo:none  --> Enable the loopback interface.
 ip=192.168.1.1:::::eth2:none --> Enable static eth2 interface.
 ip=:::::eth0:dhcp --> Enable dhcp protocol for eth0 configuration.

BOOTIF=

If you have multiple network cards, this parameter can include the MAC address of the interface you are booting from. This is often useful as interface numbering may change, or in conjunction with pxelinux IPAPPEND 2 or IPAPPEND 3 option. If not given,  will be used.

Example:

 BOOTIF=01-A1-B2-C3-D4-E5-F6  # Note the prepended "01-" and capital letters.

nfsroot=

If the  parameter is NOT given on the command line, the default  will be used.

 nfsroot=Run  for parameter explanation.

## Using LVM
If your root device is on LVM, see Install Arch Linux on LVM#Adding mkinitcpio hooks.

## Using encrypted root
If using an encrypted root see dm-crypt/System configuration#mkinitcpio for detailed information on which hooks to include.

## /usr as a separate partition
If you keep  as a separate partition, you must adhere to the following requirements:

* Add the  hook, mark  with a  of  in  to run the check on the partition at startup. While recommended for everyone, it is mandatory if you want your  partition to be fsck'ed at boot-up. Without this hook,  will never be fsck'd.
* If not using the systemd hook, add the  hook. This will mount the  partition after root is mounted.

## Tips and tricks
## Fallback initramfs generation
Fallback initramfs generation is disabled by default. To enable it:

* Adjust the respective .preset files in
** Disable  and enable  instead
** Enable
** Enable
* Regenerate initramfs
* Update your boot loader configuration.

## Troubleshooting
## Extracting the image
If you are curious about what is inside the initramfs image, you can extract it and poke at the files inside of it.

The initramfs image is an SVR4 CPIO archive, generated via the find and bsdcpio commands, optionally compressed with a compression scheme understood by the kernel. For more information on the compression schemes, see #COMPRESSION.

The  package includes a utility called  which will list and/or extract the contents of initramfs images.

You can list the files in the image with:

 # lsinitcpio /boot/initramfs-linux.img

And to extract them all in the current directory:

 # lsinitcpio --extract /boot/initramfs-linux.img

You can also get a human-friendly listing of the important parts of the image (kernel version, early CPIO presence, included modules and binaries, etc.):

 # lsinitcpio --analyze /boot/initramfs-linux.img

## Recompressing a modified extracted image
Invoke the  function of the  script with parameters

 build_image outfile compression

It can be done by creating a new script with the contents of the  function and running it with the above parameters.
This will compress the contents present in the current directory in a file named .

## "/dev must be mounted" when it already is
The test used by mkinitcpio to determine if  is mounted is to see if  is there. If everything else looks fine, it can be "created" manually by:

 # ln -s /proc/self/fd /dev/

(Obviously,  must be mounted as well. mkinitcpio requires that anyway, and that is the next thing it will check.)

## Possibly missing firmware for module XXXX
When initramfs are being rebuilt after a kernel update, you might get warnings:

 ==> WARNING: Possibly missing firmware for module: module_name

If these messages appear when generating a default initramfs image, then, as the warning says, installing additional firmware may be required. Most common firmware files can be acquired by installing the  package. For other packages providing firmware see the table below or try searching for the module name in the official repositories or AUR.

Otherwise, if the messages only appear when generating the fallback initramfs image you have the following options:

* You can safely ignore the warnings, if you know that you do not use the affected hardware.
* If you want to suppress the warnings, you can install the missing firmware. The meta-package  contains most optional firmwares. Alternatively, manually install the needed packages:
:{| class="wikitable"
|-
! Module !! Package
|-
| aic94xx        ||
|-
| ast            ||
|-
| bfa            ||
|-
| bnx2x          ||
|-
| liquidio       ||
|-
| mlxsw_spectrum ||
|-
| nfp            ||
|-
| qat_420xx      ||
|-
| qed            ||
|-
| qla1280        ||
|-
| qla2xxx        ||
|-
| wd719x         ||
|-
| xhci_pcixhci_pci_renesas ||
|}
* If you want to get rid of the warnings, but do not want to waste your system space on unneeded firmware packages, you can disable fallback initramfs generation altogether.

For unavailable firmware, you can suppress the warnings by creating dummy files, e.g.:

 # echo 'Silence the "Possibly missing firmware for module" message' \
     | tee /usr/lib/firmware/qat_6xxx{,_mmp}.bin >/dev/null

## No PS/2 controller found
On some motherboards (mostly ancient ones, but also a few new ones), the i8042 controller cannot be automatically detected. It is rare, but some people will surely be without keyboard. You can detect this situation in advance. If you have a PS/2 port and get  message, add  to the  array.[https://archlinux.org/news/linux-313-warning-ps2-keyboard-support-is-now-modular/

## Boot succeeds on one machine and fails on another
mkinitcpios  hook filters unneeded kernel modules in the primary initramfs scanning  and the modules loaded at the time it is run. If you transfer your  directory to another machine and the boot sequence fails during early userspace, it may be because the new hardware is not detected due to missing kernel modules. Note that USB 2.0 and 3.0 need different kernel modules.

To fix, first try choosing the fallback image from your boot loader, as it is not filtered by . Once booted, run mkinitcpio on the new machine to rebuild the primary image with the correct modules. If the fallback image fails, try booting into an Arch Linux live CD/USB, chroot into the installation, and run mkinitcpio on the new machine. As a last resort, try manually adding modules to the initramfs.

## Cannot open access to console, the root account is locked
The  hook disables the root account. To enable the emergency shell, temporarily add  to the kernel parameters.

Alternatively, you can use , by installing it and adding the  hook after  in , and regenerating initramfs with . More documentation is available in its GitHub repo.
