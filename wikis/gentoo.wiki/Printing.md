This page contains [[changes](https://wiki.gentoo.org/index.php?title=Printing&oldid=1387783&diff=1420890)] which are not marked for translation.

Other languages:

-   [English]
-   [español](https://wiki.gentoo.org/wiki/Printing/es "Impresión (59% translated)")
-   [français](https://wiki.gentoo.org/wiki/Printing/fr "Impression (48% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Printing/hu "Nyomtatás (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Printing/ru "Печать (65% translated)")
-   [中文](https://wiki.gentoo.org/wiki/Printing/zh "打印 (63% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Printing/ja "印刷 (88% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Printing/ko "Printing/ko (57% translated)")

**Resources**

[[]][Home](https://www.cups.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/CUPS "wikipedia:CUPS")

[[]][net-print/cups](https://packages.gentoo.org/packages/net-print/cups)

[[]][net-print/cups-meta](https://packages.gentoo.org/packages/net-print/cups-meta)

[[]][net-print/cups-filters](https://packages.gentoo.org/packages/net-print/cups-filters)

[[]][Bugs (upstream)](https://github.com/openprinting/cups-filters/issues)

[[]][GitHub](https://github.com/apple/cups)

This document covers the installation and maintenance of printers using CUPS and [Samba](https://wiki.gentoo.org/wiki/Samba "Samba"). It covers local installation and networked installations and contains instructions on using shared printers from other operating systems.

For background information on standards related to printing, such as IPP, AirPrint and IPP Everywhere, refer to the [Printing/Standards](https://wiki.gentoo.org/wiki/Printing/Standards "Printing/Standards") page.

For information about printers that support \'driverless printing\', refer to [this OpenPrinting database](https://openprinting.github.io/printers/).

For information about printers that require a driver, and the level of Linux support for such models, refer to [this OpenPrinting database](https://openprinting.org/printers).

For information about using the [lp] or [lpr] commands for printing documents see [CUPS\' excellent upstream documentation](https://www.cups.org/doc/options.html) or [this section](https://wiki.gentoo.org/wiki/Printing#Printing_from_the_command_line "Printing").

## Contents

-   [[1] [Printing and Gentoo Linux]](#Printing_and_Gentoo_Linux)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
        -   [[2.1.1] [Locally attached printer (LPT)]](#Locally_attached_printer_.28LPT.29)
        -   [[2.1.2] [Locally attached printer (USB)]](#Locally_attached_printer_.28USB.29)
        -   [[2.1.3] [Remotely attached printer (IPP and LPD)]](#Remotely_attached_printer_.28IPP_and_LPD.29)
        -   [[2.1.4] [Remotely attached printer (CIFS)]](#Remotely_attached_printer_.28CIFS.29)
    -   [[2.2] [USE flags]](#USE_flags)
    -   [[2.3] [Emerge]](#Emerge)
        -   [[2.3.1] [Recommendations]](#Recommendations)
-   [[3] [Samba]](#Samba)
-   [[4] [Avahi]](#Avahi)
-   [[5] [Configuration]](#Configuration)
    -   [[5.1] [Printing group]](#Printing_group)
    -   [[5.2] [Service]](#Service)
        -   [[5.2.1] [OpenRC]](#OpenRC)
        -   [[5.2.2] [systemd]](#systemd)
    -   [[5.3] [HTTP interface]](#HTTP_interface)
    -   [[5.4] [Files]](#Files)
    -   [[5.5] [Remote printer access]](#Remote_printer_access)
    -   [[5.6] [CUPS remote administration]](#CUPS_remote_administration)
    -   [[5.7] [Enable support for Windows PCL drivers]](#Enable_support_for_Windows_PCL_drivers)
    -   [[5.8] [Setting up a remote printer]](#Setting_up_a_remote_printer)
    -   [[5.9] [Configuring a printer]](#Configuring_a_printer)
        -   [[5.9.1] [Introduction]](#Introduction)
        -   [[5.9.2] [Detecting the printer]](#Detecting_the_printer)
        -   [[5.9.3] [Listing available drivers]](#Listing_available_drivers)
        -   [[5.9.4] [Installing the printer]](#Installing_the_printer)
        -   [[5.9.5] [Testing and reconfiguring the printer]](#Testing_and_reconfiguring_the_printer)
        -   [[5.9.6] [Installing the best driver]](#Installing_the_best_driver)
        -   [[5.9.7] [Enabling job accounting in for Xerox printers]](#Enabling_job_accounting_in_for_Xerox_printers)
    -   [[5.10] [Using special printer drivers]](#Using_special_printer_drivers)
        -   [[5.10.1] [Introduction]](#Introduction_2)
        -   [[5.10.2] [Gutenprint driver]](#Gutenprint_driver)
        -   [[5.10.3] [HPLIP driver]](#HPLIP_driver)
        -   [[5.10.4] [Lexmark driver]](#Lexmark_driver)
        -   [[5.10.5] [PNM2PPA driver]](#PNM2PPA_driver)
        -   [[5.10.6] [SpliX driver]](#SpliX_driver)
        -   [[5.10.7] [Brother printer drivers]](#Brother_printer_drivers)
        -   [[5.10.8] [Canon printer drivers]](#Canon_printer_drivers)
    -   [[5.11] [Printing to and from Microsoft Windows]](#Printing_to_and_from_Microsoft_Windows)
        -   [[5.11.1] [Configuring a Windows client for IPP]](#Configuring_a_Windows_client_for_IPP)
        -   [[5.11.2] [Configuring a Windows client for a Samba-shared printer]](#Configuring_a_Windows_client_for_a_Samba-shared_printer)
        -   [[5.11.3] [Configuring a Linux client for a Windows print server]](#Configuring_a_Linux_client_for_a_Windows_print_server)
    -   [[5.12] [Printing-related applications]](#Printing-related_applications)
        -   [[5.12.1] [Introduction]](#Introduction_3)
        -   [[5.12.2] [Gtk-LP - A GTK-powered printer configuration tool]](#Gtk-LP_-_A_GTK-powered_printer_configuration_tool)
        -   [[5.12.3] [Printer configuration tool for KDE Plasma]](#Printer_configuration_tool_for_KDE_Plasma)
-   [[6] [Printing from the command line]](#Printing_from_the_command_line)
-   [[7] [Removal]](#Removal)
    -   [[7.1] [USE flags]](#USE_flags_2)
    -   [[7.2] [Unmerge]](#Unmerge)
-   [[8] [Troubleshooting]](#Troubleshooting)
    -   [[8.1] [Debugging]](#Debugging)
    -   [[8.2] [Error: No such file or directory]](#Error:_No_such_file_or_directory)
    -   [[8.3] [Error: Unable to convert file 0 to printable format]](#Error:_Unable_to_convert_file_0_to_printable_format)
    -   [[8.4] [Error: Send-Document client-error-document-format-not-supported: Unsupported document-format \"application/postscript\"]](#Error:_Send-Document_client-error-document-format-not-supported:_Unsupported_document-format_.22application.2Fpostscript.22)
    -   [[8.5] [USB printer is not detected]](#USB_printer_is_not_detected)
-   [[9] [See also]](#See_also)
-   [[10] [External resources]](#External_resources)

## [Printing and Gentoo Linux]

In this document we will cover how to use CUPS, the [Common Unix Printing System](https://www.cups.org/), to set up a local or networked printer. It will not go into too much detail since the project has [documentation](https://www.cups.org/documentation.html) available for advanced usage.

## [Installation]

### [Kernel]

When a user desires to install a printer on a system the first step is knowing how the printer will be attached to the system. Is it through a local port like LPT or USB, or is it networked? If it is networked, does it use the Internet Printing Protocol (IPP) or the Microsoft Windows CIFS protocol (Microsoft Windows Sharing)?

The next few sections explain what minimal kernel configuration is needed to get a printer connected in Gentoo. Of course, this depends on *how* the printer is going to be attached to the system, so for convenience the instructions have been separated.

Navigate to [/usr/src/linux] and run [make menuconfig] to enter the kernel configuration. If [genkernel] was used to configure the kernel, these steps should still be performed to make sure nothing was missed. Do not rely on genkernel to configure everything in the system automatically; printing is an area configuration settings are difficult to automatically set.

In the next configuration examples, the necessary support will be added *into* the kernel, not as modules. Building the kernel this way is not mandatory; if desired modular support can be easily added, just be sure to remember to load the appropriate modules!

Now go to the appropriate section to configure (or check) the kernel.

#### [][Locally attached printer (LPT)]

The LPT port is generally used to identify the parallel printer port. You need to enable parallel port support first, then PC-style parallel port support (unless using a SPARC system) after which you enable parallel printer support.

[KERNEL] **Parallel Port printer configuration**

    Device Drivers --->
      <*> Parallel port support  --->
        <*> PC-style hardware
        [*] IEEE 1284 transfer modes
      Character devices  --->
        <*> Parallel printer support

** Note**\
Some users might may to enable other options in the `Parallel port support` section. Check the kernel configuration `Help` function for more information.

That\'s it! Exit the kernel configuration and [rebuild the kernel](https://wiki.gentoo.org/wiki/Kernel/Rebuild "Kernel/Rebuild").

Now continue with CUPS.

#### [][Locally attached printer (USB)]

USB printing is supported by CUPS with the [USB USE flag enabled](https://wiki.gentoo.org/wiki/Printing#Installation "Printing"). This uses the libusb library for user space USB support.

Some older software titles might still require the in-kernel USB printer support. If built as a module, this module would be called [usblp]:

[KERNEL] **USB Printer support**

    Symbol: USB_PRINTER [=n]
    Type  :tristate
    Prompt: USB Printer support
      Location:
        -> Device Drivers
          -> USB support (USB_SUPPORT [=y])
    (1)     -> Support for Host-side USB (USB [=y])
      Defined at drivers/usb/class/Kconfig:21
      Depends on: USB_SUPPORT [=y] && USB [=y]

However, using the in-kernel USB printer support is [considered obsolete](https://forums.gentoo.org/viewtopic-t-1053530-start-10.html). Only pursue this when needed.

** Note**\
When using a USB to parallel port adapter, CUPS will not be able to detect the printer. As a workaround, add the printer using a different connection type and then change the DeviceURI directive in [printers.conf] and restart the cupsd service:

[FILE] **`/etc/cups/printers.conf`Modify DeviceURI**

    # DeviceURI usb:/dev/usb/lp0  replace this line with
    DeviceURI parallel:/dev/usb/lp0

#### [][Remotely attached printer (IPP and LPD)]

To be able to connect to a remotely attached printer through the [Internet Printing Protocol](https://en.wikipedia.org/wiki/Internet_Printing_Protocol "wikipedia:Internet Printing Protocol") or the [Line Printer Daemon protocol](https://en.wikipedia.org/wiki/Line_Printer_Daemon_protocol "wikipedia:Line Printer Daemon protocol") the kernel needs to have networking support. Assuming the kernel has that already, continue with CUPS.

#### [][Remotely attached printer (CIFS)]

The kernel must [support CIFS](https://wiki.gentoo.org/wiki/Samba/Guide#Mounting_a_Windows_or_Samba_share_in_GNU.2FLinux "Samba/Guide"):

[KERNEL] **CIFS printer configuration**

    File systems -->
      Network File Systems -->
        <*> SMB3 and CIFS support (advanced network filesystem)

After configuration for CIFS is complete, exit the kernel configuration and rebuild the kernel. Do not forget to copy the new kernel image to the [/boot] location (and don\'t forget to mount [/boot] if needed) and update the boot loader configuration prior to rebooting the system. Note the root commands in the **LPT Printer Configuration** step above for how to perform these steps.

Now continue with the next steps in the CUPS installation process.

### [USE flags]

Some packages are aware of the [[[cups]](https://packages.gentoo.org/useflags/cups)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"). CUPS has a few optional features that might be of interest. To enable or disable those features, use the USE flags associated with them.

### [USE flags for] [net-print/cups](https://packages.gentoo.org/packages/net-print/cups) [[]] [The Common Unix Printing System]

  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                       Add support for X11
  [`acl`](https://packages.gentoo.org/useflags/acl)                   Add support for Access Control Lists
  [`dbus`](https://packages.gentoo.org/useflags/dbus)                 Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`debug`](https://packages.gentoo.org/useflags/debug)               Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)         Add kerberos support
  [`openssl`](https://packages.gentoo.org/useflags/openssl)           Use dev-libs/openssl instead of net-libs/gnutls for TLS support
  [`pam`](https://packages.gentoo.org/useflags/pam)                   Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`selinux`](https://packages.gentoo.org/useflags/selinux)           !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static-libs`](https://packages.gentoo.org/useflags/static-libs)   Build static versions of dynamic libraries as well
  [`systemd`](https://packages.gentoo.org/useflags/systemd)           Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                 Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`usb`](https://packages.gentoo.org/useflags/usb)                   Add USB support to applications that have optional USB support (e.g. cups)
  [`xinetd`](https://packages.gentoo.org/useflags/xinetd)             Add support for the xinetd super-server
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)         Support for DNS Service Discovery (DNS-SD)
  ------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-21 16:30] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Check the current USE flag settings. To deviate from the current USE settings for CUPS alone, add the appropriate USE flags to [/etc/portage/package.use] file.

`user `[`$`]`emerge -pv net-print/cups`

    [ebuild N     ] net-print/cups-1.7.3  USE="X acl dbus pam ssl threads usb -debug -gnutls -java -kerberos -lprng-compat -python (-selinux) -static-libs -systemd -xinetd -zeroconf" ABI_X86="(64) (-32) (-x32)" LINGUAS="ca es fr it ja pt_BR ru" PYTHON_SINGLE_TARGET="python2_7" PYTHON_TARGETS="python2_7" 0 kB

### [Emerge]

When happy with the result, ask Portage to install CUPS:

`root `[`#`]`emerge --ask net-print/cups`

#### [Recommendations]

To avoid any future errors or headaches when using CUPS, you should also install the [[[net-print/cups-meta]](https://packages.gentoo.org/packages/net-print/cups-meta)[]] package.

### [USE flags for] [net-print/cups-meta](https://packages.gentoo.org/packages/net-print/cups-meta) [[]] [Metapackage for a fully configured cups printer setup]

  ------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------
  [`+browsed`](https://packages.gentoo.org/useflags/+browsed)         Include support for the cups-browsed daemon.
  [`+foomatic`](https://packages.gentoo.org/useflags/+foomatic)       Include support for the foomatic-rip printer driver. Strongly recommended.
  [`+poppler`](https://packages.gentoo.org/useflags/+poppler)         Include support for the app-text/poppler filters.
  [`+postscript`](https://packages.gentoo.org/useflags/+postscript)   Enable support for the PostScript language (often with ghostscript-gpl or libspectre)
  [`pdf`](https://packages.gentoo.org/useflags/pdf)                   Add general support for PDF (Portable Document Format), this replaces the pdflib and cpdflib flags
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)         Support for DNS Service Discovery (DNS-SD)
  ------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-25 03:57] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

`root `[`#`]`emerge --ask net-print/cups-meta`

## [Samba]

To enable [Samba](https://wiki.gentoo.org/wiki/Samba "Samba") support, [[[net-fs/samba]](https://packages.gentoo.org/packages/net-fs/samba)[]] needs to be installed with CUPS support. Update the [/etc/portage/package.use] file or directory to enable the `cups` USE flag:

[FILE] **`/etc/portage/package.use`Enabling cups USE flag for Samba**

    net-fs/samba cups

Then (re)install Samba:

`root `[`#`]`emerge --ask --changed-use net-fs/samba`

## [Avahi]

CUPS uses [Avahi](https://wiki.gentoo.org/wiki/Avahi "Avahi") internally when built with the `zeroconf` USE flag to scan for printers on the local network. To use Avahi hostnames to connect to networked printers, set up .local hostname resolution and restart the CUPS service. CUPS and cups-filters need to be built with the `zeroconf` USE flag as well. Use the [[[driverless(1)]](https://man.archlinux.org/man/driverless.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] command (provided by the [[[net-print/cups-filters]](https://packages.gentoo.org/packages/net-print/cups-filters)[]] package) for listing available printers.

`user `[`$`]`driverless list`

## [Configuration]

### [Printing group]

Any user that needs to print should be added to the [lp] group:

`root `[`#`]`gpasswd -a username lp`

In order to be able to add printers and edit them via CUPS\'s web interface, any system user that is allowed to edit these settings should be in the [lpadmin] group:

`root `[`#`]`gpasswd -a username lpadmin`

### [Service]

#### [OpenRC]

If the printer is attached to the system locally, and the printer needs to be available every boot, the CUPS daemon will need to load automatically on start-up. Make sure the printer is attached and powered on before the CUPS daemon is started.

`root `[`#`]`rc-service cupsd start `

`root `[`#`]`rc-update add cupsd default `

#### [systemd]

To start the CUPS daemon immediately and to make it start when the system boots, issue:

`root `[`#`]`systemctl start cups.service `

`root `[`#`]`systemctl enable cups.service `

### [HTTP interface]

Once the service is started, printers can be added by authenticated users. root is available by default and any member of the [lpadmin] group. Open up the following URL in a web browser:

[http://localhost:631/](http://localhost:631/)

### [Files]

The default CUPS server configuration located in [/etc/cups/cupsd.conf] is sufficient for most users. However, some users might need to make changes to the CUPS configuration.

In the next section covers a few changes that are often needed:

-   Allow other systems to use the printer attached to this Linux workstation.
-   Grant access to the CUPS administration from remote systems.
-   Configure CUPS to support Windows PCL drivers. This is advised for Windows systems to be able to use a [Samba](https://wiki.gentoo.org/wiki/Samba "Samba")-shared printer since most Windows drivers are PCL drivers.
-   Configure this system to use a printer attached to another system (not Windows share).

### [Remote printer access]

For other systems to use the printer through IPP, explicit access to the printer must be granted in the [/etc/cups/cupsd.conf] file. To share the printer using [Samba](https://wiki.gentoo.org/wiki/Samba "Samba"), this change is not needed.

Open up [/etc/cups/cupsd.conf] in a favorite text editor and add in an `Allow` line for the system(s) that should be able to reach to the printer. In the next example, access is granted to the printer from localhost and from any system whose IP address starts with `192.168.0`.

[FILE] **`/etc/cups/cupsd.conf`Allowing remote access to the printer**

    <Location />
      Order allow,deny
      Allow localhost
      Allow from 192.168.0.*
    </Location>

This line broadcasts browsing information to the clients on the network; it will let network users know when the printer is available:

[FILE] **`/etc/cups/cupsd.conf`Broadcast info**

    BrowseAddress 192.168.0.*:631

The port CUPS listens to will also need to be specified so that it will respond to printing requests from other machines on the network:

[FILE] **`/etc/cups/cupsd.conf`Port configuration**

    Listen *:631
    #Listen localhost:631

The CUPS server reject a hostname or server alias in the HTTP request with \"Bad request\" message. It works with IP-addresses by default. So if you want to print or browse CUPS interface by using a hostname or domain, add the ServerAlias parameter:

[FILE] **`/etc/cups/cupsd.conf`Server alias configuration**

    ServerAlias *

### [CUPS remote administration]

If remote administration is needed, then access to the CUPS administration will need to be granted from more systems than the localhost. Edit the [/etc/cups/cupsd.conf] file and have explicit access granted to each system that requires access. For instance, to grant access to a system with an IP address of 192.168.0.3:

[FILE] **`/etc/cups/cupsd.conf`Allowing remote access**

    <Location /admin>
    (...)
      Encryption Required
      Order allow,deny
      Allow localhost
      Allow 192.168.0.3
    </Location>

Do not forget to restart the CUPS daemon after making changes to [/etc/cups/cupsd.conf] by issuing the [/etc/init.d/cupsd restart] command (for OpenRC users) or [systemctl restart cupsd.service] (for systemd users).

### [Enable support for Windows PCL drivers]

PCL drivers send raw data to the print server. To enable raw printing on CUPS, edit [/usr/share/cups/mime/mime.types] and uncomment the `application/octet-stream` line if it is not already uncommented. Then edit [/usr/share/cups/mime/mime.convs] and do the same, if it is not already uncommented.

[FILE] **`/usr/share/cups/mime/mime.types`Enable support for raw printing**

    application/octet-stream

[FILE] **`/usr/share/cups/mime/mime.convs`**

    application/octet-stream     application/vnd.cups-raw    0    -

Do not forget to restart the CUPS daemon after making these changes by running [/etc/init.d/cupsd restart] (for OpenRC users) or [systemctl restart cupsd.service] (for systemd users).

### [Setting up a remote printer]

If the printers are attached to a remote CUPS-powered server the system can be easily configured to use the remote printer by modifying the [/etc/cups/client.conf] file.

Assuming the printer is attached to a system called `printserver.mydomain`, open up [/etc/cups/client.conf] with a favorite text editor and set the `ServerName` directive:

[FILE] **`/etc/cups/client.conf`**

    # (Substitute printserver.mydomain with your print server name)
    ServerName printserver.mydomain

The remote system will have a default printer setting which will be used. To change the default printer, use the [lpoptions] command.

First list the available printers:

`root `[`#`]`lpstat -a`

    hpljet5p accepting requests since Jan 01 00:00
    hpdjet510 accepting requests since Jan 01 00:00

Set the HP LaserJet 5P as the default printer:

`root `[`#`]`lpoptions -d hpljet5p`

### [Configuring a printer]

#### [Introduction]

If the printer to be configured is remotely available through a different print server (running CUPS) then the following instructions are not needed. Instead, read [Setting up a Remote Printer](https://wiki.gentoo.org/wiki/Printing#Setting_up_a_remote_printer "Printing").

#### [Detecting the printer]

If a USB printer or parallel port printer was powered on when the Linux system booted, it might be possible to retrieve information from the kernel stating successful detection of the printer. This is merely an indication of print detection and not a requirement.

`user `[`$`]`dmesg | grep -i print`

    parport0: Printer, Hewlett-Packard HP LaserJet 2100 Series

For a USB connected printer:

`user `[`$`]`lsusb`

    (...)
    Bus 001 Device 007: ID 03f0:1004 Hewlett-Packard DeskJet 970c/970cse

\
The [[lpinfo](https://www.cups.org/doc/man-lpinfo.html)] command can be used in order to list all connected printers:

`root `[`#`]`lpinfo -v`

    network ipp
    network http
    network socket
    network https
    network ipps
    network lpd
    network lpd://BRW67890ABCDEF/BINARY_P1

Running [lpinfo -l -v] will give a more verbose output.

\

#### [Listing available drivers]

To list all available drivers, execute the following command:

`user `[`$`]`lpinfo -m`

[lpinfo] is not chatty and can be a little tricky to use. If any issue arises, see [man lpinfo] for more information.

#### [Installing the printer]

To have the printer installed on the system, fire up a browser and point it to [http://localhost:631](http://localhost:631). The CUPS web interface should be displayed from which all administrative tasks can be performed.

** Note**\
If an HTTPS connection to CUPS is used the first time the interface is accessed it *may* take a very long time before the page appears. This is because the first request triggers the generation of CUPS SSL certificates which can be a time-consuming job.

Go to [Administration] and enter the root login and password information of the box. Then, when the administrative interface has been reached, click on [Add Printer]. A new screen will be displayed allowing the following information to be entered:

-   The *spooler name*, a short but descriptive name used on the system to identify the printer. This name should not contain spaces or any special characters. For instance, for the HP LaserJet 5P could be titled `hpljet5p`.
-   The *location*, a description where the printer is physically located (for instance \"bedroom\", or \"in the kitchen right next to the dish washer\", etc.). This is to aid in maintaining several printers.
-   The *description*, a full description of the printer. A common use is the full printer name (like \"HP LaserJet 5P\").

The next screen requests the device the printer listens to. The choice of several devices will be presented. The next table covers a few possible devices, but the list is not exhaustive.

  ------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------
  Device                                     Description
  AppSocket/HP JetDirect                     This special device allows for network printers to be accessible through a HP JetDirect socket. Only specific printers include support for this option.
  Internet Printing Protocol (IPP or HTTP)   Used reach the remote printer through the IPP protocol either directly (IPP) or through HTTP.
  LPD/LPR Host or Printer                    Select this option if the printer is remote and attached to a LPD/LPR server.
  Parallel Port #1                           Select when the printer is locally attached to a parallel port (LPT). When the printer is automatically detected its name will be appended to the device.
  USB Printer #1                             Select when the printer is locally attached to a USB port. The printer name should automatically be appended to the device name.
  ------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------

If installing a remote printer, the URL to the printer will be queried:

-   An LPD printer server requires a `lpd://hostname/queue` syntax.
-   An HP JetDirect printer requires a `socket://hostname` syntax.
-   An IPP printer requires a `ipp://hostname/printers/printername` or `http://hostname:631/printers/printername` syntax.

** Note**\
[Models other than \"everywhere\" are deprecated and will not be supported in a future version of CUPS.](https://www.cups.org/doc/man-lpadmin.html#OPTIONS)

Next, select the printer manufacturer in the adjoining screen along with the model type and number in the subsequent screen. For many printers multiple drivers will be available. Select one now or search on [OpenPrinting Printer List](https://www.openprinting.org/printers) for a good driver. Drivers are easily able to be changed later.

Once the driver is selected, CUPS will inform that the printer has been added successfully to the system. Navigate to the printer management page on the administration interface and select [Configure Printer] to change the printer\'s settings (resolution, page format, \...).

#### [Testing and reconfiguring the printer]

To verify if the printer is working correctly, go to the printer administration page, select the printer and click on [Print Test Page].

If the printer does not seem to work correctly, click on [Modify Printer] to reconfigure the printer. The same screens as during the first installation will appear but the defaults will now be the current configuration.

If the printer does not function, clues may be found by looking at the CUPS error log located at [/var/log/cups/error_log]. In the next example a permission error is discovered, probably due to a wrong [Allow] setting in the [/etc/cups/cupsd.conf] file.

`root `[`#`]`tail /var/log/cups/error_log`

    (...)
    E [11/Jun/2005:10:23:28 +0200] [Job 102] Unable to get printer status (client-error-forbidden)!

#### [Installing the best driver]

** Note**\
[Printer drivers are now deprecated (Issue #5270)](https://www.cups.org/doc/relnotes.html#0203b4)\
[PPD files and printer drivers are deprecated and will not be supported in a future version of CUPS.](https://www.cups.org/doc/man-lpadmin.html#DEPRECATED_OPTIONS)\
[Driverless_printing](https://wiki.gentoo.org/wiki/Driverless_printing "Driverless printing")

Many printer drivers exist; to find out which one has the best performance the job, visit the [OpenPrinting Printer List](https://www.openprinting.org/printers). Select the brand and type/model of the printer to find out what driver the site recommends. For instance, for the HP LaserJet 5P, the site recommends the `ljet4` driver.

Download the PPD file from the site and place it in [/usr/share/cups/model] then run [/etc/init.d/cupsd restart] (for OpenRC users) or [systemctl restart cupsd.service] (for systemd users) as root. This will make the driver available through the CUPS web interface. Now reconfigure the printer as described above.

#### [Enabling job accounting in for Xerox printers]

High-end Xerox printers (often a gray, cabinet sized device) use XCPT PDL, and XML based, and poorly documented XPIF ticketing instruction format.

XCPT filter in Cups never made it to a release grade, and the work on it was eventually dropped and all XPIF must be input into a PPD manually. Luckily, it\'s largely a direct copy of IPP, using XML syntax. After peeking into docs available online, we can craft an arbitrary XPIF command using corresponding IPP attributes.

To configure XPIF solely for ticketing/accounting, drop the following into any PPD:

[CODE] **XPIF code for inserting a user id**

    *JCLBegin:"<1B>%-12345X@PJL JOB<0A>"

    *% Base JCL key code option
    *JCLOpenUI JCLPasscode/Key Code: PickOne
    *OrderDependency: 10 JCLSetup *JCLPasscode
    *JCLPasscode None/No Code: ""
    *JCLCloseUI: *JCLPasscode

    *% Custom JCL key code option
    *CustomJCLPasscode True: "@PJL XCPT <?xml version=<22>1.0<22> encoding=<22>UTF-8<22>?>
      @PJL XCPT <!DOCTYPE xpif SYSTEM <22>xpif-v02074.dtd<22><3E>
      @PJL XCPT <xpif version=<22>1.0<22> cpss-version=<22>2.07<22> xml:lang=<22>en-US<22><3E>
      @PJL XCPT          <job-template-attributes>
      @PJL XCPT <09><09><3C>job-accounting-user-id syntax=<22>name<22> xml:space=<22>preserve<22><3E>\1<3C>/job-accounting-user-id>
      @PJL XCPT          </job-template-attributes>
      @PJL XCPT </xpif>"
    *ParamCustomJCLPasscode Code/Key Code: 1 password 0 16

    *JCLEnd:"<1B>%-12345X@PJL EOJ<0A><1B>%-12345X<0A>"

It will draw a dropdown box in any printing ui compliant with CUPS PPD extensions to enter the id.

The long term solution would still be for Xerox to fully publish XPIF, and XCPT specifications, to allow for a proper XPIF cups filter to be developed.

### [Using special printer drivers]

#### [Introduction]

Some printers require specific drivers or provide additional features that are not enabled through the regular configuration process (described above). This chapter will discuss a selection of printers and how they are made to work with Gentoo Linux.

#### [Gutenprint driver]

The [Gutenprint](http://gimp-print.sourceforge.net/) drivers are high-quality, open source printer drivers for various Canon, Epson, HP, Lexmark, Sony, Olympus and PCL printers supporting CUPS. They also support ghostscript, The Gimp, and other applications.

Gentoo\'s Portage tree contains an ebuild for the gutenprint drivers. Run [emerge gutenprint] to install them. Note the ebuild requests to quite a few USE flags. At minimum `cups` and `ppds` must enabled for gutenprint drivers to work properly.

`root `[`#`]`emerge --ask net-print/gutenprint`

When the emerge process has finished, the gutenprint drivers will be available through the CUPS web interface.

#### [HPLIP driver]

See [HPLIP Driver](https://wiki.gentoo.org/wiki/HPLIP "HPLIP").

#### [Lexmark driver]

Most Lexmark printers are handled by their \"Universal Printer Driver\":

`root `[`#`]`emerge --ask net-print/lexmark-upd-ppd`

Once this is installed, there is a single Lexmark driver available in the CUPS setup wizard that should work with most printers and MFDs.

#### [PNM2PPA driver]

PPA is an HP technology that focuses on sending low-level processing to the system instead of the printer which makes the printer cheaper but more resource consuming.

If the [OpenPrinting](https://www.openprinting.org/printers) site informs the [pnm2ppa](http://pnm2ppa.sourceforge.net/) driver is the best option, then the [[[net-print/pnm2ppa]](https://packages.gentoo.org/packages/net-print/pnm2ppa)[]] filter will need to be installed on the system:

`root `[`#`]`emerge --ask net-print/pnm2ppa`

Once installed, download the PPD file for the printer [OpenPrinting](https://www.openprinting.org/printers) and put it in the [/usr/share/cups/model] folder. Then configure the printer using the steps explained above.

#### [SpliX driver]

[SpliX](http://splix.ap2c.org/) is a set of CUPS printer drivers for SPL (Samsung Printer Language) printers. While SpliX drivers are available through [OpenPrinting](https://www.openprinting.org/printers) as well, the [[[net-print/splix]](https://packages.gentoo.org/packages/net-print/splix)[]] package allows for quick portage-managed installation of these drivers. To install, run:

`root `[`#`]`emerge --ask net-print/splix`

and restart [cupsd].

#### [Brother printer drivers]

See [Brother networked printer](https://wiki.gentoo.org/wiki/Brother_networked_printer "Brother networked printer").

#### [Canon printer drivers]

See the specific pages:

-   [Canon CAPT drivers](https://wiki.gentoo.org/wiki/Canon_CAPT_Printer "Canon CAPT Printer")
-   [Canon Pixma drivers](https://wiki.gentoo.org/wiki/Canon_Pixma_Printer "Canon Pixma Printer")

Some Canon printer drivers may require the [[[net-print/cnijfilter2]](https://packages.gentoo.org/packages/net-print/cnijfilter2)[]] package to function properly, to install it, use:

`root `[`#`]`emerge --ask net-print/cnijfilter2`

### [Printing to and from Microsoft Windows]

** Note**\
Read the [Samba/CUPS Guide](https://wiki.gentoo.org/wiki/Samba/Guide "Samba/Guide") for more detailed information on setting up CUPS with Samba.

#### [Configuring a Windows client for IPP]

Microsoft Windows supports IPP. To install a printer on Windows that is attached to a Linux box, fire up the [Add Printer] wizard and select [Network Printer]. When asked for the URI, use the `http://hostname:631/printers/queue` syntax.

#### [Configuring a Windows client for a Samba-shared printer]

To share the printer on the CIFS network, [Samba](https://wiki.gentoo.org/wiki/Samba "Samba") must be installed and configured correctly. Doing this is beyond the scope of this article, however a quick configuration of Samba for shared printers will be covered.

Open [/etc/samba/smb.conf] with a favorite text editor and add a `[printers]` section to it:

[CODE] **\[printers\] section**

    [printers]
      comment      = All printers
      path         = /var/spool/samba
      browseable   = no
      guest ok     = no
      writable     = no
      printable    = yes
      public       = yes
      printer name = hpljet5p

Navigate to the top of the [smb.conf] file until inside the `[global]` section. Locate the `printcap name` and `printing` settings and set each of them to `cups` (see the example below):

[CODE] **Changing the \[global\] section of smb.conf**

    [global]
      (...)
      printcap name = cups
      printing      = cups

Make sure to enable [Windows PCL](https://wiki.gentoo.org/wiki/Printing#Enable_support_for_Windows_PCL_drivers "Printing") support in CUPS. Then, restart the smb service to have the changes take effect.

#### [Configuring a Linux client for a Windows print server]

First make sure the printer is shared on Windows systems and that [[[net-fs/samba]](https://packages.gentoo.org/packages/net-fs/samba)[]] has been emerged with the `cups` USE flag enabled (as instructed above).

To find the desired printer\'s URI, run the following command, substituting `server` with the computer that is to probe for [Samba](https://wiki.gentoo.org/wiki/Samba "Samba")-shared printers:

`user `[`$`]`smbclient -N '\\server\'`

In the CUPS web interface, configure the printer as previously described. Notice CUPS has added another driver called `Windows Printer via SAMBA`. Select it and use the `smb://username:password@workgroup/server/printername` or `smb://server/printername` syntax for the URI.

** Important**\
Any special characters in the above URI need to be appropriately quoted. For example:

`smb://BEN-DESKTOP/HP Color LaserJet CP1510 series PCL6`

becomes:

`smb://BEN-DESKTOP/HP%20Color%20LaserJet%20CP1510%20series%20PCL6`

This result string can be obtained by running the following command:

`user `[`$`]`python2 -c 'import urllib; print "smb://" + urllib.quote("BEN-DESKTOP/HP Color LaserJet CP1510 series PCL6")'`

### [Printing-related applications]

#### [Introduction]

Many tools exist to help configure a printer, use additional printing filters, add features to printing capabilities, etc. This chapter will list a few of them. Be aware the list is not exhaustive and not meant to discuss each tool in great detail.

#### [Gtk-LP - A GTK-powered printer configuration tool]

With [[[net-print/gtklp]](https://packages.gentoo.org/packages/net-print/gtklp)[]], the installation, modification and configuration of a printer can be performed from a stand-alone GTK application. It uses CUPS and provides all standard CUPS capabilities. It is definitely worth checking out if the CUPS Web interface is disliked or if a stand-alone application for day-to-day printing routines is desired.

Install via:

`root `[`#`]`emerge --ask net-print/gtklp`

#### [Printer configuration tool for KDE Plasma]

[KDE Plasma](https://wiki.gentoo.org/wiki/KDE "KDE") also has a printer config tool called [[[kde-plasma/print-manager]](https://packages.gentoo.org/packages/kde-plasma/print-manager)[]]. It works with CUPS and provides a user-friendly interface to configure printers. Install it as follows:

`root `[`#`]`emerge --ask kde-plasma/print-manager`

## [Printing from the command line]

List available printers and the default destination:

`user `[`$`]`lpstat -p -d`

    printer HLL2360D is idle.  enabled since Tue 30 Jul 2024 15:54:45
    no system default destination

List accepting status of all printers:

`user `[`$`]`lpstat -a`

    HLL2360D accepting requests since Tue 30 Jul 2024 15:54:45

Specify a default destination:

`user `[`$`]`lpoptions -d HLL2360D`

List the available options for a given printer, together with their current values:

`user `[`$`]`lpoptions -p HLL2360D -l`

Print a page range:

`user `[`$`]`lpr -o page-ranges=1-4,7,9-12 document.pdf`

For further examples of using CUPS from the command line, refer to [the CUPS \"Command-Line Printing and Options\" page](https://www.cups.org/doc/options.html).

** Note**\
Traditionally, the [[[lpr(1)]](https://man.archlinux.org/man/lpr.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] command was used on BSD-style systems, and the [[[lp(1)]](https://man.archlinux.org/man/lp.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] command was used on SysV-style systems. For backwards compatibility, CUPS provides both commands; refer to their respective man pages for information about the functionality provided by each.

## [Removal]

### [USE flags]

Packages that are currently installed with the `cups` USE flag must be modified. Search through [/etc/portage/package.use] to see if any packages explicitly have the `cups` flag and remove it.

Next, it may be necessary to remove the `cups` value from [/etc/portage/make.conf]\'s `USE` variable if it had been previously set.

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose net-print/cups`

Finally, clean the system of any packages that are no longer needed as a result of CUPS being removed.

`root `[`#`]`emerge --ask --depclean`

## [Troubleshooting]

### [Debugging]

See [archlinux wiki](https://wiki.archlinux.org/index.php/CUPS/Troubleshooting#Introduction)

### [Error: No such file or directory]

This error *may* come up when trying to print if you didn\'t emerge the [[[net-print/cups-meta]](https://packages.gentoo.org/packages/net-print/cups-meta)[]] package, to install it, use:

`root `[`#`]`emerge --ask net-print/cups-meta`

### [Error: Unable to convert file 0 to printable format]

While having printing troubles and [/var/log/cups/error_log] shows this message:

[CODE] **Error log**

    Unable to convert file 0 to printable format

Re-emerge [[[app-text/ghostscript-gpl]](https://packages.gentoo.org/packages/app-text/ghostscript-gpl)[]] with the `cups` USE flag. You can either add `cups` to the system USE flags in [/etc/portage/make.conf] or enable it only for ghostscript-gpl as shown:

`root `[`#`]`echo "app-text/ghostscript-gpl cups" >> /etc/portage/package.use`

Then run [emerge app-text/ghostscript-gpl]. When it has finished compiling, be sure to restart [cupsd] afterward.

When using OpenRC:

`root `[`#`]`rc-service cupsd restart`

When using systemd:

`root `[`#`]`systemctl restart cups`

### [][Error: Send-Document client-error-document-format-not-supported: Unsupported document-format \"application/postscript\"]

If print jobs disappear and the cups error log contains the above error message, ensure that [[[net-print/cups-filters]](https://packages.gentoo.org/packages/net-print/cups-filters)[]] is installed with the [[[postscript]](https://packages.gentoo.org/useflags/postscript)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] `USE` flag.

### [USB printer is not detected]

Assuming that cups is built with the `usb` USE flag, verify that the printer\'s character device has the correct permissions. For example:

`user `[`$`]`lsusb Bus 002 Device 058: ID 04e8:3297 Samsung Electronics Co., Ltd ML-191x/ML-252x Laser Printer`

There should be a character device for this printer at [/dev/bus/usb/002/058].

`user `[`$`]`ls -l /dev/bus/usb/002/058 crw-rw-r-- 1 root android 189, 185 Apr 16 05:55 /dev/bus/usb/002/058`

In this example, [/lib64/udev/rules.d/80-android.rules] over-zealously modified the permissions. This is [[[bug #644636]](https://bugs.gentoo.org/show_bug.cgi?id=644636)[]]. Lets try fixing them:

`root `[`#`]`chgrp lp /dev/bus/usb/002/058 `

`root `[`#`]`chmod 660 /dev/bus/usb/002/058`

Now we should see:

`user `[`$`]`ls -l /dev/bus/usb/002/058 crw-rw---- 1 root lp 189, 185 Apr 16 05:55 /dev/bus/usb/002/058`

The printer likely is detected now. You should be able to add it, configure it (provided that you have a working driver) and print a test page. This implies a permissions problem. Assuming that your system uses udev/eudev for managing its /dev directory, you can make this change permanent by making a udev file:

[FILE] **`/etc/udev/rules.d/99-printer.rules`Custom Udev Rule**

    SUBSYSTEMS=="usb", ATTRS=="04e8", ATTRS=="3297", MODE="0660", GROUP="lp"

Our device is \"ID 04e8:3297\" according to the earlier lsusb output. We split that into idVendor and idProduct as demonstrated in the example. Now udev should ensure that the correct permissions are set at every boot and at every hotplug.

## [See also]

-   [Samba](https://wiki.gentoo.org/wiki/Samba "Samba") --- a re-implementation of the [SMB/CIFS](https://wiki.gentoo.org/wiki/Smbnetfs "Smbnetfs") networking protocol, a Microsoft Windows alternative to Network File System ([NFS](https://wiki.gentoo.org/wiki/NFS "NFS")).
-   [Driverless printing](https://wiki.gentoo.org/wiki/Driverless_printing "Driverless printing")

## [External resources]

-   [OpenPrinting database of printers that support \'driverless printing\'](https://openprinting.github.io/printers/)
-   [OpenPrinting database of printers that require a driver, and their level of Linux support](https://openprinting.org/printers)
-   [Using Network Printers](https://www.cups.org/doc/network.html) - Documentation at CUPS.org.
-   [Command-Line Printing and Options](https://www.cups.org/doc/options.html) - Documentation at CUPS.org.

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **[Sven Vermeulen (SwifT)](https://wiki.gentoo.org/wiki/User:SwifT "User:SwifT") , **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*