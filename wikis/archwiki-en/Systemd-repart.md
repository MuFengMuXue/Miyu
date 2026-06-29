# Systemd-repart

is a tool for manipulating GUID Partition Tables (GPTs).

## Installation
systemd-repart is part of systemd. It is also present on the Arch Linux installation ISO.

## Usage
## During Arch Linux Installation
systemd-repart can be used to create the necessary partitions during the Arch Linux installation process. Follow the steps below to set up your partitions.

First, create the required  configuration files. The following examples illustrate how to define partitions; adjust the parameters as needed for your specific setup.

Create the directory for the repart configuration files:

 # mkdir /etc/repart.d

Then, create the configuration files for each partition:

After creating the configuration files, you can check the proposed changes by running:

 # systemd-repart --empty=allow /dev/disk

If the output meets your expectations, you can apply the changes by executing:

 # systemd-repart --dry-run=no --empty=allow /dev/disk

This command will create the partitions as specified in your configuration files, and automatically encrypt and/or format them if required. Ensure that you have backed up any important data before proceeding, as this operation may overwrite existing data on the specified disk.

For more advanced configurations, refer to .

Then, mount the required partitions and proceed with the rest of the installation:

 # cryptsetup open /dev/disk/by-partlabel/root-x86-64 root
 # mount /dev/mapper/root /mnt
 # mount -m /dev/disk/by-partlabel/esp /mnt/boot
