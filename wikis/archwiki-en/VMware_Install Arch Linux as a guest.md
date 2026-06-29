# VMware/Install Arch Linux as a guest

This article is about installing Arch Linux in a VMware product, such as Workstation Player, Fusion or Workstation Pro.

## In-kernel drivers
* - The physical memory management driver. It acts like a "balloon" that can be inflated to reclaim physical pages by reserving them in the guest and invalidating them in the monitor, freeing up the underlying machine pages so they can be allocated to other guests. It can also be deflated to allow the guest to use more physical memory. Deallocated Virtual Machine memory can be reused in the host without terminating the guest.
* - For VMware's Paravirtual SCSI (PVSCSI) HBA.
* - The Virtual Machine Communication Interface. It enables high-speed communication between host and guest in a virtual environment via the VMCI virtual device.
* - For 3D acceleration. This is a KMS enabled DRM driver for the VMware SVGA2 virtual hardware.
* - For VMware's vmxnet3 virtual ethernet NIC.
* a fuse-based hgfs implementation has been added to  10.0+ and is supported from kernel version 4.0+.
The following drivers are only needed if you are running Arch Linux on a hypervisor like VMware vSphere Hypervisor. Client-server applications can write to the VMCI Sock (vsock) interface to make use of the VMCI virtual device, when communicating between virtual machines.
* - The Virtual Socket Protocol. It is similar to the TCP/IP socket protocol, allowing communication between Virtual Machines and hypervisor or host.
* - Implements a VMCI transport for Virtual Sockets.

Some modules, such as the legacy  shared folder module, will require additional work to manually  and systemd  in order to function properly.

## VMware Tools versus Open-VM-Tools
In 2007, VMware released large portions of the VMware Tools under the LGPL as Open-VM-Tools. The official Tools are not available separately for Arch Linux.

Originally, VMware Tools provided the best drivers for network and storage, combined with the functionality for other features such as time synchronization. However, now the drivers for the network/SCSI adapter are part of the Linux kernel.

The official VMware Tools also had the advantage of being able to use the Unity mode feature, but as of VMWare Workstation 12, Unity mode for Linux guests has been removed due to lack of use and developer difficulties in maintaining the feature. See this thread.

## Open-VM-Tools
## Utilities
The  package comes with the following utilities:

*  - Service responsible for the Virtual Machine status report.
*  - Tool to check whether a program is running in the guest.
*  - Tool to obtain Virtual Machine information of the host.
*  - Tool to enable clipboard sharing (copy/paste) between host and guest.
*  - Filesystem utility. Enables drag & drop functionality between host and guest through FUSE (Filesystem in Userspace).
*  - Dumps logging/debugging information to the Virtual Machine logfile.
*  - Utility for mounting vmhgfs shared folders.

## Installation
Install . Start and/or enable  and .

Try to install  manually if copy and paste between host and guest does not work properly.

## Official VMware Tools
## Modules
* - Filesystem driver. Enables drag & drop functionality between host and guest (superseded by the  utility).
* - High performance communication interface between host and guest.
* - Virtual Machine Monitor.
* - Networking driver.
* - VMCI sockets.

## Installation (from guest)
Install the dependencies:  (for building),  (for , used by the installer) and  (for kernel headers). In order to check out  you will need  from the  package.

Then, create bogus init directories for the installer:

 # for x in {0..6}; do mkdir -p /etc/init.d/rc${x}.d; done

The installer can then be mounted:

 # mount /dev/cdrom /mnt

Extracted (e.g. to ):

 # tar xf /mnt/VMwareTools*.tar.gz -C /root

And started:

 # perl /root/vmware-tools-distrib/vmware-install.pl

The following build failures can safely be ignored:

* VMNEXT 3 virtual network card
* "Warning: This script could not find mkinitrd or update-initramfs and cannot remake the initrd file!"
* Fuse components not found on the system.

Enable  systemd services (make sure the dependencies are manually installed, or that the  flag) used. The  source code should be checked out using the Arch build system.

  $ pkgctl repo clone open-vm-tools
  $ cd open-vm-tools
  $ makepkg -s --asdeps
  # cp vm* /usr/lib/systemd/system

Enable  and .

Reboot the Virtual Machine.

Log in and start the VMware Tools:

 # /etc/init.d/rc6.d/K99vmware-tools start

Additionally, to auto start  on boot, create a new file :

And enable the new .

## Xorg configuration
Install the dependencies:  and .

These packages should be all that are required to get started with booting into a : .  will get started which will set up most of what is needed to work with the Virtual Machine.

However, if booting into  or using an uncommon setup (e.g. multiple monitors), then  needs to be enabled. In addition to this, run Xorg as root to give permission for loading drivers.

## Tips and tricks
## Shared Folders with vmhgfs-fuse
Share a folder by selecting Edit virtual machine settings > Options > Shared Folders > Always enabled, and creating a new share.

The shared folders should be visible with:

 $ vmware-hgfsclient

Now the folder can be mounted:

 # mkdir
 # vmhgfs-fuse -o allow_other -o auto_unmount .host:/' '

If the error message  is displayed, uncomment the following line in :
 user_allow_other

Other  mount options can be viewed by using the  input flag:

 # vmhgfs-fuse -h

## fstab
Add a rule for each share:

Create and mount the Shared Folders (if not done so already):

 # mkdir ''''
 # mount ''''

## systemd
Create the following :

Ensure the  folder exists on the system. If this folder does not exist then it must be created, as the systemd service depends on it:

 # mkdir -p ''''

Enable the  mount target.

If all shared folders should be mounted automatically then omit ''''.

## Legacy Shared Folders with vmhgfs module
Share a folder by selecting Edit virtual machine settings > Options > Shared Folders > Always enabled, and creating a new share.

Ensure the  driver is loaded:

 # modprobe vmhgfs

The shared folders should be viewable with:

 $ vmware-hgfsclient

Now the folder can be mounted:

 # mkdir /home/user1/shares
 # mount -n -t vmhgfs .host:/'''' /home/user1/shares

## Enable at boot
Edit  thusly:

and then regenerate the initramfs.

## fstab
Add a rule for each share:

Create and mount the Shared Folders:

 # mkdir /home/user1/shares
 # mount /home/user1/shares

## systemd
For shared folders to work the  driver must be loaded. Create the following s:

Ensure the  folder exists on the system. If this folder does not exist then it must be created, as the systemd scripts depend on it:

 # mkdir -p ''''

Enable the  mount target.

If all shared folders should be mounted automatically then omit ''''.

## Prune locate DB
When using locate, it is pointless to index the shared directories in the . Therefore, add the directories to  in .

## 3D Acceleration
If not selected at guest creation time, 3D Acceleration can be enabled in: Edit virtual machine settings > Hardware > Display > Accelerate 3D graphics.

## OpenGL and GLSL support
It is possible to update OpenGL and GLSL with new kernel modules, overriding Arch-controlled versions.

Currently, OpenGL 3.3 and GLSL 3.30 can be supported.  See https://bbs.archlinux.org/viewtopic.php?id=202713 for more details.

## Time synchronization
Configuring time synchronization in a Virtual Machine is important; fluctuations are bound to occur more easily in a guest VM. This is mostly due to the CPU being shared by more than one guest.

There are 2 options to set up time synchronization: the host or an external source.

## Host machine as time source
To use the host as a time source, ensure  is started. Then enable the time synchronization:

 # vmware-toolbox-cmd timesync enable

To synchronize the guest after suspending the host:

 # hwclock --hctosys --localtime

## External server as time source
See NTP.

## Troubleshooting
## Network slow on guest
Arch Linux, as well as other Linux guests, may have slow network speeds while using NAT. To resolve this, switch the network type to Bridged mode in the guest settings on the host, changing the configuration file for the network on the guest where necessary. For more information on configuration, see Network configuration. If on a Windows host and it is not connecting properly despite correct guest configuration, open the Virtual Network Editor on the host as Administrator and press the Restore defaults button at the bottom left.

## Sound problems
If unacceptably loud or annoying sounds occur, then it may be related to the PC speaker. The issue may be resolved by disabling the PC speaker within the guest image.

## Audio and Video stuttering problems
In virtual machines, audio and video stuttering, crackling, or lag can occur, affecting playback in applications like Firefox and system notifications. This issue is often linked to the PipeWire audio backend and emulated drivers. Adjusting ALSA ringbuffer settings or PipeWire configurations can help resolve these glitches.

For detailed steps on troubleshooting and fixing these issues, see Audio and Video stuttering/crackling

## Mouse problems
The following problems may occur with the mouse:

* The automatic grab/ungrab feature does not automatically grab input when the cursor enters the window
* Missing buttons
* Input lag
* Clicks are not registered in some applications
* Mouse cursor jumps when entering/leaving virtual machine
* Mouse position jumps to where it left the guest virtual machine

These may be fixed by uninstalling the  package.  and  should be sufficient for handling mouse and keyboard inputs.

Adding settings to the  configuration file may help (Mouse position jumps to where it left the guest VM):

VMware also attempts to automatically optimize the mouse for gaming. If problems are experienced, disabling the optimization is recommended: Edit > Preferences > Input > Optimize mouse for games: Never

Alternatively, attempting to disable the  event in  may be required:

## Boot problems
## Slow boot time
The following errors may be displayed if VMWare's memory hot-add feature is enabled:

*add_memory failed
*acpi_memory_enable_device() error

Disable the memory hot-add feature by setting  to the .

## Shutdown/Reboot hangs
Adjust the timeout for the vmtoolsd service (defaults to 90 seconds).

## Window resolution autofit problems
"Autofit" means that when the VMWare window's size is adjusted in the host, Arch Linux in the guest should automatically follow and readjust its resolution to fit the new size of the host window.

## Potential solution 1
Ensure autofit is enabled. For VMware Workstation the setting can be found in: View -> Autosize -> Autofit Guest

## Potential solution 2
For some reason, autofit requires that the packages  and , are installed. Hence ensure that those two packages are installed on the guest. If X windows is not installed or a non–GTK-based desktop environment (such as KDE) is being used, these packages might have to be installed independently.

## Potential solution 3
The relevant modules may have to be added to mkinitcpio.conf:

Do not forget to regenerate the initramfs.

## Potential solution 4
Enable .

If this does not work, ensure the  is restarted.

## Potential solution 5
If GNOME is running on Wayland, install  ().

See ==== Potential solution 6 ====

Make sure that Stretch Mode is disabled. Follow VM > Settings > Display > Display Scaling and untick the option Stretch mode.

## Potential solution 7
Manually set the resolution using the  option in the kernel command line.

## Drag and drop, copy/paste
The drag-and-drop (copy/paste) feature requires both  and  packages to be installed.

Make the command  run after X11 by either:

* Ensuring  exists, and if not, running:
 # cp /etc/vmware-tools/vmware-user.desktop /etc/xdg/autostart/vmware-user.desktop
or
* Add  to Xinitrc.

Copy/paste [https://github.com/vmware/open-vm-tools/issues/443 does not currently work on Wayland, though applications running through Xwayland work fine.

With upgrade of VMWorkstation to version 17.6.2 copy/paste again silently stopped working. Adding the lines

 keyboard.allowBothIRQs = "FALSE"
 keyboard.vusb.enable = "TRUE"

to the VMX file solved the problem.

## Problems when running as a shared virtual machine on Workstation 11
Workstation 11 has a bug where vmware-hostd crashes if an Arch guest is running as a shared virtual machine and vmtoolsd is running in the guest.  A patch to open-vm-tools to work around the bug is here.

## Virtual Network Editor Wayland
When running VMWare workstation on a Wayland host, the Virtual Network Editor will not launch. See Privilege elevation for graphical applications#Wayland for the reason and the possible solutions.
