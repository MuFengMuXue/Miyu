# Dynamic Kernel Module Support

From Wikipedia:

:Dynamic Kernel Module Support (DKMS) is a program/framework that enables generating Linux kernel modules whose sources generally reside outside the kernel source tree. The concept is to have DKMS modules automatically rebuilt when a new kernel is installed.

This means that a user does not have to wait for a company, project, or package maintainer to release a new version of the module. Since the introduction of pacman hooks, the rebuild of the modules is handled automatically when a kernel is upgraded.

## Installation
Install the  package and the headers for the target kernel(s)—for example, for the default  kernel this would be ; other kernels have their own respective headers packages.

A good number of modules that lie outside the kernel source tree have a DKMS variant; a few are hosted in the official repositories, most are found in the AUR.

## Upgrades
Though the rebuild of the DKMS modules is usually seamless during a kernel upgrade, it may still happen that the rebuild fails. You should pay extra attention to the pacman output. This applies in particular if the system relies on the DKMS module to boot successfully and/or if you use DKMS with a custom kernel not in the official repositories.

To deal with changes in the kernel, fix bugs, or add necessary features consider upgrading the DKMS package before rebooting.

## Usage
Usage for invoking DKMS manually.

Tab-completion is available by doing:

 # source /usr/share/bash-completion/completions/dkms

## List modules
To list the current status of modules, versions and kernels within the tree:

 # dkms status

## Rebuild modules
Rebuild all modules for the currently running kernel:

 # dkms autoinstall

or for a specific kernel:

 # dkms autoinstall -k 3.16.4-1-ARCH

To build a specific module for the currently running kernel:

 # dkms install -m nvidia -v 334.21

or simply:

 # dkms install nvidia/334.21

To build a module for all kernels:

 # dkms install nvidia/334.21 --all

## Remove modules
To remove a module (old ones are not automatically removed):

 # dkms remove -m nvidia -v 331.49 --all

or simply:

 # dkms remove nvidia/331.49 --all

If the package  is removed the information regarding previous module build files is lost. If this is the case, go through  and  and delete all files and directories no longer in use.

## DKMS package creation
See DKMS package guidelines.
