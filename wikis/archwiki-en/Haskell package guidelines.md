# Haskell package guidelines

This document aims to cover standards and guidelines for producing good Haskell packages on Arch.

Until this document is written, contact User:Felixonmars.

## Package naming
For Haskell libraries, use  usually the same name as on hackage.

## Architecture
See PKGBUILD#arch.

Every Haskell library or program is architecture-dependent.

## Source
The preferred source of a Haskell program or library is from hackage. PKGBUILD#source  array should use the following URL template:

 https://hackage.haskell.org/packages/archive/$_hkgname/$pkgver/$_hkgname-$pkgver.tar.gz

Note that a custom  variable is used instead of  since Haskell packages are generally prefixed with haskell-. This variable can generically be defined as follows:

 _hkgname=stm-delay

## Creating packages
 is provided to automate  generation and maintenance.

To generate a series of s for a Hackage package (and its unpackaged dependencies):

 $ arch-hs -o /path/to/workdir library_name

## Updating packages
When a Haskell library changes its build flags or is updated, all dependent packages and their transitive dependents, including makedepends and checkdepends, need to be rebuilt. See the subsections below for determining the correct rebuild order.

Moreover, in the Haskell ecosystem, the latest releases of libraries frequently do not work together. It is therefore advisable to upgrade packages incrementally, in small steps, and read upstream changelogs to identify potential upstream issues. This holds in particular for packages with a non-negligible number of packages in their reverse dependency chain. Sometimes, an incompatibility may only be discovered during the rebuilds and may turn out to be non-trivial to fix; in such cases, it may be best to revert changes and document the incompatibility in the relevant bumpbuddy ticket.

## Identifying required changes
To compare dependencies and other packaging metadata for updating an existing package:

 $ arch-hs-diff library_name old_version new_version

To compare Arch package versions and their corresponding Hackage package versions:

 $ arch-hs-sync check

Note that  uses  to maintain Hackage databases, so please update your cabal-install database regularly to keep them fresh:

 $ cabal update

## Package rebuilds
The [https://github.com/felixonmars/archlinux-futils/blob/master/genrebuild genrebuild tool can be used to find out what needs rebuilding and how.

Example usage:

 $ ./genrebuild -H haskell-basement

## PKGBUILD library example
Packaging a Haskell library is different from packaging a Haskell program, the libraries packaged in Arch Linux are meant to be used by packaged Haskell programs.

{{hc|PKGBUILD|
# Maintainer: Your Name
_hkgname=stm-delay
pkgname=haskell-stm-delay
pkgver=
pkgrel=1
license=()
arch=('x86_64')
url="https://hackage.haskell.org/package/$_hkgname"
depends=(ghc-libs)
makedepends=(ghc)
source=("https://hackage.haskell.org/packages/archive/$_hkgname/$pkgver/$_hkgname-$pkgver.tar.gz")
sha256sums=()

build() {
  cd "$_hkgname-$pkgver"

  runhaskell Setup configure -O --enable-shared --enable-debug-info --enable-executable-dynamic --disable-library-vanilla \
    --prefix=/usr --docdir="/usr/share/doc/$pkgname" --datasubdir=$pkgname --enable-tests \
    --dynlibdir=/usr/lib --libsubdir=\$compiler/site-local/\$pkgid \
    --ghc-option=-optl-Wl\,-z\,relro\,-z\,now \
    --ghc-option='-pie'

  runhaskell Setup build $MAKEFLAGS
  runhaskell Setup register --gen-script
  runhaskell Setup unregister --gen-script
  sed -i -r -e "s|ghc-pkg.*update* |&'--force' |" register.sh
  sed -i -r -e "s|ghc-pkg.*unregister* |&'--force' |" unregister.sh
}

check() {
  cd "$_hkgname-$pkgver"
  runhaskell Setup test
}

package() {
  cd "$_hkgname-$pkgver"

  install -D -m744 register.sh "$pkgdir/usr/share/haskell/register/$pkgname.sh"
  install -D -m744 unregister.sh "$pkgdir/usr/share/haskell/unregister/$pkgname.sh"
  runhaskell Setup copy --destdir="$pkgdir"
  install -D -m644 "LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  rm -f "${pkgdir}/usr/share/doc/${pkgname}/LICENSE"
}
}}
