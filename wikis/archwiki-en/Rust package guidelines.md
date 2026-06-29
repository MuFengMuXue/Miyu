# Rust package guidelines

This document covers standards and guidelines on writing PKGBUILDs for software written in Rust.

## Package naming
When packaging Rust projects, the package name should almost always be the same as the name of the generated binary. Note that it does not make any sense to package library crates, so only crates with bins will be packaged. For ones that generate more than one binary, the upstream crate name is usually appropriate. In any event the package name should be entirely lowercase.

## Source
Most Rust projects may be built from tarballs, source archives (e.g. source links on GitHub releases), or any other published source.

When other sources are not available, most Rust projects are published on crates.io which provides a stable download URL scheme for use with cargo. The downside of this source is that it usually does not include all the test files, license files, or other assets normally in the other sources. If needed, the PKGBUILD#source can use the following template:

 source=("$pkgname-$pkgver.tar.gz::https://static.crates.io/crates/$pkgname/$pkgname-$pkgver.crate")

## Depends
While some Rust projects have external dependencies, most just use Rust ecosystem libraries that are statically embedded in the final binary. As such most projects will not need to specify many . The usual exceptions that most Rust binaries do link against glibc libraries, so  and  are typically dependencies of most Rust packages. There may be more if the build process looks for and links against any system libraries.

For , the vast majority of Rust projects are designed to be built using the cargo dependency manager, which both orchestrates the download of libraries to satisfy build time dependencies as well as makes all the necessary calls to , the actual Rust compiler. Currently both cargo and rustc are provided by the  package, but there are also alternative ways of getting both of these together or separately including the  package. As such, the tool most PKGBUILDs are going to call is cargo and you should depend directly on it.

 makedepends=(cargo)

If a project requires the use of a nightly version of the Rust tool chain, use:

 makedepends=(cargo-nightly)

## Prepare
The rust dependency manager cargo is able to download all the libraries required to build a project ahead of time. Running this fetch in the  stage  enables the later  and other stages to be run entirely offline.

 prepare() {
     export RUSTUP_TOOLCHAIN=stable
     cargo fetch --locked --target host-tuple
 }

where:

*  makes sure the default tool chain is set to stable in the event users have changed their default. Of course this should be set to nightly in the event that's what the upstream project requires. This avoids a common side effect of user preferences when not building in a chroot. Also note this is not required if the upstream project has a  file or  file in their sources that serves this purpose.
*  tells cargo to strictly adhere to the versions specified in the  file and prevent it from updating dependencies. This is important for reproducible builds.
*  tells cargo to only fetch dependencies needed for the specific target platform being built, thus reducing downloads (see Fetch options).

## Build
Building a Rust package.

 build() {
     export RUSTUP_TOOLCHAIN=stable
     export CARGO_TARGET_DIR=target
     cargo build --frozen --release --all-features
 }

where:

*  tells cargo to compile a release build (the default is a debug build)
*  tells cargo to stay offline and only use the versions specified in the  file and as cached by the fetch run in the  stage. This is functionally equivalent to , which may also be used. This is important for reproducible builds.
*  tells cargo to compile with all features of the package enabled. Alternatively, use  if you want enable only selected features.
*  tells cargo to place the output in target relative to the current directory. This avoids a common side effect of user preferences when not building in a chroot.

## Check
Most Rust projects provide a simple way to run the test suite.

 check() {
     export RUSTUP_TOOLCHAIN=stable
     cargo test --frozen --all-features
 }

You should also check if the repository is a cargo workspace. Just open up  and see if it contains a  section. If so, you should add the  flag to  to ensure that all tests of the workspace members are run too.

## Package
Rust builds binaries in  and can simply be installed to .

 package() {
     install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"
 }

If a package has more than one executable in  you can use find command:

 package() {
     find target/release \
         -maxdepth 1 \
         -executable \
         -type f \
         -exec install -Dm0755 -t "$pkgdir/usr/bin/" {} +
 }

## Notes about using cargo install
Some packages should install more files such as a man page or other assets. In the event that such a package does not have any other way to install these, one can use . In this case  is unnecessary because  forces rebuilding even if the package already has been built by using . The  stage can still be used to fetch sources ahead of time:

 package() {
     export RUSTUP_TOOLCHAIN=stable
     cargo install --no-track --frozen --all-features --root "$pkgdir/usr/" --path .
 }

The  argument should always be used, otherwise  will create unwanted files such as  or .

## Complete PKGBUILD template
{{bc|1=

# Maintainer: Firstname Lastname

pkgname=
pkgver=
pkgrel=1
pkgdesc=''
url=''
license=()
makedepends=('cargo')
depends=()
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
source=()
b2sums=()

prepare() {
    export RUSTUP_TOOLCHAIN=stable
    cargo fetch --locked --target host-tuple
}

build() {
    export RUSTUP_TOOLCHAIN=stable
    export CARGO_TARGET_DIR=target
    cargo build --frozen --release --all-features
}

check() {
    export RUSTUP_TOOLCHAIN=stable
    cargo test --frozen --all-features
}

package() {
    install -Dm0755 -t "$pkgdir/usr/bin/" "target/release/$pkgname"
    # for custom license, e.g. MIT
    # install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

}}

## Example packages
Click Package Actions > Source Files in the package page to see its example PKGBUILD.

*
*
