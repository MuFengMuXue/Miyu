# Mkosi

mkosi stands for Make Operating System Image, and is a tool for easily building customized OS images. It's a fancy Python wrapper around dnf, apt, pacman and zypper that may generate disk images with a number of bells and whistles.

It has nifty features like:
*  to build images as an unpriviliged user
* An Overlay filesystem to re-use existing distribution package caches reducing disk space requirements
* Deep Freedesktop.org and systemd integration
* Wide range of output formats like Raw GPT disk image, plain directory, tar, cpio and USI / UKI.

The project is actively maintained and provides  for customizing images across various distributions.

On Arch Linux,  can be used to build bootable Unified Kernel Images (UKI), including those signed for Secure Boot. Creating images with encrypted LUKS volumes is as straightforward as defining  in . Package lists can be defined directly in the  file under the  section, and additional files or configuration can be added using overlay directories such as .

mkosi has a strong focus on developer workflows such as testing, debugging, and producing minimal, production-ready images. A common use case involves adding a  configuration file to a project (e.g. written in C or Python), which then allows automated image generation tailored to the project’s needs.

During the build process, mkosi can create a temporary development image that includes headers and tooling, compile the project within it, run tests, and then discard this image. It subsequently builds a second image without development dependencies, containing only the resulting build artifacts and any other explicitly configured packages.

This resulting image is minimal, self-contained, and suitable for deployment via tools such as RAUC, or OSTree, making it well-suited for automated provisioning of servers, embedded systems, or IoT targets.

## Installation
Install . Depending on what distribution you want to use in your OS tree/image, install the following packages:

{| class="wikitable"
! Distribution
! Package
|-
| Arch
|
|-
| Debian
| , ,
|-
| Ubuntu
| , ,
|-
| Fedora
|
|-
| OpenSUSE
|
|-
| CentOS
|
|-
|}

## Basic usage
You can create an image by just running it without any arguments:

 $ mkosi

You can specify option as arguments or by editing files in the current folder.

## Create and boot a Debian image
The following example will create a bootable image with the latest Debian version and packages openssh-client and vim installed. This command requires mkosi's optional dependencies  and . Depending on the image, can also be built by an unprivileged (non-root) user:

 $ mkosi --distribution debian --release trixie --format disk --checksum --root-password password --include mkosi-vm --package openssh-client,vim --repository-key-fetch=yes --output image.raw

systemd-nspawn can boot the resulting image:

 # systemd-nspawn --boot --image image.raw

It can also be virtualized with QEMU/KVM or with :

 $ mkosi --output image.raw --qemu-smp 2 qemu

You can also write this image to a USB drive and use it to boot your computer.

## Using configuration files
The same Debian image can be created using a configuration file, , and then run mkosi without any arguments:

The built-in  profile adds the necessary packages in order to run a system and is maintained by the mkosi maintainers.

Downloaded package files and temporary build files are stored in the home cache directory or in  and .

## Configuration settings
Settings can be specified as command-line arguments or, for example, in a file called  in the current directory.
The most important settings are:

{| class="wikitable"
! Command line
! Configuration file
! Description
|-
|
|
| Name of the distribution to install. Supported are:
|-
|
|
| Version of the distribution: a numeric string or a distribution version name ()
|-
|
|
| Format of the image to create. For example:
* directory: plain directory
* disk: image file with GPT partition table
* tar: tarball of a plain directory
|-
|
|
| Name of the image file or directory
|-
|
|
| Location of the image file or directory (and other generated artifacts)
|-
|
|
| Enable or disable generation of a bootable image:
|-
|
|
| List of packages to be installed into the image: (multi) line and/or comma separated list
|-
|
|
| Initial root password
|}

## Usage as initramfs generator
Mkosi provides a kernel-install plugin to build an initramfs, similarly to mkinitcpio or dracut.

In order to use it, install  and edit the kernel-install configuration file:
