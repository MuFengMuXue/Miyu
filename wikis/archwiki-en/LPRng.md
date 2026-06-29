# LPRng

From upstream:
:  The LPRng software is an enhanced, extended, and portable implementation of the Berkeley LPR print spooler functionality. While providing the same interface and meeting RFC1179 requirements, the implementation is completely new and provides support for the following features:
:* Complete (no databases needed) lpr, lpc, and lprm programs
:* Dynamic redirection of print queues; automatic job holding
:* Highly verbose diagnostics
:* Multiple printers serving a single queue
:* Client programs do not need to run SUID root
:* Greatly enhanced security checks
:* Greatly improved permission and authorization mechanism

LPRng is mature and stable and incorporates a flexible print filtering mechanism.  It excels as a print server but can be used as a print client.  It can also print from CUPS clients installed on other machines with minor hand configuration on the CUPS side.

## Installation
Install the  package.

Install optional filter packages:
*
*Any one out of , ,
*
*
*

## Configuration
Configuration consists of the following steps:

* Set up control files
* Configure filters
* Create a printcap file and spool directories
* Enable and start the lpd daemon

## Control files
## Local configuration
Two control files must be configured:

*
*

## Remote configuration
The default configurations in  are adequate for a client computer printing to a remote printer.  Copy these to

 # cp /usr/share/doc/lprng /etc/lprng/lpd

and edit it.

## Server configuration
For a server receiving requests across the Internet, uncomment the last line in  and configure permissions as documented in the comments of .

## Configure printer settings (filters)
It is fine if you just pick one of the following filter (settings)  instructions. Just decide which way you want to go.

## Postscript printers
If you have a network Postscript printer you are in luck.  The sample postscript filter  converts PDF and text files to Postscript.  Other file types are rejected.

Copy this file to  and rename it as desired.  Then edit it to set your paper type and your choice of single-sided/double-sided printing.

If you wish to have separate single-sided and double-sided print queues, make two copies with different names and edit appropriately.

## Foomatic system
Another mechanism for print filtering is via the Foomatic system. This system used by CUPS. Install  as the  program in the CUPS installation has been modified to remove LPRng support).

Use  as described above, editing for your desired .  Install the  file in conformance with the path specified in . ( is a good location.)

To use Hewlett Packard printers, install  from the main distribution.  This package has  files for virtually all Hewlett Packard printers.

## Ghostscript drivers
If you have a printer that has a Ghostscript driver, copy and edit  as above to set the appropriate driver and the paper type.  You can discover the drivers available in your version of Ghostscript by typing the command

Note that support for various printer features is typically limited and out of date with this option.

## Printcap file
The  file tells LPRng about the printers you have and the print filters that need to be used.

## Examples
The  file (in ) provides a short tutorial as to how to set up a printcap file. The printcap fragments  and  in this directory provide additional information.

An example file may look like this for two local printers:

 DCPJ4120DW:\
      :mx=0:\
      :sd=/var/spool/lpd/DCPJ4120DW:\
      :sh:\
      :lp=/dev/usb/lp1:\
      :if=/opt/brother/Printers/dcpj4120dw/lpd/filterdcpj4120dw:
 HL2035:\
      :mx=0:\
      :sd=/var/spool/lpd/HL2035:\
      :sh:\
      :lp=/dev/usb/lp0:\
      :if=/opt/brother/Printers/brhl2035/lpd/filterHL2030:

## Network printing advice
Generally, one computer should be designated as the server for one or more printers.  Other client computers should send their print jobs to the server rather than the printer directly.

The rather non-obvious server setup in  is needed to make print filtering work on network printers, as opposed to printers attached directly to the server computer via, say, a USB port.  (See the reference manual.)

After creating the printcap file, run the command as root

This will check your configuration and create spool directories in .  If  complains about something, address the issue and rerun.

## Start the lpd daemon
LPRng runs a daemon in background called  to manage print requests. Start/enable .

If any configuration files are changed, one must restart .

## Usage
The  command is the printing tool in LPRng. The general form of use is

If no file is specified, input is accepted on the standard input. The most useful options are  and . In the absence of the printer option, setting the environment variable  to the name of the printer will tell LPRng which printer to use.

Other useful commands are  (examine the print queue) and  (remove a print job from the queue). See , , and .

## CUPS and LPRng
CUPS may be used to access a printer on a server from a client machine on which LPRng is not installed.  The trick is to configure CUPS to access the printer via the  protocol.  This is easy to do using the web interface to CUPS.  Also, since the server as set up here does all necessary print filtering, tell CUPS to use the  filter.  Alternative divisions between filtering responsibilities can be devised, depending on your needs.

## Troubleshooting
## Printer specific instrcutions
Despite its title, some of the information at CUPS/Printer-specific problems is not Cups specific.

## GTK2
GTK2 applications still support  printing. To make this work, create the file  in your home directory containing a single line

 gtk-print-backends = "file,lpr"

## LXDE
LXDE may create its own  file if the look and feel of the desktop are altered — look in this file for instructions as to how to proceed.

## Postscript printing
The filter  from the  package is used to create Postscript from PDF files in the print filters.

Occasionally,  produces bad or no output.
An alternative filter,  from the  package, can be substituted, but this filter has its own problems.

For a one-shot case, just use  or some other converter to produce Postscript and send that to the printer.

## Double-Sided PS
Double-sided printing of Postscript files is effected in the example filters by inserting a line of Postscript code right after the first line.  For some Postscript files, this does not work.

In this case, send the Postscript file to a single-side print queue.  The print filter  set up for single-sided printing does no filtering of Postscript files.
