# Systemd-firstboot

Starting with version 216 of systemd, the command systemd-firstboot allows for setting of basic system settings before or during the first boot of a newly created system. The tool is able of initialize the following system settings: timezone, locale, hostname, the root password, as well as automated generation of a machine ID.

As systemd-firstboot interacts with the filesystem directly and does not make use of the related systemd services (such as timedatectl, hostnamectl or localectl), it should not be executed on an already running system.

Settings can be specified non-interactively when externally used on filesystem images, or interactively if executed during the early boot process.

A default Arch Linux installation will set most variables systemd-firstboot is able to manipulate, or facilitate the creation of skeleton files which prevent its use when installing the systemd package through pacstrap.

## Installation
systemd-firstboot is part of and packaged with .

## Usage
## Interactively configure system settings during boot of a fresh Arch Linux installation
Allowing systemd-firstboot to manipulate a previously un-booted Arch Linux installation is particularly useful in situations where installation is undertaken by an individual other than the eventual end user, such as in the distribution of laptops with a pre-loaded install.

The following steps should be appended to the end of the Configure the system section of the Installation guide, before the target partitions are unmounted, thus taking place within the chroot of the new installation. Make sure all locales you want available have been generated, non-generated ones will not be offered as a possible setting.

## Delete existing settings
If the following files are present, systemd-firstboot will not prompt for the setting they relate to.

 # rm /etc/{machine-id,localtime,hostname,shadow,locale.conf}

Edit  and remove the root account from it, otherwise the root will be treating as configured and systemd-firstboot will not prompt for the root password.

## Modify and enable systemd-firstboot.service
Use a drop-in file in which  makes systemd-firstboot query for all possible settings and  the  section specifies where in the boot process the service is to be activated.

Enable

## Finalize installation
Continue installing as per the Installation guide. Unless more configuration is to be undertaken, exit the chroot, unmount the partitions and shut down. Upon the next boot, systemd-firstboot will execute. Presuming no other changes to system configuration are made, removing the files above and rebooting will trigger systemd-firstboot again, in case you wish to test whether the installation worked.
