Many Microsoft servers started using encryption for their shares. This is also the case for Windows printer shares. In order to print from a Gentoo installation Samba and CUPS will be needed.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Troubleshooting]](#Troubleshooting)
-   [[4] [See also]](#See_also)

## [Installation]

Edit [/etc/portage/package.use] to enable active directory support for CIFS and Samba. The following USE flags will pull in the required encryption needed for newer Windows servers:

`root `[`#`]`echo "net-fs/cifs-utils ads creds upcall" >> /etc/portage/package.use `

`root `[`#`]`echo "net-fs/samba caps addns ads" >> /etc/portage/package.use`

Next (re)install [[[net-fs/samba]](https://packages.gentoo.org/packages/net-fs/samba)[]] and [[[net-print/cups]](https://packages.gentoo.org/packages/net-print/cups)[]]:

`root `[`#`]`emerge --ask --oneshot net-fs/samba net-print/cups`

## [Configuration]

Setting up printers is fairly simple through the web-interface of CUPS. Point a browser to [`https://localhost:631`](https://localhost:631) (which is the default location for the CUPS interface). Click [Administration] and choose [Add Printer]. There will be a prompt for a username and password of the printer administrator. Now choose [Windows Printer via SAMBA] and click continue. The connection to the Samba share is crucial to get the printers working. If on a domain a connection URL will need to be entered. An example is

`smb://USERNAME:PASSWORD@DOMAIN/URL/PRINTERSHARE`

Where the values for `USERNAME`, `PASSWORD`, `DOMAIN`, `URL` and `PRINTERSHARE` are properly substituted with the appropriate values for each use case. When not on a network with a domain-server leave out the `DOMAIN/` section of the string.

## [Troubleshooting]

If users cannot print try to connect to the print server using the Samba client:

`user `[`$`]`smbclient -W DOMAIN -U USERNAME //SERVER/PRINTER`

    Password: PASSWORD
    Domain=[DOMAIN] OS=[Windows Server 2008 R2 Datacenter 7601 Service Pack 1] Server=[Windows Server 2008 R2 Datacenter 6.1]
    smb: \> print test.ps
    printing file test.ps as test.ps (196,6 kb/s) (average 196,6 kb/s)
    smb: \> quit

Where `test.ps` is a postscript file located in the local current working directory.

If this test is working, then something went bad when setting up CUPS.

## [See also]

[Configuring a Linux Client for a Windows Print Server](https://wiki.gentoo.org/wiki/Printing#Configuring_a_Linux_Client_for_a_Windows_Print_Server "Printing")