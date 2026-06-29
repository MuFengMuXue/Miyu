# Genfstab

is a Bash script that is used to automatically detect all mounts under a given mountpoint, its output can then be redirected into a file, usually .

## Installation
It is present by default on Arch installation media and can be installed as part of the  package on an already installed system.

There is also a stand alone fork of this tool that can be used on other distributions, you can find it here.

## Usage
You can get a list of your current mounts by using:

 $ genfstab /

The script supports finding mounts by kernel descriptor, device/partition label or device/partition UUID. It will output  by default (kernel descriptor being ), you can use , ,  or  for file system label, GPT partition label, file system UUID or GPT partition UUID respectively.

The more common usage scenario would be getting an fstab for a chroot, for this you would do something like the following:

 # mount /dev/sda3 /mnt
 # mount --mkdir /dev/sda1 /mnt/efi

In this case  shows both mounts below the mountpoint  and list them by device .

Usually you would want to redirect the output to a file, this can be achieved with the following:

 # genfstab -U /mnt >> /mnt/etc/fstab
