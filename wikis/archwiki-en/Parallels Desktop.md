# Parallels Desktop

Parallels Desktop is a hypervisor for macOS which allows users to install a variety of operating systems as "virtual machines" (guests) on the host system, reducing the need for managing multiple physical machines. A more complete description on virtualization can be found at Wikipedia.

## Installation of Arch as a guest
Parallels Desktop supports Linux guests out of the box, but only offers support for a few Linux distributions - excluding Arch Linux. This means the installation of Parallels tools have not been tested by the vendor, and requires some manual intervention to work under Arch. If you do not wish to use Parallels tools, installation is as simple as choosing "other linux" when creating a new virtual machine and proceeding as you would on any real machine.

## Parallels Desktop on an Apple Mac x86_64 hardware
In addition to the instructions below, there is an installation guide for Arch Linux in Parallels Knowledgebase.

## Parallels Desktop on an Apple Mac M1 and higher
You can use the Archboot aarch64 images to install a VM as you like it.

If you want a plain image right to start: Download VM, for login information please look at the Readme

## Parallels tools
## Overview
To improve interoperability between the host and the guest operating systems, Parallels provides a package called "Parallels tools" which contains kernel modules and userspace utilities. See Parallels Tools Overview for a list of its features.

This article assumes users want to make full use of the tools, including Xorg configuration. If you are running a headless server, you can skip over the sections relating to X.

When referring to the version of parallel tools the form is .. For example: 9.0.24237.1028877 corresponds to Parallels version 9.0.24237 with tools version 1028877

## Configuring Xorg
The Parallels tools installer will take care of configuring Xorg, so just follow the instructions at Xorg to install the relevant packages on your system. Install the  package to use the vesa driver.

## Preparing dependencies
You need to install standard build utilities ,  and .

## Installing Parallels tools
Choose "install Parallels Tools" from the "Virtual Machine" menu. Parallels Tools are located on a cd-image, which will be connected to your virtual machine. You have to mount it first:

 $ mount /dev/cdrom /mnt/cdrom

Now you can proceed to install Parallels tools using the installation script as follows:

 $ cd /mnt/cdrom
 $ ./install

Parallels tools work fine out of the box in most cases, but sometimes you need to patch it:

{| class="wikitable"
! Liunx Kernel !! Parallels Desktop  !! Parallels Tools !! Work out of box
|-
| 5.17 || 17.1.4 || 51567 ||
|-
| 5.18 || 17.1.4 || 51567 ||
|-
| 5.18 || 18.0.0 || 53049 ||
|}

If you have Parallels Desktop 17.1.4 but installed a VM with kernel version 5.18 (check with ), follow the troubleshooting section below:

## Troubleshooting: Patch Parallels 17 to support Kernel 5.18
Choose "install Parallels Tools" from the "Virtual Machine" menu. Parallels Tools are located on a cd-image, which will be connected to your virtual machine.

You need root permission in this process.
Become root user, then mount the Tools virtual CD in your Linux VM:

 $ su
 $ mount /dev/cdrom /mnt

Copy the full CD directory to home directory and rename it to :

 $ cp -R /mnt ~
 $ cd ~
 $ mv mnt prl-tools-build

Download the community patch, then prepare  to be patched::

 $ wget https://raw.githubusercontent.com/wegank/nixos-config/7b89b4c6d1a87c83f10aa5d0f96fe0229795056e/hardware/parallels-unfree/prl-tools.patch
 $ cd ~/prl-tools-build/kmods
 $ tar zxf prl_mod.tar.gz
 $ rm prl_mod.tar.gz

Apply the patch, then install:

 $ cd ~/prl-tools-build
 $ patch -p1  configuration > sharing".
* The folder will appear at .

## Dynamic Display Resolution
A very helpful tool is . It changes the resolution of the display (in the guest - not the host) automatically when your resize your window. If this tool is not running, the contents of the window gets stretched or shrunken.
prlcc is usually started automatically and runs in the background. If not, run the following (or place it in a configuration file like ):

 $ prlcc &

## Synchronize clipboard
The tool  can be run to synchronize the clipboard between guest and host. Like the previous tool, if it is not executed automatically, it is recommended to start it in a configuration file like :

 $ prlcp &

## Future work
In general, updating system packages like the linux kernel or Xorg can break Parallels tools and you will need to re-install them. In some cases, new packages will be incompatible with the tools and they will stop working - in that case you will need to roll back the newly installed packages and wait until Parallels releases a new product build before updating your guest (in the hope they have resolved any previous incompatibilities).
