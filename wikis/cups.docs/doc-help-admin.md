# Command-Line Printer Administration

This help document describes how to configure and manage destinations with CUPS.

## Introduction

Destinations are individual printers and classes (pools) of printers. [Printers](#PRINTERS) use a description file with one or more driver ("filter") programs that communicate with the printer through a "backend" program. CUPS currently uses PPD (PostScript Printer Description) files to describe the printer and driver programs needed, some of which come with CUPS while others come with your operating system or Linux distribution. Backends are specified using a URI (Universal Resource Identifier) where the URI scheme is the backend name, e.g., "ipp://11.22.33.44/ipp/print" specifies the "ipp" backend - like PPD files, some backends come with CUPS while others come with your operating system.

[Classes](#CLASSES) are associated with one or more printers and are typically used to distribute print jobs amongst a group of printers or provide redundancy or high availability when printing. Print jobs sent to a class are forwarded to the next available printer in the class.

The [`lpadmin(8)`](man-lpadmin.html) program is used to add, modify, or delete destinations, while the [`lpinfo(8)`](man-lpinfo.html) command is used to list the available printer drivers and backends. The [`cupsctl(8)`](man-cupsctl.html) program is used to manage the printing system as a whole, including things like [debug logging](#DEBUG) and [printer sharing](#SHARING). The CUPS web interface ("http://localhost:631" or "https://servername:631") can also be used, and most operating systems provide their own GUI administration tools.

## Managing Printers

The `lpadmin` command is used to create, modify, or delete a printer. The `-p` option specifies a printer to create or modify:

``` command
lpadmin -p printername ...
```

The `lpadmin` accepts several additional options after `-p printername` when adding or modifying a printer:

`-D "description"`
Sets the description of the printer which is often shown instead of the printer name, for example "HP LaserJet".

`-E`
Enables the printer and accepts new print jobs.

`-L "location"`
Sets the location of the printer, for example "Conference Room".

`-m model`
Sets the printer driver using the [model name](#MODELS).

`-o option=value`
Sets the [named option](#OPTIONS).

`-v device-uri`
Sets the [URI for the printer](#DEVICES).

The `-x` option deletes the named printer:

``` command
lpadmin -x printername
```

### Printer Drivers and PPDs

The `-m` option to `lpadmin` specifies the driver ("model") to use for the printer. You can run the `lpinfo -m` command to list all of the available drivers ("models") on your system:

``` command
lpinfo -m
```

Each line contains the driver name followed by its description, for example:

``` example
drv:///sample.drv/dymo.ppd Dymo Label Printer
drv:///sample.drv/epson9.ppd Epson 9-Pin Series
drv:///sample.drv/epson24.ppd Epson 24-Pin Series
drv:///sample.drv/generpcl.ppd Generic PCL Laser Printer
drv:///sample.drv/generic.ppd Generic PostScript Printer
drv:///sample.drv/deskjet.ppd HP DeskJet Series
drv:///sample.drv/laserjet.ppd HP LaserJet Series PCL 4/5
drv:///sample.drv/intelbar.ppd Intellitech IntelliBar Label Printer, 2.1
drv:///sample.drv/okidata9.ppd Oki 9-Pin Series
drv:///sample.drv/okidat24.ppd Oki 24-Pin Series
drv:///sample.drv/zebracpl.ppd Zebra CPCL Label Printer
drv:///sample.drv/zebraep1.ppd Zebra EPL1 Label Printer
drv:///sample.drv/zebraep2.ppd Zebra EPL2 Label Printer
drv:///sample.drv/zebra.ppd Zebra ZPL Label Printer
everywhere IPP Everywhere
```

The `everywhere` driver is used for nearly all modern networks printers sold since about 2009. For example, the following command creates a destination for a printer at IP address 11.22.33.44:

``` command
lpadmin -p printername -E -v ipp://11.22.33.44/ipp/print -m everywhere
```

The CUPS sample drivers (the "drv:///sample.drv/..." lines above) can be used for "legacy" printers. For example, the following command creates a destination for a HP LaserJet printer at IP address 11.22.33.44:

``` command
lpadmin -p printername -E -v socket://11.22.33.44 -m drv:///sample.drv/laserjet.ppd
```

> Note: The CUPS sample drivers are designed to provide basic printing capabilities for the broadest range of printers possible, but generally do not exercise the full potential of the printers or CUPS. Other drivers (including the `everywhere` driver) provide greater printing capabilities and better print quality.

### Device URIs (Backends)

CUPS comes with several standard backends that communicate with printers:

1.  `dnssd`: The Bonjour (DNS-SD) protocol.
2.  `ipp`: The Internet Printing Protocol (IPP) with optional encryption.
3.  `ipps`: The Internet Printing Protocol with mandatory encryption.
4.  `lpd`: The Line Printer Daemon protocol.
5.  `socket`: The AppSocket (JetDirect) protocol.
6.  `usb`: The Universal Serial Bus (USB) printer class.

Run the `lpinfo -v` command to list the available backends and printers:

``` command
lpinfo -v
```

Each line contains the backend "class" followed by the backend name or a full printer device URI, for example:

``` example
network lpd
network ipps
network ipp
network socket
network dnssd://Acme%20Laser%20Pro._ipp._tcp.local./?uuid=545253fb-1cb7-4d8d-98ed-ab6cd607cea7
network dnssd://Bar99._printer.tcp.local./?uuid=f9efff58-9086-4c95-accb-81dee876a475
network dnssd://Example%20EX-42._ipps._tcp.local./?uuid=4a0c67ad-2824-4ddf-9115-7d4226c5fe65
network dnssd://Foo%20Fighter-1969._pdl-datastream._tcp.local./?uuid=4e216bea-c3de-4f65-a710-c99e11c80d2b
direct usb://ZP/LazerJet%20MFP?serial=42
```

The `network` class of backends is used for all network protocols. The [Using Network Printers](network.html) help document describes how to use the standard CUPS network backends. The `direct` class of backends is used for directly-connected printers such as USB and Bluetooth. Because these backends use a system-specific identifier, you should only use the reported device URIs.

Once you know the correct URI for the printer, set it using the `lpadmin` command's `-v` option:

``` command
lpadmin -p printername -v device-uri
```

### Printer Options

The `lpadmin` command allows you to set various options for a printer:

`-o cupsIPPSupplies=false`
Turns off IPP supply level reporting for a printer.

`-o cupsSNMPSupplies=false`
Turns off SNMP supply level reporting for a printer.

`-o name=value`
Sets the default value for the named PPD option. For example, `-o PageSize=Legal` sets the default page size to US Legal.

`-o printer-error-policy=name`
Sets the policy for errors such as printers that cannot be found or accessed, don't support the format being printed, fail during submission of the print data, or cause one or more filters to crash:

`abort-job`
Aborts the job on error.

`retry-job`
Retries the job at a future time.

`retry-current-job`
Retries the current job immediately.

`stop-printer`
Stops the printer on error.

`-o printer-is-shared=true/false`
Enables/disables per-printer sharing. See the section on [Printer Sharing](#SHARING) for more information.

`-o printer-op-policy=name`
Sets the operation policy associated with the printer. See the [Managing Operation Policies](policies.html) help document for more information.

`-u allow:{user|@group}{,user|,@group}*`
`-u allow:all`
`-u deny:{user|@group}{,user|,@group}*`
`-u deny:none`
Sets user-level access control for the printer. The `allow:` list defines a whitelist of users and groups while the `deny:` list defines a blacklist of users and groups.

## Printer Sharing

CUPS supports sharing of printers with other computers and mobile devices. Two `cupsctl` options control the general printer sharing features:

`--share-printers`
Enables sharing of printers with other computers and mobile devices on your local network.

`--remote-any`
Expands printer sharing to any network that can reach your server.

Once you have enabled printer sharing, you then must select which printers will be shared using the `lpadmin` command and the `-o printer-is-shared=true` option.

For example, to share two printers ("foo" and "bar") on the local network, run the following commands:

``` command
cupsctl --share-printers
lpadmin -p foo -o printer-is-shared=true
lpadmin -p bar -o printer-is-shared=true
```

## Managing Classes

The `lpadmin` command is used to create, modify, or delete a class. The `-c` option specifies a class to create or modify and is combined with the `-p` option:

``` command
lpadmin -p printername -c classname
```

The `-r` option specifies that the named printer is removed from the class:

``` command
lpadmin -p printername -r classname
```

The `-x` option deletes the named class:

``` command
lpadmin -x classname
```

## Debug Logging and Troubleshooting

The [printing system log files](man-cupsd-logs.html) track the activity of the scheduler, printer drivers, and backends. If problems occur and the log files do not provide sufficient details to diagnose the problem, you can enable debug logging using the `cupsctl` command:

``` command
cupsctl --debug-logging
```

To disable debug logging, run the same command with the `--no-debug-logging` option:

``` command
cupsctl --no-debug-logging
```
