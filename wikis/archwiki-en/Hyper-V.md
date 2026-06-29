# Hyper-V

Hyper-V is a hypervisor that is included with some versions of Microsoft Windows. It is capable of running an Arch Linux virtual machine. Hyper-V is generally oriented toward enterprise rather than desktop use, and does not provide as convenient and simple of an interface as consumer virtualization programs like VirtualBox, Parallels, or VMware. However more recent versions and builds of Windows 10 and Windows Server 2016 include easier configuration options and better compatibility for Arch Linux. Networking features such as NAT for internal switches, multiple NATs and port forwarding have been added without the need to set up Internet Connection Sharing (ICS). Generation 2 virtual machines also now work properly for Arch Linux.

## Installation
Hyper-V is included with Windows since Windows Server 2008 as well as Windows 8, 8.1, 10 and 11 in the Pro versions.

For installation instructions see Install Hyper-V in Windows and Windows Server | Microsoft Learn

## Network configuration
First, you must configure a new virtual switch so that your virtual machine will be able to connect to the Internet. Once Hyper-V is enabled, start the Hyper-V Manager: search for it, or start it from Command Prompt with the command

 %windir%\system32\mmc.exe "%windir%\system32\virtmgmt.msc"

## Set up a virtual switch
In order to connect your virtual machine to an existing network, either use an internal or external network switch (virtual network adapter). An external switch must be bound (bridged) to one of the host's existing network adapters (e.g. Ethernet or Wi-Fi). An internal switch can be used for network communication between the host and virtual machines, without the virtual machines having access to the external network. Adding NAT functionality to an internal switch makes the host act as a router for the virtual machines, enabling the virtual machines access to the external network.

Not all networking features (e.g. NAT configuration) can be set up through the Hyper-V Manager GUI. Using PowerShell, run as an Administrator, permits better control over configuration.

## External switch
To create an external switch, in the right sidebar, select "Virtual Switch Manager...". In the left sidebar of the dialog that opens, choose "New virtual network switch". Under "What type of virtual switch do you want to create?", select "External", then "Create Virtual Switch". Type a new name for the virtual switch. Under "External network", choose the network adapter to bind with the external switch.

You will be prompted about network disruption; continue and your network will be briefly disconnected as the switch is configured.

Using PowerShell (run as Administrator), the above steps can be done with the following:
 # Get a list of the network adapters in the host. In a laptop you should typically see 'Ethernet' and 'Wi-Fi'
 PS C:\WINDOWS\system32> Get-NetAdapter

 # Create the external switch with a name of VM-External-Switch, bound to the network adapter named  retrieved from the previous command
 PS C:\WINDOWS\system32> New-VMSwitch -Name "VM-External-Switch" -AllowManagementOS $True -NetAdapterName "Wi-Fi"

On an Arch Linux virtual machine, choosing the external switch as the virtual machine network adapter effectively bridges the Windows host's network adapter with the virtual machine's  interface. The interface can then be set up in Arch Linux through the usual ways (systemd-networkd, netctl, etc.) with a static IP address or with DHCP. The virtual machine will act just like another host in the external network.

For example, if you want the Arch Linux virtual machine to use a static IP, and the Windows host is configured as , then the Arch Linux virtual machine interface should be configured like , with the same gateway and DNS servers as set up in the host.

If using DHCP for the virtual machine, the IP address will be assigned by the DHCP server in the external network.

## Internal switch
As of version 1803 ("Fall Creators Update"),  Windows 10 has a NAT Switch built in (named "Default Switch") that gives you instant internet access after installing your virtual machine if you set it up to use DHCP, see this Technet blog post, so you do not need the instructions below to get a working NAT switch.

To create an internal switch, follow the same steps as the external switch, however replace the relevant choices for 'internal switch'. Starting with Windows 10 Anniversary Update (Version 1607, OS Build 14393), native NAT support for internal switches was added to Hyper-V. For earlier versions, Internet Connection Sharing (ICS) can be used to enable network access for virtual machines on internal switches.

To find out which version and build of Windows you are using, on a command prompt or PowerShell, run:
 > winver

Using PowerShell (run as Administrator), an internal switch can be created with the following commands:
 # Create the internal switch with a name of VM-Internal-Switch
 PS C:\WINDOWS\system32> New-VMSwitch -Name "VM-Internal-Switch" -SwitchType Internal

 # Verify that the internal switch was created
 PS C:\WINDOWS\system32> Get-VMSwitch

 # Get the ifIndex of the newly created internal switch, usually named 'vEthernet (name)'
 PS C:\WINDOWS\system32> Get-NetAdapter

 # Set the IP address of the internal switch, noting the ifIndex retrieved from the previous command.
 # In this example, the network address of the internal switch is 192.168.3.0/24, and the ifIndex is 50.
 PS C:\WINDOWS\system32> New-NetIPAddress -IPAddress 192.168.3.1 -PrefixLength 24 -InterfaceIndex 50

 # The virtual machines using the internal switch must use static IP addresses, such as 192.168.3.2/24.
 # Support for DHCP in internal switches is not included in current Windows versions (as of Version 1703, OS Build 15063).

With the above steps, the host and vritual machines can already communicate with each other since they will be on the same virtual network (). The virtual machines however will not be able to access the external network until NAT or ICS is configured.

On Windows 10 build 14393 or later, internal switches can be configured for NAT and port forwarding:
 # Create the NAT with IP address of the internal switch
 PS C:\WINDOWS\system32> New-NetNat -Name "VM-NAT-Network" -InternalIPInterfaceAddressPrefix 192.168.3.1/24

 # Verify that the NAT was created
 PS C:\WINDOWS\system32> Get-NetNat

 # Enable SSH port forwarding on port 2222 of any interface on the host, to a virtual machine with an IP address of 192.168.3.2/24
 PS C:\WINDOWS\system32> Add-NetNatStaticMapping -NatName "VM-NAT-Network" -Protocol TCP -ExternalIPAddress 0.0.0.0 -ExternalPort 2222 -InternalIPAddress 192.168.3.2 -InternalPort 22

 # Verify that the port forward is active
 PS C:\WINDOWS\system32> Get-NetNatStaticMapping

Consult Microsoft's NetNat documentation for a complete list of commands.

For earlier versions and builds of Windows, Internet Connection Sharing can be used. Open Network and Sharing Settings, and Adapter Settings, where you will need to enable internet connection sharing for your internet adapter that you normally use. Once the connection can be shared, add it to a bridge together with the virtual switch that you created in the previous step.

## Virtual machine creation
In the left sidebar, select your computer under "Hyper-V Manager". In the right sidebar, select "New" > "Virtual Machine...". In New Virtual Machine Wizard, you may in general specify whichever settings you like, but some must be specifically configured.

Under "Specify Generation", you may choose "Generation 1" or "Generation 2". Generation 1 virtual machines emulate a BIOS-based machine and legacy ports. Generation 2 provides a UEFI-based machine. In general, use Generation 2 unless for compatibility or portability reasons you need to use Generation 1. Also, when using Generation 2 for an Arch Linux virtual machine, make sure to disable Secure Boot in the virtual machine's settings under Hardware -> Security.

For "Startup memory" under Assign Memory, choose enough to ensure Arch and any programs will run properly.

For "Connection" under "Configure Networking", choose the virtual switch you created earlier.

For "Connect Virtual Hard Disk", choose "Create a virtual hard disk", and make sure the "Size" is appropriate for your use case. The virtual hard disk is sparse, so the virtual hard disk will only use as much real storage as is necessary to store what the virtual OS has written to it.

For "Installation Options", choose "Install an operating system from a bootable CD/DVD-ROM". If you are installing Arch from a disc or USB device, choose "Physical CD/DVD drive" under "Media", and select the appropriate letter. If you are installing Arch from an ISO file, select "Image file (.iso)", and select the file in the "Browse..." dialog. For Generation 2 machines, booting from a physical CD/DVD drive is not supported.

## Virtual machine configuration
Next, you need to configure the virtual machine's settings.

If you like, you can add more virtual processors to your virtual machine. This allows the virtual machine to use more than one of your processor cores, which will increase performance in many cases. If you plan to use the virtual machine intensively, you may wish to allot up to half of your processor cores. To change the number of virtual processors, select "Processor" in the left sidebar, then adjust "Number of virtual processors".

Change any settings, then select "OK" to apply your changes and exit the settings dialog.

## Arch installation
Once the virtual machine is fully configured, you are ready to install Arch. In the right sidebar, select Start > Connect..., and a connection window will open. The network should work automatically when the Arch installation media is running; check by using  on an address you know is responding, e.g.:

 $ ping ping.archlinux.org

If no response is received, the connection is not working. If this is the case, you are probably experiencing a bug Microsoft has acknowledged. You can try installing the hotfix from the Knowledge Base page, or just wait a little while and try again.

In general, you may now install Arch as you would on any other system. The Generation 1 virtual machines are BIOS-only (no UEFI), so you must follow the BIOS-specific instructions for the various boot loaders.

## Post-installation
After installing Arch Linux, you can continue to configure features. To use Hyper-V integration services, install , then start/enable the services  and .

Shut down the virtual machine, open the Settings dialog again, and in the left sidebar, select "DVD Drive" under "IDE Controller" or "SCSI". Under "Media", choose "None". This will stop the virtual machine from trying to boot from the install media on every start.

## File copy daemon
 currently does not install a systemd service for the hv_fcopy_daemon.To configure the file copy feature, create a systemd unit file:

Then start/enable the service .

## Shared directories
Files can be shared between the host and guest with very little effort. First, on the host, choose the folder you want to share with the guest, or create it. Open the Properties dialog for the folder ( +  or right-click and choose "Properties..."). Go to the "Sharing" tab and select "Advanced Sharing...". Activate the "Share this folder" checkbox. By default, the folder will have read-only permissions, meaning the virtual machine can read from the folder but cannot write anything to it. If you would like to modify these permissions, select "Permissions". Here, you choose which users can access the shared folder, and what permissions they have. In general, you will probably be sharing in both directions and should check "Allow" for both "Change" and "Read".
Before exiting the Properties dialog for the shared folder, note its "Network Path", which should be of the form .

Next, you need to find the IP address of the host. Exit the Properties dialog, and open Command Prompt or PowerShell. Run . You should see an entry whose name ends with the name of the virtual switch you created (e.g. ). Under this entry, look for  and note it down.

Next, you need to mount the shared folder from Arch. Boot the virtual machine. Once it is running, you will first need to install , which will allow you to mount CIFS shares (CIFS is the protocol Windows uses for shared folders). Next, you will need to decide where you will be mounting the shared folder. A reasonable choice would be somewhere in , like .

In the command to mount the share, replace any backslashes in the "Network Path" from earlier with forward slashes.

 # mount -t cifs [Network Path with forward slashes mountpoint -o user=you wish to authenticate as,ip=IP noted earlier

You will be prompted for the password for the user you are authenticating as. You can specify the password in the command options via , but this is not a good idea in terms of security as the password for the host will now be in your command history file; or if you are running the command from a script, stored in the script indefinitely. Instead, you can use a credentials file, which allows you to specify your username and password in a file with restricted access rights. It can be called anything; for an example, if it were called  and stored in your home directory, it would be of the following form:

After creating the file, change the permissions to restrict read access:

 chmod 600 ~/.credentials

Then you can add another option to the  command: . Now, when mounting the share, your username and password will automatically be applied.

For a more concrete example, let us say you are mounting a share with a Network Path of  at , where your username on the host is "John" and the host's IP is 198.123.151.23. The mount command would thus be

 # mount -t cifs //PC/share /mnt/Hyper-V -o credentials=~/.credentials,ip=198.123.151.23

One problem with this method is that if the host's IP ever changes (e.g. it has a dynamic IP assigned via DHCP, or moves to a new network), every instance of the host's IP on the guest must be replaced. However, the  package provides , a utility which finds the IP address associated with an SMB host. Thus, in the case of the example above, you would run

You only want the IP address, so you can use  and  to parse it:

Then you can simply replace the IP address in the  command:

 # mount -t cifs //PC/share /mnt/Hyper-V -o credentials=~/.credentials,ip="$(nmblookup PC | head -n 1 | cut -d ' ' -f 1)"

More ways to mount shared folders, including automatic mounting on startup, are detailed in the Samba article.

## Xorg
Graphical programs can easily be run via Xorg via the  package. Simply install it and the window manager or desktop environment you wish to use, and you should be able to start X without issue.

## Setting resolution
Screen resolution is fixed after start-up. It can be adjusted by adding  to the kernel parameters, up to a maximum size of 1920x1080 (the actual limitation is 8MB of frame buffer memory).

If changing boot options has not worked and Powershell is installed, use the  command within Powershell. Documentation for the command can be found on the Microsoft page Whichever resolution is chosen in the command must also be reflected in the boot config, like what has been previously mentioned. An example of this would be to follow the relevant config changes already mentioned, replacing any  with , and performing the following command in Powershell:

## Enhanced session mode
By default, you may suffer from poor mouse and desktop experience. [https://blogs.technet.microsoft.com/virtualization/2018/02/28/sneak-peek-taking-a-spin-with-enhanced-linux-vms/ Enhanced session mode features better mouse and video experience and integrated clipboard. This mode utilizes Xrdp and  kernel module. Run the following code to enable this mode in the guest:

Edit  to start your own desktop environment when log in a Xrdp session. Refer xinit to configure .

Then turn off your Arch virtual machine machine, and then using PowerShell (run as Administrator), you need to enable  on you machine:

After enabling the enhanced session mode, Hyper-V client automatically connects to a Xrdp session after booting.

You can permanently disable enhanced session mode by running the following command on Powershell (run as Administrator):

To connect to a TTY virtual console, you can temporarily disable Enhanced session mode. The Enhanced session mode feature can be enabled or disable for individual machine right from its View menu.

If the power shell prompts that the information related to '-EnhancedSessionTransportType' cannot be found, please make sure that your Windows operating system is the enterprise edition. The professional version does not seem to support it.

If the above doesn't work maybe you can refer to https://github.com/k247tEK/archVM-Hyper-V.

## Tips and tricks
You can also do X-forwarding to get a better experience than Hyper-V's default client. One way to do this is by using a VNC server like TigerVNC and connect to it from Windows. Alternatively, a better way to do this is to install a Windows X Server like VcXsrv (free) or x410 (commercial) and do X-forwarding to get a faster GUI experience. X410 has support for vsock which is more reliable than TCP/IP connection.

Xrdp ( with ) provides a convenient and simple way to connect to Arch Linux virtual machine GUI with remote desktop client
