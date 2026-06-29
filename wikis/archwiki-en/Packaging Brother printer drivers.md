# Packaging Brother printer drivers

Brother supplies Linux drivers for its printers, but they are provided as .rpm and/or .deb packages only. This article explains what adjustments to the contents of the DEB and RPM packages supplied by Brother will need to be made to create a PKGBUILD for the printer driver. Additional example PKGBUILDs for Brother printers can be found by searching in the AUR.

CUPS handles printers using a .ppd file and a filter binary. Once those two files are installed, the printer can be added in CUPS.

## Creating a PKGBUILD from a .deb
Brother is offering a "Driver Install Tool" as well as two .deb packages.

One is the LPR driver and the other one a CUPS wrapper (running on top of LPR driver). Both can be found on Brother's "Support & Downloads" page (e.g. for HL-L9200CDW).

It is possible to create a PKGBUILD that will automatically download and install the .deb packages directly from the URL provided by Brother. Therefore you will need to obtain the direct download links for both .deb packages from brothers website (e.g. for HL-L9200CDW you have the LPR driver and the CUPS wrapper).

Once you have obtained the download URLs for both .deb packages, use existing PKGBUILD files from  and  as templates. You will need to adjust the package name. Change  to the URL of Brother's support page for your specific printer model,  needs to be adjusted to the URL of the .deb package. The following PKGBUILD example has been based on  but has been adjusted for HL-L9200CDW LPR printer driver:

{{bc|1=
# Maintainer: John Doe
pkgname=brother-hll9200cdw-lpr-bin
pkgver=1.1.2
pkgrel=1
pkgdesc="LPR driver for Brother HL-L9200CDW(T) printer"
arch=("i686" "x86_64")
url="https://support.brother.com/g/b/producttop.aspx?c=ca&lang=en&prod=hll9200cdw_us_as_cn"
license=("EULA")
source=("http://www.brother.com/pub/bsc/linux/packages/hll9200cdwlpr-1.1.2-1.i386.deb")
md5sums=("30124df7d49362906a2a118eff3c710e")
package() {
        tar -xf data.tar.gz -C "${pkgdir}"
}
}}

Do not forget to update the md5sum. The pkgver version should be the same version as Brother's printer drivers (please note versions might differ for LPR and CUPS wrapper). Create the PKGBUILD file for the CUPS wrapper, too:

{{bc|1=
# Maintainer: John Doe
pkgname=brother-hll9200cdw-cups-bin
pkgver=1.1.3
pkgrel=1
pkgdesc="CUPS wrapper for Brother HL-L9200CDW(T) printer"
arch=("i686" "x86_64")
url="https://support.brother.com/g/b/producttop.aspx?c=ca&lang=en&prod=hll9200cdw_us_as_cn"
license=("EULA")
source=("http://www.brother.com/pub/bsc/linux/packages/hll9200cdwcupswrapper-1.1.3-1.i386.deb")
md5sums=("0a802088aac7236a3c309b2b46b37f11")
package() {
       tar -xf data.tar.gz -C "${pkgdir}"
}
}}

Finally, use makepkg to test/install your newly created PKGBUILD file(s). If everything works, do not forget to publish your new driver to AUR. See AUR submission guidelines for the details.

## Creating a PKGBUILD from a .rpm
Unfortunately, Brother's drivers have some issues:

* The CUPS driver is built on top of the lpr driver.
* The CUPS driver package contains a single installation shell script with an embedded ppd and filter. It is executed by rpm during installation. It extracts the ppd and filter, and performs some installation procedures in a Red Hat-specific way.
* The CUPS driver package uses paths that are not compliant with the Arch package guidelines.

These issues can be worked around.

* The lpr driver does not need to be installed, so the PKGBUILD can just extract the files in the lpr driver's RPM package.
* The CUPS driver's RPM should contain a single shell script. For instance, for the  package, the PKGBUILD changes three things:
*# The paths are changed.
*# All commands are disabled except "" or whatever there is that emits *.ppd or filter to separate file. It was done by wrapping irrelevant instructions by .
*# The target file names for the ppd and filter are changed so they are installed into the same directory as the PKGBUILD. Note that paths to the embedded filter where also changed.
* To fix the paths to conform to the Arch package guidelines,  or similar can be used on all text files unpacked from both the lpr and CUPS drivers. Look at the patch in the  package to check which files are affected.

Effectively after the changes described above the script will just output a ppd and a filter to some known location. The PKGBUILD will then copy them to the proper directories in :

 install -m 644 -D ppd "${pkgdir}/usr/share/cups/model/HL2030.ppd"
 install -m 755 -D filter  "${pkgdir}/usr/lib/cups/filter/brlpdwrapperHL2030"

The lpr driver files will also need to be copied into !

## Other changes
Edit the installation script:

 -#PSTOPSFILTER=`which pstops`
 +PSTOPSFILTER='/usr/lib/cups/filter/pstops'

As pstops is not installed in a standard location, the path will need to be hard-coded.

This may also need to be added.

 +psconvert2
 +pstops=/usr/lib/cups/filter/pstops

## x86_64
Because some of the supplied binaries are 32 bit only, on an x86_64 system some additional multilib packages may need to be installed. Note, however, that few 32 bit packages, such as a 32 bit version of glibc (), are in core.
