# ISCSI/Boot

Arch Linux can be installed on an iSCSI target. This allows the machine to only contain enough mass storage to contain a boot loader, such as an USB drive, while its root partition is accessed over the network with iSCSI. Any subsequent partitions can also be accessed with iSCSI, or with some other network storage protocol, such as NFS. When combined with PXE, iBFT, or some other method of network booting, it allows the machine to not contain any mass storage.

## Boot process
There are various ways of mounting an iSCSI target at boot time:

* Using a standard initramfs that is configured to initialize a network connection and mount the iSCSI target, and finally boot into it. The procedure for this is outlined below.
* Certain firmwares (BIOS or UEFI) and network adapters can initialize a network connection and mount an iSCSI target themselves before booting into the OS contained in the iSCSI target. This requires installing a boot loader in the target as well. This is common in server- and enterprise-grade hardware. Consult your hardware manual and manufacturer on how to achieve this.
* Using a custom PXE firmware, such as iPXE, to mount the iSCSI target and boot into it.

## Preparation
## Target setup
Follow the procedure outlined in iSCSI to setup an iSCSI target on a remote machine.

## Pre-installation
Boot into the Arch Linux installer using the latest official installation media from the download page. Follow the installation guide up until partitioning.

## iSCSI initiator setup
If needed, adjust your initiator name in the iSCSI configuration.

Discover the available iSCSI targets on the remote machine to ensure they are visible to the installer. Adjust the portal IP address to match your environment. The output will depend on your environment; ensure it matches the target you set up earlier.

Login to the iSCSI target.

 # iscsiadm -m node -T TARGET_NAME -p PORTAL_IP_ADDRESS -l

The iSCSI block device is now available. Verify the output of lsblk to ensure the block device is available. The kernel log messages may contain helpful information if accessing the target fails.

Continue installing Arch on the iSCSI target as usual, up until you generate the initramfs and install the boot loader.

## System setup
## iSCSI daemon
Install the  package in the new system.

Start/enable .

## Fstab
The install procedure automatically generates  to match the new install. Ensure the root filesystem is added correctly. The iSCSI daemon handles any errors in the iSCSI kernel layer, so it is important to keep it running as long as the root filesystem - and any other iSCSI filesystems - are mounted. This can be achieved by appending  to the filesystem mount options. For example:

## initramfs
This guide outlines a method which uses a busybox-based init, as opposed to a systemd-based init. The procedure will be different for a systemd-based init.

## Connect to the network automatically
The initcpio has to connect to the network before opening a connection to the iSCSI target. This can be achieved in various ways, but a simple way is to use the net-hook with the  kernel parameter. This hook is designed to be used with an NFS-based root, but omitting the NFS-specific parameters lets it only configure the network adapter.

Install the  in the new system.

Insert the  hook in the  array:

Append the  parameter accordingly to the kernel parameters. For example, to configure the  network adapter with DHCP:

## Start the iSCSI session automatically
In order to start the iSCSI session in the initramfs, a custom hook must be created for it. The hook consists of a build hook and a runtime hook, as explained in Mkinitcpio#HOOKS.

The build hook will add the required iSCSI modules to the initramfs, and the  binary.

{{hc|1=/etc/initcpio/install/iscsi|
2=build () {
        map add_module iscsi_tcp iscsi_ibft libiscsi libiscsi_tcp scsi_transport_iscsi crc32c
        add_checked_modules "/drivers/net"
        add_binary iscsistart
        add_runscript
}

help () {
cat  /sys/block/sdX/device/timeout}}

where the value is in seconds, or with an udev rule:

{{hc|/etc/udev/rules.d/50-iscsi.rules|2=
ACTION=="add", SUBSYSTEM=="scsi" , ATTR{type}=="0|7|14", RUN+="/bin/sh -c 'echo Y > /sys$$DEVPATH/timeout'"

}}

## Improving performance
Since low-level I/O-commands will go through the IO scheduler on the remote system, and are subsequently queued there, it is possible to disable any queuing algorithm on the initiator system by using the  setting for the queuing algorithm for the iSCSI device. See Improving performance#Input/output schedulers for details and configuration.

## Troubleshooting
## Detected conn error (1011)
This can occur for multiple reasons:

* The initiator, target, or network is overwhelmed from iSCSI no-ops, causing a busy connection be considered disconnected, in which case the SCSI error handler overrides the device, which can break the working-but-busy iSCSI session. See #Make the iSCSI daemon resilient to network problems on how to disable the no-ops.
* The network adapter's MTU is mismatched from that of the rest of the network.
* In rare cases, when TCP window scaling is enabled. It can be disabled with sysctl with the  setting.
