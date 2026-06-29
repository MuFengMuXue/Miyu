# Libvirt

Libvirt is a collection of software that provides a convenient way to manage virtual machines and other virtualization functionality, such as storage and network interface management. These software pieces include a long term stable C API, a daemon (libvirtd), and a command line utility (virsh). A primary goal of libvirt is to provide a single way to manage multiple different virtualization providers/hypervisors, such as the KVM/QEMU, Xen, LXC, OpenVZ or VirtualBox hypervisors (among others).

Some of the major libvirt features are:

*Virtual machine management: Various domain lifecycle operations such as start, stop, pause, save, restore, and migrate. Hotplug operations for many device types including disk and network interfaces, memory, and CPUs.
*Remote machine support: All libvirt functionality is accessible on any machine running the libvirt daemon, including remote machines. A variety of network transports are supported for connecting remotely, with the simplest being SSH, which requires no extra explicit configuration.
*Storage management: Any host running the libvirt daemon can be used to manage various types of storage: create file images of various formats (qcow2, vmdk, raw, ...), mount NFS shares, enumerate existing LVM volume groups, create new LVM volume groups and logical volumes, partition raw disk devices, mount iSCSI shares, and much more.
*Network interface management: Any host running the libvirt daemon can be used to manage physical and logical network interfaces. Enumerate existing interfaces, as well as configure (and create) interfaces, bridges, vlans, and bond devices.
*Virtual NAT and Route based networking: Any host running the libvirt daemon can manage and create virtual networks. Libvirt virtual networks use firewall rules to act as a router, providing virtual machines transparent access to the host machines network.

## Installation
Because of its daemon/client architecture, libvirt needs only be installed on the machine which will host the virtualized system. Note that the server and client can be the same physical machine.

## Server
Install the  package, as well as at least one hypervisor:

* The libvirt KVM/QEMU driver is the primary libvirt driver and if KVM is enabled, fully virtualized, hardware accelerated guests will be available. See the QEMU article for more information.
* Other supported hypervisors include LXC, VirtualBox and Xen. See the respective articles for installation instructions. With respect to   installation note:
** The libvirt LXC driver has no dependency on the LXC userspace tools provided by , therefore there is no need to install the package if planning on using the driver.  needs to be running to use  connection.
** Xen support is available, but not by default (). You need to use the ABS to modify 's PKGBUILD and build it without the  option.

For network connectivity, install:

*  for the default NAT/DHCP networking.
*  for remote management over SSH.

Other optional dependencies may provide desired or extended features, such as  for DMI system info support. Install the ones you may need as dependencies after reading pacman's output for .

## Client
The client is the user interface that will be used to manage and access the virtual machines.

*
*
*
*
*
*

A list of libvirt-compatible software can be found here.

## Configuration
Libvirt can manage QEMU virtual machines in two modes, system and session* system URIs connect to the libvirtd daemon running as root which is launched at system startup. Virtual machines created and run using 'system' are usually launched as root, unless configured otherwise (for example in )
* session URIs launch a libvirtd instance as your local user, and all virtual machines are run with local user permissions.

Regarding their pros and cons:

* Virtual machine auto-starting on host boot only works for 'system', and the root libvirtd instance has necessary permissions to use proper networking via bridges or virtual networks.  is generally what tools like virt-manager default to.
*  has a serious drawback: since the libvirtd instance does not have sufficient privileges, the only out of the box network option is qemu's usermode networking, which has non-obvious limitations, so its usage is discouraged ([https://web.archive.org/web/20210426155203/https://people.gnome.org/~markmc/qemu-networking.html more info on qemu networking options)

:The benefit of  is that permission issues vanish: disk images can easily be stored in $HOME, serial PTYs are owned by the user, etc.

For ''system-level administration (i.e. global settings and image-volume'' location), libvirt minimally requires setting up authorization, and starting the daemon.

For user-''session administration, daemon setup and configuration is not required; however, authorization is limited to local abilities; the front-end will launch a local instance of the libvirtd''' daemon.

## Set up authentication
From libvirt: Connection authentication:
:The libvirt daemon allows the administrator to choose the authentication mechanisms used for client connections on each network socket independently. This is primarily controlled via the libvirt daemon master config file in . Each of the libvirt sockets can have its authentication mechanism configured independently. There is currently a choice of ,  and .

## Using libvirt group
The easiest way to ensure your user has access to libvirt daemon is to add member to  user group.

Members of the  group have password-less access to the RW daemon socket by default.

## Using polkit
Because  pulls  as a dependency during installation, polkit is used as the default value for the  parameter (source). File-based permissions remain nevertheless available.

The libvirt daemon provides two polkit actions in :

*  for full management access (RW daemon socket), and
*  for monitoring only access (read-only socket).

The default policy for the RW daemon socket will require to authenticate as an admin. This is akin to sudo auth, but does not require that the client application ultimately run as root. Default policy will still allow any application to connect to the RO socket.

Arch defaults to consider anybody in the  group as an administrator: this is defined in  (see Polkit#Administrator identities). Therefore there is no need to create a new group and rule file if your user is a member of the  group: upon connection to the RW socket (e.g. via ) you will be prompted for your user's password.

You may change the group authorized to access the RW daemon socket. As an example, to authorize the  group, create the following file:

{{hc|/etc/polkit-1/rules.d/50-libvirt.rules|
/* Allow users in mykvm group to manage the libvirt
daemon without authentication */
polkit.addRule(function(action, subject) {
    if (action.id == "org.libvirt.unix.manage" &&
        subject.isInGroup("mykvm")) {
            return polkit.Result.YES;
    }
});
}}

Then add yourself to the  group and relogin. Replace mykvm with any group of your preference just make sure it exists and that your user is a member of it (see Users and groups for more information).

Do not forget to relogin for group changes to take effect.

## Authenticate with file-based permissions
To define file-based permissions for users in the libvirt group to manage virtual machines, uncomment and define:

While some guides mention changed permissions of certain libvirt directories to ease management, keep in mind permissions are lost on package update. To edit these system directories, root user is expected.

## Daemon
Start both  and . Optionally enable  (which will also enable  and  units, so there is NO need to also enable ).

Another possibility is to only start/enable  and  for on-demand socket activation.

## Unencrypt TCP/IP sockets
Edit :

It is also necessary to start the server in listening mode by editing :

## Access virtual machines using their hostnames
For host access to guests on non-isolated, bridged networks, enable the  and/or  NSS modules provided by . For the comparison of the two modules and technical details, see libvirt documentation.

Add desired modules in :

## Test
To test if libvirt is working properly on a system level:

 $ virsh -c qemu:///system

To test if libvirt is working properly for a user-session:

 $ virsh -c qemu:///session

## Management
Libvirt management is done mostly with three tools:  (GUI), virsh, and guestfish (which is part of ).

## virsh
The virsh program is for managing guest domains (virtual machines) and works well for scripting, virtualization administration.  Though most virsh commands require root privileges to run due to the communication channels used to talk to the hypervisor, typical management, creation, and running of domains (like that done with VirtualBox) can be done as a regular user.

The virsh program includes an interactive terminal that can be entered if no commands are passed (options are allowed though): .  The interactive terminal has support for tab completion.

From the command line:

 $ virsh [argument...

From the interactive terminal:

 virsh #  Help is available:

 $ virsh help [option* or === Storage pools ===

A pool is a location where storage volumes can be kept.  What libvirt defines as volumes others may define as "virtual disks" or "virtual machine images".  Pool locations may be a directory, a network filesystem, or partition (this includes a LVM).  Pools can be toggled active or inactive and allocated for space.

On the system-level,  will be activated by default; on a user-session,  creates .

Print active and inactive storage pools:

 $ virsh pool-list --all

## Create a new pool using virsh
If one wanted to add a storage pool, here are examples of the command form, adding a directory, and adding a LVM volume:

 $ virsh pool-define-as name type [source-host [source-dev [ format
 $ virsh pool-define-as poolname dir - - - - /home/username/.local/libvirt/images
 $ virsh pool-define-as poolname fs - -  /dev/vg0/images - mntpoint

The above command defines the information for the pool, to build it:

 $ virsh pool-build     poolname
 $ virsh pool-start     poolname
 $ virsh pool-autostart poolname

To remove it:

 $ virsh pool-undefine  poolname

## Create a new pool using virt-manager
First, connect to a hypervisor (e.g. QEMU/KVM system, or user-session).  Then, right-click on a connection and select Details; select the Storage tab, push the + button on the lower-left, and follow the wizard.

## Storage volumes
Once the pool has been created, volumes can be created inside the pool.  If building a new domain (virtual machine), this step can be skipped as a volume can be created in the domain creation process.

## Create a new volume with virsh
Create volume, list volumes, resize, and delete:
 $ virsh vol-create-as      poolname volumename 10GiB --format aw|bochs|raw|qcow|qcow2|vmdk
 $ virsh vol-upload  --pool poolname volumename volumepath
 $ virsh vol-list           poolname
 $ virsh vol-resize  --pool poolname volumename 12GiB
 $ virsh vol-delete  --pool poolname volumename
 $ virsh vol-dumpxml --pool poolname volumename  # for details.

## Domains
Virtual machines are called domains.  If working from the command line, use  to list, create, pause, shutdown domains, etc.   can be used to view domains started with .  Creation of domains is typically done either graphically with  or with  (a command line program installed as part of the  package).

Creating a new domain typically involves using some installation media, such as an  from the storage pool or an optical drive.

Print active and inactive domains:

 # virsh list --all

## Create a new domain using virt-install
For an extremely detailed domain (virtual machine) setup, it is easier to #Create a new domain using virt-manager.  However, basics can easily be done with  and still run quite well.  Minimum specifications are , , guest storage (, , or ), and an install method (generally an  or CD). See  for more details and information about unlisted options.

Arch Linux install (two GiB, qcow2 format volume create; user-networking):

 $ virt-install  \
   --name arch-linux_testing \
   --memory 1024             \
   --vcpus=2,maxvcpus=4      \
   --cpu host-model                \
   --cdrom $HOME/Downloads/arch-linux_install.iso \
   --osinfo detect=on,name=archlinux \
   --disk size=2,format=qcow2  \
   --network user            \
   --virt-type kvm

Fedora testing (Xen hypervisor, non-default pool, do not originally view):

 $ virt-install  \
   --connect xen:///     \
   --name fedora-testing \
   --memory 2048         \
   --vcpus=2             \
   --cpu=host-model            \
   --cdrom /tmp/fedora20_x84-64.iso      \
   --os-type=linux --os-variant=fedora20 \
   --disk pool=testing,size=4            \
   --network bridge=br0                  \
   --graphics=vnc                        \
   --noautoconsole
 $ virt-viewer --connect xen:/// fedora-testing

Windows:

 $ virt-install \
   --name=windows7           \
   --memory 2048             \
   --cdrom /dev/sr0          \
   --os-variant=win7         \
   --disk /mnt/storage/domains/windows7.qcow2,size=20GiB \
   --network network=vm-net  \
   --graphics spice

Import existing volume:

 $ virt-install  \
   --name demo  \
   --memory 512 \
   --disk /home/user/VMs/mydisk.img \
   --import

## Create a new domain using virt-manager
First, connect to the hypervisor (e.g. QEMU/KVM system or user session), right click on a connection and select New, and follow the wizard.

* On the fourth step, de-selecting Allocate entire disk now will make setup quicker and can save disk space in the interim; however, it may cause volume fragmentation over time.
* On the fifth step, open Advanced options and make sure that Virt Type is set to kvm (this is usually the preferred method).  If additional hardware setup is required, select the Customize configuration before install option.

## Manage a domain
Start a domain:

 $ virsh start domain
 $ virt-viewer --connect qemu:///session domain

Gracefully attempt to shutdown a domain; force off a domain:

 $ virsh shutdown domain
 $ virsh destroy  domain

Autostart domain on libvirtd start:

 $ virsh autostart domain
 $ virsh autostart domain --disable

Shutdown domain on host shutdown:

: Running domains can be automatically suspended/shutdown at host shutdown using the  systemd service. This same service will resume/startup the suspended/shutdown domain automatically at host startup. See  for details and service options.

Edit a domain's XML configuration:

 $ virsh edit domain

To know more about XML configurations read the XML format section of the libvirt wiki.

## Windows requirements
Recent Windows client and server versions have specific requirements for a machine. From Windows 11 onwards, it is necessary to configure the domain for UEFI mode, as it does not support BIOS mode. Windows Server can still be installed in a non-UEFI environment; it is however recommended by Microsoft to use UEFI mode at least for Windows Server 2022 and newer. See #UEFI support for how to achieve this.

Additionally, Windows 11 requires a Trusted Platform Module to be provided to the domain. Again, for Windows Server this is still optional, but recommended. Please note that TPM version 1.2 is not supported from Windows 11 onwards, and the domain has to be set up with a TPM version 2.0. A TPM emulator can be used, as described in #TPM support.

Lastly, Windows recommends using Secure Boot, and libvirt can provide an adequate environment. See #UEFI support and KVM#Secure Boot to view how to enroll the Microsoft keys in the firmware storage of the domain with . Alternatively, this guide can be used to achieve the same thing manually. Secure Boot is not a strict requirement though, and this can be deployed after the domain has been installed as well.

Recent Windows versions, especially Windows 11 and Windows Server 2025, ship a security feature called Virtualization-based security (VBS). This technology uses hardware virtualization itself to isolate parts of the kernel. It is possible to run Windows with VBS in a libvirt domain using QEMU/KVM if nested virtualization is available for a domain, see #Nested virtualization for how to enable it.

## Networking
## Virtual networks
Virtual networks are used to connect domains to either internal or external networks. The bridge device is used to define the virtual network. Additionally, the forwarding mode is used to define the internal or external networks a domain is able to reach.

## Forwarding modes
Some common forwarding modes are listed below:

{| class="wikitable"
! Mode !! Description
|-
| Bridge || The virtual network is connected to the same network segment as the host.
|-
| NAT || The virtual network uses the host's networking stack, uses NAT, and inbound connections are restricted.
|-
| Routed || The virtual network uses the host's networking stack, and inbound connections are restricted.
|-
| Open || The virtual network uses the host's networking stack.
|-
| Isolated || No other networks are reachable from the virtual network.
|}

## Using iptables
If iptables is to be used and not nftables, it is necessary to specify this accordingly in the configuration file.

For example:

## Retrieving a domain IP address
If using the  network and addresses are assigned using DHCP:

 $ virsh net-dhcp-leases default

If the domain is using the :

 $ virsh domifaddr --source agent domain

## Using nftables
When using network type NAT in combination with a simple nftables firewall, you may need to allow forwarding to/from the virtual network interface, and allow DNS/DHCP requests for DHCP clients from the virtual network interface to the host.

The relevant sections of  are below:

{{hc|/etc/nftables.conf|
# ...
table inet filter {
  chain input {
    type filter hook input priority filter
    policy drop
    # ...
    iifname virbr0 udp dport {53, 67} accept comment "allow VM dhcp/dns requests to host"
    # ...
  }

  chain forward {
    type filter hook forward priority filter
    policy drop

    iifname virbr0 accept
    oifname virbr0 accept
  }
}
}}

## Adding an IPv6 address
When adding an IPv6 address through any of the configuration tools, you will likely receive the following error:
 Check the host setup: enabling IPv6 forwarding with RA routes without accept_ra set to 2 is likely to cause routes loss. Interfaces to look at: eth0

Fix this by running the following command (replace  with the name of your physical interface):

 # sysctl net.ipv6.conf.eth0.accept_ra=2

## Port forwarding to domains
Details on how to do this can be found in the libvirt NAT forwarding documentation.

## Snapshots
Snapshots take the disk, memory, and device state of a domain at a point-of-time, and save it for future use.  They have many uses, from saving a "clean" copy of an OS image to saving a domain's state before a potentially destructive operation.  Snapshots are identified with a unique name.

Snapshots are saved within the volume itself and the volume must be the format: qcow2 or raw.  Snapshots use deltas in order not to take as much space as a full copy would.

## Create a snapshot
Once a snapshot is taken it is saved as a new block device and the original snapshot is taken offline.  Snapshots can be chosen from and also merged into another (even without shutting down the domain).

Print a running domain's volumes (running domains can be printed with ):

To see a volume's physical properties:

Create a disk-only snapshot (the option  will prevent the volume from being modified if snapshot creation fails):

 # virsh snapshot-create-as domain snapshot1 --disk-only --atomic

List snapshots:

One can then copy the original image with  or  and then merge the original back into snapshot:

 # virsh blockpull --domain domain --path /vms/domain.snapshot1

 becomes a new volume.  After this is done the original volume ( and snapshot metadata can be deleted.   The  would work opposite to  but it seems to be currently under development (including , scheduled to be released sometime next year.

## Other management
List virtual machines in the system mode:

 $ virsh --connect qemu:///system list --all

Connect to a non-default hypervisor:

 $ virsh --connect xen:///
 virsh # uri
 xen:///

Connect to a QEMU hypervisor over SSH; and the same with logging:

 $ virsh --connect qemu+ssh://username@host/system
 $ LIBVIRT_DEBUG=1 virsh --connect qemu+ssh://username@host/system

Connect a graphic console over SSH:

 $ virt-viewer  --connect qemu+ssh://username@host/system domain
 $ virt-manager --connect qemu+ssh://username@host/system domain

Connect to the system's VirtualBox hypervisor (VirtualBox support in libvirt is not stable yet and may cause  to crash):

 $ virsh --connect vbox:///system

List and dump network configuration:

 $ virsh -c qemu:///system net-list --all
 $ virsh -c qemu:///system net-dumpxml default

## Hooks
Hooks are scripts that are triggered by different events happening while starting and running the libvirt daemon.
They can be used to execute commands needed in preparation to launch a guest like setup networks or reserve memory.

The following hooks exists:

* daemon - occasions to trigger: start, shutdown, reload
* qemu - occasions to trigger: prepare, prepare, start, started, stopped, release, migrate, restore, reconnect, attach
* lxc - occasions to trigger: prepare, start, started, stopped, release, reconnect
* libxl - occasions to trigger: prepare, start, started, stopped, release migrate, reconnect
* network - occasions to trigger: start, started, stopped, port-created, updated, port-deleted

See the libvirt Documentation for details about each hook and trigger.

## Create a hook
Hooks are represented by scripts located at . If the folder does not exist, you have to create it.
Each hook is represented by a script in this folder with the same name (e.g. ) or a sub-folder (e.g. ). The later can contain different scripts, which are all run at the trigger points. The scripts are run like any other scripts, so they need to start with the declaration of the command interpreter to use (e.g. ) and be executable by the libvirt user.

Every time a trigger point is met, the script is run. For example, the daemon script would run at least two times in a start/stop cycle of the system, at start and at shutdown. To run an command only at a given point, you have to implement conditions in the script. To do this, libvirt passes parameters which can be used to identify the current trigger condition.

According to the libvirt documentation these parameters are defined as follows:

* Parameter 1: The name of the object involved in the operation
* Parameter 2: The name of the operation being performed
* Parameter 3: Used if a sub-operation is to be named
* Parameter 4: An extra argument if needed

If one of the arguments is not applicable, a dash is passed.

## Example
To run an command every time you start an qemu guest, before any resources are allocated, you can use the qemu hook. At this point, libvirt runs the hooks like this:
The script for this could like this:

If the guest is stopped, the same script would be run, but this time the daemon would start the command like this:

## Sharing data between host and guest
## Virtio-FS
Sharing files with Virtio-FS lists an overview of the supported options to enable filesharing with the guest.

## Set up the memory backend
Memory backends must be allocated before using virtiofs. memfd and file-backed memory backends can be used in system sessions and unprivileged QEMU/KVM user sessions. Hugepages only supports system sessions.

## memfd
To use memfd memory backend, you need to add the following domain XML elements:

## file-backed
Add the following domain XML elements:

You can configure where the backing file is stored with the  option in  or, if you are running a user session, in :

## hugepage
First you need to enable hugepages which are used by the virtual machine:

To determine the number of hugepages needed check the size of the hugepages:

 $ grep Hugepagesize /proc/meminfo

The number of hugepages is memory size of virtual machine / Hugepagesize. Add to this value some additional pages. You have to reboot after this step, so that the hugepages are allocated.

Now you have to prepare the configuration of the virtual machine:

It is necessary to add the NUMA definition so that the memory access can be declared as shared. id and cpus values for NUMA will be inserted by virsh.

## Configure filesystem passthrough
Add the following domain XML elements:

Replace  with the directory you want to share, and mount_tag with an arbitrary string that will be used to identify the shared file system in the guest.

It should now be possible to mount the folder in the shared machine:

 # mount -t virtiofs mount_tag /mnt/mount/path

Add the following fstab entry to mount the folder automatically at boot:

## Mapping user/group IDs in unprivileged mode
By default, the root user (id 0) in the guest is mapped to the current user on the host.
Other IDs are mapped to the subordinate user IDs specified in  and .

You can also configure this mapping manually using idmap tag:

## 9p
File system directories can be shared using the 9P protocol. Details are available in QEMU's documentation of 9psetup.

Configure the virtual machine as follows:

Boot the guest and mount the shared directory from it using:

 # mount -t 9p -o trans=virtio,version=9p2000.L mount_tag /path/to/mount_point/on/guest

See https://docs.kernel.org/filesystems/9p.html for more mount options.

To mount it at boot, add it to the guest's fstab:

The module for the 9p transport (i.e.  for ) will not be automatically loaded, so mounting the file system from  will fail and you will encounter an error like . The solution is to preload the module during boot:

## Samba / SMB
An other easy way to share data between guest and host is to use the smb protocol. While performance and latency may not be as good as in the other described ways, its sufficient for simple tasks like transfering simple files like images or documents from and to the guest.

The smb server can be set up directly on either the host, or the guest, for example using Samba, eliminating the need for a dedicated file server. Windows guests have the ability to create smb shares included right after installation (Microsoft Supportpage).

One possible way to access the share under linux (either from the host, or from the guest, depending, where you have installed your server) is to create an entry in your fstab. The  package is required.

 ensures that the share is only mounted when needed without causing issues if the virtual machine is not booted.  gives you the ability to mount the share on the fly while first accessing it, without needing a password.

## UEFI support
Libvirt can support UEFI virtual machines through QEMU and OVMF.

Install the  package.

Restart .

Now you are ready to create a UEFI virtual machine. Create a new virtual machine through virt-manager. When you get to the final page of the New VM wizard, do the following:

# Click Customize configuration before install, then select Finish.
# In the Overview screen, change the Firmware field to:
#*  for x64 UEFI without Secure Boot support,
#*  for x64 UEFI with Secure Boot support (without any pre-enrolled certificates).
# Click Apply.
# Click Begin Installation.

See Fedora:Using UEFI with QEMU for more information.

For enrolling keys,  can be used, see KVM#Secure Boot.

## TPM support
QEMU can provide a Trusted Platform Module to the guest. This can be either a passthrough device, i.e. using a physical TPM in a virtual machines or an emulator. For using an emulator, the  package has to be installed. It is possible to provide TPM versions 1.2 or 2.0 to the guest, but 2.0 requires the domain to use UEFI.

In its simplest form, to provide a useable TPM 2.0 for the guest machine with an emulator, the following block in the domain specification will work:

For additional information and options, please see the libvirt documentation found here.

## Hyper-V enlightenments
QEMU supports various Hyper-V compatible enlightenments that improve performance for Windows guests and add some additional features, see the QEMU documentation.

These enlightenments can also be activated through libvirt, depending on the QEMU and libvirt version present. The upstream documentation listing the currently supported enlightenments can be found in this section of the libvirt documentation. In general, they can all be enabled, but doing so will put requirements on the QEMU and libvirt versions used, which can be an issue if domain migration is desired.

## Tips and tricks
## Using an entire physical disk device inside the virtual machine
You may have a second drive with a different OS (like Windows) on it and may want to gain the ability to also boot it inside a virtual machine. Since the drive access is raw, the OS will perform quite well inside the virtual machine.

## Windows virtual machine boot prerequisites
Be sure to install the VirtIO drivers inside the OS on that drive before trying to boot it in the virtual machine.
For Win 7 use version 0.1.173-4.
Some singular drivers from newer VirtIO builds may be used on Win 7 but you will have to install them manually via the Device Manager.
For Win 10 and 11 you can use the latest VirtIO build.

Open the ISO that you downloaded and run  to install the drivers on your system. For older versions that do not have this binary, run  instead (or  for 32-bit systems).

## Set up the windows disk interface drivers
You may get a  bluescreen when trying to boot the virtual machine. This means Windows can not access the drive during the early boot stage because the disk interface driver it would need for that is not loaded / is set to start manually.

The solution is to enable these drivers to start at boot.

In , find the folders , , , ,  (may not exist), , , , ,  and . Inside each of those, set all their  values to  in order to enable them at boot. If your drive is a PCIe NVMe drive, also enable that driver (should it exist).

If you want to use the VirtIO bus to access the drive instead of the SATA bus, you need to install the block device drivers, i.e.  and . These can be installed via pnputil, on a cmd/PowerShell prompt with admin privileges (assuming the VirtIO ISO you downloaded is mounted at ):

 > pnputil.exe -a -i D:\vioscsi\w11\amd64\*.inf
 > pnputil.exe -a -i D:\viostor\w11\amd64\*.inf

Alternatively, they can be installed with the Device Manager or with Driver Store Explorer.

## Find the unique path of your drive
Run . From the output, pick out the ID of the drive you want to insert into the virtual machine, for example . Now add that ID to  so you get . That is the unique path to that drive.

Do not choose an ID that represents a partition on the drive, it must be the one representing the full drive. Here is another example, with the desired drive being :

In the example above, the full path used would be .

## Add the drive in QEMU CLI
In QEMU CLI that would probably be . Just modify  to be the unique path of your drive.

## Add the drive in libvirt
In libvirt XML that translates to

Just modify  to be the unique path of your drive.

## Add the drive in virt-manager
When creating a virtual machine, select Import existing drive and just paste that unique path. If you already have the virtual machine, click on Add hardware > Storage >  Select or create custom storage > paste the unique path.

## Python connectivity code
The  package provides a Python API in .

General examples are given in

Unofficial example using  and :

{{bc|
#! /usr/bin/env python3
import socket
import sys
import libvirt

conn = libvirt.open("qemu+ssh://xxx/system")
print("Trying to find node on xxx")
domains = conn.listDomainsID()
for domainID in domains:
    domConnect = conn.lookupByID(domainID)
    if domConnect.name() == 'xxx-node':
        print("Found shared node on xxx with ID {}".format(domainID))
        domServ = domConnect
        break
}}

## Advanced Format 4K native disk
To turn a disk into an Advanced Format 4Kn disk, both its physical and logical sector size needs to be set to 4 KiB. For virtio-blk and virtio-scsi this can be done by setting the  and  options with the element. For example:

## Nested virtualization
libvirt can provide nested virtualization to its domains when running QEMU/KVM. In order to do this, KVM must be configured appropriately, see KVM#Nested virtualization.

The only change to be made in the libvirt configuration is to set the CPU model of the domain to either  or .

## Commanding QEMU
Libvirt is capable of passing on QEMU command line arguments to the underlying QEMU instance running the virtual machine.
This functionality is highly useful when libvirt does not provide QEMU features (yet). For examples, see the entire Intel GVT-g article.

## Modify virtual machine XML schema for QEMU
This serves to enable QEMU-specific elements. Change

to

## QEMU command line arguments
In libvirt, QEMU command line arguments separated by whitespaces need to be provided separately.

The correct location to insert them is at the end of the  element, i. e. right above the closing  tag.

 -display gtk,gl=es,zoom-to-fit=off

Becomes

## Troubleshooting
## PulseAudio on system instance
The PulseAudio daemon normally runs under your regular user account, and will only accept connections from the same user. This can be a problem if QEMU is being run as root through libvirt. To run QEMU as a regular user, edit  and set the  option to your username.

 user = "dave"

You will also need to tell QEMU to use the PulseAudio backend and identify the server to connect to. Add the following section to your domain configuration using .

 is your user id. Change it if necessary.

You can omit the latency settings (in microseconds) but using the defaults might result in crackling.

## Hypervisor CPU use
Default virtual machine configuration generated by virt-manager may cause rather high (10-20%) CPU use caused by the QEMU process.
If you plan to run the virtual machine in headless mode, consider removing some of the unnecessary devices.

## Virtual machine cannot be un-paused on virt-manager
If you are using a disk image format such as qcow2 which has a specified virtual capacity, but only stores what is needed, then you need to have space on the host partition for the image to grow. If you see I/O related errors when attempting to start the virtual machine, it is possible that the host partition holding the virtual disk image is full. You can run  on the host to verify how much free space is available.

If this is the case, see System maintenance#Clean the filesystem for ways to free up space.

## Redirect USB Device is greyed out in virt-manager
If the Redirect USB Device menu item is greyed out, check that the following hardware is configured for the virtual machine:

* A USB Controller.
* One or more USB Redirectors.

If the option is still greyed out even with this hardware present, you can still add your device directly to the VM's hardware list and remove it when you're done.

## Error starting domain: Requested operation is not valid
When you try to open a virtual machine this error may pop up. This is because when you try to open a existing virtual machine libvirt tries to search for the default network which is not available. To make it available you have to autostart your network interface so that whenever your restart your computer your network interface is always active. See libvirt networking page.

Look at the name of your network interface with the following command:

 # virsh net-list --all

To autostart your network interface:

 # virsh net-autostart name_of_the_network

To start your network interface:

 # virsh net-start name_of_the_network

## Virt Manager Error 'Virt Manager doesn't have search permissions'
Ensure the folder containing your virtual machine files and installation ISO are owned by the  group

 # chown -R $USER:libvirt-qemu /path/to/virtual/machine

## Error starting domain: Requested operation is not valid: network 'default' is not active
If for any reason the default network is deactivated, you will not be able to start any guest virtual machines which are configured to use the network. Your first attempt can be simply trying to start the network with virsh.

 # virsh net-start default

For additional troubleshooting steps, see === UFW firewall blocking Libvirt ===

Libvirt requires IP forwarding to be enabled. Run the following commands:

 # sudo ufw route allow in on virbr0
 # sudo ufw route allow out on virbr0
 # sudo ufw allow in on virbr0

In addition to routing rules and policy, you must also setup IP forwarding. This may be done by setting the following in /etc/ufw/sysctl.conf:

 # net/ipv4/ip_forward=1
 # net/ipv6/conf/default/forwarding=1
 # net/ipv6/conf/all/forwarding=1

then restarting the firewall:

 # ufw disable
 # ufw enable

## EGL_NOT_INITIALIZED: render node init failed
This issue commonly affects owners of NVIDIA GPUs with the official drivers, and it prevents enabling OpenGL acceleration with the dGPU's render node selected. [https://forums.developer.nvidia.com/t/egl-errors-with-qemu-kvm-and-virtio-w-hardware-acceleration/318750 This forum thread contains many reports of this problem.

Hopefully Nvidia will fix this in a future driver release, but as of May 11th 2026, it hasn't been fixed yet. Fortunately, there are workarounds.

Switching to the Nouveau driver or doing PCI passthrough via OVMF are good options that should be considered. If there is a GPU from another brand present (e.g. an iGPU on laptops with hybrid graphics), it can be used as the render node instead of the Nvidia GPU. However, if neither of these options are desirable to you, there's another alternative, which was documented here: 1. Verify if the following udev rules are already present in your system, and add them if not: [https://github.com/virt-manager/virt-manager/issues/938#issuecomment-3814628493

2. Uncomment the  block and add the following devices to it (verify if they exist in your system):

Find the proper XYZ value that represents the GPU you wish to use. If you know the GPU's PCI address, run  to see the correct value.

Users with older driver versions may need to add  to the configuration file, but this is not recommended and should only be done as a last resource. You can read more about it in QEMU's documentation and Wikipedia.

Restart  after saving your changes to the configuration file.

3. Add the following graphics sections to your VM's XML (adjust them according to your case):

More information can be found in the Graphics Framebuffers section of the libvirt XML documentation. You can also check this thread on libvirt's GitLab.

Now you should be able to use your Nvidia GPU for OpenGL acceleration. Hopefully this workaround won't be needed in the future.
