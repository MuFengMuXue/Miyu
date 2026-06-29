# Install Arch Linux via SSH

This article is intended to show users how to install Arch remotely via an SSH connection. Consider this approach when the host is located remotely or you wish to use the copy/paste ability of an SSH client to do the Arch install.

## On the remote (target) machine
Follow the steps from Installation guide#Pre-installation up to and including connecting to the internet (setting the keyboard layout and font can be skipped).

At that point, set the required root password to allow an SSH connection, since the default Arch password for root is empty:

 # passwd

Confirm that  is set in . If it is not, set it and reload the OpenSSH daemon  to apply the changes.

## On the local machine
On the local machine, connect to the target machine via SSH with the following command:

 $ ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@ip.address.of.target

From here one is presented with the live environment's welcome message and is able to administer the target machine as if sitting at the physical keyboard. At this point, if the intent is to simply install Arch from the live media, resume at Installation guide#Update the system clock. If the intent is to edit an existing Linux install that got broken, follow the Install from existing Linux wiki article.

## Installation on a headless server
This section describes installation of Arch Linux on a headless server without a keyboard, mouse or display. It uses an additional drive with cloud-init NoCloud configuration to automatically configure OpenSSH authorized keys and optionally iwd connection(s).

## Prepare cloud-init configuration files
There are three required cloud-init configuration files: ,  and .

The  file can be empty:

 $ printf "" > meta-data

 will contain the relevant configuration:

Replace  with your public SSH key. To add multiple keys, simply repeat the statement as shown above.

To automatically connect to a Wi-Fi network, use the  statement to create iwd network configuration files in the correct directory. For example:

cloud-init creates network configuration that differs from one shipped in the ISO. I.e. mDNS responder and DHCPv6 client are not enabled. To avoid this, disable cloud-init's network configuration in :

Once all three files are created they need to be placed on a drive with an ISO 9660 or FAT volume labeled .

## Using an additional FAT formatted drive
Use a FAT formatted drive. Copy ,  and  to the drive and change the file system's LABEL to .

You will need to attach this drive to the headless machine in addition to the one with the official ISO.

## Using an additional ISO
Create a  file using xorriso from :

 $ xorrisofs -output cloud-init.iso -volid CIDATA -joliet -rational-rock meta-data user-data network-config

Prepare the cloud-init data medium by burning  to an optical disc or, if deployment options permit, use the ISO as is.

## Using a single USB flash drive
If the installation image is written to e.g. a USB flash drive, provided there is enough space on the drive, an additional partition to house cloud-init data can be created.

Install ,  and .

First create a 2 MiB FAT image with its LABEL set to :

 $ mkfs.fat -C -n CIDATA cloud-init.img 2048

Copy the  and  files to the root of it:

 $ mcopy -i cloud-init.img meta-data user-data network-config ::

Repack the official ISO to include the FAT image as a third partition:

 $ xorriso -indev archlinux-version-x86_64.iso -outdev archlinux-version-x86_64-with-cidata.iso -append_partition 3 0x0c cloud-init.img -boot_image any replay

Finally follow USB flash installation medium#Using the ISO as is (BIOS and UEFI) to prepare the USB flash drive installation medium using the repacked ISO ().

## Using a single custom-built ISO
Alternatively, create a custom ISO using Archiso. This allows using only one drive regardless of type.

Use the releng profile as basis. Place the cloud-init configuration files in  and build the ISO.

## Boot from the installation medium
Once finished, deploy the installation medium and the cloud-init data medium (if it is separate) to the headless machine using the appropriate method.

Power up the headless machine and boot into a live Arch environment from the installation medium. Wait for a minute or so to allow the headless machine time to boot up and connect to the network.

From your existing machine (with keyboard and display) SSH into the live Arch environment on the headless server and complete the installation as described in the Installation guide.
