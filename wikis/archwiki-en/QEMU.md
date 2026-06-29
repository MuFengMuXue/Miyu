# QEMU

According to the QEMU about page:

:QEMU is a generic and open source machine emulator and virtualizer.
:When used as a machine emulator, QEMU can run OSes and programs made for one machine (e.g. an ARM board) on a different machine (e.g. your x86 PC). By using dynamic translation, it achieves very good performance.

QEMU can use other hypervisors like Xen or KVM to use CPU extensions (HVM) for virtualization. When used as a virtualizer, QEMU achieves near native performance by executing the guest code directly on the host CPU.

## Installation
Install the  package (or  for the version without GUI and  for the version with only x86_64 emulation by default) and below optional packages for your needs:

*  - Glusterfs block support
*  - iSCSI block support
*  - SMB/CIFS server support

Alternatively,  exists as a usermode and static variant.

## QEMU variants
QEMU is offered in several variants suited for different use cases.

As a first classification, QEMU is offered in full-system and usermode emulation modes:

; Full-system emulation
: In this mode, QEMU emulates a full system, including one or several processors and various peripherals. It is more accurate but slower, and does not require the emulated OS to be Linux.
: QEMU commands for full-system emulation are named , e.g.  for emulating x86_64 CPUs,  for Intel 32-bit x86 CPUs,  for ARM (32 bits),  for ARM64, etc.
: If the target architecture matches the host CPU, this mode may still benefit from a significant speedup by using a hypervisor like KVM or Xen.
; Usermode emulation
: In this mode, QEMU is able to invoke a Linux executable compiled for a (potentially) different architecture by leveraging the host system resources. There may be compatibility issues, e.g. some features may not be implemented, dynamically linked executables will not work out of the box (see #Chrooting into arm/arm64 environment from x86_64 to address this) and only Linux is supported (although Wine may be used for running Windows executables).
: QEMU commands for usermode emulation are named , e.g.  for emulating 64-bit CPUs.

QEMU is offered in dynamically-linked and statically-linked variants:

; Dynamically-linked (default):  commands depend on the host OS libraries, so executables are smaller.
; Statically-linked:  commands can be copied to any Linux system with the same architecture.

In the case of Arch Linux, full-system emulation is offered as:

; Non-headless (default): This variant enables GUI features that require additional dependencies (like SDL or GTK).
; Headless: This is a slimmer variant that does not require GUI (this is suitable e.g. for servers).

Note that headless and non-headless versions install commands with the same name (e.g. ) and thus cannot be both installed at the same time.

## Details on packages available in Arch Linux
* The  package provides the  architecture emulators for full-system emulation (). The  package provides the  usermode variant () and also for the rest of supported architectures it includes both full-system and usermode variants (e.g.  and ).
* The headless versions of these packages (only applicable to full-system emulation) are  (-only) and  (rest of architectures).
* Full-system emulation can be expanded with some QEMU modules present in separate packages: ,  and .
*  provides a usermode and static variant for all target architectures supported by QEMU. The installed QEMU commands are named , for example,  for intel 64-bit CPUs.

## Graphical front-ends for QEMU
Unlike other virtualization programs such as VirtualBox and VMware, QEMU does not provide a GUI to manage virtual machines (other than the window that appears when running a virtual machine), nor does it provide a way to create persistent virtual machines with saved settings. All parameters to run a virtual machine must be specified on the command line at every launch, unless you have created a custom script to start your virtual machine(s).

Libvirt provides a convenient way to manage QEMU virtual machines. See list of libvirt clients for available front-ends.

## Creating a new virtualized system
## Creating a hard disk image
To run QEMU you will need a hard disk image, unless you are booting a live system from CD-ROM or the network (and not doing so to install an operating system to a hard disk image). A hard disk image is a file which stores the contents of the emulated hard disk.

A hard disk image can be raw, so that it is literally byte-by-byte the same as what the guest sees, and will always use the full capacity of the guest hard drive on the host. This method provides the least I/O overhead, but can waste a lot of space, as not-used space on the guest cannot be used on the host.

Alternatively, the hard disk image can be in a format such as qcow2 which only allocates space to the image file when the guest operating system actually writes to those sectors on its virtual hard disk. The image appears as the full size to the guest operating system, even though it may take up only a very small amount of space on the host system. This image format also supports QEMU snapshotting functionality (see #Creating and managing snapshots via the monitor console for details). However, using this format instead of raw will likely affect performance.

QEMU provides the  command to create hard disk images. For example to create a 4 GiB image in the raw format:

 $ qemu-img create -f raw image_file 4G

You may use  to create a qcow2 disk instead.

## Overlay storage images
You can create a storage image once (the 'backing' image) and have QEMU keep mutations to this image in an overlay image. This allows you to revert to a previous state of this storage image. You could revert by creating a new overlay image at the time you wish to revert, based on the original backing image.

To create an overlay image, issue a command like:

 $ qemu-img create -o backing_file=img1.raw,backing_fmt=raw -f qcow2 img1.cow

After that you can run your QEMU virtual machine as usual (see #Running a virtualized system):

 $ qemu-system-x86_64 img1.cow

The backing image will then be left intact and mutations to this storage will be recorded in the overlay image file.

When the path to the backing image changes, repair is required.

Make sure that the original backing image's path still leads to this image. If necessary, make a symbolic link at the original path to the new path. Then issue a command like:

 $ qemu-img rebase -b /new/img1.raw /new/img1.cow

At your discretion, you may alternatively perform an 'unsafe' rebase where the old path to the backing image is not checked:

 $ qemu-img rebase -u -b /new/img1.raw /new/img1.cow

## Resizing an image
The  executable has the  option, which enables easy resizing of a hard drive image. It works for both raw and qcow2. For example, to increase image space by 10 GiB, run:

 $ qemu-img resize disk_image +10G

After enlarging the disk image, you must use file system and partitioning tools inside the virtual machine to actually begin using the new space.

## Shrinking an image
When shrinking a disk image, you must first reduce the allocated file systems and partition sizes using the file system and partitioning tools inside the virtual machine and then shrink the disk image accordingly. For a Windows guest, this can be performed from the "create and format hard disk partitions" control panel.

Then, to decrease image space by 10 GiB, run:

 $ qemu-img resize --shrink disk_image -10G

## Converting an image
You can convert an image to other formats using . This example shows how to convert a raw image to qcow2:

 $ qemu-img convert -f raw -O qcow2 input.img output.qcow2

This will not remove the original input file.

## Preparing the installation media
To install an operating system into your disk image, you need the installation medium (e.g. optical disc, USB-drive, or ISO image) for the operating system. The installation medium should not be mounted because QEMU accesses the media directly.

## Installing the operating system
This is the first time you will need to start the emulator. To install the operating system on the disk image, you must attach both the disk image and the installation media to the virtual machine, and have it boot from the installation media.

For example on i386 guests, to install from a bootable ISO file as CD-ROM and a raw disk image:

 $ qemu-system-x86_64 -cdrom iso_image -boot order=d -drive file=disk_image,format=raw

See  for more information about loading other media types (such as floppy, disk images or physical drives) and #Running a virtualized system for other useful options.

After the operating system has finished installing, the QEMU image can be booted directly (see #Running a virtualized system).

## Pre-made virtual machine images
In many cases, it is not necessary or desired to manually install your own operating system, for instance in a cloud environment. Luckily, many pre-made images are available for download from different providers.

For Arch Linux, the official arch-boxes project provides weekly image releases.

There are similar images available for Fedora and Debian.

## Running a virtualized system
 binaries (for example  or , depending on guest's architecture) are used to run the virtualized guest. The usage is:

 $ qemu-system-x86_64 options disk_image

Options are the same for all  binaries, see  for documentation of all options.

Usually, if an option has many possible values, you can use

 $ qemu-system-x86_64 option help

to list all possible values. If it supports properties, you can use

 $ qemu-system-x86_64 option value,help

to list all available properties.

For example:
 $ qemu-system-x86_64 -machine help
 $ qemu-system-x86_64 -machine q35,help
 $ qemu-system-x86_64 -device help
 $ qemu-system-x86_64 -device qxl,help

You can use these methods and the  documentation to understand the options used in the following sections.

By default, QEMU will show the virtual machine's video output in a window. One thing to keep in mind: when you click inside the QEMU window, the mouse pointer is grabbed. To release it, press .

## Enabling KVM
KVM (Kernel-based Virtual Machine) full virtualization must be supported by your Linux kernel and your hardware, and necessary kernel modules must be loaded. See KVM for more information.

To start QEMU in KVM mode, append  to the additional start options. To check if KVM is enabled for a running virtual machine, enter the #QEMU monitor and type .

## Enabling IOMMU (Intel VT-d/AMD-Vi) support
First enable IOMMU, see PCI passthrough via OVMF#Setting up IOMMU.

Add  to create the IOMMU device:

 $ qemu-system-x86_64 -enable-kvm -machine q35 -device intel-iommu -cpu host ..

## Booting in UEFI mode
The default firmware used by QEMU is SeaBIOS, which is a Legacy BIOS implementation. QEMU uses  (provided by the  package) as a default read-only (ROM) image. You can use the  argument to select another firmware file. However, UEFI requires writable memory to work properly, so you need to emulate PC System Flash instead.

OVMF is a TianoCore project to enable UEFI support for Virtual Machines. It can be installed with the  package.

There are two ways to use OVMF as a firmware. The first is to copy , make it writable and use as a pflash drive:

 -drive if=pflash,format=raw,file=/copy/of/OVMF.4m.fd

All changes to the UEFI settings will be saved directly to this file.

Another and more preferable way is to split OVMF into two files. The first one will be read-only and store the firmware executable, and the second one will be used as a writable variable store. The advantage is that you can use the firmware file directly without copying, so it will be updated automatically by pacman.

Use  as a first read-only pflash drive. Copy , make it writable and use as a second writable pflash drive:

 -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2/x64/OVMF_CODE.4m.fd \
 -drive if=pflash,format=raw,file=/copy/of/OVMF_VARS.4m.fd

## Enabling Secure Boot
To enable Secure Boot, you must use OVMF firmware files that have Secure Boot keys installed, which is not provided by the upstream projectUnlike some other Linux distributions, Arch Linux does not currently provide its own firmware files that are pre-enrolled with Secure Boot enabled; see  for more info. Although the firmware file  exists and appears to support Secure Boot, it does not. Using it will result in a non-bootable virtual system until you swap it with another firmware file (or your previous one) to make it bootable again.

A simple workaround is to use Fedora's [https://packages.fedoraproject.org/pkgs/edk2/edk2-ovmf/ edk2-ovmf package (which already comes with Secure Boot):

* Install .
* Use either  or  as your firmware file.
* If you need NVRAM (optional for Windows 10 and 11 machines), use  or  as your template.
* Ensure QEMU is using the  chipset machine type ().

With that, Secure Boot is now enabled on your virtual machines.

Alternatively, you can provide your own OVMF files and manually enroll those with your own keys. See KVM#Secure Boot on how to do this.

## Trusted Platform Module emulation
QEMU can emulate Trusted Platform Module, which is required by some systems such as Windows 11 (which requires TPM 2.0).

Install the  package, which provides a software TPM implementation. Create some directory for storing TPM data ( will be used as an example). Run this command to start the emulator:

 $ swtpm socket --tpm2 --tpmstate dir=/path/to/mytpm --ctrl type=unixio,path=/path/to/mytpm/swtpm-sock

 will be created by swtpm: this is a UNIX socket to which QEMU will connect. You can put it in any directory.

By default, swtpm starts a TPM version 1.2 emulator. The  option enables TPM 2.0 emulation.

Finally, add the following options to QEMU:

 -chardev socket,id=chrtpm,path=/path/to/mytpm/swtpm-sock \
 -tpmdev emulator,id=tpm0,chardev=chrtpm \
 -device tpm-tis,tpmdev=tpm0

and TPM will be available inside the virtual machine. After shutting down the virtual machine, swtpm will be automatically terminated.

See the QEMU documentation for more information.

If guest OS still does not recognize the TPM device, try to adjust CPU Models and Topology options. It might cause problem.

In case you want to install Windows 11 25H2 and setup claims it does not recognise a TPM 2.0 device even though you started swtpm with the --tpm2 command line argument you might have the wrong edk2-ovmf secure boot UEFI file combination. Make sure you use the 4M variant:

  -drive if=pflash,format=raw,readonly=on,file=/usr/share/edk2-ovmf-fedora/edk2/ovmf/OVMF_CODE_4M.secboot.fd \
  -drive if=pflash,format=raw,file=/usr/share/edk2-ovmf-fedora/edk2/ovmf/OVMF_VARS_4M.secboot.fd

Also make sure to convert the qcow2 files to fd (raw) as they are not shipped with the package:

  qemu-image convert -f qcow2 -O raw infile.qcow2 outfile.fd

## Communication between host and guest
## Network
Data can be shared between the host and guest OS using any network protocol that can transfer files, such as NFS, SMB, NBD, HTTP, FTP, or SSH, provided that you have set up the network appropriately and enabled the appropriate services.

The default SLIRP-based user-mode networking allows the guest to access the host OS at the IP address 10.0.2.2. Any servers that you are running on your host OS, such as a SSH server or SMB server, will be accessible at this IP address. So on the guests, you can mount directories exported on the host via SMB or NFS, or you can access the host's HTTP server, etc.
It will not be possible for the host OS to access servers running on the guest OS, but this can be done with other network configurations (see #Tap networking with QEMU).

## QEMU's port forwarding
QEMU can forward ports from the host to the guest to enable e.g. connecting from the host to an SSH server running on the guest.

For example, to bind port 60022 on the host with port 22 (SSH) on the guest, start QEMU with a command like:

 $ qemu-system-x86_64 disk_image -nic user,hostfwd=tcp::60022-:22

Make sure the sshd is running on the guest and connect with:

 $ ssh guest-user@127.0.0.1 -p 60022

You can use SSHFS to mount the guest's file system at the host for shared read and write access.

To forward several ports, you just repeat the  in the  argument, e.g. for VNC's port:

 $ qemu-system-x86_64 disk_image -nic user,hostfwd=tcp::60022-:22,hostfwd=tcp::5900-:5900

## Accessing SSH via vsock
A secure and convenient way to connect to the virtual machine is to use SSH over . Your virtual machine needs to be systemd-based for this to work out of the box.

First, launch QEMU with a special device:

 -device vhost-vsock-pci,id=vhost-vsock-pci0,guest-cid=555

The  needs to be picked by the user to be a valid 32-bit number (see ). When systemd detects the virtual machine has been launched with a  device, it will automatically launch an SSH server via .

You can then connect to the virtual machine like this:

 $ ssh user@vsock/555

This works because of  which tells your SSH client to use  to allow SSH to use vsock.

Furthermore, using  we can inject an authorized keys file for the  user which is very convenient in case we are trying to run a downloaded image. This can be done like so:

 -smbios type=11,value=io.systemd.credential.binary:ssh.authorized_keys.root=c3NoLWVkMjU1MTkgQUFBQUMzTnphQzFsWkRJMU5URTVBQUFBSU9sVFE4ejlpeWxoMTMreCtFVFJ1R1JEaHpIVVRnaCt2ekJLOGY3TEl5eTQ=

The public key line has to be provided as a base64-encoded string. This can be done like so:

 echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOlTQ8z9iylh13+x+ETRuGRDhzHUTgh+vzBK8f7LIyy4" | base64

The same mechanism via  can be used to inject a variety of other magical variables that will get acted on by systemd. See also systemd docs: System and Service Credentials.

## QEMU's built-in SMB server
QEMU's documentation says it has a "built-in" SMB server, but actually it just starts up Samba on the host with an automatically generated  file located in  and makes it accessible to the guest at a different IP address (10.0.2.4 by default). This only works for user networking, and is useful when you do not want to start the normal Samba service on the host, which the guest can also access if you have set up shares on it.

Samba must be installed on the host. To enable this feature, start QEMU with a command like:

 $ qemu-system-x86_64 -nic user,id=nic0,smb=shared_dir_path disk_image

where  is a directory that you want to share between the guest and host.

Then, in the guest, you will be able to access the shared directory on the host 10.0.2.4 with the share name "qemu". For example, in Windows Explorer you would go to .

## Share multiple directories
One way to share multiple directories (or add or remove them while the virtual machine is running) is to share an empty directory and create/remove symbolic links. For this to work, the configuration of the running SMB server can be changed with the following script, which also allows the execution of files on the guest that are not set executable on the host:

 #!/bin/sh
 eval $(ps h -C smbd -o pid,args | grep /tmp/qemu-smb | gawk '{print "pid="$1";conf="$6}')
 echo "allow insecure wide links = yes
 [qemu
 follow symlinks = yes
 wide links = yes
 acl allow execute always = yes" >> "$conf"
 # in case the change is not detected automatically:
 smbcontrol --configfile="$conf" "$pid" reload-config

This can be applied to the running server started by qemu only after the guest has connected to the network drive the first time. An alternative to this method is to add additional shares to the configuration file like so:

 echo "path=another_path
 read only=no
 guest ok=yes
 force user=username" >> $conf

This share will be available on the guest as .

## Host file sharing with 9pfs VirtFS
See the [https://wiki.qemu.org/Documentation/9psetup QEMU documentation.

## Host file sharing with virtiofsd
virtiofsd is shipped with the  package. It is a modern and high-performance way to conveniently share files between host and guest. See the online documentation or  for a full list of available options.

You can choose to either run virtiofsd as root or as a regular user.

## Running virtiofsd as a regular user
First, make sure that there is a  and  configuration entry for the user that will execute . See also the relevant section in the Podman article.

Then, start :

 $ unshare -r --map-auto -- /usr/lib/virtiofsd --socket-path=/tmp/vm-share.sock --shared-dir /tmp/vm-share --sandbox chroot

*  causes the command after it to be launched in a new user namespace with the current user getting mapped to root in the new command. This is important because virtiofsd expects to be running as root from its point of view.
*  is a socket file
*  is a shared directory between the host and the guest virtual machine

## Running virtiofsd as root
Add the user that runs QEMU to the  user group, because it needs to access the virtiofsd socket. You might have to logout for change to take effect.

Start  as root:

 # /usr/lib/virtiofsd --socket-path /tmp/vm-share.sock --socket-group kvm --shared-dir /tmp/vm-share

where

*  is a socket file
*  is a shared directory between the host and the guest virtual machine

## Launching QEMU
Add the following configuration options when starting the virtual machine:

 -m 4G
 -object memory-backend-memfd,id=mem,size=4G,share=on
 -numa node,memdev=mem
 -chardev socket,id=char0,path=/tmp/vm-share.sock
 -device vhost-user-fs-pci,chardev=char0,tag=myfs

where

*  must match the size specified with  option
*  points to socket file started earlier
*  is an identifier that you will use later in the guest to mount the share

## Boot rootfs directly
You may also boot a rootfs directly via virtiofsd. In addition to the above arguments, append:

 -kernel /path/to/vmlinux
 -initrd /path/to/initramfs
 -append 'rootfstype=virtiofs root=myfs rootflags=rw,noatime'

## Using the share in a Linux guest
Once logged into the guest as root, you can simply mount the share on any modern distribution:

 # mount -t virtiofs myfs /mnt

This directory should now be shared between host and guest.

## Using the share in a Windows guest
See relevant Windows section.

## Mounting a partition of the guest on the host
It can be useful to mount a drive image under the host system, it can be a way to transfer files in and out of the guest. This should be done when the virtual machine is not running.

The procedure to mount the drive on the host depends on the type of qemu image, raw or qcow2. We detail thereafter the steps to mount a drive in the two formats in #Mounting a partition from a raw image and #Mounting a partition from a qcow2 image. For the full documentation see Wikibooks:QEMU/Images#Mounting an image on the host.

## Mounting a partition from a raw image
It is possible to mount partitions that are inside a raw disk image file by setting them up as loopback devices.

## With manually specifying byte offset
One way to mount a disk image partition is to mount the disk image at a certain offset using a command like the following:

 # mount -o loop,offset=32256 disk_image mountpoint

The  option is actually passed to the  program to set up a loopback device that starts at byte offset 32256 of the file and continues to the end. This loopback device is then mounted. You may also use the  option to specify the exact size of the partition, but this is usually unnecessary.

Depending on your disk image, the needed partition may not start at offset 32256. Run  to see the partitions in the image. fdisk gives the start and end offsets in 512-byte sectors, so multiply by 512 to get the correct offset to pass to .

## With loop module autodetecting partitions
The Linux loop driver actually supports partitions in loopback devices, but it is disabled by default. To enable it, do the following:

* Get rid of all your loopback devices (unmount all mounted images, etc.).
* Unload the  kernel module, and load it with the  parameter set. Additionally, the maximum number of loop devices can be controlled with the  parameter.

Set up your image as a loopback device:

 # losetup -f -P disk_image

Then, if the device created was , additional devices  will have been automatically created, where X is the number of the partition. These partition loopback devices can be mounted directly. For example:

 # mount /dev/loop0p1 mountpoint

To mount the disk image with udisksctl, see Udisks#Mount loop devices.

## With kpartx
kpartx from the  package can read a partition table on a device and create a new device for each partition. For example:

 # kpartx -a disk_image

This will setup the loopback device and create the necessary partition(s) device(s) in .

## Mounting a partition from a qcow2 image
We will use , which lets us use the NBD (network block device) protocol to share the disk image.

First, we need the nbd module loaded:

 # modprobe nbd max_part=16

Then, we can share the disk and create the device entries:

 # qemu-nbd -c /dev/nbd0 /path/to/image.qcow2

Discover the partitions:

 # partprobe /dev/nbd0

fdisk can be used to get information regarding the different partitions in :

Then mount any partition of the drive image, for example the partition 2:

 # mount /dev/nbd0p2 mountpoint

After the usage, it is important to unmount the image and reverse previous steps, i.e. unmount the partition and disconnect the nbd device:

 # umount mountpoint
 # qemu-nbd -d /dev/nbd0

## Networking
The performance of virtual networking should be better with tap devices and bridges than with user-mode networking or vde because tap devices and bridges are implemented in-kernel.

In addition, networking performance can be improved by assigning virtual machines a virtio network device rather than the default emulation of an e1000 NIC. See #Using virtio drivers for more information.

## Link-level address caveat
By giving the  argument to QEMU, it will, by default, assign a virtual machine a network interface with the link-level address . However, when using bridged networking with multiple virtual machines, it is essential that each virtual machine has a unique link-level (MAC) address on the virtual machine side of the tap device. Otherwise, the bridge will not work correctly, because it will receive packets from multiple sources that have the same link-level address. This problem occurs even if the tap devices themselves have unique link-level addresses because the source link-level address is not rewritten as packets pass through the tap device.

Make sure that each virtual machine has a unique link-level address, but it should always start with . Use the following option, replace X with arbitrary hexadecimal digit:

 $ qemu-system-x86_64 -net nic,macaddr=52:54:XX:XX:XX:XX -net vde disk_image

Generating unique link-level addresses can be done in several ways:

* Manually specify unique link-level address for each NIC. The benefit is that the DHCP server will assign the same IP address each time the virtual machine is run, but it is unusable for large number of virtual machines.
* Generate random link-level address each time the virtual machine is run. Practically zero probability of collisions, but the downside is that the DHCP server will assign a different IP address each time. You can use the following command in a script to generate random link-level address in a  variable:

* Use the following script  to generate the link-level address from the virtual machine name using a hashing function. Given that the names of virtual machines are unique, this method combines the benefits of the aforementioned methods: it generates the same link-level address each time the script is run, yet it preserves the practically zero probability of collisions.

In a script, you can use for example:

 vm_name="VM Name"
 qemu-system-x86_64 -name "$vm_name" -net nic,macaddr=$(qemu-mac-hasher.py "$vm_name") -net vde disk_image

## User-mode networking
## SLIRP
By default, without any  arguments, QEMU will use SLIRP-based user-mode networking with a built-in DHCP server. Your virtual machines will be assigned an IP address when they run their DHCP client, and they will be able to access the physical host's network through IP masquerading done by QEMU.

This default configuration allows your virtual machines to easily access the Internet, provided that the host is connected to it, but the virtual machines will not be directly visible on the external network, nor will virtual machines be able to talk to each other if you start up more than one concurrently.

QEMU's user-mode networking can offer more capabilities such as built-in TFTP or SMB servers, redirecting host ports to the guest (for example to allow SSH connections to the guest) or attaching guests to VLANs so that they can talk to each other. See the QEMU documentation on the  flag for more details.

However, SLIRP-based user-mode networking has limitations in both utility and performance. More advanced network configurations require the use of tap devices or other methods.

## passt
Users can choose to use passt-based user-mode networking. passt has several advantages over SLIRP such as better performance, full IPv6 support (including ICMPv6), better security, and more control.

To get started, install . There are two ways to launch it: Either via socket-based communication or via shared vhost-user. The latter method has better performance.

For the socket-based way, first launch :

 $ passt -f

Then, for your QEMU command, add these parameters:

 -device virtio-net-pci,netdev=s
 -netdev stream,id=s,server=off,addr.type=unix,addr.path=/tmp/passt_1.socket

For the vhost-user way, launch  with

 $ passt -f --vhost-user

Then, for your QEMU command, add these parameters:

 -m 4G
 -chardev socket,id=chr0,path=/tmp/passt_1.socket
 -netdev vhost-user,id=netdev0,chardev=chr0
 -device virtio-net,netdev=netdev0
 -object memory-backend-memfd,id=memfd0,share=on,size=4G
 -numa node,memdev=memfd0

Notice the memory sizes of  and  have to match exactly.

## Tap networking with QEMU
Tap devices are a Linux kernel feature that allows you to create virtual network interfaces that appear as real network interfaces. Packets sent to a tap interface are delivered to a userspace program, such as QEMU, that has bound itself to the interface.

QEMU can use tap networking for a virtual machine so that packets sent to the tap interface will be sent to the virtual machine and appear as coming from a network interface (usually an Ethernet interface) in the virtual machine. Conversely, everything that the virtual machine sends through its network interface will appear on the tap interface.

Tap devices are supported by the Linux bridge drivers, so it is possible to bridge together tap devices with each other and possibly with other host interfaces such as . This is desirable if you want your virtual machines to be able to talk to each other, or if you want other machines on your LAN to be able to talk to the virtual machines.

As indicated in the user-mode networking section, tap devices offer higher networking performance than user-mode. If the guest OS supports virtio network driver, then the networking performance will be increased considerably as well. Supposing the use of the tap0 device, that the virtio driver is used on the guest, and that no scripts are used to help start/stop networking, next is part of the qemu command one should see:

 -device virtio-net,netdev=network0 -netdev tap,id=network0,ifname=tap0,script=no,downscript=no

But if already using a tap device with virtio networking driver, one can even boost the networking performance by enabling vhost, like:

 -device virtio-net,netdev=network0 -netdev tap,id=network0,ifname=tap0,script=no,downscript=no,vhost=on

See for more information.

## Host-only networking
If the bridge is given an IP address and traffic destined for it is allowed, but no real interface (e.g. ) is connected to the bridge, then the virtual machines will be able to talk to each other and the host system. However, they will not be able to talk to anything on the external network, provided that you do not set up IP masquerading on the physical host. This configuration is called host-only networking by other virtualization software such as VirtualBox.

## Internal networking
If you do not give the bridge an IP address, then the virtual machines will be able to talk to each other, but not to the physical host or to the outside network. This configuration is called internal networking by other virtualization software such as VirtualBox. You will need to either assign static IP addresses to the virtual machines or run a DHCP server on one of them.

## Bridged networking using qemu-bridge-helper
This method does not require a start-up script and readily accommodates multiple taps and multiple bridges. It uses  binary, which allows creating tap devices on an existing bridge.

First, create a configuration file containing the names of all bridges to be used by QEMU:

Make sure  has  permissions. [https://gitlab.com/qemu-project/qemu/-/issues/515 QEMU issues and GNS3 issues may arise if this is not the case.

Now start the virtual machine; the most basic usage to run QEMU with the default network helper and default bridge :

 $ qemu-system-x86_64 -nic bridge ''Using the bridge  and the virtio driver:

 $ qemu-system-x86_64 -nic bridge,br=br1,model=virtio-net-pci [...

## Advanced network configuration
If you need more control over your virtual machine's networking or you have very specific needs that are not covered in the previous sections, see QEMU/Advanced networking.

## Shorthand configuration
If you are using QEMU with various networking options a lot, you probably have created a lot of  and  argument pairs, which gets quite repetitive. You can instead use the  argument to combine  and  together, so that, for example, these arguments:

 -netdev tap,id=network0,ifname=tap0,script=no,downscript=no,vhost=on -device virtio-net-pci,netdev=network0

become:

 -nic tap,script=no,downscript=no,vhost=on,model=virtio-net-pci

Notice the lack of network IDs, and that the device was created with . The first half of the  parameters are  parameters, whereas the second half (after ) are related with the device. The same parameters (for example, ) are used. To completely disable the networking use .

See QEMU networking documentation for more information on parameters you can use.

## Graphics card
QEMU can emulate a standard graphics card text mode using  command line option. This allows to type text and see text output directly inside a text terminal. Alternatively,  serves a similar purpose.

QEMU can emulate several types of VGA card. The card type is passed in the  command line option and can be , , , ,  or .

## std
With  you can get a resolution of up to 2560 x 1600 pixels without requiring guest drivers. This is the default since QEMU 2.2.

## qxl
QXL is a paravirtual graphics driver with 2D support. To use it, pass the  option and install drivers in the guest. You may want to use #SPICE for improved graphical performance when using QXL.

On Linux guests, the  and  kernel modules must be loaded in order to gain a decent performance.

Default VGA memory size for QXL devices is 16M which is sufficient to drive resolutions approximately up to QHD (2560x1440). To enable higher resolutions, increase vga_memmb.

## vmware
Although it is a bit buggy, it performs better than std and cirrus. Install the VMware drivers  and  for Arch Linux guests.

## virtio
 /  is a paravirtual 3D graphics driver based on virgl. It's mature, currently supporting only Linux guests with  compiled with the option .

To enable 3D acceleration on the guest system, select this vga with  and enable the OpenGL context in the display device with  or  for the SDL and GTK display output respectively. Successful configuration can be confirmed looking at the kernel log in the guest:

To enable Vulkan support in the guest, use options like  and install the  in the guest system === cirrus ===

The cirrus graphical adapter was the default [https://wiki.qemu.org/ChangeLog/2.2#VGA before 2.2. It should not be used on modern systems.

## none
This is like a PC that has no VGA card at all. You would not even be able to access it with the  option. Also, this is different from the  option which lets QEMU emulate a VGA card, but disables the SDL display.

## SPICE
The SPICE project aims to provide a complete open source solution for remote access to virtual machines in a seamless way.

## Enabling SPICE support on the host
The following is an example of booting with SPICE as the remote desktop protocol, including the support for copy and paste from host:

 $ qemu-system-x86_64 -vga qxl -device virtio-serial-pci -spice port=5930,disable-ticketing=on -device virtserialport,chardev=spicechannel0,name=com.redhat.spice.0 -chardev spicevmc,id=spicechannel0,name=vdagent

The parameters have the following meaning:

#  adds a virtio-serial device
#  set TCP port  for spice channels listening and allow client to connect without authentication
#  opens a port for spice vdagent in the virtio-serial device,
#  adds a spicevmc chardev for that port. It is important that the  option of the  device matches the  option given to the  option ( in this example). It is also important that the port name is , because that is the namespace where vdagent is looking for in the guest. And finally, specify  so that spice knows what this channel is for.

## Connecting to the guest with a SPICE client
A SPICE client is necessary to connect to the guest. In Arch, the following clients are available:

*
*

For clients that run on smartphone or on other platforms, refer to the Other clients section in spice-space download.

## Manually running a SPICE client
One way of connecting to a guest listening on Unix socket  is to manually run the SPICE client using  or , depending on the desired client. Since QEMU in SPICE mode acts similarly to a remote desktop server, it may be more convenient to run QEMU in daemon mode with the  parameter.

## Running a SPICE client with QEMU
QEMU can automatically start a SPICE client with an appropriate socket, if the display is set to SPICE with the  parameter. This will use the system's default SPICE client as the viewer, determined by your mimeapps.list files.

## Enabling SPICE support on the guest
For Arch Linux guests, for improved support for multiple monitors or clipboard sharing, the following packages should be installed:
* : Xorg SPICE agent client that enables copy and paste between client and X-session and more. (Refer to this issue, until fixed, for workarounds to get this to work on non-GNOME desktops.)
* : Xorg QXL video driver
* : Wayland clipboard support
* : Desktop environments other than GNOME do not react automatically when the SPICE client window is resized. This package uses a udev rule and xrandr to implement auto-resizing for all X11-based desktop environments and window managers.

For guests under other operating systems, refer to the Guest section in spice-space download.

## Password authentication with SPICE
If you want to enable password authentication with SPICE you need to remove  from the  argument and instead add . For example:

 $ qemu-system-x86_64 -vga qxl -spice port=5900,password=yourpassword -device virtio-serial-pci -device virtserialport,chardev=spicechannel0,name=com.redhat.spice.0 -chardev spicevmc,id=spicechannel0,name=vdagent

Your SPICE client should now ask for the password to be able to connect to the SPICE server.

## TLS encrypted communication with SPICE
You can also configure TLS encryption for communicating with the SPICE server. First, you need to have a directory which contains the following files (the names must be exactly as indicated):

* : the CA master certificate.
* : the server certificate signed with .
* : the server private key.

An example of generation of self-signed certificates with your own generated CA for your server is shown in the Spice User Manual.

Afterwards, you can run QEMU with SPICE as explained above but using the following  argument: , where  is the directory path that contains the three needed files shown earlier.

It is now possible to connect to the server using :

 $ remote-viewer spice://hostname?tls-port=5901 --spice-ca-file=/path/to/ca-cert.pem --spice-host-subject="C=XX,L=city,O=organization,CN=hostname" --spice-secure-channels=all

Keep in mind that the  parameter needs to be set according to your  subject. You also need to copy  to every client to verify the server certificate.

The equivalent  command is:

 $ spicy -h hostname -s 5901 --spice-ca-file=ca-cert.pem --spice-host-subject="C=XX,L=city,O=organization,CN=hostname" --spice-secure-channels=all

## VNC
One can add the  option to have QEMU redirect the VGA display to the VNC session. Substitute  for the number of the display (0 will then listen on 5900, 1 on 5901...).

 $ qemu-system-x86_64 -vnc :0

An example is also provided in the #Starting QEMU virtual machines on boot section.

## Basic password authentication
An access password can be setup easily by using the  option. The password must be indicated in the QEMU monitor and connection is only possible once the password is provided.

 $ qemu-system-x86_64 -vnc :0,password -monitor stdio

In the QEMU monitor, password is set using the command  and then indicating the password.

The following command line directly runs vnc with a password:

 $ printf "change vnc password\n%s\n" MYPASSWORD | qemu-system-x86_64 -vnc :0,password -monitor stdio

## Audio
## Creating an audio backend
The  flag sets the audio backend driver on the host and its options.

To list availabe audio backend drivers:

 $ qemu-system-x86_64 -audiodev help

Their optional settings are detailed in the  man page.

At the bare minimum, one need to choose an audio backend and set an id, for PulseAudio for example:

 -audiodev pa,id=snd0

## Using the audio backend
## Intel HD Audio
For Intel HD Audio emulation, add both controller and codec devices. To list the available Intel HDA Audio devices:

 $ qemu-system-x86_64 -device help | grep hda

Add the audio controller:

 -device ich9-intel-hda

Also, add the audio codec and map it to a host audio backend id:

 -device hda-output,audiodev=snd0

## Intel 82801AA AC97
For AC97 emulation just add the audio card device and map it to a host audio backend id:

 -device AC97,audiodev=snd0

## VirtIO sound
VirtIO sound is also available since QEMU 8.2.0. The usage is:

 -device virtio-sound-pci,audiodev=my_audiodev -audiodev alsa,id=my_audiodev

More information can be found in QEMU documentation.

## Using virtio drivers
QEMU offers guests the ability to use paravirtualized block and network devices using the virtio drivers, which provide better performance and lower overhead.

* A virtio block device requires the option  for passing a disk image, with parameter :
 $ qemu-system-x86_64 -drive file=disk_image,if=virtio

* Almost the same goes for the network:
 $ qemu-system-x86_64 -nic user,model=virtio-net-pci

## Preparing an Arch Linux guest
To use virtio devices after an Arch Linux guest has been installed, the following modules must be loaded in the guest: , , , , and . For 32-bit guests, the specific "virtio" module is not necessary.

If you want to boot from a virtio disk, the initial ramdisk must contain the necessary modules. By default, this is handled by mkinitcpio's  hook. Otherwise use the  array in  to include the necessary modules and rebuild the initial ramdisk.

Virtio disks are recognized with the prefix  (e.g. , , etc.); therefore, changes must be made in at least  and  when booting from a virtio disk.

Further information on paravirtualization with KVM can be found here.

You might also want to install  to implement support for QMP commands that will enhance the hypervisor management capabilities.

## Memory ballooning
In order to allow the guest's memory foot print to shrink as seen from the host, it needs to report to the host which pages are not needed anymore by the guest. The kernel has an API for that called Free Page Reporting and since it is built-in, it is as easy as starting QEMU like this:

 $ qemu-system-x86_64 ... -device virtio-balloon,free-page-reporting=on

After this, you should see the guest memory increasing and then shrinking again after running workloads in it.

However, while this parameter will indeed take care of shrinking the guest's memory usage from the host's perspective when pages are freed, it will not be able to automatically make use of memory that the guest is using for cache. This is an important consideration as a guest is likely to eventually use its entire unused memory for caching, making  useless. Read the next section to mitigate this problem.

## Using virtio pmem to bypass the guest's page cache
You might want to rely on the host's page cache instead of the guest's in order to allow for more efficient memory usage. Coupled with KSM, this allows you to make your virtual machines quite memory efficient, duplicating only few pages.

One way to achieve this is to use a file-mapped virtio pmem device. Add this config to your QEMU:

 -object memory-backend-file,id=mem1,share,mem-path=./virtio_pmem.img,size=32G
 -device virtio-pmem-pci,memdev=mem1,id=nv1
 -m 64G,maxmem=96G

whereby  is a local file on the host that will serve as our memory backend in side the guest. The  part is important here: Set the  parameter so that it is . In this case: .

Start the guest with those options. Inside the guest, you will find a new device at  which we will need to format with a DAX-compatible filesystem such as ext4 (btrfs is not supported):

 # mkfs.ext4 /dev/pmem0
 mount /dev/pmem0 /mnt -o dax=always

Any files you write into  will then bypass the guest's page cache.

It's also possible to have the whole root filesystem DAX-enabled in this way.

## Preparing a Windows guest
## Virtio drivers for Windows
Windows does not come with the virtio drivers. The latest and stable versions of the drivers are regularly built by Fedora, details on downloading the drivers are given on virtio-win on GitHub. In the following sections we will mostly use the stable ISO file provided here: virtio-win.iso. Alternatively, use .

## Block device drivers
## New Install of Windows
The drivers need to be loaded during installation, the procedure is to load the ISO image with the virtio drivers in a cdrom device along with the primary disk device and the Windows ISO install media:

 $ qemu-system-x86_64 ... \
 -drive file=disk_image,index=0,media=disk,if=virtio \
 -drive file=windows.iso,index=2,media=cdrom \
 -drive file=virtio-win.iso,index=3,media=cdrom \
 ...

During the installation, at some stage, the Windows installer will ask "Where do you want to install Windows?", it will give a warning that no disks are found. Follow the example instructions below (based on Windows Server 2012 R2 with Update).

* Select the option Load Drivers.
* Uncheck the box for Hide drivers that are not compatible with this computer's hardware.
* Click the browse button and open the CDROM for the virtio iso, usually named "virtio-win-XX".
* Now browse to , select it, and confirm.

You should now see your virtio disk(s) listed here, ready to be selected, formatted and installed to.

## Change existing Windows virtual machine to use virtio
Modifying an existing Windows guest for booting from virtio disk requires that the virtio driver is loaded by the guest at boot time.
We will therefore need to teach Windows to load the virtio driver at boot time before being able to boot a disk image in virtio mode.

To achieve that, first create a new disk image that will be attached in virtio mode and trigger the search for the driver:

 $ qemu-img create -f qcow2 dummy.qcow2 1G

Run the original Windows guest with the boot disk still in IDE mode, the fake disk in virtio mode and the driver ISO image.

 $ qemu-system-x86_64 -m 4G -drive file=disk_image,if=ide -drive file=dummy.qcow2,if=virtio -cdrom virtio-win.iso

Windows will detect the fake disk and look for a suitable driver. If it fails, go to Device Manager, locate the SCSI drive with an exclamation mark icon (should be open), click Update driver and select the virtual CD-ROM. Do not navigate to the driver folder within the CD-ROM, simply select the CD-ROM drive and Windows will find the appropriate driver automatically (tested for Windows 7 SP1).

Request Windows to boot in safe mode next time it starts up. This can be done using the msconfig.exe tool in Windows. In safe mode all the drivers will be loaded at boot time including the new virtio driver. Once Windows knows that the virtio driver is required at boot it will memorize it for future boot.

Once instructed to boot in safe mode, you can turn off the virtual machine and launch it again, now with the boot disk attached in virtio mode:

 $ qemu-system-x86_64 -m 4G -drive file=disk_image,if=virtio

You should boot in safe mode with virtio driver loaded, you can now return to msconfig.exe disable safe mode boot and restart Windows.

## Network drivers
Using virtio network drivers is a bit easier, simply add the  argument.

 $ qemu-system-x86_64 -m 4G -drive file=windows_disk_image,if=virtio -nic user,model=virtio-net-pci -cdrom virtio-win.iso

Windows will detect the network adapter and try to find a driver for it. If it fails, go to the Device Manager, locate the network adapter with an exclamation mark icon (should be open), click Update driver and select the virtual CD-ROM. Do not forget to select the checkbox which says to search for directories recursively.

## Balloon driver
If you want to track your guest memory state (for example via  command ) or change guest's memory size in runtime (you still will not be able to change memory size, but can limit memory usage via inflating balloon driver) you will need to install guest balloon driver.

For this you will need to go to Device Manager, locate PCI standard RAM Controller in System devices (or unrecognized PCI controller from Other devices) and choose Update driver. In opened window you will need to choose Browse my computer... and select the CD-ROM (and do not forget the Include subdirectories checkbox). Reboot after installation. This will install the driver and you will be able to inflate the balloon (for example via hmp command , which will cause balloon to take as much memory as possible in order to shrink the guest's available memory size to memory_size). However, you still will not be able to track guest memory state. In order to do this you will need to install Balloon service properly. For that open command line as administrator, go to the CD-ROM, Balloon directory and deeper, depending on your system and architecture. Once you are in amd64 (x86) directory, run  which will do the installation. After that  command  should be outputting all supported values.

## Using a virtiofsd share
Before you progress in this section, make sure you followed the section about setting up host file sharing with virtiofsd first.

First, follow the upstream instructions. Once configured, Windows will have the  drive mapped automatically with shared directory content.

Your Windows 11 guest system is properly configured if it has:

* VirtioFSSService windows service,
* WinFsp.Launcher windows service,
* VirtIO FS Device driver under "System devices" in Windows "Device Manager".

If the above installed and  drive is still not listed, try repairing "Virtio-win-guest-tools" in Windows Add/Remove programs.

## Preparing a FreeBSD guest
Install the  port if you are using FreeBSD 8.3 or later up until 10.0-CURRENT where they are included into the kernel. After installation, add the following to your  file:

Then modify your  by doing the following:

 # sed -ibak "s/ada/vtbd/g" /etc/fstab

And verify that  is consistent. If anything goes wrong, just boot into a rescue CD and copy  back to .

## QEMU monitor
While QEMU is running, a monitor console is provided in order to provide several ways to interact with the virtual machine running. The QEMU monitor offers interesting capabilities such as obtaining information about the current virtual machine, hotplugging devices, creating snapshots of the current state of the virtual machine, etc. To see the list of all commands, run  or  in the QEMU monitor console or review the relevant section of the official QEMU documentation.

## Accessing the monitor console
## Graphical view
When using the  default graphics option, one can access the QEMU monitor by pressing  or by clicking View > compatmonitor0 in the QEMU window. To return to the virtual machine graphical view either press  or click View > VGA.

However, the standard method of accessing the monitor is not always convenient and does not work in all graphic outputs QEMU supports.

## Telnet
To enable telnet, run QEMU with the  parameter. When the virtual machine is started you will be able to access the monitor via telnet:

 $ telnet 127.0.0.1 port

## UNIX socket
Run QEMU with the  parameter. Then you can connect with either ,  or .

For example, if QEMU is run via:

 $ qemu-system-x86_64 -monitor unix:/tmp/monitor.sock,server,nowait ''It is possible to connect to the monitor with:

 $ socat - UNIX-CONNECT:/tmp/monitor.sock

Or with:

 $ nc -U /tmp/monitor.sock

Alternatively with :

 $ ncat -U /tmp/monitor.sock

## TCP
You can expose the monitor over TCP with the argument . Then connect with  by running:

 $ nc 127.0.0.1 port

## Standard I/O
It is possible to access the monitor automatically from the same terminal QEMU is being run by running it with the argument .

## Sending keyboard presses to the virtual machine using the monitor console
Some combinations of keys may be difficult to perform on virtual machines due to the host intercepting them instead in some configurations (a notable example is the  key combinations, which change the active tty). To avoid this problem, the problematic combination of keys may be sent via the monitor console instead. Switch to the monitor and use the  command to forward the necessary keypresses to the virtual machine. For example:

 (qemu) sendkey ctrl-alt-f2

## Creating and managing snapshots via the monitor console
It is sometimes desirable to save the current state of a virtual machine and having the possibility of reverting the state of the virtual machine to that of a previously saved snapshot at any time. The QEMU monitor console provides the user with the necessary utilities to create snapshots, manage them, and revert the machine state to a saved snapshot.

* Use  in order to create a snapshot with the tag name.
* Use  to revert the virtual machine to the state of the snapshot name.
* Use  to delete the snapshot tagged as name.
* Use  to see a list of saved snapshots. Snapshots are identified by both an auto-incremented ID number and a text tag (set by the user on snapshot creation).

## Running the virtual machine in immutable mode
It is possible to run a virtual machine in a frozen state so that all changes will be discarded when the virtual machine is powered off just by running QEMU with the  parameter. When the disk image is written by the guest, changes will be saved in a temporary file in  and will be discarded when QEMU halts.

However, if a machine is running in frozen mode it is still possible to save the changes to the disk image if it is afterwards desired by using the monitor console and running the following command:

 (qemu) commit all

If snapshots are created when running in frozen mode they will be discarded as soon as QEMU is exited unless changes are explicitly commited to disk, as well.

## Pause and power options via the monitor console
Some operations of a physical machine can be emulated by QEMU using some monitor commands:

*  will send an ACPI shutdown request to the virtual machine. This effect is similar to the power button in a physical machine.
*  will reset the virtual machine similarly to a reset button in a physical machine. This operation can cause data loss and file system corruption since the virtual machine is not cleanly restarted.
*  will pause the virtual machine.
*  will resume a virtual machine previously paused.

## Taking screenshots of the virtual machine
Screenshots of the virtual machine graphic display can be obtained in the PPM format by running the following command in the monitor console:

 (qemu) screendump file.ppm

## QEMU machine protocol
The QEMU machine protocol (QMP) is a JSON-based protocol which allows applications to control a QEMU instance. Similarly to the #QEMU monitor it offers ways to interact with a running machine and the JSON protocol allows to do it programmatically. The description of all the QMP commands can be found in [https://raw.githubusercontent.com/coreos/qemu/master/qmp-commands.hx qmp-commands.

## Start QMP
The usual way to control the guest using the QMP protocol, is to open a TCP socket when launching the machine using the  option. Here it is using for example the TCP port 4444:

 $ qemu-system-x86_64 ''-qmp tcp:localhost:4444,server,nowait

Then one way to communicate with the QMP agent is to use netcat:

{{hc|nc localhost 4444|{"QMP": {"version": {"qemu": {"micro": 0, "minor": 1, "major": 3}, "package": ""}, "capabilities": [} } }}

At this stage, the only command that can be recognized is , so that QMP enters into command mode. Type:

 {"execute": "qmp_capabilities"}

Now, QMP is ready to receive commands, to retrieve the list of recognized commands, use:

 {"execute": "query-commands"}

## Live merging of child image into parent image
It is possible to merge a running snapshot into its parent by issuing a  command. In its simplest form the following line will commit the child into its parent:

 {"execute": "block-commit", "arguments": {"device": "devicename"}}

Upon reception of this command, the handler looks for the base image and converts it from read only to read write mode and then runs the commit job.

Once the block-commit operation has completed, the event  will be emitted, signalling that the synchronization has finished. The job can then be gracefully completed by issuing the command :

 {"execute": "block-job-complete", "arguments": {"device": "devicename"}}

Until such a command is issued, the commit operation remains active.
After successful completion, the base image remains in read write mode and becomes the new active layer. On the other hand, the child image becomes invalid and it is the responsibility of the user to clean it up.

{{Tip|The list of device and their names can be retrieved by executing the command  and parsing the results. The device name is in the  field, for example  for the hard disk in this example: {{hc|{"execute": "query-block"}|{"return": "ok", "device": "ide0-hd0", "locked": false, "removable": false, "inserted": {"iops_rd": 0, "detect_zeroes": "off", "image": {"backing-image": {"virtual-size": 27074281472, "filename": "parent.qcow2", ... } }} }}

## Live creation of a new snapshot
To create a new snapshot out of a running image, run the command:

 {"execute": "blockdev-snapshot-sync", "arguments": {"device": "devicename","snapshot-file": "new_snapshot_name.qcow2"}}

This creates an overlay file named  which then becomes the new active layer.

## Tips and tricks
## Improve virtual machine performance
There are a number of techniques that you can use to improve the performance of the virtual machine. For example:

* Apply #Enabling KVM for full virtualization.
* Use the  option to make QEMU emulate the host's exact CPU rather than a more generic CPU.
* Especially for Windows guests, enable [https://blog.wikichoon.com/2014/07/enabling-hyper-v-enlightenments-with-kvm.html Hyper-V enlightenments: . See the QEMU documentation for more information and flags.
* multiple cores can be assigned to the guest using the  option. The threads parameter is used to assign SMT cores. Leaving a physical core for QEMU, the hypervisor and the host system to operate unimpeded is highly beneficial.
* Make sure you have assigned the virtual machine enough memory. By default, QEMU only assigns 128 MiB of memory to each virtual machine. Use the  option to assign more memory. For example,  runs a virtual machine with 1024 MiB of memory.
* If supported by drivers in the guest operating system, use virtio for network and/or block devices, see #Using virtio drivers.
* Use TAP devices instead of user-mode networking, see #Tap networking with QEMU.
* If the guest OS is doing heavy writing to its disk, you may benefit from certain mount options on the host's file system. For example, you can mount an ext4 file system with the option . You should read the documentation for any options that you change because sometimes performance-enhancing options for file systems come at the cost of data integrity.
* If you have a raw disk or partition, you may want to disable the cache:
* Use the native Linux AIO:
* If you are running multiple virtual machines concurrently that all have the same operating system installed, you can save memory by enabling kernel same-page merging. See #Enabling KSM.
* In some cases, memory can be reclaimed from running virtual machines by running a memory ballooning driver in the guest operating system. See #Memory ballooning.
* It is possible to use a emulation layer for an ICH-9 AHCI controller (although it may be unstable). The AHCI emulation supports NCQ, so multiple read or write requests can be outstanding at the same time:

See https://www.linux-kvm.org/page/Tuning_KVM for more information.

## Using any real partition as the single primary partition of a hard disk image
Sometimes, you may wish to use one of your system partitions from within QEMU. Using a raw partition for a virtual machine will improve performance, as the read and write operations do not go through the file system layer on the physical host. Such a partition also provides a way to share data between the host and guest.

In Arch Linux, device files for raw partitions are, by default, owned by root and the disk group. If you would like to have a non-root user be able to read and write to a raw partition, you must either change the owner of the partition's device file to that user, add that user to the disk group, or use ACL for more fine-grained access control.

After doing so, you can attach the partition to a QEMU virtual machine as a virtual disk.

However, things are a little more complicated if you want to have the entire virtual machine contained in a partition. In that case, there would be no disk image file to actually boot the virtual machine since you cannot install a boot loader to a partition that is itself formatted as a file system and not as a partitioned device with an MBR. Such a virtual machine can be booted either by: #Specifying kernel and initramfs manually, #Simulating a virtual disk with MBR, #Using the device-mapper, #Using a linear RAID or #Using a Network Block Device.

## Specifying kernel and initramfs manually
QEMU supports loading Linux kernels and initial RAM file systems directly, thereby circumventing boot loaders such as GRUB. It then can be launched with the physical partition containing the root file system as the virtual disk, which will not appear to be partitioned. This is done by issuing a command similar to the following:

 $ qemu-system-x86_64 -kernel /boot/vmlinuz-linux -initrd /boot/initramfs-linux.img -append root=/dev/sda /dev/sda3

In the above example, the physical partition being used for the guest's root file system is  on the host, but it shows up as  on the guest.

You may, of course, specify any kernel and initramfs that you want, and not just the ones that come with Arch Linux.

When there are multiple kernel parameters to be passed to the  option, they need to be quoted using single or double quotes. For example:

 ... -append 'root=/dev/sda1 console=ttyS0'

## Simulating a virtual disk with MBR
A more complicated way to have a virtual machine use a physical partition, while keeping that partition formatted as a file system and not just having the guest partition the partition as if it were a disk, is to simulate an MBR for it so that it can boot using a boot loader such as GRUB.

For the following, suppose you have a plain, unmounted  partition with some file system on it you wish to make part of a QEMU disk image. The trick is to dynamically prepend a master boot record (MBR) to the real partition you wish to embed in a QEMU raw disk image. More generally, the partition can be any part of a larger simulated disk, in particular a block device that simulates the original physical disk but only exposes  to the virtual machine.

A virtual disk of this type can be represented by a VMDK file that contains references to (a copy of) the MBR and the partition, but QEMU does not support this VMDK format. For instance, a virtual disk created by

 $ VBoxManage internalcommands createrawvmdk -filename /path/to/file.vmdk -rawdisk /dev/hda

will be rejected by QEMU with the error message

 Unsupported image type 'partitionedDevice'

Note that  creates two files,  and , the latter being a copy of the MBR, to which the text file  points. Read operations outside the target partition or the MBR would give zeros, while written data would be discarded.

## Using the device-mapper
A method that is similar to the use of a VMDK descriptor file uses the device-mapper to prepend a loop device attached to the MBR file to the target partition. In case we do not need our virtual disk to have the same size as the original, we first create a file to hold the MBR:

 $ dd if=/dev/zero of=/path/to/mbr count=2048

Here, a 1 MiB (2048 * 512 bytes) file is created in accordance with partition alignment policies used by modern disk partitioning tools. For compatibility with older partitioning software, 63 sectors instead of 2048 might be required. The MBR only needs a single 512 bytes block, the additional free space can be used for a BIOS boot partition and, in the case of a hybrid partitioning scheme, for a GUID Partition Table. Then, we attach a loop device to the MBR file:

In this example, the resulting device is . The device mapper is now used to join the MBR and the partition:

 # echo "0 2048 linear /dev/loop0 0
 2048 `blockdev --getsz /dev/hdaN` linear /dev/hdaN 0" | dmsetup create qemu

The resulting  is what we will use as a QEMU raw disk image. Additional steps are required to create a partition table (see the section that describes the use of a linear RAID for an example) and boot loader code on the virtual disk (which will be stored in ).

The following setup is an example where the position of  on the virtual disk is to be the same as on the physical disk and the rest of the disk is hidden, except for the MBR, which is provided as a copy:

 # dd if=/dev/hda count=1 of=/path/to/mbr
 # loop=`losetup --show -f /path/to/mbr`
 # start=`blockdev --report /dev/hdaN | tail -1 | awk '{print $5}'`
 # size=`blockdev --getsz /dev/hdaN`
 # disksize=`blockdev --getsz /dev/hda`
 # echo "0 1 linear $loop 0
 1 $((start-1)) zero
 $start $size linear /dev/hdaN 0
 $((start+size)) $((disksize-start-size)) zero" | dmsetup create qemu

The table provided as standard input to  has a similar format as the table in a VMDK descriptor file produced by  and can alternatively be loaded from a file with . To the virtual machine, only  is accessible, while the rest of the hard disk reads as zeros and discards written data, except for the first sector. We can print the table for  with  (use  to translate  to the corresponding  name). Use  and  to delete the created devices.

A situation where this example would be useful is an existing Windows XP installation in a multi-boot configuration and maybe a hybrid partitioning scheme (on the physical hardware, Windows XP could be the only operating system that uses the MBR partition table, while more modern operating systems installed on the same computer could use the GUID Partition Table). Windows XP supports hardware profiles, so that that the same installation can be used with different hardware configurations alternatingly (in this case bare metal vs. virtual) with Windows needing to install drivers for newly detected hardware only once for every profile. Note that in this example the boot loader code in the copied MBR needs to be updated to directly load Windows XP from  instead of trying to start the multi-boot capable boot loader (like GRUB) present in the original system. Alternatively, a copy of the boot partition containing the boot loader installation can be included in the virtual disk the same way as the MBR.

## Using a linear RAID
You can also do this using software RAID in linear mode (you need the  kernel driver) and a loopback device:

First, you create some small file to hold the MBR:

 $ dd if=/dev/zero of=/path/to/mbr count=32

Here, a 16 KiB (32 * 512 bytes) file is created. It is important not to make it too small (even if the MBR only needs a single 512 bytes block), since the smaller it will be, the smaller the chunk size of the software RAID device will have to be, which could have an impact on performance. Then, you setup a loopback device to the MBR file:

 # losetup -f /path/to/mbr

Let us assume the resulting device is , because we would not already have been using other loopbacks. Next step is to create the "merged" MBR +  disk image using software RAID:

 # modprobe linear
 # mdadm --build --verbose /dev/md0 --chunk=16 --level=linear --raid-devices=2 /dev/loop0 /dev/hdaN

The resulting  is what you will use as a QEMU raw disk image (do not forget to set the permissions so that the emulator can access it). The last (and somewhat tricky) step is to set the disk configuration (disk geometry and partitions table) so that the primary partition start point in the MBR matches the one of  inside  (an offset of exactly 16 * 512 = 16384 bytes in this example). Do this using  on the host machine, not in the emulator: the default raw disc detection routine from QEMU often results in non-kibibyte-roundable offsets (such as 31.5 KiB, as in the previous section) that cannot be managed by the software RAID code. Hence, from the host:

 # fdisk /dev/md0

Press  to enter the expert menu. Set number of 's'ectors per track so that the size of one cylinder matches the size of your MBR file. For two heads and a sector size of 512, the number of sectors per track should be 16, so we get cylinders of size 2x16x512=16k.

Now, press  to return to the main menu.

Press  and check that the cylinder size is now 16k.

Now, create a single primary partition corresponding to . It should start at cylinder 2 and end at the end of the disk (note that the number of cylinders now differs from what it was when you entered fdisk.

Finally, 'w'rite the result to the file: you are done. You now have a partition you can mount directly from your host, as well as part of a QEMU disk image:

 $ qemu-system-x86_64 -hdc /dev/md0 ''You can, of course, safely set any boot loader on this disk image using QEMU, provided the original  partition contains the necessary tools.

## Using a Network Block Device
With [https://docs.kernel.org/admin-guide/blockdev/nbd.html Network Block Device, Linux can use a remote server as one of its block device. You may use  (from the  package) to create an MBR wrapper for QEMU.

Assuming you have already set up your MBR wrapper file like above, rename it to . Then create a symbolic link named  in the same directory, pointing to your partition. Then put the following script in the same directory:

{{bc|1=
#!/bin/sh
dir="$(realpath "$(dirname "$0")")"
cat >wrapper.conf  Select USB Devices for redirection) and  from  (File > USB device selection'') support this feature. Please make sure that you have installed the necessary SPICE Guest Tools on the virtual machine for this functionality to work as expected (see the #SPICE section for more information).

## Automatic USB forwarding with udev
Normally, forwarded devices must be available at the boot time of the virtual machine to be forwarded. If that device is disconnected, it will not be forwarded anymore.

You can use udev rules to automatically attach a device when it comes online. Create a  entry somewhere on disk. chown it to root to prevent other users modifying it.

Then create a udev rule which will attach/detach the device:

{{hc|/usr/lib/udev/rules.d/90-libvirt-mydevice|2=
ACTION=="add", \
    SUBSYSTEM=="usb", \
    ENV{ID_VENDOR_ID}=="03f0", \
    ENV{ID_MODEL_ID}=="4217", \
    RUN+="/usr/bin/virsh attach-device GUESTNAME /usr/local/hostdev-mydevice.xml"
ACTION=="remove", \
    SUBSYSTEM=="usb", \
    ENV{ID_VENDOR_ID}=="03f0", \
    ENV{ID_MODEL_ID}=="4217", \
    RUN+="/usr/bin/virsh detach-device GUESTNAME /usr/local/hostdev-mydevice.xml"
}}

Source and further reading.

## Enabling KSM
Kernel Samepage Merging (KSM) is a feature of the Linux kernel that allows for an application to register with the kernel to have its pages merged with other processes that also register to have their pages merged. The KSM mechanism allows for guest virtual machines to share pages with each other. In an environment where many of the guest operating systems are similar, this can result in significant memory savings.

To enable KSM:

 # echo 1 > /sys/kernel/mm/ksm/run

To make it permanent, use systemd's temporary files:

If KSM is running, and there are pages to be merged (i.e. at least two similar virtual machines are running), then  should be non-zero. See https://docs.kernel.org/admin-guide/mm/ksm.html for more information.

## Multi-monitor support
The Linux QXL driver supports four heads (virtual screens) by default. This can be changed via the  kernel parameter.

The default VGA memory size for QXL devices is 16M (VRAM size is 64M). This is not sufficient if you would like to enable two 1920x1200 monitors since that requires 2 × 1920 × 4 (color depth) × 1200 = 17.6 MiB VGA memory. This can be changed by replacing  by . If you ever increase vgamem_mb beyond 64M, then you also have to increase the  option.

## Custom display resolution
A custom display resolution can be set with  (see EDID and display resolution).

## Copy and paste
## SPICE
One way to share the clipboard between the host and the guest is to enable the SPICE remote desktop protocol and access the client with a SPICE client.
One needs to follow the steps described in #SPICE. A guest run this way will support copy paste with the host.

## qemu-vdagent
QEMU provides its own implementation of the spice vdagent chardev called . It interfaces with the spice-vdagent guest service and allows the guest and host share a clipboard.

To access this shared clipboard with QEMU's GTK display, you will need to compile QEMU from source with the  configure parameter. It is sufficient to replace the installed  package.

Add the following QEMU command line arguments:

 -device virtio-serial,packed=on,ioeventfd=on
 -device virtserialport,name=com.redhat.spice.0,chardev=vdagent0
 -chardev qemu-vdagent,id=vdagent0,name=vdagent,clipboard=on,mouse=off

These arguments are also valid if converted to libvirt form.

On linux guests, you may start the  user unit manually. On Windows guests, set the spice-agent startup type to automatic.

## Windows-specific notes
QEMU can run any version of Windows from Windows 95 through Windows 11.

It is possible to run Windows PE in QEMU.

## Fast startup
For Windows 8 (or later) guests it is better to disable "Turn on fast startup (recommended)" from the Power Options of the Control Panel as explained in the following forum page, as it causes the guest to hang during every other boot.

Fast Startup may also need to be disabled for changes to the  option to be properly applied.

## Remote Desktop Protocol
If you use a MS Windows guest, you might want to use RDP to connect to your guest virtual machine. If you are using a VLAN or are not in the same network as the guest, use:

 $ qemu-system-x86_64 -nographic -nic user,hostfwd=tcp::5555-:3389

Then connect with either  or  to the guest. For example:

 $ xfreerdp -g 2048x1152 localhost:5555 -z -x lan

## Time standard
By default, Windows assumes the firmware clock is set to local time, but this is usually not the case when using QEMU.
To remedy this you can configure Windows to use UTC after the installation, or you can set the virtual clock to localtime by adding  to your command line.

## Clone Linux system installed on physical equipment
Linux system installed on physical equipment can be cloned for running on a QEMU virtual machine. See Clone Linux system from hardware for QEMU virtual machine

## Chrooting into arm/arm64 environment from x86_64
Sometimes it is easier to work directly on a disk image instead of the real ARM based device. This can be achieved by mounting an SD card/storage containing the root partition and chrooting into it.

Another use case for an ARM chroot is building ARM packages on an x86_64 machine. Here, the chroot environment can be created from an image tarball from Arch Linux ARM - see for a detailed description of this approach.

Either way, from the chroot it should be possible to run pacman and install more packages, compile large libraries etc. Since the executables are for the ARM architecture, the translation to x86 needs to be performed by QEMU.

Install  on the x86_64 machine/host, and  to register the qemu binaries to binfmt service.

 is used to allow the execution of compiled programs from other architectures. This is similar to what is provided by , but the "static" variant is required for chroot. Examples:

 qemu-arm-static path_to_sdcard/usr/bin/ls
 qemu-aarch64-static path_to_sdcard/usr/bin/ls

These two lines execute the  command compiled for 32-bit ARM and 64-bit ARM respectively. Note that this will not work without chrooting, because it will look for libraries not present in the host system.

 allows automatically prefixing the ARM executable with  or .

Make sure that the ARM executable support is active:

Each executable must be listed.

If it is not active, restart .

Mount the SD card to  (the device name may be different).

 # mount --mkdir /dev/mmcblk0p2 /mnt/sdcard

Mount boot partition if needed (again, use the suitable device name):

 # mount /dev/mmcblk0p1 /mnt/sdcard/boot

Finally chroot into the SD card root as described in Change root#Using chroot:

 # chroot /mnt/sdcard /bin/bash

Alternatively, you can use arch-chroot from , as it will provide an easier way to get network support:

 # arch-chroot /mnt/sdcard /bin/bash

You can also use systemd-nspawn to chroot into the ARM environment:

 # systemd-nspawn -D /mnt/sdcard -M myARMMachine --bind-ro=/etc/resolv.conf

 is optional and gives a working network DNS inside the chroot

## sudo in chroot
If you install sudo in the chroot and receive the following error when trying to use it:

 sudo: effective uid is not 0, is /usr/bin/sudo on a file system with the 'nosuid' option set or an NFS file system without root privileges?

then you may need to modify the binfmt flags, for example for :

 # cp /usr/lib/binfmt.d/qemu-aarch64-static.conf /etc/binfmt.d/
 # vi /etc/binfmt.d/qemu-aarch64-static.conf

and add a  at the end of this file:

 :qemu-aarch64:M::\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\xb7\x00:\xff\xff\xff\xff\xff\xff\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff:/usr/bin/qemu-aarch64-static:FPC

Then restart  and check that the changes have taken effect (note the  on the  line):

See the "flags" section of the [https://docs.kernel.org/admin-guide/binfmt-misc.html kernel binfmt documentation for more information.

## Not grabbing mouse input
Tablet mode has side effect of not grabbing mouse input in QEMU window:

 -usb -device usb-tablet

It works with several  backends one of which is virtio.

## Troubleshooting
See QEMU/Troubleshooting.
