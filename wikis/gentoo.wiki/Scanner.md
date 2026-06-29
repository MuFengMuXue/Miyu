This page contains [[changes](https://wiki.gentoo.org/index.php?title=SANE&diff=1429249)] which are not marked for translation.

\

**Resources**

[[]][Home](http://www.sane-project.org/)

**S**canner **A**ccess **N**ow **E**asy (SANE) enables the use of scanners on Linux. It provides drivers for many different scanners, a daemon to manage access to all scanners attached to the system, and a command-line frontend application [scanimage] which implements basic scanning functionality.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Backend]](#Backend)
        -   [[1.1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Frontend]](#Frontend)
        -   [[1.2.1] [USE flags]](#USE_flags_2)
        -   [[1.2.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Using a network scanner]](#Using_a_network_scanner)
    -   [[2.2] [Scanning over the network]](#Scanning_over_the_network)
        -   [[2.2.1] [Server settings]](#Server_settings)
            -   [[2.2.1.1] [saned]](#saned)
            -   [[2.2.1.2] [xinetd]](#xinetd)
        -   [[2.2.2] [Client settings]](#Client_settings)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [scanimage unable to identify scanner]](#scanimage_unable_to_identify_scanner)
    -   [[3.2] [Test scan via command line]](#Test_scan_via_command_line)
    -   [[3.3] [Forcing \[USB\] identification]](#Forcing_.5BUSB.5D_identification)
-   [[4] [See also]](#See_also)

## [Installation]

### [Backend]

SANE backends (a.k.a. drivers) are provided by the [[[media-gfx/sane-backends]](https://packages.gentoo.org/packages/media-gfx/sane-backends)[]] package.

The SANE project maintains a [searchable list of supported (and some unsupported) devices](http://www.sane-project.org/sane-supported-devices.html). Find your scanner on that list, and note the values provided for **Backend** and (if it\'s a USB scanner) **USB id**, which will be needed for configuration.

In [/etc/portage/make.conf], set `SANE_BACKENDS` to a space-separated list of the backends that need to be installed, as obtained from the list on the SANE project website.

[FILE] **`/etc/portage/package.use/sane`**

    */* SANE_BACKENDS: epson2

To see all supported backends, run:

`user `[`$`]`emerge -pv sane-backends`

    [ebuild   R   ] media-gfx/sane-backends-1.0.25-r1  USE="ipv6 nls threads usb -doc -gphoto2 -snmp -systemd -v4l -xinetd -zeroconf" ABI_X86="(64) -32 (-x32)" SANE_BACKENDS="abaton agfafocus apple artec artec_eplus48u as6e avision bh canon canon630u canon_dr cardscan coolscan coolscan2 coolscan3 dc210 dc240 dc25 dell1600n_net dmc epjitsu epson epson2 fujitsu genesys gt68xx hp hp3500 hp3900 hp4200 hp5400 hp5590 hpljm1005 hs2p ibm kodak kodakaio kvs1025 kvs20xx leo lexmark ma1509 magicolor matsushita microtek microtek2 mustek mustek_usb nec net niash p5 pie pixma plustek plustek_pp qcam ricoh rts8891 s9036 sceptre sharp sm3600 sm3840 snapscan sp15c st400 stv680 tamarack teco1 teco2 teco3  u12 umax umax1220u umax_pp xerox_mfp -canon_pp -hpsj5s -kvs40xx -mustek_pp -mustek_usb2 -pnm"

or look [on the SANE project\'s website](http://www.sane-project.org/sane-backends.html).

#### [USE flags]

Ensure that the proper `USE` flags are set to support your scanner\'s features, e.g. if it is a USB scanner, set the `usb` USE flag.

### [USE flags for] [media-gfx/sane-backends](https://packages.gentoo.org/packages/media-gfx/sane-backends) [[]] [Scanner Access Now Easy - Backends]

  --------------------------------------------------------------- --------------------------------------------------------------------------------------------------
  [`+usb`](https://packages.gentoo.org/useflags/+usb)             Add USB support to applications that have optional USB support (e.g. cups)
  [`+zeroconf`](https://packages.gentoo.org/useflags/+zeroconf)   Support for DNS Service Discovery (DNS-SD)
  [`gphoto2`](https://packages.gentoo.org/useflags/gphoto2)       Add digital camera support
  [`snmp`](https://packages.gentoo.org/useflags/snmp)             Add support for the Simple Network Management Protocol if available
  [`systemd`](https://packages.gentoo.org/useflags/systemd)       Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`threads`](https://packages.gentoo.org/useflags/threads)       Add threads support for various packages. Usually pthreads
  [`v4l`](https://packages.gentoo.org/useflags/v4l)               Enable support for video4linux (using linux-headers or userspace libv4l libraries)
  [`xinetd`](https://packages.gentoo.org/useflags/xinetd)         Add support for the xinetd super-server
  --------------------------------------------------------------- --------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-13 19:23] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

It may also be necessary to change the kernel configuration to allow it to detect the scanner, e.g. for a USB scanner, USB support needs to be enabled in the kernel.

There is usually no need to explicitly install the backend package since it will be pulled in as a dependency of the frontend, but those who would like to do so anyway can run:

`root `[`#`]`emerge --ask media-gfx/sane-backends`

### [Frontend]

The [[[media-gfx/sane-backends]](https://packages.gentoo.org/packages/media-gfx/sane-backends)[]] package provides one frontend application, [scanimage]. Most users will want to install another one. The SANE project maintains [a list of frontends](http://www.sane-project.org/sane-frontends.html), many of which are available in Portage.

#### [USE flags]

XSane is a capable default option. To install XSane or any frontend, check their `USE` flags. For example:

### [USE flags for] [media-gfx/xsane](https://packages.gentoo.org/packages/media-gfx/xsane) [[]] [Graphical scanning frontend]

  ----------------------------------------------------- --------------------------------------------------------------------
  [`gimp`](https://packages.gentoo.org/useflags/gimp)   Build a plugin for the GIMP
  [`jpeg`](https://packages.gentoo.org/useflags/jpeg)   Add JPEG image support
  [`lcms`](https://packages.gentoo.org/useflags/lcms)   Add lcms support (color management engine)
  [`nls`](https://packages.gentoo.org/useflags/nls)     Add Native Language Support (using gettext - GNU locale utilities)
  [`png`](https://packages.gentoo.org/useflags/png)     Add support for libpng (PNG images)
  [`tiff`](https://packages.gentoo.org/useflags/tiff)   Add support for the TIFF image format
  ----------------------------------------------------- --------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-12-19 09:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

#### [Emerge]

Install the package:

`root `[`#`]`emerge --ask media-gfx/xsane`

## [Configuration]

Installing SANE creates the [scanner] group. Any user account that is to access the scanner needs to get added to this group.

`root `[`#`]`gpasswd -a larry scanner`

Additionally, if the scanner is connected via USB, it may be necessary to add user(s) to the [usb] group:

`root `[`#`]`gpasswd -a larry usb`

It may also be necessary to add user(s) to the [lp] group:

`root `[`#`]`gpasswd -a larry lp`

After changing the group membership, the affected user(s) will need to log out and into the system again.

** Note**\
Users of [systemd] might not need to add users to the [scanner] group. See [ArchWiki](https://wiki.archlinux.org/index.php/SANE#Permission_problem) for more.

In many cases, SANE simply works without any further configuration needed. To test this, ensure that the scanner is connected and powered on, and run:

`user `[`$`]`scanimage -L`

    device `epson2:libusb:001:009' is a Epson CX3800 flatbed scanner

If the scanner is identified, as in the example above, everything is fine.

### [Using a network scanner]

** Note**\
The higher quality eSCL protocol requires [avahi-daemon](https://wiki.gentoo.org/wiki/Avahi "Avahi") to be running. Otherwise scan quality will be reduced.

Most modern scanners can be accessed using eSCL or WSD protocols, with no additional configuration. To use this:

`root `[`#`]`emerge --ask media-gfx/sane-airscan`

And in most cases, the scanner will work out of the box.

### [Scanning over the network]

SANE includes a daemon, [saned], which allows other computers to use attached scanners over the network. To enable this feature, some configuration has to be done on both the server and client.

#### [Server settings]

There are two possible ways to configure your SANE server. The saned approach is the simplest of the two.

##### [saned]

Update [/etc/sane.d/saned.conf] to include the IP address or subnet of the clients that will be accessing this scanner server.

[FILE] **`/etc/sane.d/saned.conf`**

    192.168.0.0/24

Add [saned] to the default runlevel and start it:

`root `[`#`]`rc-update add saned default `

`root `[`#`]`/etc/init.d/saned start `

##### [xinetd]

The scanner daemon is called [saned], by default, it listens to port 6566.

When using xinetd instead of starting the server directly, remember to enable saned by setting [disable] to [No] and allow your network to access the daemon ([only_from = 192.168.0.0/24]):

[FILE] **`/etc/xinetd.d/saned`**

    1=service sane-port


If you want to access the server locally, also add [localhost] to the allowed clients.

Don\'t forget to (re)start [xinetd]:

`root `[`#`]`systemctl restart xinetd.service`

#### [Client settings]

Make sure to add the respective USE flag to be able to find scanners on the network:

[FILE] **`/etc/portage/make.conf`**

    SANE_BACKENDS="net"

** Note**\
\* Keep in mind that the client does not need any scanner drivers at all, if a server handles scanners.

-   For HP scanner-printers managed with HPLIP, HPLIP must be emerged with the `scanner` USE flag.

Recompile the [[[media-gfx/sane-backends]](https://packages.gentoo.org/packages/media-gfx/sane-backends)[]] package:

`root `[`#`]`emerge --ask --changed-use media-gfx/sane-backends`

    These are the packages that would be merged, in order:

    Calculating dependencies... done!
    [ebuild   R    ] media-gfx/sane-backends-1.0.27  SANE_BACKENDS="net*"

    Would you like to merge these packages? [Yes/No]

This will generate the file [/etc/sane.d/net.conf]:

[FILE] **`/etc/sane.d/net.conf`**

    # This is the net backend config file.

    ## net backend options
    # Timeout for the initial connection to saned. This will prevent the backend
    # from blocking for several minutes trying to connect to an unresponsive
    # saned host (network outage, host down, ...). Value in seconds.
    # connect_timeout = 60

    ## saned hosts
    # Each line names a host to attach to.
    # If you list "localhost" then your backends can be accessed either
    # directly or through the net backend.  Going through the net backend
    # may be necessary to access devices that need special privileges.
    # localhost

Uncomment `connect_timeout = 60` and replace the line `# localhost` with either the hostname or the IP address of the sane server.

Check, if the server can be found now:

`user `[`$`]`scanimage -L`

## [Troubleshooting]

### [scanimage unable to identify scanner]

If [scanimage -L] is unable to identify the scanner, it will look like this:

`user `[`$`]`scanimage -L`

    No scanners were identified. If you were expecting something different,
    check that the scanner is plugged in, turned on and detected by the
    sane-find-scanner tool (if appropriate). Please read the documentation
    which came with this software (README, FAQ, manpages).

In most cases, the first step to take in resolving this issue is to run [sane-find-scanner] as root.

`root `[`#`]`sane-find-scanner`

      # sane-find-scanner will now attempt to detect your scanner. If the
      # result is different from what you expected, first make sure your
      # scanner is powered up and properly connected to your computer.

      # No SCSI scanners found. If you expected something different, make sure that
      # you have loaded a kernel SCSI driver for your SCSI adapter.

    could not fetch string descriptor: Pipe error
    found USB scanner (vendor=0x04b8 [EPSON], product=0x0818 [USB MFP]) at libusb:001:008
    could not fetch string descriptor: Pipe error
    could not fetch string descriptor: Pipe error
    could not fetch string descriptor: Pipe error
      # Your USB scanner was (probably) detected. It may or may not be supported by
      # SANE. Try scanimage -L and read the backend's manpage.

      # Not checking for parallel port scanners.

      # Most Scanners connected to the parallel port or other proprietary ports
      # can't be detected by this program.

If the output does not contain a line saying that the scanner was detected, it probably will not work with SANE.

Assuming [sane-find-scanner] *does* find the scanner, as in the example above, there are a few things to check. First, try running [sane-find-scanner] as a non-root user. If it fails to detect the scanner when run this way, that means the problem is most likely permissions on the device node. The man page for the device type will have more information on how to handle this. For USB scanners:

`user `[`$`]`man sane-usb`

For SCSI scanners:

`user `[`$`]`man sane-scsi`

Make sure that the correct device was identified, e.g. in the example above, check that the USB vendor and product numbers listed in the output match the **USB id** obtained from the SANE website. If not, it means that SANE is detecting something other than the scanner.

If the correct device is detected, it may be necessary to edit the configuration file for the corresponding SANE backend. These configuration files are located in [/etc/sane.d/]. Each backend that gets installed has an associated configuration file with the same name, for example [/etc/sane.d/epson2.conf]. The man page for the backend will have more information on what edits may be necessary, for example:

`user `[`$`]`man sane-epson2`

### [Test scan via command line]

Look for available scanners and list them:

`user `[`$`]`scanimage --list-devices`

    device `net:<hostname>:genesys:libusb:001:004' is a Hewlett Packard ScanJet 2300c flatbed scanner

Copy the content between the quotes and execute the following command:

`user `[`$`]`scanimage --device-name net:<hostname>:genesys:libusb:001:004 --format pnm > outfile.pnm`

This will create the file [outfile.pnm] in the current working directory.

### [][Forcing \[USB\] identification]

If the scanner is not detected even while connected:

`user `[`$`]`lsusb`

    Bus 002 Device 004: ID 132b:208b Konica Minolta KONICA MINOLTA magicolor 1680MF scan

It can be forcibly identified by editing an appropriate file under [/etc/sane.d/]:

[FILE] **`/etc/sane.d/magicolor.conf`Magicolor backend configuration**

    ### USB: format is "usb" for automatic (libusb) discovery, based on USB IDs,
    ###      or "usb <vendor ID> <device ID> to force the use of a particular
    ###      device (the backend has some additional checks and will not use
    ###      non-KONICA MINOLTA devices, though)

    usb 0x132b 0x208b

## [See also]

-   [CUPS](https://wiki.gentoo.org/wiki/CUPS "CUPS") --- covers the installation and maintenance of printers using CUPS and [Samba](https://wiki.gentoo.org/wiki/Samba "Samba").