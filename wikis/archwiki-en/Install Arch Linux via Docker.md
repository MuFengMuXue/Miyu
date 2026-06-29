# Install Arch Linux via Docker

This document is a guide for installing Arch Linux using the official Arch Linux Container Image from Docker Hub. For alternative means of installation, see Installation process.

Before installing, it would be advised to view the FAQ. For conventions used in this document, see Help:Reading. In particular, code examples may contain placeholders (formatted in ) that must be replaced manually.

For more detailed instructions, see the respective ArchWiki articles or the various programs' man pages, both linked from this guide. For interactive help, the IRC channel and the forums are also available.

Arch Linux should run on any x86_64-compatible machine with a minimum of 512 MiB RAM, though more memory is needed to boot the live system for installation A basic installation should take less than 2 GiB of disk space. As the installation process needs to retrieve packages from a remote repository, this guide assumes a working internet connection is available. Furthermore a working Docker setup on the host is required. While technically it is certainly possible to use any qemu supported host to install Arch with, this guide will not cover this however.

## Pre-installation
This guide assumes that the host system is already pre-configured with regards to normally expected things. E.g. the time is setup correctly, internet connection is working normally, EFI mode if required is setup correctly etc.

## Prepare an installation medium
The installation requires a target directory to which Arch Linux will be installed. Any writable directory can be used, but it is quite likely that the target directory has a partition or volume mounted that will serve as the root disk.

## Full disk partitions
If a full disk is being used as a target, it may need to be formatted. For details see Installation guide#Partition the disks as the same partitioning instructions and order can be followed from there. All the same restrictions and requirements as from there apply as well.

Likewise, the new disk will also needed to be formatted. The instructions from Installation guide#Format the partitions can be used for this as well.

## Volumes
When using filesystems such as btrfs or zfs, filesystem volumes are an option to use. Depending on what filesystem is used, creating them uses their own list of commands. In this guide, btrfs will be used as an example.

First, a root volume for Arch Linux is created. This command assumes the current working directory is the btrfs root volume (subvolid=5), but anywhere could be used. If a different location is used, within an existing hierarchy, keep this in mind when later defining fstab and similar. Also note, that as the Arch Linux specific volume is created on a mounted (root) volume, it could be the case that the underlying stack is using (full)disk encryption.

  # btrfs subvolume create "arch_root"

## Mount the file systems
The following section assumes the location Arch Linux will be installed into /tmp/target. It is thus required that the partition is thus mounted there. Using a btrfs subvolume called arch_root, with autodefrag and LZO compression enabled would look as:

 # mkdir -p /tmp/target
 # mount /dev/disk /tmp/target -o subvol=arch_root,compress=lzo,autodefrag

The instructions from Installation guide#Mount the file systems can be used for this as well.

## Installation
## Launching the container
The remainder of the installation will be done inside a docker container, abbreviated with ADC, Arch Docker Container.

  # docker run \
           --env PS1="ADC(\#)[\d \T:\w\\$ " \
           --interactive \
           --privileged \
           --rm \
           --tty \
           --volume "/tmp/target:/target" \
           "index.docker.io/library/archlinux:latest" /bin/sh

## Select the mirrors
Packages to be installed must be downloaded from mirror servers, which are defined in . In the docker container we first install reflector, which  updates the mirror list by choosing 70 most recently synchronized HTTPS mirrors and sorting them by download rate. First we have to install reflector in the docker container to be able to use it.

 # reflector [--country  \
              --latest 5 \
              --protocol http,https \
              --save "/etc/pacman.d/mirrorlist" \
              --sort rate

The higher a mirror is placed in the list, the more priority it is given when downloading a package. Ensure to inspect the file to see if it is satisfactory. If it is not, edit the file accordingly, and move the geographically closest mirrors to the top of the list, although other criteria should be taken into account.

This file will later be copied to the new system by pacstrap, so it is worth getting right.

## Install essential packages
To be able to start the installation, the  package must be installed into the Docker image first. Once completed, the official installation guide can be followed starting with the section Installation guide#Install essential packages.

Return to this guide before executing the Reboot step from the section Installation guide#Reboot to instead continue with the #Reboot below.

## Reboot
Exit the docker container by typing  or pressing .

Optionally manually unmount all the partitions with : this allows noticing any "busy" partitions, and finding the cause with .

With a correctly setup boot loader, a reboot should now be possible into the freshly installed Arch Linux.

## Post-installation
See General recommendations for system management directions and post-installation tutorials (like setting up a graphical user interface, sound or a touchpad).

For a list of applications that may be of interest, see List of applications.
