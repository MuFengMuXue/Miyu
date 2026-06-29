# NAME

pcilib - a library for accessing PCI devices

# DESCRIPTION

The PCI library (also known as *pcilib* and *libpci*) is a portable library for accessing PCI devices and their configuration space.

# ACCESS METHODS

The library supports a variety of methods to access the configuration space on different operating systems. By default, the first matching method in this list is used, but you can specify override the decision (see the **-A** switch of *lspci*).

**linux-sysfs**
The **/sys** filesystem on Linux 2.6 and newer. The standard header of the config space is available to all users, the rest only to root. Supports extended configuration space, PCI domains, VPD (from Linux 2.6.26), physical slots (also since Linux 2.6.26) and information on attached kernel drivers.

**linux-proc**
The **/proc/bus/pci** interface supported by Linux 2.1 and newer. The standard header of the config space is available to all users, the rest only to root.

**intel-conf1**
Direct hardware access via Intel configuration mechanism 1. Available on i386 and compatibles on Linux, Solaris/x86, GNU Hurd, Windows, BeOS and Haiku. Requires root privileges.

**intel-conf2**
Direct hardware access via Intel configuration mechanism 2. Available on i386 and compatibles on Linux, Solaris/x86, GNU Hurd, Windows, BeOS and Haiku. Requires root privileges. Warning: This method is able to address only the first 16 devices on any bus and it seems to be very unreliable in many cases.

**mmio-conf1**
Direct hardware access via Intel configuration mechanism 1 via memory-mapped I/O. Mostly used on non-i386 platforms. Requires root privileges. Warning: This method needs to be properly configured via the **mmio-conf1.addrs** parameter.

**mmio-conf1-ext**
Direct hardware access via Extended PCIe Intel configuration mechanism 1 via memory-mapped I/O. Mostly used on non-i386 platforms. Requires root privileges. Warning: This method needs to be properly configured via the **mmio-conf1-ext.addrs** parameter.

**ecam**
Direct hardware access via PCIe ECAM (Enhanced Configuration Access Mechanism). Available on all PCIe-compliant hardware. Requires root privileges and access to physical memory (on Linux systems disabled CONFIG_STRICT_DEVMEM option). On ACPI compatible systems ECAM mapping is read from the MCFG table specified by the **ecam.acpimcfg** parameter. On EFI compatible systems, ACPI MCFG table can be located in physical memory via EFI system table specified by the **ecam.efisystab** parameter. On FreeBSD/NetBSD systems, physical address of ACPI MCFG table can be located by kenv or sysctl interface when the **ecam.bsd** parameter is not disabled. On x86 BIOS compatible systems, ACPI MCFG table can be located in physical memory by scanning x86 BIOS memory when the **ecam.x86bios** parameter is not disabled. Alternatively ECAM mappings can be specified by the **ecam.addrs** parameter which takes precedence over ACPI MCFG table. This option is required on systems without ACPI and also on systems without EFI or x86 BIOS.

**fbsd-device**
The **/dev/pci** device on FreeBSD. Requires root privileges.

**aix-device**
Access method used on AIX. Requires root privileges.

**nbsd-libpci**
The **/dev/pci0** device on NetBSD accessed using the local libpci library.

**obsd-device**
The **/dev/pci** device on OpenBSD. Requires root privileges.

**dump**
Read the contents of configuration registers from a file specified in the **dump.name** parameter. The format corresponds to the output of *lspci* **-x**.

**darwin**
Access method used on Mac OS X / Darwin. Must be run as root and the system must have been booted with debug=0x144.

**win32-cfgmgr32**
Device listing on Windows systems using the Windows Configuration Manager via cfgmgr32.dll system library. This method does not require any special Administrator rights or privileges. Configuration Manager provides only basic information about devices, assigned resources and device tree structure. There is no access to the PCI configuration space but libpci either tries to use other access method to access configuration space or it provides read-only virtual emulation based on information from Configuration Manager. Other access method can be chosen by the **win32.cfgmethod** parameter. By default the first working one is selected (if any). Starting with Windows 8 (NT 6.2) it is not possible to retrieve resources from 32-bit application or library on 64-bit system.

**win32-sysdbg**
Access to the PCI configuration space via NT SysDbg interface on Windows systems. Process needs to have Debug privilege, which local Administrators have by default. Not available on 64-bit systems and neither on recent 32-bit systems. Only devices from the first domain are accessible and only first 256 bytes of the PCI configuration space is accessible via this method.

**win32-kldbg**
Access to the PCI configuration space via Kernel Local Debugging Driver kldbgdrv.sys. This driver is not part of the Windows system but is part of the Microsoft WinDbg tool. It is required to have kldbgdrv.sys driver installed in the system32 directory or to have windbg.exe or kd.exe binary in PATH. windbg.exe or kd.exe binary contains embedded kldbgdrv.sys driver which libpci can automatically unpack and register. Because of embedded driver usage, it is required that architecture of windbg.exe or kd.exe binary matches the system architecture, and not the libpci application architecture. Therefore for running i386 libpci application on AMD64 system, it is required to have AMD64 version of kldbgdrv.sys driver in the native system32 directory or AMD64 version of windbg.exe or kd.exe binary in the PATH. i386 versions of these binaries would not work. win32-kldbg access method compiled for 32-bit applications supports both 32-bit and also 64-bit OS host systems, therefore i386 libpci application with win32-kldbg method can access PCI config space also on AMD64 host system. kldbgdrv.sys driver has some restrictions. Process needs to have Debug privilege and Windows system has to be booted with Debugging option. Debugging option can be enabled by calling (takes effect after next boot): **bcdedit /debug on**

Download links for WinDbg 6.12.2.633 standalone installer from Microsoft Windows SDK for Windows 7 and .NET Framework 4:
amd64: https://download.microsoft.com/download/A/6/A/A6AC035D-DA3F-4F0C-ADA4-37C8E5D34E3D/setup/WinSDKDebuggingTools_amd64/dbg_amd64.msi
ia64: https://download.microsoft.com/download/A/6/A/A6AC035D-DA3F-4F0C-ADA4-37C8E5D34E3D/setup/WinSDKDebuggingTools_ia64/dbg_ia64.msi
x86: https://download.microsoft.com/download/A/6/A/A6AC035D-DA3F-4F0C-ADA4-37C8E5D34E3D/setup/WinSDKDebuggingTools/dbg_x86.msi

Archived download links of previous WinDbg versions:
https://web.archive.org/web/20110221133326/https://www.microsoft.com/whdc/devtools/debugging/installx86.mspx
https://web.archive.org/web/20110214012715/https://www.microsoft.com/whdc/devtools/debugging/install64bit.mspx

**aos-expansion**
Access method used on PowerPC Amiga running OS4+. Access is made through Expansion.library. It offers read and write access to configuration space.

**rt-thread-smart**
The **/proc/pci** filesystem provided by RT-Thread Smart OS. This method requires PCI support (with the procfs feature enabled) to be available in the driver subsystem, and the DFS v2-based procfs must be mounted in a rootfs-enabled environment. It provides access to the standard PCI configuration space, with limited information available.

# PARAMETERS

The library is controlled by several parameters. They should have sensible default values, but in case you want to do something unusual (or even something weird), you can override them (see the **-O** switch of *lspci*).

## Parameters of specific access methods

**dump.name**
Name of the bus dump file to read from.

**fbsd.path**
Path to the FreeBSD PCI device.

**nbsd.path**
Path to the NetBSD PCI device.

**obsd.path**
Path to the OpenBSD PCI device.

**proc.path**
Path to the procfs bus tree.

**sysfs.path**
Path to the sysfs device tree.

**rt-thread-smart-dm.path**
Path to the rt-thread smart DM procfs device tree.

**devmem.path**
Path to the /dev/mem device or path to the \Device\PhysicalMemory NT section or name of the platform specific physical address access method. Generally on POSIX systems it is path to memory device and on Windows systems it is path to memory NT section. Additionally on 32-bit Windows systems are recognized also platform methods: *vxdcall*, *w32skrnl*. On DOS/DJGPP systems are recognized only platform methods: *auto*, *devmap*, *physmap*. DJGPP's *devmap* method uses DPMI 1.0 functions 0508H (Map Device in Memory Block) and 0509H (Map Conventional Memory in Memory Block). DJGPP's *physmap* method uses DPMI 0.9 function 0800H (Physical Address Mapping). DJGPP's *auto* parameter automatically chooses one of the mentioned method supported by the system.

**mmio-conf1.addrs**
Physical addresses of memory-mapped I/O ports for Intel configuration mechanism 1. CF8 (address) and CFC (data) I/O port addresses are separated by slash and multiple addresses for different PCI domains are separated by commas. Format: 0xaddr1/0xdata1,0xaddr2/0xdata2,...

**mmio-conf1-ext.addrs**
Physical addresses of memory-mapped I/O ports for Extended PCIe Intel configuration mechanism 1. It has same format as **mmio-conf1.addrs** parameter.

**ecam.addrs**
Physical addresses of PCIe ECAM mappings. Each mapping must contains first PCI bus number and physical address where mapping starts. And then it may contain the length of the mapping, the last PCI bus number and PCI domain number. When the last PCI bus number is not provided then it is calculated from the length of the mapping or it is assumed 0xff. When length of the mapping is provided then it is calculated from the last PCI bus number. And when PCI domain is not provided then 0x0 is assumed. All numbers must be supplied in hexadecimal form (leading prefix 0x is not required). Multiple mappings are separated by commas. Format: \[domain:\]start_bus\[-end_bus\]:start_addr\[+length\],...

**ecam.acpimcfg**
Path to the ACPI MCFG table. Processed by the **glob**(3) function, so it may contain wildcards (\*).

**ecam.efisystab**
Path to the EFI system table.

**ecam.bsd**
When not set to 0 then use BSD kenv or sysctl to find ACPI MCFG table. Default value is 1 on BSD systems.

**ecam.x86bios**
When not set to 0 then scan x86 BIOS memory for ACPI MCFG table. Default value is 1 on x86 systems.

**win32.cfgmethod**
Config space access method to use with win32-cfgmgr32 on Windows systems. Value *auto* or an empty string selects the first access method which supports access to the config space on Windows. Value *win32-cfgmgr32* or *none* only builds a read-only virtual emulated config space with information from the Configuration Manager.

## Parameters for resolving of IDs via DNS

**net.domain**
DNS domain containing the ID database.

**net.cache_name**
Name of the file used for caching of resolved IDs. An initial **$HOME/** is expanded to the user's home directory.

## Parameters for resolving of IDs via UDEV's HWDB

**hwdb.disable**
Disable use of HWDB if set to a non-zero value.

# SEE ALSO

**lspci**(8), **setpci**(8), **pci.ids**(5), **update-pciids**(8)

# AUTHOR

The PCI Utilities are maintained by Martin Mares \<mj@ucw.cz\>.
