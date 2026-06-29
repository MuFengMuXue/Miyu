# Windows PE

Windows PE (WinPE) is a lightweight version of Windows intended to be used for its installation, as well as for system maintenance. It runs entirely from memory and can be booted from the network.

Windows PE images are normally created in Windows using the Windows ADK. This page describes how customized Windows PE images can be created, and optionally published on the network, using an (Arch) Linux machine. This might be useful if :

* you need to install Windows from the network, or boot Windows PE from the network for system administration, using an Arch Linux-based server. This may be because you do not have a Windows-based server, or you prefer using a Linux server because of its improved security and configurability, or you are already using a Linux server for other purposes.
* you need to run a Windows environment to run Win32 programs, you do not have a Windows machine available, and you do not want to use Wine or the programs will not run correctly with Wine.
* you need to update firmware for which your device manufacturer only provides Windows binaries.

## Creating a bootable Windows PE image
Install .

## Obtain a Windows ISO or WAIK image
You need a copy of Windows installation media, in order to extract the  file that contains the initial copy of Windows PE, along with some boot files. Different versions of Windows contain different versions of Windows PE. For the relationship between Windows versions and Windows PE versions, refer to Wikipedia.

The simplest method is to download the latest Windows 11 ISO.

## Prepare a bootable Windows PE ISO
Mount the installation image, e.g.:

 # mount --mkdir winimg.iso /media/winimg

Use the  script provided with  to create a bootable Windows PE ISO :

 $ mkwinpeimg --iso --windows-dir=/media/winimg winpe.iso

See  for more information, including the  option to copy files into the image. You may want to do this to add additional Windows applications that you want to run in Windows PE, or to add any additional drivers that Windows PE needs. Drivers can be loaded using the  command within Windows PE.

Unmount the source ISO:

 # umount /media/winimg

## Prepare bootable Windows PE media for UEFI systems
 cannot build a bootable UEFI system natively, but the necessary UEFI boot files are included in  the Windows installation media.

These can be used for creating a bootable USB key or a bootable ISO file for UEFI systems.

The following steps assume that  is still mounted at .

Create a directory  which will contain the files necessary for creating UEFI boot media.

Mount the newly created Windows PE ISO file and copy the necessary files over to :

 # mount --mkdir winpe.iso /media/winpe
 # cp -r /media/winpe/* winpe_uefi
 # cp -r /media/winimg/efi winpe_uefi

## Option 1: Create an ISO file for UEFI systems
Use the following command to create a version of the ISO file which can be booted from UEFI systems:

 $ mkisofs \
     -no-emul-boot \
     -b "efi/microsoft/boot/efisys.bin" \
     -iso-level 4 \
     -udf \
     -joliet \
     -disable-deep-relocation \
     -omit-version-number \
     -relaxed-filenames \
     -output "winpe_uefi.iso" \
     winpe_uefi

You can now unmount all ISO. Your  file is ready to boot on UEFI systems now.

## Option 2: Create an USB key for UEFI systems
On a USB key, create a GPT partition table with a single partition of type , and format the partition to FAT32.

Copy the files prepared in the  directory over to the USB key:

 # mount --mkdir /dev/sdX1 /media/usb
 # cp -r winpe_uefi/* /media/usb/

You can now umount all ISO and the USB key, your USB key is ready to boot.

## Booting Windows PE
After creating a bootable ISO of Windows PE () as described in the previous section, you may want to boot Windows PE in the following ways:

## In virtual machine
Run a virtual machine with  attached as a CD-ROM.  Be sure to give it adequate memory, definitely more than the size of the ISO, since Windows PE runs from memory.  See Hypervisors for a list of available virtualization software.

## From USB key
If you have prepared a USB key for UEFI systems according to the guide above, it should just boot. It may take some time to boot (10 to 20 seconds is not uncommon, depending on your USB key) because the loader seems to copy some/all data to RAM.

## From CD
Simply burn  onto a CD, and you can boot from it.

## From Network
Windows PE can be booted from the network using PXELINUX and its MEMDISK module on BIOS systems. For UEFI systems, wimboot and iPXE can be used.

Install  and .

Copy needed PXELINUX files to the TFTP server root directory.

 # rsync -aq /usr/lib/syslinux/bios/ /var/tftpboot/

Put  in the TFTP server root directory.

 # mv winpe.iso /var/tftpboot

Create a configuration file for PXELINUX similar to the following:

Start the TFTP server.

Configure your DHCP server (such as Dhcpd or Dnsmasq) to point to  as the boot file, with the Linux server's IP address.  Beware: if your DHCP server is on a router, it may not be possible to do this without installing custom firmware.

After completing the above steps, you should be able to boot Windows PE from the network.

## Installing Windows from Windows PE
Once booted into Windows PE, you can install Windows from an installation media.

The installation media can be a network share (Samba). See Samba for seting up a Samba server on another machine on the LAN. To share the installation image mounted at , add the following share definition to :

Once booted into Windows PE command prompt, run the following command to initialize the network interface, obtain the IP of the Samba server (assuming Windows PE was booted over PXE from a machine that runs the DHCP, TFTP, and Samba server, the server IP will usually be the Gateway IP), mount the share, and launch the GUI setup:

  > wpeinit
  > ipconfig
  > net use I: \\IP.ADDRESS.OF.SAMBA.SERVER\REMINST
  > I:\setup.exe

## Tips and tricks
## Update Intel Management Engine firmware
You can use Windows PE in order to install updates for firmware such as Intel ME if your hardware manufacturer only provides Windows binaries, and you cannot update via Fwupd.

You will need to download :

* your manufacturer's Intel ME update tool
* drivers for the Intel Management Engine.

Store both extracted archives in a folder, e.g.

 /vendor_files
   ├── me_driver
   └── update_tool

Proceed with #Creating a bootable Windows PE image but make sure to :

* choose a windows PE version for which your device vendor provides Intel ME drivers, i.e. 32-bit or 64-bit.
* include the device drivers and update tool with , e.g. :
 $ mkwinpeimg --iso --windows-dir=/media/winimg --overlay=vendor_files winpe.iso

Proceed with #Booting Windows PE, then load the drivers with:

 X:\Windows\Systems32>cd \
 X:\>drvload me_driver\...\heci.inf

Finally, update the Intel ME firmware by using the update tool.

## Custom Windows PE images
Tools like Hiren's BootCD and others include Windows PE and are around half the size (~2.8GB) of a full Windows ISO. They are often fuller featured boot environments and can include Internet Explorer, which may be helpful to look up  or  commands to repair Windows boot manager.

Hiren's BootCD is not already bootable. A bootable partition needs to be created before copying the contents of the ISO to it. Make sure the USB key uses a GPT partition, and that there is a FAT32 partition of type EFI System on it—see #Prepare bootable Windows PE media for UEFI systems.

Mount the ISO and the partition on the USB key, for example:

 # mount --mkdir HBCD_PE_x64.iso /media/hbcd_iso
 # mount --mkdir /dev/sdXY /media/usb

Copy the contents of the ISO onto the USB:

 # cp -r /media/hbcd_iso/* /media/usb/

You may now unmount all ISOs and removable partitions. The USB should now be bootable.

## Troubleshooting
## System error 58 has occurred. The specified server cannot perform the requested operation
If you are getting the following error when using the  command:

 System error 58 has occurred.

 The specified server cannot perform the requested operation.

1. Make sure you have not accidentally unmounted the  directory.

2. Add a  to . Add the following at the top of the file:

3. Restart the .

4. Specify any username/password in the net use command:

 net use I: \\IP.ADDRESS.OF.SAMBA.SERVER\REMINST /user:user pass

This is happening because Windows 10 connects to anonymous shares by checking some username and password to see if it is able to log in, and if so it allows an anonymous connection.
Apparently whatever part hides this from the user did not make it into the PE build.
