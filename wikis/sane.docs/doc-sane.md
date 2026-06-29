# NAME

sane - Scanner Access Now Easy: API for accessing scanners

# DESCRIPTION

**SANE** is an application programming interface (API) that provides standardized access to any raster image scanner hardware. The standardized interface makes it possible to write just one driver for each scanner device instead of one driver for each scanner and application.

While **SANE** is primarily targeted at a UNIX environment, the standard has been carefully designed to make it possible to implement the API on virtually any hardware or operating system.

This manual page provides a summary of the information available about **SANE**.

If you have trouble getting your scanner detected, read the PROBLEMS section.

# TERMINOLOGY

An application that uses the **SANE** interface is called a **SANE frontend.** A driver that implements the **SANE** interface is called a **SANE backend.** A **meta backend** provides some means to manage one or more other backends.

# SOFTWARE PACKAGES

The package **sane-backends** contains backends, documentation, networking support, and the command line frontend **scanimage**(1). The frontends **xscanimage**(1), **xcam**(1), and **scanadf**(1) are included in the package **sane-frontends**. Both packages can be downloaded from the **SANE** homepage (*http://www.sane-project.org/*). Information about other frontends and backends can also be found on the **SANE** homepage.

# GENERAL INFORMATION

The following sections provide short descriptions and links to more information about several aspects of **SANE**. A name with a number in parenthesis (e.g. **sane-dll**(5)) points to a manual page. In this case *man 5 sane-dll* will display the page. Entries like *@DOCDIR@/README* are references to text files that were copied to the **SANE** documentation directory (*@DOCDIR@/*) during installation. Everything else is a URL to a resource on the web.

**SANE homepage**
Information on all aspects of SANE including a tutorial and a link to the SANE FAQ can be found on the SANE homepage: *http://www.sane-project.org/*.

**SANE device lists**
The **SANE** device lists contain information about the status of **SANE** support for a specific device. If your scanner is not listed there (either supported or unsupported), please contact us. See section HOW CAN YOU HELP SANE for details. There are lists for specific releases of SANE, for the current development version and a search engine: *http://www.sane-project.org/sane-supported-devices.html*. The lists are also installed on your system at *@DOCDIR@/*.

**SANE mailing list**
There is a mailing list for the purpose of discussing the SANE standard and its implementations: sane-devel. Despite its name, the list is not only intended for developers, but also for users. There are also some more lists for special topics. However, for users, sane-devel is the right list. How to subscribe and unsubscribe: *http://www.sane-project.org/mailing-lists.html*.

**SANE IRC channel**
The IRC (Internet Relay Chat) channel \#sane can be found on the Freenode network (irc.libera.chat). It's for discussing **SANE** problems, talking about development and general **SANE** related chatting. Before asking for help, please read the other documentation mentioned in this manual page. The channel's topic is also used for announcements of problems with SANE infrastructure (mailing lists, web server, etc.).

**Compiling and installing SANE**
Look at *@DOCDIR@/README* and the os-dependent README files for information about compiling and installing **SANE.**

**SCSI configuration**
For information about various systems and SCSI controllers see **sane-scsi**(5).

**USB configuration**
For information about USB configuration see **sane-usb**(5).

# FRONTENDS AND MISCELLANEOUS PROGRAMS

**scanimage**
Command-line frontend. See **scanimage**(1).

**saned**
**SANE** network daemon that allows remote clients to access image acquisition devices available on the local host. See **saned**(8).

**sane-find-scanner**
Command-line tool to find SCSI and USB scanners and determine their UNIX device files. See **sane-find-scanner**(1).

Also, have a look at the **sane-frontends** package (which includes **xscanimage**(1), **xcam**(1), and **scanadf**(1)) and the frontend information page at *http://www.sane-project.org/sane-frontends.html*.

# BACKENDS FOR SCANNERS

**abaton**
Supports Abaton flatbed scanners such as the Scan 300/GS (8bit, 256 levels of gray) and the Scan 300/S (black and white, untested). See **sane-abaton**(5) for details.

**agfafocus**
Supports AGFA Focus scanners and the Siemens S9036 (untested). See **sane-agfafocus**(5) for details.

**apple**
Supports Apple flatbed scanners including the following scanners: AppleScanner, OneScanner and ColorOneScanner. See **sane-apple**(5) for details.

**artec**
Supports several Artec/Ultima SCSI flatbed scanners as well as the BlackWidow BW4800SP and the Plustek 19200S. See **sane-artec**(5) for details.

**artec_eplus48u**
Supports the Artec E+ 48U scanner and re-badged models like Tevion MD 9693, Medion MD 9693, Medion MD 9705 and Trust Easy Webscan 19200. See **sane-artec_eplus48u**(5) for details.

**as6e**
Supports the Artec AS6E parallel port interface scanner. See **sane-as6e**(5) for details.

**avision**
Supports several Avision based scanners including the original Avision scanners (like AV 630, AV 620, ...) as well as the HP ScanJet 53xx and 74xx series, Fujitsu ScanPartner, some Mitsubishi and Minolta film-scanners. See **sane-avision**(5) for details.

**bh**
Supports Bell+Howell Copiscan II series document scanners. See **sane-bh**(5) for details.

**canon**
Supports the CanoScan 300, CanoScan 600, and CanoScan 2700F SCSI flatbed scanners. See **sane-canon**(5) for details.

**canon630u**
Supports the CanoScan 630u and 636u USB scanners. See **sane-canon630u**(5) for details.

**canon_dr**
Supports the Canon DR-Series ADF SCSI and USB scanners. See **sane-canon_dr**(5) for details.

**canon_lide70**
Supports the CanoScan LiDE 70 and 600 USB scanners. See **sane-canon_lide70**(5) for details.

**canon_pp**
Supports the CanoScan FB330P, FB630P, N340P and N640P parallel port scanners. See **sane-canon_pp**(5) for details.

**cardscan**
Support for Corex Cardscan USB scanners. See **sane-cardscan**(5) for details.

**coolscan coolscan2 coolscan3**
Supports Nikon Coolscan film-scanners. See **sane-coolscan**(5), **sane-coolscan2**(5) and **sane-coolscan3**(5) for details.

**epjitsu**
Supports Epson-based Fujitsu USB scanners. See **sane-epjitsu**(5) for details.

**epson**
Old driver for Epson SCSI, parallel port and USB flatbed scanners. See **sane-epson**(5) for details but try **epson2** first.

**epson2**
Newer driver for Epson SCSI, parallel port, network and USB flatbed scanners (try this before **epson** which is outdated). See **sane-epson2**(5) for details.

**escl**
Supports scanners through the eSCL protocol. See **sane-escl**(5) for details.

**fujitsu**
Supports most Fujitsu SCSI and USB, flatbed and adf scanners. See **sane-fujitsu**(5) for details.

**genesys**
Supports several scanners based on the Genesys Logic GL646, GL841, GL843, GL847 and GL124 chips like the Medion 6471 and Hewlett-Packard 2300c. See **sane-genesys**(5) for details.

**gt68xx**
Supports scanners based on the Grandtech GT-6801 and GT-6816 chips like the Artec Ultima 2000 and several Mustek BearPaw CU and TA models.
Some Genius, Lexmark, Medion, Packard Bell, Plustek, and Trust scanners are also supported. See **sane-gt68xx**(5) for details.

**hp**
Supports Hewlett-Packard ScanJet scanners which utilize SCL (Scanner Control Language by HP). See **sane-hp**(5) for details.

**hpsj5s**
Supports the Hewlett-Packard ScanJet 5S scanner. See **sane-hpsj5s**(5) for details.

**hp3500**
Supports the Hewlett-Packard ScanJet 3500 series. See **sane-hp3500**(5) for details.

**hp3900**
Supports the Hewlett-Packard ScanJet 3900 series. See **sane-hp3900**(5) for details.

**hp4200**
Supports the Hewlett-Packard ScanJet 4200 series. See **sane-hp4200**(5) for details.

**hp5400**
Supports the Hewlett-Packard ScanJet 54XXC series. See **sane-hp5400**(5) for details.

**hpljm1005**
Supports the Hewlett-Packard LaserJet M1005 scanner. See **sane-hpljm1005**(5) for details.

**hs2p**
Supports the Ricoh IS450 family of SCSI scanners. See **sane-hs2p**(5) for details.

**ibm**
Supports some IBM and Ricoh SCSI scanners. See **sane-ibm**(5) for details.

**kodak**
Supports some large Kodak scanners. See **sane-kodak**(5) for details.

**kodakaio**
Supports Kodak AiO printer/scanners. See **sane-kodakaio**(5) for details.

**kvs1025**
Supports Panasonic KV-S102xC scanners. See **sane-kvs1025**(5) for details.

**leo**
Supports the LEO S3 and the Across FS-1130, which is a re-badged LEO FS-1130 scanner. See **sane-leo**(5) for details.

**lexmark**
Supports the Lexmark X1100 series of USB scanners. See **sane-lexmark**(5) for details.

**lexmark_x2600**
Supports the Lexmark X2600 series of USB scanners. See **sane-lexmark_x2600**(5) for details.

**ma1509**
Supports the Mustek BearPaw 1200F USB flatbed scanner. See **sane-ma1509**(5) for details.

**magicolor**
Supports the KONICA MINOLTA magicolor 1690MF multi-function printer/scanner/fax. See **sane-magicolor**(5) for details.

**matsushita**
Supports some Panasonic KVSS high speed scanners. See **sane-matsushita**(5) for details.

**microtek**
Supports "second generation" Microtek scanners with SCSI-1 command set. See **sane-microtek**(5) for details.

**microtek2**
Supports some Microtek scanners with a SCSI-2 command set. See **sane-microtek2**(5) for details.

**mustek**
Supports most Mustek SCSI flatbed scanners including the Paragon and ScanExpress series and the 600 II N and 600 II EP (non-SCSI). Some Trust scanners are also supported. See **sane-mustek**(5) for details.

**mustek_pp**
Supports Mustek parallel port flatbed scanners. See **sane-mustek_pp**(5) for details.

**mustek_usb**
Supports some Mustek ScanExpress USB flatbed scanners. See **sane-mustek_usb**(5) for details.

**mustek_usb2**
Supports scanners using the SQ113 chipset like the Mustek BearPaw 2448 TA Pro USB flatbed scanner. See **sane-mustek_usb2**(5) for details.

**nec**
Supports the NEC PC-IN500/4C SCSI scanner. See **sane-nec**(5) for details.

**niash**
Supports the Agfa Snapscan Touch and the HP ScanJet 3300c, 3400c, and 4300c USB flatbed scanners. See **sane-niash**(5) for details.

**p5**
Supports the Primax PagePartner. See **sane-p5**(5) for details.

**pie**
Supports Pacific Image Electronics (PIE) and Devcom SCSI flatbed scanners. See **sane-pie**(5) for details.

**pixma**
Supports Canon PIXMA MP series (multi-function devices), Canon imageCLASS series (laser devices), Canon MAXIFY series and some Canon CanoScan series. See **sane-pixma**(5) for details.

**plustek**
Supports USB flatbed scanners that use the National Semiconductor LM983\[1/2/3\] chipset aka Merlin. Scanners using this LM983x chips include some models from Plustek, KYE/Genius, Hewlett-Packard, Mustek, Umax, Epson, and Canon. See **sane-plustek**(5) for details.

**plustek_pp**
Supports Plustek parallel port flatbed scanners using the Plustek ASIC P96001, P96003, P98001 and P98003, which includes some models from Plustek, KYE/Genius, Primax. See **sane-plustek_pp**(5) for details.

**ricoh**
Supports the Ricoh flatbed scanners IS50 and IS60. See **sane-ricoh**(5) for details.

**ricoh2**
Supports the Ricoh flatbed scanners: SG-3100SNw, SP-100SU, and SP-111SU. See **sane-ricoh2**(5) for details.

**s9036**
Supports Siemens 9036 flatbed scanners. See **sane-s9036**(5) for details.

**sceptre**
Supports the Sceptre S1200 flatbed scanner. See **sane-sceptre**(5) for details.

**sharp**
Supports Sharp SCSI scanners. See **sane-sharp**(5) for details.

**sm3600**
Supports the Microtek ScanMaker 3600 USB scanner. See **sane-sm3600**(5) for details.

**sm3840**
Supports the Microtek ScanMaker 3840 USB scanner. See **sane-sm3840**(5) for details.

**snapscan**
Supports AGFA SnapScan flatbed scanners including some which are rebadged to other brands. See **sane-snapscan**(5) for details.

**sp15c**
Supports the Fujitsu FCPA ScanPartner 15C flatbed scanner. See **sane-sp15c**(5) for details.

**st400**
Supports the Siemens ST400 and ST800. See **sane-st400**(5) for details.

**tamarack**
Supports Tamarack Artiscan flatbed scanners. See **sane-tamarack**(5) for details.

**teco1 teco2 teco3**
Supports some TECO scanners, usually sold under the Relisys, Trust, Primax, Piotech, Dextra names. See **sane-teco1**(5), **sane-teco2**(5) and **sane-teco3**(5) for details.

**u12**
Supports USB flatbed scanners based on Plustek's ASIC 98003 (parallel-port ASIC) and a GeneSys Logics' USB-parport bridge chip like the Plustek OpticPro U(T)12. See **sane-u12**(5) for details.

**umax**
Supports UMAX-SCSI-scanners and some Linotype Hell SCSI-scanners. See **sane-umax**(5) for details.

**umax_pp**
Supports Umax parallel port flatbed scanners and the HP 3200C. See **sane-umax_pp**(5) for details.

**umax1200u**
Supports the UMAX Astra 1220U (USB) flatbed scanner (and also the UMAX Astra 2000U, sort of). See **sane-umax1220u**(5) for details.

**xerox_mfp**
Supports multiple Samsung-based Samsung, Xerox, and Dell scanners. See **sane-xerox_mfp**(5) for details.

Also, have a look at the backend information page at *http://www.sane-project.org/sane-supported-devices.html* and the list of projects in *@DOCDIR@/PROJECTS*.

# BACKENDS FOR DIGITAL CAMERAS

**dc210**
Supports the Kodak DC210 Digital Camera. See **sane-dc210**(5).

**dc240**
Supports the Kodak DC240 Digital Camera. See **dc240**(5).

**dc25**
Supports Kodak DC20/DC25 Digital Cameras. See **dc25**(5).

**dmc**
Supports the Polaroid Digital Microscope Camera. See **dmc**(5).

**gphoto2**
Supports digital cameras supported by the gphoto2 library package. (See *http://www.gphoto.org* for more information and a list of supported cameras.) Gphoto2 supports over 140 different camera models. However, please note that more development and testing is needed before all of these cameras will be supported by **SANE** backend. See **gphoto2**(5).

**qcam**
Supports Connectix QuickCam cameras. See **qcam**(5).

**stv680**
Supports webcams with a stv680 chip. See **stv680**(5) for details.

Also, have a look at the backend information page at *http://www.sane-project.org/sane-supported-devices.html* and the list of projects in *@DOCDIR@/PROJECTS*.

# MISCELLANEOUS BACKENDS

**dll**
Implements a **SANE** backend that provides access to an arbitrary number of other **SANE** backends by dynamic loading. See **sane-dll**(5).

**net**
The **SANE** network daemon **saned**(8) provides access to scanners located on different computers in connection with the **sane-net**(5) backend. See **saned**(8).

**pnm**
PNM image reader pseudo-backend. The purpose of this backend is primarily to aid in debugging of **SANE** frontends. See **sane-pnm**(5).

**pint**
Supports scanners that use the **PINT** (Pint Is Not Twain) device driver. The **PINT** driver is being actively developed on the OpenBSD platform, and has been ported to a few other \*NIX-like operating systems. See **sane-pint**(5).

**test**
Tests frontends and the **SANE** installation. It provides test pictures and various test options. See **sane-test**(5).

**v4l**
Provides generic access to video cameras and similar equipment using the **V4L** (Video for Linux) API. See **sane-v4l**(5)**.**

Also, have a look at the backend information page at *http://www.sane-project.org/sane-supported-devices.html* and the list of projects in *@DOCDIR@/PROJECTS*.

# CHANGING THE TOP-LEVEL BACKEND

By default, all **SANE** backends (drivers) are loaded dynamically by the **sane-dll** meta backend. If you have any questions about the dynamic loading, read **sane-dll**(5). **SANE** frontends can also be linked to other backends directly by copying or linking a backend to **libsane.so** in *@LIBDIR@*.

# DEVELOPER'S DOCUMENTATION

It's not hard to write a **SANE** backend. It can take some time, however. You should have basic knowledge of C and enough patience to work through the documentation and find out how your scanner works. Appended is a list of some documents that help to write backends and frontends.

The **SANE** standard defines the application programming interface (API) that is used to communicate between frontends and backends. It can be found at *http://sane-project.gitlab.io/standard/ .*

There is some more information for programmers in *@DOCDIR@/backend-writing.txt*. Most of the internal **SANE** routines (**sanei**) are documented using doxygen: *http://www.sane-project.org/sanei/*. Before a new backend or frontend project is started, have a look at *@DOCDIR@/PROJECTS* for projects that are planned or not yet included into the **SANE** distribution and at our bug-tracking system: *http://www.http://www.sane-project.org/bugs.html*.

There are some links on how to find out about the protocol of a scanner: *http://www.meier-geinitz.de/sane/misc/develop.html*.

If you start writing a backend or frontend or any other part of **SANE,** please contact the sane-devel mailing list for coordination so that work is not duplicated.

# FILES

*@CONFIGDIR@/\*.conf*
The backend configuration files.

*@LIBDIR@/libsane-\*.a*
The static libraries implementing the backends.

*@LIBDIR@/libsane-\*.so*
The shared libraries implementing the backends (present on systems that support dynamic loading).

*@DOCDIR@/\**
**SANE** documentation: The READMEs, text files for backends etc.

# PROBLEMS

If your device isn't found but you know that it is supported, make sure that it is detected by your operating system. For SCSI and USB scanners, use the **sane-find-scanner**(1) utility. It prints one line for each scanner it has detected and some comments (#). If **sane-find-scanner**(1) finds your scanner only as root but not as normal user, the permissions for the device files are not adjusted correctly. If the scanner isn't found at all, the operating system hasn't detected it and may need some help. Depending on the type of your scanner, read **sane-usb**(5) or **sane-scsi**(5). If your scanner (or other device) is not connected over the SCSI bus or USB, read the backend's manual page for details on how to set it up.

Is your scanner detected by the operating system but not by **SANE**? Try *scanimage -L*. If the scanner is not found, check that the backend's name is mentioned in *@CONFIGDIR@/dll.conf*. Some backends are commented out by default. Remove the comment sign for your backend in this case. Also some backends aren't compiled at all if one of their prerequisites are missing. Examples include dc210, dc240, canon_pp, hpsj5s, gphoto2, pint, qcam, v4l, net, sm3600, snapscan, pnm. If you need one of these backends and it isn't available, read the build instructions in the **README** file and the individual manual pages of the backends.

Another reason for not being detected by *scanimage -L* may be a missing or incorrect configuration in the backend's configuration file. While **SANE** tries to automatically find most scanners, some can't be setup correctly without the intervention of the administrator. Also on some operating systems auto-detection may not work. Check the backend's manual page for details.

If your scanner is still not found, try setting the various environment variables that are available to assist in debugging. The environment variables are documented in the relevant manual pages. For example, to get the maximum amount of debug information when testing a Mustek SCSI scanner, set environment variables **SANE_DEBUG_DLL**, **SANE_DEBUG_MUSTEK**, and **SANE_DEBUG_SANEI_SCSI** to 128 and then invoke *scanimage -L*. The **SANE_DEBUG_DLL** messages tell if the **sane-mustek**(5) backend was found and loaded at all. The **SANE_DEBUG_MUSTEK** messages explain what the backend is doing while the **SANE_DEBUG_SCSI** debugging shows the low level handling. If you can't find out what's going on by checking the messages carefully, contact the sane-devel mailing list for help (see REPORTING BUGS below).

Now that your scanner is found by *scanimage -L*, try to do a scan: *scanimage \>image.pnm*. This command starts a scan for the default scanner with default settings. All the available options are listed by running *scanimage --help*. If scanning aborts with an error message, turn on debugging as mentioned above. Maybe the configuration file needs some tuning, e.g. to setup the path to a firmware that is needed by some scanners. See the backend's manual page for details. If you can't find out what's wrong, contact sane-devel.

To check that the **SANE** libraries are installed correctly you can use the test backend, even if you don't have a scanner or other **SANE** device:

> scanimage -d test -T

You should get a list of PASSed tests. You can do the same with your backend by changing "test" to your backend's name.

So now scanning with **scanimage (1)** works and you want to use one of the graphical frontends like **xsane**(1)**,** **xscanimage**(1)**, or** **quiteinsane**(1) but those frontends don't detect your scanner? One reason may be that you installed two versions of **SANE**. E.g. the version that was installed by your distribution in */usr* and one you installed from source in */usr/local/*. Make sure that only one version is installed. Another possible reason is, that your system's dynamic loader can't find the **SANE** libraries. For Linux, make sure that */etc/ld.so.conf* contains */usr/local/lib* and does **not** contain */usr/local/lib/sane*. See also the documentation of the frontends.

# HOW CAN YOU HELP SANE


# CONTACT

For reporting bugs or requesting new features, please use our bug-tracking system: *http://www.sane-project.org/bugs.html*. You can also contact the author of your backend directly. Usually the email address can be found in the *@DOCDIR@/AUTHORS* file or the backend's manpage. For general discussion about SANE, please use the **SANE** mailing list sane-devel (see *http://www.sane-project.org/mailing-lists.html* for details).

# SEE ALSO

**saned**(8), **sane-find-scanner**(1), **scanimage**(1), **sane-abaton**(5), **sane-agfafocus**(5), **sane-apple**(5), **sane-artec**(5), **sane-artec_eplus48u**(5), **sane-as6e**(5), **sane-avision**(5), **sane-bh**(5), **sane-canon**(5), **sane-canon630u**(5), **sane-canon_dr**(5), **sane-canon_pp**(5), **sane-cardscan**(5), **sane-coolscan**(5), **sane-coolscan2**(5), **sane-coolscan3**(5), **sane-dc210**(5), **sane-dc240**(5), **sane-dc25**(5), **sane-dll**(5), **sane-dmc**(5), **sane-epson**(5), **sane-epson2**(5), **sane-escl**(5), **sane-fujitsu**(5), **sane-genesys**(5), **sane-gphoto2**(5), **sane-gt68xx**(5), **sane-hp**(5), **sane-hpsj5s**(5), **sane-hp3500**(5), **sane-hp3900**(5), **sane-hp4200**(5), **sane-hp5400**(5), **sane-hpljm1005**(5), **sane-ibm**(5), **sane-kodak**(5), **sane-leo**(5), **sane-lexmark**(5), **sane-lexmark_x2600**(5), **sane-ma1509**(5), **sane-matsushita**(5), **sane-microtek2**(5), **sane-microtek**(5), **sane-mustek**(5), **sane-mustek_pp**(5), **sane-mustek_usb**(5), **sane-mustek_usb2**(5), **sane-nec**(5), **sane-net**(5), **sane-niash**(5), **sane-pie**(5), **sane-pint**(5), **sane-plustek**(5), **sane-plustek_pp**(5), **sane-pnm**(5), **sane-qcam**(5), **sane-ricoh**(5), **sane-ricoh2**(5), **sane-s9036**(5), **sane-sceptre**(5), **sane-scsi**(5), **sane-sharp**(5), **sane-sm3600**(5), **sane-sm3840**(5), **sane-snapscan**(5), **sane-sp15c**(5), **sane-st400**(5), **sane-stv680**(5), **sane-tamarack**(5), **sane-teco1**(5), **sane-teco2**(5), **sane-teco3**(5), **sane-test**(5), **sane-u12**(5), **sane-umax1220u**(5), **sane-umax**(5), **sane-umax_pp**(5), **sane-usb**(5), **sane-v4l**(5), **sane-xerox_mfp**(5)

# AUTHOR

David Mosberger-Tang and many many more (see *@DOCDIR@/AUTHORS* for details). This man page was written by Henning Meier-Geinitz. Quite a lot of text was taken from the **SANE** standard, several man pages, and README files.
