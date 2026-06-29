# Proxmox/Install Arch Linux as a guest

Proxmox Virtual Environment also known as Proxmox VE is an open-source hypervisor used to run operating systems in a special environment, called a virtual machine, on top of the existing operating system. It comes with a WebUI interface.

This article is about installing Arch Linux in Proxmox.

## Virtual machine installation
To create  a virtual machine, first you need to upload an image to Proxmox. This can be done by going to one of the storage entries in the GUI, like , and selecting .

After this is done you can create a virtual machine either by clicking on the blue  button and going through the installer or running the following command:

 qm create 100 --memory 8192 --cdrom local:iso/archlinux-2025.08.01-x86_64.iso --net0 virtio,bridge=vmbr0 --scsi0 local-lvm:32 --start

Available install images can be listed with

 pvesm list local

## Container installation
First a container template should be downloaded

 pveam update
 pveam available
 pveam download local archlinux-base_20240911-1_amd64.tar.zst

As of writing, Proxmox 9 has not configured any Arch templates to be downloadable through its tools so they must be downloaded manually through http://download.proxmox.com/images/system/ and placed in

Then a container can be created from the template either by clicking on the blue  button and going through the installer or running the following command:

 pct create 100 local:vztmpl/archlinux-base_20240911-1_amd64.tar.zst --rootfs local-lvm:4 --memory 8192 --net0 name=eth0,bridge=vmbr0,ip=dhcp --features nesting=1

Once configured, a template can be created out of the container which can then be cloned

 pct template 100
 pct clone 100 101 --hostname cloned_name

## Installation using Arch Linux cloud image and Cloud-init
See Arch Linux on a VPS#Official Arch Linux cloud image.
