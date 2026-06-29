**Resources**

[[]][Home](https://support.brother.com/g/b/producttop.aspx?c=us&lang=en&prod=mfcj6710dw_all)

### [Brother mfcj6710dw]

Install drivers and integrate with CUPS:

-   Create spooler directory:

`user `[`$`]`mkdir -p /var/spool/lpd/mfcj6710dw`

`user `[`$`]`chown lp:lp /var/spool/lpd/mfcj6710dw`

`user `[`$`]`chmod 700 /var/spool/lpd/mfcj6710dw`

-   Create spooler directory:

`user `[`$`]`rpm -ivh --nodeps mfcj6710dwlpr-3.0.0-1.i386.rpm`

`user `[`$`]`rpm -ivh --nodeps mfcj6710dwcupswrapper-3.0.0-1.i386.rpm`

-   Link to cupswrapper:

`user `[`$`]`ln -s /opt/brother/Printers/mfcj6710dw/lpd/filtermfcj6710dw /usr/libexec/cups/filter/brother_lpdwrapper_mfcj6710dw`

-   Restart cups:

`root `[`#`]`/etc/init.d/cups restart`

Then go to the CUPS admin interface under [http://localhost:631/](http://localhost:631/) and select lpd://\<IP ADDRESS\>/BINARY_P1

## [See also]

-   [Brother networked printer](https://wiki.gentoo.org/wiki/Brother_networked_printer "Brother networked printer")
-   [Driverless printing](https://wiki.gentoo.org/wiki/Driverless_printing "Driverless printing")