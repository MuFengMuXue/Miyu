# Kernel/Traditional compilation

This article is an introduction to building custom kernels from kernel.org sources. This method of compiling kernels is the traditional method common to all distributions. It can be, depending on your background, more complicated than using the Kernel/Arch build system. Consider the Arch build system tools are developed and maintained to make repeatable compilation tasks efficient and safe.

## Preparation
It is not necessary (or recommended) to use the root account or root privileges (i.e. via sudo) for kernel preparation.

## Install the core packages
Install the  meta package, which pulls in necessary packages such as  and . It is also recommended to install the following packages, as listed in the default Arch kernel PKGBUILD: , , , , , , , , , .

## Create a kernel compilation directory
It is recommended to create a separate build directory for your kernel(s). In this example, the directory  will be created in the  directory:

 $ mkdir ~/kernelbuild

## Download the kernel source
Download the kernel source from https://www.kernel.org. This should be the tarball (.tar.xz) file for your chosen kernel.

It can be downloaded by simply right-clicking the  link in your browser and selecting , or any other number of ways via alternative graphical or command-line tools that utilise HTTP, TFTP, Rsync, or Git.

In the following command-line commands,  has been installed and is used inside the  directory to obtain kernel A.B.C:

 $ cd ~/kernelbuild
 $ wget https://cdn.kernel.org/pub/linux/kernel/vA.x/linux-A.B.C.tar.xz

You should also verify the correctness of the download before trusting it. First grab the signature, then use that to grab the fingerprint of the signing key, then use the fingerprint to obtain the actual signing key:

 $ wget https://cdn.kernel.org/pub/linux/kernel/vA.x/linux-A.B.C.tar.sign
 $ gpg --list-packets linux-A.B.C.tar.sign | grep -i keyid | awk '{print $NF}' | xargs gpg --recv-keys

Note the signature was generated for the tar archive (i.e. extension ), not the compressed  file that you have downloaded. You need to decompress the latter without untarring it. Verify that you have  installed, then you can proceed like so:

 $ unxz linux-A.B.C.tar.xz
 $ gpg --verify linux-A.B.C.tar.sign linux-A.B.C.tar

Do not proceed if this does not result in output that includes the string "Good signature".

If  was not used inside the build directory, it will be necessary to move the tarball into it, e.g.

 $ mv /path/to/linux-A.B.C.tar.xz ~/kernelbuild/

## Semi-official kernel mirrors
Semi-official mirrors of some of the kernel.org Git repositories are provided by their respective maintainers. These tend to be faster to clone from than kernel.org.

* The mainline branch is mirrored on Linus Torvalds' GitHub account at https://github.com/torvalds/linux.git.
* The stable branches are mirrored on Greg Kroah-Hartman's GitHub account at https://github.com/gregkh/linux. === Unpack the kernel source ===

Within the build directory, unpack the kernel tarball:

 $ tar -xvf linux-A.B.C.tar

To be absolutely sure that no permission errors occur, chown needs to be run to transfer ownership of the folder to the current user.

To transfer ownership of a folder with every file in it to our user, run the chown command.

 $ chown -R $USER:$USER linux-A.B.C

This will transfer ownership of every file in the folder to you, so you do not encounter any errors related to permissions.

To finalise the preparation, ensure that the kernel tree is absolutely clean; do not rely on the source tree being clean after unpacking. To do so, first change into the new kernel source directory created, and then run the  command:

 $ cd linux-A.B.C
 $ make mrproper

## Kernel configuration
This is the most crucial step in customizing the default kernel to reflect your computer's precise specifications. Kernel configuration is set in its  file, which includes the use of Kernel modules. By setting the options in  properly, your kernel and computer will function most efficiently.

You can do a mixture of two things:

* Use the default Arch settings from an official kernel (recommended)
* Manually configure the kernel options (optional, advanced and not recommended)

## Default Arch configuration
This method will create a  file for the custom kernel using the default Arch kernel settings. If a stock Arch kernel is running, you can use the following command inside the custom kernel source directory:

 $ zcat /proc/config.gz > .config

Otherwise, the default configuration can be found online in the [https://gitlab.archlinux.org/archlinux/packaging/packages/linux/-/blob/main/config official Arch Linux kernel package.

## Advanced configuration
There are several tools available to fine-tune the kernel configuration, which provide an alternative to otherwise spending hours manually configuring each and every one of the options available during compilation.

Those tools are:

* : Newer command-line ncurses interface superseding
* : User-friendly graphical interface that requires Qt to be installed as a dependency. This is the recommended method—especially for less experienced users—as it is easier to navigate, and information about each option is also displayed.
* : Graphical configuration similar to xconfig but using GTK.

The chosen method should be run inside the kernel source directory, and all will either create a new  file, or overwrite an existing one where present. All optional configurations will be automatically enabled, although any newer configuration options (i.e. with an older kernel ) may not be automatically selected.

Once the changes have been made save the  file. It is a good idea to make a backup copy outside the source directory. You may need to do this multiple times before you get all the options right.

If unsure, only change a few options between compilations. If you cannot boot your newly built kernel, see the list of necessary items here.

Running  from live media lists names of kernel modules in use. Most importantly, you must maintain cgroups support. This is necessary for systemd. For more detailed information, see Gentoo:Kernel/Gentoo Kernel Configuration Guide and Gentoo:Intel#Kernel or Gentoo:Ryzen#Kernel for Intel or AMD Ryzen processors.

## Compilation
Compilation time will vary from as little as fifteen minutes to over an hour, depending on your kernel configuration and processor capability. Once the  file has been set for the custom kernel, within the source directory run the following command to compile:

 $ make

Start from kernel version 6.11, a new make target  is added to build pacman packages directly. You can run the following command to build several  packages which can be installed with  later.

 $ make pacman-pkg

Installing kernel image and headers package is sufficient to use and test. Api and debug packages can be installed as needed. If one would like to change package name or other makepkg options, edit the file located at  in your kernel source directory.

## Installation
## Install the modules
Once the kernel has been compiled, the modules for it must follow. First build the modules:

 $ make modules

Then install the modules. As root or with root privileges, run the following command to do so:

 # make modules_install

This will copy the compiled modules into . This keeps the modules for individual kernels used separated.

## Copy the kernel to /boot directory
The kernel compilation process will generate a compressed  (big zImage) of that kernel, if it does not, you may have to run

 $ make bzImage

This file must be copied to the  directory and renamed in the process. Provided the name is prefixed with , you may name the kernel as you wish. In the examples below, the installed and compiled A.B.C kernel has been copied over and renamed to :

 # cp -v arch/x86/boot/bzImage /boot/vmlinuz-linuxAB

## Make initial RAM file system
If you do not know what making an initial RAM file system is, see Initramfs on Wikipedia and mkinitcpio.

## Automated preset method
An existing mkinitcpio preset can be copied and modified so that the custom kernel initramfs images can be generated in the same way as for an official kernel. This is useful where intending to recompile the kernel (e.g. where updated). In the example below, the preset file for the stock Arch kernel will be copied and modified for kernel A.B.C, installed above.

First, copy the existing preset file, renaming it to match the name of the custom kernel specified as a suffix to  when copying the :

 # cp /etc/mkinitcpio.d/linux.preset /etc/mkinitcpio.d/linuxAB.preset

Second, edit the file and amend for the custom kernel. Note (again) that the  parameter also matches the name of the custom kernel specified when copying the :

Finally, generate the initramfs images for the custom kernel in the same way as for an official kernel:

 # mkinitcpio -p linuxAB

## Manual method
Rather than use a preset file, mkinitcpio can also be used to generate an initramfs file manually. The syntax of the command is:

 # mkinitcpio -k kernel_version -g /boot/initramfs-file_name.img

*  (): Specifies the modules to use when generating the initramfs image. The  name will be the same as the name the modules directory for it, located in  (alternatively, a path to the kernel image can be used).
*  (): Specifies the name of the initramfs file to generate in the  directory. Again, using the naming convention mentioned above is recommended.

For example, the command for the A.B.C custom kernel installed above would be:

 # mkinitcpio -k A.B.C -g /boot/initramfs-linuxAB.img

## Copy System.map
The  file is not required for booting Linux. It is a type of "phone directory" list of functions in a particular build of a kernel. The  contains a list of kernel symbols (i.e function names, variable names etc) and their corresponding addresses. This "symbol-name to address mapping" is used by:

* Some processes like klogd, ksymoops, etc.
* By OOPS handler when information has to be dumped to the screen during a kernel crash (i.e info like in which function it has crashed).

If your  is on a filesystem which supports symlinks (i.e. not FAT32), copy  to , appending your kernel's name to the destination file. Then create a symlink from  to point to :

 # cp System.map /boot/System.map-linuxAB
 # ln -sf /boot/System.map-linuxAB /boot/System.map

After completing all steps above, you should have the following 3 files and 1 soft symlink in your  directory along with any other previously existing files:

* Kernel:
* Initramfs:
* System Map:
* System Map kernel symlink:  (which symlinks to )

## Boot loader configuration
Add an entry for your new kernel in your boot loader configuration file. See Arch boot process#Feature comparison for possible boot loaders, their wiki articles and other information.
