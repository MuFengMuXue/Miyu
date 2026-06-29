# Go package guidelines

This document covers standards and guidelines on writing PKGBUILDs for Go.

## General guidelines
## Package naming
Use  if the package provides a program that is strongly coupled to the Go ecosystem. For other applications, use only the program name.

## Building
## Dependencies
Go 1.11 introduced the initial support for go modules. This allows Go upstream code to declare dependencies and pin them to the given project version. Currently our packaging efforts utilize this to vendor dependencies.

## Upstream project without go modules
For upstream code that does not utilise Go modules, the following workaround exists. Consider filing an issue upstream.

{{hc|PKGBUILD|2=

url=https://github.com/upstream_user/upstream_project

prepare() {
  cd "$pkgname-$pkgver"
  go mod init "${url#https://}" # strip https:// from canonical URL
  go mod tidy
}

}}

## Upstream project with go modules
By default, go will use  to download and store go modules.
It will grow the user  directory.

To keep all go modules in the package build environment, you can add a prepare step to configure {{ic|1=GOPATH="${srcdir}"}}, and download the go modules in the package src directory.

{{hc|PKGBUILD|2=

prepare() {
  cd "${pkgname}-${pkgver}"
  export GOPATH="${srcdir}"
  go mod download -modcacherw
}

}}

## Flags and build options
Go does not automatically pass system build flags (, , etc.) to its C toolchain. To compile Go binaries with RELRO and other hardening flags, , , and related variables must be explicitly set in the build environment.

{{bc|1=
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

# or alternatively you can define some of these flags from the CLI options
go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-linkmode external -extldflags \"${LDFLAGS}\"" \
    .
}}

## Flag meaning
*  enables PIE compilation for binary hardening.
*   important for reproducible builds so full build paths and module paths are not embedded.
*  ensure the module files are not updated in any go actions.
*  is not important, but it ensures that go modules creates a write-able path. Default is read-only.

## Supporting debug packages
Enabling debug packages with source listing and proper symbol look ups require a few modifications to the default buildflags.

* Removal of  to ensure source paths are rewritten in the binary
* Include  in  to ensure we can parse the DWARF headers as current tooling does not support compressed headers.
* Ensure  as the internal linker go uses does not embed a build-id into the binary.
* Include {{ic|1=GOPATH="${srcdir}"}} so makepkg can include the source code for all modules.

The above options should produce a debug package with proper detached symbols and source listings which can then be picked up by the debugger.

{{bc|1=
export CGO_CPPFLAGS="${CPPFLAGS}"
export CGO_CFLAGS="${CFLAGS}"
export CGO_CXXFLAGS="${CXXFLAGS}"
export CGO_LDFLAGS="${LDFLAGS}"
export GOPATH="${srcdir}"
export GOFLAGS="-buildmode=pie -mod=readonly -modcacherw"

go build -ldflags "-compressdwarf=false -linkmode external" .
}}

## Output directory
There are currently a few ways to build all go binaries in a project.

{{bc|
build(){
    cd "$pkgname-$pkgver"
    go build -o output-binary .
}
}}

 is a shorthand for the compiler to recursively descend into the directory and find all binaries. It can be used in conjunction with a output directory to build everything.

{{bc|
prepare(){
    cd "$pkgname-$pkgver"
    mkdir -p build
}

build(){
    cd "$pkgname-$pkgver"
    go build -o build ./cmd/...
}
}}

## Sample PKGBUILD
{{bc|
pkgname=foo
pkgver=0.0.1
pkgrel=1
pkgdesc='Go PKGBUILD Example'
arch=('x86_64')
url="https://example.org/$pkgname"
license=('GPL')
makedepends=('go')
source=("$url/$pkgname-$pkgver.tar.gz")
sha256sums=('1337deadbeef')

prepare(){
  cd "$pkgname-$pkgver"
  mkdir -p build/
}

build() {
  cd "$pkgname-$pkgver"
  export GOPATH="${srcdir}"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"
  go build -o build ./cmd/...
}

check() {
  cd "$pkgname-$pkgver"
  go test ./...
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 build/$pkgname "$pkgdir"/usr/bin/$pkgname
}
}}

## Example packages
*
*
*
