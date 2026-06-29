# Using Network Printers

This help document describes how to discover, configure, and use TCP/IP network printers with CUPS.

## Automatic Configuration Using Bonjour

Most network printers support a protocol known as Bonjour, which is a combination of zero-configuration networking ("ZeroConf"), multicast DNS (mDNS), and DNS service discovery (DNS-SD) standards published by the Internet Engineering Task Force (IETF), the same group that defined TCP/IP and all of the networking we use today.

A printer that supports Bonjour can be found automatically using the `dnssd` backend. Run the `lpinfo(8)` command to find your printer's URI:

``` command
lpinfo --include-schemes dnssd -v
network dnssd://Acme%20Laser%20Pro._ipp._tcp.local./?uuid=545253fb-1cb7-4d8d-98ed-ab6cd607cea7
network dnssd://Bar99._printer.tcp.local./?uuid=f9efff58-9086-4c95-accb-81dee876a475
network dnssd://Example%20EX-42._ipps._tcp.local./?uuid=4a0c67ad-2824-4ddf-9115-7d4226c5fe65
network dnssd://Foo%20Fighter-1969._pdl-datastream._tcp.local./?uuid=4e216bea-c3de-4f65-a710-c99e11c80d2b
```

You can then [add a printer](admin.html#PRINTERS) using the URI reported.

## Manual Configuration Using IP Addresses

You can also manually configure a printer using its Internet Protocol v4 (IPv4) address. This address is either configured manually ("static IP") through the printer's control panel or set using an automatic network protocol such as the Dynamic Host Control Protocol (DHCP) or ZeroConf.

> **Note:** Configuring a printer using an IP address set using DHCP or ZeroConf is not recommended since the address will change every time the printer is turned on or after long periods of inactivity. Thus, every time the address changes you will need to modify the print queue using the `lpadmin` command.

### Finding the IP Address

You can normally find the IP address of a printer on the printer's control panel or by printing the configuration or status page. The [Simple Network Management Protocol (SNMP)](#SNMP) can also be used to get the IP address remotely. To test that the IP address has been successfully assigned and that the printer is properly connected to your LAN or Wi-Fi network, type:

``` command
ping ip-address
```

where "ip-address" is the address reported by the printer's control panel, configuration page, and/or status page. If the connection is working properly you will see something like:

``` command
ping 10.0.1.42
PING 10.0.1.42 (10.0.1.42): 56 data bytes
64 bytes from 10.0.1.42: icmp_seq=0 ttl=15 time=1.123 ms
64 bytes from 10.0.1.42: icmp_seq=1 ttl=15 time=2.034 ms
64 bytes from 10.0.1.42: icmp_seq=2 ttl=15 time=1.765 ms
64 bytes from 10.0.1.42: icmp_seq=3 ttl=15 time=1.234 ms
...
```

If the connection is not working properly you will see something like:

``` command
ping 10.0.1.42
PING 10.0.1.42 (10.0.1.42): 56 data bytes
Request timeout for icmp_seq 0
Request timeout for icmp_seq 1
...
```

Press CTRL+C to quit the `ping` command.

> **Note:** If the command does not show responses from the printer, verify that the printer or print server is powered on and connected to the same LAN or Wi-Fi network as your computer. For LAN connections, also verify that your network cabling is good.

### Choosing a Network Protocol (Backend)

CUPS supports most network printers using one of three TCP/IP-based protocols: [AppSocket](#SOCKET), [Internet Printing Protocol](#IPP), and [Line Printer Daemon](#LPD). The following sections describe the options for each of the backends.

#### AppSocket Protocol (aka JetDirect)

The AppSocket protocol (sometimes also called the JetDirect protocol, owing to its origins with the HP JetDirect network interfaces) is the simplest and fastest network protocol used for printers. AppSocket printing normally happens over port 9100 and uses the `socket` backend. Device URIs for the `socket` backend look like this:

``` example
socket://ip-address
socket://ip-address/?contimeout=30
socket://ip-address/?waiteof=false
socket://ip-address/?contimeout=30&waiteof=false
socket://ip-address:port-number/?...
```

The "contimeout" option controls the number of seconds that the backend will wait to obtain a connection to the printer. The default is 1 week or 604800 seconds.

The "waiteof" option controls whether the `socket` backend waits for the printer to complete the printing of the job. The default is to wait (`waiteof=true`). Add `waiteof=false` to the URI to tell the backend not to wait.

> **Note:** While the AppSocket protocol is simple and fast, it also offers no security and is often an attack vector with printers. Consider using the [Internet Printing Protocol](#IPP) which supports encryption and other security features.

#### Internet Printing Protocol (IPP)

IPP is the only protocol that CUPS supports natively and is supported by most network printers and print servers. IPP supports encryption and other security features over port 631 and uses the `http` (Windows), `ipp`, and `ipps` backends. Device URIs for these backends look like this:

``` example
http://ip-address-or-hostname:port-number/printers/name/.printer
ipp://ip-address/ipp/print
ipp://ip-address-or-hostname/printers/name
ipps://ip-address/ipp/print
ipps://ip-address:443/ipp/print
ipps://ip-address-or-hostname/printers/name
```

The backends supports many options, which are summarized in [Table 2](#TABLE2). Like all backends, options are added to the end of the URI using the URL form encoding format, for example:

``` example
ipp://10.0.1.42/ipp/print?version=1.1
ipps://10.0.1.42:443/ipp/print?waitjob=false&waitprinter=false
```


| Option | Description |
|----|----|
| `contimeout=`*`seconds`* | Specifies the number of seconds to wait for the connection to the printer to complete (default 1 week or 604800 seconds). |
| `encryption=always` | Specifies that the connection to the IPP printer should be encrypted using SSL. |
| `encryption=ifrequested` | Specifies that the connection to the IPP printer should only be encrypted if the printer requests it. |
| `encryption=never` | Specifies that the connection to the IPP printer should not be encrypted. |
| `encryption=required` | Specifies that the connection to the IPP printer should be encrypted using TLS. |
| `version=1.0` | Specifies that version 1.0 of the IPP protocol should be used instead of the default version 2.0. |
| `version=1.1` | Specifies that version 1.1 of the IPP protocol should be used instead of the default version 2.0. |
| `version=2.1` | Specifies that version 2.1 of the IPP protocol should be used instead of the default version 2.0. |
| `waitjob=false` | Specifies that the IPP backend should not wait for the job to complete. |
| `waitprinter=false` | Specifies that the IPP backend should not wait for the printer to become idle before sending the print job. |

Table 2: IPP URI Options


#### Line Printer Daemon (LPD) Protocol (aka lpr)

LPD is the original network printing protocol created for the Berkeley UNIX line printer daemon (spooler) and is supported by many network printers. LPD printing normally happens over port 515 and uses the `lpd` backend. Device URIsfor the `lpd` backend look like this:

``` example
lpd://ip-address/queue
lpd://ip-address/queue?format=l
lpd://ip-address/queue?format=l&reserve=rfc1179
```

[Table 3](#TABLE3) summarizes the options supported by the `lpd` backend.

> **Note:** Due to limitations in the LPD protocol, we do not recommend using it if the printer or server supports any of the other protocols. Like AppSocket, LPD offers no security and is a common attack vector. LPD also, by default, requires that the computer save a copy of the entire print job before sending it to the printer - this can result in gigabytes of print data being saved to disk before any printing happens, delaying print jobs and shortening the life of your mass storage device!


| Option | Description |
|----|----|
| `banner=on` | Specifies that a banner page should be printed by the printer. |
| `contimeout=`*`seconds`* | Specifies the number of seconds to wait for the connection to the printer to complete (default 1 week or 604800 seconds). |
| `format=f` | Specifies that the print data is a plain text file. |
| `format=o` | Specifies that the print data is a PostScript file. |
| `format=p` | Specifies that the print data is a plain text file that should be "pretty" printed with a header and footer. |
| `mode=stream` | Specifies that the backend should stream print data to the printer and not wait for confirmation that the job has been successfully printed. |
| `order=data,control` | Specifies that the print data files should be sent before the control file. |
| `reserve=none` | Specifies that the backend should not reserve a source port. |
| `reserve=rfc1179` | Specifies that the backend should reserve a source port from 721 to 731 as required by RFC 1179. |
| `sanitize_title=no` | Specifies that the job title string should not be restricted to ASCII alphanumeric and space characters. |
| `sanitize_title=yes` | Specifies that the job title string should be restricted to ASCII alphanumeric and space characters. |
| `timeout=`*`seconds`* | Specifies the number of seconds to wait for LPD commands to complete (default 5 minutes or 300 seconds). |

Table 3: LPD URI Options


## Finding Printers Using SNMP

Whenever you view the administration web page or a list of supported device URIs, the `snmp` backend can probe the local network(s) using Simple Network Management Protocol (SNMP) v1 broadcasts. Printers that respond to these broadcasts are then interrogated for the make, model, and supported protocols, yielding a device URI that can be used to add the printer.

The [`/etc/cups/snmp.conf`](man-cups-snmp.conf.html) file configures the `snmp` backend. Add the following line to enable discovery using the `snmp` backend:

``` example
Address @LOCAL
```

If you don't use "public" as your community name, change the `Community` line as well:

``` example
Community your community name
```

> **Note:** The `snmp` backend will not be able to find any printers on your network if SNMP v1 or broadcasting are disabled on your network. Also, broadcasts are typically limited to the local subnet, so printers on different networks cannot be discovered using SNMP.

### Troubleshooting SNMP Problems

The `snmp` backend sometimes exposes problems in vendor implementations. If you are experiencing long delays in loading the CUPS web interface administration page, or if you don't see your printer listed, the following instructions will help you to diagnose those problems and/or provide important feedback to the CUPS developers so that we can correct problems and improve the `snmp` backend in future releases.

The SNMP backend supports a debugging mode that is activated by running it from a shell prompt. Run the following command to get a verbose log of the `snmp` backend:

``` command
CUPS_DEBUG_LEVEL=2 /usr/lib/cups/backend/snmp @LOCAL 2>&1 | tee snmp.log
```

On macOS you'll find the backend in /usr/libexec/cups/backend instead:

``` command
CUPS_DEBUG_LEVEL=2 /usr/libexec/cups/backend/snmp @LOCAL 2>&1 | tee snmp.log
```

The output will look something like this:

``` example
 1  INFO: Using default SNMP Address @LOCAL
 2  INFO: Using default SNMP Community public
 3  DEBUG: Scanning for devices in "public" via "@LOCAL"...
 4  DEBUG: 0.000 Sending 46 bytes to 10.0.1.255...
 5  DEBUG: SEQUENCE 44 bytes
 6  DEBUG:     INTEGER 1 bytes 0
 7  DEBUG:     OCTET STRING 6 bytes "public"
 8  DEBUG:     Get-Request-PDU 31 bytes
 9  DEBUG:         INTEGER 4 bytes 1149539174
10  DEBUG:         INTEGER 1 bytes 0
11  DEBUG:         INTEGER 1 bytes 0
12  DEBUG:         SEQUENCE 17 bytes
13  DEBUG:             SEQUENCE 15 bytes
14  DEBUG:                 OID 11 bytes .1.3.6.1.2.1.25.3.2.1.2.1
15  DEBUG:                 NULL VALUE 0 bytes
16  DEBUG: 0.001 Received 55 bytes from 10.0.1.42...
17  DEBUG: community="public"
18  DEBUG: request-id=1149539174
19  DEBUG: error-status=0
20  DEBUG: SEQUENCE 53 bytes
21  DEBUG:     INTEGER 1 bytes 0
22  DEBUG:     OCTET STRING 6 bytes "public"
23  DEBUG:     Get-Response-PDU 40 bytes
24  DEBUG:         INTEGER 4 bytes 1149539174
25  DEBUG:         INTEGER 1 bytes 0
26  DEBUG:         INTEGER 1 bytes 0
27  DEBUG:         SEQUENCE 26 bytes
28  DEBUG:             SEQUENCE 24 bytes
29  DEBUG:                 OID 11 bytes .1.3.6.1.2.1.25.3.2.1.2.1
30  DEBUG:                 OID 9 bytes .1.3.6.1.2.1.25.3.1.5
31  DEBUG: add_cache(addr=0xbfffe170, addrname="10.0.1.42", uri="(null)", id="(null)", make_and_model="(null)")
32  DEBUG: 0.002 Sending 46 bytes to 10.0.1.42...
33  DEBUG: SEQUENCE 44 bytes
34  DEBUG:     INTEGER 1 bytes 0
35  DEBUG:     OCTET STRING 6 bytes "public"
36  DEBUG:     Get-Request-PDU 31 bytes
37  DEBUG:         INTEGER 4 bytes 1149539175
38  DEBUG:         INTEGER 1 bytes 0
39  DEBUG:         INTEGER 1 bytes 0
40  DEBUG:         SEQUENCE 17 bytes
41  DEBUG:             SEQUENCE 15 bytes
42  DEBUG:                 OID 11 bytes .1.3.6.1.2.1.25.3.2.1.3.1
43  DEBUG:                 NULL VALUE 0 bytes
44  DEBUG: 0.003 Received 69 bytes from 10.0.1.42...
45  DEBUG: community="public"
46  DEBUG: request-id=1149539175
47  DEBUG: error-status=0
48  DEBUG: SEQUENCE 67 bytes
49  DEBUG:     INTEGER 1 bytes 0
50  DEBUG:     OCTET STRING 6 bytes "public"
51  DEBUG:     Get-Response-PDU 54 bytes
52  DEBUG:         INTEGER 4 bytes 1149539175
53  DEBUG:         INTEGER 1 bytes 0
54  DEBUG:         INTEGER 1 bytes 0
55  DEBUG:         SEQUENCE 40 bytes
56  DEBUG:             SEQUENCE 38 bytes
57  DEBUG:                 OID 11 bytes .1.3.6.1.2.1.25.3.2.1.3.1
58  DEBUG:                 OCTET STRING 23 bytes "HP LaserJet 4000 Series"
59  DEBUG: 1.001 Probing 10.0.1.42...
60  DEBUG: 1.001 Trying socket://10.0.1.42:9100...
61  DEBUG: 10.0.1.42 supports AppSocket!
62  DEBUG: 1.002 Scan complete!
63  network socket://10.0.1.42 "HP LaserJet 4000 Series" "HP LaserJet 4000 Series 10.0.1.42" ""
```

The first two lines are just informational and let you know that the default community name and address are being used. Lines 3-15 contain the initial SNMP query for the device type OID (.1.3.6.1.2.1.25.3.2.1.2.1) from the Host MIB.

Lines 16-31 show the response we got from an HP LaserJet 4000 network printer. At this point we discover that it is a printer device and then send another SNMP query (lines 32-43) for the device description OID (.1.3.6.1.2.1.25.3.2.1.3.1) from the Host MIB as well.

Lines 44-58 show the response to the device description query, which tells us that this is an HP LaserJet 4000 Series printer.

On line 59 we start our active connection probe and discover that this print server supports the AppSocket (JetDirect) protocol on port 9100.

Finally, line 63 shows the device information line for the print server that is sent to CUPS.

If you don't see your printer listed, or the wrong information is listed, then you need to gather more information on the printer. The easiest way to do this is to run the snmpwalk command:

``` command
snmpwalk -Cc -v 1 -c public ip-address | tee snmpwalk.log
```

where "ip-address" is the IP address of the printer or print server. You should see a *lot* of values stream by - the ones you want to see are:

``` example
HOST-RESOURCES-MIB::hrDeviceType.1 = OID: HOST-RESOURCES-TYPES::hrDevicePrinter
HOST-RESOURCES-MIB::hrDeviceDescr.1 = STRING: HP LaserJet 4000 Series
```

The hrDeviceType line should show hrDevicePrinter; if not, then your printer or print server doesn't identify itself as a printer. The hrDeviceDescr line should provide a human-readable string for the make and model of the printer, although in some cases you'll just see something less useful like "Axis OfficeBASIC Parallel Print Server".

Once you have collected the snmpwalk output, you should go to the [CUPS Issue Tracker](https://github.com/apple/cups/issues) page to submit a feature request to support your printer or print server. Be sure to attach those two log files you created - they will help us to identify the SNMP values we need to look for.
