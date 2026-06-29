# VMware

This article is about the latest major VMware versions, meaning VMware Workstation Pro and Player 17, 16, 15, 14 and 12.5.

You may also be interested in /Install Arch Linux as a guest.

## Installation
Install the  package.

It is also necessary to install the appropriate headers package(s) for your installed kernel(s): for example  or .

Start  first to generate .

Then, as desired, enable some of the following services:

*  for guest network access (otherwise you will get an error  and you will not be able to use vmware-netcfg)
*  for connecting USB devices to guest
*  for sharing virtual machines (not available since version 16)

Lastly, load the VMware modules:

 # modprobe -a vmw_vmci vmmon

If it loads for too long without response, try #Cannot load module vmmon.

## Usage
To open VMware Workstation Pro:

 $ vmware

or Player:

 $ vmplayer

## Tips and tricks
## Entering the Workstation Pro license key
## From terminal
 # /usr/lib/vmware/bin/vmware-vmx-debug --new-sn XXXXX-XXXXX-XXXXX-XXXXX-XXXXX

Where  is your license key.

## From GUI
If the above does not work, you can try:

 # /usr/lib/vmware/bin/vmware-enter-serial

## Extracting the VMware BIOS
 $ objcopy /usr/lib/vmware/bin/vmware-vmx -O binary -j bios440 --set-section-flags bios440=a bios440.rom.Z
 $ perl -e 'use Compress::Zlib; my $v; read STDIN, $v, '$(stat -c%s "./bios440.rom.Z")'; $v = uncompress($v); print $v;'  bios440.rom

## Extracting the installer
To view the contents of the installer :

 $ sh VMware-edition-version.release.architecture.bundle --extract /tmp/vmware-bundle/

## Using the modified BIOS
If and when you decide to modify the extracted BIOS you can make your virtual machine use it by moving it to :

 $ mv bios440.rom ~/vmware/Virtual_machine_name/

then adding the name to the  file:

## Enable 3D graphics on Intel, Optimus and AMD
Some graphics drivers are blacklisted by default, due to poor and/or unstable 3D acceleration. After enabling Accelerate 3D graphics, the log may show something like:

 Disabling 3D on this host due to presence of Mesa DRI driver.  Set mks.gl.allowBlacklistedDrivers = TRUE to override.

The configuration file where you can set this setting is .

VMware Workstation 16.2 switched from OpenGL to Vulkan, so the setting is a bit different. If your driver is unsupported, you might see a message like this in the log:

 mks Vulkan Renderer: Only the AMDVLK driver is supported at this time.
 mks Vulkan Renderer: No supported Vulkan device/driver found (See mks.vk.allowUnsupportedDevices or mks.vk.forceDevice configuration options).

If your Vulkan driver is blacklisted, you might have to add  to  or switch to a supported driver - check  in the VM's directory if unsure.

When using Vulkan with multiple graphics adapters (GPUs) a specific device can be chosen by examining  to retrieve the correct adapter string then placing it into the VM's  file.  Example from :

 mks Vulkan Renderer: Name: 'AMD Radeon RX 570 Series (RADV POLARIS10)'

Then to the VM's  file we would add:

 mks.vk.ForceDevice = "AMD Radeon RX 570 Series (RADV POLARIS10)"

## Suspend virtual machines before host suspend/hibernate
Create an executable file:

{{hc|/usr/lib/systemd/system-sleep/vmware_suspend_all.sh|
#!/bin/bash

set -eu

if  $# -ne 2 ; then
    echo "Usage: $0  "
    exit 1
fi

period=$1
action=$2

echo "vmware system-sleep hook argv: ${period} ${action}"

if ! command -v vmrun &>/dev/null; then
    echo "command not found: vmrun"
fi

if  "${period}" = "pre" ; then
    readarray -t vms  /sys/kernel/mm/transparent_hugepage/enabled

To make the change persistent across boots, add the kernel parameter .

You can also use  instead of  to still allow applications that are optimized for transparent hugepages to obtain the performance benefitsThis does the same for vmware as above.

## Ensure direct RAM access
By default, VMware writes a running guest system's RAM to a file on disk. If you are certain you have enough spare memory, you can ensure the guest OS writes its memory directly to the host's RAM by adding the following to the VM's :

## Choppy/Slow Chromium Browser Graphics in VM Guests
Browse to  and enable "Override software rendering list" then restart the browser.

## Performance tips
To improve the performance of your virtual machine, try the following tips:

## Paravirtual SCSI adapter
[https://kb.vmware.com/kb/1010398 VMware Paravirtual SCSI (PVSCSI) adapters are high-performance storage adapters for VMware ESXi that can result in greater throughput and lower CPU utilization. PVSCSI adapters are best suited for environments, where hardware or applications drive a very high amount of I/O throughput.

The SCSI adapter type  is available in the Virtual Machine settings.

If these settings are not in the virtual machine's configuration, the paravirtual SCSI adapter can still be enabled. Ensure that the paravirtual SCSI adapter is included in the kernel image by modifying the :

Regenerate the initramfs.

Shut down the virtual machine and change the SCSI adapter: set the  to the following:

 scsi0.virtualDev = "pvscsi"

## Paravirtual network adapter
VMware offers multiple network adapters for the guest OS.  The default adapter used is usually the  adapter, which emulates an Intel 82545EM Gigabit Ethernet NIC.  This Intel adapter is generally compatible with the built-in drivers across most operating systems, including Arch.

For more performance and additional features (such as multiqueue support), the VMware native  network adapter can be used.

Arch has the  kernel module available with a default install.  Once enabled in mkinitcpio (or if it is auto-detected; check by running  to see if it is loaded), shut down and change the network adapter type in the .vmx file to the following:

 ethernet0.virtualDev = "vmxnet3"

After changing network adapters, the network and dhcpcd settings will need to be updated to use the new adapter name and MAC address.

 # dhcpcd new_interface_name
 # systemctl enable dhcpcd@new_interface_name.service

The new interface name can be obtained by running .

## Virtual machine settings
These settings could help improve the responsiveness of the virtual machine by reducing disk I/O, at the expense of using more host memory. Vmware's KB1008885 provides the following optimizations:

 mainMem.useNamedFile = "FALSE"
 MemTrimRate = "0"
 prefvmx.useRecommendedLockedMemSize = "TRUE"
 MemAllowAutoScaleDown = "FALSE"
 sched.mem.pshare.enable = "FALSE"

* mainMem.useNamedFile: This will only work for Windows hosts and this parameter can be used if high disk activity is experienced upon shutting down the virtual machine. This will prevent VMware from creating a .vmem file. Use mainmem.backing = "swap" on Linux hosts instead.
* MemTrimRate: This setting prevents that memory which was released by the guest is released on the host also.
* prefvmx.useRecommendedLockedMemSize: Unfortunately there does not seem to exist a proper explanation for this setting; it seems to prevent the host system from swapping parts of the guest memory.
* MemAllowAutoScaleDown: Prevents VMware from adjusting the memory size of the virtual machine if it cannot allocate enough memory.
* sched.mem.pshare.enable: If several virtual machines are running simultaneously, VMware will try to locate identical pages and share these between the virtual machines. This can be very I/O intensive.

The following settings can also be set in the configuration dialog of VMware Workstation(Edit -> Preferences... -> Memory/Priority).

 prefvmx.minVmMemPct = "100"
 mainMem.partialLazySave = "FALSE"
 mainMem.partialLazyRestore = "FALSE"

* prefvmx.minVmMemPct: Sets amount of RAM in percent which should be reserved by the virtual machine on the host system. If this is set to a lower value it is possible to assign the virtual machine more memory than is available in the host system. Be careful though, as in this case it will most likely lead to excessive hard drive usage. If enough RAM is on the host system, this value should be left at 100.
* mainMem.partialLazySave and mainMem.partialLazyRestore: These two parameters will prevent the virtual machine from creating partial snapshots for suspends. When these parameters are used, virtual machine suspension will take slightly longer, but there should be less hard disk activity from VMware trying to store this information.

## Troubleshooting
## Kernel headers for version x.y-zzzz were not found. If you installed them
Install the headers ().

## Cannot load module vmmon
As [https://communities.vmware.com/t5/VMware-Workstation-Pro/Kernel-module-vmmon-not-loading-on-Fedora-21-w-Workstation-11/m-p/2242975#M133526 VMware Comunity explained, please disable Secure Boot to use  to load the VMware module.

## Incorrect login/password when trying to access VMware remotely
VMware Workstation provides the possibility to remotely manage Shared VMs through the  service. However, this will fail with the error  due to incorrect PAM configuration of the  service. To fix it, edit  like this:

and restart the  systemd service.

Now you can connect to the server with the credentials provided during the installation.

## Issues with ALSA output
To fix sound quality issues or enabling proper HD audio output, first run:

 $ aplay -L

If interested in playing 5.1 surround sound from the guest, look for , if experiencing quality issues, look for . Finally put the name in the :

OSS emulation should also be disabled.

## Kernel-based Virtual Machine (KVM) is running
To disable  on boot, you can use something like:

## Icons and padding in VMware application UI are not scaled properly on HiDPI display
See HiDPI#VMware.

## Wayland issues
## Keyboard capture does not work on GNOME
VMWare Player/Workstation 17.5 (and older) have issues discussed here.

To allow the user interface to capture the keyboard:

 $ gsettings set org.gnome.mutter.wayland xwayland-allow-grabs "true"
 $ gsettings set org.gnome.mutter.wayland xwayland-grab-access-rules "As an alternative, you can use the following keyboard shortcuts in Windows:

*  instead of  for the task switcher
*  for the Start menu

## Module issues
## /dev/vmmon not found
The full error is:

 Could not open /dev/vmmon: No such file or directory.
 Please make sure that the kernel module 'vmmon' is loaded.

This means that at least the  module is not loaded. Enable the services (see #Installation) for automatic loading.

Another possible reason is Indirect Branch Tracking on 11th Gen and later Intel processors and starting from kernel 5.18.

Add  to your kernel command line. See [https://communities.vmware.com/t5/VMware-Workstation-Player/kernel-6-3-4-may-break-vmware-player/td-p/2971432 for more details.

## /dev/vmci not found
The full error is:

 Failed to open device "/dev/vmci": No such file or directory
 Please make sure that the kernel module 'vmci' is loaded.

First, try to manually load the modules

 # modprobe -a vmw_vmci

Try to recompile VMware kernel modules with:

 # vmware-modconfig --console --install-all

## VMware fails to start
## Module CPUIDEarly power on failed
Version 14 has stricter CPU requirements than version 12. If you try to start a virtual machine with an affected CPU, the following message will appear:

  This host does not support virtualizing real mode.
  The Intel "VMX Unrestricted Guest" feature is necessary to run this virtual machine on an Intel processor.

The solution is to uninstall version 14 and install version 12 ().

When VMware was usable and this error suddenly appears it could be due to a warm/soft boot or after suspending the system. Please try a cold boot (shutting the system down and starting it again).

## Segmentation fault at startup due to old Intel microcode
Old Intel microcode may result in the following kind of segmentation fault at startup:

 /usr/bin/vmware: line 31: 4941 Segmentation fault "$BINDIR"/vmware-modconfig --appname="VMware Workstation" --icon="vmware-workstation"

See Microcode for how to update the microcode.

## vmplayer/vmware version 14 fails to start
On systems with  version 2:2.44.0 and above, the log files (located in ) show several instances of the following error:

 appLoader| I125+ undefined symbol

A workaround is to downgrade  to earlier version, or more preferably, force VMware to use its own shipped version of :

 # export LD_LIBRARY_PATH=/lib/vmware/lib/librsvg-2.so.2:$LD_LIBRARY_PATH

VMware also has a  variable:

 $ env VMWARE_USE_SHIPPED_LIBS=1 vmware

## vmplayer/vmware fails to start from version 12.5.4
As per the temporary workaround is to downgrade the package  to version 1.6.28-1 and keep it in the  parameter in /etc/pacman.conf.

An easier workaround is to make VMWare use the system's version of zlib instead of its own one:

 # cd /usr/lib/vmware/lib/libz.so.1
 # mv libz.so.1 libz.so.1.old
 # ln -s /usr/lib/libz.so.1 .

## vmplayer/vmware fails to start from version 12.5.3 to version 12.5.5
It seems to be a problem with the file , missing .

If the system have installed , that library is already installed. Therefore, it is possible to remove that file and vmplayer will use the one provided by gcc-libs instead. As root do:

 # mv /usr/lib/vmware/lib/libstdc++.so.6/libstdc++.so.6 /usr/lib/vmware/lib/libstdc++.so.6/libstdc++.so.6.bak

Also there is a workaround:

 # export VMWARE_USE_SHIPPED_LIBS='yes'

## vmware 12 process terminates immediately after start, no GUI is launched
Registered bug at [https://bugs.mageia.org/show_bug.cgi?id=9739 Mageia, but it seems that there are no error messages shown in terminal with arch. When inspecting the logs, which are in , there are , , ,  issues. Process simply terminates with  after vmware or vmplayer is executed. Solution is the same, as root do:

 # mv /etc/vmware/icu/icudt44l.dat /etc/vmware/icu/icudt44l.dat.bak

Also there is a workaround:

 # export VMWARE_USE_SHIPPED_LIBS='yes'

Despite setting the VMWARE_USE_SHIPPED_LIBS variable, VMWare may still fail to find certain libraries. An example is the libfontconfig.so.1 library. Check vmware logs in the tmp directory to see which libraries are still not found. Copy them to the appropriate path with libraries existing on the system:

 # cp /usr/lib/libfontconfig.so.1 /usr/lib/vmware/lib/libfontconfig.so.1/

Instead of copying all these files manually, you may want to try exporting an additional setting:

 # export VMWARE_USE_SYSTEM_LIBS='yes'

On systems with fontconfig version 2.13.0 and above, it may be needed to force VMware to use the shipped libfontconfig file instead of the newer system file. In such case, it is also necessary to provide a shared object library file  for the shipped fontconfig. This applies for at least VMware version 12.5.9. As root do:

 # ln -s /usr/lib/libexpat.so /usr/lib/vmware/lib/libfontconfig.so.1/libexpat.so.0
 # export LD_LIBRARY_PATH=/usr/lib/vmware/lib/libfontconfig.so.1:$LD_LIBRARY_PATH

## Guest issues
## Unable to download VMware Tools for guests
To download the tools manually, visit the VMware repository.

Navigate to: "application name / version / build ID / linux / packages/" and download the appropriate Tools.

Extract with:

 $ tar -xvf vmware-tools-name-version-buildID.x86_64.component.tar

And install using the VMware installer:

 # vmware-installer --install-component=/path/vmware-tools-name-version-buildID.x86_64.component

If the above does not work, try installing .

## Networking on Guests not available after system restart
This is likely due to the  module not being loaded https://www.linuxquestions.org/questions/slackware-14/could-not-connect-ethernet0-to-virtual-network-dev-vmnet8-796095/. Enable the services (see #Installation) for automatic loading.

## Mouse issues
## Mouse buttons above 5 do not work
If your mouse's thumb buttons or other additional buttons do not work,  set guest to use advanced mouse.

## Strange mouse wheel behavior on Guest
This is related to the current Xorg keyboard layout on Host system. Keep primary layout (e.g., English) selected on Host while working on Guest.

## No IP address and network access for nested VMs
This issue is related to promiscuous mode which, following standard Linux practice, can only be enabled by the root user. To work around these limitations, the permissions for the networking device in question have to be changed.

Give permissions to one group:

 # chgrp group /dev/vmnetX

 # chmod g+rw /dev/vmnetX

Give permissions to all users:

 # chmod a+rw /dev/vmnetX
