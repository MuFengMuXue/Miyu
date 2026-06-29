# Install Arch Linux from existing Linux

This document describes the bootstrapping process required to install Arch Linux from a running Linux host system.
After bootstrapping, the installation proceeds as described in the Installation guide.

Installing Arch Linux from a running Linux is useful for:

* remotely installing Arch Linux, e.g. a (virtual) root server
* replacing an existing Linux without an installation medium (see #Replacing the existing system without an installation medium)
* creating a new Linux distribution or LiveMedia based on Arch Linux
* creating an Arch Linux chroot environment, e.g. for a Docker base container
* rootfs-over-NFS for diskless machines

The goal of the bootstrapping procedure is to setup an environment from which the scripts from  (such as  and ) can be run.

If the host system runs Arch Linux, this can be achieved by simply installing . If the host system runs another Linux distribution, you will first need to set up an Arch Linux-based chroot.

## Backup and preparation
Backup all your data including mails, webservers, etc. Have all information at your fingertips. Preserve all your server configurations, hostnames, etc.

Here is a list of data you will likely need:

* IP address
* hostname(s), (note: rootserver are mostly also part of the providers domain, check or save your  before you delete)
* DNS server (check )
* SSH keys (if other people work on your server, they will have to accept new keys otherwise. This includes keys from your Apache, your mail servers, your SSH server and others.)
* Hardware info (network card, etc. Refer to your pre-installed  )
* Boot loader configuration files.

In general, it is a good idea to have a local copy of your original  directory on your local hard drive.

## From a host running Arch Linux
Install the  package.

Follow Installation guide#Mount the file systems to mount the filesystem that will be used for the root directory as well as all the other needed mount points. If you already use the  directory for something else, just create another directory such as  and use it as the mount point base for the rest of the installation.

At this stage, Arch Linux can either be installed from scratch or it can mirror the host installation. The two options are described thereafter.

## Create a new Arch installation
Follow Installation guide#Installation.

In the procedure, the first step, Installation guide#Select the mirrors, can be skipped since the host should already have a correct mirrorlist.

## Create a copy of an existing Arch installation
It is possible to replicate an existing Arch Linux installation by copying the host filesystem to the new partition and make some adjustments to it to make it bootable and unique.

The first step is to copy the host files into the mounted new partition, for this, consider using the approach exhibited in rsync#Full system backup.

Then, follow the procedure described in Installation guide#Configure the system with some caveats and additional steps:

* Installation guide#Time, Installation guide#Localization and Installation guide#Root password can be skipped.
* Installation guide#Initramfs may be required in particular if changing file system. For example, from ext4 to Btrfs. (If you get errors in this step, return to it after installing the boot loader)
* Regarding Installation guide#Boot loader, it is necessary to reinstall the boot loader.
* Delete  and create a new one with .

If the mirrored Arch installation may be used within a different configuration or with another hardware, consider the following additional operations:

* Use the CPU microcode update adapted to the target system during the step Installation guide#Boot loader
* If any specific Xorg#Configuration was present on the host and may be incompatible with the target system, follow Moving an existing install into (or out of) a virtual machine#Disable any Xorg-related files
* Make any other adjustment appropriate to the target system, like reconfiguring the network or the audio.

## From a host running another Linux distribution
There are multiple tools which automate a large part of the steps described in the following subsections. See their respective homepages for detailed instructions.

* archstrap (Bash)
* digitalocean-debian-to-arch (repartition disk, DigitalOcean specific; does not perform PGP signature verification)
* image-bootstrap (Python; does not perform PGP signature verification)
* vps2arch (Bash; does not perform PGP signature verification)

The manual way is presented in the following subsections. The idea is to either get pacman working directly on the host system, or to run an Arch system inside the host system, with the actual installation being executed from the Arch system. The nested system is contained inside a chroot.

## Using pacman from the host system
Pacman can be compiled on most Linux distributions, and used directly on the host system to bootstrap Arch Linux. The arch-install-scripts should run without issues directly from the downloaded sources on any recent distribution.

Some distributions provide a package for pacman and/or arch-install-scripts in their official repositories which can be used for this purpose. As of July 2020, Void Linux is known to provide the pacman package, and Alpine Linux and Fedora are known to provide both pacman and arch-install-scripts.

## Creating a chroot
Download the bootstrap tarball from a mirror into .

Download the bootstrap tarball signature from the download page and place it in the same directory. Do not download it from a mirror.

Verify the signature with GnuPG.

Extract the tarball:

 # tar xf /path-to-bootstrap-image/archlinux-bootstrap-x86_64.tar.zst --numeric-owner

Take note of the final  option, which is important for preserving correct UID and GID numbers of extracted files in case your existing Linux system uses different numbers than Arch Linux.

Select a repository server by editing .

Enter the chroot:

* If bash 4 or later is installed, and unshare supports the  and  options (util-linux 2.24 or later):
* Otherwise, run the following commands:

:

## Using a chroot environment
The bootstrap environment is really barebones (no  or ). Therefore, we need to set up pacman in order to download other necessary packages.

## Initializing pacman keyring
Before starting the installation, pacman keys need to be setup. Run the following commands:

 # pacman-key --init
 # pacman-key --populate

See pacman/Package signing#Initializing the keyring for details.

## Downloading basic tools
Refresh the package lists and install what you need: ,  etc.

## Installation tips
You can now proceed to Installation guide#Mount the file systems and follow the rest of the Installation guide.

Some host systems or configurations may require certain extra steps. See the sections below for tips.

## Debian-based host
## /dev/shm
On some Debian-based host systems, pacstrap may produce the following error:

This is because in some versions of Debian,  points to  while in the Arch-based chroot,  does not exist and the link is broken. To correct this error, create a directory :

 # mkdir /run/shm

## Fedora-based host
On Fedora based hosts and live USBs you may encounter problems when using genfstab to generate your fstab. Remove duplicate entries and the  option where it appears, as this is SELinux-specific and will keep your system from booting normally.

## Things to check before you reboot
Before rebooting, double check a few details in your installation to achieve a successful installation. To do so, first chroot into the newly-installed system, and then:

* create a user with password, so you can login via ssh. This is critical since root login is disabled by default since OpenSSH-7.1p2.
* set a root password so that you can switch to root via su later
* install a ssh solution and enable its server instance to start automatically at boot.
* set up your network configuration  in order to have a connection started automatically at boot.
* set up a boot loader and configure it to use the swap partition you appropriated earlier as the root partition. You might want to configure your boot loader to be able to boot into your old system; it is helpful to re-use the server's existing  partition in the new system for this purpose.

## Replacing the existing system without an installation medium
Find ~700 MiB of free space somewhere on the disk, e.g. by partitioning a swap partition. You can disable the swap partition and set up your system there.

## Set old swap partition as new root partition
Check ,  or  to find your swap partition. Assuming your hard drive is located on  ( will be a number).

Do the following:

Disable the swap space:

 # swapoff /dev/sdaX

Create a filesystem on it

 # fdisk /dev/sda
 (set /dev/sdaX ID field to "Linux" - Hex 83)
 # mke2fs -j /dev/sdaX

Create a directory to mount it in

 # mkdir /mnt/newsys

Finally, mount the new directory for installing the intermediate system.

 # mount -t ext4 /dev/sdaX /mnt/newsys

## Installation
Install essentials packages and any other package required to get a system with internet connection up and running in the temporary partition, being careful with the limit of ~700 MiB space. When specifying packages to be installed with pacstrap, consider adding the  flag to avoid filling up valuable space by downloading packages to the host system.

Once the new Arch Linux system is installed, fix the boot loader configuration, then reboot into the newly created system, and rsync the entire system to the primary partition.
