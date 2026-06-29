# Kernel-install

is a flexible utility designed to streamline the installation and administration of Linux kernel images on a system. It features a plugin system, allowing for seamless integration with other utilities. These plugins define a range of actions and configurations required during the installation and management of Linux kernel images. Examples of such tasks include configuring boot loader entries, generating Unified kernel images (UKI), or facilitating kernel signing for Secure Boot compliance.

## Installation
kernel-install is part of and packaged with . The  optional dependency is also needed for unified kernel images unless a different UKI generator is specified (see #Main configuration).

## Configuration
## Main configuration
The main configuration file is . Use it to configure the layout you want to use, i.e.  for traditional split kernel and initramfs images, or  for Unified kernel images:

## Kernel command line
Kernel parameters must be set in . They will either be embedded in the UKI, or added to the boot loader configuration, according to the layout used. If  doesn't exist, kernel install will use the parameters in  or , not setting the kernel parameters in  could result in kernel-install using the parameters of the current running kernel.

## Plugins
To list active plugins used by  when installing, upgrading, or removing a kernel image, you can use the  argument:

Available plugins are found under :

Similarly named files in  will override the default ones.

For example, to disable the default  plugin (which automatically signs new UKIs for Secure Boot):

 # ln -sf /dev/null /etc/kernel/install.d/91-sbctl.install

You can also write your own  plugins, and place them in .

## Unified kernel images
See Unified kernel image#kernel-install

## Usage
## Manually
To manually install a kernel from , use the following  command:

 # kernel-install add A.B.C-name /usr/lib/modules/A.B.C-name/vmlinuz

To remove a kernel manually, use the  command:

 # kernel-install remove A.B.C-name

## Automatically
To trigger  and all active plugins automatically when a kernel package is installed or updated, you can install .
