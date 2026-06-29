# Makepkg-optimize

is a collection of supplemental tidy, buildenv, and executable scripts for pacman which provide macros for several kinds of optimization in the  and  stages.

## Installation
Install  and, to make available optimizations requiring them, install backends: , , , , and .

## Configuration
 generates a redundant configuration file, , from your current  configuration.

This file lists supplementary COMPILE FLAGS, BUILD ENVIRONMENT options, GLOBAL PACKAGE OPTIONS, PACKAGE OUTPUT options, and COMPRESSION DEFAULTS, all of which are disabled by default.

## Build an optimized package
After selecting your preferred optimizations, pass the configuration file when building:

 $ makepkg -c --config /etc/makepkg-optimize.conf

## Build an optimized package in a clean chroot
Alternatively,  can be used to build optimized packages within a classic way of clean chroot.

## Chroot setup
After setting up a chroot, a few additional steps are needed.

First, install some of the backends for the optimization macros to the base chroot:

 $ arch-nspawn "$CHROOT"/root pacman -S openmp upx optipng polly

Then download and build the  and  packages.

To install them in the base chroot, copy their package files into it and install them, e.g.:

 # cp svgo-1.2.2-2-any.pkg.tar.xz "$CHROOT"/root/root/
 $ arch-nspawn "$CHROOT"/root pacman -U /root/svgo-1.2.2-2-any.pkg.tar.xz

## Using the chroot
## Build a package
First, edit  and select your preferred optimizations.

When building, pass the configuration file to :

 $ makechrootpkg -c -r "$CHROOT" -- -c --config /etc/makepkg-optimize.conf

## Building with PGO
The  option for  enables either generation or application of profiles, depending on if this is the first or second build of the package with this flag enabled. Clean chroot building complicates this because the software is run outside of the chroot to generate profiles, but the profiles need to be applied from inside the chroot when recompiling later. The solution is to bridge the three filesystems with a bind mounted folder.

## Create a PGO cache
Create and bind a folder to store profiles:

 # mkdir -m 777 {"$CHROOT"/{root,"$USER"},}/mnt/pgo
 # mount -o bind {,"$CHROOT"/root}/mnt/pgo
 # mount -o bind "$CHROOT"/{root,"$USER"}/mnt/pgo

Edit  and set .

## Profile a program
Build, then install the package and test-run its executables.

After thoroughly utilizing the software, close it, then rebuild and reinstall its package.
