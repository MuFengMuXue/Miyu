# Pacstrap

From the :

:pacstrap is designed to create a new system installation from scratch.

pacstrap is mainly used during the installation of the system, and comes pre-installed within the Arch installation media. It is also used to bootstrap Linux containers.

## Installation
Install the  package.

## Tips and tricks
## Creating a clean chroot
Currently,  only supports sudo. This can not be changed as devtools require the use of the complex functionality of sudo, which  does not support. You can use pacstrap to create a chroot manually.

First, create the chroot directory:

 # mkdir /var/chroot

Then, install the  system and  (meta package containing tools which are used by the makepkg utility):

 # pacstrap -K /var/chroot base base-devel

If you have not mounted a partition to , you must bind the directory on itself to make it a mountpoint, therefore ensuring compatibility with arch-chroot.

 # mount --bind /var/chroot /var/chroot

Then you can enter the chroot, using arch-chroot:

 # arch-chroot /var/chroot

You can not build arch pages as root, makepkg does not permit the use of the root, due to security concerns. Create a build user:

 # useradd -m build

You can then become the build user using the following command:

 # su -l build

You can now build any AUR package you wish by cloning them into the chroot, or use the chroot for testing and debugging of arch packages.
