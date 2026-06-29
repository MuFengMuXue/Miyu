# MinGW package guidelines

This page explains how to write PKGBUILDs for software running on Windows.

In order to build software for Windows on Linux one needs:

* Windows header files and import libraries for the WinAPI and the C standard library. There are two options to get those:
** mingw-w64: provides 32 and 64-bit toolchains with secure crt, Vista+ API, DDK (ReactOS), and DirectX (WINE) support. For a full list of supported features and differences with the old MinGW.org, see here. Available from the official repositories by installing  and . AUR packages providing further libraries rely on those packages.
** MinGW: provides 32-bit toolchains with limited DirectX support. It also suffers from long-standing breakage in the implementation of thread-local storage and the floating point library support. It has been removed from the official repositories and the AUR.
* A compiler and its runtime library.
** For C/C++ one can use GCC and Clang. To use GCC one needs to install  as the regular  package cannot be used. To use Clang one can simply use  specifying an `*-w64-mingw32` platform triple as target. Since the regular  package does not contain the compiler runtime libraries for Windows targets one needs to compile them separately or use the runtime provided by . AUR packages providing further libraries rely on .
** For Rust one can use . The regular  package is not built to be able to cross-compile for Windows. If Rust was installed using the  package, you should instead add the Windows target: .
** For Go one can just use the regular  package.
* A C/C++ standard library. One can use libstdc++ provided by  or libc++ from the LLVM project. AUR packages providing further libraries rely on libstdc++.
* A linker and additional tooling. One can use GNU binutils provided by  or LLVM/lld provided by  and . There is also  providing a few additional Windows-specific tools.

For ix86/x86_64 the typical choice is to use mingw-w64- with GCC/libstdc++ and binutils. This is therefore what AUR packages following the package naming  use. The rest of this Wiki page focuses on those packages.

There are also AUR packages named  that use LLVM/Clang/libc++ and support aarch64 besides just i686 and x86_64. Those packages rely on builds from https://github.com/mstorsjo/llvm-mingw and do not utilize LLVM/Clang provided by Arch Linux. Only a few core packages exist.

There are also packages named  provided by https://github.com/Martchus/PKGBUILDs. Those packages use ,  and  as provided by Arch Linux and only provide mingw-w64, the LLVM compiler runtime and libc++ on top of that. Those packages so far only exist for the aarch64 target. They are mainly generated from  AUR packages via a conversion script to be able to provide more than just the core toolchain without much extra effort. Over 100  packages have been converted into  packages so far. They have not been uploaded to the AUR yet as they are generated anyway but the generator and a binary repository can be found on the mentioned GitHub repository.

## Package naming
A package for mingw-w64 should be named . If a static variant of the package is being built, suffix the package name with  (see below for the cases where this is necessary).

## Packaging
Packaging for cross platform packages can be fairly tricky as there are many different build systems and low-level quirks. Take a note of the following things though:

* always add  to , unless it depends on another package which implicitly depends on it
* always add  to , unless using  or
* always add ,  and  to
* always use the original  and append  to the end of
* always use and follow the original  of the official package
* always build both 32-bit and 64-bit versions of libraries
* always put all stuff under the  and  prefix
* always use  as the architecture (unless the package contains executables which must run on the build system)
* always build both shared and static libraries
** autotools-based projects often support building both in one go, when using  shared and static libraries are both enabled
** if the build system or project does not support this, build both separately
** if the shared and static build conflict (e.g. because headers or CMake configuration files differ) consider installing static libraries into  and
** for bigger projects, consider creating a separate  package
* consider removing unneeded documentation ({{ic|rm -r $pkgdir/usr/i686-w64-mingw32/share/{doc,info,man}}}, {{ic|rm -r $pkgdir/usr/x86_64-w64-mingw32/share/{doc,info,man}}})
* consider using  for building with configure scripts
* consider using  for building with CMake
* consider using  for building with Meson
* consider using  for building with raw Makefiles
* consider using  for building with QMake
* consider explicitly stripping symbols with {{ic|${_arch}-strip}} in 's for-loop as demonstrated in the below PKGBUILD examples.
** consider using the find command to iterate over  since not all DLLs, static libraries, or executables may reside in their appropriate locations.
*** if the binary is a DLL, use {{ic|${_arch}-strip --strip-unneeded *.dll}}
*** if the binary is a static lib, use {{ic|${_arch}-strip -g *.a}}
* if a package is modular (requires certain build dependencies, but said dependencies are optional to the end user) add these to  and . Be sure to subtract them from  if updating an existing package. Example of this in use:
* if a package installs a {{ic|$pkgdir/usr/${_arch}/bin/*-config}} script, symlink it to {{ic|$pkgdir/usr/bin/${_arch}-*-config}}
* if a package uses autoconf, explicitly set  for  to workaround autoconf bug #108405 or use

As mentioned above, the files should all be installed into  and . Specifically, all DLLs should be put into  as they are dynamic libraries needed at runtime. Their corresponding  files should go into . Please delete any unnecessary documentation and perhaps other files from . Cross-compilations packages are not meant for the user but only for the compiler and binary distribution, and as such you should try to make them as small as possible.

Always try to match the  in your mingw-w64 packages to the  of the corresponding regular packages in the official Arch Linux repos (not the testing repos). This ensures that the cross-compiled software works exactly the same way on Windows without any unexpected bugs. If packages in Arch are out-of-date, there usually is a good reason and you should still follow the Arch version instead of using the most recent upstream release. If the corresponding native package is in the AUR, you need not follow this version policy, as many AUR packages are often orphaned or left unmaintained.

## Examples
The following examples will try to cover some of the most common conventions and build systems.

## Autotools
{{bc|
pkgname=mingw-w64-foo
pkgver=1.0
pkgrel=1
pkgdesc="Foo bar (mingw-w64)"
arch=('any')
url="http://www.foo.bar"
license=('GPL')
makedepends=('mingw-w64-configure')
depends=('mingw-w64-crt')
options=('!strip' '!buildflags' 'staticlibs')
source=("http://www.foo.bar/foobar.tar.gz")
sha256sums=('8f32d4617390d1c2d16f26a27ab60d97807b35440d45891fa340fc2648b04406')

_architectures="i686-w64-mingw32 x86_64-w64-mingw32"

build() {
  cd foo-$pkgver
  for _arch in ${_architectures}; do
    mkdir -p build-${_arch} && pushd build-${_arch}
    ${_arch}-configure ..
    make
    popd
  done
}

package() {
  cd "foo-$pkgver"
  for _arch in ${_architectures}; do
    make DESTDIR="${pkgdir}" install -C build-${_arch}
    ${_arch}-strip --strip-unneeded "$pkgdir"/usr/${_arch}/bin/*.dll
    ${_arch}-strip -g "$pkgdir"/usr/${_arch}/lib/*.a
  done
}
}}

## CMake
{{bc|
pkgname=mingw-w64-foo
pkgver=1.0
pkgrel=1
pkgdesc="Foo bar (mingw-w64)"
arch=('any')
url="http://www.foo.bar"
license=('GPL')
makedepends=('mingw-w64-cmake')
depends=('mingw-w64-crt')
options=('!strip' '!buildflags' 'staticlibs')
source=("http://www.foo.bar/foobar.tar.gz")
sha256sums=('8f32d4617390d1c2d16f26a27ab60d97807b35440d45891fa340fc2648b04406')

_architectures="i686-w64-mingw32 x86_64-w64-mingw32"

build() {
  cd foo-$pkgver
  for _arch in ${_architectures}; do
    ${_arch}-cmake -B build-${_arch} .
    cmake --build build-${_arch}
  done
}

package() {
  cd "foo-$pkgver"
  for _arch in ${_architectures}; do
    DESTDIR="${pkgdir}" cmake --install build-${_arch}
    ${_arch}-strip --strip-unneeded "$pkgdir"/usr/${_arch}/bin/*.dll
    ${_arch}-strip -g "$pkgdir"/usr/${_arch}/lib/*.a
  done
}
}}
