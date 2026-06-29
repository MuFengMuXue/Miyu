# Cross-compiling tools package guidelines

This page describes how to create packages for cross-compiler toolchains.  Another method to cross-compile makes use of distcc on mixed architectures. See Distcc#Cross compiling with distcc.

## Important note
This page describes the new way of doing things, inspired by the following packages:

* and other packages from  series
* and other packages from  series
*Other packages from  series

## Version compatibility
The following strategies allows you to select compatible versions of gcc, binutils, kernel and C library:

* General rules:
** there is a correlation between gcc and binutils releases, use simultaneously released versions;
** it is better to use latest kernel headers to compile libc but use  switch (specific to glibc, other C libraries may use different conventions) to enforce work on older kernels;
* Official repositories: you may have to apply additional fixes and hacks, but versions used by Arch Linux (or its architecture-specific forks) most probably can be made to work together;
* Software documentation: all GNU software have  and  files, documenting things like minimal required versions of dependencies;
* Other distributions: they too do cross-compilation
* https://trac.clfs.org covers steps, necessary for building cross-compiler and mentions somewhat up-to-date versions of dependencies.

## Building a cross compiler
The general approach to building a cross compiler is:

# binutils: Build a cross-binutils, which links and processes for the target architecture
# headers: Install a set of C library and kernel headers for the target architecture
## use  as reference and pass  to make
## create libc headers package (process for Glibc is described here)
# gcc-stage-1: Build a basic (stage 1) gcc cross-compiler. This will be used to compile the C library. It will be unable to build almost anything else (because it cannot link against the C library it does not have).
# libc: Build the cross-compiled C library (using the stage 1 cross compiler).
# gcc-stage-2: Build a full (stage 2) C cross-compiler

The source of the headers and libc will vary across platforms.

## Package naming
The package name shall not be prefixed with the word  (it was previously proposed, but was not adopted in official packages, probably due to additional length of names), and shall consist of the package name, prefixed by GNU triplet without vendor field or with "unknown" in vendor field; example: . If shorter naming convention exists (e.g. ), it may be used, but this is not recommended.

## File placement
Latest versions of gcc and binutils use non-conflicting paths for sysroot and libraries. Executables shall be placed into , to prevent conflicts here, prefix all of them with architecture name.

Typically,  would have at least following parameters:

{{bc|1=
_target=your_target
_sysroot=/usr/lib/${_target}
...
./configure \
    --prefix=${_sysroot} \
    --sysroot=${_sysroot} \
    --bindir=/usr/bin
}}

where  can be, e.g., "i686-pc-mingw32".

## Example
This is PKGBUILD for binutils for MinGW. Things worth noticing are:

* specifying root directory of the cross-environment
* usage of {{ic|${_pkgname} }}, {{ic|${_target} }} and {{ic|${_sysroot} }} variables to make the code more readable
* removal of the duplicated/conflicting files

{{bc|
# Maintainer: Allan McRae

# cross toolchain build order: binutils, headers, gcc (pass 1), w32api, mingwrt, gcc (pass 2)

_target=i686-pc-mingw32
_sysroot=/usr/lib/${_target}

pkgname=${_target}-binutils
_pkgname=binutils
pkgver=2.19.1
pkgrel=1
pkgdesc="MinGW Windows binutils"
arch=('i686' 'x86_64')
url="http://www.gnu.org/software/binutils/"
license=('GPL')
depends=('glibc>=2.10.1' 'zlib')
options=('!libtool' '!distcc' '!ccache')
source=(http://ftp.gnu.org/gnu/${_pkgname}/${_pkgname}-${pkgver}.tar.bz2)
md5sums=('09a8c5821a2dfdbb20665bc0bd680791')

build() {
  cd ${_pkgname}-${pkgver}
  mkdir binutils-build && cd binutils-build

  ../configure --prefix=${_sysroot} --bindir=/usr/bin \
    --with-sysroot=${_sysroot} \
    --build=$CHOST --host=$CHOST --target=${_target} \
    --with-gcc --with-gnu-as --with-gnu-ld \
    --enable-shared --without-included-gettext \
    --disable-nls --disable-debug --disable-win32-registry
  make
  make DESTDIR=${pkgdir}/ install

  # clean-up cross compiler root
  rm -r ${pkgdir}/${_sysroot}/{info,man}
}
}}

## Hows and whys
## Why not installing into /opt
Two reasons:

# First, according to File Hierarchy Standard, these files just belong somewhere to . Period.
# Second, installing into  is a last measure when there is no other option.

## What is that "out-of-path executables" thing?
This weird thing allows easier cross-compiling. Sometimes, project Makefiles do not use  & co. variables and instead use gcc directly. If you just want to try to cross-compile such project, editing the Makefile could be a very lengthy operation. However, changing the  to use "our" executables first is a very quick solution. You would then run  instead of .

## Troubleshooting
## What to do if compilation fails without clear message?
For error, occurred during running , read . For error, occurred during compilation, scroll console log up or search for word "error".

## What does this error message means?
Most probably you made some of non-obvious errors:

* Too many or too few configuration flags. Try to use already proven set of flags.
* Dependencies are corrupted. For example misplaced or missing binutils files may result in cryptic error during gcc configuration.
* You did not add  to your  function (see bug 25672 in GCC Bugzilla).
* Some / combination may require directories to be writable (non-obvious from clfs guides).
* sysroot does nor yet has kernel/libc headers.
* If google-fu does not help, immediately abandon current configuration and try more stable/proven one.

## Why do files get installed in wrong places?
Various methods of running generic  line results in different results. For example, some make targets may not provide  support and instead require  usage. The same for ,  and other similar arguments. Sometimes providing parameters as arguments instead of environment variables, e.g

 ./configure CC=arm-elf-gcc

instead of

 CC=arm-elf-gcc ./configure

and vice versa may result in different outcomes (often caused by recursive self-invocation of configure/make).
