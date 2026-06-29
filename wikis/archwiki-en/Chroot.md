# Chroot

A chroot is an operation that changes the apparent root directory for the current running process and their children. A program that is run in such a modified environment cannot access files and commands outside that environmental directory tree.  This modified environment is called a chroot jail.

## Reasoning
Changing root is commonly done for performing system maintenance on systems where booting and/or logging in is no longer possible. Common examples are:

* Reinstalling the boot loader.
* Rebuilding the initramfs image.
* Upgrading or downgrading packages.
* Resetting a forgotten password.
* Building packages in a clean chroot.

See also Wikipedia:Chroot#Limitations.

## Requirements
In order to use chroot, you need another Linux installation or installation media (of any distribution), with:

* Root privilege (see #Without root privileges for alternatives).
* The same instruction set architecture as the system being chrooted into. The architecture of the current environment can be discovered with:  (e.g. i686 or x86_64). It is also possible to use QEMU to execute code that does not have a matching native architecture.
* Kernel modules loaded that are needed in the chroot environment.
* Swap enabled if needed:
* Internet connection established if needed.

## Prepare new root location
The chroot target should be a directory which contains a file system hierarchy.

In the installation guide, this directory would be . For an existing installation, you need to mount existing partitions into  yourself:

Run  and note the partition layout of your installation. It will be usually something like  or if you have an NVMe drive .

Mount the file system:

 # mount /dev/sdXY /mnt

If you have an EFI system partition and need to make changes in it (e.g. updating the vmlinuz or initramfs images):

 # mount /dev/sdXZ /mnt/esp

If you have any discrete partitions, mount them too.

In the following examples,  is the directory where the new root resides (e.g. ).

## Usage
There are two main options for using chroot, described below.

## Using arch-chroot
The bash script  is part of the  package. arch-chroot wraps the chroot command while ensuring that important functionality is available, e.g. mounting ,  and other API filesystems, or exposing  to the chroot.

## Enter a chroot
Run arch-chroot with the new root directory as first argument:

 # arch-chroot /path/to/new/root

You can now do most of the operations available from your existing installation. Some tasks which needs D-Bus will not work as noted in #Usage.

## Exit a chroot
To exit the chroot, use:

 # exit

## Run a single command and exit
To run a command from the chroot and exit again, append the command to the end of the line:

 # arch-chroot /path/to/new/root mycommand

For example, to run  for a chroot located at , do:

 # arch-chroot /mnt/arch mkinitcpio -p linux

## Running on Btrfs
On a Btrfs root file system with subvolumes, you have to make sure that all subvolumes are properly mounted as specified in fstab before entering chroot.

An example with the Btrfs default setup from archinstall:

## Using chroot
If you run chroot directly, below steps are needed before actual chroot.

First, mount the temporary API filesystems:

 # cd /path/to/new/root
 # mount -t proc /proc proc/
 # mount -t sysfs /sys sys/
 # mount --rbind /dev dev/

And optionally:

 # mount --rbind /run run/

If you are running a UEFI system, you will also need access to EFI variables. Otherwise, when installing GRUB, you will receive a message similar to: :

 # mount --rbind /sys/firmware/efi/efivars sys/firmware/efi/efivars/

Next, in order to use an internet connection in the chroot environment, copy over the DNS details:

 # cp /etc/resolv.conf etc/resolv.conf

Finally, to change root into  using a bash shell:

 # chroot /path/to/new/root /bin/bash

After chrooting, it may be necessary to load the local Bash configuration:

 # source /etc/profile
 # source ~/.bashrc

When finished with the chroot, you can exit it via:

 # exit

Then unmount the temporary file systems:

 # cd /
 # umount --recursive /path/to/new/root

## Run graphical applications from chroot
If you have an X server running on your system, you can start graphical applications from the chroot environment.

To allow the chroot environment to connect to an X server, open a virtual terminal inside the X server (i.e. inside the desktop of the user that is currently logged in), then run the xhost command, which gives permission to anyone to connect to the user's X server (see also Xhost):

 $ xhost +local:

Then, to direct the applications to the X server from chroot, set the  environment variable inside the chroot to match the  variable of the user that owns the X server. So for example, run:

 $ echo $DISPLAY

as the user that owns the X server to see the value of . If the value is ":0" (for example), then run the following in the chroot environment:

 # export DISPLAY=:0

## Without root privileges
Chroot requires root privileges, which may not be desirable or possible for the user to obtain in certain situations. There are, however, various ways to simulate chroot-like behavior using alternative implementations.

## PRoot
PRoot may be used to change the apparent root directory and use  without root privileges. This is useful for confining applications to a single directory or running programs built for a different CPU architecture, but it has limitations due to the fact that all files are owned by the user on the host system. PRoot provides a  argument that can be used as a workaround for some of these limitations in a similar (albeit more limited) manner to fakeroot.

## Fakechroot
 is a library shim which intercepts the chroot call and fakes the results. It can be used in conjunction with  to simulate a chroot as a regular user.

 $ fakechroot fakeroot chroot ~/my-chroot bash

## Unshare
, part of , can be used to create a new kernel namespace. This works with the usual chroot command. For example:

 $ unshare --map-root-user chroot ~/namespace /bin/sh

## Tips and tricks
## chroot detection
 detect whether invoked in a chroot environment. See  for detection of other virtualized environments. For a broader discussion, and usage of traditional tools, see how-do-i-tell-im-running-in-a-chroot.

## Troubleshooting
## arch-chroot: /path/to/new/root is not a mountpoint. This may have undesirable side effects.
Upon executing , a warning is issued:

 ==> WARNING: /path/to/new/root is not a mountpoint. This may have undesirable side effects.

See  for an explanation and an example of using bind mounting to make the chroot directory a mountpoint.
