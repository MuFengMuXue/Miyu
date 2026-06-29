# VirtualBox

VirtualBox is a hypervisor used to run operating systems in a special environment, called a virtual machine, on top of the existing operating system. VirtualBox is in constant development and new features are implemented continuously. It comes with a Qt graphical user interface, as well as headless and SDL command-line tools for managing and running virtual machines.

In order to integrate functions of the host system to the guests, including shared folders and clipboard, video acceleration and a seamless window integration mode, guest additions are provided for some guest operating systems.

For more information, see the official documentation.

## Installation steps for Arch Linux hosts
In order to launch VirtualBox virtual machines on your Arch Linux box, follow these installation steps.

## Install the core packages
Install the  package. You will also need to choose a package to provide host modules:

* for the  kernel, choose ,
* for the  kernel, choose ,
* for any other kernel, choose .

To compile the VirtualBox modules provided by , it will also be necessary to install the appropriate headers package(s) for your installed kernel(s) (e.g.  for ). When either VirtualBox or the kernel is updated, the kernel modules will be automatically recompiled thanks to the DKMS pacman hook.

## Sign modules
When using a custom kernel with  option enabled, you must sign your modules with a key generated during kernel compilation.

You can sign the modules by executing the following command as root:

 # find "/lib/modules/$(uname -r)/" '(' -name 'vboxdrv.ko*' -o -name 'vboxnetadp.ko*' -o -name 'vboxnetflt.ko*' ')' -exec /lib/modules/$(uname -r)/build/scripts/sign-file sha256 /lib/modules/$(uname -r)/build/certs/signing_key.pem /lib/modules/$(uname -r)/build/certs/signing_key.x509 {} ';'

If you experience an error such as the following:

Then run the command  to navigate to your kernel tree folder and check if the  folder actually has a  file. If not, create a file somewhere on your system (does not have to be in the kernel tree folder) named  with the following contents (based on Gentoo:Signed kernel module support#Building the kernel with proper keys):

Then run  in the directory you created the  file and move the resulting files to the  directory in the kernel tree folder, then run  as root. You should then be able to rerun the signing command without an error.

If this still does not work, try updating your kernel to a newer version that has signing files already available (most kernel packages should), or if you are compiling your own, make sure that you copy the  and  from the folder you are building the kernel with to the  directory after you have built the kernel and are running it.

## Load the VirtualBox kernel modules
 and  use  to load VirtualBox modules automatically at boot time. For the modules to be loaded after installation, either reboot or load the modules once manually; the list of modules can be found in ,  or .

Among the kernel modules VirtualBox uses, there is a mandatory module named , which must be loaded before any virtual machines can run.

To load the module manually, run:

 # modprobe vboxdrv

The following modules are only required in advanced configurations:

*  and  are both needed when you intend to use the [https://www.virtualbox.org/manual/ch06.html#network_bridged bridged or host-only networking feature. More precisely,  is needed to create the host interface in the VirtualBox global preferences, and  is needed to launch a virtual machine using that network interface.

## Accessing host USB devices in guest
To use the USB ports of your host machine in your virtual machines, add users that will be authorized to use this feature to the  user group.

## Guest additions
It is also recommended to install the  package on the host running VirtualBox. This package will act as a disc image that can be used to install the guest additions onto guest systems other than Arch Linux. The .iso file will be located at , and may have to be mounted manually inside the virtual machine. Once mounted, you can run the guest additions installer inside the guest. For Arch Linux guest also see VirtualBox/Install Arch Linux as a guest#Install the Guest Additions.

## Extension pack
The Oracle VM VirtualBox Extension Pack provides additional features and is released under a non-free license only available for personal use. To install it, the  package is available, and a prebuilt version can be found in the seblu repository.

If you prefer to use the traditional and manual way: download the extension pack manually and install it via the GUI (File > Tools > Extension Pack Manager) or via , make sure you have a toolkit like Polkit to grant privileged access to VirtualBox. The installation of extension pack requires root access.

You can also install the extension pack without using Polkit via the following command:

 # vboxmanage extpack install path-to-extension-pack

One of the non-free extension pack features is support for the Remote Desktop Protocol (RDP). This part of functionality can also be obtained with the open source VNC Extension Pack, by installing the  package.

## Front-ends
VirtualBox comes with four front-ends:

* If you want to use VirtualBox with the regular GUI, use .
* If you want to launch and manage your virtual machines from the command-line, use the  command, which only provides a plain window for the virtual machine without any overlays.
* If you want to use VirtualBox without running any GUI (e.g. on a server), use the  command. With the VRDP extension you can still remotely access the displays of your virtual machines.
* If you want to remotely manage virtual machines, the VirtualBox web service () provides the server side backend. It can be used with RemoteBox (GUI) or phpVirtualBox (WebUI).

Refer to the VirtualBox manual to learn how to create virtual machines.

A security feature in Wayland (i.e. when using GDM) disallows VirtualBox to grab all keyboard input. This is annoying when you want to pass window manager shortcuts to your guest operating system. It can be bypassed by whitelisting VirtualBox:

 $ gsettings get org.gnome.mutter.wayland xwayland-grab-access-rules
 $ gsettings set org.gnome.mutter.wayland xwayland-grab-access-rules "Machine'"

The first command will show if any other applications are already whitelisted. If so, add VirtualBox Machine to that list, rather than having it as the only one.

## Installation steps for Arch Linux guests
See VirtualBox/Install Arch Linux as a guest.

## Virtual disks management
See also #Import/export VirtualBox virtual machines from/to other hypervisors.

## Formats supported by VirtualBox
VirtualBox supports the following virtual disk formats:

* VDI: The Virtual Disk Image is the VirtualBox own open container used by default when you create a virtual machine with VirtualBox.
* VMDK: The Virtual Machine Disk has been initially developed by VMware for their products. The specification was initially closed source, but has since become an open format which is fully supported by VirtualBox. This format offers the ability to be split into several 2GB files. This feature is especially useful if you want to store the virtual machine on machines which do not support very large files. Other formats, excluding the HDD format from Parallels, do not provide such an equivalent feature.
* VHD: The Virtual Hard Disk is the format used by Microsoft in Windows Virtual PC and Hyper-V. If you intend to use any of these Microsoft products, you will have to choose this format.
:
* VHDX (read only): This is the eXtended version of the Virtual Hard Disk format developed by Microsoft, which has been released on 2012-09-04 with Hyper-V 3.0 coming with Windows Server 2012. This new version of the disk format does offer enhanced performance (better block alignment), larger blocks size, and journal support which brings power failure resiliency. VirtualBox should support this format in read only.
* HDD (version 2): The HDD format is developed by Parallels Inc and used in their hypervisor solutions like Parallels Desktop for Mac. Newer versions of this format (i.e. 3 and 4) are not supported due to the lack of documentation for this proprietary format.
* QED: The QEMU Enhanced Disk format is an old file format for QEMU, another free and open source hypervisor. This format was designed from 2010 in a way to provide a superior alternative to QCOW2 and others. This format features a fully asynchronous I/O path, strong data integrity, backing files, and sparse files. QED format is supported only for compatibility with virtual machines created with old versions of QEMU.
* QCOW: The QEMU Copy On Write format is the current format for QEMU. The QCOW format does support zlib-based transparent compression and encryption (the latter is flawed and is not recommended). QCOW is available in two versions: QCOW and QCOW2. QCOW2 tends to supersede the first one. QCOW is currently fully supported by VirtualBox. QCOW2 comes in two revisions: QCOW2 0.10 and QCOW2 1.1 (which is the default when you create a virtual disk with QEMU). VirtualBox does not support QCOW2.
* OVF: The Open Virtualization Format is an open format which has been designed for interoperability and distributions of virtual machines between different hypervisors. VirtualBox supports all revisions of this format via the VBoxManage import/export feature but with known limitations.
* RAW: This is the mode when the virtual disk is exposed directly to the disk without being contained in a specific file format container. VirtualBox supports this feature in several ways: converting RAW disk to a specific format, or by cloning a disk to RAW, or by using directly a VMDK file which points to a physical disk or a simple file.

## Disk image format conversion
VBoxManage clonehd can be used to convert between VDI, VMDK, VHD and RAW.

 $ VBoxManage clonehd inputfile outputfile --format outputformat

For example to convert VDI to VMDK:

 $ VBoxManage clonehd source.vdi destination.vmdk --format VMDK

## QCOW
VirtualBox does not support QEMU's QCOW2 disk image format. To use a QCOW2 disk image with VirtualBox you therefore need to convert it, which you can do with . qemu-img can convert QCOW to / from VDI, VMDK, VHDX, RAW and various other formats (which you can see by running ).

 $ qemu-img convert -O output_fmt inputfile outputfile

For example to convert QCOW2 to VDI:

 $ qemu-img convert -O vdi source.qcow2 destination.vdi

There are two revisions of QCOW2: 0.10 and 1.1. You can specify the revision to use with .

## Mount virtual disks
## VDI
Mounting VDI images only works with fixed size images (a.k.a. static images); dynamic (dynamically size allocating) images are not easily mountable.

The offset of the partition (within the VDI) is needed, then add the value of  to  (e.g. 69632 + 32256 = 101888):

 $ VBoxManage internalcommands dumphdinfo storage.vdi | grep "offData"

The storage can now be mounted with:

 # mount -t ext4 -o rw,noatime,noexec,loop,offset=101888 storage.vdi /mntpoint/

For VDI disks with more partitions you can also use :

 # losetup -o $offData -Pf

After this you should find the partitions under  (e.g. ). Then you can mount them as usual (e.g. ).

You can also use mount.vdi script that, which you can use as (install script itself to ):

 # mount -t vdi -o fstype=ext4,rw,noatime,noexec vdi_file_location /mnt/

Alternately you can use the nbd kernel module and qemu-nbd from # modprobe nbd max_part=16
 # qemu-nbd -c /dev/nbd0 storage.vdi
 # mount /dev/nbd0p1 /mnt/dir/

And then to unmount:

 # umount /mnt/dir/
 # qemu-nbd -d /dev/nbd0

If the partition nodes are not propagated try using ; otherwise, a VDI partition can be mapped directly to a node by: .

## VHD
Like VDI, VHD images can be mounted with QEMU's nbd module:

 # modprobe nbd
 # qemu-nbd -c /dev/nbd0 storage.vhd
 # mount /dev/nbd0p1 /mnt

To unmount:

 # umount /mnt
 # qemu-nbd -d /dev/nbd0

## Compact virtual disks
Compacting virtual disks only works with .vdi files and basically consists of the following steps.

Boot your virtual machine and remove all bloat manually or by using cleaning tools like  which is [https://www.bleachbit.org/download/windows available for Windows systems too.

Wiping free space with zeroes can be achieved with several tools:

* If you were previously using Bleachbit, check the checkbox System > Free disk space in the GUI, or use  in CLI;
* On UNIX-based systems, by using :
:
:When  reaches the limit of the partition, you will get a message like . This means that all of the user-space and non-reserved blocks of the partition will be filled with zeros. Since cat reports this as error,  will remove the file afterward, freeing the space again.
:Using this command as root is important to make sure all free blocks have been overwritten. Indeed, by default, when using partitions with ext filesystem, a specified percentage of filesystem blocks is reserved for the super-user (see the  argument in the  man pages or use  to see how much space is reserved for root applications).

* On Windows, there are two tools available:
**  from the Sysinternals Suite, type , where you need to reexecute the command for each drive you have in your virtual machine;
** or, if you love scripts, there is a PowerShell solution, but which still needs to be repeated for all drives.
::
::

Once the free disk space have been wiped, shut down your virtual machine.

The next time you boot your virtual machine, it is recommended to do a filesystem check.

* On UNIX-based systems, you can use  manually;
** On GNU/Linux systems, and thus on Arch Linux, you can force a disk check at boot thanks to a kernel boot parameter;
* On Windows systems, you can use:
** either  where  needs to be replaced by each disk you need to scan and fix errors;
** or  from here which is basically the same software as , but without the need to repeat the command for all drives;

Now, remove the zeros from the .vdi file with VBoxManage modifyhd:

 $ VBoxManage modifyhd your_disk.vdi --compact

## TRIM
VirtualBox offers simulation of TRIM in VDI files via an experimental "discard" attachment option. This option is undocumented and can be accessed by commandline or .vbox file editing. When enabled, TRIM commands from the guest operating system causes the corresponding part of the VDI file to be compacted away.

## Increase virtual disks
## General procedure
If you are running out of space due to the small hard drive size you selected when you created your virtual machine, the solution adviced by the VirtualBox manual is to use VBoxManage modifyhd. However this command only works for VDI and VHD disks and only for the dynamically allocated variants. If you want to resize a fixed size virtual disk disk too, read on this trick which works either for a Windows or UNIX-like virtual machine.

First, create a new virtual disk next to the one you want to increase:

 $ VBoxManage createmedium disk -filename new.vdi --size 10000

where size is in MiB, in this example 10000MiB ~= 10GiB, and new.vdi is name of new hard drive to be created.

Next, the old virtual disk needs to be cloned to the new one which this may take some time:

 $ VBoxManage clonemedium disk old.vdi new.vdi --existing

Detach the old hard drive and attach new one, replace all mandatory italic arguments by your own:

 $ VBoxManage storageattach virtual_machine_name --storagectl SATA --port 0 --medium none
 $ VBoxManage storageattach virtual_machine_name --storagectl SATA --port 0 --medium new.vdi --type hdd

To get the storage controller name and the port number, you can use the command . Among the output you will get such a result (what you are looking for is in italic):

{{bc|
Storage Controller Name (0):            IDE
Storage Controller Type (0):            PIIX4
Storage Controller Instance Number (0): 0
Storage Controller Max Port Count (0):  2
Storage Controller Port Count (0):      2
Storage Controller Bootable (0):        on
Storage Controller Name (1):            SATA
Storage Controller Type (1):            IntelAhci
Storage Controller Instance Number (1): 0
Storage Controller Max Port Count (1):  30
Storage Controller Port Count (1):      1
Storage Controller Bootable (1):        on
IDE (1, 0): Empty
SATA (0, 0): /home/wget/IT/Virtual_machines/GNU_Linux_distributions/ArchLinux_x64_EFI/Snapshots/{6bb17af7-e8a2-4bbf-baac-fbba05ebd704}.vdi (UUID: 6bb17af7-e8a2-4bbf-baac-fbba05ebd704)
[...
}}

Download GParted live image and mount it as a virtual CD/DVD disk file, boot your virtual machine, increase/move your partitions, umount GParted live and reboot.

Finally, unregister the virtual disk from VirtualBox and remove the file:

 $ VBoxManage closemedium disk old.vdi
 $ rm old.vdi

## Increasing the size of VDI disks
If your disk is a VDI one, run:

 $ VBoxManage modifymedium disk your_virtual_disk.vdi --resize the_new_size

Then jump back to the Gparted step, to increase the size of the partition on the virtual disk.

## Replace a virtual disk manually from the .vbox file
If you think that editing a simple XML file is more convenient than playing with the GUI or with  and you want to replace (or add) a virtual disk to your virtual machine, in the .vbox configuration file corresponding to your virtual machine, simply replace the GUID, the file location and the format to your needs:

then in the  sub-tag of , replace the GUID by the new one.

## Transfer between Linux host and other operating system
The information about path to harddisks and the snapshots is stored between  tags in the file with the .vbox extension. You can edit them manually or use this script where you will need change only the path or use defaults, assumed that .vbox is in the same directory with a virtual harddisk and the snapshots folder. It will print out new configuration to stdout.

{{bc|1=
#!/bin/sh
NewPath="${PWD}/"
Snapshots="Snapshots/"
Filename="$1"

 awk -v SetPath="$NewPath" -v SnapPath="$Snapshots" '{if(index($0," Add... or use hotkeys  and then browse to .vbox'' file that contains configuration or use command line
}}

## Clone a virtual disk and assigning a new UUID to it
UUIDs are widely used by VirtualBox. Each virtual machines and each virtual disk of a virtual machine must have a different UUID. When you launch a virtual machine in VirtualBox, VirtualBox will keep track of all UUIDs of your virtual machine instance. See the VBoxManage list to list the items registered with VirtualBox.

If you cloned a virtual disk manually by copying the virtual disk file, you will need to assign a new UUID to the cloned virtual drive if you want to use the disk in the same virtual machine or even in another (if that one has already been opened, and thus registered, with VirtualBox).

You can use this command to assign a new UUID to a virtual disk:

 $ VBoxManage internalcommands sethduuid /path/to/disk.vdi

## Tips and tricks
## Import/export VirtualBox virtual machines from/to other hypervisors
If you plan to use your virtual machine on another hypervisor or want to import in VirtualBox a virtual machine created with another hypervisor, you might be interested in reading the following steps.

## Remove additions
Guest additions are available in most hypervisor solutions: VirtualBox comes with the Guest Additions, VMware with the VMware Tools, Parallels with the Parallels Tools, etc. These additional components are designed to be installed inside a virtual machine after the guest operating system has been installed. They consist of device drivers and system applications that optimize the guest operating system for better performance and usability by providing these features.

If you have installed the additions to your virtual machine, please uninstall them first. Your guest, especially if it is using an operating system from the Windows family, might behave weirdly, crash or even might not boot at all if you are still using the specific drivers in another hypervisor.

## Use the right virtual disk format
This step will depend on the ability to convert the virtual disk image directly or not.

## Automatic tools
Some companies provide tools which offer the ability to create virtual machines from a Windows or GNU/Linux operating system located either in a virtual machine or even in a native installation. With such a product, you do not need to apply this and the following steps and can stop reading here.

* Parallels Transporter which is non free, is a product from Parallels Inc. This solution basically consists in an piece of software called agent that will be installed in the guest you want to import/convert. Then, Parallels Transporter, which only works on OS X, will create a virtual machine from that agent which is contacted either by USB or Ethernet network.
* VMware vCenter Converter which is free upon registration on the VMware website, works nearly the same way as Parallels Transporter, but the piece of software that will gather the data to create the virtual machine only works on a Windows platform.

## Manual conversion
First, familiarize yourself with the formats supported by VirtualBox and those supported by third-party hypervisors.

* Importing or exporting a virtual machine from/to a VMware solution is not a problem at all if you use the VMDK or OVF disk format, otherwise converting VMDK to VDI and VDI to VMDK is possible and the aforementioned VMware vCenter Converter tool is available.
* Importing or exporting from/to QEMU is not a problem neither: some QEMU formats are supported directly by VirtualBox and conversion between QCOW2 to VDI and VDI to QCOW2 is still available if needed.
* Importing or exporting from/to Parallels hypervisor is the hardest way: Parallels does only support its own HDD format (even the standard and portable OVF format is not supported!).
:* To export your virtual machine to Parallels, you will need to use the Parallels Transporter tool described above.
:* To import your virtual machine to VirtualBox, you will need to use the VMware vCenter Converter described above to convert the virtual machine to the VMware format first. Then, apply the solution to migrate from VMware.

## Create the virtual machine configuration for your hypervisor
Each hypervisor have their own virtual machine configuration file: .vbox for VirtualBox, .vmx for VMware, a  file located in the virtual machine bundle (.pvm file), etc. You will have thus to recreate a new virtual machine in your new destination hypervisor and specify its hardware configuration as close as possible as your initial virtual machine.

Pay a close attention to the firmware interface (BIOS or UEFI) used to install the guest operating system. While an option is available to choose between these 2 interfaces on VirtualBox and on Parallels solutions, on VMware, you will have to add manually the following line to your .vmx file.

Finally, ask your hypervisor to use the existing virtual disk you have converted and launch the virtual machine.

## Virtual machine launch management
## Starting virtual machines with a service (autostart)
Find hereafter the implementation details of a systemd service that will be used to consider a virtual machine as a service.

Enable the  systemd unit in order to launch the virtual machine at next boot. To launch it directly, simply start the systemd unit.

VirtualBox 4.2 introduces a new way for UNIX-like systems to have virtual machines started automatically, other than using a systemd service.

## Starting virtual machines with a keyboard shortcut
It can be useful to start virtual machines directly with a keyboard shortcut instead of using the VirtualBox interface (GUI or CLI). For that, you can simply define key bindings in . Please refer to Xbindkeys for more details.

Example, using the  key of a laptop with an unused battery key ( on the computer used in this example):

 "VBoxManage startvm 'Windows 7'"
 m:0x0 + c:244
 XF86Battery

## Use specific device in the virtual machine
## Using USB webcam / microphone
# Make sure the virtual machine is not running and your webcam / microphone is not being used.
# Bring up the main VirtualBox window and go to settings for Arch machine. Go to USB section.
# Make sure Enable USB Controller is selected. Also make sure that Enable USB 2.0 (EHCI) Controller is selected too.
# Click the Add filter from device button (the cable with the + icon).
# Select your USB webcam/microphone device from the list.
# Now click OK and start your virtual machine.

## Detecting web-cams and other USB devices
If the device that you are looking for does not show up on any of the menus in the section above and you have tried all three USB controller options,
boot up your virtual machine three separate times. Once using the USB 1.1 controller, another using the USB 2.0 controller, etc. Leave the virtual machine running for at least 5 minutes after startup. Sometimes Windows will autodetect the device for you. Be sure you filter any devices that are not a keyboard or a mouse so they do not start up at boot. This ensures that Windows will detect the device at start-up.

## Access a guest server
To access Apache server on a Virtual Machine from the host machine only, simply execute the following lines on the host:

 $ VBoxManage setextradata GuestName "VBoxInternal/Devices/pcnet/0/LUN#0/Config/Apache/HostPort" 8888
 $ VBoxManage setextradata GuestName "VBoxInternal/Devices/pcnet/0/LUN#0/Config/Apache/GuestPort" 80
 $ VBoxManage setextradata GuestName "VBoxInternal/Devices/pcnet/0/LUN#0/Config/Apache/Protocol" TCP

where  is the port the host should listen on and  is the port the virtual machine will send Apache's signal on.

To use a port lower than 1024 on the host machine, changes need to be made to the firewall on that host machine. This can also be set up to work with SSH or any other services by changing "Apache" to the corresponding service and ports.

To communicate between the VirtualBox guest and host using ssh, the server port must be forwarded under Settings > Network. When connecting from the client/host, connect to the IP address of the client/host machine, as opposed to the connection of the other machine. This is because the connection will be made over a virtual adapter.

## D3D acceleration in Windows guests
Recent versions of VirtualBox have support for accelerating OpenGL inside guests. This can be enabled with a simple checkbox in the machine's settings, right below where video ram is set, and installing the VirtualBox guest additions. However, most Windows games use Direct3D (part of DirectX), not OpenGL, and are thus not helped by this method. However, it is possible to gain accelerated Direct3D in your Windows guests by borrowing the d3d libraries from Wine, which translate d3d calls into OpenGL, which is then accelerated. These libraries are now part of VirtualBox guest additions.

After enabling OpenGL acceleration as described above, reboot the guest into safe mode (press F8 before the Windows screen appears but after the VirtualBox screen disappears), and install VirtualBox guest additions, during install enable checkbox Direct3D support. Reboot back to normal mode and you should have accelerated Direct3D.

## VirtualBox on a USB key
When using VirtualBox on a USB key, for example to start an installed machine with an ISO image, you will manually have to create VMKDs from the existing drives. However, once the new VMDKs are saved and you move on to another machine, you may experience problems launching an appropriate machine again. To get rid of this issue, you can use the following script to launch VirtualBox. This script will clean up and unregister old VMDK files and it will create new, proper VMDKs for you:

{{bc|
#!/bin/sh
# Erase old VMDK entries
rm ~/.VirtualBox/*.vmdk

# Clean up VBox-Registry
sed -i '/sd/d' ~/.VirtualBox/VirtualBox.xml

# Remove old harddisks from existing machines
find ~/.VirtualBox/Machines -name \*.xml | while read -r file; do
  line=$(grep -e "type\=\"HardDisk\"" -n "$file" | cut -d ':' -f 1)
  if [ -n "$line" ]; then
    sed -i "${line}"d "$file"
    sed -i "${line}"d "$file"
    sed -i "${line}"d "$file"
  fi
  sed -i "/rg/d" "$file"
done

# Delete prev-files created by VirtualBox
find ~/.VirtualBox/Machines -name \*-prev -exec rm '{}' \;

# Recreate VMDKs
ls -l /dev/disk/by-uuid | cut -d ' ' -f 9,11 | while read -r ln; do
  if [ -n "$ln" ]; then
    uuid=$(echo "$ln" | cut -d ' ' -f 1)
    device=$(echo "$ln" | cut -d ' ' -f 2 | cut -d '/' -f 3 | cut -b 1-3)

    # determine whether drive is mounted already
    checkstr1=$(mount | grep "$uuid")
    checkstr2=$(mount | grep "$device")
    checkstr3=$(ls ~/.VirtualBox/*.vmdk | grep "$device")
    if [ -z "$checkstr1" ] && [ -z "$checkstr2" ] && [ -z "$checkstr3" ]; then
      VBoxManage internalcommands createrawvmdk -filename ~/.VirtualBox/"$device".vmdk -rawdisk /dev/"$device" -register
    fi
  fi
done

# Start VirtualBox
VirtualBox
}}

Note that your user has to be added to the "disk" group to create VMDKs out of existing drives.

## Run a native Arch Linux installation inside VirtualBox
If you have a dual boot system between Arch Linux and another operating system, it can become tedious to switch back and forth if you need to work in both. You may also experience performance or compatibility issues when using a virtual machine, which can impact your ability to do certain tasks.

This guide will let you reuse, in a virtual machine, your native Arch Linux installation when you are running your second operating system. This way, you keep the ability to run each operating system natively, but have the option to run your Arch Linux installation inside a virtual machine.

## Make sure you have a persistent naming scheme
Depending on your hard drive setup, device files representing your hard drives may appear differently when you will run your Arch Linux installation natively or in virtual machine. This problem occurs when using FakeRAID for example. The fake RAID device will be mapped in  when you run your GNU/Linux distribution natively, while the devices are still accessible separately. However, in your virtual machine, it can appear without any mapping in  for example, because the drivers controlling the fake RAID in your host operating system (e.g. Windows) are abstracting the fake RAID device.

To circumvent this problem, we will need to use an addressing scheme that is persistent to both systems. This can be achieved using UUIDs. Make sure your boot loader and fstab file is using UUIDs, otherwise fix this issue. Read fstab and Persistent block device naming.

## Make sure your mkinitcpio image is correct
Make sure your mkinitcpio configuration uses the HOOK :

If it is not present, add it and regenerate the initramfs.

## Create a virtual machine configuration to boot from the physical drive
## Create a raw disk VMDK image
Now, we need to create a new virtual machine which will use a RAW disk as virtual drive, for that we will use a ~ 1Kio VMDK file which will be mapped to a physical disk. Unfortunately, VirtualBox does not have this option in the GUI, so we will have to use the console and use an internal command of .

Boot the host which will use the Arch Linux virtual machine. The command will need to be adapted according to the host you have.

; On a GNU/Linux host:

There are 3 ways to achieve this: login as root, changing the access right of the device with , adding your user to the  group. The latter way is the more elegant, let us proceed that way:

 # gpasswd -a your_user disk

Apply the new group settings with:

 $ newgrp

Now, you can use the command:

 $ VBoxManage internalcommands createrawvmdk -filename /path/to/file.vmdk -rawdisk /dev/sdb -register

Adapt the above command to your need, especially the path and filename of the VMDK location and the raw disk location to map which contain your Arch Linux installation.

; On a Windows host:

Open a command prompt must be run as administrator.

On Windows, as the disk filename convention is different from UNIX, use this command to determine what drives you have in your Windows system and their location:

In this example, as the Windows convention is  where X is a number from 0,  could be analogous to  from the Linux disk terminology.

To use the  command on Windows, you can either, change the current directory to your VirtualBox installation folder first with

 # .\VBoxManage.exe internalcommands createrawvmdk -filename C:\file.vmdk -rawdisk \\.\PHYSICALDRIVE1

or use the absolute path name:

 # "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" internalcommands createrawvmdk -filename C:\file.vmdk -rawdisk \\.\PHYSICALDRIVE1

; On another operating system host:

There are other limitations regarding the aforementioned command when used in other operating systems like OS X, please thus read carefully the manual page, if you are concerned.

## Create the virtual machine configuration file
After, we need to create a new machine (replace the virtual_machine_name to your convenience) and register it with VirtualBox.

 $ VBoxManage createvm -name virtual_machine_name -register

Then, the newly raw disk needs to be attached to the machine. This will depend if your computer or actually the root of your native Arch Linux installation is on an IDE or a SATA controller.

If you need an IDE controller:

 $ VBoxManage storagectl virtual_machine_name --name "IDE Controller" --add ide
 $ VBoxManage storageattach virtual_machine_name --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium /path/to/file.vmdk

otherwise:

 $ VBoxManage storagectl virtual_machine_name --name "SATA Controller" --add sata
 $ VBoxManage storageattach virtual_machine_name --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium /path/to/file.vmdk

While you continue using the CLI, it is recommended to use the VirtualBox GUI, to personalise the virtual machine configuration. Indeed, you must specify its hardware configuration as close as possible as your native machine: turning on the 3D acceleration, increasing video memory, setting the network interface, etc.

Finally, you may want to seamlessly integrate your Arch Linux with your host operating system and allow copy pasting between both operating systems. Please refer to VirtualBox/Install Arch Linux as a guest#Install the Guest Additions for that, since this Arch Linux virtual machine is basically an Arch Linux guest.

{{Warning|For Xorg to work in natively and in the virtual machine, since obviously it will be using different drivers, it is best if there is no , so Xorg will pick up everything it needs on the fly. However, if you really do need your own Xorg configuration, maybe is it worth to set your default systemd target to  with  as root (more details at systemd#Targets and systemd#Change current target). In that way, the graphical interface is disabled (i.e. Xorg is not launched) and after you logged in, you can } manually with a custom .}}

## Install a native Arch Linux system from VirtualBox
In some cases it may be useful to install a native Arch Linux system while running another operating system: one way to accomplish this is to perform the installation through VirtualBox on a raw disk. If the existing operating system is Linux based, you may want to consider following Install from existing Linux instead.

This scenario is very similar to #Run a native Arch Linux installation inside VirtualBox, but will follow those steps in a different order: start by #Create a raw disk VMDK image, then #Create the virtual machine configuration file.

Now, you should have a working virtual machine configuration whose virtual VMDK disk is tied to a real disk. The installation process is exactly the same as the steps described in VirtualBox/Install Arch Linux as a guest, but #Make sure you have a persistent naming scheme and #Make sure your mkinitcpio image is correct.

After completing the installation, boot your computer natively with an GNU/Linux installation media (whether it be Arch Linux or not), chroot into your installed Arch Linux installation and install and configure a boot loader.

## Install MacOS guest
Before starting the virtual machine, run the following commands on the host machine $ VBoxManage modifyvm "MyMacVM" --cpuid-set 00000001 000106e5 00100800 0098e3fd bfebfbff
 $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/efi/0/Config/DmiSystemProduct" "iMac11,3"
 $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/efi/0/Config/DmiSystemVersion" "1.0"
 $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/efi/0/Config/DmiBoardProduct" "Iloveapple"
 $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/smc/0/Config/DeviceKey" "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"
 $ VBoxManage setextradata "MyMacVM" "VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC" 1
 $ VBoxManage setextradata "MyMacVM" VBoxInternal2/EfiGopMode 4

If you use an AMD processor and the first boot gets stuck, you also have to run

 $ VBoxManage modifyvm "MyMacVM" --cpu-profile "Intel Core i7-6700K"

## No keyboard/mouse input when attempting to install Mojave
If you are attempting to install Mojave, after doing the aforementioned steps, the installer will load up but you might not be able to send keyboard or mouse input. The reason seems to be that Mojave no longer supports the USB 1.1 controllers and in order to fix the issue you need to emulating USB 3.0. To do that first install the extension pack.

Then go to Machine > Settings > USB and select USB 3.0. Input should work from this point onwards.

## UEFI interactive shell after restart
If the installer is unable to properly format the bootable drive during installation and you end up in an UEFI shell, enter the following:

# Type  at the UEFI prompt
# Select Boot Maintenance Manager
# Select Boot From File

You will now be brought to couple of obscure PCI paths. The first one is the one that you just attempted to boot from and it did not work. The second (or third) one should be the one with the MacOS recovery partition that you need to load to continue the installation. Click the second Entry. If it is empty, press  to go back and select the third entry. Once you get one with folders click though the folders. It should be something like macOS Install Data > Locked Files > Boot Files > boot.efi. Once you click enter on the boot.efi you should boot into the MacOS installer and resume installation. Note that some of the subdirectories might be missing. Remember that you need to get to a .[https://superuser.com/questions/1235970/stuck-on-uefi-interactive-shell-with-mac-os-x-high-sierra-vm

## Move a native Windows installation to a virtual machine
If you want to migrate an existing native Windows installation to a virtual machine which will be used with VirtualBox on GNU/Linux, this use case is for you. This section only covers native Windows installation using the MSDOS/Intel partition scheme. Your Windows installation must reside on the first MBR partition for this operation to success. Operation for other partitions are available but have been untested (see #Known limitations for details).

A couple of tasks are required to be done inside your native Windows installation first, then on your GNU/Linux host.

## Tasks on Windows
The first three following points comes from this outdated VirtualBox wiki page, but are updated here.

* Remove IDE/ATA controllers checks (Windows XP only): Windows memorize the IDE/ATA drive controllers it has been installed on and will not boot if it detects these have changed. The solution proposed by Microsoft is to reuse the same controller or use one of the same serial, which is impossible to achieve since we are using a Virtual Machine. MergeIDE, a German tool, developped upon another other solution proposed by Microsoft can be used. That solution basically consists in taking all IDE/ATA controller drivers supported by Windows XP from the initial driver archive (the location is hard coded, or specify it as the first argument to the .bat script), installing them and registering them with the regedit database.
* Use the right type of Hardware Abstraction Layer (old 32 bits Windows versions): Microsoft ships 3 default versions:  (Standard PC),  (ACPI HAL) and  (ACPI HAL with IO APIC). Your Windows install could come installed with the first or the second version. In that way, please disable the Enable IO/APIC VirtualBox extended feature.
* Disable any AGP device driver (only outdated Windows versions): If you have the files  or  inside the  directory, remove it. As VirtualBox uses a PCI virtual graphics card, this can cause problems when this AGP driver is used.
* Create a Windows recovery disk: In the following steps, if things turn bad, you will need to repair your Windows installation. Make sure you have an install media at hand, or create one with Create a recovery disk from Vista SP1, Create a system repair disc on Windows 7 or Create a recovery drive on Windows 8.x).

## Using Disk2vhd to clone Windows partition
Boot into Windows, clean up the installation (with CCleaner for example), use disk2vhd tool to create a VHD image. Include a reserved system partition (if present) and the actual Windows partition (usually disk C:). The size of Disk2vhd-created image will be the sum of the actual files on the partition (used space), not the size of a whole partition. If all goes well, the image should just boot in a virtual machine and you will not have to go through the hassle with MBR and Windows boot loader, as in the case of cloning an entire partition.

## Tasks on GNU/Linux
* Reduce the native Windows partition size to the size Windows actually needs with  available from . The size you will specify will be the same size of the VDI that will be created in the next step. If this size is too low, you may break your Windows install and the latter might not boot at all.

:Use the  option first to run a test:
:

:If only the previous test succeeded, execute this command again, but this time without the aforementioned test flag.

* Install VirtualBox on your GNU/Linux host (see #Installation steps for Arch Linux hosts if your host is Arch Linux).

* Create the Windows disk image from the beginning of the drive to the end of the first partition where is located your Windows installation. Copying from the beginning of the disk is necessary because the MBR space at the beginning of the drive needs to be on the virtual drive along with the Windows partition. In this example two following partitions  and will be later removed from the partition table and the MBR boot loader will be updated.

:
:Using  will output the number of total sectors of the first partition of the disk . Adapt where necessary.

:
:We need to display the size in byte,  will convert the sector numbers to bytes.

* Since you created your disk image as root, set the right ownership to the virtual disk image:

* Create your virtual machine configuration file and use the virtual disk created previously as the main virtual hard disk.

* Try to boot your Windows virtual machine, it may just work. First though remove and repair disks from the boot process as it may interfere (and likely will) booting into safe-mode.

* Attempt to boot your Windows virtual machine in safe mode (press the F8 key before the Windows logo shows up)... if running into boot issues, read #Fix MBR and Microsoft boot loader. In safe-mode, drivers will be installed likely by the Windows plug-and-play detection mechanism view. Additionally, install the VirtualBox Guest Additions via the menu Devices > Insert Guest Additions CD image.... If a new disk dialog does not appear, navigate to the CD drive and start the installer manually.

* You should finally have a working Windows virtual machine. Do not forget to read the #Known limitations.

* Performance tip: according to VirtualBox manual, SATA controller has a better performance than IDE. If you cannot boot Windows off virtual SATA controller right away, it is probably due to the lack of SATA drivers. Attach virtual disk to IDE controller, create an empty SATA controller and boot the virtual machine - Windows should automatically install SATA drivers for the controller. You can then shutdown the virtual machine, detach virtual disk from IDE controller and attach it to SATA controller instead.

## Fix MBR and Microsoft boot loader
If your Windows virtual machine refuses to boot, you may need to apply the following modifications to your virtual machine.

* Boot a GNU/Live live distribution inside your virtual machine before Windows starts up.

* Remove other partitions entries from the virtual disk MBR. Indeed, since we copied the MBR and only the Windows partition, the entries of the other partitions are still present in the MBR, but the partitions are not available anymore. Use  to achieve this for example.
:

* Write the updated partition table to the disk (this will recreate the MBR) using the  command inside .

* Use  (see here for details) to add a generic MBR:
:

* With the new MBR and updated partition table, your Windows virtual machine should be able to boot. If you are still encountering issues, boot your Windows recovery disk from on of the previous step, and inside your Windows RE environment, execute the commands described here.

## Known limitations
* Your virtual machine can sometimes hang and overrun your RAM, this can be caused by conflicting drivers still installed inside your Windows virtual machine. Good luck to find them!
* Additional software expecting a given driver beneath may either not be disabled/uninstalled or needs to be uninstalled first as the drivers that are no longer available.
* Your Windows installation must reside on the first partition for the above process to work. If this requirement is not met, the process might be achieved too, but this had not been tested. This will require either copying the MBR and editing in hexadecimal see VirtualBox: booting cloned disk or will require to fix the partition table manually or by repairing Windows with the recovery disk you created in a previous step. Let us consider our Windows installation on the second partition; we will copy the MBR, then the second partition where to the disk image.  needs the total number of bytes that will be written: calculated thanks to the size of the MBR (the start of the first partition) plus the size of the second (Windows) partition. {{ic|{ dd if=/dev/sda bs=512 count=$(cat /sys/block/sda/sda1/start) ; dd if=/dev/sda2 bs=512 count=$(cat /sys/block/sda/sda2/size) ; } | VBoxManage convertfromraw stdin windows.vdi $(( ($(cat /sys/block/sda/sda1/start) + $(cat /sys/block/sda/sda2/size)) * 512 ))}}.

## Run a native Windows installation inside VirtualBox
In some cases, it is useful to be able to dual boot with Windows and access the partition in a virtual machine. This process is significantly different from #Move a native Windows installation to a virtual machine in several ways:

* The Windows partition is not copied to a virtual disk image. Instead, a raw VMDK file is created;
* Changes in the virtual machine will be mirrored in the partition, and vice versa;
* OEM licenses should still be satisfied, since the Windows partition still boots directly on the hardware.

## Creating the virtual machine
A VirtualBox virtual machine must be manually created. As of now do not add any storage device any disk to the virtual machine, it will be done manually later.

Configure the virtual machine with the following settings (settings panel can be opened by clicking the "Settings" button in the main toolbar):

* View: System:
** Tab: Motherboard:
*** mark Enable I/O APIC;
*** mark Enable EFI;
*** mark Hardware Clock in UTC Time if is your case.
** Tab: Processor:
*** mark Enable PAE/NX;
*** mark Enable Nested VT-x/AMD-V;
** Tab: Acceleration:
*** Choose the paravirtualization interface Hyper-V from the drop down menu;
*** mark Enable Nested Paging.

Optionally you can enable also the following settings:

* View: Display
** Tab: Screen
*** mark Enable 3D Acceleration. Note that it could cause glitches.

## Creating virtual machine disks
To access the Windows partitions, create a raw VMDK file pointing to the relevant Windows partitions (root privileges are required to read disk partition table):

 # VBoxManage createmedium disk -filename VM_DIRECTORY/windows.vmdk --format=VMDK --variant RawDisk --property RawDrive=DISK --property Partitions=RESERVED_PARTITION_NUMBER,BASIC_DATA_PARTITION_NUMBER

Replace capitalized placeholder strings as follow:

*  with the path of the virtual machine folder (usually a subdirectory of ;
*  must be replaced with the block device containing all the Windows partitions (e.g.:  or );
*  must be replaced with the number of partition labeled "Microsoft reserved partition" (e.g.: if the partition is the  the number will be );
*  must be replaced with the partition containing the Windows installation (e.g.: if the partition is the  the number will be );

Example:

 # VBoxManage createmedium disk -filename "/home/user/VirtualBox VMs/windows.vmdk" --format=VMDK --variant RawDisk --property RawDrive=/dev/nvme0n1 --property Partitions=2,3

The command will also create an extra file inside the virtual machine folder, "windows-pt.vmdk", that will be just ignored.

Now change the virtual disk owner to give access the user and group running VirtualBox.

Replace  and  with the user and the group that will run VirtualBox, which most likely will be your user.

## Allowing VirtualBox to read physical partitions
VirtualBox must have raw disk access in order to run a Windows partition. Normally, this would require VirtualBox to be run with full root privileges, but more elegant options are available.

## Higher security option: using a dedicated group for the Windows partitions
Here udev is configured to restrict the access to partitions Windows partitions to the vboxusers group, and then the user running VirtualBox is added to the group.

Assigning the disks to the vboxusers group can be done automatically by creating the following file:

{{hc|/etc/udev/rules.d/99-vbox.rules|
#
# Rules to give VirtualBox users raw access to Windows partitions
#

# Microsoft Reserved partition
SUBSYSTEM=="block", ENV{ID_PART_ENTRY_TYPE}=="e3c9e316-0b5c-4db8-817d-f92df00215ae", GROUP="vboxusers"

# Windows partition
SUBSYSTEM=="block", ENV{ID_PART_ENTRY_TYPE}=="ebd0a0a2-b9e5-4433-87c0-68b6b72699c7", GROUP="vboxusers"

#
# Rules to give VirtualBox users raw access to Windows disk
#

# sdb
ENV{ID_PART_TABLE_UUID}=="WINDOWS_DISK_ID_PART_TABLE_UUID", GROUP="vboxusers"
}}

 must be replaced with the value obtained from  (replace  with the disk containing Windows partitions). The UUIDs in these rules correspond to particular GPT partition types while the other capitalized strings are supposed to be written that way, so those does not have to be replaced.

Then the user running VirtualBox must be added to the vboxusers group. This can be done with the following command:

 # usermod -aG vboxusers VIRTUALBOX_RUNNING_USER

Replace  and with the user that will run VirtualBox, which most likely will be your user.

## Lower security option: using 'disk' group
To be able to add the VMDK file in VirtualBox Virtual Media Manager without running VirtualBox as root, the user running VirtualBox need to be in  and  groups.

Replace  and with the user that will run VirtualBox, which most likely will be your user.

## Setting up a separate EFI system partition
Virtual machine EFI boot files will refer to different disks than the ones in the physical EFI system partition, so VirtualBox must not make use of the latter but instead of an EFI system partition inside a dedicated virtual disk. This disk can be created with the following command:

 $ VBoxManage createmedium disk --filename VM_DIRECTORY/esp.vmdk --size 512 --format VMDK

Replace  with the folder containing the virtual machine being built.

## Adding virtual disks to the virtual machine
Configure the virtual machine storage devices (Settings panel - Storage) as following:

* add  as a SATA hard disk attached to the "SATA Port 0";
* add  as a SATA hard disk attached to the "SATA Port 1";
* mount Windows installation iso into the virtual optical drive .

## Configuring the virtual UEFI firmware and creating Windows boot files
Now start the virtual machine and it should automatically boot from Windows installation disk. After choosing the installation locales click on the "Repair your computer" link, then choose "Troubleshoot" and then " Command Prompt" in order to launch a command prompt from the install media.

Enter the following commands to create a new GPT table in the  disk and install the Windows boot loader onto it using configuration from the existing Windows partition:

Open Diskpart:

 X:\ diskpart

List all disks identified by the system:

 DISKPART> list disk

The  disk should be labeled as  due to the fact that was attached to the SATA port 0, ~512 MiB in size and unpartitioned. The  disk should be labeled as ; note that the column "Size" displays the disk size, not the partition one.

Select the  disk:

 DISKPART> select Disk 0

Now create a GPT partition table, an EFI system partition, big as the whole disk, and assign to it a label and drive letter:

Check that the partition has been correctly created:

 DISKPART> list volume

Our newly created EFI system partition will be labeled as "SYSTEM" with letter as "S".

Take note of the Windows installation volume letter because it will be used in next steps. Usually its  but it could be different: you can infer it from its label and its size. The size is the same as the Windows installation partition size on your physical hard disk.

Exit diskpart:

 DISKPART> exit

Install the Windows boot loader into the EFI system partition.

Now close the command prompt, power off the virtual machine and detach the Windows installation disk (from "Preferences > Devices" remove the optical disk). The virtual machine should now boot from the newly installed boot partition and load the physical Windows installation. It may show some UEFI related errors on the top of the virtual machine window and the first boot may take a while, but if everything has been done correctly you will be able to access your windows installation.

## Run an entire physical disk in VirtualBox
This works the same way as #Run a native Windows installation inside VirtualBox but the vmdk will contain the entire disk rather than one partition, and so you will not need to create a separate ESP or MBR partition as the one in the physical disk will be used.

Create the raw disk:

 # VBoxManage internalcommands createrawvmdk -filename /path/to/file.vmdk -rawdisk /dev/sdb

Then follow the same method as in #Run a native Windows installation inside VirtualBox for the configuration and virtual disk attachement.

## Set guest starting resolution
Typically after installing Guest Additions, a fullscreen Arch guest running X will be set to the optimal resolution for your display; however, the virtual console's framebuffer will be set to a standard, often smaller, resolution detected from VirtualBox's custom VESA driver.

To use the virtual consoles at optimal resolution, Arch needs to recognize that resolution as valid, which in turn requires VirtualBox to pass this information along to the guest OS.

First, check if your desired resolution is not already recognized by running the command ( need to be installed):

 hwinfo --framebuffer

If the optimal resolution does not show up, then you will need to run the  tool on the host machine and add "extra resolutions" to your virtual machine (on a Windows host, go to the VirtualBox installation directory to find ). For example:

 $ VBoxManage setextradata "Arch Linux" "CustomVideoMode1" "1360x768x24"

The parameters "Arch Linux" and "1360x768x24" in the example above should be replaced with your virtual machine name and the desired framebuffer resolution. Incidentally, this command allows for defining up to 16 extra resolutions ("CustomVideoMode1" through "CustomVideoMode16"). Recommended resolutions are 1280x720, 1920x1080, 2048x1080, 2560x1440, 3840x2160, 1280x800, 1280x1024, 1440x900, 1600x900.

Afterwards, restart the virtual machine and run  once more to verify that the new resolutions have been recognized by your guest system (which does not guarantee they will all work, depending on your hardware limitations).

Finally, add a  kernel parameter to set the framebuffer to the new resolution, for example:

 video=1360x768

Additionally you may want to configure your boot loader to use the same resolution. If you use GRUB, see GRUB/Tips and tricks#Setting the framebuffer resolution.

## SSH from host to guest
The Network tab of the virtual machine settings contains a Port Forwarding tool. It is possible to use it to forward the Guest SSH port  to a Host port, e.g. . Afterwards, you can connect to the guest from the host via the specified host port:

 ssh -p 60022 user@localhost

## SSHFS as alternative to shared folders
Using this port forwarding and SSHFS it is straightforward to mount the Guest filesystem onto the Host one:

 [user@host$ sshfs -p 60022 user@localhost:$HOME ~/shared_folder

and then transfer files between both.

## Specify Host-Only Network
For security reasons, the VirtualBox network driver limits the usable subnet ranges. This will cause  errors when changing the virtual network adapter settingsYou can change the allowed list of networks by creating  and adding the network subnets to it. For example:

For IPv6 it is best practice to generate a new, randomized [https://datatracker.ietf.org/doc/html/rfc4193 ULA prefix.

Do not forget to reload the driver and restart VirtualBox after changing :

 # modprobe -r vboxnetadp vboxnetflt
 # modprobe vboxnetadp vboxnetflt

## Troubleshooting
## Keyboard and mouse are locked into virtual machine
This means your virtual machine has captured the input of your keyboard and your mouse. Simply press the right  key and your input should control your host again.

To control transparently your virtual machine with your mouse going back and forth your host, without having to press any key, and thus have a seamless integration, install the guest additions inside the guest. Read from VirtualBox/Install Arch Linux as a guest#Install the Guest Additions if your guest is Arch Linux, otherwise read the official VirtualBox help.

## No 64-bit operating system client options
When launching a virtual machine client, and no 64-bit options are available, make sure your CPU virtualization capabilities (usually named ) are enabled in the BIOS.

If you are using a Windows host, you may need to disable Hyper-V, as it prevents VirtualBox from using VT-x. === VirtualBox GUI does not match host GTK theme ===

See Uniform look for Qt and GTK applications for information about theming Qt-based applications like VirtualBox.

## Cannot send Ctrl+Alt+Fn to guest
Your guest operating system is a GNU/Linux distribution and you want to open a new TTY shell by hitting  or exit your current X session with . If you type these keyboard shortcuts without any adaptation, the guest will not receive any input and the host (if it is a GNU/Linux distribution too) will intercept these shortcut keys. To send  to the guest for example, simply hit your Host Key (usually the right  key) and press  simultaneously.

## USB modem not working on host
If you have a USB modem which is being used by the guest operating system, killing the guest operating system can cause the modem to become unusable by the host system. Killing and restarting  should fix this problem.

## USB device crashes guest
If attaching a USB device to the guest causes a crash or any other erroneous behavior, try switching the USB controller from USB 2 (EHCI) to USB 3 (xHCI) or vice versa.

## Host freezes on virtual machine start
Generally, such issues are observed after upgrading VirtualBox or Linux kernel. Downgrading them to the previous versions of theirs might solve the problem.

## Analog microphone not working
If the audio input from an analog microphone is working correctly on the host, but no sound seems to get through to the guest, despite the microphone device apparently being detected normally, installing a sound server such as PulseAudio on the host might fix the problem.

If after installing PulseAudio the microphone still refuses to work, setting Host Audio Driver (under VirtualBox > Machine > Settings > Audio) to ALSA Audio Driver might help.

## Problems with images converted to ISO
Some image formats cannot be reliably converted to ISO. For instance,  ignores .ccd and .sub files, which can result in disk images with broken files.

In this case, you will either have to use CDemu for Linux inside VirtualBox or any other utility used to mount disk images.

## Failed to create the host-only network interface
Make sure all required kernel modules are loaded. See #Load the VirtualBox kernel modules.

If all required kernel modules are loaded and you are still unable to create the host-only adapter, navigate to File > Host Network Manager and click the Create button to add the network interface.

## Failed to insert module
When you get the following error when trying to load modules:

 Failed to insert 'vboxdrv': Required key not available

Sign your modules or disable  in your kernel config.

## VBOX_E_INVALID_OBJECT_STATE (0x80BB0007)
This can occur if a virtual machine is exited ungracefully. Run the following command:

 $ VBoxManage controlvm virtual_machine_name poweroff

## NS_ERROR_FAILURE and missing menu items
This error might appear if extension pack has not been updated and becomes incompatible with a newly released VirtualBox version.

This error also happens sometimes when selecting QCOW/QCOW2/QED disk format when creating a new virtual disk.

If you encounter this message the first time you start the virtual machine:

Exit VirtualBox, delete all files of the new machine and from VirtualBox configuration file remove the last line in  menu (or the offending machine you are creating):

## OpenBSD unusable when virtualisation instructions unavailable
While OpenBSD is reported to work fine on other hypervisors without virtualisation instructions (VT-x AMD-V) enabled, an OpenBSD virtual machine running on VirtualBox without these instructions will be unusable, manifesting with a bunch of segmentation faults. Starting VirtualBox with the -norawr0 argument [https://www.virtualbox.org/ticket/3947 may solve the problem. You can do it like this:

 $ VBoxSDL -norawr0 -vm name_of_OpenBSD_virtual_machine

## Windows: "The specified path does not exist. Check the path and then try again."
This error message may appear when running an .exe file which requires administrator privileges from a shared folder in windows guests. As a workaround, copy the file to the virtual drive or use UNC paths (). See [https://support.microsoft.com/de-de/help/2019185/copying-files-from-a-mapped-drive-to-a-local-directory-fails-with-erro for more information.

## Windows 8.x error code 0x000000C4
If you get this error code while booting, even if you choose operating system type Win 8, try to enable the  CPU instruction:

 $ vboxmanage setextradata virtual_machine_name VBoxInternal/CPUM/CMPXCHG16B 1

## Windows 8, 8.1 or 10 fails to install, boot or has error "ERR_DISK_FULL"
Update the virtual machine's settings by going to Settings > Storage > Controller:SATA and check Use Host I/O Cache.

## WinXP: Bit-depth cannot be greater than 16
If you are running at 16-bit color depth, then the icons may appear fuzzy/choppy. However, upon attempting to change the color depth to a higher level, the system may restrict you to a lower resolution or simply not enable you to change the depth at all. To fix this, run  in Windows and add the following key to the Windows XP virtual machine's registry:

 NT\Terminal Services
 "ColorDepth"=dword:00000004

Then update the color depth in the "desktop properties" window. If nothing happens, force the screen to redraw through some method (i.e.  to redraw/enter full screen).

## Windows: Screen flicker if 3D acceleration enabled
VirtualBox > 4.3.14 has a regression in which Windows guests with 3D acceleration flicker. Since r120678 a patch has been implemented to recognize an environment variable setting, launch VirtualBox like this:

 $ CR_RENDER_FORCE_PRESENT_MAIN_THREAD=0 VirtualBox

Make sure no VirtualBox services are still running. See VirtualBox bug 13653.

## Cannot launch VirtualBox with Wayland: Segmentation fault
This problem is caused by Qt detecting Wayland (e.g., if ), while VirtualBox does not work on Wayland yet. See  and the upstream bug.

The Qt platform detection can be disabled and X11 forced over Wayland by setting the environment variable .
To not affect the other Qt applications (which usually work well with Wayland),  should only be set when launching VirtualBox.

If starting through the desktop entry, follow the instructions in Desktop entries#Modify environment variables and change the lines starting with  to . If starting from the shell, alias (Bash#Aliases)  to .

## Random freezing in guests with Intel GPU
With Intel CPU and graphics, allocating more processors for the guest can lower render performance, thus cause random freezing. Allocating less processors can help.

## Unable to view desktop in fullscreen mode
Disable the Mini Toolbar by selecting Machine > Settings, select the User Interface tab and uncheck the Mini Toolbar checkbox

## Random crashes with Windows 10 guest operating system with Intel Tiger Lake chipset
Disable split lock detection by adding  to the kernel parameters.

Details are described in VirtualBox's Ticket #20180.

## Failed to save the settings when enabling Secure Boot
In VirtualBox 7.0.0, enabling Secure Boot in a virtual machine that was created in a previous VirtualBox version will fail with a nondescript error ():

 Failed to save the settings.

The solution is to click the Reset Keys to Default button right below the Enable Secure Boot checkbox.

## Failed to start VirtualBox machine after using Android Studio emulator
KVM and VirtualBox kernel modules can be loaded but not used simultaneously. Android Studio emulator is a QEMU emulator, which uses KVM for acceleration. So Android Studio emulator and VirtualBox machine (if hardware acceleration is enabled) cannot run at the same time. We have to use one after the other stopped completely.

Sometimes, VirtualBox kernel module can still be used unexpectedly by some process, and keep all VirtualBox machines failing to start, the error message on VirtualBox GUI is "A critical error has occurred".

At this time, we can check and reload VirtualBox kernel modules using  as root. If it saying some modules is still be in use, you need to manually kill related process and rerun the command.

## 3D Acceleration is not working
* Make sure guest additions are installed on guest, and the host modules are installed on the host
* Make sure the guest additions and host kernel modules versions match
** host:
** guest: open logs of your VM, find "Guest Additions information report"
* Make sure vulkan is installed and working on the host

## VirtualBox UI elements are improperly rendered with Kvantum installed
On some configurations of Kvantum () with third party themes, some UI elements such as toolbars and menus are rendered black or improperly. This seems to be limited to translucent windows being enabled. See Kvantum's issue #418.

To fix this behavior, do one of:

* Disable Translucent windows under section Configure Active Theme > Compositing & General Look of Kvantum Manager.
* Add  in Kvantum Manager, to the Configure Active Theme > Compositing & General Look > Opaque apps: menu field.
** This makes an exception for virtualbox windows to be ignored.

## VirtualBox is taking exclusive control of an audio device, preventing PipeWire from accessing it while the virtual machine is running
By default, VirtualBox should auto-select the best audio driver. However, on PipeWire systems this often falls back to ALSA (see Pipewire issue).

It could cause journal records like these:

 pipewirespa.audioadapter: params Spa:Enum:ParamId:EnumFormat: 1:0 (convert format) Device or reso>
 pipewire[2370: pw.node: (alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__Speaker__sink-6>
 pipewirespa.alsa: '_ucm0001.hw:sofhdadsp': playback open failed: Device or resource busy

The solution is to configure VirtualBox to use the PulseAudio backend (which PipeWire will handle via pipewire-pulse):

 $ VBoxManage modifyvm virtual_machine_name --audio-driver pulse --audio-controller hda
