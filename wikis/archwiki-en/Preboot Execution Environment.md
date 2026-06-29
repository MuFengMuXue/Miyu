# Preboot Execution Environment

From Wikipedia:Preboot Execution Environment:
:The Preboot eXecution Environment (PXE, most often pronounced as pixie) specification describes a standardized client-server environment that boots a software assembly, retrieved from a network, on PXE-enabled clients. On the client side it requires only a PXE-capable network interface controller (NIC), and uses a small set of industry-standard network protocols such as DHCP and TFTP.

In this guide, PXE is used to boot the installation medium with an appropriate option ROM that supports PXE on the target. This works well when you already have a server set up.

## Preparation
## Overview
It is useful to give an overview of the PXE boot process in order to understand the #Server setup, the #Installation on the client side and the Arch Linux files needed.

The client starts by broadcasting packets asking for a DHCP server and containing specific PXE options. The DHCP server responds with networking information (the IP address assigned to the client) and also provides, by using specific bootstrap protocol (BOOTP) parameters of the DHCP, additional information like the TFTP server address, the path of the initial network bootstrap program (NBP) to download or the boot configuration file name.

The NBP is transferred from the PXE server to the client using TFTP, to be loaded into memory and executed. The kernel and the initramfs are also transferred this way.

Then the root file system is transferred using one of the following protocols: HTTP, NFS or NBD.

## Boot from install medium
In order to gather the files that will be transferred from the server to the client for booting, get the latest official install image from the download page.

Next mount the image:

 # mount --mkdir -o loop,ro archlinux-release_date-x86_64.iso /mnt/archiso

where  is the release date in the ISO filename like, e.g., .

## Boot from netboot
Arch Linux netboot images can be used to download the latest Arch Linux release on the fly upon system boot. Download the image compatible with your configuration.

## Pixiecore
An all-in-one solution is provided by pixiecore

# Install
# Run  as root
# Boot via PXE

## Server setup
You will need to setup a DHCP server, a TFTP server for transferring the NBP and one of the following services for transferring the root file system: HTTP server, NFS or NBD.

## Network
Bring up your wired network adapter, and assign it an address appropriately.

 # ip link set eth0 up
 # ip addr add 192.168.0.1/24 dev eth0

You can also use one of the network managers to configure the static IP.

## DHCP + TFTP
You will need both a DHCP server and a TFTP server to configure networking on the install target and to facilitate the transfer of files between the server and the client.
dnsmasq does both, and is extremely easy to set up.

Install the  package.

dnsmasq needs to be configured.
See instructions on how to setup a dnsmasq#TFTP server and a dnsmasq#PXE server.

Are provided below some common configuration instructions. tftp_root is the directory where the Arch ISO is mounted (e.g. ) or where the network boot program is located.

To enable the DHCP server and give IPv4 addresses within a range, add to the configuration file a line similar to:

 dhcp-range=192.168.0.50,192.168.0.150

Or in case there is already a DHCP-server running on the network and you want to interoperate with it, see dnsmasq#Proxy DHCP.

Two examples covering different boot style and installation media are provided below.

Once configured according to your needs, start .

## BIOS boot from install medium
The path of the initial bootstrap program to be transferred is defined with the  option in the configuration file.

 dhcp-boot=/boot/syslinux/lpxelinux.0

In order to send specific bootstrap protocol (BOOTP) parameters, like the configuration file path, the  line is used.

 dhcp-option-force=209,archiso_pxe.cfg # this file might be under /mnt/archiso/boot/syslinux
 dhcp-option-force=210,

## UEFI boot from netboot
To send a file depending on the architecture, here the netboot image for UEFI-style boot, use:

 pxe-service=BC_EFI, "Boot from network BC EFI", ipxe.efi
 pxe-service=X86-64_EFI, "Boot from network X86-64 EFI", ipxe.efi

If using netboot, the rest of the server setup section which focuses on the Arch ISO does not apply.

## Transferring archiso root file system
Thanks to ,  and  initcpio hooks in archiso, it is possible to boot using HTTP, NFS or NBD. Boot time is approximately the same in all three methods, but HTTP method allows you to watch a state of downloading  in percents.

## HTTP
Among all alternatives, darkhttpd is by far the most trivial to setup (and the lightest-weight).

First, install the  package.

Then start darkhttpd using our  as the document root:

## NFS
You will need to set up an NFS server with an export at the root of your mounted installation medium, which would be  if you followed #Preparation. After setting up the server, add the following line to your  file:

If the server was already running, re-export the file systems with .

The default settings in the installer expect to find the NFS at , so you will need to edit the boot options.  To do this, press Tab on the appropriate boot menu choice and edit the  option accordingly:

 archiso_nfs_srv=${pxeserver}:/mnt/archiso

Alternatively, you can use  for the entire process.

After the kernel loads, the Arch bootstrap image will copy the root file system via NFS to the booting host.  This can take a little while.  Once this completes, you should have a running system.

## NBD
Install the  package and configure it:

where  is the release date in the ISO filename like, e.g., .

Start .

## Existing PXE server
If you have an existing PXE server with a PXELINUX system setup (e.g. a combination of DHCP and TFTP), you can add the following menu items to your  file in order to boot Arch via your preferred method.

Since PXELINUX supports HTTP, only the boot loader needs to be transferred over TFTP, everything else can use HTTP. E.g.:

For NFS and NBD, the kernel and initramfs must be downloaded from TFTP. E.g., for NFS:

The  and  paths are relative to TFTP root. For NBD, replace  with  in the above example. See usage examples in  file resided on Arch Linux ISO.

Whichever method you choose, you must pass  parameter to instruct the kernel to bring up the network interface before it attempts to mount the installation medium over the network. Passing  is required when there are several wired interfaces on the client side and/or you want  to be already configured inside booted archiso. You can use sysappend mask  (which is +) to pass these parameters automatically. For available boot parameters see README.bootparams.

## Installation
For this portion you will need to figure out how to tell the client to attempt a PXE boot; in the corner of the screen along with the normal post messages, usually there will be some hint on which key to press to try PXE booting first. On an IBM x3650  brings up a boot menu, the first option of which is Network; on a Dell PE 1950/2950 pressing  initiates PXE booting directly.

## Boot
Looking at journald on the PXE server will provide some additional insight to what exactly is going on during the early stages of the PXE boot process:

After you load  and  via TFTP, you will (hopefully) be presented with a syslinux boot menu with several options, where you can select Boot Arch Linux (x86_64) (HTTP).

Next the kernel and initramfs (appropriate for the architecture you selected) will be transferred, again via TFTP:

If all goes well, you should then see activity on darkhttpd coming from the PXE-target; at this point the kernel would be loaded on the PXE-target, and in init:

After the root file system is downloaded via HTTP, you will eventually end up at the normal live system root zsh prompt.

## Post-boot
Unless you want all traffic to be routed through your PXE server (which will not work anyway unless you set it up properly), you will want to stop  and get a new lease on the install target, as appropriate for your network layout.

You can also kill darkhttpd; the target has already downloaded the root file system, so it is no longer needed. While you are at it, you can also unmount the installation image:

 # umount /mnt/archiso

At this point you can follow the Installation guide.

## Low memory systems
The  initramfs option can be used to control whether the root file system should be copied to ram in its entirety in early-boot.

It highly recommended to leave this option alone, and should only be disabled if entirely necessary (systems with less than ~256MB physical memory). Append  to your kernel line if you wish to do so.

## Sharing internet with PXE clients
If your network for PXE clients is private (for example, 192.168.1.0/24), and you want them to be able to access internet (for example, for packages installation), you should configure masquerade/source nat properly. Your PXE server must have a separate NIC connected to the internet. You can use such command to pass through the internet to clients:

 iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -j MASQUERADE

To make this rule persistent after reboot, run the following command:

 iptables-save -f /etc/iptables/iptables.rules

and enable .

See Simple stateful firewall#Setting up a NAT gateway and Internet sharing#Enable NAT for more information.

## Troubleshooting
## DHCP interface rename bug
 causes default predictable network interface renaming to fail and then DHCP client to fail because of it. A workaround is to add the kernel boot parameter  to disable predictable interface names.

## VirtualBox cannot boot while real machines can
When using VirtualBox to test your configuration, the virtual machine may get stuck at:

 Probing EDD (edd=off to disable)... ok

While PXE booting with a real machine works fine. The problem may be because you have set several CPU cores to your client machine, and you set its type as Other and version as Other/Unknown (64 bit). So VirtualBox does not know which paravirtualization interface to use by default.

Adding  to the kernel parameters lets you see where it actually got stuck:

 [    0.063697] smp: Bringing up secondary CPUs...
 [    0.103768] x86: Booting SMP configuration:

To resolve this, either use one CPU core, or go to Machine > Settings > System > Acceleration and set one of the following paravirtualization interface: Minimal, Hyper-V or KVM.
