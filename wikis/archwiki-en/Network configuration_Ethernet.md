# Network configuration/Ethernet

This article describes Ethernet specifics, general network configuration is covered in Network configuration.

## Device driver
## Check the status
udev should detect your network interface controller (NIC) and automatically load the necessary kernel module at startup. Check the output of  (where  means the "Ethernet controller" subclass of the "Network controller" PCI device class)
. It should tell you which kernel module contains the driver for your network device. For example:

Next, check that the driver was loaded by running  as root. For example:

Skip the next section if the driver was loaded successfully. Otherwise, you will need to know which module is needed for your particular model.

## Load the module
Search the internet for the right module/driver for your chipset. Some common modules are  for cards with a Realtek chipset, or  for cards with a SiS chipset. Once you know which module to use, try to load it manually. If you get an error saying that the module was not found, verify first if you recently upgraded the kernel (see General troubleshooting#Cannot use some peripherals after kernel upgrade). Alternatively, it is possible that the driver is not included in the Arch kernel. You may search the AUR for the module name.

If udev is not detecting and loading the proper module automatically during bootup, you can explicitly load the module at boot.

## Tips and tricks
## ifplugd for laptops
 is a daemon which will automatically configure your Ethernet device when a cable is plugged in and automatically unconfigure it if the cable is pulled. This is useful on laptops with onboard network adapters, since it will only configure the interface when a cable is really connected. Another use is when you just need to restart the network but do not want to restart the computer or do it from the shell.

By default it is configured to work for the  device. This and other settings like delays can be configured in .

## Reduce link speed
Forcing 100Mbps or 10Mbps full-duplex speed on a gigabit ethernet NIC can save a lot of power (~1W) on most network workloads. This also reduces components temperature.

Using  on every boot is inconvenient.

Boot time initialization of lower ethernet NIC speed is possible through systemd.link files. The actual setup is performed by the  udev builtin. Add the  option to the network link file:

Also see  for more information.

## Troubleshooting
## Swapping computers on the cable modem
Some cable ISPs (Vidéotron for example) have the cable modem configured to recognize only one client PC, by the MAC address of its network interface. Once the cable modem has learned the MAC address of the first PC or equipment that talks to it, it will not respond to another MAC address in any way. Thus if you swap one PC for another (or for a router), the new PC (or router) will not work with the cable modem, because the new PC (or router) has a MAC address different from the old one. To reset the cable modem so that it will recognise the new PC, you must power the cable modem off and on again. Once the cable modem has rebooted and gone fully online again (indicator lights settled down), reboot the newly connected PC so that it makes a DHCP request, or manually make it request a new DHCP lease.

If this method does not work, you will need to clone the MAC address of the original machine. See also MAC address spoofing.

## Explicit Congestion Notification
Explicit Congestion Notification (ECN) may cause traffic problems with old/bad routers As of [https://github.com/systemd/systemd/pull/20535 systemd 240, it is enabled for incoming connections that request it (kernel default).

To enable ECN for both incoming and outgoing connections:

 # sysctl net.ipv4.tcp_ecn=1

To enable ECN only when requested by incoming connections (the reasonably safe, kernel default):

 # sysctl net.ipv4.tcp_ecn=2

To disable ECN completely (to e.g. test whether ECN was causing problems):

 # sysctl net.ipv4.tcp_ecn=0

See also the kernel documentation.

## Broadcom BCM57780
This Broadcom chipset sometimes does not behave well unless you specify the order of the modules to be loaded. The modules are  and , the former needing to be loaded first.

These steps should help if your computer has this chipset:

* Find your NIC in lspci output:

* If your wired networking is not functioning in some way or another, unplug your cable then do the following:

 # modprobe -r tg3
 # modprobe broadcom
 # modprobe tg3

* Plug your network cable back in and check whether the module succeeded with:

 # dmesg | grep tg3

* If this procedure solved the issue you can make it permanent by adding  and  (in this order) to the  array:

* Regenerate the initramfs
* Alternatively, you can create an :

 softdep tg3 pre: broadcom

## Realtek no link / WOL problem
Users with Realtek 8168 8169 8101 8111(C) 8156B based NICs (cards / and on-board) may notice a problem where the NIC seems to be disabled on boot and has no Link light. This can usually be found on a dual boot system where Windows is also installed. It seems that using the official Realtek drivers (dated anything after May 2007) under Windows is the cause. These newer drivers disable the Wake-On-LAN feature by disabling the NIC at Windows shutdown time, where it will remain disabled until the next time Windows boots. You will be able to notice if this problem is affecting you if the Link light remains off until Windows boots up; during Windows shutdown the Link light will switch off. Normal operation should be that the link light is always on as long as the system is on, even during POST. This problem will also affect other operating systems without newer drivers (eg. Live CDs). Here are a few fixes for this problem.

## Enable the NIC directly in Linux
Follow Network configuration#Enabling and disabling network interfaces to enable the interface.

## Rollback/change Windows driver
You can roll back your Windows NIC driver to the Microsoft provided one (if available), or roll back/install an official Realtek driver pre-dating May 2007 (may be on the CD that came with your hardware).

## Enable WOL in Windows driver
Probably the best and the fastest fix is to change this setting in the Windows driver. This way it should be fixed system-wide and not only under Arch (eg. live CDs, other operating systems). In Windows, under Device Manager, find your Realtek network adapter and double-click it. Under the "Advanced" tab, change "Wake-on-LAN after shutdown" to "Enable".

## Enable LAN Boot ROM in BIOS/CMOS
It appears that setting Integrated Peripherals > Onboard LAN Boot ROM > Enabled in BIOS/CMOS reactivates the Realtek LAN chip on system boot-up, despite the Windows driver disabling it on OS shutdown.

## Disable USB AutoSuspend
When using power saving features, specifically USB autosuspend, the device can fail to load correctly, resulting in a NO-CARRIER state (tested with RT8156B), and no established link.

To resolve, see Power management#USB autosuspend for details on blacklisting a device for USB autosuspend manually, or TLP documentation on USB devices if using TLP; then reconnect the device.

## Realtek RTL8111/8168B
The adapter should be recognized by the  module. However, with some chip revisions the connection may go off and on all the time. The alternative  should be used for a reliable connection in this case. Blacklist , if  is not automatically loaded by udev, you can explicitly load the module at boot.

Another fault in the drivers for some revisions of this adapter is poor IPv6 support. IPv6#Disable functionality can be helpful if you encounter issues such as hanging webpages and slow speeds.

## Gigabyte Motherboard with Realtek 8111/8168/8411
With motherboards such as the Gigabyte GA-990FXA-UD3, booting with IOMMU off (which can be the default) will cause the network interface to be unreliable, often failing to connect or connecting but allowing no throughput. This will apply to the onboard NIC and to any other pci-NIC in the box because the IOMMU setting affects the entire network interface on the board. Enabling IOMMU and booting with the install media will throw AMD I-10/xhci page faults for a second, but then boots normally, resulting in a fully functional onboard NIC (even with the r8169 module).

When configuring the boot process for your installation, add  as a kernel parameter to eliminate the error messages on boot and restore USB3.0 functionality.

## MicroStar Motherboard with Realtek 8111/8168/8411
With motherboards such as the "MicroStar B450M MORTAR TITANIUM", unpluging/pluging Ethernet cables or restarting router's DHCP server would cause  to enter a downshifted status, and downgrade the 1000 Mbit/s Ethernet speed to 100 Mbit/s. The kernel log will show:

In this case, restart the adapter (set it down and up). For example:

 # ip link set dev enp34s0 down
 # ip link set dev enp34s0 up

## Realtek RTL8153 Tx timeout
USB Network Adapters with the following controller will often hang and stop transmit until its link is reset. This is accompanied with  or  errors in the kernel log. This can be fixed by setting .

The quirk can be set at boot by adding the kernel parameter . It can also be set immediately via the sysfs by

Note that  should be replaced with your own device's USB ID which can be found using lsusb.
