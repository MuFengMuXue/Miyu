# CLR package guidelines

This document defines the standard for packaging Common Language Runtime (.NET) projects under Arch Linux. Currently only Mono is capable of providing a usable, efficient CLR runtime for multiple systems and this standard will reflect its use. Be aware that a lot of CLR programs were developed with Microsoft .NET in mind and, as such, may or may not run under Mono because of .NET-exclusive factors such as P/Invoke calls and Microsoft digital rights management (DRM) APIs and are thus will not yield a usable package for Arch Linux. However, if combined with Wine as of version 1.5.6 (?), your package may have a chance to run under it. Please see the Wine PKGBUILD Guidelines for more information if such is the case.

## Packaging gotchas
* Always add  to
* Always set  to . Mono does not yet support compiling (running?) 64-bit assemblies.
* Always add  to
* If the package is a library (DLL), consider installing it to Mono's global assembly cache (GAC) if it is to be used as a dependency.
* If the assembly is precompiled and comes with a program debug database file (Foo.dll.pdb), consider converting it as such:
* If the package is meant to be executed (EXE), be sure to install to  a shell script to run it, similar to this one:

 #!/bin/sh
 exec mono foo.exe "$@"

## Signed assemblies
If the package is to be installed into the GAC, be sure it has a signed key file. If not, you can generate one like this: . Following that, the easiest way to embed the key file into the assembly is to disassemble it like this: . Afterwards, reassemble it like so:

## Sample PKGBUILDs
The following examples will try to cover some of the most common conventions and build systems.

## xbuild
## Unsigned DLL
{{bc|
# Maintainer: yourname
pkgname=foo
pkgver=1.0
pkgrel=1
pkgdesc="Fantabulous library for .Net"
arch=('any')
url="http://www.foo.bar"
license=('GPL')
depends=('mono')
options=('!strip')
source=("http://www.foo.bar/foobar.tar.gz")
md5sums=('4736ac4f34fd9a41fa0197eac23bbc24')

build() {
  cd foobar

  xbuild Foo.sln

  # if the package is unsigned, do the following:
  cd /bin/x86/Debug
  monodis Foo.dll --output=Foo.il
  sn -k 1024 Foo.snk
  ilasm /dll /key:Foo.snk Foo.il
}

package() {
  cd foobar/bin/x86/Debug

  install -Dm644 Foo.dll "$pkgdir/usr/lib/foobar/Foo.dll"
  install -Dm644 Foo.dll.mdb "$pkgdir/usr/lib/foobar/Foo.dll.mdb"

  # Register assembly into Mono's GAC
  gacutil -i Foo.dll -root "$pkgdir/usr/lib"
}
}}
