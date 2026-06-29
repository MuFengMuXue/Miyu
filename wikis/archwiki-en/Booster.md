# Booster

Booster is a fast initramfs generator similar to mkinitcpio and dracut.
Booster is inspired by the "distri" project and aims to create a small and fast init image.

Booster provides the  user-space tool, responsible for initramfs image generation. The generated images are located at  by default.

## Install
Install . The package installation hook will generate initramfs images, one per installed kernel (e.g. for , ). The images are located under  directory:

## Usage
When configuration is done to Booster, the initramfs images need to be regenerated for the changes to take affect. To do so, see the examples below.

Booster offers a convenience script that iterates over all installed kernels and generates an image for each of them:

 # /usr/lib/booster/regenerate_images

Alternatively, you can generate images manually by calling booster directly with the build argument:

 $ booster build mybooster.img

This will build an initramfs image in your current directory. Do note that it may require elevated privileges depending on where it is being run on the file system.

## Configuration
Booster's generator configuration file is located at . If there is no configuration file then the default configuration (host-specific images, no network) is used.

The configuration file helps to override the default behaviour. See  for detailed information.

## Early module loading
You can load some modules at initramfs stage forcibly.

For example, if you need Kernel mode setting#Early KMS start to avoid graphical session run before NVIDIA GPU is initialized, use the following configuration setting:

And then regenerate booster images.

## Encryption
Booster supports LUKS based full-disk encryption out-of-the-box like Clevis. The generator does not need any extra configuration. Yet, for the initramfs you need to append information about the LUKS partition where the root resides. This is done with either  or  kernel parameter that need to be specified in the boot loader configuration file.  specifies the UUID of the encrypted LUKS partition that needs to be unlocked by Booster. The  manual recommends that the UUID does not contain any quotes.  specifies name of the unlocked partition (as in ). See  for related options.

No image rebuild is required. Once the boot loader configuration is done, reboot the computer. After that you will see a  prompt at boot time asking for a password for the encrypted root partition.

## systemd style binding
Booster also supports partitions bound with systemd such as  and .

If you use `systemd-fido2` then please install  package and add fido2-assert to the image using following configuration:

Regenerate the booster images. Booster will detect this configuration during boot and use the present YubiKey to unlock the drive.

## Removing modules
You can remove modules from initramfs via the  sign. An example to choose every modules manually and doing as same as Mkinitcpio/Minimal initramfs to improve boot performance is

## Stripping modules
You can reduce size of by initramfs by stripping modules.

## Compression
Booster supports compression of initramfs, by default using the  algorithm. Currently supported algorithms are , , ,  or .

## Boot loader configuration
Once the image is generated it is time to configure the boot loader.

## Microcode updates
Unlike mkinitcpio and dracut, Booster does not support including microcode updates into generated images; see Microcode#Microcode in a separate initramfs file for details on how to configure your boot loader to additionally load the appropriate microcode image.

## rEFInd
If the configuration relies on automatic detection already, no additional configuration change is necessary. rEFInd supports initramfs files named booster*.

If you specify the initramfs path manually, either in refind.conf or in manual boot stanzas, make sure to use the correct files names. I.e.  instead of .

## systemd-boot
To enable the new initramfs image with systemd-boot simply create a new boot loader entry like this one:

Where the root filesystem is referenced by . To find your root device UUID run .

## Troubleshooting
## Debug
If Booster has issues and does not work as expected, enable debug output that provides extra information about what is going on:

* for generator there is a  command line flag: .
* for init there is a  kernel parameter.

If you believe it is an issue with Booster itself, then please file a ticket on GitHub.

## Booster generator fails with "too many open files" error
If you enabled  and  and see an error like , then you need to increase per-process limit for open files. See Limits.conf#nofile.
