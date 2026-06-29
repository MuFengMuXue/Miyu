# Archiso

Archiso is a highly-customizable tool for building Arch Linux live CD/USB ISO images, netboot artifacts and bootstrap tarballs. The official images are built with archiso and include these packages. It can be used as the basis for rescue systems, Linux installers or other systems.

This article explains how to install archiso, and how to configure it to control aspects of the resulting ISO image such as included packages and files.

Technical requirements and build steps can be found in the official project documentation. Archiso is implemented with a number of bash scripts. The core component of archiso is the mkarchiso command. Its options are documented in  and not covered here.

## Installation
Install the  package.

## Prepare a custom profile
Archiso comes with two profiles, releng and baseline.

* releng is used to create the official monthly installation ISO. It can be used as a starting point for creating a customized ISO image.
*  baseline is a minimal configuration, that includes only the bare minimum packages required to boot the live environment from the medium.

To build an unmodified version of the profiles, skip to #Build the ISO. Otherwise, if you wish to adapt or customize one of archiso's shipped profiles, copy it from  to a writable directory with a name of your choice. For example:

 $ cp -r /usr/share/archiso/configs/releng/ archlive

Proceed to the following sections to customize and build the custom profile.

## Profile structure
An archiso profile contains configuration that defines the resulting ISO image. The profile structure is documented in === Selecting packages ===

Edit  to select which packages are to be installed on the live system image, listing packages line by line.

## Custom local repository
To add packages not located in standard Arch repositories (e.g. packages from the AUR or customized with the ABS), set up a custom local repository and add your custom packages to it. Then add your repository to  as follows:

## Packages from multilib
To install packages from the multilib repository, simply uncomment that repository in .

## Adding files to image
The airootfs directory is used as the starting point for the root directory () of the live system on the image. All its contents will be copied over to the working directory before packages are installed.

Place any custom files and/or directories in the desired location under . For example, if you have custom nftables rules on your current system you want to be used on your live image, copy them over as such:

 $ cp /etc/nftables.conf archlive/airootfs/etc/

Similarly, some care is required for special configuration files that reside somewhere down the hierarchy. Missing parts of the directory structure can be simply created with .

By default, permissions will be  for files and  for directories. All of them will be owned by the root user. To set different permissions or ownership for specific files and/or folders, use the  associative array in . See [https://gitlab.archlinux.org/archlinux/archiso/-/blob/master/docs/README.profile.rst README.profile.rst for details.

## Adding repositories to the image
To add a repository that can be used in the live environment, create a suitably modified  and place it in .

If the repository also uses a key, place the key in . The key file name must end with . Additionally, the key must be trusted. This can be accomplished by creating a GnuPG exported trust file in the same directory. The file name must end with . The first field is the key fingerprint, and the second is the trust. You can reference  for an example.

## ArchZFS example
The files in this example are:

 airootfs
 ├── etc
 │   ├── pacman.conf
 │   └── pacman.d
 │       └── archzfs_mirrorlist
 └── usr
     └── share
         └── pacman
             └── keyrings
                 ├── archzfs.gpg
                 └── archzfs-trusted

Import and trust the key (during image build or post-boot setup script):

 $ curl -Lo archzfs.gpg 'https://github.com/archzfs/archzfs-keyring/raw/master/keyring/packager/archzfs/3A9917BF0DED5C13F69AC68FABEC0A1208037BE9/3A9917BF0DED5C13F69AC68FABEC0A1208037BE9.asc'
 # pacman-key --add archzfs.gpg
 # pacman-key --lsign-key 3A9917BF0DED5C13F69AC68FABEC0A1208037BE9

## Kernel
Although both archiso's included profiles only have , ISOs can be made to include other or even multiple kernels.

First, edit  to include kernel package names that you want. When mkarchiso runs, it will include all  and  files in the ISO (and additionally in the FAT image used for UEFI booting).

mkinitcpio presets by default will build fallback initramfs images. For an ISO, the main initramfs image would not typically include the  hook, thus making an additional fallback image unnecessary. To prevent the creation of an fallback initramfs image, so that it does not take up space or slow down the build process, place a custom preset in . For example, for :

Finally create boot loader configuration to allow booting the kernel(s).

## Boot loader
Archiso supports syslinux for BIOS booting and GRUB or systemd-boot for UEFI booting. Refer to the articles of the boot loaders for information on their configuration syntax.

mkarchiso expects that GRUB configuration is in the  directory, systemd-boot configuration is in the  directory and syslinux configuration in the  directory.

## UEFI Secure Boot
If you want to make your archiso bootable on a UEFI Secure Boot enabled environment, you must use a signed boot loader. You can follow the instructions on Secure Boot#Booting an installation medium.

## systemd units
To enable systemd services/sockets/timers for the live environment, you need to manually create the symbolic links just as  does it.

For example, to enable , which contains , run:

 $ mkdir -p archlive/airootfs/etc/systemd/system/multi-user.target.wants
 $ ln -s /usr/lib/systemd/system/gpm.service archlive/airootfs/etc/systemd/system/multi-user.target.wants/

The required symlinks can be found out by reading the systemd unit, or if you have the service installed, by enabling it and observing the systemctl output.

## Login manager
Starting X at boot is done by enabling your login manager's systemd service. If you do not know which .service to enable, you can easily find out in case you are using the same program on the system you build your ISO on. Just use:

 $ ls -l /etc/systemd/system/display-manager.service

Now create the same symlink in . For LXDM:

 $ ln -s /usr/lib/systemd/system/lxdm.service archlive/airootfs/etc/systemd/system/display-manager.service

This will enable LXDM at system start on your live system.

## Changing automatic login
The configuration for getty's automatic login is located under .

You can modify this file to change the auto login user:

 ExecStart=
 ExecStart=-/sbin/agetty --noreset --noclear --autologin ''username'' - ${TERM}

Or remove  altogether to disable auto login.

If you are using the serial console, create  with the following content instead:

 [Service
 ExecStart=
 ExecStart=-/sbin/agetty --noreset --noclear --autologin root --keep-baud 115200,57600,38400,9600 - ${TERM}

## Users and passwords
To create a user which will be available in the live environment, you must manually edit , ,  and .

For example, to add a user . Add them to  following the  syntax:

Add the user to  following the syntax of . If you want to define a password for the user, generate a password hash with  and add it to the file. For example:

Otherwise, you may keep the password field empty, meaning that the user can log in with no password.

Add the user's group and the groups which they will part of to  according to . For example:

Create the appropriate  according to :

Make sure  and  have the correct permissions:

After package installation, mkarchiso will create all specified home directories for users listed in  and copy  to them. The copied files will have proper user and group ownership.

## Keymaps
To change the live system's default keymap on the console, add a  with the desired keymap. Check Linux console/Keyboard configuration and  for details and more options.

For example, to change the console's and X11's default keymap to German (), create  with the following contents:

## Locales
To change the live system's locale, you must first enable and generate the localization files. For this to work you must add a custom  with the required locales and run  within the live system. This then enables you to also change the system's default locale.

For example, to enable  and , create  with the following contents (check Locale#Generating locales for details):

You then need to run  within the live system. This can be achieved with a Pacman hook that is later automatically removed from the image by another hook. Create  with the following contents (check Pacman#Hooks and  for details):

Optionally, you can then change the live system's default locale by adding a custom . For example, to change the default locale to , create  with the following contents (check Locale#Variables and  for details):

## Changing the distribution name used in the ISO
Start by copying the file  into the  folder in the rootfs. Then, edit the file accordingly. You can also change the name inside of GRUB and syslinux.

## Build the ISO
Build an ISO which you can then burn to CD or USB by running:

 # mkarchiso -v -r -w /tmp/archiso-tmp -o /path/to/out_dir /path/to/profile/

*  specifies the working directory. If the option is not specified, it will default to  in the current directory. If memory allows, it is preferred to place the working directory on tmpfs (as shown above) to speed up the process.
*  deletes the working directory (if it was created by mkarchiso) after successfully building the ISO.
*  specifies the directory where the built ISO image will be placed. If the option is not specified, it will default to  in the current directory.
* It should be noted the profile file  cannot be specified when running mkarchiso, only the path to the file.

Replace  with the path to your custom profile, or with  if you are building an unmodified profile.

When run, the script will download and install the packages you specified to , create the kernel and init images, apply your customizations and finally build the ISO into the output directory.

## Removal of work directory
Temporary files are copied into a work directory. If mkarchiso is run with the  option, it will delete the work directory after successfully building the ISO as long as the directory did not exist beforehand. Alternatively, you can delete the work directory manually:

 # rm -rf /path/to/work_dir

## Using the ISO
See Installation guide#Prepare an installation medium for various options.

## Test the ISO in QEMU
Install the optional dependencies  and .

Use the convenience script  to run a built image using QEMU.

 $ run_archiso -i /path/to/archlinux-yyyy.mm.dd-x86_64.iso

The virtual machine can also be run using UEFI emulation:

 $ run_archiso -u -i /path/to/archlinux-yyyy.mm.dd-x86_64.iso

## Tips and tricks
## Run setup commands as part of the ISO build process
When creating a custom profile, some modifications will require you to run setup commands within the live system's environment before creating the ISO. For example, if you want to enable additional locales, you must run  within the live system to generate the necessary localization files.

To run setup commands before creating the ISO, add a Pacman hook below . Check Pacman#Hooks and  for details on how to create custom Pacman hooks. Also check #Locales for an example.

Since these setup hooks are often required to run just once as part of the ISO build process, the releng profile includes a Pacman hook that removes any Pacman hook that is marked with the string . So, if you don't want your Pacman hook to also apply on the running live system, add the following comment to your Pacman hook:

 # remove from airootfs!

## Prepare an ISO for an installation via SSH
To install Arch Linux via SSH without any interaction with the system, an SSH public key must be placed in .

Adding the SSH key can either be done manually (explained here), or by cloud-init.

To add the key manually, first copy archiso's releng profile to a writable directory. The following example uses .

 $ cp -r /usr/share/archiso/configs/profile/ archlive

Create a  directory in the home directory of the user which will be used to log in. The following example will be using the root user.

 $ mkdir archlive/airootfs/root/.ssh

Add the SSH public key(s), which will be used to log in, to :

 $ cat ~/.ssh/key1.pub >> archlive/airootfs/root/.ssh/authorized_keys
 $ cat ~/.ssh/key2.pub >> archlive/airootfs/root/.ssh/authorized_keys

Set correct permissions and ownership for the  directory and the  file:

Finally build the ISO. Upon booting the ISO, OpenSSH will start and it will be possible to log in using the corresponding SSH private key(s).

## Automatically connect to a Wi-Fi network using iwd
Create  inside the profile's  directory and set the correct permissions:

 $ mkdir -p archlive/airootfs/var/lib/iwd

Follow the instructions in iwd#Network configuration and  to create a network configuration file for your Wi-Fi network.

Save the configuration file inside .

## Adjusting the size of the root file system
When installing packages in the live environment, for example on hardware requiring DKMS modules, the default size of the root file system might not allow the download and installation of such packages due to its size.

It will manifest as the following error message when downloading files or installing packages in the live environment:

 error: partition / too full: 63256 blocks needed, 61450 blocks free
 error: not enough free disk space
 error: failed to commit transaction (not enough free disk space)
 Errors occurred: no packages were upgraded.

To adjust the size on the fly:

 # mount -o remount,size=SIZE /run/archiso/cowspace

See  for the possible parameters of .

To adjust the size at the boot loader stage (by pressing  or ) use the boot option:

 cow_spacesize=SIZE

To adjust the size while building an image add the boot option to:

*
*
*

The result can be checked with:

 $ df -h

See mkinitcpio-archiso boot parameters.

## Troubleshooting
## Window manager freezes
If you want to use a window manager in the Live CD, you must add the necessary and correct video drivers, or the WM may freeze on loading.
