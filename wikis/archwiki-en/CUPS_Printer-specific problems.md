# CUPS/Printer-specific problems

This article contains printer or manufacturer-specific instructions for CUPS.
See OpenPrinting if your printer is not already listed here, or if none of the listed drivers work.

## Brother
Drivers for several models:

{|class="wikitable"
! Printers
! Driver/filter
! Notes
|-
| DCP-1510 series (DCP-1510, DCP-1510r, DCP-1511, DCP-1512, DCP-1512r, DCP-1518) ||  ||
|-
| DCP-7010, DCP-7020, DCP-7025, DCP-8060, DCP-8065DN, FAX-2820, FAX-2920, HL-2030, HL-2040, HL-2070N, HL-5240, HL-5250DN, HL-5270DN, HL-5280DW, MFC-7220, MFC-7225N, MFC-7420, MFC-7820N, MFC-8460N, MFC-8660DN, MFC-8860DN, MFC-8870DW ||  ||
|-
| HL-4040CN, HL-4040CDN, HL-4050CDN, HL-4070CDW, MFC-9440CN, MFC-9450CDN, MFC-9840CDW, DCP-9040CN, DCP-9042CDN, DCP-9045CDN ||  ||
|-
| DCP-1510 series, DCP-1600 series, DCP-7030, DCP-7040, DCP-7055, DCP-7055W, DCP-7060D, DCP-7065DN, DCP-7080, DCP-L2500D series, DCP-L2520D series, DCP-L2540DW series, HL-1110 series, HL-1200 series, HL-2030 series, HL-2140 series, HL-2220 series, HL-2270DW series, HL-5030 series, HL-L2300D series, HL-L2320D series, HL-L2340D series, HL-L2360D series, MFC-1910W, MFC-1919NW, MFC-7240, MFC-7360N, MFC-7365DN, MFC-7840W, Lenovo M7605D ||  || Unofficial driver, may be compatible with more models
|}

Drivers for one model:

{| class="wikitable"
! Printer
! Driver/filter
! Notes
|-
| DCP-135C ||  ||
|-
| DCP-150C ||  ||
|-
| DCP-150C ||  ||
|-
| DCP-195C ||  ||
|-
| DCP-2550DW || ||
|-
| DCP-B7500D ||  ||
|-
| DCP-L3550CDW ||  || Use IPP driver as described here and here.
|-
| DCP-7020 || foomatic || Or Brother's driver.
|-
| DCP-7030 ||  ||
|-
| DCP-7065DN ||  ||
|-
| DCP-7090DW ||  ||
|-
| DCP-9020CDW ||  ||
|-
| DCP-9022CDW ||  ||
|-
| DCP-J515W ||  ||
|-
| DCP-J4110DW ||  ||
|-
| DCP-J925DW ||  || Use the  protocol as described in #Network printers. I need to restart the printer first, after trying to use ipp-protocol instead of socket.
|-
| DCP-J1200W ||  || "DCPJ1200W" is added automatically to cups when installing this aur package. multilib not required. SANE drivers for this model:
|-
| DCP-L2500D ||  || Better support for printer capabilities than
|-
| DCP-T430W ||  ||
|-
| DCP-T735DW ||  ||
|-
| FAX-2820 ||  ||
|-
| FAX-2840 ||  || Or foomatic - works mostly with . Same as the HL-2170W.
|-
| FAX-2940 ||  ||
|-
| HL-1110 ||  || Tested and it works
|-
| HL-2030 || foomatic || Or
|-
| HL-2035 || foomatic || Should be compatible with any drivers for the HL-2030.
|-
| HL-2040 || foomatic || Or
|-
| HL-2130 || foomatic (using the HL-2140 driver) || Or
|-
| HL-2135W ||  ||
|-
| HL-2140 || foomatic || Or
|-
| HL-2170W || foomatic || Or Brother's driver.
|-
| HL-2230 || foomatic || Same as HL-2170W. Select HL-2170W as the driver in CUPS admin when adding a printer.
|-
| HL-2250DN ||  ||  is broken?
|-
| HL-2270DW ||  ||
|-
| HL-2280DW ||  ||
|-
| HL-3045CN || Install Brother's driver or .||
|-
| HL-3140CW ||  || Use IPP and Brother's driver to avoid page-shrinking and endless blank printouts
|-
| HL-3150CDW ||  ||
|-
| HL-3170CDW ||  ||
|-
| HL-4150CDN ||  ||
|-
| HL-5140 || foomatic || Or Brother's driver.
|-
| HL-5340 || foomatic || Using the Generic PCL 6/PCL XL Printer - CUPS+Gutenprint ( and ). Or Brother's driver, which may result in failed prints with postscript errors.
|-
| HL-L2300D ||  ||  works better. Using the brother driver, only defaults are honored and print-specific settings are ignored.
|-
| HL-L2340DW ||  ||
|-
| HL-L2350DW ||  ||
|-
| HL-L2360DN ||  || Or
|-
| HL-L2360DW ||  ||  should works.
|-
| HL-L2365DW ||  ||  should works.
|-
| HL-L2380DW ||  ||
|-
| HL-L2390DW || Arch-provided Brother Driver || Choose the  Driverless Brother Printer that appears on the list of #Network printers.
|-
| HL-L2395DW ||  || Use the  protocol as described in #Network printers
|-
| HL-L3230CDW ||  || Or https://github.com/splitbrain/archlinux-brother-hll3230cdw
|-
| HL-L3270CDW ||  || Use the  protocol as described in #Network printers.
|-
| HL-L5100DN || HP LaserJet Foomatic driver || This model will emulate a HP LaserJet. Use the  protocol as described in #Network printers.
|-
| HL-L8360CDW ||  ||
|-
| MFC-420CN ||  ||
|-
| MFC-440CN ||  ||
|-
| MFC-7360N ||  || Or
|-
| MFC-7460DN || Gutenprint || Use the Generic PCL 6 Printer wide margin - CUPS+Gutenprint driver, with address .
|-
| MFC-7840W ||  || Or
|-
| MFC-9320CW || Install Brother's driver. ||
|-
| MFC-9332CDW ||  ||
|-
| MFC-9840CDW || foomatic || Or Brother's driver. This printer also works with the generic PCL-6 driver from the  package. Use pcl_p1 for the printer's address when using the PCL-6 driver.
|-
| MFC-J1300DW ||  || Use the  protocol as described in #Network printers.
|-
| MFC-J3540DW ||  ||
|-
| MFC-J435W ||  || Use  or  as described in the comments section of the AUR package page.
|-
| MFC-J470DW ||  || Use the  protocol as described in #Network printers.
|-
| MFC-J4710DW ||  ||
|-
| MFC-J480DW ||  || Use the  protocol as described in #Network printers.
|-
| MFC-J5520DW ||  ||
|-
| MFC-J5845DW ||  || Use the  protocol as described in #Network printers.
|-
| MFC-J5910DW ||  ||
|-
| MFC-J650DW || Install Brother's driver. ||
|-
| MFC-J6520DW ||  || Use the  protocol as described in #Network printers
|-
| MFC-J885DW ||  ||
|-
| MFC-J985DW ||  ||
|-
| MFC-L2700DN ||  || Please look also at the comments section of the AUR package page.
|-
| MFC-L2700DW ||  || Please look also at the comments section of the AUR package page.
|-
| MFC-L2710DN ||  || Use the  protocol as described in #Network printers.
|-
| MFC-L2710DW ||  || Use the  protocol as described in #Network printers.
|-
| MFC-L2720DW ||  || Please look also at the comments section of the AUR package page.
|-
| MFC-L2730DW ||  || Please look also at the comments section of the AUR package page.
|-
| MFC-L2740DW ||  || Please look also at the comments section of the AUR package page.
|-
| MFC-L2750DW ||  || Please look also at the comments section of the AUR package page.
|-
| MFC-L3770CDW ||  || Please look also at the comments section of the AUR package page.
|-
| MFC-L5800DW ||  ||
|-
| MFC-L8600CDW ||  || Please follow the instructions on the AUR page.
|-
| QL-500 ||  ||
|-
| QL-570 ||  ||
|-
| QL-580N ||  ||
|-
| QL-650TD ||  ||
|-
| QL-700 ||  ||
|-
| QL-710W ||  ||
|-
| QL-720NW ||  ||
|-
| QL-1050 ||  ||
|-
| QL-1050N ||  ||
|-
| QL-1060 ||  ||
|-
| QL-1110NWB ||  ||
|-
| TD-2020 ||  ||
|-
| TD-2120N ||  ||
|-
| TD-2130N ||  ||
|-
| TD-4000 ||  ||
|-
| TD-4100N ||  ||
|-
! Printer
! Driver/filter
! Notes
|}

## Network printers
For network printers, use  as printer address.
For some older printers, this might not work. If not, try  instead.

Some printers use the socket protocol. For these printers, use .
For http, use .

## Custom drivers
Brother provides custom drivers on their website, either in source tarball, rpm, or deb form. Packaging Brother printer drivers covers creating PKGBUILDs from the existing RPM packages.

## Manually installing from the RPM packages
Install the  package, and extract both rpm packages using . Extracting both files will create a var and a usr directory - move the contents of both directories into the corresponding root directories.

Run the cups wrapper file in . This should automatically install and configure your brother printer.

For some of the drivers 32 bit libraries may need to be installed from multilib.

## Updating the firmware
## Network printers
Install  and run:

 $ snmpwalk -c public $PRINTER_IP | grep -A 1 3.6.1.4.1.2435.2.4.3.99.3.1.6.1.2

Or alternatively:

 $ snmpwalk -v 2c -c public 192.168.23.11 iso.3.6.1.4.1.2435.2.4.3.99.3.1.6.1.2

At this point, you will have the relevant data to get a valid firmware download link from Brother. The file should look similar to the one below:

Post this file to Brother:

 $ curl -X POST -d @request.xml https://firmverup.brother.co.jp/kne_bh7_update_nt_ssl/ifax2.asmx/fileUpdate -H "Content-Type:text/xml" > response.xml

In  you will find a  tag that contains the firmware download URL. Next, download the firmware, push it to the printer, and let the printer process it. Before that is done, change the Admin password to something known, it will be used as the user to log into the FTP site (VERY bad practice, do not do this).

 $ wget https://web.archive.org/web/20210515183359/http://update-akamai.brother.co.jp/CS/LZ4266_W.djf
 $ ftp $PRINTER_IP|
 ftp> bin
 ftp> hash
 ftp> send LZ4266_W.djf
 ftp> bye

With that, the printer will restart, and the latest firmware will be installed and (hopefully) your printing woes will be solved.

## USB connected printers
Disconnect printer USB cable. On powered on printer enter Maintenance mode by pressing Menu, then Start, LCD should blank out for 1-2 seconds, and during that time, when LCD is blank, press + button four times. Now enter code 77 using numpad or + / - buttons. This should print maintenance information. Now go back to main screen of the mode by pressing Stop button, on 16x2 LCDs it should look like this: ▮▮MAINTENANCE▮▮▮

To get proper firmware file You'll need to craft  file similar to the one for network printers. Use information from maintenance printout to fill mandatory tags, for  use model name (i.e. "DCP-L2500D series"), for  use country code (i.e. "1004") and for  repeat the model name. This is a crafted file for DCP-L2500D printer:

Post this file to Brother:

 $ curl -X POST -d @request.xml https://firmverup.brother.co.jp/kne_bh7_update_nt_ssl/ifax2.asmx/fileUpdate -H "Content-Type:text/xml" > response.xml

In  you will find a  tag that contains the firmware download URL. Next, download the firmware and connect PC with the printer (still in maintenance mode) using USB cable. PC should report in kernel log different USB product ID, i.e. for DCP-L2500D it was  instead of usual , and a generic serial number string like . Now push the firmware to the printer , where  is a number of Your printer. Example command flow for DCP-L2500D:

 $ wget http://update-akamai.brother.co.jp/CS/LZ5100_E.djf
 # cat LZ5100_E.djf > /dev/usb/lp0

On LCD You should see now information about firmware updating. After update printer will automatically reboot to normal state with new firmware version in place.

## IPP-over-USB
You might experience some trouble while using the USB port on certain models.

Brother provides a shell script to create udev rules to prevent the use of IPP-over-USB. This might solve USB printing problems but means that you need to use the legacy LPR driver. See the FAQ article.

## Canon
There are many possible drivers for Canon printers. Many Canon printers are supported by Gutenprint and . Some of Canon's LBP, iR, and MF printers use a driver supporting the UFR II/UFR II LT/LIPSLX protocols,  #UFRII . Others use the #CARPS, or #cnijfilter (), or Canon CAPT drivers.

{| class="wikitable"
! Printer
! Driver/filter
! Notes
|-
| iP4300 || rowspan="2" |  Gutenprint || Or use the TurboPrint driver.
|-
| PIXMA G4000 series|| Misidentifies itself as Canon G3010 Series. Use Canon PIXMA G4000 - CUPS+Gutenprint driver instead.
|-
| LBP810 || rowspan="34" | Canon CAPT ||
|-
| LBP1120 ||
|-
| LBP1210 ||
|-
| LBP2900 ||
|-
| LBP3000 ||
|-
| LBP3010 ||
|-
| LBP3018 ||
|-
| LBP3050 ||
|-
| LBP3100 ||
|-
| LBP3108 ||
|-
| LBP3150 ||
|-
| LBP3200 ||
|-
| LBP3210 ||
|-
| LBP3250 ||
|-
| LBP3300 ||
|-
| LBP3310 ||
|-
| LBP3500 ||
|-
| LBP5000 ||
|-
| LBP5050 series ||
|-
| LBP5100 ||
|-
| LBP5300 ||
|-
| LBP6000 ||
|-
| LBP6018 ||
|-
| LBP6020 ||
|-
| LBP6200 ||
|-
| LBP6300 ||
|-
| LBP6300n ||
|-
| LBP6310dn ||
|-
| LBP7010C ||
|-
| LBP7018C ||
|-
| LBP7200Cdn (network mode) ||
|-
| LBP7200C series ||
|-
| LBP7210Cdn ||
|-
| LBP9100C ||
|-
| LBP7110cw (network mode) ||  v 5.00
|-
| LBP112 || rowspan="11" |  ||
|-
| LBP113w ||
|-
| LBP151dw ||
|-
| LBP6018nl ||
|-
| LBP6030 ||
|-
| LBP6040 ||
|-
| LBP6230 ||
|-
| LBP6240 ||
|-
| LBP7100c ||
|-
| LBP7110c ||
|-
| LBP8100  ||
|-
| MF216n (network over ldp) || rowspan="5" |  ||
|-
| MF635Cx ||
|-
| MF4720w ||
|-
| MF4770n ||
|-
| MF8080Cw || See CUPS#Network for discovery.
|-
| FAX-L400 || rowspan="21" |  ||
|-
| FP-L170 || Should work, unverified.
|-
| ICD300 ||
|-
| imageCLASS D300 ||
|-
| L380 || Should work, unverified.
|-
| L389 || Should work, unverified.
|-
| L390 ||
|-
| L408S ||
|-
| LASERCLASS 500 || Should work, unverified.
|-
| LC180 ||
|-
| LC310 ||
|-
| LC380S ||
|-
| LC398S ||
|-
| MF350 || Should work, unverified.
|-
| MF3110 ||
|-
| MF5630 ||
|-
| MF5650 || Should work, unverified.
|-
| MF5730 ||
|-
| MF5750 ||
|-
| MF5770 ||
|-
| PC-D300 ||
|-
| PIXMA iP110 || rowspan="30" |  ||
|-
| PIXMA E4200 series || Works in driverless mode. Nevertheless,  provides a PPD driver file if desired. See CUPS#Network for discovery.
|-
| PIXMA TR150 series ||
|-
| PIXMA TS200 series ||
|-
| PIXMA MX490 series ||
|-
| PIXMA MX530 series ||
|-
| PIXMA TS700 series ||
|-
| PIXMA MB2300 series ||
|-
| PIXMA MG2500 series ||
|-
| PIXMA MG2900 series ||
|-
| PIXMA MG3000 series ||
|-
| PIXMA TS3100 series ||
|-
| PIXMA TS3500 series ||
|-
| PIXMA MG3600 series ||
|-
| PIXMA TS3700 series ||
|-
| PIXMA TR4500 series ||
|-
| PIXMA TR4700 series ||
|-
| PIXMA MB5450 ||
|-
| PIXMA MG5620 series ||
|-
| PIXMA MG5700 series ||
|-
| PIXMA MG6600 series ||
|-
| PIXMA MG6800 series ||
|-
| PIXMA TR7000 series ||
|-
| PIXMA TR7500 series ||
|-
| PIXMA MG7500 series ||
|-
| PIXMA TS7700 series ||
|-
| PIXMA TR7800 series ||
|-
| PIXMA TS8050 || Without  printing will fail with a filter error or you might get "Rendering Completed" and nothing will print.
|-
| PIXMA MG8200 series ||
|-
| PIXMA TR8350 series ||
|-
| PIXMA TR8500 series ||
|-
| PIXMA MG2400 series ||  ||
|-
| PIXMA MG4200 series ||  || Avoid the web interface when adding the printer as it will not find the PPD file.
|-
| PIXMA TR8600 series ||  ||
|-
| PIXMA TS9020 ||  ||
|-
! Printer
! Driver/filter
! Notes
|}

Some Canon printers will use a similar setup to the iP4500, so consider modifying the  package for other, similar printers.

## UFRII
Many LBP, iR, and MF printers use a protocol that has had several names over the years: UFR II, UFR II LT, LIPSLX. There are multiple packages for these printers in AUR, and at least the imageCLASS MF4570dn is reported to only work with the older v3.70 version.
The i-SENSYS MF633C is confirmed to work with the 6.00 version.

 v 6.10: latest version built from source

 v 6.00: binary build that allows choosing between repackaging rpm or deb build.

 3-1 : binary build that repackages the .deb archive from canon .
pkgver does not reflect the driver version but the 3-1 uses version 6.20

Older versions

 v3.70: uses Canon provided binaries with location/config adjustments to make them work on Arch Linux

 v5.00: uses Canon provided binaries for other printers (e.g. LBP6030).

## CARPS
Some of Canon's printers use Canon's proprietary CARPS (Canon Advanced Raster Printing System) driver.
Rainbow Software have managed to reverse engineer the CARPS data format and have successfully created a CARPS CUPS driver, which is available as .
The project's GitHub page includes a list of working printers.

## USB over IP (BJNP)
Some Canon printers use Canon's proprietary USB over IP BJNP protocol to communicate over the network. There is a CUPS backend for this, which is available as .

## cnijfilter
Some printers using the cnijfilter drivers support the  protocol. To find the printer URI run

 $ cnijnetprn --search auto

and use the  URI in the output.

Other driver versions, as is the case for the current version of , provide the  binary to search for available printers.

The printer can be added to cups using the  url and an appropriate  file, which should be shipped with your driver.

 $ lpadmin -p CustomPrinterNameMB2300 -P /usr/share/cups/model/canonmb2300.ppd -v "cnijbe2://Canon/?port=net&serial=60-12-81-A7-7D-34" -E

The argument  in the cnijbe2 url corresponds to the MAC address of the printer.

## IPP Everywhere
For recent Canon printers, like the G7000 series, it can be hard to find a valid driver. However, it is possible to use a driverless installation using IPP Everywhere.

If you have installed avahi, CUPS should be able to detect your printer automatically.

However, if it fails, you can always enter your printer settings manually. In CUPS web interface select  and enter the IPP URL of the printer. Then at the driver selection screen select{{ic|Generic > {current_make_and_model} - IPP Everywhere ™}}.

For the G7000 series the IPP URL is  or .

## Dell
{| class="wikitable"
! Printer
! Driver/filter
! Notes
|-
| 1250C
| rowspan=2 |
| rowspan=2 | The printer may also work with the Xerox Phaser 6000B driver ().
|-
| C1660NW
|-
| E515
| rowspan=2 | Install Dell's driver.
| rowspan=2 | Both e515dwcupswrapper-3.2.0-1.i386.deb and e515dwlpr-3.2.0-1.i386.deb need to be installed. You could either write a PKGBUILD, use , or use  (using dpkg is not recommended as the files will not be managed by pacman). The driver works on both the x86_64 and i386 platforms, but may require multilib.
|-
| E515dw
|-
| S1130n || rowspan="16" |  || rowspan="16" | Driver conflicts with  (as  appears to be based on the Samsung one, and they create several of the same files)
|-
|1130
|-
|1133
|-
|1135n
|-
|1815
|-
|2145cn
|-
|2335dn
|-
|2355dn
|-
|5330
|-
|B1160
|-
|B1160w
|-
|B1165nfw
|-
|B1260dn
|-
|B1265dfw
|-
|B1265dnf
|-
|B2365dnf
|-

! Printer
! Driver/filter
! Notes
|}

## Epson
## Inkjet
Most models are covered by the official Epson Inkjet Printer Driver for Linux, either  or , which are sets of CUPS drivers for printers using the ESC/P-R or ESC/P-R 2 specifications of the ESC/P protocol, respectively.

Drivers using the original ESC/P protocol are distributed across multiple packages:

{| class="wikitable"
! Printers
! Driver/filter
! Notes
|-
| ME 340, Stylus NX130, Stylus SX130, Stylus TX130, Stylus TX133, Stylus TX135 ||  ||
|-
| PX-7V ||  ||
|-
| R2000 ||  ||
|-
| PX-403A ||  ||
|-
| K300, WorkForce K301 ||  ||
|-
| PX-434A ||  ||
|-
| ME OFFICE 570W, Stylus NX330, Stylus NX430, Stylus SX430W, Stylus SX435W, Stylus SX440W, Stylus SX445W, Stylus TX430W, Stylus TX435W ||  ||
|-
| PX-204, PX-504A ||  ||
|-
| ME OFFICE 940FW, Stylus NX530, Stylus NX635, Stylus SX535WD, Stylus Office BX535WD, Stylus Office BX630FW, Stylus Office BX635FWD, WorkForce 545, WorkForce 645 ||  ||
|-
| Stylus Office BX935FWD, WorkForce 845 ||  ||
|-
| PX-404A ||  ||
|-
| ME OFFICE 535, Stylus NX230, Stylus SX230, Stylus SX235W, Stylus TX230W, Stylus TX235, Stylus TX235W ||  ||
|-
| Stylus Office BX305FW Plus, WorkForce 435 ||  ||
|-
| PX-1600F ||  ||
|-
| WF-7510, WF-7511, WF-7515 ||  ||
|-
| EP-704A ||  ||
|-
| Artisan 635 ||  ||
|-
| EP-804A, EP-804AR, EP-804AW, EP-904A, EP-904F ||  ||
|-
| Artisan 730, Artisan 837, Stylus Photo PX730WD, Stylus Photo PX830FWD, Stylus Photo TX730WD ||  ||
|-
| PX-B700, PX-B750F ||  ||
|-
| WP-4010, WP-4011, WP-4015, WP-4020, WP-4022, WP-4023, WP-4025, WP-4090, WP-4091, WP-4092, WP-4095, WP-4511, WP-4515, WP-4520, WP-4521, WP-4525, WP-4530, WP-4531, WP-4532, WP-4533, WP-4535, WP-4540, WP-4545, WP-4590, WP-4592, WP-4595 ||  ||
|-
| EP-4004 ||  ||
|-
| Artisan 1430, Stylus Photo 1430W, Stylus Photo 1500W ||  ||
|-
| PX-1200, PX-1700F ||  ||
|-
| WF-7010, WF-7011, WF-7012, WF-7015, WF-7520, WF-7521, WF-7525 ||  ||
|-
| PX-1004 ||  ||
|-
| XP-302, XP-303, XP-305, XP-306, XP-402, XP-403, XP-405, XP-406 ||  ||
|-
| XP-30, XP-33, XP-102, XP-103, XP-202, XP-203, XP-205, XP-207 ||  ||
|-
| PX-405A, PX-435A ||  ||
|-
| ME-303, ME-401, XP-300, XP-400, XP-401 ||  ||
|-
| PX-045A ||  ||
|-
| ME-301, XP-100, XP-101, XP-104, XP-200, XP-201, XP-204 ||  ||
|-
| EP-705A ||  ||
|-
| ME-10, ME-101 ||  ||
|-
| L110, L111, L210, L211, L300, L301, L303, L350, L351, L353, L355, L356, L550, L551, L555 ||  ||
|-
| XP-600, XP-601, XP-605, XP-700, XP-701, XP-702, XP-800, XP-801, XP-802 ||  ||
|-
| EP-805A, EP-805AR, EP-805AW, EP-905A, EP-905F ||  ||
|-
| XP-750, XP-850 ||  ||
|-
| EP-775A, EP-775AW ||  ||
|-
| PX-105, PX-505F, PX-535F ||  ||
|-
| WF-2010, WF-2510, WF-2520, WF-2521, WF-2528, WF-2530, WF-2531, WF-2532, WF-2538, WF-2540, WF-2541, WF-2548 ||  ||
|-
| PX-205, PX-605F, PX-675F ||  ||
|-
| WF-3010, WF-3011, WF-3012, WF-3520, WF-3521, WF-3530, WF-3531, WF-3540, WF-3541 ||  ||
|-
| PX-K701, PX-K751F ||  ||
|-
| WP-M4011, WP-M4015, WP-M4023, WP-M4090, WP-M4095, WP-M4521, WP-M4525, WP-M4533, WP-M4590, WP-M4595 ||  ||
|-
| PX-K150 ||  ||
|-
| WF-M1030, WF-M1560, WF-M1561 ||  ||
|-
| M100, M101, M105, M200, M201, M205 ||  ||
|-
| XP-312, XP-313, XP-315, XP-412, XP-413, XP-415 ||  ||
|-
| XP-212, XP-213, XP-215, XP-217 ||  ||
|-
| PX-436A ||  ||
|-
| XP-310, XP-410 ||  ||
|-
| PX-046A ||  ||
|-
| XP-211, XP-214, XP-216 ||  ||
|-
| EP-976A3 ||  ||
|-
| XP-950 ||  ||
|-
| EP-306, EP-806AB, EP-806AR, EP-806AW, EP-906F ||  ||
|-
| EP-706A, EP-776A ||  ||
|-
| XP-610, XP-710, XP-810 ||  ||
|-
| XP-510 ||  ||
|-
| L120 ||  ||
|-
| ET-14000, L1300 ||  ||
|-
| L1800 ||  ||
|-
| L130, L132, L220, L222, L310, L312, L360, L362, L365, L366, L455, L456 ||  ||
|-
| L380, L382 ||  ||
|-
| L1210, L1250, L3200, L3210 ||  ||
|-
| Artisan 725, Artisan 835, Stylus Photo PX720WD, Stylus Photo PX820FWD, Stylus Photo TX720WD, Stylus Photo TX820FWD ||  ||
|-
| EP-302 ||  ||
|-
| EP-702A ||  ||
|-
| EP-703A ||  ||
|-
| EP-774A, EP-803A, EP-803AW, EP-903A, EP-903F ||  ||
|-
| EP-802A, EP-902A ||  ||
|-
| K100, K200, WorkForce K101 ||  ||
|-
| L100, L101, L200, L201 ||  ||
|-
| L800 ||  ||
|-
| L805 ||  ||
|-
| ME 10, ME 32, ME 33, ME 35, ME 320, ME 330, ME 350, Stylus N10, Stylus N11, Stylus NX125, Stylus NX127, Stylus S22, Stylus SX125, Stylus T12, Stylus T13, Stylus T22, Stylus T22E, Stylus T25, Stylus TX120, Stylus TX121, Stylus TX123, Stylus TX125, Stylus TX129 ||  ||
|-
| ME OFFICE 560W, Stylus NX420, Stylus SX420W, Stylus SX425W, Stylus TX420W ||  ||
|-
| PX-20000 ||  ||
|-
| PX-402A ||  ||
|-
| PX-502A ||  ||
|-
| PX-203, PX-503A, PX-603F ||  ||
|-
| PX-5V ||  ||
|-
| PX-602F ||  ||
|-
| PX-673F ||  ||
|-
| PX-F8000, PX-F10000 ||  ||
|-
| PX-H7000, PX-H9000 ||  ||
|-
| PX-K100 ||  ||
|-
| SC-P10000, SC-P20000 ||  ||
|-
| SC-P10000, SC-P20000 ||  ||
|-
| SC-P5000 ||  ||
|-
| SC-P5000 ||  ||
|-
| SC-P5300 ||  ||
|-
| SC-P7500, SC-P9500 ||  ||
|-
| SC-P6500, SC-P6500D, SC-P8500D, SC-P8500DL, SC-P8500DM ||  ||
|-
| SC-P6000, SC-P7000, SC-P8000, SC-P9000 ||  ||
|-
| SC-P6000, SC-P7000, SC-P8000, SC-P9000 ||  ||
|-
| SC-T2100 ||  ||
|-
| SC-T3100M ||  ||
|-
| SC-T3100, SC-T5100 ||  ||
|-
| SC-T3400, SC-T5400 ||  ||
|-
| SC-T3050, SC-T5050, SC-T7050 ||  ||
|-
| SC-T3000, SC-T3070, SC-T3080, SC-T5000, SC-T5070, SC-T5080, SC-T7000, SC-T7070, SC-T7080 ||  ||
|-
| SC-T5100M ||  ||
|-
| SC-T3700D, SC-T5700D, SC-T5700DM, SC-T7700D, SC-T7700DL, SC-T7700DM ||  ||
|-
| SC-T3200, SC-T5200, SC-T7200, SC-T5200D, SC-T7200D ||  ||
|-
| SC-T3200, SC-T3270, SC-T3280, SC-T5200, SC-T5270, SC-T5280, SC-T7200, SC-T7270, SC-T7280, SC-T5200D, SC-T5270D, SC-T5280D, SC-T7200D, SC-T7270D, SC-T7280D ||  ||
|-
| Stylus NX110, Stylus NX115, Stylus SX110, Stylus SX115, Stylus TX110, Stylus TX111, Stylus TX112, Stylus TX113, Stylus TX115, Stylus TX117, Stylus TX119 ||  ||
|-
| ME OFFICE 650FN, Stylus Office BX310FN, Stylus Office TX510FN, Stylus Office TX515FN, WorkForce 310 ||  ||
|-
| Stylus SX610FW, Stylus Office BX610FW, Stylus Office TX610FW, WorkForce 610, WorkForce 615 ||  ||
|-
| Stylus Photo PX660 ||  ||
|-
| Artisan 710, Artisan 810, Stylus Photo PX710W, Stylus Photo PX810FW, Stylus Photo TX710W, Stylus Photo TX810FW ||  ||
|-
| Stylus Photo R3000 ||  ||
|-
| Artisan 50, Stylus Photo P50, Stylus Photo R330, Stylus Photo T50, Stylus Photo T59, Stylus Photo T60 ||  ||
|-
| Stylus Photo PX650, Stylus Photo TX650, Stylus Photo TX659 ||  ||
|-
| Stylus Pro 11880, Stylus Pro 11880C ||  ||
|-
| Stylus Pro 4450 ||  ||
|-
| Stylus Pro 4880, Stylus Pro 4880C ||  ||
|-
| Stylus Pro 4900, Stylus Pro 4910 ||  ||
|-
| Stylus Pro 7700, Stylus Pro 7710, Stylus Pro 9700, Stylus Pro 9710 ||  ||
|-
| Stylus Pro 7890, Stylus Pro 7908, Stylus Pro 9890, Stylus Pro 9908 ||  ||
|-
| Stylus S21, Stylus T21, Stylus T24, Stylus T27 ||  ||
|-
| Stylus NX510, Stylus NX515, Stylus SX510W, Stylus SX515W, Stylus TX550W ||  ||
|-
| ME OFFICE 520, ME OFFICE 620F, Stylus NX220, Stylus SX218, Stylus TX220, Stylus TX228, Stylus Office BX305F, Stylus BX305FW, Stylus TX320F, Stylus TX325F, WorkForce 320, WorkForce 323, WorkForce 325 ||  ||
|-
| Stylus Office BX320FW, Stylus Office TX525FW, WorkForce 520, WorkForce 525 ||  ||
|-
| ME OFFICE 82WD, ME OFFICE 85ND, ME OFFICE 900WD, ME OFFICE 960FWD, Stylus NX625, Stylus SX525WD, Stylus SX620FW, Stylus TX560WD, Stylus Office B42WD, Stylus BX525WD, Stylus BX625FWD, Stylus TX620FWD, WorkForce 60, WorkForce 625, WorkForce 630, WorkForce 633, WorkForce 635, WorkForce T42WD ||  ||
|-
| Stylus Office BX925, WorkForce 840 ||  ||
|-
! Printers
! Driver/filter
! Notes
|}

## Laser
Some printers require a PPD file, which can be obtained from Epson's driver download page. Others are supported through packaged drivers:

{| class="wikitable"
! Printers
! Driver/filter
! Notes
|-
| LP-M8180A, LP-M8180F ||  ||
|-
| LP-S180D ||  ||
|-
| LP-S180DN ||  ||
|-
| LP-S2290, LP-S3290, LP-S3590, LP-S4290 ||  ||
|-
| LP-S6160 ||  ||
|-
| LP-S7160 ||  ||
|-
| LP-S7180, LP-S8180 ||  ||
|-
! Printers
! Driver/filter
! Notes
|}

## TM Series
{| class="wikitable"
! Printers
! Driver/filter
! Notes
|-
| TM-U220 ||  ||
|-
| TM-H6000IV ||  ||
|-
| TM-m30, TM-T88VI, TM-H6000V ||  ||
|-
! Printers
! Driver/filter
! Notes
|}

## Utilities
## Epson Printer Utility
 provides a graphical interface for managing Epson printers. It can be used to check ink levels, view error messages and other printer status information, perform nozzle checks and head cleanings, and manage print settings. The utility integrates with CUPS and is designed to complement the ESC/P-R driver packages.

## escputil
escputil is part of the  package, and performs some utility functions on Epson printers such as nozzle cleaning.

## ReInkPy
This is a Python utility that allows resetting of the Waste Ink Counters (WIC), in case of a message similar to "A printer's ink pad is at the end of its service life".

The ReInkPy repo on Codeberg contains instructions to install and use, but one should replace  with  from  to install the utility in a virtual environment.

Note that physical servicing (either by replacing the Ink Pad tray with a new one or by manually cleaning the pad) might actually be needed. This utility merely resets the internal counters that act as a heuristic as to when to change the pads.

## mtink
This is a printer status monitor which enables to get the remaining ink quantity, to print test patterns, to reset printer and to clean nozzle. It use an intuitive graphical user interface.

## Stylus-toolbox
This is a GUI using escputil and cups drivers. It supports nearly all USB printer of Epson and displays ink quantity, can clean and align print heads and print test patterns.

## Adding missing paper sizes
Some of the PPD files in  are missing paper size definitions for media that is supported by the printers and the filter. It is relatively straightforward to add the missing media types to the PPD files.

To begin, download the PKGBUILD for the  package, either with an AUR helper or from a snapshot tarball. Once in the directory with the PKGBUILD, download and extract the source of the package by running .

Change directory to . Open the file  in a text editor for reference.

Identify the PPD used by your printer in the  directory. For example, a Workforce 7710 printer uses . Let us call it . Convert the relevant PPD to a PPD compiler source file using the  utility from the  package.

 $ ppdi -o your_ppd_filename.drv ppd/your_ppd_filename.ppd

Open the newly-created  in a text editor. Identify the section of the file with a lot of lines starting with . Duplicate one such line to modify. For example:

 CustomMedia "Legal/US Legal" 612.00 1008.00 8.40 8.40 8.40 8.40 ">setpagedevice" ">setpagedevice"

The pair of numbers  represents the width and height of the paper in inches, multiplied by 72. Replace all three instances of these numbers with the dimensions of the paper you want to add. For example to add 11"x17" paper, replace the numbers with .

The string  identifies the paper. On the left side of the slash,  is a magic identifier that the filter uses to identify the paper size. Replace it with the one you want to use. Refer to the  array in  for a list of possible values. The string to the right of the slash can be set to any human-readable value.

If you want to enable borderless printing for a paper size, prefix the magic identifier string you just found with the letter T. So  would become . Additionally, change the four numbers  to .

For example, I was able to add 11x17 paper to the PPD for a Workforce 7710 by adding the following lines:

 CustomMedia "USB/US B(11x17 in)" 792.00 1224.00 8.40 8.40 8.40 8.40 ">setpagedevice" ">setpagedevice"
 CustomMedia "TUSB/US B(11x17 in) (Borderless)" 792.00 1224.00 0.00 0.00 0.00 0.00 ">setpagedevice" ">setpagedevice"

Once you have added your custom size, recompile  into a PPD file with ppdc (also from ):

 $ ppdc your_ppd_filename.drv

This will create a ppd file in the  directory with a file name derived from the  parameter in . You can test this file by uploading it to the CUPS web interface, or install it permanently by overwriting the original PPD file and making the package with .

## HP
Most HP printers will use , see also CUPS/Troubleshooting#HP issues.

Some may use , while for multifunction laser printers  might be required. Some laser printers are also supported by .

Notice that if  tells you that the driver "requires proprietary plugin", you need to install .

{| class="wikitable"
! Printer
! Driver/filter
! Notes
|-
| DeskJet 710C || rowspan="8" |  ||
|-
| DeskJet 712C ||
|-
| DeskJet 720C ||
|-
| DeskJet 722C ||
|-
| DeskJet 820se ||
|-
| DeskJet 820Cxi ||
|-
| DeskJet 1000Cse ||
|-
| DeskJet 1000Cxi ||
|-
| LaserJet MFP M433 || rowspan="7" |  ||
|-
| LaserJet MFP M436 ||
|-
| LaserJet MFP M72625 72630 ||
|-
| Laser 10x Series ||
|-
| Laser MFP 13x Series ||
|-
| Color Laser 15x Series ||
|-
| Color Laser MFP 17x Series ||
|-
| LaserJet 1200 ||  || Use  driver. The postscript driver that  suggests is slow and buggy
|-
! Printer
! Driver/filter
! Notes
|}

## HPLIP
 provides drivers for HP DeskJet, OfficeJet, Photosmart, Business Inkjet, and some LaserJet printers, and also provides an easy to use setup tool. See https://developers.hp.com/hp-linux-imaging-and-printing/supported_devices/index for the list of supported printers.

hplip requires  to run the GUI qt frontend. hp-setup requires CUPS to be installed and  to be started to save the printer. hp-setup also requires the lsusb software, which is provided by the  package.

To run the setup tool with the GUI qt frontend:

 $ hp-setup -u

To run the setup tool with the command line frontend:

 $ hp-setup -i

To set up directly the configuration of a network connected HP printer:

 $ hp-setup -i ip_address

To run systray spool manager:

 $ hp-systray

To generate a URI for a given ip address:

 # hp-makeuri ''''

PPD files are in .

If your printer is listed as requiring a binary plugin, install the  package from AUR.
If the binary plugin  is a requirement you will need to start the  before the PPD is recognized by . If that does not work, reboot and log in with the printer off. Then switch it on and run a test print.

## HPULD
See Debian:CUPSPrintQueues#hpuld for more information.

The package  collects the sparse "HP + ULD" packages into one single package.

## foo2zjs
foo2zjs supports some HP LaserJet printers. As of June 2018 the hplip package interferes with , as described at this forum post and .

## Konica Minolta
{| class="wikitable"
! Printer
! Driver/filter
! Notes
|-
| Minolta Magicolor 1600W || rowspan=7 | foomatic ||
|-
| Minolta Magicolor 1680MF ||
|-
| Minolta Magicolor 1690MF ||
|-
| Minolta Magicolor 2480MF ||
|-
| Minolta Magicolor 2490MF ||
|-
| Minolta Magicolor 2530DL ||
|-
| Minolta Magicolor 4690MF ||
|-
! Printer
! Driver/filter
! Notes
|}

## foo2zjs
#foo2zjs, mentioned above for supporting some HP printers, also support some Minolta printers.

## Lexmark
Note that most Lexmark printers are now supported by CUPS without needing further installation. See also SANE/Scanner-specific problems#Lexmark for Lexmark scanners issues.

## Utilities
Lexmark provides a utility called lexijtools with the drivers.

## Custom drivers
Lexmark does provide Linux drivers for all their hardware.
The following packages are required:

*
*
*
*
*
*
*
*
*
*  (for the automated installer)
* Java (for the automated installer, and some of the Lexmark tools)

The drivers will need to be downloaded from Lexmark's website. Preferably, create a package (see Creating packages) and install it.  Here is a basic PKGBUILD that still needs work but will give an idea of what is required.

{{hc|PKGBUILD|
# Contributor: Todd Partridge (Gen2ly) toddrpartridge (at) yahoo

pkgname=cups-lexmark-Z2300-2600
pkgver=1
pkgrel=1
pkgdesc="Lexmark Z2300 and 2600 Series printer driver for cups"
arch=('i686')
url="http://www.lexmark.com/"
license=('custom')
depends=('cups' 'glibc' 'ncurses' 'libusb' 'libxext' 'libxtst' 'libxi' 'libstdc++5' 'krb5' 'lua' 'java-runtime')
conflicts=('z600' 'cjlz35le-cups' 'cups-lexmark-700')
source=(lexmark-inkjet-08-driver-1.0-1.i386.tar.gz.sh)
md5sums=(3c37eb87e3dad4853bf29344f9695134)

package() {
  # Extract installer
  sh lexmark-inkjet-08-driver-1.0-1.i386.tar.gz.sh --target Installer-Files
  cd Installer-Files
  mkdir Driver
  tar xvvf instarchive_all --lzma -C Driver/
  cd Driver
  tar xv lexmark-inkjet-08-driver-1.0-1.i386.tar.gz -C $pkgdir
}
}}

Keep in mind you can use the automated installer but doing so will leave the resulting changes untracked. The PPD will be installed into  or similar, depending on the printer model.

## Oki
{| class="wikitable"
! Printer
! Driver/filter
! Notes
|-
| C110|| foomatic ||
|-
| MC561|| foomatic-db-nonfree ||
|-
! Printer
! Driver/filter
! Notes
|}

## Ricoh
Install  if your device is black and white, or  if it is color. Note that Ricoh copiers are sometimes branded as Savin, Gestetner, Lanier, Rex-Rotary, Nashuatec, and/or IKON. So, if you have a device bearing one of these brands, it may be supported by these drivers as well.

* List of supported black and white models
* List of supported color models

SG or GX series printers requiring RPCS drivers may be suppported by , which provides PPDs and needed filter programs found on the Japanese Ricoh website.

{| class="wikitable"
! Printer
! Driver/filter
! Notes
|-
| IPSiO GX e3300 || rowspan="19" |  || rowspan="19" | As the Japanese products seem to be called IPSiO instead of Aficio, products not listed here could still work with specific printer models.
|-
| IPSiO GX e5500
|-
| IPSiO SG 2010L
|-
| IPSiO SG 2100
|-
| IPSiO SG 3100
|-
| IPSiO SG 3100SF
|-
| IPSiO SG 7100
|-
| SG 2200
|-
| SG 2300
|-
| SG 3100KE
|-
| SG 3120SF
|-
| SG 3120B SF
|-
| SG 3200
|-
| SG 3300
|-
| SG 5100
|-
| SG 5100FT
|-
| SG 5200
|-
| SG 5200FT
|-
| SG 7200
|-
| 213W || Generic PCL Laser || Obtain a WPS code by holding down the Wi-Fi button for 2 seconds, then hitting the stop/start button.
|-
! Printer
! Driver/filter
! Notes
|}

## Samsung
Since 2016, or 2017, Samsung is no longer in the printers/scanners business. As of 2019, HP partially support some of Samsung printers/scanners. Before 2016, Samsung was a major player. Which is why there are still many Samsung machines around. In addition, Linux, and cups, keep evolving. The bottom line of all this is that supporting Samsung products is at a flux.

A major site for information about Samsung printers/scanners is Samsung Unified Linux Driver Repository. Despite its name, it is not affiliated by Samsung (HP). Neither it is devoted only to . Yet the actual drivers suggested are the closed source from Samsung (HP). , on the other hand, also encompass Windows and Mac. It might be the first stop to get a driver for a Samsung printer and scanner as it, or was, claim to support practically every one of these. Note that  includes software that can stand on its own, not tied to cups. If you can not get the printer to work with cups, you might try this route.

That said, there are more options. An overview is at alternatives.

* For Samsung Printer Language, there is . For a list of models that are supported, see its home page. Other SPL Samsung printers, even though not in that list, might work with .
* QPDL (Quick Page Description Language) printers, some of which are supported by , are also supported by by , provided by the #foo2zjs package. A list of known to work models is here.
 and  are free software.

You should also note that many Samsung printers support PostScript. Chances are that it will work with CUPS  generic postscript printer, especially if it is only  black & white and only printer, without a scanner added to it. Generic driver may be missing functionality or limited, for example in their support for duplex, color control, and resolution settings, and print quality may be lower.

## Xerox or FujiXerox
{| class="wikitable"
! Printer
! Driver/filter
! Notes
|-
| DocuPrint 203A ||  || Using the DocuPrint P8e(hpijs) driver, or the Brother driver on FujiXerox's website (see #Brother for more information on how to install custom Brother drivers).
|-
| Phaser 3020 ||  || Also supports Phaser 3052, 3117, 3140, 3155, 3160, 3200MFP, 3250, 3260, 3300MFP, 3320, 3435, 3600, 6110MFP, WorkCentre 3025, 3210, 3215, 3220, 3225, 3315, 3325, 3550, 4118, PE120, PE220, FaxCentre 2218.
|-
| Phaser 3100MFP || Install Xerox's driver || See #Phaser 3100MFP for more instructions.
|-
| Phaser 6115MFP || foomatic ||
|-
| Phaser 6121MFP || foomatic ||
|-
| Xerox Workcentre 3119 ||  || Since Samsung SCX-4200 is the rebranded Xerox 3119, splix package works for both
|-
| Phaser 6510 ||  || Double-sided duplex unit requires a workaround in CUPS printer configuration
|-
| WorkCentre 6015 ||  || PPD for Workcentre 6015B/6015N/6015NI in english and french
|-
! Printer
! Driver/filter
! Notes
|}

## Custom drivers
## Phaser 3100MFP
Once you have downloaded the drivers, execute the driver installer and accept the licence:

 # cd printer
 # ./XeroxPhaser3100.install

Note that the driver is 32 bit, so some 32 bit libraries will be required on an x86_64 system: , , , , , , ,

For the scanner, create an  directory if it does not already exist, because it is needed by the installer:

 # mkdir -p /etc/sane.d

Now install the driver:

 # cd scanner/
 # ./XeroxPhaser3100sc.install

Again, on an x86_64 install, 32 bit libraries will be needed.

## Phaser 6125N
FujiXerox does not support Linux on this model. A slightly adapted custom driver has been found to work out of the box.

To install the tarball, run:

 # tar -C / --keep-newer-files -xvzf cups-xerox-phaser-6125n-1.0.0.tar.gz

## Phaser 6510
This Xerox printer should work with IPP Everywhere.

The PPD file is still available in the AUR if needed. Double-sided duplex printing in the PPD file must be enabled with a special flag  passed to .
