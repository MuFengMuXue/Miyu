This page contains [[changes](https://wiki.gentoo.org/index.php?title=Driverless_printing&diff=1387831)] which are not marked for translation.

\

**Resources**

[[]][Bugs (upstream)](https://github.com/openprinting/cups-filters/issues?q=driverless+sort%3Aupdated-desc+)

[[]][lpadmin(8)](https://www.cups.org/doc/man-lpadmin.html)

## Contents

-   [[1] [Preconditions]](#Preconditions)
-   [[2] [Setup the printer]](#Setup_the_printer)
-   [[3] [Set the user\'s default printer]](#Set_the_user.27s_default_printer)
-   [[4] [Go ahead with printing]](#Go_ahead_with_printing)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [The driverless command]](#The_driverless_command)
-   [[7] [See also]](#See_also)
-   [[8] [External resources]](#External_resources)
-   [[9] [References]](#References)

## [Preconditions]

-   [[[net-print/cups]](https://packages.gentoo.org/packages/net-print/cups)[]] needs to be [installed](https://wiki.gentoo.org/wiki/Printing#Emerge "Printing") and [started](https://wiki.gentoo.org/wiki/Printing#Service "Printing").
-   The printer needs to be connected to the network with a known IP address.

## [Setup the printer]

Following procedure shown here with Brother\'s [HL-L2340DW](http://support.brother.com/g/b/spec.aspx?c=us&lang=en&prod=hll2340dw_us_eu_as) as an example can be used.

The [lpadmin] command is called with these options:

    -p destination          Specify/add the named destination
                            This can be arbitrary e.g. foobar.

    -E                      Enable and accept jobs on the printer (after -p)

    -v device-uri           Specify the device URI for the printer
                            Needs go have the format ipp://192.168.178.23/ipp
                            using the real IP address of the printer

    -m model                Specify a standard model/PPD file for the printer
                            Must be everywhere

Models other than **everywhere** are deprecated and will not be supported in a future version of CUPS.^[\[1\]](#cite_note-1)^

`root `[`#`]`lpadmin -p foobar -E -v ipp://192.168.178.23/ipp/print -m everywhere`

This adds the printer to the configuration and also creates the **foobar.ppd** file in [/etc/cups/ppd/].

`user `[`$`]`ls -al /etc/cups/ppd/`

    total 16
    drwxr-xr-x 2 root lp   4096 Apr 15 13:16 .
    drwxr-xr-x 5 root lp   4096 Apr 15 13:19 ..
    -rw-r----- 1 root lp   8113 Apr 15 13:16 foobar.ppd
    -rw-r--r-- 1 root root    0 Apr 15 11:51 .keep_net-print_cups-0

    localhost - - [15/Apr/2020:12:55:50 +0200] "POST / HTTP/1.1" 401 75 CUPS-Get-Devices successful-ok
    localhost - root [15/Apr/2020:12:55:50 +0200] "POST / HTTP/1.1" 200 1814 CUPS-Get-Devices -
    localhost - - [15/Apr/2020:12:59:16 +0200] "POST / HTTP/1.1" 200 11535 CUPS-Get-PPDs -
    localhost - - [15/Apr/2020:13:02:17 +0200] "POST /admin/ HTTP/1.1" 401 8441 CUPS-Add-Modify-Printer successful-ok
    localhost - root [15/Apr/2020:13:02:17 +0200] "POST /admin/ HTTP/1.1" 200 8441 CUPS-Add-Modify-Printer successful-ok

The setup can be viewed using [lpstat -le]:

`user `[`$`]`lpstat -le`

    foobar permanent ipp://localhost/printers/foobar ipp://192.168.178.23/ipp/print

## [][Set the user\'s default printer]

`user `[`$`]`lpstat -a`

    foobar accepting requests since Wed Apr 15 2020 13:16:32 PM CEST

`user `[`$`]`lpoptions -d foobar`

    copies=1 device-uri=ipp://192.168.178.23/ipp finishings=3 job-cancel-after=10800 job-hold-until=no-hold job-priority=50 job-sheets=none,none marker-change-time=0 number-up=1 printer-commands=none printer-info='Brother HL-L2340D series' printer-is-accepting-jobs=true printer-is-shared=true printer-is-temporary=false printer-location printer-make-and-model='HL-L2340D series - IPP Everywhere' printer-state=3 printer-state-change-time=1591115192 printer-state-reasons=none printer-type=36948 printer-uri-supported=ipp://localhost/printers/foobar

`user `[`$`]`lpstat -t`

    scheduler is running
    system default destination: foobar
    device for foobar: ipp://192.168.178.23/ipp
    foobar accepting requests since Wed 15 Apr 2020 01:02:17 PM CEST
    printer foobar is idle.  enabled since Wed 15 Apr 2020 01:02:17 PM CEST

## [Go ahead with printing]

`user `[`$`]`echo 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ...' | lp`

    request id is foobar-545 (0 file(s))

## [Troubleshooting]

-   Driverless printing on USB connected printers seems to require additional software like [ipp-usb](https://github.com/OpenPrinting/ipp-usb#ipp-usb).
-   Using CUPS\' graphical interface might confusingly show more than one IPP Everywhere entries. The trademarked one should work.
-   [Forums topic: How to install an Brother (DCP-J572) Printer correctly?](https://forums.gentoo.org/viewtopic-p-8303306.html#8303306)
-   [Forums topic: Internet printing protocol - driverless printing](https://forums.gentoo.org/viewtopic-t-1111418.html)
-   [Forums topic: brlaser](https://forums.gentoo.org/viewtopic-t-1112076.html)
-   [Forums topic: Unable to print to a network printer](https://forums.gentoo.org/viewtopic-t-1123318.html)
-   [Forums topic: How do you add a network printer?](https://forums.gentoo.org/viewtopic-t-1127275.html)

<!-- -->

-   Find out which printers are available

`root `[`#`]`lpinfo -lv`

```
Device: uri = http
        class = network
        info = Internet Printing Protocol (http)
        make-and-model = Unknown
        device-id =
        location =
Device: uri = ipp
        class = network
        info = Internet Printing Protocol (ipp)
        make-and-model = Unknown
        device-id =
        location =
Device: uri = lpd
        class = network
        info = LPD/LPR Host or Printer
        make-and-model = Unknown
        device-id =
        location =
Device: uri = ipps
        class = network
        info = Internet Printing Protocol (ipps)
        make-and-model = Unknown
        device-id =
        location =
Device: uri = beh
        class = network
        info = Backend Error Handler
        make-and-model = Unknown
        device-id =
        location =
Device: uri = cups-brf:/
        class = file
        info = CUPS-BRF
        make-and-model = Virtual Braille BRF Printer
        device-id = MFG:Generic;MDL:CUPS-BRF Printer;DES:Generic CUPS-BRF Printer;CLS:PRINTER;CMD:BRF;
        location =
Device: uri = socket
        class = network
        info = AppSocket/HP JetDirect
        make-and-model = Unknown
        device-id =
        location =
Device: uri = https
        class = network
        info = Internet Printing Protocol (https)
        make-and-model = Unknown
        device-id =
        location =
Device: uri = lpd://BRW1008B1372DF2/BINARY_P1
        class = network
        info = Brother HL-L2340D series
        make-and-model = Brother HL-L2340D series
        device-id = MFG:Brother;CMD:PJL,HBP,URF;MDL:HL-L2340D series;CLS:PRINTER;CID:Brother Laser Type1;URF:W8,CP1,IS4-1,MT1-3-4-5-8,OB10,PQ4,RS300-600,V1.3,DM1;
        location =
```

That command would create some stuff in the logs:

[FILE] **`/var/log/cups/access_log`**

    localhost - - [15/Apr/2020:12:55:50 +0200] "POST / HTTP/1.1" 401 75 CUPS-Get-Devices successful-ok
    localhost - root [15/Apr/2020:12:55:50 +0200] "POST / HTTP/1.1" 200 1814 CUPS-Get-Devices -

[FILE] **`/var/log/cups/error_log`**

    E [15/Apr/2020:12:55:50 +0200] [CGI] Unable to execute ippfind utility: No such file or directory

No need to worry about [[[**ippfind utility**]](https://bugs.gentoo.org/show_bug.cgi?id=720958)[]]. It is not there, but who needs it?

-   Get some more information with **lpinfo -m**:

`user `[`$`]`lpinfo -m | grep -i ipp`

    drv:///cupsfilters.drv/pwgrast.ppd Generic IPP Everywhere Printer
    everywhere IPP Everywhere

The important is the last line **everywhere IPP Everywhere**. That query creates another line in the access log and again says it cannot find ippfind.

[FILE] **`/var/log/cups/access_log`**

    localhost - - [15/Apr/2020:12:55:50 +0200] "POST / HTTP/1.1" 401 75 CUPS-Get-Devices successful-ok
    localhost - root [15/Apr/2020:12:55:50 +0200] "POST / HTTP/1.1" 200 1814 CUPS-Get-Devices -
    localhost - - [15/Apr/2020:12:59:16 +0200] "POST / HTTP/1.1" 200 11535 CUPS-Get-PPDs -

[FILE] **`/var/log/cups/error_log`**

    E [15/Apr/2020:12:55:50 +0200] [CGI] Unable to execute ippfind utility: No such file or directory
    E [15/Apr/2020:12:59:16 +0200] [CGI] Unable to execute ippfind utility: No such file or directory

-   disabled - reason unknown

If nothing works the printer might be **disabled**

`user `[`$`]`lpstat -p`

    printer foobar disabled since Fri 16 Jul 2021 03:08:25 PM CEST -
            reason unknown

`root `[`#`]`cupsenable foobar`

`user `[`$`]`lpstat -p`

    printer Brother now printing Brother-669.  enabled since Fri 16 Jul 2021 03:24:54 PM CEST
            Waiting for job to complete.

## [The driverless command]

The [driverless](https://wiki.gentoo.org/wiki/Printing#Avahi "Printing") command is part of [[[net-print/cups-filters]](https://packages.gentoo.org/packages/net-print/cups-filters)[]].

[driverless] generates PPD files for printers which are designed for driverless IPP printing (currently IPP Everywhere, AirPrint, Mopria, and Wi-Fi-Direct printers, network printers and also IPP-over-USB printers with the help of ippusbxd(8)) by polling capability information from the printers via IPP. it can be either called for listing suitable printers in the network and for actually generating the PPD. It can also be called by CUPS when CUPS is listing available PPDs/drivers or creating print queues, making the setup of driverless printers with printer setup tools transparently working. \[\...\] The CUPS web interface at [http://localhost:631/](http://localhost:631/), and CUPS\' command line utilities can use [driverless] with CUPS to list available driverless-capable printers, determine their IPP device URIs and generate PPDs for them. The printers will be automatically and correctly set up for driverless printing. Note that driverless printing requires IPP communication with the printer.^[\[2\]](#cite_note-2)^

`user `[`$`]`driverless`

    ERROR: Unable to execute ippfind utility: No such file or directory

The absence of [ippfind] might be due to [[[net-print/cups-filters]](https://packages.gentoo.org/packages/net-print/cups-filters)[]] being compiled without [avahi](https://packages.gentoo.org/useflags/zeroconf) support. But printer setup is possible and the printer should work.

## [See also]

-   [Printing](https://wiki.gentoo.org/wiki/Printing "Printing") --- covers the installation and maintenance of printers using CUPS and [Samba](https://wiki.gentoo.org/wiki/Samba "Samba").
-   [Brother networked printer](https://wiki.gentoo.org/wiki/Brother_networked_printer "Brother networked printer")

## [External resources]

-   [Repository news item](https://www.gentoo.org/support/news-items/2023-12-17-cups-filters.html)
-   [https://openprinting.github.io/current/#the-new-architecture-for-printing-and-scanning](https://openprinting.github.io/current/#the-new-architecture-for-printing-and-scanning)
-   [https://www.cups.org/doc/spec-ipp.html](https://www.cups.org/doc/spec-ipp.html)
-   [https://openprinting.github.io/driverless/01-standards-and-their-pdls/](https://openprinting.github.io/driverless/01-standards-and-their-pdls/)
-   [http://shallowsky.com/blog/linux/cups-printers-urls.html](http://shallowsky.com/blog/linux/cups-printers-urls.html)
-   [https://pwg.org/pwg-books/ippguide.html](https://pwg.org/pwg-books/ippguide.html)
-   [https://wiki.debian.org/CUPSDriverlessPrinting#Driverless_Printing_and_Printers](https://wiki.debian.org/CUPSDriverlessPrinting#Driverless_Printing_and_Printers)
-   [http://support.brother.com/g/b/spec.aspx?c=us&lang=en&prod=hll2340dw_us_eu_as](http://support.brother.com/g/b/spec.aspx?c=us&lang=en&prod=hll2340dw_us_eu_as)

## [References]

1.  [[[↑](#cite_ref-1)] [[https://www.cups.org/doc/man-lpadmin.html#OPTIONS](https://www.cups.org/doc/man-lpadmin.html#OPTIONS)]]
2.  [[[↑](#cite_ref-2)] [[man 1 driverless]]]