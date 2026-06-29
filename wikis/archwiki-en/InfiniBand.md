# InfiniBand

This page explains how to set up, diagnose, and benchmark InfiniBand networks.

## Introduction
## Overview
InfiniBand (abbreviated IB) is an alternative to Ethernet and Fibre Channel. IB provides high bandwidth and low latency. IB can transfer data directly to and from a storage device on one machine to userspace on another machine, bypassing and avoiding the overhead of a system call. IB adapters can handle the networking protocols, unlike Ethernet networking protocols which are ran on the CPU. This allows the OS's and CPU's to remain free while the high bandwidth transfers take place, which can be a real problem with 10Gb+ Ethernet.

IB hardware is made by Mellanox (which merged with Voltaire, and is heavily backed by Oracle) and Intel (which acquired QLogic's IB division in 2012). Mellanox was acquired by Nvidia in 2019. IB is most often used by supercomputers, clusters, and data centers. IBM, HP, and Cray are also members of the InfiniBand Steering Committee. Facebook, Twitter, eBay, YouTube, and PayPal are examples of IB users.

IB software is developed under the OpenFabrics Open Source Alliance

## Affordable used equipment
With large businesses benefiting so much from jumping to newer versions, the maximum length limitations of passive IB cabling, the high cost of active IB cabling, and the more technically complex setup than Ethernet, the used IB market is heavily saturated, allowing used IB devices to affordably be used at home or smaller businesses for their internal networks.

## Bandwidth
## Signal transfer rates
IB transfer rates corresponded in the beginning to the maximum supported by PCI Express (abbreviated PCIe), later on, as PCIe made less progress, the transfer rates corresponded to other I/O technologies and the number of PCIe lanes per port was increased instead. It launched using SDR (Single Data Rate) with a signaling rate of 2.5Gb/s per lane (corresponding with PCI Express v1.0), and has added: DDR (Double Data Rate) at 5Gb/s (PCI Express v2.0); QDR (Quad Data Rate) at 10Gb/s (matching the throughput of PCI Express 3.0 with improved coding of PCIe 3.0 instead of the signaling rate); and FDR (Fourteen Data Rate) at 14.0625Gbps (matching 16GFC Fibre Channel). IB is now delivering EDR (Enhanced Data Rate) at 25Gb/s (matching 25Gb Ethernet). Planned around 2017 will be HDR (High Data Rate) at 50Gb/s.

## Effective throughput
Because SDR, DDR, and QDR versions use 8/10 encoding (8 bits of data takes 10 bits of signaling), effective throughput for these is lowered to 80%: SDR at 2Gb/s/link; DDR at 4Gb/s/link; and QDR at 8Gb/s/link. Starting with FDR, IB uses 64/66 encoding, allowing a higher effective throughput to signaling rate ratio of 96.97%: FDR at 13.64Gb/s/link; EDR at 24.24Gb/s/lane; and HDR at 48.48Gb/s/link.

IB devices are capable of sending data over multiple links, though commercial products standardized around 4 links per cable.

When using the common 4X link devices, this effectively allows total effective throughputs of: SDR of 8Gb/s; DDR of 16Gb/s; QDR of 32Gb/s; FDR of 54.54Gb/s; EDR of 96.97Gb/s; and HDR of 193.94Gb/s.

## Latency
IB's latency is incredibly small: SDR (5us); DDR (2.5us); QDR (1.3us); FDR (0.7us); EDR (0.5us); and HDR ( query|...
FW Version:      2.7.1000
...
PSID:            MT_04A0110002}}
* Check latest firmware version
** Visit Mellanox's firmware download page (this guide incorporates this link's "firmware burning instructions", using its mstflint option)
** Choose the category of device you have
** Locate your device's PSID on their list, that mstflint gave you
** Examine the Firmware Image filename to see if it is more recent than your adapter's FW Version, i.e. , is version
* If there is a more recent version, download new firmware and burn it to your adapter
 $ unzip
 # mstflint -d  -i  burn

## For Intel/QLogic
Search for the model number (or a substring) over at Intel Download Center and follow the instructions. The downloaded software will probably need to be run from RHEL/CentOS or SUSE/OpenSUSE.

## Kernel modules
Edit  and  to your liking. Then load the kernel modules written in these files such as , or just reboot the system. (Although there should be no need to do this, start and enable both  and  if kernel modules are not loaded correctly. Rebooting the system will be fine).

## Subnet manager
Each IB network requires at least one subnet manager. Without one, devices may show having a link, but will never change state from  to . A subnet manager often (typically every 5 or 30 seconds) checks the network for new adapters and adds them to the routing tables. If you have an IB switch with an embedded subnet manager, you can use that, or you can keep it disabled and use a software subnet manager instead. Dedicated IB subnet manager devices also exist.

## Enable port
If the port is in the physical state  (can be verified with ) then it first needs to be enabled by running  for it to wake up. This may need to be automated at boot if the ports at both ends of the link are sleeping.

## Software subnet manager
On one system:

* Install
* Correct the systemd file  as the following instruction.
* Start and enable

The current opensm's configuration for opensm is not compatible with RDMA's systemd configuration. That is, edit the 2 lines in  as following (Commented ones are original contents.).

All of your connected IB ports should now be in a (port) state of , and a physical state of . You can check this by running ibstat.

Or by examining the  filesystem:

## TCP/IP (IPoIB)
You can create a virtual Ethernet Adapter that runs on the HCA. This is intended so programs designed to work with TCP/IP but not IB, can (indirectly) use IB networks. Performance is negatively affected due to sending all traffic through the normal TCP stack; requiring system calls, memory copies, and network protocols to run on the CPU rather than on the HCA.

IB interface will appear when the module  is loaded. The simple configuration to make it appear is adding the line  in  then rebooting the system. After booting the system with the module , links with the name like  should be confirmed with the command .

Detailed configuration is possible for the IB interface (e.g. naming it  and assigning IP addresses like a traditional Ethernet adapter).

## Connection mode
IPoIB can run in datagram (default) or connected mode. Connected mode allows you to set a higher MTU, but does increase TCP latency for short messages by about 5% more than datagram mode.

To see the current mode used:

 $ cat /sys/class/net/interface/mode

## MTU
In datagram mode, UD (Unreliable Datagram) transport is used, which typically forces the MTU to be 2044 bytes. Technically to the IB L2 MTU - 4 bytes for the IPoIB encapsulation header, which is usually 2044 bytes.

In connected mode, RC (Reliable Connected) transport is used, which allows a MTU up to the maximum IP packet size, 65520 bytes.

To see your MTU:

 $ ip link show interface

## Finetuning connection mode and MTU
You only need  if you want to change the default connection mode and/or MTU.

* Install and set up TCP/IP over IB (IPoIB)
* Install
* Configure  through , which contains instructions on how to do so
** It defaults to setting a single IB port  to  mode and MTU
* Start and enable

Different setups will see different results. Some people see a gigantic (double+) speed increase by using  mode and MTU , and a few see about the same or even worse speeds. Use qperf and iperf to finetune your system.

Using the qperf examples given in this article, here are example results from an SDR network (8 theoretical Gb/s) with various finetuning:
{| class="wikitable"
! Mode !! MTU !! MB/s !! us latency
|-
| datagram || 2044 || 707 || 19.4
|-
| connected || 2044 || 353 || 18.9
|-
| connected || 65520 || 726 || 19.6
|}

## Soft RoCE (RXE)
Soft ROCE is a software implementation of RoCE that allows using Infiniband over any ethernet adapter.

* Install
* Run  to configure an RXE instance on ethernet device ethN.

You should now have an rxe0 device:

## Remote data storage
You can share physical or virtual devices from a target (host/server) to an initiator (guest/client) system over an IB network, using iSCSI, iSCSI with iSER, or SRP. These methods differ from traditional file sharing (i.e. Samba or NFS) because the initiator system views the shared device as its own block level device, rather than a traditionally mounted network shared folder. i.e. ,

The disadvantage is only one system can use each shared device at a time; trying to mount a shared device on the target or another initiator system will fail (an initiator system can certainly run traditional file sharing on top).

The advantages are faster bandwidth, more control, and even having an initiator's root filesystem being physically located remotely (remote booting).

## targetcli
 acts like a shell that presents its complex (and not worth creating by hand)  as a pseudo-filesystem.

## Installing and using
On the target system:
* Install
* Start and enable

In :
* In any pseudo-directory, you can run  to see the commands available in that pseudo-directory or  (like ) for more detailed help
* Tab-completion is also available for many commands
* Run  to see the entire pseudo-filesystem at and below the current pseudo-directory

## Create backstores
Enter the configuration shell:

 # targetcli

Within , setup a backstore for each device or virtual device to share:
* To share an actual block device, run: ; and
* To share a file as a virtual block device, run: ; and
* To share a physical SCSI device as a pass-through, run: ; and
* To share a RAM disk, run: ; and
* Where name is for the backstore's name
* Where dev is the block device to share (i.e. , , , or a LVM logical volume )
* Where file is the file to share (i.e. )
* Where size is the size of the RAM disk to create (i.e. 512MB, 20GB)

## iSCSI
iSCSI allows storage devices and virtual storage devices to be used over a network. For IB networks, the storage can either work over IPoIB or iSER.

There is a lot of overlap with the iSCSI Target, iSCSI Initiator, and iSCSI Boot articles, but the necessities will be discussed since much needs to be customized for usage over IB.

## Over IPoIB
Perform the target system instructions first, which will direct you when to temporarily switch over to the initiator system instructions.

* On the target and initiator systems, install TCP/IP over IB

* On the target system, for each device or virtual device you want to share, in :
** Create a backstore
** For each backstore, create an IQN (iSCSI Qualified Name) (the name other systems' configurations will see the storage as)
*** Run: ; and . It will give you a randomly_generated_target_name, i.e.
*** Set up the TPG (Target Portal Group), automatically created in the last step as tpg1
**** Create a lun (Logical Unit Number)
***** Run: ; and . Where  is a full path to an existing storage object, i.e.
**** Create an acl (Access Control List)
***** Run: ; and , where  is the initiator system's IQN (iSCSI Qualified Name), aka its (World Wide Name)
****** Get the  by running on the initiator system, not this target system: (after installing on it )
** Save and exit by running: ; ; and

* On the initiator system:
** Install
** At this point, you can obtain this initiator system's IQN (iSCSI Qualified Name), aka its wwn (World Wide Name), for setting up the target system's :
***  should have displayed
*** Otherwise, run:  to see
** Start and enable
** To automatically login to discovered targets at boot, before discovering targets, edit  to set
** Discover online targets. Run  as root, where portal is an IP (v4 or v6) address or hostname
*** If using a hostname, make sure it routes to the IB IP address rather than Ethernet - it may be beneficial to just use the IB IP address
** To automatically login to discovered targets at boot, Start and enable
** To manually login to discovered targets, run  as root.
** View which block device ID was given to each target logged into. Run  as root. The block device ID will be the last line in the tree for each target ( is the print command, its option is the verbosity level, and only level 3 lists the block device IDs)

## Over iSER
iSER (iSCSI Extensions for RDMA) takes advantage of IB's RDMA protocols, rather than using TCP/IP. It eliminates TCP/IP overhead, and provides higher bandwidth, zero copy time, lower latency, and lower CPU utilization.

Follow the iSCSI Over IPoIB instructions, with the following changes:

* If you wish, instead of installing IPoIB, you can just install RDMA for loading kernel modules
* On the target system, after everything else is setup, while still in , enable iSER on the target:
** Run  for each iqn you want to have use iSER rather than IPoIB
*** Where iqn is the randomly generated target name, i.e.
** Run
** Save and exit by running: ; ; and
* On the initiator system, when running  to discover online targets, use the additional argument , and when you login to them, you should see:

## Adding to /etc/fstab
The last time you discovered targets, automatic login must have been turned on.

Add your mount entry to  as if it were a local block device, except add a  option to avoid attempting to mount it before network initialization.

## Network segmentation
An IB subnet can be partitioned for different customers or applications, giving security and quality of service guarantees. Each partition is identified by a PKEY (Partition Key).

## SDP (Sockets Direct Protocol)
Use  (successor to rsockets and libspd) and  to intercept non-IB programs' socket calls, and transparently (to the program) send them over IB via RDMA. Dramatically speeding up programs built for TCP/IP, much more than can be achieved by using IPoIB. It avoids the need to change the program's source code to work with IB and can even be used for closed source programs. It does not work for programs that statically link in socket libraries.

## Diagnosing and benchmarking
All IB specific tools are included in  and .

## ibstat - View a computer's IB GUIDs
ibstat will show you detailed information about each IB adapter in the computer it is ran on, including: model number; number of ports; firmware and hardware version; node, system image, and port GUIDs; and port state, physical state, rate, base lid, lmc, SM lid, capability mask, and link layer.

This example shows a Mellanox Technologies (MT) adapter. Its PCI Device ID is reported (25418), rather than the model number of part number. It shows a state of "Active", which means is it properly connected to a subnet manager. It shows a physical state of "LinkUp", which means it has an electrical connection via cable, but is not necessarily properly connected to a subnet manager. It shows a total rate of 20 Gb/s (which for this card is from a 5.0 Gb/s signaling rate and 4 virtual lanes). It shows the subnet manager assigned the port a lid of 3.

## ibhosts - View all hosts on IB network
ibhosts will show you the Node GUIDs, number of ports, and device names, for each host on the IB network.

## ibswitches - View all switches on IB network
ibswitches will show you the Node GUIDs, number of ports, and device names, for each switch on the IB network. If you are running with direct connections only, it will show nothing.

 # ibswitches

## iblinkinfo - View link information on IB network
iblinkinfo will show you the device names, Port GUIDs, number of virtual lanes, signal transfer rates, state, physical state, and what it is connected to.

This example shows two adapters directly connected with out a switch, using a 5.0 Gb/s signal transfer rate, and 4 virtual lanes (4X).

## ibping - Ping another IB device
ibping will attempt pinging another IB GUID. ibping must be ran in server mode on one computer, and in client mode on another.

ibping must be ran in server mode on one computer.

 # ibping -S

And in client mode on another. It is pinging a specific port, so it cannot take a CA name, or a Node or System GUID. It requires  with a Port GUID, or  with a Lid.

If you are running IPoIB, you can use regular  which pings through the TCP/IP stack. ibping uses IB interfaces, and does not use the TCP/IP stack.

## ibdiagnet - Show diagnostic information for entire subnet
ibdiagnet will show you potential problems on your subnet. You can run it without options.  specifies the expected link width (number of virtual lanes) for your computer's adapter, so it can check if it is running as intended.  specifies the expected link speed (signaling rate) for your computer's adapter, so it can check if it is running as intended, but it does not yet support options faster than 10 for FDR+ devices.  overrides the default number of packets to be sent of 10.

## qperf - Measure performance over RDMA or TCP/IP
qperf can measure bandwidth and latency over RDMA (SDP, UDP, UD, and UC) or TCP/IP (including IPoIB)

qperf must be ran in server mode on one computer.

 $ qperf

And in client mode on another. SERVERNODE can be a hostname, or for IPoIB a TCP/IP address. There are many tests. Some of the most useful are below.

 $ qperf SERVERNODE OPTIONS TESTS

## TCP/IP over IPoIB
## iperf - Measure performance over TCP/IP
iperf is not an IB aware program, and is meant to test over TCP/IP or UDP. Even though qperf can test your IB TCP/IP performace using IPoIB, iperf is still another program you can use.

iperf must be ran in server mode on one computer.

 $ iperf3 -s

And in client mode on another.

iperf shows Transfer in base 10 GB's, and Bandwidth in base 2 GB's. So, this example shows 6.23GB (base 10) in 10 seconds. That is 6.69GB (base 2) in 10 seconds. (6.23 * 2^30 / 10^9) That's 5.35 Gb/s (base 2), as shown by iperf. (6.23 * 2^30 / 10^9 * 8 / 10) That is 685 MB/s (base 2), which is roughly the speed that qperf reported. (6.23 * 2^30 / 10^9 * 8 / 10 * 1024 / 8)

## Common problems / FAQ
## Connection problems
## Link, physical state and port state
* See if the IB hardware modules are recognized by the system. If you have an Intel adapter, you will have to use Intel here and look through a few lines if you have other Intel hardware:

If nothing is shown, your kernel is not recognizing your adapter. This example shows approximately what you will see if you have a Mellanox ConnectX adapter, which uses the mlx4_0 kernel module.

* Check the port and physical states. Either run ibstat or examine .

or

The physical state should be "LinkUp". If it is not, your cable likely is not plugged in, is not connected to anything on the other end, or is defective. The (port) state should be "Active". If it is "Initializing" or "INIT", your subnet manager does not exist, is not running, or has not added the port to the network's routing tables.

* Can you successfully ibping which uses IB directly, rather than IPoIB? Can you successfully , if you are running IPoIB?

* Consider upgrading firmware.

## getaddrinfo failed: Name or service not known
* Run ibhosts to see the CA names at the end of each line in quotes.

## Speed problems
* Start by double-checking your expectations.
How have you determined you have a speed problem? Are you using qperf or iperf, which both transmit data to and from memory rather than hard drives. Or, are you benchmarking actual file transfers, which relies on your hard drives? Unless you are running RAID to boost speed, even with the fastest SSD's available in mid 2015, a single hard drive (or sometimes even multiple ones) will be bottlenecking your IB transfer speeds. Are you using RDMA or TCP/IP via IPoIB? If so, there is a performance hit for using IPoIB instead of RDMA.

* Check your link speeds. Run ibstat, iblinkinfo, or examine .

or

or

Does this match your expected bandwidth and number of virtual lanes?

* Check diagnostic information for entire subnet. Run #ibdiagnet - Show diagnostic information for entire subnet. Make sure to use  with the proper signaling rate, which is likely the advertised speed of your card divided by 4.
 # ibdiagnet -lw  -c 1000

* Consider upgrading firmware.
