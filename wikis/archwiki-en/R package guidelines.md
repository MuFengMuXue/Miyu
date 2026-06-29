# R package guidelines

This document covers standards and guidelines on writing PKGBUILDs for R packages. Most information can be obtained by looking at the package's  file. You can get most of this from inside R by running . You could also visit CRAN, Bioconductor link1, and Bioconductor link2 for all the R packages' information.

## Package naming
Packages should be named , where pkgname is taken from the  field from the  file.
The package name should be lowercase.

## Package Version
Take it from the  field. R allows packages to have colons and hyphens in their version, this is disallowed in PKGBUILDs. Convert these to a period or underscore.

## Arch
See PKGBUILD#arch. If the package's CRAN webpage has  it is likely architecture-specific. Otherwise, it is likely not.

## Dependencies
R packages listed in , , or the  fields in a package's  file should be listed under depends.

R packages listed in  should be listed as optdepends.

Some packages require external tools, these are listed under .

 is needed as depends for some packages but is not always listed in the  file.

## Source
All R packages available on CRAN are available at the website  where  is the name of the package on CRAN and  the cran version.

R packages avalable on Bioconductor are available at the website  or  where  is the name of the package on Bioconductor and  the version.

## Build and Package
R has built-in support for building packages. Here are three templates of s for three repositories: MRAN, CRAN and Bioconductor. MRAN is a snapshot mirror of CRAN, using this template will allow the package to build even when out-of-date.

## MRAN
{{bc|
_cranname=
_cranver=
_updatedate=YYYY-MM-DD
pkgname=r-${_cranname,,}
pkgver=${_cranver//pkgrel=1
pkgdesc=""
arch=()
url="https://cran.r-project.org/package=${_cranname}"
license=()
depends=(r)
makedepends=()
optdepends=()
source=("https://cran.microsoft.com/snapshot/${_updatedate}/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
}}

## CRAN
{{bc|
_cranname=
_cranver=
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-/.}
pkgrel=1
pkgdesc=""
arch=()
url="https://cran.r-project.org/package=${_cranname}"
license=()
depends=(r)
makedepends=()
optdepends=()
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
}}

## Bioconductor
{{bc|
_bcname=
_bcver=
pkgname=r-${_bcname,,}
pkgver=${_bcver//:-/.}
pkgrel=1
pkgdesc=""
arch=()
url="https://bioconductor.org/packages/${_bcname}"
license=()
depends=(r)
makedepends=()
optdepends=()
source=("https://bioconductor.org/packages/release/bioc/src/contrib/${_bcname}_${_bcver}.tar.gz")
# or
# source=("https://bioconductor.org/packages/release/data/annotation/src/contrib/${_bcname}_${_bcver}.tar.gz")
sha256sums=('')

build() {
  R CMD INSTALL ${_bcname}_${_bcver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_bcname}" "${pkgdir}/usr/lib/R/library"
}
}}

## Tips and tricks
## Bioconductor repository
To access the bioconductor packages easily, you can add the bioarchlinux repository.
