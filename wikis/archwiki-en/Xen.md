# Xen

From Xen Overview:

:Xen is an open-source type-1 or baremetal hypervisor, which makes it possible to run many instances of an operating system or indeed different operating systems in parallel on a single machine (or host). Xen is the only type-1 hypervisor that is available as open source.

The Xen hypervisor is a thin layer of software which emulates a computer architecture allowing multiple operating systems to run simultaneously. The hypervisor is started by the boot loader of the computer it is installed on. Once the hypervisor is loaded, it starts the dom0—short for "domain 0", sometimes called the host or privileged domain—which in our case runs Arch Linux. Once the dom0 has started, one or more domU (short for user domains, sometimes called VMs or guests) can be started and controlled from the dom0.  For the domU, Xen supports paravirtualized (PV) domains, hardware virtualized  domains (HVM), and paravirtualised domains inside a hardware virtualization wrapper (PVH). See Xenproject.org for a full overview.

The Xen hypervisor relies on a full install of the base operating system. Before attempting to install the Xen hypervisor, the  host machine should have a fully operational and up-to-date install of Arch Linux. This installation can be a minimal install with only the base package and does not require a Desktop environment or even Xorg.

If you are building a new host from scratch, see the Installation guide for instructions on installing Arch Linux.

## Installation
## System requirements
The Xen hypervisor requires kernel-level support which is built into the  and  Arch kernel packages. To run HVM domU, the physical hardware must have either Intel VT-x or AMD-V (SVM) virtualization support. In order to verify this, check for the vmx or svm CPU flags when the Xen hypervisor is not running:

 $ grep -E 'vmx|svm' --color -m 1 /proc/cpuinfo

If the above command does not produce output, then hardware virtualization support is unavailable and your hardware is unable to run HVM domU (or you are already running the Xen hypervisor). If you believe the CPU supports one of these features you should access the host system's BIOS configuration menu during the boot process and look if options related to virtualization support have been disabled. If such an option exists and is disabled, then enable it, boot the system and repeat the above command. The Xen hypervisor also supports PCI passthrough where PCI devices can be passed directly to the domU even in the absence of dom0 support for the device. In order to use PCI passthrough, the CPU must support IOMMU/VT-d.

## Installation of the Xen Hypervisor
To install the Xen hypervisor, install the  package. It provides the Xen hypervisor, current xl interface and all configuration and support files, including systemd services. To run most VMs, you will also need to install .

For BIOS support in VMs, install .  For UEFI support, install . To boot VM-local kernels inside of a PVH VM, install .

## Building xen
It is recommended that xen and its components are built in a clean environment, either in a VM or a clean chroot.  When building Xen, there are environmental variables that can be passed to makepkg.

# build_stubdom -- Build the components to run Xen stubdoms, mainly for dom0 disaggregation.  Components for stubdom are broken off into xen-stubdom if built.  Defaults to false.
# boot_dir-- Your boot directory.  Defaults to /boot.
# efi_dir, efi_mountpoint -- Your EFI directory and mountpoint.   Defaults to /boot.

Pass these arguments to makepkg as variables:

 $ build_stubdom=true efi_dir="/boot/EFI" makepkg

 will be also built for the man pages and documentation. If you choose to build stubdom support, a xen-stubdom package will be built.

## Modification of the boot loader
The boot loader must be modified to load a special Xen kernel ( or in the case of UEFI ) which is then used to boot the normal kernel. To do this a new boot loader entry is needed.

## UEFI
Xen supports booting from UEFI as specified in Xen EFI systems.  It also might be necessary to use efibootmgr to set boot order and other parameters.

First, ensure the  file is in the EFI system partition along with your kernel and ramdisk files.

Second, Xen requires an ASCII (no UTF-8, UTC-16, etc) configuration file that specifies what kernel should be booted as dom0.  This file must be placed in the same EFI system partition as the binary.  Xen looks for several configuration files and uses the first one it finds.  The order of search starts with the  extension of the binary's name replaced by , then drops trailing name components at ,  and  until a match is found.  Typically, a single file named  is used with the system requirements, such as:

## systemd-boot
Add a new EFI-type loader entry. See systemd-boot#UEFI Shells or other EFI applications for more details.  For example:

## EFI boot stub
It is possible to boot an EFI kernel directly from UEFI by using an EFI boot stub.

Drop to the build-in UEFI shell and call the EFI file directly.  For example:

 Shell> fs0:
 FS0:\> xen.efi

Note that a  configuration file in the EFI system partition is still required as outlined above.  In addition, a different configuration file may be specified with the  parameter.  For example:

 Shell> fs0:
 FS0:\> xen.efi -cfg=xen-rescue.cfg

These additional configuration files must reside in the same directory as the Xen EFI binary and linux stub files.

## BIOS
Xen supports booting from system firmware configured as BIOS.

## GRUB
For GRUB users, install the  package for booting dom0 as well as building PvGrub2 images for booting user domains.

The file  can be edited to customize the Xen boot commands. For example, to allocate 512 MiB of RAM to dom0 at boot, modify  by replacing the line:

 #GRUB_CMDLINE_XEN_DEFAULT=""

with

 GRUB_CMDLINE_XEN_DEFAULT="dom0_mem=512M"

More information on GRUB configuration keys for Xen can be found in the GRUB documentation.

After customizing the options, update the boot loader configuration with the following command:

 # grub-mkconfig -o /boot/grub/grub.cfg

## Building GRUB images for booting guests
Besides the usual platform targets, the  package builds GRUB for three additional targets that can be used to boot Xen guests: i386-xen, i386-xen_pvh, and x86_64-xen. To create a boot image from one of these targets, first create a GRUB configuration file. Depending on your preference, this file can either locate and load a GRUB configuration file in the guest or it could manage more of the boot process from dom0.  Assuming all that is needed is to locate and load a configuration file in the guest, add the following to a file,

and then create a GRUB/Tips and tricks#GRUB standalone image that will incorporate that file:

  # grub-mkstandalone -O x86_64-xen -o /usr/lib/xen/boot/pv-grub2-x86_64-xen "/boot/grub/grub.cfg=./grub.cfg"

Lastly, add that image as value of the kernel in the domU configuration file (for a 64-bit guest in this example):

  kernel = "/usr/lib/xen/boot/pv-grub2-x86_64-xen"

More examples of configuring GRUB images for GRUB guests can be found in the Xen Project's PvGrub2 documentation.

## Syslinux
For Syslinux users, add a stanza like this to your :

 LABEL xen
     MENU LABEL Xen
     KERNEL mboot.c32
     APPEND ../xen-X.Y.Z.gz --- ../vmlinuz-linux console=tty0 root=/dev/sdaX ro --- ../initramfs-linux.img

where  is your xen version and  is your root partition.

This also requires  (and ) to be in the same directory as . If you do not have  in , copy it from:

 # cp /usr/lib/syslinux/bios/mboot.c32 /boot/syslinux

## Creation of a network bridge
Xen requires that network communications between domU and the dom0 (and beyond) be set up manually. The use of both DHCP and static addressing is possible, and the choice should be determined by the network topology. Complex setups are possible, see the Networking article on the Xen wiki for details and  for scripts for various networking configurations. A basic bridged network, in which a virtual switch is created in dom0 that every domU is attached to, can be set up by creating a network bridge with the expected name .

See Network bridge#Creating a bridge for details.

## systemd-networkd
See systemd-networkd#Bridge interface for details.

## Network Manager
Gnome's Network Manager can sometime be troublesome. If following the bridge creation section outlined in the bridges section of the wiki are unclear or do not work, then the following steps may work.

Open the Network Settings and disable the interface you wish to use in your bridge (ex enp5s0). Edit the setting to off and uncheck "connect automatically."

Create a new bridge connection profile by clicking on the "+" symbol in the bottom left of the network settings. Optionally, run:

 # nm-connection-editor

to bring up the window immediately. Once the window opens, select Bridge.

Click "Add" next to the "Bridged Connections" and select the interface you wished to use in your bridge (ex. Ethernet). Select the device mac address that corresponds to the interface you intend to use and save the settings

If your bridge is going to receive an IP address via DHCP, leave the IPv4/IPv6 sections as they are. If DHCP is not running for this particular connection, make sure to give your bridge an IP address. Needless to say, all connections will fail if an IP address is not assigned to the bridge. If you forget to add the IP address when you first create the bridge, it can always be edited later.

Now, as root, run:

 # nmcli con show

You should see a connection that matches the name of the bridge you just created. Highlight and copy the UUID on that connection, and then run (again as root):

 # nmcli con up

A new connection should appear under the network settings. It may take 30 seconds to a minute. To confirm that it is up and running, run:

 # brctl show

to show a list of active bridges.

Reboot. If everything works properly after a reboot (ie. bridge starts automatically), then you are all set.

 In your network settings, remove the connection profile on your bridge interface that does NOT connect to the bridge. This just keeps things from being confusing later on.

## Installation of Xen systemd services
The Xen dom0 requires the , ,  and  to be started and possibly enabled.

## Confirming successful installation
Reboot your dom0 host and ensure that the Xen kernel boots correctly and that all settings survive a reboot. A properly set up dom0 should report the following when you run  as root:

Of course, the Mem, VCPUs and Time columns will be different depending on machine configuration and uptime. The important thing is that dom0 is listed.

In addition to the required steps above, see best practices for running Xen which includes information on allocating a fixed amount of memory and how to dedicate (pin) a CPU core for dom0 use. It also may be beneficial to create a xenfs filesystem mount point by including in
 none /proc/xen xenfs defaults 0 0

## Configure Best Practices
Review Xen Project Best Practices before using Xen.

## Using Xen
Xen supports both paravirtualized (PV) and hardware virtualized (HVM) domU. In the following sections the steps for creating HVM and PV domU running Arch Linux are described. In general, the steps for creating an HVM domU are independent of the domU OS and HVM domU support a wide range of operating systems including Microsoft Windows. To use HVM domU the dom0 hardware must have virtualization support. Paravirtualized domU do not require virtualization support, but instead require modifications to the guest operating system making the installation procedure different for each operating system (see the Guest Install page of the Xen wiki for links to instructions). Some operating systems (e.g., Microsoft Windows) cannot be installed as a PV domU. In general, HVM domU often run slower than PV domU since HVMs run on emulated hardware. While there are some common steps involved in setting up PV and HVM domU, the processes are substantially different. In both cases, for each domU, a "hard disk" will need to be created and a configuration file needs to be written. Additionally, for installation each domU will need access to a copy of the installation ISO stored on the dom0 (see the Download Page to obtain the Arch Linux ISO).

## Create a domU "hard disk"
Xen supports a number of different types of "hard disks" including Logical Volumes, raw partitions, and image files. To create a sparse file, that will grow to a maximum of 10GiB, called , use:

 $ truncate -s 10G domU.img

If file IO speed is of greater importance than domain portability, using Logical Volumes or raw partitions may be a better choice.

Xen may present any partition / disk available to the host machine to a domain as either a partition or disk. This means that, for example, an LVM partition on the host can appear as a hard drive (and hold multiple partitions) to a domain. Note that making sub-partitons on a partition will make accessing those partitions on the host machine more difficult. See  for information on how to map out partitions within a partition.

## Create a domU configuration
Each domU requires a separate configuration file that is used to create the virtual machine. Full details about the configuration files can be found at the Xen Wiki or the  man page. Both HVM and PV domU share some components of the configuration file. These include

 name = "domU"
 memory = 512
 disk = [ "file:/path/to/ISO,sdb,r", "phy:/path/to/partition,sda1,w" ]
 vif = [ 'mac=00:16:3e:XX:XX:XX,bridge=xenbr0' ]

The  is the name by which the xl tools manage the domU and needs to be unique across all domU. The  includes information about both the installation media () and the partition created for the domU . If an image file is being used instead of a physical partition, the  needs to be changed to . The  defines a network controller. The  MAC block is reserved for Xen domains, so the last three digits of the  must be randomly filled in (hex values 0-9 and a-f only).

## Managing a domU
If a domU should be started on boot, create a symlink to the configuration file in  and ensure the  service is set up correctly. Some useful commands for managing domU are:

 # xl top
 # xl list
 # xl console domUname
 # xl shutdown domUname
 # xl destroy domUname

## Configuring a hardware virtualized (HVM) Arch domU
In order to use HVM domU install the ,  and  packages.

A minimal configuration file for a HVM Arch domU is:

 name = 'HVM_domU'
 builder = 'hvm'
 memory = 512
 vcpus = 2
 disk = [ 'phy:/dev/vg0/hvm_arch,xvda,w', 'file:/path/to/ISO,hdc:cdrom,r' ]
 vif = [ 'mac=00:16:3e:00:00:00,bridge=xenbr0' ]
 vnc = 1
 vnclisten = '0.0.0.0'
 vncdisplay = 1

Since HVM machines do not have a console, they can only be connected to via a vncviewer. The configuration file allows for unauthenticated remote access of the domU vncserver and is not suitable for unsecured networks. The vncserver will be available on port , where X is the value of , of the dom0. The domU can be created with:

 # xl create /path/to/config/file

and its status can be checked with

 # xl list

Once the domU is created, connect to it via the vncserver and install Arch Linux as described in the Installation guide.

## Configuring a paravirtualized (PV) Arch domU
A minimal configuration file for a PV Arch domU is:

 name = "PV_domU"
 kernel = "/mnt/arch/boot/x86_64/vmlinuz-linux"
 ramdisk = "/mnt/arch/boot/x86_64/initramfs-linux.img"
 extra = "archisobasedir=arch archisodevice=UUID=YYYY-mm-dd-HH-MM-SS-00"
 memory = 512
 disk = [ "phy:/path/to/partition,sda1,w", "file:/path/to/ISO,sdb,r" ]
 vif = [ 'mac=00:16:3e:XX:XX:XX,bridge=xenbr0' ]

This file needs to tweaked for your specific use. Most importantly, the  line must be edited to use the creation date and time of the ISO being used.

Before creating the domU, the installation ISO must be loop-mounted. To do this, ensure the directory  exists and is empty, then run the following command (being sure to fill in the correct ISO path):

 # mount -o loop /path/to/iso /mnt

Once the ISO is mounted, the domU can be created with:

 # xl create -c /path/to/config/file

The "-c" option will enter the domUs console when successfully created. Then you can install Arch Linux as described in the Installation guide, but with the following deviations. The block devices listed in the disks line of the cfg file will show up as . Use these devices when partitioning the domU. After installation and before the domU is rebooted, the , , ,  modules must be added to Mkinitcpio. Without these modules, the domU will not boot correctly. For booting, it is not necessary to install Grub. Xen has a Python-based grub emulator, so all that is needed to boot is a  file: (It may be necessary to create the  directory)

{{hc|/boot/grub/grub.cfg|
menuentry 'Arch GNU/Linux, with Linux core repo kernel' --class arch --class gnu-linux --class gnu --class os $menuentry_id_option 'gnulinux-core repo kernel-true-__UUID__' {
        insmod gzio
        insmod part_msdos
        insmod ext2
        set root='hd0,msdos1'
        if [ x$feature_platform_search_hint = xy ]; then
          search --no-floppy --fs-uuid --set=root --hint-bios=hd0,msdos1 --hint-efi=hd0,msdos1 --hint-baremetal=ahci0,msdos1  __UUID__
        else
          search --no-floppy --fs-uuid --set=root __UUID__
        fi
        echo    'Loading Linux core repo kernel ...'
        linux   /boot/vmlinuz-linux root=UUID=__UUID__ ro
        echo    'Loading initial ramdisk ...'
        initrd  /boot/initramfs-linux.img
}
}}

This file must be edited to match the UUID of the root partition. From within the domU, run the following command:

 # blkid

Replace all instances of  with the real UUID of the root partition (the one that mounts as ).:

 # sed -i 's/__UUID__/12345678-1234-1234-1234-123456789abcd/g' /boot/grub/grub.cfg

Shutdown the domU with the  command. The console will be returned to the hypervisor when the domain is fully shut down, and the domain will no longer appear in the xl domains list. Now the ISO file may be unmounted:

 # umount /mnt

The domU cfg file should now be edited. Delete the , , and  lines and replace them with the following line:

 bootloader = "pygrub"

Also remove the ISO disk from the  line.

The Arch domU is now set up. It may be started with the same line as before:

 # xl create -c /etc/xen/archdomu.cfg

## Troubleshooting
## "xl list" complains about libxl
Either you have not booted into the Xen system, or xen modules listed in  script are not installed.

## "xl create" fails
Check the guest's kernel is located correctly, check the  file for spelling mistakes (like using  instead of ).

## Creating HVM fails
If creating HVM fails with:

 libxl: error: libxl_dm.c:3131:device_model_spawn_outcome: Domain 33:domain 33 device model: spawn failed (rc=-3)
 libxl: error: libxl_dm.c:3351:device_model_postconfig_done: Domain 33:Post DM startup configs failed, rc=-3
 libxl: error: libxl_create.c:1837:domcreate_devmodel_started: Domain 33:device model did not start: -3
 libxl: error: libxl_aoutils.c:646:libxl__kill_xs_path: Device Model already exited

You have missed to install .

## Arch Linux guest hangs with a ctrl-d message
Press  until you get back to a prompt, rebuild its initramfs described.

## "udev_event" fails
An error like

 failed to execute '/usr/lib/udev/socket:/org/xen/xend/udev_event' 'socket:/org/xen/xend/udev_event': No such file or directory

is caused by . Xend is deprecated and not used, so it is safe to remove that file.
