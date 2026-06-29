# CUPS

CUPS is the standards-based, open source printing system developed by OpenPrinting for Linux® and other Unix®-like operating systems.

Arch Linux packages the OpenPrinting CUPS fork, not the Apple CUPS fork.

## Installation
Install the  package.

Optionally, install the  package if you intend to "print" into a PDF document. By default, PDF files are stored in . The location can be changed in .

Then enable and start  or alternatively use socket activation to only start CUPS when a program wants to use the service.

## Print steps
It is important to know how CUPS works if wanting to solve related issues:

# An application sends a PDF file to CUPS when 'print' has been selected (in case the application sends another format, it is converted to PDF first).
# CUPS then looks at the printer's PPD file (printer description file) and figures out what filters it needs to use to convert the PDF file to a language that the printer understands (like PJL, PCL, bitmap or native PDF).
# The filter converts the PDF file to a format understood by the printer.
# Then it is sent to the back-end. For example, if the printer is connected to a USB port, it uses the USB back-end.

## Connection interfaces
Additional steps for printer detection are listed below for various connection interfaces.

## USB
To see if your USB printer is detected, make sure you have the  package installed, then:

## Parallel port
To use a parallel port printer, the ,  and  kernel modules are required.

## Network
## Adding known location printers
It is not required to rely on dynamic printer discovery on the network (DNS-SD/mDNS) when the address of the printer is known (e.g. obtained via printers display or other network scanning approaches).
A CUPS queue can be directly added to use the printer. Documentation for adding the queue with lpadmin  can be found in following sections and official documentation at Setting up printers.

## Printer discovery
To discover, make use of discovered or share printers using DNS-SD/mDNS, setup .local hostname resolution with Avahi and restart .

To share printers with Samba, e.g. if the system is to be a print server for Windows clients, the  package will be required.

## Printer drivers
Most recent printers (2010+) support driverless usage by implementing AirPrint and/or IPP_Everywhere (c.f. below).

The drivers for a printer may come from any of the sources shown below. See CUPS/Printer-specific problems for an incomplete list of drivers that others have managed to get working.

To drive a printer, CUPS needs a PPD file and, for most printers, some filters. For details on how CUPS uses PPDs and filters, see The [https://www.openprinting.org/printers OpenPrinting Printer List provides driver recommendations for many printers. It also supplies PPD files for each printer, but most are available through foomatic or the recommended driver package.

When a PPD file is provided to CUPS, the CUPS server will regenerate the PPD files and save them in .

To test if they are working before creating a PKGBUILD, PPD files can be manually added to , the driver should be available after the next restart of the cups service.

## AirPrint and IPP Everywhere
CUPS includes support for AirPrint and IPP Everywhere printers. These should be discovered automatically if  is running without any extra configuration.

Installing an IPP Everywhere printer is described in the CUPS README. It can be done with the   command.

Example:

 # lpadmin -p MyPrinter -E -v "ipp://11.22.33.44/ipp/print" -m everywhere

The   option specifies the printer name. The  option enables the printer and accepts new print jobs immediately. The  option specifies the device URI for the printer, which tells CUPS how to communicate with the printer. And the   option specifies the model (driver) to use, in this case the IPP Everywhere ("everywhere") driver that is used for AirPrint and IPP Everywhere printers as well as shared printers and printers supported through Printer Applications.

The USB or Network device URI can be found with the  command.

## OpenPrinting CUPS filters
The Linux Foundation's OpenPrinting workgroup provides cups-filters. Those are backends, filters, and other binaries that were once part of CUPS but have been dropped from the project. They are available in the  package that is a dependency of .

Non-PDF printers require  to be installed. For PostScript printers,  may also be required.

## Foomatic
The Linux Foundation's OpenPrinting workgroup's foomatic provides PPDs for many printer drivers, both free and non-free. For more information about what foomatic does, see Foomatic from the Developer's View.

To use foomatic, install  and at least one of:

*  — a collection of XML files used by foomatic-db-engine to generate PPD files.
*  — prebuilt PPD files.
*  — a collection of XML files from printer manufacturers under non-free licenses used by foomatic-db-engine to generate PPD files.
*  — prebuilt PPD files under non-free licenses.

The foomatic PPDs may require additional filters, such as .

## Gutenprint
The Gutenprint project provides drivers for Canon, Epson, Lexmark, Sony, Olympus, Brother, HP, Ricoh, PCL printers and some generic printers for use with CUPS and GIMP.

Install  and .

## Manufacturer-specific drivers
Many printer manufacturers supply their own Linux drivers. These are often available in the official Arch repositories or in the AUR.

Some of those drivers are described in more detail in CUPS/Printer-specific problems.

## Printer URI
Listed below are additional steps to manually generate the URI if required. Some printers or drivers may need a special URI as described in CUPS/Printer-specific problems.

## USB
CUPS should be able to automatically generate a URI for USB printers, for example .

If it does not, see CUPS/Troubleshooting#USB printers for troubleshooting steps.

## Parallel port
The URI should be of the form . For instance, if the printer is connected on , use . If you are using a USB to parallel port adapter, use  as the printer URI.

## Network
If you have set up Avahi as in #Network, CUPS should detect the printer URI. You can also use  to find the name of your printer and its address (for instance, ).

The URI can also be generated manually, without using Avahi. A list of the available URI schemes for networked printers is available in the CUPS documentation. As exact details of the URIs differ between printers, check either the manual of the printer or CUPS/Printer-specific problems.

The URI for printers on SMB shares is described in the  man page.

Remote CUPS print servers can be accessed through a URI of the form . See CUPS/Printer sharing#Printer sharing for details on setting up the remote print server.

See CUPS/Troubleshooting#Networking issues for additional issues and solutions.

## Usage
CUPS can be fully controlled using the lp* and cups* CLI tools. Alternatively, the #Web interface or one of several #GUI applications can be used.

* The queue name is a short but descriptive name used on the system to identify the queue. This name should not contain spaces or any special characters. For instance, a print queue corresponding to a HP LaserJet 5P could be named "hpljet5p". More than one queue can be associated with each physical printer.
* The location is a description of the printer's physical location (for instance "bedroom", or "kitchen"). This is to aid in maintaining several printers.
* The description is a full description of the print queue. A common use is a full printer name (like "HP LaserJet 5P").

## CLI tools
See CUPS local documentation for more tips on the command-line tools.

Use SNMP to find a URI:

 $ /usr/lib/cups/backend/snmp ip_address

## lp*
The lpinfo command lists the URI of the printers connected to your system with the  flag, and lists all of the available drivers (or "models", in CUPS parlance) installed on your system with .

The lpadmin utility creates a new queue with . The  flag added to  enables and accepts jobs on the printer. The  flag specifies the device URI. The  flag specifies the driver (or "model", in CUPS parlance) or PPD file to use.

You can also use the  flag to remove a printer (read #cups* beforehand).

Examples :

 # lpadmin -p HP_DESKJET_940C -E -v "usb://HP/DESKJET%20940C?serial=CN16E6C364BH" -m drv:///HP/hp-deskjet_940c.ppd.gz

For a driver-less queue (Apple AirPrint or IPP Everywhere):

 # lpadmin -p AirPrint -E -v "ipp://10.0.1.25/ipp/print" -m everywhere

For a raw queue; no PPD or filter:

 # lpadmin -p SHARED_PRINTER -m raw

When specifying a PPD instead of a model:

 # lpadmin -p Test_Printer -E -v "ipp://10.0.1.3/ipp/print" -m pxlmono.ppd

The lpq utility checks the queue. Add the  flag to check on all queues.

The lprm utility clears the queue. Add a  to remove all entries instead of only the last one by default.

The lpr utility prints. Use  to print the file N times, use the  flag to add a header.

Examples of test prints using lpr:

 $ lpr /usr/share/cups/data/testprint
 $ echo 'Hello, world!' | lpr -p

The lpstat utility, used with the  flag, checks the status. The  flag allows to specify which queue to check.

The lpoptions utility uses the same  flag as lpadmin shown above. With the  flag, it lists the options. The  flag sets the default printer with the argument . The  flag sets options to a value:

 $ lpoptions -p HP_DESKJET_940C -o PageSize=A4
 $ lpoptions -p HP_DESKJET_940C -o cupsIPPSupplies=true -o Duplex=DuplexNoTumble

## cups*
The cupsaccept, cupsdisable, cupsenable and cupsreject utilities do as they are called. Respectively: setting the printer to accept jobs, disabling a printer, activating a printer, setting the printer to reject all incoming tasks.

As an example of their usage, we will cleanly remove a printer:

 # cupsreject queue_name
 # cupsdisable queue_name
 # lpadmin -x queue_name

## ink
Install  to view the ink levels.

Add your user to the additional  user group, log out and log in again.

For usage information, run  without options.

## Web interface
The CUPS server can be fully administered through the web interface, available on http://localhost:631/.

To perform administrative tasks from the web interface, authentication is required; see #Permissions.

;Add a queue
Go to the Administration page. If not explicitly configured otherwise, root and its password could be the credentials requested.

;Modify existing queues
Go to the Printers page, and select a queue to modify.

;Test a queue
Go to the Printers page, and select a queue.

## GUI applications
If your user does not have sufficient privileges to administer CUPS, the applications will request the root password when they start. To give users administrative privileges without needing root access, see #Configuration.

*
*
*
*

## Configuration
The CUPS server configuration is located in  and  (see  and ). After editing either file, restart  to apply any changes. The default configuration is sufficient for most users.

## Permissions
## Groups
User groups with printer administration privileges are defined in  in the . The  and  and  groups are used by default.

CUPS helper programs are run as the  user and group. This allows the helper programs to access printer devices and read configuration files in , which are owned by the  group.

## Allowing admin authentication through PolicyKit
PolicyKit can be configured to allow users to configure printers using a GUI without the admin password.

Here is an example that allows members of the wheel user group to administer printers without a password:

{{hc|/etc/polkit-1/rules.d/49-allow-passwordless-printer-admin.rules|2=
polkit.addRule(function(action, subject) {
    if (action.id == "org.opensuse.cupspkhelper.mechanism.all-edit" &&
        subject.isInGroup("wheel")){
        return polkit.Result.YES;
    }
});
}}

## Default paper size
 is built with  support and libpaper defaults to the Letter paper size (called  in ). To avoid having to change the paper size for each print queue you add, edit  and set your system default paper size. See .

## Archival PDF/A
To save PDF files in the highly compatible format, normally called Archival PDF, or PDF/A, or PDFA, or ISO 19005.

There is currently no option, so it must be added to the command used by cups to call gs.

## Log files
By default, all logs are sent to files in .

The log level can be changed in . See cupsd.conf documentation.

By changing the values of the , , and  directives in  to , CUPS can be made to log to the systemd journal instead. See Fedora:Changes/CupsJournalLogging for information on the original proposed change.

## cups-browsed
CUPS can use Avahi browsing to discover unknown shared printers in your network. This can be useful in large setups where the server is unknown. To use this feature, set up .local hostname resolution, and start both  and . Jobs are sent directly to the printer without any processing so the created queues may not work, however driverless printers such as those supporting IPP Everywhere or AirPrint should work out of the box.

## Print servers and remote administration
See CUPS/Printer sharing and CUPS/Printer sharing#Remote administration.

## Without a local CUPS server
CUPS can be configured to directly connect to remote printer servers instead of running a local print server. This requires installation of the  package. Some applications will still require the  package for printing.

To use a remote CUPS server, set the  environment variable to . For instance, if you want to use a different print server for a single Firefox instance (substitute  with your print server name/port):

 $ CUPS_SERVER=printserver.mydomain:port firefox

To make this configuration permanent create configuration file  and add a hostname of the remote CUPS server to it:

 ServerName server

You can also specify a custom port:

 ServerName server:port

See for details.

## Troubleshooting
See CUPS/Troubleshooting and CUPS/Printer-specific problems.
