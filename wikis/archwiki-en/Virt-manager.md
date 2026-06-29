# Virt-manager

virt-manager is a graphical user front end for the libvirt library, which provides virtual machine management services. virt-manager interface makes it easy for the user to create, delete and manipulate virtual machines without going through the terminal.

virt-manager mainly supports KVM but it can work with other hypervisors, such as Xen and LXC.

## Installation
First follow the libvirt or LXC pages and ensure you can create virtual machines, then install the  package. Install QEMU if needed.

To use a LXC connection, enable/start the  unit.

To use a QEMU connection, enable/start the  unit.

You can check the unit status to make sure the service is running.

## Configuration
## Basic configuration
Add yourself to the  user group.

It is also a good idea to ensure that any files/folders outside of virt-manager's default pool are owned by the  group, otherwise you might encounter permission errors when accessing files outside of the default pool.

## Tips and tricks
## Non root KVM without Socket
To use as a normal user without root, we need to configure KVM. This will also enable libvirt's networking components.

Set the UNIX domain socket ownership to  and the UNIX socket permission to read and write by changing the following:

If you haven't already, add your user to the  user group.

Add your user to . Otherwise, QEMU will give a  error when trying to access local drives.

Search for  or , uncomment both entries and change  to your user name or ID. Once edited it should look something like this:

Upon opening Virt-Manager, it will default to the system variant (root) of the QEMU connection. This can be changed to the user connection by going to: File > Add Connection. Now select  as the hypervisor and click OK. This will now auto-connect to the user session. You can now disconnect and remove the system connection if desired.

## Networking
To use a network bridge in user session it has to be setup in  system administration first.

For this the  daemon must be running.

When it is started successfully, the system variant (root) of the QEMU connection can be opened in virt-manager. Setup the bridge with the desired settings in the networking tab there.

To be able to use the bridge in a user session virtual machine, setup the qemu-bridge-helper according to your bridge setup.

After that the bridge can be used at a virtual network that runs in virt-manager user session.

## Creating a Virtual Interface
Go to Edit > Connection Details > Add

The following options are available:

* NAT
* Routed
* Open
* Isolated
* SR-IOV Pool

You can read further details in libvirt's documentation.

## NAT
NAT routes the VM over the same IP as the host. This option is available in the Show hardware > NIC and usually does not need any additional configuration.

## Bridged
Bridged mode acts as if the VM is its own client in the network.
In virt-manager you must select an interface for it.

This functionality is different from VirtualBox and VMware, where the interface is automatically selected.
In order to use Bridged you should create a virtual interface with NAT.

It is possible to use your own interface, but that might require additional configuration.

## Host-Only
A host-only configuration only permits network operations between host and guest.

This option doesn't exist for virt-manager. Instead you must use a bridge connected to a virtual isolated network. See #Creating a Virtual Interface

## 3D acceleration
virtio is a paravirtual 3D graphics driver. To enable basic 3D acceleration:

# Go to a virtual machine's setting page.
# Click on the "Add Hardware" button > Video > select the "Model" as "Virtio".  Then remove any other "Video" virtual hardware (within the sidebar).
# Go to "Display Spice" and set "Listen Type" to "None".  Also tick the "OpenGL" checkbox and select the appropriate renderer.
# Click on "Video Virtio" and tick "3D Acceleration".

You can use glxgears from the  package to test the 3D graphics.  displays OpenGL renderer info in the console.

## Troubleshooting
## No network connectivity with QEMU/KVM
Change this setting. See == See also ==

* [https://virt-manager.org Project homepage
* Project repository
* Spice drivers (graphics)
* VirtIO Windows drivers
