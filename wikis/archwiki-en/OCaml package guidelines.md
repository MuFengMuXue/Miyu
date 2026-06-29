# OCaml package guidelines

Writing PKGBUILDs for software written in OCaml.

## Package naming
For libraries, use . For applications, use the program name. In either case, the name should be entirely lowercase.

## File placement
## Libraries
OCaml libraries should be installed under . Installation in  is deprecated.

OCaml libraries should be installed using .  includes library metadata in the package that makes it easy to manage libraries. It is a de-facto standard and a lot of OCaml software now requires it.

 extracts necessary data from a file named  that should be included in the source archive. If this file is not included, one should either be obtained from the corresponding Debian, Ubuntu, or Fedora package, or created for the package by the maintainer. A request to include the file should also be made to the upstream developers of the package.

The  variable should be used when installing packages with . See the example PKGBUILD below for details.

## OASIS
OCaml packages that install executables using OASIS ignore . This is a known limitation of OASIS (issue #493). One way to enable -like functionality is to run the  script with the  argument, like so:

{{bc|build() {
    cd "${srcname}-${pkgver}"
    ./configure --prefix /usr --destdir "$pkgdir"

    # build commands
}
}}

## OCaml bytecode and levels
OCaml can run code on multiple "levels", the top level interprets OCaml Code without compiling, the bytecode level creates machine independent bytecode and the native level creates machine code binaries (just like C/C++).

When building OCaml Packages you need to be aware if the build process is compiling native machine code, bytecode, or as in many cases both. This creates a number of situations which can cause problems with package options and the right dependencies.

If bytecode is produced at all then the PKGBUILD must contain the following to protect the bytecode:

 options=('!strip')

If the package does not contain bytecode and only distributes a binary, then  is not needed as a dependency, but it of course is required as a makedepends since the  package provides the OCaml compiler. If the package contains both native code and bytecode then  should be a dependency and a makedepends.

OCaml code is rarely (if ever) distributed as bytecode only and will almost always include native code: the only case where using any as the arch is advisable is when only un-compiled source code is distributed, usually with a library, though many libraries still distribute native code.

The moral of the story here is to be aware of what it is you are distributing, chances are your package contains both native machine code and bytecode.

## Example PKGBUILD using Dune
Dune is a new build system that is becoming more and more used by OCaml projects.

One thing to be aware is that a single project can build several "packages" in the OPAM/findlib sense, each with its own directory in . See  for an example. For release builds, all "packages" have to be explicitly listed.

{{bc|1=
# Contributor: Your Name

pkgname=ocaml-
pkgver=4.2
pkgrel=1
license=('')
arch=('x86_64')
pkgdesc="An OCaml Package"
url=""
depends=('ocaml')
makedepends=('dune')
source=()
options=('!strip')
sha256sums=()

build() {
  cd "${pkgname}-${pkgver}"
  # The "-p" flag is necessary for release builds, see the Dune manpage. Dune will complain if you forget some packages.
  dune build -p package1,package1-extension,package2
}

package() {
  cd "${pkgname}-${pkgver}"
  DESTDIR="${pkgdir}" dune install --prefix "/usr" --libdir "/usr/lib/ocaml" --docdir "/usr/share/doc"
}
}}

## Example PKGBUILD using plain findlib
{{bc|1=
# Contributor: Your Name

pkgname=ocaml-
pkgver=4.2
pkgrel=1
license=('')
arch=('x86_64')
pkgdesc="An OCaml Package"
url=""
depends=('ocaml')
makedepends=('ocaml-findlib')
source=()
options=('!strip')
md5sums=()

OCAMLFIND_DESTDIR="${pkgdir}$(ocamlfind printconf destdir)"

build() {
  cd "${pkgname}-${pkgver}"
  mkdir -p "$OCAMLFIND_DESTDIR"
  ./configure --prefix=/usr
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  env DESTDIR="${pkgdir}" \
    OCAMLFIND_DESTDIR="$OCAMLFIND_DESTDIR" \
    make install
}
}}

Keep in mind that many OCaml Packages will often need extra parameters passed to  and . Also remember to remove the  option and change the architecture if the package does not produce bytecode.
